
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
import random

faces = np.array(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])
suits = np.array(['Spades', 'Hearts', 'Clubs', 'Diamonds'])

class Player():
    count_of_players = 0
    def __init__(self, cards, position, mine):
        self.cards = cards
        self.position = position
        self.mine = mine
        count_of_players = self.count_of_players+1
    
    def get_cards(self):
        return self.cards
    
    def get_position(self):
        return self.position
    
    def set_cards(self, cards):
        self.cards = cards

    def set_position(self, position):
        self.position

    def print_player_details(self):
        print("Cards: ",  self.cards)
        print("Position: " ,  self.position)
        print("Me? ", self.mine)

    def get_my_player(self):
        return self.cards, self.position

    def set_as_my_player(self, mine):
        self.mine = True

    def number_of_players(self):
        return self.count_of_players


def take_card_from_deck(face, suit):
    card = deck_dataframe.loc[face, suit]
    deck_dataframe.loc[face, suit] = ''
    ## DESIGN SO THAT USER CANNOT BE RETURNED BLANK VALUE
    return card

def new_deck_as_nparray():
    i, j = 0, 0
    
    for count in range(52):
        dek = []
    count = 0
    for face in faces:
        
        for suit in suits:
            
            dek.append(face + suit)
            count = count+1

    np.random.shuffle(dek)
    np_deck = np.array(dek)
    return np_deck

def seat_rotation(position_array, pos1, pos2):
    tmp = position_array[pos1]
    position_array[pos1] = position_array[pos2]
    position_array[pos2] = tmp

deck_nparray = new_deck_as_nparray() 
deck_dataframe = pd.DataFrame(index=suits, columns = faces) ## NOT COMPLETE
for seq1 in faces:
    for seq2 in suits:
        deck_dataframe.loc[seq1,seq2] = seq1+seq2
deck_dataframe = (deck_dataframe.loc['2':, 'Spades':])




player_list = []
positions = ['Dealer', 'SB', 'BB'] ## More players may be added to the array
my_character_tracker = ''

class Hand_in_game():

    def __init__(self):
        pass
      
    
    def get_players(self):
        #return self.players
        pass

    def generate_hand(self):

        for position in positions:

            randomSuit = random.choice(suits)
            randomFace = random.choice(faces)
            self.generatedCardOne = take_card_from_deck(randomFace, randomSuit)
            randomSuit = random.choice(suits)
            randomFace = random.choice(faces)
            self.generatedCardTwo = take_card_from_deck(randomFace, randomSuit)
            
            return self.generatedCardOne, self.generatedCardTwo
            
    def generate_players(self, pos, tmp):
            
            if tmp.index(pos) == 0:
               
                p = Player(np.array(self.generate_hand()), pos, True)
                player_list.append(p)

            else:
                
                p = Player(np.array(self.generate_hand()), pos, False)
                player_list.append(p)

            positions.insert(0, positions.pop())
            

         
            # original_state = []
            # original_state.append(positions[len(positions)-1])
            # if pos == (len(positions)-1):
            #     print("set 1")
            #     seat_rotation(original_state, pos, 0)
            # else: 
            #     print("set 2")
            #     for swap_position in range(len(positions)-1):
            #         original_state.append(positions[swap_position])
            #     for swap_position in range(len(positions)-1):
            #         seat_rotation(original_state, swap_position,swap_position+1) 
            
handDF = pd.DataFrame()

for handOfRound in range(len(positions)):
    hand = Hand_in_game()  
    tmp = positions.copy()
    ## REMINDER: Tmp is used as local copy for shifting of positions
    for p in tmp: 
        hand.generate_players(p, tmp)    

    # hand.generate_hand()
    cardsPerPlayer = []
    for p in player_list:
        cardsPerPlayer.append(p.get_cards())
    handDF = pd.DataFrame(index=tmp, columns = cardsPerPlayer)
    print(handDF)
        
    for seq1 in faces:
        for seq2 in suits:
            deck_dataframe.loc[seq1,seq2] = seq1+seq2

    tmp.insert(0, tmp.pop())
    


# for player in player_list:
#     player.print_player_details()



