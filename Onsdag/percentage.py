input = input("Type a percentage: ")

result = f'{float(input) / 100:.0%}'

print(result)

def percentage(a, b):
    return abs(a / b) * 100

print(percentage(25, 50))