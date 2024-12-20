class Ecommerce:
    Cart = {}
    total = 0

    def AddCard(self):
        newCart = input("Enter the Cart Name You Wantt to Add = ")
        newCartPrice = int(input(f"Enter cost of {newCart} = "))
        self.Cart[newCart] = newCartPrice

    def DeleteCart(self):
        print(self.Cart)
        deleteCartName = input("Enter the Cart Name You Want To delete = ")
        if deleteCartName in self.Cart:
            del self.Cart[deleteCartName]
        else:
            print("Item not found in the cart.")

    def ViewCartItemsCost(self):
        print("_______________________")
        print("Your Cart Items Are")
        for key, value in self.Cart.items():
            print(f"{key} = {value}")
        self.total = sum(value for value in self.Cart.values() if value >= 0)
        if len(self.Cart) >= 5:
            discount = self.total * 0.10
            discounted_total = self.total - discount
            print(f"Total Cost Of Shopping is = {self.total}")
            print(f"Discount Applied (10%) = {discount}")
            print(f"Total Cost After Discount = {discounted_total}")
        else:
            print(f"Total Cost Of Shopping is = {self.total}")
        print("_______________________")

    def End(self):
        print("==========Thank you Visit Again==========")
        print("Your Purchased Items Are")
        for key, value in self.Cart.items():
            print(f"{key} = {value}")
        self.total = sum(value for value in self.Cart.values() if value >= 0)
        if len(self.Cart) >= 5:
            discount = self.total * 0.10
            discounted_total = self.total - discount
            print(f"Total Cost Of Shopping is = {self.total}")
            print(f"Discount Applied (10%) = {discount}")
            print(f"Total Cost After Discount = {discounted_total}")
        else:
            print(f"Total Cost Of Shopping is = {self.total}")
        exit()

    def ViewOptions(self):
        while True:
            try:
                print("================================")
                print("1.To Add Items Into Cart.")
                print("2.To Delete Items From Cart.")
                print("3.To View Cart Items & Cost of Each.")
                print("4.End of Shopping.")
                print("================================")
                operation = int(input("Enter Option = "))
                match operation:
                    case 1:
                        self.AddCard()
                    case 2:
                        self.DeleteCart()
                    case 3:
                        self.ViewCartItemsCost()
                    case 4:
                        self.End()
                    case _:
                        print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")

object = Ecommerce()
object.ViewOptions()
