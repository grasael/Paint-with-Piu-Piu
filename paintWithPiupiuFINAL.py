from cmu_112_graphics import *
import math
import ast

##########################################
# Home Page Screen Mode
##########################################

#from https://www.cs.cmu.edu/~112/notes/notes-graphics.html
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def newPaintingButton(app, canvas):
    font = 'Times 15'
    canvas.create_rectangle(app.width//2 - 100, 225, app.width//2 + 100, 275,fill='white')
    canvas.create_text(app.width//2, 250, text='new painting', font=font)

def openPaintingButton(app, canvas):
    font = 'Times 15'
    canvas.create_rectangle(app.width//2 - 100, 300, app.width//2 + 100, 350,fill='white')
    canvas.create_text(app.width//2, 325, text='open painting', font=font)

def drawErrorMsg(app, canvas):
    font = 'Times 15'
    canvas.create_text(app.width//2, app.height - 40, 
    text='No previous painting found. Please select new painting.', fill='red')
    canvas.create_image(app.width//2 + 180, app.height - 60, image=ImageTk.PhotoImage(app.errorPiupiuScale))

def homePageScreenMode_redrawAll(app, canvas):
    background = rgbString(246,210,177)
    canvas.create_rectangle(0, 0, app.width, app.height, fill=background)
    fontMain = 'Times 25 bold'
    fontSub = 'Times 16'
    #symbols from https://cutekaomoji.com/misc/sparkles/
    canvas.create_text(app.width//2, 10, 
        text='🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕', font=fontSub, fill='white')
    canvas.create_text(app.width//2, app.height - 10, 
        text='🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕 ┈┈┈┈ 🎕', font=fontSub, fill='white')
    canvas.create_text(app.width//2, 100, text='❀⑅*❀⑅*❀', font=fontSub)
    canvas.create_text(app.width//2, 415, text='❀⑅*❀⑅*❀', font=fontSub)
    canvas.create_text(app.width//2, 175, text='Paint with Piupiu', font=fontMain)
    newPaintingButton(app, canvas)
    openPaintingButton(app, canvas)
    canvas.create_image(app.width//2 - 180, app.height//2 + 60, image=ImageTk.PhotoImage(app.homePiupiuScale))
    if(app.cannotOpen == True):
        drawErrorMsg(app, canvas)
        
def homePageScreenMode_mousePressed(app, event):
    app.coordinates.append((event.x, event.y))
    if((app.width//2 - 100 <= event.x and event.x <= app.width//2 + 100) and 
                                        (225 <= event.y and event.y <= 275)):
        app.mode = 'paintMode'
    if((app.width//2 - 100 <= event.x <=  app.width//2 + 100) and 300 <= event.y <= 350):
        app.isOpen = True
        if(app.isOpen):
            app.isDrawing = True
            app.isCircle = True
            app.isOval = True
            app.isTriangle = True
            app.isStraightLine = True
            app.isErase = True
            app.isSave = False
            app.isScore = False
            app.lineI = 1
            app.triI = 1
            app.ovalI = 1
            app.circleI = 1
        try:
            contentOpen = ast.literal_eval(readFile("paintingData.txt"))
            for key in contentOpen:
                if(key == 'draw'):
                    app.drawCoord = ast.literal_eval(contentOpen[key])
                if(key == 'circle'):
                    app.circleCoord = ast.literal_eval(contentOpen[key])
                if(key == 'circle index'):
                    app.circleI = ast.literal_eval(contentOpen[key])
                if(key == 'oval'):
                    app.ovalCoord = ast.literal_eval(contentOpen[key])
                if(key == 'oval index'):
                    app.ovalI = ast.literal_eval(contentOpen[key])
                if(key == 'triangle1'):
                    app.triCoord = ast.literal_eval(contentOpen[key])
                if(key == 'triangle2'):
                    app.triList = ast.literal_eval(contentOpen[key])
                if(key == 'triangle index'):
                    app.triI = ast.literal_eval(contentOpen[key])
                if(key == 'line'):
                    app.lineCoord = ast.literal_eval(contentOpen[key])
                if(key == 'line index'):
                    app.lineI = ast.literal_eval(contentOpen[key])
                if(key == 'erase'):
                    app.eraseList = ast.literal_eval(contentOpen[key])
            app.mode = 'paintMode'
        except:
            app.cannotOpen = True

##########################################
# Paint Mode
##########################################

#drawing buttons for each tool
def drawPencilButton(app, canvas):
    canvas.create_rectangle(25, 25, 75, 75)

def drawCircleButton(app, canvas):
    canvas.create_rectangle(25, 75, 75, 125)

def drawOvalButton(app, canvas):
    canvas.create_rectangle(25, 125, 75, 175)

def drawTriangleButton(app, canvas):
    canvas.create_rectangle(25, 175, 75, 225)

def drawStraightLineButton(app, canvas):
    canvas.create_rectangle(25, 225, 75, 275)

def drawEraseButton(app, canvas):
    canvas.create_rectangle(25, 275, 75, 325)

def drawColorPalette(app, canvas):
    canvas.create_rectangle(50, app.height - 60, 100, app.height - 10, fill="white")
    canvas.create_rectangle(100, app.height - 60, 150, app.height - 10, fill='red')
    canvas.create_rectangle(150, app.height - 60, 200, app.height - 10, fill='pink')
    canvas.create_rectangle(200, app.height - 60, 250, app.height - 10, fill='orange')
    canvas.create_rectangle(250, app.height - 60, 300, app.height - 10, fill='yellow')
    canvas.create_rectangle(300, app.height - 60, 350, app.height - 10, fill='green')
    canvas.create_rectangle(350, app.height - 60, 400, app.height - 10, fill='blue')
    canvas.create_rectangle(400, app.height - 60, 450, app.height - 10, fill='purple')
    canvas.create_rectangle(450, app.height - 60, 500, app.height - 10, fill='brown')
    canvas.create_rectangle(500, app.height - 60, 550, app.height - 10, fill='black')

def drawSaveButton(app, canvas):
    canvas.create_rectangle(25, 325, 75, 375)

def drawScoreButton(app, canvas):
    canvas.create_rectangle(25, 375, 75, 425)

def drawCanvasBorder(app, canvas):
    canvas.create_rectangle(100, 75, 550, 425)

def drawFullnessScore(app, canvas):
    canvas.create_text(app.width//2 - 100, 45, text=f'fullness = {app.fullnessPercent}%')

def drawColorScore(app, canvas):
    canvas.create_text(app.width//2 - 15, 45, text=f'color = {app.colorScore}%')

def drawNeatnessScore(app, canvas):
    canvas.create_text(app.width//2 + 75, 45, text=f'neatness = {app.neatnessScore}%')

def drawAverageScore(app, canvas):
    canvas.create_text(app.width//2 + 170, 45, text=f'score = {app.averageScore}%')

def drawInstructionsBox(app, canvas):
    canvas.create_rectangle(125, 60, 550, 30, fill='white')
    
    if(app.isDefault == True):
        canvas.create_text(app.width - 255, 45, text=app.textList[0])
    if(app.isSave == True):
        #app.isDefault = False
        canvas.create_text(app.width - 255, 45, text=app.textList[1])

#from: https://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

#mouse functions
def paintMode_mousePressed(app, event):
    app.coordinates.append((event.x, event.y))
    if(25 <= event.x <= 75) and (25 <= event.y <= 75):
        app.tool = 'draw'
        app.isDrawing = True
    if(25 <= event.x <= 75) and (75 <= event.y <= 125):
        app.tool = 'circle'
        app.isCircle = True
    if(25 <= event.x <= 75) and (125 <= event.y <= 175):
        app.tool = 'oval'
        app.isOval = True
    if(25 <= event.x <= 75) and (175 <= event.y <= 225):
        app.tool = 'triangle'
        app.isTriangle = True
    if(25 <= event.x <= 75) and (225 <= event.y <= 275):
        app.tool = 'straight line'
        app.isStraightLine = True
    if(25 <= event.x <= 75) and (275 <= event.y <= 325):
        app.tool = 'erase'
        app.isErase = True
    if(25 <= event.x <= 75) and (325 <= event.y <= 375):
        app.isSave = True
        app.isDefault = False
        app.isScore = False
        if(len(app.drawCoord) > 1  or len(app.lineCoord) > 1 or len(app.circleCoord) > 1
         or len(app.ovalCoord) > 1 or len(app.triCoord) > 1 or len(app.eraseList) > 1):
            contentsToWrite = {
            'draw': repr(app.drawCoord),
            'circle': repr(app.circleCoord),            
            'circle index': repr(app.circleI),
            'oval': repr(app.ovalCoord),
            'oval index': repr(app.ovalI),
            'triangle1': repr(app.triCoord),
            'triangle2': repr(app.triList),
            'triangle index': repr(app.triI),
            'line': repr(app.lineCoord),
            'line index': repr(app.lineI),
            'erase': repr(app.eraseList)
            }
            writeFile("paintingData.txt", repr(contentsToWrite))
            contentsRead = ast.literal_eval(readFile("paintingData.txt"))
            assert(contentsRead == contentsToWrite)
            print("Open the file paintingData.txt and verify its contents.")

    if(25 <= event.x <= 75) and (375 <= event.y <= 425):
        app.tool = 'score'
        app.isScore = True
        app.isDefault = False
        app.isSave = False

    for i in range(50, 550, 50):
        if((i <= event.x and event.x <= i + 50) and 
                    (app.height - 60 <= event.y and event.y <= app.height - 10)):
            app.colorIndex = i//50 - 1
            app.color = app.colorList[app.colorIndex]

def paintMode_mouseDragged(app, event):
    if(app.tool == 'draw' and (100 <= event.x <= 550) and (75 <= event.y <= 425)):
        if(len(app.drawCoord) == 0):
            app.drawCoord.append([])
            app.drawCoord[0].append((event.x, event.y))
        elif(len(app.drawCoord) >= 1):
            app.drawCoord[-2].append((event.x, event.y))
    if(app.tool == 'circle' and (100 <= event.x <= 550) and (75 <= event.y <= 425)):
        if(len(app.circleCoord) == 0):
            app.circleCoord.append([])
            app.circleCoord[0].append((event.x, event.y))
        elif(len(app.circleCoord) >= 1):
            if((100 <= event.x <= 550) and (75 <= event.y <= 425)):
                pass
            app.circleCoord[-2].append((event.x, event.y))
    if(app.tool == 'oval' and (100 <= event.x <= 550) and (75 <= event.y <= 425)):
        if(len(app.ovalCoord) == 0):
            app.ovalCoord.append([])
            app.ovalCoord[0].append((event.x, event.y))
        elif(len(app.ovalCoord) >= 1):
            if((100 <= event.x <= 550) and (75 <= event.y <= 425)):
                pass
            app.ovalCoord[-2].append((event.x, event.y))
    if(app.tool == 'triangle' and (100 <= event.x <= 550) and (75 <= event.y <= 425)):
        if(len(app.triCoord) == 0):
            app.triCoord.append([])
            app.triCoord[0].append((event.x, event.y))
        elif(len(app.triCoord) >= 1):
            if((100 <= event.x <= 550) and (75 <= event.y <= 425)):
                pass
            app.triCoord[-2].append((event.x, event.y))
    if(app.tool == 'straight line' and (100 <= event.x <= 550) and (75 <= event.y <= 425)):
        if(len(app.lineCoord) == 0):
            app.lineCoord.append([])
            app.lineCoord[0].append((event.x, event.y))
        elif(len(app.lineCoord) >= 1):
            app.lineCoord[-2].append((event.x, event.y))
    if(app.tool == 'erase' and (100 <= event.x <= 550) and (75 <= event.y <= 425)):
        if(len(app.eraseList) == 0):
            app.eraseList.append([])
            app.eraseList[0].append((event.x, event.y))
        elif(len(app.eraseList) >= 1):
            app.eraseList[-1].append((event.x, event.y))

def paintMode_mouseReleased(app, event):
    if(app.tool == 'draw'):
        app.drawCoord[-1].append(app.color)
        app.drawCoord.append([])
    if(app.tool == 'circle'):
        app.circleCoord[-1].append(app.color)
        app.circleCoord.append([])
        app.circleI += 1
    if(app.tool == 'oval'):
        app.ovalCoord[-1].append(app.color)
        app.ovalCoord.append([])
        app.ovalI += 1
    if(app.tool == 'triangle'):
        app.triCoord[-1].append(app.color)
        app.triCoord.append([])
        app.triI += 1
        if(len(app.triCoord[app.triI-2])> 1):
            calculateTriangleCoord(app, app.triI-2)
        print("triCoord:", app.triCoord)

    if(app.tool == 'straight line'):
        app.lineCoord[-1].append(app.color)
        app.lineCoord.append([])
        app.lineI += 1
    if(app.tool == 'erase'):
        app.eraseList.append([])

    if(app.tool == 'score'):
        calculateFullness(app)
        calculateColorScore(app)
        calculateNeatnessScore(app)
        calculateAverageScore(app)

#tool functions
def draw(app, canvas):
    if(app.isDrawing):
        for i in range(len(app.drawCoord)):
            for j in range(1, len(app.drawCoord[i])-1):
                canvas.create_line(app.drawCoord[i][j][0], app.drawCoord[i][j][1], 
                            app.drawCoord[i][j+1][0], app.drawCoord[i][j+1][1], fill = app.drawCoord[i][0],
                smooth = True)

def erase(app, canvas):
    if(app.isErase):
        for i in range(len(app.eraseList)):
            for j in range(len(app.eraseList[i])-1):
                canvas.create_line(app.eraseList[i][j][0], app.eraseList[i][j][1], 
                            app.eraseList[i][j+1][0], app.eraseList[i][j+1][1], fill='white')    

def circleRadius(app, i):
    if(len(app.circleCoord[i]) > 1):
        x1 = app.circleCoord[i][1][0]
        y1 = app.circleCoord[i][1][1]
        x2 = app.circleCoord[i][-1][0]
        y2 = app.circleCoord[i][-1][1]
        if(100 > x2):
            x2 = abs(x1-100)
        elif(x2 > 550):
            x2 = abs(x1-550)
        if(75 > y2):
            y2 = abs(y1-75)
        elif(y2 > 425):
            y2 = abs(y1-425)
        radius = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return radius

def isLegalCircle(app, cx, cy, cr):
    if((100 < cx + cr < 550) and (100 < cx - cr < 550) and 
        (75 < cy + cr < 425) and (75 < cy - cr < 425)):
        return True
    else:
        return False

def circle(app, canvas):
    if(app.isCircle):
        for i in range(0, app.circleI):
            if(len(app.circleCoord[i]) > 1):
                if(isLegalCircle(app, app.circleCoord[i][1][0], 
                app.circleCoord[i][1][1], circleRadius(app, i))):
                    canvas.create_oval(app.circleCoord[i][1][0]-circleRadius(app, i), 
                        app.circleCoord[i][1][1]+circleRadius(app, i), 
                        app.circleCoord[i][1][0]+circleRadius(app, i),
                        app.circleCoord[i][1][1]-circleRadius(app, i), outline = app.circleCoord[i][0])

def ovalRadius(app, i):
    if(len(app.ovalCoord[i]) > 1):
        x1 = app.ovalCoord[i][1][0]
        y1 = app.ovalCoord[i][1][1]
        x2 = app.ovalCoord[i][-1][0]
        y2 = app.ovalCoord[i][-1][1]
        if(100 > x2):
            x2 = abs(x1-100)
        elif(x2 > 550):
            x2 = abs(x1-550)
        if(75 > y2):
            y2 = abs(y1-75)
        elif(y2 > 425):
            y2 = abs(y1-425)
        radius = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return radius

def isLegalOval(app, cx, cy, cr):
    if((100 < cx + cr < 550) and (100 < cx - cr < 550) and 
        (75 < cy + cr//2 < 425) and (75 < cy - cr//2 < 425)):
        return True
    else:
        return False

def oval(app, canvas):
    if(app.isOval):
        for i in range(0, app.ovalI):
            if(len(app.ovalCoord[i]) > 1):
                if(isLegalOval(app, app.ovalCoord[i][1][0], 
                app.ovalCoord[i][1][1], ovalRadius(app, i))):
                    canvas.create_oval(app.ovalCoord[i][1][0]-ovalRadius(app, i), 
                            app.ovalCoord[i][1][1]+ovalRadius(app, i)//2, 
                            app.ovalCoord[i][1][0]+ovalRadius(app, i),
                            app.ovalCoord[i][1][1]-ovalRadius(app, i)//2, outline = app.ovalCoord[i][0])

def calculateTriangleCoord(app, i):
    if(len(app.triCoord) > 1):
        if(len(app.triCoord[i]) >= 3):
            firstClickX = app.triCoord[i][1][0]
            firstClickY = app.triCoord[i][1][1]
            lastClickX = app.triCoord[i][-1][0]
            print("lastClickX:", lastClickX)
            lastClickY = app.triCoord[i][-1][1]
            topX = firstClickX + (firstClickX - lastClickX)//2
            topY = firstClickY
            bottomLeftX = lastClickX
            bottomLeftY = firstClickY + (firstClickY - lastClickY) // 2
            bottomRightX = lastClickX
            bottomRightY = lastClickY
            app.triList.append((app.triCoord[i][0], topX, topY, bottomLeftX, bottomLeftY, bottomRightX,
                                bottomRightY))

def isLegalTriangle(app, topX, topY, bottomLeftX, bottomLeftY, bottomRightX,
                             bottomRightY):
    if((100 < topX < 550) and (100 < bottomLeftX < 550) and (100 < bottomRightX < 550)
        and (75 < topY < 425) and (75 < bottomLeftY < 425) and (75 < bottomRightY < 425)):
        return True
    else:
        return False

def triangle(app, canvas):
    if(app.isTriangle):
        for i in range(0, len(app.triList)):
            if(len(app.triList[i]) > 1):
                if(isLegalTriangle(app, app.triList[i][1], app.triList[i][2],
                    app.triList[i][3], app.triList[i][4], app.triList[i][5],
                    app.triList[i][6])):
                    canvas.create_polygon(app.triList[i][1], app.triList[i][2],
                    app.triList[i][3], app.triList[i][4], app.triList[i][5],
                    app.triList[i][6], fill="", outline = app.triList[i][0], width = 1)
    
def straightLine(app, canvas):
    for i in range(0, app.lineI):
        if(len(app.lineCoord[i]) > 1):
            canvas.create_line(app.lineCoord[i][1][0], app.lineCoord[i][1][1], 
                                app.lineCoord[i][-1][0], app.lineCoord[i][-1][1],
                                fill = app.lineCoord[i][0], width = 2)

def distance(app, x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculateFullness(app):
    drawPerimeter = 0
    lineDistance = 0
    circleCircum = 0
    ovalCircum = 0
    triPerimeter = 0
    if(len(app.drawCoord) > 1  or len(app.lineCoord) > 1 or len(app.circleCoord) > 1
         or len(app.ovalCoord) > 1 or len(app.triCoord) > 1):
        for i in range(len(app.drawCoord)):
            for j in range(1, len(app.drawCoord[i])-1):
                drawPerimeter += distance(app, app.drawCoord[i][j][0], app.drawCoord[i][j][1],
                        app.drawCoord[i][j+1][0], app.drawCoord[i][j+1][1])
        for i in range(0, app.lineI):
            if(len(app.lineCoord[i]) > 1):
                lineDistance += distance(app, app.lineCoord[i][1][0], app.lineCoord[i][1][1], 
                                app.lineCoord[i][-1][0], app.lineCoord[i][-1][1])
        for i in range(0, app.circleI):
            if(len(app.circleCoord[i]) > 1):
                circleCircum += 2 * math.pi * circleRadius(app, i)
        for i in range(0, app.ovalI):
            if(len(app.ovalCoord[i]) > 1):
                ovalCircum += 2 * math.pi * math.sqrt((ovalRadius(app, i)**2 + (ovalRadius(app, i)//2)**2))//2
        for i in range(0, len(app.triList)):
            if(len(app.triList[i]) > 1):
                triPerimeter += (distance(app, app.triList[i][1], app.triList[i][2], app.triList[i][3],
                    app.triList[i][4]) + distance(app, app.triList[i][3], app.triList[i][4], app.triList[i][5],
                    app.triList[i][6]) + distance(app, app.triList[i][1], app.triList[i][2], app.triList[i][5],
                    app.triList[i][6]))
    totalPerimeter = drawPerimeter + lineDistance + circleCircum + ovalCircum + triPerimeter 
    totalCanvasArea = 450 * 350
    app.fullnessPercent = round((totalPerimeter / totalCanvasArea) * 100, 2)
    
def calculateColorScore(app):
    score = 0
    if(len(app.drawCoord) > 1  or len(app.lineCoord) > 1 or len(app.circleCoord) > 1
         or len(app.ovalCoord) > 1 or len(app.triCoord) > 1):
        for i in range(len(app.drawCoord)):
            for j in range(1, len(app.drawCoord[i])-1):
                app.colorScoreSet.add(app.drawCoord[i][0])
        for i in range(0, app.lineI):
            if(len(app.lineCoord[i]) > 1):
                app.colorScoreSet.add(app.lineCoord[i][0])
        for i in range(0, app.circleI):
            if(len(app.circleCoord[i]) > 1):
                app.colorScoreSet.add(app.circleCoord[i][0])
        for i in range(0, app.ovalI):
            if(len(app.ovalCoord[i]) > 1):
                app.colorScoreSet.add(app.ovalCoord[i][0])
        for i in range(0, len(app.triList)):
            if(len(app.triList[i]) > 1):
                app.colorScoreSet.add(app.triList[i][0])
        #There are 5 categories: achromatic, monochromatic, complimetary, color diad
        # and color triad. +10 points for each category that is met through
        # certain color combinations
        ############################
        # Achromatic
        if('white' and 'black' in app.colorScoreSet):
            score += 20
        #Monochromatic
        if(('red' in app.colorScoreSet) and ('pink' in app.colorScoreSet)
        or ('orange' in app.colorScoreSet) and ('brown' in app.colorScoreSet)):
            score += 20
        #Complimetary
        if(('red' in app.colorScoreSet) and ('green'  in app.colorScoreSet) or 
        ('orange' in app.colorScoreSet) and ('blue' in app.colorScoreSet) 
        or ('yellow'  in app.colorScoreSet) and ('purple' in app.colorScoreSet)):
            score += 20
        #Color Diad
        if(('red'  in app.colorScoreSet) and ('orange' in app.colorScoreSet) or 
        ('orange'  in app.colorScoreSet) and ('yellow' in app.colorScoreSet) 
        or ('yellow'  in app.colorScoreSet) and ('green' in app.colorScoreSet) or 
        ('green' in app.colorScoreSet) and ('blue' in app.colorScoreSet) or 
        ('blue' in app.colorScoreSet) and ('purple' in app.colorScoreSet)):
            score += 20
        #Color Triad
        if(('red' in app.colorScoreSet) and ('yellow' in app.colorScoreSet) and 
        ('blue' in app.colorScoreSet) or ('orange' in app.colorScoreSet) and 
        ('green' in app.colorScoreSet) and ('purple' in app.colorScoreSet)):
            score += 20
        app.colorScore = score
    
def findAngle(app, x1, y1, x2, y2, x3, y3):
    sideA = distance(app, x1, y1, x2, y2)
    sideB = distance(app, x2, y2, x3, y3)
    sideC = distance(app, x3, y3, x1, y1)
    #trying to find the angle of c
    angleC = math.degrees(math.acos((sideC**2-sideA**2-sideB**2)/(-2*(sideA)*(sideB))))
    return angleC

def calculateNeatnessScoreHelper(app):
    listCounter = 0
    miniLineAngleList = []
    for i in range(len(app.drawCoord)):
        miniLineAngleList.append([])
        for j in range(1, len(app.drawCoord[i])-2):
            miniLineAngle = findAngle(app, app.drawCoord[i][j][0], 
            app.drawCoord[i][j][1], app.drawCoord[i][j+1][0], app.drawCoord[i][j+1][1],
            app.drawCoord[i][j+2][0], app.drawCoord[i][j+2][1])
            miniLineAngleList[listCounter].append(round(miniLineAngle, 2))
        listCounter += 1
    return miniLineAngleList

def angleDifference(app, L):
    differenceList = []
    for list in range(len(L)):
        if(L[list] != []):
            biggestAngle = max(L[list])
            smallestAngle = min(L[list])
            difference = biggestAngle - smallestAngle
            differenceList.append(difference)
    sumDiff = sum(differenceList)
    averageDiff = sumDiff/len(differenceList)
    return averageDiff

def calculateNeatnessScore(app):
    if(len(app.drawCoord[0]) < 1 or len(app.circleCoord[0]) > 1 or len(app.ovalCoord[0]) > 1
    or len(app.triCoord[0]) > 1 or len(app.lineCoord[0]) > 1):
        app.neatnessScore = 100
    elif(len(app.drawCoord[0]) > 1):
        app.neatnessScore = round((1 - (angleDifference(app, calculateNeatnessScoreHelper(app)))/180) * 100, 2)

def calculateAverageScore(app):
    app.averageScore = round((app.fullnessPercent + app.colorScore + app.neatnessScore)/3, 2)

def paintMode_redrawAll(app, canvas):
    drawInstructionsBox(app, canvas)
    background = rgbString(246,210,177)
    canvas.create_rectangle(0, 0, 100, app.height, fill=background, outline='')
    canvas.create_rectangle(100, 0, app.width, 75, fill=background, outline='')
    canvas.create_rectangle(100, 425, app.width, app.height, fill=background, outline='')
    canvas.create_rectangle(550, 75, app.width, app.height-60, fill=background, outline='')
    drawInstructionsBox(app, canvas)
    font = 'Times 20 bold'
    canvas.create_image(app.width//2 - 184, 40, image=ImageTk.PhotoImage(app.helpPiupiuScale))
    canvas.create_image(50, 50, image=ImageTk.PhotoImage(app.imageDrawScale))
    drawPencilButton(app, canvas)
    canvas.create_image(50, 100, image=ImageTk.PhotoImage(app.imageCircleScale))
    drawCircleButton(app, canvas)
    canvas.create_image(50, 150, image=ImageTk.PhotoImage(app.imageOvalScale))
    drawOvalButton(app, canvas)
    canvas.create_image(50, 200, image=ImageTk.PhotoImage(app.imageTriangleScale))
    drawTriangleButton(app, canvas)
    canvas.create_image(50, 250, image=ImageTk.PhotoImage(app.imageLineScale))
    drawStraightLineButton(app, canvas)
    drawColorPalette(app, canvas)
    canvas.create_image(50, 300, image=ImageTk.PhotoImage(app.imageEraseScale))
    drawEraseButton(app, canvas)
    canvas.create_image(50, 350, image=ImageTk.PhotoImage(app.imageSaveScale))
    drawSaveButton(app, canvas)
    canvas.create_image(50, 400, image=ImageTk.PhotoImage(app.imageScoreScale))
    drawScoreButton(app, canvas)
    drawCanvasBorder(app, canvas)
    
    if(app.isScore):
        drawFullnessScore(app, canvas)
        drawColorScore(app, canvas)
        drawNeatnessScore(app, canvas)
        drawAverageScore(app, canvas)
    
    draw(app, canvas)
    circle(app, canvas)
    oval(app, canvas)
    triangle(app, canvas)
    straightLine(app, canvas)
    erase(app, canvas)
    
##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'homePageScreenMode'
    app.coordinates = []
    app.drawCoord = [[]]
    #all images of icons used with attributions
    #from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">
    # Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageDraw = app.loadImage('drawP.png')
    app.imageDrawScale = app.scaleImage(app.imageDraw, 1/14)
    #from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">
    # Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageCircle = app.loadImage('circle.png')
    app.imageCircleScale = app.scaleImage(app.imageCircle, 1/14)
    #from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">
    # Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageOval = app.loadImage('oval.png')
    app.imageOvalScale = app.scaleImage(app.imageOval, 1/14)
    #from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">
    # Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageTriangle = app.loadImage('triangleP.png')
    app.imageTriangleScale = app.scaleImage(app.imageTriangle, 1/14)
    #from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">
    # Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageLine = app.loadImage('line.png')
    app.imageLineScale = app.scaleImage(app.imageLine, 1/14)
    #from <div>Icons made by <a href="https://www.flaticon.com/authors/dave-gandy" 
    # title="Dave Gandy">Dave Gandy</a> from <a href="https://www.flaticon.com/" 
    # title="Flaticon">www.flaticon.com</a></div>
    app.imageErase = app.loadImage('eraseP.png')
    app.imageEraseScale = app.scaleImage(app.imageErase, 1/14)
    #from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">
    # Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageSave = app.loadImage('saveP.png')
    app.imageSaveScale = app.scaleImage(app.imageSave, 1/14)
    #from <div>Icons made by <a href="https://www.flaticon.com/authors/octopocto"
    #  title="Octopocto">Octopocto</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    app.imageScore = app.loadImage('three-stars.png')
    app.imageScoreScale = app.scaleImage(app.imageScore, 1/14)
    #from https://pin.it/2xz9N2K
    app.errorPiupiu = app.loadImage('piupiu1t.png')
    app.errorPiupiuScale = app.scaleImage(app.errorPiupiu, 1/3)
    #from https://favpng.com/png_search/molang
    app.helpPiupiu = app.loadImage('piupiu3t.png')
    app.helpPiupiuScale = app.scaleImage(app.helpPiupiu, 1/5)
    #from https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%
    # 2Fpin%2F774548835908983872%2F&psig=AOvVaw1cLspJ4ZS4IaXr1FjvGsD_&ust=163847
    # 7810139000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJjT2NG7w_QCFQAAAAAdAAAAABAD
    app.homePiupiu = app.loadImage('piupiuHomet.png')
    app.homePiupiuScale = app.scaleImage(app.homePiupiu, 1/7)
    #color palette variables
    app.colorList = ['white', 'red', 'pink', 'orange', 'yellow', 'green', 'blue',
                    'purple', 'brown', 'black']
    app.colorRGBList = [(255, 255, 255), (254, 0, 0), (255, 192, 203), (254, 164, 0), 
        (254, 250, 29), (0, 128, 1), (0, 0, 254), (129, 0, 127), (0, 0, 0)]
    app.colorIndex = 0
    app.color = app.colorList[app.colorIndex]
    app.tool = ''
    #circle 
    app.circleCoord = [[]]
    app.circleRadius = 0
    app.circleI = 0
    #oval
    app.ovalCoord = [[]]
    app.ovalRadius = 0
    app.ovalI = 0
    #triangle
    app.triCoord = [[]]
    app.triList = []
    app.triRadius = 0
    app.triI = 0
    #straightLine
    app.lineCoord = [[]]
    app.lineI = 0
    #a bunch of booleans for tools
    app.isDrawing = False
    app.isCircle = False
    app.isOval = False
    app.isTriangle = False
    app.isStraightLine = False
    app.isErase = False
    app.isSave = False
    #erase
    app.eraseList = []
    #open
    app.isOpen = False
    app.cannotOpen = False
    #score
    app.isScore = False
    app.fullnessPercent = 0
    app.colorScore = 0
    app.colorScoreSet = set()
    app.neatnessScore = 0
    app.averageScore = 0

    app.isDefault = True

    app.textList = ['Welcome! Click on a color from the color palette, and then a tool on the left.',
    'Your painting is saved in paintData.txt. You may close the application now.']

runApp(width=600, height=500)