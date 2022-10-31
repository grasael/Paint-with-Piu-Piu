from cmu_112_graphics import *

def appStarted(app): 
    app.coordinates = []
    app.eraseList = []
    app.isErasing = False
    app.isDrawing = True

def keyPressed(app, event):
    if(event.key == 'e'):
        app.isErasing = True
        app.isDrawing = False
    if(event.key == 'd'):
        app.isDrawing = True
        app.isErasing = False

def mouseDragged(app, event):
    if(app.isDrawing):
        if(len(app.coordinates) == 0):
            app.coordinates.append([])
            app.coordinates[0].append((event.x, event.y))
        elif(len(app.coordinates) >= 1):
            app.coordinates[-1].append((event.x, event.y))
    elif(app.isErasing):
        if(len(app.eraseList) == 0):
            app.eraseList.append([])
            app.eraseList[0].append((event.x, event.y))
        elif(len(app.eraseList) >= 1):
            app.eraseList[-1].append((event.x, event.y))

def mouseReleased(app, event):
    if(app.isDrawing):
        app.coordinates.append([])
    elif(app.isErasing):
        app.eraseList.append([])

def draw(app, canvas):
    for i in range(len(app.coordinates)):
        for j in range(len(app.coordinates[i])-1):
            canvas.create_line(app.coordinates[i][j][0], app.coordinates[i][j][1], 
                            app.coordinates[i][j+1][0], app.coordinates[i][j+1][1])

def erase(app, canvas):
    for i in range(len(app.eraseList)):
        for j in range(len(app.eraseList[i])-1):
            canvas.create_line(app.eraseList[i][j][0], app.eraseList[i][j][1], 
                            app.eraseList[i][j+1][0], app.eraseList[i][j+1][1], fill='white')

def redrawAll(app, canvas):
    draw(app, canvas)
    erase(app, canvas)

runApp(width=600, height=600)
