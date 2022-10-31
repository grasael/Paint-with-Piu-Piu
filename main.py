from cmu_112_graphics import *

def appStarted(app): 
    app.coordinates = []

def mouseDragged(app, event):
    if(len(app.coordinates) == 0):
        app.coordinates.append([])
        app.coordinates[0].append((event.x, event.y))
    elif(len(app.coordinates) >= 1):
        app.coordinates[-1].append((event.x, event.y))

def mouseReleased(app, event):
    app.coordinates.append([])
    print(app.coordinates)

def draw(app, canvas):
    for i in range(len(app.coordinates)):
        for j in range(len(app.coordinates[i])-1):
            canvas.create_line(app.coordinates[i][j][0], app.coordinates[i][j][1], 
                            app.coordinates[i][j+1][0], app.coordinates[i][j+1][1])

def redrawAll(app, canvas):
    draw(app, canvas)

runApp(width=600, height=600)
