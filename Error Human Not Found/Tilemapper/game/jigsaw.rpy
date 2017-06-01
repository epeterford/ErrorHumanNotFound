init python:
    def gate_dragged(drags,drop):
        if not drop:
                return
                
        if drop:
            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop
                if drags[0].drag_name == "and_gate":
                    #give the x and y of the drop 
                    #list of images to replace the old lines
                    return 
            return
                

        return 


screen logicGates:
    #row 125
    add "images/blankTile.png" pos(425,125)    
    add "images/blankTile.png" pos(525,125)  
    add "images/blankTile.png" pos(625,125)  
    add "images/blankTile.png" pos(725,125)  
    add "images/blankTile.png" pos(825,125)  
    add "images/blankTile.png" pos(925,125) 
    add "images/blankTile.png" pos(1025,125)  
    add "images/blankTile.png" pos(1125,125)  
    add "images/blankTile.png" pos(1225,125)  
    add "images/blankTile.png" pos(1325,125)  
    #row 225
    add "images/2_1.png" pos(325,225)     #start point 1
    add "images/horizontalB.png" pos(425,225)
    add "images/horizontalB.png" pos(525,225)
    add "images/horizontalB.png" pos(625,225)
    add "images/horizontalB.png" pos(725,225)
    add "images/cornBLB.png" pos(825,225)
    add "images/blankTile.png" pos(925,225)
    add "images/blankTile.png" pos(1025,225)
    add "images/blankTile.png" pos(1125,225)
    add "images/blankTile.png" pos(1225,225)
    add "images/blankTile.png" pos(1325,225)
    #row 325
    add "images/blankTile.png" pos(425,325)
    add "images/blankTile.png" pos(525,325)
    add "images/blankTile.png" pos(625,325)
    add "images/blankTile.png" pos(725,325)
    add "images/inputBG.png" pos(825,325)
    #add "images/blankTile.png" pos(925,325) #gate location
    add "images/horizontalG.png" pos(1025,325)
    add "images/cornGLB.png" pos(1125,325)
    add "images/blankTile.png" pos(1225,325)
    add "images/blankTile.png" pos(1325,325)
    #row 425
    add "images/2_3.png" pos(325,425)     #start point 2
    add "images/horizontalB.png" pos(425,425)
    add "images/cornBLB.png" pos(525,425)
    add "images/blankTile.png" pos(625,425)
    add "images/blankTile.png" pos(725,425)
    add "images/verticalG.png" pos(825,425)
    add "images/blankTile.png" pos(925,425)
    add "images/blankTile.png" pos(1025,425)
    add "images/inputGG.png" pos(1125,425)
    add "images/1_1.png" pos(1225,425)
    add "images/horizontalG.png" pos(1325,425)
    add "images/1_4.png" pos(1425,425)     #finish point
    #row 525
    add "images/blankTile.png" pos(425,525)
    add "images/inputBR.png" pos(525,525)
    #add "images/blankTile.png" pos(625,525) #gate location
    add "images/horizontalG.png" pos(725,525)
    add "images/cornGLT.png" pos(825,525)
    add "images/blankTile.png" pos(925,525)
    add "images/blankTile.png" pos(1025,525)
    add "images/verticalG.png" pos(1125,525)
    add "images/blankTile.png" pos(1225,525)
    add "images/blankTile.png" pos(1325,525)
    #row 625
    add "images/2_2.png" pos(325,625)     #start point 3
    add "images/horizontalR.png" pos(425,625)
    add "images/cornRLT.png" pos(525,625)
    add "images/blankTile.png" pos(625,625)
    add "images/cornGTR.png" pos(725,625)
    add "images/horizontalG.png" pos(825,625)
    add "images/cornGLB.png" pos(925,625)
    add "images/blankTile.png" pos(1025,625)
    add "images/verticalG.png" pos(1125,625)
    add "images/blankTile.png" pos(1225,625)
    add "images/blankTile.png" pos(1325,625)
    #row 725
    add "images/verticalR.png" pos(425,725)
    add "images/blankTile.png" pos(525,725) 
    add "images/blankTile.png" pos(625,725) 
    add "images/blankTile.png" pos(725,725) 
    add "images/blankTile.png" pos(825,725) 
    add "images/inputGR.png" pos(925,725)
    #add "images/blankTile.png" pos(1025,725) #gate location
    add "images/cornGLT.png" pos(1125,725)
    add "images/blankTile.png" pos(1225,725)
    add "images/blankTile.png" pos(1325,725)
    #row 825
    add "images/cornRTR.png" pos(425,825)  
    add "images/horizontalR.png" pos(525,825)
    add "images/horizontalR.png" pos(625,825)  
    add "images/horizontalR.png" pos(725,825)  
    add "images/horizontalR.png" pos(825,825) 
    add "images/cornRLT.png" pos(925,825) 
    add "images/blankTile.png" pos(1025,825)  
    add "images/blankTile.png" pos(1125,825)  
    add "images/blankTile.png" pos(1225,825)  
    add "images/blankTile.png" pos(1325,825) 
    

    draggroup:
        #and gates
        drag:
                drag_name "and_gate"
                child "1_2.png"
                droppable False
                dragged gate_dragged
                xpos 50 ypos 125
        #or gates
        drag:
                drag_name "or_gate"
                child "1_3.png"
                droppable False
                dragged gate_dragged
                xpos 175 ypos 125
        
        #location to be dropped
        drag:
                drag_name "gate slot one"
                child "images/1_1.png"
                draggable False
                xpos 625 ypos 525
        drag:
                drag_name "gate slot two"
                child "images/1_1.png"
                draggable False
                xpos 925 ypos 325
        drag:
                drag_name "gate slot three"
                child "images/1_1.png"
                draggable False
                xpos 1025 ypos 725
                
screen logcGates1:
    add "images/blankTile.png" pos(1325,825) 