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

screen logicGatesh4:

    draggroup:
        #and gates
        drag:
                drag_name "letterK1"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK1x ypos letterK1y
        drag:
                drag_name "letterK2"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK2X ypos letterK2y
        drag:
                drag_name "letterM1"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM3x ypos letterM3y
        drag:
                drag_name "letterA1"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA4x ypos letterA4y
        drag:
                drag_name "letterT1"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos lettertT5x ypos lettertT5y
        drag:
                drag_name "letterA2"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA6x ypos letterA6y
        drag:
                drag_name "letterH1"
                child "letterH.png"
                droppable False
                dragged gate_dragged
                xpos letterH7x ypos letterH7y

        drag:
                drag_name "letterA3"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA8x ypos letterA8y

        drag:
                drag_name "letterT2"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT9x ypos letterT9y

        drag:
                drag_name "letterA4"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA10x ypos letterA10y

        drag:
                drag_name "letterT3"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT11x ypos letterT11y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 865 ypos 340
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1265 ypos 340
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 1665 ypos 340
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 865 ypos 515
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1015 ypos 515
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1265 ypos 515
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 1515 ypos 515
        drag:
                drag_name "gate slot eight"
                draggable False
                child "images/border.png"
                xpos 1665 ypos 515
        drag:
                drag_name "gate slot nine"
                draggable False
                child "images/border.png"
                xpos 1115 ypos 690
        drag:
                drag_name "gate slot ten"
                draggable False
                child "images/border.png"
                xpos 1265 ypos 690
        drag:
                drag_name "gate slot eleven"
                draggable False
                child "images/border.png"
                xpos 1415 ypos 690
                
        #Dragbacks
        drag:
                drag_name "letterK_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562

        drag:
                drag_name "letterM_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
                
        drag:
                drag_name "letterA_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648

        drag:
                drag_name "letterT_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738

        drag:
                drag_name "letterH_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738

init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_h4:

    scene bg Eng_Tile
    $ quick_menu = False
    $ game_menu = True

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image instructions = "instructions14.png"
    image baseSlot = "1_1_green.png"
    image baseLetter = "letterS.png"
    show instructions at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show baseSlot at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show baseLetter at Position(xpos = 1265, xanchor = 0, ypos = 165, yanchor = 0)
    
    #row2 5-8

    image connector1 = "leftTreelong2.png"
    image connector2 = "treeGrey.png"
    image connector3 = "rightTreelong2.png"

    show connector1 at Position(xpos = 885, xanchor = 0, ypos = 250, yanchor = 0)
    show connector2 at Position(xpos = 1250, xanchor = 0, ypos = 250, yanchor = 0)
    show connector3 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image slot1 = "1_1_grey.png"
    image slot2 = "1_1_grey.png"
    image slot3 = "1_1_grey.png"
    

    show slot1 at Position(xpos = 850, xanchor = 0, ypos = 325, yanchor = 0)
    show slot2 at Position(xpos = 1250, xanchor = 0, ypos = 325, yanchor = 0)
    show slot3 at Position(xpos = 1650, xanchor = 0, ypos = 325, yanchor = 0)


    #row4 14-20

    image connector4 = "treeGrey.png"
    image connector5 = "leftTreelong1.png"
    image connector6 = "treeGrey.png"
    image connector7 = "rightTreelong1.png"
    image connector8 = "treeGrey.png"

    show connector4 at Position(xpos = 850, xanchor = 0, ypos = 425, yanchor = 0)
    show connector5 at Position(xpos = 1040, xanchor = 0, ypos = 425, yanchor = 0)
    show connector6 at Position(xpos = 1250, xanchor = 0, ypos = 425, yanchor = 0)
    show connector7 at Position(xpos = 1310, xanchor = 0, ypos = 425, yanchor = 0)
    show connector8 at Position(xpos = 1650, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image slot4 = "1_1_grey.png"
    image slot5 = "1_1_grey.png"
    image slot6 = "1_1_grey.png"
    image slot7 = "1_1_grey.png"
    image slot8 = "1_1_grey.png"

    show slot4 at Position(xpos = 850, xanchor = 0, ypos = 500, yanchor = 0)
    show slot5 at Position(xpos = 1000, xanchor = 0, ypos = 500, yanchor = 0)
    show slot6 at Position(xpos = 1250, xanchor = 0, ypos = 500, yanchor = 0)
    show slot7 at Position(xpos = 1500, xanchor = 0, ypos = 500, yanchor = 0)
    show slot8 at Position(xpos = 1650, xanchor = 0, ypos = 500, yanchor = 0)
    
    
    #row6 28-34

    image connector9 = "leftTreelong.png"
    image connector10 = "treeGrey.png"
    image connector11 = "rightTreelong.png"
    
    show connector9 at Position(xpos = 1140, xanchor = 0, ypos = 600, yanchor = 0)
    show connector10 at Position(xpos = 1250, xanchor = 0, ypos = 600, yanchor = 0)
    show connector11 at Position(xpos = 1310, xanchor = 0, ypos = 600, yanchor = 0)
    
    #row6 35-41

    image slot9 = "1_1_grey.png"
    image slot10 = "1_1_grey.png"
    image slot11 = "1_1_grey.png"

    show slot9 at Position(xpos = 1100, xanchor = 0, ypos = 675, yanchor = 0)
    show slot10 at Position(xpos = 1250, xanchor = 0, ypos = 675, yanchor = 0)
    show slot11 at Position(xpos = 1400, xanchor = 0, ypos = 675, yanchor = 0)

    image eaeng_m4_tile31 = "letterBorder.png"
    image eaeng_m4_tile32 = "letterBorder.png"
    image eaeng_m4_tile33 = "letterBorder.png"
    image eaeng_m4_tile34 = "letterBorder.png"
    image eaeng_m4_tile35 = "letterBorder.png"
    show eaeng_m4_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_m4_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_m4_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_m4_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_m4_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)

    image eng_gram_h4_grayK = "letterK_grey.png"
    image eng_gram_h4_grayH = "letterH_grey.png"
    image eng_gram_h4_grayM = "letterM_grey.png"
    image eng_gram_h4_grayT = "letterA_grey.png"
    image eng_gram_h4_grayA = "letterT_grey.png"
    show eng_gram_h4_grayK at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eng_gram_h4_grayH at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eng_gram_h4_grayM at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eng_gram_h4_grayT at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eng_gram_h4_grayA at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)

    
    # gates
    $ letterK1x = 275
    $ letterK1y = 575
    $ letterK2X = 275 
    $ letterK2y = 575
    $ letterM3x = 342 
    $ letterM3y = 660
    $ letterA4x = 275
    $ letterA4y = 750
    $ lettertT5x = 410
    $ lettertT5y = 750
    $ letterA6x = 275 
    $ letterA6y = 750
    $ letterH7x = 410 
    $ letterH7y = 575
    $ letterA8x = 275 
    $ letterA8y = 750
    $ letterT9x = 410 
    $ letterT9y = 750
    $ letterA10x = 275 
    $ letterA10y = 750
    $ letterT11x = 410 
    $ letterT11y = 750

    # check conditons for locations
    $ letterK1in1 = False
    $ letterK1in2 = False
    $ letterK1in3 = False
    $ letterK1in4 = False
    $ letterK1in5 = False
    $ letterK1in6 = False
    $ letterK1in7 = False
    $ letterK1in8 = False
    $ letterK1in9 = False
    $ letterK1in10 = False
    $ letterK1in11 = False

    $ letterK2in1 = False
    $ letterK2in2 = False
    $ letterK2in3 = False
    $ letterK2in4 = False
    $ letterK2in5 = False
    $ letterK2in6 = False
    $ letterK2in7 = False
    $ letterK2in8 = False
    $ letterK2in9 = False
    $ letterK2in10 = False
    $ letterK2in11 = False

    $ letterM3in1 = False
    $ letterM3in2 = False
    $ letterM3in3 = False
    $ letterM3in4 = False
    $ letterM3in5 = False
    $ letterM3in6 = False
    $ letterM3in7 = False
    $ letterM3in8 = False
    $ letterM3in9 = False
    $ letterM3in10 = False
    $ letterM3in11 = False

    $ letterA4in1 = False
    $ letterA4in2 = False
    $ letterA4in3 = False
    $ letterA4in4 = False
    $ letterA4in5 = False
    $ letterA4in6 = False
    $ letterA4in7 = False
    $ letterA4in8 = False
    $ letterA4in9 = False
    $ letterA4in10 = False
    $ letterA4in11 = False

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
    $ letterT5in11 = False

    $ letterA6in1 = False
    $ letterA6in2 = False
    $ letterA6in3 = False
    $ letterA6in4 = False
    $ letterA6in5 = False
    $ letterA6in6 = False
    $ letterA6in7 = False
    $ letterA6in8 = False
    $ letterA6in9 = False
    $ letterA6in10 = False
    $ letterA6in11 = False

    $ letterH7in1 = False
    $ letterH7in2 = False
    $ letterH7in3 = False
    $ letterH7in4 = False
    $ letterH7in5 = False
    $ letterH7in6 = False
    $ letterH7in7 = False
    $ letterH7in8 = False
    $ letterH7in9 = False
    $ letterH7in10 = False
    $ letterH7in11 = False

    $ letterA8in1 = False
    $ letterA8in2 = False
    $ letterA8in3 = False
    $ letterA8in4 = False
    $ letterA8in5 = False
    $ letterA8in6 = False
    $ letterA8in7 = False
    $ letterA8in8 = False
    $ letterA8in9 = False
    $ letterA8in10 = False
    $ letterA8in11 = False

    $ letterT9in1 = False
    $ letterT9in2 = False
    $ letterT9in3 = False
    $ letterT9in4 = False
    $ letterT9in5 = False
    $ letterT9in6 = False
    $ letterT9in7 = False
    $ letterT9in8 = False
    $ letterT9in9 = False
    $ letterT9in10 = False
    $ letterT9in11 = False

    $ letterA10in1 = False
    $ letterA10in2 = False
    $ letterA10in3 = False
    $ letterA10in4 = False
    $ letterA10in5 = False
    $ letterA10in6 = False
    $ letterA10in7 = False
    $ letterA10in8 = False
    $ letterA10in9 = False
    $ letterA10in10 = False
    $ letterA10in11 = False

    $ letterT11in1 = False
    $ letterT11in2 = False
    $ letterT11in3 = False
    $ letterT11in4 = False
    $ letterT11in5 = False
    $ letterT11in6 = False
    $ letterT11in7 = False
    $ letterT11in8 = False
    $ letterT11in9 = False
    $ letterT11in10 = False
    $ letterT11in11 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 15
    
    call gamefile_h4

