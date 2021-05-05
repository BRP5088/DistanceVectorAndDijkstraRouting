import sys # allows the use of command line arguments
import os
from dv_Node import *







# def initialize_table( filepath, a_node):





def run( filepath ):

    a_node = dv_Node( "A" )



    for index, line in enumerate( open( filepath, "r" ) ):
        
        if index > 0:
            break

        print( f"index={index}" )
        print( line )

        if index == 0:
            init_lst = line.split( "," )

            letters_arr = []
            numbers_arr = []

            for n in init_lst:
                tmp = n.split( "=" ) # e.g., [ "B", "10" ]
                
                letters_arr.append( tmp[0].strip() )
                numbers_arr.append( tmp[1].strip() )
                
            for index, letter in enumerate( letters_arr ):

                a_node.distanceTable[letter] = {}

                for sec_letter in letters_arr:

                    if letter != sec_letter:


                        # if a_node.distanceTable[letter] == None:
                        #     a_node.distanceTable[letter] = {}
                        a_node.distanceTable[ letter ][ sec_letter ] = "-"
                
                a_node.distanceTable[letter][letter] = numbers_arr[ index ]

    a_node.print_distanceTable()




def main():

    filepath = ""
    output_path = ""

    for index, arg in enumerate( sys.argv ):
        if index == 1:
            filepath = arg
        if index == 2:
            output_path = arg

    filepath = "inputFile.txt"

    print( filepath )

    if filepath == "":
        print("\033[1;31;40mA filepath must be provided to run the program.\033[1;37;40m")
        sys.exit( 1000 )

    # print(os.path.curdir + os.path.sep + filepath )

    # if os.path.cur( filepath ):
    #     print( "\033[1;31;40mThe filepath must exist to run the program.\033[1;37;40m")
    #     sys.exit(1001)


    run( filepath )


if __name__ == "__main__":
    main()
