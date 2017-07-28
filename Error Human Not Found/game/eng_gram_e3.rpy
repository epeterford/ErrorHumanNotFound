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
        
#image blink:
 #   xpos 925 ypos 325
  #  xanchor 1.0 yanchor 1.0
   # "images/leftTree.png"
    #2
    #linear 0.5 alpha 1.0
    #"images/leftTreegreen.png"
    #2
    #linear 0.5 alpha 1.0
    #"images/leftTreered.png"
    #2
    #.15
    #linear 0.5 alpha 1.0
    #repeat

     #   if drag_name == "gate slot one" && child == "images/1_1.png":
      #  xpos 925 ypos 325
      #  add "images/leftTreegreen.png"
      #  return

screen logicGatese3:

    draggroup:
        #and gates
        drag:
                drag_name "letterS1"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3and1x ypos eae3and1y
        drag:
                drag_name "letterS2"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3and2x ypos eae3and2y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae3and3x ypos eae3and3y
        drag:
                drag_name "letterS3"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3and4x ypos eae3and4y
        drag:
                drag_name "letterS4"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3and5x ypos eae3and5y
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos eae3and6x ypos eae3and6y
       #drag:
       #        drag_name "and_gate6"
       #        child "letterP.png"
       #        droppable False
       #        dragged gate_dragged
       #        xpos and7x ypos and7y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 1115 ypos 340
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1415 ypos 335
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 1040 ypos 510
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 1190 ypos 510
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1340 ypos 510
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1490 ypos 510
       #drag:
       #        drag_name "gate slot seven"
       #        draggable False
       #        child "images/border.png"
       #        xpos 1000 ypos 725

init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_e3:

    scene bg Eng_Tile
    $ quick_menu = False
    $ game_menu = True
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image eaeng_e3_tile0 = "instructions3.png"
    image eaeng_e3_tile1 = "1_1_green.png"
    image eaeng_e3_tile2 = "letterS.png"
    show eaeng_e3_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_e3_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_e3_tile2 at Position(xpos = 1260, xanchor = 0, ypos = 165, yanchor = 0)
    
    #row2 5-8

    image eaeng_e3_tile5 = "leftTreelong.png"
    image eaeng_e3_tile6 = "rightTreelong.png"

    show eaeng_e3_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_e3_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_e3_tile9 = "1_1_grey.png"
    image eaeng_e3_tile10 = "1_1_grey.png"
    

    show eaeng_e3_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_e3_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_e3_tile14 = "leftTree.png"
    image eaeng_e3_tile15 = "rightTree.png"
    image eaeng_e3_tile16 = "leftTree.png"
    image eaeng_e3_tile17 = "rightTree.png"

    show eaeng_e3_tile14 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e3_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e3_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e3_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_e3_tile21 = "1_1_grey.png"
    image eaeng_e3_tile22 = "1_1_grey.png"
    image eaeng_e3_tile23 = "1_1_grey.png"
    image eaeng_e3_tile24 = "1_1_grey.png"

    show eaeng_e3_tile21 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e3_tile22 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e3_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e3_tile24 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)


    image eaeng_e3_tile31 = "letterBorder.png"
    image eaeng_e3_tile32 = "letterBorder.png"
    image eaeng_e3_tile33 = "letterBorder.png"
    #image eaengeaeng_e3_tile34 = "letterBorder.png"
    #image eaengeaeng_e3_tile35 = "letterBorder.png"
    #image eaengeaeng_e3_tile36 = "letterBorder.png"
    show eaeng_e3_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e3_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e3_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    #show eaengeaeng_e3_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    #show eaengeaeng_e3_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    #show eaengeaeng_e3_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ eae3and1x = 275 
    $ eae3and1y = 575
    $ eae3and2x = 275
    $ eae3and2y = 575
    $ eae3and3x = 342 
    $ eae3and3y = 660
    $ eae3and4x = 275
    $ eae3and4y = 575
    $ eae3and5x = 275
    $ eae3and5y = 575
    $ eae3and6x = 410 
    $ eae3and6y = 575

    
    # check conditons for locations
    $ and1in1 = False
    $ and1in2 = False
    $ and1in3 = False
    $ and1in4 = False
    $ and1in5 = False
    $ and1in6 = False
    $ and1in7 = False

    $ and2in1 = False
    $ and2in2 = False
    $ and2in3 = False
    $ and2in4 = False
    $ and2in5 = False
    $ and2in6 = False
    $ and2in7 = False

    $ and3in1 = False
    $ and3in2 = False
    $ and3in3 = False
    $ and3in4 = False
    $ and3in5 = False
    $ and3in6 = False
    $ and3in7 = False

    $ and4in1 = False
    $ and4in2 = False
    $ and4in3 = False
    $ and4in4 = False
    $ and4in5 = False
    $ and4in6 = False
    $ and4in7 = False

    $ and5in1 = False
    $ and5in2 = False
    $ and5in3 = False
    $ and5in4 = False
    $ and5in5 = False
    $ and5in6 = False
    $ and5in7 = False


    $ and6in1 = False
    $ and6in2 = False
    $ and6in3 = False
    $ and6in4 = False
    $ and6in5 = False
    $ and6in6 = False
    $ and6in7 = False



    #attempts for players
    $ attempts = 8
    
    call gamefile_e3



