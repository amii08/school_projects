from random import *
from random_id import * 
from nickname import *
from time_date import *


id_data = final_id
time_data = data_time
nick_data = nickname
def euro_script():
    euro_win_1 = []
    for i in range(0,5):
        number_1 = randint(1,50)

        while number_1 in euro_win_1: #aby uniknąć powtórzeń 
            number_1 = randint(1,50)
        
        euro_win_1.append(number_1)
    
    euro_win_1.sort()
    euro_win_1_str = (' '.join(map(str,euro_win_1)))
    user_numbers_1 = []
    #for e in range(0,5):
    #    number_1 = int(input("Podaj liczbę: "))
    #    while number_1 in user_numbers_1 or number_1 < 0 or number_1 > 50:
    #        print("Błąd.\nPodaj liczbe od 1 do 50!")
    #        number_1 = int(input("Podaj liczbę: "))
    #    user_numbers_1.append(number_1)
    user_numbers_1 = []
    for e in range(0,1):
        inp = input("Podaj 5 liczb przez space od 1 do 50: ")
        inp_list = inp.split()
        user_numbers_1 = []
    for x in inp_list:
        try:
            x = int(x)
            user_numbers_1.append(x)
            if len(user_numbers_1) > 5:
                del user_numbers_1[5:1000]
        except ValueError:
            pass
    
    user_numbers_1.sort()
    user_numbers_1_srt = (' '.join(map(str,user_numbers_1)))
    print("Teraz podaj 2 liczby z 12")
    euro_win_2 = []
    for e in range(0,2):
        number_2 = randint(1,12)

        while number_2 in euro_win_2: #aby uniknąć powtórzeń 
            number_2 = randint(1,12)
        
        euro_win_2.append(number_2)

    
    euro_win_2.sort()
    euro_win_2_str = (' '.join(map(str,euro_win_2)))
    #user_numbers_2 = []
    #for i in range(0,2):
    #    number_2 = int(input("Podaj liczbę: "))
    #    while (number_2 in user_numbers_2 or number_2 < 0 or number_2 > 12):
    #        print("Błąd.\nPodaj liczbe od 1 do 12!")
    #        number_2 = int(input("Podaj liczbę: "))
    #    user_numbers_2.append(number_2)
    user_numbers_2 = []
    for e in range(0,1):
        inp = input("Podaj 2 liczby przez space od 1 do 12: ")
        inp_list = inp.split()
        user_numbers_2 = []
    for x in inp_list:
        try:
            x = int(x)
            user_numbers_2.append(x)
            if len(user_numbers_2) > 2:
                del user_numbers_2[2:1000]
        except ValueError:
            pass
        
    user_numbers_2.sort()
    user_number_2_srt = (' '.join(map(str,user_numbers_2)))
    if user_numbers_1 == euro_win_1 and user_numbers_2 == euro_win_2:
        wl_euro = "WIN"
        print("\nWin_numbers_from_1 to 50:",euro_win_1_str,';')
        #print(euro_win_1)
        print("Your_numbers_from_1 to 50:",user_numbers_1_srt,";")
        #print(user_numbers_1)
        print("Win_numbers_from_1_to_12:",euro_win_2_str,';')
        #print(euro_win_2)
        print("Your_numbers_from_1_to_12:",user_number_2_srt,";")
        #print(user_numbers_2)
        print(""+wl_euro)
    else:
        wl_euro = "LOSE"
        print("\nWin_numbers_from_1 to 50:",euro_win_1_str,';')
        #print(euro_win_1)
        print("Your_numbers_from_1 to 50:",user_numbers_1_srt,";")
        #print(user_numbers_1)
        print("Win_numbers_from_1_to_12:",euro_win_2_str,';')
        #print(euro_win_2)
        print("Your_numbers_from_1_to_12:",user_number_2_srt,";")
        #print(user_numbers_2)
        print(""+wl_euro)
        
        
    all_data = [id_data,nick_data,time_data,euro_win_1_str,euro_win_2_str,wl_euro]
    with open('data.csv','a') as file:
        file.write("\nId: "+all_data[0]+"|""Date: "+all_data[2]+"|""Nickname: "+all_data[1]+"|""Win_numbers_from_1 to 50: "+all_data[3]+"|""Win_numbers_from_1_to_12: "+all_data[4]+"|""Result: "+all_data[5]+"|""Game: Eurojackpot")

