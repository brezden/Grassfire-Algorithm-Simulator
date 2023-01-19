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