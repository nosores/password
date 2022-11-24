import random
import pyperclip as pc

def generatePassword(x):  

    max_char=0
    if x == "low":
        max_char=8
    elif x== "middle":
        max_char = 12 
    else:
        max_char = 16
    lst_pass=[]
    lst_char=[]
    character =""
    for i in range(1,max_char+1):
      lst_char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","(",")","[","]","$",".","-",]
      character=random.choice(lst_char)
      lst_pass.append(character)
    a = "".join(lst_pass)
    return a 
level_security = input("Seleccion el nivel de seguridad (low/middle/high): ")
pw  = generatePassword(level_security)
print(pw)

pc.copy(pw)