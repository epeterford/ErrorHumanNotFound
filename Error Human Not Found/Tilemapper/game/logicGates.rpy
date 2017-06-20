init python:

    #makes it so the game doesn't stop early
    def gate_dragged(drags,drop):
        if not drop:
            return
        #checks to see the drop location and makes it snap        
        if drop:
            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop 
           
            #this store the values for the if checks
            store.gate_name = drags[0].drag_name
            store.slot_name = drop.drag_name

            return True
        return

screen logicGates:
    
    #drags and drop location
    draggroup:
            #and gates
            drag:
                drag_name "and_gate"
                child "1_2.png"
                droppable False
                dragged gate_dragged
                xpos and1x ypos and1y

            drag:
                drag_name "and_gate1"
                child "1_2.png"
                droppable False
                dragged gate_dragged
                xpos and2x ypos and2y
            #or gates
            drag:
                drag_name "or_gate"
                child "1_3.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y
           
            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "border.png"
                draggable False
                xpos 625 ypos 525
            drag:
                drag_name "gate slot two"
                child "border.png"
                draggable False
                xpos 925 ypos 325
            drag:
                drag_name "gate slot three"
                child "border.png"
                draggable False
                xpos 1025 ypos 725
 
