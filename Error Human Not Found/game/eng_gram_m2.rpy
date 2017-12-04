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

screen logicGates_med2:
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
        action Jump("hints_gramMed_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 178
        ypos 285
    text "Moves" xpos 200 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 315 ypos 293 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 350 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27
    draggroup:
        #and gates
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM1x ypos letterM1y
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK2x ypos letterK2y
        drag:
                drag_name "letterR"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterR3x ypos letterR3y
        drag:
                drag_name "letterJ2"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJ4x ypos letterJ4y
        drag:
                drag_name "letterT"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT5x ypos letterT5y
        drag:
                drag_name "letterJ1"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJ6x ypos letterJ6y
        drag:
                drag_name "letterJ3"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJ7x ypos letterJ7y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 1115 ypos 310
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1415 ypos 310
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 1013 ypos 485
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 1200 ypos 485
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1340 ypos 485
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1513 ypos 485
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 860 ypos 660

       #letter dragback
        
        drag:
                drag_name "LetterM_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterJ_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648
        drag:
                drag_name "LetterT_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterR_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738

init:
    image bg Eng_gram_m2_tile = "eng_tile_bg.png"

label gram_m2: #start:
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg Eng_gram_m2_tile

    #row1 1-4
    image gram_m2_tile0 = "instructions7.png"
    image gram_m2_tile1 = "1_1_green.png"
    image gram_m2_tile2 = "letterS.png"
    #image gram_m2_tile3 = "treeGrey.png"
    show gram_m2_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_m2_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 130, yanchor = 0)
    show gram_m2_tile2 at Position(xpos = 1260, xanchor = 0, ypos = 145, yanchor = 0)
    #show gram_m2_tile3 at Position(xpos = 1248, xanchor = 0, ypos = 228, yanchor = 0)
    
    #row2 5-8
    #image gram_m2_tile4 = "1_1_grey.png"
    image gram_m2_tile5 = "leftTreelong.png"
    image gram_m2_tile6 = "rightTreelong.png"
    #show gram_m2_tile4 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)
    show gram_m2_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 225, yanchor = 0)
    show gram_m2_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 225, yanchor = 0)
    
    #row3 9-13   

    image gram_m2_tile9 = "1_1_grey.png"
    image gram_m2_tile10 = "1_1_grey.png"
    

    show gram_m2_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 300, yanchor = 0)
    show gram_m2_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 300, yanchor = 0)

    #row4 14-20

    image gram_m2_tile14 = "leftTree.png"
    image gram_m2_tile15 = "rightTree.png"
    image gram_m2_tile16 = "leftTree.png"
    image gram_m2_tile17 = "rightTree.png"

    show gram_m2_tile14 at Position(xpos = 1050, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m2_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m2_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m2_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 400, yanchor = 0)


    #row5 21-27

    image gram_m2_tile21 = "1_1_grey.png"
    image gram_m2_tile22 = "1_1_grey.png"
    image gram_m2_tile23 = "1_1_grey.png"
    image gram_m2_tile24 = "1_1_grey.png"

    show gram_m2_tile21 at Position(xpos = 1000, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m2_tile22 at Position(xpos = 1185, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m2_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m2_tile24 at Position(xpos = 1500, xanchor = 0, ypos = 475, yanchor = 0)

    image gram_m2_tile25 = "leftTreelong.png"
    image gram_m2_tile26 = "1_1_grey.png"
    show gram_m2_tile25 at Position(xpos = 885, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m2_tile26 at Position(xpos = 845, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m2_tile31 = "letterBorder.png"
    image gram_m2_tile32 = "letterBorder.png"
    image gram_m2_tile33 = "letterBorder.png"
    image gram_m2_tile34 = "letterBorder.png"
    image gram_m2_tile35 = "letterBorder.png"
    #image gram_m2_tile36 = "letterBorder.png"
    show gram_m2_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m2_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m2_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show gram_m2_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show gram_m2_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    #show gram_m2_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)

    image eaeng_m2_tile300 = "letterM_grey.png"
    image eaeng_m2_tile301 = "letterK_grey.png"
    image eaeng_m2_tile302 = "letterJ_grey.png"
    image eaeng_m2_tile303 = "letterT_grey.png"
    image eaeng_m2_tile304 = "letterR_grey.png"
    show eaeng_m2_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_m2_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_m2_tile302 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_m2_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_m2_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)


    # gates
    $ letterM1x = 275 
    $ letterM1y = 575
    $ letterK2x = 410
    $ letterK2y = 575
    $ letterR3x = 410 
    $ letterR3y = 750
    $ letterJ4x = 342
    $ letterJ4y = 660
    $ letterT5x = 275
    $ letterT5y = 750
    $ letterJ6x = 342 
    $ letterJ6y = 660
    $ letterJ7x = 342 
    $ letterJ7y = 660

    # check conditons for locations
    $ letterM1in1 = False
    $ letterM1in2 = False
    $ letterM1in3 = False
    $ letterM1in4 = False
    $ letterM1in5 = False
    $ letterM1in6 = False
    $ letterM1in7 = False

    $ letterK2in1 = False
    $ letterK2in2 = False
    $ letterK2in3 = False
    $ letterK2in4 = False
    $ letterK2in5 = False
    $ letterK2in6 = False
    $ letterK2in7 = False

    $ letterR3in1 = False
    $ letterR3in2 = False
    $ letterR3in3 = False
    $ letterR3in4 = False
    $ letterR3in5 = False
    $ letterR3in6 = False
    $ letterR3in7 = False

    $ letterJ4in1 = False
    $ letterJ4in2 = False
    $ letterJ4in3 = False
    $ letterJ4in4 = False
    $ letterJ4in5 = False
    $ letterJ4in6 = False
    $ letterJ4in7 = False

    $ letterT5in1 = False
    $ letterT5in2 = False
    $ letterT5in3 = False
    $ letterT5in4 = False
    $ letterT5in5 = False
    $ letterT5in6 = False
    $ letterT5in7 = False


    $ letterJ6in1 = False
    $ letterJ6in2 = False
    $ letterJ6in3 = False
    $ letterJ6in4 = False
    $ letterJ6in5 = False
    $ letterJ6in6 = False
    $ letterJ6in7 = False


    $ letterJ7in1 = False
    $ letterJ7in2 = False
    $ letterJ7in3 = False
    $ letterJ7in4 = False
    $ letterJ7in5 = False
    $ letterJ7in6 = False
    $ letterJ7in7 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 10
    
    call gamefile_m2 from _call_gamefile_m2

label gamefile_m2:
    #image moon = "images/blankgram_m2_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGates_med2

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m2_tile here
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False
            #sets values for checks
            $ letterM1x = 1115
            $ letterM1y = 315
            $ letterM1in1 = True
            $ letterM1in2 = False
            $ letterM1in3 = False
            $ letterM1in4 = False
            $ letterM1in5 = False
            $ letterM1in6 = False
            $ letterM1in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterM1x = 1415
            $ letterM1y = 315
            $ letterM1in1 = False
            $ letterM1in2 = True
            $ letterM1in3 = False
            $ letterM1in4 = False
            $ letterM1in5 = False
            $ letterM1in6 = False
            $ letterM1in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterM1x = 1013
            $ letterM1y = 490
            $ letterM1in1 = False
            $ letterM1in2 = False
            $ letterM1in3 = True
            $ letterM1in4 = False
            $ letterM1in5 = False
            $ letterM1in6 = False
            $ letterM1in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterM1x = 1200
            $ letterM1y = 490
            $ letterM1in1 = False
            $ letterM1in2 = False
            $ letterM1in3 = False
            $ letterM1in4 = True
            $ letterM1in5 = False
            $ letterM1in6 = False
            $ letterM1in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterM1x = 1340
            $ letterM1y = 490
            $ letterM1in1 = False
            $ letterM1in2 = False
            $ letterM1in3 = False
            $ letterM1in4 = False
            $ letterM1in5 = True
            $ letterM1in6 = False
            $ letterM1in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterM1x = 1513
            $ letterM1y = 490
            $ letterM1in1 = False
            $ letterM1in2 = False
            $ letterM1in3 = False
            $ letterM1in4 = False
            $ letterM1in5 = False
            $ letterM1in6 = True
            $ letterM1in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterM1x = 860
            $ letterM1y = 665
            $ letterM1in1 = False
            $ letterM1in2 = False
            $ letterM1in3 = False
            $ letterM1in4 = False
            $ letterM1in5 = False
            $ letterM1in6 = False
            $ letterM1in7 = True

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False

            #sets values for checks
            $ letterK2x = 1115
            $ letterK2y = 315
            $ letterK2in1 = True
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterK2x = 1415
            $ letterK2y = 315
            $ letterK2in1 = False
            $ letterK2in2 = True
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterK2x = 1013
            $ letterK2y = 490
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = True
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterK2x = 1200
            $ letterK2y = 490
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = True
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterK2x = 1340
            $ letterK2y = 490
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = True
            $ letterK2in6 = False
            $ letterK2in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterK2x = 1513
            $ letterK2y = 490
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = True
            $ letterK2in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterK2x = 860
            $ letterK2y = 665
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = True

    if gate_name == "letterR":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False

            #sets values for checks
            $ letterR3x = 1115
            $ letterR3y = 315
            $ letterR3in1 = True
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterR3x = 1415
            $ letterR3y = 315
            $ letterR3in1 = False
            $ letterR3in2 = True
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterR3x = 1013
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = True
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterR3x = 1200
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = True
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterR3x = 1340
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = True
            $ letterR3in6 = False
            $ letterR3in7 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterR3x = 1513
            $ letterR3y = 490
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = True
            $ letterR3in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterR3x = 860
            $ letterR3y = 660
            $ letterR3in1 = False
            $ letterR3in2 = False
            $ letterR3in3 = False
            $ letterR3in4 = False
            $ letterR3in5 = False
            $ letterR3in6 = False
            $ letterR3in7 = True
          


    if gate_name == "letterJ2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False

            #sets values for checks
            $ letterJ4x = 1115
            $ letterJ4y = 315
            $ letterJ4in1 = True
            $ letterJ4in2 = False
            $ letterJ4in3 = False
            $ letterJ4in4 = False
            $ letterJ4in5 = False
            $ letterJ4in6 = False
            $ letterJ4in7 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterJ4x = 1415
            $ letterJ4y = 315
            $ letterJ4in1 = False
            $ letterJ4in2 = True
            $ letterJ4in3 = False
            $ letterJ4in4 = False
            $ letterJ4in5 = False
            $ letterJ4in6 = False
            $ letterJ4in7 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterJ4x = 1013
            $ letterJ4y = 490
            $ letterJ4in1 = False
            $ letterJ4in2 = False
            $ letterJ4in3 = True
            $ letterJ4in4 = False
            $ letterJ4in5 = False
            $ letterJ4in6 = False
            $ letterJ4in7 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterJ4x = 1200
            $ letterJ4y = 490
            $ letterJ4in1 = False
            $ letterJ4in2 = False
            $ letterJ4in3 = False
            $ letterJ4in4 = True
            $ letterJ4in5 = False
            $ letterJ4in6 = False
            $ letterJ4in7 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterJ4x = 1340
            $ letterJ4y = 490
            $ letterJ4in1 = False
            $ letterJ4in2 = False
            $ letterJ4in3 = False
            $ letterJ4in4 = False
            $ letterJ4in5 = True
            $ letterJ4in6 = False
            $ letterJ4in7 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterJ4x = 1513
            $ letterJ4y = 490
            $ letterJ4in1 = False
            $ letterJ4in2 = False
            $ letterJ4in3 = False
            $ letterJ4in4 = False
            $ letterJ4in5 = False
            $ letterJ4in6 = True
            $ letterJ4in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterJ4x = 860
            $ letterJ4y = 665
            $ letterJ4in1 = False
            $ letterJ4in2 = False
            $ letterJ4in3 = False
            $ letterJ4in4 = False
            $ letterJ4in5 = False
            $ letterJ4in6 = False
            $ letterJ4in7 = True
           


    if gate_name == "letterT":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False

            #sets values for checks
            $ letterT5x = 1115
            $ letterT5y = 315
            $ letterT5in1 = True
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterT5x = 1415
            $ letterT5y = 315
            $ letterT5in1 = False
            $ letterT5in2 = True
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterT5x = 1013
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = True
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterT5x = 1200
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = True
            $ letterT5in5 = False
            $ letterT5in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterT5x = 1340
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = True
            $ letterT5in6 = False
            $ letterT5in7 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterT5x = 1513
            $ letterT5y = 490
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = True
            $ letterT5in7 = False
            
                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterT5x = 860
            $ letterT5y = 665
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = True
  

    if gate_name == "letterJ1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False

            #sets values for checks
            $ letterJ6x = 1115
            $ letterJ6y = 315
            $ letterJ6in1 = True
            $ letterJ6in2 = False
            $ letterJ6in3 = False
            $ letterJ6in4 = False
            $ letterJ6in5 = False
            $ letterJ6in6 = False
            $ letterJ6in7 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterJ6x = 1415
            $ letterJ6y = 315
            $ letterJ6in1 = False
            $ letterJ6in2 = True
            $ letterJ6in3 = False
            $ letterJ6in4 = False
            $ letterJ6in5 = False
            $ letterJ6in6 = False
            $ letterJ6in7 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterJ6x = 1013
            $ letterJ6y = 490
            $ letterJ6in1 = False
            $ letterJ6in2 = False
            $ letterJ6in3 = True
            $ letterJ6in4 = False
            $ letterJ6in5 = False
            $ letterJ6in6 = False
            $ letterJ6in7 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterJ6x = 1200
            $ letterJ6y = 490
            $ letterJ6in1 = False
            $ letterJ6in2 = False
            $ letterJ6in3 = False
            $ letterJ6in4 = True
            $ letterJ6in5 = False
            $ letterJ6in6 = False
            $ letterJ6in7 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterJ6x = 1340
            $ letterJ6y = 490
            $ letterJ6in1 = False
            $ letterJ6in2 = False
            $ letterJ6in3 = False
            $ letterJ6in4 = False
            $ letterJ6in5 = True
            $ letterJ6in6 = False
            $ letterJ6in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterJ6x = 1513
            $ letterJ6y = 490
            $ letterJ6in1 = False
            $ letterJ6in2 = False
            $ letterJ6in3 = False
            $ letterJ6in4 = False
            $ letterJ6in5 = False
            $ letterJ6in6 = True
            $ letterJ6in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterJ6x = 860
            $ letterJ6y = 665
            $ letterJ6in1 = False
            $ letterJ6in2 = False
            $ letterJ6in3 = False
            $ letterJ6in4 = False
            $ letterJ6in5 = False
            $ letterJ6in6 = False
            $ letterJ6in7 = True


    if gate_name == "letterJ3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterM1in1 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterR3in1 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in1 = False
            if letterJ4in1 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in1 = False
            if letterT5in1 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in1 = False
            if letterJ6in1 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in1 = False
            if letterJ7in1 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in1 = False

            #sets values for checks
            $ letterJ7x = 1115
            $ letterJ7y = 315
            $ letterJ7in1 = True
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterM1in2 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterR3in2 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in2 = False
            if letterJ4in2 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in2 = False
            if letterT5in2 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in2 = False
            if letterJ6in2 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in2 = False
            if letterJ7in2 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in2 = False

            #sets check values
            $ letterJ7x = 1415
            $ letterJ7y = 315
            $ letterJ7in1 = False
            $ letterJ7in2 = True
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterM1in3 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterR3in3 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in3 = False
            if letterJ4in3 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in3 = False
            if letterT5in3 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in3 = False
            if letterJ6in3 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in3 = False
            if letterJ7in3 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in3 = False

            #sets values for the checks
            $ letterJ7x = 1013
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = True
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterM1in4 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterR3in4 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in4 = False
            if letterJ4in4 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in4 = False
            if letterT5in4 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in4 = False
            if letterJ6in4 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in4 = False
            if letterJ7in4 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in4 = False

            #sets values for the checks
            $ letterJ7x = 1200
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = True
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterM1in5 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterR3in5 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in5 = False
            if letterJ4in5 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in5 = False
            if letterT5in5 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in5 = False
            if letterJ6in5 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in5 = False
            if letterJ7in5 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in5 = False

            #sets values for the checks
            $ letterJ7x = 1340
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = True
            $ letterJ7in6 = False
            $ letterJ7in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterM1in6 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterR3in6 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in6 = False
            if letterJ4in6 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in6 = False
            if letterT5in6 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in6 = False
            if letterJ6in6 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in6 = False
            if letterJ7in6 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in6 = False

            #sets values for the checks
            $ letterJ7x = 1513
            $ letterJ7y = 490
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = True
            $ letterJ7in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterM1in7 == True:
               $ letterM1x = 275
               $ letterM1y = 575
               $ letterM1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 410
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterR3in7 == True:
               $ letterR3x = 410
               $ letterR3y = 750
               $ letterR3in7 = False
            if letterJ4in7 == True:
               $ letterJ4x = 342
               $ letterJ4y = 660
               $ letterJ4in7 = False
            if letterT5in7 == True:
               $ letterT5x = 275
               $ letterT5y = 750
               $ letterT5in7 = False
            if letterJ6in7 == True:
               $ letterJ6x = 342
               $ letterJ6y = 660
               $ letterJ6in7 = False
            if letterJ7in7 == True:
               $ letterJ7x = 342
               $ letterJ7y = 660
               $ letterJ7in7 = False

            #sets values for the checks
            $ letterJ7x = 860
            $ letterJ7y = 665
            $ letterJ7in1 = False
            $ letterJ7in2 = False
            $ letterJ7in3 = False
            $ letterJ7in4 = False
            $ letterJ7in5 = False
            $ letterJ7in6 = False
            $ letterJ7in7 = True


#Dragbacks
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "LetterM_return" or slot_name == "LetterK_return" or slot_name == "LetterR_return" or slot_name == "LetterJ_return" or slot_name == "LetterT_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
           $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ letterM1x = 275
                    $ letterM1y = 575
                    $ letterM1in1 = False
                    $ letterM1in2 = False
                    $ letterM1in3 = False
                    $ letterM1in4 = False
                    $ letterM1in5 = False
                    $ letterM1in6 = False
                    $ letterM1in7 = False
   
            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ letterK2x = 410
                    $ letterK2y = 575
                    $ letterK2in1 = False
                    $ letterK2in2 = False
                    $ letterK2in3 = False
                    $ letterK2in4 = False
                    $ letterK2in5 = False
                    $ letterK2in6 = False
                    $ letterK2in7 = False
            
            if slot_name == "LetterR_return":
                $ attempts +=1
                if gate_name == "letterR":
                    $ letterR3x = 410
                    $ letterR3y = 750
                    $ letterR3in1 = False
                    $ letterR3in2 = False
                    $ letterR3in3 = False
                    $ letterR3in4 = False
                    $ letterR3in5 = False
                    $ letterR3in6 = False
                    $ letterR3in7 = False
                    
            if slot_name == "LetterJ_return":
                $ attempts +=1
                if gate_name == "letterJ1":
                    $ letterJ6x = 342
                    $ letterJ6y = 660
                    $ letterJ6in1 = False
                    $ letterJ6in2 = False
                    $ letterJ6in3 = False
                    $ letterJ6in4 = False
                    $ letterJ6in5 = False
                    $ letterJ6in6 = False
                    $ letterJ6in7 = False
                
                elif gate_name == "letterJ2":
                    $ letterJ4x = 342
                    $ letterJ4y = 660
                    $ letterJ4in1 = False
                    $ letterJ4in2 = False
                    $ letterJ4in3 = False
                    $ letterJ4in4 = False
                    $ letterJ4in5 = False
                    $ letterJ4in6 = False
                    $ letterJ4in7 = False
                elif gate_name == "letterJ3":
                    $ letterJ7x = 342
                    $ letterJ7y = 660
                    $ letterJ7in1 = False
                    $ letterJ7in2 = False
                    $ letterJ7in3 = False
                    $ letterJ7in4 = False
                    $ letterJ7in5 = False
                    $ letterJ7in6 = False
                    $ letterJ7in7 = False
            
            if slot_name == "LetterT_return":
                $ attempts +=1
                if gate_name == "letterT":
                    $ letterT5x = 275
                    $ letterT5y = 750
                    $ letterT5in1 = False
                    $ letterT5in2 = False
                    $ letterT5in3 = False
                    $ letterT5in4 = False
                    $ letterT5in5 = False
                    $ letterT5in6 = False
                    $ letterT5in7 = False


    #START SOUNDS HERE
    hide gram_m2_tile42
    hide gram_m2_tile43
    hide gram_m2_tile44
    hide gram_m2_tile45
    hide gram_m2_tile46
    hide gram_m2_tile47
    hide gram_m2_tile48
    hide gram_m2_tile207
    hide gram_m2_tile49
    hide gram_m2_tile50
    hide gram_m2_tile51
    hide gram_m2_tile52
    hide gram_m2_tile53
    hide gram_m2_tile54
    hide gram_m2_tile55
    hide gram_m2_tile56
    hide gram_m2_tile57
    hide gram_m2_tile58
    hide gram_m2_tile209
    hide gram_m2_tile210
    hide gram_m2_tile59
    hide gram_m2_tile60
    hide gram_m2_tile61
    hide gram_m2_tile62
    hide gram_m2_tile63
    hide gram_m2_tile64
    hide gram_m2_tile65
    hide gram_m2_tile66
    hide gram_m2_tile211
    hide gram_m2_tile212
    hide gram_m2_tile67
    hide gram_m2_tile68
    hide gram_m2_tile69
    hide gram_m2_tile70
    hide gram_m2_tile71
    hide gram_m2_tile72
    hide gram_m2_tile213
    hide gram_m2_tile214
    hide gram_m2_tile73
    hide gram_m2_tile74
    hide gram_m2_tile75
    hide gram_m2_tile90
    hide gram_m2_tile91
    hide gram_m2_tile92
    hide gram_m2_tile93
    hide gram_m2_tile01S
    hide gram_m2_tile02S
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if (letterT5in1) and (letterM1in2):
        image gram_m2_tile42 = "leftTreegreenlong.png"
        image gram_m2_tile43 = "1_1_green.png"
        show gram_m2_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 225, yanchor = 0)
        show gram_m2_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m2_tile62 = "rightTreegreenlong.png"
        image gram_m2_tile63 = "1_1_green.png"
        show gram_m2_tile62 at Position(xpos = 1310, xanchor = 0, ypos = 225, yanchor = 0)
        show gram_m2_tile63 at Position(xpos = 1400, xanchor = 0, ypos = 300, yanchor = 0)
        if gramRow1_C_sound_right1==0:
            play sound gramTree1
            $gramRow1_C_sound_right1 +=1
        if (letterR3in3) and (letterJ6in4 or letterJ4in4 or letterJ7in4):
            image gram_m2_tile44 = "leftTreegreen.png"
            image gram_m2_tile45 = "1_1_green.png"

            show gram_m2_tile44 at Position(xpos = 1050, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile45 at Position(xpos = 1000, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m2_tile56 = "rightTreegreen.png"
            image gram_m2_tile57 = "1_1_green.png"
            image gram_m2_tile58 = "solutionLine.png"
            image gram_m2_tile209 = "solutionLine.png"
            image gram_m2_tile210 = "solutionLine.png"
            image gram_m2_tile59 = "a.png"
            show gram_m2_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile57 at Position(xpos = 1185, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m2_tile58 at Position(xpos = 1185, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m2_tile209 at Position(xpos = 1185, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m2_tile210 at Position(xpos = 1185, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m2_tile59 at Position(xpos = 1150, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_L_sound_right1 ==0:
                play sound gramTree1
                queue sound gramText3
                $gramRow2_L_sound_right1 +=1
            if (letterJ4in7 or letterJ6in7 or letterJ7in7):
                image gram_m2_tile50 = "leftTreegreenlong.png"
                image gram_m2_tile51 = "1_1_green.png"
                image gram_m2_tile52 = "solutionLine.png"
                image gram_m2_tile53 = "a.png"
                show gram_m2_tile50 at Position(xpos = 885, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m2_tile51 at Position(xpos = 845, xanchor = 0, ypos = 650, yanchor = 0)
                show gram_m2_tile52 at Position(xpos = 850, xanchor = 0, ypos = 750, yanchor = 0)
                show gram_m2_tile53 at Position(xpos = 820, xanchor = 0, ypos = 800, yanchor = 0)

                image gram_m2_tile46 = "solutionLine_grey.png"
                image gram_m2_tile47 = "solutionLine_grey.png"
                image gram_m2_tile48 = "solutionLine_grey.png"
                image gram_m2_tile207 = "solutionLine_grey.png"
                image gram_m2_tile49 = "epsilon.png"
                if gramRow3_C_sound_right1==0:
                    play sound gramTree1
                    queue sound gramText1
                    $gramRow3_C_sound_right1 +=1
                show gram_m2_tile44 at Position(xpos = 1050, xanchor = 0, ypos = 400, yanchor = 0)
                show gram_m2_tile45 at Position(xpos = 1000, xanchor = 0, ypos = 475, yanchor = 0)
                show gram_m2_tile46 at Position(xpos = 1005, xanchor = 0, ypos = 572, yanchor = 0)
                show gram_m2_tile47 at Position(xpos = 1005, xanchor = 0, ypos = 646, yanchor = 0)
                show gram_m2_tile48 at Position(xpos = 1005, xanchor = 0, ypos = 715, yanchor = 0)
                show gram_m2_tile207 at Position(xpos = 1005, xanchor = 0, ypos = 755, yanchor = 0)
                show gram_m2_tile49 at Position(xpos = 985, xanchor = 0, ypos = 800, yanchor = 0)
                    
            elif (letterK2in7):
                image gram_m2_tile01S = "leftTreeredlong.png"
                image gram_m2_tile02S = "1_1_red.png"
                show gram_m2_tile01S at Position(xpos = 885, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m2_tile02S at Position(xpos = 845, xanchor = 0, ypos = 650, yanchor = 0)
                if gramRow3_L_sound_wrong1 ==0:
                    play sound gramTree5
                    $gramRow3_L_sound_wrong1 +=1
                    
            if not(letterJ4in7 or letterJ6in7 or letterJ7in7):
                if gramRow3_C_sound_right1==1:
                    $gramRow3_C_sound_right1 -=1
                    
            if not(letterK2in7):
                if gramRow3_L_sound_wrong1 ==1:
                    $gramRow3_L_sound_wrong1 -=1
                    
        elif (letterK2in3 or letterJ4in3 or letterJ6in3 or letterJ7in3 or letterR3in3) and (letterK2in4 or letterR3in4 or letterJ4in4 or letterJ6in4 or letterJ7in4):
            image gram_m2_tile54 = "leftTreered.png"
            image gram_m2_tile55 = "1_1_red.png"
            show gram_m2_tile54 at Position(xpos = 1050, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile55 at Position(xpos = 1000, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_L_sound_wrong1 ==0:
                play sound gramTree5
                $gramRow2_L_sound_wrong1 +=1
            image gram_m2_tile60 = "rightTreered.png"
            image gram_m2_tile61 = "1_1_red.png"
            show gram_m2_tile60 at Position(xpos = 1170, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile61 at Position(xpos = 1185, xanchor = 0, ypos = 475, yanchor = 0)
        
        if not((letterR3in3) and (letterJ6in4 or letterJ4in4 or letterJ7in4)):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1

        if not((letterK2in3 or letterJ4in3 or letterJ6in3 or letterJ7in3 or letterR3in3) and (letterK2in4 or letterR3in4 or letterJ4in4 or letterJ6in4 or letterJ7in4)):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1
                
        if (letterJ4in5 or letterJ6in5 or letterJ7in5) and (letterK2in6):
            image gram_m2_tile64 = "leftTreegreen.png"
            image gram_m2_tile65 = "1_1_green.png"
            image gram_m2_tile66 = "solutionLine.png"
            image gram_m2_tile211 = "solutionLine.png"
            image gram_m2_tile212 = "solutionLine.png"
            image gram_m2_tile67 = "a.png"
            show gram_m2_tile64 at Position(xpos = 1370, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile65 at Position(xpos = 1325, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m2_tile66 at Position(xpos = 1330, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m2_tile211 at Position(xpos = 1330, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m2_tile212 at Position(xpos = 1330, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m2_tile67 at Position(xpos = 1310, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_R_sound_right1==0:
                play sound gramTree1
                queue sound gramText2
                $gramRow2_R_sound_right1 +=1
            image gram_m2_tile70 = "rightTreegreen.png"
            image gram_m2_tile71 = "1_1_green.png"
            image gram_m2_tile72 = "solutionLine.png"
            image gram_m2_tile213 = "solutionLine.png"
            image gram_m2_tile214 = "solutionLine.png"
            image gram_m2_tile73 = "b.png"
            show gram_m2_tile70 at Position(xpos = 1470, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile71 at Position(xpos = 1500, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m2_tile72 at Position(xpos = 1505, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m2_tile213 at Position(xpos = 1505, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m2_tile214 at Position(xpos = 1505, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m2_tile73 at Position(xpos = 1485, xanchor = 0, ypos = 800, yanchor = 0)
                
        elif (letterK2in5 or letterR3in5 or letterJ4in5 or letterJ6in5 or letterJ7in5) and (letterR3in6 or letterJ4in6 or letterJ6in6 or letterJ7in6 or letterK2in6):
            image gram_m2_tile68 = "leftTreered.png"
            image gram_m2_tile69 = "1_1_red.png"
            show gram_m2_tile68 at Position(xpos = 1370, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile69 at Position(xpos = 1325, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m2_tile74 = "rightTreered.png"
            image gram_m2_tile75 = "1_1_red.png"
            show gram_m2_tile74 at Position(xpos = 1470, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m2_tile75 at Position(xpos = 1500, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_R_sound_wrong1==0:
                play sound gramTree5
                $gramRow2_R_sound_wrong1 +=1
                
        if not((letterJ4in5 or letterJ6in5 or letterJ7in5) and (letterK2in6)):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
                
        if not((letterK2in5 or letterR3in5 or letterJ4in5 or letterJ6in5 or letterJ7in5) and (letterR3in6 or letterJ4in6 or letterJ6in6 or letterJ7in6 or letterK2in6)):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1

    elif (letterM1in1 or letterK2in1 or letterR3in1 or letterJ4in1 or letterT5in1 or letterJ6in1 or letterJ7in1) and (letterM1in2 or letterK2in2 or letterR3in2 or letterJ4in2 or letterT5in2 or letterJ6in2 or letterJ7in2):
        image gram_m2_tile90 = "leftTreeredlong.png"
        image gram_m2_tile91 = "1_1_red.png"
        show gram_m2_tile90 at Position(xpos = 1140, xanchor = 0, ypos = 225, yanchor = 0)
        show gram_m2_tile91 at Position(xpos = 1100, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m2_tile92 = "rightTreeredlong.png"
        image gram_m2_tile93 = "1_1_red.png"
        show gram_m2_tile92 at Position(xpos = 1310, xanchor = 0, ypos = 225, yanchor = 0)
        show gram_m2_tile93 at Position(xpos = 1400, xanchor = 0, ypos = 300, yanchor = 0)
        if gramRow1_C_sound_wrong1==0:
            play sound gramTree5
            $gramRow1_C_sound_wrong1 +=1
            
    if not((letterM1in1 or letterK2in1 or letterR3in1 or letterJ4in1 or letterT5in1 or letterJ6in1 or letterJ7in1) and (letterM1in2 or letterK2in2 or letterR3in2 or letterJ4in2 or letterT5in2 or letterJ6in2 or letterJ7in2)):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1  -=1
            
    if not(letterT5in1 and letterM1in2):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1


    #win conditions
    if (letterT5in1 == True) and (letterR3in3 == True) and (letterJ4in7 == True or letterJ6in7 == True or letterJ7in7 == True) and (letterJ6in4 == True or letterJ4in4 == True or letterJ7in4 == True) and letterM1in2 == True and (letterJ4in5 == True or letterJ6in5 == True or letterJ7in5 == True) and letterK2in6 == True: 
        image gram_m2_tile202 = "letterM.png"
        image gram_m2_tile206 = "letterK.png"
        image gram_m2_tile203 = "letterR.png"
        image gram_m2_tile205 = "letterJ.png"
        image gram_m2_tile201 = "letterT.png"
        image gram_m2_tile204 = "letterJ.png"
        image gram_m2_tile208 = "letterJ.png"
        
        show gram_m2_tile202 at Position(xpos = letterM1x, xanchor = 0, ypos = letterM1y, yanchor = 0)
        show gram_m2_tile206 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
        show gram_m2_tile203 at Position(xpos = letterR3x, xanchor = 0, ypos = letterR3y, yanchor = 0)
        show gram_m2_tile205 at Position(xpos = letterJ4x, xanchor = 0, ypos = letterJ4y, yanchor = 0)
        show gram_m2_tile201 at Position(xpos = letterT5x, xanchor = 0, ypos = letterT5y, yanchor = 0)
        show gram_m2_tile204 at Position(xpos = letterJ6x, xanchor = 0, ypos = letterJ6y, yanchor = 0)
        show gram_m2_tile208 at Position(xpos = letterJ7x, xanchor = 0, ypos = letterJ7y, yanchor = 0)
        queue sound gramWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramMedWin
        jump gramMed_win

    if attempts ==0:
        show gram_m2_tile202 at Position(xpos = letterM1x, xanchor = 0, ypos = letterM1y, yanchor = 0)
        show gram_m2_tile206 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
        show gram_m2_tile203 at Position(xpos = letterR3x, xanchor = 0, ypos = letterR3y, yanchor = 0)
        show gram_m2_tile205 at Position(xpos = letterJ4x, xanchor = 0, ypos = letterJ4y, yanchor = 0)
        show gram_m2_tile201 at Position(xpos = letterT5x, xanchor = 0, ypos = letterT5y, yanchor = 0)
        show gram_m2_tile204 at Position(xpos = letterJ6x, xanchor = 0, ypos = letterJ6y, yanchor = 0)
        show gram_m2_tile208 at Position(xpos = letterJ7x, xanchor = 0, ypos = letterJ7y, yanchor = 0)
        queue sound gramLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_gramMedLose
        $gramMed_attempts +=1
        jump gramMed_lose #start
    
    jump gamefile_m2