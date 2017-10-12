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
        return 


screen logicGatesh2:
    
    draggroup:
        # and gates
        drag:
                drag_name "letterT1"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT1x ypos letterT1y
        drag:
                drag_name "letterT2"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT2x ypos letterT2y
        drag:
                drag_name "letterT3"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT3x ypos letterT3y
        drag:
                drag_name "letterQ1"
                child "letterQ.png"
                droppable False
                dragged gate_dragged
                xpos letterQ4x ypos letterQ4y
        drag:
                drag_name "letterQ2"
                child "letterQ.png"
                droppable False
                dragged gate_dragged
                xpos letterQ5x ypos letterQ5y
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK6x ypos letterK6y
                
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJ7x ypos letterJ7y
        
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM8x ypos letterM8y
        
        drag:
                drag_name "letterS1"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS9x ypos letterS9y
        
        drag:
                drag_name "letterS2"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS10x ypos letterS10y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 1085 ypos 340
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1465 ypos 340
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 925 ypos 510
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 1245 ypos 510
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1465 ypos 510
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1035 ypos 685
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 1170 ypos 685
        drag:
                drag_name "gate slot eight"
                draggable False
                child "images/border.png"
                xpos 1325 ypos 685
        drag:
                drag_name "gate slot nine"
                draggable False
                child "images/border.png"
                xpos 1465 ypos 685
        drag:
                drag_name "gate slot ten"
                draggable False
                child "images/border.png"
                xpos 1595 ypos 685
                
                #letter dragback
        
        drag:
                drag_name "LetterT_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterM_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738
                
        drag:
                drag_name "LetterJ_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648
                
        drag:
                drag_name "LetterS_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 817
                
        drag:
                drag_name "LetterQ_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738


