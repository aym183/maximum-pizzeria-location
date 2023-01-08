import threading
import numpy as np

class Pizzeria:
    ''' Represents creation of city dimensions, implementing possible moves, and getting final output

    Attributes:
        dimensions_input: User input to create city NxN matrix
        possible_moves: The blocks delivery guy can move to from a given pizzeria
        pizzeria_specs: User input that contains the location of a pizzeria [x,y]
        city_dimension: The built NxN matrix where all transformations take place
        max_pizzerias: Final output that is max number of pizzerias that deliver 
        pizzas to the block with the greatest selection of pizzas
    '''
    def __init__(self, dimensions_input, possible_moves, pizzeria_specs):
        self.dimensions_input = dimensions_input
        self.possible_moves = possible_moves
        self.pizzeria_specs = pizzeria_specs
        self.city_dimension = []
        self.max_pizzerias = 0

    def set_city_dimensions(self):
        ''' Sets city dimensions matrix based on user input

        Args:
            None

        Returns:
            self.city_dimension: The NxN zero filled matrix classed as the city dimension
        '''
        sub_dimension = [0]*self.dimensions_input
        for idx in range(self.dimensions_input):
            self.city_dimension.append(list(sub_dimension))
        return self.city_dimension

    def implement_delivery_moves(self):
        ''' Implements possible moves a delivery guy can make from a pizzeria 
        
        Creates the list in the PossibleMoves class as a fixed nested list and increments those 
        blocks accordingly
        
        Args:
            None

        Returns:
            city_dimension: The updated city dimensions after the increments have been added
            for the pizzeria
        '''
        location_x, location_y = int(self.pizzeria_specs[0]), int(self.pizzeria_specs[1])
        self.possible_moves.append([location_x, location_y])
        for idx in range(len(self.possible_moves)):
            try:
                if ((0 <= self.possible_moves[idx][0] <= self.dimensions_input - 1) and (0 <= self.possible_moves[idx][1] <= self.dimensions_input - 1)):
                    self.city_dimension[self.possible_moves[idx][0]][self.possible_moves[idx][1]] += 1
            except IndexError:
                pass
        return self.city_dimension

    def get_max_pizzerias(self, implemented_moves):
        ''' Concatenates all the city dimensions for all X user inputted pizzerias
        
        Args:
            implemented_moves: contains all the transformed matrices with all
            made moves by the delivery guy from one pizzeria

        Returns:
            self.max_pizzerias: The max number of pizzerias that deliver 
            pizzas to the block with the greatest selection of pizzas
        '''
        output = np.array(implemented_moves).sum(0).tolist()
        for idx in range(len(output)):
            for snd_idx in range(len(output[0])):
                if output[idx][snd_idx] > self.max_pizzerias:
                    self.max_pizzerias = output[idx][snd_idx]
        return self.max_pizzerias


class PossibleMoves:
    ''' Object representing the simulation of all blocks a elivery guy can move to

    Attributes:
        max_delivery_range: User input that shows max distance a delivery guy can travel
        fixed_start_point: User input that contains the fixed location of a pizzeria [x,y]
        var_start_point: user input that contains the same value as fixed_start_point but will be manipulated
        present_pizzeria_outputs: Contains all the possible blocks a delivey guy can go to
        moves_counter: Counter that ensures that all moves are within the max_delivery_range
    '''
    def __init__(self, max_delivery_range, fixed_start_point, var_start_point):
        self.max_delivery_range = max_delivery_range
        self.fixed_start_point = fixed_start_point
        self.var_start_point = var_start_point
        self.present_pizzeria_outputs = []
        self.moves_counter = 0

    def straight_moves(self, type, split):
        ''' Implements all the straight blocks a delivery guy can move to. 

        Args:
            type: Indicates whether delivery guy should go forwards or backwards
            split: Indicates whether delivery guy goes purely in one direction or can make a turn too

        Returns:
            self.present_pizzeria_outputs: List containing all the moves a delivery guy can make
        '''
        for idx in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if split == True:
                    self.var_start_point.reverse()
                    
                if type == "plus":
                    self.var_start_point[0] += 1
                elif type == 'subtract':
                    self.var_start_point[0] -= 1
                self.moves_counter += 1

                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
                self.var_start_point.reverse()
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
       
        self.moves_counter = 0
        self.var_start_point= list(self.fixed_start_point)
        return self.present_pizzeria_outputs
    
    def split_moves(self):
        ''' Implements the non straight blocks that a delivery guy can move to. 
        
        For example, going straight and right.

        Args:
            None

        Returns:
            self.present_pizzeria_outputs: List containing all the moves a delivery guy can make
        '''
        for idx in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if idx%2 == 1:
                    self.var_start_point[0] += 1
                else:
                    self.var_start_point[0] -= 1
                self.moves_counter += 1
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
                self.var_start_point.reverse()
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))

        self.moves_counter = 0    
        self.var_start_point= list(self.fixed_start_point)
        return self.present_pizzeria_outputs

def main():
    ''' Implements the CLI 
    
    Takes the user inputs, creates objects that does the transformations and 
    prints the final output
    '''
    final_dimension = []
    [dimensions, no_of_pizzerias] = input().strip().split(" ")
    if ((0 <= int(dimensions) <= 10000) and (0 <= int(no_of_pizzerias) <= 10000) and (no_of_pizzerias.isdigit() and dimensions.isdigit())):
        pizzeria_specs_input = []
        for idx in range (int(no_of_pizzerias)):
            [pizzeria_location_x, pizzeria_location_y, max_delivery_range] = input().strip().split(" ")
            
            if ((all(n.isdigit() for n in (pizzeria_location_x, pizzeria_location_y, max_delivery_range)))
             and (1 <= int(max_delivery_range) <= 5000) and (all(1 <= int(n) <= int(dimensions) for n in (pizzeria_location_x, pizzeria_location_y)))):
                pizzeria_specs_input.append([pizzeria_location_x, pizzeria_location_y, max_delivery_range])
            else:
                print("Error! Invalid input")
                exit()
        
        for idx in range(len(pizzeria_specs_input)):
            pizzeria_spec_decremented = [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1]
            possible_moves = PossibleMoves(int(pizzeria_specs_input[idx][2]), pizzeria_spec_decremented, pizzeria_spec_decremented)
            # Use of multithreading to go through all possible moves delivery guy can make (forward, backward, right, left) without harming core program performance
            threading.Thread(target = possible_moves.straight_moves, args = ("plus", True)).start()
            threading.Thread(target = possible_moves.straight_moves, args = ("plus", False)).start()
            threading.Thread(target = possible_moves.straight_moves, args = ("subtract", True)).start()
            threading.Thread(target = possible_moves.straight_moves, args = ("subtract", False)).start()
            threading.Thread(target = possible_moves.split_moves).start()

            pizzeria = Pizzeria(int(dimensions), possible_moves.present_pizzeria_outputs, pizzeria_spec_decremented)
            pizzeria.set_city_dimensions()
            pizzeria.implement_delivery_moves()
            final_dimension.append(list(pizzeria.city_dimension))
        print(pizzeria.get_max_pizzerias(final_dimension))
   
    else:
        print("Error! Input limit is 2 and keep within range [0, 10000]")
        exit()

if __name__ == "__main__":
    main()