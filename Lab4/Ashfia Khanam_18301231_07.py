import re
s = int("abc")
file1 = open("input.txt","r")
data = file1.read().split("\n")
expression = "(public|(public static)) (int|void)+ ([a-z]+[(])"

for i in data:
    if re.match(expression, i) and "main" not in i:
        line = i.split() #space
        if "static" in i:
            print(" ".join(line[3:]),"return type:",line[2]) # list to string #int or void
        elif "void" in i:
            print(" ".join(line[2:]),"return type: void")
        else:
            print(" ".join(line[2:]),"return type:",line[1])
