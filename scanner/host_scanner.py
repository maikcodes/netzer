import nmap
from .messages import print_process, print_result, print_array_result

DEFAULT_HOSTS = '127.0.0.1'
DEFAULT_PORTS = '80'


def host_scanner(hosts=DEFAULT_HOSTS, ports=DEFAULT_PORTS):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=hosts, ports=ports)
    return scanner


def split_elements(ports_list):
    result = []

    for port in ports_list:
        result.append(port.split(';'))

    return result


def convert_to_array(scan_result):
    try:
        ports_csv = scan_result.csv()
        print_result(f'{ports_csv}')
        ports_list = ports_csv.split('\r\n')
        ports_list_cleaned = list(filter(('').__ne__, ports_list))
        ports_list_cleaned.pop(0)
        ports_array = split_elements(ports_list_cleaned)
        return ports_array
    except:
        return []


def scan(hosts, ports):
    print_process(f'Scanning HOST:{hosts}, PORTS: [{ports}]')
    scan_result = host_scanner(hosts, ports)
    scan_result_array = convert_to_array(scan_result)
    print_array_result(scan_result_array)
    return scan_result_array
