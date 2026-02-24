phone_book = {"Amal":"0568323222","Mohammed":"0522222232","Khadijah":"0532335983",
              "Abdullah":"0545341144","Rawan":"0545534556","Faisal":"0560664566",
              "Layla":"0567917077"}

def phone_search(phone_book,user_input):
    
    if len(user_input) == 10 and user_input.isdigit():
        for name, number in phone_book.items():
            if user_input == number:
                found = True
                return name
        
        return "Sorry, the number is not found"
    else:
        return "This is invalid number"



while True:
    user_input = input("please inter a phone number:")
    print(phone_search(phone_book,user_input))