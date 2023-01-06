class Pizzeria:
    def __init__(self, dimensions_input, no_of_pizzerias, pizzeria_specs):
        self.dimensions_input = dimensions_input
        self.no_of_pizzerias = no_of_pizzerias
        self.pizzeria_specs = pizzeria_specs
        self.city_dimension = []
        self.max_pizzerias = 0

    def set_city_dimensions(self):
        sub_dimension = [0]*self.dimensions_input
        for idx in range(self.dimensions_input):
            self.city_dimension.append(sub_dimension)

    def set_max_delivery_range(self, pizzeria_specs_input):
        max_delivery_range = int(pizzeria_specs_input[2])
        location_x, location_y = int(pizzeria_specs_input[0]), int(pizzeria_specs_input[1])
        possible_moves_x, possible_moves_y = [], []
        valid_moves = []
        for idx in range(max_delivery_range+1):
            
            possible_moves_x.append(location_x + idx) 
            possible_moves_x.append(location_x - idx) 
            possible_moves_y.append(location_y + idx) 
            possible_moves_y.append(location_y - idx) 
        
        list(set(possible_moves_x))
        list(set(possible_moves_y))
        
        for idx in range(len(possible_moves_x)):
            for snd_idx in range(len(possible_moves_y)):
                if (possible_moves_x[idx] >= location_x)  and  (possible_moves_y[snd_idx] <= location_y):
                    valid_moves.append([possible_moves_x[idx], possible_moves_y[snd_idx]])
        print(valid_moves)

    
class PossibleMoves:
    def __init__(self, max_delivery_range):
        self.max_delivery_range = max_delivery_range
        self.start_point = [0,0]
        self.outputs = []
        self.moves_counter = 0

    def straight_moves(self, type, split):
        for i in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if split == 'No':
                    self.start_point.reverse()
                
                if type == "plus":
                    self.start_point[0] += 1
                elif type == 'subtract':
                    self.start_point[0] -= 1
                self.moves_counter+= 1
                self.outputs.append(list(self.start_point))
                self.start_point.reverse()
                self.outputs.append(list(self.start_point))
            
        # print(self.outputs)
        self.moves_counter = 0
            
    
    def split_moves(self):
        for i in range(1, self.max_delivery_range+1):
            if self.moves_counter != self.max_delivery_range:
                if i%2 == 1:
                    self.start_point[0] += 1
                else:
                    self.start_point[0] -= 1
                self.moves_counter+= 1
                self.outputs.append(list(self.start_point))
                self.start_point.reverse()
                self.outputs.append(list(self.start_point))
 
        # print(self.outputs)
        self.moves_counter = 0        

    # def split_moves(self, type):
    #     for i in range(1, self.max_delivery_range+1):
    #         if self.moves_counter != self.max_delivery_range:
    #             if type == "plus":
    #                 self.start_point[0] += 1
    #             elif type == 'subtract':
    #                 self.start_point[0] -= 1
    #             self.moves_counter+= 1
    #             self.outputs.append(list(self.start_point))
    #             self.start_point.reverse()
    #             self.outputs.append(list(self.start_point))
            
    #         print(set(self.outputs)
    #         self.moves_counter = 0   



    
    # def forward_moves(self, max_range):

        
    # def get_max_pizzerias(self):
    #     
        
    #     possible_moves
    #     self.city_dimension[location_x, location_y] += 1


if __name__ == "__main__":
    create_class = PossibleMoves(3)
    create_class.straight_moves("plus", "No")
    create_class.straight_moves("subtract", "No")
    create_class.straight_moves("plus", "Yes")
    create_class.straight_moves("subtract", "Yes")
    print(create_class.outputs)
    # create_class.split_moves()
    

    # first_input = input().split(" ")
    # pizzeria_specs = []
    # for i in range (int(first_input[1])):
    #     pizzeria_inputs = input(" ").split(" ")
    #     pizzeria_specs.append(pizzeria_inputs)

    # create_class = Pizzeria(int(first_input[0]), int(first_input[1]), pizzeria_specs)
    # # create_class.set_city_dimensions()
    # # print(create_class.city_dimension)
    # create_class.set_max_delivery_range(pizzeria_specs[0])
