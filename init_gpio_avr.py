def configure_gpio_reg(num_of_bits):
    DDRB = 0b00000000; 
    for bit in range(0, num_of_bits):
        bit_mode = str(input(f"Enter bit {bit} mode (in/out) : "))

        if(bit_mode == "in"):
            DDRB |= (1 << bit)
        elif(bit_mode == "out"):
            DDRB &= ~(1 << bit)
        else:
            DDRB &= ~(1 << bit)
    print(f"final configuration of DDRA : {bin(DDRB)} -> {DDRB}")
    return DDRB


configure_gpio_reg(8)