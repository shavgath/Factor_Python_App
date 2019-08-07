class Factors():
    # assigning input to n, whilst stripping any spaces entered by user
    n = int(input("Please enter a number: ").strip())

    if (n % 3 == 0):
        print("Pling")

    elif (n % 5 == 0):
        print("Plang")

    elif (n % 7 == 0):
        print("Plong")

    else:
        print(n)