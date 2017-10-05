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

screen logicGates_med1:
    key 'h'action NullAction()# action Hide("")
    key 'K_PAGEUP' action NullAction()# action Hide("")
    key 'repeat_K_PAGEUP' action NullAction()# action Hide("")
    key 'K_AC_BACK' action NullAction()#action Hide("")
    key 'mousedown_4'action NullAction()# action Hide("")
    key 'K_LCTRL' action NullAction()# action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 260
        ypos 200
        focus_mask True
        action Jump("hints_gramMed1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 178
        ypos 285
    text "Moves" xpos 185 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 325 ypos 294 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 380 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27
    draggroup:
        #and gates
        drag:
                drag_name "letterT1"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT1x ypos letterT1y
        drag:
                drag_name "letterR2"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterR2x ypos letterR2y
        drag:
                drag_name "letterB1"
                child "letterB.png"
                droppable False
                dragged gate_dragged
                xpos letterB3x ypos letterB3y
        drag:
                drag_name "letterB2"
                child "letterB.png"
                droppable False
                dragged gate_dragged
                xpos letterB4x ypos letterB4y
        drag:
                drag_name "letterT2"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT5x ypos letterT5y
        drag:
                drag_name "letterR1"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterR6x ypos letterR6y
        drag:
                drag_name "letterT3"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT7x ypos letterT7y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 1115 ypos 360
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1415 ypos 355
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 1040 ypos 530
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 1190 ypos 530
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1340 ypos 530
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1490 ypos 530
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 1260 ypos 282

init:
    image bg Eng_gram_m1_tile = "eng_tile_bg.png"

<<<<<<< HEAD
label gram_m1: #start:

=======
label gram_m1:
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
>>>>>>> 436351a011be9347feffac38add90907369680d5
    scene bg Eng_gram_m1_tile

    #row1 1-4
    image gram_m1_tile0 = "instructions6.png"
    image gram_m1_tile1 = "1_1_green.png"
    image gram_m1_tile2 = "letterS.png"
    image gram_m1_tile3 = "treeGrey.png"
    show gram_m1_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_m1_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 130, yanchor = 0)
    show gram_m1_tile2 at Position(xpos = 1260, xanchor = 0, ypos = 145, yanchor = 0)
    show gram_m1_tile3 at Position(xpos = 1248, xanchor = 0, ypos = 228, yanchor = 0)
    
    #row2 5-8
    image gram_m1_tile4 = "1_1_grey.png"
    image gram_m1_tile5 = "leftTreelong.png"
    image gram_m1_tile6 = "rightTreelong.png"
    show gram_m1_tile4 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)
    show gram_m1_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 370, yanchor = 0)
    show gram_m1_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 370, yanchor = 0)
    
    #row3 9-13   

    image gram_m1_tile9 = "1_1_grey.png"
    image gram_m1_tile10 = "1_1_grey.png"
    

    show gram_m1_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 345, yanchor = 0)
    show gram_m1_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 345, yanchor = 0)

    #row4 14-20

    image gram_m1_tile14 = "leftTree.png"
    image gram_m1_tile15 = "rightTree.png"
    image gram_m1_tile16 = "leftTree.png"
    image gram_m1_tile17 = "rightTree.png"

    show gram_m1_tile14 at Position(xpos = 1070, xanchor = 0, ypos = 445, yanchor = 0)
    show gram_m1_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 445, yanchor = 0)
    show gram_m1_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 445, yanchor = 0)
    show gram_m1_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 445, yanchor = 0)


    #row5 21-27

    image gram_m1_tile21 = "1_1_grey.png"
    image gram_m1_tile22 = "1_1_grey.png"
    image gram_m1_tile23 = "1_1_grey.png"
    image gram_m1_tile24 = "1_1_grey.png"

    show gram_m1_tile21 at Position(xpos = 1025, xanchor = 0, ypos = 520, yanchor = 0)
    show gram_m1_tile22 at Position(xpos = 1175, xanchor = 0, ypos = 520, yanchor = 0)
    show gram_m1_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 520, yanchor = 0)
    show gram_m1_tile24 at Position(xpos = 1475, xanchor = 0, ypos = 520, yanchor = 0)

    image gram_m1_tile31 = "letterBorder.png"
    image gram_m1_tile32 = "letterBorder.png"
    image gram_m1_tile33 = "letterBorder.png"
    #image gram_m1_tile34 = "letterBorder.png"
    #image gram_m1_tile35 = "letterBorder.png"
    #image gram_m1_tile36 = "letterBorder.png"
    show gram_m1_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m1_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m1_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    #show gram_m1_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    #show gram_m1_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    #show gram_m1_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ letterT1x = 275 
    $ letterT1y = 575
    $ letterR2x = 410
    $ letterR2y = 575
    $ letterB3x = 342 
    $ letterB3y = 660
    $ letterB4x = 342
    $ letterB4y = 660
    $ letterT5x = 275
    $ letterT5y = 575
    $ letterR6x = 410 
    $ letterR6y = 575
    $ letterT7x = 275 
    $ letterT7y = 575

    # check conditons for locations
    $ letterT1in1 = False
    $ letterT1in2 = False
    $ letterT1in3 = False
    $ letterT1in4 = False
    $ letterT1in5 = False
    $ letterT1in6 = False
    $ letterT1in7 = False

    $ letterR2in1 = False
    $ letterR2in2 = False
    $ letterR2in3 = False
    $ letterR2in4 = False
    $ letterR2in5 = False
    $ letterR2in6 = False
    $ letterR2in7 = False

    $ letterB3in1 = False
    $ letterB3in2 = False
    $ letterB3in3 = False
    $ letterB3in4 = False
    $ letterB3in5 = False
    $ letterB3in6 = False
    $ letterB3in7 = False

    $ letterB4in1 = False
    $ letterB4in2 = False
    $ letterB4in3 = False
    $ letterB4in4 = False
    $ letterB4in5 = False
    $ letterB4in6 = False
    $ letterB4in7 = False

    $ letterT5in1 = False
    $ letterT5in2 = False
    $ letterT5in3 = False
    $ letterT5in4 = False
    $ letterT5in5 = False
    $ letterT5in6 = False
    $ letterT5in7 = False


    $ letterR6in1 = False
    $ letterR6in2 = False
    $ letterR6in3 = False
    $ letterR6in4 = False
    $ letterR6in5 = False
    $ letterR6in6 = False
    $ letterR6in7 = False


    $ letterT7in1 = False
    $ letterT7in2 = False
    $ letterT7in3 = False
    $ letterT7in4 = False
    $ letterT7in5 = False
    $ letterT7in6 = False
    $ letterT7in7 = False

    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""


    #attempts for players
    $ attempts = 15
    
    call gamefile_m1



