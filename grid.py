import numpy as np

class Grid():

    grid = gridWidth = gridHeight = obstaclePercent = startNodeX = startNodeY = endNodeX = endNodeY = amountOfObstacles = 0
    emptyNode = np.array([255, 255, 255])
    obstacleNode = np.array([60, 0, 60])
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
    
    def calculateObstacles():
        while (Grid.amountOfObstacles != 0):
            obsX = Grid.randomGridValueX()
            obsY = Grid.randomGridValueY()

            if (Grid.isNodeEmpty(Grid.grid[obsX, obsY])):
                Grid.grid[obsX, obsY] =  Grid.obstacleNode
                Grid.amountOfObstacles -= 1

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
        Grid.calculateObstacles()
        return Grid.grid

class GridSearch():

    searchGrid = 0
    nodes = []
    
    def findShortestPath():
        GridSearch.searchGrid = Grid.grid
        GridSearch.searchGrid[Grid.startNodeX, Grid.startNodeY] = np.array([0, 0, 100])
        currentNodeCords = [Grid.startNodeX, Grid.startNodeY]
        GridSearch.nodes.append(currentNodeCords)

        while (len(GridSearch.nodes) != 0):
            node = GridSearch.nodes[0]
            del GridSearch.nodes[0]
            nodeX = node[0]
            nodeY = node[1]
            nodeDistance = (GridSearch.searchGrid[nodeX, nodeY])[0]

            GridSearch.searchNode(nodeX, nodeY - 1, nodeDistance + 1)
            GridSearch.searchNode(nodeX + 1, nodeY, nodeDistance + 1)
            GridSearch.searchNode(nodeX, nodeY + 1, nodeDistance + 1)
            GridSearch.searchNode(nodeX - 1, nodeY, nodeDistance + 1)
        
        print(GridSearch.searchGrid)
        return GridSearch.searchGrid

                    
    def searchNode(x, y, nodeDistance):
        if (GridSearch.validateNode(x, y)):
            print(GridSearch.searchGrid[x, y])
            GridSearch.searchGrid[x, y] = np.array([nodeDistance, nodeDistance, nodeDistance])
            print(GridSearch.searchGrid[x, y])
            GridSearch.nodes.append([x, y])

    def validateNode(x, y):
        if ((x >= Grid.gridWidth) or (x < 0)):
            return False
        
        if ((y >= Grid.gridHeight) or (y < 0)):
            return False
        
        if not(Grid.isNodeEmpty((GridSearch.searchGrid[x, y]))):
            return False

        return True