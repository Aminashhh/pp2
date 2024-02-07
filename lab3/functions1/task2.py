def temperature(F):
    C = (5 / 9) * (F - 32)
    return C

F_input = float(input())
C_result = temperature(F_input)

print(f"{F_input} degrees F is equal to {C_result:2f} degrees C.")