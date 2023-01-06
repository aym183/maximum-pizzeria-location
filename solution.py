class Pizzeria:
    def __init__(self, dimensions_input, no_of_pizzerias, pizzeria_specs):
        self.dimensions_input = dimensions_input
        self.no_of_pizzerias = no_of_pizzerias
        self.pizzeria_specs = pizzeria_specs
        self.city_dimension = []
        self.max_pizzerias = 0

    def set_city_dimensions(self):
        sub_dimension = [0]*self.dimensions_input
        for i in range(self.dimensions_input):
            self.city_dimension.append(sub_dimension)


if __name__ == "__main__":
    
    first_input = input()
    first_input = first_input.split(" ")
    pizzeria_specs = []
    for i in range (int(first_input[1])):
        pizzeria_inputs = input(" ")
        pizzeria_specs.append(pizzeria_inputs.split(" "))

    create_class = Pizzeria(int(first_input[0]), int(first_input[1]), pizzeria_specs)
    create_class.set_city_dimensions()
    print(create_class.city_dimension)