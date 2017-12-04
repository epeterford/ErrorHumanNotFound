

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
    text "Moves" xpos 200 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 315 ypos 293 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 350 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27
    draggroup:
        #and gates
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae2letterKx ypos eae2letterKy
        drag:
                drag_name "letterN"
                child "letterN.png"
                droppable False
                dragged gate_dragged
                xpos eae2letterNx ypos eae2letterNy
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae2letterMx ypos eae2letterMy
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae2letterPx ypos eae2letterPy
        drag:
                drag_name "letterS"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae2letterSx ypos eae2letterSy
        drag:
                drag_name "letterQ"
                child "letterQ.png"
                droppable False
                dragged gate_dragged
                xpos eae2letterQx ypos eae2letterQy
        
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

        #dragback
        
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterN_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterM_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648
        drag:
                drag_name "LetterP_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterS_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738
        drag:
                drag_name "LetterQ_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 817




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

   #Transparent Letters for Dragbacks
    image eaeng_e2_tile300 = "letterK_grey.png"
    image eaeng_e2_tile301 = "letterN_grey.png"
    image eaeng_e2_tile302 = "letterM_grey.png"
    image eaeng_e2_tile303 = "letterP_grey.png"
    image eaeng_e2_tile304 = "letterS_grey.png"
    image eaeng_e2_tile305 = "letterQ_grey.png"
    show eaeng_e2_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e2_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e2_tile302 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_e2_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e2_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e2_tile305 at Position(xpos = 342, xanchor = 0, ypos = 832, yanchor = 0)


    # gates
    $ eae2letterKx = 275 
    $ eae2letterKy = 575
    $ eae2letterNx = 410
    $ eae2letterNy = 575
    $ eae2letterMx = 342 
    $ eae2letterMy = 660
    $ eae2letterPx = 275
    $ eae2letterPy = 750
    $ eae2letterSx = 410
    $ eae2letterSy = 750
    $ eae2letterQx = 342 
    $ eae2letterQy = 832
    
    # check conditons for locations
    $ letterKin1 = False
    $ letterKin2 = False
    $ letterKin3 = False
    $ letterKin4 = False
    $ letterKin5 = False
    $ letterKin6 = False
    $ letterKin7 = False

    $ letterNin1 = False
    $ letterNin2 = False
    $ letterNin3 = False
    $ letterNin4 = False
    $ letterNin5 = False
    $ letterNin6 = False
    $ letterNin7 = False

    $ letterMin1 = False
    $ letterMin2 = False
    $ letterMin3 = False
    $ letterMin4 = False
    $ letterMin5 = False
    $ letterMin6 = False
    $ letterMin7 = False

    $ letterPin1 = False
    $ letterPin2 = False
    $ letterPin3 = False
    $ letterPin4 = False
    $ letterPin5 = False
    $ letterPin6 = False
    $ letterPin7 = False

    $ letterSin1 = False
    $ letterSin2 = False
    $ letterSin3 = False
    $ letterSin4 = False
    $ letterSin5 = False
    $ letterSin6 = False
    $ letterSin7 = False


    $ letterQin1 = False
    $ letterQin2 = False
    $ letterQin3 = False
    $ letterQin4 = False
    $ letterQin5 = False
    $ letterQin6 = False
    $ letterQin7 = False



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
            if letterKin1 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin1 = False
            if letterNin1 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin1 = False
            if letterMin1 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin1 = False
            if letterSin1 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin1 = False
            if letterQin1 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin1 = False
            #sets values for checks
            $ eae2letterKx = 1115
            $ eae2letterKy = 340
            $ letterKin1 = True
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin2 = False
            if letterNin2 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin2 = False
            if letterMin2 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin2 = False
            if letterSin2 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin2 = False
            if letterQin2 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin2 = False

            #sets check values
            $ eae2letterKx = 1415
            $ eae2letterKy = 340
            $ letterKin1 = False
            $ letterKin2 = True
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin3 = False
            if letterNin3 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin3 = False
            if letterMin3 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin3 = False
            if letterSin3 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin3 = False
            if letterQin3 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin3 = False

            #sets values for the checks
            $ eae2letterKx = 1040
            $ eae2letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = True
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin4 = False
            if letterNin4 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin4 = False
            if letterMin4 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin4 = False
            if letterSin4 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin4 = False
            if letterQin4 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin4 = False

            #sets values for the checks
            $ eae2letterKx = 1190
            $ eae2letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = True
            $ letterKin5 = False
            $ letterKin6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin5 = False
            if letterNin5 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin5 = False
            if letterMin5 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin5 = False
            if letterSin5 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin5 = False
            if letterQin5 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin5 = False

            #sets values for the checks
            $ eae2letterKx = 1340
            $ eae2letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = True
            $ letterKin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterNin6 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin6 = False
            if letterMin6 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin6 = False
            if letterSin6 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin6 = False
            if letterQin6 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin6 = False

            #sets values for the checks
            $ eae2letterKx = 1490
            $ eae2letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = True

    if gate_name == "letterN":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin1 = False
            if letterNin1 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin1 = False
            if letterMin1 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin1 = False
            if letterSin1 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin1 = False
            if letterQin1 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin1 = False

            #sets values for checks
            $ eae2letterNx = 1115
            $ eae2letterNy = 340
            $ letterNin1 = True
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin2 = False
            if letterNin2 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin2 = False
            if letterMin2 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin2 = False
            if letterSin2 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin2 = False
            if letterQin2 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin2 = False

            #sets check values
            $ eae2letterNx = 1415
            $ eae2letterNy = 340
            $ letterNin1 = False
            $ letterNin2 = True
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin3 = False
            if letterNin3 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin3 = False
            if letterMin3 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin3 = False
            if letterSin3 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin3 = False
            if letterQin3 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin3 = False

            #sets values for the checks
            $ eae2letterNx = 1040
            $ eae2letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = True
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin4 = False
            if letterNin4 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin4 = False
            if letterMin4 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin4 = False
            if letterSin4 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin4 = False
            if letterQin4 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin4 = False

            #sets values for the checks
            $ eae2letterNx = 1190
            $ eae2letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = True
            $ letterNin5 = False
            $ letterNin6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin5 = False
            if letterNin5 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin5 = False
            if letterMin5 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin5 = False
            if letterSin5 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin5 = False
            if letterQin5 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin5 = False

            #sets values for the checks
            $ eae2letterNx = 1340
            $ eae2letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = True
            $ letterNin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin6 = False
            if letterNin6 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin6 = False
            if letterMin6 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin6 = False
            if letterSin6 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin6 = False
            if letterQin6 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin6 = False

            #sets values for the checks
            $ eae2letterNx = 1490
            $ eae2letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin1 = False
            if letterNin1 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin1 = False
            if letterMin1 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin1 = False
            if letterSin1 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin1 = False
            if letterQin1 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin1 = False

            #sets values for checks
            $ eae2letterMx = 1115
            $ eae2letterMy = 340
            $ letterMin1 = True
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin2 = False
            if letterNin2 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin2 = False
            if letterMin2 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin2 = False
            if letterSin2 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin2 = False
            if letterQin2 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin2 = False

            #sets check values
            $ eae2letterMx = 1415
            $ eae2letterMy = 340
            $ letterMin1 = False
            $ letterMin2 = True
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin3 = False
            if letterNin3 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin3 = False
            if letterMin3 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin3 = False
            if letterSin3 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin3 = False
            if letterQin3 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin3 = False

            #sets values for the checks
            $ eae2letterMx = 1040
            $ eae2letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = True
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin4 = False
            if letterNin4 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin4 = False
            if letterMin4 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin4 = False
            if letterSin4 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin4 = False
            if letterQin4 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin4 = False

            #sets values for the checks
            $ eae2letterMx = 1190
            $ eae2letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = True
            $ letterMin5 = False
            $ letterMin6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin5 = False
            if letterNin5 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin5 = False
            if letterMin5 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin5 = False
            if letterSin5 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin5 = False
            if letterQin5 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin5 = False

            #sets values for the checks
            $ eae2letterMx = 1340
            $ eae2letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = True
            $ letterMin6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin6 = False
            if letterNin6 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin6 = False
            if letterMin6 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin6 = False
            if letterSin6 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin6 = False
            if letterQin6 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin6 = False

            #sets values for the checks
            $ eae2letterMx = 1490
            $ eae2letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = True
          


    if gate_name == "letterP":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin1 = False
            if letterNin1 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin1 = False
            if letterMin1 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin1 = False
            if letterSin1 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin1 = False
            if letterQin1 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin1 = False

            #sets values for checks
            $ eae2letterPx = 1115
            $ eae2letterPy = 340
            $ letterPin1 = True
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin2 = False
            if letterNin2 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin2 = False
            if letterMin2 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin2 = False
            if letterSin2 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin2 = False
            if letterQin2 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin2 = False

            #sets check values
            $ eae2letterPx = 1415
            $ eae2letterPy = 340
            $ letterPin1 = False
            $ letterPin2 = True
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin3 = False
            if letterNin3 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin3 = False
            if letterMin3 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin3 = False
            if letterSin3 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin3 = False
            if letterQin3 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin3 = False

            #sets values for the checks
            $ eae2letterPx = 1040
            $ eae2letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = True
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin4 = False
            if letterNin4 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin4 = False
            if letterMin4 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin4 = False
            if letterSin4 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin4 = False
            if letterQin4 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin4 = False

            #sets values for the checks
            $ eae2letterPx = 1190
            $ eae2letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = True
            $ letterPin5 = False
            $ letterPin6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin5 = False
            if letterNin5 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin5 = False
            if letterMin5 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin5 = False
            if letterSin5 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin5 = False
            if letterQin5 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin5 = False

            #sets values for the checks
            $ eae2letterPx = 1340
            $ eae2letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = True
            $ letterPin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin6 = False
            if letterNin6 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin6 = False
            if letterMin6 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin6 = False
            if letterSin6 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin6 = False
            if letterQin6 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin6 = False

            #sets values for the checks
            $ eae2letterPx = 1490
            $ eae2letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = True
           


    if gate_name == "letterS":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin1 = False
            if letterNin1 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin1 = False
            if letterMin1 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin1 = False
            if letterSin1 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin1 = False
            if letterQin1 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin1 = False

            #sets values for checks
            $ eae2letterSx = 1115
            $ eae2letterSy = 340
            $ letterSin1 = True
            $ letterSin2 = False
            $ letterSin3 = False
            $ letterSin4 = False
            $ letterSin5 = False
            $ letterSin6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin2 = False
            if letterNin2 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin2 = False
            if letterMin2 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin2 = False
            if letterSin2 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin2 = False
            if letterQin2 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin2 = False

            #sets check values
            $ eae2letterSx = 1415
            $ eae2letterSy = 340
            $ letterSin1 = False
            $ letterSin2 = True
            $ letterSin3 = False
            $ letterSin4 = False
            $ letterSin5 = False
            $ letterSin6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin3 = False
            if letterNin3 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin3 = False
            if letterMin3 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin3 = False
            if letterSin3 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin3 = False
            if letterQin3 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin3 = False

            #sets values for the checks
            $ eae2letterSx = 1040
            $ eae2letterSy = 515
            $ letterSin1 = False
            $ letterSin2 = False
            $ letterSin3 = True
            $ letterSin4 = False
            $ letterSin5 = False
            $ letterSin6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin4 = False
            if letterNin4 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin4 = False
            if letterMin4 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin4 = False
            if letterSin4 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin4 = False
            if letterQin4 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin4 = False

            #sets values for the checks
            $ eae2letterSx = 1190
            $ eae2letterSy = 515
            $ letterSin1 = False
            $ letterSin2 = False
            $ letterSin3 = False
            $ letterSin4 = True
            $ letterSin5 = False
            $ letterSin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin5 = False
            if letterNin5 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin5 = False
            if letterMin5 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin5 = False
            if letterSin5 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin5 = False
            if letterQin5 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin5 = False

            #sets values for the checks
            $ eae2letterSx = 1340
            $ eae2letterSy = 515
            $ letterSin1 = False
            $ letterSin2 = False
            $ letterSin3 = False
            $ letterSin4 = False
            $ letterSin5 = True
            $ letterSin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin6 = False
            if letterNin6 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin6 = False
            if letterMin6 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin6 = False
            if letterSin6 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin6 = False
            if letterQin6 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin6 = False

            #sets values for the checks
            $ eae2letterSx = 1490
            $ eae2letterSy = 515
            $ letterSin1 = False
            $ letterSin2 = False
            $ letterSin3 = False
            $ letterSin4 = False
            $ letterSin5 = False
            $ letterSin6 = True
            
  

    if gate_name == "letterQ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin1 = False
            if letterNin1 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin1 = False
            if letterMin1 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin1 = False
            if letterSin1 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin1 = False
            if letterQin1 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin1 = False

            #sets values for checks
            $ eae2letterQx = 1115
            $ eae2letterQy = 340
            $ letterQin1 = True
            $ letterQin2 = False
            $ letterQin3 = False
            $ letterQin4 = False
            $ letterQin5 = False
            $ letterQin6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin2 = False
            if letterNin2 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin2 = False
            if letterMin2 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin2 = False
            if letterSin2 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin2 = False
            if letterQin2 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin2 = False

            #sets check values
            $ eae2letterQx = 1415
            $ eae2letterQy = 340
            $ letterQin1 = False
            $ letterQin2 = True
            $ letterQin3 = False
            $ letterQin4 = False
            $ letterQin5 = False
            $ letterQin6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin3 = False
            if letterNin3 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin3 = False
            if letterMin3 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin3 = False
            if letterSin3 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin3 = False
            if letterQin3 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin3 = False

            #sets values for the checks
            $ eae2letterQx = 1040
            $ eae2letterQy = 515
            $ letterQin1 = False
            $ letterQin2 = False
            $ letterQin3 = True
            $ letterQin4 = False
            $ letterQin5 = False
            $ letterQin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin4 = False
            if letterNin4 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin4 = False
            if letterMin4 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin4 = False
            if letterSin4 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin4 = False
            if letterQin4 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin4 = False

            #sets values for the checks
            $ eae2letterQx = 1190
            $ eae2letterQy = 515
            $ letterQin1 = False
            $ letterQin2 = False
            $ letterQin3 = False
            $ letterQin4 = True
            $ letterQin5 = False
            $ letterQin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin5 = False
            if letterNin5 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin5 = False
            if letterMin5 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin5 = False
            if letterSin5 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin5 = False
            if letterQin5 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin5 = False

            #sets values for the checks
            $ eae2letterQx = 1340
            $ eae2letterQy = 515
            $ letterQin1 = False
            $ letterQin2 = False
            $ letterQin3 = False
            $ letterQin4 = False
            $ letterQin5 = True
            $ letterQin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae2letterKx = 275
               $ eae2letterKy = 575
               $ letterKin6 = False
            if letterNin6 == True:
               $ eae2letterNx = 410
               $ eae2letterNy = 575
               $ letterNin6 = False
            if letterMin6 == True:
               $ eae2letterMx = 342
               $ eae2letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae2letterPx = 275
               $ eae2letterPy = 750
               $ letterPin6 = False
            if letterSin6 == True:
               $ eae2letterSx = 410
               $ eae2letterSy = 750
               $ letterSin6 = False
            if letterQin6 == True:
               $ eae2letterQx = 342
               $ eae2letterQy = 832
               $ letterQin6 = False

            #sets values for the checks
            $ eae2letterQx = 1490
            $ eae2letterQy = 515
            $ letterQin1 = False
            $ letterQin2 = False
            $ letterQin3 = False
            $ letterQin4 = False
            $ letterQin5 = False
            $ letterQin6 = True
    if (temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "LetterK_return" or slot_name == "LetterN_return" or slot_name == "LetterM_return" or slot_name == "LetterP_return" or slot_name == "LetterS_return" or slot_name == "LetterQ_return"):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ eae2letterKx = 275
                    $ eae2letterKy = 575
                    $ letterKin1 = False
                    $ letterKin2 = False
                    $ letterKin3 = False
                    $ letterKin4 = False
                    $ letterKin5 = False
                    $ letterKin6 = False
                    $ letterKin7 = False
   
            if slot_name == "LetterN_return":
                $ attempts +=1
                if gate_name == "letterN":
                    $ eae2letterNx = 410
                    $ eae2letterNy = 575
                    $ letterNin1 = False
                    $ letterNin2 = False
                    $ letterNin3 = False
                    $ letterNin4 = False
                    $ letterNin5 = False
                    $ letterNin6 = False
                    $ letterNin7 = False
                    
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ eae2letterMx = 342
                    $ eae2letterMy = 660
                    $ letterMin1 = False
                    $ letterMin2 = False
                    $ letterMin3 = False
                    $ letterMin4 = False
                    $ letterMin5 = False
                    $ letterMin6 = False
                    $ letterMin7 = False

            if slot_name == "LetterP_return":
                $ attempts +=1
                if gate_name == "letterP":
                    $ eae2letterPx = 275
                    $ eae2letterPy = 750
                    $ letterPin1 = False
                    $ letterPin2 = False
                    $ letterPin3 = False
                    $ letterPin4 = False
                    $ letterPin5 = False
                    $ letterPin6 = False
                    $ letterPin7 = False

            if slot_name == "LetterS_return":
                $ attempts +=1
                if gate_name == "letterS":
                    $ eae2letterSx = 410
                    $ eae2letterSy = 750
                    $ letterSin1 = False
                    $ letterSin2 = False
                    $ letterSin3 = False
                    $ letterSin4 = False
                    $ letterSin5 = False
                    $ letterSin6 = False
                    $ letterSin7 = False

            if slot_name == "LetterQ_return":
                $ attempts +=1
                if gate_name == "letterQ":
                    $ eae2letterQx = 342
                    $ eae2letterQy = 832
                    $ letterQin1 = False
                    $ letterQin2 = False
                    $ letterQin3 = False
                    $ letterQin4 = False
                    $ letterQin5 = False
                    $ letterQin6 = False
                    $ letterQin7 = False
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
    hide eaeng_e2_tile78
    hide eaeng_e2_tile79
    hide eaeng_e2_tile80
    hide eaeng_e2_tile81
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if letterSin1 and letterKin2:
        image eaeng_e2_tile42 = "leftTreegreenlong.png"
        image eaeng_e2_tile43 = "1_1_green.png"
        image eaeng_e2_tile44 = "rightTreegreenlong.png"
        image eaeng_e2_tile45 = "1_1_green.png"
        if (gramRow1_C_sound_right1 ==0):
            $gramRow1_C_sound_right1 +=1
            play sound gramTree1
        show eaeng_e2_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e2_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        
        if letterMin3 and letterQin4:
            image eaeng_e2_tile46 = "leftTreegreen.png"
            image eaeng_e2_tile47 = "1_1_green.png"
            image eaeng_e2_tile48 = "solutionLine.png"
            image eaeng_e2_tile49 = "change.png"
            image eaeng_e2_tile50 = "rightTreegreen.png"
            image eaeng_e2_tile51 = "1_1_green.png"
            image eaeng_e2_tile52 = "solutionLine.png"
            image eaeng_e2_tile53 = "your.png"
            if gramRow2_L_sound_right1 ==0:
                play sound gramTree1
                queue sound gramText1
                $gramRow2_L_sound_right1 +=1
            show eaeng_e2_tile46 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile47 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile48 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile49 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e2_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)
     
        elif (letterNin3 or letterPin3 or letterMin3 or letterQin3) and (letterNin4 or letterMin4 or letterPin4 or letterQin4):
            image eaeng_e2_tile54 = "leftTreered.png"
            image eaeng_e2_tile55 = "1_1_red.png"
            image eaeng_e2_tile56 = "rightTreered.png"
            image eaeng_e2_tile57 = "1_1_red.png"
            if gramRow2_L_sound_wrong1 ==0:
                $gramRow2_L_sound_wrong1 +=1
                play sound gramTree5
            show eaeng_e2_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        if not(letterMin3 and letterQin4):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1
        if not((letterNin3 or letterPin3 or letterMin3 or letterQin3) and (letterNin4 or letterMin4 or letterPin4 or letterQin4)):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1

        if letterPin5 and letterNin6:
            image eaeng_e2_tile62 = "leftTreegreen.png"
            image eaeng_e2_tile63 = "1_1_green.png"
            image eaeng_e2_tile64 = "solutionLine.png"
            image eaeng_e2_tile65 = "password.png"
            image eaeng_e2_tile66 = "rightTreegreen.png"
            image eaeng_e2_tile67 = "1_1_green.png"
            image eaeng_e2_tile68 = "solutionLine.png"
            image eaeng_e2_tile69 = "roberta.png"
            if gramRow2_R_sound_right1 ==0:
                $gramRow2_R_sound_right1 +=1
                play sound gramTree1
                queue sound gramText1
            show eaeng_e2_tile62 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile63 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile64 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile65 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e2_tile66 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile67 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile68 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e2_tile69 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)

        elif ((letterNin5 or letterPin5 or letterMin5 or letterQin5) and (letterNin6 or letterMin6 or letterPin6 or letterQin6)):
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

        if (not((letterNin5 or letterPin5 or letterMin5 or letterQin5) and (letterNin6 or letterMin6 or letterPin6 or letterQin6))):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1
        if not(letterPin5 and letterNin6):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1

    elif letterMin1 and letterQin2:
        if (gramRow1_C_sound_right2 ==0):
            $gramRow1_C_sound_right2 +=1
            play sound gramTree1
        show eaeng_e2_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e2_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e2_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

        if (letterKin3 or letterNin3 or letterPin3 or letterSin3) and (letterKin4 or letterNin4 or letterPin4 or letterSin4 or letterQin4):
            if gramRow2_L_sound_wrong2 ==0:
                $gramRow2_L_sound_wrong2 +=1
                play sound gramTree5
            show eaeng_e2_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        if not((letterNin3 or letterPin3 or letterKin3 or letterSin3) and (letterNin4 or letterKin4 or letterPin4 or letterSin4)):
            if gramRow2_L_sound_wrong2 ==1:
                $gramRow2_L_sound_wrong2 -=1


        if (letterKin5 or letterNin5 or letterPin5 or letterSin5) and (letterKin6 or letterNin6 or letterPin6 or letterSin6):
            if gramRow2_R_sound_wrong2 ==0:
                $gramRow2_R_sound_wrong2 +=1
                play sound gramTree5
            show eaeng_e2_tile70 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile71 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e2_tile72 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e2_tile73 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        if (not((letterNin5 or letterPin5 or letterKin5 or letterSin5) and (letterNin6 or letterKin6 or letterPin6 or letterSin6))):
            if gramRow2_R_sound_wrong2 ==1:
                $gramRow2_R_sound_wrong2 -=1
    elif(letterKin1 or letterNin1 or letterPin1 or letterQin1 or letterSin1 or letterMin1) and (letterNin2 or letterMin2 or letterPin2 or letterSin2 or letterKin2 or letterQin2):
         image eaeng_e2_tile78 = "leftTreeredlong.png"
         image eaeng_e2_tile79 = "1_1_red.png"
         image eaeng_e2_tile80 = "rightTreeredlong.png"
         image eaeng_e2_tile81 = "1_1_red.png"
         if (gramRow1_C_sound_wrong1==0):
             play sound gramTree5
             $gramRow1_C_sound_wrong1 +=1
         show eaeng_e2_tile78 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile79 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e2_tile80 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e2_tile81 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    if not(letterSin1 and letterKin2):
        if (gramRow1_C_sound_right1 ==1):
            $gramRow1_C_sound_right1 -=1
    if not(letterMin1 and letterQin2):
        if (gramRow1_C_sound_right2 ==1):
            $gramRow1_C_sound_right2 -=1
    if not((letterKin1 or letterNin1 or letterPin1 or letterQin1 or letterSin1 or letterMin1) and (letterNin2 or letterMin2 or letterPin2 or letterSin2 or letterKin2 or letterMin2)):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1
         
    #win conditions
    if letterSin1 == True and letterMin3 == True and letterQin4 == True and letterKin2 == True and letterPin5 == True and letterNin6 == True: 
        image eaeng_e2_tile107 = "letterK.png"
        image eaeng_e2_tile111 = "letterN.png"
        image eaeng_e2_tile108 = "letterM.png"
        image eaeng_e2_tile110 = "letterP.png"
        image eaeng_e2_tile106 = "letterS.png"
        image eaeng_e2_tile109 = "letterQ.png"
        

        show eaeng_e2_tile107 at Position(xpos = eae2letterKx, xanchor = 0, ypos = eae2letterKy, yanchor = 0)
        show eaeng_e2_tile111 at Position(xpos = eae2letterNx, xanchor = 0, ypos = eae2letterNy, yanchor = 0)
        show eaeng_e2_tile108 at Position(xpos = eae2letterMx, xanchor = 0, ypos = eae2letterMy, yanchor = 0)
        show eaeng_e2_tile110 at Position(xpos = eae2letterPx, xanchor = 0, ypos = eae2letterPy, yanchor = 0)
        show eaeng_e2_tile106 at Position(xpos = eae2letterSx, xanchor = 0, ypos = eae2letterSy, yanchor = 0)
        show eaeng_e2_tile109 at Position(xpos = eae2letterQx, xanchor = 0, ypos = eae2letterQy, yanchor = 0)

        queue sound gramWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramEasyWin
        jump gramEasyDone
        
        
    if attempts ==0:
        queue sound gramLose
        image eaeng_e2_tile107 = "letterK.png"
        image eaeng_e2_tile111 = "letterN.png"
        image eaeng_e2_tile108 = "letterM.png"
        image eaeng_e2_tile110 = "letterP.png"
        image eaeng_e2_tile106 = "letterS.png"
        image eaeng_e2_tile109 = "letterQ.png"
        show eaeng_e2_tile107 at Position(xpos = eae2letterKx, xanchor = 0, ypos = eae2letterKy, yanchor = 0)
        show eaeng_e2_tile111 at Position(xpos = eae2letterNx, xanchor = 0, ypos = eae2letterNy, yanchor = 0)
        show eaeng_e2_tile108 at Position(xpos = eae2letterMx, xanchor = 0, ypos = eae2letterMy, yanchor = 0)
        show eaeng_e2_tile110 at Position(xpos = eae2letterPx, xanchor = 0, ypos = eae2letterPy, yanchor = 0)
        show eaeng_e2_tile106 at Position(xpos = eae2letterSx, xanchor = 0, ypos = eae2letterSy, yanchor = 0)
        show eaeng_e2_tile109 at Position(xpos = eae2letterQx, xanchor = 0, ypos = eae2letterQy, yanchor = 0)
        $ renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_gramEasyLose
        $attemptsGramEasy +=1
        jump gramEasyLose
    
    jump gamefile_e2