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
        action Jump("hints_gramMed_3")
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

        #letter dragback
        
        drag:
                drag_name "LetterM_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterN_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterL_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738

init:
    image bg Eng_gram_m3_tile = "eng_tile_bg.png"

label gram_m3: #start:
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
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
    image gram_m3_tile5 = "leftTreelong1.png"
    image gram_m3_tile6 = "rightTreelong1.png"
    show gram_m3_tile5 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
    show gram_m3_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
    
    #row3 9-13   

    image gram_m3_tile9 = "1_1_grey.png"
    image gram_m3_tile10 = "1_1_grey.png"
    

    show gram_m3_tile9 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)
    show gram_m3_tile10 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)

    #row4 14-20

    image gram_m3_tile14 = "leftTreelong.png"
    image gram_m3_tile15 = "rightTreelong.png"
    image gram_m3_tile16 = "leftTreelong.png"
    image gram_m3_tile17 = "rightTreelong.png"

    show gram_m3_tile14 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
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

    image eaeng_m3_tile300 = "letterM_grey.png"
    image eaeng_m3_tile301 = "letterN_grey.png"
    image eaeng_m3_tile303 = "letterK_grey.png"
    image eaeng_m3_tile304 = "letterL_grey.png"
    show eaeng_m3_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_m3_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_m3_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_m3_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)

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
    $ attempts = 11
    
    call gamefile_m3 from _call_gamefile_m3

label gamefile_m3:
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

