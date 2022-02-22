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


def screen(lives,word,hidden):
    buffer = " "
    while lives >=0:
        print("                                                               Hangman Game\n\n")
        print("Lives : ",lives,"\n")
        #print(word,"\n")
        print(buffer.join(hidden))
        letter = input("Ingrese una letra : ").lower()
        if check_if_exist(letter,word):
            hidden = update(word,letter,hidden)
        else:
            lives-=1
        os.system("cls")
    lose()


def update(word,letter,hidden):
    list_of_indices = [i for i in range(len(word)) if word[i] == letter]
    for i in list_of_indices:
        hidden[i]=word[i]    
    return hidden


def win():
    pass


def lose():
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
    hidden = list(len(word)*"_")
    screen(lives,word,hidden)


if __name__ == "__main__":
    run()