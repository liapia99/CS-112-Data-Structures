
#Julia Piascik

class Node:
    def __init__(self, name, solvedp, time):
        self.name = name
        self.solvedp = solvedp
        self.time = time
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None
#-------------------------- Add New Team ------------------
    def add_team(self, name, solvedp, time):
            new_node = Node(name, solvedp, time)
            new_node.ref = self.start_node
            self.start_node = new_node

#-------------------------- Print All Teams ------------------
    def print_teams(self):
       if self.start_node is None:
            print("No teams in the list.")
            return
       else:
            current_team = self.start_node
            while current_team is not None:
                print("Team Name:", current_team.name, "Number of problems solved:", current_team.solvedp, "Time taken in minutes:", current_team.time)
                current_team = current_team.ref
       print(" ")
#-------------------------- Teams that Solved More Than 3 Problems ------------------
    def print_teams_above_three(self, solvedp):
        if self.start_node is None:
            print("No teams in the list.")
            return
        else:
            current_team = self.start_node
            while current_team is not None:
                if current_team.solvedp > 3:
                    print("Team Name:", current_team.name, "Number of problems solved:", current_team.solvedp, "Time taken in minutes:", current_team.time)
                    current_team = current_team.ref
                else:
                    print("No teams in the list.")
                    return
                    
        print(" ")  
#-------------------------- Winning Teams ------------------
    def get_winningteam(self,solvedp,time):
      if self.start_node is None:
           print("No teams in the list.")
           return 
      else:
        current_team = self.start_node
        max = n.item
        while current_team is not None:
               if n.item > max:
                 max = n.item
               elif n.item == n.item:
                 print("Real winner is:")
               n = n.ref
        return max
#  ------------ Count Teams ---------------------------           

     def get_count(self, name):
          if self.start_node is None:
               return 0
          n = self.start_node
          count = 0
          while n is not None:
               count = count + 1
               n = n.ref
          return count
      # --------------- Sum ----------------------------------
     def get_sum(self, time):
           if self.start_node is None:
               return 0
           n = self.start_node
           sum = 0
           while n is not None:
               sum = sum + n.item 
               n = n.ref
           return sum
        # --------------- Average ----------------
     def get_average(self, name, time):
         if self.start_node is None:
               return 0
         else:
              sum = self.get_sum()
              count = self.get_count()
         return sum / count
         
# --------------- MAIN ---------------------
product_list = LinkedList()

choice = 0
while choice != 6:
    # Prompt user for action
    
    print("1. Add a new team.")
    print("2. Print all teams.")
    print("3. Print the teams that solved more than 3 problems.")
    print("4. Print the winning team(s).")
    print("5. Print average time taken.")
    print("6. Exit")
    choice = int(input("\n Enter Choice: "))

  
    if choice == 1:
        name = input("Enter team name: ")
        solvedp = float(input("Enter the number of porblems solved: "))
        time = int(input("Enter amount of time taken: "))
        team_list.add_team(name, solvedp, time)
        print("Team added.\n")

    elif choice == 2:
        team_list.print_teams()

    elif choice == 3:
        team.list.print_teams_above_three(solvedp)
      
    elif choice == 4:
        team_list.get_winningteam(solvedp,time)
      
    elif choice == 5:
        team_list.get_average(name, time)


    
print("Goodbye.")