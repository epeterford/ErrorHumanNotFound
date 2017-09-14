

screen logicGatese2:
    key 'h' action Hide("")
    key 'K_PAGEUP' action Hide("")
    key 'repeat_K_PAGEUP' action Hide("")
    key 'K_AC_BACK' action Hide("")
    key 'mousedown_4' action Hide("")
    key 'K_LCTRL' action Skip("")
    key 'K_RCTRL' action Skip("")
    key 'K_TAB' action Hide("")
    key '>' action Skip("")
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 260
        ypos 200
        focus_mask True
        action Jump("gramEasyHints2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 178
        ypos 285
    text "Moves" xpos 185 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 365 ypos 294 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 380 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27

    draggroup:
        #and gates
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae2and1x ypos eae2and1y
        drag:
                drag_name "letterN"
                child "letterN.png"
                droppable False
                dragged gate_dragged
                xpos eae2and2x ypos eae2and2y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae2and3x ypos eae2and3y
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae2and4x ypos eae2and4y
        drag:
                drag_name "letterS"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae2and5x ypos eae2and5y
        drag:
                drag_name "letterQ"
                child "letterQ.png"
                droppable False
                dragged gate_dragged
                xpos eae2and6x ypos eae2and6y
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




init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_e2:
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""

    scene bg Eng_Tile
    $ quick_menu = False
    $ game_menu = True

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image eaeng_e2_tile0 = "instructions2.png"
    image eaeng_e2_tile1 = "1_1_green.png"
    image eaeng_e2_tile2 = "letterS.png"
    show eaeng_e2_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_e2_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_e2_tile2 at Position(xpos = 1265, xanchor = 0, ypos = 167, yanchor = 0)
    
    #row2 5-8

    image eaeng_e2_tile5 = "leftTreelong.png"
    image eaeng_e2_tile6 = "rightTreelong.png"

    show eaeng_e2_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_e2_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_e2_tile9 = "1_1_grey.png"
    image eaeng_e2_tile10 = "1_1_grey.png"
    

    show eaeng_e2_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_e2_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_e2_tile14 = "leftTree.png"
    image eaeng_e2_tile15 = "rightTree.png"
    image eaeng_e2_tile16 = "leftTree.png"
    image eaeng_e2_tile17 = "rightTree.png"

    show eaeng_e2_tile14 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e2_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e2_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e2_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_e2_tile21 = "1_1_grey.png"
    image eaeng_e2_tile22 = "1_1_grey.png"
    image eaeng_e2_tile23 = "1_1_grey.png"
    image eaeng_e2_tile24 = "1_1_grey.png"

    show eaeng_e2_tile21 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e2_tile22 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e2_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e2_tile24 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)

    image eaeng_e2_tile31 = "letterBorder.png"
    image eaeng_e2_tile32 = "letterBorder.png"
    image eaeng_e2_tile33 = "letterBorder.png"
    image eaeng_e2_tile34 = "letterBorder.png"
    image eaeng_e2_tile35 = "letterBorder.png"
    image eaeng_e2_tile36 = "letterBorder.png"
    show eaeng_e2_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e2_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e2_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_e2_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e2_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e2_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ eae2and1x = 275 
    $ eae2and1y = 575
    $ eae2and2x = 410
    $ eae2and2y = 575
    $ eae2and3x = 342 
    $ eae2and3y = 660
    $ eae2and4x = 275
    $ eae2and4y = 750
    $ eae2and5x = 410
    $ eae2and5y = 750
    $ eae2and6x = 342 
    $ eae2and6y = 832
    
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
    
    jump gamefile_e2

