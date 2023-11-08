order = 300
order2 = 100

while order > 0 or order2 > 0:
    ask = int(input("Where would you like your seats? 1 for Hall and 2 for Mezzanine"))
    if ask == 1:
        child = int(input("How many child tickets?"))
        adult = int(input("How many adult tickets?"))
        tickets = (child + adult) 
        total = (child*7) + (adult*10)
        if tickets > order:
            print("Unable to make transaction for Hall tickets.")
            print("We are sorry for the inconvenience. Have a nice day!")
            if tickets <= order2:
                print("There are seats in Mezzanine seating if you would like.")
                ask2 = int(input("1 for No and 2 for Yes"))
                if ask2 == 2:
                    child = int(input("How many child tickets?"))
                    adult = int(input("How many adult tickets?"))
                    tickets = (child + adult) 
                    total = (child*5) + (adult*8)
                    order2 = order2 - tickets
                    print("Wonderful! Your total is $",total,". You bought", child,"children tickets and", adult, "adult tickets. Enjoy the movie!")
                    print(order2,"tickets left for Mezzanine seating.",order,"tickets left for Hall seating.")
                else:
                    print("We are sorry for the inconvenience. Have a nice day!")
                #endif
                
        else:
            order = order - tickets
            print("Wonderful! Your total is $",total,". You bought", child,"children tickets and", adult, "adult tickets. Enjoy the movie!")
            print(order2,"tickets left for Mezzanine seating.",order,"tickets left for Hall seating.")
        #endif 
    elif ask == 2:
        child = int(input("How many child tickets?"))
        adult = int(input("How many adult tickets?"))
        tickets = (child + adult) 
        total = (child*5) + (adult*8)
        if tickets > order2:
            print("Unable to make transaction for Mezzanine tickets.")
            print("We are sorry for the inconvenience. Have a nice day!")
            if tickets <= order:
                print("There are seats in Hall seating if you would like.")
                ask2 = int(input("1 for No and 2 for Yes"))
                if ask2 == 2:
                    child = int(input("How many child tickets?"))
                    adult = int(input("How many adult tickets?"))
                    tickets = (child + adult) 
                    total = (child*7) + (adult*10)
                    order = order - tickets
                    print("Wonderful! Your total is $",total,". You bought", child,"children tickets and", adult, "adult tickets. Enjoy the movie!")
                    print(order2,"tickets left for Mezzanine seating.",order,"tickets left for Hall seating.")
                else:
                    print("We are sorry for the inconvenience. Have a nice day!")
                #endif
                
        else:
            order2 = order2 - tickets
            print("Wonderful! Your total is $",total,". You bought", child,"children tickets and", adult, "adult tickets. Enjoy the movie!")
            print(order2,"tickets left for Mezzanine seating.",order,"tickets left for Hall seating.")
        #endif
    else:
        print("Invalid input.")
    #endif
#endwhile
