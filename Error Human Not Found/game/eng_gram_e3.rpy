
screen logicGatese3:
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
        action Jump("gramEasyHints3")
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
                drag_name "letterS1"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3letterS1x ypos eae3letterS1y
        drag:
                drag_name "letterS2"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3letterS2x ypos eae3letterS2y
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos eae3letterMx ypos eae3letterMy
        drag:
                drag_name "letterS3"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos eae3letterS3x ypos eae3letterS3y
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos eae3letterKx ypos eae3letterKy
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos eae3letterJx ypos eae3letterJy
        
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
                drag_name "LetterS1_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterM_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 758
        drag:
                drag_name "LetterJ_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562

init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_e3:
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
    image eaeng_e3_tile0 = "instructions3.png"
    image eaeng_e3_tile1 = "1_1_green.png"
    image eaeng_e3_tile2 = "letterS.png"
    show eaeng_e3_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_e3_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_e3_tile2 at Position(xpos = 1265, xanchor = 0, ypos = 167, yanchor = 0)
    
    #row2 5-8

    image eaeng_e3_tile5 = "leftTreelong.png"
    image eaeng_e3_tile6 = "rightTreelong.png"

    show eaeng_e3_tile5 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_e3_tile6 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_e3_tile9 = "1_1_grey.png"
    image eaeng_e3_tile10 = "1_1_grey.png"
    

    show eaeng_e3_tile9 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_e3_tile10 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_e3_tile14 = "leftTree.png"
    image eaeng_e3_tile15 = "rightTree.png"
    image eaeng_e3_tile16 = "leftTree.png"
    image eaeng_e3_tile17 = "rightTree.png"

    show eaeng_e3_tile14 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e3_tile15 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e3_tile16 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_e3_tile17 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_e3_tile21 = "1_1_grey.png"
    image eaeng_e3_tile22 = "1_1_grey.png"
    image eaeng_e3_tile23 = "1_1_grey.png"
    image eaeng_e3_tile24 = "1_1_grey.png"

    show eaeng_e3_tile21 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e3_tile22 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e3_tile23 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_e3_tile24 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)


    image eaeng_e3_tile31 = "letterBorder.png"
    image eaeng_e3_tile32 = "letterBorder.png"
    image eaeng_e3_tile33 = "letterBorder.png"
    image eaeng_e3_tile34 = "letterBorder.png"
    show eaeng_e3_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e3_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_e3_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_e3_tile34 at Position(xpos = 330, xanchor = 0, ypos = 758, yanchor = 0)

    #Transparent Letters for Dragbacks
    image eaeng_e3_tile300 = "letterS_grey.png"
    image eaeng_e3_tile301 = "letterJ_grey.png"
    image eaeng_e3_tile302 = "letterM_grey.png"
    image eaeng_e3_tile303 = "letterK_grey.png"
    show eaeng_e3_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e3_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_e3_tile302 at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eaeng_e3_tile303 at Position(xpos = 342, xanchor = 0, ypos = 770, yanchor = 0)


    # gates
    $ eae3letterS1x = 275 
    $ eae3letterS1y = 575
    $ eae3letterS2x = 275
    $ eae3letterS2y = 575
    $ eae3letterMx = 342 
    $ eae3letterMy = 660
    $ eae3letterS3x = 275
    $ eae3letterS3y = 575
    $ eae3letterKx = 342
    $ eae3letterKy = 770
    $ eae3letterJx = 410 
    $ eae3letterJy = 575

    
    # check conditons for locations
    $ letterS1in1 = False
    $ letterS1in2 = False
    $ letterS1in3 = False
    $ letterS1in4 = False
    $ letterS1in5 = False
    $ letterS1in6 = False
    $ letterS1in7 = False

    $ letterS2in1 = False
    $ letterS2in2 = False
    $ letterS2in3 = False
    $ letterS2in4 = False
    $ letterS2in5 = False
    $ letterS2in6 = False
    $ letterS2in7 = False

    $ letterMin1 = False
    $ letterMin2 = False
    $ letterMin3 = False
    $ letterMin4 = False
    $ letterMin5 = False
    $ letterMin6 = False
    $ letterMin7 = False

    $ letterS3in1 = False
    $ letterS3in2 = False
    $ letterS3in3 = False
    $ letterS3in4 = False
    $ letterS3in5 = False
    $ letterS3in6 = False
    $ letterS3in7 = False

    $ letterKin1 = False
    $ letterKin2 = False
    $ letterKin3 = False
    $ letterKin4 = False
    $ letterKin5 = False
    $ letterKin6 = False
    $ letterKin7 = False


    $ letterJin1 = False
    $ letterJin2 = False
    $ letterJin3 = False
    $ letterJin4 = False
    $ letterJin5 = False
    $ letterJin6 = False
    $ letterJin7 = False



    #attempts for players
    $ attempts = 8
    
    jump gamefile_e3



