
def Converter(n, unit):
    if unit == "km":
        mi = n / 1.609344
        print("{} kilometers to miles are: {:.2f} miles.".format(n, mi))
    elif unit == "mi":
        km = n * 1.609344
        print("{} miles to kilometers are: {:.2f} kilimeters.".format(n, km))
    else:
        print("Introduce 'km' (kilometers) or 'mi' (miles) as the second argument.")
    
if __name__ == "__main__":
    Converter(1000, "km")
    Converter(1000, "mi")
    Converter(75, "km")
    Converter(48, "mi")