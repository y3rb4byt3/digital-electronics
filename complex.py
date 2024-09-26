import matplotlib.pyplot as plt
import numpy as np

def seven_segment_decoder(bin_val):
    decoder = {
        0x0: 0b0111111,
        0x1: 0b0000110,
        0x2: 0b1011011,
        0x3: 0b1001111,
        0x4: 0b1100110,
        0x5: 0b1101101,
        0x6: 0b1111101,
        0x7: 0b0000111,
        0x8: 0b1111111,
        0x9: 0b1101111,
        0xA: 0b1110111,
        0xB: 0b1111100,
        0xC: 0b0111001,
        0xD: 0b1011110,
        0xE: 0b1111001,
        0xF: 0b1110001
    }
    return decoder.get(bin_val, 0b0000000)

def simulate_counter_and_decoder(clk_cycles, rst_active_cycles):
    counter_values = []
    seven_segment_values = []
    clk = []
    rst = []

    counter = 0
    reset = True

    for cycle in range(clk_cycles):
        clk.append(cycle % 2)

        if cycle < rst_active_cycles:
            reset = True
        else:
            reset = False
        rst.append(reset)

        if reset:
            counter = 0
        elif clk[-1] == 1:  
            counter = (counter + 1) % 16 

        counter_values.append(counter)
        seven_segment_values.append(seven_segment_decoder(counter))

    return clk, rst, counter_values, seven_segment_values

clk_cycles = 32
rst_active_cycles = 2
clk, rst, counter_values, seven_segment_values = simulate_counter_and_decoder(clk_cycles, rst_active_cycles)

time = np.arange(clk_cycles)

plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.step(time, clk, where='post')
plt.title('Clock Signal')
plt.ylabel('CLK')

plt.subplot(4, 1, 2)
plt.step(time, rst, where='post')
plt.title('Reset Signal')
plt.ylabel('RST')

plt.subplot(4, 1, 3)
plt.step(time, counter_values, where='post')
plt.title('Counter Output (bin)')
plt.ylabel('Counter')

plt.subplot(4, 1, 4)
plt.step(time, seven_segment_values, where='post')
plt.title('Seven-Segment Output')
plt.ylabel('7-Segment')
plt.xlabel('Time (cycles)')

plt.tight_layout()
plt.show()
