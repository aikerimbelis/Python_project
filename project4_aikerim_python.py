# MSIT 501 - Project 4.

# Code implemented by: Aikerim Belispayeva


import pickle


class Item:

    def __init__(self, category, desc, value, quant):
        self.category = category
        self.desc = desc
        self.value = value
        self.quant = quant

    def display(self):
        print("{:<30}{:<18}{:8.2f}{:7d}".format(self.desc, self.category, self.value, self.quant))


class Collection:

    def __init__(self):
        self.items = []

    def addItem(self, category, desc, value, quant):
        item = Item(category, desc, value, quant)
        self.items.append(item)

    def displayAllItems(self):
        for Item in self.items:
            print("{:<30s}{:<18s}{:8.2s}{:7s}".format("Description", "Category", "Value", "Amount"))
            print("_" * 70)
            print("{:<30}{:<18}{:8.2f}{:7d}".format(Item.desc, Item.category, Item.value, Item.quant))

    def displayAllCategories(self):
        for Item in self.items:
            for Item.category in self.items:
                print("Categories")
                print("_" * 20)
                print(Item.category)

    def displayAllItemsForCategory(self, category):
        category = input("Enter category: ").strip()
        for Item in self.items:
            if category not in Item.category:
                print("Category not found")
            else:
                print("Items for category:", category)
                print("{:<30s}{:<18s}{:8.2s}{:7s}".format("Description", "Category", "Value", "Amount"))
                print(("{:<30}{:<18}{:8.2f}{:7d}".format(Item.desc, Item.category, Item.value, Item.quant)))

    def displayItemsOverValue(self, value):
        value = eval(input("Enter the value: "))
        for Item in self.items:
            if Item.value >= value:
                print("Items over $", value )
                print(f"{'Description':<30s}{'Category':<18s}{'Value':8.2s}{'Amount':7s}")
                print(("{:<30}{:<18}{:8.2f}{:7d}".format(Item.desc, Item.category, Item.value, Item.quant)))

    def displayItemFromDescription(self, desc):
        itemToFind = input("Enter item's description: ").strip()
        for Item in self.items:
            if itemToFind in Item.desc:
                print("{:<30s}{:<18s}{:8.2s}{:7s}".format("Description", "Category", "Value", "Amount"))
                print(("{:<30}{:<18}{:8.2f}{:7d}".format(Item.desc, Item.category, Item.value, Item.quant)))
            else:
                print("No item found")

    def displayCollectionValue(self):
        val = 0
        for Item in self.items:
            val = val + Item.value * Item.quant
            print("Collection Value: $", val)


def printMenu():
    print("")
    print("1. Display all items in my collection")
    print("2. Display all categories of my items")
    print("3. Display all items in a given category")
    print("4. Search for an item by description")
    print("5. Add an new item to my collection")
    print("6. Display all items above a given value")
    print("7. Calculate the total value of my collection")
    print("S. Save to disk")
    print("L. Load data from disk")
    print("Q. Quit")
    print()


def main():
    stuff = Collection()
    print()
    print('Welcome to my Collection Manager')
    while True:
        printMenu()
        selection = input("Please enter a selection: ").strip().upper()
        if selection not in ['1', '2', '3', '4', '5', '6', '7', 'S', 'L', 'Q']:
            print("Please enter a valid choice...")
            continue
        if selection == '1':
            stuff.displayAllItems()
        elif selection == '2':
            stuff.displayAllCategories()
        elif selection == '3':
            category = input("Enter category: ").strip()
            stuff.displayAllItemsForCategory(category)
        elif selection == '4':
            itemToFind = input("Enter item's description: ").strip()
            stuff.displayItemFromDescription(itemToFind)
        elif selection == '5':
            cat = input("Enter the item's category: ").strip()
            desc = input("Enter the item's description: ").strip()
            value = eval(input("Enter the item's value: "))
            quant = eval(input("Enter the item's quantity: "))
            stuff.addItem(cat, desc, value, quant)
            print("Item added")
        elif selection == '6':
            value = eval(input("Enter the value: "))
            stuff.displayItemsOverValue(value)
        elif selection == '7':
            stuff.displayCollectionValue()
        elif selection == 'S':
            pickle.dump(stuff, open("stuff.p", "wb"))
            print("Data saved...")
        elif selection == 'L':
            stuff = pickle.load(open("stuff.p", "rb"))
            print("Data loaded...")
        else:
            print("Thanks for using my Collection Manager")
            break


if __name__ == "__main__":
    main()