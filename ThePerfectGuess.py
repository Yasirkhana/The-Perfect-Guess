#                               THE PERFECT GUESS GAME :

import random
rand = random.randint(0,100)
userscore = 1
# print(rand)


while userscore <= 10:
    user = int(input("Guess the number : "))

    if(user == rand):
        print(f'''HURAYYY...YOU guess it right BRAWO
                 YOUR SCORE :  {userscore}  ''')
        break

    elif (user < rand):
        userscore += 1
        print(" INSCREASE PLEASE !!")
        

    elif (user > rand):
        userscore += 1
        print(" DECREASE PLEASE !!")
        
            
else:
    print("HAWWW YOU LOST !")
    


