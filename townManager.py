def townGenerate(matrix, posX, posY, size, townList):
    topLeftX = posX - size - 1
    topLeftY = posY - 2
    town = Town((topLeftX, topLeftY), (topLeftX + size*2, topLeftY + size*2), matrix)
    townList.append(town)
    return matrix, townList

class Town():
    def __init__(self, topLeft, bottomRight, matrix):
        topLeftX, topLeftY = topLeft
        bottomRightX, bottomRightY = bottomRight
        size = topLeftX - bottomRightX
        width = size * 2 + 2
        for i in range(width):
            for j in range(width):
                matrix[topLeftX+i][posY+j] = "grass"
        for i in range(-size,size):
            matrix[posX+i][posY - 1] = "townWall"
            matrix[posX+i][posY + size*2] = "townWall"
            matrix[posX-size][posY+i+size] = "townWall"
            matrix[posX+size][posY+i+size] = "townWall"
        matrix[posX+size][posY-1] = "townWall"
        matrix[posX+size][posY+size*2] = "townWall"
        matrix[posX-1][posY+size*2] = "alter"
        matrix[posX][posY+size*2] = "alter"
        matrix[posX+1][posY+size*2] = "alter"
        matrix[posX-1][posY+size*2+1] = "alter"
        matrix[posX][posY+size*2+1] = "alter"
        matrix[posX+1][posY+size*2+1] = "alter"
        return matrix