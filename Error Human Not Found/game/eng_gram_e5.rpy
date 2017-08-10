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

screen logicGatese5:
    key 'h' action Hide("")
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 260
        ypos 200
        focus_mask True
        action Jump("gramEasyHints5")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 178
        ypos 285
    text "Attempts" xpos 185 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 358 ypos 294 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 380 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27
    draggroup:
        #and gates
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae5and1x ypos eae5and1y
        drag:
                drag_name "letterI"
                child "letterI.png"
                droppable False
                dragged gate_dragged
                xpos eae5and2x ypos eae5and2y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae5and3x ypos eae5and3y
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae5and4x ypos eae5and4y
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos eae5and5x ypos eae5and5y
        drag:
                drag_name "letterG"
                child "letterG.png"
                droppable False
                dragged gate_dragged
                xpos eae5and6x ypos eae5and6y
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

label eng_gram_e5:

    scene bg Eng_Tile
    $ quick_menu = False
    $ game_menu = True

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image eaeng_e5_tile0 = "instructions5.png"
    image eaeng_e5_tile1 = "1_1_green.png"
    image eaeng_e5_tile2 = "letterS.png"
    show eaeng_e5_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_e5_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_e5_tile2 at Position(xpos = 1265, xanchor = 0, ypos = 167, yanchor = 0)
    
    #row2 5-8

    image eaeng_e5_tile5 = "leftTreelong.png"
    image eaeng_e5_tile6 = "rightTreelong.png"

    show eaeng_e5_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_e5_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_e5_tile9 = "1_1_grey.png"
    image eaeng_e5_tile10 = "1_1_grey.png"
    

    show eaeng_e5_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_e5_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_e5_tile14 = "leftTree.png"
    image eaeng_e5_tile15 = "rightTree.png"
    image eaeng_e5_tile16 = "leftTree.png"
    image eaeng_e5_tile17 = "rightTree.png"

    show eaeng_e5_tile14 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e5_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e5_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e5_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_e5_tile21 = "1_1_grey.png"
    image eaeng_e5_tile22 = "1_1_grey.png"
    image eaeng_e5_tile23 = "1_1_grey.png"
    image eaeng_e5_tile24 = "1_1_grey.png"

    show eaeng_e5_tile21 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e5_tile22 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e5_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e5_tile24 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)

    image eaeng_e5_tile31 = "letterBorder.png"
    image eaeng_e5_tile32 = "letterBorder.png"
    image eaeng_e5_tile33 = "letterBorder.png"
    image eaeng_e5_tile34 = "letterBorder.png"
    image eaeng_e5_tile35 = "letterBorder.png"
    image eaeng_e5_tile36 = "letterBorder.png"
    show eaeng_e5_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e5_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e5_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_e5_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e5_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e5_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ eae5and1x = 275 
    $ eae5and1y = 575
    $ eae5and2x = 410
    $ eae5and2y = 575
    $ eae5and3x = 342 
    $ eae5and3y = 660
    $ eae5and4x = 275
    $ eae5and4y = 750
    $ eae5and5x = 410
    $ eae5and5y = 750
    $ eae5and6x = 342 
    $ eae5and6y = 832
    
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
    
    call gamefile_e5



