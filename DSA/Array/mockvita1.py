# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:59:09 2020

@author: KayDee / Sam 
"""

import random
class bankAccount():
    
    def __init__(self,name,amount):
        self.name = name 
        self.amount = amount
        
    def bet(self,b):
        self.b = b
        if self.b > self.amount:
            print("Not enough funds")
            print("Restarting game")
            driver_core()
        else:
            self.amount -= self.b
            print("Bet placed")
        
class deck_hand():
    def __init__(self):
        self.deck = []
    def start(self):
        for i in range(2):
            self.deck.append(random.randint(1,13))
        return self.deck
    def hit(self):
        pass
    def stay(self):
        pass
            
        
        
 


       

    


def card(c):
    global deck
    
    for i in c:
    
       print("+-----+")
       print("|{0}    |".format(deck[i][2]))
       print("|     |")
       print("|    {0}|".format(deck[i][2]))
       print("+-----+")       
  

    
    
class show_deck():
    def __init__(self,deck):
        self.deck = deck
        pass
    def dealer_deck(self):
        print("Dealer Deck(One card is hidden) :")
        card(self.deck[:-1])
    def player_deck(self):
        print("Player Deck :")
        card(self.deck)



def deck_init():   
    for i in range(2,11):
        deck[i] = [4,i,str(i)]
    deck[1] = [4,11,'A']
    deck[11] = [4,10,'J']
    deck[12] = [4,10,'Q']
    deck[13] = [4,10,'K']
    



def gamestart():
    dealer = deck_hand()
    player = deck_hand()
    deck_init()
    d_deck = dealer.start()
    p_deck = player.start()
    dds = show_deck(d_deck)
    pds = show_deck(p_deck)
    dds.dealer_deck()
    pds.player_deck()
    p_deck_sum = []
    print("Your deck current total : {}".format(sum([deck[p_deck[0]][1], deck[p_deck[1]][1]])))
    cmd = input("Hit or Stay : ")
    while (cmd == "hit" or "Hit"):
        p_deck.append(random.randint(1,13))
        print(p_deck)
        for i in p_deck:
            p_deck_sum.append(deck[i][1])
        pds.player_deck()
        print("Your deck current total : {}".format(sum(p_deck_sum)))
        if sum(p_deck_sum) > 21:
            print("You are busted, play again? (yes/no)")   
            if (input() == "yes"):
                driver_core()
            else:
                break
        cmd = input("Hit or Stay : ")
                
    
    
   



def driver_core(): 
    deck = {}
    name = input("Enter your name : ")
    amt = int(input("Enter the amount : "))
    playerAC = bankAccount(name,amt)
    bet_call = int(input("Enter bet amount : "))
    playerAC.bet(bet_call)
    
    gamestart()
        
deck = {}

driver_core()      
        
        
        