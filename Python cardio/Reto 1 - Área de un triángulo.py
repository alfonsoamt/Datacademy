
def triangle_area(s):

    if len(s) == 1:

        a = s[0]
        base = a
        base2 = a / 2
        height = pitagoras(base2, c = a)
        area = base * height / 2
        print("This is an Equilateral triangle with three 'a' sides of {} units of lenght.".format(a))
        print("The triangle area is {:,.2f} units^2.".format(area))

    elif len(s) == 2:

        if (s[1] ** 2) - ((s[0] / 2) ** 2)  > 0.0:
            a = s[0]
            b = s[1]
            print("This is an Isosceles triangle with one 'a' side of {} units and two 'b' sides of {} of length.".format(a, b))
        else:
            a = s[1]
            b = s[0]
            print("This triangle does not exist. Length sides were interchanged: 'a' side is {} and 'b' sides {}.".format(a, b))

        base = a
        base2 = a / 2
        height = pitagoras(base2, c = b)
        area = base * height / 2
        print("The triangle area is {:,.2f} units^2".format(area))

    elif  len(s) == 3:

        a = s[0]
        b = s[1]
        c = s[2]

        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):

            print("This is a Scalene triangle; 'a' side is {}, 'b' side is {} and 'c' side is {} units of length.".format(a, b, c))
            S = (a + b + c) / 2
            area = pow (S * (S - a) * (S - b) * (S - c), 0.5)
            print("The triangle area is {:,.2f} units^2".format(area))

        else:
            print("This triangle does not exist.")


def pitagoras(a ,b = None, c = None):
    if isinstance(b, (int, float)) and c == None:
        c = pow(a **2 + b **2, 0.5)
        return c
    
    elif isinstance(c, (int, float)) and b == None:
        b = pow(c **2 - a ** 2, 0.5)
        return b

    else:
        print("Please introduce the length of the 'a' side and the 'b' or 'c' side")

if __name__ == "__main__":
    a = 8
    b = 5
    c = 12
    s1 = [a]
    triangle_area(s1)
    s2 = [a, b]
    triangle_area(s2)
    s3 = [a, b, c]
    triangle_area(s3)
