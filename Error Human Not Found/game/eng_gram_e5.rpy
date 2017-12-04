
screen logicGatese5:
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
        action Jump("gramEasyHints5")
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
                xpos eae5letterKx ypos eae5letterKy
        drag:
                drag_name "letterI"
                child "letterI.png"
                droppable False
                dragged gate_dragged
                xpos eae5letterIx ypos eae5letterIy
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae5letterMx ypos eae5letterMy
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae5letterPx ypos eae5letterPy
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos eae5letterJx ypos eae5letterJy
        drag:
                drag_name "letterG"
                child "letterG.png"
                droppable False
                dragged gate_dragged
                xpos eae5letterGx ypos eae5letterGy
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

      #dragback
        
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterI_return"
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
                drag_name "LetterJ_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738
        drag:
                drag_name "LetterG_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 817 

init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_e5:
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

    #Transparent Letters for Dragbacks
    image eaeng_e5_tile300 = "letterK_grey.png"
    image eaeng_e5_tile301 = "letterI_grey.png"
    image eaeng_e5_tile302 = "letterM_grey.png"
    image eaeng_e5_tile303 = "letterP_grey.png"
    image eaeng_e5_tile304 = "letterJ_grey.png"
    image eaeng_e5_tile305 = "letterG_grey.png"
    show eaeng_e5_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e5_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e5_tile302 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_e5_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e5_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e5_tile305 at Position(xpos = 342, xanchor = 0, ypos = 832, yanchor = 0)


    # gates
    $ eae5letterKx = 275 
    $ eae5letterKy = 575
    $ eae5letterIx = 410
    $ eae5letterIy = 575
    $ eae5letterMx = 342 
    $ eae5letterMy = 660
    $ eae5letterPx = 275
    $ eae5letterPy = 750
    $ eae5letterJx = 410
    $ eae5letterJy = 750
    $ eae5letterGx = 342 
    $ eae5letterGy = 832
    
    # check conditons for locations
    $ letterKin1 = False
    $ letterKin2 = False
    $ letterKin3 = False
    $ letterKin4 = False
    $ letterKin5 = False
    $ letterKin6 = False
    $ letterKin7 = False

    $ letterIin1 = False
    $ letterIin2 = False
    $ letterIin3 = False
    $ letterIin4 = False
    $ letterIin5 = False
    $ letterIin6 = False
    $ letterIin7 = False

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

    $ letterJin1 = False
    $ letterJin2 = False
    $ letterJin3 = False
    $ letterJin4 = False
    $ letterJin5 = False
    $ letterJin6 = False
    $ letterJin7 = False


    $ letterGin1 = False
    $ letterGin2 = False
    $ letterGin3 = False
    $ letterGin4 = False
    $ letterGin5 = False
    $ letterGin6 = False
    $ letterGin7 = False


    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""


    #attempts for players
    $ attempts = 8
    
    jump gamefile_e5



