def new(str):
    if len(str) >=2 and str[:2]=="Is":
        return str
    return "Is" +str
print(new("memory"))
print(new("IsEmpty"))
