import random 
from game_data import data
from art1 import logo
from art1 import vs
import os 
should_continue=True
account=[]
data1=[]
data2=[]
k=0
def format():
    account=random.choice(data)
    name=account["name"]
    desription=account["description"]
    country=account["country"]
    follower=account["follower_count"]
    return [name,desription,country,follower]


def compare(choice,data3,data4):
    if data3>data4 and choice=="B":
        return "You got it correct"
       
            
    elif data4>data3 and choice=="B":
        return "You got it correct"
    else:
        return "You guessed wrong"    
        
                





while should_continue:
    print(logo)
    data1=format()
    print(f"Compare A:{data1[0]},{data1[1]},{data1[2]}")
    print(vs)
    data2=format()
    print(f"Compare B:{data2[0]},{data2[1]},{data2[2]}")
    choice=input("Guess between A and B which one has greater followers.").upper()
    choice_ans=compare(choice,data1[3],data2[3])

    if choice_ans=="You got it correct":
        k=k+1
        data1=[]
        data2=[]
        os.system('cls')
        print(f"{choice_ans},Your score is {k}")
        continue
    elif choice_ans=="You guessed wrong":
        data1=[]
        data2=[]
        os.system('cls')
        print(f"{choice_ans},Your score is {k}")


    choose=input("Do you want to start a new a game 'yes' or 'no'?").lower()
    if choose=="no":
        should_continue=False
    else:
        os.system('cls')        

    