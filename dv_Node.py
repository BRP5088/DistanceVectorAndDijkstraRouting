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

        output_str = ""

        for index, col_name in enumerate( col_keys ):
            if index == 0:
                # print( f"     { col_name }    ", end="")
                output_str += f"     { col_name }    "
            else:
                # print( f" { col_name }    ", end="")
                output_str += f" { col_name }    "
        # print()
        output_str += "\n"

        for key in row_keys:
            string = " " + key + " "
            for col in col_keys:

                if self.distanceTable[key][col] == "--":
                    string += " " + self.distanceTable[key][col] + "   "
                else:
                    if len(self.distanceTable[key][col] ) > 1:
                        string += " " + self.distanceTable[key][col] + "   "
                    else:
                        string += "  " + self.distanceTable[key][col] + "   "
            # print( string )
            output_str += string + "\n"

        return output_str
    

    def print_routingTable( self ):

        keys = list(self.distanceTable.keys())
        keys = sorted( keys )

        # print("Dest NxtHp")
        output_str = "Dest NxtHp\n"

        for key in keys:
            # print( f" {key}    { self.routingTable[key] }" )
            output_str += f" {key}    { self.routingTable[key] }\n"

        return output_str



    def generate_messages( self ):
        string = []

        letter_lst = sorted( list(self.distanceTable.keys() ) )

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
            
            tmp += letter + "," + str( min_value ) + "}"
            string.append( tmp )

        string = sorted( string, key=lambda x: x[3] )
        return "".join(string)


    def update_distanceTable(self, message_lst):
        for message in message_lst:

            source, destination, value = message.split(",")

            source = source[1:]
            value = int(value[0: len(value) - 1])

            if destination == "A":
                continue

            if source not in list(self.distanceTable.keys()):
                self.distanceTable[source] = {}
                for letter in self.nodesAwareOf:
                    self.distanceTable[source][letter] = "--"

            if destination not in list(self.distanceTable.keys()):
                self.distanceTable[destination] = {}
                for letter in self.nodesAwareOf:
                    self.distanceTable[destination][letter] = "--"

            if self.distanceTable[source][source] != "--":
                value += int(self.distanceTable[source][source])

            self.distanceTable[destination][source] = str(value)


    def update_routingTable(self):
        row_keys = list(self.distanceTable.keys())
        col_keys = list(self.distanceTable[row_keys[0]].keys())

        for letter in row_keys:
            min_letter = "?"
            min_value = sys.maxsize

            for col in self.nodesAwareOf:
                value = self.distanceTable[letter][col] 

                if value != "--":
                    value = int( value )

                    if value < min_value:
                        min_letter = col
                        min_value = value


            self.routingTable[letter] = min_letter
