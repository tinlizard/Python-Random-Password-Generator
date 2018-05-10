import random
import time

def passwordGenerator():
    integer = ['12', '26', '45', '321', '187', '92', '451', '877']
    string = ['ArtilerrY','TONgue','Persson','AppLe','Orrange','Magg','LiFe', 'Arrgon','Kryyptonite','MarVel','Universe','Acccellerate']
    string2 = ['Amon', 'Salmon', 'Cheese', 'Omano', 'Tiger', 'Giraffe', 'Euro', 'Lego']
    
    print("Generating password, please wait.")
    time.sleep(1)
    print(random.choice(string) + random.choice(string2) + random.choice(integer))

passwordGenerator()
    
