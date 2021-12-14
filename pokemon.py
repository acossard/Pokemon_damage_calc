"""
pokemon and moves classes 

define effective, kinda effective, and not effective dictionaries 

create the move class 
    define the following attributes 
    name 
    element 
    power 
    accuracy 
    attack type 
    
    define the followign methods 
    __init__
    __eq__
    __str__
    _-self__
    __repr__
    get_name 
    get_element 
    get_power 
    get_accuracy 
    get_attack_type 
    
create the Pokemon class 
    define the following attributes 
    name 
    element 1 
    elemetn 2 
    hp 
    patt 
    pdef
    satt
    sdef
    moves
    
    define the floowing methods 
    __init__
    __str__
    __eq__
    __rept__
    get name 
    get_element 
    get_hp 
    get_pdef
    get satt 
    get_sdef
    get_moves 
    get_number_moves 
    chose 
    show_move_elements 
    show_move_power 
    show_move_accuracy 
    add_move
    attack 
    
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
        reutns a string of the move's name
        '''        
        string = self.name 
        
        return string 

    def __repr__(self):
        '''
        retuns a string of the moves name 
        '''
        string = self.name 
        
        return string 
    
    def get_name(self):
        '''
        returns a sting of the moves name 
        '''
        string = self.name 
        
        return string 
    
    def get_element(self):
        '''
        returns a sting of the moves elemetn 
        '''
        string = self.element 
        
        return string 
    
    def get_power(self):
        '''
        retuns an int of the moves power 
        '''
        integer = int(self.power)
        
        return integer 
    
    def get_accuracy(self):
        '''
        returns an int of the moves accuracy 
        '''
        integer = int(self.accuracy)
        
        return integer 
    
    def get_attack_type(self):
        '''
        retuns an int of the moves attack type 
        '''
        integer = int(self.attack_type)
        
        return integer 

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
        retuns a sting of all the information for the pokemon object 
        '''
        L1 = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(self.name, 
                        self.hp, self.patt, self.pdef, self.satt, self.sdef)
        L2 = '{:<15}{:<15}'.format(self.element1, self.element2)
        L3 = ''
        for move in self.moves:
            move = str(move)
            L3 = L3 + '{:<15}'.format(move) 
            
        string = '{}\n{}\n{}'.format(L1, L2, L3)
        return string 

    def __repr__(self):
        '''
        retunrs a sting of all the information for the pokemon object 
        '''
        L1 = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(self.name, 
                        self.hp, self.patt, self.pdef, self.satt, self.sdef)
        L2 = '{:<15}{:<15}'.format(self.element1, self.element2)
        L3 = ''
        for move in self.moves:
            move = str(move)
            L3 = L3 + '{:<15}'.format(move) 
            
        string = '{}\n{}\n{}'.format(L1, L2, L3)
        return string 


    def get_name(self):
        '''
        returns a sting of the pokemons name 
        '''
        string = self.name 
        return string 
    
    def get_element1(self):
        '''
        returns a sting of the pokemons element 1
        '''
        string = self.element1
        return string
    
    def get_element2(self):
        '''
        reutns a string of the pokemons element 2
        '''
        string = self.element2 
        return string
    
    def get_hp(self):
        '''
        returns an int of the pokemons health 
        '''
        integer = self.hp
        return integer 
    
    def get_patt(self):
        '''
        retuns an int of the pokemons patt
        '''
        integer = self.patt
        return integer 

    def get_pdef(self):
        '''
        returns a string of the pokemons pdef 
        '''
        integer = self.pdef 
        return integer 

    def get_satt(self):
        '''
        retuns an int of the pokemons satt
        '''
        integer = self.satt
        return integer

    def get_sdef(self):
        '''
        retuns an int of the pokemons sdef
        '''
        integer = self.sdef 
        return integer
    
    def get_moves(self):
        '''
        retuns the pokemons list of moves
        '''
        lst = self.moves 
        return lst

    def get_number_moves(self):
        '''
        retuns the number of moves for the pokemon 
        '''
        num_moves = len(self.moves)
        return num_moves 

    def choose(self,index):
        '''
        retuns the users move choice for the pokemon 
        '''
        try: 
            choice = self.moves[index]
            return choice 
        except:
            return None 

        
    def show_move_elements(self):
        '''
        displays the move elemnts of the pokemon 
        '''
        string = ''
        for move in self.moves:
            #move = str(move)
            string = string + '{:<15}'.format(move.get_element()) 
            
        print(string)


    def show_move_power(self):
        '''
        displays the move power of the pokemon 
        '''
        string = ''
        for move in self.moves:
            #move = str(move)
            string = string + '{:<15}'.format(move.get_power()) 
            
        print(string)

    def show_move_accuracy(self):
        '''
        displauys the accuracy of the pokemons move accuracies
        '''
        string = ''
        for move in self.moves:
            #move = str(move)
            string = string + '{:<15}'.format(move.get_accuracy()) 
            
        print(string)
        
        
    def add_move(self, move):
        '''
        adds moves to the pokemons list of moves 
        '''
        if len(self.moves) <= 3: 
            self.moves.append(move)
            
    def subtract_hp(self,damage):
        '''
        subratcts the damage from the pokemons hp
        '''
        self.hp = self.hp - damage 
        if self.hp < 0: 
            self.hp = 0 
            
        
    def attack(self, move, opponent):
        '''
        this is where the damage of a move on the other pokemon 
        is calculated 
        '''
        mp = move.get_power()
        at = move.get_attack_type()
        if at ==2 or at == 3: 
            
            if at == 2: 
                A = self.get_patt()
                D = opponent.get_pdef()
            elif at == 3:
                A = self.get_satt()
                D = opponent.get_sdef()
                
            acc_att = move.get_accuracy()
            rando = randint(0,100)
            if rando > acc_att: 
                print('Move missed!')
                return
            else: 
                mod = 1.0 
                move_el = move.get_element()
                
                #for opponents first element 
                opp_el1 = opponent.get_element1() 
                if opp_el1 in is_effective_dictionary[move_el]:
                    mod *= 2 
                    damage_b = True 
                elif opp_el1 in not_effective_dictionary[move_el]:
                    mod *= .5
                    damage_b = True 
                elif opp_el1 in no_effect_dictionary[move_el]:
                    #mod = 0 
                    damage_b = False 
                    return
                else: 
                    damage_b = True
                    
                #for opponents second element 
                opp_el2 = opponent.get_element2() 
                if opp_el2 in is_effective_dictionary[move_el]:
                    mod *= 2 
                    damage_b = True 
                elif opp_el2 in not_effective_dictionary[move_el]:
                    mod *= .5
                    damage_b = True 
                elif opp_el2 in no_effect_dictionary[move_el]:
                    #mod = 0 
                    damage_b = False 
                    return
                else: 
                    damage_b = True 
                        
                if mod > 1:
                    print("It's super effective!!!!")
                elif mod < 1: 
                    print('Not very effective...')
                       
                
                #STAB 
                if move_el ==  self.get_element1() or move_el == self.get_element2():
                    mod *= 1.5
                 
                if damage_b == True:
                    ad = A/D
                    top = mp * ad * 20 
                    top = top / 50 
                    damage = (top + 2) * mod
                    damage = int(damage)
                    opponent.subtract_hp(damage)
            
        else: 
            print('Invalid attack_type, turn skipped.')
            return
            
            

    

        
