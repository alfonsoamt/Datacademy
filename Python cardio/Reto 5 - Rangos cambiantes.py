def numbers():
    print("Introduce three numbers.")
    L = int(input("Lower limit: "))
    U = int(input("Upper limit: "))
    C = int(input("Comparation number: "))
    while not ((C <= U)  and (C >= L)):
        print("The comparation number {} is out of the limits. Intrroduce a new one.".format(C))
        C = int(input("Comparation number: "))
    print("The comparation number {} is in the limits.".format(C))

if __name__ == "__main__":
    numbers()