label gamefile_e3:
    #image moon = "images/blankeaeng_e3_tile.png"
    #show blink
    #calls jigsaw game with the images selected
    call screen logicGatese3

    if gate_name == "letterS1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other eaeng_e3_tile here
            if letterS1in1 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in1 = False
            if letterS2in1 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in1 = False
            if letterMin1 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin1 = False
            if letterS3in1 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in1 = False
            if letterKin1 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin1 = False
            if letterJin1 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin1 = False
            #sets values for checks
            $ eae3letterS1x = 1115
            $ eae3letterS1y = 340
            $ letterS1in1 = True
            $ letterS1in2 = False
            $ letterS1in3 = False
            $ letterS1in4 = False
            $ letterS1in5 = False
            $ letterS1in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterS1in2 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in2 = False
            if letterS2in2 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in2 = False
            if letterMin2 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin2 = False
            if letterS3in2 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in2 = False
            if letterKin2 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin2 = False
            if letterJin2 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin2 = False

            #sets check values
            $ eae3letterS1x = 1415
            $ eae3letterS1y = 340
            $ letterS1in1 = False
            $ letterS1in2 = True
            $ letterS1in3 = False
            $ letterS1in4 = False
            $ letterS1in5 = False
            $ letterS1in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterS1in3 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in3 = False
            if letterS2in3 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in3 = False
            if letterMin3 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin3 = False
            if letterS3in3 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in3 = False
            if letterKin3 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin3 = False
            if letterJin3 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin3 = False

            #sets values for the checks
            $ eae3letterS1x = 1040
            $ eae3letterS1y = 515
            $ letterS1in1 = False
            $ letterS1in2 = False
            $ letterS1in3 = True
            $ letterS1in4 = False
            $ letterS1in5 = False
            $ letterS1in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterS1in4 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in4 = False
            if letterS2in4 == True:
               $ eae3letterS2x = 275 
               $ eae3letterS2y = 575
               $ letterS2in4 = False
            if letterMin4 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin4 = False
            if letterS3in4 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in4 = False
            if letterKin4 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin4 = False
            if letterJin4 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin4 = False

            #sets values for the checks
            $ eae3letterS1x = 1190
            $ eae3letterS1y = 515
            $ letterS1in1 = False
            $ letterS1in2 = False
            $ letterS1in3 = False
            $ letterS1in4 = True
            $ letterS1in5 = False
            $ letterS1in6 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterS1in5 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in5 = False
            if letterS2in5 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in5 = False
            if letterMin5 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin5 = False
            if letterS3in5 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in5 = False
            if letterKin5 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin5 = False
            if letterJin5 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin5 = False

            #sets values for the checks
            $ eae3letterS1x = 1340
            $ eae3letterS1y = 515
            $ letterS1in1 = False
            $ letterS1in2 = False
            $ letterS1in3 = False
            $ letterS1in4 = False
            $ letterS1in5 = True
            $ letterS1in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterS1in6 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in6 = False
            if letterS2in6 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in6 = False
            if letterMin6 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin6 = False
            if letterS3in6 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in6 = False
            if letterKin6 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin6 = False
            if letterJin6 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin6 = False

            #sets values for the checks
            $ eae3letterS1x = 1490
            $ eae3letterS1y = 515
            $ letterS1in1 = False
            $ letterS1in2 = False
            $ letterS1in3 = False
            $ letterS1in4 = False
            $ letterS1in5 = False
            $ letterS1in6 = True

    if gate_name == "letterS2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterS1in1 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in1 = False
            if letterS2in1 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in1 = False
            if letterMin1 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin1 = False
            if letterS3in1 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in1 = False
            if letterKin1 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin1 = False
            if letterJin1 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin1 = False

            #sets values for checks
            $ eae3letterS2x = 1115
            $ eae3letterS2y = 340
            $ letterS2in1 = True
            $ letterS2in2 = False
            $ letterS2in3 = False
            $ letterS2in4 = False
            $ letterS2in5 = False
            $ letterS2in6 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterS1in2 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in2 = False
            if letterS2in2 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in2 = False
            if letterMin2 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin2 = False
            if letterS3in2 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in2 = False
            if letterKin2 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin2 = False
            if letterJin2 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin2 = False

            #sets check values
            $ eae3letterS2x = 1415
            $ eae3letterS2y = 340
            $ letterS2in1 = False
            $ letterS2in2 = True
            $ letterS2in3 = False
            $ letterS2in4 = False
            $ letterS2in5 = False
            $ letterS2in6 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterS1in3 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in3 = False
            if letterS2in3 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in3 = False
            if letterMin3 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin3 = False
            if letterS3in3 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in3 = False
            if letterKin3 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin3 = False
            if letterJin3 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin3 = False

            #sets values for the checks
            $ eae3letterS2x = 1040
            $ eae3letterS2y = 515
            $ letterS2in1 = False
            $ letterS2in2 = False
            $ letterS2in3 = True
            $ letterS2in4 = False
            $ letterS2in5 = False
            $ letterS2in6 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterS1in4 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in4 = False
            if letterS2in4 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in4 = False
            if letterMin4 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin4 = False
            if letterS3in4 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in4 = False
            if letterKin4 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin4 = False
            if letterJin4 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin4 = False

            #sets values for the checks
            $ eae3letterS2x = 1190
            $ eae3letterS2y = 515
            $ letterS2in1 = False
            $ letterS2in2 = False
            $ letterS2in3 = False
            $ letterS2in4 = True
            $ letterS2in5 = False
            $ letterS2in6 = False


                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterS1in5 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in5 = False
            if letterS2in5 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in5 = False
            if letterMin5 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin5 = False
            if letterS3in5 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in5 = False
            if letterKin5 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin5 = False
            if letterJin5 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin5 = False

            #sets values for the checks
            $ eae3letterS2x = 1340
            $ eae3letterS2y = 515
            $ letterS2in1 = False
            $ letterS2in2 = False
            $ letterS2in3 = False
            $ letterS2in4 = False
            $ letterS2in5 = True
            $ letterS2in6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterS1in6 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in6 = False
            if letterS2in6 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in6 = False
            if letterMin6 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin6 = False
            if letterS3in6 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in6 = False
            if letterKin6 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin6 = False
            if letterJin6 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin6 = False

            #sets values for the checks
            $ eae3letterS2x = 1490
            $ eae3letterS2y = 515
            $ letterS2in1 = False
            $ letterS2in2 = False
            $ letterS2in3 = False
            $ letterS2in4 = False
            $ letterS2in5 = False
            $ letterS2in6 = True

    if gate_name == "letterM":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterS1in1 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in1 = False
            if letterS2in1 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in1 = False
            if letterMin1 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin1 = False
            if letterS3in1 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in1 = False
            if letterKin1 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin1 = False
            if letterJin1 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin1 = False

            #sets values for checks
            $ eae3letterMx = 1115
            $ eae3letterMy = 340
            $ letterMin1 = True
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
 

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterS1in2 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in2 = False
            if letterS2in2 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in2 = False
            if letterMin2 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin2 = False
            if letterS3in2 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in2 = False
            if letterKin2 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin2 = False
            if letterJin2 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin2 = False

            #sets check values
            $ eae3letterMx = 1415
            $ eae3letterMy = 340
            $ letterMin1 = False
            $ letterMin2 = True
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterS1in3 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in3 = False
            if letterS2in3 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in3 = False
            if letterMin3 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin3 = False
            if letterS3in3 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in3 = False
            if letterKin3 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin3 = False
            if letterJin3 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin3 = False

            #sets values for the checks
            $ eae3letterMx = 1040
            $ eae3letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = True
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = False
        

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterS1in4 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in4 = False
            if letterS2in4 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in4 = False
            if letterMin4 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin4 = False
            if letterS3in4 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in4 = False
            if letterKin4 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin4 = False
            if letterJin4 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin4 = False

            #sets values for the checks
            $ eae3letterMx = 1190
            $ eae3letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = True
            $ letterMin5 = False
            $ letterMin6 = False
       

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterS1in5 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in5 = False
            if letterS2in5 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in5 = False
            if letterMin5 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin5 = False
            if letterS3in5 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in5 = False
            if letterKin5 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin5 = False
            if letterJin5 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin5 = False

            #sets values for the checks
            $ eae3letterMx = 1340
            $ eae3letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = True
            $ letterMin6 = False
        

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterS1in6 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in6 = False
            if letterS2in6 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in6 = False
            if letterMin6 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin6 = False
            if letterS3in6 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in6 = False
            if letterKin6 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin6 = False
            if letterJin6 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin6 = False

            #sets values for the checks
            $ eae3letterMx = 1490
            $ eae3letterMy = 515
            $ letterMin1 = False
            $ letterMin2 = False
            $ letterMin3 = False
            $ letterMin4 = False
            $ letterMin5 = False
            $ letterMin6 = True
          


    if gate_name == "letterS3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterS1in1 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in1 = False
            if letterS2in1 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in1 = False
            if letterMin1 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin1 = False
            if letterS3in1 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in1 = False
            if letterKin1 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin1 = False
            if letterJin1 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin1 = False

            #sets values for checks
            $ eae3letterS3x = 1115
            $ eae3letterS3y = 340
            $ letterS3in1 = True
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
         

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterS1in2 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in2 = False
            if letterS2in2 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in2 = False
            if letterMin2 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin2 = False
            if letterS3in2 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in2 = False
            if letterKin2 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770 
               $ letterKin2 = False
            if letterJin2 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin2 = False

            #sets check values
            $ eae3letterS3x = 1415
            $ eae3letterS3y = 340
            $ letterS3in1 = False
            $ letterS3in2 = True
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
          
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterS1in3 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in3 = False
            if letterS2in3 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in3 = False
            if letterMin3 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin3 = False
            if letterS3in3 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in3 = False
            if letterKin3 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin3 = False
            if letterJin3 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin3 = False

            #sets values for the checks
            $ eae3letterS3x = 1040
            $ eae3letterS3y = 515
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = True
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterS1in4 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in4 = False
            if letterS2in4 == True:
               $ eae3letterS2x = 275 
               $ eae3letterS2y = 575 
               $ letterS2in4 = False
            if letterMin4 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin4 = False
            if letterS3in4 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in4 = False
            if letterKin4 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin4 = False
            if letterJin4 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin4 = False

            #sets values for the checks
            $ eae3letterS3x = 1190
            $ eae3letterS3y = 515
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = True
            $ letterS3in5 = False
            $ letterS3in6 = False
           

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterS1in5 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in5 = False
            if letterS2in5 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in5 = False
            if letterMin5 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin5 = False
            if letterS3in5 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in5 = False
            if letterKin5 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin5 = False
            if letterJin5 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin5 = False

            #sets values for the checks
            $ eae3letterS3x = 1340
            $ eae3letterS3y = 515
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = True
            $ letterS3in6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterS1in6 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in6 = False
            if letterS2in6 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in6 = False
            if letterMin6 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin6 = False
            if letterS3in6 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in6 = False
            if letterKin6 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin6 = False
            if letterJin6 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin6 = False

            #sets values for the checks
            $ eae3letterS3x = 1490
            $ eae3letterS3y = 515
            $ letterS3in1 = False
            $ letterS3in2 = False
            $ letterS3in3 = False
            $ letterS3in4 = False
            $ letterS3in5 = False
            $ letterS3in6 = True
           


    if gate_name == "letterK":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterS1in1 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in1 = False
            if letterS2in1 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in1 = False
            if letterMin1 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin1 = False
            if letterS3in1 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in1 = False
            if letterKin1 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin1 = False
            if letterJin1 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin1 = False

            #sets values for checks
            $ eae3letterKx = 1115
            $ eae3letterKy = 340
            $ letterKin1 = True
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
           

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterS1in2 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in2 = False
            if letterS2in2 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in2 = False
            if letterMin2 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin2 = False
            if letterS3in2 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in2 = False
            if letterKin2 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin2 = False
            if letterJin2 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin2 = False

            #sets check values
            $ eae3letterKx = 1415
            $ eae3letterKy = 340
            $ letterKin1 = False
            $ letterKin2 = True
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
         
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterS1in3 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in3 = False
            if letterS2in3 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in3 = False
            if letterMin3 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin3 = False
            if letterS3in3 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in3 = False
            if letterKin3 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin3 = False
            if letterJin3 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin3 = False

            #sets values for the checks
            $ eae3letterKx = 1040
            $ eae3letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = True
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = False
           

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterS1in4 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in4 = False
            if letterS2in4 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in4 = False
            if letterMin4 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin4 = False
            if letterS3in4 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in4 = False
            if letterKin4 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin4 = False
            if letterJin4 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin4 = False

            #sets values for the checks
            $ eae3letterKx = 1190
            $ eae3letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = True
            $ letterKin5 = False
            $ letterKin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterS1in5 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in5 = False
            if letterS2in5 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in5 = False
            if letterMin5 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin5 = False
            if letterS3in5 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in5 = False
            if letterKin5 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin5 = False
            if letterJin5 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin5 = False

            #sets values for the checks
            $ eae3letterKx = 1340
            $ eae3letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = True
            $ letterKin6 = False
            

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterS1in6 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in6 = False
            if letterS2in6 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in6 = False
            if letterMin6 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin6 = False
            if letterS3in6 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in6 = False
            if letterKin6 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin6 = False
            if letterJin6 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin6 = False

            #sets values for the checks
            $ eae3letterKx = 1490
            $ eae3letterKy = 515
            $ letterKin1 = False
            $ letterKin2 = False
            $ letterKin3 = False
            $ letterKin4 = False
            $ letterKin5 = False
            $ letterKin6 = True
            
  

    if gate_name == "letterJ":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if letterS1in1 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in1 = False
            if letterS2in1 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in1 = False
            if letterMin1 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin1 = False
            if letterS3in1 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in1 = False
            if letterKin1 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin1 = False
            if letterJin1 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin1 = False

            #sets values for checks
            $ eae3letterJx = 1115
            $ eae3letterJy = 340
            $ letterJin1 = True
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
            

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterS1in2 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in2 = False
            if letterS2in2 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in2 = False
            if letterMin2 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin2 = False
            if letterS3in2 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in2 = False
            if letterKin2 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin2 = False
            if letterJin2 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin2 = False

            #sets check values
            $ eae3letterJx = 1415
            $ eae3letterJy = 340
            $ letterJin1 = False
            $ letterJin2 = True
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
            
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterS1in3 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in3 = False
            if letterS2in3 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in3 = False
            if letterMin3 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin3 = False
            if letterS3in3 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in3 = False
            if letterKin3 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin3 = False
            if letterJin3 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin3 = False

            #sets values for the checks
            $ eae3letterJx = 1040
            $ eae3letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = True
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = False
            

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterS1in4 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in4 = False
            if letterS2in4 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in4 = False
            if letterMin4 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin4 = False
            if letterS3in4 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in4 = False
            if letterKin4 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin4 = False
            if letterJin4 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin4 = False

            #sets values for the checks
            $ eae3letterJx = 1190
            $ eae3letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = True
            $ letterJin5 = False
            $ letterJin6 = False
            

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterS1in5 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in5 = False
            if letterS2in5 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in5 = False
            if letterMin5 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin5 = False
            if letterS3in5 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in5 = False
            if letterKin5 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin5 = False
            if letterJin5 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin5 = False

            #sets values for the checks
            $ eae3letterJx = 1340
            $ eae3letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = True
            $ letterJin6 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterS1in6 == True:
               $ eae3letterS1x = 275
               $ eae3letterS1y = 575
               $ letterS1in6 = False
            if letterS2in6 == True:
               $ eae3letterS2x = 275
               $ eae3letterS2y = 575
               $ letterS2in6 = False
            if letterMin6 == True:
               $ eae3letterMx = 342
               $ eae3letterMy = 660
               $ letterMin6 = False
            if letterS3in6 == True:
               $ eae3letterS3x = 275
               $ eae3letterS3y = 575
               $ letterS3in6 = False
            if letterKin6 == True:
               $ eae3letterKx = 342
               $ eae3letterKy = 770
               $ letterKin6 = False
            if letterJin6 == True:
               $ eae3letterJx = 410
               $ eae3letterJy = 575
               $ letterJin6 = False

            #sets values for the checks
            $ eae3letterJx = 1490
            $ eae3letterJy = 515
            $ letterJin1 = False
            $ letterJin2 = False
            $ letterJin3 = False
            $ letterJin4 = False
            $ letterJin5 = False
            $ letterJin6 = True

    if (temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "LetterJ_return" or slot_name == "LetterK_return" or slot_name == "LetterM_return" or slot_name == "LetterS1_return"):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "LetterS1_return":
                $ attempts +=1
                if gate_name == "letterS1":
                    $ eae3letterS1x = 275
                    $ eae3letterS1y = 575
                    $ letterS1in1 = False
                    $ letterS1in2 = False
                    $ letterS1in3 = False
                    $ letterS1in4 = False
                    $ letterS1in5 = False
                    $ letterS1in6 = False
                
                elif gate_name == "letterS2":
                    $ eae3letterS2x = 275
                    $ eae3letterS2y = 575
                    $ letterS2in1 = False
                    $ letterS2in2 = False
                    $ letterS2in3 = False
                    $ letterS2in4 = False
                    $ letterS2in5 = False
                    $ letterS2in6 = False
                
                elif gate_name == "letterS3":
                    $ eae3letterS3x = 275
                    $ eae3letterS3y = 575
                    $ letterS3in1 = False
                    $ letterS3in2 = False
                    $ letterS3in3 = False
                    $ letterS3in4 = False
                    $ letterS3in5 = False
                    $ letterS3in6 = False
                    
            if slot_name == "LetterM_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ eae3letterMx = 342
                    $ eae3letterMy = 660
                    $ letterMin1 = False
                    $ letterMin2 = False
                    $ letterMin3 = False
                    $ letterMin4 = False
                    $ letterMin5 = False
                    $ letterMin6 = False

            if slot_name == "LetterK_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ eae3letterKx = 342
                    $ eae3letterKy = 770
                    $ letterKin1 = False
                    $ letterKin2 = False
                    $ letterKin3 = False
                    $ letterKin4 = False
                    $ letterKin5 = False
                    $ letterKin6 = False

            if slot_name == "LetterJ_return":
                $ attempts +=1
                if gate_name == "letterJ":
                    $ eae3letterJx = 410
                    $ eae3letterJy = 575
                    $ letterJin1 = False
                    $ letterJin2 = False
                    $ letterJin3 = False
                    $ letterJin4 = False
                    $ letterJin5 = False
                    $ letterJin6 = False
                    
    hide eaeng_e3_tile42
    hide eaeng_e3_tile43
    hide eaeng_e3_tile44
    hide eaeng_e3_tile45
    hide eaeng_e3_tile46
    hide eaeng_e3_tile47
    hide eaeng_e3_tile48
    hide eaeng_e3_tile49
    hide eaeng_e3_tile50
    hide eaeng_e3_tile51
    hide eaeng_e3_tile52
    hide eaeng_e3_tile53
    hide eaeng_e3_tile54
    hide eaeng_e3_tile55
    hide eaeng_e3_tile56
    hide eaeng_e3_tile57
    hide eaeng_e3_tile58
    hide eaeng_e3_tile59
    hide eaeng_e3_tile60
    hide eaeng_e3_tile61
    hide eaeng_e3_tile62
    hide eaeng_e3_tile63
    hide eaeng_e3_tile64
    hide eaeng_e3_tile65
    hide eaeng_e3_tile66
    hide eaeng_e3_tile67
    hide eaeng_e3_tile68
    hide eaeng_e3_tile69
    hide eaeng_e3_tile74
    hide eaeng_e3_tile75
    hide eaeng_e3_tile76
    hide eaeng_e3_tile77
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if (letterS1in1 or letterS2in1 or letterS3in1) and (letterKin2):
        image eaeng_e3_tile42 = "leftTreegreenlong.png"
        image eaeng_e3_tile43 = "1_1_green.png"
        image eaeng_e3_tile44 = "rightTreegreenlong.png"
        image eaeng_e3_tile45 = "1_1_green.png"
        if (gramRow1_C_sound_right1 ==0):
            play sound gramTree1
            $ gramRow1_C_sound_right1 +=1
        show eaeng_e3_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e3_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e3_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e3_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)

        if letterMin3 and letterJin4: 
            image eaeng_e3_tile46 = "leftTreegreen.png"
            image eaeng_e3_tile47 = "1_1_green.png"
            image eaeng_e3_tile48 = "solutionLine.png"
            image eaeng_e3_tile49 = "big.png"
            image eaeng_e3_tile50 = "rightTreegreen.png"
            image eaeng_e3_tile51 = "1_1_green.png"
            image eaeng_e3_tile52 = "solutionLine.png"
            image eaeng_e3_tile53 = "sister.png"
            if (gramRow2_L_sound_right1==0):
                play sound gramTree1
                queue sound gramText1
                $gramRow2_L_sound_right1 +=1
            show eaeng_e3_tile46 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile47 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile48 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile49 at Position(xpos = 990, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e3_tile50 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile51 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile52 at Position(xpos = 1175, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile53 at Position(xpos = 1145, xanchor = 0, ypos = 700, yanchor = 0)


        elif (letterS1in3 or letterS2in3 or letterS3in3 or letterKin3 or letterJin3 or letterMin3) and (letterS1in4 or letterS2in4 or letterMin4 or letterS3in4 or letterKin4 or letterJin4):
            image eaeng_e3_tile54 = "leftTreered.png"
            image eaeng_e3_tile55 = "1_1_red.png"
            image eaeng_e3_tile56 = "rightTreered.png"
            image eaeng_e3_tile57 = "1_1_red.png"
            if (gramRow2_L_sound_wrong1 ==0):
                play sound gramTree5
                $gramRow2_L_sound_wrong1 +=1
            show eaeng_e3_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
        if not(letterMin3 and letterJin4):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1
        if not((letterS1in3 or letterS2in3 or letterS3in3 or letterKin3 or letterJin3 or letterMin3) and (letterS1in4 or letterS2in4 or letterMin4 or letterS3in4 or letterKin4 or letterJin4)):
            if gramRow2_L_sound_wrong1 ==1:
                $gramRow2_L_sound_wrong1 -=1

        if (letterS3in5 or letterS1in5 or letterS2in5) and (letterS1in6 or letterS2in6 or letterS3in6):
            image eaeng_e3_tile58 = "leftTreegreen.png"
            image eaeng_e3_tile59 = "1_1_green.png"
            image eaeng_e3_tile60 = "solutionLine.png"
            image eaeng_e3_tile61 = "is.png"
            image eaeng_e3_tile62 = "rightTreegreen.png"
            image eaeng_e3_tile63 = "1_1_green.png"
            image eaeng_e3_tile64 = "solutionLine.png"
            image eaeng_e3_tile65 = "watching.png"
            if (gramRow2_R_sound_right1 ==0):
                play sound gramTree1
                queue sound gramText1
                $gramRow2_R_sound_right1 +=1
            show eaeng_e3_tile58 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile59 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile60 at Position(xpos = 1325, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile61 at Position(xpos = 1298, xanchor = 0, ypos = 700, yanchor = 0)
            show eaeng_e3_tile62 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile63 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile64 at Position(xpos = 1475, xanchor = 0, ypos = 600, yanchor = 0)
            show eaeng_e3_tile65 at Position(xpos = 1450, xanchor = 0, ypos = 700, yanchor = 0)

        elif(letterMin5 or letterS1in5 or letterS2in5 or letterS3in5 or letterJin5 or letterKin5) and (letterJin6 or letterMin6 or letterS1in6 or letterS2in6 or letterS3in6 or letterKin6):
            image eaeng_e3_tile66 = "leftTreered.png"
            image eaeng_e3_tile67 = "1_1_red.png"
            image eaeng_e3_tile68 = "rightTreered.png"
            image eaeng_e3_tile69 = "1_1_red.png"
            if (gramRow2_R_sound_wrong1==0):
                play sound gramTree5
                $gramRow2_R_sound_wrong1 +=1
            show eaeng_e3_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
        if not((letterS3in5 or letterS1in5 or letterS2in5) and (letterS1in6 or letterS2in6 or letterS3in6)):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
        if not((letterMin5 or letterS1in5 or letterS2in5 or letterS3in5 or letterJin5 or letterKin5) and (letterJin6 or letterMin6 or letterS1in6 or letterS2in6 or letterS3in6 or letterKin6)):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1

    elif letterMin1 and letterJin2:
        show eaeng_e3_tile42 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e3_tile43 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
        show eaeng_e3_tile44 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
        show eaeng_e3_tile45 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
        if (gramRow1_C_sound_right2 ==0):
            play sound gramTree1
            $gramRow1_C_sound_right2 +=1
        
        if (letterS1in3 or letterS2in3 or letterS3in3 or letterKin3) and (letterS1in4 or letterS2in4 or letterS3in4 or letterKin4):
            show eaeng_e3_tile54 at Position(xpos = 1070, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile55 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile56 at Position(xpos = 1170, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile57 at Position(xpos = 1175, xanchor = 0, ypos = 500, yanchor = 0)
            if (gramRow2_L_sound_wrong2 ==0):
                play sound gramTree5
                $gramRow2_L_sound_wrong2 +=1
        if not((letterS1in3 or letterS2in3 or letterS3in3 or letterKin3) and (letterS1in4 or letterS2in4 or letterS3in4 or letterKin4)):
            if gramRow2_L_sound_wrong2 ==1:
                $gramRow2_L_sound_wrong2 -=1
                
        if (letterS1in5 or letterS2in5 or letterS3in5 or letterKin5) and (letterS1in6 or letterS2in6 or letterS3in6 or letterKin6):
            show eaeng_e3_tile66 at Position(xpos = 1370, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile67 at Position(xpos = 1325, xanchor = 0, ypos = 500, yanchor = 0)
            show eaeng_e3_tile68 at Position(xpos = 1470, xanchor = 0, ypos = 425, yanchor = 0)
            show eaeng_e3_tile69 at Position(xpos = 1475, xanchor = 0, ypos = 500, yanchor = 0)
            if (gramRow2_R_sound_wrong2==0):
                play sound gramTree5
                $gramRow2_R_sound_wrong2 +=1
        if not((letterS1in5 or letterS2in5 or letterS3in5 or letterKin5) and (letterS1in6 or letterS2in6 or letterS3in6 or letterKin6)):
            if gramRow2_R_sound_wrong2==1:
                $gramRow2_R_sound_wrong2 -=1

    elif (letterJin1 or letterKin1 or letterS1in1 or letterS2in1 or letterS3in1 or letterMin1) and (letterMin2 or letterS1in2 or letterS2in2 or letterS3in2 or letterJin2 or letterKin2):
         image eaeng_e3_tile74 = "leftTreeredlong.png"
         image eaeng_e3_tile75 = "1_1_red.png"
         image eaeng_e3_tile76 = "rightTreeredlong.png"
         image eaeng_e3_tile77 = "1_1_red.png"
         if (gramRow1_C_sound_wrong1 ==0):
             play sound gramTree5
             $gramRow1_C_sound_wrong1 +=1
         show eaeng_e3_tile74 at Position(xpos = 1140, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e3_tile75 at Position(xpos = 1100, xanchor = 0, ypos = 325, yanchor = 0)
         show eaeng_e3_tile76 at Position(xpos = 1310, xanchor = 0, ypos = 250, yanchor = 0)
         show eaeng_e3_tile77 at Position(xpos = 1400, xanchor = 0, ypos = 325, yanchor = 0)
    if not((letterS1in1 or letterS2in1 or letterS3in1) and (letterKin2)):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
    if not(letterMin1 and letterJin2):
        if gramRow1_C_sound_right2 ==1:
            $gramRow1_C_sound_right2 -=1
    if not((letterJin1 or letterKin1 or letterS1in1 or letterS2in1 or letterS3in1 or letterMin1) and (letterMin2 or letterS1in2 or letterS2in2 or letterS3in2 or letterJin2 or letterKin2)):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1
    #win conditions
    if (letterKin1 == True or letterS1in1 == True or letterS2in1 == True or letterS3in1 == True) and letterMin3 == True and letterJin4 == True and (letterS1in2 == True or letterS2in2 == True or letterS3in2 == True or letterKin2 == True) and (letterS3in5 == True or letterS1in5 == True or letterS2in5 == True or letterKin5 == True) and (letterS1in6 == True or letterS2in6 == True or letterS3in6 == True or letterKin6 == True):

        image eaeng_e3_tile202 = "letterS.png"
        image eaeng_e3_tile206 = "letterS.png"
        image eaeng_e3_tile203 = "letterM.png"
        image eaeng_e3_tile205 = "letterS.png"
        image eaeng_e3_tile201 = "letterK.png"
        image eaeng_e3_tile204 = "letterJ.png"
        
        show eaeng_e3_tile202 at Position(xpos = eae3letterS1x, xanchor = 0, ypos = eae3letterS1y, yanchor = 0)
        show eaeng_e3_tile206 at Position(xpos = eae3letterS2x, xanchor = 0, ypos = eae3letterS2y, yanchor = 0)
        show eaeng_e3_tile203 at Position(xpos = eae3letterMx, xanchor = 0, ypos = eae3letterMy, yanchor = 0)
        show eaeng_e3_tile205 at Position(xpos = eae3letterS3x, xanchor = 0, ypos = eae3letterS3y, yanchor = 0)
        show eaeng_e3_tile201 at Position(xpos = eae3letterKx, xanchor = 0, ypos = eae3letterKy, yanchor = 0)
        show eaeng_e3_tile204 at Position(xpos = eae3letterJx, xanchor = 0, ypos = eae3letterJy, yanchor = 0)
        queue sound gramWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramEasyWin
        jump gramEasyDone

    if attempts ==0:
        queue sound gramLose
        show eaeng_e3_tile202 at Position(xpos = eae3letterS1x, xanchor = 0, ypos = eae3letterS1y, yanchor = 0)
        show eaeng_e3_tile206 at Position(xpos = eae3letterS2x, xanchor = 0, ypos = eae3letterS2y, yanchor = 0)
        show eaeng_e3_tile203 at Position(xpos = eae3letterMx, xanchor = 0, ypos = eae3letterMy, yanchor = 0)
        show eaeng_e3_tile205 at Position(xpos = eae3letterS3x, xanchor = 0, ypos = eae3letterS3y, yanchor = 0)
        show eaeng_e3_tile201 at Position(xpos = eae3letterKx, xanchor = 0, ypos = eae3letterKy, yanchor = 0)
        show eaeng_e3_tile204 at Position(xpos = eae3letterJx, xanchor = 0, ypos = eae3letterJy, yanchor = 0)
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_gramEasyLose
        $attemptsGramEasy +=1
        jump gramEasyLose
    
    jump gamefile_e3