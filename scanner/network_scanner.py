import nmap
from .middleware import mask_to_bits
from .messages import print_process, print_end_process

# fincion para escaneo de redes
def network_scanner(network, subnet_mask):
    # estructura los parametros	de escaneo
    hosts = f'{network}/{subnet_mask}'

    scanner = nmap.PortScanner()

    # argumentos para escanear sistema operativo y puertos abiertos
    arguments = '-O -sS'
    # escanea la red
    scanner.scan(hosts=hosts, arguments=arguments)

    # obtiene una lista con estructura (host, resultados)
    # por cada host detectado
    host_list = [(x, scanner[x]) for x in scanner.all_hosts()]

    return host_list


# funcion para convertir los resultados en una lista para 
# presentarlos en la ui
def convert_to_array(scan_result):

    # crea una lista vacia para todos los resultados
    hosts_data = []

    # recorre cada resultado de la lista de resultados
    for host in scan_result:
        
        # crea una lista vacia para los resultados de cada host
        host_data = []
        operative_system_match = host[1]['osmatch']

        # is no se detecta el sistema operativo del host
        if len(operative_system_match) < 1:
            host_data.append(host[0])
            host_data.append(host[1]['status']['state'])
            host_data.append('')
            host_data.append('')
            hosts_data.append(host_data)
            continue # saltar a la iteracion, no continua con el siguiente codigo 

        # si se detecta el sistema operativo del host
        host_data.append(host[0])
        host_data.append(host[1]['status']['state'])
        host_data.append(operative_system_match[0]['name'])
        host_data.append(operative_system_match[0]['osclass'][0]['osgen'])
        hosts_data.append(host_data)
    return hosts_data


# funcion para ecanear la red
def scan(network, subnet_mask):
    # convertir la mascara de red a mascara de bits
    subnet_mask_bits = mask_to_bits(subnet_mask)
    print_process(f'Scanning NETWORK: {network}/{subnet_mask_bits}')
    # scanear la red
    scan_result = network_scanner(network, subnet_mask_bits)
    scan_result_array = convert_to_array(scan_result)
    print_end_process()
    return scan_result_array
