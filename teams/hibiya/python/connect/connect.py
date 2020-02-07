class ConnectGame:
    
    def __init__(self, board):
        debug = False # only for debug
        
        # Decode the input
        """ Sample input format like below. represented in 2d lists
            X O . .
            O X X X
            O X O .
            . O X .
            X X O O """
        arr = board.split("\n")
        for _ in range(len(arr)):
            arr[_] = list(arr[_].strip().replace(' ',''))
        self.arr = arr
        w = len(arr[0])
        h = len(arr)
        n = w * h
        
        # INIT local variables
        self.winner = ""
        arr_o = [[ 0 for _ in range(n) ] for _ in range(n)]
        arr_x = [[ 0 for _ in range(n) ] for _ in range(n)]
        dp_o  = [[ ] for _ in range(n)]
        dp_x  = [[ ] for _ in range(n)]
        tmp_o = [[ 0 for _ in range(n) ] for _ in range(n)]
        tmp_x = [[ 0 for _ in range(n) ] for _ in range(n)]
        
        # Define the links among nodes.
        moves = [
                    (0,-1), (1,-1),
            (-1, 0),(0, 0), (1, 0),
            (-1, 1),(0, 1)
        ]
        
        # make a map
        for y in range(h):
            for x in range(w):
                for (i,j) in moves:
                    sx = x+i ; sy = y+j
                    if 0 <= sx < w and 0 <= sy < h:
                        a = y*w+x ; b = sy*w+sx
                        if arr[y][x] == 'X' and 'X' == arr[sy][sx]:
                            arr_x[a][b] = arr_x[b][a] = 1
                            dp_x[a].append(b);dp_x[b].append(a)
                        if arr[y][x] == 'O' and 'O' == arr[sy][sx]:
                            arr_o[a][b] = arr_o[b][a] = 1
                            dp_o[a].append(b);dp_o[b].append(a)
        
        # Find all paths
        for s in range(n):
            for d in dp_o[s]:   self.search(s,d, tmp_o[s], dp_o, arr_o)
            for d in dp_x[s]:   self.search(s,d, tmp_x[s], dp_x, arr_x)
        
        # O wins in case Top to the bottom
        for _ in range(w):
            if sum(arr_o[_][n-w:n]):
                self.winner = "O"
                break
            if debug:   print(arr_o[_][n-w:n])
        
        # X wins in case Left to the right
        for y in range(h):
            x = 0
            for j in range(h):
                if 1 == arr_x[y*w+x][j*w+x+(w-1)]:
                    self.winner = "X"
                    break
                if debug:   print(arr_x[y*w+x][j*w+x+(w-1)])
    
    # output the result
    def get_winner(self):
        return self.winner
    
    # link connection tests
    def search(self, src, dst, tmp, dp, arr):
        tmp[dst] = arr[src][dst] = 1
        for DST in dp[dst]:
            if not tmp[DST]:
                self.search(src, DST, tmp, dp, arr)