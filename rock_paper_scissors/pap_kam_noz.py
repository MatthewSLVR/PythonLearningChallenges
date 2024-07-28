import random
import time

x = input("Wybierz papier, kamień, albo nożyce\n")
playerChose = 0
botChose = 0
translatedChose = ''
def player_choose_transform(x):
    global playerChose
    while playerChose == 0:
        match x:
            case "papier":
                playerChose = 1
                print("Wybrałeś papier!")
                bot_guess()
                compare()
            case "kamien":
                playerChose = 2
                print("Wybrałeś kamień!")
                bot_guess()
                compare()
            case "kamień":
                playerChose = 2
                print("Wybrałeś kamień!")
                bot_guess()
                compare()
            case "nozyce":
                playerChose = 3
                print("Wybrałeś nożyce!")
                bot_guess()
                compare()
            case "nożyce":
                playerChose = 3
                print("Wybrałeś nożyce!")
                bot_guess()
                compare()
            case _:
                print("Zły wybór!")
                x = input("Wybierz papier, kamień, albo nożyce\n")


def bot_guess():
    global botChose
    print("Teraz wybiera bot!")
    wait = 3
    while wait != 0:
        print("Komputer wybiera...")
        wait -= 1
        time.sleep(1)
    botChose = random.randint(1,3)
    translate_guess()
    print(f"Komputer wybrał {translatedChose}")

def translate_guess():
    global botChose
    global translatedChose
    match botChose:
        case 1:
            translatedChose = "papier"
        case 2:
            translatedChose = "kamień"
        case 3:
            translatedChose = "nożyce"
def compare():
    global playerChose
    global botChose
    if playerChose == botChose:
        print("Remis!")
        play_again()
    elif playerChose == 1 and botChose == 2:
        print("Wygrałeś!")
        play_again()
    elif playerChose == 1 and botChose == 3:
        print("Przegrałeś!")
        play_again()
    elif playerChose == 2 and botChose == 1:
        print("Przegrałeś!")
        play_again()
    elif playerChose == 2 and botChose == 3:
        print("Wygrałeś!")
        play_again()
    elif playerChose == 3 and botChose == 1:
        print("Wygrałeś!")
        play_again()
    elif playerChose == 3 and botChose == 2:
        print("Przegrałeś!!")
        play_again()
def play_again():
    global playerChose
    global botChose
    global translatedChose
    again = input("Czy chcesz zagrać jeszcze raz? Napisz tak, lub nie\n")
    match again:
        case "tak":
            x = input("Wybierz papier, kamień, albo nożyce\n")
            playerChose = 0
            botChose = 0
            translatedChose = ''
            player_choose_transform(x)
        case "nie":
            wait = 3
            while wait != 0:
                print(f"Program wyłączy się za {wait}...")
                wait -= 1
                time.sleep(1)
        case _:
            play_again()

player_choose_transform(x)
