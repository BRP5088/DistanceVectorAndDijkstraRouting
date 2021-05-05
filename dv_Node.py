
class dv_Node():

    def __init__(self, name):
        self.neighbors = []
        self.distanceTable = { }
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
                print( f"    { col_name }   ", end="")
            else:
                print( f" { col_name }   ", end="")
        print()

        for key in row_keys:
            string = " " + key + " "
            for col in col_keys:
                string += " " + self.distanceTable[key][col] + "   "
            print( string )
