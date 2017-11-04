import random as ran

def sample(numberThrown):
    hits = 0

    for i in range (0, numberThrown):
        x = ran.uniform(-1,1)
        y = ran.uniform(-1,1)

        inCircle = x**2 + y**2

        if(inCircle < 1):
            hits = hits + 1

    return hits


def sampleRando(numberThrown):
    hits = 0
    x = 1
    y = 1

    change = 1

    for i in range (numberThrown):
        difX = ran.uniform(-change,change)
        difY = ran.uniform(-change,change)



        if(((x + difX) < 1) and ((y + difY) < 1) and  (x + difX) > -1) and ((y + difY) > -1):
            x = x + difX
            y = y + difY


        if(x**2 + y**2 < 1):
            hits = hits + 1

    return hits




class StandardNeighbourTable():

    grid = [[0 for x in range(5)] for y in range(9)]

    def __init__(self):


        for i in range(9):
            for j in range(5):
                if(j == 0):
                    self.grid[i][j] = i
                else:
                    self.grid[i][j] = -1

        #Node 1

        self.grid[0][1] = 1
        self.grid[0][2] = 3

        #Node 2

        self.grid[1][1] = 2
        self.grid[1][2] = 4
        self.grid[1][3] = 0

        #Node 3

        self.grid[2][2] = 5
        self.grid[2][3] = 1

        #Node 4

        self.grid[3][1] = 4
        self.grid[3][2] = 6
        self.grid[3][4] = 0

        # Node 5

        self.grid[4][1] = 5
        self.grid[4][2] = 7
        self.grid[4][3] = 3
        self.grid[4][4] = 1

        # Node 6

        self.grid[5][2] = 8
        self.grid[5][3] = 4
        self.grid[5][4] = 2

        # Node 7

        self.grid[6][1] = 7
        self.grid[6][4] = 3

        # Node 8

        self.grid[7][1] = 8
        self.grid[7][3] = 6
        self.grid[7][4] = 4

        # Node 9

        self.grid[8][3] = 7
        self.grid[8][4] = 5

    def printGrid(self):

        topRow = str(self.grid[6][0] + 1) + " " + str(self.grid[7][0] + 1) + " " + str(self.grid[8][0] + 1)
        midRow = str(self.grid[3][0] + 1) + " " + str(self.grid[4][0] + 1) + " " + str(self.grid[5][0] + 1)
        lowRow = str(self.grid[0][0] + 1) + " " + str(self.grid[1][0] + 1) + " " + str(self.grid[2][0] + 1)

        print(topRow)
        print(midRow)
        print(lowRow)


    def run(self, numberOfTimestamps, node):

        timestamp = 0


        numCollector = [[0 for x in range(2)] for y in range(9)]

        for i in range(9):
            numCollector[i][0] = i
            numCollector[i][1] = 0


        currentnode = node

        print(currentnode + 1)

        while(timestamp != numberOfTimestamps):
            moveSpace = ran.randint(1, 4)
            newNode = self.grid[currentnode][moveSpace]

            if(newNode != -1):

                timestamp = timestamp + 1
                currentnode = newNode

                numCollector[currentnode][1] = numCollector[currentnode][1] + 1

                #print(currentnode + 1)

            else:
                timestamp = timestamp + 1

                numCollector[currentnode][1] = numCollector[currentnode][1] + 1
                #print("Out")


        for i in range(9):
            print(str(numCollector[i][0] + 1) + ": " + str(numCollector[i][1]))






class FunkyNeighbourTable():

    grid = [[0 for x in range(5)] for y in range(9)]

    transitionWeights = [[0 for x in range(5)] for y in range(9)]

    def __init__(self):


        for i in range(9):
            for j in range(5):
                if(j == 0):
                    self.transitionWeights[i][j] = i
                    self.grid[i][j] = i
                else:
                    self.grid[i][j] = -1

        #Node 1

        self.grid[0][1] = 1
        self.grid[0][2] = 3

        self.transitionWeights [0][1] =
        self.transitionWeights [0][2] =


        #Node 2

        self.grid[1][1] = 2
        self.grid[1][2] = 4
        self.grid[1][3] = 0

        #Node 3

        self.grid[2][2] = 5
        self.grid[2][3] = 1

        #Node 4

        self.grid[3][1] = 4
        self.grid[3][2] = 6
        self.grid[3][4] = 0

        # Node 5

        self.grid[4][1] = 5
        self.grid[4][2] = 7
        self.grid[4][3] = 3
        self.grid[4][4] = 1

        # Node 6

        self.grid[5][2] = 8
        self.grid[5][3] = 4
        self.grid[5][4] = 2

        # Node 7

        self.grid[6][1] = 7
        self.grid[6][4] = 3

        # Node 8

        self.grid[7][1] = 8
        self.grid[7][3] = 6
        self.grid[7][4] = 4

        # Node 9

        self.grid[8][3] = 7
        self.grid[8][4] = 5

    def printGrid(self):

        topRow = str(self.grid[6][0] + 1) + " " + str(self.grid[7][0] + 1) + " " + str(self.grid[8][0] + 1)
        midRow = str(self.grid[3][0] + 1) + " " + str(self.grid[4][0] + 1) + " " + str(self.grid[5][0] + 1)
        lowRow = str(self.grid[0][0] + 1) + " " + str(self.grid[1][0] + 1) + " " + str(self.grid[2][0] + 1)

        print(topRow)
        print(midRow)
        print(lowRow)


    def run(self, numberOfTimestamps, node):

        timestamp = 0


        numCollector = [[0 for x in range(2)] for y in range(9)]

        for i in range(9):
            numCollector[i][0] = i
            numCollector[i][1] = 0


        currentnode = node

        print(currentnode + 1)

        while(timestamp != numberOfTimestamps):
            moveSpace = ran.randint(1, 4)
            newNode = self.grid[currentnode][moveSpace]

            if(newNode != -1):

                timestamp = timestamp + 1
                currentnode = newNode

                numCollector[currentnode][1] = numCollector[currentnode][1] + 1

                #print(currentnode + 1)

            else:
                timestamp = timestamp + 1

                numCollector[currentnode][1] = numCollector[currentnode][1] + 1
                #print("Out")


        for i in range(9):
            print(str(numCollector[i][0] + 1) + ": " + str(numCollector[i][1]))


print(sample(8000))
print(sampleRando(4000))

grido = StandardNeighbourTable()
grido.printGrid()
print()
grido.run(100000,0)


