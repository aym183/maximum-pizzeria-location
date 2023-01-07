import threading
from time import sleep
import numpy as np
'''UNIT TESTS'''

'''
The Pizzeria class does the following:
(i) Create the base NxN matrix based on city dimension inputs
(ii) Implement all the possible blocks the delivery guy can go to
(iii) Returns the final output

Inputs: dimensions_input (user input to create city matrix), possible_moves (all the blocks delivery guy can move to), pizzeria_specs (user input, contains the location of a pizzeria [x,y])
Output: self.max_pizzerias (Gets the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas)
'''
class Pizzeria:
    def __init__(self, dimensions_input, possible_moves, pizzeria_specs):
        self.dimensions_input = dimensions_input
        self.possible_moves = possible_moves
        self.pizzeria_specs = pizzeria_specs
        self.city_dimension = []
        self.max_pizzerias = 0

    # The function creates a 0 filled NxN matrix for the dimension of the city where N is the user input 
    def set_city_dimensions(self):
        sub_dimension = [0]*self.dimensions_input
        for idx in range(self.dimensions_input):
            self.city_dimension.append(list(sub_dimension))

    # The function takes all the possible moves created in the PossibleMoves class and implements them in the city dimension blocks
    def implement_delivery_moves(self):
        location_x, location_y = int(self.pizzeria_specs[0]), int(self.pizzeria_specs[1])
        self.possible_moves.append([location_x, location_y])
        for idx in range(len(self.possible_moves)):
            try:
                if ((0 <= self.possible_moves[idx][0] <= self.dimensions_input - 1) and (0 <= self.possible_moves[idx][1] <= self.dimensions_input - 1)):
                    self.city_dimension[self.possible_moves[idx][0]][self.possible_moves[idx][1]] += 1
            except IndexError:
                pass

    # The function concats all blocks the delivery guy can move too for each pizzeria and returns the final output (Mentioned above class name)
    def get_max_pizzerias(self, implemented_moves):
        output = np.array(implemented_moves).sum(0).tolist()
        for idx in range(len(output)):
            for snd_idx in range(len(output[0])):
                if output[idx][snd_idx] > self.max_pizzerias:
                    self.max_pizzerias = output[idx][snd_idx]
        return self.max_pizzerias

'''
The PossibleMoves class does the following:
It takes the location of a pizzeria and gets all the possible blocks a delivery guy can go to

Inputs: max_delivery_range (user input that shows max distance a delivery guy can travel), fixed_start_point (user input that contains the fixed location of a pizzeria [x,y], var_start_point (user input that contains the same value as fixed_start_point but will be manipulated))
Output: present_pizz_outputs (Contains all the possible blocks a delivey guy can go to)
'''
class PossibleMoves:
    def __init__(self, max_delivery_range, fixed_start_point, var_start_point):
        self.max_delivery_range = max_delivery_range
        self.fixed_start_point = fixed_start_point
        self.var_start_point = var_start_point
        self.present_pizz_outputs = []
        self.moves_counter = 0

    # The function implements all the straight blocks a delivery guy can move to. It stores all the reverse outputs as its more efficient than doing calculations again
    def straight_moves(self, type, split):
        for i in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if split == 'No':
                    self.var_start_point.reverse()
                    
                if type == "plus":
                    self.var_start_point[0] += 1
                elif type == 'subtract':
                    self.var_start_point[0] -= 1
                self.moves_counter+= 1

                if self.var_start_point not in self.present_pizz_outputs:
                    self.present_pizz_outputs.append(list(self.var_start_point))
                self.var_start_point.reverse()
                if self.var_start_point not in self.present_pizz_outputs:
                    self.present_pizz_outputs.append(list(self.var_start_point))
       
        self.moves_counter = 0
        self.var_start_point= list(self.fixed_start_point)
    
    # The function implements the non straight blocks that a delivery guy can move to, for example, going straight and right.
    def split_moves(self):
        for i in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if i%2 == 1:
                    self.var_start_point[0] += 1
                else:
                    self.var_start_point[0] -= 1
                self.moves_counter+= 1
                if self.var_start_point not in self.present_pizz_outputs:
                    self.present_pizz_outputs.append(list(self.var_start_point))
                self.var_start_point.reverse()
                if self.var_start_point not in self.present_pizz_outputs:
                    self.present_pizz_outputs.append(list(self.var_start_point))

        self.moves_counter = 0    
        self.var_start_point= list(self.fixed_start_point)

'''
Contains the main part of the program that:
(i) Takes the user input and undergo error handling
(ii) Create the relevant objects, calling relevant methods
(iii) Call the method to return the final output
'''
if __name__ == "__main__":

    final_dimension = []
    first_input = input().strip().split(" ")
    if (len(first_input) == 2) and ((0 <= int(first_input[0]) <= 10000) and (0 <= int(first_input[1]) <= 10000)):
        pizzeria_specs_input = []
        for i in range (int(first_input[1])):
            pizzeria_inputs = input().strip().split(" ")
            if (len(pizzeria_inputs) == 3) and (1 <= int(pizzeria_inputs[0]) <= int(first_input[0])) and (1 <= int(pizzeria_inputs[1]) <= int(first_input[0])) and (1 <= int(pizzeria_inputs[2]) <= 5000):
                pizzeria_specs_input.append(pizzeria_inputs)
            else:
                print("Error! Invalid input")
                exit()
                
        for idx in range(len(pizzeria_specs_input)):
            create_class = PossibleMoves(int(pizzeria_specs_input[idx][2]), [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1], [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1])
            T1 =  threading.Thread(target=create_class.straight_moves, args = ("plus", "No"))
            T2 =  threading.Thread(target=create_class.straight_moves, args = ("plus", "Yes"))
            T3 =  threading.Thread(target=create_class.straight_moves, args = ("subtract", "Yes"))
            T4 =  threading.Thread(target=create_class.straight_moves, args = ("subtract", "No"))
            T5 =  threading.Thread(target=create_class.split_moves)
            T1.start()
            T2.start()
            T3.start()
            T4.start()
            T5.start()
            pizzeria_class = Pizzeria(int(first_input[0]), create_class.present_pizz_outputs, [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1])
            pizzeria_class.set_city_dimensions()
            pizzeria_class.implement_delivery_moves()
            final_dimension.append(list(pizzeria_class.city_dimension))
        print(pizzeria_class.get_max_pizzerias(final_dimension))
   
    else:
        print("Error! Input limit is 2 and keep within range [0, 10000]")
        exit()