label gamefile_e3:
    #image moon = "images/blankeaeng_e3_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatese3

    if gate_name == "letterS1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other eaeng_e3_tile here
            if and1in1 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in1 = False
            if and5in1 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in1 = False
            if and6in1 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in1 = False
            #sets values for checks
            $ eae3and1x = 1115
            $ eae3and1y = 340
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in2 = False
            if and5in2 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in2 = False
            if and6in2 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in2 = False

            #sets check values
            $ eae3and1x = 1415
            $ eae3and1y = 340
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in3 = False
            if and5in3 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in3 = False
            if and6in3 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in3 = False

            #sets values for the checks
            $ eae3and1x = 1040
            $ eae3and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae3and2x = 275 
               $ eae3and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in4 = False
            if and5in4 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in4 = False
            if and6in4 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in4 = False

            #sets values for the checks
            $ eae3and1x = 1190
            $ eae3and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = True
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in5 = False
            if and5in5 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in5 = False
            if and6in5 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in5 = False

            #sets values for the checks
            $ eae3and1x = 1340
            $ eae3and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = True
            $ and1in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in6 = False
            if and5in6 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in6 = False
            if and6in6 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in6 = False

            #sets values for the checks
            $ eae3and1x = 1490
            $ eae3and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = True

    if gate_name == "letterS2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in1 = False
            if and5in1 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in1 = False
            if and6in1 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in1 = False

            #sets values for checks
            $ eae3and2x = 1115
            $ eae3and2y = 340
            $ and2in1 = True
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in2 = False
            if and5in2 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in2 = False
            if and6in2 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in2 = False

            #sets check values
            $ eae3and2x = 1415
            $ eae3and2y = 340
            $ and2in1 = False
            $ and2in2 = True
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in3 = False
            if and5in3 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in3 = False
            if and6in3 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in3 = False

            #sets values for the checks
            $ eae3and2x = 1040
            $ eae3and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = True
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in4 = False
            if and5in4 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in4 = False
            if and6in4 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in4 = False

            #sets values for the checks
            $ eae3and2x = 1190
            $ eae3and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = True
            $ and2in5 = False
            $ and2in6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in5 = False
            if and5in5 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in5 = False
            if and6in5 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in5 = False

            #sets values for the checks
            $ eae3and2x = 1340
            $ eae3and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = True
            $ and2in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in6 = False
            if and5in6 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in6 = False
            if and6in6 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in6 = False

            #sets values for the checks
            $ eae3and2x = 1490
            $ eae3and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in1 = False
            if and5in1 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in1 = False
            if and6in1 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in1 = False

            #sets values for checks
            $ eae3and3x = 1115
            $ eae3and3y = 340
            $ and3in1 = True
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in2 = False
            if and5in2 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in2 = False
            if and6in2 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in2 = False

            #sets check values
            $ eae3and3x = 1415
            $ eae3and3y = 340
            $ and3in1 = False
            $ and3in2 = True
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in3 = False
            if and5in3 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in3 = False
            if and6in3 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in3 = False

            #sets values for the checks
            $ eae3and3x = 1040
            $ eae3and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = True
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in4 = False
            if and5in4 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in4 = False
            if and6in4 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in4 = False

            #sets values for the checks
            $ eae3and3x = 1190
            $ eae3and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = True
            $ and3in5 = False
            $ and3in6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in5 = False
            if and5in5 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in5 = False
            if and6in5 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in5 = False

            #sets values for the checks
            $ eae3and3x = 1340
            $ eae3and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = True
            $ and3in6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in6 = False
            if and5in6 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in6 = False
            if and6in6 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in6 = False

            #sets values for the checks
            $ eae3and3x = 1490
            $ eae3and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = True
          


    if gate_name == "letterS3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in1 = False
            if and5in1 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in1 = False
            if and6in1 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in1 = False

            #sets values for checks
            $ eae3and4x = 1115
            $ eae3and4y = 340
            $ and4in1 = True
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in2 = False
            if and5in2 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575 
               $ and5in2 = False
            if and6in2 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in2 = False

            #sets check values
            $ eae3and4x = 1415
            $ eae3and4y = 340
            $ and4in1 = False
            $ and4in2 = True
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in3 = False
            if and5in3 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in3 = False
            if and6in3 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in3 = False

            #sets values for the checks
            $ eae3and4x = 1040
            $ eae3and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = True
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae3and2x = 275 
               $ eae3and2y = 575 
               $ and2in4 = False
            if and3in4 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in4 = False
            if and5in4 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in4 = False
            if and6in4 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in4 = False

            #sets values for the checks
            $ eae3and4x = 1190
            $ eae3and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = True
            $ and4in5 = False
            $ and4in6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in5 = False
            if and5in5 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in5 = False
            if and6in5 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in5 = False

            #sets values for the checks
            $ eae3and4x = 1340
            $ eae3and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = True
            $ and4in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in6 = False
            if and5in6 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in6 = False
            if and6in6 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in6 = False

            #sets values for the checks
            $ eae3and4x = 1490
            $ eae3and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = True
           


    if gate_name == "letterS4":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in1 = False
            if and5in1 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in1 = False
            if and6in1 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in1 = False

            #sets values for checks
            $ eae3and5x = 1115
            $ eae3and5y = 340
            $ and5in1 = True
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in2 = False
            if and5in2 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in2 = False
            if and6in2 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in2 = False

            #sets check values
            $ eae3and5x = 1415
            $ eae3and5y = 340
            $ and5in1 = False
            $ and5in2 = True
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in3 = False
            if and5in3 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in3 = False
            if and6in3 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in3 = False

            #sets values for the checks
            $ eae3and5x = 1040
            $ eae3and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = True
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in4 = False
            if and5in4 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in4 = False
            if and6in4 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in4 = False

            #sets values for the checks
            $ eae3and5x = 1190
            $ eae3and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = True
            $ and5in5 = False
            $ and5in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in5 = False
            if and5in5 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in5 = False
            if and6in5 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in5 = False

            #sets values for the checks
            $ eae3and5x = 1340
            $ eae3and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = True
            $ and5in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in6 = False
            if and5in6 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in6 = False
            if and6in6 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in6 = False

            #sets values for the checks
            $ eae3and5x = 1490
            $ eae3and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = True
            
  

    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in1 = False
            if and5in1 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in1 = False
            if and6in1 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in1 = False

            #sets values for checks
            $ eae3and6x = 1115
            $ eae3and6y = 340
            $ and6in1 = True
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in2 = False
            if and5in2 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in2 = False
            if and6in2 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in2 = False

            #sets check values
            $ eae3and6x = 1415
            $ eae3and6y = 340
            $ and6in1 = False
            $ and6in2 = True
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in3 = False
            if and5in3 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in3 = False
            if and6in3 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in3 = False

            #sets values for the checks
            $ eae3and6x = 1040
            $ eae3and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = True
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in4 = False
            if and5in4 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in4 = False
            if and6in4 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in4 = False

            #sets values for the checks
            $ eae3and6x = 1190
            $ eae3and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = True
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in5 = False
            if and5in5 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in5 = False
            if and6in5 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in5 = False

            #sets values for the checks
            $ eae3and6x = 1340
            $ eae3and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = True
            $ and6in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae3and1x = 275
               $ eae3and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae3and2x = 275
               $ eae3and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae3and3x = 342
               $ eae3and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae3and4x = 275
               $ eae3and4y = 575
               $ and4in6 = False
            if and5in6 == True:
               $ eae3and5x = 275
               $ eae3and5y = 575
               $ and5in6 = False
            if and6in6 == True:
               $ eae3and6x = 410
               $ eae3and6y = 575
               $ and6in6 = False

            #sets values for the checks
            $ eae3and6x = 1490
            $ eae3and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = True


    if and5in1 == True or and1in1 == True or and2in1 == True or and4in1 == True:
        image eaeng_e3_tile42 = "leftTreegreenlong.png"
        image eaeng_e3_tile43 = "1_1_green.png"
        show eaeng_e3_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e3_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)

        
        if and3in3 == True:
            image eaeng_e3_tile44 = "leftTreegreen.png"
            image eaeng_e3_tile45 = "1_1_green.png"
            image eaeng_e3_tile46 = "solutionLine.png"
            image eaeng_e3_tile47 = "big.png"
            show eaeng_e3_tile44 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile45 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile46 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile47 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
        if and3in3 == False:
            hide eaeng_e3_tile44
            hide eaeng_e3_tile45
            hide eaeng_e3_tile46
            hide eaeng_e3_tile47
     
        if and1in3 == True or and2in3 == True or and4in3 == True or and5in3 == True or and6in3 == True:
            image eaeng_e3_tile48 = "leftTreered.png"
            image eaeng_e3_tile49 = "1_1_red.png"
            show eaeng_e3_tile48 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile49 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in3 == False:
            hide eaeng_e3_tile48
            hide eaeng_e3_tile49

        if and6in4 == True:
            image eaeng_e3_tile50 = "rightTreegreen.png"
            image eaeng_e3_tile51 = "1_1_green.png"
            image eaeng_e3_tile52 = "solutionLine.png"
            image eaeng_e3_tile53 = "sister.png"
            show eaeng_e3_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)
        if and6in4 == False:
            hide eaeng_e3_tile50
            hide eaeng_e3_tile51
            hide eaeng_e3_tile52
            hide eaeng_e3_tile53

        if and1in4 == True or and2in4 == True or and3in4 == True or and4in4 == True or and5in4 == True:
            image eaeng_e3_tile54 = "rightTreered.png"
            image eaeng_e3_tile55 = "1_1_red.png"
            show eaeng_e3_tile54 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile55 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in4 == False:
            hide eaeng_e3_tile54
            hide eaeng_e3_tile55

    if and5in1 == False and and1in1 == False and and2in1 == False and and4in1 == False:
        hide eaeng_e3_tile42
        hide eaeng_e3_tile43
        hide eaeng_e3_tile44
        hide eaeng_e3_tile45
        hide eaeng_e3_tile46
        hide eaeng_e3_tile47
        hide eaeng_e3_tile48
        hide eaeng_e3_tile49
        hide eaeng_e3_tile50
        hide eaeng_e3_tile51
        hide eaeng_e3_tile52
        hide eaeng_e3_tile53
        hide eaeng_e3_tile54
        hide eaeng_e3_tile55

    if and1in2 == True or and2in2 == True or and4in2 == True or and5in2 == True:
        image eaeng_e3_tile60 = "rightTreegreenlong.png"
        image eaeng_e3_tile61 = "1_1_green.png"
        show eaeng_e3_tile60 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e3_tile61 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

        if and4in5 == True or and1in5 == True or and2in5 == True or and5in5 == True:
            image eaeng_e3_tile62 = "leftTreegreen.png"
            image eaeng_e3_tile63 = "1_1_green.png"
            image eaeng_e3_tile64 = "solutionLine.png"
            image eaeng_e3_tile65 = "is.png"
            show eaeng_e3_tile62 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile63 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile64 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile65 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
        if and4in5 == False and and1in5 == False and and2in5 == False and and5in5 == False:
            hide eaeng_e3_tile62
            hide eaeng_e3_tile63
            hide eaeng_e3_tile64
            hide eaeng_e3_tile65

        if and3in5 == True or and6in5 == True:
            image eaeng_e3_tile66 = "leftTreered.png"
            image eaeng_e3_tile67 = "1_1_red.png"
            show eaeng_e3_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
        elif and3in5 == False and and6in5 == False:
            hide eaeng_e3_tile66
            hide eaeng_e3_tile67

        if and1in6 == True or and2in6 == True or and4in6 == True or and5in6 == True:
            image eaeng_e3_tile68 = "rightTreegreen.png"
            image eaeng_e3_tile69 = "1_1_green.png"
            image eaeng_e3_tile70 = "solutionLine.png"
            image eaeng_e3_tile71 = "watching.png"
            show eaeng_e3_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile70 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile71 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)
        if and1in6 == False and and2in6 == False and and4in6 == False and and5in6 == False:
            hide eaeng_e3_tile68
            hide eaeng_e3_tile69
            hide eaeng_e3_tile70
            hide eaeng_e3_tile71

        if and3in6 == True or and6in6 == True:
            image eaeng_e3_tile72 = "rightTreered.png"
            image eaeng_e3_tile73 = "1_1_red.png"
            show eaeng_e3_tile72 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile73 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and3in6 == False and and6in6 == False:
            hide eaeng_e3_tile72
            hide eaeng_e3_tile73
    
    if and1in2 == False and and2in2 == False and and4in2 == False and and5in2 == False:
        hide eaeng_e3_tile60
        hide eaeng_e3_tile61
        hide eaeng_e3_tile62
        hide eaeng_e3_tile63
        hide eaeng_e3_tile64
        hide eaeng_e3_tile65
        hide eaeng_e3_tile66
        hide eaeng_e3_tile67
        hide eaeng_e3_tile68
        hide eaeng_e3_tile69
        hide eaeng_e3_tile70
        hide eaeng_e3_tile71
        hide eaeng_e3_tile72
        hide eaeng_e3_tile73

    
    if and3in1 == True or and6in1 == True:
         image eaeng_e3_tile74 = "leftTreeredlong.png"
         image eaeng_e3_tile75 = "1_1_red.png"
         show eaeng_e3_tile74 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e3_tile75 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    elif and3in1 == False and and6in1 == False:
         hide eaeng_e3_tile74
         hide eaeng_e3_tile75

    if and3in2 == True or and6in2 == True:
         image eaeng_e3_tile76 = "rightTreeredlong.png"
         image eaeng_e3_tile77 = "1_1_red.png"
         show eaeng_e3_tile76 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e3_tile77 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and3in2 == False and and6in2 == False:
         hide eaeng_e3_tile76
         hide eaeng_e3_tile77

    #win conditions
    if (and5in1 == True or and1in1 == True or and2in1 == True or and4in1 == True) and and3in3 == True and and6in4 == True and (and1in2 == True or and2in2 == True or and4in2 == True or and5in2 == True) and (and4in5 == True or and1in5 == True or and2in5 == True or and5in5 == True) and (and1in6 == True or and2in6 == True or and4in6 == True or and5in6 == True):

        image eaeng_e3_tile202 = "letterS.png"
        image eaeng_e3_tile206 = "letterS.png"
        image eaeng_e3_tile203 = "letterM.png"
        image eaeng_e3_tile205 = "letterS.png"
        image eaeng_e3_tile201 = "letterS.png"
        image eaeng_e3_tile204 = "letterJ.png"
        
        show eaeng_e3_tile202 at Position(xpos = eae3and1x, xanchor = 0, ypos = eae3and1y, yanchor = 0)
        show eaeng_e3_tile206 at Position(xpos = eae3and2x, xanchor = 0, ypos = eae3and2y, yanchor = 0)
        show eaeng_e3_tile203 at Position(xpos = eae3and3x, xanchor = 0, ypos = eae3and3y, yanchor = 0)
        show eaeng_e3_tile205 at Position(xpos = eae3and4x, xanchor = 0, ypos = eae3and4y, yanchor = 0)
        show eaeng_e3_tile201 at Position(xpos = eae3and5x, xanchor = 0, ypos = eae3and5y, yanchor = 0)
        show eaeng_e3_tile204 at Position(xpos = eae3and6x, xanchor = 0, ypos = eae3and6y, yanchor = 0)

        "Access Gained"

        jump hiroseDoorPassed
    if slot_name == "null":
        $attempts +=1

    $attempts -=1
    if attempts ==0:
        hide eaeng_e3_tile42
        hide eaeng_e3_tile43
        hide eaeng_e3_tile44
        hide eaeng_e3_tile45
        hide eaeng_e3_tile46
        hide eaeng_e3_tile47
        hide eaeng_e3_tile48
        hide eaeng_e3_tile49
        hide eaeng_e3_tile50
        hide eaeng_e3_tile51
        hide eaeng_e3_tile52
        hide eaeng_e3_tile53
        hide eaeng_e3_tile54
        hide eaeng_e3_tile55
        hide eaeng_e3_tile56
        hide eaeng_e3_tile61
        hide eaeng_e3_tile62
        hide eaeng_e3_tile63
        hide eaeng_e3_tile64
        hide eaeng_e3_tile65
        hide eaeng_e3_tile66
        hide eaeng_e3_tile67
        hide eaeng_e3_tile68
        hide eaeng_e3_tile69
        hide eaeng_e3_tile70
        hide eaeng_e3_tile71
        hide eaeng_e3_tile72
        hide eaeng_e3_tile73
        hide eaeng_e3_tile74
        hide eaeng_e3_tile75
        hide eaeng_e3_tile76
        hide eaeng_e3_tile77

        "You Lose Try Again"

        jump chooseEasyGram     
    
    jump gamefile_e3