init python:
    def gate_dragged(drags,drop):
        if not drop:
            store.gate_name = drags[0].drag_name
            store.slot_name = "null"
            return True
                
        if drop:
            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop
                
                store.gate_name = drags[0].drag_name
                store.slot_name = drop.drag_name
            
                return True
        return True 

screen logicGates_med5:

    draggroup:
        #and gates
        drag:
                drag_name "letterT"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT1x ypos letterT1y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM2x ypos letterM2y
        drag:
                drag_name "letterR"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterR3x ypos letterR3y
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK4x ypos letterK4y
        drag:
                drag_name "letterT2"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT5x ypos letterT5y
        drag:
                drag_name "letterR2"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterR6x ypos letterR6y
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJ7x ypos letterJ7y

        drag:
                drag_name "letterJ2"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJ8x ypos letterJ8y

        drag:
                drag_name "letterM2"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM9x ypos letterM9y

        drag:
                drag_name "letterR3"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterR10x ypos letterR10y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 1025 ypos 310
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1505 ypos 310
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 875 ypos 485
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 1175 ypos 485
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1505 ypos 485
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 875 ypos 660
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 1095 ypos 660
        drag:
                drag_name "gate slot eight"
                draggable False
                child "images/border.png"
                xpos 1250 ypos 660
        drag:
                drag_name "gate slot nine"
                draggable False
                child "images/border.png"
                xpos 1425 ypos 660
        drag:
                drag_name "gate slot ten"
                draggable False
                child "images/border.png"
                xpos 1585 ypos 660

init:
    image bg Eng_gram_m5_tile = "eng_tile_bg.png"

