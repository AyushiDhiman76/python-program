#WAP to determine the type of input using match statement
match data:
    case int():
        print("int")
    case float():
        print ("float")
    case str():
        print("str")
    case list():
        print("list")
    case tuple():
        print("tuple")
    case dict():
        print("dict")
    case set():
        print("set")    
