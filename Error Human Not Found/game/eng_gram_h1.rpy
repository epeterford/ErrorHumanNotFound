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


screen grammar_h1:
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
        action Jump("hints_gramHard_1")
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
                drag_name "letterK1"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK1x ypos letterK1y
        drag:
                drag_name "letterK2"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK2x ypos letterK2y
        drag:
                drag_name "letterT3"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT3x ypos letterT3y
        drag:
                drag_name "letterA1"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA4x ypos letterA4y
        drag:
                drag_name "letterT1"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos lettertT5x ypos lettertT5y
        drag:
                drag_name "letterA2"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterA6x ypos letterA6y
        drag:
                drag_name "letterF1"
                child "letterF.png"
                droppable False
                dragged gate_dragged
                xpos letterF7x ypos letterF7y
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos 1035 ypos 340
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos 1495 ypos 340
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos 1035 ypos 515
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos 1335 ypos 515
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos 1495 ypos 515
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos 1655 ypos 515
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos 1495 ypos 685
         
        #dragback 
        drag:
                drag_name "LetterK_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562
        drag:
                drag_name "LetterF_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
        drag:
                drag_name "LetterA_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738
        drag:
                drag_name "LetterT_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738

init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_h1:
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg Eng_Tile

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image eaeng_h1_tile0 = "instructions11.png"
    image eaeng_h1_tile1 = "1_1_green.png"
    image eaeng_h1_tile2 = "letterS.png"
    show eaeng_h1_tile0 at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show eaeng_h1_tile1 at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show eaeng_h1_tile2 at Position(xpos = 1265, xanchor = 0, ypos = 165, yanchor = 0)
    
    #row2 5-8

    image eaeng_h1_tile5 = "leftTreelong1.png"
    image eaeng_h1_tile6 = "rightTreelong1.png"

    show eaeng_h1_tile5 at Position(xpos = 1050, xanchor = 0, ypos = 250, yanchor = 0)
    show eaeng_h1_tile6 at Position(xpos = 1300, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image eaeng_h1_tile9 = "1_1_grey.png"
    image eaeng_h1_tile10 = "1_1_grey.png"
    

    show eaeng_h1_tile9 at Position(xpos = 1020, xanchor = 0, ypos = 325, yanchor = 0)
    show eaeng_h1_tile10 at Position(xpos = 1480, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image eaeng_h1_tile14 = "treeGrey.png"
    image eaeng_h1_tile15 = "leftTreelong.png"
    image eaeng_h1_tile16 = "treeGrey.png"
    image eaeng_h1_tile17 = "rightTreelong.png"

    show eaeng_h1_tile14 at Position(xpos = 1020, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_h1_tile15 at Position(xpos = 1365, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_h1_tile16 at Position(xpos = 1480, xanchor = 0, ypos = 425, yanchor = 0)
    show eaeng_h1_tile17 at Position(xpos = 1550, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image eaeng_h1_tile21 = "1_1_grey.png"
    image eaeng_h1_tile22 = "1_1_grey.png"
    image eaeng_h1_tile23 = "1_1_grey.png"
    image eaeng_h1_tile24 = "1_1_grey.png"

    show eaeng_h1_tile21 at Position(xpos = 1020, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_h1_tile22 at Position(xpos = 1320, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_h1_tile23 at Position(xpos = 1480, xanchor = 0, ypos = 500, yanchor = 0)
    show eaeng_h1_tile24 at Position(xpos = 1640, xanchor = 0, ypos = 500, yanchor = 0)
    
    
    #row6 28-34

    image eaeng_h1_tile1031 = "treeGrey.png"
    
    show eaeng_h1_tile1031 at Position(xpos = 1480, xanchor = 0, ypos = 600, yanchor = 0)
    
    
    #row6 35-41

    image eaeng_h1_tile38 = "1_1_grey.png"
    
    show eaeng_h1_tile38 at Position(xpos = 1480, xanchor = 0, ypos = 675, yanchor = 0)

    image eaeng_h1_tile31 = "letterBorder.png"
    image eaeng_h1_tile32 = "letterBorder.png"
    image eaeng_h1_tile34 = "letterBorder.png"
    image eaeng_h1_tile35 = "letterBorder.png"
    show eaeng_h1_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_h1_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
#    show eaeng_h1_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_h1_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_h1_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)
#    show eaeng_h1_tile36 at Position(xpos = 330, xanchor = 0, ypos = 817, yanchor = 0)

    #Transparent Letters for Dragbacks
    image eaeng_h1_tile300 = "letterK_grey.png"
    image eaeng_h1_tile301 = "letterF_grey.png"
    image eaeng_h1_tile303 = "letterA_grey.png"
    image eaeng_h1_tile304 = "letterT_grey.png"
    show eaeng_h1_tile300 at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_h1_tile301 at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    show eaeng_h1_tile303 at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eaeng_h1_tile304 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)


    # gates
    $ letterK1x = 275
    $ letterK1y = 575
    $ letterK2x = 275
    $ letterK2y = 575
    $ letterT3x = 410 
    $ letterT3y = 750
    $ letterA4x = 275
    $ letterA4y = 750
    $ lettertT5x = 410
    $ lettertT5y = 750
    $ letterA6x = 275 
    $ letterA6y = 750
    $ letterF7x = 410 
    $ letterF7y = 575

    # check conditons for locations
    $ letterK1in1 = False
    $ letterK1in2 = False
    $ letterK1in3 = False
    $ letterK1in4 = False
    $ letterK1in5 = False
    $ letterK1in6 = False
    $ letterK1in7 = False

    $ letterK2in1 = False
    $ letterK2in2 = False
    $ letterK2in3 = False
    $ letterK2in4 = False
    $ letterK2in5 = False
    $ letterK2in6 = False
    $ letterK2in7 = False

    $ letterT3in1 = False
    $ letterT3in2 = False
    $ letterT3in3 = False
    $ letterT3in4 = False
    $ letterT3in5 = False
    $ letterT3in6 = False
    $ letterT3in7 = False

    $ letterA4in1 = False
    $ letterA4in2 = False
    $ letterA4in3 = False
    $ letterA4in4 = False
    $ letterA4in5 = False
    $ letterA4in6 = False
    $ letterA4in7 = False

    $ letterT5in1 = False
    $ letterT5in2 = False
    $ letterT5in3 = False
    $ letterT5in4 = False
    $ letterT5in5 = False
    $ letterT5in6 = False
    $ letterT5in7 = False

    $ letterA6in1 = False
    $ letterA6in2 = False
    $ letterA6in3 = False
    $ letterA6in4 = False
    $ letterA6in5 = False
    $ letterA6in6 = False
    $ letterA6in7 = False

    $ letterF7in1 = False
    $ letterF7in2 = False
    $ letterF7in3 = False
    $ letterF7in4 = False
    $ letterF7in5 = False
    $ letterF7in6 = False
    $ letterF7in7 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 11
    
    call gamefile_h1 from _call_gamefile_h1



label gamefile_h1:
    call screen grammar_h1

    if gate_name == "letterK1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False

            #sets values for checks
            $ letterK1x = 1035
            $ letterK1y = 340
            $ letterK1in1 = True
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False


                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ letterK1x = 1495
            $ letterK1y = 340
            $ letterK1in1 = False
            $ letterK1in2 = True
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False

                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ letterK1x = 1035
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = True
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ letterK1x = 1335
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = True
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ letterK1x = 1495
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = True
            $ letterK1in6 = False
            $ letterK1in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ letterK1x = 1655
            $ letterK1y = 515
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = True
            $ letterK1in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ letterK1x = 1495
            $ letterK1y = 690
            $ letterK1in1 = False
            $ letterK1in2 = False
            $ letterK1in3 = False
            $ letterK1in4 = False
            $ letterK1in5 = False
            $ letterK1in6 = False
            $ letterK1in7 = True

    if gate_name == "letterK2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False

            #sets values for checks
            $ letterK2x = 1035
            $ letterK2y = 340
            $ letterK2in1 = True
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ letterK2x = 1495
            $ letterK2y = 340
            $ letterK2in1 = False
            $ letterK2in2 = True
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ letterK2x = 1035
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = True
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ letterK2x = 1335
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = True
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ letterK2x = 1495
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = True
            $ letterK2in6 = False
            $ letterK2in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ letterK2x = 1655
            $ letterK2y = 515
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = True
            $ letterK2in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ letterK2x = 1495
            $ letterK2y = 690
            $ letterK2in1 = False
            $ letterK2in2 = False
            $ letterK2in3 = False
            $ letterK2in4 = False
            $ letterK2in5 = False
            $ letterK2in6 = False
            $ letterK2in7 = True

    if gate_name == "letterT3":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False
            #sets values for checks
            $ letterT3x = 1035
            $ letterT3y = 340
            $ letterT3in1 = True
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ letterT3x = 1495
            $ letterT3y = 340
            $ letterT3in1 = False
            $ letterT3in2 = True
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ letterT3x = 1035
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = True
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ letterT3x = 1335
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = True
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ letterT3x = 1495
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = True
            $ letterT3in6 = False
            $ letterT3in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ letterT3x = 1655
            $ letterT3y = 515
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = True
            $ letterT3in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ letterT3x = 1495
            $ letterT3y = 690
            $ letterT3in1 = False
            $ letterT3in2 = False
            $ letterT3in3 = False
            $ letterT3in4 = False
            $ letterT3in5 = False
            $ letterT3in6 = False
            $ letterT3in7 = True

    if gate_name == "letterA1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False
            #sets values for checks
            $ letterA4x = 1035
            $ letterA4y = 340
            $ letterA4in1 = True
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ letterA4x = 1495
            $ letterA4y = 340
            $ letterA4in1 = False
            $ letterA4in2 = True
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ letterA4x = 1035
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = True
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ letterA4x = 1335
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = True
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ letterA4x = 1495
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = True
            $ letterA4in6 = False
            $ letterA4in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ letterA4x = 1655
            $ letterA4y = 515
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = True
            $ letterA4in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ letterA4x = 1495
            $ letterA4y = 690
            $ letterA4in1 = False
            $ letterA4in2 = False
            $ letterA4in3 = False
            $ letterA4in4 = False
            $ letterA4in5 = False
            $ letterA4in6 = False
            $ letterA4in7 = True


    if gate_name == "letterT1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False

            #sets values for checks
            $ lettertT5x = 1035
            $ lettertT5y = 340
            $ letterT5in1 = True
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ lettertT5x = 1495
            $ lettertT5y = 340
            $ letterT5in1 = False
            $ letterT5in2 = True
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ lettertT5x = 1035
            $ lettertT5y = 515
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = True
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ lettertT5x = 1335
            $ lettertT5y = 515
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = True
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ lettertT5x = 1495
            $ lettertT5y = 515
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = True
            $ letterT5in6 = False
            $ letterT5in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ lettertT5x = 1655
            $ lettertT5y = 515
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = True
            $ letterT5in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ lettertT5x = 1495
            $ lettertT5y = 690
            $ letterT5in1 = False
            $ letterT5in2 = False
            $ letterT5in3 = False
            $ letterT5in4 = False
            $ letterT5in5 = False
            $ letterT5in6 = False
            $ letterT5in7 = True

    if gate_name == "letterA2":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False
            #sets values for checks
            $ letterA6x = 1035
            $ letterA6y = 340
            $ letterA6in1 = True
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ letterA6x = 1495
            $ letterA6y = 340
            $ letterA6in1 = False
            $ letterA6in2 = True
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ letterA6x = 1035
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = True
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ letterA6x = 1335
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = True
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ letterA6x = 1495
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = True
            $ letterA6in6 = False
            $ letterA6in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ letterA6x = 1655
            $ letterA6y = 515
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = True
            $ letterA6in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ letterA6x = 1495
            $ letterA6y = 690
            $ letterA6in1 = False
            $ letterA6in2 = False
            $ letterA6in3 = False
            $ letterA6in4 = False
            $ letterA6in5 = False
            $ letterA6in6 = False
            $ letterA6in7 = True


    if gate_name == "letterF1":
            #call and_gate_pos_1
            #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #check to make sure no other gram_h1_tile here
            if letterK1in1 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in1 = False
            if letterK2in1 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in1 = False
            if letterT3in1 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in1 = False
            if letterA4in1 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in1 = False
            if letterT5in1 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in1 = False
            if letterA6in1 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in1 = False
            if letterF7in1 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in1 = False

            #sets values for checks
            $ letterF7x = 1035
            $ letterF7y = 340
            $ letterF7in1 = True
            $ letterF7in2 = False
            $ letterF7in3 = False
            $ letterF7in4 = False
            $ letterF7in5 = False
            $ letterF7in6 = False
            $ letterF7in7 = False

                    #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if letterK1in2 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in2 = False
            if letterK2in2 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in2 = False
            if letterT3in2 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in2 = False
            if letterA4in2 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in2 = False
            if letterT5in2 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in2 = False
            if letterA6in2 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in2 = False
            if letterF7in2 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in2 = False

            #sets check values
            $ letterF7x = 1495
            $ letterF7y = 340
            $ letterF7in1 = False
            $ letterF7in2 = True
            $ letterF7in3 = False
            $ letterF7in4 = False
            $ letterF7in5 = False
            $ letterF7in6 = False
            $ letterF7in7 = False
                
        #gate slot number 3******************************
        if slot_name == "gate slot three":
            if letterK1in3 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in3 = False
            if letterK2in3 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in3 = False
            if letterT3in3 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in3 = False
            if letterA4in3 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in3 = False
            if letterT5in3 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in3 = False
            if letterA6in3 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in3 = False
            if letterF7in3 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in3 = False

            #sets values for the checks
            $ letterF7x = 1035
            $ letterF7y = 515
            $ letterF7in1 = False
            $ letterF7in2 = False
            $ letterF7in3 = True
            $ letterF7in4 = False
            $ letterF7in5 = False
            $ letterF7in6 = False
            $ letterF7in7 = False

                #gate slot number 4******************************
        if slot_name == "gate slot four":
            if letterK1in4 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in4 = False
            if letterK2in4 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in4 = False
            if letterT3in4 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in4 = False
            if letterA4in4 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in4 = False
            if letterT5in4 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in4 = False
            if letterA6in4 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in4 = False
            if letterF7in4 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in4 = False

            #sets values for the checks
            $ letterF7x = 1335
            $ letterF7y = 515
            $ letterF7in1 = False
            $ letterF7in2 = False
            $ letterF7in3 = False
            $ letterF7in4 = True
            $ letterF7in5 = False
            $ letterF7in6 = False
            $ letterF7in7 = False

                #gate slot number 5******************************
        if slot_name == "gate slot five":
            if letterK1in5 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in5 = False
            if letterK2in5 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in5 = False
            if letterT3in5 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in5 = False
            if letterA4in5 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in5 = False
            if letterT5in5 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in5 = False
            if letterA6in5 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in5 = False
            if letterF7in5 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in5 = False

            #sets values for the checks
            $ letterF7x = 1495
            $ letterF7y = 515
            $ letterF7in1 = False
            $ letterF7in2 = False
            $ letterF7in3 = False
            $ letterF7in4 = False
            $ letterF7in5 = True
            $ letterF7in6 = False
            $ letterF7in7 = False

                #gate slot number 6******************************
        if slot_name == "gate slot six":
            if letterK1in6 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in6 = False
            if letterK2in6 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in6 = False
            if letterT3in6 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in6 = False
            if letterA4in6 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in6 = False
            if letterT5in6 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in6 = False
            if letterA6in6 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in6 = False
            if letterF7in6 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in6 = False

            #sets values for the checks
            $ letterF7x = 1655
            $ letterF7y = 515
            $ letterF7in1 = False
            $ letterF7in2 = False
            $ letterF7in3 = False
            $ letterF7in4 = False
            $ letterF7in5 = False
            $ letterF7in6 = True
            $ letterF7in7 = False

                #gate slot number 7******************************
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
               $ letterK1x = 275
               $ letterK1y = 575
               $ letterK1in7 = False
            if letterK2in7 == True:
               $ letterK2x = 275
               $ letterK2y = 575
               $ letterK2in7 = False
            if letterT3in7 == True:
               $ letterT3x = 410
               $ letterT3y = 750
               $ letterT3in7 = False
            if letterA4in7 == True:
               $ letterA4x = 275
               $ letterA4y = 750
               $ letterA4in7 = False
            if letterT5in7 == True:
               $ lettertT5x = 410
               $ lettertT5y = 750
               $ letterT5in7 = False
            if letterA6in7 == True:
               $ letterA6x = 275
               $ letterA6y = 750
               $ letterA6in7 = False
            if letterF7in7 == True:
               $ letterF7x = 410
               $ letterF7y = 575
               $ letterF7in7 = False

            #sets values for the checks
            $ letterF7x = 1495
            $ letterF7y = 690
            $ letterF7in1 = False
            $ letterF7in2 = False
            $ letterF7in3 = False
            $ letterF7in4 = False
            $ letterF7in5 = False
            $ letterF7in6 = False
            $ letterF7in7 = True


    #Dragbacks
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "LetterK_return" or slot_name == "LetterF_return" or slot_name == "LetterA_return" or slot_name == "LetterT_return")):
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
                if gate_name == "letterK1":
                    $ letterK1x = 275
                    $ letterK1y = 575
                    $ letterK1in1 = False
                    $ letterK1in2 = False
                    $ letterK1in3 = False
                    $ letterK1in4 = False
                    $ letterK1in5 = False
                    $ letterK1in6 = False
                    $ letterK1in7 = False
                if gate_name == "letterK2":
                    $ letterK2x = 275
                    $ letterK2y = 575
                    $ letterK2in1 = False
                    $ letterK2in2 = False
                    $ letterK2in3 = False
                    $ letterK2in4 = False
                    $ letterK2in5 = False
                    $ letterK2in6 = False
                    $ letterK2in7 = False
   
            if slot_name == "LetterF_return":
                $ attempts +=1
                if gate_name == "letterF1":
                    $ letterF7x = 410
                    $ letterF7y = 575
                    $ letterF7in1 = False
                    $ letterF7in2 = False
                    $ letterF7in3 = False
                    $ letterF7in4 = False
                    $ letterF7in5 = False
                    $ letterF7in6 = False
                    $ letterF7in7 = False
            
            if slot_name == "LetterA_return":
                $ attempts +=1
                if gate_name == "letterA1":
                    $ letterA4x = 275
                    $ letterA4y = 750
                    $ letterA4in1 = False
                    $ letterA4in2 = False
                    $ letterA4in3 = False
                    $ letterA4in4 = False
                    $ letterA4in5 = False
                    $ letterA4in6 = False
                    $ letterA4in7 = False
                                    
                if gate_name == "letterA2":
                    $ letterA6x = 275
                    $ letterA6y = 750
                    $ letterA6in1 = False
                    $ letterA6in2 = False
                    $ letterA6in3 = False
                    $ letterA6in4 = False
                    $ letterA6in5 = False
                    $ letterA6in6 = False
                    $ letterA6in7 = False
                    
            if slot_name == "LetterT_return":
                $ attempts +=1
                if gate_name == "letterT1":
                    $ lettertT5x = 410
                    $ lettertT5y = 750
                    $ letterT5in1 = False
                    $ letterT5in2 = False
                    $ letterT5in3 = False
                    $ letterT5in4 = False
                    $ letterT5in5 = False
                    $ letterT5in6 = False
                    $ letterT5in7 = False
                
                if gate_name == "letterT3":
                    $ letterT3x = 410
                    $ letterT3y = 750
                    $ letterT3in1 = False
                    $ letterT3in2 = False
                    $ letterT3in3 = False
                    $ letterT3in4 = False
                    $ letterT3in5 = False
                    $ letterT3in6 = False
                    $ letterT3in7 = False
                    

    hide gram_h1_tile46
    hide gram_h1_tile47
    hide gram_h1_tile48
    hide gram_h1_tile49
    hide gram_h1_tile50
    hide gram_h1_tile51
    hide gram_h1_tile78
    hide gram_h1_tile79
    hide gram_h1_tile66
    hide gram_h1_tile67
    hide gram_h1_tile68
    hide gram_h1_tile69
    hide gram_h1_tile70
    hide gram_h1_tile71
    hide gram_h1_tile52
    hide gram_h1_tile53
    hide gram_h1_tile54
    hide gram_h1_tile55
    hide gram_h1_tile56
    hide gram_h1_tile57
    hide gram_h1_tile58
    hide gram_h1_tile59
    hide gram_h1_tile60
    hide gram_h1_tile61
    hide gram_h1_tile62
    hide gram_h1_tile63
    hide gram_h1_tile64
    hide gram_h1_tile65
    hide gram_h1_tile66
    hide gram_h1_tile67
    hide gram_h1_tile68
    hide gram_h1_tile69
    hide gram_h1_tile70
    hide gram_h1_tile71
    hide gram_h1_tile88
    hide gram_h1_tile89
    hide gram_h1_tile90
    hide gram_h1_tile91
    hide gram_h1_tile92
    hide gram_h1_tile93
    hide gram_h1_tile80
    hide gram_h1_tile81
    hide gram_h1_tile82
    hide gram_h1_tile83
    hide gram_h1_tile42
    hide gram_h1_tile43
    hide gram_h1_tile44
    hide gram_h1_tile45
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if ((letterT3in1 or letterT5in1) and (letterT3in2 or letterT5in2)):
        image gram_h1_tile42 = "leftTreegreenlong1.png"
        image gram_h1_tile43 = "1_1_green.png"
        show gram_h1_tile42 at Position(xpos = 1050, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_h1_tile43 at Position(xpos = 1020, xanchor = 0, ypos = 325, yanchor = 0)

        image gram_h1_tile44 = "rightTreegreenlong1.png"
        image gram_h1_tile45 = "1_1_green.png"
        show gram_h1_tile44 at Position(xpos = 1300, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_h1_tile45 at Position(xpos = 1480, xanchor = 0, ypos = 325, yanchor = 0)
        if gramRow1_C_sound_right1 ==0:
            $gramRow1_C_sound_right1 +=1
            play sound gramTree1
        if(letterK1in3 or letterK2in3):
            image gram_h1_tile46 = "treeGreen.png"
            image gram_h1_tile47 = "1_1_green.png"
            show gram_h1_tile46 at Position(xpos = 1020, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile47 at Position(xpos = 1020, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h1_tile48 = "solutionLine.png"
            image gram_h1_tile49 = "solutionLine.png"
            show gram_h1_tile48 at Position(xpos = 1020, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_h1_tile49 at Position(xpos = 1020, xanchor = 0, ypos = 692, yanchor = 0)           
            image gram_h1_tile50 = "solutionLine.png"
            show gram_h1_tile50 at Position(xpos = 1020, xanchor = 0, ypos = 785, yanchor = 0)
            image gram_h1_tile51 = "squishy.png"
            show gram_h1_tile51 at Position(xpos = 1000, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_L_sound_right1 ==0:
                $gramRow2_L_sound_right1 +=1
                play sound gramTree1
                queue sound gramText1
        elif(letterA4in3 or letterA6in3 or letterF7in3):
            image gram_h1_tile78 = "treeRed.png"
            image gram_h1_tile79 = "1_1_Red.png"
            show gram_h1_tile78 at Position(xpos = 1020, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile79 at Position(xpos = 1020, xanchor = 0, ypos = 500, yanchor = 0)
            if gramRow2_L_sound_wrong1 ==0:
                $gramRow2_L_sound_wrong1 +=1
                play sound gramTree5
        if(not(letterK1in3 or letterK2in3)):
            if gramRow2_L_sound_right1==1:
                $gramRow2_L_sound_right1 -=1
        if(not(letterA4in3 or letterA6in3 or letterF7in3)):
            if gramRow2_L_sound_wrong1==1:
                $gramRow2_L_sound_wrong1 -=1
        if((letterA4in4 or letterA6in4) and (letterK1in5 or letterK2in5) and (letterA4in6 or letterA6in6)):
            image gram_h1_tile52 = "leftTreegreenlong.png"
            image gram_h1_tile53 = "1_1_green.png"
            show gram_h1_tile52 at Position(xpos = 1365, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile53 at Position(xpos = 1320, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h1_tile54 = "solutionLine.png"
            image gram_h1_tile55 = "solutionLine.png"
            show gram_h1_tile54 at Position(xpos = 1320, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_h1_tile55 at Position(xpos = 1320, xanchor = 0, ypos = 692, yanchor = 0)
            image gram_h1_tile56 = "solutionLine.png"
            image gram_h1_tile57 = "simian.png"
            show gram_h1_tile56 at Position(xpos = 1320, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_h1_tile57 at Position(xpos = 1290, xanchor = 0, ypos = 800, yanchor = 0)

            image gram_h1_tile58 = "treeGreen.png"
            image gram_h1_tile59 = "1_1_green.png"
            show gram_h1_tile58 at Position(xpos = 1480, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile59 at Position(xpos = 1480, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_h1_tile60 = "rightTreegreenlong.png"
            image gram_h1_tile61 = "1_1_green.png"
            show gram_h1_tile60 at Position(xpos = 1550, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile61 at Position(xpos = 1640, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h1_tile62 = "solutionLine.png"
            image gram_h1_tile63 = "solutionLine.png"
            image gram_h1_tile64 = "solutionLine.png"
            image gram_h1_tile65 = "scratcher.png"
            show gram_h1_tile62 at Position(xpos = 1640, xanchor = 0, ypos = 600, yanchor = 0)
            show gram_h1_tile63 at Position(xpos = 1640, xanchor = 0, ypos = 692, yanchor = 0)
            show gram_h1_tile64 at Position(xpos = 1640, xanchor = 0, ypos = 785, yanchor = 0)
            show gram_h1_tile65 at Position(xpos = 1640, xanchor = 0, ypos = 800, yanchor = 0)
            if gramRow2_R_sound_right1 ==0:
                $gramRow2_R_sound_right1 +=1
                play sound gramTree1
                queue sound gramText2
            if(letterF7in7):
                image gram_h1_tile66 = "treeGreen.png"
                image gram_h1_tile67 = "1_1_green.png"
                show gram_h1_tile66 at Position(xpos = 1480, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h1_tile67 at Position(xpos = 1480, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h1_tile68 = "solutionLine.png"
                image gram_h1_tile69 = "nose.png"
                show gram_h1_tile68 at Position(xpos = 1485, xanchor = 0, ypos = 770, yanchor = 0)
                show gram_h1_tile69 at Position(xpos = 1460, xanchor = 0, ypos = 800, yanchor = 0)
                if gramRow3_R_sound_right1 ==0:
                    $gramRow3_R_sound_right1 +=1
                    play sound gramTree1
                    queue sound gramText3
            elif(letterK1in7 or letterK2in7):
                image gram_h1_tile70 = "treeRed.png"
                image gram_h1_tile71 = "1_1_Red.png"
                show gram_h1_tile70 at Position(xpos = 1480, xanchor = 0, ypos = 600, yanchor = 0)
                show gram_h1_tile71 at Position(xpos = 1480, xanchor = 0, ypos = 675, yanchor = 0)
                if gramRow3_R_sound_wrong1 ==0:
                    $gramRow3_R_sound_wrong1 +=1
                    play sound gramTree5
            if(not(letterF7in7)):
                if gramRow3_R_sound_right1 ==1:
                    $gramRow3_R_sound_right1 -=1
            if(not(letterK1in7 or letterK2in7)):
                if gramRow3_R_sound_wrong1 ==1:
                    $gramRow3_R_sound_wrong1 -=1
        elif((letterA4in4 or letterA6in4 or letterK1in4 or letterK2in4 or letterF7in4) and (letterA4in5 or letterA6in5 or letterK1in5 or letterK2in5 or letterF7in5) and (letterA4in6 or letterA6in6 or letterK1in6 or letterK2in6 or letterF7in6)):
            image gram_h1_tile88 = "leftTreeredlong.png"
            image gram_h1_tile89 = "1_1_red.png"
            show gram_h1_tile88 at Position(xpos = 1365, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile89 at Position(xpos = 1320, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_h1_tile90 = "treeRed.png"
            image gram_h1_tile91 = "1_1_red.png"
            show gram_h1_tile90 at Position(xpos = 1480, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile91 at Position(xpos = 1480, xanchor = 0, ypos = 500, yanchor = 0)

            image gram_h1_tile92 = "rightTreeredlong.png"
            image gram_h1_tile93 = "1_1_red.png"
            show gram_h1_tile92 at Position(xpos = 1550, xanchor = 0, ypos = 425, yanchor = 0)
            show gram_h1_tile93 at Position(xpos = 1640, xanchor = 0, ypos = 500, yanchor = 0)
            if gramRow2_R_sound_wrong1 ==0:
                $gramRow2_R_sound_wrong1 +=1
                play sound gramTree5
        if(not((letterA4in4 or letterA6in4) and (letterK1in5 or letterK2in5) and (letterA4in6 or letterA6in6))):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
        if(not((letterA4in4 or letterA6in4 or letterK1in4 or letterK2in4 or letterF7in4) and (letterA4in5 or letterA6in5 or letterK1in5 or letterK2in5 or letterF7in5) and (letterA4in6 or letterA6in6 or letterK1in6 or letterK2in6 or letterF7in6))):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1

    elif((letterK2in1 or letterK1in1 or letterT3in1 or letterT5in1 or letterA4in1 or letterA6in1 or letterF7in1) and (letterK2in2 or letterK1in2 or letterT3in2 or letterT5in2 or letterA4in2 or letterA6in2 or letterF7in2)):
        image gram_h1_tile80 = "leftTreeredlong1.png"
        image gram_h1_tile81 = "1_1_Red.png"
        show gram_h1_tile80 at Position(xpos = 1050, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_h1_tile81 at Position(xpos = 1020, xanchor = 0, ypos = 325, yanchor = 0)

        image gram_h1_tile82 = "rightTreeredlong1.png"
        image gram_h1_tile83 = "1_1_Red.png"
        show gram_h1_tile82 at Position(xpos = 1300, xanchor = 0, ypos = 250, yanchor = 0)
        show gram_h1_tile83 at Position(xpos = 1480, xanchor = 0, ypos = 325, yanchor = 0)
        if gramRow1_C_sound_wrong1 ==0:
            $gramRow1_C_sound_wrong1 +=1
            play sound gramTree5
    if(not((letterT3in1 or letterT5in1) and (letterT3in2 or letterT5in2))):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
    if(not((letterK2in1 or letterK1in1 or letterT3in1 or letterT5in1 or letterA4in1 or letterA6in1 or letterF7in1) and (letterK2in2 or letterK1in2 or letterT3in2 or letterT5in2 or letterA4in2 or letterA6in2 or letterF7in2))):
        if gramRow1_C_sound_wrong1 ==1:
            $gramRow1_C_sound_wrong1 -=1
    if ((letterT3in1 or letterT5in1) and (letterT3in2 or letterT5in2) and 
        (letterK1in3 or letterK2in3) and (letterA4in4 or letterA6in4) and (letterK2in5 or letterK1in5) and 
        (letterA4in6 or letterA6in6) and (letterF7in7)):

        image gram_h1_tile202 = "letterK.png"
        image gram_h1_tile206 = "letterK.png"
        image gram_h1_tile203 = "letterT.png"
        image gram_h1_tile205 = "letterA.png"
        image gram_h1_tile201 = "letterT.png"
        image gram_h1_tile204 = "letterA.png"
        image gram_h1_tile208 = "letterF.png"
        
        show gram_h1_tile202 at Position(xpos = letterK1x, xanchor = 0, ypos = letterK1y, yanchor = 0)
        show gram_h1_tile206 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
        show gram_h1_tile203 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
        show gram_h1_tile205 at Position(xpos = letterA4x, xanchor = 0, ypos = letterA4y, yanchor = 0)
        show gram_h1_tile201 at Position(xpos = lettertT5x, xanchor = 0, ypos = lettertT5y, yanchor = 0)
        show gram_h1_tile204 at Position(xpos = letterA6x, xanchor = 0, ypos = letterA6y, yanchor = 0)
        show gram_h1_tile208 at Position(xpos = letterF7x, xanchor = 0, ypos = letterF7y, yanchor = 0)
        queue sound gramWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_gramHardWin
        $gramHard_solved = True
        jump gramHard_win

    if attempts ==0:

        show gram_h1_tile202 at Position(xpos = letterK1x, xanchor = 0, ypos = letterK1y, yanchor = 0)
        show gram_h1_tile206 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
        show gram_h1_tile203 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
        show gram_h1_tile205 at Position(xpos = letterA4x, xanchor = 0, ypos = letterA4y, yanchor = 0)
        show gram_h1_tile201 at Position(xpos = lettertT5x, xanchor = 0, ypos = lettertT5y, yanchor = 0)
        show gram_h1_tile204 at Position(xpos = letterA6x, xanchor = 0, ypos = letterA6y, yanchor = 0)
        show gram_h1_tile208 at Position(xpos = letterF7x, xanchor = 0, ypos = letterF7y, yanchor = 0)
        queue sound gramLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_gramHardLose
        $gramHard_attempts +=1
        jump gramHard_lose
    
    jump gamefile_h1