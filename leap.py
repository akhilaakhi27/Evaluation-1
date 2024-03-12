n=int(input("enter a year"))
def year():
    if n % 4==0:
        if n% 100==0:
            if n% 400==0:
                print("the given year is a leap year")
            else:
                print("the given year is a not leap year")
        else:
            print("the given year is a leap year")
    else:
        print("the given year is not a leap year")
year()


                