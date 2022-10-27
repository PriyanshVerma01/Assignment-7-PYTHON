n=int(input("Enter A Number: "))
match n:
    case n if n>0:
        print("Positive Number")
    case n if n<0:
        print("Negative Number")
    case n if n==0:
        print("Zero")
     