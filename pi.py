import time

def pi_spigot():
    # Generator to calculate pi digits using spigot algorithm
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q + r - t < n*t:
            yield n
            q, r, t, k, n, l = (10*q, 10*(r - n*t), t, k, (10*(3*q + r)) // t - 10*n, l)
        else:
            q, r, t, k, n, l = (q*k, (2*q + r)*l, t*l, k + 1, (q*(7*k + 2) + r*l) // (t*l), l + 2)

# Initialize generator
pi_gen = pi_spigot()

# Open or create a text file for writing the digits of pi
with open("pi_digits.txt", "a") as file:
    # Print the integer part of π and the decimal point, and write to the file
    first_digit = next(pi_gen)
    print(first_digit, end='.', flush=True)
    file.write(f"{first_digit}.")
    
    # Continuously print digits of π and write to the file with a very small delay
    try:
        while True:
            digit = next(pi_gen)
            print(digit, end='', flush=True)
            file.write(f"{digit}")
    except KeyboardInterrupt:
        print("\nStopped generating π digits.")
