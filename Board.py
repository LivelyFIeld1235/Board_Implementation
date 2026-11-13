"""  column  0   1   2
     row 0  .x.|.x.|.x.
            ---+---+---
     row 1  .x.|.x.|.x.
            ---+---+---
     row 2  .x.|.x.|.x.     . is margin, value can only be character

    print(board) to display tiles
    board.set_coord_update(rownum) to set the coordinates
    board.get_coord() to get coordinate
    board.get_patterns({row, column, full, empty})

"""


class Board:
    def __init__(self, d_sq_Num, initkey="_"):
        self.size = d_sq_Num;
        self.key = initkey
        self.aam_board = [];
        for ind in range(self.size):
            temp = [];
            for jind in range(self.size):
                temp.append(initkey);
            self.aam_board.append(temp);
        self.ValuePresets = {"row":None,"column":None,"full":None,"empty":None}


    def __str__(self,s_margin = " "):
        '''
        .x.|.x.|.x.
        ---+---+---
        .x.|.x.|.x.
        ---+---+---
        .x.|.x.|.x.
        '''
        #0 , 1, 1
        cSTRING,separator,divider = "", "-","+"
        for ind in range(self.size):
            for jnd in range(self.size):
                cSTRING += s_margin + str(self.aam_board[ind][jnd]) + s_margin
                cSTRING+= "" if jnd == len(self.aam_board[ind]) -1 else "|"
            cSTRING += "\n"
            if ind != self.size -1:
                for knd in range(self.size):
                    cSTRING += separator*self.size
                    cSTRING += divider if knd != self.size -1 else ""

            cSTRING += "\n"

        return cSTRING

    def get_patterns(self, var):
        for key in self.ValuePresets.keys():
            key, self.ValuePresets[key]
        match var.lower():
            case "row":
                return self.check_row()
            case "column":
                return self.check_column()
            case "full":
                return self.check_full()
            case "empty":
                return self.check_empty()
            case _:
                return "invalid, please enter a valid entry"
    def get_size(self):
        return self.size
    def check_row(self):
        COUNT = 0;
        for ind in range(self.size):
            for jind in range(self.size):
                COUNT += 1 if self.aam_board[ind][jind] == "X" else 0
                b_check = (True if COUNT == self.size else False)
            if b_check == True:
                return b_check;
        return False

    def check_column(self):
        for ind in range(self.size):
            COUNT = 0
            for jind in range(self.size):
                COUNT += 1 if self.aam_board[jind][ind] == "X" else 0;
                b_check = (True if COUNT == self.size else False)
                if b_check == True:
                    return b_check;
            return False

    def check_full(self):
        COUNT = 0;
        for ind in range(self.size):
            for jind in range(self.size):
                COUNT += 1 if self.aam_board[jind][ind] != self.key else 0;
            b_check = (True if COUNT == self.size ** 2 else False)
            if b_check == True:
                return b_check;
        return False

    def check_empty(self):
        COUNT = 0;
        for ind in range(self.size):
            for jind in range(self.size):
                COUNT += 1 if self.aam_board[jind][ind] == self.key else 0;
            b_check = (True if COUNT == self.size ** 2 else False)
            if b_check == True:
                return b_check;
        return False


    def get_coord(self,*args):
        #self object reference, row, index
        b_returnVal = all([True if vals in range(self.size) else None for vals in args])
        if b_returnVal:
            return self.aam_board[args[0]][args[1]]
        else:
            print("out of range, please try again")

    def set_coord_update(self,value,*args):
        #self object reference, row, index
        if len(value) == 1:
            b_returnVal = all([True if vals in range(self.size) else None for vals in args])
            self.aam_board[args[0]][args[1]] = value
            self.ValuePresets["row"], self.ValuePresets["column"],self.ValuePresets["full"],self.ValuePresets["empty"] = self.check_row(),self.check_column(),self.check_full(),self.check_empty()
        else:
            print("please enter a valid value")

board = Board(3)
print(board)


