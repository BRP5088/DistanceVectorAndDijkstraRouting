import sys


class ls_Node():

    def __init__(self, name ):
        self.name = name
        
        self.distanceTable = {}
        self.routingTable = {}

    def __str__(self):
        return f"{ self.name }"


    # def print_routingTable(self):

    #     keys = list(self.distanceTable.keys())
    #     keys = sorted(keys)

    #     # print("Dest NxtHp")
    #     output_str = "Dest NxtHp\n"

    #     for key in keys:
    #         # print( f" {key}    { self.routingTable[key] }" )
    #         output_str += f" {key}    { self.routingTable[key] }\n"

    #     return output_str

    # def update_routingTable(self):
    #     row_keys = list(self.distanceTable.keys())
    #     col_keys = list(self.distanceTable[row_keys[0]].keys())

    #     for letter in row_keys:
    #         min_letter = "?"
    #         min_value = sys.maxsize

    #         for col in self.nodesAwareOf:
    #             value = self.distanceTable[letter][col]

    #             if value != "--":
    #                 value = int(value)

    #                 if value < min_value:
    #                     min_letter = col
    #                     min_value = value

    #         self.routingTable[letter] = min_letter

    # def print_routingTable(self):

    #     keys = list(self.distanceTable.keys())
    #     keys = sorted(keys)

    #     # print("Dest NxtHp")
    #     output_str = "Dest NxtHp\n"

    #     for key in keys:
    #         # print( f" {key}    { self.routingTable[key] }" )
    #         output_str += f" {key}    { self.routingTable[key] }\n"

    #     return output_str
