import random

#BlackJack 


suits = ("Copas", "Paus", "Espadas", "Ouros")

ranks = ("Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Valete","Dama","Rei","As")

values = {"Dois":2,"Tres":3,"Quatro":4,"Cinco":5,"Seis":6,"Sete":7,"Oito":8,"Nove":9,"Dez":10,"Valete":11,"Dama":12,"Rei":13,"As":14}

class Card():

    def __init__(self,rank,suit) -> None:

        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]

    def __str__(self) -> str:
        return self.rank + " de " + self.suit




class Deck():

    def __init__(self) -> None:
        
        self.allcards = []
        
        for rank in ranks:
            for suit in suits:

                created_card = Card(rank,suit)

                self.allcards.append(created_card)
    
    def shuffle(self):

        random.shuffle(self.allcards)
    
    def deal_one(self):

        card = self.allcards.pop(0)
        return card.value

baralho = Deck()

class Dealer():
    
    def __init__(self) -> None:
        
        self.d_card = [] 

    def add(self,i):
            self.d_card.append(i)

    def __str__(self) -> str:
        
        return f" O valor da carta do dealer    ->  {self.d_card[0]} "

class Player():

    def __init__(self,name) -> None:

        self.name = name
        self.p_all_cards = []

    def add(self,a):

        self.p_all_cards.append(a)
    

    def __str__(self) -> str:
        
        return f"\n O valor de suas cartas  ->  {self.p_all_cards[1]} "


class Chips:

    pass




def menu():
    while True:

    
        print          ("BEM VINDO A BLACKJACK")
        
        

        # BETTING CHIPS

One = Player("Heitor")     

dealer = Dealer()

baralho.shuffle()

for x in range(1):
    dealer.add(baralho.deal_one())
    
for x in range(2):
    One.add(baralho.deal_one())


def jogar():
    while True:


        
        while True:

            print(dealer)

            print(One)
            
            while True:
                choice = input("Hit or Stand --->  ")
                if choice not in ["Hit","H","h","Stand","S","s","stand","hit"]:
                    print("Invalid Input")
                    continue
                else:
                    break

            if choice.lower().startswith("h"):
                One.add(baralho.deal_one())

                if  sum(One.p_all_cards) > 21:
                    print("YOU BUSTED")
                    break
                else:
                    continue
                            
            elif choice.lower().startswith("s"):

                while sum(One.p_all_cards) > sum(dealer.d_card):
                    dealer.add(baralho.deal_one())
        

jogar()
        

                






        




    

    









