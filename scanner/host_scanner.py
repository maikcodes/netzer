import nmap
from .messages import *
from .middleware import generate_scan_ranges

INDEX_HEADER = 0


def host_scanner(hosts, ports):
    scanner = nmap.PortScanner()

    if (ports.count('-') == 0):
        scanner.scan(hosts=hosts, ports=ports)
        scan_result = convert_to_array(scanner)
        return scan_result

    scan_range_list = generate_scan_ranges(ports)

    scan_results = []
    for current_range in scan_range_list:
        print_processing(f'Current scanning range: {current_range}')
        scanner.scan(hosts=hosts, arguments=f'-p {current_range}')
        scan_result = convert_to_array(scanner)
        for scan_port_result in scan_result:
            scan_results.append(scan_port_result)

    return scan_results


def split_elements(ports_list):
    result = []

    for port in ports_list:
        result.append(port.split(';'))

    return result


def convert_to_array(scan_result):
    try:
        global INDEX_HEADER
        port_csv_data = scan_result.csv()
        print_blue_result('Scan result (csv)', port_csv_data)
        ports_list = port_csv_data.split('\r\n')
        ports_list_cleaned = list(filter(('').__ne__, ports_list))
        ports_list_cleaned.pop(INDEX_HEADER)
        ports_array = split_elements(ports_list_cleaned)
        return ports_array
    except:
        return []


def scan(hosts, ports):
    print_process(f'Scanning HOST: {hosts}, PORTS: [{ports}]')
    scan_result = host_scanner(hosts, ports)
    print_green_result('Scan result (array)', scan_result)
    print_end_process()
    return scan_result
