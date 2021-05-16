from math import pi

def menu():
    print("This program calculates the volume of a figure.")
    print("[1] Cube")
    print("[2] Parallelepiped")
    print("[3] Cylinder")
    print("[4] Cone")
    print("[5] Sphere")
    figure = input("Choose one: ")
    return int(figure)

def volume(figure):
    if figure == 1:

        print("You choose a cube.")
        a = int(input("Introduce de size of the 'a' side: "))
        v = a ** 3

    elif  figure == 2:

        print("You choose a Parallelepiped.")
        a = int(input("Introduce de size of the 'a' side: "))
        b = int(input("Introduce de size of the 'b' side: "))
        c = int(input("Introduce de size of the 'c' side: "))
        v = a * b * c

    elif  figure == 3:

        print("You choose a Cylinder.")
        r = int(input("Introduce the radius: "))
        h = int(input("Introduce the height: "))
        v = pi * r * r * h

    elif figure == 4:

        print("You choose a Cone.")
        r = int(input("Introduce the radius: "))
        h = int(input("Introduce the height: "))
        v = pi * r * r * h / 3

    elif figure == 5:

        print("You choose a Sphere.")
        r = int(input("Introduce the radius: "))
        v = 4 * pi * r * r * r / 3

    else:
        print("The input is not a valid option.")
        return

    print("The volume of the figure is {:.2f} units^3".format(v))
    return v

if __name__ == "__main__":
    f = menu()
    volume(f)

