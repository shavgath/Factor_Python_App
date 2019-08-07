# Simple factor program
class Factors():
    # assigning input to n, whilst stripping any spaces entered by user
    n = int(input("Please enter a number: ").strip())

    # Check if number is factor of 3 then go inside nested if statement
    if (n % 3 == 0):
        # Check if number is factor of 3 and 5 then go inside nested if statement
        if (n % 3 == 0) & (n % 5 == 0):
            # Check if number is factor of 3, 5 and 7 then print statement
            if (n % 3 == 0) & (n % 5 == 0) & (n % 7 == 0):
                print("PlingPlangPlong")
            else:
            # If not and number is factor of 3 and 5 then print statement
                print("PlingPlang")
        else:
            # If not and number is factor of 3 then print statement
            print("Pling")

    # Check if number is factor of 5 then go inside nested if statement
    elif (n % 5 == 0):
        # Check if number is factor of 5 and 7 then print statement
        if (n % 5 == 0) & (n % 7 == 0):
            print("PlangPlong")
        else:
            # If not and number is factor of 5 then print statement
            print("Plang")
    # Check if number is factor of 7 then print statement
    elif (n % 7 == 0):
        print("Plong")

    # If number has no factor 3, 5 or 7
    else:
        print(n)


