from random import *
from random_id import * 
from nickname import *
from time_date import *

id_data = final_id
time_data = data_time
nick_data = nickname
def multi_script():
    multi_win = []
    for m in range(0,10):
        ran_number = randint(1,80)

        while ran_number in multi_win: #aby uniknąć powtórzeń 
            ran_number = randint(1,80)

        multi_win.append(ran_number)

    multi_win.sort()
    multi_win_str = (' '.join(map(str,multi_win)))
    for m in range(0,1):
        inp = input("Podaj 10 liczb przez space od 1 do 80: ")
        inp_list = inp.split()
        user_numbers = []
        for x in inp_list:           
            try:
                x = int(x)
                if x in user_numbers or x < 1 or x > 80:
                    continue
                if len(user_numbers) > 10:
                    del user_numbers[10:]
                user_numbers.append(x)
            except ValueError:
                pass

        #user_numbers.append(x)
    user_numbers.sort()
    user_numbers_srt = (' '.join(map(str,user_numbers)))
    if user_numbers == multi_win:
        wl_multi = "WIN"
        print("\nWin_numbers_from_1_to_80:",multi_win_str,";")
        #print(multi_win)
        print("Your_numbers_from_1_to_80:",user_numbers_srt,";")
        #print(user_numbers)
        print(wl_multi)     
    else:
        wl_multi = "LOSE"
        print("\nWin_numbers_from_1_to_80:",multi_win_str,";")
        #print(multi_win)
        print("Your_numbers_from_1_to_80:",user_numbers_srt,";")
        #print(user_numbers)
        print(wl_multi)


    all_data = [id_data,nick_data,time_data,multi_win_str,wl_multi]
    with open('data.csv','a') as file:
        file.write("\nId: "+all_data[0]+"| ""Date: "+all_data[2]+"| ""Nickname: "+all_data[1]+"| ""Win_numbers_from_1 to 80: "+all_data[3]+"| ""Result: "+all_data[4]+"| ""Game: Multi Multi")
