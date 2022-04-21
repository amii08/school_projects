from random import *
from random_id import * 
from nickname import *
from time_date import *

id_data = final_id
time_data = data_time
nick_data = nickname
def lotto_script():
    lotto_win = []
    for l in range(0,6):
        ran_number = randint(1,49)

        while ran_number in lotto_win: #aby uniknąć powtórzeń 
            ran_number = randint(1,49)

        lotto_win.append(ran_number)

    lotto_win.sort()
    lotto_win_str = (' '.join(map(str,lotto_win)))
    user_numbers = []
    for l in range(0,1):
        inp = input("Podaj 6 liczb przez space od 1 do 49: ")
        inp_list = inp.split()
        user_numbers = []
    for x in inp_list:
        try:
            x = int(x)
            if x in user_numbers or x < 1 or x > 49:
                continue
            if len(user_numbers) > 6:
                del user_numbers[6:1000]
            user_numbers.append(x)
        except ValueError:
            pass


    user_numbers.sort()
    user_numbers_srt  = (' '.join(map(str,user_numbers)))
    if user_numbers == lotto_win:
        wl_lotto = "WIN"
        print("Win numbers:",lotto_win_str,";")
        #print(lotto_win)
        print("Your numbers:",user_numbers_srt,";")
        #print(user_numbers)
        print(wl_lotto)
    else:
        wl_lotto = "LOSE"
        print("Win numbers:",lotto_win_str,";")
        #print(lotto_win)
        print("Your numbers:",user_numbers_srt,";")
        #print(user_numbers)
        print(wl_lotto)
        
    all_data = [id_data,nick_data,time_data,lotto_win_str,wl_lotto]
    with open('data.csv','a') as file:
        file.write("\nId: "+all_data[0]+"|""Date: "+all_data[2]+"|""Nickname: "+all_data[1]+"|""Win_numbers_from_1 to 49: "+all_data[3]+"|""Result: "+all_data[4]+"|""Game: Lotto")

