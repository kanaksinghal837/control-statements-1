day = int(input("Enter a num (1-7): "))
match day:
    case 1 :
        print("Sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wedneseday")
    case 5:
        print("thrusday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("INVALID")
