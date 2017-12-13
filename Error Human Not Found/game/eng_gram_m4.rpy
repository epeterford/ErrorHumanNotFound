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

screen logicGates_med4:
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
        action Jump("hints_gramMed_4")
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
                drag_name "letterS2"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS3x ypos letterS3y
        drag:
                drag_name "letterT2"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT4x ypos letterT4y
        drag:
                drag_name "letterS"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS5x ypos letterS5y
        drag:
                drag_name "letterA"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA6x ypos letterA6y
        drag:
                drag_name "letterA2"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA7x ypos letterA7y

        drag:
                drag_name "letterM2"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterM8x ypos letterM8y
        
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
                xpos 1095 ypos 660

        drag:
                drag_name "gate slot eight"
                draggable False
                child "images/border.png"
                xpos 1250 ypos 660

         #letter dragback
        
        drag:
                drag_name "LetterT_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterM_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterA_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterS_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738

init:
    image bg Eng_gram_m4_tile = "eng_tile_bg.png"

label gram_m4:#start:
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg Eng_gram_m4_tile

    #row1 1-4
    image gram_m4_tile0 = "instructions9.png"
    image gram_m4_tile1 = "1_1_green.png"
    image gram_m4_tile2 = "letterS.png"
    #image gram_m4_tile3 = "treeGrey.png"
    show gram_m4_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_m4_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 130, yanchor = 0)
    show gram_m4_tile2 at Position(xpos = 1260, xanchor = 0, ypos = 145, yanchor = 0)
    #show gram_m4_tile3 at Position(xpos = 1248, xanchor = 0, ypos = 228, yanchor = 0)
    
    #row2 5-8
    #image gram_m4_tile4 = "1_1_grey.png"
    image gram_m4_tile5 = "leftTreelong1.png"
    image gram_m4_tile6 = "rightTreelong1.png"
    #show gram_m4_tile4 at Position(xpos = 1250, xanchor = 0, ypos = 270, yanchor = 0)
    show gram_m4_tile5 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
    show gram_m4_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
    
    #row3 9-13   

    image gram_m4_tile9 = "1_1_grey.png"
    image gram_m4_tile10 = "1_1_grey.png"
    

    show gram_m4_tile9 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)
    show gram_m4_tile10 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    #row4 14-20

    image gram_m4_tile14 = "leftTreelong.png"
    #image gram_m4_tile14 = "leftTreelong.png"
    image gram_m4_tile15 = "rightTreelong.png"
    image gram_m4_tile16 = "leftTreelong.png"
    image gram_m4_tile17 = "rightTreelong.png"

    show gram_m4_tile14 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
    #show gram_m4_tile14 at Position(xpos = 1000, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m4_tile15 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m4_tile16 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
    show gram_m4_tile17 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)


    #row5 21-27

    image gram_m4_tile21 = "1_1_grey.png"
    image gram_m4_tile22 = "1_1_grey.png"
    image gram_m4_tile23 = "1_1_grey.png"
    image gram_m4_tile24 = "1_1_grey.png"

    show gram_m4_tile21 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m4_tile22 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m4_tile23 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)
    show gram_m4_tile24 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)

    image gram_m4_tile25 = "leftTree.png"
    image gram_m4_tile26 = "1_1_grey.png"
    show gram_m4_tile25 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m4_tile26 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m4_tile27 = "rightTree.png"
    image gram_m4_tile28 = "1_1_grey.png"
    show gram_m4_tile27 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
    show gram_m4_tile28 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)

    image gram_m4_tile31 = "letterBorder.png"
    image gram_m4_tile32 = "letterBorder.png"
    #image gram_m4_tile33 = "letterBorder.png"
    image gram_m4_tile34 = "letterBorder.png"
    image gram_m4_tile35 = "letterBorder.png"
    #image gram_m4_tile36 = "letterBorder.png"
    show gram_m4_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show gram_m4_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    #show gram_m4_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show gram_m4_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show gram_m4_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    #show gram_m4_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)

    #transparent letters for dragbacks
    image eaeng_m4_tile300 = "letterT_grey.png"
    image eaeng_m4_tile301 = "letterM_grey.png"
    image eaeng_m4_tile303 = "letterA_grey.png"
    image eaeng_m4_tile304 = "letterS_grey.png"
    show eaeng_m4_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_m4_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_m4_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_m4_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)


    # gates
    $ letterT1x = 275 
    $ letterT1y = 575
    $ letterM2x = 410
    $ letterM2y = 575
    $ letterS3x = 410 
    $ letterS3y = 750
    $ letterT4x = 275
    $ letterT4y = 575
    $ letterS5x = 410
    $ letterS5y = 750
    $ letterA6x = 275 
    $ letterA6y = 750
    $ letterA7x = 275 
    $ letterA7y = 750
    $ letterM8x = 410 
    $ letterM8y = 575

    # check conditons for locations
    $ letterT1in1 = False
    $ letterT1in2 = False
    $ letterT1in3 = False
    $ letterT1in4 = False
    $ letterT1in5 = False
    $ letterT1in6 = False
    $ letterT1in7 = False
    $ letterT1in8 = False

    $ letterM2in1 = False
    $ letterM2in2 = False
    $ letterM2in3 = False
    $ letterM2in4 = False
    $ letterM2in5 = False
    $ letterM2in6 = False
    $ letterM2in7 = False
    $ letterM2in8 = False

    $ letterS3in1 = False
    $ letterS3in2 = False
    $ letterS3in3 = False
    $ letterS3in4 = False
    $ letterS3in5 = False
    $ letterS3in6 = False
    $ letterS3in7 = False
    $ letterS3in8 = False

    $ letterT4in1 = False
    $ letterT4in2 = False
    $ letterT4in3 = False
    $ letterT4in4 = False
    $ letterT4in5 = False
    $ letterT4in6 = False
    $ letterT4in7 = False
    $ letterT4in8 = False

    $ letterS5in1 = False
    $ letterS5in2 = False
    $ letterS5in3 = False
    $ letterS5in4 = False
    $ letterS5in5 = False
    $ letterS5in6 = False
    $ letterS5in7 = False
    $ letterS5in8 = False

    $ letterA6in1 = False
    $ letterA6in2 = False
    $ letterA6in3 = False
    $ letterA6in4 = False
    $ letterA6in5 = False
    $ letterA6in6 = False
    $ letterA6in7 = False
    $ letterA6in8 = False

    $ letterA7in1 = False
    $ letterA7in2 = False
    $ letterA7in3 = False
    $ letterA7in4 = False
    $ letterA7in5 = False
    $ letterA7in6 = False
    $ letterA7in7 = False
    $ letterA7in8 = False

    $ letterM8in1 = False
    $ letterM8in2 = False
    $ letterM8in3 = False
    $ letterM8in4 = False
    $ letterM8in5 = False
    $ letterM8in6 = False
    $ letterM8in7 = False
    $ letterM8in8 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 11
    
    call gamefile_m4 from _call_gamefile_m4

