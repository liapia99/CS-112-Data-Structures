#Julia Piascik

class Node:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None
#-------------------------- Add Product ------------------
    def add_product(self, name, price, stock):
            new_node = Node(name, price, stock)
            new_node.ref = self.start_node
            self.start_node = new_node

#-------------------------- Print All Products ------------------
    def print_products(self):
       if self.start_node is None:
            print("No products in the list.")
            return
       else:
            current_product = self.start_node
            while current_product is not None:
                print("Product:", current_product.name, "Price:", current_product.price, "Stock:", current_product.stock)
                current_product = current_product.ref
       print(" ")
#-------------------------- Products Above Price ------------------
    def print_products_above_price(self, price):
        if self.start_node is None:
            print("No products in the list.")
            return
        else:
            current_product = self.start_node
            while current_product is not None:
                if current_product.price > price:
                    print("Product:", current_product.name, "Price:", current_product.price, "Stock:", current_product.stock)
                    current_product = current_product.ref
                else:
                    print("No products in the list.")
                    return
                    
        print(" ")  
#-------------------------- Low Stock Products ------------------
    def print_low_stock_products(self):
        if self.start_node is None:
            print("No products in the list.")
            return
        else:
            current_product = self.start_node
            while current_product is not None:
                if current_product.stock < 20:
                    print("Product:", current_product.name, "Price:", current_product.price, "Stock:", current_product.stock)
                    current_product = current_product.ref
        print(" ")  

# --------------- MAIN ---------------------
product_list = LinkedList()

choice = 0
while choice != 5:
    # Prompt user for action
    
    print("1. Add a product")
    print("2. Print all products")
    print("3. Print products above a certain price")
    print("4. Print low-stock products")
    print("5. Exit")
    choice = int(input("\n Enter Choice: "))

  
    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        product_list.add_product(name, price, stock)
        print("Product added.\n")

    elif choice == 2:
        product_list.print_products()

    elif choice == 3:
        price = float(input("Enter minimum price: "))
        product_list.print_products_above_price(price)

    elif choice == 4:
        product_list.print_low_stock_products()


    
print("Goodbye.")
