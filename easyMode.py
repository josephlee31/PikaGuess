""" Description: An interactive Hangman game based on the popular video-game franchise "Pokémon"."""

# Importing libraries
import pypokedex
import random


def checkCorrect(query):         # Function checks if player has guessed all letters of the name correctly
    state = True
    for i in range(len(query)):
        if query[i] == "_":
            state = False
    return state


def pokeHint(num, pokemon_name):
    if num == 3:
        print(f"HINT #1: The typing of the Pokémon is {pokemon_name.types}.")


# Guessing Pokemon Game Function
def PokeHangman(regionLink):
    with open(regionLink) as list_file:
        pokemon_names = list_file.read()

    # Create list object that contains all Kanto Pokemon
    ListOfPokemon = pokemon_names.split(", ")

    tries = 0
    maxTries = 8
    pokemon = random.choice(ListOfPokemon)
    pokemonQuery = pypokedex.get(name=pokemon)
    blank = "_" * len(pokemon)

    lettersGuessed = []  # Contains all letters the player has guessed

    # While loop to iterate through player's turns
    while tries < maxTries:
        print(blank)
        guess = input("Enter a letter: ")
        capitalGuess = guess.upper()

        # If the player correctly guesses a letter:
        if capitalGuess not in lettersGuessed:
            lettersGuessed.append(capitalGuess)

            if capitalGuess in pokemon.upper():
                # Replace _(s) with correctly guessed letter
                for i in range(len(pokemon)):
                    if capitalGuess == pokemon.upper()[i]:
                        string_list = list(blank)
                        string_list[i] = capitalGuess
                        blank = "".join(string_list)
                print(f"Correct! There is one or more '{guess}' in the Pokémon name. (Remaining Turns: {maxTries - tries})\n")

                # Check if player has won the game
                if checkCorrect(blank):
                    print(f"Congratulations! You've guessed all the letters correctly! The Pokémon was {pokemon}.")
                    return True

                # Provide hint to player if reached a certain number of turns, and hasn't won yet
                pokeHint(maxTries - tries, pokemonQuery)

            # If players has entered an incorrect letter
            else:
                tries += 1
                print(
                    f"Incorrect! There is no '{guess}' in the Pokémon name. Try again! (Remaining Turns: {maxTries - tries})\n")
                if maxTries - tries == 0:
                    print(f"GAME OVER! You have no attempts remaining. The Pokémon was {pokemon}.")
                    return False
                pokeHint(maxTries - tries, pokemonQuery)

        # If a player has entered a letter that is already guessed
        elif capitalGuess in lettersGuessed:
            print(f"You already guessed the letter '{guess}'! Please enter another letter. (Remaining Turns: {maxTries - tries})\n")