label gamefile_m4:
    #image moon = "images/blankgram_m4_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGates_med4

    if gate_name == "letterT":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_m4_tile here
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False
            #sets values for checks
            $ letterT1x = 1025
            $ letterT1y = 315
            $ letterT1in1 = True
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterT1x = 1505
            $ letterT1y = 315
            $ letterT1in1 = False
            $ letterT1in2 = True
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterT1x = 875
            $ letterT1y = 490
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = True
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterT1x = 1175
            $ letterT1y = 490
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = True
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterT1x = 1355
            $ letterT1y = 490
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = True
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterT1x = 1655
            $ letterT1y = 490
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = True
            $ letterT1in7 = False
            $ letterT1in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterT1x = 1095
            $ letterT1y = 665
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = True
            $ letterT1in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterT1x = 1250
            $ letterT1y = 665
            $ letterT1in1 = False
            $ letterT1in2 = False
            $ letterT1in3 = False
            $ letterT1in4 = False
            $ letterT1in5 = False
            $ letterT1in6 = False
            $ letterT1in7 = False
            $ letterT1in8 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

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

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

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
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

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

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

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


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterM2x = 1355
            $ letterM2y = 490
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = True
            $ letterM2in6 = False
            $ letterM2in7 = False
            $ letterM2in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterM2x = 1655
            $ letterM2y = 490
            $ letterM2in1 = False
            $ letterM2in2 = False
            $ letterM2in3 = False
            $ letterM2in4 = False
            $ letterM2in5 = False
            $ letterM2in6 = True
            $ letterM2in7 = False
            $ letterM2in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

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

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

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

    if gate_name == "letterS2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

            #sets values for checks
            $ letterS3x = 1025
            $ letterS3y = 315
            $ letterS3in1 = True
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
            $ letterS3in7 = False
            $ letterS3in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterS3x = 1505
            $ letterS3y = 315
            $ letterS3in1 = False
            $ letterS3in2 = True
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
            $ letterS3in7 = False
            $ letterS3in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterS3x = 875
            $ letterS3y = 490
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = True
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
            $ letterS3in7 = False
            $ letterS3in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterS3x = 1175
            $ letterS3y = 490
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = True
            $ letterS3in5 = False
            $ letterS3in6 = False
            $ letterS3in7 = False
            $ letterS3in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterS3x = 1355
            $ letterS3y = 490
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = True
            $ letterS3in6 = False
            $ letterS3in7 = False
            $ letterS3in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterS3x = 1655
            $ letterS3y = 490
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = True
            $ letterS3in7 = False
            $ letterS3in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterS3x = 1095
            $ letterS3y = 665
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
            $ letterS3in7 = True
            $ letterS3in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterS3x = 1250
            $ letterS3y = 665
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
            $ letterS3in7 = False
            $ letterS3in8 = True


    if gate_name == "letterT2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

            #sets values for checks
            $ letterT4x = 1025
            $ letterT4y = 315
            $ letterT4in1 = True
            $ letterT4in2 = False
            $ letterT4in3 = False
            $ letterT4in4 = False
            $ letterT4in5 = False
            $ letterT4in6 = False
            $ letterT4in7 = False
            $ letterT4in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterT4x = 1505
            $ letterT4y = 315
            $ letterT4in1 = False
            $ letterT4in2 = True
            $ letterT4in3 = False
            $ letterT4in4 = False
            $ letterT4in5 = False
            $ letterT4in6 = False
            $ letterT4in7 = False
            $ letterT4in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterT4x = 875
            $ letterT4y = 490
            $ letterT4in1 = False
            $ letterT4in2 = False
            $ letterT4in3 = True
            $ letterT4in4 = False
            $ letterT4in5 = False
            $ letterT4in6 = False
            $ letterT4in7 = False
            $ letterT4in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterT4x = 1175
            $ letterT4y = 490
            $ letterT4in1 = False
            $ letterT4in2 = False
            $ letterT4in3 = False
            $ letterT4in4 = True
            $ letterT4in5 = False
            $ letterT4in6 = False
            $ letterT4in7 = False
            $ letterT4in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterT4x = 1355
            $ letterT4y = 490
            $ letterT4in1 = False
            $ letterT4in2 = False
            $ letterT4in3 = False
            $ letterT4in4 = False
            $ letterT4in5 = True
            $ letterT4in6 = False
            $ letterT4in7 = False
            $ letterT4in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterT4x = 1655
            $ letterT4y = 490
            $ letterT4in1 = False
            $ letterT4in2 = False
            $ letterT4in3 = False
            $ letterT4in4 = False
            $ letterT4in5 = False
            $ letterT4in6 = True
            $ letterT4in7 = False
            $ letterT4in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterT4x = 1095
            $ letterT4y = 665
            $ letterT4in1 = False
            $ letterT4in2 = False
            $ letterT4in3 = False
            $ letterT4in4 = False
            $ letterT4in5 = False
            $ letterT4in6 = False
            $ letterT4in7 = True
            $ letterT4in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterT4x = 1250
            $ letterT4y = 665
            $ letterT4in1 = False
            $ letterT4in2 = False
            $ letterT4in3 = False
            $ letterT4in4 = False
            $ letterT4in5 = False
            $ letterT4in6 = False
            $ letterT4in7 = False
            $ letterT4in8 = True


    if gate_name == "letterS":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

            #sets values for checks
            $ letterS5x = 1025
            $ letterS5y = 315
            $ letterS5in1 = True
            $ letterS5in2 = False
            $ letterS5in3 = False
            $ letterS5in4 = False
            $ letterS5in5 = False
            $ letterS5in6 = False
            $ letterS5in7 = False
            $ letterS5in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterS5x = 1505
            $ letterS5y = 315
            $ letterS5in1 = False
            $ letterS5in2 = True
            $ letterS5in3 = False
            $ letterS5in4 = False
            $ letterS5in5 = False
            $ letterS5in6 = False
            $ letterS5in7 = False
            $ letterS5in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterS5x = 875
            $ letterS5y = 490
            $ letterS5in1 = False
            $ letterS5in2 = False
            $ letterS5in3 = True
            $ letterS5in4 = False
            $ letterS5in5 = False
            $ letterS5in6 = False
            $ letterS5in7 = False
            $ letterS5in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterS5x = 1175
            $ letterS5y = 490
            $ letterS5in1 = False
            $ letterS5in2 = False
            $ letterS5in3 = False
            $ letterS5in4 = True
            $ letterS5in5 = False
            $ letterS5in6 = False
            $ letterS5in7 = False
            $ letterS5in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterS5x = 1355
            $ letterS5y = 490
            $ letterS5in1 = False
            $ letterS5in2 = False
            $ letterS5in3 = False
            $ letterS5in4 = False
            $ letterS5in5 = True
            $ letterS5in6 = False
            $ letterS5in7 = False
            $ letterS5in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterS5x = 1655
            $ letterS5y = 490
            $ letterS5in1 = False
            $ letterS5in2 = False
            $ letterS5in3 = False
            $ letterS5in4 = False
            $ letterS5in5 = False
            $ letterS5in6 = True
            $ letterS5in7 = False
            $ letterS5in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterS5x = 1095
            $ letterS5y = 665
            $ letterS5in1 = False
            $ letterS5in2 = False
            $ letterS5in3 = False
            $ letterS5in4 = False
            $ letterS5in5 = False
            $ letterS5in6 = False
            $ letterS5in7 = True
            $ letterS5in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterS5x = 1250
            $ letterS5y = 665
            $ letterS5in1 = False
            $ letterS5in2 = False
            $ letterS5in3 = False
            $ letterS5in4 = False
            $ letterS5in5 = False
            $ letterS5in6 = False
            $ letterS5in7 = False
            $ letterS5in8 = True

    if gate_name == "letterA":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

            #sets values for checks
            $ letterA6x = 1025
            $ letterA6y = 315
            $ letterA6in1 = True
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterA6x = 1505
            $ letterA6y = 315
            $ letterA6in1 = False
            $ letterA6in2 = True
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterA6x = 875
            $ letterA6y = 490
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = True
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterA6x = 1175
            $ letterA6y = 490
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = True
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterA6x = 1355
            $ letterA6y = 490
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = True
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterA6x = 1655
            $ letterA6y = 490
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = True
            $ letterA6in7 = False
            $ letterA6in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterA6x = 1095
            $ letterA6y = 665
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = True
            $ letterA6in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterA6x = 1250
            $ letterA6y = 665
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
            $ letterA6in8 = True

    if gate_name == "letterA2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

            #sets values for checks
            $ letterA7x = 1025
            $ letterA7y = 315
            $ letterA7in1 = True
            $ letterA7in2 = False
            $ letterA7in3 = False
            $ letterA7in4 = False
            $ letterA7in5 = False
            $ letterA7in6 = False
            $ letterA7in7 = False
            $ letterA7in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterA7x = 1505
            $ letterA7y = 315
            $ letterA7in1 = False
            $ letterA7in2 = True
            $ letterA7in3 = False
            $ letterA7in4 = False
            $ letterA7in5 = False
            $ letterA7in6 = False
            $ letterA7in7 = False
            $ letterA7in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterA7x = 875
            $ letterA7y = 490
            $ letterA7in1 = False
            $ letterA7in2 = False
            $ letterA7in3 = True
            $ letterA7in4 = False
            $ letterA7in5 = False
            $ letterA7in6 = False
            $ letterA7in7 = False
            $ letterA7in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterA7x = 1175
            $ letterA7y = 490
            $ letterA7in1 = False
            $ letterA7in2 = False
            $ letterA7in3 = False
            $ letterA7in4 = True
            $ letterA7in5 = False
            $ letterA7in6 = False
            $ letterA7in7 = False
            $ letterA7in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterA7x = 1355
            $ letterA7y = 490
            $ letterA7in1 = False
            $ letterA7in2 = False
            $ letterA7in3 = False
            $ letterA7in4 = False
            $ letterA7in5 = True
            $ letterA7in6 = False
            $ letterA7in7 = False
            $ letterA7in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterA7x = 1655
            $ letterA7y = 490
            $ letterA7in1 = False
            $ letterA7in2 = False
            $ letterA7in3 = False
            $ letterA7in4 = False
            $ letterA7in5 = False
            $ letterA7in6 = True
            $ letterA7in7 = False
            $ letterA7in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterA7x = 1095
            $ letterA7y = 665
            $ letterA7in1 = False
            $ letterA7in2 = False
            $ letterA7in3 = False
            $ letterA7in4 = False
            $ letterA7in5 = False
            $ letterA7in6 = False
            $ letterA7in7 = True
            $ letterA7in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterA7x = 1250
            $ letterA7y = 665
            $ letterA7in1 = False
            $ letterA7in2 = False
            $ letterA7in3 = False
            $ letterA7in4 = False
            $ letterA7in5 = False
            $ letterA7in6 = False
            $ letterA7in7 = False
            $ letterA7in8 = True

    if gate_name == "letterM2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterT1in1 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in1 = False
            if letterM2in1 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in1 = False
            if letterS3in1 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in1 = False
            if letterT4in1 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in1 = False
            if letterS5in1 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterA7in1 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in1 = False
            if letterM8in1 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in1 = False

            #sets values for checks
            $ letterM8x = 1025
            $ letterM8y = 315
            $ letterM8in1 = True
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterT1in2 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in2 = False
            if letterM2in2 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in2 = False
            if letterS3in2 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in2 = False
            if letterT4in2 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in2 = False
            if letterS5in2 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterA7in2 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in2 = False
            if letterM8in2 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in2 = False

            #sets check values
            $ letterM8x = 1505
            $ letterM8y = 315
            $ letterM8in1 = False
            $ letterM8in2 = True
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterT1in3 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in3 = False
            if letterM2in3 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in3 = False
            if letterS3in3 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in3 = False
            if letterT4in3 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in3 = False
            if letterS5in3 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterA7in3 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in3 = False
            if letterM8in3 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in3 = False

            #sets values for the checks
            $ letterM8x = 875
            $ letterM8y = 490
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = True
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterT1in4 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in4 = False
            if letterM2in4 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in4 = False
            if letterS3in4 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in4 = False
            if letterT4in4 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in4 = False
            if letterS5in4 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterA7in4 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in4 = False
            if letterM8in4 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in4 = False

            #sets values for the checks
            $ letterM8x = 1175
            $ letterM8y = 490
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = True
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterT1in5 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in5 = False
            if letterM2in5 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in5 = False
            if letterS3in5 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in5 = False
            if letterT4in5 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in5 = False
            if letterS5in5 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterA7in5 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in5 = False
            if letterM8in5 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in5 = False

            #sets values for the checks
            $ letterM8x = 1355
            $ letterM8y = 490
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = True
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterT1in6 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in6 = False
            if letterM2in6 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in6 = False
            if letterS3in6 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in6 = False
            if letterT4in6 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in6 = False
            if letterS5in6 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterA7in6 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in6 = False
            if letterM8in6 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in6 = False

            #sets values for the checks
            $ letterM8x = 1655
            $ letterM8y = 490
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = True
            $ letterM8in7 = False
            $ letterM8in8 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterT1in7 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in7 = False
            if letterM2in7 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in7 = False
            if letterS3in7 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in7 = False
            if letterT4in7 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in7 = False
            if letterS5in7 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterA7in7 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in7 = False
            if letterM8in7 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in7 = False

            #sets values for the checks
            $ letterM8x = 1095
            $ letterM8y = 665
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = True
            $ letterM8in8 = False

                #gate slot number 8******************************
        if slot_name == "gate slot eight":
            if letterT1in8 == True:
               $ letterT1x = 275
               $ letterT1y = 575
               $ letterT1in8 = False
            if letterM2in8 == True:
               $ letterM2x = 410
               $ letterM2y = 575
               $ letterM2in8 = False
            if letterS3in8 == True:
               $ letterS3x = 410
               $ letterS3y = 750
               $ letterS3in8 = False
            if letterT4in8 == True:
               $ letterT4x = 275
               $ letterT4y = 575
               $ letterT4in8 = False
            if letterS5in8 == True:
               $ letterS5x = 410
               $ letterS5y = 750
               $ letterS5in8 = False
            if letterA6in8 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in8 = False
            if letterA7in8 == True:
               $ letterA7x = 275
               $ letterA7y = 750
               $ letterA7in8 = False
            if letterM8in8 == True:
               $ letterM8x = 410
               $ letterM8y = 575
               $ letterM8in8 = False

            #sets values for the checks
            $ letterM8x = 1250
            $ letterM8y = 665
            $ letterM8in1 = False
            $ letterM8in2 = False
            $ letterM8in3 = False
            $ letterM8in4 = False
            $ letterM8in5 = False
            $ letterM8in6 = False
            $ letterM8in7 = False
            $ letterM8in8 = True

 #Dragbacks
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "LetterT_return" or slot_name == "LetterM_return" or slot_name == "LetterS_return" or slot_name == "LetterA_return")):
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
                if gate_name == "letterT":
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
                if gate_name == "letterT2":
                    $ letterT4x = 275
                    $ letterT4y = 575
                    $ letterT4in1 = False
                    $ letterT4in2 = False
                    $ letterT4in3 = False
                    $ letterT4in4 = False
                    $ letterT4in5 = False
                    $ letterT4in6 = False
                    $ letterT4in7 = False
                    $ letterT4in8 = False
   
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ letterM2x = 410
                    $ letterM2y = 575
                    $ letterM2in1 = False
                    $ letterM2in2 = False
                    $ letterM2in3 = False
                    $ letterM2in4 = False
                    $ letterM2in5 = False
                    $ letterM2in6 = False
                    $ letterM2in7 = False
                    $ letterM2in8 = False
                
                if gate_name == "letterM2":
                    $ letterM8x = 410
                    $ letterM8y = 575
                    $ letterM8in1 = False
                    $ letterM8in2 = False
                    $ letterM8in3 = False
                    $ letterM8in4 = False
                    $ letterM8in5 = False
                    $ letterM8in6 = False
                    $ letterM8in7 = False
                    $ letterM8in8 = False
            
            if slot_name == "LetterS_return":
                $ attempts +=1
                if gate_name == "letterS2":
                    $ letterS3x = 410
                    $ letterS3y = 750
                    $ letterS3in1 = False
                    $ letterS3in2 = False
                    $ letterS3in3 = False
                    $ letterS3in4 = False
                    $ letterS3in5 = False
                    $ letterS3in6 = False
                    $ letterS3in7 = False
                    $ letterS3in8 = False
                
                if gate_name == "letterS":
                    $ letterS5x = 410
                    $ letterS5y = 750
                    $ letterS5in1 = False
                    $ letterS5in2 = False
                    $ letterS5in3 = False
                    $ letterS5in4 = False
                    $ letterS5in5 = False
                    $ letterS5in6 = False
                    $ letterS5in7 = False
                    $ letterS5in8 = False

            if slot_name == "LetterA_return":
                $ attempts +=1
                if gate_name == "letterA":
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
                    
                if gate_name == "letterA2":
                    $ letterA7x = 275
                    $ letterA7y = 750
                    $ letterA7in1 = False
                    $ letterA7in2 = False
                    $ letterA7in3 = False
                    $ letterA7in4 = False
                    $ letterA7in5 = False
                    $ letterA7in6 = False
                    $ letterA7in7 = False
                    $ letterA7in8 = False


    #START SOUNDS HERE
    hide gram_m4_tile42
    hide gram_m4_tile43
    hide gram_m4_tile44
    hide gram_m4_tile45
    hide gram_m4_tile46
    hide gram_m4_tile47
    hide gram_m4_tile48
    hide gram_m4_tile207
    hide gram_m4_tile49
    hide gram_m4_tile50
    hide gram_m4_tile51
    hide gram_m4_tile52
    hide gram_m4_tile53
    hide gram_m4_tile54
    hide gram_m4_tile55 
    hide gram_m4_tile215
    hide gram_m4_tile216
    hide gram_m4_tile210
    hide gram_m4_tile59
    hide gram_m4_tile260
    hide gram_m4_tile261
    hide gram_m4_tile262
    hide gram_m4_tile263
    hide gram_m4_tile56
    hide gram_m4_tile57
    hide gram_m4_tile210
    hide gram_m4_tile59
    hide gram_m4_tile60
    hide gram_m4_tile61
    hide gram_m4_tile62
    hide gram_m4_tile61
    hide gram_m4_tile62
    hide gram_m4_tile63
    hide gram_m4_tile64
    hide gram_m4_tile65
    hide gram_m4_tile66
    hide gram_m4_tile211
    hide gram_m4_tile212
    hide gram_m4_tile67
    hide gram_m4_tile68
    hide gram_m4_tile69
    hide gram_m4_tile70
    hide gram_m4_tile71
    hide gram_m4_tile72
    hide gram_m4_tile213
    hide gram_m4_tile214
    hide gram_m4_tile73
    hide gram_m4_tile74
    hide gram_m4_tile75
    hide gram_m4_tile90
    hide gram_m4_tile91

    hide gram_m4_tile92
    hide gram_m4_tile93
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if ((letterS5in1 or letterS3in1 ) and (letterT1in2 or letterT4in2)):
        image gram_m4_tile42 = "leftTreegreenlong1.png"
        image gram_m4_tile43 = "1_1_green.png"
        show gram_m4_tile42 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m4_tile43 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m4_tile62 = "rightTreegreenlong1.png"
        image gram_m4_tile63 = "1_1_green.png"
        show gram_m4_tile62 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m4_tile63 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)
        if gramRow1_C_sound_right1==0:
            $gramRow1_C_sound_right1 +=1
            play sound gramTree1
        if (letterS3in3 or letterS5in3) and (letterT1in4 or letterT4in4):
            image gram_m4_tile44 = "leftTreegreenlong.png"
            image gram_m4_tile45 = "1_1_green.png"
            image gram_m4_tile46 = "solutionLine_grey.png"
            image gram_m4_tile47 = "solutionLine_grey.png"
            image gram_m4_tile48 = "solutionLine_grey.png"
            image gram_m4_tile207 = "solutionLine_grey.png"
            image gram_m4_tile49 = "epsilon.png"

            show gram_m4_tile44 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile45 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m4_tile46 at Position(xpos = 860, xanchor = 0, ypos = 572, yanchor = 0)
            show gram_m4_tile47 at Position(xpos = 860, xanchor = 0, ypos = 646, yanchor = 0)
            show gram_m4_tile48 at Position(xpos = 860, xanchor = 0, ypos = 715, yanchor = 0)
            show gram_m4_tile207 at Position(xpos = 860, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m4_tile49 at Position(xpos = 835, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_m4_tile56 = "rightTreegreenlong.png"
            image gram_m4_tile57 = "1_1_green.png"
            show gram_m4_tile56 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile57 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_L_sound_right1 == 0:
                play sound gramTree1
                queue sound gramText3
                $gramRow2_L_sound_right1 +=1
            if (letterA6in7 or letterA7in7) and (letterM2in8 or letterM8in8):
                image gram_m4_tile50 = "leftTreegreen.png"
                image gram_m4_tile51 = "1_1_green.png"
                image gram_m4_tile52 = "solutionLine.png"
                image gram_m4_tile53 = "a.png"
                show gram_m4_tile50 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m4_tile51 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)
                show gram_m4_tile52 at Position(xpos = 1070, xanchor = 0, ypos = 750, yanchor = 0)
                show gram_m4_tile53 at Position(xpos = 1030, xanchor = 0, ypos = 800, yanchor = 0)

                image gram_m4_tile215 = "rightTreegreen.png"
                image gram_m4_tile216 = "1_1_green.png"
                show gram_m4_tile215 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m4_tile216 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)
                image gram_m4_tile210 = "solutionLine.png"
                image gram_m4_tile59 = "b.png"
                show gram_m4_tile210 at Position(xpos = 1230, xanchor = 0, ypos = 750, yanchor = 0)
                show gram_m4_tile59 at Position(xpos = 1185, xanchor = 0, ypos = 800, yanchor = 0)
                if gramRow3_C_sound_right1 ==0:
                    $gramRow3_C_sound_right1 +=1
                    play sound gramTree1
                    queue sound gramText1

            elif (letterM2in7 or letterA6in7 or letterA7in7 or letterM8in7) and (letterA6in8 or letterA7in8 or letterM2in8 or letterM8in8):
                image gram_m4_tile260 = "leftTreered.png"
                image gram_m4_tile261 = "1_1_red.png"
                show gram_m4_tile260 at Position(xpos = 1120, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m4_tile261 at Position(xpos = 1080, xanchor = 0, ypos = 650, yanchor = 0)
                image gram_m4_tile262 = "rightTreered.png"
                image gram_m4_tile263 = "1_1_red.png"
                show gram_m4_tile262 at Position(xpos = 1220, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m4_tile263 at Position(xpos = 1235, xanchor = 0, ypos = 650, yanchor = 0)
                if gramRow3_C_sound_wrong1==0:
                    $gramRow3_C_sound_wrong1 +=1
                    play sound gramTree5
            if not((letterM2in7 or letterA6in7 or letterA7in7 or letterM8in7) and (letterA6in8 or letterA7in8 or letterM2in8 or letterM8in8)):
                if gramRow3_C_sound_wrong1 ==1:
                    $gramRow3_C_sound_wrong1 -=1
            if not((letterA6in7 or letterA7in7) and (letterM2in8 or letterM8in8)):
               if gramRow3_C_sound_right1 == 1:
                   $gramRow3_C_sound_right1 -=1
        
        elif (letterT1in3 or letterM2in3 or letterS3in3 or letterT4in3 or letterS5in3 or letterA6in3 or letterA7in3 or letterM8in3) and (letterT1in4 or letterM2in4 or letterS3in4 or letterT4in4 or letterS5in4 or letterA6in4 or letterA7in4 or letterM8in4):
            image gram_m4_tile54 = "leftTreeredlong.png"
            image gram_m4_tile55 = "1_1_red.png"
            show gram_m4_tile54 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile55 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m4_tile60 = "rightTreeredlong.png"
            image gram_m4_tile61 = "1_1_red.png"
            show gram_m4_tile60 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile61 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_L_sound_wrong1 ==0:
                $gramRow2_L_sound_wrong1 +=1
                play sound gramTree5
                
        if not((letterT1in3 or letterM2in3 or letterS3in3 or letterT4in3 or letterS5in3 or letterA6in3 or letterA7in3 or letterM8in3) and (letterT1in4 or letterM2in4 or letterS3in4 or letterT4in4 or letterS5in4 or letterA6in4 or letterA7in4 or letterM8in4)):
            if gramRow2_L_sound_wrong1==1:
                $gramRow2_L_sound_wrong1 -=1
                
        if not((letterS3in3 or letterS5in3) and (letterT1in4 or letterT4in4)):
            if gramRow2_L_sound_right1 == 1:
                $gramRow2_L_sound_right1 -=1

        if (letterA6in5 or letterA7in5) and (letterM2in6 or letterM8in6):
            image gram_m4_tile64 = "leftTreegreenlong.png"
            image gram_m4_tile65 = "1_1_green.png"
            image gram_m4_tile66 = "solutionLine.png"
            image gram_m4_tile211 = "solutionLine.png"
            image gram_m4_tile212 = "solutionLine.png"
            image gram_m4_tile67 = "a.png"
            show gram_m4_tile64 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile65 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m4_tile66 at Position(xpos = 1350, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m4_tile211 at Position(xpos = 1350, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m4_tile212 at Position(xpos = 1350, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m4_tile67 at Position(xpos = 1345, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_m4_tile70 = "rightTreegreenlong.png"
            image gram_m4_tile71 = "1_1_green.png"
            image gram_m4_tile72 = "solutionLine.png"
            image gram_m4_tile213 = "solutionLine.png"
            image gram_m4_tile214 = "solutionLine.png"
            image gram_m4_tile73 = "b.png"
            show gram_m4_tile70 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile71 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m4_tile72 at Position(xpos = 1640, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m4_tile213 at Position(xpos = 1640, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m4_tile214 at Position(xpos = 1640, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m4_tile73 at Position(xpos = 1620, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_R_sound_right1==0:
                $gramRow2_R_sound_right1 +=1
                play sound gramTree1
                queue sound gramText2

        elif (letterT1in5 or letterM2in5 or letterS3in5 or letterT4in5 or letterS5in5 or letterA6in5 or letterA7in5 or letterM8in5) and (letterT1in6 or letterM2in6 or letterS3in6 or letterT4in6 or letterS5in6 or letterA6in6 or letterA7in6 or letterM8in6):
            image gram_m4_tile68 = "leftTreeredlong.png"
            image gram_m4_tile69 = "1_1_red.png"
            show gram_m4_tile68 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile69 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m4_tile74 = "rightTreeredlong.png"
            image gram_m4_tile75 = "1_1_red.png"
            show gram_m4_tile74 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m4_tile75 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_R_sound_wrong1 ==0:
                $gramRow2_R_sound_wrong1 +=1
                play sound gramTree5
                
        if not((letterA6in5 or letterA7in5) and (letterM2in6 or letterM8in6)):
            if gramRow2_R_sound_right1==1:
                $gramRow2_R_sound_right-=1
                
        if not((letterT1in5 or letterM2in5 or letterS3in5 or letterT4in5 or letterS5in5 or letterA6in5 or letterA7in5 or letterM8in5) and (letterT1in6 or letterM2in6 or letterS3in6 or letterT4in6 or letterS5in6 or letterA6in6 or letterA7in6 or letterM8in6)):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1

    elif ((letterT1in1 or letterM2in1 or letterS3in1 or letterT4in1 or letterS5in1 or letterA6in1 or letterA7in1 or letterM8in1) and (letterT1in2 or letterM2in2 or letterS3in2 or letterT4in2 or letterS5in2 or letterA6in2 or letterA7in2 or letterM8in2)):
        image gram_m4_tile90 = "leftTreeredlong1.png"
        image gram_m4_tile91 = "1_1_red.png"
        show gram_m4_tile90 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m4_tile91 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m4_tile92 = "rightTreeredlong1.png"
        image gram_m4_tile93 = "1_1_red.png"
        show gram_m4_tile92 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m4_tile93 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)
        if gramRow1_C_sound_wrong1 == 0:
            $gramRow1_C_sound_wrong1 +=1
            play sound gramTree5
    if not((letterT1in1 or letterM2in1 or letterS3in1 or letterT4in1 or letterS5in1 or letterA6in1 or letterA7in1 or letterM8in1) and (letterT1in2 or letterM2in2 or letterS3in2 or letterT4in2 or letterS5in2 or letterA6in2 or letterA7in2 or letterM8in2)):
        if gramRow1_C_sound_wrong1==1:
            $gramRow1_C_sound_wrong1 -=1
            
    if not((letterS5in1 or letterS3in1) and (letterT1in2 or letterT4in2)):
        if gramRow1_C_sound_right1==1:
            $gramRow1_C_sound_right1 -=1

    #win conditions
    if  (letterS5in1 == True or letterS3in1 == True) and (letterT1in2 == True or letterT4in2 == True) and (letterS3in3 == True or letterS5in3 == True) and (letterT1in4 == True or letterT4in4 == True) and (letterA6in7 == True or letterA7in7 == True) and (letterM2in8 == True or letterM8in8 == True) and (letterT4in5 == True or letterA6in5 == True or letterA7in5 == True) and (letterM2in6 == True or letterM8in6 == True):
        image gram_m4_tile202 = "letterT.png"
        image gram_m4_tile206 = "letterM.png"
        image gram_m4_tile203 = "letterS.png"
        image gram_m4_tile205 = "letterT.png"
        image gram_m4_tile201 = "letterS.png"
        image gram_m4_tile204 = "letterA.png"
        image gram_m4_tile208 = "letterA.png"
        image gram_m4_tile250 = "letterM.png"
        show gram_m4_tile202 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_m4_tile206 at Position(xpos = letterM2x, xanchor = 0, ypos = letterM2y, yanchor = 0)
        show gram_m4_tile203 at Position(xpos = letterS3x, xanchor = 0, ypos = letterS3y, yanchor = 0)
        show gram_m4_tile205 at Position(xpos = letterT4x, xanchor = 0, ypos = letterT4y, yanchor = 0)
        show gram_m4_tile201 at Position(xpos = letterS5x, xanchor = 0, ypos = letterS5y, yanchor = 0)
        show gram_m4_tile204 at Position(xpos = letterA6x, xanchor = 0, ypos = letterA6y, yanchor = 0)
        show gram_m4_tile208 at Position(xpos = letterA7x, xanchor = 0, ypos = letterA7y, yanchor = 0)
        show gram_m4_tile250 at Position(xpos = letterM8x, xanchor = 0, ypos = letterM8y, yanchor = 0)
        queue sound gramWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramMedWin
        jump gramMed_win

    if attempts ==0:
        show gram_m4_tile202 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_m4_tile206 at Position(xpos = letterM2x, xanchor = 0, ypos = letterM2y, yanchor = 0)
        show gram_m4_tile203 at Position(xpos = letterS3x, xanchor = 0, ypos = letterS3y, yanchor = 0)
        show gram_m4_tile205 at Position(xpos = letterT4x, xanchor = 0, ypos = letterT4y, yanchor = 0)
        show gram_m4_tile201 at Position(xpos = letterS5x, xanchor = 0, ypos = letterS5y, yanchor = 0)
        show gram_m4_tile204 at Position(xpos = letterA6x, xanchor = 0, ypos = letterA6y, yanchor = 0)
        show gram_m4_tile208 at Position(xpos = letterA7x, xanchor = 0, ypos = letterA7y, yanchor = 0)
        show gram_m4_tile250 at Position(xpos = letterM8x, xanchor = 0, ypos = letterM8y, yanchor = 0)
        queue sound gramLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 4
            jump pg_gramMedLose
        $gramMed_attempts +=1
        jump gramMed_lose #start
    
    jump gamefile_m4