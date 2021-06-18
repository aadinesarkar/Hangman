from random import choice
from os import system, name
import dump


def clear_screen():
    if name=="nt":
        system("cls")
    else:
        system("clear")

class hangman:
    count=0
    guessed_word=[]
    def start_game(self):
        print("Press enter to start")
        input()
        clear_screen()
        self.chosen_word=dump.choose_word()
        self.chosen_word_cpy=self.chosen_word
        self.chosen_word=list(self.chosen_word)
        for i in self.chosen_word:
            self.guessed_word.append("_ ")
    def print_man(self):
        clear_screen()
        print(dump.get_man(self.count),end="\n\n")
        print("The word:",end="") 
        for i in self.guessed_word:
            print(i,end="")
        print()           
    def check_letter(self,letter):
        if letter in self.chosen_word:
            while letter in self.chosen_word:
                i=self.chosen_word.index(letter)
                self.guessed_word[i]=letter+" "
                self.chosen_word[i]="~"
        else:
            self.count+=1


p1=hangman()
p1.start_game()
while p1.count<6 and "_ " in p1.guessed_word:
    p1.print_man()
    p1.check_letter(input("Enter a letter:"))
if p1.count==6:
    p1.print_man()
    print(f"\033[31mGAME OVER\033[0m\nThe word was:{p1.chosen_word_cpy}\n\nPress enter to exit")
    input()
else:
    p1.print_man()
    print("You won!!!🏆\n\nPress enter to exit")
    input()