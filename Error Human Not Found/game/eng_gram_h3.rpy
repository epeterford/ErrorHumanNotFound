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

init:
    image bg Eng_Tile = "eng_tile_bg.png"

screen grammar_hard3:
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
        action Jump("hints_gramHard_3")
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
        drag:
                drag_name "letterS1"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS1x ypos letterS1y
        drag:
                drag_name "letterS2"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS2x ypos letterS2y
        drag:
                drag_name "letterS3"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS3x ypos letterS3y
        drag:
                drag_name "letterS4"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS4x ypos letterS4y
        drag:
                drag_name "letterS5"
                child "letterS.png"
                droppable False
                dragged gate_dragged
                xpos letterS5x ypos letterS5y
        drag:
                drag_name "letterT1"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT1x ypos letterT1y
        drag:
                drag_name "letterT2"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT2x ypos letterT2y
        drag:
                drag_name "letterT3"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterT3x ypos letterT3y
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJx ypos letterJy
        drag:
                drag_name "letterK"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterKx ypos letterKy
        drag:
                drag_name "letterH"
                child "letterH.png"
                droppable False
                dragged gate_dragged
                xpos letterHx ypos letterHy
        
        #location to be dropped
        drag:
                drag_name "gate slot one"                
                draggable False
                child "images/border.png"
                xpos gate1x ypos gate1y
        drag:
                drag_name "gate slot two"
                draggable False
                child "images/border.png"
                xpos gate2x ypos gate2y
        drag:
                drag_name "gate slot three"
                draggable False
                child "images/border.png"
                xpos gate3x ypos gate3y
        drag:
                drag_name "gate slot four"
                draggable False
                child "images/border.png"
                xpos gate4x ypos gate4y
        drag:
                drag_name "gate slot five"
                draggable False
                child "images/border.png"
                xpos gate5x ypos gate5y
        drag:
                drag_name "gate slot six"
                draggable False
                child "images/border.png"
                xpos gate6x ypos gate6y
        drag:
                drag_name "gate slot seven"
                draggable False
                child "images/border.png"
                xpos gate7x ypos gate7y
        drag:
                drag_name "gate slot eight"
                draggable False
                child "images/border.png"
                xpos gate8x ypos gate8y
        drag:
                drag_name "gate slot nine"
                draggable False
                child "images/border.png"
                xpos gate9x ypos gate9y
        drag:
                drag_name "gate slot ten"
                draggable False
                child "images/border.png"
                xpos gate10x ypos gate10y
        drag:
                drag_name "gate slot eleven"
                draggable False
                child "images/border.png"
                xpos gate11x ypos gate11y

        #Gate Slots ******************************************************************************
        drag:
                drag_name "letterS_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 562

        drag:
                drag_name "letterT_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 562
                
        drag:
                drag_name "letterJ_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 330 ypos 648

        drag:
                drag_name "letterK_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 738

        drag:
                drag_name "letterH_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 738
                
