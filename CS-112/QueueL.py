
Queue = []

choice = 0
while choice !=  5 :
    print("\nWhat do you want to do?")
    print(" 1. Add an item to the end of the queue")
    print(" 2. Remove first item in queue")
    print(" 3. Print out queue")
    print(" 4. Display length of queue")
    print(" 5. Exit")
    choice = int(input(" Choice: "))
    if choice == 1 :
        x = int(input("\n Enter data to add: "))
        Queue.append(x)
        print( x , "added to Queue")
    elif choice == 2 :
        if len(Queue)>0 :
            y = Queue.pop(0)
            print("\n", y , " was removed from Queue")
        else:
            print("\n Queue is empty")
    elif choice == 3 :
         print("\nQueue" , Queue)
    elif choice == 4 :
         print("\nQueue size is ",len(Queue)) 
                 
print("Goodbye")