label gamefile_e5:
    #image moon = "images/blankeaeng_e5_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatese5

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other eaeng_e5_tile here
            if and1in1 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in1 = False
            #sets values for checks
            $ eae5and1x = 1115
            $ eae5and1y = 340
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae5and1x = 1415
            $ eae5and1y = 340
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae5and1x = 1040
            $ eae5and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae5and1x = 1190
            $ eae5and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = True
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae5and1x = 1340
            $ eae5and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = True
            $ and1in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae5and1x = 1490
            $ eae5and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = True

    if gate_name == "letterI":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae5and2x = 1115
            $ eae5and2y = 340
            $ and2in1 = True
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae5and2x = 1415
            $ eae5and2y = 340
            $ and2in1 = False
            $ and2in2 = True
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae5and2x = 1040
            $ eae5and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = True
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae5and2x = 1190
            $ eae5and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = True
            $ and2in5 = False
            $ and2in6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae5and2x = 1340
            $ eae5and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = True
            $ and2in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae5and2x = 1490
            $ eae5and2y = 515
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
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae5and3x = 1115
            $ eae5and3y = 340
            $ and3in1 = True
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae5and3x = 1415
            $ eae5and3y = 340
            $ and3in1 = False
            $ and3in2 = True
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae5and3x = 1040
            $ eae5and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = True
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae5and3x = 1190
            $ eae5and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = True
            $ and3in5 = False
            $ and3in6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae5and3x = 1340
            $ eae5and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = True
            $ and3in6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae5and3x = 1490
            $ eae5and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = True
          


    if gate_name == "letterP":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae5and4x = 1115
            $ eae5and4y = 340
            $ and4in1 = True
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae5and4x = 1415
            $ eae5and4y = 340
            $ and4in1 = False
            $ and4in2 = True
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae5and4x = 1040
            $ eae5and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = True
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae5and4x = 1190
            $ eae5and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = True
            $ and4in5 = False
            $ and4in6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae5and4x = 1340
            $ eae5and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = True
            $ and4in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae5and4x = 1490
            $ eae5and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = True
           


    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae5and5x = 1115
            $ eae5and5y = 340
            $ and5in1 = True
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae5and5x = 1415
            $ eae5and5y = 340
            $ and5in1 = False
            $ and5in2 = True
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae5and5x = 1040
            $ eae5and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = True
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae5and5x = 1190
            $ eae5and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = True
            $ and5in5 = False
            $ and5in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae5and5x = 1340
            $ eae5and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = True
            $ and5in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae5and5x = 1490
            $ eae5and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = True
            
  

    if gate_name == "letterG":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae5and6x = 1115
            $ eae5and6y = 340
            $ and6in1 = True
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae5and6x = 1415
            $ eae5and6y = 340
            $ and6in1 = False
            $ and6in2 = True
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae5and6x = 1040
            $ eae5and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = True
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae5and6x = 1190
            $ eae5and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = True
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae5and6x = 1340
            $ eae5and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = True
            $ and6in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae5and1x = 275
               $ eae5and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae5and2x = 410
               $ eae5and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae5and3x = 342
               $ eae5and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae5and4x = 275
               $ eae5and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae5and5x = 410
               $ eae5and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae5and6x = 342
               $ eae5and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae5and6x = 1490
            $ eae5and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = True

    play sound gramTree2
    if and5in1 == True and  and1in2 == True:
        image eaeng_e5_tile42 = "leftTreegreenlong.png"
        image eaeng_e5_tile43 = "1_1_green.png"
        image eaeng_e5_tile44 = "rightTreegreenlong.png"
        image eaeng_e5_tile45 = "1_1_green.png"
        show eaeng_e5_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e5_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        if (gramRow1_sound ==0):
            $gramRow1_sound +=1
            play sound gramTree1
        show eaeng_e5_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e5_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        
        if and3in3 == True and and6in4 == True:
            image eaeng_e5_tile46 = "leftTreegreen.png"
            image eaeng_e5_tile47 = "1_1_green.png"
            image eaeng_e5_tile48 = "solutionLine.png"
            image eaeng_e5_tile49 = "its.png"
            image eaeng_e5_tile50 = "rightTreegreen.png"
            image eaeng_e5_tile51 = "1_1_green.png"
            image eaeng_e5_tile52 = "solutionLine.png"
            image eaeng_e5_tile53 = "a.png"

            show eaeng_e5_tile46 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile47 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile48 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile49 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            if ((gramRow2_soundA ==0) and (gramRow2_soundB==0)) or ((gramRow2_soundA==0) and (gramRow2_soundB==1)):
                play sound gramText1
                $gramRow2_soundA +=1
            show eaeng_e5_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)

        if and3in3 == False or and6in4 == False:
            hide eaeng_e5_tile46
            hide eaeng_e5_tile47
            hide eaeng_e5_tile48
            hide eaeng_e5_tile49
            hide eaeng_e5_tile50
            hide eaeng_e5_tile51
            hide eaeng_e5_tile52
            hide eaeng_e5_tile53

     
        if (and1in3 == True or and2in3 == True or and4in3 == True or and5in3 == True or and6in3 == True) and (and1in4 == True or and2in4 == True or and3in4 == True or and4in4 == True or and5in4 == True):
            image eaeng_e5_tile54 = "leftTreered.png"
            image eaeng_e5_tile55 = "1_1_red.png"
            image eaeng_e5_tile56 = "rightTreered.png"
            image eaeng_e5_tile57 = "1_1_red.png"
            show eaeng_e5_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            if((gramRow2_soundA==0)and(gramRow2_soundB==0)):
                play sound gramTree5
            if((gramRow2_soundA==0)and(gramRow2_soundB==1)):
                play sound gramTree5
        elif and1in3 == False or and1in4 == False:
            hide eaeng_e5_tile54
            hide eaeng_e5_tile55
            hide eaeng_e5_tile56
            hide eaeng_e5_tile57

        if and4in5 == True and and2in6 == True:
            image eaeng_e5_tile58 = "leftTreegreen.png"
            image eaeng_e5_tile59 = "1_1_green.png"
            image eaeng_e5_tile60 = "solutionLine.png"
            image eaeng_e5_tile61 = "small.png"
            image eaeng_e5_tile62 = "rightTreegreen.png"
            image eaeng_e5_tile63 = "1_1_green.png"
            image eaeng_e5_tile64 = "solutionLine.png"
            image eaeng_e5_tile65 = "world.png"
            if ((gramRow2_soundA ==0) and (gramRow2_soundB==0)) or ((gramRow2_soundA ==1) and (gramRow2_soundB==0)):
                play sound gramText1
                $gramRow2_soundB +=1
            show eaeng_e5_tile58 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile59 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile60 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile61 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e5_tile62 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile63 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile64 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile65 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)
        if and4in5 == False or and2in6 == False:
            hide eaeng_e5_tile58
            hide eaeng_e5_tile59
            hide eaeng_e5_tile60
            hide eaeng_e5_tile61
            hide eaeng_e5_tile62
            hide eaeng_e5_tile63
            hide eaeng_e5_tile64
            hide eaeng_e5_tile65

        if (and1in5 == True or and2in5 == True or and3in5 == True or and5in5 == True or and6in5 == True) and (and1in6 == True or and3in6 == True or and4in6 == True or and5in6 == True or and6in6 == True):
            image eaeng_e5_tile66 = "leftTreered.png"
            image eaeng_e5_tile67 = "1_1_red.png"
            image eaeng_e5_tile68 = "rightTreered.png"
            image eaeng_e5_tile69 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e5_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in5 == False or and1in6 == False:
            hide eaeng_e5_tile66
            hide eaeng_e5_tile67
            hide eaeng_e5_tile68
            hide eaeng_e5_tile69


        if and3in3 == True and (and1in4 == True or and2in4 == True or and4in4 == True or and5in4 == True) or and6in4 == True and (and1in3 == True or and2in3 == True or and4in3 == True or and3in4 == True):
            image eaeng_e5_tile70 = "leftTreered.png"
            image eaeng_e5_tile71 = "1_1_red.png"
            image eaeng_e5_tile72 = "rightTreered.png"
            image eaeng_e5_tile73 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==0) and (gramRow2_soundB==1):
                play sound gramTree5
            show eaeng_e5_tile70 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile71 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile72 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile73 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)

        elif and1in3 == False or and1in4 == False:
            hide eaeng_e5_tile70
            hide eaeng_e5_tile71
            hide eaeng_e5_tile72
            hide eaeng_e5_tile73

        if and4in5 == True and (and1in6 == True or and3in6 == True or and5in6 == True or and6in6 == True) or and2in6 == True and (and1in5 == True or and2in5 == True or and3in5 == True or and5in5 == True or and6in5 == True):
            image eaeng_e5_tile74 = "leftTreered.png"
            image eaeng_e5_tile75 = "1_1_red.png"
            image eaeng_e5_tile76 = "rightTreered.png"
            image eaeng_e5_tile77 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e5_tile74 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile75 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile76 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile77 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in4 == False or and1in4 == False:
            hide eaeng_e5_tile74
            hide eaeng_e5_tile75
            hide eaeng_e5_tile76
            hide eaeng_e5_tile77



    if and5in1 == False or and1in2 == False:
        hide eaeng_e5_tile42
        hide eaeng_e5_tile43
        hide eaeng_e5_tile44
        hide eaeng_e5_tile45
        hide eaeng_e5_tile46
        hide eaeng_e5_tile47
        hide eaeng_e5_tile48
        hide eaeng_e5_tile49
        hide eaeng_e5_tile50
        hide eaeng_e5_tile51
        hide eaeng_e5_tile52
        hide eaeng_e5_tile53
        hide eaeng_e5_tile54
        hide eaeng_e5_tile55
        hide eaeng_e5_tile56
        hide eaeng_e5_tile57
        hide eaeng_e5_tile58
        hide eaeng_e5_tile59
        hide eaeng_e5_tile60
        hide eaeng_e5_tile61
        hide eaeng_e5_tile62
        hide eaeng_e5_tile63
        hide eaeng_e5_tile64
        hide eaeng_e5_tile65
        hide eaeng_e5_tile66
        hide eaeng_e5_tile67
        hide eaeng_e5_tile68
        hide eaeng_e5_tile69
        hide eaeng_e5_tile70
        hide eaeng_e5_tile71
        hide eaeng_e5_tile72
        hide eaeng_e5_tile73
        hide eaeng_e5_tile74
        hide eaeng_e5_tile75
        hide eaeng_e5_tile76
        hide eaeng_e5_tile77


    
    if (and1in1 == True or and2in1 == True or and3in1 == True or and4in1 == True or and6in1 == True) and (and2in2 == True or and3in2 == True or and4in2 == True or and5in2 == True or and6in2 == True):
         image eaeng_e5_tile78 = "leftTreeredlong.png"
         image eaeng_e5_tile79 = "1_1_red.png"
         image eaeng_e5_tile80 = "rightTreeredlong.png"
         image eaeng_e5_tile81 = "1_1_red.png"
         if(gramRow1_sound==0):
             play sound gramTree5
         show eaeng_e5_tile78 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e5_tile79 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         #play sound gramTree4
         show eaeng_e5_tile80 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e5_tile81 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and1in1 == False or and2in2 == False:
         hide eaeng_e5_tile78
         hide eaeng_e5_tile79
         hide eaeng_e5_tile80
         hide eaeng_e5_tile81

    if and5in1 == True and (and2in2 == True or and3in2 == True or and4in2 == True or and6in2 == True) or and1in2 == True and (and2in1 == True or and3in1 == True or and4in1 == True or and6in1 == True):
         image eaeng_e5_tile82 = "leftTreeredlong.png"
         image eaeng_e5_tile83 = "1_1_red.png"
         image eaeng_e5_tile84 = "rightTreeredlong.png"
         image eaeng_e5_tile85 = "1_1_red.png"
         if(gramRow1_sound==0):
             play sound gramTree5
         show eaeng_e5_tile82 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e5_tile83 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e5_tile84 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e5_tile85 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and1in1 == False or and2in2 == False:
         hide eaeng_e5_tile82
         hide eaeng_e5_tile83
         hide eaeng_e5_tile84
         hide eaeng_e5_tile85

    #win conditions
    if and5in1 == True and and3in3 == True and and6in4 == True and and1in2 == True and and4in5 == True and and2in6 == True: 
        image eaeng_e5_tile202 = "letterK.png"
        image eaeng_e5_tile206 = "letterI.png"
        image eaeng_e5_tile203 = "letterM.png"
        image eaeng_e5_tile205 = "letterP.png"
        image eaeng_e5_tile201 = "letterJ.png"
        image eaeng_e5_tile204 = "letterG.png"
        
        show eaeng_e5_tile202 at Position(xpos = eae5and1x, xanchor = 0, ypos = eae5and1y, yanchor = 0)
        show eaeng_e5_tile206 at Position(xpos = eae5and2x, xanchor = 0, ypos = eae5and2y, yanchor = 0)
        show eaeng_e5_tile203 at Position(xpos = eae5and3x, xanchor = 0, ypos = eae5and3y, yanchor = 0)
        show eaeng_e5_tile205 at Position(xpos = eae5and4x, xanchor = 0, ypos = eae5and4y, yanchor = 0)
        show eaeng_e5_tile201 at Position(xpos = eae5and5x, xanchor = 0, ypos = eae5and5y, yanchor = 0)
        show eaeng_e5_tile204 at Position(xpos = eae5and6x, xanchor = 0, ypos = eae5and6y, yanchor = 0)
        queue sound gramWin
        $ renpy.pause(1.0)
        jump gramEasyDone
    if slot_name == "null":
        $attempts +=1

    if temp_slot == "" and temp_gate == "" and slot_name != "null":
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        $ attempts -=1
    else:
       if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
           $ attempts -=1
           $ temp_slot = slot_name
           $ temp_gate = gate_name
    $ temp_slot = ""
    $ temp_gate = ""  
    if attempts ==0:
        queue sound gramLose
        show eaeng_e5_tile202 at Position(xpos = eae5and1x, xanchor = 0, ypos = eae5and1y, yanchor = 0)
        show eaeng_e5_tile206 at Position(xpos = eae5and2x, xanchor = 0, ypos = eae5and2y, yanchor = 0)
        show eaeng_e5_tile203 at Position(xpos = eae5and3x, xanchor = 0, ypos = eae5and3y, yanchor = 0)
        show eaeng_e5_tile205 at Position(xpos = eae5and4x, xanchor = 0, ypos = eae5and4y, yanchor = 0)
        show eaeng_e5_tile201 at Position(xpos = eae5and5x, xanchor = 0, ypos = eae5and5y, yanchor = 0)
        show eaeng_e5_tile204 at Position(xpos = eae5and6x, xanchor = 0, ypos = eae5and6y, yanchor = 0)
        $ renpy.pause(1.0)
        hide eaeng_e5_tile42
        hide eaeng_e5_tile43
        hide eaeng_e5_tile44
        hide eaeng_e5_tile45
        hide eaeng_e5_tile46
        hide eaeng_e5_tile47
        hide eaeng_e5_tile48
        hide eaeng_e5_tile49
        hide eaeng_e5_tile50
        hide eaeng_e5_tile51
        hide eaeng_e5_tile52
        hide eaeng_e5_tile53
        hide eaeng_e5_tile54
        hide eaeng_e5_tile55
        hide eaeng_e5_tile56
        hide eaeng_e5_tile61
        hide eaeng_e5_tile62
        hide eaeng_e5_tile63
        hide eaeng_e5_tile64
        hide eaeng_e5_tile65
        hide eaeng_e5_tile66
        hide eaeng_e5_tile67
        hide eaeng_e5_tile68
        hide eaeng_e5_tile69
        hide eaeng_e5_tile70
        hide eaeng_e5_tile71
        hide eaeng_e5_tile72
        hide eaeng_e5_tile73
        hide eaeng_e5_tile74
        hide eaeng_e5_tile75
        hide eaeng_e5_tile76
        hide eaeng_e5_tile77
        $ attemptsLogicGate1 +=1
        jump gramEasyLose
          
    
    jump gamefile_e5