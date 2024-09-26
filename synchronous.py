def process_bits(bits):
    ones_count = 0
    zeros_count = 0
    output = []

    for bit in bits:
        if bit == '1':
            ones_count += 1
        elif bit == '0':
            zeros_count += 1
        
        if ones_count % 3 == 0 and zeros_count > 0 and zeros_count % 2 == 0:
            output.append('1')
        else:
            output.append('0')
    
    return ''.join(output)

# Testing the function with a sample bit sequence
input_bits = "1100100110001"
output_signals = process_bits(input_bits)
print(f"Input:  {input_bits}")
print(f"Output:  {output_signals}")
