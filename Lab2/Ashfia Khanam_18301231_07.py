def EmailORWeb(lim):
    addr = []
    for i in range(lim):
        case = input("Enter a string: ")
        if "." in case:
            if not ".." in case:
                spcase = case.split(".")
                if "@" in case and case.count("@") == 1:
                    if not ".@" in case:
                        if not "@." in case:
                            if not case[0].isnumeric():
                                if not spcase[-1].isnumeric():
                                    addr.append("Email")
                                else:
                                    addr.append("Unknown")
                            else:
                                addr.append("Unknown")
                        else:
                            addr.append("Unknown")
                    else:
                        addr.append("Unknown")
                elif len(spcase)> 2:
                    if not (case[0].isnumeric() or spcase[-1].isnumeric()):
                        addr.append("Web")
                    else:
                        addr.append("Unknown")
                else:
                    addr.append("Web")
            else:
                addr.append("Unknown")
        else:
            addr.append("Unknown")
    return addr
                


limit = int(input("Enter the limit: "))
res = EmailORWeb(limit)
for i in range(len(res)):
    print(res[i],end = ", ")
    print(i+1)