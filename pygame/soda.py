class Soda:
    def __init__(self,topping=None):
        self.topping = topping
    def show_my_drink(self):
        if self.topping == "" or self.topping == None:
            print("soda")
        else:
            print("soda with {}".format(self.topping))

coca_cola = Soda("apple")
no_topping = Soda()

coca_cola.show_my_drink()
no_topping.show_my_drink()