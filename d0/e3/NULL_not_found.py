def NULL_not_found(object: any) -> int :
    if object is None :
        print("Nothing: None", type(object))
    elif object != object:
        print("Cheese: nan", type(object))
    elif object == False and type(object) == bool:
        print("Fake: False", type(object))
    elif object is Empty :
        print ("Empty:", type(object))
    elif object == 0 :
        print("Zero, 0", type(object))
    else :
        print("Type not Found")
    return 1