import numpy as np

class Grid():

    grid = distanceValue = totalDistance = gridWidth = gridHeight = obstaclePercent = startNodeX = startNodeY = endNodeX = endNodeY = amountOfObstacles = 0
    listOfPathCords = []
    emptyNode = np.array([255, 255, 255])
    obstacleNode = np.array([0, 0, 0])
    startNode = np.array([0, 100, 0])
    endNode = np.array([214, 71, 49])
    path = np.array([0, 167, 189])

    def isNodeEmpty(arrayValues):
        return (np.array_equal(arrayValues, Grid.emptyNode))
    
    def isNodeObstacle(arrayValues):
        return (np.array_equal(arrayValues, Grid.obstacleNode))
    
    def isNodeStart(arrayValues):
        return (np.array_equal(arrayValues, Grid.startNode))
    
    def isNodeEnd(arrayValues):
        return (np.array_equal(arrayValues, Grid.endNode))
    
    def isNodePath(arrayValues):
        return (np.array_equal(arrayValues, Grid.path))

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

class GridSlowMode():

    def printPathStep():
        if not(len(Grid.listOfPathCords) == 0):
            x = Grid.listOfPathCords.pop()
            Grid.grid[x[0], x[1]] = np.array([0, 167, 189])
            Grid.distanceValue += 1


class GridShortestPath():
    
    def findShortestDistanceValue(nodeX, nodeY):
        upNodeValue = GridShortestPath.searchNode(nodeX, nodeY - 1)
        rightNodeValue = GridShortestPath.searchNode(nodeX + 1, nodeY)
        downNodeValue = GridShortestPath.searchNode(nodeX, nodeY + 1)
        leftNodeValue = GridShortestPath.searchNode(nodeX - 1, nodeY)                

        x = [upNodeValue, rightNodeValue, downNodeValue, leftNodeValue]
        while 0 in x: x.remove(0)

        if (len(x) == 0):
            return 0

        return min(x)

    def findShortestPath(slowMode):
        GridSearch.findShortestPath()

        node = GridSearch.searchGrid[Grid.endNodeX, Grid.endNodeY]
        nodeX = Grid.endNodeX
        nodeY = Grid.endNodeY

        Grid.distanceValue = GridShortestPath.findShortestDistanceValue(nodeX, nodeY)

        counter = Grid.gridWidth * Grid.gridHeight
        i = 0

        while (i < counter):

            upNodeValue = GridShortestPath.searchNode(nodeX, nodeY - 1)
            rightNodeValue = GridShortestPath.searchNode(nodeX + 1, nodeY)
            downNodeValue = GridShortestPath.searchNode(nodeX, nodeY + 1)
            leftNodeValue = GridShortestPath.searchNode(nodeX - 1, nodeY)                

            x = [upNodeValue, rightNodeValue, downNodeValue, leftNodeValue]
            while 0 in x: x.remove(0)

            if (len(x) == 0):
                break

            x = min(x)

            if ((upNodeValue == 100) or (rightNodeValue == 100) or (downNodeValue == 100) or (leftNodeValue == 100)): break
            
            if (x == upNodeValue): nodeY = nodeY - 1
            elif (x == rightNodeValue): nodeX = nodeX + 1    
            elif (x == downNodeValue): nodeY = nodeY + 1
            else: nodeX = nodeX - 1

            if (slowMode == True):
                Grid.listOfPathCords.append([nodeX, nodeY])

            else:
                Grid.grid[nodeX, nodeY] = np.array([0, 167, 189])
            
            Grid.totalDistance += 1
            i += 1

        GridShortestPath.cleanGrid()

        return Grid.grid
    
    def searchNode(x, y):
        if (GridShortestPath.validateNode(x, y)):
            return (GridSearch.searchGrid[x, y])[1]

        return 0

    def validateNode(x, y):
        if ((x >= Grid.gridWidth) or (x < 0)):
            return False
        
        if ((y >= Grid.gridHeight) or (y < 0)):
            return False
   
        if (Grid.isNodeObstacle((Grid.grid[x, y]))):
            return False
                
        if (Grid.isNodeEnd((Grid.grid[x, y]))):
            return False

        return True

    def cleanGrid():
        for i in range(0, Grid.gridWidth, 1):
            for j in range(0, Grid.gridHeight, 1):
                if ((not(Grid.isNodeObstacle(Grid.grid[i, j]))) and (not(Grid.isNodeStart(Grid.grid[i, j]))) and (not(Grid.isNodeEnd(Grid.grid[i, j]))) and (not(Grid.isNodePath(Grid.grid[i, j])))):
                    Grid.grid[i,j] = np.array([255, 255, 255])


class GridSearch():

    searchGrid = 0
    nodes = []
    
    def findShortestPath():
        x = Grid.grid
        GridSearch.searchGrid = x
        GridSearch.searchGrid[Grid.startNodeX, Grid.startNodeY] = np.array([0, 100, 0])
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

        return GridSearch.searchGrid
                   
    def searchNode(x, y, nodeDistance):
        if (GridSearch.validateNode(x, y)):
            GridSearch.searchGrid[x, y] = np.array([nodeDistance, nodeDistance, nodeDistance])
            GridSearch.nodes.append([x, y])

    def validateNode(x, y):
        if ((x >= Grid.gridWidth) or (x < 0)):
            return False
        
        if ((y >= Grid.gridHeight) or (y < 0)):
            return False
        
        if not(Grid.isNodeEmpty((GridSearch.searchGrid[x, y]))):
            return False

        return True