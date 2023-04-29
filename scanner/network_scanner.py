import nmap
from .middleware import mask_to_bits


def network_scanner(network, subnet_mask):
    hosts = f'{network}/{subnet_mask}'
    nm = nmap.PortScanner()
    arguments = '-O -sV -sS'
    nm.scan(hosts=hosts, arguments=arguments)
    host_list = [(x, nm[x]) for x in nm.all_hosts()]

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
        print(operative_system_match)
        host_data.append(operative_system_match[0]['name'])
        host_data.append(operative_system_match[0]['osclass'][0]['osgen'])
        hosts_data.append(host_data)
        print(f'\n\n{host_data}\n{hosts_data}')
    return hosts_data


def scan(network, subnet_mask):
    subnet_mask_bits = mask_to_bits(subnet_mask)
    scan_result = network_scanner(network, subnet_mask_bits)
    scan_result_array = convert_to_array(scan_result)
    return scan_result_array