#Dragbacks
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "LetterM_return" or slot_name == "LetterN_return" or slot_name == "LetterK_return" or slot_name == "LetterL_return")):
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
                    $ letterM4x = 275
                    $ letterM4y = 575
                    $ letterM4in1 = False
                    $ letterM4in2 = False
                    $ letterM4in3 = False
                    $ letterM4in4 = False
                    $ letterM4in5 = False
                    $ letterM4in6 = False
                    $ letterM4in7 = False
                    $ letterM4in8 = False
   
            if slot_name == "LetterN_return":
                $ attempts +=1
                if gate_name == "letterN":
                    $ letterN2x = 410
                    $ letterN2y = 575
                    $ letterN2in1 = False
                    $ letterN2in2 = False
                    $ letterN2in3 = False
                    $ letterN2in4 = False
                    $ letterN2in5 = False
                    $ letterN2in6 = False
                    $ letterN2in7 = False
                    $ letterN2in8 = False
                
                if gate_name == "letterN2":
                    $ letterN8x = 410
                    $ letterN8y = 575
                    $ letterN8in1 = False
                    $ letterN8in2 = False
                    $ letterN8in3 = False
                    $ letterN8in4 = False
                    $ letterN8in5 = False
                    $ letterN8in6 = False
                    $ letterN8in7 = False
                    $ letterN8in8 = False
            
            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ letterK3x = 275
                    $ letterK3y = 750
                    $ letterK3in1 = False
                    $ letterK3in2 = False
                    $ letterK3in3 = False
                    $ letterK3in4 = False
                    $ letterK3in5 = False
                    $ letterK3in6 = False
                    $ letterK3in7 = False
                    $ letterK3in8 = False
                
                if gate_name == "letterK2":
                    $ letterK6x = 275
                    $ letterK6y = 750
                    $ letterK6in1 = False
                    $ letterK6in2 = False
                    $ letterK6in3 = False
                    $ letterK6in4 = False
                    $ letterK6in5 = False
                    $ letterK6in6 = False
                    $ letterK6in7 = False
                    $ letterK6in8 = False
                
                if gate_name == "letterK3":
                    $ letterK7x = 275
                    $ letterK7y = 750
                    $ letterK7in1 = False
                    $ letterK7in2 = False
                    $ letterK7in3 = False
                    $ letterK7in4 = False
                    $ letterK7in5 = False
                    $ letterK7in6 = False
                    $ letterK7in7 = False
                    $ letterK7in8 = False
                    
            if slot_name == "LetterL_return":
                $ attempts +=1
                if gate_name == "letterL":
                    $ letterL5x = 410
                    $ letterL5y = 750
                    $ letterL5in1 = False
                    $ letterL5in2 = False
                    $ letterL5in3 = False
                    $ letterL5in4 = False
                    $ letterL5in5 = False
                    $ letterL5in6 = False
                    $ letterL5in7 = False
                    $ letterL5in8 = False
                    
                if gate_name == "letterL2":
                    $ letterL1x = 410
                    $ letterL1y = 750
                    $ letterL1in1 = False
                    $ letterL1in2 = False
                    $ letterL1in3 = False
                    $ letterL1in4 = False
                    $ letterL1in5 = False
                    $ letterL1in6 = False
                    $ letterL1in7 = False
                    $ letterL1in8 = False

    #START SOUNDS HERE
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
    hide gram_m3_tile260Syd
    hide gram_m3_tile261Syd
    hide gram_m3_tile260x
    hide gram_m3_tile261x
    hide gram_m3_tile262
    hide gram_m3_tile263
    hide gram_m3_tile56
    hide gram_m3_tile57
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
    hide gram_m3_tile90
    hide gram_m3_tile91
    hide gram_m3_tile92
    hide gram_m3_tile93
    hide gram_m3_tile70S
    hide gram_m3_tile71S
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if (letterL5in1 or letterL1in1 ) and (letterL1in2 or letterL5in2):
        image gram_m3_tile42 = "leftTreegreenlong1.png"
        image gram_m3_tile43 = "1_1_green.png"
        show gram_m3_tile42 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m3_tile43 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

        image gram_m3_tile62 = "rightTreegreenlong1.png"
        image gram_m3_tile63 = "1_1_green.png"
        show gram_m3_tile62 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
        show gram_m3_tile63 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)
        if gramRow1_C_sound==0:
            play sound gramTree1
            $gramRow1_C_sound +=1
        if (letterK3in3 or letterK6in3 or letterK7in3) and (letterM4in4):
            image gram_m3_tile44 = "leftTreegreenlong.png"
            image gram_m3_tile45 = "1_1_green.png"

            show gram_m3_tile44 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile45 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile56 = "rightTreegreenlong.png"
            image gram_m3_tile57 = "1_1_green.png"
            show gram_m3_tile56 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile57 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_L_sound_right1==0:
                play sound gramTree1
                $gramRow2_L_sound_right1 +=1
            if (letterK3in7 or letterK6in7 or letterK7in7):
                image gram_m3_tile46 = "solutionLine_grey.png"
                image gram_m3_tile47 = "solutionLine_grey.png"
                image gram_m3_tile48 = "solutionLine_grey.png"
                image gram_m3_tile207 = "solutionLine_grey.png"
                image gram_m3_tile49 = "epsilon.png"
                image gram_m3_tile50 = "rightTreegreen.png"
                image gram_m3_tile51 = "1_1_green.png"
                image gram_m3_tile52 = "solutionLine.png"
                image gram_m3_tile53 = "d.png"
                show gram_m3_tile50 at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m3_tile51 at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)
                show gram_m3_tile52 at Position(xpos = 950, xanchor = 0, ypos = 750, yanchor = 0)
                show gram_m3_tile53 at Position(xpos = 945, xanchor = 0, ypos = 800, yanchor = 0)
                show gram_m3_tile46 at Position(xpos = 830, xanchor = 0, ypos = 572, yanchor = 0)
                show gram_m3_tile47 at Position(xpos = 830, xanchor = 0, ypos = 646, yanchor = 0)
                show gram_m3_tile48 at Position(xpos = 830, xanchor = 0, ypos = 715, yanchor = 0)
                show gram_m3_tile207 at Position(xpos = 830, xanchor = 0, ypos = 755, yanchor = 0)
                show gram_m3_tile49 at Position(xpos = 785, xanchor = 0, ypos = 800, yanchor = 0)
                if gramRow3_L_sound_right1==0:
                    play sound gramTree1
                    queue sound gramText1
                    $gramRow3_L_sound_right1 +=1
            if not(letterK3in7 or letterK6in7 or letterK7in7):
                if gramRow3_L_sound_right1==1:
                    $gramRow3_L_sound_right1 -=1

            if (letterN2in7 or letterN8in7):
               image gram_m3_tile260Syd = "rightTreered.png"
               image gram_m3_tile261Syd = "1_1_red.png"
               show gram_m3_tile260Syd at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile261Syd at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)
               if gramRow3_L_sound_wrong1 ==0:
                   play sound gramTree5
                   $gramRow3_R_sound_wrong1 +=1
            if not(letterN2in7 or letterN8in7):
               if gramRow3_L_sound_wrong1 ==1:
                   $gramRow3_L_sound_wrong1 -=1
                   
            if (letterN2in8 or letterN8in8):
                image gram_m3_tile215 = "treeGreen.png"
                image gram_m3_tile216 = "1_1_green.png"
                show gram_m3_tile215 at Position(xpos = 1160, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m3_tile216 at Position(xpos = 1160, xanchor = 0, ypos = 650, yanchor = 0)
                image gram_m3_tile210 = "solutionLine.png"
                image gram_m3_tile59 = "c.png"
                show gram_m3_tile210 at Position(xpos = 1165, xanchor = 0, ypos = 750, yanchor = 0)
                show gram_m3_tile59 at Position(xpos = 1140, xanchor = 0, ypos = 800, yanchor = 0)
                if gramRow3_R_sound_right1 ==0:
                    $gramRow3_R_sound_right1 +=1
                    play sound gramTree1
                    queue sound gramText3
            if not(letterN2in8 or letterN8in8):
               if gramRow3_R_sound_right1 ==1:
                   $gramRow3_R_sound_right1 -=1
                   
            if (letterK3in8 or letterK6in8 or letterK7in8):
                image gram_m3_tile262 = "treeRed.png"
                image gram_m3_tile263 = "1_1_red.png"
                show gram_m3_tile262 at Position(xpos = 1160, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m3_tile263 at Position(xpos = 1160, xanchor = 0, ypos = 650, yanchor = 0)
                if gramRow3_R_sound_wrong1 == 0:
                    play sound gramTree5
                    $gramRow3_R_sound_wrong1 +=1
            if not(letterK3in8 or letterK6in8 or letterK7in8):
                if gramRow3_R_sound_wrong1 ==1:
                    $gramRow3_R_sound_wrong1 -=1
                
        #Incorrect solution but correct substitution
        elif (letterK3in3 or letterK6in3 or letterK7in3) and (letterN2in4 or letterN8in4):
            image gram_m3_tile44 = "leftTreegreenlong.png"
            image gram_m3_tile45 = "1_1_green.png"

            show gram_m3_tile44 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile45 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile56 = "rightTreegreenlong.png"
            image gram_m3_tile57 = "1_1_green.png"
            show gram_m3_tile56 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile57 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_L_sound_right2==0:
                play sound gramTree1
                $gramRow2_L_sound_right2 +=1
            if (letterK3in7 or letterK6in7 or letterK7in7):
                show gram_m3_tile50 at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m3_tile51 at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)
                show gram_m3_tile52 at Position(xpos = 950, xanchor = 0, ypos = 750, yanchor = 0)
                show gram_m3_tile53 at Position(xpos = 945, xanchor = 0, ypos = 800, yanchor = 0)
                show gram_m3_tile46 at Position(xpos = 830, xanchor = 0, ypos = 572, yanchor = 0)
                show gram_m3_tile47 at Position(xpos = 830, xanchor = 0, ypos = 646, yanchor = 0)
                show gram_m3_tile48 at Position(xpos = 830, xanchor = 0, ypos = 715, yanchor = 0)
                show gram_m3_tile207 at Position(xpos = 830, xanchor = 0, ypos = 755, yanchor = 0)
                show gram_m3_tile49 at Position(xpos = 785, xanchor = 0, ypos = 800, yanchor = 0)
                if gramRow3_L_sound_right1 ==0:
                    play sound gramTree1
                    queue sound gramText1
                    $gramRow3_L_sound_right1 +=1
            if not(letterK3in7 or letterK6in7 or letterK7in7):
                if gramRow3_L_sound_right1 ==1:
                    $gramRow3_L_sound_right1 -=1

            if (letterN2in7 or letterN8in7 or letterM4in7):
               image gram_m3_tile260x = "rightTreered.png"
               image gram_m3_tile261x = "1_1_red.png"
               show gram_m3_tile260x at Position(xpos = 930, xanchor = 0, ypos = 575, yanchor = 0)
               show gram_m3_tile261x at Position(xpos = 945, xanchor = 0, ypos = 650, yanchor = 0)
               if gramRow3_L_sound_wrong1 ==0:
                   play sound gramTree5
                   $gramRow3_L_sound_wrong1 +=1

            if not(letterN2in7 or letterN8in7 or letterM4in7):
               if gramRow3_L_sound_wrong1 ==1:
                   $gramRow3_L_sound_wrong1 -=1

            if (letterM4in8 or letterK3in8 or letterK6in8 or letterK7in8 or letterN2in8 or letterN8in8):
                image gram_m3_tile262 = "treeRed.png"
                image gram_m3_tile263 = "1_1_red.png"
                show gram_m3_tile262 at Position(xpos = 1160, xanchor = 0, ypos = 575, yanchor = 0)
                show gram_m3_tile263 at Position(xpos = 1160, xanchor = 0, ypos = 650, yanchor = 0)
                if gramRow3_R_sound_wrong1 == 0:
                    play sound gramTree5
                    $gramRow3_R_sound_wrong1 +=1
            if not(letterM4in8 or letterK3in8 or letterK6in8 or letterK7in8 or letterN2in8 or letterN8in8):
                if gramRow3_R_sound_wrong1 ==1:
                    $gramRow3_R_sound_wrong1 -=1
                    
        elif (letterK7in3 or letterK3in3 or letterK6in3 or letterN2in3 or letterM4in3 or letterN8in3) and (letterN2in4 or letterK3in4 or letterK6in4 or letterK7in4 or letterN8in4 or letterM4in4):
            image gram_m3_tile54 = "leftTreeredlong.png"
            image gram_m3_tile55 = "1_1_red.png"
            show gram_m3_tile54 at Position(xpos = 900, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile55 at Position(xpos = 860, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile60 = "rightTreeredlong.png"
            image gram_m3_tile61 = "1_1_red.png"
            show gram_m3_tile60 at Position(xpos = 1070, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile61 at Position(xpos = 1160, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_L_sound_wrong1 ==0:
                $gramRow2_L_sound_wrong1 +=1
                play sound gramTree5
        if not((letterK7in3 or letterK3in3 or letterK6in3 or letterN2in3 or letterM4in3 or letterN8in3) and (letterN2in4 or letterK3in4 or letterK6in4 or letterK7in4 or letterN8in4 or letterM4in4)):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1
                
        if not((letterK3in3 or letterK6in3 or letterK7in3) and (letterM4in4)):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1

        if (letterK3in5 or letterK6in5 or letterK7in5 ) and (letterN2in6 or letterN8in6):
            image gram_m3_tile64 = "leftTreegreenlong.png"
            image gram_m3_tile65 = "1_1_green.png"
            image gram_m3_tile66 = "solutionLine.png"
            image gram_m3_tile211 = "solutionLine.png"
            image gram_m3_tile212 = "solutionLine.png"
            image gram_m3_tile67 = "d.png"
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
            image gram_m3_tile73 = "c.png"
            show gram_m3_tile70 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile71 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m3_tile72 at Position(xpos = 1640, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m3_tile213 at Position(xpos = 1640, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m3_tile214 at Position(xpos = 1640, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m3_tile73 at Position(xpos = 1620, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_R_sound_right1==0:
                $gramRow2_R_sound_right1 +=1
                play sound gramTree1
                queue sound gramText2

            
        elif(letterK3in5 or letterK6in5 or letterK7in5 ) and (letterM4in6):
            image gram_m3_tile70S = "rightTreegreenlong.png"
            image gram_m3_tile71S = "1_1_green.png"
            show gram_m3_tile70S at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile71S at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)
            

            show gram_m3_tile64 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile65 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)
            show gram_m3_tile66 at Position(xpos = 1340, xanchor = 0, ypos = 570, yanchor = 0)
            show gram_m3_tile211 at Position(xpos = 1340, xanchor = 0, ypos = 662, yanchor = 0)
            show gram_m3_tile212 at Position(xpos = 1340, xanchor = 0, ypos = 755, yanchor = 0)
            show gram_m3_tile67 at Position(xpos = 1315, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_R_sound_right2 ==0:
                $gramRow2_R_sound_right2 +=1
                play sound gramTree1
                queue sound gramText2

        elif(letterK3in5 or letterK6in5 or letterK7in5 or letterN2in5 or letterN8in5 or letterM4in5) and (letterK3in6 or letterK6in6 or letterK7in6 or letterN2in6 or letterM4in6 or letterN8in6):
            image gram_m3_tile68 = "leftTreeredlong.png"
            image gram_m3_tile69 = "1_1_red.png"
            show gram_m3_tile68 at Position(xpos = 1380, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile69 at Position(xpos = 1340, xanchor = 0, ypos = 475, yanchor = 0)

            image gram_m3_tile74 = "rightTreeredlong.png"
            image gram_m3_tile75 = "1_1_red.png"
            show gram_m3_tile74 at Position(xpos = 1550, xanchor = 0, ypos = 400, yanchor = 0)
            show gram_m3_tile75 at Position(xpos = 1640, xanchor = 0, ypos = 475, yanchor = 0)
            if gramRow2_R_sound_wrong1 ==0:
                $gramRow2_R_sound_wrong1 +=1
                play sound gramTree5
                
        if not((letterK3in5 or letterK6in5 or letterK7in5 ) and (letterN2in6 or letterN8in6)):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
                
        if not((letterK3in5 or letterK6in5 or letterK7in5 or letterN2in5 or letterN8in5 or letterM4in5) and (letterK3in6 or letterK6in6 or letterK7in6 or letterN2in6 or letterM4in6 or letterN8in6)):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1
        
        if not((letterK3in5 or letterK6in5 or letterK7in5 ) and (letterM4in6)):
            if gramRow2_R_sound_right2 ==1:
                $gramRow2_R_sound_right2 -=1

    elif (letterL1in1 or letterN2in1 or letterK3in1 or letterM4in1 or letterL5in1 or letterK6in1 or letterK7in1 or letterN8in1) and (letterL1in2 or  letterN2in2 or letterK3in2 or letterM4in2 or letterL5in2 or letterK6in2 or letterK7in2 or letterN8in2):
         image gram_m3_tile90 = "leftTreeredlong1.png"
         image gram_m3_tile91 = "1_1_red.png"
         show gram_m3_tile90 at Position(xpos = 1040, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m3_tile91 at Position(xpos = 1010, xanchor = 0, ypos = 300, yanchor = 0)

         image gram_m3_tile92 = "rightTreeredlong1.png"
         image gram_m3_tile93 = "1_1_red.png"
         show gram_m3_tile92 at Position(xpos = 1310, xanchor = 0, ypos = 230, yanchor = 0)
         show gram_m3_tile93 at Position(xpos = 1490, xanchor = 0, ypos = 300, yanchor = 0)
         if gramRow1_C_sound_wrong1 ==0:
             $gramRow1_C_sound_wrong1 +=1
             play sound gramTree5
             
    if not((letterL5in1 or letterL1in1 ) and (letterL1in2 or letterL5in2)):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
            
    if not((letterL1in1 or letterN2in1 or letterK3in1 or letterM4in1 or letterL5in1 or letterK6in1 or letterK7in1 or letterN8in1) and (letterL1in2 or  letterN2in2 or letterK3in2 or letterM4in2 or letterL5in2 or letterK6in2 or letterK7in2 or letterN8in2)):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1

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
        queue sound gramWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramMedWin
        jump gramMed_win

    if attempts ==0:
        show gram_m3_tile202 at Position(xpos = letterL1x, xanchor = 0, ypos = letterL1y, yanchor = 0)
        show gram_m3_tile206 at Position(xpos = letterN2x, xanchor = 0, ypos = letterN2y, yanchor = 0)
        show gram_m3_tile203 at Position(xpos = letterK3x, xanchor = 0, ypos = letterK3y, yanchor = 0)
        show gram_m3_tile205 at Position(xpos = letterM4x, xanchor = 0, ypos = letterM4y, yanchor = 0)
        show gram_m3_tile201 at Position(xpos = letterL5x, xanchor = 0, ypos = letterL5y, yanchor = 0)
        show gram_m3_tile204 at Position(xpos = letterK6x, xanchor = 0, ypos = letterK6y, yanchor = 0)
        show gram_m3_tile208 at Position(xpos = letterK7x, xanchor = 0, ypos = letterK7y, yanchor = 0)
        show gram_m3_tile250 at Position(xpos = letterN8x, xanchor = 0, ypos = letterN8y, yanchor = 0)
        $renpy.pause(1.5)
        queue sound gramLose
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_gramMedLose
        $gramMed_attempts +=1
        jump gramMed_lose
        
    
    jump gamefile_m3