label gamefile_h4:
    #image moon = "images/blankgram_m5_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatesh4

    if gate_name == "letterK1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterK1x = 865
            $ letterK1y = 340
            $ letterK1in1 = True
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterK1x = 1265
            $ letterK1y = 340
            $ letterK1in1 = False
            $ letterK1in2 = True
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterK1x = 1665
            $ letterK1y = 340
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = True
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterK1x = 865
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = True
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterK1x = 1015
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = True
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterK1x = 1265
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = True
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterK1x = 1515
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = True
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterK1x = 1665
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = True
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterK1x = 1115
            $ letterK1y = 690
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = True
            $ letterK1in10 = False
            $ letterK1in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterK1x = 1265
            $ letterK1y = 690
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = True
            $ letterK1in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterK1x = 1415
            $ letterK1y = 690
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False
            $ letterK1in8 = False
            $ letterK1in9 = False
            $ letterK1in10 = False
            $ letterK1in11 = True

    if gate_name == "letterK2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterK2X = 865
            $ letterK2y = 340
            $ letterK2in1 = True
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterK2X = 1265
            $ letterK2y = 340
            $ letterK2in1 = False
            $ letterK2in2 = True
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterK2X = 1665
            $ letterK2y = 340
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = True
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterK2X = 865
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = True
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterK2X = 1015
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = True
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterK2X = 1265
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = True
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterK2X = 1515
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = True
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterK2X = 1665
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = True
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterK2X = 1115
            $ letterK2y = 690
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = True
            $ letterK2in10 = False
            $ letterK2in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterK2X = 1265
            $ letterK2y = 690
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = True
            $ letterK2in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterK2X = 1415
            $ letterK2y = 690
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
            $ letterK2in8 = False
            $ letterK2in9 = False
            $ letterK2in10 = False
            $ letterK2in11 = True

    if gate_name == "letterM1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterM3x = 865
            $ letterM3y = 340
            $ letterM3in1 = True
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterM3x = 1265
            $ letterM3y = 340
            $ letterM3in1 = False
            $ letterM3in2 = True
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterM3x = 1665
            $ letterM3y = 340
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = True
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterM3x = 865
            $ letterM3y = 515
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = True
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterM3x = 1015
            $ letterM3y = 515
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = True
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterM3x = 1265
            $ letterM3y = 515
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = True
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterM3x = 1515
            $ letterM3y = 515
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = True
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterM3x = 1665
            $ letterM3y = 515
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = True
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterM3x = 1115
            $ letterM3y = 690
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = True
            $ letterM3in10 = False
            $ letterM3in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterM3x = 1265
            $ letterM3y = 690
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = True
            $ letterM3in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterM3x = 1415
            $ letterM3y = 690
            $ letterM3in1 = False
            $ letterM3in2 = False
            $ letterM3in3 = False
            $ letterM3in4 = False
            $ letterM3in5 = False
            $ letterM3in6 = False
            $ letterM3in7 = False
            $ letterM3in8 = False
            $ letterM3in9 = False
            $ letterM3in10 = False
            $ letterM3in11 = True


    if gate_name == "letterA1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterA4x = 865
            $ letterA4y = 340
            $ letterA4in1 = True
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterK41in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterA4x = 1265
            $ letterA4y = 340
            $ letterA4in1 = False
            $ letterA4in2 = True
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterA4x = 1665
            $ letterA4y = 340
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = True
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterA4x = 865
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = True
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterA4x = 1015
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = True
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterA4x = 1265
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = True
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterA4x = 1515
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = True
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterA4x = 1665
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = True
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterA4x = 1115
            $ letterA4y = 690
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = True
            $ letterA4in10 = False
            $ letterA4in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False


            #sets values for the checks
            $ letterA4x = 1265
            $ letterA4y = 690
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = True
            $ letterA4in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterA4x = 1415
            $ letterA4y = 690
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
            $ letterA4in8 = False
            $ letterA4in9 = False
            $ letterA4in10 = False
            $ letterA4in11 = True


    if gate_name == "letterT1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ lettertT5x = 865
            $ lettertT5y = 340
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
            $ letterT5in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ lettertT5x = 1265
            $ lettertT5y = 340
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
            $ letterT5in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ lettertT5x = 1665
            $ lettertT5y = 340
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
            $ letterT5in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ lettertT5x = 865
            $ lettertT5y = 515
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
            $ letterT5in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ lettertT5x = 1015
            $ lettertT5y = 515
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
            $ letterT5in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ lettertT5x = 1265
            $ lettertT5y = 515
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
            $ letterT5in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ lettertT5x = 1515
            $ lettertT5y = 515
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
            $ letterT5in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ lettertT5x = 1665
            $ lettertT5y = 515
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
            $ letterT5in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ lettertT5x = 1115
            $ lettertT5y = 690
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
            $ letterT5in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ lettertT5x = 1265
            $ lettertT5y = 690
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
            $ letterT5in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ lettertT5x = 1415
            $ lettertT5y = 690
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
            $ letterT5in11 = True

    if gate_name == "letterA2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterA6x = 865
            $ letterA6y = 340
            $ letterA6in1 = True
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterA6x = 1265
            $ letterA6y = 340
            $ letterA6in1 = False
            $ letterA6in2 = True
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterA6x = 1665
            $ letterA6y = 340
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = True
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterA6x = 865
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = True
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterA6x = 1015
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = True
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterA6x = 1265
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = True
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterA6x = 1515
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = True
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterA6x = 1665
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = True
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterA6x = 1115
            $ letterA6y = 690
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = True
            $ letterA6in10 = False
            $ letterA6in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterA6x = 1265
            $ letterA6y = 690
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = True
            $ letterA6in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterA6x = 1415
            $ letterA6y = 690
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
            $ letterA6in9 = False
            $ letterA6in10 = False
            $ letterA6in11 = True

    if gate_name == "letterH1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterH7x = 865
            $ letterH7y = 340
            $ letterH7in1 = True
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterH7x = 1265
            $ letterH7y = 340
            $ letterH7in1 = False
            $ letterH7in2 = True
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterH7x = 1665
            $ letterH7y = 340
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = True
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterH7x = 865
            $ letterH7y = 515
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = True
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterH7x = 1015
            $ letterH7y = 515
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = True
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterH7x = 1265
            $ letterH7y = 515
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = True
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterH7x = 1515
            $ letterH7y = 515
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = True
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterH7x = 1665
            $ letterH7y = 515
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = True
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterH7x = 1115
            $ letterH7y = 690
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = True
            $ letterH7in10 = False
            $ letterH7in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterH7x = 1265
            $ letterH7y = 690
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = True
            $ letterH7in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterH7x = 1415
            $ letterH7y = 690
            $ letterH7in1 = False
            $ letterH7in2 = False
            $ letterH7in3 = False
            $ letterH7in4 = False
            $ letterH7in5 = False
            $ letterH7in6 = False
            $ letterH7in7 = False
            $ letterH7in8 = False
            $ letterH7in9 = False
            $ letterH7in10 = False
            $ letterH7in11 = True

           #8
    if gate_name == "letterA3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterA8x = 865
            $ letterA8y = 340
            $ letterA8in1 = True
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterA8x = 1265
            $ letterA8y = 340
            $ letterA8in1 = False
            $ letterA8in2 = True
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterA8x = 1665
            $ letterA8y = 340
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = True
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterA8x = 865
            $ letterA8y = 515
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = True
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterA8x = 1015
            $ letterA8y = 515
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = True
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterA8x = 1265
            $ letterA8y = 515
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = True
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterA8x = 1515
            $ letterA8y = 515
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = True
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterA8x = 1665
            $ letterA8y = 515
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = True
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False


            #sets values for the checks
            $ letterA8x = 1115
            $ letterA8y = 690
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = True
            $ letterA8in10 = False
            $ letterA8in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterA8x = 1265
            $ letterA8y = 690
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = True
            $ letterA8in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterA8x = 1415
            $ letterA8y = 690
            $ letterA8in1 = False
            $ letterA8in2 = False
            $ letterA8in3 = False
            $ letterA8in4 = False
            $ letterA8in5 = False
            $ letterA8in6 = False
            $ letterA8in7 = False
            $ letterA8in8 = False
            $ letterA8in9 = False
            $ letterA8in10 = False
            $ letterA8in11 = True

            #9
    if gate_name == "letterT2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterT9x = 865
            $ letterT9y = 340
            $ letterT9in1 = True
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterT9x = 1265
            $ letterT9y = 340
            $ letterT9in1 = False
            $ letterT9in2 = True
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterT9x = 1665
            $ letterT9y = 340
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = True
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterT9x = 865
            $ letterT9y = 515
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = True
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterT9x = 1015
            $ letterT9y = 515
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = True
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterT9x = 1265
            $ letterT9y = 515
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = True
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterT9x = 1515
            $ letterT9y = 515
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = True
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterT9x = 1665
            $ letterT9y = 515
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = True
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterT9x = 1115
            $ letterT9y = 690
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = True
            $ letterT9in10 = False
            $ letterT9in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterT9x = 1265
            $ letterT9y = 690
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = True
            $ letterT9in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterT9x = 1415
            $ letterT9y = 690
            $ letterT9in1 = False
            $ letterT9in2 = False
            $ letterT9in3 = False
            $ letterT9in4 = False
            $ letterT9in5 = False
            $ letterT9in6 = False
            $ letterT9in7 = False
            $ letterT9in8 = False
            $ letterT9in9 = False
            $ letterT9in10 = False
            $ letterT9in11 = True

    if gate_name == "letterA4":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterA10x = 865
            $ letterA10y = 340
            $ letterA10in1 = True
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterA10x = 1265
            $ letterA10y = 340
            $ letterA10in1 = False
            $ letterA10in2 = True
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterA10x = 1665
            $ letterA10y = 340
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = True
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterA10x = 865
            $ letterA10y = 515
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = True
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterA10x = 1015
            $ letterA10y = 515
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = True
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterA10x = 1265
            $ letterA10y = 515
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = True
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterA10x = 1515
            $ letterA10y = 515
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = True
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterA10x = 1665
            $ letterA10y = 515
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = True
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterA10x = 1115
            $ letterA10y = 690
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = True
            $ letterA10in10 = False
            $ letterA10in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterA10x = 1265
            $ letterA10y = 690
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = True
            $ letterA10in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterA10x = 1415
            $ letterA10y = 690
            $ letterA10in1 = False
            $ letterA10in2 = False
            $ letterA10in3 = False
            $ letterA10in4 = False
            $ letterA10in5 = False
            $ letterA10in6 = False
            $ letterA10in7 = False
            $ letterA10in8 = False
            $ letterA10in9 = False
            $ letterA10in10 = False
            $ letterA10in11 = True



    if gate_name == "letterT3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m5_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterM3in1 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterH7in1 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in1 = False
            if letterA8in1 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in1 = False
            if letterT9in1 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in1 = False
            if letterA10in1 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in1 = False
            if letterT11in1 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in1 = False
            #sets values for checks
            $ letterT11x = 865
            $ letterT11y = 340
            $ letterT11in1 = True
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterM3in2 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterH7in2 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in2 = False
            if letterA8in2 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in2 = False
            if letterT9in2 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in2 = False
            if letterA10in2 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in2 = False
            if letterT11in2 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in2 = False

            #sets check values
            $ letterT11x = 1265
            $ letterT11y = 340
            $ letterT11in1 = False
            $ letterT11in2 = True
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterM3in3 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterH7in3 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in3 = False
            if letterA8in3 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in3 = False
            if letterT9in3 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in3 = False
            if letterA10in3 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in3 = False
            if letterT11in3 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in3 = False

            #sets values for the checks
            $ letterT11x = 1665
            $ letterT11y = 340
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = True
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterM3in4 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterH7in4 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in4 = False
            if letterA8in4 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in4 = False
            if letterT9in4 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in4 = False
            if letterA10in4 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in4 = False
            if letterT11in4 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in4 = False

            #sets values for the checks
            $ letterT11x = 865
            $ letterT11y = 515
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = True
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterM3in5 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterH7in5 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in5 = False
            if letterA8in5 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in5 = False
            if letterT9in5 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in5 = False
            if letterA10in5 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in5 = False
            if letterT11in5 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in5 = False

            #sets values for the checks
            $ letterT11x = 1015
            $ letterT11y = 515
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = True
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterM3in6 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterH7in6 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in6 = False
            if letterA8in6 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in6 = False
            if letterT9in6 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in6 = False
            if letterA10in6 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in6 = False
            if letterT11in6 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in6 = False

            #sets values for the checks
            $ letterT11x = 1265
            $ letterT11y = 515
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = True
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterM3in7 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterH7in7 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in7 = False
            if letterA8in7 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in7 = False
            if letterT9in7 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in7 = False
            if letterA10in7 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in7 = False
            if letterT11in7 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in7 = False

            #sets values for the checks
            $ letterT11x = 1515
            $ letterT11y = 515
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = True
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in8 = False
            if letterK2in8 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in8 = False
            if letterM3in8 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in8 = False
            if letterA4in8 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in8 = False
            if letterT5in8 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterH7in8 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in8 = False
            if letterA8in8 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in8 = False
            if letterT9in8 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in8 = False
            if letterA10in8 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in8 = False
            if letterT11in8 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in8 = False

            #sets values for the checks
            $ letterT11x = 1665
            $ letterT11y = 515
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = True
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 9******************************
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in9 = False
            if letterK2in9 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in9 = False
            if letterM3in9 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in9 = False
            if letterA4in9 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in9 = False
            if letterT5in9 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in9 = False
            if letterA6in9 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in9 = False
            if letterH7in9 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in9 = False
            if letterA8in9 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in9 = False
            if letterT9in9 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in9 = False
            if letterA10in9 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in9 = False
            if letterT11in9 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in9 = False

            #sets values for the checks
            $ letterT11x = 1115
            $ letterT11y = 690
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = True
            $ letterT11in10 = False
            $ letterT11in11 = False

                #gate slot number 10******************************
        if slot_name == "gate slot ten":
            if letterK1in10 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in10 = False
            if letterK2in10 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in10 = False
            if letterM3in10 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in10 = False
            if letterA4in10 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in10 = False
            if letterT5in10 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in10 = False
            if letterA6in10 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in10 = False
            if letterH7in10 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in10 = False
            if letterA8in10 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in10 = False
            if letterT9in10 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in10 = False
            if letterA10in10 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in10 = False
            if letterT11in10 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in10 = False

            #sets values for the checks
            $ letterT11x = 1265
            $ letterT11y = 690
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = True
            $ letterT11in11 = False

                #gate slot number 11******************************
        if slot_name == "gate slot eleven":
            if letterK1in11 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in11 = False
            if letterK2in11 == True:
               $ letterK2X = 275
               $ letterK2y = 575
               $ letterK2in11 = False
            if letterM3in11 == True:
               $ letterM3x = 342
               $ letterM3y = 660
               $ letterM3in11 = False
            if letterA4in11 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in11 = False
            if letterT5in11 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in11 = False
            if letterA6in11 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in11 = False
            if letterH7in11 == True:
               $ letterH7x = 410
               $ letterH7y = 575
               $ letterH7in11 = False
            if letterA8in11 == True:
               $ letterA8x = 275
               $ letterA8y = 750
               $ letterA8in11 = False
            if letterT9in11 == True:
               $ letterT9x = 410
               $ letterT9y = 750
               $ letterT9in11 = False
            if letterA10in11 == True:
               $ letterA10x = 275
               $ letterA10y = 750
               $ letterA10in11 = False
            if letterT11in11 == True:
               $ letterT11x = 410
               $ letterT11y = 750
               $ letterT11in11 = False

            #sets values for the checks
            $ letterT11x = 1415
            $ letterT11y = 690
            $ letterT11in1 = False
            $ letterT11in2 = False
            $ letterT11in3 = False
            $ letterT11in4 = False
            $ letterT11in5 = False
            $ letterT11in6 = False
            $ letterT11in7 = False
            $ letterT11in8 = False
            $ letterT11in9 = False
            $ letterT11in10 = False
            $ letterT11in11 = True



    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "LetterK_gate_return" or slot_name == "LetterM_gate_return" or slot_name == "LetterA_gate_return" or slot_name == "LetterT_gate_return" or slot_name == "LetterH_gate_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
           
    #Dragbacks *******************************************************************************************
            if slot_name == "letterK_gate_return":
                $ attempts +=1
                if gate_name == "letterK1":
                    $ letterK1x = 275
                    $ letterK1y = 575
                    $ letterK1in1 = False
                    $ letterK1in2 = False
                    $ letterK1in3 = False
                    $ letterK1in4 = False
                    $ letterK1in5 = False
                    $ letterK1in6 = False
                    $ letterK1in7 = False
                    $ letterK1in8 = False
                    $ letterK1in9 = False
                    $ letterK1in10 = False
                    $ letterK1in11 = False
                if gate_name == "letterK2":
                    $ letterK2x = 275
                    $ letterK2y = 575
                    $ letterK2in1 = False
                    $ letterK2in2 = False
                    $ letterK2in3 = False
                    $ letterK2in4 = False
                    $ letterK2in5 = False
                    $ letterK2in6 = False
                    $ letterK2in7 = False
                    $ letterK2in8 = False
                    $ letterK2in9 = False
                    $ letterK2in10 = False
                    $ letterK2in11 = False
            if slot_name == "letterM_gate_return":
                $ attempts +=1
                if gate_name == "letterM1":
                    $ letterM3x = 342
                    $ letterM3y = 660
                    $ letterM3in1 = False
                    $ letterM3in2 = False
                    $ letterM3in3 = False
                    $ letterM3in4 = False
                    $ letterM3in5 = False
                    $ letterM3in6 = False
                    $ letterM3in7 = False
                    $ letterM3in8 = False
                    $ letterM3in9 = False
                    $ letterM3in10 = False
                    $ letterM3in11 = False
            if slot_name == "letterA_gate_return":
                $ attempts +=1
                if gate_name == "letterA1":
                    $ letterA4x = 275
                    $ letterA4y = 750
                    $ letterA4in1 = False
                    $ letterA4in2 = False
                    $ letterA4in3 = False
                    $ letterA4in4 = False
                    $ letterA4in5 = False
                    $ letterA4in6 = False
                    $ letterA4in7 = False
                    $ letterA4in8 = False
                    $ letterA4in9 = False
                    $ letterA4in10 = False
                    $ letterA4in11 = False
                if gate_name == "letterA2":
                    $ letterA6x = 275
                    $ letterA6y = 750
                    $ letterA6in1 = False
                    $ letterA6in2 = False
                    $ letterA6in3 = False
                    $ letterA6in4 = False
                    $ letterA6in5 = False
                    $ letterA6in6 = False
                    $ letterA6in7 = False
                    $ letterA6in8 = False
                    $ letterA6in9 = False
                    $ letterA6in10 = False
                    $ letterA6in11 = False
                if gate_name == "letterA3":
                    $ letterA8x = 275
                    $ letterA8y = 750
                    $ letterA8in1 = False
                    $ letterA8in2 = False
                    $ letterA8in3 = False
                    $ letterA8in4 = False
                    $ letterA8in5 = False
                    $ letterA8in6 = False
                    $ letterA8in7 = False
                    $ letterA8in8 = False
                    $ letterA8in9 = False
                    $ letterA8in10 = False
                    $ letterA8in11 = False
                if gate_name == "letterA4":
                    $ letterA10x = 275
                    $ letterA10y = 750
                    $ letterA10in1 = False
                    $ letterA10in2 = False
                    $ letterA10in3 = False
                    $ letterA10in4 = False
                    $ letterA10in5 = False
                    $ letterA10in6 = False
                    $ letterA10in7 = False
                    $ letterA10in8 = False
                    $ letterA10in9 = False
                    $ letterA10in10 = False
                    $ letterA10in11 = False
            if slot_name == "letterH_gate_return":
                $ attempts +=1
                if gate_name == "letterH1":
                    $ letterH7x = 410
                    $ letterH7y = 575
                    $ letterH7in1 = False
                    $ letterH7in2 = False
                    $ letterH7in3 = False
                    $ letterH7in4 = False
                    $ letterH7in5 = False
                    $ letterH7in6 = False
                    $ letterH7in7 = False
                    $ letterH7in8 = False
                    $ letterH7in9 = False
                    $ letterH7in10 = False
                    $ letterH7in11 = False
            if slot_name == "letterT_gate_return":
                $ attempts +=1
                if gate_name == "letterT1":
                    $ letterT5x = 410
                    $ letterT5y = 750
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
                    $ letterT5in11 = False
                if gate_name == "letterT2":
                    $ letterT9x = 410
                    $ letterT9y = 750
                    $ letterT9in1 = False
                    $ letterT9in2 = False
                    $ letterT9in3 = False
                    $ letterT9in4 = False
                    $ letterT9in5 = False
                    $ letterT9in6 = False
                    $ letterT9in7 = False
                    $ letterT9in8 = False
                    $ letterT9in9 = False
                    $ letterT9in10 = False
                    $ letterT9in11 = False
                if gate_name == "letterT3":
                    $ letterT11x = 410
                    $ letterT11y = 750
                    $ letterT11in1 = False
                    $ letterT11in2 = False
                    $ letterT11in3 = False
                    $ letterT11in4 = False
                    $ letterT11in5 = False
                    $ letterT11in6 = False
                    $ letterT11in7 = False
                    $ letterT11in8 = False
                    $ letterT11in9 = False
                    $ letterT11in10 = False
                    $ letterT11in11 = False
 
           
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
    hide gram_m5_tile57
    hide gram_m5_tile58
    hide gram_m5_tile59
    hide gram_m5_tile60
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
    hide gram_m5_tile76
    hide gram_m5_tile77
    hide gram_m5_tile78
    hide gram_m5_tile79
    hide gram_m5_tile80
    hide gram_m5_tile81
    hide gram_m5_tile82
    hide gram_m5_tile83
    hide gram_m5_tile84
    hide gram_m5_tile85
    hide gram_m5_tile86
    hide gram_m5_tile87
    hide gram_m5_tile88
    hide gram_m5_tile89
    hide gram_m5_tile90
    hide gram_m5_tile91
    hide gram_m5_tile92
    hide gram_m5_tile93
    hide gram_m5_tile94
    hide gram_m5_tile95
    hide gram_m5_tile96
    hide gram_m5_tile97
    hide gram_m5_tile98
    hide gram_m5_tile99
    hide gram_m5_tile100
    hide gram_m5_tile101
    hide gram_m5_tile102
    hide gram_m5_tile103
    hide gram_m5_tile104
    hide gram_m5_tile105
    hide gram_m5_tile106
    hide gram_m5_tile107
    hide gram_m5_tile108
    hide gram_m5_tile109
    hide gram_m5_tile110
    hide gram_m5_tile111
    hide gram_m5_tile112
    hide gram_m5_tile113
    hide gram_m5_tile114
    hide gram_m5_tile115
    hide gram_m5_tile116
    hide gram_m5_tile117
    hide gram_m5_tile118
    hide gram_m5_tile119
    hide gram_m5_tile120
    hide gram_m5_tile121
    hide gram_m5_tile122
    hide gram_m5_tile123
    hide gram_m5_tile124
    hide gram_m5_tile125
    hide gram_m5_tile126
    hide gram_m5_tile127
    hide gram_m5_tile128
    hide gram_m5_tile129
    hide gram_m5_tile130
    hide gram_m5_tile131
    hide gram_m5_tile132
    hide gram_m5_tile133
    hide gram_m5_tile134
    hide gram_m5_tile135
    hide gram_m5_tile136
    hide gram_m5_tile137
    hide gram_m5_tile138
    hide gram_m5_tile139
    hide gram_m5_tile140
    hide gram_m5_tile141
    hide gram_m5_tile142
    hide gram_m5_tile143
    hide gram_m5_tile144
    hide gram_m5_tile145
        
    if (letterK2in1 == True or letterK1in1 == True) and (letterA4in3 == True or letterA6in3 == True or letterA8in3 == True or letterA10in3 == True) and (letterT5in2 == True or letterT9in2 == True or letterT11in2 == True):
        image gram_m5_tile42 = "leftTreegreenlong2.png"
        image gram_m5_tile43 = "1_1_green.png"
        show gram_m5_tile42 at Position(xpos = 885, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_m5_tile43 at Position(xpos = 850, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_m5_tile44 = "treeGreen.png"
        image gram_m5_tile45 = "1_1_green.png"
        show gram_m5_tile44 at Position(xpos = 1250, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_m5_tile45 at Position(xpos = 1250, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_m5_tile46 = "rightTreegreenlong2.png"
        image gram_m5_tile47 = "1_1_green.png"
        show gram_m5_tile46 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_m5_tile47 at Position(xpos = 1650, xanchor = 0, ypos = 325, yanchor = 0)

        if (letterM3in4 == True):
            image gram_m5_tile48 = "treeGreen.png"
            image gram_m5_tile49 = "1_1_green.png"
            show gram_m5_tile48 at Position(xpos = 850, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile49 at Position(xpos = 850, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile50 = "solutionLine.png"
            image gram_m5_tile51 = "solutionLine.png"
            show gram_m5_tile50 at Position(xpos = 830, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_m5_tile51 at Position(xpos = 830, xanchor = 0, ypos = 692, yanchor = 0)           
            image gram_m5_tile52 = "solutionLine.png"
            show gram_m5_tile52 at Position(xpos = 830, xanchor = 0, ypos = 785, yanchor = 0)
            image gram_m5_tile53 = "foolish.png"
            show gram_m5_tile53 at Position(xpos = 750, xanchor = 0, ypos = 800, yanchor = 0)
        elif (letterK1in4 or letterK2in4 or letterA4in4 or letterT5in4 or letterA6in4 or letterH7in4 or letterA8in4 or letterT9in4 or letterA10in4 or letterT11in4):
            image gram_m5_tile54 = "treeRed.png"
            image gram_m5_tile55 = "1_1_red.png"
            show gram_m5_tile54 at Position(xpos = 850, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile55 at Position(xpos = 850, xanchor = 0, ypos = 500, yanchor = 0)

        if (letterH7in8 == True):
            image gram_m5_tile56 = "treeGreen.png"
            image gram_m5_tile57 = "1_1_green.png"
            show gram_m5_tile56 at Position(xpos = 1650, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile57 at Position(xpos = 1650, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile58 = "solutionLine.png"
            image gram_m5_tile59 = "solutionLine.png"
            show gram_m5_tile58 at Position(xpos = 1650, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_m5_tile59 at Position(xpos = 1650, xanchor = 0, ypos = 692, yanchor = 0)
            image gram_m5_tile60 = "solutionLine.png"
            image gram_m5_tile61 = "suit.png"
            show gram_m5_tile60 at Position(xpos = 1650, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_m5_tile61 at Position(xpos = 1650, xanchor = 0, ypos = 800, yanchor = 0)
        elif (letterK1in8 or letterK2in8 or letterM3in8 or letterA4in8 or letterT5in8 or letterA6in8 or letterA8in8 or letterT9in8 or letterA10in8 or letterT11in8):
            image gram_m5_tile114 = "treeRed.png"
            image gram_m5_tile115 = "1_1_red.png"
            show gram_m5_tile114 at Position(xpos = 1650, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile115 at Position(xpos = 1650, xanchor = 0, ypos = 500, yanchor = 0)
        
        if (letterA4in5 == True or letterA6in5 == True or letterA8in5 == True or letterA10in5 == True) and (letterT5in6 == True or letterT9in6 == True or letterT11in6 == True) and ((letterK2in7 == True or letterK1in7 == True)):
            image gram_m5_tile62 = "leftTreegreenlong1.png"
            image gram_m5_tile63 = "1_1_green.png"
            show gram_m5_tile62 at Position(xpos = 1040, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile63 at Position(xpos = 1000, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile64 = "solutionLine.png"
            image gram_m5_tile65 = "solutionLine.png"
            show gram_m5_tile64 at Position(xpos = 980, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_m5_tile65 at Position(xpos = 980, xanchor = 0, ypos = 692, yanchor = 0)
            image gram_m5_tile66 = "solutionLine.png"
            image gram_m5_tile67 = "epsilon.png"
            show gram_m5_tile66 at Position(xpos = 980, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_m5_tile67 at Position(xpos = 900, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_m5_tile68 = "treeGreen.png"
            image gram_m5_tile69 = "1_1_green.png"
            show gram_m5_tile68 at Position(xpos = 1250, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile69 at Position(xpos = 1250, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_m5_tile70 = "rightTreegreenlong1.png"
            image gram_m5_tile71 = "1_1_green.png"

            show gram_m5_tile70 at Position(xpos = 1310, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile71 at Position(xpos = 1500, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_m5_tile72 = "solutionLine.png"
            image gram_m5_tile73 = "solutionLine.png"
            image gram_m5_tile74 = "solutionLine.png"
            image gram_m5_tile75 = "meat.png"

            show gram_m5_tile72 at Position(xpos = 1500, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_m5_tile73 at Position(xpos = 1500, xanchor = 0, ypos = 692, yanchor = 0)
            show gram_m5_tile74 at Position(xpos = 1500, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_m5_tile75 at Position(xpos = 1500, xanchor = 0, ypos = 800, yanchor = 0)


            if (letterA4in9 == True or letterA6in9 == True or letterA8in9 == True or letterA10in9 == True) and (letterT5in10 == True or letterT9in10 == True or letterT11in10 == True) and ((letterA4in11 == True or letterA6in11 == True or letterA8in11 == True or letterA10in11 == True)):
               image gram_m5_tile76 = "leftTreegreenlong.png"
               image gram_m5_tile77 = "1_1_green.png"
               image gram_m5_tile78 = "solutionLine.png"
               image gram_m5_tile79 = "epsilon.png"
               show gram_m5_tile76 at Position(xpos = 1140, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile77 at Position(xpos = 1100, xanchor = 0, ypos = 675, yanchor = 0)
               show gram_m5_tile78 at Position(xpos = 1100, xanchor = 0, ypos = 770, yanchor = 0)
               show gram_m5_tile79 at Position(xpos = 1050, xanchor = 0, ypos = 800, yanchor = 0)
               image gram_m5_tile80 = "treeGreen.png"
               image gram_m5_tile81 = "1_1_green.png"
               show gram_m5_tile80 at Position(xpos = 1250, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile81 at Position(xpos = 1250, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile82 = "solutionLine.png"
               image gram_m5_tile83 = "organic.png"
               show gram_m5_tile82 at Position(xpos = 1250, xanchor = 0, ypos = 770, yanchor = 0)
               show gram_m5_tile83 at Position(xpos = 1202, xanchor = 0, ypos = 800, yanchor = 0)
               image gram_m5_tile84 = "rightTreegreenlong.png"
               image gram_m5_tile85 = "1_1_green.png"
               show gram_m5_tile84 at Position(xpos = 1310, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile85 at Position(xpos = 1400, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile86 = "solutionLine.png"
               image gram_m5_tile87 = "epsilon.png"
               show gram_m5_tile86 at Position(xpos = 1400, xanchor = 0, ypos = 770, yanchor = 0)
               show gram_m5_tile87 at Position(xpos = 1355, xanchor = 0, ypos = 800, yanchor = 0)
            elif ((letterK1in9 or letterK2in9 or letterM3in9 or letterA4in9 or letterT5in9 or letterA6in9 or letterH7in9 or letterA8in9 or letterT9in9 or letterA10in9 or letterT11in9) and
                    (letterK1in10 or letterK2in10 or letterM3in10 or letterA4in10 or letterT5in10 or letterA6in10 or letterH7in10 or letterA8in10 or letterT9in10 or letterA10in10 or letterT11in10) and
                    (letterK1in11 or letterK2in11 or letterM3in11 or letterA4in11 or letterT5in11 or letterA6in11 or letterH7in11 or letterA8in11 or letterT9in11 or letterA10in11 or letterT11in11)):
               image gram_m5_tile134 = "leftTreeredlong.png"
               image gram_m5_tile135 = "1_1_red.png"
               show gram_m5_tile134 at Position(xpos = 1140, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile135 at Position(xpos = 1100, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile136 = "treeRed.png"
               image gram_m5_tile137 = "1_1_red.png"
               show gram_m5_tile136 at Position(xpos = 1250, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile137 at Position(xpos = 1250, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile138 = "rightTreeredlong.png"
               image gram_m5_tile139 = "1_1_red.png"
               show gram_m5_tile138 at Position(xpos = 1310, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile139 at Position(xpos = 1400, xanchor = 0, ypos = 675, yanchor = 0)

        elif ((letterK1in5 or letterK2in5 or letterM3in5 or letterA4in5 or letterT5in5 or letterA6in5 or letterH7in5 or letterA8in5 or letterT9in5 or letterA10in5 or letterT11in5) and
                (letterK1in6 or letterK2in6 or letterM3in6 or letterA4in6 or letterT5in6 or letterA6in6 or letterH7in6 or letterA8in6 or letterT9in6 or letterA10in6 or letterT11in6) and
                (letterK1in7 or letterK2in7 or letterM3in7 or letterA4in7 or letterT5in7 or letterA6in7 or letterH7in7 or letterA8in7 or letterT9in7 or letterA10in7 or letterT11in7)):
            image gram_m5_tile122 = "leftTreeredlong1.png"
            image gram_m5_tile123 = "1_1_red.png"
            show gram_m5_tile122 at Position(xpos = 1040, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile123 at Position(xpos = 1000, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile124 = "treeRed.png"
            image gram_m5_tile125 = "1_1_red.png"
            show gram_m5_tile124 at Position(xpos = 1250, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile125 at Position(xpos = 1250, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile126 = "rightTreeredlong1.png"
            image gram_m5_tile127 = "1_1_red.png"
            show gram_m5_tile126 at Position(xpos = 1310, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile127 at Position(xpos = 1500, xanchor = 0, ypos = 500, yanchor = 0)        
            
            
        if (letterA4in5 == True or letterA6in5 == True or letterA8in5 == True or letterA10in5 == True) and (letterT5in6 == True or letterT9in6 == True or letterT11in6 == True) and (letterA4in7 == True or letterA6in7 == True or letterA8in7 == True or letterA10in7 == True):
            image gram_m5_tile100 = "leftTreegreenlong1.png"
            image gram_m5_tile101 = "1_1_green.png"
            show gram_m5_tile100 at Position(xpos = 1040, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile101 at Position(xpos = 1000, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile102 = "solutionLine.png"
            image gram_m5_tile103 = "solutionLine.png"
            show gram_m5_tile102 at Position(xpos = 980, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_m5_tile103 at Position(xpos = 980, xanchor = 0, ypos = 692, yanchor = 0)
            image gram_m5_tile104 = "solutionLine.png"
            image gram_m5_tile105 = "epsilon.png"
            show gram_m5_tile104 at Position(xpos = 980, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_m5_tile105 at Position(xpos = 900, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_m5_tile106 = "treeGreen.png"
            image gram_m5_tile107 = "1_1_green.png"
            show gram_m5_tile106 at Position(xpos = 1250, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile107 at Position(xpos = 1250, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_m5_tile108 = "rightTreegreenlong1.png"
            image gram_m5_tile109 = "1_1_green.png"

            show gram_m5_tile108 at Position(xpos = 1310, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile109 at Position(xpos = 1500, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_m5_tile110 = "solutionLine.png"
            image gram_m5_tile111 = "solutionLine.png"
            image gram_m5_tile112 = "solutionLine.png"
            image gram_m5_tile113 = "epsilon.png"

            show gram_m5_tile110 at Position(xpos = 1500, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_m5_tile111 at Position(xpos = 1500, xanchor = 0, ypos = 692, yanchor = 0)
            show gram_m5_tile112 at Position(xpos = 1500, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_m5_tile113 at Position(xpos = 1500, xanchor = 0, ypos = 800, yanchor = 0)

            if (letterA4in9 == True or letterA6in9 == True or letterA8in9 == True or letterA10in9 == True) and (letterT5in10 == True or letterT9in10 == True or letterT11in10 == True) and ((letterK2in11 == True or letterK1in11 == True)):
               #image gram_m5_tile50 = "leftTreegreen.png"
               image gram_m5_tile88 = "leftTreegreenlong.png"
               image gram_m5_tile89 = "1_1_green.png"
               image gram_m5_tile90 = "solutionLine.png"
               image gram_m5_tile91 = "epsilon.png"
               #show gram_m5_tile50 at Position(xpos = 960, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m5_tile88 at Position(xpos = 1140, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile89 at Position(xpos = 1100, xanchor = 0, ypos = 675, yanchor = 0)
               show gram_m5_tile90 at Position(xpos = 1100, xanchor = 0, ypos = 770, yanchor = 0)
               show gram_m5_tile91 at Position(xpos = 1050, xanchor = 0, ypos = 800, yanchor = 0)

               image gram_m5_tile92 = "treeGreen.png"
               image gram_m5_tile93 = "1_1_green.png"
               show gram_m5_tile92 at Position(xpos = 1250, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile93 at Position(xpos = 1250, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile94 = "solutionLine.png"
               image gram_m5_tile95 = "organic.png"
               show gram_m5_tile94 at Position(xpos = 1250, xanchor = 0, ypos = 770, yanchor = 0)
               show gram_m5_tile95 at Position(xpos = 1202, xanchor = 0, ypos = 800, yanchor = 0)

               image gram_m5_tile96 = "rightTreegreenlong.png"
               image gram_m5_tile97 = "1_1_green.png"
               show gram_m5_tile96 at Position(xpos = 1310, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile97 at Position(xpos = 1400, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile98 = "solutionLine.png"
               image gram_m5_tile99 = "meat.png"
               show gram_m5_tile98 at Position(xpos = 1400, xanchor = 0, ypos = 770, yanchor = 0)
               show gram_m5_tile99 at Position(xpos = 1355, xanchor = 0, ypos = 800, yanchor = 0)
            elif ((letterK1in9 or letterK2in9 or letterM3in9 or letterA4in9 or letterT5in9 or letterA6in9 or letterH7in9 or letterA8in9 or letterT9in9 or letterA10in9 or letterT11in9) and
                    (letterK1in10 or letterK2in10 or letterM3in10 or letterA4in10 or letterT5in10 or letterA6in10 or letterH7in10 or letterA8in10 or letterT9in10 or letterA10in10 or letterT11in10) and
                    (letterK1in11 or letterK2in11 or letterM3in11 or letterA4in11 or letterT5in11 or letterA6in11 or letterH7in11 or letterA8in11 or letterT9in11 or letterA10in11 or letterT11in11)):
               image gram_m5_tile140 = "leftTreeredlong.png"
               image gram_m5_tile141 = "1_1_red.png"
               show gram_m5_tile140 at Position(xpos = 1140, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile141 at Position(xpos = 1100, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile142 = "treeRed.png"
               image gram_m5_tile143 = "1_1_red.png"
               show gram_m5_tile142 at Position(xpos = 1250, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile143 at Position(xpos = 1250, xanchor = 0, ypos = 675, yanchor = 0)
               image gram_m5_tile144 = "rightTreeredlong.png"
               image gram_m5_tile145 = "1_1_red.png"
               show gram_m5_tile144 at Position(xpos = 1310, xanchor = 0, ypos = 600, yanchor = 0)
               show gram_m5_tile145 at Position(xpos = 1400, xanchor = 0, ypos = 675, yanchor = 0)
               
        elif ((letterK1in5 or letterK2in5 or letterM3in5 or letterA4in5 or letterT5in5 or letterA6in5 or letterH7in5 or letterA8in5 or letterT9in5 or letterA10in5 or letterT11in5) and
                (letterK1in6 or letterK2in6 or letterM3in6 or letterA4in6 or letterT5in6 or letterA6in6 or letterH7in6 or letterA8in6 or letterT9in6 or letterA10in6 or letterT11in6) and
                (letterK1in7 or letterK2in7 or letterM3in7 or letterA4in7 or letterT5in7 or letterA6in7 or letterH7in7 or letterA8in7 or letterT9in7 or letterA10in7 or letterT11in7)):
            image gram_m5_tile128 = "leftTreeredlong1.png"
            image gram_m5_tile129 = "1_1_red.png"
            show gram_m5_tile128 at Position(xpos = 1040, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile129 at Position(xpos = 1000, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile130 = "treeRed.png"
            image gram_m5_tile131 = "1_1_red.png"
            show gram_m5_tile130 at Position(xpos = 1250, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile131 at Position(xpos = 1250, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_m5_tile132 = "rightTreeredlong1.png"
            image gram_m5_tile133 = "1_1_red.png"
            show gram_m5_tile132 at Position(xpos = 1310, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_m5_tile133 at Position(xpos = 1500, xanchor = 0, ypos = 500, yanchor = 0)   
            
    elif ((letterK1in1 or letterK2in1 or letterM3in1 or letterA4in1 or letterT5in1 or letterA6in1 or letterH7in1 or letterA8in1 or letterT9in1 or letterA10in1 or letterT11in1) and
            (letterK1in2 or letterK2in2 or letterM3in2 or letterA4in2 or letterT5in2 or letterA6in2 or letterH7in2 or letterA8in2 or letterT9in2 or letterA10in2 or letterT11in2) and
            (letterK1in3 or letterK2in3 or letterM3in3 or letterA4in3 or letterT5in3 or letterA6in3 or letterH7in3 or letterA8in3 or letterT9in3 or letterA10in3 or letterT11in3)):
        image gram_m5_tile116 = "leftTreeredlong2.png"
        image gram_m5_tile117 = "1_1_red.png"
        show gram_m5_tile116 at Position(xpos = 885, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_m5_tile117 at Position(xpos = 850, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_m5_tile118 = "treeRed.png"
        image gram_m5_tile119 = "1_1_red.png"
        show gram_m5_tile118 at Position(xpos = 1250, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_m5_tile119 at Position(xpos = 1250, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_m5_tile120 = "rightTreeredlong2.png"
        image gram_m5_tile121 = "1_1_red.png"
        show gram_m5_tile120 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_m5_tile121 at Position(xpos = 1650, xanchor = 0, ypos = 325, yanchor = 0)
        
    #win conditions
    if (((letterK2in1 == True or letterK1in1 == True) and (letterA4in3 == True or letterA6in3 == True or letterA8in3 == True or letterA10in3 == True) and 
        (letterT5in2 == True or letterT9in2 == True or letterT11in2 == True) and
        (letterM3in4 == True) and (letterH7in8 == True) and
        ((letterA4in5 == True or letterA6in5 == True or letterA8in5 == True or letterA10in5 == True) and (letterT5in6 == True or letterT9in6 == True or letterT11in6 == True) and 
        (letterA4in7 == True or letterA6in7 == True or letterA8in7 == True or letterA10in7 == True) and (letterA4in9 == True or letterA6in9 == True or letterA8in9 == True or letterA10in9 == True) and 
        (letterT5in10 == True or letterT9in10 == True or letterT11in10 == True) and (letterK2in11 == True or letterK1in11 == True))) or

        ((letterK2in1 == True or letterK1in1 == True) and (letterA4in3 == True or letterA6in3 == True or letterA8in3 == True or letterA10in3 == True) and 
        (letterT5in2 == True or letterT9in2 == True or letterT11in2 == True) and
        (letterM3in4 == True) and (letterH7in8 == True) and
        ((letterA4in5 == True or letterA6in5 == True or letterA8in5 == True or letterA10in5 == True) and (letterT5in6 == True or letterT9in6 == True or letterT11in6 == True) and 
        (letterK2in7 == True or letterK1in7 == True) and
        (letterA4in9 == True or letterA6in9 == True or letterA8in9 == True or letterA10in9 == True) and (letterT5in10 == True or letterT9in10 == True or letterT11in10 == True) and 
        (letterA4in11 == True or letterA6in11 == True or letterA8in11 == True or letterA10in11 == True)))):


        image gram_m5_tile202 = "letterK.png"
        image gram_m5_tile206 = "letterK.png"
        image gram_m5_tile203 = "letterM.png"
        image gram_m5_tile205 = "letterA.png"
        image gram_m5_tile201 = "letterT.png"
        image gram_m5_tile204 = "letterA.png"
        image gram_m5_tile208 = "letterH.png"
        image gram_m5_tile408 = "letterA.png"
        image gram_m5_tile409 = "letterT.png"
        image gram_m5_tile410 = "letterA.png"
        image gram_m5_tile411 = "letterT.png"
        
        show gram_m5_tile202 at Position(xpos = 865, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_m5_tile206 at Position(xpos = 1415, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_m5_tile203 at Position(xpos = 865, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile205 at Position(xpos = 1665, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_m5_tile201 at Position(xpos = 1265, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_m5_tile204 at Position(xpos = 1015, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile208 at Position(xpos = 1665, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile408 at Position(xpos = 1515, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile409 at Position(xpos = 1265, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile410 at Position(xpos = 1115, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_m5_tile411 at Position(xpos = 1265, xanchor = 0, ypos = 690, yanchor = 0)

        "Access Gained"

        jump eng_gram_h4#gram_m5#start

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
        hide gram_m5_tile57
        hide gram_m5_tile58
        hide gram_m5_tile59
        hide gram_m5_tile60
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
        hide gram_m5_tile76
        hide gram_m5_tile77
        hide gram_m5_tile78
        hide gram_m5_tile79
        hide gram_m5_tile80
        hide gram_m5_tile81
        hide gram_m5_tile82
        hide gram_m5_tile83
        hide gram_m5_tile84
        hide gram_m5_tile85
        hide gram_m5_tile86
        hide gram_m5_tile87
        hide gram_m5_tile88
        hide gram_m5_tile89
        hide gram_m5_tile90
        hide gram_m5_tile91
        hide gram_m5_tile92
        hide gram_m5_tile93
        hide gram_m5_tile94
        hide gram_m5_tile95
        hide gram_m5_tile96
        hide gram_m5_tile97
        hide gram_m5_tile98
        hide gram_m5_tile99
        hide gram_m5_tile100
        hide gram_m5_tile101
        hide gram_m5_tile102
        hide gram_m5_tile103
        hide gram_m5_tile104
        hide gram_m5_tile105
        hide gram_m5_tile106
        hide gram_m5_tile107
        hide gram_m5_tile108
        hide gram_m5_tile109
        hide gram_m5_tile110
        hide gram_m5_tile111
        hide gram_m5_tile112
        hide gram_m5_tile113
        hide gram_m5_tile114
        hide gram_m5_tile115
        hide gram_m5_tile116
        hide gram_m5_tile117
        hide gram_m5_tile118
        hide gram_m5_tile119
        hide gram_m5_tile120
        hide gram_m5_tile121
        hide gram_m5_tile122
        hide gram_m5_tile123
        hide gram_m5_tile124
        hide gram_m5_tile125
        hide gram_m5_tile126
        hide gram_m5_tile127
        hide gram_m5_tile128
        hide gram_m5_tile129
        hide gram_m5_tile130
        hide gram_m5_tile131
        hide gram_m5_tile132
        hide gram_m5_tile133
        hide gram_m5_tile134
        hide gram_m5_tile135
        hide gram_m5_tile136
        hide gram_m5_tile137
        hide gram_m5_tile138
        hide gram_m5_tile139
        hide gram_m5_tile140
        hide gram_m5_tile141
        hide gram_m5_tile142
        hide gram_m5_tile143
        hide gram_m5_tile144
        hide gram_m5_tile145

        show gram_m5_tile202 at Position(xpos = 865, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_m5_tile206 at Position(xpos = 1415, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_m5_tile203 at Position(xpos = 865, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile205 at Position(xpos = 1665, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_m5_tile201 at Position(xpos = 1265, xanchor = 0, ypos = 340, yanchor = 0)
        show gram_m5_tile204 at Position(xpos = 1015, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile208 at Position(xpos = 1665, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile408 at Position(xpos = 1515, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile409 at Position(xpos = 1265, xanchor = 0, ypos = 515, yanchor = 0)
        show gram_m5_tile410 at Position(xpos = 1115, xanchor = 0, ypos = 690, yanchor = 0)
        show gram_m5_tile411 at Position(xpos = 1265, xanchor = 0, ypos = 690, yanchor = 0)
        
        "You Lose Try Again"

        jump eng_gram_h4#gram_m5#start
    

#    if letterK1in1 == True or letterK2in1 ==True or letterM3in1 ==True or letterA4in1 ==True:
#        image gram_m5_tile109 = "leftTreegreen.png"
#        #shows gram_m5_tiles
#        show gram_m5_tile109 at Position(xpos = 825, xanchor = 0, ypos = 225, yanchor = 0)
#    if letterK1in1 == False and letterK2in1 == False and letterM3in1 == False and letterA4in1 ==False:
#        hide gram_m5_tile109      
    
    jump gamefile_m5