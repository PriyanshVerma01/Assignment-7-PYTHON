year=int(input("Enter Year Number:- "))
match year:
    case year if year%100!=0 and year%4==0:
        print("Non century leap year")
    case year if year%4==0 :
        print("Century leap year")
    case year if year%400!=0 and year%4!=0:
        print("Non century non leap year")
    case year if year%400==0 and year%4!=0:
        print("Century non leap year")