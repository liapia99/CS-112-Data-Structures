class Node:
     def __init__(self, data):
         self.item = data
         self.ref = None

class Queue:
     # ---------------Create an empty Queue -------------
     
     def __init__(self):
         self.first = None
         self.last = None
         
     # --------------- Traverse the Queue  ----------------------
     
     def traverse_list(self):
         print("Queue: ", end = " ")
         if self.first is None:
             print("Queue is empty")
             return
         else:
             n = self.first
             while n is not None:
                 print(n.item, end =" " )
                 n = n.ref
         print(" ")        
                 
    #  ------------- Add to the end ----------------------
    
     def Add(self, data):
            new_node = Node(data)
            if self.first is None:
                 self.first = new_node
                 self.last = new_node
                 return
            self.last.ref = new_node
            self.last = new_node
     
   # -------------- Pop  ------------------

     def Remove(self):
            if self.first is None:
                print("Queue is empty!")
                return
            x = self.first.item
            if (self.first==self.last):
                self.last = None
            self.first = self.first.ref
            return x
# ---------------------- Main ----------
        
My_Queue = Queue()

choice = 0
while choice != 4:
    print("\n Queue Demo, what do you want to do?")
    print(" 1 = Add to the end ")
    print(" 2 = Remove the first node ")
    print(" 3 = Print Queue")
    print(" 4 = Exit ")
    choice = int(input("\n Enter Choice: "))

    if choice==1:
        num = int(input("\n Enter number to add: "))
        My_Queue.Add(num)
        print( num , " added to queue")
    elif choice==2:
        x = My_Queue.Remove()
        print(x,  " was removed ")
    elif choice==3:
        My_Queue.traverse_list()
       
print("\n Goodbye \n")
