import numpy

class Peg:
    x = -1
    y = -1
    xMin = -1
    xMax = -1
    yMin = -1
    yMax = -1
    neighbours = {}
    moves = {}
    visited = 0

    def __init__(self, configuration, x, y, xMin, xMax, yMin, yMax):
        self.x = x
        self.y = y
        self.xMin = xMin
        self.yMin = yMin
        self.xMax = xMax
        self.yMax = yMax
        self.findNeighbours(configuration)
        self.findMoves(configuration)
        self.visited = configuration[x][y]

    def findNeighbours(self, configuration):

        if(self.x+1 <= self.xMax):
            if(configuration[self.x + 1][self.y] != -1):
                self.neighbours["d"] = [self.x + 1, self.y] #configuration[self.x + 1][self.y]

        if (self.x - 1 >= self.xMin):
            if (configuration[self.x - 1][self.y] != -1):
                self.neighbours["u"] = [self.x - 1, self.y] #configuration[self.x - 1][self.y]

        if (self.y + 1 <= self.yMax):
            if (configuration[self.x][self.y + 1] != -1):
                self.neighbours["r"] = [self.x, self.y + 1] #configuration[self.x][self.y + 1]

        if (self.y - 1 >= self.yMin):
            if (configuration[self.x][self.y - 1] != -1):
                self.neighbours["l"] = [self.x, self.y - 1] #configuration[self.x][self.y - 1]

    def findMoves(self, configuration):

        if(self.x+2 <= self.xMax):
            if(configuration[self.x + 2][self.y] != -1):
                if(configuration[self.x + 1][self.y] == 1):
                    self.moves["d"] = [self.x + 2, self.y] #configuration[self.x + 2][self.y]

        if (self.x - 2 >= self.xMin):
            if (configuration[self.x - 2][self.y] != -1):
                if (configuration[self.x - 1][self.y] == 1):
                    self.moves["u"] = [self.x - 2, self.y]#configuration[self.x - 2][self.y]

        if (self.y + 2 <= self.yMax):
            if (configuration[self.x][self.y + 2] != -1):
                if (configuration[self.x][self.y + 1] == 1):
                    self.moves["r"] = [self.x, self.y + 2] #configuration[self.x][self.y + 2]

        if (self.y - 2 >= self.yMin):
            if (configuration[self.x][self.y - 2] != -1):
                if (configuration[self.x][self.y - 1] == 1):
                    self.moves["l"] = [self.x, self.y - 2] #configuration[self.x][self.y - 2]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setVisited(self, val):
        self.visited = val

    def getVisited(self):
        return self.visited