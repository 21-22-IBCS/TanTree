def main():

    usValue = input("Please enter the value in USD you wish to convert here")
    usValue = int(usValue)
    print(" British Pound\n Serbian Dinar\n Japanese Yen\n Swiss Franc\n Mexican Peso\n EURO")
    #print("Please choose your desired currency")
    dictionary = {
        "British Pound":.738,
        "Serbian Dinar":102.,
        "Japanese Yen":115.,
        "Swiss Franc":.924,
        "Mexican Peso":20.6,
        "EURO":.875
        }
    choice = input("Please choose your desired currency")
    conversion = dictionary.get(choice)* usValue
    print(conversion)



   
    
if __name__ == "__main__":
    main()
