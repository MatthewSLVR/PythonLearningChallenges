import time
import os

letterList = []
wrongGuesses = []
guessedLetter = ''
tries = 8
typeWord = []

def gamestart():
    print("Witaj w wisielcu! Jeżeli to czytasz, to znaczy, że jesteś graczem który wybiera słowo!\nJeżeli tak nie jest, podaruj klawiaturę tej osobie, żeby wybrała słowo do odgadnięcia!\n")
    global typeWord
    typeWord = list(input("Wpisz słowo, które odgadnąć ma przeciwnik!\n"))
    os.system('cls' if os.name == 'nt' else 'clear')

gamestart()

def blank_letters(typeWord):
    for letter in range(len(typeWord)):
        letterList.append('_')

blank_letters(typeWord)

def game(typeWord):
    global tries
    while '_' in letterList and tries > 0:
        guess = input("Zgadnij literę!\n")
        for letter in range(len(typeWord)):
            wrongLetter = False
            if guess in typeWord[letter]:
                letterList[letter] = guess
                print("Zgadłeś literę 8)\n", ' '.join(letterList))
        if len(guess) > 1:
            print("Tylko jedna litera...")
        elif guess not in typeWord:
            wrongGuesses.append(guess)
            print("nie zgadłeś :C")
            minus_tries()
            print(f"Zostało Ci {tries} prób, twoje dotychczasowe próby to: {', '.join(wrongGuesses)}")
            match tries:
                case 7:
                    print("""
                            +---+
                            |   |
                                |
                                |
                                |
                                |
                          =========
                          """)
                case 6:
                    print(""" 
                              +---+
                              |   |
                              O   |
                                  |
                                  |
                                  |
                            =========
                            """)
                case 5:
                    print("""  
                               +---+
                               |   |
                               O   |
                               |   |
                                   |
                                   |
                             =========
                             """)
                case 4:
                    print(""" 
                               +---+
                               |   |
                               O   |
                              /|   |
                                   |
                                   |
                             =========
                             """)
                case 3:
                    print(""" 
                               +---+
                               |   |
                               O   |
                              /|\  |
                                   |
                                   |
                             =========
                             """)
                case 2:
                    print(""" 
                              +---+
                              |   |
                              O   |
                             /|\  |
                             /    |
                                  |
                            =========
                            """)
                case 1:
                    print("""  
                               +---+
                               |   |
                               O   |
                              /|\  |
                              / \  |
                                   |
                             =========
                             """)

    else:
        letterList.clear()
        wrongGuesses.clear()
        typeWord.clear()
        play_again()

def minus_tries():
    global tries
    tries -= 1
    if tries == 0:
        print("Koniec gry, przegrałeś :C")
        print(f"Oto pełne słowo! - {''.join(typeWord)}")

def play_again():
    global tries
    again = input("Chcesz zagrać jeszcze raz? Napisz 'tak' lub 'nie'\n")
    if again == 'tak':
        os.system('cls' if os.name == 'nt' else 'clear')
        tries = 8
        gamestart()
        blank_letters(typeWord)
        game(typeWord)
    elif again == 'nie':
        print("Żegnaj więc, miłego dzionka!")
        codedelay = 5
        while codedelay > 0:
            time.sleep(1)
            codedelay -= 1
            print(f"Program wyłączy się za {codedelay}...")
    else:
        play_again()

game(typeWord)

