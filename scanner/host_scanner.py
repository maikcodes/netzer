import nmap
from .messages import *
from .middleware import generate_scan_ranges

INDEX_HEADER = 0

# funcion de escaneo de host
def host_scanner(hosts, ports):
    scanner = nmap.PortScanner()

    # si no se especifica puerto, escanear los activos
    if (ports == ''):
        # ecanear todos los puertos activos
        scanner.scan(hosts=hosts, arguments='-p-')
        scan_result = convert_to_array(scanner)
        return scan_result
    
    # si no se especifica rango, escanear los puertos especificos
    if (ports.count('-') == 0):
        # escanear los puertos especificos
        scanner.scan(hosts=hosts, ports=ports)
        scan_result = convert_to_array(scanner)
        return scan_result

    # si los puertos estan en rango, divide en rangos de 25 el escaneo
    # y crea una lista de rangos
    scan_range_list = generate_scan_ranges(ports)

    # crear lista vacía de los resultados del escaneo
    scan_results = []

    # recorre cada rango de la lista de rangos
    for current_range in scan_range_list:
        print_processing(f'Current scanning range: {current_range}')

        # escanea el rango actual de la lista
        scanner.scan(hosts=hosts, arguments=f'-p {current_range}')
        scan_result = convert_to_array(scanner)

        # agregar el resultado del escaneo de cada rango
        # a la lista de de resultados de escaneo
        for scan_port_result in scan_result:
            scan_results.append(scan_port_result)

    return scan_results


# funcion para separar los elementos del 
# resultado del escaneo de cada puerto
def split_elements(ports_list):
    result = []

    for port in ports_list:
        result.append(port.split(';'))

    return result


# funcion para convertir los resultados en una lista para 
# presentarlos en la ui
def convert_to_array(scan_result):
    try:
        # accede a la variable gloabl INDEX_HEADER
        global INDEX_HEADER

        # convierte los resultados del escaneo en formato csv
        port_csv_data = scan_result.csv()
        print_blue_result('Scan result (csv)', port_csv_data)

        # separa en filas los resultados del escaneo (separar cada puerto)
        ports_list = port_csv_data.split('\r\n')
        
        # crear una nueva lista de resultados que no contienen filas vacias
        ports_list_cleaned = list(filter(('').__ne__, ports_list))

        # elimina la cabecera de cada lista
        ports_list_cleaned.pop(INDEX_HEADER)

        # separa los los elementos de cada puerto, que estan en formato csv
        ports_array = split_elements(ports_list_cleaned)
        return ports_array
    except:
        return []


# funcion para escanar un host
def scan(hosts, ports):
    print_process(f'Scanning HOST: {hosts}, PORTS: [{ports}]')
    # escanea el host
    scan_result = host_scanner(hosts, ports)
    print_green_result('Scan result (array)', scan_result)
    print_end_process()
    return scan_result
