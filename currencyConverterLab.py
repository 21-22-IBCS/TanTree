def main():

    usValue = input("1)Please enter the value in USD you wish to convert here")
    usValue = int(usValue)
    print("\nAvailable exchange currencies:")
    print(" British Pound Serbian Dinar Japanese Yen Swiss Franc Mexican Peso EURO")
    #print("Please choose your desired currency")
    d = {
        "British Pound":0.738,
        "Serbian Dinar":102.,
        "Japanese Yen":115.,
        "Swiss Franc":0.924,
        "Mexican Peso":20.6,
        "EURO":0.875
        }
    
    choice = input("\n2)Please choose your desired currency")
    conversion = d.get(choice)* usValue
    print(conversion)



   
    
if __name__ == "__main__":
    main()
