s1=input("Enter First String: ")
s2=input("Enter Second String: ")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical String")
    case (s1,s2) if s1>s2:
        print("{} Comes After {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} Comes After {}").formate(s2,s1)