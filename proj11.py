"""

define the element id list 
def read file moves 
    reads the move file and returns a list of move objests 
def read file pokemeon 
    reads the pokemon file adn returns a list of pokemon objects 
def choose pokemon 
    Lets the users chose their pokemons for the battle 
def add moves
    adds for moves to each of the players pokemon objects 
def turn 
    this is where each player takes thier turn, chooses their move, or prints 
    out more information 

def main 
    ask the user if they want to play 
    ask the users to choise a pokemon 
    each player takes their turn 
    decides if the game is won or not 
    asks the players if they want to play again if the battle is over

"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
    takes the file pointer as an argument 
    returns a list of move objects
    '''
    
    move_list = []
    header = 'not skipped'
    for line in fp: 
        
        #skip the header line 
        if header == 'not skipped':
            header = 'skipped'
            continue 
        else: 
            line_list = line.split(',')   
            
            #not included 
            if line_list[4] == '' or \
                int(line_list[2]) != 1 or \
                int(line_list[9]) == 1 or \
                line_list[6] == '':
                    continue 

            name = line_list[1] 
            element = element_id_list[int(line_list[3])]
            power = int(line_list[4])    
            accuracy = int(line_list[6])
            attack_type = int(line_list[9])
            
            #create the move object 
            move_obj = Move(name, element, power, accuracy, attack_type)
            move_list.append(move_obj)
    
    return move_list
                
def read_file_pokemon(fp):
    '''
    takes the pokemon file pointer as an argument 
    returns a list of pokemon objects 
    '''
    
    poke_list = [] 
    id_list = [] 
    header = 'not skipped'
    for line in fp: 
        
        #skip the header line 
        if header == 'not skipped':
            header = 'skipped'
            continue 
        else: 
            
            #skip lines 
            line_list = line.split(',') 
            if line_list[0] in id_list:
                continue 
            else: 
                id_list.append(line_list[0])
            
            if int(line_list[11]) != 1:
                continue 
            
            #assign variables 
            name = line_list[1].lower()
            element1 = line_list[2].lower()
            element2 = line_list[3].lower()
            moves = None 
            hp = int(line_list[5])
            patt = int(line_list[6])
            pdef = int(line_list[7])
            satt = int(line_list[8])
            sdef = int(line_list[9])
            
            #create pokemon object 
            poke_obj = Pokemon(name, element1, element2, moves, hp, patt,
                               pdef, satt, sdef)
            poke_list.append(poke_obj)
        
    return poke_list
            
            
def choose_pokemon(choice,pokemon_list):
    '''
    takes the user choice and the pokemon list as arguments 
    returns a pokemon object if valud choice 
    returns None if invalid choice 
    '''

    try: 
        choice = int(choice) - 1 
        if choice > len(pokemon_list): 
            return None 
        else:
            poke_choice = pokemon_list[choice]
            poke_choice = deepcopy(poke_choice)
            return poke_choice
    except: 
        names_list = []
        for objs in pokemon_list: 
            name = Pokemon.get_name(objs)
            names_list.append(name)
            
        if choice in names_list: 
            c_index = names_list.index(choice)
            poke_choice = deepcopy(pokemon_list[c_index])
            return poke_choice 
            #print(choice) 
        else: 
            return None 
            

def add_moves(pokemon,moves_list):
    '''
    takes a pokemon object and the list of move objects as arguments
    returns a boolean, True if the moves were added, false if not 
    '''
    
    #adds the first random move 
    moves_added_list = [] 
    rand_1 = randint(0, len(moves_list)-1)
    rand_move_1 = moves_list[rand_1]
    pokemon.add_move(rand_move_1)
    moves_added_list.append(rand_move_1)
    
    p_el_1 = pokemon.get_element1()
    p_el_2 = pokemon.get_element2()
    #print(p_el_1, p_el_2)
    
    attempts = 0 
    while attempts <= 200 and len(moves_added_list) <4: 
        rand_2 = randint(0, len(moves_list) -1)
        attempts +=1 
        rand_move_2 = moves_list[rand_2]
        rand_move_el = rand_move_2.get_element()
        
        if rand_move_el == p_el_1 or rand_move_el == p_el_2:
            if rand_move_2 not in moves_added_list:
                pokemon.add_move(rand_move_2)
                moves_added_list.append(rand_move_2)
                
    if len(moves_added_list) == 4:
        return True 
    else: 
        return False


def turn (player_num, player_pokemon, opponent_pokemon):
    '''
    this is where the player takes their turn 
    Player decides their moves or prints out a more information 
    takes the player number, the attackers pokemon object, 
    and the opponents pokemon object 
    
    a boolean of weather the game was won or not is returned 
    '''
    if player_num == 1:
        other_player = 2 
    else: 
        other_player = 1 
    
    print('Player {}\'s turn'.format(player_num))
    print(player_pokemon)
    
    moves_list = player_pokemon.get_moves()  
    
    move_finished = False
    while not move_finished:    
        
        print("Show options: 'show ele', 'show pow', 'show acc'")
        p_choice = input("Select an attack between 1 and 4 or show option or 'q': ")
        
        #if the player wants to show an option 
        if p_choice == 'show ele':
            player_pokemon.show_move_elements()
        elif p_choice == 'show pow':
            player_pokemon.show_move_power()
        elif p_choice == 'show acc':
            player_pokemon.show_move_accuracy()
            
        #if the player selects a move 
        elif p_choice == '1' or p_choice == '2' or p_choice == '3' or p_choice == '4': 
            m_index = int(p_choice) - 1 
            p_move = moves_list[m_index]
            print('selected move: {}'.format(p_move)) 
            
            print()
            hp_before = opponent_pokemon.get_hp()
            print('{} hp before:{}'.format(opponent_pokemon.get_name(), 
                                            opponent_pokemon.get_hp()))
            #make the attack 
            no_effect = False
            player_pokemon.attack(p_move, opponent_pokemon)
            if hp_before == opponent_pokemon.get_hp():
                no_effect = True 
                print('No effect!')
            print('{} hp after:{}\n'.format(opponent_pokemon.get_name(), 
                                            opponent_pokemon.get_hp()))  
            
            if player_pokemon.get_hp() != 0 and opponent_pokemon.get_hp() != 0 and player_num == 2:
                print('Player 1 hp after: {}'.format(opponent_pokemon.get_hp()))
                print('Player 2 hp after: {}\n'.format(player_pokemon.get_hp()))
    
            move_finished == True 
            if opponent_pokemon.get_hp() == 0: 
                print('Player {}\'s pokemon fainted, Player {} has won the pokemon battle!'
                      .format(other_player, player_num))
                return False 
            else: 
                return True 
            
        elif p_choice == 'q':
            print('Player {} quits, Player {} has won the pokemon battle!'
                  .format(player_num, other_player))
            return False 
        

def main():
    '''
    does not take an argument 
    returns nothing 
    
    calls all the above functions here 
    asks the user for an input 
    players choose their pokemons 
    the battle happens here 
    
    '''
        
    #open and read the files 
    moves_fp = open('moves.csv', 'r') 
    moves_list = read_file_moves(moves_fp)
    poke_fp = open('pokemon.csv', 'r')
    poke_list = read_file_pokemon(poke_fp)

                   
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    
    #while loop for invalud options 
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
    
    while usr_inp == 'y':
    
        #player 1 chose pokemon
        val = None 
        while val == None: 
            choice = input('Player 1, choose a pokemon by name or index: ').lower()
            p1 = choose_pokemon(choice, poke_list)
            if type(p1) == Pokemon: 
                val = True 
            else: 
                val = None 
         
        print('pokemon1:')
        print(p1)
        
        #add moves to player 2 pokemon 
        p1_bool = add_moves(p1, moves_list)
        
        #player 2 choose pokemon 
        val = None 
        while val == None: 
            choice = input('Player 2, choose a pokemon by name or index: ').lower()
            p2 = choose_pokemon(choice, poke_list)
            if type(p2) == Pokemon: 
                val = True 
            else: 
                val = None 
         
        print('pokemon2:')
        print(p2)
        
        #add moves to player 2 pokemon
        p2_bool = add_moves(p2, moves_list)
        
        ### START BATTLE ###    
        p1_continue = True
        p2_continue = True
        
        while p1_continue == True and p2_continue == True:
            p1_continue = turn(1, p1, p2)
            if p1_continue == True: #if flase, the loop will exit 
                p2_continue = turn(2, p2, p1)
                #if false, the loop will exi 
                
        #start the loop over 
        usr_inp = input('Battle over, would you like to have another? ').lower()
        
    print("Well that's a shame, goodbye")                

if __name__ == "__main__":
    main()
