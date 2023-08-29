import re 

regex = [] 
strs = {} 

for i in range(int(input("Please tell how many expressions will be there: "))): 
    regex.append(input("Please write an expression: ")) 
for i in range(int(input("Please tell how many strings will be there: "))): 
    strs[input("Please write a string: ")] = "0" 

for i in range(len(regex)): 
    for j in strs: 
        if re.match(regex[i], j): 
            strs[j] = (i+1)       #regex loc
        else:
            if int(strs[j]) < 1:
                strs[j] = "0" 

for i in strs: 
    if int(strs[i]) > 0:
        print("Yes,",strs[i])
    else:
        print("No,",strs[i])


    


