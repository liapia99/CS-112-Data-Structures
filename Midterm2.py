#Julia Piascik
class Node:
 
def __init__(self, name, solvedp, time)
:
 
self.name = name
 
self.solvedp = solvedp
 
self.time = time
 
self.ref = None
class LinkedList:
 
def __init__(self)
:
 
self.start_node = None
#-------------------------- Add New Team ------------------
 
def add_team(self, name, solvedp, time)
:
 
new_node = Node(name, solvedp, time)
 
new_node.ref = self.start_node
 
self.start_node = new_node
#-------------------------- Print All Teams ------------------
 
def print_teams(self)
:
 
if self.start_node is None:
 
print("No teams in the list.")
 
return
 
else:
 
current_team = self.start_node
 
while current_team is not None:
 
print("\n Team Name:", current_team.name, "\n Number of problems solved:", current_team.solvedp, "\n Time taken in minutes:", 
current_team.time)
 
current_team = current_team.ref
 
print(" ")
#-------------------------- Teams that Solved More Than 3 Problems ------------------
 
def print_teams_above_three(self, solvedp)
:
 
if self.start_node is None:
 
print("No teams in the list.")
 
return
 
else:
 
current_team = self.start_node
 
while current_team is not None:
 
if current_team.solvedp > 3:
 
print("\n Team Name:", current_team.name, "\n Number of problems solved:", current_team.solvedp, "\n Time taken in minutes:", current_team.time)
 
current_team = current_team.ref
 
elif current_team.solvedp < 3:
 
print("No teams solved more than three problems.")
 
current_team = current_team.ref
 
print(" ") 
#-------------------------- Winning Teams ------------------
 
def get_winningteam(self)
:
 
if self.start_node is None:
 
print("No teams in the list.")
 
return 
 
else:
 
max_solvedp = 0
 
current_team = self.start_node
 
while current_team is not None:
 
if current_team.solvedp > max_solvedp:
 
max_solvedp = current_team.solvedp
 
print("\n Team Name:", current_team.name, "\n Number of problems solved:", current_team.solvedp, "\n Time taken in minutes:", 
current_team.time)
 
current_team = current_team.ref
 
else:
 
print("No teams in the list.")
 
current_team = current_team.ref
 
print(" ")
# ------------ Average Time Taken --------------------------- 
 
def get_average(self)
:
 
if self.start_node is None:
 
return 0
 
current_team = self.start_node
 
count = 0
 
sum = 0
 
while current_team is not None:
 
count = count + 1
 
sum = sum + current_team.time
 
avg = sum/count
 
print("\n Average Time:", avg)
 
current_team = current_team.ref
 
print(" ")
 
# --------------- MAIN ---------------------
team_list = LinkedList()
choice = 0
while choice != 6:
 
# Prompt user for action
 
 
print("1. Add a new team.")
 
print("2. Print all teams.")
 
print("3. Print the teams that solved more than 3 problems.")
 
print("4. Print the winning team(s)
.")
 
print("5. Print average time taken.")
 
print("6. Exit")
 
choice = int(input("\n Enter Choice: ")
)
 
 
if choice == 1:
 
name = input("Enter team name: ")
 
solvedp = float(input("Enter the number of problems solved: ")
)
 
time = int(input("Enter amount of time taken: ")
)
 
team_list.add_team(name, solvedp, time)
 
print("Team added.\n")
 
elif choice == 2:
 
team_list.print_teams()
 
elif choice == 3:
 
team_list.print_teams_above_three(solvedp)
 
 
elif choice == 4:
 
team_list.get_winningteam()
 
 
elif choice == 5:
 
team_list.get_average()
 
print("Goodbye.")