init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_h2:

    scene bg Eng_Tile
    $ quick_menu = False
    $ game_menu = True

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image eaeng_h2_tile0 = "instructions12.png"
    image eaeng_h2_tile1 = "1_1_green.png"
    image eaeng_h2_tile2 = "letterS.png"
    show eaeng_h2_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_h2_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_h2_tile2 at Position(xpos = 1265, xanchor = 0, ypos = 165, yanchor = 0)
    
    #row2 5-8

    image eaeng_h2_tile5 = "leftTreelong.png"
    image eaeng_h2_tile6 = "rightTreelong.png"

    show eaeng_h2_tile5 at Position(xpos = 1120, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_h2_tile6 at Position(xpos = 1330, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_h2_tile9 = "1_1_grey.png"
    image eaeng_h2_tile10 = "1_1_grey.png"
    

    show eaeng_h2_tile9 at Position(xpos = 1070, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_h2_tile10 at Position(xpos = 1450, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_h2_tile14 = "leftTreelong.png"
    image eaeng_h2_tile15 = "rightTreelong.png"
    image eaeng_h2_tile17 = "treeGrey.png"

    show eaeng_h2_tile14 at Position(xpos = 950, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_h2_tile15 at Position(xpos = 1140, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_h2_tile17 at Position(xpos = 1450, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_h2_tile21 = "1_1_grey.png"
    image eaeng_h2_tile22 = "1_1_grey.png"
    image eaeng_h2_tile23 = "1_1_grey.png"

    show eaeng_h2_tile21 at Position(xpos = 910, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_h2_tile22 at Position(xpos = 1230, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_h2_tile23 at Position(xpos = 1450, xanchor = 0, ypos = 500, yanchor = 0)
    
    
    #row6 28-34

    image eaeng_h2_tile29 = "rightTree.png"
    image eaeng_h2_tile30 = "leftTree.png"
    image eaeng_h2_tile31 = "rightTree.png"
    image eaeng_h2_tile32 = "treeGrey.png"
    image eaeng_h2_tile33 = "rightTree.png"
    
    show eaeng_h2_tile29 at Position(xpos = 990, xanchor = 0, ypos = 600, yanchor = 0)
    show eaeng_h2_tile30 at Position(xpos = 1195, xanchor = 0, ypos = 600, yanchor = 0)
    show eaeng_h2_tile31 at Position(xpos = 1295, xanchor = 0, ypos = 600, yanchor = 0)
    show eaeng_h2_tile32 at Position(xpos = 1450, xanchor = 0, ypos = 600, yanchor = 0)
    show eaeng_h2_tile33 at Position(xpos = 1530, xanchor = 0, ypos = 600, yanchor = 0)
    
    
    #row6 35-41

    image eaeng_h2_tile36 = "1_1_grey.png"
    image eaeng_h2_tile37 = "1_1_grey.png"
    image eaeng_h2_tile38 = "1_1_grey.png"
    image eaeng_h2_tile39 = "1_1_grey.png"
    image eaeng_h2_tile40 = "1_1_grey.png"
    
    show eaeng_h2_tile36 at Position(xpos = 1020, xanchor = 0, ypos = 675, yanchor = 0)
    show eaeng_h2_tile37 at Position(xpos = 1155, xanchor = 0, ypos = 675, yanchor = 0)
    show eaeng_h2_tile38 at Position(xpos = 1310, xanchor = 0, ypos = 675, yanchor = 0)
    show eaeng_h2_tile39 at Position(xpos = 1450, xanchor = 0, ypos = 675, yanchor = 0)
    show eaeng_h2_tile40 at Position(xpos = 1580, xanchor = 0, ypos = 675, yanchor = 0)

    image eaeng_h2_tile41 = "letterT_grey.png"
    image eaeng_h2_tile42 = "letterK_grey.png"
    image eaeng_h2_tile43 = "letterJ_grey.png"
    image eaeng_h2_tile44 = "letterQ_grey.png"
    image eaeng_h2_tile45 = "letterM_grey.png"
    image eaeng_h2_tile46 = "letterS_grey.png"
    show eaeng_h2_tile41 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_h2_tile42 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_h2_tile43 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_h2_tile44 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_h2_tile45 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_h2_tile46 at Position(xpos = 342, xanchor = 0, ypos = 831, yanchor = 0)


    # gates
    $ letterT1x = 275 
    $ letterT1y = 575
    $ letterT2x = 275
    $ letterT2y = 575
    $ letterT3x = 275 
    $ letterT3y = 575
    $ letterQ4x = 275
    $ letterQ4y = 750
    $ letterQ5x = 275
    $ letterQ5y = 750
    $ letterK6x = 410 
    $ letterK6y = 575
    $ letterJ7x = 342 
    $ letterJ7y = 660
    $ letterM8x = 410 
    $ letterM8y = 750
    $ letterS9x = 342 
    $ letterS9y = 832
    $ letterS10x = 342 
    $ letterS10y = 832
    
    # check conditons for locations
    $ letterT1in1 = False
    $ letterT1in2 = False
    $ letterT1in3 = False
    $ letterT1in4 = False
    $ letterT1in5 = False
    $ letterT1in6 = False
    $ letterT1in7 = False
    $ letterT1in8 = False
    $ letterT1in9 = False
    $ letterT1in10 = False

    $ letterT2in1 = False
    $ letterT2in2 = False
    $ letterT2in3 = False
    $ letterT2in4 = False
    $ letterT2in5 = False
    $ letterT2in6 = False
    $ letterT2in7 = False
    $ letterT2in8 = False
    $ letterT2in9 = False
    $ letterT2in10 = False

    $ letterT3in1 = False
    $ letterT3in2 = False
    $ letterT3in3 = False
    $ letterT3in4 = False
    $ letterT3in5 = False
    $ letterT3in6 = False
    $ letterT3in7 = False
    $ letterT3in8 = False
    $ letterT3in9 = False
    $ letterT3in10 = False

    $ letterQ4in1 = False
    $ letterQ4in2 = False
    $ letterQ4in3 = False
    $ letterQ4in4 = False
    $ letterQ4in5 = False
    $ letterQ4in6 = False
    $ letterQ4in7 = False
    $ letterQ4in8 = False
    $ letterQ4in9 = False
    $ letterQ4in10 = False
    
    $ letterQ5in1 = False
    $ letterQ5in2 = False
    $ letterQ5in3 = False
    $ letterQ5in4 = False
    $ letterQ5in5 = False
    $ letterQ5in6 = False
    $ letterQ5in7 = False
    $ letterQ5in8 = False
    $ letterQ5in9 = False
    $ letterQ5in10 = False
    
    $ letterK6in1 = False
    $ letterK6in2 = False
    $ letterK6in3 = False
    $ letterK6in4 = False
    $ letterK6in5 = False
    $ letterK6in6 = False
    $ letterK6in7 = False
    $ letterK6in8 = False
    $ letterK6in9 = False
    $ letterK6in10 = False

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

    $ letterM8in1 = False
    $ letterM8in2 = False
    $ letterM8in3 = False
    $ letterM8in4 = False
    $ letterM8in5 = False
    $ letterM8in6 = False
    $ letterM8in7 = False
    $ letterM8in8 = False
    $ letterM8in9 = False
    $ letterM8in10 = False
    
    $ letterS9in1 = False
    $ letterS9in2 = False
    $ letterS9in3 = False
    $ letterS9in4 = False
    $ letterS9in5 = False
    $ letterS9in6 = False
    $ letterS9in7 = False
    $ letterS9in8 = False
    $ letterS9in9 = False
    $ letterS9in10 = False
    
    $ letterS10in1 = False
    $ letterS10in2 = False
    $ letterS10in3 = False
    $ letterS10in4 = False
    $ letterS10in5 = False
    $ letterS10in6 = False
    $ letterS10in7 = False
    $ letterS10in8 = False
    $ letterS10in9 = False
    $ letterS10in10 = False
    
    #gate test vars for dragbacks
    $ temp_slot = ""
    $ temp_gate = ""
    
    #attempts for players
    $ attempts = 15
    
    call gamefile_h2



label gamefile_h2:
    #image moon = "images/blankeaeng_h2_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatesh2

    if gate_name == "letterT1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterT1x = 1085
            $ letterT1y = 340
            $ letterT1in1 = True
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterT1x = 1465
            $ letterT1y = 340
            $ letterT1in1 = False
            $ letterT1in2 = True
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False

        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterT1x = 925
            $ letterT1y = 515
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = True
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterT1x = 1245
            $ letterT1y = 515
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = True
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterT1x = 1465
            $ letterT1y = 515
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = True
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterT1x = 1035
            $ letterT1y = 690
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = True
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterT1x = 1170
            $ letterT1y = 690
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = True
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterT1x = 1325
            $ letterT1y = 690
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = True
            $ letterT1in9 = False
            $ letterT1in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterT1x = 1465
            $ letterT1y = 690
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = True
            $ letterT1in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterT1x = 1595
            $ letterT1y = 690
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
            $ letterT1in9 = False
            $ letterT1in10 = True
            

    if gate_name == "letterT2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterT2x = 1085
            $ letterT2y = 340
            $ letterT2in1 = True
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterT2x = 1465
            $ letterT2y = 340
            $ letterT2in1 = False
            $ letterT2in2 = True
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterT2x = 925
            $ letterT2y = 515
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = True
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterT2x = 1245
            $ letterT2y = 515
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = True
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterT2x = 1465
            $ letterT2y = 515
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = True
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterT2x = 1035
            $ letterT2y = 690
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = True
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterT2x = 1170
            $ letterT2y = 690
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = True
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterT2x = 1325
            $ letterT2y = 690
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = True
            $ letterT2in9 = False
            $ letterT2in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterT2x = 1465
            $ letterT2y = 690
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = True
            $ letterT2in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterT2x = 1595
            $ letterT2y = 690
            $ letterT2in1 = False
            $ letterT2in2 = False
            $ letterT2in3 = False
            $ letterT2in4 = False
            $ letterT2in5 = False
            $ letterT2in6 = False
            $ letterT2in7 = False
            $ letterT2in8 = False
            $ letterT2in9 = False
            $ letterT2in10 = True    
    
    if gate_name == "letterT3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterT3x = 1085
            $ letterT3y = 340
            $ letterT3in1 = True
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterT3x = 1465
            $ letterT3y = 340
            $ letterT3in1 = False
            $ letterT3in2 = True
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterT3x = 925
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = True
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterT3x = 1245
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = True
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterT3x = 1465
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = True
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterT3x = 1035
            $ letterT3y = 690
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = True
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterT3x = 1170
            $ letterT3y = 690
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = True
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterT3x = 1325
            $ letterT3y = 690
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = True
            $ letterT3in9 = False
            $ letterT3in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterT3x = 1465
            $ letterT3y = 690
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = True
            $ letterT3in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterT3x = 1595
            $ letterT3y = 690
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
            $ letterT3in8 = False
            $ letterT3in9 = False
            $ letterT3in10 = True       
                
    if gate_name == "letterQ1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterQ4x = 1085
            $ letterQ4y = 340
            $ letterQ4in1 = True
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterQ4x = 1465
            $ letterQ4y = 340
            $ letterQ4in1 = False
            $ letterQ4in2 = True
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterQ4x = 925
            $ letterQ4y = 515
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = True
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterQ4x = 1245
            $ letterQ4y = 515
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = True
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterQ4x = 1465
            $ letterQ4y = 515
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = True
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterQ4x = 1035
            $ letterQ4y = 690
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = True
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterQ4x = 1170
            $ letterQ4y = 690
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = True
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterQ4x = 1325
            $ letterQ4y = 690
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = True
            $ letterQ4in9 = False
            $ letterQ4in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterQ4x = 1465
            $ letterQ4y = 690
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = True
            $ letterQ4in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS9y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterQ4x = 1595
            $ letterQ4y = 690
            $ letterQ4in1 = False
            $ letterQ4in2 = False
            $ letterQ4in3 = False
            $ letterQ4in4 = False
            $ letterQ4in5 = False
            $ letterQ4in6 = False
            $ letterQ4in7 = False
            $ letterQ4in8 = False
            $ letterQ4in9 = False
            $ letterQ4in10 = True


    if gate_name == "letterQ2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterQ5x = 1085
            $ letterQ5y = 340
            $ letterQ5in1 = True
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterQ5x = 1465
            $ letterQ5y = 340
            $ letterQ5in1 = False
            $ letterQ5in2 = True
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterQ5x = 925
            $ letterQ5y = 515
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = True
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterQ5x = 1245
            $ letterQ5y = 515
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = True
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterQ5x = 1465
            $ letterQ5y = 515
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = True
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterQ5x = 1035
            $ letterQ5y = 690
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = True
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterQ5x = 1170
            $ letterQ5y = 690
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = True
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterQ5x = 1325
            $ letterQ5y = 690
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = True
            $ letterQ5in9 = False
            $ letterQ5in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterQ5x = 1465
            $ letterQ5y = 690
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = True
            $ letterQ5in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterQ5x = 1595
            $ letterQ5y = 690
            $ letterQ5in1 = False
            $ letterQ5in2 = False
            $ letterQ5in3 = False
            $ letterQ5in4 = False
            $ letterQ5in5 = False
            $ letterQ5in6 = False
            $ letterQ5in7 = False
            $ letterQ5in8 = False
            $ letterQ5in9 = False
            $ letterQ5in10 = True

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterK6x = 1085
            $ letterK6y = 340
            $ letterK6in1 = True
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterK6x = 1465
            $ letterK6y = 340
            $ letterK6in1 = False
            $ letterK6in2 = True
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterK6x = 925
            $ letterK6y = 515
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = True
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterK6x = 1245
            $ letterK6y = 515
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = True
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterK6x = 1465
            $ letterK6y = 515
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = True
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterK6x = 1035
            $ letterK6y = 690
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = True
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterK6x = 1170
            $ letterK6y = 690
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = True
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterK6x = 1325
            $ letterK6y = 690
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = True
            $ letterK6in9 = False
            $ letterK6in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterK6x = 1465
            $ letterK6y = 690
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = True
            $ letterK6in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterK6x = 1595
            $ letterK6y = 690
            $ letterK6in1 = False
            $ letterK6in2 = False
            $ letterK6in3 = False
            $ letterK6in4 = False
            $ letterK6in5 = False
            $ letterK6in6 = False
            $ letterK6in7 = False
            $ letterK6in8 = False
            $ letterK6in9 = False
            $ letterK6in10 = True


    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterJ7x = 1085
            $ letterJ7y = 340
            $ letterJ7in1 = True
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            $ letterJ7in8 = False
            $ letterJ7in9 = False
            $ letterJ7in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterJ7x = 1465
            $ letterJ7y = 340
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
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterJ7x = 925
            $ letterJ7y = 515
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
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterJ7x = 1245
            $ letterJ7y = 515
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
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterJ7x = 1465
            $ letterJ7y = 515
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
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterJ7x = 1035
            $ letterJ7y = 690
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
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterJ7x = 1170
            $ letterJ7y = 690
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
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterJ7x = 1325
            $ letterJ7y = 690
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
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterJ7x = 1465
            $ letterJ7y = 690
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
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterJ7x = 1595
            $ letterJ7y = 690
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
            
    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterM8x = 1085
            $ letterM8y = 340
            $ letterM8in1 = True
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterM8x = 1465
            $ letterM8y = 340
            $ letterM8in1 = False
            $ letterM8in2 = True
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterM8x = 925
            $ letterM8y = 515
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = True
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterM8x = 1245
            $ letterM8y = 515
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = True
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterM8x = 1465
            $ letterM8y = 515
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = True
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterM8x = 1035
            $ letterM8y = 690
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = True
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterM8x = 1170
            $ letterM8y = 690
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = True
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterM8x = 1325
            $ letterM8y = 690
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = True
            $ letterM8in9 = False
            $ letterM8in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterM8x = 1465
            $ letterM8y = 690
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = True
            $ letterM8in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterM8x = 1595
            $ letterM8y = 690
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
            $ letterM8in9 = False
            $ letterM8in10 = True
            
    if gate_name == "letterS1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterS9x = 1085
            $ letterS9y = 340
            $ letterS9in1 = True
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterS9x = 1465
            $ letterS9y = 340
            $ letterS9in1 = False
            $ letterS9in2 = True
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterS9x = 925
            $ letterS9y = 515
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = True
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterS9x = 1245
            $ letterS9y = 515
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = True
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterS9x = 1465
            $ letterS9y = 515
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = True
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterS9x = 1035
            $ letterS9y = 690
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = True
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterS9x = 1170
            $ letterS9y = 690
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = True
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterS9x = 1325
            $ letterS9y = 690
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = True
            $ letterS9in9 = False
            $ letterS9in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterS9x = 1465
            $ letterS9y = 690
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = True
            $ letterS9in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterS9x = 1595
            $ letterS9y = 690
            $ letterS9in1 = False
            $ letterS9in2 = False
            $ letterS9in3 = False
            $ letterS9in4 = False
            $ letterS9in5 = False
            $ letterS9in6 = False
            $ letterS9in7 = False
            $ letterS9in8 = False
            $ letterS9in9 = False
            $ letterS9in10 = True

    if gate_name == "letterS2":
            #call and_gate_pos_1
            #gate slot numeber one ******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h2_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterT2in1 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in1 = False
            if letterQ4in1 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in1 = False
            if letterQ5in1 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in1 = False
            if letterK6in1 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in1 = False
            if letterS9in1 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in1 = False
            if letterS10in1 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in1 = False

            #sets values for checks
            $ letterS10x = 1085
            $ letterS10y = 340
            $ letterS10in1 = True
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterT2in2 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in2 = False
            if letterQ4in2 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in2 = False
            if letterQ5in2 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in2 = False
            if letterK6in2 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in2 = False
            if letterS9in2 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in2 = False
            if letterS10in2 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in2 = False

            #sets values for checks
            $ letterS10x = 1465
            $ letterS10y = 340
            $ letterS10in1 = False
            $ letterS10in2 = True
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterT2in3 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in3 = False
            if letterQ4in3 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in3 = False
            if letterQ5in3 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in3 = False
            if letterK6in3 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in3 = False
            if letterS9in3 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in3 = False
            if letterS10in3 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in3 = False

            #sets values for checks
            $ letterS10x = 925
            $ letterS10y = 515
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = True
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterT2in4 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in4 = False
            if letterQ4in4 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in4 = False
            if letterQ5in4 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in4 = False
            if letterK6in4 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in4 = False
            if letterS9in4 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in4 = False
            if letterS10in4 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in4 = False

            #sets values for checks
            $ letterS10x = 1245
            $ letterS10y = 515
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = True
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterT2in5 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in5 = False
            if letterQ4in5 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in5 = False
            if letterQ5in5 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in5 = False
            if letterK6in5 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in5 = False
            if letterS9in5 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in5 = False
            if letterS10in5 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in5 = False

            #sets values for checks
            $ letterS10x = 1465
            $ letterS10y = 515
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = True
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False
            
                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterT2in6 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in6 = False
            if letterQ4in6 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in6 = False
            if letterQ5in6 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in6 = False
            if letterK6in6 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in6 = False
            if letterS9in6 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in6 = False
            if letterS10in6 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in6 = False

            #sets values for checks
            $ letterS10x = 1035
            $ letterS10y = 690
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = True
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterT2in7 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in7 = False
            if letterQ4in7 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in7 = False
            if letterQ5in7 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in7 = False
            if letterK6in7 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in7 = False
            if letterS9in7 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in7 = False
            if letterS10in7 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in7 = False

            #sets values for checks
            $ letterS10x = 1170
            $ letterS10y = 690
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = True
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = False
            
                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterT2in8 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in8 = False
            if letterT3in8 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in8 = False
            if letterQ4in8 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in8 = False
            if letterQ5in8 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in8 = False
            if letterK6in8 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in8 = False
            if letterJ7in8 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in8 = False
            if letterS9in8 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in8 = False
            if letterS10in8 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in8 = False

            #sets values for checks
            $ letterS10x = 1325
            $ letterS10y = 690
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = True
            $ letterS10in9 = False
            $ letterS10in10 = False
            
                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterT1in9 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in9 = False
            if letterT2in9 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in9 = False
            if letterT3in9 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in9 = False
            if letterQ4in9 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in9 = False
            if letterQ5in9 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in9 = False
            if letterK6in9 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in9 = False
            if letterJ7in9 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in9 = False
            if letterM8in9 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in9 = False
            if letterS9in9 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in9 = False
            if letterS10in9 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in9 = False

            #sets values for checks
            $ letterS10x = 1465
            $ letterS10y = 690
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = True
            $ letterS10in10 = False
            
                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterT1in10 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in10 = False
            if letterT2in10 == True:
               $ letterT2x = 275
               $ letterT2y = 575
               $ letterT2in10 = False
            if letterT3in10 == True:
               $ letterT3x = 275
               $ letterT3y = 575
               $ letterT3in10 = False
            if letterQ4in10 == True:
               $ letterQ4x = 275
               $ letterQ4y = 750
               $ letterQ4in10 = False
            if letterQ5in10 == True:
               $ letterQ5x = 275
               $ letterQ5y = 750
               $ letterQ5in10 = False
            if letterK6in10 == True:
               $ letterK6x = 410
               $ letterK6y = 575
               $ letterK6in10 = False
            if letterJ7in10 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in10 = False
            if letterM8in10 == True:
               $ letterM8x = 410
               $ letterM8y = 750
               $ letterM8in10 = False
            if letterS9in10 == True:
               $ letterS9x = 342
               $ letterS10y = 832
               $ letterS9in10 = False
            if letterS10in10 == True:
               $ letterS10x = 342
               $ letterS10y = 832
               $ letterS10in10 = False

            #sets values for checks
            $ letterS10x = 1595
            $ letterS10y = 690
            $ letterS10in1 = False
            $ letterS10in2 = False
            $ letterS10in3 = False
            $ letterS10in4 = False
            $ letterS10in5 = False
            $ letterS10in6 = False
            $ letterS10in7 = False
            $ letterS10in8 = False
            $ letterS10in9 = False
            $ letterS10in10 = True

    #Dragbacks
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "LetterT_return" or slot_name == "LetterK_return" or slot_name == "LetterM_return" or slot_name == "LetterJ_return" or slot_name == "LetterS_return" or slot_name == "LetterQ_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
            
      
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            
            if slot_name == "LetterT_return":
                $ attempts +=1
                if gate_name == "letterT1":
                    $ letterT1x = 275
                    $ letterT1y = 575
                    $ letterT1in1 = False
                    $ letterT1in2 = False
                    $ letterT1in3 = False
                    $ letterT1in4 = False
                    $ letterT1in5 = False
                    $ letterT1in6 = False
                    $ letterT1in7 = False
                    $ letterT1in8 = False
                    $ letterT1in9 = False
                    $ letterT1in10 = False
                if gate_name == "letterT2":
                    $ letterT2x = 275
                    $ letterT2y = 575
                    $ letterT2in1 = False
                    $ letterT2in2 = False
                    $ letterT2in3 = False
                    $ letterT2in4 = False
                    $ letterT2in5 = False
                    $ letterT2in6 = False
                    $ letterT2in7 = False
                    $ letterT2in8 = False
                    $ letterT2in9 = False
                    $ letterT2in10 = False
                if gate_name == "letterT3":
                    $ letterT3x = 275
                    $ letterT3y = 575
                    $ letterT3in1 = False
                    $ letterT3in2 = False
                    $ letterT3in3 = False
                    $ letterT3in4 = False
                    $ letterT3in5 = False
                    $ letterT3in6 = False
                    $ letterT3in7 = False
                    $ letterT3in8 = False
                    $ letterT3in9 = False
                    $ letterT3in10 = False
                
            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ letterK6x = 410
                    $ letterK6y = 575
                    $ letterK6in1 = False
                    $ letterK6in2 = False
                    $ letterK6in3 = False
                    $ letterK6in4 = False
                    $ letterK6in5 = False
                    $ letterK6in6 = False
                    $ letterK6in7 = False
                    $ letterK6in8 = False
                    $ letterK6in9 = False
                    $ letterK6in10 = False
            
            if slot_name == "LetterQ_return":
                $ attempts +=1
                if gate_name == "letterQ1":
                    $ letterQ4x = 275
                    $ letterQ4y = 750
                    $ letterQ4in1 = False
                    $ letterQ4in2 = False
                    $ letterQ4in3 = False
                    $ letterQ4in4 = False
                    $ letterQ4in5 = False
                    $ letterQ4in6 = False
                    $ letterQ4in7 = False
                    $ letterQ4in8 = False
                    $ letterQ4in9 = False
                    $ letterQ4in10 = False
                    
                if gate_name == "letterQ2":
                    $ letterQ5x = 275
                    $ letterQ5y = 750
                    $ letterQ5in1 = False
                    $ letterQ5in2 = False
                    $ letterQ5in3 = False
                    $ letterQ5in4 = False
                    $ letterQ5in5 = False
                    $ letterQ5in6 = False
                    $ letterQ5in7 = False
                    $ letterQ5in8 = False
                    $ letterQ5in9 = False
                    $ letterQ5in10 = False
                    
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ letterM8x = 410
                    $ letterM8y = 750
                    $ letterM8in1 = False
                    $ letterM8in2 = False
                    $ letterM8in3 = False
                    $ letterM8in4 = False
                    $ letterM8in5 = False
                    $ letterM8in6 = False
                    $ letterM8in7 = False
                    $ letterM8in8 = False
                    $ letterM8in9 = False
                    $ letterM8in10 = False
            
            if slot_name == "LetterJ_return":
                $ attempts +=1
                if gate_name == "letterJ":
                    $ letterJ7x = 342
                    $ letterJ7y = 660
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
                    
            if slot_name == "LetterS_return":
                $ attempts +=1
                if gate_name == "letterS1":
                    $ letterS9x = 342
                    $ letterS9y = 832
                    $ letterS9in1 = False
                    $ letterS9in2 = False
                    $ letterS9in3 = False
                    $ letterS9in4 = False
                    $ letterS9in5 = False
                    $ letterS9in6 = False
                    $ letterS9in7 = False
                    $ letterS9in8 = False
                    $ letterS9in9 = False
                    $ letterS9in10 = False
                if gate_name == "letterS2":
                    $ letterS10x = 342
                    $ letterS10y = 832
                    $ letterS10in1 = False
                    $ letterS10in2 = False
                    $ letterS10in3 = False
                    $ letterS10in4 = False
                    $ letterS10in5 = False
                    $ letterS10in6 = False
                    $ letterS10in7 = False
                    $ letterS10in8 = False
                    $ letterS10in9 = False
                    $ letterS10in10 = False
                    

    if (letterT1in1 == True or letterT2in1 == True or letterT3in1 == True) and (letterT1in2 == True or letterT2in2 == True or letterT3in2 == True):
        image gram_h2_tile42 = "leftTreegreenlong.png"
        image gram_h2_tile43 = "1_1_green.png"
        show gram_h2_tile42 at Position(xpos = 1120, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_h2_tile43 at Position(xpos = 1070, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h2_tile44 = "rightTreegreenlong.png"
        image gram_h2_tile45 = "1_1_green.png"
        show gram_h2_tile44 at Position(xpos = 1330, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_h2_tile45 at Position(xpos = 1450, xanchor = 0, ypos = 325, yanchor = 0)

        if (letterQ4in3 == True or letterQ5in3 == True) and (letterQ4in4 == True or letterQ5in4 == True):
            image gram_h2_tile46 = "leftTreegreenlong.png"
            image gram_h2_tile47 = "1_1_green.png"
            show gram_h2_tile46 at Position(xpos = 950, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile47 at Position(xpos = 910, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h2_tile48 = "rightTreegreenlong.png"
            image gram_h2_tile49 = "1_1_green.png"
            show gram_h2_tile48 at Position(xpos = 1140, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile49 at Position(xpos = 1230, xanchor = 0, ypos = 500, yanchor = 0)           
            image gram_h2_tile500 = "solutionLine.png"
            image gram_h2_tile501 = "solutionLine.png"
            image gram_h2_tile502 = "ai.png"
            show gram_h2_tile500 at Position(xpos = 910, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_h2_tile501 at Position(xpos = 910, xanchor = 0, ypos = 692, yanchor = 0)
            show gram_h2_tile502 at Position(xpos = 835, xanchor = 0, ypos = 790, yanchor = 0)
            
            if (letterS9in6 == True or letterS10in6 == True):
                image gram_h2_tile503 = "rightTreegreen.png"
                image gram_h2_tile504 = "1_1_green.png"
                image gram_h2_tile505 = "solutionLine.png"
                image gram_h2_tile506 = "epsilon.png"
                show gram_h2_tile503 at Position(xpos = 990, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile504 at Position(xpos = 1020, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile505 at Position(xpos = 1020, xanchor = 0, ypos = 775, yanchor = 0)
                show gram_h2_tile506 at Position(xpos = 990, xanchor = 0, ypos = 790, yanchor = 0)
            
            if (letterS9in6 == False and letterS10in6 == False):
                hide gram_h2_tile503
                hide gram_h2_tile504
                hide gram_h2_tile505
                hide gram_h2_tile506
            
            if (letterT1in6 == True or letterT2in6 == True or letterT3in6 == True or letterQ4in6 == True or letterQ5in6 == True or letterJ7in6 == True or letterM8in6 == True):
                image gram_h2_tile507 = "rightTreered.png"
                image gram_h2_tile508 = "1_1_Red.png"
                show gram_h2_tile507 at Position(xpos = 990, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile508 at Position(xpos = 1020, xanchor = 0, ypos = 675, yanchor = 0)
            
            if (letterT1in6 == False and letterT2in6 == False and letterT3in6 == False and letterQ4in6 == False and letterQ5in6 == False and letterJ7in6 == False and letterM8in6 == False):
                hide gram_h2_tile507
                hide gram_h2_tile508
            
            if ((letterK6in7 == True) and (letterS9in8 == True or letterS10in8 == True)):
                image gram_h2_tile509 = "leftTreegreen.png"
                image gram_h2_tile510 = "1_1_green.png"
                image gram_h2_tile511 = "rightTreegreen.png"
                image gram_h2_tile512 = "1_1_green.png"
                image gram_h2_tile513 = "solutionLine.png"
                image gram_h2_tile514 = "are.png"
                image gram_h2_tile515 = "solutionLine.png"
                image gram_h2_tile516 = "epsilon.png"
                
                show gram_h2_tile509 at Position(xpos = 1195, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile510 at Position(xpos = 1155, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile511 at Position(xpos = 1295, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile512 at Position(xpos = 1310, xanchor = 0, ypos = 675, yanchor = 0)
                
                show gram_h2_tile513 at Position(xpos = 1155, xanchor = 0, ypos = 775, yanchor = 0)
                show gram_h2_tile514 at Position(xpos = 1145, xanchor = 0, ypos = 790, yanchor = 0)
                show gram_h2_tile515 at Position(xpos = 1310, xanchor = 0, ypos = 775, yanchor = 0)
                show gram_h2_tile516 at Position(xpos = 1300, xanchor = 0, ypos = 790, yanchor = 0)
            
            if ((letterK6in7 == False) or (letterS9in8 == False and letterS10in8 == False)):
                hide gram_h2_tile509
                hide gram_h2_tile510
                hide gram_h2_tile511
                hide gram_h2_tile512
                hide gram_h2_tile513
                hide gram_h2_tile514
                hide gram_h2_tile515
                hide gram_h2_tile516
            
        
            if ((letterT1in7 == True or letterT2in7 == True or letterT3in7 == True or letterQ4in7 == True or letterQ5in7 == True or letterJ7in7 == True or letterM8in7 == True or letterS9in7 == True or letterS10in7 == True) and (letterT1in8 == True or letterT2in8 == True or letterT3in8 == True or letterQ4in8 == True or letterQ5in8 == True or letterK6in8 == True or letterJ7in8 == True or letterM8in8 == True)):
                image gram_h2_tile517 = "leftTreered.png"
                image gram_h2_tile518 = "1_1_red.png"
                image gram_h2_tile519 = "rightTreered.png"
                image gram_h2_tile520 = "1_1_red.png"
                
                show gram_h2_tile517 at Position(xpos = 1195, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile518 at Position(xpos = 1155, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile519 at Position(xpos = 1295, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile520 at Position(xpos = 1310, xanchor = 0, ypos = 675, yanchor = 0)
                
            if ((letterT1in7 == False and letterT2in7 == False and letterT3in7 == False and letterQ4in7 == False and letterQ5in7 == False and letterJ7in7 == False and letterM8in7 == False and letterS9in7 == False and letterS10in7 == False) or (letterT1in8 == False and letterT2in8 == False and letterT3in8 == False and letterQ4in8 == False and letterQ5in8 == False and letterK6in8 == False and letterJ7in8 == False and letterM8in8 == False)):
                hide gram_h2_tile517
                hide gram_h2_tile518
                hide gram_h2_tile519
                hide gram_h2_tile520
                
            if ((letterK6in7 == True) and (letterT1in8 == True or letterT2in8 == True or letterT3in8 == True or letterQ4in8 == True or letterQ5in8 == True or letterK6in8 == True or letterJ7in8 == True or letterM8in8 == True)):
                image gram_h2_tile525 = "leftTreered.png"
                image gram_h2_tile526 = "1_1_red.png"
                image gram_h2_tile527 = "rightTreered.png"
                image gram_h2_tile528 = "1_1_red.png"
                
                show gram_h2_tile525 at Position(xpos = 1195, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile526 at Position(xpos = 1155, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile527 at Position(xpos = 1295, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile528 at Position(xpos = 1310, xanchor = 0, ypos = 675, yanchor = 0)
                
            if ((letterK6in7 == False) or (letterT1in8 == False and letterT2in8 == False and letterT3in8 == False and letterQ4in8 == False and letterQ5in8 == False and letterK6in8 == False and letterJ7in8 == False and letterM8in8 == False)):
                hide gram_h2_tile525
                hide gram_h2_tile526
                hide gram_h2_tile527
                hide gram_h2_tile528
            
            if ((letterT1in7 == True or letterT2in7 == True or letterT3in7 == True or letterQ4in7 == True or letterQ5in7 == True or letterJ7in7 == True or letterM8in7 == True or letterS9in7 == True or letterS10in7 == True) and (letterS9in8 == True or letterS10in8 == True)):
                image gram_h2_tile529 = "leftTreered.png"
                image gram_h2_tile530 = "1_1_red.png"
                image gram_h2_tile531 = "rightTreered.png"
                image gram_h2_tile532 = "1_1_red.png"
                
                show gram_h2_tile529 at Position(xpos = 1195, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile530 at Position(xpos = 1155, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile531 at Position(xpos = 1295, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile532 at Position(xpos = 1310, xanchor = 0, ypos = 675, yanchor = 0)
                
            if ((letterT1in7 == False and letterT2in7 == False and letterT3in7 == False and letterQ4in7 == False and letterQ5in7 == False and letterJ7in7 == False and letterM8in7 == False and letterS9in7 == False and letterS10in7 == False) or (letterS9in8 == True and letterS10in8 == True)):
                hide gram_h2_tile529
                hide gram_h2_tile530
                hide gram_h2_tile531
                hide gram_h2_tile532
                
        if (letterQ4in3 == False and letterQ5in3 == False) or (letterQ4in4 == False and letterQ5in4 == False):
            hide gram_h2_tile46
            hide gram_h2_tile47
            hide gram_h2_tile48
            hide gram_h2_tile49
            hide gram_h2_tile500
            hide gram_h2_tile501
            hide gram_h2_tile502
            hide gram_h2_tile509
            hide gram_h2_tile510
            hide gram_h2_tile511
            hide gram_h2_tile512
            hide gram_h2_tile513
            hide gram_h2_tile514
            hide gram_h2_tile515
            hide gram_h2_tile516
            hide gram_h2_tile517
            hide gram_h2_tile518
            hide gram_h2_tile519
            hide gram_h2_tile520
            hide gram_h2_tile521
            hide gram_h2_tile522
            hide gram_h2_tile523
            hide gram_h2_tile524
            hide gram_h2_tile525
            hide gram_h2_tile526
            hide gram_h2_tile527
            hide gram_h2_tile528
            hide gram_h2_tile529
            hide gram_h2_tile530
            hide gram_h2_tile531
            hide gram_h2_tile532
            

        if (letterT1in3 == True or letterT2in3 == True or letterT3in3 == True or letterK6in3 == True or letterJ7in3 == True or letterM8in3 == True or letterS9in3 == True or letterS10in3 == True) and (letterT1in4 == True or letterT2in4 == True or letterT3in4 == True or letterK6in4 == True or letterJ7in4 == True or letterM8in4 == True or letterS9in4 == True or letterS10in4 == True):
            image gram_h2_tile78 = "leftTreeredlong.png"
            image gram_h2_tile79 = "1_1_Red.png"
            image gram_h2_tile50 = "rightTreeredlong.png"
            image gram_h2_tile51 = "1_1_Red.png"
            
            show gram_h2_tile78 at Position(xpos = 950, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile79 at Position(xpos = 910, xanchor = 0, ypos = 500, yanchor = 0)
            show gram_h2_tile50 at Position(xpos = 1140, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile51 at Position(xpos = 1230, xanchor = 0, ypos = 500, yanchor = 0)
        
        if (letterT1in3 == False and letterT2in3 == False and letterT3in3 == False and letterK6in3 == False and letterJ7in3 == False and letterM8in3 == False and letterS9in3 == False and letterS10in3 == False) and (letterT1in4 == False or letterT2in4 == False or letterT3in4 == False or letterK6in4 == False or letterJ7in4 == False or letterM8in4 == False or letterS9in4 == False or letterS10in4 == False):
            hide gram_h2_tile78
            hide gram_h2_tile79
            hide gram_h2_tile50
            hide gram_h2_tile51
        
        if (letterQ4in3 == True or letterQ5in3 == True) and (letterT1in4 == True or letterT2in4 == True or letterT3in4 == True or letterK6in4 == True or letterJ7in4 == True or letterM8in4 == True or letterS9in4 == True or letterS10in4 == True):
            image gram_h2_tile578 = "leftTreeredlong.png"
            image gram_h2_tile579 = "1_1_Red.png"
            image gram_h2_tile580 = "rightTreeredlong.png"
            image gram_h2_tile581 = "1_1_Red.png"
            
            show gram_h2_tile578 at Position(xpos = 950, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile579 at Position(xpos = 910, xanchor = 0, ypos = 500, yanchor = 0)
            show gram_h2_tile580 at Position(xpos = 1140, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile581 at Position(xpos = 1230, xanchor = 0, ypos = 500, yanchor = 0)
        
        if (letterQ4in3 == False and letterQ5in3 == False) or (letterT1in4 == False or letterT2in4 == False or letterT3in4 == False or letterK6in4 == False or letterJ7in4 == False or letterM8in4 == False or letterS9in4 == False or letterS10in4 == False):
            hide gram_h2_tile578
            hide gram_h2_tile579
            hide gram_h2_tile580
            hide gram_h2_tile581
        
        if (letterT1in3 == True or letterT2in3 == True or letterT3in3 == True or letterK6in3 == True or letterJ7in3 == True or letterM8in3 == True or letterS9in3 == True or letterS10in3 == True) and (letterQ4in4 == True or letterQ5in4 == True):
            image gram_h2_tile582 = "leftTreeredlong.png"
            image gram_h2_tile583 = "1_1_Red.png"
            image gram_h2_tile584 = "rightTreeredlong.png"
            image gram_h2_tile585 = "1_1_Red.png"
            
            show gram_h2_tile582 at Position(xpos = 950, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile583 at Position(xpos = 910, xanchor = 0, ypos = 500, yanchor = 0)
            show gram_h2_tile584 at Position(xpos = 1140, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile585 at Position(xpos = 1230, xanchor = 0, ypos = 500, yanchor = 0)
        
        if (letterT1in3 == False and letterT2in3 == False and letterT3in3 == False and letterK6in3 == False and letterJ7in3 == False and letterM8in3 == False and letterS9in3 == False and letterS10in3 == False) or (letterQ4in4 == False and letterQ5in4 == False):
            hide gram_h2_tile582
            hide gram_h2_tile583
            hide gram_h2_tile584
            hide gram_h2_tile585
        
        if (letterT1in5 == True or letterT2in5 == True or letterT3in5 == True):
            image gram_h2_tile52 = "treeGreen.png"
            image gram_h2_tile53 = "1_1_green.png"
            show gram_h2_tile52 at Position(xpos = 1450, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile53 at Position(xpos = 1450, xanchor = 0, ypos = 500, yanchor = 0)

            if (letterJ7in9 == True and letterM8in10 == True):
                image gram_h2_tile66 = "treeGreen.png"
                image gram_h2_tile67 = "1_1_green.png"
                show gram_h2_tile66 at Position(xpos = 1450, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile67 at Position(xpos = 1450, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h2_tile68 = "rightTreegreen.png"
                image gram_h2_tile69 = "1_1_green.png"
                show gram_h2_tile68 at Position(xpos = 1530, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile69 at Position(xpos = 1580, xanchor = 0, ypos = 675, yanchor = 0)
                   
                image gram_h2_tile54 = "solutionLine.png"
                image gram_h2_tile55 = "superior.png"
                image gram_h2_tile56 = "solutionLine.png"
                image gram_h2_tile57 = "beings.png"
                   
                show gram_h2_tile54 at Position(xpos = 1450, xanchor = 0, ypos = 775, yanchor = 0)
                show gram_h2_tile55 at Position(xpos = 1455, xanchor = 0, ypos = 790, yanchor = 0)
                show gram_h2_tile56 at Position(xpos = 1580, xanchor = 0, ypos = 775, yanchor = 0)
                show gram_h2_tile57 at Position(xpos = 1610, xanchor = 0, ypos = 790, yanchor = 0)
                
            if (letterJ7in9 == False or letterM8in10 == False):
                hide gram_h2_tile66
                hide gram_h2_tile67
                hide gram_h2_tile68
                hide gram_h2_tile69
                hide gram_h2_tile54
                hide gram_h2_tile55
                hide gram_h2_tile56
                hide gram_h2_tile57

            if ((letterT1in9 == True or letterT2in9 == True or letterT3in9 == True or letterQ4in9 == True or letterQ5in9 == True or letterK6in9 == True or letterM8in9 == True or letterS9in9 == True or letterS10in9 == True) and (letterT1in10 == True or letterT2in10 == True or letterT3in10 == True or letterQ4in10 == True or letterQ5in10 == True or letterK6in10 == True or letterJ7in10 == True or letterS9in10 == True or letterS10in10 == True)):
                image gram_h2_tile70 = "treeRed.png"
                image gram_h2_tile71 = "1_1_Red.png"
                image gram_h2_tile170 = "rightTreered.png"
                image gram_h2_tile171 = "1_1_Red.png"
                show gram_h2_tile70 at Position(xpos = 1450, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile71 at Position(xpos = 1450, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile170 at Position(xpos = 1530, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile171 at Position(xpos = 1580, xanchor = 0, ypos = 675, yanchor = 0)

            if ((letterT1in9 == False and letterT2in9 == False and letterT3in9 == False and letterQ4in9 == False and letterQ5in9 == False and letterK6in9 == False and letterM8in9 == False and letterS9in9 == False and letterS10in9 == False) or (letterT1in10 == False and letterT2in10 == False and letterT3in10 == False and letterQ4in10 == False and letterQ5in10 == False and letterK6in10 == False and letterJ7in10 == False and letterS9in10 == False and letterS10in10 == False)):
                hide gram_h2_tile70
                hide gram_h2_tile71
                hide gram_h2_tile170
                hide gram_h2_tile171
                
            if ((letterJ7in9 == True) and (letterT1in10 == True or letterT2in10 == True or letterT3in10 == True or letterQ4in10 == True or letterQ5in10 == True or letterK6in10 == True or letterJ7in10 == True or letterS9in10 == True or letterS10in10 == True)):
                image gram_h2_tile552 = "treeRed.png"
                image gram_h2_tile553 = "1_1_Red.png"
                image gram_h2_tile554 = "rightTreered.png"
                image gram_h2_tile555 = "1_1_Red.png"
                show gram_h2_tile552 at Position(xpos = 1450, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile553 at Position(xpos = 1450, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile554 at Position(xpos = 1530, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile555 at Position(xpos = 1580, xanchor = 0, ypos = 675, yanchor = 0)

            if ((letterJ7in9 == False) or (letterT1in10 == False and letterT2in10 == False and letterT3in10 == False and letterQ4in10 == False and letterQ5in10 == False and letterK6in10 == False and letterJ7in10 == False and letterS9in10 == False and letterS10in10 == False)):
                hide gram_h2_tile552
                hide gram_h2_tile553
                hide gram_h2_tile554
                hide gram_h2_tile555
            
            if ((letterT1in9 == True or letterT2in9 == True or letterT3in9 == True or letterQ4in9 == True or letterQ5in9 == True or letterK6in9 == True or letterM8in9 == True or letterS9in9 == True or letterS10in9 == True) and (letterM8in10 == True)):
                image gram_h2_tile556 = "treeRed.png"
                image gram_h2_tile557 = "1_1_Red.png"
                image gram_h2_tile558 = "rightTreered.png"
                image gram_h2_tile559 = "1_1_Red.png"
                show gram_h2_tile556 at Position(xpos = 1450, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile557 at Position(xpos = 1450, xanchor = 0, ypos = 675, yanchor = 0)
                show gram_h2_tile558 at Position(xpos = 1530, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h2_tile559 at Position(xpos = 1580, xanchor = 0, ypos = 675, yanchor = 0)

            if ((letterT1in9 == False and letterT2in9 == False and letterT3in9 == False and letterQ4in9 == False and letterQ5in9 == False and letterK6in9 == False and letterM8in9 == False and letterS9in9 == False and letterS10in9 == False) or (letterM8in10 == False)):
                hide gram_h2_tile556
                hide gram_h2_tile557
                hide gram_h2_tile558
                hide gram_h2_tile559
                
        if (letterT1in5 == False and letterT2in5 == False and letterT3in5 == False):
            hide gram_h2_tile52
            hide gram_h2_tile53
            hide gram_h2_tile66
            hide gram_h2_tile67
            hide gram_h2_tile68
            hide gram_h2_tile69
            hide gram_h2_tile54
            hide gram_h2_tile55
            hide gram_h2_tile56
            hide gram_h2_tile57
            hide gram_h2_tile70
            hide gram_h2_tile71
            hide gram_h2_tile170
            hide gram_h2_tile171
            hide gram_h2_tile552
            hide gram_h2_tile553
            hide gram_h2_tile554
            hide gram_h2_tile555
            hide gram_h2_tile556
            hide gram_h2_tile557
            hide gram_h2_tile558
            hide gram_h2_tile559
        
        if (letterQ4in5 == True or letterQ5in5 == True or letterK6in5 == True or letterJ7in5 == True or letterM8in5 == True or letterS9in5 == True or letterS10in5 == True):
            image gram_h2_tile550 = "treeRed.png"
            image gram_h2_tile551 = "1_1_Red.png"
            show gram_h2_tile550 at Position(xpos = 1450, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h2_tile551 at Position(xpos = 1450, xanchor = 0, ypos = 500, yanchor = 0)
        
        if (letterQ4in5 == False and letterQ5in5 == False and letterK6in5 == False and letterJ7in5 == False and letterM8in5 == False and letterS9in5 == False and letterS10in5 == False):
            hide gram_h2_tile550
            hide gram_h2_tile551
        

    elif (letterT1in1 == False and letterT2in1 == False and letterT3in1 == False) or (letterT1in2 == False and letterT2in2 == False and letterT3in2 == False):

            hide gram_h2_tile42
            hide gram_h2_tile43
            hide gram_h2_tile44
            hide gram_h2_tile45
            hide gram_h2_tile46
            hide gram_h2_tile47
            hide gram_h2_tile48
            hide gram_h2_tile49
            hide gram_h2_tile52
            hide gram_h2_tile53
            hide gram_h2_tile54
            hide gram_h2_tile55
            hide gram_h2_tile50
            hide gram_h2_tile51
            hide gram_h2_tile56
            hide gram_h2_tile57
            hide gram_h2_tile58
            hide gram_h2_tile59
            hide gram_h2_tile60
            hide gram_h2_tile61
            hide gram_h2_tile62
            hide gram_h2_tile63
            hide gram_h2_tile64
            hide gram_h2_tile65
            hide gram_h2_tile66
            hide gram_h2_tile67
            hide gram_h2_tile68
            hide gram_h2_tile69
            hide gram_h2_tile70
            hide gram_h2_tile71
            hide gram_h2_tile75
            hide gram_h2_tile78
            hide gram_h2_tile79
            hide gram_h2_tile170
            hide gram_h2_tile171
            hide gram_h2_tile500
            hide gram_h2_tile501
            hide gram_h2_tile502
            hide gram_h2_tile503
            hide gram_h2_tile504
            hide gram_h2_tile505
            hide gram_h2_tile506
            hide gram_h2_tile507
            hide gram_h2_tile508
            hide gram_h2_tile509
            hide gram_h2_tile510
            hide gram_h2_tile511
            hide gram_h2_tile512
            hide gram_h2_tile513
            hide gram_h2_tile514
            hide gram_h2_tile515
            hide gram_h2_tile516
            hide gram_h2_tile517
            hide gram_h2_tile518
            hide gram_h2_tile519
            hide gram_h2_tile520
            hide gram_h2_tile521
            hide gram_h2_tile522
            hide gram_h2_tile523
            hide gram_h2_tile524
            hide gram_h2_tile525
            hide gram_h2_tile526
            hide gram_h2_tile527
            hide gram_h2_tile528
            hide gram_h2_tile529
            hide gram_h2_tile530
            hide gram_h2_tile531
            hide gram_h2_tile532
            hide gram_h2_tile550
            hide gram_h2_tile551
            hide gram_h2_tile552
            hide gram_h2_tile553
            hide gram_h2_tile554
            hide gram_h2_tile555
            hide gram_h2_tile556
            hide gram_h2_tile557
            hide gram_h2_tile558
            hide gram_h2_tile559
            hide gram_h2_tile578
            hide gram_h2_tile579
            hide gram_h2_tile580
            hide gram_h2_tile581
            
    if ((letterQ4in1 == True or letterQ5in1 == True or letterK6in1 == True or letterJ7in1 == True or letterM8in1 == True or letterS9in1 == True or letterS10in1 == True) and (letterQ4in2 == True or letterQ5in2 == True or letterK6in2 == True or letterJ7in2 == True or letterM8in2 == True or letterS9in2 == True or letterS10in2 == True)):
            image gram_h2_tile521 = "leftTreeredlong.png"
            image gram_h2_tile522 = "1_1_red.png"
            image gram_h2_tile523 = "rightTreeredlong.png"
            image gram_h2_tile524 = "1_1_red.png"
            
            show gram_h2_tile521 at Position(xpos = 1120, xanchor = 0, ypos = 250, yanchor = 0)
            show gram_h2_tile522 at Position(xpos = 1070, xanchor = 0, ypos = 325, yanchor = 0)
            show gram_h2_tile523 at Position(xpos = 1330, xanchor = 0, ypos = 250, yanchor = 0)
            show gram_h2_tile524 at Position(xpos = 1450, xanchor = 0, ypos = 325, yanchor = 0)

    if ((letterQ4in1 == False and letterQ5in1 == False and letterK6in1 == False and letterJ7in1 == False and letterM8in1 == False and letterS9in1 == False and letterS10in1 == False) or (letterQ4in2 == False and letterQ5in2 == False and letterK6in2 == False and letterJ7in2 == False and letterM8in2 == False and letterS9in2 == False and letterS10in2 == False)):
            hide gram_h2_tile521
            hide gram_h2_tile522
            hide gram_h2_tile523
            hide gram_h2_tile524
     
    if ((letterT1in1 == True or letterT2in1 == True or letterT3in1 == True) and (letterQ4in2 == True or letterQ5in2 == True or letterK6in2 == True or letterJ7in2 == True or letterM8in2 == True or letterS9in2 == True or letterS10in2 == True)):
            image gram_h2_tile525 = "leftTreeredlong.png"
            image gram_h2_tile526 = "1_1_red.png"
            image gram_h2_tile527 = "rightTreeredlong.png"
            image gram_h2_tile528 = "1_1_red.png"
            
            show gram_h2_tile525 at Position(xpos = 1120, xanchor = 0, ypos = 250, yanchor = 0)
            show gram_h2_tile526 at Position(xpos = 1070, xanchor = 0, ypos = 325, yanchor = 0)
            show gram_h2_tile527 at Position(xpos = 1330, xanchor = 0, ypos = 250, yanchor = 0)
            show gram_h2_tile528 at Position(xpos = 1450, xanchor = 0, ypos = 325, yanchor = 0)

    if ((letterT1in1 == False and letterT2in1 == False and letterT3in1 == False) or (letterQ4in2 == False and letterQ5in2 == False and letterK6in2 == False and letterJ7in2 == False and letterM8in2 == False and letterS9in2 == False and letterS10in2 == False)):
            hide gram_h2_tile525
            hide gram_h2_tile526
            hide gram_h2_tile527
            hide gram_h2_tile528
            
    if ((letterQ4in1 == True or letterQ5in1 == True or letterK6in1 == True or letterJ7in1 == True or letterM8in1 == True or letterS9in1 == True or letterS10in1 == True) and (letterT1in2 == True or letterT2in2 == True or letterT3in2 == True)):
            image gram_h2_tile529 = "leftTreeredlong.png"
            image gram_h2_tile530 = "1_1_red.png"
            image gram_h2_tile531 = "rightTreeredlong.png"
            image gram_h2_tile532 = "1_1_red.png"
            
            show gram_h2_tile529 at Position(xpos = 1120, xanchor = 0, ypos = 250, yanchor = 0)
            show gram_h2_tile530 at Position(xpos = 1070, xanchor = 0, ypos = 325, yanchor = 0)
            show gram_h2_tile531 at Position(xpos = 1330, xanchor = 0, ypos = 250, yanchor = 0)
            show gram_h2_tile532 at Position(xpos = 1450, xanchor = 0, ypos = 325, yanchor = 0)

    if ((letterQ4in1 == False and letterQ5in1 == False and letterK6in1 == False and letterJ7in1 == False and letterM8in1 == False and letterS9in1 == False and letterS10in1 == False) or (letterT1in2 == True and letterT2in2 == True and letterT3in2 == True)):
            hide gram_h2_tile529
            hide gram_h2_tile530
            hide gram_h2_tile531
            hide gram_h2_tile532
            
            
    #win conditions
    if ((letterT1in1 == True or letterT2in1 == True or letterT3in1 == True) and (letterT1in2 == True or letterT2in2 == True or letterT3in2 == True) and (letterQ4in3 == True or letterQ5in3 == True) and (letterQ4in4 == True or letterQ5in4 == True) and (letterT1in5 == True or letterT2in5 == True or letterT3in5 == True) and (letterS9in6 == True or letterS10in6 == True) and (letterK6in7 == True) and (letterS9in8 == True or letterS10in8 == True) and (letterJ7in9 == True) and (letterM8in10 == True)):

        image gram_h2_tile202 = "letterT.png"
        image gram_h2_tile206 = "letterT.png"
        image gram_h2_tile203 = "letterT.png"
        image gram_h2_tile205 = "letterQ.png"
        image gram_h2_tile201 = "letterQ.png"
        image gram_h2_tile204 = "letterK.png"
        image gram_h2_tile208 = "letterJ.png"
        image gram_h2_tile209 = "letterM.png"
        image gram_h2_tile210 = "letterS.png"
        image gram_h2_tile211 = "letterS.png"
        
        show gram_h2_tile202 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_h2_tile206 at Position(xpos = letterT2x, xanchor = 0, ypos = letterT2y, yanchor = 0)
        show gram_h2_tile203 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
        show gram_h2_tile205 at Position(xpos = letterQ4x, xanchor = 0, ypos = letterQ4y, yanchor = 0)
        show gram_h2_tile201 at Position(xpos = letterQ5x, xanchor = 0, ypos = letterQ5y, yanchor = 0)
        show gram_h2_tile204 at Position(xpos = letterK6x, xanchor = 0, ypos = letterK6y, yanchor = 0)
        show gram_h2_tile208 at Position(xpos = letterJ7x, xanchor = 0, ypos = letterJ7y, yanchor = 0)
        show gram_h2_tile209 at Position(xpos = letterM8x, xanchor = 0, ypos = letterM8y, yanchor = 0)
        show gram_h2_tile210 at Position(xpos = letterS9x, xanchor = 0, ypos = letterS9y, yanchor = 0)
        show gram_h2_tile211 at Position(xpos = letterS10x, xanchor = 0, ypos = letterS10y, yanchor = 0)


        "Access Gained"

        jump eng_gram_h2#gram_m5#start

    if attempts ==0:

        show gram_h2_tile202 at Position(xpos = 1085, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_h2_tile206 at Position(xpos = 1465, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_h2_tile205 at Position(xpos = 1465, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_h2_tile201 at Position(xpos = 925, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_h2_tile203 at Position(xpos = 1245, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_h2_tile204 at Position(xpos = 1170, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_h2_tile209 at Position(xpos = 1595, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_h2_tile208 at Position(xpos = 1465, xanchor = 0, ypos = 695, yanchor = 0)
        show gram_h2_tile210 at Position(xpos = 1035, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_h2_tile211 at Position(xpos = 1325, xanchor = 0, ypos = 690, yanchor = 0)

        hide gram_h2_tile42
        hide gram_h2_tile43
        hide gram_h2_tile44
        hide gram_h2_tile45
        hide gram_h2_tile46
        hide gram_h2_tile47
        hide gram_h2_tile48
        hide gram_h2_tile49
        hide gram_h2_tile50
        hide gram_h2_tile51
        hide gram_h2_tile52
        hide gram_h2_tile53
        hide gram_h2_tile54
        hide gram_h2_tile55
        hide gram_h2_tile56
        hide gram_h2_tile57
        hide gram_h2_tile58
        hide gram_h2_tile59
        hide gram_h2_tile60
        hide gram_h2_tile61
        hide gram_h2_tile62
        hide gram_h2_tile63
        hide gram_h2_tile64
        hide gram_h2_tile65
        hide gram_h2_tile66
        hide gram_h2_tile67
        hide gram_h2_tile68
        hide gram_h2_tile69
        hide gram_h2_tile70
        hide gram_h2_tile71
        hide gram_h2_tile72
        hide gram_h2_tile73
        hide gram_h2_tile74
        hide gram_h2_tile75
        hide gram_h2_tile76
        hide gram_h2_tile77
        hide gram_h2_tile78
        hide gram_h2_tile79
        hide gram_h2_tile80
        hide gram_h2_tile81
        hide gram_h2_tile82
        hide gram_h2_tile83
        hide gram_h2_tile84
        hide gram_h2_tile85
        hide gram_h2_tile86
        hide gram_h2_tile87
        hide gram_h2_tile88
        hide gram_h2_tile89
        hide gram_h2_tile90
        hide gram_h2_tile91
        hide gram_h2_tile92
        hide gram_h2_tile93
        hide gram_h2_tile170
        hide gram_h2_tile171
        hide gram_h2_tile500
        hide gram_h2_tile501
        hide gram_h2_tile502
        hide gram_h2_tile503
        hide gram_h2_tile504
        hide gram_h2_tile505
        hide gram_h2_tile506
        hide gram_h2_tile507
        hide gram_h2_tile508
        hide gram_h2_tile509
        hide gram_h2_tile510
        hide gram_h2_tile511
        hide gram_h2_tile512
        hide gram_h2_tile513
        hide gram_h2_tile514
        hide gram_h2_tile515
        hide gram_h2_tile516
        hide gram_h2_tile517
        hide gram_h2_tile518
        hide gram_h2_tile519
        hide gram_h2_tile520
        hide gram_h2_tile521
        hide gram_h2_tile522
        hide gram_h2_tile523
        hide gram_h2_tile524
        hide gram_h2_tile525
        hide gram_h2_tile526
        hide gram_h2_tile527
        hide gram_h2_tile528
        hide gram_h2_tile529
        hide gram_h2_tile530
        hide gram_h2_tile531
        hide gram_h2_tile532
        hide gram_h2_tile550
        hide gram_h2_tile551
        hide gram_h2_tile552
        hide gram_h2_tile553
        hide gram_h2_tile554
        hide gram_h2_tile555
        hide gram_h2_tile556
        hide gram_h2_tile557
        hide gram_h2_tile558
        hide gram_h2_tile559
        hide gram_h2_tile578
        hide gram_h2_tile579
        hide gram_h2_tile580
        hide gram_h2_tile581
        hide gram_h2_tile582
        hide gram_h2_tile583
        hide gram_h2_tile584
        hide gram_h2_tile585

        "You Lose Try Again"

        jump eng_gram_h2#gram_m5#start
    

#    if and1in1 == True or letterT2in1 ==True or letterT3in1 ==True or letterA4in1 ==True:
#        image gram_h2_tile109 = "leftTreegreen.png"
#        #shows gram_h2_tiles
#        show gram_h2_tile109 at Position(xpos = 825, xanchor = 0, ypos = 225, yanchor = 0)
#    if and1in1 == False and letterT2in1 == False and letterT3in1 == False and letterA4in1 ==False:
#        hide gram_h2_tile109      

          
    jump gamefile_h2