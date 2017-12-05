
screen logicGatese4:
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
        action Jump("gramEasyHints4")
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
                drag_name "letterH"
                child "letterH.png"
                droppable False
                dragged gate_dragged
                xpos eae4letterHx ypos eae4letterHy
        drag:
                drag_name "letterB"
                child "letterB.png"
                droppable False
                dragged gate_dragged
                xpos eae4letterBx ypos eae4letterBy
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae4letterPx ypos eae4letterPy
        drag:
                drag_name "letterR"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos eae4letterRx ypos eae4letterRy
        drag:
                drag_name "letterG"
                child "letterG.png"
                droppable False
                dragged gate_dragged
                xpos eae4letterGx ypos eae4letterGy
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae4letterKx ypos eae4letterKy
        
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
                drag_name "LetterH_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterB_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterP_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648
        drag:
                drag_name "LetterR_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterG_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 817



init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_e4:
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
    image eaeng_e4_tile0 = "instructions4.png"
    image eaeng_e4_tile1 = "1_1_green.png"
    image eaeng_e4_tile2 = "letterS.png"
    show eaeng_e4_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_e4_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_e4_tile2 at Position(xpos = 1265, xanchor = 0, ypos = 167, yanchor = 0)
    
    #row2 5-8

    image eaeng_e4_tile5 = "leftTreelong.png"
    image eaeng_e4_tile6 = "rightTreelong.png"

    show eaeng_e4_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_e4_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_e4_tile9 = "1_1_grey.png"
    image eaeng_e4_tile10 = "1_1_grey.png"
    

    show eaeng_e4_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_e4_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_e4_tile14 = "leftTree.png"
    image eaeng_e4_tile15 = "rightTree.png"
    image eaeng_e4_tile16 = "leftTree.png"
    image eaeng_e4_tile17 = "rightTree.png"

    show eaeng_e4_tile14 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e4_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e4_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e4_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_e4_tile21 = "1_1_grey.png"
    image eaeng_e4_tile22 = "1_1_grey.png"
    image eaeng_e4_tile23 = "1_1_grey.png"
    image eaeng_e4_tile24 = "1_1_grey.png"

    show eaeng_e4_tile21 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e4_tile22 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e4_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e4_tile24 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)

    image eaeng_e4_tile31 = "letterBorder.png"
    image eaeng_e4_tile32 = "letterBorder.png"
    image eaeng_e4_tile33 = "letterBorder.png"
    image eaeng_e4_tile34 = "letterBorder.png"
    image eaeng_e4_tile35 = "letterBorder.png"
    image eaeng_e4_tile36 = "letterBorder.png"
    show eaeng_e4_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e4_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e4_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_e4_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e4_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_e4_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)

    #Transparent Letters for Dragbacks
    image eaeng_e4_tile300 = "letterH_grey.png"
    image eaeng_e4_tile301 = "letterB_grey.png"
    image eaeng_e4_tile302 = "letterP_grey.png"
    image eaeng_e4_tile303 = "letterR_grey.png"
    image eaeng_e4_tile304 = "letterG_grey.png"
    image eaeng_e4_tile305 = "letterK_grey.png"
    show eaeng_e4_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e4_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e4_tile302 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_e4_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e4_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e4_tile305 at Position(xpos = 342, xanchor = 0, ypos = 832, yanchor = 0)


    # gates
    $ eae4letterHx = 275 
    $ eae4letterHy = 575
    $ eae4letterBx = 410
    $ eae4letterBy = 575
    $ eae4letterPx = 342 
    $ eae4letterPy = 660
    $ eae4letterRx = 275
    $ eae4letterRy = 750
    $ eae4letterGx = 410
    $ eae4letterGy = 750
    $ eae4letterKx = 342 
    $ eae4letterKy = 832
    
    # check conditons for locations
    $ letterHin1 = False
    $ letterHin2 = False
    $ letterHin3 = False
    $ letterHin4 = False
    $ letterHin5 = False
    $ letterHin6 = False
    $ letterHin7 = False

    $ letterBin1 = False
    $ letterBin2 = False
    $ letterBin3 = False
    $ letterBin4 = False
    $ letterBin5 = False
    $ letterBin6 = False
    $ letterBin7 = False

    $ letterPin1 = False
    $ letterPin2 = False
    $ letterPin3 = False
    $ letterPin4 = False
    $ letterPin5 = False
    $ letterPin6 = False
    $ letterPin7 = False

    $ letterRin1 = False
    $ letterRin2 = False
    $ letterRin3 = False
    $ letterRin4 = False
    $ letterRin5 = False
    $ letterRin6 = False
    $ letterRin7 = False

    $ letterGin1 = False
    $ letterGin2 = False
    $ letterGin3 = False
    $ letterGin4 = False
    $ letterGin5 = False
    $ letterGin6 = False
    $ letterGin7 = False


    $ letterKin1 = False
    $ letterKin2 = False
    $ letterKin3 = False
    $ letterKin4 = False
    $ letterKin5 = False
    $ letterKin6 = False
    $ letterKin7 = False



    #attempts for players
    $ attempts = 8
    
    jump gamefile_e4

