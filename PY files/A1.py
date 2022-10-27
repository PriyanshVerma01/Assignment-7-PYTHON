month=int(input("Enter Month Number: "))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 DAYS")
    case month if month in (4,6,9,11):
        print("30 DAYS")
    case 2:
        print("28 OR 29 DAYS")
    case _:
        print("Invalid Month Number")
print()