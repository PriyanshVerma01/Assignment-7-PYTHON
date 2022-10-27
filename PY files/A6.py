s=input("Enter A String: ")
match s.strip():
    case s if ' ' in s:
        print("Multiword String")
    case s if ' ' not in s:
        print("Singal word String")
    