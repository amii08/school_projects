import sys
from lotto import * 
from multi import *
from eurojackpot import *
from nickname import *
from rules import *


#print("Welcome "+nickname+"!") 
#print("Wybierz grę!")
#print("·Lotto(1)")
#print("·Multi Multi(2)")
#print("·Eurojackpot(3)")
#main_input = input("Enter game: ").upper()

while True:
    print("Welcome "+nickname+"!") 
    print("Wybierz grę!")
    print("·Lotto(1)")
    print("·Multi Multi(2)")
    print("·Eurojackpot(3)")
    main_input = input("Enter game: ").upper()
    if main_input == "1" or main_input == "LOTTO":
        agree = input("Are you sure (yes/no): ").upper()
        if agree == "YES":
            agree_rules = input("Chcesz poznac zasady(yes/no)?:").upper()
            if agree_rules == "YES":
                print(all_rules['lotto'])
                lotto_script()
            elif agree_rules == "NO":
                lotto_script() 
        if agree == "NO":
            sys.exit("Ok")

      
    elif main_input == "2" or main_input == "MULTI":
        agree = input("Are you sure (yes/no): ").upper()
        if agree == "YES":
            agree_rules = input("Chcesz poznac zasady(yes/no)?:").upper()
            if agree_rules == "YES":
                print(all_rules['multi-multi'])
                multi_script()
            elif agree_rules == "NO":
                multi_script()
            if agree == "NO":
                sys.exit("Bye, come again!")

    elif main_input == "3" or main_input == "EUROJACKPOT":
        agree = input("Are you sure (yes/no): ").upper()
        if agree == "YES":
            agree_rules = input("Chcesz poznac zasady(yes/no)?:").upper()
            if agree_rules == "YES":
                print(all_rules['eurojackpot'])
                euro_script()
            elif agree_rules == "NO":
                euro_script()
            if agree == "NO":
                sys.exit("Bye, come again!")
    
    play_again = input("Chcesz zagrac ponownie? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")
            
         

