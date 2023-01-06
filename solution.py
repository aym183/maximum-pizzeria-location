import threading
from time import sleep
class Pizzeria:
    def __init__(self, dimensions_input, no_of_pizzerias, pizzeria_specs, possible_moves):
        self.dimensions_input = dimensions_input
        self.no_of_pizzerias = no_of_pizzerias
        self.pizzeria_specs = pizzeria_specs
        self.possible_moves = possible_moves
        self.city_dimension = []
        self.max_pizzerias = 0

    def set_city_dimensions(self):
        sub_dimension = [0]*self.dimensions_input
        for idx in range(self.dimensions_input):
            self.city_dimension.append(sub_dimension)

    def get_max_pizzerias(self):
        location_x, location_y = int(self.pizzeria_specs[0][0])-1, int(self.pizzeria_specs[0][1])-1
        print(location_x, location_y)
        valid_moves = []
        for idx in range(len(self.possible_moves)):
            after_move_x, after_move_y = location_x + self.possible_moves[idx][0], location_y + self.possible_moves[idx][1]

            # if ((after_move_x >= 0) and (after_move_x <= self.dimensions_input - 1)) and ((after_move_y >= 0) and (after_move_y <= self.dimensions_input - 1)):
            valid_moves.append([after_move_x, after_move_y])
        print(valid_moves)
        

            
    
class PossibleMoves:
    def __init__(self, max_delivery_range):
        self.max_delivery_range = max_delivery_range
        self.start_point = [3,3]
        self.outputs = []
        self.moves_counter = 0

    def straight_moves(self, type, split):
        print(self.moves_counter)
        for i in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if split == 'No':
                    self.start_point.reverse()
                
                if type == "plus":
                    self.start_point[0] += 1
                elif type == 'subtract':
                    self.start_point[0] -= 1
                self.moves_counter+= 1

                if self.start_point not in self.outputs:
                    self.outputs.append(list(self.start_point))
                self.start_point.reverse()
                if self.start_point not in self.outputs:
                    self.outputs.append(list(self.start_point))
            
        # print(self.outputs)
        self.moves_counter = 0
        self.start_point= [3,3]    
    
    def split_moves(self):
        print(self.moves_counter)
        for i in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if i%2 == 1:
                    self.start_point[0] += 1
                else:
                    self.start_point[0] -= 1
                self.moves_counter+= 1
                if self.start_point not in self.outputs:
                    self.outputs.append(list(self.start_point))
                self.start_point.reverse()
                if self.start_point not in self.outputs:
                    self.outputs.append(list(self.start_point))
        # print(self.outputs)
        self.moves_counter = 0    
        self.start_point= [3,3]    

    


if __name__ == "__main__":
    
    # create_class.split_moves()
    

    first_input = input().split(" ")
    pizzeria_specs = []
    for i in range (int(first_input[1])):
        pizzeria_inputs = input(" ").split(" ")
        pizzeria_specs.append(pizzeria_inputs)
    
    create_class = PossibleMoves(int(pizzeria_specs[0][2]))

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
    # create_class.straight_moves("plus", "No")
    # create_class.straight_moves("plus", "Yes")
    # create_class.straight_moves("subtract", "Yes")
    # create_class.straight_moves("subtract", "No")
    # create_class.split_moves()
    print(create_class.outputs)

    # create_pizzeria_class = Pizzeria(int(first_input[0]), int(first_input[1]), pizzeria_specs, create_class.outputs)
    # create_pizzeria_class.set_city_dimensions()
    # # print(create_class.city_dimension)
    # # create_pizzeria_class.set_max_delivery_range(pizzeria_specs[0])
    # create_pizzeria_class.get_max_pizzerias()
