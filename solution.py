import threading
from time import sleep
import numpy as np
''' DO ERROR HANDLING, UNIT TESTS, COMMENTS '''
class Pizzeria:
    def __init__(self, dimensions_input, possible_moves, pizzeria_specs):
        self.dimensions_input = dimensions_input
        self.possible_moves = possible_moves
        self.pizzeria_specs = pizzeria_specs
        self.city_dimension = []
        self.max_pizzerias = 0

    def set_city_dimensions(self):
        sub_dimension = [0]*self.dimensions_input
        for idx in range(self.dimensions_input):
            self.city_dimension.append(list(sub_dimension))

    def implement_delivery_moves(self):
        location_x, location_y = int(self.pizzeria_specs[0]), int(self.pizzeria_specs[1])
        self.possible_moves.append([location_x, location_y])
        for idx in range(len(self.possible_moves)):
            try:
                if ((0 <= self.possible_moves[idx][0] <= self.dimensions_input - 1) and (0 <= self.possible_moves[idx][1] <= self.dimensions_input - 1)):
                    self.city_dimension[self.possible_moves[idx][0]][self.possible_moves[idx][1]] += 1
            
            except IndexError:
                pass
         
    def get_max_pizzerias(self, implemented_moves):
        output = np.array(implemented_moves).sum(0).tolist()
        for idx in range(len(output)):
            for snd_idx in range(len(output[0])):
                if output[idx][snd_idx] > self.max_pizzerias:
                    self.max_pizzerias = output[idx][snd_idx]
        # return self.max_pizzerias


    
class PossibleMoves:
    def __init__(self, max_delivery_range, fixed_start_point, var_start_point):
        self.max_delivery_range = max_delivery_range
        self.fixed_start_point = fixed_start_point
        self.var_start_point = var_start_point
        self.present_pizz_outputs = []
        self.moves_counter = 0

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
            sleep(0.2)
            T2.start()
            sleep(0.2)
            T3.start()
            sleep(0.2)
            T4.start()
            sleep(0.2)
            T5.start()
            sleep(0.2)
            # print(create_class.present_pizz_outputs)
            pizzeria_class = Pizzeria(int(first_input[0]), create_class.present_pizz_outputs, [int(pizzeria_specs_input[idx][0]) - 1, int(pizzeria_specs_input[idx][1]) - 1])
            pizzeria_class.set_city_dimensions()
            pizzeria_class.implement_delivery_moves()
            final_dimension.append(list(pizzeria_class.city_dimension))
        pizzeria_class.get_max_pizzerias(final_dimension)
        print(pizzeria_class.max_pizzerias)
    else:
        print("Error! Input limit is 2 and keep within range [0, 10000]")
        exit()