label gamefile_e2:
    #image moon = "images/blankTile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatese2

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other tile here
            if and1in1 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in1 = False
            #sets values for checks
            $ eae2and1x = 1115
            $ eae2and1y = 340
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae2and1x = 1415
            $ eae2and1y = 340
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae2and1x = 1040
            $ eae2and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae2and1x = 1190
            $ eae2and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = True
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae2and1x = 1340
            $ eae2and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = True
            $ and1in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and2in6 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae2and1x = 1490
            $ eae2and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = True

    if gate_name == "letterN":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae2and2x = 1115
            $ eae2and2y = 340
            $ and2in1 = True
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae2and2x = 1415
            $ eae2and2y = 340
            $ and2in1 = False
            $ and2in2 = True
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae2and2x = 1040
            $ eae2and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = True
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae2and2x = 1190
            $ eae2and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = True
            $ and2in5 = False
            $ and2in6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae2and2x = 1340
            $ eae2and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = True
            $ and2in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae2and2x = 1490
            $ eae2and2y = 515
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
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae2and3x = 1115
            $ eae2and3y = 340
            $ and3in1 = True
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae2and3x = 1415
            $ eae2and3y = 340
            $ and3in1 = False
            $ and3in2 = True
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae2and3x = 1040
            $ eae2and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = True
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae2and3x = 1190
            $ eae2and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = True
            $ and3in5 = False
            $ and3in6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae2and3x = 1340
            $ eae2and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = True
            $ and3in6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae2and3x = 1490
            $ eae2and3y = 515
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
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae2and4x = 1115
            $ eae2and4y = 340
            $ and4in1 = True
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae2and4x = 1415
            $ eae2and4y = 340
            $ and4in1 = False
            $ and4in2 = True
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae2and4x = 1040
            $ eae2and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = True
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae2and4x = 1190
            $ eae2and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = True
            $ and4in5 = False
            $ and4in6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae2and4x = 1340
            $ eae2and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = True
            $ and4in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae2and4x = 1490
            $ eae2and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = True
           


    if gate_name == "letterS":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae2and5x = 1115
            $ eae2and5y = 340
            $ and5in1 = True
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae2and5x = 1415
            $ eae2and5y = 340
            $ and5in1 = False
            $ and5in2 = True
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae2and5x = 1040
            $ eae2and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = True
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae2and5x = 1190
            $ eae2and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = True
            $ and5in5 = False
            $ and5in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae2and5x = 1340
            $ eae2and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = True
            $ and5in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae2and5x = 1490
            $ eae2and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = True
            
  

    if gate_name == "letterQ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae2and6x = 1115
            $ eae2and6y = 340
            $ and6in1 = True
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae2and6x = 1415
            $ eae2and6y = 340
            $ and6in1 = False
            $ and6in2 = True
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae2and6x = 1040
            $ eae2and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = True
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae2and6x = 1190
            $ eae2and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = True
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae2and6x = 1340
            $ eae2and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = True
            $ and6in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae2and1x = 275
               $ eae2and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae2and2x = 410
               $ eae2and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae2and3x = 342
               $ eae2and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae2and4x = 275
               $ eae2and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae2and5x = 410
               $ eae2and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae2and6x = 342
               $ eae2and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae2and6x = 1490
            $ eae2and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = True
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
    play sound gramTree2
    if and5in1 == True and and1in2 == True:
        image eaeng_e2_tile42 = "leftTreegreenlong.png"
        image eaeng_e2_tile43 = "1_1_green.png"
        image eaeng_e2_tile44 = "rightTreegreenlong.png"
        image eaeng_e2_tile45 = "1_1_green.png"
        if (gramRow1_sound ==0):
            $gramRow1_sound +=1
            play sound gramTree1
        show eaeng_e2_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e2_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        
        if and3in3 == True and and6in4 == True:
            image eaeng_e2_tile46 = "leftTreegreen.png"
            image eaeng_e2_tile47 = "1_1_green.png"
            image eaeng_e2_tile48 = "solutionLine.png"
            image eaeng_e2_tile49 = "change.png"
            image eaeng_e2_tile50 = "rightTreegreen.png"
            image eaeng_e2_tile51 = "1_1_green.png"
            image eaeng_e2_tile52 = "solutionLine.png"
            image eaeng_e2_tile53 = "your.png"
            if ((gramRow2_soundA ==0) and (gramRow2_soundB==0)) or ((gramRow2_soundA==0) and (gramRow2_soundB==1)):
                play sound gramText1
                $gramRow2_soundA +=1
            show eaeng_e2_tile46 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile47 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile48 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile49 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e2_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)

        if and3in3 == False or and6in4 == False:
            hide eaeng_e2_tile46
            hide eaeng_e2_tile47
            hide eaeng_e2_tile48
            hide eaeng_e2_tile49
            hide eaeng_e2_tile50
            hide eaeng_e2_tile51
            hide eaeng_e2_tile52
            hide eaeng_e2_tile53
     
        if (and1in3 == True or and2in3 == True or and4in3 == True or and5in3 == True or and6in3 == True) and (and1in4 == True or and2in4 == True or and3in4 == True or and4in4 == True or and5in4 == True):
            image eaeng_e2_tile54 = "leftTreered.png"
            image eaeng_e2_tile55 = "1_1_red.png"
            image eaeng_e2_tile56 = "rightTreered.png"
            image eaeng_e2_tile57 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==0) and (gramRow2_soundB==1):
                play sound gramTree5
            show eaeng_e2_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in3 == False or and1in4 == False:
            hide eaeng_e2_tile54
            hide eaeng_e2_tile55
            hide eaeng_e2_tile56
            hide eaeng_e2_tile57

        if and3in3 == True and (and1in4 == True or and2in4 == True or and4in4 == True or and5in4 == True) or and6in4 == True and (and1in3 == True or and2in3 == True or and4in3 == True or and5in3 == True):
            image eaeng_e2_tile58 = "leftTreered.png"
            image eaeng_e2_tile59 = "1_1_red.png"
            image eaeng_e2_tile60 = "rightTreered.png"
            image eaeng_e2_tile61 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==0) and (gramRow2_soundB==1):
                play sound gramTree5
            show eaeng_e2_tile58 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile59 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile60 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile61 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in3 == False or and1in4 == False:
            hide eaeng_e2_tile58
            hide eaeng_e2_tile59
            hide eaeng_e2_tile60
            hide eaeng_e2_tile61

        if and4in5 == True and and2in6 == True:
            image eaeng_e2_tile62 = "leftTreegreen.png"
            image eaeng_e2_tile63 = "1_1_green.png"
            image eaeng_e2_tile64 = "solutionLine.png"
            image eaeng_e2_tile65 = "password.png"
            image eaeng_e2_tile66 = "rightTreegreen.png"
            image eaeng_e2_tile67 = "1_1_green.png"
            image eaeng_e2_tile68 = "solutionLine.png"
            image eaeng_e2_tile69 = "roberta.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramText1
                $gramRow2_soundB +=1
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramText1
                $gramRow2_soundB +=1
            show eaeng_e2_tile62 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile63 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile64 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile65 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            #play sound gramText2
            show eaeng_e2_tile66 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile67 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile68 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile69 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)
        if and4in5 == False or and2in6 == False:
            hide eaeng_e2_tile62
            hide eaeng_e2_tile63
            hide eaeng_e2_tile64
            hide eaeng_e2_tile65
            hide eaeng_e2_tile66
            hide eaeng_e2_tile67
            hide eaeng_e2_tile68
            hide eaeng_e2_tile69

        if (and1in5 == True or and2in5 == True or and3in5 == True or and5in5 == True or and6in5 == True) and (and1in6 == True or and3in6 == True or and4in6 == True or and5in6 == True or and6in6 == True):
            image eaeng_e2_tile70 = "leftTreered.png"
            image eaeng_e2_tile71 = "1_1_red.png"
            image eaeng_e2_tile72 = "rightTreered.png"
            image eaeng_e2_tile73 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e2_tile70 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile71 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile72 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile73 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in5 == False or and1in6 == False:
            hide eaeng_e2_tile70
            hide eaeng_e2_tile71
            hide eaeng_e2_tile72
            hide eaeng_e2_tile73

        if and4in5 == True and (and1in6 == True or and3in6 == True or and5in6 == True or and6in6 == True) or and2in6 == True and (and1in5 == True or and3in5 == True or and5in5 == True or and6in5 == True):
            image eaeng_e2_tile74 = "leftTreered.png"
            image eaeng_e2_tile75 = "1_1_red.png"
            image eaeng_e2_tile76 = "rightTreered.png"
            image eaeng_e2_tile77 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e2_tile74 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile75 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile76 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile77 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and4in5 == False or and2in6 == False:
            hide eaeng_e2_tile74
            hide eaeng_e2_tile75
            hide eaeng_e2_tile76
            hide eaeng_e2_tile77


    if and5in1 == False or and1in2 == False:
        hide eaeng_e2_tile42
        hide eaeng_e2_tile43
        hide eaeng_e2_tile44
        hide eaeng_e2_tile45
        hide eaeng_e2_tile46
        hide eaeng_e2_tile47
        hide eaeng_e2_tile48
        hide eaeng_e2_tile49
        hide eaeng_e2_tile50
        hide eaeng_e2_tile51
        hide eaeng_e2_tile52
        hide eaeng_e2_tile53
        hide eaeng_e2_tile54
        hide eaeng_e2_tile55
        hide eaeng_e2_tile56
        hide eaeng_e2_tile57
        hide eaeng_e2_tile58
        hide eaeng_e2_tile59
        hide eaeng_e2_tile60
        hide eaeng_e2_tile61
        hide eaeng_e2_tile62
        hide eaeng_e2_tile63
        hide eaeng_e2_tile64
        hide eaeng_e2_tile65
        hide eaeng_e2_tile66
        hide eaeng_e2_tile67
        hide eaeng_e2_tile68
        hide eaeng_e2_tile69
        hide eaeng_e2_tile70
        hide eaeng_e2_tile71
        hide eaeng_e2_tile72
        hide eaeng_e2_tile73
        hide eaeng_e2_tile74
        hide eaeng_e2_tile75
        hide eaeng_e2_tile76
        hide eaeng_e2_tile77
    
    if (and1in1 == True or and2in1 == True or and4in1 == True or and6in1 == True) and (and2in2 == True or and3in2 == True or and4in2 == True or and5in2 == True):
         image eaeng_e2_tile78 = "leftTreeredlong.png"
         image eaeng_e2_tile79 = "1_1_red.png"
         image eaeng_e2_tile80 = "rightTreeredlong.png"
         image eaeng_e2_tile81 = "1_1_red.png"
         if (gramRow1_sound==0):
             play sound gramTree5
         show eaeng_e2_tile78 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile79 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e2_tile80 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile81 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and1in1 == False or and2in2 == False:
         hide eaeng_e2_tile78
         hide eaeng_e2_tile79
         hide eaeng_e2_tile80
         hide eaeng_e2_tile81

    if and5in1 == True and (and2in2 == True or and3in2 == True or and4in2 == True or and6in2 == True) or and1in2 == True and (and2in1 == True or and3in1 == True or and4in1 == True or and6in1 == True):
         image eaeng_e2_tile82 = "leftTreeredlong.png"
         image eaeng_e2_tile83 = "1_1_red.png"
         image eaeng_e2_tile84 = "rightTreeredlong.png"
         image eaeng_e2_tile85 = "1_1_red.png"
         if (gramRow1_sound==0):
             play sound gramTree5
         show eaeng_e2_tile82 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile83 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e2_tile84 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile85 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and1in1 == False or and2in2 == False:
         hide eaeng_e2_tile82
         hide eaeng_e2_tile83
         hide eaeng_e2_tile84
         hide eaeng_e2_tile85

    if and3in1 == True and and6in2 == True:
        image eaeng_e2_tile86 = "leftTreegreenlong.png"
        image eaeng_e2_tile87 = "1_1_green.png"
        image eaeng_e2_tile88 = "rightTreegreenlong.png"
        image eaeng_e2_tile89 = "1_1_green.png"
        if (gramRow1_sound ==0):
            $gramRow1_sound +=1
            play sound gramTree1
        show eaeng_e2_tile86 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile87 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e2_tile88 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile89 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

        
        if (and1in3 == True or and2in3 == True or and4in3 == True or and5in3 == True or and6in3 == True) and (and1in4 == True or and2in4 == True or and4in4 == True or and5in4 == True or and6in4 == True):
            image eaeng_e2_tile90 = "leftTreered.png"
            image eaeng_e2_tile91 = "1_1_red.png"
            image eaeng_e2_tile92 = "rightTreered.png"
            image eaeng_e2_tile93 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==0) and (gramRow2_soundB==1):
                play sound gramTree5
            show eaeng_e2_tile90 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile91 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile92 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile93 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in5 == False or and1in6 == False:
            hide eaeng_e2_tile90
            hide eaeng_e2_tile91
            hide eaeng_e2_tile92
            hide eaeng_e2_tile93


        if (and1in5 == True or and2in5 == True or and3in5 == True or and4in5 == True or and5in5 == True) and (and1in6 == True or and2in6 == True or and3in6 == True or and4in6 == True or and5in6 == True):
            image eaeng_e2_tile94 = "leftTreered.png"
            image eaeng_e2_tile95 = "1_1_red.png"
            image eaeng_e2_tile96 = "rightTreered.png"
            image eaeng_e2_tile97 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e2_tile94 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile95 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile96 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile97 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in5 == False or and1in6 == False:
            hide eaeng_e2_tile94
            hide eaeng_e2_tile95
            hide eaeng_e2_tile96
            hide eaeng_e2_tile97

        if and4in5 == True and (and1in6 == True or and3in6 == True or and4in6 == True or and5in6 == True or and6in6 == True) or and2in6 == True and (and1in5 == True or and2in5 == True or and3in5 == True or and5in6 == True or and6in5 == True):
            image eaeng_e2_tile98 = "leftTreered.png"
            image eaeng_e2_tile99 = "1_1_red.png"
            image eaeng_e2_tile100 = "rightTreered.png"
            image eaeng_e2_tile101 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e2_tile98 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile99 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile100 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile101 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in6 == False or and1in5 == False:
            hide eaeng_e2_tile98
            hide eaeng_e2_tile99
            hide eaeng_e2_tile100
            hide eaeng_e2_tile101

    if and3in1 == False or and6in2 == False:
        hide eaeng_e2_tile86
        hide eaeng_e2_tile87
        hide eaeng_e2_tile88
        hide eaeng_e2_tile89
        hide eaeng_e2_tile90
        hide eaeng_e2_tile91
        hide eaeng_e2_tile92
        hide eaeng_e2_tile93
        hide eaeng_e2_tile94
        hide eaeng_e2_tile95
        hide eaeng_e2_tile96
        hide eaeng_e2_tile97
        hide eaeng_e2_tile98
        hide eaeng_e2_tile99
        hide eaeng_e2_tile100
        hide eaeng_e2_tile101

    if and3in1 == True and (and1in2== True or and2in2 == True or and4in2 == True or and5in2 == True) or and6in2 == True and (and1in1 == True or and2in1 == True or and4in1 == True or and5in1 == True):
         image eaeng_e2_tile102 = "leftTreeredlong.png"
         image eaeng_e2_tile103 = "1_1_red.png"
         image eaeng_e2_tile104 = "rightTreeredlong.png"
         image eaeng_e2_tile105 = "1_1_red.png"
         if(gramRow1_sound==0):
             play sound gramTree5
         show eaeng_e2_tile102 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile103 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         #play sound gramTree5
         show eaeng_e2_tile104 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile105 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and3in1 == False or and6in2 == False:
         hide eaeng_e2_tile102
         hide eaeng_e2_tile103
         hide eaeng_e2_tile104
         hide eaeng_e2_tile105

    #win conditions
    if and5in1 == True and and3in3 == True and and6in4 == True and and1in2 == True and and4in5 == True and and2in6 == True: 
        image eaeng_e2_tile107 = "letterK.png"
        image eaeng_e2_tile111 = "letterN.png"
        image eaeng_e2_tile108 = "letterM.png"
        image eaeng_e2_tile110 = "letterP.png"
        image eaeng_e2_tile106 = "letterS.png"
        image eaeng_e2_tile109 = "letterQ.png"
        

        show eaeng_e2_tile107 at Position(xpos = eae2and1x, xanchor = 0, ypos = eae2and1y, yanchor = 0)
        show eaeng_e2_tile111 at Position(xpos = eae2and2x, xanchor = 0, ypos = eae2and2y, yanchor = 0)
        show eaeng_e2_tile108 at Position(xpos = eae2and3x, xanchor = 0, ypos = eae2and3y, yanchor = 0)
        show eaeng_e2_tile110 at Position(xpos = eae2and4x, xanchor = 0, ypos = eae2and4y, yanchor = 0)
        show eaeng_e2_tile106 at Position(xpos = eae2and5x, xanchor = 0, ypos = eae2and5y, yanchor = 0)
        show eaeng_e2_tile109 at Position(xpos = eae2and6x, xanchor = 0, ypos = eae2and6y, yanchor = 0)

        queue sound gramWin
        $ renpy.pause(1.0)
        hide eaeng_e2_tile42
        hide eaeng_e2_tile43
        hide eaeng_e2_tile44
        hide eaeng_e2_tile45
        hide eaeng_e2_tile46
        hide eaeng_e2_tile47
        hide eaeng_e2_tile48
        hide eaeng_e2_tile49
        hide eaeng_e2_tile50
        hide eaeng_e2_tile51
        hide eaeng_e2_tile52
        hide eaeng_e2_tile53
        hide eaeng_e2_tile54
        hide eaeng_e2_tile55
        hide eaeng_e2_tile60
        hide eaeng_e2_tile61
        hide eaeng_e2_tile62
        hide eaeng_e2_tile63
        hide eaeng_e2_tile64
        hide eaeng_e2_tile65
        hide eaeng_e2_tile66
        hide eaeng_e2_tile67
        hide eaeng_e2_tile68
        hide eaeng_e2_tile69
        hide eaeng_e2_tile70
        hide eaeng_e2_tile71
        hide eaeng_e2_tile72
        hide eaeng_e2_tile73
        hide eaeng_e2_tile74
        hide eaeng_e2_tile75
        hide eaeng_e2_tile76
        hide eaeng_e2_tile77
        hide eaeng_e2_tile78
        hide eaeng_e2_tile79
        hide eaeng_e2_tile80
        hide eaeng_e2_tile81
        hide eaeng_e2_tile82
        hide eaeng_e2_tile83
        hide eaeng_e2_tile84
        hide eaeng_e2_tile85
        hide eaeng_e2_tile86
        hide eaeng_e2_tile87
        hide eaeng_e2_tile88
        hide eaeng_e2_tile89
        hide eaeng_e2_tile90
        hide eaeng_e2_tile91
        hide eaeng_e2_tile92
        hide eaeng_e2_tile93
        hide eaeng_e2_tile94
        hide eaeng_e2_tile95
        hide eaeng_e2_tile96
        hide eaeng_e2_tile97
        hide eaeng_e2_tile98
        hide eaeng_e2_tile99
        hide eaeng_e2_tile100
        hide eaeng_e2_tile101
        
        jump gramEasyDone
        
        
    if attempts ==0:
        queue sound gramLose
        image eaeng_e2_tile107 = "letterK.png"
        image eaeng_e2_tile111 = "letterN.png"
        image eaeng_e2_tile108 = "letterM.png"
        image eaeng_e2_tile110 = "letterP.png"
        image eaeng_e2_tile106 = "letterS.png"
        image eaeng_e2_tile109 = "letterQ.png"
        show eaeng_e2_tile107 at Position(xpos = eae2and1x, xanchor = 0, ypos = eae2and1y, yanchor = 0)
        show eaeng_e2_tile111 at Position(xpos = eae2and2x, xanchor = 0, ypos = eae2and2y, yanchor = 0)
        show eaeng_e2_tile108 at Position(xpos = eae2and3x, xanchor = 0, ypos = eae2and3y, yanchor = 0)
        show eaeng_e2_tile110 at Position(xpos = eae2and4x, xanchor = 0, ypos = eae2and4y, yanchor = 0)
        show eaeng_e2_tile106 at Position(xpos = eae2and5x, xanchor = 0, ypos = eae2and5y, yanchor = 0)
        show eaeng_e2_tile109 at Position(xpos = eae2and6x, xanchor = 0, ypos = eae2and6y, yanchor = 0)
        $attemptsGramEasy +=1
        $ renpy.pause(1.5)
        hide eaeng_e2_tile42
        hide eaeng_e2_tile43
        hide eaeng_e2_tile44
        hide eaeng_e2_tile45
        hide eaeng_e2_tile46
        hide eaeng_e2_tile47
        hide eaeng_e2_tile48
        hide eaeng_e2_tile49
        hide eaeng_e2_tile50
        hide eaeng_e2_tile51
        hide eaeng_e2_tile52
        hide eaeng_e2_tile53
        hide eaeng_e2_tile54
        hide eaeng_e2_tile55
        hide eaeng_e2_tile60
        hide eaeng_e2_tile61
        hide eaeng_e2_tile62
        hide eaeng_e2_tile63
        hide eaeng_e2_tile64
        hide eaeng_e2_tile65
        hide eaeng_e2_tile66
        hide eaeng_e2_tile67
        hide eaeng_e2_tile68
        hide eaeng_e2_tile69
        hide eaeng_e2_tile70
        hide eaeng_e2_tile71
        hide eaeng_e2_tile72
        hide eaeng_e2_tile73
        hide eaeng_e2_tile74
        hide eaeng_e2_tile75
        hide eaeng_e2_tile76
        hide eaeng_e2_tile77
        hide eaeng_e2_tile78
        hide eaeng_e2_tile79
        hide eaeng_e2_tile80
        hide eaeng_e2_tile81
        hide eaeng_e2_tile82
        hide eaeng_e2_tile83
        hide eaeng_e2_tile84
        hide eaeng_e2_tile85
        hide eaeng_e2_tile86
        hide eaeng_e2_tile87
        hide eaeng_e2_tile88
        hide eaeng_e2_tile89
        hide eaeng_e2_tile90
        hide eaeng_e2_tile91
        hide eaeng_e2_tile92
        hide eaeng_e2_tile93
        hide eaeng_e2_tile94
        hide eaeng_e2_tile95
        hide eaeng_e2_tile96
        hide eaeng_e2_tile97
        hide eaeng_e2_tile98
        hide eaeng_e2_tile99
        hide eaeng_e2_tile100
        hide eaeng_e2_tile101
        jump gramEasyLose
    
    jump gamefile_e2