label gamefile_e4:
    #image moon = "images/blankeaeng_e4_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatese4

    if gate_name == "letterH":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other eaeng_e4_tile here
            if letterHin1 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin1 = False
            if letterBin1 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin1 = False
            if letterPin1 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin1 = False
            if letterRin1 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin1 = False
            if letterGin1 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin1 = False
            if letterKin1 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin1 = False
            #sets values for checks
            $ eae4letterHx = 1115
            $ eae4letterHy = 340
            $ letterHin1 = True
            $ letterHin2 = False
            $ letterHin3 = False
            $ letterHin4 = False
            $ letterHin5 = False
            $ letterHin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterHin2 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin2 = False
            if letterBin2 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin2 = False
            if letterPin2 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin2 = False
            if letterRin2 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin2 = False
            if letterGin2 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin2 = False
            if letterKin2 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin2 = False

            #sets check values
            $ eae4letterHx = 1415
            $ eae4letterHy = 340
            $ letterHin1 = False
            $ letterHin2 = True
            $ letterHin3 = False
            $ letterHin4 = False
            $ letterHin5 = False
            $ letterHin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterHin3 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin3 = False
            if letterBin3 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin3 = False
            if letterPin3 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin3 = False
            if letterRin3 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin3 = False
            if letterGin3 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin3 = False
            if letterKin3 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin3 = False

            #sets values for the checks
            $ eae4letterHx = 1040
            $ eae4letterHy = 515
            $ letterHin1 = False
            $ letterHin2 = False
            $ letterHin3 = True
            $ letterHin4 = False
            $ letterHin5 = False
            $ letterHin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterHin4 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin4 = False
            if letterBin4 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin4 = False
            if letterPin4 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin4 = False
            if letterRin4 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin4 = False
            if letterGin4 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin4 = False
            if letterKin4 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin4 = False

            #sets values for the checks
            $ eae4letterHx = 1190
            $ eae4letterHy = 515
            $ letterHin1 = False
            $ letterHin2 = False
            $ letterHin3 = False
            $ letterHin4 = True
            $ letterHin5 = False
            $ letterHin6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterHin5 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin5 = False
            if letterBin5 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin5 = False
            if letterPin5 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin5 = False
            if letterRin5 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin5 = False
            if letterGin5 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin5 = False
            if letterKin5 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin5 = False

            #sets values for the checks
            $ eae4letterHx = 1340
            $ eae4letterHy = 515
            $ letterHin1 = False
            $ letterHin2 = False
            $ letterHin3 = False
            $ letterHin4 = False
            $ letterHin5 = True
            $ letterHin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterHin6 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin6 = False
            if letterBin6 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin6 = False
            if letterPin6 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin6 = False
            if letterRin6 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin6 = False
            if letterGin6 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin6 = False
            if letterKin6 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin6 = False

            #sets values for the checks
            $ eae4letterHx = 1490
            $ eae4letterHy = 515
            $ letterHin1 = False
            $ letterHin2 = False
            $ letterHin3 = False
            $ letterHin4 = False
            $ letterHin5 = False
            $ letterHin6 = True

    if gate_name == "letterB":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterHin1 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin1 = False
            if letterBin1 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin1 = False
            if letterPin1 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin1 = False
            if letterRin1 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin1 = False
            if letterGin1 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin1 = False
            if letterKin1 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin1 = False

            #sets values for checks
            $ eae4letterBx = 1115
            $ eae4letterBy = 340
            $ letterBin1 = True
            $ letterBin2 = False
            $ letterBin3 = False
            $ letterBin4 = False
            $ letterBin5 = False
            $ letterBin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterHin2 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin2 = False
            if letterBin2 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin2 = False
            if letterPin2 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin2 = False
            if letterRin2 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin2 = False
            if letterGin2 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin2 = False
            if letterKin2 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin2 = False

            #sets check values
            $ eae4letterBx = 1415
            $ eae4letterBy = 340
            $ letterBin1 = False
            $ letterBin2 = True
            $ letterBin3 = False
            $ letterBin4 = False
            $ letterBin5 = False
            $ letterBin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterHin3 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin3 = False
            if letterBin3 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin3 = False
            if letterPin3 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin3 = False
            if letterRin3 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin3 = False
            if letterGin3 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin3 = False
            if letterKin3 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin3 = False

            #sets values for the checks
            $ eae4letterBx = 1040
            $ eae4letterBy = 515
            $ letterBin1 = False
            $ letterBin2 = False
            $ letterBin3 = True
            $ letterBin4 = False
            $ letterBin5 = False
            $ letterBin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterHin4 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin4 = False
            if letterBin4 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin4 = False
            if letterPin4 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin4 = False
            if letterRin4 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin4 = False
            if letterGin4 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin4 = False
            if letterKin4 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin4 = False

            #sets values for the checks
            $ eae4letterBx = 1190
            $ eae4letterBy = 515
            $ letterBin1 = False
            $ letterBin2 = False
            $ letterBin3 = False
            $ letterBin4 = True
            $ letterBin5 = False
            $ letterBin6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterHin5 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin5 = False
            if letterBin5 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin5 = False
            if letterPin5 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin5 = False
            if letterRin5 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin5 = False
            if letterGin5 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin5 = False
            if letterKin5 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin5 = False

            #sets values for the checks
            $ eae4letterBx = 1340
            $ eae4letterBy = 515
            $ letterBin1 = False
            $ letterBin2 = False
            $ letterBin3 = False
            $ letterBin4 = False
            $ letterBin5 = True
            $ letterBin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterHin6 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin6 = False
            if letterBin6 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin6 = False
            if letterPin6 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin6 = False
            if letterRin6 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin6 = False
            if letterGin6 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin6 = False
            if letterKin6 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin6 = False

            #sets values for the checks
            $ eae4letterBx = 1490
            $ eae4letterBy = 515
            $ letterBin1 = False
            $ letterBin2 = False
            $ letterBin3 = False
            $ letterBin4 = False
            $ letterBin5 = False
            $ letterBin6 = True

    if gate_name == "letterP":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterHin1 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin1 = False
            if letterBin1 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin1 = False
            if letterPin1 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin1 = False
            if letterRin1 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin1 = False
            if letterGin1 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin1 = False
            if letterKin1 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin1 = False

            #sets values for checks
            $ eae4letterPx = 1115
            $ eae4letterPy = 340
            $ letterPin1 = True
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterHin2 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin2 = False
            if letterBin2 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin2 = False
            if letterPin2 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin2 = False
            if letterRin2 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin2 = False
            if letterGin2 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin2 = False
            if letterKin2 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin2 = False

            #sets check values
            $ eae4letterPx = 1415
            $ eae4letterPy = 340
            $ letterPin1 = False
            $ letterPin2 = True
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterHin3 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin3 = False
            if letterBin3 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin3 = False
            if letterPin3 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin3 = False
            if letterRin3 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin3 = False
            if letterGin3 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin3 = False
            if letterKin3 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin3 = False

            #sets values for the checks
            $ eae4letterPx = 1040
            $ eae4letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = True
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterHin4 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin4 = False
            if letterBin4 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin4 = False
            if letterPin4 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin4 = False
            if letterRin4 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin4 = False
            if letterGin4 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin4 = False
            if letterKin4 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin4 = False

            #sets values for the checks
            $ eae4letterPx = 1190
            $ eae4letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = True
            $ letterPin5 = False
            $ letterPin6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterHin5 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin5 = False
            if letterBin5 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin5 = False
            if letterPin5 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin5 = False
            if letterRin5 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin5 = False
            if letterGin5 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin5 = False
            if letterKin5 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin5 = False

            #sets values for the checks
            $ eae4letterPx = 1340
            $ eae4letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = True
            $ letterPin6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterHin6 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin6 = False
            if letterBin6 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin6 = False
            if letterPin6 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin6 = False
            if letterRin6 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin6 = False
            if letterGin6 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin6 = False
            if letterKin6 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin6 = False

            #sets values for the checks
            $ eae4letterPx = 1490
            $ eae4letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = True
          


    if gate_name == "letterR":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterHin1 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin1 = False
            if letterBin1 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin1 = False
            if letterPin1 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin1 = False
            if letterRin1 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin1 = False
            if letterGin1 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin1 = False
            if letterKin1 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin1 = False

            #sets values for checks
            $ eae4letterRx = 1115
            $ eae4letterRy = 340
            $ letterRin1 = True
            $ letterRin2 = False
            $ letterRin3 = False
            $ letterRin4 = False
            $ letterRin5 = False
            $ letterRin6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterHin2 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin2 = False
            if letterBin2 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin2 = False
            if letterPin2 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin2 = False
            if letterRin2 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin2 = False
            if letterGin2 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin2 = False
            if letterKin2 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin2 = False

            #sets check values
            $ eae4letterRx = 1415
            $ eae4letterRy = 340
            $ letterRin1 = False
            $ letterRin2 = True
            $ letterRin3 = False
            $ letterRin4 = False
            $ letterRin5 = False
            $ letterRin6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterHin3 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin3 = False
            if letterBin3 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin3 = False
            if letterPin3 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin3 = False
            if letterRin3 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin3 = False
            if letterGin3 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin3 = False
            if letterKin3 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin3 = False

            #sets values for the checks
            $ eae4letterRx = 1040
            $ eae4letterRy = 515
            $ letterRin1 = False
            $ letterRin2 = False
            $ letterRin3 = True
            $ letterRin4 = False
            $ letterRin5 = False
            $ letterRin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterHin4 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin4 = False
            if letterBin4 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin4 = False
            if letterPin4 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin4 = False
            if letterRin4 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin4 = False
            if letterGin4 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin4 = False
            if letterKin4 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin4 = False

            #sets values for the checks
            $ eae4letterRx = 1190
            $ eae4letterRy = 515
            $ letterRin1 = False
            $ letterRin2 = False
            $ letterRin3 = False
            $ letterRin4 = True
            $ letterRin5 = False
            $ letterRin6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterHin5 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin5 = False
            if letterBin5 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin5 = False
            if letterPin5 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin5 = False
            if letterRin5 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin5 = False
            if letterGin5 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin5 = False
            if letterKin5 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin5 = False

            #sets values for the checks
            $ eae4letterRx = 1340
            $ eae4letterRy = 515
            $ letterRin1 = False
            $ letterRin2 = False
            $ letterRin3 = False
            $ letterRin4 = False
            $ letterRin5 = True
            $ letterRin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterHin6 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin6 = False
            if letterBin6 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin6 = False
            if letterPin6 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin6 = False
            if letterRin6 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin6 = False
            if letterGin6 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin6 = False
            if letterKin6 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin6 = False

            #sets values for the checks
            $ eae4letterRx = 1490
            $ eae4letterRy = 515
            $ letterRin1 = False
            $ letterRin2 = False
            $ letterRin3 = False
            $ letterRin4 = False
            $ letterRin5 = False
            $ letterRin6 = True
           


    if gate_name == "letterG":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterHin1 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin1 = False
            if letterBin1 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin1 = False
            if letterPin1 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin1 = False
            if letterRin1 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin1 = False
            if letterGin1 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin1 = False
            if letterKin1 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin1 = False

            #sets values for checks
            $ eae4letterGx = 1115
            $ eae4letterGy = 340
            $ letterGin1 = True
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterHin2 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin2 = False
            if letterBin2 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin2 = False
            if letterPin2 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin2 = False
            if letterRin2 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin2 = False
            if letterGin2 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin2 = False
            if letterKin2 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin2 = False

            #sets check values
            $ eae4letterGx = 1415
            $ eae4letterGy = 340
            $ letterGin1 = False
            $ letterGin2 = True
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterHin3 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin3 = False
            if letterBin3 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin3 = False
            if letterPin3 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin3 = False
            if letterRin3 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin3 = False
            if letterGin3 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin3 = False
            if letterKin3 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin3 = False

            #sets values for the checks
            $ eae4letterGx = 1040
            $ eae4letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = True
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterHin4 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin4 = False
            if letterBin4 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin4 = False
            if letterPin4 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin4 = False
            if letterRin4 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin4 = False
            if letterGin4 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin4 = False
            if letterKin4 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin4 = False

            #sets values for the checks
            $ eae4letterGx = 1190
            $ eae4letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = True
            $ letterGin5 = False
            $ letterGin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterHin5 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin5 = False
            if letterBin5 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin5 = False
            if letterPin5 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin5 = False
            if letterRin5 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin5 = False
            if letterGin5 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin5 = False
            if letterKin5 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin5 = False

            #sets values for the checks
            $ eae4letterGx = 1340
            $ eae4letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = True
            $ letterGin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterHin6 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin6 = False
            if letterBin6 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin6 = False
            if letterPin6 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin6 = False
            if letterRin6 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin6 = False
            if letterGin6 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin6 = False
            if letterKin6 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin6 = False

            #sets values for the checks
            $ eae4letterGx = 1490
            $ eae4letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = True
            
  

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterHin1 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin1 = False
            if letterBin1 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin1 = False
            if letterPin1 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin1 = False
            if letterRin1 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin1 = False
            if letterGin1 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin1 = False
            if letterKin1 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin1 = False

            #sets values for checks
            $ eae4letterKx = 1115
            $ eae4letterKy = 340
            $ letterKin1 = True
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterHin2 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin2 = False
            if letterBin2 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin2 = False
            if letterPin2 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin2 = False
            if letterRin2 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin2 = False
            if letterGin2 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin2 = False
            if letterKin2 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin2 = False

            #sets check values
            $ eae4letterKx = 1415
            $ eae4letterKy = 340
            $ letterKin1 = False
            $ letterKin2 = True
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterHin3 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin3 = False
            if letterBin3 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin3 = False
            if letterPin3 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin3 = False
            if letterRin3 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin3 = False
            if letterGin3 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin3 = False
            if letterKin3 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin3 = False

            #sets values for the checks
            $ eae4letterKx = 1040
            $ eae4letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = True
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterHin4 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin4 = False
            if letterBin4 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin4 = False
            if letterPin4 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin4 = False
            if letterRin4 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin4 = False
            if letterGin4 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin4 = False
            if letterKin4 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin4 = False

            #sets values for the checks
            $ eae4letterKx = 1190
            $ eae4letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = True
            $ letterKin5 = False
            $ letterKin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterHin5 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin5 = False
            if letterBin5 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin5 = False
            if letterPin5 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin5 = False
            if letterRin5 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin5 = False
            if letterGin5 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin5 = False
            if letterKin5 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin5 = False

            #sets values for the checks
            $ eae4letterKx = 1340
            $ eae4letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = True
            $ letterKin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterHin6 == True:
               $ eae4letterHx = 275
               $ eae4letterHy = 575
               $ letterHin6 = False
            if letterBin6 == True:
               $ eae4letterBx = 410
               $ eae4letterBy = 575
               $ letterBin6 = False
            if letterPin6 == True:
               $ eae4letterPx = 342
               $ eae4letterPy = 660
               $ letterPin6 = False
            if letterRin6 == True:
               $ eae4letterRx = 275
               $ eae4letterRy = 750
               $ letterRin6 = False
            if letterGin6 == True:
               $ eae4letterGx = 410
               $ eae4letterGy = 750
               $ letterGin6 = False
            if letterKin6 == True:
               $ eae4letterKx = 342
               $ eae4letterKy = 832
               $ letterKin6 = False

            #sets values for the checks
            $ eae4letterKx = 1490
            $ eae4letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = True

    if (temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "LetterH_return" or slot_name == "LetterB_return" or slot_name == "LetterP_return" or slot_name == "LetterR_return" or slot_name == "LetterG_return" or slot_name == "LetterK_return"):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "LetterH_return":
                $ attempts +=1
                if gate_name == "letterH":
                    $ eae4letterHx = 275
                    $ eae4letterHy = 575
                    $ letterHin1 = False
                    $ letterHin2 = False
                    $ letterHin3 = False
                    $ letterHin4 = False
                    $ letterHin5 = False
                    $ letterHin6 = False
   
            if slot_name == "LetterB_return":
                $ attempts +=1
                if gate_name == "letterB":
                    $ eae4letterBx = 410
                    $ eae4letterBy = 575
                    $ letterBin1 = False
                    $ letterBin2 = False
                    $ letterBin3 = False
                    $ letterBin4 = False
                    $ letterBin5 = False
                    $ letterBin6 = False
                    
            if slot_name == "LetterP_return":
                $ attempts +=1
                if gate_name == "letterP":
                    $ eae4letterPx = 342
                    $ eae4letterPy = 660
                    $ letterPin1 = False
                    $ letterPin2 = False
                    $ letterPin3 = False
                    $ letterPin4 = False
                    $ letterPin5 = False
                    $ letterPin6 = False

            if slot_name == "LetterR_return":
                $ attempts +=1
                if gate_name == "letterR":
                    $ eae4letterRx = 275
                    $ eae4letterRy = 750
                    $ letterRin1 = False
                    $ letterRin2 = False
                    $ letterRin3 = False
                    $ letterRin4 = False
                    $ letterRin5 = False
                    $ letterRin6 = False

            if slot_name == "LetterG_return":
                $ attempts +=1
                if gate_name == "letterG":
                    $ eae4letterGx = 410
                    $ eae4letterGy = 750
                    $ letterGin1 = False
                    $ letterGin2 = False
                    $ letterGin3 = False
                    $ letterGin4 = False
                    $ letterGin5 = False
                    $ letterGin6 = False

            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ eae4letterKx = 342
                    $ eae4letterKy = 832
                    $ letterKin1 = False
                    $ letterKin2 = False
                    $ letterKin3 = False
                    $ letterKin4 = False
                    $ letterKin5 = False
                    $ letterKin6 = False
    hide eaeng_e4_tile42
    hide eaeng_e4_tile43
    hide eaeng_e4_tile44
    hide eaeng_e4_tile45
    hide eaeng_e4_tile46
    hide eaeng_e4_tile47
    hide eaeng_e4_tile48
    hide eaeng_e4_tile49
    hide eaeng_e4_tile50
    hide eaeng_e4_tile51
    hide eaeng_e4_tile52
    hide eaeng_e4_tile53
    hide eaeng_e4_tile54
    hide eaeng_e4_tile55
    hide eaeng_e4_tile60
    hide eaeng_e4_tile61
    hide eaeng_e4_tile62
    hide eaeng_e4_tile63
    hide eaeng_e4_tile64
    hide eaeng_e4_tile65
    hide eaeng_e4_tile66
    hide eaeng_e4_tile67
    hide eaeng_e4_tile68
    hide eaeng_e4_tile69
    hide eaeng_e4_tile70
    hide eaeng_e4_tile71
    hide eaeng_e4_tile72
    hide eaeng_e4_tile73
    hide eaeng_e4_tile86
    hide eaeng_e4_tile87
    hide eaeng_e4_tile88
    hide eaeng_e4_tile89
    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    if letterGin1 and letterHin2:
        image eaeng_e4_tile42 = "leftTreegreenlong.png"
        image eaeng_e4_tile43 = "1_1_green.png"
        image eaeng_e4_tile60 = "rightTreegreenlong.png"
        image eaeng_e4_tile61 = "1_1_green.png"
        if (gramRow1_C_sound_right1==0):
            play sound gramTree1
            $gramRow1_C_sound_right1 +=1
        show eaeng_e4_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e4_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e4_tile60 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e4_tile61 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

        if letterPin3 and letterKin4:
            image eaeng_e4_tile44 = "leftTreegreen.png"
            image eaeng_e4_tile45 = "1_1_green.png"
            image eaeng_e4_tile46 = "solutionLine.png"
            image eaeng_e4_tile47 = "speak.png"
            image eaeng_e4_tile50 = "rightTreegreen.png"
            image eaeng_e4_tile51 = "1_1_green.png"
            image eaeng_e4_tile52 = "solutionLine.png"
            image eaeng_e4_tile53 = "friend.png"
            if (gramRow2_L_sound_right1 ==0):
                play sound gramTree1
                queue sound gramText1
                $gramRow2_L_sound_right1 +=1
            show eaeng_e4_tile44 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile45 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e4_tile46 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e4_tile47 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e4_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e4_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e4_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)

        elif (letterBin3 or letterRin3 or letterPin3 or letterKin3) and (letterKin4 or letterBin4 or letterPin4 or letterRin4):
            image eaeng_e4_tile48 = "leftTreered.png"
            image eaeng_e4_tile49 = "1_1_red.png"
            image eaeng_e4_tile54 = "rightTreered.png"
            image eaeng_e4_tile55 = "1_1_red.png"
            if (gramRow2_L_sound_wrong1 ==0):
                play sound gramTree5
                $gramRow2_L_sound_wrong1 +=1
            show eaeng_e4_tile48 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile49 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e4_tile54 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile55 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        if (not(letterPin3 and letterKin4)):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1
        if (not((letterBin3 or letterRin3 or letterPin3 or letterKin3) and (letterKin4 or letterBin4 or letterPin4 or letterRin4))):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1
            
        if letterRin5 and letterBin6:
            image eaeng_e4_tile62 = "leftTreegreen.png"
            image eaeng_e4_tile63 = "1_1_green.png"
            image eaeng_e4_tile64 = "solutionLine.png"
            image eaeng_e4_tile65 = "and.png"
            image eaeng_e4_tile68 = "rightTreegreen.png"
            image eaeng_e4_tile69 = "1_1_green.png"
            image eaeng_e4_tile70 = "solutionLine.png"
            image eaeng_e4_tile71 = "enter.png"
            if (gramRow2_R_sound_right1==0):
                play sound gramTree1
                queue sound gramText1
                $gramRow2_R_sound_right1 +=1
            show eaeng_e4_tile62 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile63 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e4_tile64 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e4_tile65 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e4_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e4_tile70 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e4_tile71 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)

        elif(letterRin5 or letterBin5 or letterPin5 or letterKin5 == True) and (letterPin6 or letterRin6 or letterBin6 or letterKin6):
            image eaeng_e4_tile66 = "leftTreered.png"
            image eaeng_e4_tile67 = "1_1_red.png"
            image eaeng_e4_tile72 = "rightTreered.png"
            image eaeng_e4_tile73 = "1_1_red.png"
            if (gramRow2_R_sound_wrong1 ==0):
                play sound gramTree5
                $gramRow2_R_sound_wrong1 +=1
            show eaeng_e4_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e4_tile72 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e4_tile73 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            
        if (not(letterRin5 and letterBin6)):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
        if (not((letterRin5 or letterBin5 or letterPin5 or letterKin5 == True) and (letterPin6 or letterRin6 or letterBin6 or letterKin6))):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1


    elif (letterGin1 or letterBin1 or letterPin1 or letterRin1 or letterKin1 or letterHin1) and (letterBin2 or letterPin2 or letterRin2 or letterKin2 or letterHin2 or letterGin2):
         image eaeng_e4_tile86 = "leftTreeredlong.png"
         image eaeng_e4_tile87 = "1_1_red.png"
         image eaeng_e4_tile88 = "rightTreeredlong.png"
         image eaeng_e4_tile89 = "1_1_red.png"
         if (gramRow1_C_sound_wrong1==0):
             play sound gramTree5
             $gramRow1_C_sound_wrong1 +=1
         show eaeng_e4_tile86 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e4_tile87 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e4_tile88 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e4_tile89 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
         
    if (not(letterGin1 and letterHin2)):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
    
    if (not((letterGin1 or letterBin1 or letterPin1 or letterRin1 or letterKin1 or letterHin1) and (letterBin2 or letterPin2 or letterRin2 or letterKin2 or letterHin2 or letterGin2))):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1
            
            
    #win conditions
    if letterGin1 == True and letterPin3 == True and letterKin4 == True and letterHin2 == True and letterRin5 == True and letterBin6 == True: 
        image eaeng_e4_tile202 = "letterH.png"
        image eaeng_e4_tile206 = "letterB.png"
        image eaeng_e4_tile203 = "letterP.png"
        image eaeng_e4_tile205 = "letterR.png"
        image eaeng_e4_tile201 = "letterG.png"
        image eaeng_e4_tile204 = "letterK.png"
        
        show eaeng_e4_tile202 at Position(xpos = eae4letterHx, xanchor = 0, ypos = eae4letterHy, yanchor = 0)
        show eaeng_e4_tile206 at Position(xpos = eae4letterBx, xanchor = 0, ypos = eae4letterBy, yanchor = 0)
        show eaeng_e4_tile203 at Position(xpos = eae4letterPx, xanchor = 0, ypos = eae4letterPy, yanchor = 0)
        show eaeng_e4_tile205 at Position(xpos = eae4letterRx, xanchor = 0, ypos = eae4letterRy, yanchor = 0)
        show eaeng_e4_tile201 at Position(xpos = eae4letterGx, xanchor = 0, ypos = eae4letterGy, yanchor = 0)
        show eaeng_e4_tile204 at Position(xpos = eae4letterKx, xanchor = 0, ypos = eae4letterKy, yanchor = 0)
        queue sound gramWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramEasyWin
        jump gramEasyDone

    if attempts ==0:
        queue sound gramLose
        show eaeng_e4_tile202 at Position(xpos = eae4letterHx, xanchor = 0, ypos = eae4letterHy, yanchor = 0)
        show eaeng_e4_tile206 at Position(xpos = eae4letterBx, xanchor = 0, ypos = eae4letterBy, yanchor = 0)
        show eaeng_e4_tile203 at Position(xpos = eae4letterPx, xanchor = 0, ypos = eae4letterPy, yanchor = 0)
        show eaeng_e4_tile205 at Position(xpos = eae4letterRx, xanchor = 0, ypos = eae4letterRy, yanchor = 0)
        show eaeng_e4_tile201 at Position(xpos = eae4letterGx, xanchor = 0, ypos = eae4letterGy, yanchor = 0)
        show eaeng_e4_tile204 at Position(xpos = eae4letterKx, xanchor = 0, ypos = eae4letterKy, yanchor = 0)
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 4
            jump pg_gramEasyLose
        $attemptsGramEasy +=1
        jump gramEasyLose 
    
    jump gamefile_e4