import numpy as np

class Grid():

    grid = gridWidth = gridHeight = obstaclePercent = startNodeX = startNodeY = endNodeX = endNodeY = amountOfObstacles = 0
    emptyNode = np.array([255, 255, 255])
    obstacleNode = np.array([0, 0, 0])
    startNode = np.array([71, 181, 69])
    endNode = np.array([214, 71, 49])

    def isNodeEmpty(arrayValues):
        return (np.array_equal(arrayValues, Grid.emptyNode))
    
    def isNodeObstacle(arrayValues):
        return (np.array_equal(arrayValues, Grid.obstacleNode))
    
    def isNodeStart(arrayValues):
        return (np.array_equal(arrayValues, Grid.startNode))
    
    def isNodeEnd(arrayValues):
        return (np.array_equal(arrayValues, Grid.endNode))

    def randomGridValueX():
        return np.random.randint(0, Grid.gridWidth)
    
    def randomGridValueY():
        return np.random.randint(0, Grid.gridHeight)

    def calculateAmountOfObstacles():
        Grid.amountOfObstacles = round((Grid.gridHeight * Grid.gridWidth) * Grid.obstaclePercent)

    def calculateStartNode():
        Grid.startNodeX = Grid.randomGridValueX()
        Grid.startNodeY = Grid.randomGridValueY()
        Grid.grid[Grid.startNodeX, Grid.startNodeY] = Grid.startNode
    
    def calculateEndNode():
        Grid.endNodeY = Grid.randomGridValueY()

        while True:
            Grid.endNodeX = Grid.randomGridValueX()
            if (Grid.startNodeX != Grid.endNodeX): break
        
        Grid.grid[Grid.endNodeX, Grid.endNodeY] = Grid.endNode

    def gridComputation(gridWidth, gridHeight, obstaclePercent):
        Grid.grid = np.random.randint(255,256, (gridWidth, gridHeight, 3), dtype=np.uint8)
        Grid.gridWidth = gridWidth
        Grid.gridHeight = gridHeight
        Grid.obstaclePercent = obstaclePercent

        Grid.calculateStartNode()
        Grid.calculateEndNode()
        Grid.calculateAmountOfObstacles()

        while (Grid.amountOfObstacles != 0):
            obsX = Grid.randomGridValueX()
            obsY = Grid.randomGridValueY()

            if (Grid.isNodeEmpty(Grid.grid[obsX, obsY])):
                Grid.grid[obsX, obsY] =  Grid.obstacleNode
                Grid.amountOfObstacles -= 1
        
        return Grid.grid