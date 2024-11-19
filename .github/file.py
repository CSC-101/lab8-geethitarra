total = 0.0
fileinput = input("Enter the name of the file to open: ")

try:
    with open(fileinput, 'r') as file:
        linecounter = 1
        for line in file:
            try:
                values = line.strip().split()
                if len(values) != 2:
                    raise ValueError("Line doesn't have two float values")
                num1 = float(values[0])
                num2 = float(values[1])
                linesum = num1 + num2
                print("Line " + str(linecounter) + ": Sum = " + str(linesum))
                total += linesum
            except ValueError:
                print("Error on line " + str(linecounter))
            linecounter += 1

except FileNotFoundError:
    print("Error: The file couldn't be opened")
    exit(1)

print("Sum: " + str(total))