label gamefile_m1:
    #image moon = "images/blankgram_m1_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGates_med1

    if gate_name == "letterT1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m1_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False
            #sets values for checks
            $ letterT1x = 1115
            $ letterT1y = 362
            $ letterT1in1 = True
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in2 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in2 = False

            #sets check values
            $ letterT1x = 1415
            $ letterT1y = 360
            $ letterT1in1 = False
            $ letterT1in2 = True
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in3 = False
            if letterT7in3 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in3 = False

            #sets values for the checks
            $ letterT1x = 1040
            $ letterT1y = 535
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = True
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in4 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in4 = False

            #sets values for the checks
            $ letterT1x = 1190
            $ letterT1y = 535
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = True
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in5 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in5 = False

            #sets values for the checks
            $ letterT1x = 1340
            $ letterT1y = 535
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = True
            $ letterT1in6 = False
            $ letterT1in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in6 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in6 = False

            #sets values for the checks
            $ letterT1x = 1490
            $ letterT1y = 535
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = True
            $ letterT1in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterT1x = 1260
            $ letterT1y = 284
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = True

    if gate_name == "letterR2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for checks
            $ letterR2x = 1115
            $ letterR2y = 362
            $ letterR2in1 = True
            $ letterR2in2 = False
            $ letterR2in3 = False
            $ letterR2in4 = False
            $ letterR2in5 = False
            $ letterR2in6 = False
            $ letterR2in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in2 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in2 = False

            #sets check values
            $ letterR2x = 1415
            $ letterR2y = 360
            $ letterR2in1 = False
            $ letterR2in2 = True
            $ letterR2in3 = False
            $ letterR2in4 = False
            $ letterR2in5 = False
            $ letterR2in6 = False
            $ letterR2in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in3 = False
            if letterT7in3 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in3 = False

            #sets values for the checks
            $ letterR2x = 1040
            $ letterR2y = 535
            $ letterR2in1 = False
            $ letterR2in2 = False
            $ letterR2in3 = True
            $ letterR2in4 = False
            $ letterR2in5 = False
            $ letterR2in6 = False
            $ letterR2in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in4 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in4 = False

            #sets values for the checks
            $ letterR2x = 1190
            $ letterR2y = 535
            $ letterR2in1 = False
            $ letterR2in2 = False
            $ letterR2in3 = False
            $ letterR2in4 = True
            $ letterR2in5 = False
            $ letterR2in6 = False
            $ letterR2in7 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in5 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in5 = False

            #sets values for the checks
            $ letterR2x = 1340
            $ letterR2y = 535
            $ letterR2in1 = False
            $ letterR2in2 = False
            $ letterR2in3 = False
            $ letterR2in4 = False
            $ letterR2in5 = True
            $ letterR2in6 = False
            $ letterR2in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in6 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in6 = False

            #sets values for the checks
            $ letterR2x = 1490
            $ letterR2y = 535
            $ letterR2in1 = False
            $ letterR2in2 = False
            $ letterR2in3 = False
            $ letterR2in4 = False
            $ letterR2in5 = False
            $ letterR2in6 = True
            $ letterR2in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in7 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterR2x = 1260
            $ letterR2y = 284
            $ letterR2in1 = False
            $ letterR2in2 = False
            $ letterR2in3 = False
            $ letterR2in4 = False
            $ letterR2in5 = False
            $ letterR2in6 = False
            $ letterR2in7 = True

    if gate_name == "letterB1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for checks
            $ letterB3x = 1115
            $ letterB3y = 362
            $ letterB3in1 = True
            $ letterB3in2 = False
            $ letterB3in3 = False
            $ letterB3in4 = False
            $ letterB3in5 = False
            $ letterB3in6 = False
            $ letterB3in7 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets check values
            $ letterB3x = 1415
            $ letterB3y = 360
            $ letterB3in1 = False
            $ letterB3in2 = True
            $ letterB3in3 = False
            $ letterB3in4 = False
            $ letterB3in5 = False
            $ letterB3in6 = False
            $ letterB3in7 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in3 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB3x = 1040
            $ letterB3y = 535
            $ letterB3in1 = False
            $ letterB3in2 = False
            $ letterB3in3 = True
            $ letterB3in4 = False
            $ letterB3in5 = False
            $ letterB3in6 = False
            $ letterB3in7 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB3x = 1190
            $ letterB3y = 535
            $ letterB3in1 = False
            $ letterB3in2 = False
            $ letterB3in3 = False
            $ letterB3in4 = True
            $ letterB3in5 = False
            $ letterB3in6 = False
            $ letterB3in7 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB3x = 1340
            $ letterB3y = 535
            $ letterB3in1 = False
            $ letterB3in2 = False
            $ letterB3in3 = False
            $ letterB3in4 = False
            $ letterB3in5 = True
            $ letterB3in6 = False
            $ letterB3in7 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB3x = 1490
            $ letterB3y = 535
            $ letterB3in1 = False
            $ letterB3in2 = False
            $ letterB3in3 = False
            $ letterB3in4 = False
            $ letterB3in5 = False
            $ letterB3in6 = True
            $ letterB3in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in7 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterB3x = 1260
            $ letterB3y = 284
            $ letterB3in1 = False
            $ letterB3in2 = False
            $ letterB3in3 = False
            $ letterB3in4 = False
            $ letterB3in5 = False
            $ letterB3in6 = False
            $ letterB3in7 = True
          


    if gate_name == "letterB2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for checks
            $ letterB4x = 1115
            $ letterB4y = 362
            $ letterB4in1 = True
            $ letterB4in2 = False
            $ letterB4in3 = False
            $ letterB4in4 = False
            $ letterB4in5 = False
            $ letterB4in6 = False
            $ letterB4in7 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets check values
            $ letterB4x = 1415
            $ letterB4y = 360
            $ letterB4in1 = False
            $ letterB4in2 = True
            $ letterB4in3 = False
            $ letterB4in4 = False
            $ letterB4in5 = False
            $ letterB4in6 = False
            $ letterB4in7 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in3 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB4x = 1040
            $ letterB4y = 535
            $ letterB4in1 = False
            $ letterB4in2 = False
            $ letterB4in3 = True
            $ letterB4in4 = False
            $ letterB4in5 = False
            $ letterB4in6 = False
            $ letterB4in7 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB4x = 1190
            $ letterB4y = 535
            $ letterB4in1 = False
            $ letterB4in2 = False
            $ letterB4in3 = False
            $ letterB4in4 = True
            $ letterB4in5 = False
            $ letterB4in6 = False
            $ letterB4in7 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB4x = 1340
            $ letterB4y = 535
            $ letterB4in1 = False
            $ letterB4in2 = False
            $ letterB4in3 = False
            $ letterB4in4 = False
            $ letterB4in5 = True
            $ letterB4in6 = False
            $ letterB4in7 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterB4x = 1490
            $ letterB4y = 535
            $ letterB4in1 = False
            $ letterB4in2 = False
            $ letterB4in3 = False
            $ letterB4in4 = False
            $ letterB4in5 = False
            $ letterB4in6 = True
            $ letterB4in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in7 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterB4x = 1260
            $ letterB4y = 284
            $ letterB4in1 = False
            $ letterB4in2 = False
            $ letterB4in3 = False
            $ letterB4in4 = False
            $ letterB4in5 = False
            $ letterB4in6 = False
            $ letterB4in7 = True
           


    if gate_name == "letterT2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for checks
            $ letterT5x = 1115
            $ letterT5y = 362
            $ letterT5in1 = True
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets check values
            $ letterT5x = 1415
            $ letterT5y = 360
            $ letterT5in1 = False
            $ letterT5in2 = True
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT5x = 1040
            $ letterT5y = 535
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = True
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT5x = 1190
            $ letterT5y = 535
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = True
            $ letterT5in5 = False
            $ letterT5in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT5x = 1340
            $ letterT5y = 535
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = True
            $ letterT5in6 = False
            $ letterT5in7 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT5x = 1490
            $ letterT5y = 535
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = True
            $ letterT5in7 = False
            
                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in7 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterT5x = 1260
            $ letterT5y = 284
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = True
  

    if gate_name == "letterR1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for checks
            $ letterR6x = 1115
            $ letterR6y = 362
            $ letterR6in1 = True
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets check values
            $ letterR6x = 1415
            $ letterR6y = 360
            $ letterR6in1 = False
            $ letterR6in2 = True
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in3 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterR6x = 1040
            $ letterR6y = 535
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = True
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterR6x = 1190
            $ letterR6y = 535
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = True
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterR6x = 1340
            $ letterR6y = 535
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = True
            $ letterR6in6 = False
            $ letterR6in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterR6x = 1490
            $ letterR6y = 535
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = True
            $ letterR6in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in7 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterR6x = 1260
            $ letterR6y = 284
            $ letterR6in1 = False
            $ letterR6in2 = False
            $ letterR6in3 = False
            $ letterR6in4 = False
            $ letterR6in5 = False
            $ letterR6in6 = False
            $ letterR6in7 = True


    if gate_name == "letterT3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterR2in1 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in1 = False
            if letterB3in1 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in1 = False
            if letterB4in1 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in1 = False
            if letterR6in1 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in1 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for checks
            $ letterT7x = 1115
            $ letterT7y = 362
            $ letterT7in1 = True
            $ letterT7in2 = False
            $ letterT7in3 = False
            $ letterT7in4 = False
            $ letterT7in5 = False
            $ letterT7in6 = False
            $ letterT7in7 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterR2in2 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in2 = False
            if letterB3in2 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in2 = False
            if letterB4in2 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in2 = False
            if letterR6in2 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in2 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets check values
            $ letterT7x = 1415
            $ letterT7y = 360
            $ letterT7in1 = False
            $ letterT7in2 = True
            $ letterT7in3 = False
            $ letterT7in4 = False
            $ letterT7in5 = False
            $ letterT7in6 = False
            $ letterT7in7 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterR2in3 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in3 = False
            if letterB3in3 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in3 = False
            if letterB4in3 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in3 = False
            if letterR6in3 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in3 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT7x = 1040
            $ letterT7y = 535
            $ letterT7in1 = False
            $ letterT7in2 = False
            $ letterT7in3 = True
            $ letterT7in4 = False
            $ letterT7in5 = False
            $ letterT7in6 = False
            $ letterT7in7 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterR2in4 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in4 = False
            if letterB3in4 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in4 = False
            if letterB4in4 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in4 = False
            if letterR6in4 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in4 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT7x = 1190
            $ letterT7y = 535
            $ letterT7in1 = False
            $ letterT7in2 = False
            $ letterT7in3 = False
            $ letterT7in4 = True
            $ letterT7in5 = False
            $ letterT7in6 = False
            $ letterT7in7 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterR2in5 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in5 = False
            if letterB3in5 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in5 = False
            if letterB4in5 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in5 = False
            if letterR6in5 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in5 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT7x = 1340
            $ letterT7y = 535
            $ letterT7in1 = False
            $ letterT7in2 = False
            $ letterT7in3 = False
            $ letterT7in4 = False
            $ letterT7in5 = True
            $ letterT7in6 = False
            $ letterT7in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterR2in6 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in6 = False
            if letterB3in6 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in6 = False
            if letterB4in6 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in6 = False
            if letterR6in6 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in6 = False
            if letterT7in1 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in1 = False

            #sets values for the checks
            $ letterT7x = 1490
            $ letterT7y = 535
            $ letterT7in1 = False
            $ letterT7in2 = False
            $ letterT7in3 = False
            $ letterT7in4 = False
            $ letterT7in5 = False
            $ letterT7in6 = True
            $ letterT7in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterR2in7 == True:
               $ letterR2x = 410
               $ letterR2y = 575
               $ letterR2in7 = False
            if letterB3in7 == True:
               $ letterB3x = 342
               $ letterB3y = 660
               $ letterB3in7 = False
            if letterB4in7 == True:
               $ letterB4x = 342
               $ letterB4y = 660
               $ letterB4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 575
               $ letterT5in7 = False
            if letterR6in7 == True:
               $ letterR6x = 410
               $ letterR6y = 575
               $ letterR6in7 = False
            if letterT7in7 == True:
               $ letterT7x = 275
               $ letterT7y = 575
               $ letterT7in7 = False

            #sets values for the checks
            $ letterT7x = 1262
            $ letterT7y = 284
            $ letterT7in1 = False
            $ letterT7in2 = False
            $ letterT7in3 = False
            $ letterT7in4 = False
            $ letterT7in5 = False
            $ letterT7in6 = False
            $ letterT7in7 = True

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


    
    if (letterT1in7 == True or letterT5in7 == True or letterT7in7 == True):
        image gram_m1_tile36 = "treeGreen.png"
        image gram_m1_tile37 = "1_1_green.png"
        show gram_m1_tile36 at Position(xpos = 1250, xanchor = 0, ypos = 227, yanchor = 0)
        show gram_m1_tile37 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)

        if (letterT5in1 == True or letterT7in1 == True or letterT1in1 == True) and (letterT5in2 == True or letterT7in2 == True or letterT1in2 == True):
            image gram_m1_tile42 = "leftTreegreenlong.png"
            image gram_m1_tile43 = "1_1_green.png"
            show gram_m1_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 370, yanchor = 0)
            show gram_m1_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 345, yanchor = 0)

            image gram_m1_tile60 = "rightTreegreenlong.png"
            image gram_m1_tile61 = "1_1_green.png"
            show gram_m1_tile60 at Position(xpos = 1310, xanchor = 0, ypos = 370, yanchor = 0)
            show gram_m1_tile61 at Position(xpos = 1400, xanchor = 0, ypos = 345, yanchor = 0)
        
            if (letterB3in3 == True or letterB4in3 == True) and (letterR6in4 == True or letterR2in4 == True):
                image gram_m1_tile44 = "leftTreegreen.png"
                image gram_m1_tile45 = "1_1_green.png"
                image gram_m1_tile46 = "solutionLine.png"
                image gram_m1_tile47 = "c.png"
                show gram_m1_tile44 at Position(xpos = 1070, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile45 at Position(xpos = 1025, xanchor = 0, ypos = 520, yanchor = 0)
                show gram_m1_tile46 at Position(xpos = 1025, xanchor = 0, ypos = 620, yanchor = 0)
                show gram_m1_tile47 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)

                image gram_m1_tile50 = "rightTreegreen.png"
                image gram_m1_tile51 = "1_1_green.png"
                image gram_m1_tile52 = "solutionLine.png"
                image gram_m1_tile53 = "d.png"
                show gram_m1_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 520, yanchor = 0)
                show gram_m1_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 620, yanchor = 0)
                show gram_m1_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)

            if (letterB3in3 == False and letterB4in3 == False) or (letterR6in4 == False and letterR2in4 == False):
                hide gram_m1_tile44
                hide gram_m1_tile45
                hide gram_m1_tile46
                hide gram_m1_tile47

                hide gram_m1_tile50
                hide gram_m1_tile51
                hide gram_m1_tile52
                hide gram_m1_tile53
     
            if (letterT1in3 == True or letterR2in3 == True or letterT5in3 == True or letterR6in3 == True or letterT7in3 == True) and (letterT1in4 == True or letterB3in4 == True or letterB4in4 == True or letterT5in4 == True or letterT7in4 == True):
                image gram_m1_tile48 = "leftTreered.png"
                image gram_m1_tile49 = "1_1_red.png"
                show gram_m1_tile48 at Position(xpos = 1070, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile49 at Position(xpos = 1025, xanchor = 0, ypos = 520, yanchor = 0)

                image gram_m1_tile54 = "rightTreered.png"
                image gram_m1_tile55 = "1_1_red.png"
                show gram_m1_tile54 at Position(xpos = 1170, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile55 at Position(xpos = 1175, xanchor = 0, ypos = 520, yanchor = 0)

            elif (letterT1in3 == False and letterR2in3 == False and letterT5in3 == False and letterR6in3 == False and letterT7in3 == False) or (letterT1in4 == False and letterB3in4 == False and letterB4in4 == False and letterT5in4 == False and letterT7in4 == False):
                hide gram_m1_tile48
                hide gram_m1_tile49

                hide gram_m1_tile54
                hide gram_m1_tile55


            if (letterB4in5 == True or letterB3in5 == True) and (letterR2in6 == True or letterR6in6 == True):
                image gram_m1_tile62 = "leftTreegreen.png"
                image gram_m1_tile63 = "1_1_green.png"
                image gram_m1_tile64 = "solutionLine.png"
                image gram_m1_tile65 = "c.png"
                show gram_m1_tile62 at Position(xpos = 1370, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile63 at Position(xpos = 1325, xanchor = 0, ypos = 520, yanchor = 0)
                show gram_m1_tile64 at Position(xpos = 1325, xanchor = 0, ypos = 620, yanchor = 0)
                show gram_m1_tile65 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)

                image gram_m1_tile68 = "rightTreegreen.png"
                image gram_m1_tile69 = "1_1_green.png"
                image gram_m1_tile70 = "solutionLine.png"
                image gram_m1_tile71 = "d.png"
                show gram_m1_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 520, yanchor = 0)
                show gram_m1_tile70 at Position(xpos = 1475, xanchor = 0, ypos = 620, yanchor = 0)
                show gram_m1_tile71 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)
            
            if (letterB4in5 == False and letterB3in5 == False) or (letterR2in6 == False and letterR6in6 == False):
                hide gram_m1_tile62
                hide gram_m1_tile63
                hide gram_m1_tile64
                hide gram_m1_tile65

                hide gram_m1_tile68
                hide gram_m1_tile69
                hide gram_m1_tile70
                hide gram_m1_tile71

            if (letterT1in5 == True or letterR2in5 == True or letterT5in5 == True or letterR6in5 == True or letterT7in5 == True) and (letterT1in6 == True or letterB3in6 == True or letterB4in6 == True or letterT5in6 == True or letterT7in6 == True):
                image gram_m1_tile66 = "leftTreered.png"
                image gram_m1_tile67 = "1_1_red.png"
                show gram_m1_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 520, yanchor = 0)

                image gram_m1_tile72 = "rightTreered.png"
                image gram_m1_tile73 = "1_1_red.png"
                show gram_m1_tile72 at Position(xpos = 1470, xanchor = 0, ypos = 445, yanchor = 0)
                show gram_m1_tile73 at Position(xpos = 1475, xanchor = 0, ypos = 520, yanchor = 0)

            elif (letterT1in5 == False and letterR2in5 == False and letterT5in5 == False and letterR6in5 == False and letterT7in5 == False) or (letterT1in6 == False and letterB3in6 == False and letterB4in6 == False and letterT5in6 == False and letterT7in6 == False):
                hide gram_m1_tile66
                hide gram_m1_tile67

                hide gram_m1_tile72
                hide gram_m1_tile73
    
        if (letterT5in1 == False and letterT7in1 == False and letterT1in1 == False) or (letterT5in2 == False and letterT7in2 == False and letterT1in2 == False):
            hide gram_m1_tile60
            hide gram_m1_tile61
            hide gram_m1_tile62
            hide gram_m1_tile63
            hide gram_m1_tile64
            hide gram_m1_tile65
            hide gram_m1_tile66
            hide gram_m1_tile67
            hide gram_m1_tile68
            hide gram_m1_tile69
            hide gram_m1_tile70
            hide gram_m1_tile71
            hide gram_m1_tile72
            hide gram_m1_tile73
            hide gram_m1_tile42
            hide gram_m1_tile43
            hide gram_m1_tile44
            hide gram_m1_tile45
            hide gram_m1_tile46
            hide gram_m1_tile47
            hide gram_m1_tile48
            hide gram_m1_tile49
            hide gram_m1_tile50
            hide gram_m1_tile51
            hide gram_m1_tile52
            hide gram_m1_tile53
            hide gram_m1_tile54
            hide gram_m1_tile55


        if (letterR2in1 == True or letterR6in1 == True) and (letterB3in2 == True or letterB4in2 == True):
            image gram_m1_tile74 = "leftTreeredlong.png"
            image gram_m1_tile75 = "1_1_red.png"
            show gram_m1_tile74 at Position(xpos = 1140, xanchor = 0, ypos = 370, yanchor = 0)
            show gram_m1_tile75 at Position(xpos = 1100, xanchor = 0, ypos = 345, yanchor = 0)

            image gram_m1_tile76 = "rightTreeredlong.png"
            image gram_m1_tile77 = "1_1_red.png"
            show gram_m1_tile76 at Position(xpos = 1310, xanchor = 0, ypos = 370, yanchor = 0)
            show gram_m1_tile77 at Position(xpos = 1400, xanchor = 0, ypos = 345, yanchor = 0)

        elif (letterR2in1 == False and letterR6in1 == False) or (letterB3in2 == False and letterB4in2 == False):
            hide gram_m1_tile74
            hide gram_m1_tile75

            hide gram_m1_tile76
            hide gram_m1_tile77

    if (letterB3in1 == True or letterB4in1 == True) and (letterR2in2 == True or letterR6in2 == True):
        image gram_m1_tile78 = "leftTreegreenlong.png"
        image gram_m1_tile79 = "1_1_green.png"
        show gram_m1_tile78 at Position(xpos = 1140, xanchor = 0, ypos = 370, yanchor = 0)
        show gram_m1_tile79 at Position(xpos = 1100, xanchor = 0, ypos = 345, yanchor = 0)

        image gram_m1_tile84 = "rightTreegreenlong.png"
        image gram_m1_tile85 = "1_1_green.png"
        show gram_m1_tile84 at Position(xpos = 1310, xanchor = 0, ypos = 370, yanchor = 0)
        show gram_m1_tile85 at Position(xpos = 1400, xanchor = 0, ypos = 345, yanchor = 0)
        
        if (letterT1in3 == True or letterR2in3 == True or letterB3in3 == True or letterB4in3 == True or letterT5in3 == True or letterR6in3 == True or letterT7in3 == True) and (letterT1in4 == True or letterR2in4 == True or letterB4in4 == True or letterT5in4 == True or letterR6in4 == True or letterB3in4 == True or letterT7in4 == True):
            image gram_m1_tile80 = "leftTreered.png"
            image gram_m1_tile81 = "1_1_red.png"
            show gram_m1_tile80 at Position(xpos = 1070, xanchor = 0, ypos = 445, yanchor = 0)
            show gram_m1_tile81 at Position(xpos = 1025, xanchor = 0, ypos = 520, yanchor = 0)

            image gram_m1_tile82 = "rightTreered.png"
            image gram_m1_tile83 = "1_1_red.png"
            show gram_m1_tile82 at Position(xpos = 1170, xanchor = 0, ypos = 445, yanchor = 0)
            show gram_m1_tile83 at Position(xpos = 1175, xanchor = 0, ypos = 520, yanchor = 0)

        elif (letterT1in5 == False) or (letterT1in6 == False):
            hide gram_m1_tile80
            hide gram_m1_tile81

            hide gram_m1_tile82
            hide gram_m1_tile83

        if (letterT1in5 == True or letterR2in5 == True or letterB3in5 == True or letterB4in5 == True or letterT5in5 == True or letterR6in5 == True or letterT7in5 == True) and (letterT1in6 == True or letterR2in6 == True or letterB3in6 == True or letterB4in6 == True or letterT5in6 == True or letterR6in6 == True or letterT7in6 == True):
            image gram_m1_tile86 = "leftTreered.png"
            image gram_m1_tile87 = "1_1_red.png"
            show gram_m1_tile86 at Position(xpos = 1370, xanchor = 0, ypos = 445, yanchor = 0)
            show gram_m1_tile87 at Position(xpos = 1325, xanchor = 0, ypos = 520, yanchor = 0)

            image gram_m1_tile88 = "rightTreered.png"
            image gram_m1_tile89 = "1_1_red.png"
            show gram_m1_tile88 at Position(xpos = 1470, xanchor = 0, ypos = 445, yanchor = 0)
            show gram_m1_tile89 at Position(xpos = 1475, xanchor = 0, ypos = 520, yanchor = 0)

        elif (letterT1in5 == False) or (letterT1in6 == False):
            hide gram_m1_tile86
            hide gram_m1_tile87

            hide gram_m1_tile88
            hide gram_m1_tile89

    if (letterB3in1 == False and letterB4in1 == False) or (letterR2in2 == False and letterR6in2 == False):
        hide gram_m1_tile78
        hide gram_m1_tile79
        hide gram_m1_tile80
        hide gram_m1_tile81
        hide gram_m1_tile82
        hide gram_m1_tile83

        hide gram_m1_tile84
        hide gram_m1_tile85
        hide gram_m1_tile86
        hide gram_m1_tile87
        hide gram_m1_tile88
        hide gram_m1_tile89


    if (letterT1in7 == False and letterT5in7 == False and letterT7in7 == False):
        hide gram_m1_tile36
        hide gram_m1_tile37
        hide gram_m1_tile40
        hide gram_m1_tile41
        hide gram_m1_tile42
        hide gram_m1_tile43
        hide gram_m1_tile44
        hide gram_m1_tile45
        hide gram_m1_tile46
        hide gram_m1_tile47
        hide gram_m1_tile48
        hide gram_m1_tile49
        hide gram_m1_tile50
        hide gram_m1_tile51
        hide gram_m1_tile52
        hide gram_m1_tile53
        hide gram_m1_tile54
        hide gram_m1_tile55
        hide gram_m1_tile60
        hide gram_m1_tile61
        hide gram_m1_tile62
        hide gram_m1_tile63
        hide gram_m1_tile64
        hide gram_m1_tile65
        hide gram_m1_tile66
        hide gram_m1_tile67
        hide gram_m1_tile68
        hide gram_m1_tile69
        hide gram_m1_tile70
        hide gram_m1_tile71
        hide gram_m1_tile72
        hide gram_m1_tile73
        hide gram_m1_tile74
        hide gram_m1_tile75
        hide gram_m1_tile76
        hide gram_m1_tile77
        hide gram_m1_tile78
        hide gram_m1_tile79
        hide gram_m1_tile80
        hide gram_m1_tile81
        hide gram_m1_tile82
        hide gram_m1_tile83
        hide gram_m1_tile84
        hide gram_m1_tile85
        hide gram_m1_tile86
        hide gram_m1_tile87
        hide gram_m1_tile88
        hide gram_m1_tile89

    if (letterR2in7 == True or letterB3in7 == True or letterB4in7 == True or letterR6in7 == True):
        image gram_m1_tile38 = "treeRed.png"
        image gram_m1_tile39 = "1_1_red.png"
        show gram_m1_tile38 at Position(xpos = 1250, xanchor = 0, ypos = 227, yanchor = 0)
        show gram_m1_tile39 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)

    elif (letterR2in7 == False and letterB3in7 == False and letterB4in7 == False and letterR6in7 == False):
        hide gram_m1_tile38
        hide gram_m1_tile39

    #win conditions
    if (letterT1in7 == True or letterT5in7 == True or letterT7in7 == True) and (letterT5in1 == True or letterT7in1 == True or letterT1in1 == True) and (letterB3in3 == True or letterB4in3 == True) and (letterR6in4 == True or letterR2in4 == True) and (letterT5in2 == True or letterT7in2 == True or letterT1in2 == True) and (letterB4in5 == True or letterB3in5 == True) and (letterR2in6 == True or letterR6in6 == True): 
        image gram_m1_tile202 = "letterT.png"
        image gram_m1_tile206 = "letterR.png"
        image gram_m1_tile203 = "letterB.png"
        image gram_m1_tile205 = "letterB.png"
        image gram_m1_tile201 = "letterT.png"
        image gram_m1_tile204 = "letterR.png"
        image gram_m1_tile207 = "letterT.png"
        
        show gram_m1_tile202 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_m1_tile206 at Position(xpos = letterR2x, xanchor = 0, ypos = letterR2y, yanchor = 0)
        show gram_m1_tile203 at Position(xpos = letterB3x, xanchor = 0, ypos = letterB3y, yanchor = 0)
        show gram_m1_tile205 at Position(xpos = letterB4x, xanchor = 0, ypos = letterB4y, yanchor = 0)
        show gram_m1_tile201 at Position(xpos = letterT5x, xanchor = 0, ypos = letterT5y, yanchor = 0)
        show gram_m1_tile204 at Position(xpos = letterR6x, xanchor = 0, ypos = letterR6y, yanchor = 0)
        show gram_m1_tile207 at Position(xpos = letterT7x, xanchor = 0, ypos = letterT7y, yanchor = 0)

        "Access Gained"

        jump gram_m1 #start

    if attempts ==0:
        hide gram_m1_tile42
        hide gram_m1_tile43
        hide gram_m1_tile44
        hide gram_m1_tile45
        hide gram_m1_tile46
        hide gram_m1_tile47
        hide gram_m1_tile48
        hide gram_m1_tile49
        hide gram_m1_tile50
        hide gram_m1_tile51
        hide gram_m1_tile52
        hide gram_m1_tile53
        hide gram_m1_tile54
        hide gram_m1_tile55
        hide gram_m1_tile56
        hide gram_m1_tile61
        hide gram_m1_tile62
        hide gram_m1_tile63
        hide gram_m1_tile64
        hide gram_m1_tile65
        hide gram_m1_tile66
        hide gram_m1_tile67
        hide gram_m1_tile68
        hide gram_m1_tile69
        hide gram_m1_tile70
        hide gram_m1_tile71
        hide gram_m1_tile72
        hide gram_m1_tile73
        hide gram_m1_tile74
        hide gram_m1_tile75
        hide gram_m1_tile76
        hide gram_m1_tile77
        hide gram_m1_tile78
        hide gram_m1_tile79
        hide gram_m1_tile80
        hide gram_m1_tile81
        hide gram_m1_tile82
        hide gram_m1_tile83
        hide gram_m1_tile84
        hide gram_m1_tile85
        hide gram_m1_tile86
        hide gram_m1_tile87
        hide gram_m1_tile88
        hide gram_m1_tile89

        "You Lose Try Again"

        jump gram_m1 #start
      
    
    jump gamefile_m1

