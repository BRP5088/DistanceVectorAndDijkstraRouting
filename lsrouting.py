import sys
import os
from ls_Node import *
import copy


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
    a_node = node_map.get( 'A' )
    letters = sorted( node_map.keys() )
    for letter in letters:
        a_node.routingTable[letter] = letter



def display_board( node_map, board, output ):
    for row in board:

        for index, cell in enumerate( row ):

            if index == 0:
                output.append(f" { cell }" )
            
            if index == 1:
                output.append(f"\t{ cell }" + " " * ( len( node_map.keys() ) - len( cell ) ) )

            if index > 1:

                if index == 2:
                    output.append( " " * (len( node_map.keys() ) ) )

                if cell == "":
                    output.append("       ")
                elif cell == "-,-":
                    output.append(f"{cell}    ")
                elif cell == "*":
                    output.append(f" {cell}     ")
                else:
                    output.append( f"{ cell[0] },{cell[1]}    " )
        
        output.append( "\n" )



def generate_board( node_map, board ):

    num_iterations = len( node_map.keys() )
    iteration = 0

    looked_at = []
    node_lst = [ node_map["A"] ]

    node_index_lst = sorted( list( node_map.keys() ) )
    node_index_lst.remove('A')

    while len( node_lst ) > 0:

        node = node_lst.pop(0)
        looked_at.append(node.name)

        node_neighbor_lst = sorted(list(node.distanceTable.keys()))

        for spot in range(0, len( node_map.keys() ) + 1 ):

            if spot == 0:
                board[iteration].append( iteration )
            
            if spot == 1:
                if iteration == 0:
                    board[iteration].append( node.name )
                else:
                    board[iteration].append( board[ iteration - 1][1] + node.name )
        
            if spot > 1:

                if iteration == 0:
                    if spot -2 < len( node_neighbor_lst ):
                        letter = node_neighbor_lst[spot - 2]        
                        board[iteration].append( (node.distanceTable[ letter ], letter) )
                    else:
                        board[iteration].append( "-,-" )

                else:
                    size_diff = len(node_index_lst)-(len(board[iteration]) - 2)
                    if size_diff > 0:
                        for _ in range(size_diff):
                            board[iteration].append("    ")

                    if node_index_lst.index( node.name ) == spot - 2:
                        board[iteration][spot] = "*"
                        continue

                    if node_index_lst[spot - 2] not in node_neighbor_lst:
                        if board[iteration][spot] != "-,-":
                            board[iteration][spot] = board[iteration-1][spot]
                        else:
                            board[iteration][spot] = "-,-"
                        continue


                    a_node = node_map[ "A" ]
                    weight_to_curr_node = int( a_node.distanceTable[ node.name ] )

                    for node_neighbor in node_neighbor_lst:

                        if not node_neighbor == "A":

                            
                            if node_neighbor not in looked_at:
                            

                                weight_to_neighbor = int( node.distanceTable[ node_neighbor ] ) + weight_to_curr_node
                                
                                letter_placement = node_index_lst.index( node_neighbor )
                                cell_above = board[iteration - 1][ 2 + letter_placement]

                                previous_round_weight = sys.maxsize

                                if type( cell_above ) == tuple:
                                    previous_round_weight = int( cell_above[0] )
                                elif cell_above == " * " or cell_above == "    ":
                                    continue

                                
                                if weight_to_neighbor > previous_round_weight:
                                    board[iteration][2+letter_placement] = copy.deepcopy( cell_above )
                                else:
                                    board[iteration][2+letter_placement] = (weight_to_neighbor, node.name )
                                    
                                    a_node.distanceTable[node_neighbor] = weight_to_neighbor
                                    a_node.routingTable[ node_neighbor ] = node.name

                            else:
                                board[iteration][spot] = ""
        
        
        node_neighbor_lst = sorted( list( node.distanceTable.keys() ), key=lambda x: node.distanceTable[x] ) # this sorts the nodes by weight

        for neighbor in node_neighbor_lst:
            if neighbor not in looked_at and node_map[neighbor] not in node_lst:
                node_lst.append( node_map[ neighbor ] )

        iteration += 1


def display_routing_table( node_map, board, output ):


    a_node = node_map[ 'A' ]
    keys = sorted( list( a_node.routingTable.keys()) )

    keys.remove("A")
    output.append("\nRouting Table for A\n-------------------\nDest NxtHp\n")

    for key in keys:
        output.append( f"{key}    {a_node.routingTable[key]}\n" )

    output.append("\n")



def run(filepath, output):

    node_map = {}

    a_node = ls_Node( "A" )
    node_map[ "A" ] = a_node

    initialize_distanceTable( filepath, node_map )
    initialize_routingTable( node_map )


    output.append("Step\tN")
    nodes = sorted( node_map.keys() )

    output.append( " " * (len( nodes ) + 5))


    for node_name in nodes:
        if node_name != "A":
            output.append( f"D({ node_name})" )
            output.append(" " * 3 )

    output.append( "\n" + ( "_" * ( len( nodes ) * 9 ) ) + "\n")

    board = [ ]

    for _ in range(0, len( node_map.keys() ) ):
        board.append( [ ] )

    generate_board( node_map, board )
    display_board( node_map, board, output )
    display_routing_table( node_map, board, output )




def main():

    filepath = ""
    output_path = ""

    for index, arg in enumerate(sys.argv):
        if index == 1:
            filepath = arg
        if index == 2:
            output_path = arg

    # filepath = "DijkstraInput.txt"
    # output_path = "DijkstraOutputFile.txt"

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
