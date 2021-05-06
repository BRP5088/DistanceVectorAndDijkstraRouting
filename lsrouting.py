import sys
import os
from ls_Node import *


def initialize_distanceTable(filepath, node_map):
    for line in open(filepath, "r"):

        lsa = line.split(";")
        lsa = [el.strip() for el in lsa]

        for relation in lsa:
            source, destination, value = relation.split(",")

            source = source[1:]
            value = value[0: len(value) - 1]

            if source not in node_map:
                new_node = ls_Node(source)
                node_map[source] = new_node

            if destination not in node_map:
                new_node = ls_Node(destination)
                node_map[destination] = new_node

            source_node = node_map[source]
            destination_node = node_map[destination]

            source_node.distanceTable[destination_node.name] = value


def initialize_routingTable(node_map):
    a_node = node_map.get( "A" )
    letters = sorted( node_map.keys() )
    for letter in letters:
        a_node.routingTable[letter] = letter



def display_board( node_map, board, output ):
    for row in board:

        for index, cell in enumerate( row ):

            if index == 0:
                # print( f" { cell }\t", end="" )
                output.append(f" { cell }\t" )
            
            if index == 1:

                # print(f"{ cell }" + " " * ( len( cell ) -1 ), end="")
                output.append(f"{ cell }" + " " * (len(cell) - 1) )
        
        # print()
        output.append( "\n" )





def generate_board( node_map, board ):

    num_iterations = len( node_map.keys() )
    iteration = 0

    looked_at = []
    node_lst = [ node_map["A"] ]

    while len( node_lst ) > 0:

        node = node_lst.pop(0)
        looked_at.append(node.name)

        for spot in range(0, len( node_map.keys() ) ):

            if spot == 0:
                board[iteration].append( iteration )
            
            if spot == 1:
                if iteration == 0:
                    board[iteration].append( node.name )
                else:
                    board[iteration].append( board[ iteration - 1][1] )
        
            if spot > 1:


                if iteration == 0:

                    # node_neighbor_lst = sorted( list( node.distanceTable.keys() ), key=lambda x: node.distanceTable[x] )
                    node_neighbor_lst = sorted( list( node.distanceTable.keys() ) )
                
                # for neighbor in node_neighbor_lst:
                #     if neighbor not in looked_at:
                #         node_lst.append( node_map[ neighbor ] )
                        
                #         board[ iteration ].append( ( node.distanceTable[ neighbor ], "B" ) )
        
        iteration += 1
    


def run(filepath, output):

    node_map = {}

    a_node = ls_Node( "A" )
    node_map[ "A" ] = a_node

    initialize_distanceTable( filepath, node_map )
    initialize_routingTable( node_map )


    output.append("Step\tN")
    nodes = sorted( node_map.keys() )

    output.append( " " * (len( nodes ) + 1))


    for node_name in nodes:
        if node_name != "A":
            output.append( f"D({ node_name})   " )
    

    output.append( "\n" )
    output.append( "_" * ( len( nodes ) * 8 ) )
    output.append( "\n" )

    board = [ ]

    for _ in range(0, len( node_map.keys() ) ):
        board.append( [ ] )

    # display_board( node_map, board, output )

    generate_board( node_map, board )

    # a_node.update_routingTable()

    # output.append( a_node.print_routingTable() )

    display_board( node_map, board, output )

    




def main():

    filepath = ""
    output_path = ""

    for index, arg in enumerate(sys.argv):
        if index == 1:
            filepath = arg
        if index == 2:
            output_path = arg

    filepath = "DijkstraInput.txt"
    # output_path = "outputFile.txt"

    if filepath == "":
        print(
            "\033[1;31;40mA filepath must be provided to run the program.\033[1;37;40m")
        sys.exit(1000)

    output = []

    run(filepath, output)

    for el in output:
        print(el, end="")


    if output_path:
        fp = open(output_path, "w")
        for el in output:
            fp.write(el)
        fp.close()


if __name__ == "__main__":
    main()
