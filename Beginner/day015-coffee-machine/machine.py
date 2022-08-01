import data

class Machine():
    
    def __init__(self):
        self.menu = data.menu.copy()
        self.ingredients = data.ingredients.copy()
        self.stored_funds = 10.00

    def get_product_cost(self, product_name):
        return self.menu[product_name]["cost"]
    
    def order(self, product_name):
        product = self.menu[product_name]
        self.manage_ingredients(product)
        self.stored_funds += self.get_product_cost(product_name)

    def manage_ingredients(self, product):
        list(product.keys())[0]
        ingredient_list = list(product["ingredients"].keys())
        for ingredient in ingredient_list:
            self.have_enough(product, ingredient)
            self.update_stock(product, ingredient)

    def have_enough(self, product, ingredient):
        if product["ingredients"][ingredient] > self.ingredients[ingredient]:
            raise InadequateIngredientsException("Inadequate ingredients.")

    def update_stock(self, product, ingredient):
        self.ingredients[ingredient] -= product["ingredients"][ingredient]  

class InadequateIngredientsException(Exception):
    def __init__(self, *args):
        super().__init__(args)
        self.message = args[0]