class Ecommerce:
    Cart ={}
    def AddCard(self):
        newCart=input("Enter the Cart Name You Want to Add = ")
        newCartPrice = int(input(f"Enter cost of {newCart} = "))
        self.Cart [newCart] = newCartPrice
        print(self.Cart)

    def DeleteCart(self):
        print(self.Cart)
        deleteCartName=input("Enter the Cart Name You Want To delete = ")
        del self.Cart [deleteCartName]

    def TotalPrice(self):
        total = sum(value for value in self.Cart.values() if value >= 0)
        print(total)


object = Ecommerce()
object.AddCard()
object.TotalPrice()
