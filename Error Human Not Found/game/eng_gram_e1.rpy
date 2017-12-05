
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
    text "Moves" xpos 200 ypos 305 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 315 ypos 293 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 350 ypos 303 color "#0060db" font "United Kingdom DEMO.otf" size 27
    draggroup:
        #and gates
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos eae1letterJx ypos eae1letterJy
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae1letterKx ypos eae1letterKy
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae1letterMx ypos eae1letterMy
        drag:
                drag_name "letterN"
                child "letterN.png"
                droppable False
                dragged gate_dragged
                xpos eae1letterNx ypos eae1letterNy
        drag:
                drag_name "letterP"
                child "letterP.png"
                droppable False
                dragged gate_dragged
                xpos eae1letterPx ypos eae1letterPy
        drag:
                drag_name "letterL"
                child "letterL.png"
                droppable False
                dragged gate_dragged
                xpos eae1letterLx ypos eae1letterLy

        
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

   #Transparent Letters for Dragbacks
    image eaeng_e1_tile300 = "letterJ_grey.png"
    image eaeng_e1_tile301 = "letterK_grey.png"
    image eaeng_e1_tile302 = "letterM_grey.png"
    image eaeng_e1_tile303 = "letterN_grey.png"
    image eaeng_e1_tile304 = "letterP_grey.png"
    image eaeng_e1_tile305 = "letterL_grey.png"
    show eaeng_e1_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e1_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e1_tile302 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_e1_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e1_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_e1_tile305 at Position(xpos = 342, xanchor = 0, ypos = 832, yanchor = 0)


    # gates
    $ eae1letterJx = 275 
    $ eae1letterJy = 575
    $ eae1letterKx = 410
    $ eae1letterKy = 575
    $ eae1letterMx = 342 
    $ eae1letterMy = 660
    $ eae1letterNx = 275
    $ eae1letterNy = 750
    $ eae1letterPx = 410
    $ eae1letterPy = 750
    $ eae1letterLx = 342 
    $ eae1letterLy = 832
    
    # check conditons for locations
    $ letterJin1 = False
    $ letterJin2 = False
    $ letterJin3 = False
    $ letterJin4 = False
    $ letterJin5 = False
    $ letterJin6 = False
    $ letterJin7 = False

    $ letterKin1 = False
    $ letterKin2 = False
    $ letterKin3 = False
    $ letterKin4 = False
    $ letterKin5 = False
    $ letterKin6 = False
    $ letterKin7 = False

    $ letterMin1 = False
    $ letterMin2 = False
    $ letterMin3 = False
    $ letterMin4 = False
    $ letterMin5 = False
    $ letterMin6 = False
    $ letterMin7 = False

    $ letterNin1 = False
    $ letterNin2 = False
    $ letterNin3 = False
    $ letterNin4 = False
    $ letterNin5 = False
    $ letterNin6 = False
    $ letterNin7 = False

    $ letterPin1 = False
    $ letterPin2 = False
    $ letterPin3 = False
    $ letterPin4 = False
    $ letterPin5 = False
    $ letterPin6 = False
    $ letterPin7 = False


    $ letterLin1 = False
    $ letterLin2 = False
    $ letterLin3 = False
    $ letterLin4 = False
    $ letterLin5 = False
    $ letterLin6 = False
    $ letterLin7 = False



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
            if letterJin1 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin1 = False
            if letterKin1 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin1 = False
            if letterMin1 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin1 = False
            if letterNin1 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin1 = False
            if letterPin1 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin1 = False
            if letterLin1 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin1 = False
            #sets values for checks
            $ eae1letterJx = 1115
            $ eae1letterJy = 340
            $ letterJin1 = True
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterJin2 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin2 = False
            if letterKin2 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin2 = False
            if letterMin2 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin2 = False
            if letterNin2 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin2 = False
            if letterPin2 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin2 = False
            if letterLin2 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin2 = False

            #sets check values
            $ eae1letterJx = 1415
            $ eae1letterJy = 340
            $ letterJin1 = False
            $ letterJin2 = True
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterJin3 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin3 = False
            if letterKin3 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin3 = False
            if letterMin3 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin3 = False
            if letterNin3 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin3 = False
            if letterPin3 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin3 = False
            if letterLin3 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin3 = False

            #sets values for the checks
            $ eae1letterJx = 1040
            $ eae1letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = True
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterJin4 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin4 = False
            if letterKin4 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin4 = False
            if letterMin4 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin4 = False
            if letterNin4 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin4 = False
            if letterPin4 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin4 = False
            if letterLin4 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin4 = False

            #sets values for the checks
            $ eae1letterJx = 1190
            $ eae1letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = True
            $ letterJin5 = False
            $ letterJin6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterJin5 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin5 = False
            if letterKin5 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin5 = False
            if letterMin5 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin5 = False
            if letterNin5 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin5 = False
            if letterPin5 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin5 = False
            if letterLin5 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin5 = False

            #sets values for the checks
            $ eae1letterJx = 1340
            $ eae1letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = True
            $ letterJin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterJin6 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin6 = False
            if letterKin6 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin6 = False
            if letterMin6 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin6 = False
            if letterNin6 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin6 = False
            if letterPin6 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin6 = False
            if letterLin6 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin6 = False

            #sets values for the checks
            $ eae1letterJx = 1490
            $ eae1letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = True

    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterJin1 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin1 = False
            if letterKin1 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin1 = False
            if letterMin1 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin1 = False
            if letterNin1 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin1 = False
            if letterPin1 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin1 = False
            if letterLin1 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin1 = False

            #sets values for checks
            $ eae1letterKx = 1115
            $ eae1letterKy = 340
            $ letterKin1 = True
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterJin2 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin2 = False
            if letterKin2 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin2 = False
            if letterMin2 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin2 = False
            if letterNin2 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin2 = False
            if letterPin2 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin2 = False
            if letterLin2 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin2 = False

            #sets check values
            $ eae1letterKx = 1415
            $ eae1letterKy = 340
            $ letterKin1 = False
            $ letterKin2 = True
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterJin3 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin3 = False
            if letterKin3 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin3 = False
            if letterMin3 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin3 = False
            if letterNin3 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin3 = False
            if letterPin3 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin3 = False
            if letterLin3 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin3 = False

            #sets values for the checks
            $ eae1letterKx = 1040
            $ eae1letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = True
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterJin4 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin4 = False
            if letterKin4 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin4 = False
            if letterMin4 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin4 = False
            if letterNin4 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin4 = False
            if letterPin4 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin4 = False
            if letterLin4 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin4 = False

            #sets values for the checks
            $ eae1letterKx = 1190
            $ eae1letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = True
            $ letterKin5 = False
            $ letterKin6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterJin5 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin5 = False
            if letterKin5 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin5 = False
            if letterMin5 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin5 = False
            if letterNin5 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin5 = False
            if letterPin5 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin5 = False
            if letterLin5 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin5 = False

            #sets values for the checks
            $ eae1letterKx = 1340
            $ eae1letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = True
            $ letterKin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterJin6 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin6 = False
            if letterKin6 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin6 = False
            if letterMin6 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin6 = False
            if letterNin6 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin6 = False
            if letterPin6 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin6 = False
            if letterLin6 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin6 = False

            #sets values for the checks
            $ eae1letterKx = 1490
            $ eae1letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterJin1 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin1 = False
            if letterKin1 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin1 = False
            if letterMin1 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin1 = False
            if letterNin1 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin1 = False
            if letterPin1 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin1 = False
            if letterLin1 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin1 = False

            #sets values for checks
            $ eae1letterMx = 1115
            $ eae1letterMy = 340
            $ letterMin1 = True
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterJin2 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin2 = False
            if letterKin2 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin2 = False
            if letterMin2 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin2 = False
            if letterNin2 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin2 = False
            if letterPin2 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin2 = False
            if letterLin2 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin2 = False

            #sets check values
            $ eae1letterMx = 1415
            $ eae1letterMy = 340
            $ letterMin1 = False
            $ letterMin2 = True
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterJin3 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin3 = False
            if letterKin3 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin3 = False
            if letterMin3 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin3 = False
            if letterNin3 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin3 = False
            if letterPin3 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin3 = False
            if letterLin3 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin3 = False

            #sets values for the checks
            $ eae1letterMx = 1040
            $ eae1letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = True
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterJin4 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin4 = False
            if letterKin4 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin4 = False
            if letterMin4 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin4 = False
            if letterNin4 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin4 = False
            if letterPin4 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin4 = False
            if letterLin4 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin4 = False

            #sets values for the checks
            $ eae1letterMx = 1190
            $ eae1letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = True
            $ letterMin5 = False
            $ letterMin6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterJin5 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin5 = False
            if letterKin5 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin5 = False
            if letterMin5 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin5 = False
            if letterNin5 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin5 = False
            if letterPin5 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin5 = False
            if letterLin5 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin5 = False

            #sets values for the checks
            $ eae1letterMx = 1340
            $ eae1letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = True
            $ letterMin6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterJin6 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin6 = False
            if letterKin6 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin6 = False
            if letterMin6 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin6 = False
            if letterNin6 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin6 = False
            if letterPin6 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin6 = False
            if letterLin6 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin6 = False

            #sets values for the checks
            $ eae1letterMx = 1490
            $ eae1letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = True
          


    if gate_name == "letterN":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterJin1 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin1 = False
            if letterKin1 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin1 = False
            if letterMin1 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin1 = False
            if letterNin1 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin1 = False
            if letterPin1 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin1 = False
            if letterLin1 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin1 = False

            #sets values for checks
            $ eae1letterNx = 1115
            $ eae1letterNy = 340
            $ letterNin1 = True
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterJin2 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin2 = False
            if letterKin2 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin2 = False
            if letterMin2 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin2 = False
            if letterNin2 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin2 = False
            if letterPin2 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin2 = False
            if letterLin2 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin2 = False

            #sets check values
            $ eae1letterNx = 1415
            $ eae1letterNy = 340
            $ letterNin1 = False
            $ letterNin2 = True
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterJin3 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin3 = False
            if letterKin3 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin3 = False
            if letterMin3 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin3 = False
            if letterNin3 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin3 = False
            if letterPin3 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin3 = False
            if letterLin3 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin3 = False

            #sets values for the checks
            $ eae1letterNx = 1040
            $ eae1letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = True
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterJin4 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin4 = False
            if letterKin4 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin4 = False
            if letterMin4 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin4 = False
            if letterNin4 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin4 = False
            if letterPin4 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin4 = False
            if letterLin4 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin4 = False

            #sets values for the checks
            $ eae1letterNx = 1190
            $ eae1letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = True
            $ letterNin5 = False
            $ letterNin6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterJin5 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin5 = False
            if letterKin5 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin5 = False
            if letterMin5 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin5 = False
            if letterNin5 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin5 = False
            if letterPin5 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin5 = False
            if letterLin5 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin5 = False

            #sets values for the checks
            $ eae1letterNx = 1340
            $ eae1letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = True
            $ letterNin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterJin6 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin6 = False
            if letterKin6 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin6 = False
            if letterMin6 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin6 = False
            if letterNin6 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin6 = False
            if letterPin6 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin6 = False
            if letterLin6 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin6 = False

            #sets values for the checks
            $ eae1letterNx = 1490
            $ eae1letterNy = 515
            $ letterNin1 = False
            $ letterNin2 = False
            $ letterNin3 = False
            $ letterNin4 = False
            $ letterNin5 = False
            $ letterNin6 = True
           


    if gate_name == "letterP":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterJin1 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin1 = False
            if letterKin1 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin1 = False
            if letterMin1 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin1 = False
            if letterNin1 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin1 = False
            if letterPin1 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin1 = False
            if letterLin1 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin1 = False

            #sets values for checks
            $ eae1letterPx = 1115
            $ eae1letterPy = 340
            $ letterPin1 = True
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterJin2 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin2 = False
            if letterKin2 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin2 = False
            if letterMin2 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin2 = False
            if letterNin2 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin2 = False
            if letterPin2 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin2 = False
            if letterLin2 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin2 = False

            #sets check values
            $ eae1letterPx = 1415
            $ eae1letterPy = 340
            $ letterPin1 = False
            $ letterPin2 = True
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterJin3 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin3 = False
            if letterKin3 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin3 = False
            if letterMin3 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin3 = False
            if letterNin3 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin3 = False
            if letterPin3 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin3 = False
            if letterLin3 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin3 = False

            #sets values for the checks
            $ eae1letterPx = 1040
            $ eae1letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = True
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterJin4 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin4 = False
            if letterKin4 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin4 = False
            if letterMin4 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin4 = False
            if letterNin4 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin4 = False
            if letterPin4 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin4 = False
            if letterLin4 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin4 = False

            #sets values for the checks
            $ eae1letterPx = 1190
            $ eae1letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = True
            $ letterPin5 = False
            $ letterPin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterJin5 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin5 = False
            if letterKin5 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin5 = False
            if letterMin5 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin5 = False
            if letterNin5 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin5 = False
            if letterPin5 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin5 = False
            if letterLin5 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin5 = False

            #sets values for the checks
            $ eae1letterPx = 1340
            $ eae1letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = True
            $ letterPin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterJin6 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin6 = False
            if letterKin6 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin6 = False
            if letterMin6 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin6 = False
            if letterNin6 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin6 = False
            if letterPin6 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin6 = False
            if letterLin6 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin6 = False

            #sets values for the checks
            $ eae1letterPx = 1490
            $ eae1letterPy = 515
            $ letterPin1 = False
            $ letterPin2 = False
            $ letterPin3 = False
            $ letterPin4 = False
            $ letterPin5 = False
            $ letterPin6 = True
            
  

    if gate_name == "letterL":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterJin1 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin1 = False
            if letterKin1 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin1 = False
            if letterMin1 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin1 = False
            if letterNin1 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin1 = False
            if letterPin1 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin1 = False
            if letterLin1 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin1 = False

            #sets values for checks
            $ eae1letterLx = 1115
            $ eae1letterLy = 340
            $ letterLin1 = True
            $ letterLin2 = False
            $ letterLin3 = False
            $ letterLin4 = False
            $ letterLin5 = False
            $ letterLin6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterJin2 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin2 = False
            if letterKin2 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin2 = False
            if letterMin2 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin2 = False
            if letterNin2 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin2 = False
            if letterPin2 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin2 = False
            if letterLin2 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin2 = False

            #sets check values
            $ eae1letterLx = 1415
            $ eae1letterLy = 340
            $ letterLin1 = False
            $ letterLin2 = True
            $ letterLin3 = False
            $ letterLin4 = False
            $ letterLin5 = False
            $ letterLin6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterJin3 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin3 = False
            if letterKin3 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin3 = False
            if letterMin3 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin3 = False
            if letterNin3 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin3 = False
            if letterPin3 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin3 = False
            if letterLin3 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin3 = False

            #sets values for the checks
            $ eae1letterLx = 1040
            $ eae1letterLy = 515
            $ letterLin1 = False
            $ letterLin2 = False
            $ letterLin3 = True
            $ letterLin4 = False
            $ letterLin5 = False
            $ letterLin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterJin4 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin4 = False
            if letterKin4 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin4 = False
            if letterMin4 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin4 = False
            if letterNin4 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin4 = False
            if letterPin4 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin4 = False
            if letterLin4 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin4 = False

            #sets values for the checks
            $ eae1letterLx = 1190
            $ eae1letterLy = 515
            $ letterLin1 = False
            $ letterLin2 = False
            $ letterLin3 = False
            $ letterLin4 = True
            $ letterLin5 = False
            $ letterLin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterJin5 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin5 = False
            if letterKin5 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin5 = False
            if letterMin5 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin5 = False
            if letterNin5 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin5 = False
            if letterPin5 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin5 = False
            if letterLin5 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin5 = False

            #sets values for the checks
            $ eae1letterLx = 1340
            $ eae1letterLy = 515
            $ letterLin1 = False
            $ letterLin2 = False
            $ letterLin3 = False
            $ letterLin4 = False
            $ letterLin5 = True
            $ letterLin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterJin6 == True:
               $ eae1letterJx = 275
               $ eae1letterJy = 575
               $ letterJin6 = False
            if letterKin6 == True:
               $ eae1letterKx = 410
               $ eae1letterKy = 575
               $ letterKin6 = False
            if letterMin6 == True:
               $ eae1letterMx = 342
               $ eae1letterMy = 660
               $ letterMin6 = False
            if letterNin6 == True:
               $ eae1letterNx = 275
               $ eae1letterNy = 750
               $ letterNin6 = False
            if letterPin6 == True:
               $ eae1letterPx = 410
               $ eae1letterPy = 750
               $ letterPin6 = False
            if letterLin6 == True:
               $ eae1letterLx = 342
               $ eae1letterLy = 832
               $ letterLin6 = False

            #sets values for the checks
            $ eae1letterLx = 1490
            $ eae1letterLy = 515
            $ letterLin1 = False
            $ letterLin2 = False
            $ letterLin3 = False
            $ letterLin4 = False
            $ letterLin5 = False
            $ letterLin6 = True

    #Dragbacks
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "LetterJ_return" or slot_name == "LetterK_return" or slot_name == "LetterM_return" or slot_name == "LetterP_return" or slot_name == "LetterN_return" or slot_name == "LetterL_return")):
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
                    $ eae1letterJx = 275
                    $ eae1letterJy = 575
                    $ letterJin1 = False
                    $ letterJin2 = False
                    $ letterJin3 = False
                    $ letterJin4 = False
                    $ letterJin5 = False
                    $ letterJin6 = False
   
            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ eae1letterKx = 410
                    $ eae1letterKy = 575
                    $ letterKin1 = False
                    $ letterKin2 = False
                    $ letterKin3 = False
                    $ letterKin4 = False
                    $ letterKin5 = False
                    $ letterKin6 = False
                    
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ eae1letterMx = 342
                    $ eae1letterMy = 660
                    $ letterMin1 = False
                    $ letterMin2 = False
                    $ letterMin3 = False
                    $ letterMin4 = False
                    $ letterMin5 = False
                    $ letterMin6 = False

            if slot_name == "LetterN_return":
                $ attempts +=1
                if gate_name == "letterN":
                    $ eae1letterNx = 275
                    $ eae1letterNy = 750
                    $ letterNin1 = False
                    $ letterNin2 = False
                    $ letterNin3 = False
                    $ letterNin4 = False
                    $ letterNin5 = False
                    $ letterNin6 = False

            if slot_name == "LetterP_return":
                $ attempts +=1
                if gate_name == "letterP":
                    $ eae1letterPx = 410
                    $ eae1letterPy = 750
                    $ letterPin1 = False
                    $ letterPin2 = False
                    $ letterPin3 = False
                    $ letterPin4 = False
                    $ letterPin5 = False
                    $ letterPin6 = False

            if slot_name == "LetterL_return":
                $ attempts +=1
                if gate_name == "letterL":
                    $ eae1letterLx = 342
                    $ eae1letterLy = 832
                    $ letterLin1 = False
                    $ letterLin2 = False
                    $ letterLin3 = False
                    $ letterLin4 = False
                    $ letterLin5 = False
                    $ letterLin6 = False
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
    hide eaeng_e1_tile210
    hide eaeng_e1_tile211
    hide eaeng_e1_tile212
    hide eaeng_e1_tile213
    hide eaeng_e1_tile202
    hide eaeng_e1_tile203
    hide eaeng_e1_tile204
    hide eaeng_e1_tile205
    hide eaeng_e1_tile218
    hide eaeng_e1_tile219
    hide eaeng_e1_tile220
    hide eaeng_e1_tile221

    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    
    if letterPin1 and letterJin2:
        image eaeng_e1_tile182 = "leftTreegreenlong.png"
        image eaeng_e1_tile183 = "1_1_green.png"
        image eaeng_e1_tile184 = "rightTreegreenlong.png"
        image eaeng_e1_tile185 = "1_1_green.png"
        if (gramRow1_C_sound_right1 ==0):
            $gramRow1_C_sound_right1 +=1
            play sound gramTree1
        show eaeng_e1_tile182 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e1_tile183 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e1_tile184 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e1_tile185 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        
        if letterMin3 and letterLin4:
            image eaeng_e1_tile186 = "leftTreegreen.png"
            image eaeng_e1_tile187 = "1_1_green.png"
            image eaeng_e1_tile188 = "solutionLine.png"
            image eaeng_e1_tile189 = "the.png"
            image eaeng_e1_tile190 = "rightTreegreen.png"
            image eaeng_e1_tile191 = "1_1_green.png"
            image eaeng_e1_tile192 = "solutionLine.png"
            image eaeng_e1_tile193 = "password.png"
            show eaeng_e1_tile186 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile187 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile188 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile189 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e1_tile190 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile191 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile192 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile193 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)
            if gramRow2_L_sound_right1 ==0:
                play sound gramTree1
                queue sound gramText1
                $gramRow2_L_sound_right1 +=1
        elif (letterMin3 or letterNin3 or letterLin3 or letterKin3) and (letterMin4 or letterNin4 or letterLin4 or letterKin4):
            if gramRow2_L_sound_wrong1 ==0:
                play sound gramTree5
                $gramRow2_L_sound_wrong1 +=1
            image eaeng_e1_tile210 = "leftTreered.png"
            image eaeng_e1_tile211 = "1_1_red.png"
            image eaeng_e1_tile212 = "rightTreered.png"
            image eaeng_e1_tile213 = "1_1_red.png"
            show eaeng_e1_tile210 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile211 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile212 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile213 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        if not((letterMin3 or letterNin3 or letterLin3 or letterKin3) and (letterMin4 or letterNin4 or letterLin4 or letterKin4)):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1
        if not(letterMin3 and letterLin4):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1

        if letterNin5 and letterKin6:
            image eaeng_e1_tile194 = "leftTreegreen.png"
            image eaeng_e1_tile195 = "1_1_green.png"
            image eaeng_e1_tile196 = "solutionLine.png"
            image eaeng_e1_tile197 = "is.png"
            image eaeng_e1_tile198 = "rightTreegreen.png"
            image eaeng_e1_tile199 = "1_1_green.png"
            image eaeng_e1_tile200 = "solutionLine.png"
            image eaeng_e1_tile201 = "oolong.png"
            show eaeng_e1_tile194 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile195 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile196 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile197 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e1_tile198 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile199 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile200 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e1_tile201 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)
            if gramRow2_R_sound_right1 ==0:
                play sound gramTree1
                queue sound gramText1
                $gramRow2_R_sound_right1 +=1
        elif ((letterMin5 or letterNin5 or letterLin5 or letterKin5) and (letterMin6 or letterNin6 or letterLin6 or letterKin6)):
            image eaeng_e1_tile202 = "leftTreered.png"
            image eaeng_e1_tile203 = "1_1_red.png"
            image eaeng_e1_tile204 = "rightTreered.png"
            image eaeng_e1_tile205 = "1_1_red.png"
            show eaeng_e1_tile202 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile203 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e1_tile204 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e1_tile205 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            if gramRow2_R_sound_wrong1 ==0:
                play sound gramTree5
                $gramRow2_R_sound_wrong1 +=1
        if (not((letterMin5 or letterNin5 or letterLin5 or letterKin5) and (letterMin6 or letterNin6 or letterLin6 or letterKin6))):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1
        if not(letterNin5 and letterKin6):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
    
    elif (letterJin1 or letterKin1 or letterMin1 or letterNin1 or letterLin1 or letterPin1) and (letterKin2 or letterMin2 or letterNin2 or letterPin2 or letterLin2 or letterJin2):
         image eaeng_e1_tile218 = "leftTreeredlong.png"
         image eaeng_e1_tile219 = "1_1_red.png"
         image eaeng_e1_tile220 = "rightTreeredlong.png"
         image eaeng_e1_tile221 = "1_1_red.png"
         if(gramRow1_C_sound_wrong1==0):
            play sound gramTree5
            $gramRow1_C_sound_wrong1 +=1
         show eaeng_e1_tile218 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e1_tile219 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e1_tile220 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e1_tile221 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    if (not((letterJin1 or letterKin1 or letterMin1 or letterNin1 or letterLin1 or letterPin1) and (letterKin2 or letterMin2 or letterNin2 or letterPin2 or letterLin2 or letterJin2))):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1
    if (not(letterPin1 and letterJin2)):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
    #win conditions
    if letterPin1 == True and letterMin3 == True and letterLin4 == True and letterJin2 == True and letterNin5 == True and letterKin6 == True: 
        image eaeng_e1_tile226 = "letterP.png"
        image eaeng_e1_tile227 = "letterJ.png"
        image eaeng_e1_tile228 = "letterM.png"
        image eaeng_e1_tile229 = "letterL.png"
        image eaeng_e1_tile230 = "letterN.png"
        image eaeng_e1_tile231 = "letterK.png"
        show eaeng_e1_tile226 at Position(xpos = eae1letterPx, xanchor = 0, ypos = eae1letterPy, yanchor = 0)
        show eaeng_e1_tile227 at Position(xpos = eae1letterJx, xanchor = 0, ypos = eae1letterJy, yanchor = 0)
        show eaeng_e1_tile228 at Position(xpos = eae1letterMx, xanchor = 0, ypos = eae1letterMy, yanchor = 0)
        show eaeng_e1_tile229 at Position(xpos = eae1letterLx, xanchor = 0, ypos = eae1letterLy, yanchor = 0)
        show eaeng_e1_tile230 at Position(xpos = eae1letterNx, xanchor = 0, ypos = eae1letterNy, yanchor = 0)
        show eaeng_e1_tile231 at Position(xpos = eae1letterKx, xanchor = 0, ypos = eae1letterKy, yanchor = 0)
        queue sound gramWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramEasyWin
        jump gramEasyDone  
    
    if attempts==0:
        queue sound gramLose
        image eaeng_e1_tile232 = "letterP.png"
        image eaeng_e1_tile233 = "letterJ.png"
        image eaeng_e1_tile234 = "letterM.png"
        image eaeng_e1_tile235 = "letterL.png"
        image eaeng_e1_tile236 = "letterN.png"
        image eaeng_e1_tile237 = "letterK.png"
        show eaeng_e1_tile232 at Position(xpos = eae1letterPx, xanchor = 0, ypos = eae1letterPy, yanchor = 0)
        show eaeng_e1_tile233 at Position(xpos = eae1letterJx, xanchor = 0, ypos = eae1letterJy, yanchor = 0)
        show eaeng_e1_tile234 at Position(xpos = eae1letterMx, xanchor = 0, ypos = eae1letterMy, yanchor = 0)
        show eaeng_e1_tile235 at Position(xpos = eae1letterLx, xanchor = 0, ypos = eae1letterLy, yanchor = 0)
        show eaeng_e1_tile236 at Position(xpos = eae1letterNx, xanchor = 0, ypos = eae1letterNy, yanchor = 0)
        show eaeng_e1_tile237 at Position(xpos = eae1letterKx, xanchor = 0, ypos = eae1letterKy, yanchor = 0)
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_gramEasyLose
        $attemptsGramEasy +=1
        jump gramEasyLose
    
    jump gamefile_e1