label eng_gram_h3:
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
    image gram_h3_instructions = "instructions13.png"
    image gram_h3_baseSlot = "1_1_green.png"
    image gram_h3_baseLetter = "letterS.png"
    show gram_h3_instructions at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_h3_baseSlot at Position(xpos = 1420, xanchor = 0, ypos = 150, yanchor = 0)
    show gram_h3_baseLetter at Position(xpos = 1435, xanchor = 0, ypos = 165, yanchor = 0)
    
    #row2 5-8

    image gram_h3_connector1 = "leftTreelong2.png"
    image gram_h3_connector2 = "treeGrey.png"
    image gram_h3_connector3 = "rightTreelong1.png"

    show gram_h3_connector1 at Position(xpos = 1055, xanchor = 0, ypos = 250, yanchor = 0)
    show gram_h3_connector2 at Position(xpos = 1420, xanchor = 0, ypos = 250, yanchor = 0)
    show gram_h3_connector3 at Position(xpos = 1480, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image gram_h3_slot1 = "1_1_grey.png"
    image gram_h3_slot2 = "1_1_grey.png"
    image gram_h3_slot3 = "1_1_grey.png"
    

    show gram_h3_slot1 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
    show gram_h3_slot2 at Position(xpos = 1420, xanchor = 0, ypos = 325, yanchor = 0)
    show gram_h3_slot3 at Position(xpos = 1660, xanchor = 0, ypos = 325, yanchor = 0)


    #row4 14-20

    image gram_h3_connector4 = "leftTreelong.png"
    image gram_h3_connector5 = "treeGrey.png"
    image gram_h3_connector6 = "rightTreelong.png"
    image gram_h3_connector7 = "leftTree.png"
    image gram_h3_connector8 = "rightTree.png"

    show gram_h3_connector4 at Position(xpos = 900, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h3_connector5 at Position(xpos = 1025, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h3_connector6 at Position(xpos = 1100, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h3_connector7 at Position(xpos = 1380, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h3_connector8 at Position(xpos = 1490, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image gram_h3_slot4 = "1_1_grey.png"
    image gram_h3_slot5 = "1_1_grey.png"
    image gram_h3_slot6 = "1_1_grey.png"
    image gram_h3_slot7 = "1_1_grey.png"
    image gram_h3_slot8 = "1_1_grey.png"

    show gram_h3_slot4 at Position(xpos = 860, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h3_slot5 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h3_slot6 at Position(xpos = 1190, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h3_slot7 at Position(xpos = 1340, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h3_slot8 at Position(xpos = 1505, xanchor = 0, ypos = 500, yanchor = 0)
    
    
    #row6 28-34

    image gram_h3_connector10 = "leftTree.png"
    image gram_h3_connector13 = "treeGrey.png"
    image gram_h3_connector12 = "treeGrey.png"
    
    show gram_h3_connector10 at Position(xpos = 820, xanchor = 0, ypos = 600, yanchor = 0)
    show gram_h3_connector13 at Position(xpos = 890, xanchor = 0, ypos = 600, yanchor = 0)
    show gram_h3_connector12 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
    
    #row6 35-41

    image gram_h3_slot9 = "1_1_grey.png"
    image gram_h3_slot10 = "1_1_grey.png"
    image gram_h3_slot12 = "1_1_grey.png"

    show gram_h3_slot9 at Position(xpos = 780, xanchor = 0, ypos = 675, yanchor = 0)
    show gram_h3_slot10 at Position(xpos = 890, xanchor = 0, ypos = 675, yanchor = 0)
    show gram_h3_slot12 at Position(xpos = 1025, xanchor = 0, ypos = 675, yanchor = 0)
                
    image eaeng_h3_tile31 = "letterBorder.png"
    image eaeng_h3_tile32 = "letterBorder.png"
    image eaeng_h3_tile33 = "letterBorder.png"
    image eaeng_h3_tile34 = "letterBorder.png"
    image eaeng_h3_tile35 = "letterBorder.png"
    show eaeng_h3_tile31 at Position(xpos = 262, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_h3_tile32 at Position(xpos = 397, xanchor = 0, ypos = 562, yanchor = 0)
    show eaeng_h3_tile33 at Position(xpos = 330, xanchor = 0, ypos = 648, yanchor = 0)
    show eaeng_h3_tile34 at Position(xpos = 262, xanchor = 0, ypos = 738, yanchor = 0)
    show eaeng_h3_tile35 at Position(xpos = 397, xanchor = 0, ypos = 738, yanchor = 0)

    image eng_gram_h3_grayK = "letterK_grey.png"
    image eng_gram_h3_grayH = "letterH_grey.png"
    image eng_gram_h3_grayJ = "letterJ_grey.png"
    image eng_gram_h3_grayS = "letterS_grey.png"
    image eng_gram_h3_grayT = "letterT_grey.png"
    #x: 275/342/410
    #y: 575/660/750
    show eng_gram_h3_grayK at Position(xpos = 275, xanchor = 0, ypos = 750, yanchor = 0)
    show eng_gram_h3_grayH at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    show eng_gram_h3_grayJ at Position(xpos = 342, xanchor = 0, ypos = 660, yanchor = 0)
    show eng_gram_h3_grayS at Position(xpos = 275, xanchor = 0, ypos = 575, yanchor = 0)
    show eng_gram_h3_grayT at Position(xpos = 410, xanchor = 0, ypos = 575, yanchor = 0)
    
    $startletterSx = 275
    $startletterSy = 575
    $startletterTx = 410
    $startletterTy = 575
    $startletterJx = 342
    $startletterJy = 660
    $startletterKx = 275
    $startletterKy = 750
    $startletterHx = 410
    $startletterHy = 750
    
    $letterS1x = startletterSx
    $letterS1y = startletterSy
    $letterS2x = startletterSx
    $letterS2y = startletterSy
    $letterS3x = startletterSx
    $letterS3y = startletterSy
    $letterS4x = startletterSx
    $letterS4y = startletterSy
    $letterS5x = startletterSx
    $letterS5y = startletterSy
    $letterT1x = startletterTx
    $letterT1y = startletterTy
    $letterT2x = startletterTx
    $letterT2y = startletterTy
    $letterT3x = startletterTx
    $letterT3y = startletterTy
    $letterJx = startletterJx
    $letterJy = startletterJy
    $letterKx = startletterKx
    $letterKy = startletterKy
    $letterHx = startletterHx
    $letterHy = startletterHy

    # gates
    $ gate1x = 1040 
    $ gate1y = 340
    $ gate2x = 1435
    $ gate2y = 340
    $ gate3x = 1675 
    $ gate3y = 340
    $ gate4x = 875
    $ gate4y = 515
    $ gate5x = 1040
    $ gate5y = 515
    $ gate6x = 1205 
    $ gate6y = 515
    $ gate7x = 1355 
    $ gate7y = 515
    $ gate8x = 1520
    $ gate8y = 515
    $ gate9x = 795 
    $ gate9y = 690
    $ gate10x = 905
    $ gate10y = 690
    $ gate11x = 1040
    $ gate11y = 690
    
    #location conditions
    $letterS1in1 = False
    $letterS1in2 = False
    $letterS1in3 = False
    $letterS1in4 = False
    $letterS1in5 = False
    $letterS1in6 = False
    $letterS1in7 = False
    $letterS1in8 = False
    $letterS1in9 = False
    $letterS1in10 = False
    $letterS1in11 = False
    
    $letterS2in1 = False
    $letterS2in2 = False
    $letterS2in3 = False
    $letterS2in4 = False
    $letterS2in5 = False
    $letterS2in6 = False
    $letterS2in7 = False
    $letterS2in8 = False
    $letterS2in9 = False
    $letterS2in10 = False
    $letterS2in11 = False
    
    $letterS3in1 = False
    $letterS3in2 = False
    $letterS3in3 = False
    $letterS3in4 = False
    $letterS3in5 = False
    $letterS3in6 = False
    $letterS3in7 = False
    $letterS3in8 = False
    $letterS3in9 = False
    $letterS3in10 = False
    $letterS3in11 = False
    
    $letterS4in1 = False
    $letterS4in2 = False
    $letterS4in3 = False
    $letterS4in4 = False
    $letterS4in5 = False
    $letterS4in6 = False
    $letterS4in7 = False
    $letterS4in8 = False
    $letterS4in9 = False
    $letterS4in10 = False
    $letterS4in11 = False
    
    $letterS5in1 = False
    $letterS5in2 = False
    $letterS5in3 = False
    $letterS5in4 = False
    $letterS5in5 = False
    $letterS5in6 = False
    $letterS5in7 = False
    $letterS5in8 = False
    $letterS5in9 = False
    $letterS5in10 = False
    $letterS5in11 = False
    
    $letterT1in1 = False
    $letterT1in2 = False
    $letterT1in3 = False
    $letterT1in4 = False
    $letterT1in5 = False
    $letterT1in6 = False
    $letterT1in7 = False
    $letterT1in8 = False
    $letterT1in9 = False
    $letterT1in10 = False
    $letterT1in11 = False
    
    $letterT2in1 = False
    $letterT2in2 = False
    $letterT2in3 = False
    $letterT2in4 = False
    $letterT2in5 = False
    $letterT2in6 = False
    $letterT2in7 = False
    $letterT2in8 = False
    $letterT2in9 = False
    $letterT2in10 = False
    $letterT2in11 = False
    
    $letterT3in1 = False
    $letterT3in2 = False
    $letterT3in3 = False
    $letterT3in4 = False
    $letterT3in5 = False
    $letterT3in6 = False
    $letterT3in7 = False
    $letterT3in8 = False
    $letterT3in9 = False
    $letterT3in10 = False
    $letterT3in11 = False
    
    $letterJin1 = False
    $letterJin2 = False
    $letterJin3 = False
    $letterJin4 = False
    $letterJin5 = False
    $letterJin6 = False
    $letterJin7 = False
    $letterJin8 = False
    $letterJin9 = False
    $letterJin10 = False
    $letterJin11 = False
    
    $letterKin1 = False
    $letterKin2 = False
    $letterKin3 = False
    $letterKin4 = False
    $letterKin5 = False
    $letterKin6 = False
    $letterKin7 = False
    $letterKin8 = False
    $letterKin9 = False
    $letterKin10 = False
    $letterKin11 = False
    
    $letterHin1 = False
    $letterHin2 = False
    $letterHin3 = False
    $letterHin4 = False
    $letterHin5 = False
    $letterHin6 = False
    $letterHin7 = False
    $letterHin8 = False
    $letterHin9 = False
    $letterHin10 = False
    $letterHin11 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 15
    
    call gamefile_h3

label gamefile_h3:
    call screen grammar_hard3
    
    #First Letter *******************************************************************************************
    if gate_name == "letterS1":
        if slot_name == "gate slot one":
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterS1x = gate1x
            $letterS1y = gate1y
            $letterS1in1 = True
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot two":
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterS1x = gate2x
            $letterS1y = gate2y
            $letterS1in1 = False
            $letterS1in2 = True
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot three":
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterS1x = gate3x
            $letterS1y = gate3y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = True
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot four":
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterS1x = gate4x
            $letterS1y = gate4y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = True
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot five":
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterS1x = gate5x
            $letterS1y = gate5y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = True
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot six":
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterS1x = gate6x
            $letterS1y = gate6y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = True
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterS1x = gate7x
            $letterS1y = gate7y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = True
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot eight":
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterS1x = gate8x
            $letterS1y = gate8y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = True
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot nine":
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterS1x = gate9x
            $letterS1y = gate9y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = True
            $letterS1in10 = False
            $letterS1in11 = False
            
        if slot_name == "gate slot ten":
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterS1x = gate10x
            $letterS1y = gate10y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = True
            $letterS1in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterS1x = gate11x
            $letterS1y = gate11y
            $letterS1in1 = False
            $letterS1in2 = False
            $letterS1in3 = False
            $letterS1in4 = False
            $letterS1in5 = False
            $letterS1in6 = False
            $letterS1in7 = False
            $letterS1in8 = False
            $letterS1in9 = False
            $letterS1in10 = False
            $letterS1in11 = True
    
    #Second Letter *******************************************************************************************
    if gate_name == "letterS2":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterS2x = gate1x
            $letterS2y = gate1y
            $letterS2in1 = True
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterS2x = gate2x
            $letterS2y = gate2y
            $letterS2in1 = False
            $letterS2in2 = True
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterS2x = gate3x
            $letterS2y = gate3y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = True
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterS2x = gate4x
            $letterS2y = gate4y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = True
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterS2x = gate5x
            $letterS2y = gate5y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = True
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterS2x = gate6x
            $letterS2y = gate6y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = True
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterS2x = gate7x
            $letterS2y = gate7y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = True
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterS2x = gate8x
            $letterS2y = gate8y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = True
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterS2x = gate9x
            $letterS2y = gate9y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = True
            $letterS2in10 = False
            $letterS2in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterS2x = gate10x
            $letterS2y = gate10y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = True
            $letterS2in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterS2x = gate11x
            $letterS2y = gate11y
            $letterS2in1 = False
            $letterS2in2 = False
            $letterS2in3 = False
            $letterS2in4 = False
            $letterS2in5 = False
            $letterS2in6 = False
            $letterS2in7 = False
            $letterS2in8 = False
            $letterS2in9 = False
            $letterS2in10 = False
            $letterS2in11 = True
    
    #Third Letter *******************************************************************************************
    if gate_name == "letterS3":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterS3x = gate1x
            $letterS3y = gate1y
            $letterS3in1 = True
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterS3x = gate2x
            $letterS3y = gate2y
            $letterS3in1 = False
            $letterS3in2 = True
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterS3x = gate3x
            $letterS3y = gate3y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = True
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterS3x = gate4x
            $letterS3y = gate4y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = True
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterS3x = gate5x
            $letterS3y = gate5y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = True
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterS3x = gate6x
            $letterS3y = gate6y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = True
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterS3x = gate7x
            $letterS3y = gate7y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = True
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterS3x = gate8x
            $letterS3y = gate8y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = True
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterS3x = gate9x
            $letterS3y = gate9y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = True
            $letterS3in10 = False
            $letterS3in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterS3x = gate10x
            $letterS3y = gate10y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = True
            $letterS3in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterS3x = gate11x
            $letterS3y = gate11y
            $letterS3in1 = False
            $letterS3in2 = False
            $letterS3in3 = False
            $letterS3in4 = False
            $letterS3in5 = False
            $letterS3in6 = False
            $letterS3in7 = False
            $letterS3in8 = False
            $letterS3in9 = False
            $letterS3in10 = False
            $letterS3in11 = True
    
    #Fourth Letter *******************************************************************************************
    if gate_name == "letterS4":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterS4x = gate1x
            $letterS4y = gate1y
            $letterS4in1 = True
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterS4x = gate2x
            $letterS4y = gate2y
            $letterS4in1 = False
            $letterS4in2 = True
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterS4x = gate3x
            $letterS4y = gate3y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = True
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterS4x = gate4x
            $letterS4y = gate4y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = True
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterS4x = gate5x
            $letterS4y = gate5y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = True
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterS4x = gate6x
            $letterS4y = gate6y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = True
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterS4x = gate7x
            $letterS4y = gate7y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = True
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterS4x = gate8x
            $letterS4y = gate8y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = True
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterS4x = gate9x
            $letterS4y = gate9y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = True
            $letterS4in10 = False
            $letterS4in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterS4x = gate10x
            $letterS4y = gate10y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = True
            $letterS4in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterS4x = gate11x
            $letterS4y = gate11y
            $letterS4in1 = False
            $letterS4in2 = False
            $letterS4in3 = False
            $letterS4in4 = False
            $letterS4in5 = False
            $letterS4in6 = False
            $letterS4in7 = False
            $letterS4in8 = False
            $letterS4in9 = False
            $letterS4in10 = False
            $letterS4in11 = True
    
    #Fifth Letter *******************************************************************************************
    if gate_name == "letterS5":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterS5x = gate1x
            $letterS5y = gate1y
            $letterS5in1 = True
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterS5x = gate2x
            $letterS5y = gate2y
            $letterS5in1 = False
            $letterS5in2 = True
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterS5x = gate3x
            $letterS5y = gate3y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = True
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterS5x = gate4x
            $letterS5y = gate4y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = True
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterS5x = gate5x
            $letterS5y = gate5y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = True
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterS5x = gate6x
            $letterS5y = gate6y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = True
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterS5x = gate7x
            $letterS5y = gate7y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = True
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterS5x = gate8x
            $letterS5y = gate8y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = True
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterS5x = gate9x
            $letterS5y = gate9y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = True
            $letterS5in10 = False
            $letterS5in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterS5x = gate10x
            $letterS5y = gate10y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = True
            $letterS5in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterS5x = gate11x
            $letterS5y = gate11y
            $letterS5in1 = False
            $letterS5in2 = False
            $letterS5in3 = False
            $letterS5in4 = False
            $letterS5in5 = False
            $letterS5in6 = False
            $letterS5in7 = False
            $letterS5in8 = False
            $letterS5in9 = False
            $letterS5in10 = False
            $letterS5in11 = True
    
    #Sixth Letter *******************************************************************************************
    if gate_name == "letterT1":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterT1x = gate1x
            $letterT1y = gate1y
            $letterT1in1 = True
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterT1x = gate2x
            $letterT1y = gate2y
            $letterT1in1 = False
            $letterT1in2 = True
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterT1x = gate3x
            $letterT1y = gate3y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = True
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterT1x = gate4x
            $letterT1y = gate4y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = True
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterT1x = gate5x
            $letterT1y = gate5y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = True
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterT1x = gate6x
            $letterT1y = gate6y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = True
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterT1x = gate7x
            $letterT1y = gate7y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = True
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterT1x = gate8x
            $letterT1y = gate8y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = True
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterT1x = gate9x
            $letterT1y = gate9y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = True
            $letterT1in10 = False
            $letterT1in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterT1x = gate10x
            $letterT1y = gate10y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = True
            $letterT1in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterT1x = gate11x
            $letterT1y = gate11y
            $letterT1in1 = False
            $letterT1in2 = False
            $letterT1in3 = False
            $letterT1in4 = False
            $letterT1in5 = False
            $letterT1in6 = False
            $letterT1in7 = False
            $letterT1in8 = False
            $letterT1in9 = False
            $letterT1in10 = False
            $letterT1in11 = True
    
    #Seventh Letter *******************************************************************************************
    if gate_name == "letterT2":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterT2x = gate1x
            $letterT2y = gate1y
            $letterT2in1 = True
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterT2x = gate2x
            $letterT2y = gate2y
            $letterT2in1 = False
            $letterT2in2 = True
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterT2x = gate3x
            $letterT2y = gate3y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = True
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterT2x = gate4x
            $letterT2y = gate4y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = True
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterT2x = gate5x
            $letterT2y = gate5y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = True
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterT2x = gate6x
            $letterT2y = gate6y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = True
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterT2x = gate7x
            $letterT2y = gate7y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = True
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterT2x = gate8x
            $letterT2y = gate8y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = True
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterT2x = gate9x
            $letterT2y = gate9y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = True
            $letterT2in10 = False
            $letterT2in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterT2x = gate10x
            $letterT2y = gate10y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = True
            $letterT2in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterT2x = gate11x
            $letterT2y = gate11y
            $letterT2in1 = False
            $letterT2in2 = False
            $letterT2in3 = False
            $letterT2in4 = False
            $letterT2in5 = False
            $letterT2in6 = False
            $letterT2in7 = False
            $letterT2in8 = False
            $letterT2in9 = False
            $letterT2in10 = False
            $letterT2in11 = True
    
    #Eighth Letter *******************************************************************************************
    if gate_name == "letterT3":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterT3x = gate1x
            $letterT3y = gate1y
            $letterT3in1 = True
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterT3x = gate2x
            $letterT3y = gate2y
            $letterT3in1 = False
            $letterT3in2 = True
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterT3x = gate3x
            $letterT3y = gate3y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = True
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterT3x = gate4x
            $letterT3y = gate4y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = True
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterT3x = gate5x
            $letterT3y = gate5y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = True
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterT3x = gate6x
            $letterT3y = gate6y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = True
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterT3x = gate7x
            $letterT3y = gate7y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = True
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterT3x = gate8x
            $letterT3y = gate8y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = True
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterT3x = gate9x
            $letterT3y = gate9y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = True
            $letterT3in10 = False
            $letterT3in11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterT3x = gate10x
            $letterT3y = gate10y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = True
            $letterT3in11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterT3x = gate11x
            $letterT3y = gate11y
            $letterT3in1 = False
            $letterT3in2 = False
            $letterT3in3 = False
            $letterT3in4 = False
            $letterT3in5 = False
            $letterT3in6 = False
            $letterT3in7 = False
            $letterT3in8 = False
            $letterT3in9 = False
            $letterT3in10 = False
            $letterT3in11 = True
    
    #Ninth Letter *******************************************************************************************
    if gate_name == "letterJ":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterJx = gate1x
            $letterJy = gate1y
            $letterJin1 = True
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterJx = gate2x
            $letterJy = gate2y
            $letterJin1 = False
            $letterJin2 = True
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterJx = gate3x
            $letterJy = gate3y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = True
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterJx = gate4x
            $letterJy = gate4y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = True
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterJx = gate5x
            $letterJy = gate5y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = True
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterJx = gate6x
            $letterJy = gate6y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = True
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterJx = gate7x
            $letterJy = gate7y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = True
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterJx = gate8x
            $letterJy = gate8y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = True
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterJx = gate9x
            $letterJy = gate9y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = True
            $letterJin10 = False
            $letterJin11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterJx = gate10x
            $letterJy = gate10y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = True
            $letterJin11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterJx = gate11x
            $letterJy = gate11y
            $letterJin1 = False
            $letterJin2 = False
            $letterJin3 = False
            $letterJin4 = False
            $letterJin5 = False
            $letterJin6 = False
            $letterJin7 = False
            $letterJin8 = False
            $letterJin9 = False
            $letterJin10 = False
            $letterJin11 = True
    
    #Tenth Letter *******************************************************************************************
    if gate_name == "letterK":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterHin1 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin1 = False
            #sets values for checks
            $letterKx = gate1x
            $letterKy = gate1y
            $letterKin1 = True
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterHin2 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin2 = False
            #sets values for checks
            $letterKx = gate2x
            $letterKy = gate2y
            $letterKin1 = False
            $letterKin2 = True
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterHin3 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin3 = False
            #sets values for checks
            $letterKx = gate3x
            $letterKy = gate3y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = True
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterHin4 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin4 = False
            #sets values for checks
            $letterKx = gate4x
            $letterKy = gate4y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = True
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterHin5 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin5 = False
            #sets values for checks
            $letterKx = gate5x
            $letterKy = gate5y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = True
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterHin6 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin6 = False
            #sets values for checks
            $letterKx = gate6x
            $letterKy = gate6y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = True
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterHin7 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin7 = False
            #sets values for checks
            $letterKx = gate7x
            $letterKy = gate7y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = True
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterHin8 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin8 = False
            #sets values for checks
            $letterKx = gate8x
            $letterKy = gate8y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = True
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterHin9 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin9 = False
            #sets values for checks
            $letterKx = gate9x
            $letterKy = gate9y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = True
            $letterKin10 = False
            $letterKin11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterHin10 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin10 = False
            #sets values for checks
            $letterKx = gate10x
            $letterKy = gate10y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = True
            $letterKin11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterHin11 == True:
                $letterHx = startletterHx
                $letterHy = startletterHy
                $letterHin11 = False
            #sets values for checks
            $letterKx = gate11x
            $letterKy = gate11y
            $letterKin1 = False
            $letterKin2 = False
            $letterKin3 = False
            $letterKin4 = False
            $letterKin5 = False
            $letterKin6 = False
            $letterKin7 = False
            $letterKin8 = False
            $letterKin9 = False
            $letterKin10 = False
            $letterKin11 = True           
    
    #Eleventh Letter *******************************************************************************************
    if gate_name == "letterH":
        if slot_name == "gate slot one":
            if letterS1in1 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in1 = False
            if letterS2in1 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in1 = False
            if letterS3in1 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in1 = False
            if letterS4in1 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in1 = False
            if letterS5in1 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in1 = False
            if letterT1in1 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in1 = False
            if letterT2in1 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in1 = False
            if letterT3in1 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterKin1 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin1 = False
            #sets values for checks
            $letterHx = gate1x
            $letterHy = gate1y
            $letterHin1 = True
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot two":
            if letterS1in2 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in2 = False
            if letterS2in2 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in2 = False
            if letterS3in2 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in2 = False
            if letterS4in2 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in2 = False
            if letterS5in2 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in2 = False
            if letterT1in2 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in2 = False
            if letterT2in2 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in2 = False
            if letterT3in2 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterKin2 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin2 = False
            #sets values for checks
            $letterHx = gate2x
            $letterHy = gate2y
            $letterHin1 = False
            $letterHin2 = True
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot three":
            if letterS1in3 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in3 = False
            if letterS2in3 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in3 = False
            if letterS3in3 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in3 = False
            if letterS4in3 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in3 = False
            if letterS5in3 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in3 = False
            if letterT1in3 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in3 = False
            if letterT2in3 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in3 = False
            if letterT3in3 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterKin3 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin3 = False
            #sets values for checks
            $letterHx = gate3x
            $letterHy = gate3y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = True
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot four":
            if letterS1in4 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in4 = False
            if letterS2in4 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in4 = False
            if letterS3in4 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in4 = False
            if letterS4in4 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in4 = False
            if letterS5in4 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in4 = False
            if letterT1in4 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in4 = False
            if letterT2in4 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in4 = False
            if letterT3in4 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterKin4 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin4 = False
            #sets values for checks
            $letterHx = gate4x
            $letterHy = gate4y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = True
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot five":
            if letterS1in5 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in5 = False
            if letterS2in5 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in5 = False
            if letterS3in5 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in5 = False
            if letterS4in5 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in5 = False
            if letterS5in5 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in5 = False
            if letterT1in5 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in5 = False
            if letterT2in5 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in5 = False
            if letterT3in5 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterKin5 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin5 = False
            #sets values for checks
            $letterHx = gate5x
            $letterHy = gate5y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = True
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot six":
            if letterS1in6 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in6 = False
            if letterS2in6 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in6 = False
            if letterS3in6 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in6 = False
            if letterS4in6 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in6 = False
            if letterS5in6 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in6 = False
            if letterT1in6 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in6 = False
            if letterT2in6 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in6 = False
            if letterT3in6 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterKin6 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin6 = False
            #sets values for checks
            $letterHx = gate6x
            $letterHy = gate6y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = True
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
                        
        if slot_name == "gate slot seven":
            if letterS1in7 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in7 = False
            if letterS2in7 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in7 = False
            if letterS3in7 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in7 = False
            if letterS4in7 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in7 = False
            if letterS5in7 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in7 = False
            if letterT1in7 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in7 = False
            if letterT2in7 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in7 = False
            if letterT3in7 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterKin7 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin7 = False
            #sets values for checks
            $letterHx = gate7x
            $letterHy = gate7y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = True
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot eight":
            if letterS1in8 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in8 = False
            if letterS2in8 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in8 = False
            if letterS3in8 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in8 = False
            if letterS4in8 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in8 = False
            if letterS5in8 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in8 = False
            if letterT1in8 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in8 = False
            if letterT2in8 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in8 = False
            if letterT3in8 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterKin8 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin8 = False
            #sets values for checks
            $letterHx = gate8x
            $letterHy = gate8y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = True
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot nine":
            if letterS1in9 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in9 = False
            if letterS2in9 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in9 = False
            if letterS3in9 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in9 = False
            if letterS4in9 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in9 = False
            if letterS5in9 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in9 = False
            if letterT1in9 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in9 = False
            if letterT2in9 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in9 = False
            if letterT3in9 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterKin9 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin9 = False
            #sets values for checks
            $letterHx = gate9x
            $letterHy = gate9y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = True
            $letterHin10 = False
            $letterHin11 = False
            
        if slot_name == "gate slot ten":
            if letterS1in10 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in10 = False
            if letterS2in10 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in10 = False
            if letterS3in10 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in10 = False
            if letterS4in10 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in10 = False
            if letterS5in10 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in10 = False
            if letterT1in10 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in10 = False
            if letterT2in10 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in10 = False
            if letterT3in10 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in10 = False
            if letterJin10 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin10 = False
            if letterKin10 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin10 = False
            #sets values for checks
            $letterHx = gate10x
            $letterHy = gate10y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = True
            $letterHin11 = False
            
        if slot_name == "gate slot eleven":
            if letterS1in11 == True:
                $letterS1x = startletterSx
                $letterS1y = startletterSy
                $letterS1in11 = False
            if letterS2in11 == True:
                $letterS2x = startletterSx
                $letterS2y = startletterSy
                $letterS2in11 = False
            if letterS3in11 == True:
                $letterS3x = startletterSx
                $letterS3y = startletterSy
                $letterS3in11 = False
            if letterS4in11 == True:
                $letterS4x = startletterSx
                $letterS4y = startletterSy
                $letterS4in11 = False
            if letterS5in11 == True:
                $letterS5x = startletterSx
                $letterS5y = startletterSy
                $letterS5in11 = False
            if letterT1in11 == True:
                $letterT1x = startletterTx
                $letterT1y = startletterTy
                $letterT1in11 = False
            if letterT2in11 == True:
                $letterT2x = startletterTx
                $letterT2y = startletterTy
                $letterT2in11 = False
            if letterT3in11 == True:
                $letterT3x = startletterTx
                $letterT3y = startletterTy
                $letterT3in11 = False
            if letterJin11 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin11 = False
            if letterKin11 == True:
                $letterKx = startletterKx
                $letterKy = startletterKy
                $letterKin11 = False
            #sets values for checks
            $letterHx = gate11x
            $letterHy = gate11y
            $letterHin1 = False
            $letterHin2 = False
            $letterHin3 = False
            $letterHin4 = False
            $letterHin5 = False
            $letterHin6 = False
            $letterHin7 = False
            $letterHin8 = False
            $letterHin9 = False
            $letterHin10 = False
            $letterHin11 = True
            
 
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name == "letterK_gate_return" or slot_name == "letterS_gate_return" or slot_name == "letterT_gate_return" or slot_name == "letterJ_gate_return" or slot_name == "letterH_gate_return")):
       $ temp_slot = slot_name
       $ temp_gate = gate_name
       if temp_slot != "" and temp_gate != "":
           $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $attempts -=1
            $temp_slot = slot_name
            $temp_gate = gate_name

            if slot_name == "letterS_gate_return":
                $ attempts +=1
                if gate_name == "letterS1":
                    $ letterS1x = startletterSx
                    $ letterS1y = startletterSy
                    $ letterS1in1 = False
                    $ letterS1in2 = False
                    $ letterS1in3 = False
                    $ letterS1in4 = False
                    $ letterS1in5 = False
                    $ letterS1in6 = False
                    $ letterS1in7 = False
                    $ letterS1in8 = False
                    $ letterS1in9 = False
                    $ letterS1in10 = False
                    $ letterS1in11 = False
                if gate_name == "letterS2":
                    $ letterS2x = startletterSx
                    $ letterS2y = startletterSy
                    $ letterS2in1 = False
                    $ letterS2in2 = False
                    $ letterS2in3 = False
                    $ letterS2in4 = False
                    $ letterS2in5 = False
                    $ letterS2in6 = False
                    $ letterS2in7 = False
                    $ letterS2in8 = False
                    $ letterS2in9 = False
                    $ letterS2in10 = False
                    $ letterS2in11 = False
                if gate_name == "letterS3":
                    $ letterS3x = startletterSx
                    $ letterS3y = startletterSy
                    $ letterS3in1 = False
                    $ letterS3in2 = False
                    $ letterS3in3 = False
                    $ letterS3in4 = False
                    $ letterS3in5 = False
                    $ letterS3in6 = False
                    $ letterS3in7 = False
                    $ letterS3in8 = False
                    $ letterS3in9 = False
                    $ letterS3in10 = False
                    $ letterS3in11 = False
                if gate_name == "letterS4":
                    $ letterS4x = startletterSx
                    $ letterS4y = startletterSy
                    $ letterS4in1 = False
                    $ letterS4in2 = False
                    $ letterS4in3 = False
                    $ letterS4in4 = False
                    $ letterS4in5 = False
                    $ letterS4in6 = False
                    $ letterS4in7 = False
                    $ letterS4in8 = False
                    $ letterS4in9 = False
                    $ letterS4in10 = False
                    $ letterS4in11 = False
                if gate_name == "letterS5":
                    $ letterS5x = startletterSx
                    $ letterS5y = startletterSy
                    $ letterS5in1 = False
                    $ letterS5in2 = False
                    $ letterS5in3 = False
                    $ letterS5in4 = False
                    $ letterS5in5 = False
                    $ letterS5in6 = False
                    $ letterS5in7 = False
                    $ letterS5in8 = False
                    $ letterS5in9 = False
                    $ letterS5in10 = False
                    $ letterS5in11 = False
            if slot_name == "letterT_gate_return":
                $ attempts +=1
                if gate_name == "letterT1":
                    $ letterT1x = startletterTx
                    $ letterT1y = startletterTy
                    $ letterT1in1 = False
                    $ letterT1in2 = False
                    $ letterT1in3 = False
                    $ letterT1in4 = False
                    $ letterT1in5 = False
                    $ letterT1in6 = False
                    $ letterT1in7 = False
                    $ letterT1in8 = False
                    $ letterT1in9 = False
                    $ letterT1in10 = False
                    $ letterT1in11 = False
                if gate_name == "letterT2":
                    $ letterT2x = startletterTx
                    $ letterT2y = startletterTy
                    $ letterT2in1 = False
                    $ letterT2in2 = False
                    $ letterT2in3 = False
                    $ letterT2in4 = False
                    $ letterT2in5 = False
                    $ letterT2in6 = False
                    $ letterT2in7 = False
                    $ letterT2in8 = False
                    $ letterT2in9 = False
                    $ letterT2in10 = False
                    $ letterT2in11 = False
                if gate_name == "letterT3":
                    $ letterT3x = startletterTx
                    $ letterT3y = startletterTy
                    $ letterT3in1 = False
                    $ letterT3in2 = False
                    $ letterT3in3 = False
                    $ letterT3in4 = False
                    $ letterT3in5 = False
                    $ letterT3in6 = False
                    $ letterT3in7 = False
                    $ letterT3in8 = False
                    $ letterT3in9 = False
                    $ letterT3in10 = False
                    $ letterT3in11 = False
            if slot_name == "letterJ_gate_return":
                $ attempts +=1
                if gate_name == "letterJ":
                    $ letterJx = startletterJx
                    $ letterJy = startletterJy
                    $ letterJin1 = False
                    $ letterJin2 = False
                    $ letterJin3 = False
                    $ letterJin4 = False
                    $ letterJin5 = False
                    $ letterJin6 = False
                    $ letterJin7 = False
                    $ letterJin8 = False
                    $ letterJin9 = False
                    $ letterJin10 = False
                    $ letterJin11 = False
            if slot_name == "letterK_gate_return":
                $ attempts +=1
                if gate_name == "letterK":
                    $ letterKx = startletterKx
                    $ letterKy = startletterKy
                    $ letterKin1 = False
                    $ letterKin2 = False
                    $ letterKin3 = False
                    $ letterKin4 = False
                    $ letterKin5 = False
                    $ letterKin6 = False
                    $ letterKin7 = False
                    $ letterKin8 = False
                    $ letterKin9 = False
                    $ letterKin10 = False
                    $ letterKin11 = False
            if slot_name == "letterH_gate_return":
                $ attempts +=1
                if gate_name == "letterH":
                    $ letterHx = startletterHx
                    $ letterHy = startletterHy
                    $ letterHin1 = False
                    $ letterHin2 = False
                    $ letterHin3 = False
                    $ letterHin4 = False
                    $ letterHin5 = False
                    $ letterHin6 = False
                    $ letterHin7 = False
                    $ letterHin8 = False
                    $ letterHin9 = False
                    $ letterHin10 = False
                    $ letterHin11 = False
           
    
    #Logic Implementation *********************************************************************
    hide gram_h3_colorTile1
    hide gram_h3_colorTile2
    hide gram_h3_colorTile3
    hide gram_h3_colorTile4
    hide gram_h3_colorTile5
    hide gram_h3_colorTile6
    hide gram_h3_colorTile7
    hide gram_h3_colorTile8
    hide gram_h3_colorTile9
    hide gram_h3_colorTile10
    hide gram_h3_colorTile11
    hide gram_h3_colorTile12
    hide gram_h3_colorTile13
    hide gram_h3_colorTile14
    hide gram_h3_colorTile15
    hide gram_h3_colorTile16
    hide gram_h3_colorTile17
    hide gram_h3_colorTile18
    hide gram_h3_colorTile19
    hide gram_h3_colorTile20
    hide gram_h3_colorTile21
    hide gram_h3_colorTile22
    hide gram_h3_colorTile23
    hide gram_h3_colorTile24
    hide gram_h3_colorTile25
    hide gram_h3_colorTile26
    hide gram_h3_colorTile27
    hide gram_h3_colorTile28
    hide gram_h3_colorTile29
    hide gram_h3_colorTile30
    hide gram_h3_colorTile31
    hide gram_h3_colorTile32
    hide gram_h3_colorTile33
    hide gram_h3_colorTile34
    hide gram_h3_colorTile35
    hide gram_h3_colorTile36
    hide gram_h3_colorTile37
    hide gram_h3_colorTile38
    hide gram_h3_colorTile39
    hide gram_h3_colorTile40
    hide gram_h3_colorTile41
    hide gram_h3_colorTile42
    hide gram_h3_colorTile43
    hide gram_h3_colorTile44
    hide gram_h3_colorTile45
    hide gram_h3_colorTile46
    hide gram_h3_colorTile47
    hide gram_h3_colorTile48
    hide gram_h3_colorTile49
    hide gram_h3_colorTile50
    hide gram_h3_colorTile51
    hide gram_h3_colorTile52
    hide gram_h3_colorTile53
    hide gram_h3_colorTile54
    hide gram_h3_colorTile55
    hide gram_h3_colorTile56
    hide gram_h3_colorTile57
    hide gram_h3_colorTile58
    hide gram_h3_colorTile59
    hide gram_h3_colorTile60
    hide gram_h3_colorTile61
    hide gram_h3_colorTile62
    hide gram_h3_colorTile63
    hide gram_h3_colorTile64
    hide gram_h3_colorTile65
    hide gram_h3_colorTile66
    hide gram_h3_colorTile67
    hide gram_h3_colorTile68
    $gramNormal = renpy.random.randint(0,2)
    if (gramNormal==0):
        play sound gramTree2
    if (gramNormal==1):
        play sound gramTree3
    if (gramNormal==2):
        play sound gramTree4
    if ((letterS1in1 or letterS2in1 or letterS3in1 or letterS4in1 or letterS5in1) and (letterT1in2 or letterT2in2 or letterT3in2) and
            (letterS1in3 or letterS2in3 or letterS3in3 or letterS4in3 or letterS5in3)):
        image gram_h3_colorTile1 = "leftTreegreenlong2.png"
        show gram_h3_colorTile1 at Position(xpos = 1055, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h3_colorTile2 = "treeGreen.png"
        show gram_h3_colorTile2 at Position(xpos = 1420, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h3_colorTile3 = "rightTreegreenlong1.png"
        show gram_h3_colorTile3 at Position(xpos = 1480, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h3_colorTile43 = "solutionLine.png"
        show gram_h3_colorTile43 at Position(xpos = 1660, xanchor = 0, ypos = 410, yanchor = 0)
        image gram_h3_colorTile44 = "solutionLine.png"
        show gram_h3_colorTile44 at Position(xpos = 1660, xanchor = 0, ypos = 500, yanchor = 0)
        image gram_h3_colorTile45 = "solutionLine.png"
        show gram_h3_colorTile45 at Position(xpos = 1660, xanchor = 0, ypos = 590, yanchor = 0)
        image gram_h3_colorTile46 = "solutionLine.png"
        show gram_h3_colorTile46 at Position(xpos = 1660, xanchor = 0, ypos = 680, yanchor = 0)
        image gram_h3_colorTile47 = "solutionLine.png"
        show gram_h3_colorTile47 at Position(xpos = 1660, xanchor = 0, ypos = 770, yanchor = 0)
        image gram_h3_colorTile4 = "1_1_green.png"
        show gram_h3_colorTile4 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h3_colorTile5 = "1_1_green.png"
        show gram_h3_colorTile5 at Position(xpos = 1420, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h3_colorTile6 = "1_1_green.png"
        show gram_h3_colorTile6 at Position(xpos = 1660, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h3_colorTile48 = "epsilon.png"
        show gram_h3_colorTile48 at Position(xpos = 1645, xanchor = 0, ypos = 820, yanchor = 0)
        if gramRow1_C_sound_right1 ==0:
            $gramRow1_C_sound_right1 +=1
            play sound gramTree1
            queue sound gramText3
        
        if ((letterS1in4 or letterS2in4 or letterS3in4 or letterS4in4 or letterS5in4) and (letterT1in5 or letterT2in5 or letterT3in5) and
                (letterS1in6 or letterS2in6 or letterS3in6 or letterS4in6 or letterS5in6)):
            image gram_h3_colorTile13 = "leftTreegreenlong.png"
            show gram_h3_colorTile13 at Position(xpos = 900, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile14 = "treeGreen.png"
            show gram_h3_colorTile14 at Position(xpos = 1025, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile15 = "rightTreegreenlong.png"
            show gram_h3_colorTile15 at Position(xpos = 1100, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile49 = "solutionLine.png"
            show gram_h3_colorTile49 at Position(xpos = 1190, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h3_colorTile50 = "solutionLine.png"
            show gram_h3_colorTile50 at Position(xpos = 1190, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h3_colorTile51 = "solutionLine.png"
            show gram_h3_colorTile51 at Position(xpos = 1190, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h3_colorTile16 = "1_1_green.png"
            show gram_h3_colorTile16 at Position(xpos = 860, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile17 = "1_1_green.png"
            show gram_h3_colorTile17 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile18 = "1_1_green.png"
            show gram_h3_colorTile18 at Position(xpos = 1190, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile52 = "epsilon.png"
            show gram_h3_colorTile52 at Position(xpos = 1165, xanchor = 0, ypos = 820, yanchor = 0)
            if gramRow2_L_sound_right1 ==0:
                $gramRow2_L_sound_right1 +=1
                play sound gramTree1
                queue sound gramText3
            if((letterS1in9 or letterS2in9 or letterS3in9 or letterS4in9 or letterS5in9) and (letterT1in10 or letterT2in10 or letterT3in10)):
                image gram_h3_colorTile25 = "leftTreegreen.png"
                show gram_h3_colorTile25 at Position(xpos = 820, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h3_colorTile26 = "treeGreen.png"
                show gram_h3_colorTile26 at Position(xpos = 890, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h3_colorTile29 = "solutionLine.png"
                show gram_h3_colorTile29 at Position(xpos = 760, xanchor = 0, ypos = 770, yanchor = 0)
                image gram_h3_colorTile30 = "solutionLine.png"
                show gram_h3_colorTile30 at Position(xpos = 895, xanchor = 0, ypos = 770, yanchor = 0)
                image gram_h3_colorTile27 = "1_1_green.png"
                show gram_h3_colorTile27 at Position(xpos = 780, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h3_colorTile28 = "1_1_green.png"
                show gram_h3_colorTile28 at Position(xpos = 890, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h3_colorTile31 = "epsilon.png"
                show gram_h3_colorTile31 at Position(xpos = 685, xanchor = 0, ypos = 820, yanchor = 0)
                image gram_h3_colorTile32 = "humans.png"
                show gram_h3_colorTile32 at Position(xpos = 845, xanchor = 0, ypos = 820, yanchor = 0)
                if gramRow3_L_sound_right1 ==0:
                    $gramRow3_L_sound_right1 +=1
                    play sound gramTree1
                    queue sound gramText1
            elif ((letterS1in9 or letterS2in9 or letterS3in9 or letterS4in9 or letterS5in9 or letterT1in9 or letterT2in9 or letterT3in9 or letterJin9 or letterKin9 or letterHin9) and
                    (letterS1in10 or letterS2in10 or letterS3in10 or letterS4in10 or letterS5in10 or letterT1in10 or letterT2in10 or letterT3in10 or letterJin10 or letterKin10 or letterHin10)):
                image gram_h3_colorTile33 = "leftTreered.png"
                show gram_h3_colorTile33 at Position(xpos = 820, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h3_colorTile34 = "treeRed.png"
                show gram_h3_colorTile34 at Position(xpos = 890, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h3_colorTile35 = "1_1_red.png"
                show gram_h3_colorTile35 at Position(xpos = 780, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h3_colorTile36 = "1_1_red.png"
                show gram_h3_colorTile36 at Position(xpos = 890, xanchor = 0, ypos = 675, yanchor = 0)
                if gramRow3_L_sound_wrong1 ==0:
                    $gramRow3_L_sound_wrong1 +=1
                    play sound gramTree5
            if((not(letterS1in9 or letterS2in9 or letterS3in9 or letterS4in9 or letterS5in9)) or (not(letterT1in10 or letterT2in10 or letterT3in10))):
                if gramRow3_L_sound_right1 ==1:
                    $gramRow3_L_sound_right1 -=1
            if((not(letterS1in9 or letterS2in9 or letterS3in9 or letterS4in9 or letterS5in9 or letterT1in9 or letterT2in9 or letterT3in9 or letterJin9 or letterKin9 or letterHin9)) or
                   (not(letterS1in10 or letterS2in10 or letterS3in10 or letterS4in10 or letterS5in10 or letterT1in10 or letterT2in10 or letterT3in10 or letterJin10 or letterKin10 or letterHin10))):
                if gramRow3_L_sound_wrong1 ==1:
                    $gramRow3_L_sound_wrong1 -=1
                    
            if letterJin11:
                image gram_h3_colorTile37 = "treeGreen.png"
                show gram_h3_colorTile37 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h3_colorTile38 = "solutionLine.png"
                show gram_h3_colorTile38 at Position(xpos = 1030, xanchor = 0, ypos = 770, yanchor = 0)
                image gram_h3_colorTile39 = "1_1_green.png"
                show gram_h3_colorTile39 at Position(xpos = 1025, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h3_colorTile40 = "are.png"
                show gram_h3_colorTile40 at Position(xpos = 1005, xanchor = 0, ypos = 820, yanchor = 0)
                if gramRow3_R_sound_right1 ==0:
                    $gramRow3_R_sound_right1 +=1
                    play sound gramTree1
                    queue sound gramText2
            elif ((letterS1in11 or letterS2in11 or letterS3in11 or letterS4in11 or letterS5in11 or letterT1in11 or letterT2in11 or letterT3in11 or letterKin11 or letterHin11)):
                image gram_h3_colorTile41 = "treeRed.png"
                show gram_h3_colorTile41 at Position(xpos = 1025, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h3_colorTile42 = "1_1_red.png"
                show gram_h3_colorTile42 at Position(xpos = 1025, xanchor = 0, ypos = 675, yanchor = 0)
                if gramRow3_R_sound_wrong1 ==0:
                    $gramRow3_R_sound_wrong1 +=1
                    play sound gramTree5
            if (not(letterJin11)):
                if gramRow3_R_sound_right1 ==1:
                    $gramRow3_R_sound_right1 -=1
            if (not(letterS1in11 or letterS2in11 or letterS3in11 or letterS4in11 or letterS5in11 or letterT1in11 or letterT2in11 or letterT3in11 or letterKin11 or letterHin11)):
                if gramRow3_R_sound_wrong1 ==1:
                    $gramRow3_R_sound_wrong1 -=1
        elif ((letterS1in4 or letterS2in4 or letterS3in4 or letterS4in4 or letterS5in4 or letterT1in4 or letterT2in4 or letterT3in4 or letterJin4 or letterKin4 or letterHin4) and
                (letterS1in5 or letterS2in5 or letterS3in5 or letterS4in5 or letterS5in5 or letterT1in5 or letterT2in5 or letterT3in5 or letterJin5 or letterKin5 or letterHin5) and
                (letterS1in6 or letterS2in6 or letterS3in6 or letterS4in6 or letterS5in6 or letterT1in6 or letterT2in6 or letterT3in6 or letterJin6 or letterKin6 or letterHin6)):
            image gram_h3_colorTile19 = "leftTreeredlong.png"
            show gram_h3_colorTile19 at Position(xpos = 900, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile20 = "treeRed.png"
            show gram_h3_colorTile20 at Position(xpos = 1025, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile21 = "rightTreeredlong.png"
            show gram_h3_colorTile21 at Position(xpos = 1100, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile22 = "1_1_red.png"
            show gram_h3_colorTile22 at Position(xpos = 860, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile23 = "1_1_red.png"
            show gram_h3_colorTile23 at Position(xpos = 1025, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile24 = "1_1_red.png"
            show gram_h3_colorTile24 at Position(xpos = 1190, xanchor = 0, ypos = 500, yanchor = 0)
            if gramRow2_L_sound_wrong1 ==0:
                $gramRow2_L_sound_wrong1 +=1
                play sound gramTree5
        
        if ((not(letterS1in4 or letterS2in4 or letterS3in4 or letterS4in4 or letterS5in4)) or (not(letterT1in5 or letterT2in5 or letterT3in5)) or
                (not(letterS1in6 or letterS2in6 or letterS3in6 or letterS4in6 or letterS5in6))):
            if gramRow2_L_sound_right1 ==1:
                $gramRow2_L_sound_right1 -=1
            
        if ((not(letterS1in4 or letterS2in4 or letterS3in4 or letterS4in4 or letterS5in4 or letterT1in4 or letterT2in4 or letterT3in4 or letterJin4 or letterKin4 or letterHin4)) or
                (not(letterS1in5 or letterS2in5 or letterS3in5 or letterS4in5 or letterS5in5 or letterT1in5 or letterT2in5 or letterT3in5 or letterJin5 or letterKin5 or letterHin5)) or
                (not(letterS1in6 or letterS2in6 or letterS3in6 or letterS4in6 or letterS5in6 or letterT1in6 or letterT2in6 or letterT3in6 or letterJin6 or letterKin6 or letterHin6))):
            if gramRow2_L_sound_wrong1==1:
                $gramRow2_L_sound_wrong1 -=1
            
        if letterKin7 and letterHin8:
            image gram_h3_colorTile53 = "leftTreegreen.png"
            show gram_h3_colorTile53 at Position(xpos = 1380, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile54 = "rightTreegreen.png"
            show gram_h3_colorTile54 at Position(xpos = 1490, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile55 = "solutionLine.png"
            show gram_h3_colorTile55 at Position(xpos = 1340, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h3_colorTile56 = "solutionLine.png"
            show gram_h3_colorTile56 at Position(xpos = 1505, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h3_colorTile57 = "solutionLine.png"
            show gram_h3_colorTile57 at Position(xpos = 1340, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h3_colorTile58 = "solutionLine.png"
            show gram_h3_colorTile58 at Position(xpos = 1505, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h3_colorTile59 = "solutionLine.png"
            show gram_h3_colorTile59 at Position(xpos = 1340, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h3_colorTile60 = "solutionLine.png"
            show gram_h3_colorTile60 at Position(xpos = 1505, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h3_colorTile61 = "1_1_green.png"
            show gram_h3_colorTile61 at Position(xpos = 1340, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile62 = "1_1_green.png"
            show gram_h3_colorTile62 at Position(xpos = 1505, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile63 = "so.png"
            show gram_h3_colorTile63 at Position(xpos = 1325, xanchor = 0, ypos = 820, yanchor = 0)
            image gram_h3_colorTile64 = "inefficient.png"
            show gram_h3_colorTile64 at Position(xpos = 1485, xanchor = 0, ypos = 820, yanchor = 0)
            if gramRow2_R_sound_right1 ==0:
                $gramRow2_R_sound_right1 +=1
                play sound gramTree1
                queue sound gramText1
        elif ((letterS1in7 or letterS2in7 or letterS3in7 or letterS4in7 or letterS5in7 or letterT1in7 or letterT2in7 or letterT3in7 or letterJin7 or letterKin7 or letterHin7) and
                (letterS1in8 or letterS2in8 or letterS3in8 or letterS4in8 or letterS5in8 or letterT1in8 or letterT2in8 or letterT3in8 or letterJin8 or letterKin8 or letterHin8)):
            image gram_h3_colorTile65 = "leftTreered.png"
            show gram_h3_colorTile65 at Position(xpos = 1380, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile66 = "rightTreered.png"
            show gram_h3_colorTile66 at Position(xpos = 1490, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h3_colorTile67 = "1_1_red.png"
            show gram_h3_colorTile67 at Position(xpos = 1340, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h3_colorTile68 = "1_1_red.png"
            show gram_h3_colorTile68 at Position(xpos = 1505, xanchor = 0, ypos = 500, yanchor = 0)
            if gramRow2_R_sound_wrong1 ==0:
                $gramRow2_R_sound_wrong1 +=1
                play sound gramTree5
        if (not(letterKin7 and letterHin8)):
            if gramRow2_R_sound_right1 ==1:
                $gramRow2_R_sound_right1 -=1
        if ((not(letterS1in7 or letterS2in7 or letterS3in7 or letterS4in7 or letterS5in7 or letterT1in7 or letterT2in7 or letterT3in7 or letterJin7 or letterKin7 or letterHin7)) or
                (not(letterS1in8 or letterS2in8 or letterS3in8 or letterS4in8 or letterS5in8 or letterT1in8 or letterT2in8 or letterT3in8 or letterJin8 or letterKin8 or letterHin8))):
            if gramRow2_R_sound_wrong1 ==1:
                $gramRow2_R_sound_wrong1 -=1
        
    elif ((letterS1in1 or letterS2in1 or letterS3in1 or letterS4in1 or letterS5in1 or letterT1in1 or letterT2in1 or letterT3in1 or letterJin1 or letterKin1 or letterHin1) and
            (letterS1in2 or letterS2in2 or letterS3in2 or letterS4in2 or letterS5in2 or letterT1in2 or letterT2in2 or letterT3in2 or letterJin2 or letterKin2 or letterHin2) and
            (letterS1in3 or letterS2in3 or letterS3in3 or letterS4in3 or letterS5in3 or letterT1in3 or letterT2in3 or letterT3in3 or letterJin3 or letterKin3 or letterHin3)):
        image gram_h3_colorTile7 = "leftTreeredlong2.png"
        show gram_h3_colorTile7 at Position(xpos = 1055, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h3_colorTile8 = "treeRed.png"
        show gram_h3_colorTile8 at Position(xpos = 1420, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h3_colorTile9 = "rightTreeredlong1.png"
        show gram_h3_colorTile9 at Position(xpos = 1480, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h3_colorTile10 = "1_1_red.png"
        show gram_h3_colorTile10 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h3_colorTile11 = "1_1_red.png"
        show gram_h3_colorTile11 at Position(xpos = 1420, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h3_colorTile12 = "1_1_red.png"
        show gram_h3_colorTile12 at Position(xpos = 1660, xanchor = 0, ypos = 325, yanchor = 0)
        if gramRow1_C_sound_wrong1 ==0:
            play sound gramTree5
            $gramRow1_C_sound_wrong1 +=1
    
    if ((not(letterS1in1 or letterS2in1 or letterS3in1 or letterS4in1 or letterS5in1)) or (not(letterT1in2 or letterT2in2 or letterT3in2)) or
            (not(letterS1in3 or letterS2in3 or letterS3in3 or letterS4in3 or letterS5in3))):
        if gramRow1_C_sound_right1 ==1:
            $gramRow1_C_sound_right1 -=1
    if ((not(letterS1in1 or letterS2in1 or letterS3in1 or letterS4in1 or letterS5in1 or letterT1in1 or letterT2in1 or letterT3in1 or letterJin1 or letterKin1 or letterHin1)) or
            (not(letterS1in2 or letterS2in2 or letterS3in2 or letterS4in2 or letterS5in2 or letterT1in2 or letterT2in2 or letterT3in2 or letterJin2 or letterKin2 or letterHin2)) or
            (not(letterS1in3 or letterS2in3 or letterS3in3 or letterS4in3 or letterS5in3 or letterT1in3 or letterT2in3 or letterT3in3 or letterJin3 or letterKin3 or letterHin3))):
        if gramRow1_C_sound_wrong1 == 1:
            $gramRow1_C_sound_wrong1 -=1
        
    #Win Condition **********************************************************************************************
    if ((letterS1in1 or letterS2in1 or letterS3in1 or letterS4in1 or letterS5in1) and (letterT1in2 or letterT2in2 or letterT3in2) and (letterS1in3 or letterS2in3 or letterS3in3 or letterS4in3 or letterS5in3) and
        (letterS1in4 or letterS2in4 or letterS3in4 or letterS4in4 or letterS5in4) and (letterT1in5 or letterT2in5 or letterT3in5) and (letterS1in6 or letterS2in6 or letterS3in6 or letterS4in6 or letterS5in6) and
        letterKin7 and letterHin8 and (letterS1in9 or letterS2in9 or letterS3in9 or letterS4in9 or letterS5in9) and (letterT1in10 or letterT2in10 or letterT3in10) and letterJin11):
    
        image gram_h3_letterS1 = "letterS.png"
        image gram_h3_letterS2 = "letterS.png"
        image gram_h3_letterS3 = "letterS.png"
        image gram_h3_letterS4 = "letterS.png"
        image gram_h3_letterS5 = "letterS.png"
        image gram_h3_letterT1 = "letterT.png"
        image gram_h3_letterT2 = "letterT.png"
        image gram_h3_letterT3 = "letterT.png"
        image gram_h3_letterJ = "letterJ.png"
        image gram_h3_letterK = "letterK.png"
        image gram_h3_letterH = "letterH.png"
        
        show gram_h3_letterS1 at Position(xpos = letterS1x, xanchor = 0, ypos = letterS1y, yanchor = 0)
        show gram_h3_letterS2 at Position(xpos = letterS2x, xanchor = 0, ypos = letterS2y, yanchor = 0)
        show gram_h3_letterS3 at Position(xpos = letterS3x, xanchor = 0, ypos = letterS3y, yanchor = 0)
        show gram_h3_letterS4 at Position(xpos = letterS4x, xanchor = 0, ypos = letterS4y, yanchor = 0)
        show gram_h3_letterS5 at Position(xpos = letterS5x, xanchor = 0, ypos = letterS5y, yanchor = 0)
        show gram_h3_letterT1 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_h3_letterT2 at Position(xpos = letterT2x, xanchor = 0, ypos = letterT2y, yanchor = 0)
        show gram_h3_letterT3 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
        show gram_h3_letterJ at Position(xpos = letterJx, xanchor = 0, ypos = letterJy, yanchor = 0)
        show gram_h3_letterK at Position(xpos = letterKx, xanchor = 0, ypos = letterKy, yanchor = 0)
        show gram_h3_letterH at Position(xpos = letterHx, xanchor = 0, ypos = letterHy, yanchor = 0)
        queue sound gramWin
        $renpy.pause(0.7)
        $gramHard_solved = True
        jump gramHard_win
    
    #Lose Condition **********************************************************************************************
    if attempts == 0:
        show gram_h3_letterS1 at Position(xpos = letterS1x, xanchor = 0, ypos = letterS1y, yanchor = 0)
        show gram_h3_letterS2 at Position(xpos = letterS2x, xanchor = 0, ypos = letterS2y, yanchor = 0)
        show gram_h3_letterS3 at Position(xpos = letterS3x, xanchor = 0, ypos = letterS3y, yanchor = 0)
        show gram_h3_letterS4 at Position(xpos = letterS4x, xanchor = 0, ypos = letterS4y, yanchor = 0)
        show gram_h3_letterS5 at Position(xpos = letterS5x, xanchor = 0, ypos = letterS5y, yanchor = 0)
        show gram_h3_letterT1 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
        show gram_h3_letterT2 at Position(xpos = letterT2x, xanchor = 0, ypos = letterT2y, yanchor = 0)
        show gram_h3_letterT3 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
        show gram_h3_letterJ at Position(xpos = letterJx, xanchor = 0, ypos = letterJy, yanchor = 0)
        show gram_h3_letterK at Position(xpos = letterKx, xanchor = 0, ypos = letterKy, yanchor = 0)
        show gram_h3_letterH at Position(xpos = letterHx, xanchor = 0, ypos = letterHy, yanchor = 0)
        queue sound gramLose
        $renpy.pause(0.8)
        hide gram_h3_colorTile1
        hide gram_h3_colorTile2
        hide gram_h3_colorTile3
        hide gram_h3_colorTile4
        hide gram_h3_colorTile5
        hide gram_h3_colorTile6
        hide gram_h3_colorTile7
        hide gram_h3_colorTile8
        hide gram_h3_colorTile9
        hide gram_h3_colorTile10
        hide gram_h3_colorTile11
        hide gram_h3_colorTile12
        hide gram_h3_colorTile13
        hide gram_h3_colorTile14
        hide gram_h3_colorTile15
        hide gram_h3_colorTile16
        hide gram_h3_colorTile17
        hide gram_h3_colorTile18
        hide gram_h3_colorTile19
        hide gram_h3_colorTile20
        hide gram_h3_colorTile21
        hide gram_h3_colorTile22
        hide gram_h3_colorTile23
        hide gram_h3_colorTile24
        hide gram_h3_colorTile25
        hide gram_h3_colorTile26
        hide gram_h3_colorTile27
        hide gram_h3_colorTile28
        hide gram_h3_colorTile29
        hide gram_h3_colorTile30
        hide gram_h3_colorTile31
        hide gram_h3_colorTile32
        hide gram_h3_colorTile33
        hide gram_h3_colorTile34
        hide gram_h3_colorTile35
        hide gram_h3_colorTile36
        hide gram_h3_colorTile37
        hide gram_h3_colorTile38
        hide gram_h3_colorTile39
        hide gram_h3_colorTile40
        hide gram_h3_colorTile41
        hide gram_h3_colorTile42
        hide gram_h3_colorTile43
        hide gram_h3_colorTile44
        hide gram_h3_colorTile45
        hide gram_h3_colorTile46
        hide gram_h3_colorTile47
        hide gram_h3_colorTile48
        hide gram_h3_colorTile49
        hide gram_h3_colorTile50
        hide gram_h3_colorTile51
        hide gram_h3_colorTile52
        hide gram_h3_colorTile53
        hide gram_h3_colorTile54
        hide gram_h3_colorTile55
        hide gram_h3_colorTile56
        hide gram_h3_colorTile57
        hide gram_h3_colorTile58
        hide gram_h3_colorTile59
        hide gram_h3_colorTile60
        hide gram_h3_colorTile61
        hide gram_h3_colorTile62
        hide gram_h3_colorTile63
        hide gram_h3_colorTile64
        hide gram_h3_colorTile65
        hide gram_h3_colorTile66
        hide gram_h3_colorTile67
        hide gram_h3_colorTile68
        $gramHard_attempts +=1
        jump gramHard_lose
        
    jump gamefile_h3
    