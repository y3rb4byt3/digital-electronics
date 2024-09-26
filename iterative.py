def negation_between_zeros(binary_sequence):
    
    reversed_sequence = list(binary_sequence)
    reversed_sequence.reverse()
    result = ''
    left_zero = -1
    right_zero = -1
    
    # left-most zero
    for i, bit in enumerate(binary_sequence):
        if bit == "0":
            left_zero = i
            result += "0"
            break
        else:
            result += bit
    
    # right-most zero
    for i, bit in enumerate(reversed_sequence):
        if bit == "0":
            right_zero = len(binary_sequence) - i - 1
            break
    # condition checking if there's only one zero in the sequence
    if left_zero == -1 or right_zero == -1:
        return binary_sequence

    # numbers between the zeros
    for i in range(left_zero + 1, right_zero):
        if binary_sequence[i] == "0":
            result += "1"
        else:
            result += "0"
    
    # zero after negated numbers
    result += "0"
    
    # numbers to the right
    for i in range(right_zero + 1, len(binary_sequence)):
        result += binary_sequence[i]

    return result

binary_sequence = input("Enter your binary sequence:\n")
print(negation_between_zeros(binary_sequence))
