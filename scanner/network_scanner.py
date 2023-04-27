from colorama import init, Fore, Back, Style
from .midlewawre import mask_to_bits
import nmap

init(autoreset=True)


def gateway_scanner(network, subnet_mask):
    default_gateway = f'{network}/{subnet_mask}'

    nm = nmap.PortScanner()
    arguments = '-n -sP -PE -PA21,23,80,3389'
    print(
        f'\n{Style.BRIGHT}{Back.LIGHTYELLOW_EX}{Fore.BLACK} scanning {default_gateway} 🔃...')

    nm.scan(hosts=default_gateway, arguments=arguments)
    host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    return host_list


def scan(network, subnet_mask):

    # host_to_scan = {
    #     'network': '192.168.1.0',
    #     'subnet_mask': '24'
    # }
    
    host_to_scan = {
        'network': network,
        'subnet_mask': mask_to_bits(subnet_mask)
    }

    host_list = gateway_scanner(
        network=host_to_scan['network'],
        subnet_mask=host_to_scan['subnet_mask']
    )

    nm = nmap.PortScanner()

    csv_keys = ['host', 'hostname', 'hostname_type', 'protocol', 'port', 'name',
                'state', 'product', 'extrainfo', 'reason', 'version', 'conf', 'cpe']

    xxx = []

    for host, state in host_list:
        nm.scan(hosts=host, ports='80')
        print(
            f'\n{Style.BRIGHT}{Fore.CYAN}host: {host} ({state})\ncsv:\n{nm.csv()}')
        csv_data = nm.csv().split('\r\n')
        csv_data = list(filter(('').__ne__, csv_data))

        if len(csv_data) == 1:  # only one row (if not only header)
            continue

        current_split = csv_data.remove(
            'host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe')

        final_csv_data = []
        for line in csv_data:
            final_csv_data.append(line.split(';'))

        xxx.append(final_csv_data)
        print(final_csv_data)

    print('xxx', xxx)
    return (xxx)
