# for loops challenge: binary hexadecimal converter app
print("Welcome to the Binary/Hexadecimal Converter App")

# get user input and generate list:
max_value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value+1)) # plus one because range function includes one till max value but not max value
binary = []
hexadecimal = []
#the bin function returns the binary version of an integer
#the hex function converts an integer to a lowercase hexadecimal string
for num in decimal:
    binary.append(bin(num)) # this takes the num in decimal, converts it into a bin, then appends to binary list
    hexadecimal.append(hex(num))
print("Generating lists... Complete!")

# get slicing index from user
print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("What decimal number would you like to start at: "))
upper_range = int(input("What decimal number would you like to stop at: "))

# slice through each list individually, You can return a range of characters by using the slice syntax.
print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in decimal[lower_range-1:upper_range]: # -1 because the index is starting one above of what we want
    print(num)

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in binary[lower_range-1:upper_range]: # -1 because the index is starting one above of what we want
    print(num)

print("\nHexadecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")
for num in hexadecimal[lower_range-1:upper_range]: # -1 because the index is starting one above of what we want
    print(num)

# output the whole list to the screen
input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----Binary----Hexadecimal")
print("-----------------------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal): # zip allows for tuples to be assigned to letters?
    print(str(d) + "------" + str(b) + "------" + str(h))