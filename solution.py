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


