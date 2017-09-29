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

screen logicGates_med3:

    draggroup:
        #and gates
        drag:
                drag_name "letterL2"
                child "letterL.png"
                droppable False
                dragged gate_dragged
                xpos letterL1x ypos letterL1y
        drag:
                drag_name "letterN"
                child "letterN.png"
                droppable False
                dragged gate_dragged
                xpos letterN2x ypos letterN2y
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK3x ypos letterK3y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM4x ypos letterM4y
        drag:
                drag_name "letterL"
                child "letterL.png"
                droppable False
                dragged gate_dragged
                xpos letterL5x ypos letterL5y
        drag:
                drag_name "letterK2"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK6x ypos letterK6y
        drag:
                drag_name "letterK3"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK7x ypos letterK7y

        drag:
                drag_name "letterN2"
                child "letterN.png"
                droppable False
                dragged gate_dragged
                xpos letterN8x ypos letterN8y
        
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
                xpos 1355 ypos 485
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1655 ypos 485
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 960 ypos 660

        drag:
                drag_name "gate slot eight"
                draggable False
                child "images/border.png"
                xpos 1175 ypos 660

init:
    image bg Eng_gram_m3_tile = "eng_tile_bg.png"

label gram_m3#start:

    scene bg Eng_gram_m3_tile

    #row1 1-4
    image gram_m3_tile0 = "instruction8.png"
    image gram_m3_tile1 = "1_1_green.png"
    image gram_m3_tile2 = "letterS.png"
    #image gram_m3_tile3 = "treeGrey.png"
    show gram_m3_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_m3_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 130, yanchor = 0)
    show gram_m3_tile2 at Position(xpos = 1260, xanchor = 0, ypos = 145, yanchor = 0)
    #show gram_m3_tile3 at Position(xpos = 1248, xanchor = 0, ypos = 228, yanchor = 0)
    
    #row2 5-8
    #image gram_m3_tile4 = "1_1_grey.png"
    image gram_m3_tile5 = "leftTreelong1.png"
    image gram_m3_tile6 = "rightTreelong1.png"
    #show gram_m3_tile4 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)
    show gram_m3_tile5 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
    show gram_m3_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
    
    #row3 9-13   

    image gram_m3_tile9 = "1_1_grey.png"
    image gram_m3_tile10 = "1_1_grey.png"
    

    show gram_m3_tile9 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)
    show gram_m3_tile10 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    #row4 14-20

    image gram_m3_tile14 = "leftTreelong.png"
    #image gram_m3_tile14 = "leftTreelong.png"
    image gram_m3_tile15 = "rightTreelong.png"
    image gram_m3_tile16 = "leftTreelong.png"
    image gram_m3_tile17 = "rightTreelong.png"

    show gram_m3_tile14 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
    #show gram_m3_tile14 at Position(xpos = 1000, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m3_tile15 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m3_tile16 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m3_tile17 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)


    #row5 21-27

    image gram_m3_tile21 = "1_1_grey.png"
    image gram_m3_tile22 = "1_1_grey.png"
    image gram_m3_tile23 = "1_1_grey.png"
    image gram_m3_tile24 = "1_1_grey.png"

    show gram_m3_tile21 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m3_tile22 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m3_tile23 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m3_tile24 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)

    image gram_m3_tile25 = "rightTree.png"
    image gram_m3_tile26 = "1_1_grey.png"
    show gram_m3_tile25 at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m3_tile26 at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m3_tile27 = "treeGrey.png"
    image gram_m3_tile28 = "1_1_grey.png"
    show gram_m3_tile27 at Position(xpos = 1160, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m3_tile28 at Position(xpos = 1160, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m3_tile31 = "letterBorder.png"
    image gram_m3_tile32 = "letterBorder.png"
    #image gram_m3_tile33 = "letterBorder.png"
    image gram_m3_tile34 = "letterBorder.png"
    image gram_m3_tile35 = "letterBorder.png"
    #image gram_m3_tile36 = "letterBorder.png"
    show gram_m3_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m3_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    #show gram_m3_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show gram_m3_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show gram_m3_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    #show gram_m3_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ letterL1x = 410
    $ letterL1y = 750
    $ letterN2x = 410
    $ letterN2y = 575
    $ letterK3x = 275 
    $ letterK3y = 750
    $ letterM4x = 275
    $ letterM4y = 575
    $ letterL5x = 410
    $ letterL5y = 750
    $ letterK6x = 275 
    $ letterK6y = 750
    $ letterK7x = 275 
    $ letterK7y = 750
    $ letterN8x = 410 
    $ letterN8y = 575

    # check conditons for locations
    $ letterL1in1 = False
    $ letterL1in2 = False
    $ letterL1in3 = False
    $ letterL1in4 = False
    $ letterL1in5 = False
    $ letterL1in6 = False
    $ letterL1in7 = False
    $ letterL1in8 = False

    $ letterN2in1 = False
    $ letterN2in2 = False
    $ letterN2in3 = False
    $ letterN2in4 = False
    $ letterN2in5 = False
    $ letterN2in6 = False
    $ letterN2in7 = False
    $ letterN2in8 = False

    $ letterK3in1 = False
    $ letterK3in2 = False
    $ letterK3in3 = False
    $ letterK3in4 = False
    $ letterK3in5 = False
    $ letterK3in6 = False
    $ letterK3in7 = False
    $ letterK3in8 = False

    $ letterM4in1 = False
    $ letterM4in2 = False
    $ letterM4in3 = False
    $ letterM4in4 = False
    $ letterM4in5 = False
    $ letterM4in6 = False
    $ letterM4in7 = False
    $ letterM4in8 = False

    $ letterL5in1 = False
    $ letterL5in2 = False
    $ letterL5in3 = False
    $ letterL5in4 = False
    $ letterL5in5 = False
    $ letterL5in6 = False
    $ letterL5in7 = False
    $ letterL5in8 = False

    $ letterK6in1 = False
    $ letterK6in2 = False
    $ letterK6in3 = False
    $ letterK6in4 = False
    $ letterK6in5 = False
    $ letterK6in6 = False
    $ letterK6in7 = False
    $ letterK6in8 = False

    $ letterK7in1 = False
    $ letterK7in2 = False
    $ letterK7in3 = False
    $ letterK7in4 = False
    $ letterK7in5 = False
    $ letterK7in6 = False
    $ letterK7in7 = False
    $ letterK7in8 = False

    $ letterN8in1 = False
    $ letterN8in2 = False
    $ letterN8in3 = False
    $ letterN8in4 = False
    $ letterN8in5 = False
    $ letterN8in6 = False
    $ letterN8in7 = False
    $ letterN8in8 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 15
    
    call gamefile_m3

label gamefile_m3:
    #image moon = "images/blankgram_m3_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGates_med3

    if gate_name == "letterL2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m3_tile here
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False
            #sets values for checks
            $ letterL1x = 1025
            $ letterL1y = 315
            $ letterL1in1 = True
            $ letterL1in2 = False
            $ letterL1in3 = False
            $ letterL1in4 = False
            $ letterL1in5 = False
            $ letterL1in6 = False
            $ letterL1in7 = False
            $ letterL1in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterL1x = 1505
            $ letterL1y = 315
            $ letterL1in1 = False
            $ letterL1in2 = True
            $ letterL1in3 = False
            $ letterL1in4 = False
            $ letterL1in5 = False
            $ letterL1in6 = False
            $ letterL1in7 = False
            $ letterL1in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterL1x = 875
            $ letterL1y = 490
            $ letterL1in1 = False
            $ letterL1in2 = False
            $ letterL1in3 = True
            $ letterL1in4 = False
            $ letterL1in5 = False
            $ letterL1in6 = False
            $ letterL1in7 = False
            $ letterL1in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterL1x = 1175
            $ letterL1y = 490
            $ letterL1in1 = False
            $ letterL1in2 = False
            $ letterL1in3 = False
            $ letterL1in4 = True
            $ letterL1in5 = False
            $ letterL1in6 = False
            $ letterL1in7 = False
            $ letterL1in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterL1x = 1355
            $ letterL1y = 490
            $ letterL1in1 = False
            $ letterL1in2 = False
            $ letterL1in3 = False
            $ letterL1in4 = False
            $ letterL1in5 = True
            $ letterL1in6 = False
            $ letterL1in7 = False
            $ letterL1in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterL1x = 1655
            $ letterL1y = 490
            $ letterL1in1 = False
            $ letterL1in2 = False
            $ letterL1in3 = False
            $ letterL1in4 = False
            $ letterL1in5 = False
            $ letterL1in6 = True
            $ letterL1in7 = False
            $ letterL1in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterL1x = 960
            $ letterL1y = 665
            $ letterL1in1 = False
            $ letterL1in2 = False
            $ letterL1in3 = False
            $ letterL1in4 = False
            $ letterL1in5 = False
            $ letterL1in6 = False
            $ letterL1in7 = True
            $ letterL1in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterL1x = 1175
            $ letterL1y = 665
            $ letterL1in1 = False
            $ letterL1in2 = False
            $ letterL1in3 = False
            $ letterL1in4 = False
            $ letterL1in5 = False
            $ letterL1in6 = False
            $ letterL1in7 = False
            $ letterL1in8 = True

    if gate_name == "letterN":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterN2x = 1025
            $ letterN2y = 315
            $ letterN2in1 = True
            $ letterN2in2 = False
            $ letterN2in3 = False
            $ letterN2in4 = False
            $ letterN2in5 = False
            $ letterN2in6 = False
            $ letterN2in7 = False
            $ letterN2in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterN2x = 1505
            $ letterN2y = 315
            $ letterN2in1 = False
            $ letterN2in2 = True
            $ letterN2in3 = False
            $ letterN2in4 = False
            $ letterN2in5 = False
            $ letterN2in6 = False
            $ letterN2in7 = False
            $ letterN2in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterN2x = 875
            $ letterN2y = 490
            $ letterN2in1 = False
            $ letterN2in2 = False
            $ letterN2in3 = True
            $ letterN2in4 = False
            $ letterN2in5 = False
            $ letterN2in6 = False
            $ letterN2in7 = False
            $ letterN2in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterN2x = 1175
            $ letterN2y = 490
            $ letterN2in1 = False
            $ letterN2in2 = False
            $ letterN2in3 = False
            $ letterN2in4 = True
            $ letterN2in5 = False
            $ letterN2in6 = False
            $ letterN2in7 = False
            $ letterN2in8 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterN2x = 1355
            $ letterN2y = 490
            $ letterN2in1 = False
            $ letterN2in2 = False
            $ letterN2in3 = False
            $ letterN2in4 = False
            $ letterN2in5 = True
            $ letterN2in6 = False
            $ letterN2in7 = False
            $ letterN2in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterN2x = 1655
            $ letterN2y = 490
            $ letterN2in1 = False
            $ letterN2in2 = False
            $ letterN2in3 = False
            $ letterN2in4 = False
            $ letterN2in5 = False
            $ letterN2in6 = True
            $ letterN2in7 = False
            $ letterN2in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterN2x = 960
            $ letterN2y = 665
            $ letterN2in1 = False
            $ letterN2in2 = False
            $ letterN2in3 = False
            $ letterN2in4 = False
            $ letterN2in5 = False
            $ letterN2in6 = False
            $ letterN2in7 = True
            $ letterN2in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterN2x = 1175
            $ letterN2y = 665
            $ letterN2in1 = False
            $ letterN2in2 = False
            $ letterN2in3 = False
            $ letterN2in4 = False
            $ letterN2in5 = False
            $ letterN2in6 = False
            $ letterN2in7 = False
            $ letterN2in8 = True

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterK3x = 1025
            $ letterK3y = 315
            $ letterK3in1 = True
            $ letterK3in2 = False
            $ letterK3in3 = False
            $ letterK3in4 = False
            $ letterK3in5 = False
            $ letterK3in6 = False
            $ letterK3in7 = False
            $ letterK3in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterK3x = 1505
            $ letterK3y = 315
            $ letterK3in1 = False
            $ letterK3in2 = True
            $ letterK3in3 = False
            $ letterK3in4 = False
            $ letterK3in5 = False
            $ letterK3in6 = False
            $ letterK3in7 = False
            $ letterK3in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterK3x = 875
            $ letterK3y = 490
            $ letterK3in1 = False
            $ letterK3in2 = False
            $ letterK3in3 = True
            $ letterK3in4 = False
            $ letterK3in5 = False
            $ letterK3in6 = False
            $ letterK3in7 = False
            $ letterK3in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterK3x = 1175
            $ letterK3y = 490
            $ letterK3in1 = False
            $ letterK3in2 = False
            $ letterK3in3 = False
            $ letterK3in4 = True
            $ letterK3in5 = False
            $ letterK3in6 = False
            $ letterK3in7 = False
            $ letterK3in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterK3x = 1355
            $ letterK3y = 490
            $ letterK3in1 = False
            $ letterK3in2 = False
            $ letterK3in3 = False
            $ letterK3in4 = False
            $ letterK3in5 = True
            $ letterK3in6 = False
            $ letterK3in7 = False
            $ letterK3in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterK3x = 1655
            $ letterK3y = 490
            $ letterK3in1 = False
            $ letterK3in2 = False
            $ letterK3in3 = False
            $ letterK3in4 = False
            $ letterK3in5 = False
            $ letterK3in6 = True
            $ letterK3in7 = False
            $ letterK3in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterK3x = 960
            $ letterK3y = 665
            $ letterK3in1 = False
            $ letterK3in2 = False
            $ letterK3in3 = False
            $ letterK3in4 = False
            $ letterK3in5 = False
            $ letterK3in6 = False
            $ letterK3in7 = True
            $ letterK3in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterK3x = 1175
            $ letterK3y = 665
            $ letterK3in1 = False
            $ letterK3in2 = False
            $ letterK3in3 = False
            $ letterK3in4 = False
            $ letterK3in5 = False
            $ letterK3in6 = False
            $ letterK3in7 = False
            $ letterK3in8 = True


    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterM4x = 1025
            $ letterM4y = 315
            $ letterM4in1 = True
            $ letterM4in2 = False
            $ letterM4in3 = False
            $ letterM4in4 = False
            $ letterM4in5 = False
            $ letterM4in6 = False
            $ letterM4in7 = False
            $ letterM4in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterM4x = 1505
            $ letterM4y = 315
            $ letterM4in1 = False
            $ letterM4in2 = True
            $ letterM4in3 = False
            $ letterM4in4 = False
            $ letterM4in5 = False
            $ letterM4in6 = False
            $ letterM4in7 = False
            $ letterM4in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterM4x = 875
            $ letterM4y = 490
            $ letterM4in1 = False
            $ letterM4in2 = False
            $ letterM4in3 = True
            $ letterM4in4 = False
            $ letterM4in5 = False
            $ letterM4in6 = False
            $ letterM4in7 = False
            $ letterM4in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterM4x = 1175
            $ letterM4y = 490
            $ letterM4in1 = False
            $ letterM4in2 = False
            $ letterM4in3 = False
            $ letterM4in4 = True
            $ letterM4in5 = False
            $ letterM4in6 = False
            $ letterM4in7 = False
            $ letterM4in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterM4x = 1355
            $ letterM4y = 490
            $ letterM4in1 = False
            $ letterM4in2 = False
            $ letterM4in3 = False
            $ letterM4in4 = False
            $ letterM4in5 = True
            $ letterM4in6 = False
            $ letterM4in7 = False
            $ letterM4in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterM4x = 1655
            $ letterM4y = 490
            $ letterM4in1 = False
            $ letterM4in2 = False
            $ letterM4in3 = False
            $ letterM4in4 = False
            $ letterM4in5 = False
            $ letterM4in6 = True
            $ letterM4in7 = False
            $ letterM4in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterM4x = 960
            $ letterM4y = 665
            $ letterM4in1 = False
            $ letterM4in2 = False
            $ letterM4in3 = False
            $ letterM4in4 = False
            $ letterM4in5 = False
            $ letterM4in6 = False
            $ letterM4in7 = True
            $ letterM4in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterM4x = 1175
            $ letterM4y = 665
            $ letterM4in1 = False
            $ letterM4in2 = False
            $ letterM4in3 = False
            $ letterM4in4 = False
            $ letterM4in5 = False
            $ letterM4in6 = False
            $ letterM4in7 = False
            $ letterM4in8 = True


    if gate_name == "letterL":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterL5x = 1025
            $ letterL5y = 315
            $ letterL5in1 = True
            $ letterL5in2 = False
            $ letterL5in3 = False
            $ letterL5in4 = False
            $ letterL5in5 = False
            $ letterL5in6 = False
            $ letterL5in7 = False
            $ letterL5in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterL5x = 1505
            $ letterL5y = 315
            $ letterL5in1 = False
            $ letterL5in2 = True
            $ letterL5in3 = False
            $ letterL5in4 = False
            $ letterL5in5 = False
            $ letterL5in6 = False
            $ letterL5in7 = False
            $ letterL5in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterL5x = 875
            $ letterL5y = 490
            $ letterL5in1 = False
            $ letterL5in2 = False
            $ letterL5in3 = True
            $ letterL5in4 = False
            $ letterL5in5 = False
            $ letterL5in6 = False
            $ letterL5in7 = False
            $ letterL5in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterL5x = 1175
            $ letterL5y = 490
            $ letterL5in1 = False
            $ letterL5in2 = False
            $ letterL5in3 = False
            $ letterL5in4 = True
            $ letterL5in5 = False
            $ letterL5in6 = False
            $ letterL5in7 = False
            $ letterL5in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterL5x = 1355
            $ letterL5y = 490
            $ letterL5in1 = False
            $ letterL5in2 = False
            $ letterL5in3 = False
            $ letterL5in4 = False
            $ letterL5in5 = True
            $ letterL5in6 = False
            $ letterL5in7 = False
            $ letterL5in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterL5x = 1655
            $ letterL5y = 490
            $ letterL5in1 = False
            $ letterL5in2 = False
            $ letterL5in3 = False
            $ letterL5in4 = False
            $ letterL5in5 = False
            $ letterL5in6 = True
            $ letterL5in7 = False
            $ letterL5in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterL5x = 960
            $ letterL5y = 665
            $ letterL5in1 = False
            $ letterL5in2 = False
            $ letterL5in3 = False
            $ letterL5in4 = False
            $ letterL5in5 = False
            $ letterL5in6 = False
            $ letterL5in7 = True
            $ letterL5in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterL5x = 1175
            $ letterL5y = 665
            $ letterL5in1 = False
            $ letterL5in2 = False
            $ letterL5in3 = False
            $ letterL5in4 = False
            $ letterL5in5 = False
            $ letterL5in6 = False
            $ letterL5in7 = False
            $ letterL5in8 = True

    if gate_name == "letterK2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterK6x = 1025
            $ letterK6y = 315
            $ letterK6in1 = True
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterK6x = 1505
            $ letterK6y = 315
            $ letterK6in1 = False
            $ letterK6in2 = True
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterK6x = 875
            $ letterK6y = 490
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = True
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterK6x = 1175
            $ letterK6y = 490
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = True
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterK6x = 1355
            $ letterK6y = 490
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = True
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterK6x = 1655
            $ letterK6y = 490
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = True
            $ letterK6in7 = False
            $ letterK6in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterK6x = 960
            $ letterK6y = 665
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = True
            $ letterK6in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterK6x = 1175
            $ letterK6y = 665
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = True

    if gate_name == "letterK3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterK7x = 1025
            $ letterK7y = 315
            $ letterK7in1 = True
            $ letterK7in2 = False
            $ letterK7in3 = False
            $ letterK7in4 = False
            $ letterK7in5 = False
            $ letterK7in6 = False
            $ letterK7in7 = False
            $ letterK7in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterK7x = 1505
            $ letterK7y = 315
            $ letterK7in1 = False
            $ letterK7in2 = True
            $ letterK7in3 = False
            $ letterK7in4 = False
            $ letterK7in5 = False
            $ letterK7in6 = False
            $ letterK7in7 = False
            $ letterK7in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterK7x = 875
            $ letterK7y = 490
            $ letterK7in1 = False
            $ letterK7in2 = False
            $ letterK7in3 = True
            $ letterK7in4 = False
            $ letterK7in5 = False
            $ letterK7in6 = False
            $ letterK7in7 = False
            $ letterK7in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterK7x = 1175
            $ letterK7y = 490
            $ letterK7in1 = False
            $ letterK7in2 = False
            $ letterK7in3 = False
            $ letterK7in4 = True
            $ letterK7in5 = False
            $ letterK7in6 = False
            $ letterK7in7 = False
            $ letterK7in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterK7x = 1355
            $ letterK7y = 490
            $ letterK7in1 = False
            $ letterK7in2 = False
            $ letterK7in3 = False
            $ letterK7in4 = False
            $ letterK7in5 = True
            $ letterK7in6 = False
            $ letterK7in7 = False
            $ letterK7in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterK7x = 1655
            $ letterK7y = 490
            $ letterK7in1 = False
            $ letterK7in2 = False
            $ letterK7in3 = False
            $ letterK7in4 = False
            $ letterK7in5 = False
            $ letterK7in6 = True
            $ letterK7in7 = False
            $ letterK7in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterK7x = 960
            $ letterK7y = 665
            $ letterK7in1 = False
            $ letterK7in2 = False
            $ letterK7in3 = False
            $ letterK7in4 = False
            $ letterK7in5 = False
            $ letterK7in6 = False
            $ letterK7in7 = True
            $ letterK7in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterK7x = 1175
            $ letterK7y = 665
            $ letterK7in1 = False
            $ letterK7in2 = False
            $ letterK7in3 = False
            $ letterK7in4 = False
            $ letterK7in5 = False
            $ letterK7in6 = False
            $ letterK7in7 = False
            $ letterK7in8 = True

    if gate_name == "letterN2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterL1in1 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in1 = False
            if letterN2in1 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in1 = False
            if letterK3in1 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in1 = False
            if letterM4in1 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in1 = False
            if letterL5in1 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in1 = False
            if letterK7in1 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in1 = False
            if letterN8in1 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in1 = False

            #sets values for checks
            $ letterN8x = 1025
            $ letterN8y = 315
            $ letterN8in1 = True
            $ letterN8in2 = False
            $ letterN8in3 = False
            $ letterN8in4 = False
            $ letterN8in5 = False
            $ letterN8in6 = False
            $ letterN8in7 = False
            $ letterN8in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterL1in2 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in2 = False
            if letterN2in2 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in2 = False
            if letterK3in2 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in2 = False
            if letterM4in2 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in2 = False
            if letterL5in2 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in2 = False
            if letterK7in2 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in2 = False
            if letterN8in2 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in2 = False

            #sets check values
            $ letterN8x = 1505
            $ letterN8y = 315
            $ letterN8in1 = False
            $ letterN8in2 = True
            $ letterN8in3 = False
            $ letterN8in4 = False
            $ letterN8in5 = False
            $ letterN8in6 = False
            $ letterN8in7 = False
            $ letterN8in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterL1in3 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in3 = False
            if letterN2in3 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in3 = False
            if letterK3in3 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in3 = False
            if letterM4in3 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in3 = False
            if letterL5in3 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in3 = False
            if letterK7in3 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in3 = False
            if letterN8in3 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in3 = False

            #sets values for the checks
            $ letterN8x = 875
            $ letterN8y = 490
            $ letterN8in1 = False
            $ letterN8in2 = False
            $ letterN8in3 = True
            $ letterN8in4 = False
            $ letterN8in5 = False
            $ letterN8in6 = False
            $ letterN8in7 = False
            $ letterN8in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterL1in4 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in4 = False
            if letterN2in4 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in4 = False
            if letterK3in4 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in4 = False
            if letterM4in4 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in4 = False
            if letterL5in4 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in4 = False
            if letterK7in4 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in4 = False
            if letterN8in4 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in4 = False

            #sets values for the checks
            $ letterN8x = 1175
            $ letterN8y = 490
            $ letterN8in1 = False
            $ letterN8in2 = False
            $ letterN8in3 = False
            $ letterN8in4 = True
            $ letterN8in5 = False
            $ letterN8in6 = False
            $ letterN8in7 = False
            $ letterN8in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterL1in5 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in5 = False
            if letterN2in5 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in5 = False
            if letterK3in5 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in5 = False
            if letterM4in5 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in5 = False
            if letterL5in5 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in5 = False
            if letterK7in5 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in5 = False
            if letterN8in5 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in5 = False

            #sets values for the checks
            $ letterN8x = 1355
            $ letterN8y = 490
            $ letterN8in1 = False
            $ letterN8in2 = False
            $ letterN8in3 = False
            $ letterN8in4 = False
            $ letterN8in5 = True
            $ letterN8in6 = False
            $ letterN8in7 = False
            $ letterN8in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterL1in6 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in6 = False
            if letterN2in6 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in6 = False
            if letterK3in6 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in6 = False
            if letterM4in6 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in6 = False
            if letterL5in6 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in6 = False
            if letterK7in6 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in6 = False
            if letterN8in6 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in6 = False

            #sets values for the checks
            $ letterN8x = 1655
            $ letterN8y = 490
            $ letterN8in1 = False
            $ letterN8in2 = False
            $ letterN8in3 = False
            $ letterN8in4 = False
            $ letterN8in5 = False
            $ letterN8in6 = True
            $ letterN8in7 = False
            $ letterN8in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterL1in7 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in7 = False
            if letterN2in7 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in7 = False
            if letterK3in7 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in7 = False
            if letterM4in7 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in7 = False
            if letterL5in7 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in7 = False
            if letterK7in7 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in7 = False
            if letterN8in7 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in7 = False

            #sets values for the checks
            $ letterN8x = 960
            $ letterN8y = 665
            $ letterN8in1 = False
            $ letterN8in2 = False
            $ letterN8in3 = False
            $ letterN8in4 = False
            $ letterN8in5 = False
            $ letterN8in6 = False
            $ letterN8in7 = True
            $ letterN8in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterL1in8 == True:
               $ letterL1x = 410
               $ letterL1y = 750
               $ letterL1in8 = False
            if letterN2in8 == True:
               $ letterN2x = 410
               $ letterN2y = 575
               $ letterN2in8 = False
            if letterK3in8 == True:
               $ letterK3x = 275
               $ letterK3y = 750
               $ letterK3in8 = False
            if letterM4in8 == True:
               $ letterM4x = 275
               $ letterM4y = 575
               $ letterM4in8 = False
            if letterL5in8 == True:
               $ letterL5x = 410
               $ letterL5y = 750
               $ letterL5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 275
               $ letterK6y = 750
               $ letterK6in8 = False
            if letterK7in8 == True:
               $ letterK7x = 275
               $ letterK7y = 750
               $ letterK7in8 = False
            if letterN8in8 == True:
               $ letterN8x = 410
               $ letterN8y = 575
               $ letterN8in8 = False

            #sets values for the checks
            $ letterN8x = 1175
            $ letterN8y = 665
            $ letterN8in1 = False
            $ letterN8in2 = False
            $ letterN8in3 = False
            $ letterN8in4 = False
            $ letterN8in5 = False
            $ letterN8in6 = False
            $ letterN8in7 = False
            $ letterN8in8 = True

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



    if (letterL5in1 == True or letterL1in1 == True) and (letterL1in2 == True or letterL5in2 == True):
        image gram_m3_tile42 = "leftTreegreenlong1.png"
        image gram_m3_tile43 = "1_1_green.png"
        show gram_m3_tile42 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m3_tile43 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m3_tile62 = "rightTreegreenlong1.png"
        image gram_m3_tile63 = "1_1_green.png"
        show gram_m3_tile62 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m3_tile63 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)
        
        if (letterK3in3 == True or letterK6in3 == True or letterK7in3 == True) and (letterM4in4 == True):
            image gram_m3_tile44 = "leftTreegreenlong.png"
            #image gram_m3_tile44 = "leftTreegreenlong.png"
            image gram_m3_tile45 = "1_1_green.png"
            image gram_m3_tile46 = "solutionLine_grey.png"
            image gram_m3_tile47 = "solutionLine_grey.png"
            image gram_m3_tile48 = "solutionLine_grey.png"
            image gram_m3_tile207 = "solutionLine_grey.png"
            image gram_m3_tile49 = "epsilon.png"

            show gram_m3_tile44 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            #show gram_m3_tile44 at Position(xpos = 1000, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile45 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m3_tile46 at Position(xpos = 830, xanchor = 0, ypos = 572, yanchor = 0)
            show gram_m3_tile47 at Position(xpos = 830, xanchor = 0, ypos = 646, yanchor = 0)
            show gram_m3_tile48 at Position(xpos = 830, xanchor = 0, ypos = 715, yanchor = 0)
            show gram_m3_tile207 at Position(xpos = 830, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m3_tile49 at Position(xpos = 785, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_m3_tile56 = "rightTreegreenlong.png"
            image gram_m3_tile57 = "1_1_green.png"
            #image gram_m3_tile58 = "solutionLine.png"
            #image gram_m3_tile209 = "solutionLine.png"
            #image gram_m3_tile210 = "solutionLine.png"
            #image gram_m3_tile59 = "a.png"
            show gram_m3_tile56 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile57 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
            #show gram_m3_tile58 at Position(xpos = 1185, xanchor = 0, ypos = 570, yanchor = 0)
            #show gram_m3_tile209 at Position(xpos = 1185, xanchor = 0, ypos = 662, yanchor = 0)
            #show gram_m3_tile210 at Position(xpos = 1185, xanchor = 0, ypos = 755, yanchor = 0)
            #show gram_m3_tile59 at Position(xpos = 1150, xanchor = 0, ypos = 800, yanchor = 0)

            if (letterK3in7 == True or letterK6in7 == True or letterK7in7 == True):
               #image gram_m3_tile50 = "leftTreegreen.png"
               image gram_m3_tile50 = "rightTreegreen.png"
               image gram_m3_tile51 = "1_1_green.png"
               image gram_m3_tile52 = "solutionLine.png"
               image gram_m3_tile53 = "a.png"
               #show gram_m3_tile50 at Position(xpos = 960, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile50 at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile51 at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)
               show gram_m3_tile52 at Position(xpos = 950, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m3_tile53 at Position(xpos = 945, xanchor = 0, ypos = 800, yanchor = 0)

            if (letterK3in7 == False and letterK6in7 == False and letterK7in7 == False):
               hide gram_m3_tile50
               hide gram_m3_tile51
               hide gram_m3_tile52
               hide gram_m3_tile53


            if (letterN2in8 == True or letterN8in8 == True):
               image gram_m3_tile215 = "treeGreen.png"
               image gram_m3_tile216 = "1_1_green.png"
               show gram_m3_tile215 at Position(xpos = 1160, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile216 at Position(xpos = 1160, xanchor = 0, ypos = 650, yanchor = 0)
               image gram_m3_tile210 = "solutionLine.png"
               image gram_m3_tile59 = "b.png"
               show gram_m3_tile210 at Position(xpos = 1165, xanchor = 0, ypos = 750, yanchor = 0)
               show gram_m3_tile59 at Position(xpos = 1140, xanchor = 0, ypos = 800, yanchor = 0)



            if (letterN2in8 == False and letterN8in8 == False):
               hide gram_m3_tile215
               hide gram_m3_tile216
               hide gram_m3_tile210
               hide gram_m3_tile59

            if (letterL1in7 == True or letterN2in7 == True or letterM4in7 == True or letterL5in7 == True or letterN8in7 == True):
               image gram_m3_tile260 = "rightTreered.png"
               image gram_m3_tile261 = "1_1_red.png"
               show gram_m3_tile260 at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile261 at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)

            if (letterL1in7 == False and letterN2in7 == False and letterM4in7 == False and letterL5in7 == False and letterN8in7 == False):
               hide gram_m3_tile260
               hide gram_m3_tile261

            if (letterL1in8 == True or letterK3in8 == True or letterM4in8 == True or letterL5in8 == True or letterK6in8 == True or letterK7in8 == True):
               image gram_m3_tile262 = "treeRed.png"
               image gram_m3_tile263 = "1_1_red.png"
               show gram_m3_tile262 at Position(xpos = 1160, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile263 at Position(xpos = 1160, xanchor = 0, ypos = 650, yanchor = 0)

            if (letterL1in8 == False and letterK3in8 == False and letterM4in8 == False and letterL5in8 == False and letterK6in8 == False and letterK7in8 == False):
               hide gram_m3_tile262
               hide gram_m3_tile263

            #if (letterL1in7 == True or letterN2in7 == True or letterK3in7 == True or letterM4in7 == True or letterL5in7 == True or letterN8in7 == True) and (letterL1in8 == True or letterN2in8 == True or letterK3in8 == True or letterM4in8 == True or letterL5in8 == True or letterK6in8 == True or letterK7in8 == True or letterN8in8 == True):
            #   image gram_m3_tile264 = "rightTreered.png"
            #   image gram_m3_tile265 = "1_1_red.png"
            #   show gram_m3_tile264 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
            #   show gram_m3_tile265 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)
            #   image gram_m3_tile266 = "treeRed.png"
            #   image gram_m3_tile267 = "1_1_red.png"
            #   show gram_m3_tile266 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
            #   show gram_m3_tile267 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)

            #if (letterL1in7 == False and letterN2in7 == False and letterK3in7 == False and letterM4in7 == False and letterL5in7 == False and letterN8in7 == False) or (letterL1in8 == False and letterN2in8 == False and letterK3in8 == False and letterM4in8 == False and letterL5in8 == False and letterK6in8 == False and letterK7in8 == False and letterN8in8 == False):
            #   hide gram_m3_tile264
            #   hide gram_m3_tile265
            #   hide gram_m3_tile266
            #   hide gram_m3_tile267

        if (letterK3in3 == False and letterK6in3 == False and letterK7in3 == False) or (letterM4in4 == False):
            hide gram_m3_tile44
            hide gram_m3_tile45
            hide gram_m3_tile46
            hide gram_m3_tile47
            hide gram_m3_tile48
            hide gram_m3_tile207
            hide gram_m3_tile49
            hide gram_m3_tile50
            hide gram_m3_tile51
            hide gram_m3_tile52
            hide gram_m3_tile53

            hide gram_m3_tile215
            hide gram_m3_tile216
            hide gram_m3_tile210
            hide gram_m3_tile59

            hide gram_m3_tile56
            hide gram_m3_tile57
            hide gram_m3_tile58
            hide gram_m3_tile209
            hide gram_m3_tile210
            hide gram_m3_tile59

            hide gram_m3_tile260
            hide gram_m3_tile261
            hide gram_m3_tile262
            hide gram_m3_tile263

            hide gram_m3_tile264
            hide gram_m3_tile265
            hide gram_m3_tile266
            hide gram_m3_tile267
     
        if (letterL1in3 == True or letterN2in3 == True or letterK3in3 == True or letterM4in3 == True or letterL5in3 == True or letterK6in3 == True or letterK7in3 == True or letterN8in3 == True) and (letterL1in4 == True or letterN2in4 == True or letterK3in4 == True or letterL5in4 == True or letterK6in4 == True or letterK7in4 == True or letterN8in4 == True):
            image gram_m3_tile54 = "leftTreeredlong.png"
            image gram_m3_tile55 = "1_1_red.png"
            show gram_m3_tile54 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile55 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile60 = "rightTreeredlong.png"
            image gram_m3_tile61 = "1_1_red.png"
            show gram_m3_tile60 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile61 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
        if (letterL1in3 == False and letterN2in3 == False and letterK3in3 == False and letterM4in3 == False and letterL5in3 == False and letterK6in3 == False and letterK7in3 == False and letterN8in3 == False) or (letterN2in4 == False and letterK3in4 == False and letterL5in4 == False and letterK6in4 == False and letterK7in4 == False and letterN8in4 == False):
            hide gram_m3_tile54
            hide gram_m3_tile55

            hide gram_m3_tile60
            hide gram_m3_tile61

        if (letterL1in3 == True or letterN2in3 == True or letterM4in3 == True or letterL5in3 == True or letterN8in3 == True) and (letterL1in4 == True or letterN2in4 == True or letterK3in4 == True or letterM4in4 == True or letterL5in4 == True or letterK6in4 == True or letterK7in4 == True or letterN8in4 == True):
            image gram_m3_tile254 = "leftTreeredlong.png"
            image gram_m3_tile255 = "1_1_red.png"
            show gram_m3_tile254 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile255 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile260 = "rightTreeredlong.png"
            image gram_m3_tile261 = "1_1_red.png"
            show gram_m3_tile260 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile261 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
        if (letterL1in3 == False and letterN2in3 == False and letterM4in3 == False and letterL5in3 == False and letterN8in3 == False) or (letterL1in4 == False and letterN2in4 == False and letterK3in4 == False and letterM4in4 == False and letterL5in4 == False and letterK6in4 == False and letterK7in4 == False and letterN8in4 == False):
            hide gram_m3_tile254
            hide gram_m3_tile255

            hide gram_m3_tile260
            hide gram_m3_tile261

        if (letterK3in5 == True or letterK6in5 == True or letterK7in5 == True) and (letterN2in6 == True or letterN8in6 == True):
            image gram_m3_tile64 = "leftTreegreenlong.png"
            image gram_m3_tile65 = "1_1_green.png"
            image gram_m3_tile66 = "solutionLine.png"
            image gram_m3_tile211 = "solutionLine.png"
            image gram_m3_tile212 = "solutionLine.png"
            image gram_m3_tile67 = "a.png"
            show gram_m3_tile64 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile65 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m3_tile66 at Position(xpos = 1340, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m3_tile211 at Position(xpos = 1340, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m3_tile212 at Position(xpos = 1340, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m3_tile67 at Position(xpos = 1315, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_m3_tile70 = "rightTreegreenlong.png"
            image gram_m3_tile71 = "1_1_green.png"
            image gram_m3_tile72 = "solutionLine.png"
            image gram_m3_tile213 = "solutionLine.png"
            image gram_m3_tile214 = "solutionLine.png"
            image gram_m3_tile73 = "b.png"
            show gram_m3_tile70 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile71 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m3_tile72 at Position(xpos = 1640, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m3_tile213 at Position(xpos = 1640, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m3_tile214 at Position(xpos = 1640, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m3_tile73 at Position(xpos = 1620, xanchor = 0, ypos = 800, yanchor = 0)


        if (letterK3in5 == False and letterK6in5 == False and letterK7in5 == False) or (letterN2in6 == False and letterN8in6 == False):
            hide gram_m3_tile64
            hide gram_m3_tile65
            hide gram_m3_tile66
            hide gram_m3_tile211
            hide gram_m3_tile212
            hide gram_m3_tile67

            hide gram_m3_tile70
            hide gram_m3_tile71
            hide gram_m3_tile72
            hide gram_m3_tile213
            hide gram_m3_tile214
            hide gram_m3_tile73

        if (letterL1in5 == True or letterN2in5 == True or letterK3in5 == True or letterM4in5 == True or letterL5in5 == True or letterK6in5 == True or letterK7in5 == True or letterN8in5 == True) and (letterL1in6 == True or letterK3in6 == True or letterM4in6 == True or letterL5in6 == True or letterK6in6 == True or letterK7in6 == True):
            image gram_m3_tile68 = "leftTreeredlong.png"
            image gram_m3_tile69 = "1_1_red.png"
            show gram_m3_tile68 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile69 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile74 = "rightTreeredlong.png"
            image gram_m3_tile75 = "1_1_red.png"
            show gram_m3_tile74 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile75 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)

        if (letterL1in5 == False and letterN2in5 == False and letterK3in5 == False and letterM4in5 == False and letterL5in5 == False and letterK6in5 == False and letterK7in5 == False and letterN8in5 == False) or (letterL1in6 == False and letterK3in6 == False and letterM4in6 == False and letterL5in6 == False and letterK6in6 == False and letterK7in6 == False):
            hide gram_m3_tile68
            hide gram_m3_tile69

            hide gram_m3_tile74
            hide gram_m3_tile75

        if (letterL1in5 == True or letterN2in5 == True or letterM4in5 == True or letterL5in5 == True or letterN8in5 == True) and (letterL1in6 == True or letterN2in6 == True or letterK3in6 == True or letterM4in6 == True or letterL5in6 == True or letterK6in6 == True or letterK7in6 == True or letterN8in6 == True):
            image gram_m3_tile76 = "leftTreeredlong.png"
            image gram_m3_tile77 = "1_1_red.png"
            show gram_m3_tile76 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile77 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile78 = "rightTreeredlong.png"
            image gram_m3_tile79 = "1_1_red.png"
            show gram_m3_tile78 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile79 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)

        if (letterL1in5 == False and letterN2in5 == False and letterM4in5 == False and letterL5in5 == False and letterN8in5 == False) or (letterL1in6 == False and letterN2in6 == False and letterK3in6 == False and letterM4in6 == False and letterL5in6 == False and letterK6in6 == False and letterK7in6 == False and letterN8in6 == False):
            hide gram_m3_tile76
            hide gram_m3_tile77

            hide gram_m3_tile78
            hide gram_m3_tile79

    if (letterL5in1 == False and letterL1in1 == False) or (letterL1in2 == False and letterL5in2 == False):
        hide gram_m3_tile42
        hide gram_m3_tile43
        hide gram_m3_tile44
        hide gram_m3_tile45
        hide gram_m3_tile46
        hide gram_m3_tile47
        hide gram_m3_tile48
        hide gram_m3_tile207
        hide gram_m3_tile49
        hide gram_m3_tile50
        hide gram_m3_tile51
        hide gram_m3_tile52
        hide gram_m3_tile53

        hide gram_m3_tile215
        hide gram_m3_tile216
        hide gram_m3_tile210
        hide gram_m3_tile59

        hide gram_m3_tile260
        hide gram_m3_tile261
        hide gram_m3_tile262
        hide gram_m3_tile263

        hide gram_m3_tile264
        hide gram_m3_tile265
        hide gram_m3_tile266
        hide gram_m3_tile267

        hide gram_m3_tile56
        hide gram_m3_tile57
        hide gram_m3_tile58
        hide gram_m3_tile209
        hide gram_m3_tile210
        hide gram_m3_tile59
        hide gram_m3_tile60
        hide gram_m3_tile61

        hide gram_m3_tile62
        hide gram_m3_tile61
        hide gram_m3_tile62
        hide gram_m3_tile63
        hide gram_m3_tile64
        hide gram_m3_tile65
        hide gram_m3_tile66
        hide gram_m3_tile211
        hide gram_m3_tile212
        hide gram_m3_tile67
        hide gram_m3_tile68
        hide gram_m3_tile69
        hide gram_m3_tile70
        hide gram_m3_tile71
        hide gram_m3_tile72
        hide gram_m3_tile213
        hide gram_m3_tile214
        hide gram_m3_tile73
        hide gram_m3_tile74
        hide gram_m3_tile75


    if (letterL1in1 == True or letterN2in1 == True or letterK3in1 == True or letterM4in1 == True or letterL5in1 == True or letterK6in1 == True or letterK7in1 == True or letterN8in1 == True) and (letterN2in2 == True or letterK3in2 == True or letterM4in2 == True or letterK6in2 == True or letterK7in2 == True or letterN8in2 == True):
         image gram_m3_tile90 = "leftTreeredlong1.png"
         image gram_m3_tile91 = "1_1_red.png"
         show gram_m3_tile90 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m3_tile91 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

         image gram_m3_tile92 = "rightTreeredlong1.png"
         image gram_m3_tile93 = "1_1_red.png"
         show gram_m3_tile92 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m3_tile93 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    elif (letterL1in1 == False and letterN2in1 == False and letterK3in1 == False and letterM4in1 == False and letterL5in1 == False and letterK6in1 == False and letterK7in1 == False and letterN8in1 == False) or (letterN2in2 == False and letterK3in2 == False and letterM4in2 == False and letterK6in2 == False and letterK7in2 == False and letterN8in2 == False):
         hide gram_m3_tile90
         hide gram_m3_tile91

         hide gram_m3_tile92
         hide gram_m3_tile93

    if (letterN2in1 == True or letterK3in1 == True or letterM4in1 == True or letterK6in1 == True or letterK7in1 == True or letterN8in1 == True) and (letterL1in2 == True or letterN2in2 == True or letterK3in2 == True or letterM4in2 == True or letterL5in2 == True or letterK6in2 == True or letterK7in2 == True or letterN8in2 == True):
         image gram_m3_tile94 = "leftTreeredlong1.png"
         image gram_m3_tile95 = "1_1_red.png"
         show gram_m3_tile94 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m3_tile95 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

         image gram_m3_tile96 = "rightTreeredlong1.png"
         image gram_m3_tile97 = "1_1_red.png"
         show gram_m3_tile96 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m3_tile97 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    elif (letterN2in1 == False and letterK3in1 == False and letterM4in1 == False and letterK6in1 == False and letterK7in1 == False and letterN8in1 == False) or (letterL1in2 == False and letterN2in2 == False and letterK3in2 == False and letterM4in2 == False and letterL5in2 == False and letterK6in2 == False and letterK7in2 == False and letterN8in2 == False):
         hide gram_m3_tile94
         hide gram_m3_tile95

         hide gram_m3_tile96
         hide gram_m3_tile97



    #win conditions
    if  (letterL5in1 == True or letterL1in1 == True) and (letterL1in2 == True or letterL5in2 == True) and (letterK3in3 == True or letterK6in3 == True or letterK7in3 == True) and (letterM4in4 == True) and (letterK3in7 == True or letterK6in7 == True or letterK7in7 == True) and (letterN2in8 == True or letterN8in8 == True) and (letterK3in5 == True or letterK6in5 == True or letterK7in5 == True) and (letterN2in6 == True or letterN8in6 == True):
        image gram_m3_tile202 = "letterL.png"
        image gram_m3_tile206 = "letterN.png"
        image gram_m3_tile203 = "letterK.png"
        image gram_m3_tile205 = "letterM.png"
        image gram_m3_tile201 = "letterL.png"
        image gram_m3_tile204 = "letterK.png"
        image gram_m3_tile208 = "letterK.png"
        image gram_m3_tile250 = "letterN.png"
        
        show gram_m3_tile202 at Position(xpos = letterL1x, xanchor = 0, ypos = letterL1y, yanchor = 0)
        show gram_m3_tile206 at Position(xpos = letterN2x, xanchor = 0, ypos = letterN2y, yanchor = 0)
        show gram_m3_tile203 at Position(xpos = letterK3x, xanchor = 0, ypos = letterK3y, yanchor = 0)
        show gram_m3_tile205 at Position(xpos = letterM4x, xanchor = 0, ypos = letterM4y, yanchor = 0)
        show gram_m3_tile201 at Position(xpos = letterL5x, xanchor = 0, ypos = letterL5y, yanchor = 0)
        show gram_m3_tile204 at Position(xpos = letterK6x, xanchor = 0, ypos = letterK6y, yanchor = 0)
        show gram_m3_tile208 at Position(xpos = letterK7x, xanchor = 0, ypos = letterK7y, yanchor = 0)
        show gram_m3_tile250 at Position(xpos = letterN8x, xanchor = 0, ypos = letterN8y, yanchor = 0)

        "Access Gained"

        jump gram_m3#start

    if attempts ==0:
        hide gram_m3_tile42
        hide gram_m3_tile43
        hide gram_m3_tile44
        hide gram_m3_tile45
        hide gram_m3_tile46
        hide gram_m3_tile47
        hide gram_m3_tile48
        hide gram_m3_tile49
        hide gram_m3_tile50
        hide gram_m3_tile51
        hide gram_m3_tile52
        hide gram_m3_tile53
        hide gram_m3_tile54
        hide gram_m3_tile55
        hide gram_m3_tile56
        hide gram_m3_tile61
        hide gram_m3_tile62
        hide gram_m3_tile63
        hide gram_m3_tile64
        hide gram_m3_tile65
        hide gram_m3_tile66
        hide gram_m3_tile67
        hide gram_m3_tile68
        hide gram_m3_tile69
        hide gram_m3_tile70
        hide gram_m3_tile71
        hide gram_m3_tile72
        hide gram_m3_tile73
        hide gram_m3_tile74
        hide gram_m3_tile75

        "You Lose Try Again"

        jump gram_m3#start
    

#    if letterL1in1 == True or letterN2in1 ==True or letterK3in1 ==True or letterM4in1 ==True:
#        image gram_m3_tile109 = "leftTreegreen.png"
#        #shows gram_m3_tiles
#        show gram_m3_tile109 at Position(xpos = 825, xanchor = 0, ypos = 225, yanchor = 0)
#    if letterL1in1 == False and letterN2in1 == False and letterK3in1 == False and letterM4in1 ==False:
#        hide gram_m3_tile109      
    
    jump gamefile_m3