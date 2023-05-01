import nmap
from .middleware import mask_to_bits
from .messages import print_process, print_end_process


def network_scanner(network, subnet_mask):
    hosts = f'{network}/{subnet_mask}'
    scanner = nmap.PortScanner()
    arguments = '-O -sS'
    scanner.scan(hosts=hosts, arguments=arguments)
    host_list = [(x, scanner[x]) for x in scanner.all_hosts()]

    return host_list


def convert_to_array(scan_result):
    hosts_data = []
    for host in scan_result:
        host_data = []
        operative_system_match = host[1]['osmatch']

        if len(operative_system_match) < 1:
            host_data.append(host[0])
            host_data.append(host[1]['status']['state'])
            host_data.append('')
            host_data.append('')
            hosts_data.append(host_data)
            continue

        host_data.append(host[0])
        host_data.append(host[1]['status']['state'])
        host_data.append(operative_system_match[0]['name'])
        host_data.append(operative_system_match[0]['osclass'][0]['osgen'])
        hosts_data.append(host_data)
    return hosts_data


def scan(network, subnet_mask):
    subnet_mask_bits = mask_to_bits(subnet_mask)
    print_process(f'Scanning NETWORK: {network}/{subnet_mask_bits}')
    scan_result = network_scanner(network, subnet_mask_bits)
    scan_result_array = convert_to_array(scan_result)
    print_end_process()
    return scan_result_array
