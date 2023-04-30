def mask_to_bits(mask):
    octets = [int(octet) for octet in mask.split('.')]
    bits = [bin(octet).count('1') for octet in octets]
    total_bits = sum(bits)
    return total_bits


def generate_scan_ranges(range_ports):
    start_port, end_port = map(int, range_ports.split('-'))

    if (end_port - start_port) < 25:
        return [range_ports]

    num_ranges = (end_port - start_port) // 25 + 1

    scan_ranges = []
    for i in range(num_ranges):
        start = start_port + i * 25
        end = min(start + 24, end_port)
        scan_ranges.append(f'{start}-{end}')

    return scan_ranges


