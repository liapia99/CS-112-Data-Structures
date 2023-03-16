#########################################################
# Computer Usage Report using file : computer.dat
# File:  computerusagereport.py
# Author: Julia Piascik
# Date: Oct 24, 2022
#########################################################

computerfile = open( "computer.dat", mode = 'r' )

customers = []                   # customers null list
tc = 0                           # total customer counter
tm = 0                         # total computer time accumulator
tch = 0.0                       # total chargers accumulator

hour = (120 * 0.99) 


#print headers
print("\n====================================================================================")
print("                                   COMPUTER USAGE REPORT                     ")
print("")
print("     CUSTOMER NAME              COMPUTER               MINUTES            CHARGE")
print("======================================================================================")

for customer in computerfile:
              customer = customer.split()
              name = customer[0]
              computer = str(customer[1])
              time = int(customer[2])
              
              if time > 120:
                    charge = ((time - 120)*(0.86)) + hour 
              else:
                    charge = (time * 0.99) 
              #endif
              # accumulate and count
              tc = tc + 1
              tm = tm + time
              tch = tch + charge
              #output
              #print(name,computer,time,charge)
              print( "%10s %29s %19i %19.2f"  %  (name,computer,time,charge))
#end for
computerfile.close()
print("==============================================================")
print("  Total customers found   ==> ", tc)
print("  Total minutes of computer time used               ==> ",tm)
print("  Total charges          ==> $", (tch))
print("\n .... End of job!")
computerfile.close()
# end of main
