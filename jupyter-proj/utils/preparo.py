

class Preparo:

    def __init__(self):
        self.ingredients_bought = False
        self.ingredients_meat_stew = []
        self.slow_cook_oven = False
        self.cooked = False
        self.ingredients_pirao = []
        self.quality_meat = ""
        self.type_meat=""
        self.good = False

    def buy_ingredients(self):
        self.ingredients_meat_stew = ['chives', 'salt', 'laurel', 'pepper','vegetables']
        self.ingredients_pirao = ['salt','mandioca', 'stew_sauce']
        self.quality_meat = "high"
        self.type_meat="chambaril"
        self.ingredients_bought = True

    def to_cook(self):
        if self.ingredients_bought == True:
            self.slow_cook_oven = True
            self.cooked = True

    def avaliar(self):
        if len(self.ingredients_meat_stew) < 5:
            print("falta ingredientes para a carne")

        elif (self.slow_cook_oven == False):
            print("carne dura")

        elif self.ingredients_pirao != ['salt','mandioca', 'stew_sauce']:
            print("estão inventando a receita do pirão")

        elif self.quality_meat != "high":
            print("carne ruim")

        elif self.type_meat != "chambaril":
            print("é apenas um cozido normal")

        elif self.ingredients_bought == False:
            print("não fizeram compras")

        else:
            self.good = True
            print("o prato está bom")

    def do_a_chambaril(self):   
        self.buy_ingredients()
        self.to_cook()
        self.avaliar()
        if self.good == True:
            return("pode servir")
