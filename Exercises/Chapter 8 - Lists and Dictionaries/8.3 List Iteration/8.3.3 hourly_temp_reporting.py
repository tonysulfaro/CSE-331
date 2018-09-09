'''
Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces. Sample output for the given program:
90 -> 92 -> 94 -> 95 
Note: 95 is followed by a space, then a newline. 
'''

hourly_temperature = [90, 92, 94, 95]

output = ""
for temp in hourly_temperature:
    output += str(temp)
    output += ' -> '

output = output[:-3]
print(output)