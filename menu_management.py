class MenuManagement:
    menu = []

    def AddToMenu(self):
        item = input("Enter The Name Of The Item You Want To Add = ")
        self.menu.append(item)
        print("==========Available Items In The Menu==========")
        for index, name in enumerate(self.menu, start=1):
            print(f"{index}. {name}")

    def DeleteFromMenu(self):
        print("=======Available Items In Menu Are=======")
        for index, name in enumerate(self.menu, start=1):
            print(f"{index}. {name}")
        itemsToRemove = input("Enter The Name Of The Item You Want To Delete = ")
        if itemsToRemove in self.menu:
            self.menu.remove(itemsToRemove)
            print(f"{itemsToRemove} has been removed from the menu.")
        else:
            print(f"{itemsToRemove} not found in the menu.")

    def CheckMenuAvailableOrNot(self):
        checkMenuItem = input("Enter the item name to check if it's in the menu or Not = ")
        if checkMenuItem in self.menu:
            print(f"{checkMenuItem} is available in the menu.")
        else:
            print(f"{checkMenuItem} is not available in the menu.")

    def ViewMenu(self):
        print("==========Available Items In The Menu==========")
        for index, name in enumerate(self.menu, start=1):
            print(f"{index}. {name}")
    def End(self):
        print("==========Available Items In The Menu==========")
        for index, name in enumerate(self.menu, start=1):
            print(f"{index}. {name}")
        exit()

    def ViewOptions(self):
        print("1.View Menu.")
        print("2.Add Items To Menu.")
        print("3.Remove Items From The Menu.")
        print("4.Check if Item is in menu or Not.")
        print("5.End")
        operation = int("Enter The operation To Perform = ")

menu = MenuManagement()
