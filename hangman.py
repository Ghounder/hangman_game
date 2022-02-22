import os
import random


def read():
    words = []
    with open("./archivos/data.txt","r", encoding="utf-8") as data:
        for line in data:
            words.append(line)
    return words


def random_choice(words):
    return random.choice(words)


def screen(lives,word,hidden,remaining_words):
    buffer = " "
    while lives >=0:
        print("                                                               Hangman Game\n\n")
        print("Lives : ",lives,"\n")
        print(remaining_words)
        print(word,"\n")
        print(buffer.join(hidden))
        letter = input("Ingrese una letra : ").lower()
        if check_if_exist(letter,word):
            hidden = update(word,letter,hidden)
            remaining_words-=1
        else:
            lives-=1
        if remaining_words <= 0:
            os.system("cls")
            win(word)
        os.system("cls")
    lose(word)


def update(word,letter,hidden):
    list_of_indices = [i for i in range(len(word)) if word[i] == letter]
    for i in list_of_indices:
        hidden[i]=word[i]    
    return hidden


def win(word):
    buffer = ""
    print(buffer.join(word))
    print("YOU WIN")
    print("Try again?\n\n1.Yes\n2.No")
    ans = input("continue? : ")
    if ans == 1:
        run()
    elif ans == 2:
        return print("GAME OVER")


def lose(word):
    buffer = ""
    print(buffer.join(word))
    print("Try again?\n\n1.Yes\n2.No")
    ans = input("continue? : ")
    if ans == 1:
        run()
    elif ans == 2:
        return print("GAME OVER")


def check_if_exist(letter, word):
    if letter in word:
        return True


def run ():
    lives = 8
    words = read()
    word = random_choice(words).strip()
    table = word.maketrans("áéíóú","aeiou")
    word = list(word.translate(table))
    remaining_words = len(list(set(word)))
    hidden = list(len(word)*"_")
    screen(lives,word,hidden,remaining_words)


if __name__ == "__main__":
    run()