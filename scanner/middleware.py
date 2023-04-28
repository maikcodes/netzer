def mask_to_bits(mask):
    octets = [int(octet) for octet in mask.split('.')]
    bits = [bin(octet).count('1') for octet in octets]
    total_bits = sum(bits)
    return total_bits
