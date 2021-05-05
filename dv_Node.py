import sys

class dv_Node():

    def __init__(self, name):
        self.nodesAwareOf = [ ]
        self.distanceTable = { }
        self.routingTable = { }
        self.name = name

    def __str__( self ):
        return f"{ self.name }"


    def print_distanceTable( self ):
        row_keys = list( self.distanceTable.keys() )
        col_keys = list( self.distanceTable[ row_keys[0] ].keys() )
        
        row_keys = sorted( row_keys )
        col_keys = sorted( col_keys )

        for index, col_name in enumerate( col_keys ):
            if index == 0:
                print( f"     { col_name }    ", end="")
            else:
                print( f" { col_name }    ", end="")
        print()

        for key in row_keys:
            string = " " + key + " "
            for col in col_keys:

                if self.distanceTable[key][col] == "--":
                    string += " " + self.distanceTable[key][col] + "   "
                else:
                    string += "  " + self.distanceTable[key][col] + "   "
            print( string )
    

    def print_routingTable( self ):

        keys = self.nodesAwareOf
        keys = sorted( keys )

        print("Dest NxtHp")

        for key in keys:
            print( f" {key}    { self.routingTable[key] }" )



    def generate_messages( self ):
        string = ""

        letter_lst = list(self.distanceTable.keys())
        letter_lst = sorted( letter_lst )

        for letter in letter_lst:
            tmp = "{" + self.name + ","

            min_letter = "?"
            min_value = sys.maxsize
            for sec_letter in sorted( self.nodesAwareOf ):

                value = self.distanceTable[letter][sec_letter]
                
                if value != "--": 
                    if min_value > int( value ):
                        min_letter = sec_letter
                        min_value = int( value )
            
            tmp += min_letter + "," + str( min_value ) + "}"
            string += tmp

        return string