label gram_m5:#start:

    scene bg Eng_gram_m5_tile

    #row1 1-4
    image gram_m5_tile0 = "instructions10.png"
    image gram_m5_tile1 = "1_1_green.png"
    image gram_m5_tile2 = "letterS.png"
    #image eaenggram_m5_tile3 = "treeGrey.png"
    show gram_m5_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_m5_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 130, yanchor = 0)
    show gram_m5_tile2 at Position(xpos = 1260, xanchor = 0, ypos = 145, yanchor = 0)
    #show eaenggram_m5_tile3 at Position(xpos = 1248, xanchor = 0, ypos = 228, yanchor = 0)
    
    #row2 5-8
    #image eaenggram_m5_tile4 = "1_1_grey.png"
    image gram_m5_tile5 = "leftTreelong1.png"
    image gram_m5_tile6 = "rightTreelong1.png"
    #show eaenggram_m5_tile4 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)
    show gram_m5_tile5 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
    show gram_m5_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
    
    #row3 9-13   

    image gram_m5_tile9 = "1_1_grey.png"
    image gram_m5_tile10 = "1_1_grey.png"
    

    show gram_m5_tile9 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)
    show gram_m5_tile10 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    #row4 14-20

    image gram_m5_tile14 = "leftTreelong.png"
    #image eaenggram_m5_tile14 = "leftTreelong.png"
    image gram_m5_tile15 = "rightTreelong.png"
    image gram_m5_tile16 = "treeGrey.png"
    image gram_m5_tile17 = "treeGrey.png"

    show gram_m5_tile14 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
    #show eaenggram_m5_tile14 at Position(xpos = 1000, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m5_tile15 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m5_tile16 at Position(xpos = 1490, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m5_tile17 at Position(xpos = 860, xanchor = 0, ypos = 575, yanchor = 0)


    #row5 21-27

    image gram_m5_tile21 = "1_1_grey.png"
    image gram_m5_tile22 = "1_1_grey.png"
    image gram_m5_tile23 = "1_1_grey.png"
    image gram_m5_tile24 = "1_1_grey.png"

    show gram_m5_tile21 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m5_tile22 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m5_tile23 at Position(xpos = 1490, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m5_tile24 at Position(xpos = 860, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m5_tile25 = "leftTree.png"
    image gram_m5_tile26 = "1_1_grey.png"
    show gram_m5_tile25 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m5_tile26 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m5_tile27 = "rightTree.png"
    image gram_m5_tile28 = "1_1_grey.png"
    show gram_m5_tile27 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m5_tile28 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m5_tile29 = "leftTree.png"
    image gram_m5_tile30 = "1_1_grey.png"
    show gram_m5_tile29 at Position(xpos = 1450, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m5_tile30 at Position(xpos = 1410, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m5_tile37 = "rightTree.png"
    image gram_m5_tile38 = "1_1_grey.png"
    show gram_m5_tile37 at Position(xpos = 1550, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m5_tile38 at Position(xpos = 1570, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m5_tile31 = "letterBorder.png"
    image gram_m5_tile32 = "letterBorder.png"
    image gram_m5_tile33 = "letterBorder.png"
    image gram_m5_tile34 = "letterBorder.png"
    image gram_m5_tile35 = "letterBorder.png"
    #image eaenggram_m5_tile36 = "letterBorder.png"
    show gram_m5_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m5_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m5_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show gram_m5_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show gram_m5_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    #show eaenggram_m5_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ letterT1x = 410 
    $ letterT1y = 750
    $ letterM2x = 410
    $ letterM2y = 575
    $ letterR3x = 275 
    $ letterR3y = 750
    $ letterK4x = 275
    $ letterK4y = 575
    $ letterT5x = 410
    $ letterT5y = 750
    $ letterR6x = 275 
    $ letterR6y = 750
    $ letterJ7x = 342 
    $ letterJ7y = 660
    $ letterJ8x = 342 
    $ letterJ8y = 660
    $ letterM9x = 410 
    $ letterM9y = 575
    $ letterR10x = 275 
    $ letterR10y = 750

    # check conditons for locations
    $ and1in1 = False
    $ and1in2 = False
    $ and1in3 = False
    $ and1in4 = False
    $ and1in5 = False
    $ and1in6 = False
    $ and1in7 = False
    $ and1in8 = False
    $ and1in9 = False
    $ and1in10 = False

    $ letterM2in1 = False
    $ letterM2in2 = False
    $ letterM2in3 = False
    $ letterM2in4 = False
    $ letterM2in5 = False
    $ letterM2in6 = False
    $ letterM2in7 = False
    $ letterM2in8 = False
    $ letterM2in9 = False
    $ letterM2in10 = False

    $ letterR3in1 = False
    $ letterR3in2 = False
    $ letterR3in3 = False
    $ letterR3in4 = False
    $ letterR3in5 = False
    $ letterR3in6 = False
    $ letterR3in7 = False
    $ letterR3in8 = False
    $ letterR3in9 = False
    $ letterR3in10 = False

    $ letterK4in1 = False
    $ letterK4in2 = False
    $ letterK4in3 = False
    $ letterK4in4 = False
    $ letterK4in5 = False
    $ letterK4in6 = False
    $ letterK4in7 = False
    $ letterK4in8 = False
    $ letterK4in9 = False
    $ letterK4in10 = False

    $ letterT5in1 = False
    $ letterT5in2 = False
    $ letterT5in3 = False
    $ letterT5in4 = False
    $ letterT5in5 = False
    $ letterT5in6 = False
    $ letterT5in7 = False
    $ letterT5in8 = False
    $ letterT5in9 = False
    $ letterT5in10 = False

    $ letterR6in1 = False
    $ letterR6in2 = False
    $ letterR6in3 = False
    $ letterR6in4 = False
    $ letterR6in5 = False
    $ letterR6in6 = False
    $ letterR6in7 = False
    $ letterR6in8 = False
    $ letterR6in9 = False
    $ letterR6in10 = False

    $ letterJ7in1 = False
    $ letterJ7in2 = False
    $ letterJ7in3 = False
    $ letterJ7in4 = False
    $ letterJ7in5 = False
    $ letterJ7in6 = False
    $ letterJ7in7 = False
    $ letterJ7in8 = False
    $ letterJ7in9 = False
    $ letterJ7in10 = False

    $ letterJ8in1 = False
    $ letterJ8in2 = False
    $ letterJ8in3 = False
    $ letterJ8in4 = False
    $ letterJ8in5 = False
    $ letterJ8in6 = False
    $ letterJ8in7 = False
    $ letterJ8in8 = False
    $ letterJ8in9 = False
    $ letterJ8in10 = False

    $ letterM9in1 = False
    $ letterM9in2 = False
    $ letterM9in3 = False
    $ letterM9in4 = False
    $ letterM9in5 = False
    $ letterM9in6 = False
    $ letterM9in7 = False
    $ letterM9in8 = False
    $ letterM9in9 = False
    $ letterM9in10 = False

    $ and10in1 = False
    $ and10in2 = False
    $ and10in3 = False
    $ and10in4 = False
    $ and10in5 = False
    $ and10in6 = False
    $ and10in7 = False
    $ and10in8 = False
    $ and10in9 = False
    $ and10in10 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 15
    
    call gamefile_m5

label gamefile_m5:
    #image moon = "images/blankgram_m5_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGates_med5

    if gate_name == "letterT":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterT1x = 1025
            $ letterT1y = 315
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterT1x = 1505
            $ letterT1y = 315
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterT1x = 875
            $ letterT1y = 490
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterT1x = 1175
            $ letterT1y = 490
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = True
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterT1x = 1505
            $ letterT1y = 490
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = True
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterT1x = 875
            $ letterT1y = 665
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = True
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterT1x = 1095
            $ letterT1y = 665
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = True
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterT1x = 1250
            $ letterT1y = 665
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = True
            $ and1in9 = False
            $ and1in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterT1x = 1425
            $ letterT1y = 665
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = True
            $ and1in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterT1x = 1585
            $ letterT1y = 665
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
            $ and1in7 = False
            $ and1in8 = False
            $ and1in9 = False
            $ and1in10 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterM2x = 1025
            $ letterM2y = 315
            $ letterM2in1 = True
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterM2x = 1505
            $ letterM2y = 315
            $ letterM2in1 = False
            $ letterM2in2 = True
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterM2x = 875
            $ letterM2y = 490
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = True
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterM2x = 1175
            $ letterM2y = 490
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = True
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterM2x = 1505
            $ letterM2y = 490
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = True
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterM2x = 875
            $ letterM2y = 665
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = True
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterM2x = 1095
            $ letterM2y = 665
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = True
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterM2x = 1250
            $ letterM2y = 665
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = True
            $ letterM2in9 = False
            $ letterM2in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterM2x = 1425
            $ letterM2y = 665
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = True
            $ letterM2in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterM2x = 1585
            $ letterM2y = 665
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False
            $ letterM2in9 = False
            $ letterM2in10 = True

    if gate_name == "letterR":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterR3x = 1025
            $ letterR3y = 315
            $ letterR3in1 = True
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterR3x = 1505
            $ letterR3y = 315
            $ letterR3in1 = False
            $ letterR3in2 = True
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterR3x = 875
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = True
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterR3x = 1175
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = True
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterR3x = 1505
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = True
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterR3x = 875
            $ letterR3y = 665
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = True
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterR3x = 1095
            $ letterR3y = 665
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = True
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterR3x = 1250
            $ letterR3y = 665
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = True
            $ letterR3in9 = False
            $ letterR3in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterR3x = 1425
            $ letterR3y = 665
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = True
            $ letterR3in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterR3x = 1585
            $ letterR3y = 665
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
            $ letterR3in8 = False
            $ letterR3in9 = False
            $ letterR3in10 = True


    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterK4x = 1025
            $ letterK4y = 315
            $ letterK4in1 = True
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK41in9 = False
            $ letterK4in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterK4x = 1505
            $ letterK4y = 315
            $ letterK4in1 = False
            $ letterK4in2 = True
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterK4x = 875
            $ letterK4y = 490
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = True
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterK4x = 1175
            $ letterK4y = 490
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = True
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterK4x = 1505
            $ letterK4y = 490
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = True
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterK4x = 875
            $ letterK4y = 665
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = True
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterK4x = 1095
            $ letterK4y = 665
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = True
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterK4x = 1250
            $ letterK4y = 665
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = True
            $ letterK4in9 = False
            $ letterK4in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterK4x = 1425
            $ letterK4y = 665
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK41in9 = True
            $ letterK4in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterK4x = 1585
            $ letterK4y = 665
            $ letterK4in1 = False
            $ letterK4in2 = False
            $ letterK4in3 = False
            $ letterK4in4 = False
            $ letterK4in5 = False
            $ letterK4in6 = False
            $ letterK4in7 = False
            $ letterK4in8 = False
            $ letterK4in9 = False
            $ letterK4in10 = True


    if gate_name == "letterT2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterT5x = 1025
            $ letterT5y = 315
            $ letterT5in1 = True
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterT5x = 1505
            $ letterT5y = 315
            $ letterT5in1 = False
            $ letterT5in2 = True
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterT5x = 875
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = True
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterT5x = 1175
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = True
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterT5x = 1505
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = True
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterT5x = 875
            $ letterT5y = 665
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = True
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterT5x = 1095
            $ letterT5y = 665
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = True
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterT5x = 1250
            $ letterT5y = 665
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = True
            $ letterT5in9 = False
            $ letterT5in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterT5x = 1425
            $ letterT5y = 665
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = True
            $ letterT5in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterT5x = 1585
            $ letterT5y = 665
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
            $ letterT5in8 = False
            $ letterT5in9 = False
            $ letterT5in10 = True

    if gate_name == "letterR2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterR6x = 1025
            $ letterR6y = 315
            $ letterR6in1 = True
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterR6x = 1505
            $ letterR6y = 315
            $ letterR6in1 = False
            $ letterR6in2 = True
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterR6x = 875
            $ letterR6y = 490
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = True
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterR6x = 1175
            $ letterR6y = 490
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = True
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterR6x = 1505
            $ letterR6y = 490
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = True
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterR6x = 875
            $ letterR6y = 665
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = True
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterR6x = 1095
            $ letterR6y = 665
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = True
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterR6x = 1250
            $ letterR6y = 665
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = True
            $ letterR6in9 = False
            $ letterR6in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterR6x = 1425
            $ letterR6y = 665
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = True
            $ letterR6in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterR6x = 1585
            $ letterR6y = 665
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            $ letterR6in8 = False
            $ letterR6in9 = False
            $ letterR6in10 = True

    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterJ7x = 1025
            $ letterJ7y = 315
            $ letterJ7in1 = True
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ71in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterJ7x = 1505
            $ letterJ7y = 315
            $ letterJ7in1 = False
            $ letterJ7in2 = True
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterJ7x = 875
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = True
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterJ7x = 1175
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = True
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterJ7x = 1505
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = True
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterJ7x = 875
            $ letterJ7y = 665
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = True
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterJ7x = 1095
            $ letterJ7y = 665
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = True
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterJ7x = 1250
            $ letterJ7y = 665
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = True
            $ letterJ7in9 = False
            $ letterJ7in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterJ7x = 1425
            $ letterJ7y = 665
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = True
            $ letterJ7in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterJ7x = 1585
            $ letterJ7y = 665
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = True

           #8
    if gate_name == "letterJ2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterJ8x = 1025
            $ letterJ8y = 315
            $ letterJ8in1 = True
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterJ8x = 1505
            $ letterJ8y = 315
            $ letterJ8in1 = False
            $ letterJ8in2 = True
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterJ8x = 875
            $ letterJ8y = 490
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = True
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterJ8x = 1175
            $ letterJ8y = 490
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = True
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterJ8x = 1505
            $ letterJ8y = 490
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = True
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterJ8x = 875
            $ letterJ8y = 665
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = True
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterJ8x = 1095
            $ letterJ8y = 665
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = True
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterJ8x = 1250
            $ letterJ8y = 665
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = True
            $ letterJ8in9 = False
            $ letterJ8in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterJ8x = 1425
            $ letterJ8y = 665
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = True
            $ letterJ8in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterJ8x = 1585
            $ letterJ8y = 665
            $ letterJ8in1 = False
            $ letterJ8in2 = False
            $ letterJ8in3 = False
            $ letterJ8in4 = False
            $ letterJ8in5 = False
            $ letterJ8in6 = False
            $ letterJ8in7 = False
            $ letterJ8in8 = False
            $ letterJ8in9 = False
            $ letterJ8in10 = True

            #9
    if gate_name == "letterM2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterM9x = 1025
            $ letterM9y = 315
            $ letterM9in1 = True
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterM9x = 1505
            $ letterM9y = 315
            $ letterM9in1 = False
            $ letterM9in2 = True
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterM9x = 875
            $ letterM9y = 490
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = True
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterM9x = 1175
            $ letterM9y = 490
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = True
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterM9x = 1505
            $ letterM9y = 490
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = True
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterM9x = 875
            $ letterM9y = 665
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = True
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterM9x = 1095
            $ letterM9y = 665
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = True
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterM9x = 1250
            $ letterM9y = 665
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = True
            $ letterM9in9 = False
            $ letterM9in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterM9x = 1425
            $ letterM9y = 665
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = True
            $ letterM9in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterM9x = 1585
            $ letterM9y = 665
            $ letterM9in1 = False
            $ letterM9in2 = False
            $ letterM9in3 = False
            $ letterM9in4 = False
            $ letterM9in5 = False
            $ letterM9in6 = False
            $ letterM9in7 = False
            $ letterM9in8 = False
            $ letterM9in9 = False
            $ letterM9in10 = True

    if gate_name == "letterR3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if and1in1 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterK4in1 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterJ8in1 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in1 = False
            if letterM9in1 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in1 = False
            if and10in1 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in1 = False
            #sets values for checks
            $ letterR10x = 1025
            $ letterR10y = 315
            $ and10in1 = True
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterK4in2 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterJ8in2 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in2 = False
            if letterM9in2 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in2 = False
            if and10in2 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in2 = False

            #sets check values
            $ letterR10x = 1505
            $ letterR10y = 315
            $ and10in1 = False
            $ and10in2 = True
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterK4in3 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterJ8in3 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in3 = False
            if letterM9in3 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in3 = False
            if and10in3 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in3 = False

            #sets values for the checks
            $ letterR10x = 875
            $ letterR10y = 490
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = True
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterK4in4 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterJ8in4 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in4 = False
            if letterM9in4 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in4 = False
            if and10in4 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in4 = False

            #sets values for the checks
            $ letterR10x = 1175
            $ letterR10y = 490
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = True
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterK4in5 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterJ8in5 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in5 = False
            if letterM9in5 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in5 = False
            if and10in5 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in5 = False

            #sets values for the checks
            $ letterR10x = 1505
            $ letterR10y = 490
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = True
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterK4in6 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterJ8in6 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in6 = False
            if letterM9in6 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in6 = False
            if and10in6 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in6 = False

            #sets values for the checks
            $ letterR10x = 875
            $ letterR10y = 665
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = True
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if and1in7 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterK4in7 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterJ8in7 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in7 = False
            if letterM9in7 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in7 = False
            if and10in7 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in7 = False

            #sets values for the checks
            $ letterR10x = 1095
            $ letterR10y = 665
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = True
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if and1in8 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterR3in8 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in8 = False
            if letterK4in8 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in8 = False
            if letterT5in8 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in8 = False
            if letterR6in8 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterJ8in8 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in8 = False
            if letterM9in8 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in8 = False
            if and10in8 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in8 = False

            #sets values for the checks
            $ letterR10x = 1250
            $ letterR10y = 665
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = True
            $ and10in9 = False
            $ and10in10 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if and1in9 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in9 = False
            if letterM2in9 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in9 = False
            if letterR3in9 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in9 = False
            if letterK4in9 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in9 = False
            if letterT5in9 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in9 = False
            if letterR6in9 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterJ8in9 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in9 = False
            if letterM9in9 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in9 = False
            if and10in9 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in9 = False

            #sets values for the checks
            $ letterR10x = 1425
            $ letterR10y = 665
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = True
            $ and10in10 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if and1in10 == True:
               $ letterT1x = 410
               $ letterT1y = 750
               $ and1in10 = False
            if letterM2in10 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in10 = False
            if letterR3in10 == True:
               $ letterR3x = 275
               $ letterR3y = 750
               $ letterR3in10 = False
            if letterK4in10 == True:
               $ letterK4x = 275
               $ letterK4y = 575
               $ letterK4in10 = False
            if letterT5in10 == True:
               $ letterT5x = 410
               $ letterT5y = 750
               $ letterT5in10 = False
            if letterR6in10 == True:
               $ letterR6x = 275
               $ letterR6y = 750
               $ letterR6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterJ8in10 == True:
               $ letterJ8x = 342
               $ letterJ8y = 660
               $ letterJ8in10 = False
            if letterM9in10 == True:
               $ letterM9x = 410
               $ letterM9y = 575
               $ letterM9in10 = False
            if and10in10 == True:
               $ letterR10x = 275
               $ letterR10y = 750
               $ and10in10 = False

            #sets values for the checks
            $ letterR10x = 1585
            $ letterR10y = 665
            $ and10in1 = False
            $ and10in2 = False
            $ and10in3 = False
            $ and10in4 = False
            $ and10in5 = False
            $ and10in6 = False
            $ and10in7 = False
            $ and10in8 = False
            $ and10in9 = False
            $ and10in10 = True



    if (temp_slot == "" and temp_gate == "" and slot_name != "null"):
       $ temp_slot = slot_name
       $ temp_gate = gate_name
       if temp_slot != "" and temp_gate != "":
           $ attempts -=1
    else:
       if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
           $ attempts -=1
           $ temp_slot = slot_name
           $ temp_gate = gate_name



    if (letterT5in1 == True or and1in1 == True) and (and1in2 == True or letterT5in2 == True):
        image gram_m5_tile42 = "leftTreegreenlong1.png"
        image gram_m5_tile43 = "1_1_green.png"
        show gram_m5_tile42 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m5_tile43 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m5_tile62 = "rightTreegreenlong1.png"
        image gram_m5_tile63 = "1_1_green.png"
        show gram_m5_tile62 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m5_tile63 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)
        
        if (letterR3in3 == True or letterR6in3 == True or and10in3 == True) and (letterK4in4 == True):
            image gram_m5_tile44 = "leftTreegreenlong.png"
            #image gram_m5_tile44 = "leftTreegreenlong.png"
            image gram_m5_tile45 = "1_1_green.png"

            show gram_m5_tile44 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            #show gram_m5_tile44 at Position(xpos = 1000, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile45 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)
            
            image gram_m5_tile56 = "rightTreegreenlong.png"
            image gram_m5_tile57 = "1_1_green.png"
            show gram_m5_tile56 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile57 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)

            if (letterM2in6 == True or letterM9in6 == True):
               image gram_m5_tile70 = "treeGreen.png"
               image gram_m5_tile71 = "1_1_green.png"
               #image gram_m5_tile72 = "solutionLine.png"
               #image gram_m5_tile213 = "solutionLine.png"
               image gram_m5_tile214 = "solutionLine.png"
               image gram_m5_tile73 = "a.png"
               show gram_m5_tile70 at Position(xpos = 860, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile71 at Position(xpos = 860, xanchor = 0, ypos = 650, yanchor = 0)
               #show gram_m5_tile72 at Position(xpos = 1640, xanchor = 0, ypos = 570, yanchor = 0)
               #show gram_m5_tile213 at Position(xpos = 860, xanchor = 0, ypos = 682, yanchor = 0)
               show gram_m5_tile214 at Position(xpos = 860, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m5_tile73 at Position(xpos = 830, xanchor = 0, ypos = 800, yanchor = 0)


            if (letterM2in6 == False and letterM9in6 == False):
               hide gram_m5_tile70
               hide gram_m5_tile71
               hide gram_m5_tile72
               hide gram_m5_tile213
               hide gram_m5_tile214
               hide gram_m5_tile73

            if (and1in6 == True or letterR3in6 == True or letterK4in6 == True or letterT5in6 == True or letterR6in6 == True or letterJ7in6 == True or letterJ8in6 == True or and10in6 == True):
               image gram_m5_tile76 = "treeRed.png"
               image gram_m5_tile77 = "1_1_red.png"
               show gram_m5_tile76 at Position(xpos = 860, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile77 at Position(xpos = 860, xanchor = 0, ypos = 650, yanchor = 0)

            if (and1in6 == False and letterR3in6 == False and letterK4in6 == False and letterT5in6 == False and letterR6in6 == False and letterJ7in6 == False and letterJ8in6 == False and and10in6 == False):
               hide gram_m5_tile76
               hide gram_m5_tile77

            if (letterJ7in7 == True or letterJ8in7 == True) and (letterJ7in8 == True or letterJ8in8 == True):
               #image gram_m5_tile50 = "leftTreegreen.png"
               image gram_m5_tile50 = "leftTreegreen.png"
               image gram_m5_tile51 = "1_1_green.png"
               image gram_m5_tile52 = "solutionLine.png"
               image gram_m5_tile53 = "b.png"
               #show gram_m5_tile50 at Position(xpos = 960, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile50 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile51 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)
               show gram_m5_tile52 at Position(xpos = 1080, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m5_tile53 at Position(xpos = 1050, xanchor = 0, ypos = 800, yanchor = 0)

               image gram_m5_tile215 = "rightTreegreen.png"
               image gram_m5_tile216 = "1_1_green.png"
               show gram_m5_tile215 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile216 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m5_tile210 = "solutionLine.png"
               image gram_m5_tile59 = "b.png"
               show gram_m5_tile210 at Position(xpos = 1240, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m5_tile59 at Position(xpos = 1205, xanchor = 0, ypos = 800, yanchor = 0)



            if (letterJ7in7 == False and letterJ8in7 == False) or (letterJ7in8 == False and letterJ8in8 == False):
               hide gram_m5_tile50
               hide gram_m5_tile51
               hide gram_m5_tile52
               hide gram_m5_tile53

               hide gram_m5_tile215
               hide gram_m5_tile216
               hide gram_m5_tile210
               hide gram_m5_tile59

            if (and1in7 == True or letterM2in7 == True or letterR3in7 == True or letterK4in7 == True or letterT5in7 == True or letterR6in7 == True or letterJ7in7 == True or letterJ8in7 == True or letterM9in7 == True or and10in7 == True) and (and1in8 == True or letterM2in8 == True or letterR3in8 == True or letterK4in8 == True or letterT5in8 == True or letterR6in8 == True or letterM9in8 == True or and10in8 == True):
               image gram_m5_tile260 = "leftTreered.png"
               image gram_m5_tile261 = "1_1_red.png"
               show gram_m5_tile260 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile261 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m5_tile262 = "rightTreered.png"
               image gram_m5_tile263 = "1_1_red.png"
               show gram_m5_tile262 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile263 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)

            if (and1in7 == False and letterM2in7 == False and letterR3in7 == False and letterK4in7 == False and letterT5in7 == False and letterR6in7 == False and letterJ7in7 == False and letterJ8in7 == False and letterM9in7 == False and and10in7 == False) or (and1in8 == False and letterM2in8 == False and letterR3in8 == False and letterK4in8 == False and letterT5in8 == False and letterR6in8 == False and letterM9in8 == False and and10in8 == False):
               hide gram_m5_tile260
               hide gram_m5_tile261
               hide gram_m5_tile262
               hide gram_m5_tile263

            if (and1in7 == True or letterM2in7 == True or letterR3in7 == True or letterK4in7 == True or letterT5in7 == True or letterR6in7 == True or letterM9in7 == True or and10in7 == True) and (and1in8 == True or letterM2in8 == True or letterR3in8 == True or letterK4in8 == True or letterT5in8 == True or letterR6in8 == True or letterJ7in8 == True or letterJ8in8 == True or letterM9in8 == True or and10in8 == True):
               image gram_m5_tile264 = "leftTreered.png"
               image gram_m5_tile265 = "1_1_red.png"
               show gram_m5_tile264 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile265 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m5_tile266 = "rightTreered.png"
               image gram_m5_tile267 = "1_1_red.png"
               show gram_m5_tile266 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile267 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)

            if (and1in7 == False and letterM2in7 == False and letterR3in7 == False and letterK4in7 == False and letterT5in7 == False and letterR6in7 == False and letterM9in7 == False and and10in7 == False) or (and1in8 == False and letterM2in8 == False and letterR3in8 == False and letterK4in8 == False and letterT5in8 == False and letterR6in8 == False and letterJ7in8 == False and letterJ8in8 == False and letterM9in8 == False and and10in8 == False):
               hide gram_m5_tile264
               hide gram_m5_tile265
               hide gram_m5_tile266
               hide gram_m5_tile267

        if (letterR3in3 == False and letterR6in3 == False and and10in3 == False) or (letterK4in4 == False):
            hide gram_m5_tile44
            hide gram_m5_tile45
            hide gram_m5_tile46
            hide gram_m5_tile47
            hide gram_m5_tile48
            hide gram_m5_tile207
            hide gram_m5_tile49
            hide gram_m5_tile50
            hide gram_m5_tile51
            hide gram_m5_tile52
            hide gram_m5_tile53

            hide gram_m5_tile215
            hide gram_m5_tile216
            hide gram_m5_tile210
            hide gram_m5_tile59

            hide gram_m5_tile56
            hide gram_m5_tile57
            hide gram_m5_tile58
            hide gram_m5_tile209
            hide gram_m5_tile210
            hide gram_m5_tile59

            hide gram_m5_tile260
            hide gram_m5_tile261
            hide gram_m5_tile262
            hide gram_m5_tile263

            hide gram_m5_tile264
            hide gram_m5_tile265
            hide gram_m5_tile266
            hide gram_m5_tile267
     
        if (and1in3 == True or letterM2in3 == True or letterR3in3 == True or letterK4in3 == True or letterT5in3 == True or letterR6in3 == True or letterJ7in3 == True or letterJ8in3 == True or letterM9in3 == True or and10in3 == True) and (and1in4 == True or letterM2in4 == True or letterR3in4 == True or letterT5in4 == True or letterR6in4 == True or letterJ7in4 == True or letterJ8in4 == True or letterM9in4 == True or and10in4 == True):
            image gram_m5_tile54 = "leftTreeredlong.png"
            image gram_m5_tile55 = "1_1_red.png"
            show gram_m5_tile54 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile55 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m5_tile60 = "rightTreeredlong.png"
            image gram_m5_tile61 = "1_1_red.png"
            show gram_m5_tile60 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile61 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
        if (and1in3 == False and letterM2in3 == False and letterR3in3 == False and letterK4in3 == False and letterT5in3 == False and letterR6in3 == False and letterJ7in3 == False and letterJ8in3 == False and letterM9in3 == False and and10in3 == False) or (and1in4 == False and letterM2in4 == False and letterR3in4 == False and letterT5in4 == False and letterR6in4 == False and letterJ7in4 == False and letterJ8in4 == False and letterM9in4 == False and and10in4 == False):
            hide gram_m5_tile54
            hide gram_m5_tile55

            hide gram_m5_tile60
            hide gram_m5_tile61

        if (and1in3 == True or letterM2in3 == True or letterK4in3 == True or letterJ7in3 == True or letterJ8in3 == True or letterM9in3 == True) and (and1in4 == True or letterM2in4 == True or letterR3in4 == True or letterK4in4 == True or letterT5in4 == True or letterR6in4 == True or letterJ7in4 == True or letterJ8in4 == True or letterM9in4 == True or and10in4 == True):
            image gram_m5_tile254 = "leftTreeredlong.png"
            image gram_m5_tile255 = "1_1_red.png"
            show gram_m5_tile254 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile255 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m5_tile260 = "rightTreeredlong.png"
            image gram_m5_tile261 = "1_1_red.png"
            show gram_m5_tile260 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile261 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
        if (and1in3 == False and letterM2in3 == False and letterK4in3 == False and letterJ7in3 == False and letterJ8in3 == False and letterM9in3 == False) or (and1in4 == False and letterM2in4 == False and letterR3in4 == False and letterK4in4 == False and letterT5in4 == False and letterR6in4 == False and letterJ7in4 == False and letterJ8in4 == False and letterM9in4 == False and and10in4 == False):
            hide gram_m5_tile254
            hide gram_m5_tile255

            hide gram_m5_tile260
            hide gram_m5_tile261

        if (letterR3in5 == True or letterR6in5 == True or and10in5 == True):
            image gram_m5_tile64 = "treeGreen.png"
            image gram_m5_tile65 = "1_1_green.png"

            show gram_m5_tile64 at Position(xpos = 1490, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile65 at Position(xpos = 1490, xanchor = 0, ypos = 475, yanchor = 0)



            if (letterM2in9 == True or letterM9in9 == True) and (letterR3in10 == True or letterR6in10 == True or and10in10 == True):
               #image gram_m5_tile50 = "leftTreegreen.png"
               image gram_m5_tile350 = "leftTreegreen.png"
               image gram_m5_tile351 = "1_1_green.png"
               image gram_m5_tile352 = "solutionLine.png"
               image gram_m5_tile353 = "a.png"
               #show gram_m5_tile50 at Position(xpos = 960, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile350 at Position(xpos = 1450, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile351 at Position(xpos = 1410, xanchor = 0, ypos = 650, yanchor = 0)
               show gram_m5_tile352 at Position(xpos = 1410, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m5_tile353 at Position(xpos = 1380, xanchor = 0, ypos = 800, yanchor = 0)

               image gram_m5_tile3215 = "rightTreegreen.png"
               image gram_m5_tile3216 = "1_1_green.png"
               show gram_m5_tile3215 at Position(xpos = 1550, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile3216 at Position(xpos = 1570, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m5_tile3210 = "solutionLine.png"
               image gram_m5_tile359 = "epsilon.png"
               show gram_m5_tile3210 at Position(xpos = 1570, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m5_tile359 at Position(xpos = 1550, xanchor = 0, ypos = 800, yanchor = 0)



            if (letterM2in9 == False and letterM9in9 == False) or (letterR3in10 == False and letterR6in10 == False and and10in10 == False):
               hide gram_m5_tile350
               hide gram_m5_tile351
               hide gram_m5_tile352
               hide gram_m5_tile353

               hide gram_m5_tile3215
               hide gram_m5_tile3216
               hide gram_m5_tile3210
               hide gram_m5_tile359

            if (and1in9 == True or letterM2in9 == True or letterR3in9 == True or letterK4in9 == True or letterT5in9 == True or letterR6in9 == True or letterJ7in9 == True or letterJ8in9 == True or letterM9in9 == True or and10in9 == True) and (and1in10 == True or letterM2in10 == True or letterK4in10 == True or letterT5in10 == True or letterJ7in10 == True or letterJ8in10 == True or letterM9in10 == True):
               image gram_m5_tile3260 = "leftTreered.png"
               image gram_m5_tile3261 = "1_1_red.png"
               show gram_m5_tile3260 at Position(xpos = 1450, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile3261 at Position(xpos = 1410, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m5_tile3262 = "rightTreered.png"
               image gram_m5_tile3263 = "1_1_red.png"
               show gram_m5_tile3262 at Position(xpos = 1550, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile3263 at Position(xpos = 1570, xanchor = 0, ypos = 650, yanchor = 0)

            if (and1in9 == False and letterM2in9 == False and letterR3in9 == False and letterK4in9 == False and letterT5in9 == False and letterR6in9 == False and letterJ7in9 == False and letterJ8in9 == False and letterM9in9 == False and and10in9 == False) or (and1in10 == False and letterM2in10 == False and letterK4in10 == False and letterT5in10 == False and letterJ7in10 == False and letterJ8in10 == False and letterM9in10 == False):
               hide gram_m5_tile3260
               hide gram_m5_tile3261
               hide gram_m5_tile3262
               hide gram_m5_tile3263

            if (and1in9 == True or letterR3in9 == True or letterK4in9 == True or letterT5in9 == True or letterJ7in9 == True or letterJ8in9 == True or and10in9 == True) and (and1in10 == True or letterM2in10 == True or letterR3in10 == True or letterK4in10 == True or letterT5in10 == True or letterR6in10 == True or letterJ7in10 == True or letterJ8in10 == True or letterM9in10 == True or and10in10 == True):
               image gram_m5_tile3264 = "leftTreered.png"
               image gram_m5_tile3265 = "1_1_red.png"
               show gram_m5_tile3264 at Position(xpos = 1450, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile3265 at Position(xpos = 1410, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m5_tile3266 = "rightTreered.png"
               image gram_m5_tile3267 = "1_1_red.png"
               show gram_m5_tile3266 at Position(xpos = 1550, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile3267 at Position(xpos = 1570, xanchor = 0, ypos = 650, yanchor = 0)

            if (and1in9 == False and letterR3in9 == False and letterK4in9 == False and letterT5in9 == False and letterJ7in9 == False and letterJ8in9 == False and and10in9 == False) or (and1in10 == False and letterM2in10 == False and letterR3in10 == False and letterK4in10 == False and letterT5in10 == False and letterR6in10 == False and letterJ7in10 == False and letterJ8in10 == False and letterM9in10 == False and and10in10 == False):
               hide gram_m5_tile3264
               hide gram_m5_tile3265
               hide gram_m5_tile3266
               hide gram_m5_tile3267

        if (letterR3in5 == False and letterR6in5 == False and and10in5 == False):
            hide gram_m5_tile64
            hide gram_m5_tile65
            hide gram_m5_tile66
            hide gram_m5_tile211
            hide gram_m5_tile212
            hide gram_m5_tile67

            hide gram_m5_tile3260
            hide gram_m5_tile3261
            hide gram_m5_tile3262
            hide gram_m5_tile3263

            hide gram_m5_tile3264
            hide gram_m5_tile3265
            hide gram_m5_tile3266
            hide gram_m5_tile3267

        if (and1in5 == True or letterM2in5 == True or letterK4in5 == True or letterT5in5 == True or letterJ7in5 == True or letterJ8in5 == True or letterM9in5 == True):
            image gram_m5_tile68 = "treeRed.png"
            image gram_m5_tile69 = "1_1_red.png"
            show gram_m5_tile68 at Position(xpos = 1490, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m5_tile69 at Position(xpos = 1490, xanchor = 0, ypos = 475, yanchor = 0)

        if (and1in5 == False and letterM2in5 == False and letterR3in5 == False and letterK4in5 == False and letterT5in5 == False and letterR6in5 == False and letterJ7in5 == False and letterJ8in5 == False):
            hide gram_m5_tile68
            hide gram_m5_tile69

    if (letterT5in1 == False and and1in1 == False) or (and1in2 == False and letterT5in2 == False):
        hide gram_m5_tile42
        hide gram_m5_tile43
        hide gram_m5_tile44
        hide gram_m5_tile45
        hide gram_m5_tile46
        hide gram_m5_tile47
        hide gram_m5_tile48
        hide gram_m5_tile207
        hide gram_m5_tile49
        hide gram_m5_tile50
        hide gram_m5_tile51
        hide gram_m5_tile52
        hide gram_m5_tile53

        hide gram_m5_tile215
        hide gram_m5_tile216
        hide gram_m5_tile210
        hide gram_m5_tile59

        hide gram_m5_tile260
        hide gram_m5_tile261
        hide gram_m5_tile262
        hide gram_m5_tile263

        hide gram_m5_tile264
        hide gram_m5_tile265
        hide gram_m5_tile266
        hide gram_m5_tile267

        hide gram_m5_tile56
        hide gram_m5_tile57
        hide gram_m5_tile58
        hide gram_m5_tile209
        hide gram_m5_tile210
        hide gram_m5_tile59
        hide gram_m5_tile60
        hide gram_m5_tile61

        hide gram_m5_tile62
        hide gram_m5_tile61
        hide gram_m5_tile62
        hide gram_m5_tile63
        hide gram_m5_tile64
        hide gram_m5_tile65
        hide gram_m5_tile66
        hide gram_m5_tile211
        hide gram_m5_tile212
        hide gram_m5_tile67
        hide gram_m5_tile68
        hide gram_m5_tile69
        hide gram_m5_tile70
        hide gram_m5_tile71
        hide gram_m5_tile72
        hide gram_m5_tile213
        hide gram_m5_tile214
        hide gram_m5_tile73
        hide gram_m5_tile74
        hide gram_m5_tile75


    if (and1in1 == True or letterM2in1 == True or letterR3in1 == True or letterK4in1 == True or letterT5in1 == True or letterR6in1 == True or letterJ7in1 == True or letterJ8in1 == True or letterM9in1 == True or and10in1 == True) and (letterM2in2 == True or letterR3in2 == True or letterK4in2 == True or letterR6in2 == True or letterJ7in2 == True or letterJ8in2 == True or letterM9in2 == True or and10in2 == True):
         image gram_m5_tile90 = "leftTreeredlong1.png"
         image gram_m5_tile91 = "1_1_red.png"
         show gram_m5_tile90 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m5_tile91 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

         image gram_m5_tile92 = "rightTreeredlong1.png"
         image gram_m5_tile93 = "1_1_red.png"
         show gram_m5_tile92 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m5_tile93 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    elif (and1in1 == False and letterM2in1 == False and letterR3in1 == False and letterK4in1 == False and letterT5in1 == False and letterR6in1 == False and letterJ7in1 == False and letterJ8in1 == False and letterM9in1 == False and and10in1 == False) or (letterM2in2 == False and letterR3in2 == False and letterK4in2 == False and letterR6in2 == False and letterJ7in2 == False and letterJ8in2 == False and letterM9in2 == False and and10in2 == False):
         hide gram_m5_tile90
         hide gram_m5_tile91

         hide gram_m5_tile92
         hide gram_m5_tile93

    if (letterM2in1 == True or letterR3in1 == True or letterK4in1 == True or letterR6in1 == True or letterJ7in1 == True or letterJ8in1 == True or letterM9in1 == True or and10in1 == True) and (and1in2 == True or letterM2in2 == True or letterR3in2 == True or letterK4in2 == True or letterT5in2 == True or letterR6in2 == True or letterJ7in2 == True or letterJ8in2 == True or letterM9in2 == True or and10in2 == True):
         image gram_m5_tile94 = "leftTreeredlong1.png"
         image gram_m5_tile95 = "1_1_red.png"
         show gram_m5_tile94 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m5_tile95 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

         image gram_m5_tile96 = "rightTreeredlong1.png"
         image gram_m5_tile97 = "1_1_red.png"
         show gram_m5_tile96 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m5_tile97 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    elif (letterM2in1 == False and letterR3in1 == False and letterK4in1 == False and letterR6in1 == False and letterJ7in1 == False and letterJ8in1 == False and letterM9in1 == False and and10in1 == False) or (and1in2 == False and letterM2in2 == False and letterR3in2 == False and letterK4in2 == False and letterT5in2 == False and letterR6in2 == False and letterJ7in2 == False and letterJ8in2 == False and letterM9in2 == False and and10in2 == False):
         hide gram_m5_tile94
         hide gram_m5_tile95

         hide gram_m5_tile96
         hide gram_m5_tile97



    #win conditions
    if (letterT5in1 == True or and1in1 == True) and (and1in2 == True or letterT5in2 == True) and (letterR3in3 == True or letterR6in3 == True or and10in3 == True) and (letterK4in4 == True) and (letterJ7in7 == True or letterJ8in7 == True) and (letterJ7in8 == True or letterJ8in8 == True) and (letterR3in5 == True or letterR6in5 == True or and10in5 == True) and (letterM2in9 == True or letterM9in9 == True) and (letterR3in10 == True or letterR6in10 == True or and10in10 == True) and (letterM2in6 == True or letterM9in6 == True):
        image gram_m5_tile202 = "letterT.png"
        image gram_m5_tile206 = "letterM.png"
        image gram_m5_tile203 = "letterR.png"
        image gram_m5_tile205 = "letterK.png"
        image gram_m5_tile201 = "letterT.png"
        image gram_m5_tile204 = "letterR.png"
        image gram_m5_tile208 = "letterJ.png"
        image gram_m5_tile408 = "letterJ.png"
        image gram_m5_tile409 = "letterM.png"
        image gram_m5_tile410 = "letterR.png"
        
        show gram_m5_tile202 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_m5_tile206 at Position(xpos = letterM2x, xanchor = 0, ypos = letterM2y, yanchor = 0)
        show gram_m5_tile203 at Position(xpos = letterR3x, xanchor = 0, ypos = letterR3y, yanchor = 0)
        show gram_m5_tile205 at Position(xpos = letterK4x, xanchor = 0, ypos = letterK4y, yanchor = 0)
        show gram_m5_tile201 at Position(xpos = letterT5x, xanchor = 0, ypos = letterT5y, yanchor = 0)
        show gram_m5_tile204 at Position(xpos = letterR6x, xanchor = 0, ypos = letterR6y, yanchor = 0)
        show gram_m5_tile208 at Position(xpos = letterJ7x, xanchor = 0, ypos = letterJ7y, yanchor = 0)
        show gram_m5_tile408 at Position(xpos = letterJ8x, xanchor = 0, ypos = letterJ8y, yanchor = 0)
        show gram_m5_tile409 at Position(xpos = letterM9x, xanchor = 0, ypos = letterM9y, yanchor = 0)
        show gram_m5_tile410 at Position(xpos = letterR10x, xanchor = 0, ypos = letterR10y, yanchor = 0)

        "Access Gained"

        jump gram_m5#start

    if attempts ==0:
        hide gram_m5_tile42
        hide gram_m5_tile43
        hide gram_m5_tile44
        hide gram_m5_tile45
        hide gram_m5_tile46
        hide gram_m5_tile47
        hide gram_m5_tile48
        hide gram_m5_tile49
        hide gram_m5_tile50
        hide gram_m5_tile51
        hide gram_m5_tile52
        hide gram_m5_tile53
        hide gram_m5_tile54
        hide gram_m5_tile55
        hide gram_m5_tile56
        hide gram_m5_tile61
        hide gram_m5_tile62
        hide gram_m5_tile63
        hide gram_m5_tile64
        hide gram_m5_tile65
        hide gram_m5_tile66
        hide gram_m5_tile67
        hide gram_m5_tile68
        hide gram_m5_tile69
        hide gram_m5_tile70
        hide gram_m5_tile71
        hide gram_m5_tile72
        hide gram_m5_tile73
        hide gram_m5_tile74
        hide gram_m5_tile75

        "You Lose Try Again"

        jump gram_m5#start
    

#    if and1in1 == True or letterM2in1 ==True or letterR3in1 ==True or letterK4in1 ==True:
#        image gram_m5_tile109 = "leftTreegreen.png"
#        #shows gram_m5_tiles
#        show gram_m5_tile109 at Position(xpos = 825, xanchor = 0, ypos = 225, yanchor = 0)
#    if and1in1 == False and letterM2in1 == False and letterR3in1 == False and letterK4in1 ==False:
#        hide gram_m5_tile109      
    
    jump gamefile_m5