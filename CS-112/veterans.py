#########################################################
# Veterans Financial Assistance Report using file : veteran.dat
# File:  vet.py
# Author: Julia Piascik
# Date: Oct 24, 2022
#########################################################

veteranfile = open( "veteran.dat", mode = 'r' )

veterans = []                   # veterans null list

fl = 0                          # full-time count
pt = 0                          # part-time count
fi = 0.0                        # financial aid total
amo = 0

#print headers
print("\n====================================================================================")
print("                                   VETERANS FINANCIAL ASSISTANCE REPORT                     ")
print("")
print("     STUDENT NAME              UNITS               DEPS            AMOUNT")
print("======================================================================================")

for veterans in veteranfile:
              veterans = veterans.split()
              name = veterans[0]
              code = int(veterans[1])
              units = int(veterans[2])
              deps = int(veterans[3])
             
              if code == 2:
                  if units >= 15:
                        fl = fl + 1
                        if deps > 2:
                            amo = (30.00 * units)
                            units = 'FULL-TIME'
                            fi = fi + amo
                        else:
                            amo = (27.00 * units)
                            units = 'FULL-TIME'
                            fi = fi + amo
                  else:
                        
                        pt = pt + 1
                        if deps > 2:
                            amo = (23.00 * units)
                            units = 'PART-TIME'
                            fi = fi + amo
                        else:
                            amo = (20.00 * units)
                            units = 'PART-TIME'
                            fi = fi + amo
            
                    

                         #endif
                         #endif
                    #endif
                 # accumulate and count
                  
                 #output
                 #print(name,units,deps,amo)
                  print( "%15s %18s %18i %19f"  %  (name,units,deps,amo))

                  #endif
#end for
veteranfile.close()

print("==============================================================")
print("  Total full-time veteran students   ==> ", fl)
print("  Total part-time veteran students   ==> ",pt)
print("  Total financial aid amount          ==> $", (fi))
print("\n .... End of job!")
veteranfile.close()
# end of main



