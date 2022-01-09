import easyMode
import extremeMode

# Game Introduction
user = input("Welcome to the world of Pokémon! First, please tell me your name: ")
streaks = 0


def StatusCheck(state):
    if state:
        global streaks
        streaks += 1
        print(f"Good Work! Your streak has went up by 1. (Current Streak: {streaks})")
    if not state:
        streaks = 0
        print("Good try! Aww. Your streak got reset back to 0.")


print(f"\nHello {user}! Thank you for playing PikaGuess.")

# Game-mode Selection
while True:
    levelChoice = input("""
[1] Easy Mode
[2] Extreme Mode
[3] Rules
[4] Exit

Please select which difficulty (listed above) you'd like to play: """)

    levelOptions = ["1", "2", "3", "4"]
    regionOptions = ["1", "2", "3", "4"]

    if levelChoice not in levelOptions:
        print("Wrong number selected! Please enter a number between 1 to 4.")

    if levelChoice == "1":
        regionChoice = input("""Easy Mode selected. 
[1] Kanto
[2] Johto 
[3] Hoenn
[4] Sinnoh
\nSelect a region: """)

        if regionChoice not in regionOptions:
            print("Wrong number selected! Please enter a number between 1 to 3.")

        if regionChoice == "1":
            print(f"\nKanto Region selected! The game will now begin. Good luck {user}!")
            status = easyMode.PokeHangman('assets/kanto.txt')
            StatusCheck(status)

        elif regionChoice == "2":
            print(f"\nJohto Region selected! The game will now begin. Good luck {user}!")
            status = easyMode.PokeHangman('assets/johto.txt')
            StatusCheck(status)

        elif regionChoice == "3":
            print(f"\nHoenn Region selected! The game will now begin. Good luck {user}!")
            status = easyMode.PokeHangman('assets/hoenn.txt')
            StatusCheck(status)

        elif regionChoice == "4":
            print(f"\nSinnoh Region selected! The game will now begin. Good luck {user}!")
            status = easyMode.PokeHangman('assets/sinnoh.txt')
            StatusCheck(status)

    elif levelChoice == "2":
        print(f"\nExtreme Mode selected! The game will now begin. Good luck {user}!")
        status = extremeMode.PokeHangman('assets/combined.txt')
        StatusCheck(status)

    elif levelChoice == "3":
        print("""\n========= RULES =========
1. Depending on the difficulty you've selected, I will select a random Pokémon.
2. You will have to guess the name of that Pokémon under a certain number of attempts.
3. I will draw a number of dashes equal to the number of letters in that Pokémon's name.
4. Once you have a certain number of turns left, I will give you some hints (Not in Champion Mode tho)
5. Guess the name before you run out of attempts!""")

    elif levelChoice == "4":
        if streaks == 0:
            print(f"Exiting game with a streak of {streaks}. Better luck next time, {user}!")
        if 1 <= streaks <= 10:
            print(f"Exiting game with a streak of {streaks}. You're quite the expert, {user}!")
        if streaks > 10:
            print(f"Exiting game with a streak of {streaks}. You're quite the champion, {user}!")
        exit()
