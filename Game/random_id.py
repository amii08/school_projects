import random
import string
letter_id = str(random.choice(string.ascii_letters)).upper()
number_id = str(random.randint(0,100))
full_id = letter_id+number_id
final_id = "#"+full_id
print("Your id: "+final_id)

