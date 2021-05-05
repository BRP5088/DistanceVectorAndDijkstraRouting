import sys # allows the use of command line arguments
import os
from dv_Node import *







def initialize_distanceTable( init_line, a_node):
    init_lst = init_line.split(",")

    letters_arr = []
    numbers_arr = []

    for n in init_lst:
        tmp = n.split("=")  # e.g., [ "B", "10" ]

        letters_arr.append(tmp[0].strip())
        numbers_arr.append(tmp[1].strip())

    for index, letter in enumerate(letters_arr):

        a_node.distanceTable[letter] = {}
        for sec_letter in letters_arr:
            if letter != sec_letter:
                a_node.distanceTable[letter][sec_letter ] = "--"

        a_node.distanceTable[letter][letter] = numbers_arr[index]
        a_node.nodesAwareOf.append( letter )

def initialize_routingTable( a_node ):
    letters = a_node.nodesAwareOf
    for letter in letters:
        a_node.routingTable[letter] = letter





def round_print( time, a_node ):
    print(f"Time { time }:")
    print("Distance Table for A:\n--------------------\nTo Via")
    a_node.print_distanceTable()
    print("\nRouting Table for A\n-------------------")
    a_node.print_routingTable()
    print( "\nMessages Sent:")
    print( a_node.generate_messages() )


def run( filepath ):

    a_node = dv_Node( "A" )
    time = 0

    for index, line in enumerate( open( filepath, "r" ) ):

        messages = ""
        
        if index > 0:
            break

        # print( f"index={index}" )
        # print( line )

        if index == 0:
            initialize_distanceTable( line, a_node )
            initialize_routingTable( a_node )
            round_print(time, a_node)
        
        if index > 0:
            round_print( time, a_node )
        
        time += 1
            





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
