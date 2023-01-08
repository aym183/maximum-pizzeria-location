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
    def __init__(self, dimensions_input: int, possible_moves: list[list[int, int]], pizzeria_specs: list[int, int]):
        self.dimensions_input = dimensions_input
        self.possible_moves = possible_moves
        self.pizzeria_specs = pizzeria_specs
        self.city_dimension = []
        self.max_pizzerias = 0

    def set_city_dimensions(self) -> list[list[int, int]]:
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

    def implement_delivery_moves(self) -> list[list[int, int]]:
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
        completed_moves = []
        for idx in range(len(self.possible_moves)):
            try:
                # ((0 <= self.possible_moves[idx][0] <= self.dimensions_input - 1) and (0 <= self.possible_moves[idx][1] <= self.dimensions_input - 1)):
                if (self.possible_moves[idx] not in completed_moves) and all(0 <= int(n) <= self.dimensions_input - 1 for n in (self.possible_moves[idx][0], self.possible_moves[idx][1])):
                    self.city_dimension[self.possible_moves[idx][0]][self.possible_moves[idx][1]] += 1
                    completed_moves.append(self.possible_moves[idx])
            except IndexError:
                pass
        return self.city_dimension
         
    def get_max_pizzerias(self, implemented_moves: list[list[int, int]]) -> int:
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
    def __init__(self, max_delivery_range: int, fixed_start_point: list[int, int], var_start_point: list[int, int]):
        self.max_delivery_range = max_delivery_range
        self.fixed_start_point = fixed_start_point
        self.var_start_point = var_start_point
        self.present_pizzeria_outputs = []
        self.moves_counter = 0

    def straight_moves(self, type: str, split: str):
        ''' Implements all the straight blocks a delivery guy can move to. 

        Args:
            type: Indicates whether delivery guy should go forwards or backwards
            split: Indicates whether delivery guy goes purely in one direction or can make a turn too

        Returns:
            self.present_pizzeria_outputs: List containing all the moves a delivery guy can make
        '''
        for idx in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if split == 'No':
                    self.var_start_point.reverse()
                    
                if type == "plus":
                    self.var_start_point[0] += 1
                elif type == 'subtract':
                    self.var_start_point[0] -= 1
                self.moves_counter+= 1
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
                self.var_start_point.reverse()
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
       
        self.moves_counter = 0
        self.var_start_point= list(self.fixed_start_point)
    
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
                self.moves_counter+= 1
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
                self.var_start_point.reverse()
                if self.var_start_point not in self.present_pizzeria_outputs:
                    self.present_pizzeria_outputs.append(list(self.var_start_point))
                    
        self.moves_counter = 0    
        self.var_start_point= list(self.fixed_start_point)
    
def main():
    ''' Implements the CLI 
    
    Takes the user inputs, creates objects that does the transformations and 
    prints the final output
    '''
    final_dimension = []
    [dimensions, no_of_pizzerias] = input().strip().split(" ")
    if ((no_of_pizzerias.isdigit() and dimensions.isdigit()) and ((0 <= int(dimensions) <= 10000) and (0 <= int(no_of_pizzerias) <= 10000))):
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
            possible_moves = PossibleMoves(int(pizzeria_specs_input[idx][2]), [int(pizzeria_specs_input[idx][0]) - 1, 
            int(pizzeria_specs_input[idx][1]) - 1], [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1])
            threading.Thread(target = possible_moves.straight_moves, args = ("plus", "No")).start()
            threading.Thread(target = possible_moves.straight_moves, args = ("plus", "Yes")).start()
            threading.Thread(target = possible_moves.straight_moves, args = ("subtract", "Yes")).start()
            threading.Thread(target = possible_moves.straight_moves, args = ("subtract", "No")).start()
            threading.Thread(target = possible_moves.split_moves).start()
            pizzeria = Pizzeria(int(dimensions), possible_moves.present_pizzeria_outputs, 
            [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1])
            pizzeria.set_city_dimensions()
            pizzeria.implement_delivery_moves()
            final_dimension.append(list(pizzeria.city_dimension))
    
        pizzeria.get_max_pizzerias(final_dimension)
        print(pizzeria.max_pizzerias)
    else:
        print("Error! Input limit is 2 and keep within range [0, 10000]")
        exit()

if __name__ == "__main__":
    main()
