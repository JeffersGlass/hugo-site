from random import randint
from js import setInterval, document, DOMParser
from pyodide import create_proxy

class PathFollower:
    def __init__(self, canvas, width, height, numPoints = 10):
        self.numPoints = numPoints
        self.width = width
        self.height = height
        self.ctx = canvas.getContext("2d")
        
        canvas.style.width = f"{width}px"
        canvas.style.height = f"{height}px"

        canvas.width = width
        canvas.height = height
        self.randomizePath()
        print(self.pathPoints)

    def getNewPoint(self):
        return (randint(2,self.width-2), randint(2, self.height-2))
    
    def randomizePath(self):
        self.pathPoints = [self.getNewPoint() for _ in range(self.numPoints)]

    def movePath(self):
        self.pathPoints = self.pathPoints[1:]
        self.pathPoints.append(self.getNewPoint())

    def clearPath(self):
        self.ctx.clearRect(0,0,1000,1000)
    
    def drawPath(self):
        self.ctx.beginPath()    
        self.ctx.moveTo(*self.pathPoints[0])
        for i, point in enumerate(self.pathPoints[1:]):
            self.ctx.lineTo(*point)
            self.ctx.stroke()

    def remakePath(self):
        self.clearPath()
        #self.randomizePath()
        self.movePath()
        self.drawPath()

    def start(self, interval):
        setInterval(create_proxy(self.remakePath), interval)


        