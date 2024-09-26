def update(R1, R2):
    # Case when both devices request access to the resource at the same time
    if R1 == '1' and R2 == '1':
        # Priority for device 1
        G1 = 1
        G2 = 0
    elif R1 == '1':
        G1 = 1
        G2 = 0
    elif R2 == '1':
        G1 = 0
        G2 = 1
    else:
        G1 = 0
        G2 = 0
    return G1, G2

# Example usage with user inputs
while True:
    user_input = input("Enter values for R1 and R2 (e.g., 10 for R1=1 and R2=0, or 'q' to quit): ")
    if user_input.lower() == 'q':
        break

    if len(user_input) == 2 and user_input[0] in '01' and user_input[1] in '01':
        R1, R2 = user_input[0], user_input[1]
        G1, G2 = update(R1, R2)
        print(f"Inputs: R1={R1}, R2={R2} => Outputs: G1={G1}, G2={G2}")
    else:
        print("Invalid input. Try again.")
