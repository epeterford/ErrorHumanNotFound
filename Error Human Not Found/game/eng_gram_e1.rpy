
screen logicGatese1:
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
        action Jump("gramEasyHints1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 178
        ypos 285
    text "Moves" xpos 185 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 325 ypos 294 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 380 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27
    imagebutton:
        idle "letterP_grey.png"
        xpos 410
        ypos 750
    imagebutton:
        idle "letterJ_grey.png"
        xpos 275
        ypos 575
    imagebutton:
        idle "letterM_grey.png"
        xpos 342
        ypos 660
    imagebutton: 
        idle "letterL_grey.png"
        xpos 342
        ypos 832
    imagebutton:
        idle "letterN_grey.png"
        xpos 275
        ypos 750
    imagebutton:
        idle "letterK_grey.png"
        xpos 410
        ypos 575
    draggroup:
        #and gates
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos eae1and1x ypos eae1and1y
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae1and2x ypos eae1and2y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae1and3x ypos eae1and3y
        drag:
                drag_name "letterN"
                child "letterN.png"
                droppable False
                dragged gate_dragged
                xpos eae1and4x ypos eae1and4y
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae1and5x ypos eae1and5y
        drag:
                drag_name "letterL"
                child "letterL.png"
                droppable False
                dragged gate_dragged
                xpos eae1and6x ypos eae1and6y

        
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

        #letter dragback
        
        drag:
                drag_name "LetterJ_return"
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
                xpos 330 ypos 648
        drag:
                drag_name "LetterN_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterP_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738
        drag:
                drag_name "LetterL_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 817


init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_e1:
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
    image eaeng_e1_tile161 = "instructions1.png"
    image eaeng_e1_tile162 = "1_1_green.png"
    image eaeng_e1_tile163 = "letterS.png"
    show eaeng_e1_tile161 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_e1_tile162 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_e1_tile163 at Position(xpos = 1265, xanchor = 0, ypos = 167, yanchor = 0)
    
    #row2 5-8

    image eaeng_e1_tile164 = "leftTreelong.png"
    image eaeng_e1_tile165 = "rightTreelong.png"

    show eaeng_e1_tile164 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_e1_tile165 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_e1_tile166 = "1_1_grey.png"
    image eaeng_e1_tile167 = "1_1_grey.png"
    

    show eaeng_e1_tile166 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_e1_tile167 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_e1_tile168 = "leftTree.png"
    image eaeng_e1_tile169 = "rightTree.png"
    image eaeng_e1_tile170 = "leftTree.png"
    image eaeng_e1_tile171 = "rightTree.png"

    show eaeng_e1_tile168 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e1_tile169 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e1_tile170 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e1_tile171 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_e1_tile172 = "1_1_grey.png"
    image eaeng_e1_tile173 = "1_1_grey.png"
    image eaeng_e1_tile174 = "1_1_grey.png"
    image eaeng_e1_tile175 = "1_1_grey.png"

    show eaeng_e1_tile172 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e1_tile173 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e1_tile174 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e1_tile175 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)

    image eaeng_e1_tile176 = "letterBorder.png"
    image eaeng_e1_tile177 = "letterBorder.png"
    image eaeng_e1_tile178 = "letterBorder.png"
    image eaeng_e1_tile179 = "letterBorder.png"
    image eaeng_e1_tile180 = "letterBorder.png"
    image eaeng_e1_tile181 = "letterBorder.png"
    show eaeng_e1_tile176 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e1_tile177 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e1_tile178 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_e1_tile179 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e1_tile180 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e1_tile181 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)


    # gates
    $ eae1and1x = 275 
    $ eae1and1y = 575
    $ eae1and2x = 410
    $ eae1and2y = 575
    $ eae1and3x = 342 
    $ eae1and3y = 660
    $ eae1and4x = 275
    $ eae1and4y = 750
    $ eae1and5x = 410
    $ eae1and5y = 750
    $ eae1and6x = 342 
    $ eae1and6y = 832
    
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
    
    jump gamefile_e1

    label gamefile_e1:
    call screen logicGatese1

    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other tile here
            if and1in1 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in1 = False
            #sets values for checks
            $ eae1and1x = 1115
            $ eae1and1y = 340
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae1and1x = 1415
            $ eae1and1y = 340
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae1and1x = 1040
            $ eae1and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae1and1x = 1190
            $ eae1and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = True
            $ and1in5 = False
            $ and1in6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae1and1x = 1340
            $ eae1and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = True
            $ and1in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae1and1x = 1490
            $ eae1and1y = 515
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            $ and1in5 = False
            $ and1in6 = True

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae1and2x = 1115
            $ eae1and2y = 340
            $ and2in1 = True
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae1and2x = 1415
            $ eae1and2y = 340
            $ and2in1 = False
            $ and2in2 = True
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae1and2x = 1040
            $ eae1and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = True
            $ and2in4 = False
            $ and2in5 = False
            $ and2in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae1and2x = 1190
            $ eae1and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = True
            $ and2in5 = False
            $ and2in6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae1and2x = 1340
            $ eae1and2y = 515
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = False
            $ and2in4 = False
            $ and2in5 = True
            $ and2in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae1and2x = 1490
            $ eae1and2y = 515
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
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae1and3x = 1115
            $ eae1and3y = 340
            $ and3in1 = True
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae1and3x = 1415
            $ eae1and3y = 340
            $ and3in1 = False
            $ and3in2 = True
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae1and3x = 1040
            $ eae1and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = True
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae1and3x = 1190
            $ eae1and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = True
            $ and3in5 = False
            $ and3in6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae1and3x = 1340
            $ eae1and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = True
            $ and3in6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae1and3x = 1490
            $ eae1and3y = 515
            $ and3in1 = False
            $ and3in2 = False
            $ and3in3 = False
            $ and3in4 = False
            $ and3in5 = False
            $ and3in6 = True
          


    if gate_name == "letterN":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae1and4x = 1115
            $ eae1and4y = 340
            $ and4in1 = True
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae1and4x = 1415
            $ eae1and4y = 340
            $ and4in1 = False
            $ and4in2 = True
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae1and4x = 1040
            $ eae1and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = True
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae1and4x = 1190
            $ eae1and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = True
            $ and4in5 = False
            $ and4in6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae1and4x = 1340
            $ eae1and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = True
            $ and4in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae1and4x = 1490
            $ eae1and4y = 515
            $ and4in1 = False
            $ and4in2 = False
            $ and4in3 = False
            $ and4in4 = False
            $ and4in5 = False
            $ and4in6 = True
           


    if gate_name == "letterP":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae1and5x = 1115
            $ eae1and5y = 340
            $ and5in1 = True
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae1and5x = 1415
            $ eae1and5y = 340
            $ and5in1 = False
            $ and5in2 = True
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae1and5x = 1040
            $ eae1and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = True
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae1and5x = 1190
            $ eae1and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = True
            $ and5in5 = False
            $ and5in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae1and5x = 1340
            $ eae1and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = True
            $ and5in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae1and5x = 1490
            $ eae1and5y = 515
            $ and5in1 = False
            $ and5in2 = False
            $ and5in3 = False
            $ and5in4 = False
            $ and5in5 = False
            $ and5in6 = True
            
  

    if gate_name == "letterL":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in1 = False
            if and2in1 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in1 = False
            if and3in1 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in1 = False
            if and4in1 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in1 = False
            if and5in1 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in1 = False
            if and6in1 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in1 = False

            #sets values for checks
            $ eae1and6x = 1115
            $ eae1and6y = 340
            $ and6in1 = True
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in2 = False
            if and2in2 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in2 = False
            if and3in2 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in2 = False
            if and4in2 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in2 = False
            if and5in2 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in2 = False
            if and6in2 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in2 = False

            #sets check values
            $ eae1and6x = 1415
            $ eae1and6y = 340
            $ and6in1 = False
            $ and6in2 = True
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in3 = False
            if and2in3 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in3 = False
            if and3in3 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in3 = False
            if and4in3 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in3 = False
            if and5in3 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in3 = False
            if and6in3 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in3 = False

            #sets values for the checks
            $ eae1and6x = 1040
            $ eae1and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = True
            $ and6in4 = False
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if and1in4 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in4 = False
            if and2in4 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in4 = False
            if and3in4 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in4 = False
            if and4in4 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in4 = False
            if and5in4 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in4 = False
            if and6in4 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in4 = False

            #sets values for the checks
            $ eae1and6x = 1190
            $ eae1and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = True
            $ and6in5 = False
            $ and6in6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if and1in5 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in5 = False
            if and2in5 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in5 = False
            if and3in5 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in5 = False
            if and4in5 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in5 = False
            if and5in5 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in5 = False
            if and6in5 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in5 = False

            #sets values for the checks
            $ eae1and6x = 1340
            $ eae1and6y = 515
            $ and6in1 = False
            $ and6in2 = False
            $ and6in3 = False
            $ and6in4 = False
            $ and6in5 = True
            $ and6in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if and1in6 == True:
               $ eae1and1x = 275
               $ eae1and1y = 575
               $ and1in6 = False
            if and2in6 == True:
               $ eae1and2x = 410
               $ eae1and2y = 575
               $ and2in6 = False
            if and3in6 == True:
               $ eae1and3x = 342
               $ eae1and3y = 660
               $ and3in6 = False
            if and4in6 == True:
               $ eae1and4x = 275
               $ eae1and4y = 750
               $ and4in6 = False
            if and5in6 == True:
               $ eae1and5x = 410
               $ eae1and5y = 750
               $ and5in6 = False
            if and6in6 == True:
               $ eae1and6x = 342
               $ eae1and6y = 832
               $ and6in6 = False

            #sets values for the checks
            $ eae1and6x = 1490
            $ eae1and6y = 515
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

            if slot_name == "LetterJ_return":
                $ attempts +=1
                if gate_name == "letterJ":
                    $ eae1and1x = 275
                    $ eae1and1y = 575
                    $ and1in1 = False
                    $ and1in2 = False
                    $ and1in3 = False
                    $ and1in4 = False
                    $ and1in5 = False
                    $ and1in6 = False
   
            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ eae1and2x = 410
                    $ eae1and2y = 575
                    $ and2in1 = False
                    $ and2in2 = False
                    $ and2in3 = False
                    $ and2in4 = False
                    $ and2in5 = False
                    $ and2in6 = False
                    
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ eae1and3x = 342
                    $ eae1and3y = 660
                    $ and3in1 = False
                    $ and3in2 = False
                    $ and3in3 = False
                    $ and3in4 = False
                    $ and3in5 = False
                    $ and3in6 = False

            if slot_name == "LetterN_return":
                $ attempts +=1
                if gate_name == "letterN":
                    $ eae1and4x = 275
                    $ eae1and4y = 750
                    $ and4in1 = False
                    $ and4in2 = False
                    $ and4in3 = False
                    $ and4in4 = False
                    $ and4in5 = False
                    $ and4in6 = False

            if slot_name == "LetterP_return":
                $ attempts +=1
                if gate_name == "letterP":
                    $ eae1and5x = 410
                    $ eae1and5y = 750
                    $ and5in1 = False
                    $ and5in2 = False
                    $ and5in3 = False
                    $ and5in4 = False
                    $ and5in5 = False
                    $ and5in6 = False

            if slot_name == "LetterL_return":
                $ attempts +=1
                if gate_name == "letterL":
                    $ eae1and6x = 342
                    $ eae1and6y = 832
                    $ and6in1 = False
                    $ and6in2 = False
                    $ and6in3 = False
                    $ and6in4 = False
                    $ and6in5 = False
                    $ and6in6 = False

    play sound gramTree2



    if and5in1 == True and and1in2 == True:
        image eaeng_e1_tile182 = "leftTreegreenlong.png"
        image eaeng_e1_tile183 = "1_1_green.png"
        image eaeng_e1_tile184 = "rightTreegreenlong.png"
        image eaeng_e1_tile185 = "1_1_green.png"
        if (gramRow1_sound ==0):
            $gramRow1_sound +=1
            play sound gramTree1
        show eaeng_e1_tile182 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e1_tile183 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e1_tile184 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e1_tile185 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        
        if and3in3 == True and and6in4 == True:
            image eaeng_e1_tile186 = "leftTreegreen.png"
            image eaeng_e1_tile187 = "1_1_green.png"
            image eaeng_e1_tile188 = "solutionLine.png"
            image eaeng_e1_tile189 = "the.png"
            image eaeng_e1_tile190 = "rightTreegreen.png"
            image eaeng_e1_tile191 = "1_1_green.png"
            image eaeng_e1_tile192 = "solutionLine.png"
            image eaeng_e1_tile193 = "password.png"
            if ((gramRow2_soundA ==0) and (gramRow2_soundB==0)) or ((gramRow2_soundA==0) and (gramRow2_soundB==1)):
                play sound gramText1
                $gramRow2_soundA +=1
            show eaeng_e1_tile186 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile187 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile188 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile189 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e1_tile190 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile191 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile192 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile193 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)
        if and3in3 == False or and6in4 == False:
            hide eaeng_e1_tile186
            hide eaeng_e1_tile187
            hide eaeng_e1_tile188
            hide eaeng_e1_tile189
            hide eaeng_e1_tile190
            hide eaeng_e1_tile191
            hide eaeng_e1_tile192
            hide eaeng_e1_tile193

        if and4in5 == True and and2in6 == True:
            image eaeng_e1_tile194 = "leftTreegreen.png"
            image eaeng_e1_tile195 = "1_1_green.png"
            image eaeng_e1_tile196 = "solutionLine.png"
            image eaeng_e1_tile197 = "is.png"
            image eaeng_e1_tile198 = "rightTreegreen.png"
            image eaeng_e1_tile199 = "1_1_green.png"
            image eaeng_e1_tile200 = "solutionLine.png"
            image eaeng_e1_tile201 = "oolong.png"
            if ((gramRow2_soundA ==0) and (gramRow2_soundB==0)) or ((gramRow2_soundA ==1) and (gramRow2_soundB==0)):
                play sound gramText1
                $gramRow2_soundB +=1
            show eaeng_e1_tile194 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile195 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile196 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile197 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e1_tile198 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile199 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile200 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile201 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)
        if and4in5 == False or and2in6 == False:
            hide eaeng_e1_tile194
            hide eaeng_e1_tile195
            hide eaeng_e1_tile196
            hide eaeng_e1_tile197
            hide eaeng_e1_tile198
            hide eaeng_e1_tile199
            hide eaeng_e1_tile200
            hide eaeng_e1_tile201


        if (and1in5 == True or and2in5 == True or and3in5 == True or and5in5 == True or and6in5 == True) and (and1in6 == True or and3in6 == True or and4in6 == True or and5in6 == True or and6in6 == True):
            image eaeng_e1_tile202 = "leftTreered.png"
            image eaeng_e1_tile203 = "1_1_red.png"
            image eaeng_e1_tile204 = "rightTreered.png"
            image eaeng_e1_tile205 = "1_1_red.png"
            if((gramRow2_soundA==0) and (gramRow2_soundB==0))or((gramRow2_soundA==1) and (gramRow2_soundB==0)):
                play sound gramTree5
            show eaeng_e1_tile202 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile203 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile204 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile205 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in5 == False or and1in6 == False:
            hide eaeng_e1_tile202
            hide eaeng_e1_tile203
            hide eaeng_e1_tile204
            hide eaeng_e1_tile205

        if and4in5 == True and (and1in6 == True or and3in6 == True or and5in6 == True or and6in6 == True) or and2in6 == True and (and1in5 == True or and2in5 == True or and3in5 == True or and5in5 == True or and6in5 == True):
            image eaeng_e1_tile206 = "leftTreered.png"
            image eaeng_e1_tile207 = "1_1_red.png"
            image eaeng_e1_tile208 = "rightTreered.png"
            image eaeng_e1_tile209 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==1) and (gramRow2_soundB==0):
                play sound gramTree5
            show eaeng_e1_tile206 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile207 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile208 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile209 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in5 == False or and1in6 == False:
            hide eaeng_e1_tile206
            hide eaeng_e1_tile207
            hide eaeng_e1_tile208
            hide eaeng_e1_tile209

        if (and1in3 == True or and2in3 == True or and4in3 == True or and5in3 == True or and6in3 == True) and (and1in4 == True or and2in4 == True or and3in4 == True or and4in4 == True or and5in4 == True):
            image eaeng_e1_tile210 = "leftTreered.png"
            image eaeng_e1_tile211 = "1_1_red.png"
            image eaeng_e1_tile212 = "rightTreered.png"
            image eaeng_e1_tile213 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==0) and (gramRow2_soundB==1):
                play sound gramTree5
            show eaeng_e1_tile210 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile211 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile212 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile213 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in3 == False:
            hide eaeng_e1_tile210
            hide eaeng_e1_tile211
            hide eaeng_e1_tile212
            hide eaeng_e1_tile213

        if and3in3 == True and (and1in4 == True or and2in4 == True or and4in4 == True or and5in4 == True) or and6in4 == True and (and1in3 == True or and2in3 == True or and4in3 == True or and3in4 == True):
            image eaeng_e1_tile214 = "leftTreered.png"
            image eaeng_e1_tile215 = "1_1_red.png"
            image eaeng_e1_tile216 = "rightTreered.png"
            image eaeng_e1_tile217 = "1_1_red.png"
            if (gramRow2_soundA==0) and (gramRow2_soundB==0):
                play sound gramTree5
            if (gramRow2_soundA==0) and (gramRow2_soundB==1):
                play sound gramTree5
            show eaeng_e1_tile214 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile215 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile216 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile217 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        elif and1in3 == False or and1in4 == False: 
            hide eaeng_e1_tile214
            hide eaeng_e1_tile215
            hide eaeng_e1_tile216
            hide eaeng_e1_tile217


    if and5in1 == False or and1in2 == False:
        hide eaeng_e1_tile182
        hide eaeng_e1_tile183
        hide eaeng_e1_tile184
        hide eaeng_e1_tile185
        hide eaeng_e1_tile186
        hide eaeng_e1_tile187
        hide eaeng_e1_tile188
        hide eaeng_e1_tile189
        hide eaeng_e1_tile190
        hide eaeng_e1_tile191
        hide eaeng_e1_tile192
        hide eaeng_e1_tile193
        hide eaeng_e1_tile194
        hide eaeng_e1_tile195
        hide eaeng_e1_tile196
        hide eaeng_e1_tile197
        hide eaeng_e1_tile198
        hide eaeng_e1_tile199
        hide eaeng_e1_tile200
        hide eaeng_e1_tile201
        hide eaeng_e1_tile202
        hide eaeng_e1_tile203
        hide eaeng_e1_tile204
        hide eaeng_e1_tile205
        hide eaeng_e1_tile206
        hide eaeng_e1_tile207
        hide eaeng_e1_tile208
        hide eaeng_e1_tile209
        hide eaeng_e1_tile210
        hide eaeng_e1_tile211
        hide eaeng_e1_tile212
        hide eaeng_e1_tile213
        hide eaeng_e1_tile214
        hide eaeng_e1_tile215
        hide eaeng_e1_tile216
        hide eaeng_e1_tile217

    
    if (and1in1 == True or and2in1 == True or and3in1 == True or and4in1 == True or and6in1 == True) and (and2in2 == True or and3in2 == True or and4in2 == True or and5in2 == True or and6in2 == True):
         image eaeng_e1_tile218 = "leftTreeredlong.png"
         image eaeng_e1_tile219 = "1_1_red.png"
         image eaeng_e1_tile220 = "rightTreeredlong.png"
         image eaeng_e1_tile221 = "1_1_red.png"
         if(gramRow1_sound==0):
            play sound gramTree5
         show eaeng_e1_tile218 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e1_tile219 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e1_tile220 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e1_tile221 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and1in1 == False or and2in2 == False:
         hide eaeng_e1_tile218
         hide eaeng_e1_tile219
         hide eaeng_e1_tile220
         hide eaeng_e1_tile221

    if and5in1 == True and (and2in2 == True or and3in2 == True or and4in2 == True or and6in2 == True) or and1in2 == True and (and2in1 == True or and3in1 == True or and4in1 == True or and6in1 == True):
         image eaeng_e1_tile222 = "leftTreeredlong.png"
         image eaeng_e1_tile223 = "1_1_red.png"
         image eaeng_e1_tile224 = "rightTreeredlong.png"
         image eaeng_e1_tile225 = "1_1_red.png"
         if(gramRow1_sound==0):
            play sound gramTree5
         show eaeng_e1_tile222 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e1_tile223 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e1_tile224 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e1_tile225 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    elif and2in2 == False or and2in1 == False:
         hide eaeng_e1_tile222
         hide eaeng_e1_tile223
         hide eaeng_e1_tile224
         hide eaeng_e1_tile225


    #win conditions
    if and5in1 == True and and3in3 == True and and6in4 == True and and1in2 == True and and4in5 == True and and2in6 == True: 
        image eaeng_e1_tile226 = "letterP.png"
        image eaeng_e1_tile227 = "letterJ.png"
        image eaeng_e1_tile228 = "letterM.png"
        image eaeng_e1_tile229 = "letterL.png"
        image eaeng_e1_tile230 = "letterN.png"
        image eaeng_e1_tile231 = "letterK.png"
        show eaeng_e1_tile226 at Position(xpos = eae1and5x, xanchor = 0, ypos = eae1and5y, yanchor = 0)
        show eaeng_e1_tile227 at Position(xpos = eae1and1x, xanchor = 0, ypos = eae1and1y, yanchor = 0)
        show eaeng_e1_tile228 at Position(xpos = eae1and3x, xanchor = 0, ypos = eae1and3y, yanchor = 0)
        show eaeng_e1_tile229 at Position(xpos = eae1and6x, xanchor = 0, ypos = eae1and6y, yanchor = 0)
        show eaeng_e1_tile230 at Position(xpos = eae1and4x, xanchor = 0, ypos = eae1and4y, yanchor = 0)
        show eaeng_e1_tile231 at Position(xpos = eae1and2x, xanchor = 0, ypos = eae1and2y, yanchor = 0)
        queue sound gramWin
        $ renpy.pause(1.0)
        hide eaeng_e1_tile182
        hide eaeng_e1_tile183
        hide eaeng_e1_tile184
        hide eaeng_e1_tile185
        hide eaeng_e1_tile186
        hide eaeng_e1_tile187
        hide eaeng_e1_tile188
        hide eaeng_e1_tile189
        hide eaeng_e1_tile190
        hide eaeng_e1_tile191
        hide eaeng_e1_tile192
        hide eaeng_e1_tile193
        hide eaeng_e1_tile194
        hide eaeng_e1_tile195
        hide eaeng_e1_tile196
        hide eaeng_e1_tile197
        hide eaeng_e1_tile198
        hide eaeng_e1_tile199
        hide eaeng_e1_tile200
        hide eaeng_e1_tile201
        hide eaeng_e1_tile202
        hide eaeng_e1_tile203
        hide eaeng_e1_tile204
        hide eaeng_e1_tile205
        hide eaeng_e1_tile206
        hide eaeng_e1_tile207
        hide eaeng_e1_tile208
        hide eaeng_e1_tile209
        hide eaeng_e1_tile210
        hide eaeng_e1_tile211
        hide eaeng_e1_tile212
        hide eaeng_e1_tile213
        hide eaeng_e1_tile214
        hide eaeng_e1_tile215
        hide eaeng_e1_tile216
        hide eaeng_e1_tile217
        jump gramEasyDone  
    
    if attempts==0:
        queue sound gramLose
        image eaeng_e1_tile232 = "letterP.png"
        image eaeng_e1_tile233 = "letterJ.png"
        image eaeng_e1_tile234 = "letterM.png"
        image eaeng_e1_tile235 = "letterL.png"
        image eaeng_e1_tile236 = "letterN.png"
        image eaeng_e1_tile237 = "letterK.png"
        show eaeng_e1_tile232 at Position(xpos = eae1and5x, xanchor = 0, ypos = eae1and5y, yanchor = 0)
        show eaeng_e1_tile233 at Position(xpos = eae1and1x, xanchor = 0, ypos = eae1and1y, yanchor = 0)
        show eaeng_e1_tile234 at Position(xpos = eae1and3x, xanchor = 0, ypos = eae1and3y, yanchor = 0)
        show eaeng_e1_tile235 at Position(xpos = eae1and6x, xanchor = 0, ypos = eae1and6y, yanchor = 0)
        show eaeng_e1_tile236 at Position(xpos = eae1and4x, xanchor = 0, ypos = eae1and4y, yanchor = 0)
        show eaeng_e1_tile237 at Position(xpos = eae1and2x, xanchor = 0, ypos = eae1and2y, yanchor = 0)
        $attemptsGramEasy +=1
        $renpy.pause(1.5)
        hide eaeng_e1_tile182
        hide eaeng_e1_tile183
        hide eaeng_e1_tile184
        hide eaeng_e1_tile185
        hide eaeng_e1_tile186
        hide eaeng_e1_tile187
        hide eaeng_e1_tile188
        hide eaeng_e1_tile189
        hide eaeng_e1_tile190
        hide eaeng_e1_tile191
        hide eaeng_e1_tile192
        hide eaeng_e1_tile193
        hide eaeng_e1_tile194
        hide eaeng_e1_tile195
        hide eaeng_e1_tile196
        hide eaeng_e1_tile197
        hide eaeng_e1_tile198
        hide eaeng_e1_tile199
        hide eaeng_e1_tile200
        hide eaeng_e1_tile201
        hide eaeng_e1_tile202
        hide eaeng_e1_tile203
        hide eaeng_e1_tile204
        hide eaeng_e1_tile205
        hide eaeng_e1_tile206
        hide eaeng_e1_tile207
        hide eaeng_e1_tile208
        hide eaeng_e1_tile209
        hide eaeng_e1_tile210
        hide eaeng_e1_tile211
        hide eaeng_e1_tile212
        hide eaeng_e1_tile213
        hide eaeng_e1_tile214
        hide eaeng_e1_tile215
        hide eaeng_e1_tile216
        hide eaeng_e1_tile217
        jump gramEasyLose
    
    jump gamefile_e1