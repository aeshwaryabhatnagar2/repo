number =7
user_input= input("Enter y if you want to play the game: ").lower()
if user_input == 'y':
    user_number = int(input("Enter the number: "))
    if user_number == number:
        print("You guessed correctly")
    elif number - user_number in (1, -1):
        print("you were off by one")
    else:
        print("sorry, its wrong")