from cmu_112_graphics import *

def appStarted(app): 
    app.coordinates = []
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

def straightLine(app, canvas):
    for i in range(0, app.i):
        if(len(app.coordinates) != 0):
            canvas.create_line(app.coordinates[i][0][0], app.coordinates[i][0][1], 
                                app.coordinates[i][-1][0], app.coordinates[i][-1][1],
                                fill = "black", width = 3)

def redrawAll(app, canvas):
    straightLine(app, canvas)

runApp(width=600, height=600)