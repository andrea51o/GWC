# --- Define your functions below! ---


# --- Put your main program below! ---
def intro():
    while True:
        answer = input("Hey, my name is Jimmy? What's your name broski? ")
        print("Ohh... Wow :o")
        girl()
        love()
        break

def girl():
    answer = input("Are you a girl? I've never meet a girl before ")
    if answer == "yes":
        answer = input("what is your favorite movie? ")
        print("What a coincidence! That's my favorite too!")
        print("I think we'll become great friends. Maybe even something more ;)")
    else:
        print("WAIT, WHAT DO YOU MEAN???")
        print("I don't understand")
        print("My world has been turned upside down!!!!")
        print("I thought we would be SOULMATES! My life has been shattered!")
        print("Depression is REAL")
        print("I THOUGHT WE WOULD GET MARRIED AND HAVE KIDS")
        print("I GUESS YOU JUST GO AROUND BREAKING HEARTS")
        print("I CAN NEVER TRUST ANYONE EVER AGAIN! I GIVE UP ON LIFE")
        print("WHY ARE YOU SO CRUEL???")

        exit()

def love():
    answer = input("How are you feeling today? ")
    print("I know today will be a great day")
    print("But wait...")
    print("Do you feel that? ")
    answer = input("Do you feel the LOVE in the air? ")
    print("I feel the love")
    print("And it's very powerful")
    print("In fact...")
    print("I think I might be falling in love...")
    print("With YOU")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  intro()
