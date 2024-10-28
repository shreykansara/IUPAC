#IUPAC Nomenclature.

print("This program is designed to derive the IUPAC Name of Hydrocarbons.")
c = int(input("Enter the no. of Carbon atoms (between 1-10) in the Parent Chain (or the Longest Carbon Chain):"))

if c > 1:
    fngrp = input("Enter the name of the Principal Funtional Group (Alkane/Alkene/Alkyne):")

    poly = {
        1:"meth",
        2:"eth",
        3:"prop",
        4:"but",
        5:"pent",
        6:"hex",
        7:"hept",
        8:"oct",
        9:"non",
        10:"dec",
        }

    no_of_fg = {
        1:"",
        2:"di",
        3:"tri",
        4:"tetra",
        5:"penta",
        6:"hexa",
        7:"hepta",
        9:"nona",
        10:"deca"
        }

    posi = {
        1:"First",
        2:"Second",
        3:"Third",
        4:"Fourth",
        5:"Fifth",
        6:"Sixth",
        7:"Seventh",
        8:"Eighth",
        9:"Ninth",
        }

    if fngrp.lower() == "alkane":
        print("The IUPAC Name of the given organic compound is", poly[c].capitalize()+"ane.")

    elif fngrp.lower() == "alkene":
        no_of_db = int(input("Enter the no. of Double Bonds in the Parent Chain:"))
        sum_of_posi = 0
        sum_of_posi_rev = 0
        final_posi = ""
        final_posi_rev = ""

        if no_of_db == 1:
            posi_db = int(input("Enter the position of the Double Bond:"))
            posi_db_rev = c - posi_db
            sum_of_posi = sum_of_posi + posi_db
            sum_of_posi_rev = sum_of_posi_rev + posi_db_rev
            final_posi = " "+str(posi_db)
            final_posi_rev = str(posi_db_rev)+" "

        elif no_of_db < c and no_of_db > 1:
           for i in range(no_of_db):
                posi_db = int(input("Enter the position of the "+ str(posi[i+1]) + " Double bond:"))
                posi_db_rev = c - posi_db
                sum_of_posi = sum_of_posi + posi_db
                sum_of_posi_rev = sum_of_posi_rev + posi_db_rev
                final_posi = final_posi+","+str(posi_db)
                final_posi_rev = str(posi_db_rev)+","+final_posi_rev

        tb = input("Does this compound have any Triple bond?:")

        if tb.lower() == "no":

            if sum_of_posi <= sum_of_posi_rev:
                iupac = poly[c].capitalize()+"-"+final_posi[1:]+"-"+no_of_fg[no_of_db]+"ene."
                print("The IUPAC Name of the given organic compound is", iupac)

            else:
                iupac = poly[c].capitalize()+"-"+final_posi_rev[:-1]+"-"+no_of_fg[no_of_db]+"ene."
                print("The IUPAC Name of the given organic compound is", iupac)

        elif tb.lower() == "yes":
            no_of_tb = int(input("Enter the no. of triple bonds:"))

            if (no_of_db + no_of_tb) < c:
                final_posi_tb = ""
                final_posi_tb_rev = ""
                
                if no_of_tb == 1:
                    posi_tb = int(input("Enter the position of Triple Bond:"))
                    posi_tb_rev = c - posi_tb
                    final_posi_tb = " "+str(posi_tb)
                    final_posi_tb_rev = str(posi_tb_rev)+" "

                elif no_of_tb > 1:
                    for i in range(no_of_tb):
                        posi_tb = int(input("Enter the position of the " + posi[i+1] + " Triple bond:"))
                        posi_tb_rev = c - posi_tb
                        final_posi_tb = final_posi_tb+","+str(posi_tb)
                        final_posi_tb_rev = str(posi_tb_rev)+","+final_posi_tb_rev

            if sum_of_posi <= sum_of_posi_rev:
                iupac = poly[c].capitalize()+"-"+final_posi[1:]+"-"+no_of_fg[no_of_db]+"en"+"-"+final_posi_tb[1:]+"-"+no_of_fg[no_of_tb]+"yne."
                print("The IUPAC Name of the given organic compound is", iupac)

            else:
                iupac = poly[c].capitalize()+"-"+final_posi_rev[:-1]+"-"+no_of_fg[no_of_db]+"en"+"-"+final_posi_tb_rev[:-1]+"-"+no_of_fg[no_of_tb]+"yne."
                print("The IUPAC Name of the given organic compound is", iupac)

        else:
            print("This Organic Compound cannot exist.")

    elif fngrp.lower() == "alkyne":
        no_of_tb = int(input("Enter the no. of triple bonds:"))

        if no_of_tb < c:
            sum_of_posi = 0
            sum_of_posi_rev = 0
            final_posi_tb = ""
            final_posi_tb_rev = ""
                
            if no_of_tb == 1:
                posi_tb = int(input("Enter the position of Triple Bond:"))
                posi_tb_rev = c - posi_tb
                sum_of_posi = posi_tb + sum_of_posi
                sum_of_posi_rev = sum_of_posi_rev + posi_tb_rev
                final_posi_tb = " "+str(posi_tb)
                final_posi_tb_rev = str(posi_tb_rev)+" "

            elif no_of_tb > 1:
                for i in range(no_of_tb):
                    posi_tb = int(input("Enter the position of the " + posi[i+1] + " Triple bond:"))
                    posi_tb_rev = c - posi_tb
                    sum_of_posi = posi_tb + sum_of_posi
                    sum_of_posi_rev = sum_of_posi_rev + posi_tb_rev
                    final_posi_tb = final_posi_tb+","+str(posi_tb)
                    final_posi_tb_rev = str(posi_tb_rev)+","+final_posi_tb_rev


        if sum_of_posi <= sum_of_posi_rev:
            iupac = poly[c].capitalize()+"-"+str(final_posi_tb)[1:]+"-"+no_of_fg[no_of_tb]+"yne."
            print("The IUPAC Name of the given organic compound is", iupac)

        else:
            iupac = poly[c].capitalize()+"-"+str(final_posi_tb_rev)[:-1]+"-"+no_of_fg[no_of_tb]+"yne."
            print("The IUPAC Name of the given organic compound is" , iupac)

elif c == 1:
    print("The IUPAC Name of the given organic compound is Methane.")

else:
    print("Please enter a no. between 1-10") 
