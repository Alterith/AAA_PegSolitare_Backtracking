import numpy as np
import Peg
# 0 = empty block
# 1 = peg
# -1 = out of bound
configuration = np.zeros(shape=(7,7));
configuration.fill(-1)

configurationSolution = np.zeros(shape=(7,7));
configurationSolution.fill(-1)

for i in range(0,7):
    for j in range(0,7):
        if (i >= 2 and i < 5) or (j >= 2 and j < 5):
            configuration[i][j] = 1
            configurationSolution[i][j] = 0


configuration[3][3] = 0
configurationSolution[3][3] = 1
# configuration[4][3] = 0
# configuration[5][3] = 3
# configuration[3][5] = 7
# configuration[1][3] = 5
# configuration[3][1] = 6

# peg1 = Peg.Peg(configuration, 3, 3, 0, 6, 0, 6)
board = []
for i in range(0,7):
    boardRow = []
    for j in range(0,7):
        boardRow.append(Peg.Peg(configuration, i, j, 0, 6, 0, 6))
    board.append(boardRow)

# neighbours = peg1.neighbours
#
# for key,val in neighbours.items():
#     print(key, 'is the key for neighbour ', val)
#
# moves = peg1.moves
# print('\n')
# for key,val in moves.items():
#     print(key, 'is the key for move ', val)

print('\n' ,configuration);
print('\n' ,configurationSolution);
print('\n' ,len(board))
print('\n' ,len(board[0]))
# for i in range(0,7):
#     for j in range(0, 7):
#         peg1 = board[i][j]
#         print('\n' ,peg1.neighbours);

def checkSolution(configuration):
    comparedList = []
    for i in range(0, 7):
        comparison =  configuration[i] == configurationSolution[i]
        if(False in comparison):
            return False
    return True

def backtrackingSolution(configuration):
    if(checkSolution(configuration)):
        return True
    else:
        for i in range(0, 7):
            for j in range(0, 7):
                if (i >= 2 and i < 5) or (j >= 2 and j < 5):
                    if(configuration[i][j] == 1):

                        pass

                        #make move

                        # run backtracking algorithm a = backtracking
                        # if(a) break return true
                        # elseif(i == 6, j == 4) return false
                        # else revert move and run backtracking again on next point
        return


print('\n', checkSolution(configuration))

for i in range(0,7):
    for j in range(0,7):
        print(board[i][j].getVisited(), end="    ")
    print()
