from cmu_112_graphics import *
import math

def appStarted(app): 
    app.coordinates = []
    app.radius = 0
    app.i = 0

def mouseDragged(app, event):
    if(len(app.coordinates) == 0):
        app.coordinates.append([])
        app.coordinates[0].append((event.x, event.y))
    elif(len(app.coordinates) >= 1):
        app.coordinates[-1].append((event.x, event.y))

def mouseReleased(app, event):
    app.coordinates.append([])
    app.i += 1
    print(app.coordinates)

def radius(app, i):
    x1 = app.coordinates[i][0][0]
    y1 = app.coordinates[i][0][1]
    x2 = app.coordinates[i][-1][0]
    y2 = app.coordinates[i][-1][1]
    radius = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(i)
    return radius

def oval(app, canvas):
    for i in range(0, app.i):
        if(len(app.coordinates) != 0):
            canvas.create_oval(app.coordinates[i][0][0]-radius(app, i), 
                        app.coordinates[i][0][1]+radius(app, i)//2, 
                        app.coordinates[i][0][0]+radius(app, i),
                        app.coordinates[i][0][1]-radius(app, i), fill = '')

def redrawAll(app, canvas):
    oval(app, canvas)

runApp(width=600, height=600)