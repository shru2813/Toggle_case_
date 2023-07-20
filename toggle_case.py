def toggle_case(string):
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

# Test cases
input1 = "Hello"
input2 = "tHiSiSaStRiNg"

output1 = toggle_case(input1)
output2 = toggle_case(input2)

print("Output 1:", output1)
print("Output 2:", output2)
