class Board:
    def __init__(self, initial : int, final : int, times : int):
        self.board_list : list[int] = []
        self.initial = initial
        self.final = final
        self.times = times
        
    def create_board(self):
        for i in  range(self.initial, self.final + 1):
            for j in range(self.times):
                self.board_list.append(i)
    
    def turn(self, number_added_to_sum : int):
        while len(self.board_list) > 1:
            first : int = self.board_list.pop(0)
            last : int = self.board_list.pop()
            total : int = first + last + number_added_to_sum
            self.board_list.append(total)
        
board = Board(1, 10, 10)
board.create_board()
board.turn(number_added_to_sum = 1)
print(board.board_list)