label gamefile_e5:
    call screen logicGatese5

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other eaeng_e5_tile here
            if letterKin1 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin1 = False
            if letterIin1 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin1 = False
            if letterMin1 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin1 = False
            if letterJin1 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin1 = False
            if letterGin1 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin1 = False
            #sets values for checks
            $ eae5letterKx = 1115
            $ eae5letterKy = 340
            $ letterKin1 = True
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin2 = False
            if letterIin2 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin2 = False
            if letterMin2 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin2 = False
            if letterJin2 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin2 = False
            if letterGin2 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin2 = False

            #sets check values
            $ eae5letterKx = 1415
            $ eae5letterKy = 340
            $ letterKin1 = False
            $ letterKin2 = True
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin3 = False
            if letterIin3 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin3 = False
            if letterMin3 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin3 = False
            if letterJin3 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin3 = False
            if letterGin3 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin3 = False

            #sets values for the checks
            $ eae5letterKx = 1040
            $ eae5letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = True
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin4 = False
            if letterIin4 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin4 = False
            if letterMin4 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin4 = False
            if letterJin4 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin4 = False
            if letterGin4 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin4 = False

            #sets values for the checks
            $ eae5letterKx = 1190
            $ eae5letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = True
            $ letterKin5 = False
            $ letterKin6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin5 = False
            if letterIin5 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin5 = False
            if letterMin5 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin5 = False
            if letterJin5 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin5 = False
            if letterGin5 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin5 = False

            #sets values for the checks
            $ eae5letterKx = 1340
            $ eae5letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = True
            $ letterKin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin6 = False
            if letterIin6 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin6 = False
            if letterMin6 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin6 = False
            if letterJin6 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin6 = False
            if letterGin6 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin6 = False

            #sets values for the checks
            $ eae5letterKx = 1490
            $ eae5letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = True

    if gate_name == "letterI":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin1 = False
            if letterIin1 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin1 = False
            if letterMin1 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin1 = False
            if letterJin1 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin1 = False
            if letterGin1 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin1 = False

            #sets values for checks
            $ eae5letterIx = 1115
            $ eae5letterIy = 340
            $ letterIin1 = True
            $ letterIin2 = False
            $ letterIin3 = False
            $ letterIin4 = False
            $ letterIin5 = False
            $ letterIin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin2 = False
            if letterIin2 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin2 = False
            if letterMin2 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin2 = False
            if letterJin2 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin2 = False
            if letterGin2 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin2 = False

            #sets check values
            $ eae5letterIx = 1415
            $ eae5letterIy = 340
            $ letterIin1 = False
            $ letterIin2 = True
            $ letterIin3 = False
            $ letterIin4 = False
            $ letterIin5 = False
            $ letterIin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin3 = False
            if letterIin3 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin3 = False
            if letterMin3 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin3 = False
            if letterJin3 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin3 = False
            if letterGin3 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin3 = False

            #sets values for the checks
            $ eae5letterIx = 1040
            $ eae5letterIy = 515
            $ letterIin1 = False
            $ letterIin2 = False
            $ letterIin3 = True
            $ letterIin4 = False
            $ letterIin5 = False
            $ letterIin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin4 = False
            if letterIin4 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin4 = False
            if letterMin4 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin4 = False
            if letterJin4 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin4 = False
            if letterGin4 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin4 = False

            #sets values for the checks
            $ eae5letterIx = 1190
            $ eae5letterIy = 515
            $ letterIin1 = False
            $ letterIin2 = False
            $ letterIin3 = False
            $ letterIin4 = True
            $ letterIin5 = False
            $ letterIin6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin5 = False
            if letterIin5 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin5 = False
            if letterMin5 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin5 = False
            if letterJin5 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin5 = False
            if letterGin5 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin5 = False

            #sets values for the checks
            $ eae5letterIx = 1340
            $ eae5letterIy = 515
            $ letterIin1 = False
            $ letterIin2 = False
            $ letterIin3 = False
            $ letterIin4 = False
            $ letterIin5 = True
            $ letterIin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin6 = False
            if letterIin6 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin6 = False
            if letterMin6 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin6 = False
            if letterJin6 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin6 = False
            if letterGin6 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin6 = False

            #sets values for the checks
            $ eae5letterIx = 1490
            $ eae5letterIy = 515
            $ letterIin1 = False
            $ letterIin2 = False
            $ letterIin3 = False
            $ letterIin4 = False
            $ letterIin5 = False
            $ letterIin6 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin1 = False
            if letterIin1 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin1 = False
            if letterMin1 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin1 = False
            if letterJin1 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin1 = False
            if letterGin1 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin1 = False

            #sets values for checks
            $ eae5letterMx = 1115
            $ eae5letterMy = 340
            $ letterMin1 = True
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin2 = False
            if letterIin2 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin2 = False
            if letterMin2 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin2 = False
            if letterJin2 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin2 = False
            if letterGin2 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin2 = False

            #sets check values
            $ eae5letterMx = 1415
            $ eae5letterMy = 340
            $ letterMin1 = False
            $ letterMin2 = True
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin3 = False
            if letterIin3 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin3 = False
            if letterMin3 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin3 = False
            if letterJin3 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin3 = False
            if letterGin3 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin3 = False

            #sets values for the checks
            $ eae5letterMx = 1040
            $ eae5letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = True
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin4 = False
            if letterIin4 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin4 = False
            if letterMin4 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin4 = False
            if letterJin4 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin4 = False
            if letterGin4 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin4 = False

            #sets values for the checks
            $ eae5letterMx = 1190
            $ eae5letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = True
            $ letterMin5 = False
            $ letterMin6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin5 = False
            if letterIin5 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin5 = False
            if letterMin5 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin5 = False
            if letterJin5 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin5 = False
            if letterGin5 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin5 = False

            #sets values for the checks
            $ eae5letterMx = 1340
            $ eae5letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = True
            $ letterMin6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin6 = False
            if letterIin6 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin6 = False
            if letterMin6 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin6 = False
            if letterJin6 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin6 = False
            if letterGin6 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin6 = False

            #sets values for the checks
            $ eae5letterMx = 1490
            $ eae5letterMy = 515
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
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin1 = False
            if letterIin1 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin1 = False
            if letterMin1 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin1 = False
            if letterJin1 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin1 = False
            if letterGin1 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin1 = False

            #sets values for checks
            $ eae5letterPx = 1115
            $ eae5letterPy = 340
            $ letterPin1 = True
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin2 = False
            if letterIin2 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin2 = False
            if letterMin2 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin2 = False
            if letterJin2 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin2 = False
            if letterGin2 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin2 = False

            #sets check values
            $ eae5letterPx = 1415
            $ eae5letterPy = 340
            $ letterPin1 = False
            $ letterPin2 = True
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin3 = False
            if letterIin3 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin3 = False
            if letterMin3 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin3 = False
            if letterJin3 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin3 = False
            if letterGin3 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin3 = False

            #sets values for the checks
            $ eae5letterPx = 1040
            $ eae5letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = True
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin4 = False
            if letterIin4 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin4 = False
            if letterMin4 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin4 = False
            if letterJin4 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin4 = False
            if letterGin4 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin4 = False

            #sets values for the checks
            $ eae5letterPx = 1190
            $ eae5letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = True
            $ letterPin5 = False
            $ letterPin6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin5 = False
            if letterIin5 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin5 = False
            if letterMin5 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin5 = False
            if letterJin5 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin5 = False
            if letterGin5 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin5 = False

            #sets values for the checks
            $ eae5letterPx = 1340
            $ eae5letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = True
            $ letterPin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin6 = False
            if letterIin6 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin6 = False
            if letterMin6 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin6 = False
            if letterJin6 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin6 = False
            if letterGin6 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin6 = False

            #sets values for the checks
            $ eae5letterPx = 1490
            $ eae5letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = True
           


    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin1 = False
            if letterIin1 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin1 = False
            if letterMin1 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin1 = False
            if letterJin1 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin1 = False
            if letterGin1 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin1 = False

            #sets values for checks
            $ eae5letterJx = 1115
            $ eae5letterJy = 340
            $ letterJin1 = True
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin2 = False
            if letterIin2 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin2 = False
            if letterMin2 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin2 = False
            if letterJin2 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin2 = False
            if letterGin2 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin2 = False

            #sets check values
            $ eae5letterJx = 1415
            $ eae5letterJy = 340
            $ letterJin1 = False
            $ letterJin2 = True
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin3 = False
            if letterIin3 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin3 = False
            if letterMin3 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin3 = False
            if letterJin3 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin3 = False
            if letterGin3 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin3 = False

            #sets values for the checks
            $ eae5letterJx = 1040
            $ eae5letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = True
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin4 = False
            if letterIin4 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin4 = False
            if letterMin4 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin4 = False
            if letterJin4 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin4 = False
            if letterGin4 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin4 = False

            #sets values for the checks
            $ eae5letterJx = 1190
            $ eae5letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = True
            $ letterJin5 = False
            $ letterJin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin5 = False
            if letterIin5 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin5 = False
            if letterMin5 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin5 = False
            if letterJin5 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin5 = False
            if letterGin5 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin5 = False

            #sets values for the checks
            $ eae5letterJx = 1340
            $ eae5letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = True
            $ letterJin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin6 = False
            if letterIin6 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin6 = False
            if letterMin6 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin6 = False
            if letterJin6 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin6 = False
            if letterGin6 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin6 = False

            #sets values for the checks
            $ eae5letterJx = 1490
            $ eae5letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = True
            
  

    if gate_name == "letterG":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterKin1 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin1 = False
            if letterIin1 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin1 = False
            if letterMin1 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin1 = False
            if letterPin1 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin1 = False
            if letterJin1 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin1 = False
            if letterGin1 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin1 = False

            #sets values for checks
            $ eae5letterGx = 1115
            $ eae5letterGy = 340
            $ letterGin1 = True
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterKin2 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin2 = False
            if letterIin2 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin2 = False
            if letterMin2 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin2 = False
            if letterPin2 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin2 = False
            if letterJin2 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin2 = False
            if letterGin2 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin2 = False

            #sets check values
            $ eae5letterGx = 1415
            $ eae5letterGy = 340
            $ letterGin1 = False
            $ letterGin2 = True
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterKin3 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin3 = False
            if letterIin3 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin3 = False
            if letterMin3 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin3 = False
            if letterPin3 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin3 = False
            if letterJin3 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin3 = False
            if letterGin3 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin3 = False

            #sets values for the checks
            $ eae5letterGx = 1040
            $ eae5letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = True
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterKin4 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin4 = False
            if letterIin4 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin4 = False
            if letterMin4 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin4 = False
            if letterPin4 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin4 = False
            if letterJin4 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin4 = False
            if letterGin4 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin4 = False

            #sets values for the checks
            $ eae5letterGx = 1190
            $ eae5letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = True
            $ letterGin5 = False
            $ letterGin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterKin5 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin5 = False
            if letterIin5 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin5 = False
            if letterMin5 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin5 = False
            if letterPin5 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin5 = False
            if letterJin5 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin5 = False
            if letterGin5 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin5 = False

            #sets values for the checks
            $ eae5letterGx = 1340
            $ eae5letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = True
            $ letterGin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterKin6 == True:
               $ eae5letterKx = 275
               $ eae5letterKy = 575
               $ letterKin6 = False
            if letterIin6 == True:
               $ eae5letterIx = 410
               $ eae5letterIy = 575
               $ letterIin6 = False
            if letterMin6 == True:
               $ eae5letterMx = 342
               $ eae5letterMy = 660
               $ letterMin6 = False
            if letterPin6 == True:
               $ eae5letterPx = 275
               $ eae5letterPy = 750
               $ letterPin6 = False
            if letterJin6 == True:
               $ eae5letterJx = 410
               $ eae5letterJy = 750
               $ letterJin6 = False
            if letterGin6 == True:
               $ eae5letterGx = 342
               $ eae5letterGy = 832
               $ letterGin6 = False

            #sets values for the checks
            $ eae5letterGx = 1490
            $ eae5letterGy = 515
            $ letterGin1 = False
            $ letterGin2 = False
            $ letterGin3 = False
            $ letterGin4 = False
            $ letterGin5 = False
            $ letterGin6 = True

    if (temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "LetterJ_return" or slot_name == "LetterK_return" or slot_name == "LetterM_return" or slot_name == "LetterP_return" or slot_name == "LetterG_return" or slot_name == "LetterI_return"):
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
                    $ eae5letterKx = 275
                    $ eae5letterKy = 575
                    $ letterKin1 = False
                    $ letterKin2 = False
                    $ letterKin3 = False
                    $ letterKin4 = False
                    $ letterKin5 = False
                    $ letterKin6 = False
   
            if slot_name == "LetterI_return":
                $ attempts +=1
                if gate_name == "letterI":
                    $ eae5letterIx = 410
                    $ eae5letterIy = 575
                    $ letterIin1 = False
                    $ letterIin2 = False
                    $ letterIin3 = False
                    $ letterIin4 = False
                    $ letterIin5 = False
                    $ letterIin6 = False
                    
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ eae5letterMx = 342
                    $ eae5letterMy = 660
                    $ letterMin1 = False
                    $ letterMin2 = False
                    $ letterMin3 = False
                    $ letterMin4 = False
                    $ letterMin5 = False
                    $ letterMin6 = False

            if slot_name == "LetterP_return":
                $ attempts +=1
                if gate_name == "letterP":
                    $ eae5letterPx = 275
                    $ eae5letterPy = 750
                    $ letterPin1 = False
                    $ letterPin2 = False
                    $ letterPin3 = False
                    $ letterPin4 = False
                    $ letterPin5 = False
                    $ letterPin6 = False

            if slot_name == "LetterJ_return":
                $ attempts +=1
                if gate_name == "letterJ":
                    $ eae5letterJx = 410
                    $ eae5letterJy = 750
                    $ letterJin1 = False
                    $ letterJin2 = False
                    $ letterJin3 = False
                    $ letterJin4 = False
                    $ letterJin5 = False
                    $ letterJin6 = False

            if slot_name == "LetterG_return":
                $ attempts +=1
                if gate_name == "letterG":
                    $ eae5letterGx = 342
                    $ eae5letterGy = 832
                    $ letterGin1 = False
                    $ letterGin2 = False
                    $ letterGin3 = False
                    $ letterGin4 = False
                    $ letterGin5 = False
                    $ letterGin6 = False
                    
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
    hide eaeng_e5_tile78
    hide eaeng_e5_tile79
    hide eaeng_e5_tile80
    hide eaeng_e5_tile81

    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if letterJin1 and  letterKin2:
        image eaeng_e5_tile42 = "leftTreegreenlong.png"
        image eaeng_e5_tile43 = "1_1_green.png"
        image eaeng_e5_tile44 = "rightTreegreenlong.png"
        image eaeng_e5_tile45 = "1_1_green.png"
        show eaeng_e5_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e5_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        if (gramRow1_C_sound_right1 ==0):
            $gramRow1_C_sound_right1 +=1
            play sound gramTree1
        show eaeng_e5_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e5_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        
        if letterMin3 and letterGin4:
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
            if (gramRow2_L_sound_right1 ==0):
                play sound gramTree1
                queue sound gramText1
                $gramRow2_L_sound_right1 +=1
            show eaeng_e5_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)
     
        elif (letterMin3 or letterIin3 or letterPin3  or letterGin3) and (letterIin4 or letterMin4 or letterPin4 or letterGin4):
            image eaeng_e5_tile54 = "leftTreered.png"
            image eaeng_e5_tile55 = "1_1_red.png"
            image eaeng_e5_tile56 = "rightTreered.png"
            image eaeng_e5_tile57 = "1_1_red.png"
            show eaeng_e5_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            if(gramRow2_L_sound_wrong1 ==0):
                $gramRow2_L_sound_wrong1 +=1
                play sound gramTree5
        if (not(letterMin3 and letterGin4)):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1
        if (not((letterMin3 or letterIin3 or letterPin3  or letterGin3) and (letterIin4 or letterMin4 or letterPin4 or letterGin4))):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1
            
        if letterPin5 and letterIin6:
            image eaeng_e5_tile58 = "leftTreegreen.png"
            image eaeng_e5_tile59 = "1_1_green.png"
            image eaeng_e5_tile60 = "solutionLine.png"
            image eaeng_e5_tile61 = "small.png"
            image eaeng_e5_tile62 = "rightTreegreen.png"
            image eaeng_e5_tile63 = "1_1_green.png"
            image eaeng_e5_tile64 = "solutionLine.png"
            image eaeng_e5_tile65 = "world.png"
            if gramRow2_R_sound_right1==0:
                play sound gramTree1
                queue sound gramText1
                $gramRow2_R_sound_right1 +=1
            show eaeng_e5_tile58 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile59 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile60 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile61 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e5_tile62 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile63 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile64 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e5_tile65 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)

        elif (letterPin5 or letterIin5 or letterMin5 or letterGin5) and (letterPin6 or letterMin6 or letterIin6 or letterGin6):
            image eaeng_e5_tile66 = "leftTreered.png"
            image eaeng_e5_tile67 = "1_1_red.png"
            image eaeng_e5_tile68 = "rightTreered.png"
            image eaeng_e5_tile69 = "1_1_red.png"
            if (gramRow2_R_sound_wrong1 ==0):
                play sound gramTree5
                $gramRow2_R_sound_wrong1 +=1
            show eaeng_e5_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e5_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e5_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        if(not(letterPin5 and letterIin6)):
            if gramRow2_R_sound_right1==1:
                $gramRow2_R_sound_right1 -=1
        if(not(letterPin5 or letterIin5 or letterMin5 or letterGin5) and (letterPin6 or letterMin6 or letterPin6 or letterGin6)):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_right1 -=1

    
    elif (letterKin1 or letterIin1 or letterMin1 or letterPin1 or letterGin1 or letterJin1) and (letterIin2 or letterMin2 or letterPin2 or letterJin2 or letterGin2 or letterKin2):
         image eaeng_e5_tile78 = "leftTreeredlong.png"
         image eaeng_e5_tile79 = "1_1_red.png"
         image eaeng_e5_tile80 = "rightTreeredlong.png"
         image eaeng_e5_tile81 = "1_1_red.png"
         if(gramRow1_C_sound_wrong1==0):
             play sound gramTree5
             $gramRow1_C_sound_wrong1 +=1
         show eaeng_e5_tile78 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e5_tile79 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e5_tile80 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e5_tile81 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    if (not((letterKin1 or letterIin1 or letterMin1 or letterPin1 or letterGin1 or letterJin1) and (letterIin2 or letterMin2 or letterPin2 or letterJin2 or letterGin2 or letterKin2))):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1
    if (not(letterJin1 and  letterKin2)):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
    
    #win conditions
    if letterJin1 and letterMin3 and letterGin4 and letterKin2 and letterPin5 and letterIin6: 
        image eaeng_e5_tile202 = "letterK.png"
        image eaeng_e5_tile206 = "letterI.png"
        image eaeng_e5_tile203 = "letterM.png"
        image eaeng_e5_tile205 = "letterP.png"
        image eaeng_e5_tile201 = "letterJ.png"
        image eaeng_e5_tile204 = "letterG.png"
        
        show eaeng_e5_tile202 at Position(xpos = eae5letterKx, xanchor = 0, ypos = eae5letterKy, yanchor = 0)
        show eaeng_e5_tile206 at Position(xpos = eae5letterIx, xanchor = 0, ypos = eae5letterIy, yanchor = 0)
        show eaeng_e5_tile203 at Position(xpos = eae5letterMx, xanchor = 0, ypos = eae5letterMy, yanchor = 0)
        show eaeng_e5_tile205 at Position(xpos = eae5letterPx, xanchor = 0, ypos = eae5letterPy, yanchor = 0)
        show eaeng_e5_tile201 at Position(xpos = eae5letterJx, xanchor = 0, ypos = eae5letterJy, yanchor = 0)
        show eaeng_e5_tile204 at Position(xpos = eae5letterGx, xanchor = 0, ypos = eae5letterGy, yanchor = 0)
        queue sound gramWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramEasyWin
        jump gramEasyDone
 
    if attempts ==0:
        queue sound gramLose
        show eaeng_e5_tile202 at Position(xpos = eae5letterKx, xanchor = 0, ypos = eae5letterKy, yanchor = 0)
        show eaeng_e5_tile206 at Position(xpos = eae5letterIx, xanchor = 0, ypos = eae5letterIy, yanchor = 0)
        show eaeng_e5_tile203 at Position(xpos = eae5letterMx, xanchor = 0, ypos = eae5letterMy, yanchor = 0)
        show eaeng_e5_tile205 at Position(xpos = eae5letterPx, xanchor = 0, ypos = eae5letterPy, yanchor = 0)
        show eaeng_e5_tile201 at Position(xpos = eae5letterJx, xanchor = 0, ypos = eae5letterJy, yanchor = 0)
        show eaeng_e5_tile204 at Position(xpos = eae5letterGx, xanchor = 0, ypos = eae5letterGy, yanchor = 0)
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 5
            jump pg_gramEasyLose
        $attemptsGramEasy +=1
        jump gramEasyLose
          
    
    jump gamefile_e5