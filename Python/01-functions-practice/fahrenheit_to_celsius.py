def far_to_cel(far):
    cel = (far - 32) / (9 / 5)
    return cel


far = int(input("fahrenheit: "))

print(far_to_cel(far))