import numpy as np

class Calculations():

    emptyNode = np.array([255, 255, 255])
    obstacleNode = np.array([0, 0, 0])
    startNode = np.array([71, 181, 69])
    endNode = np.array([214, 71, 49])

    def isNodeEmpty(arrayValues):
        return (np.array_equal(arrayValues, Calculations.emptyNode))
    
    def isNodeObstacle(arrayValues):
        return (np.array_equal(arrayValues, Calculations.obstacleNode))
    
    def isNodeStart(arrayValues):
        return (np.array_equal(arrayValues, Calculations.startNode))
    
    def isNodeEnd(arrayValues):
        return (np.array_equal(arrayValues, Calculations.endNode))

    def randomGridValue(max):
        return np.random.randint(0, max)
    
    def calculateAmountOfObstacles(gridWidth, gridHeight, obstaclePercent):
        return round((gridHeight * gridWidth) * obstaclePercent)

    def grassfireComputation(gridWidth, gridHeight, obstaclePercent):

        grid = np.random.randint(255,256, (gridWidth, gridHeight, 3), dtype=np.uint8)
        startNodeX = Calculations.randomGridValue(gridWidth)
        startNodeY = Calculations.randomGridValue(gridHeight)

        grid[startNodeX, startNodeY] = Calculations.startNode

        endNodeY = Calculations.randomGridValue(gridHeight)

        while True:
            endNodeX = Calculations.randomGridValue(gridWidth)

            if (startNodeX != endNodeX):
                break
        
        grid[endNodeX, endNodeY] = Calculations.endNode

        amountOfObstacles = Calculations.calculateAmountOfObstacles(gridWidth, gridHeight, obstaclePercent)

        while (amountOfObstacles != 0):
            obsX = Calculations.randomGridValue(gridWidth)
            obsY = Calculations.randomGridValue(gridHeight)
            possibleObstacleNode = grid[obsX, obsY]

            if not(Calculations.isNodeObstacle(possibleObstacleNode) or Calculations.isNodeStart(possibleObstacleNode) or Calculations.isNodeEnd(possibleObstacleNode)):
                grid[obsX, obsY] =  Calculations.obstacleNode
                amountOfObstacles -= 1
        
        return grid