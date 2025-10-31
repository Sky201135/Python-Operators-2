word = input("Enter something: ")

if len(word) == 1:
    if word.isalpha():
        if word.lower() == 'a':
            print("It's the alphabet 'a'.")
        else:
            print("It's an alphabet but not 'a'.")
    else:
        print("It's not an alphabet.")
else:
    print("Please enter exactly one character.")
