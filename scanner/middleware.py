
# funcion para calcular la mascara de bits
def mask_to_bits(mask):
    # separa la mascara de red en octetos y
    # crea ua lista de octetos a partir de ello
    octets = [int(octet) for octet in mask.split('.')]

    # convierte cada octeto a bits y cuenta la cantidad de 1s y
    # crea una lista con cada elemento igual a la cantidad de bits
    # de cada octeto
    bits = [bin(octet).count('1') for octet in octets]

    # suma cada elemento de la lista de bits para obtener la mascara de bits
    total_bits = sum(bits)
    return total_bits


# generar rangos de escaneo, de 25 en 25
def generate_scan_ranges(range_ports):

    # separa el valor del puerto inicial y final, y los convierte a enteros
    start_port, end_port = map(int, range_ports.split('-'))

    # si el rango de puertos es menor a 25, devuelve el mismo rango
    if (end_port - start_port) < 25:
        return [range_ports]

    # si el rango de puertos es mayor a 25
    # calcula la cantidad de rangos, usan la división entera '//' (no redondeo) y
    # suma 1 para obtener la cantidad de rangos
    num_ranges = (end_port - start_port) // 25 + 1

    # crea una lista vacia para los rangos de escaneo
    scan_ranges = []

    # calcula los valores de los rangos pora la cantidad de rangos calculados
    for i in range(num_ranges):

        # calcula el valor inicial del rango
        start = start_port + (i * 25)

        # calcula el valor final del rango, obtiene el minimo entre
        # el valor final del rango actual y el valor del ultimo puerto
        end = min(start + 24, end_port)

        # agrega a la lista de rangos el rango actual
        scan_ranges.append(f'{start}-{end}')

    return scan_ranges


