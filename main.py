while True:
    try:
        num = int(input("please enter a number: "))
    except:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("Developed by Raphael")
