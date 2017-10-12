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
        return 

init:
    image bg Eng_Tile = "eng_tile_bg.png"

label eng_gram_h5:

    scene bg Eng_Tile

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon

    #row1 1-4
    image gram_h5_instructions = "instructions15.png"
    image gram_h5_baseSlot = "1_1_green.png"
    image gram_h5_baseLetter = "letterS.png"
    show gram_h5_instructions at Position(xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    show gram_h5_baseSlot at Position(xpos = 1250, xanchor = 0, ypos = 150, yanchor = 0)
    show gram_h5_baseLetter at Position(xpos = 1265, xanchor = 0, ypos = 165, yanchor = 0)
    
    #row2 5-8

    image gram_h5_connector1 = "leftTreelong.png"
    image gram_h5_connector2 = "rightTreelong.png"

    show gram_h5_connector1 at Position(xpos = 1130, xanchor = 0, ypos = 250, yanchor = 0)
    show gram_h5_connector2 at Position(xpos = 1320, xanchor = 0, ypos = 250, yanchor = 0)
    
    #row3 9-13   

    image gram_h5_slot1 = "1_1_grey.png"
    image gram_h5_slot2 = "1_1_grey.png"
    

    show gram_h5_slot1 at Position(xpos = 1090, xanchor = 0, ypos = 325, yanchor = 0)
    show gram_h5_slot2 at Position(xpos = 1410, xanchor = 0, ypos = 325, yanchor = 0)

    #row4 14-20

    image gram_h5_connector3 = "leftTreelong.png"
    image gram_h5_connector4 = "treeGrey.png"
    image gram_h5_connector5 = "leftTreelong.png"
    image gram_h5_connector6 = "treeGrey.png"
    image gram_h5_connector7 = "rightTreelong.png"

    show gram_h5_connector3 at Position(xpos = 970, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h5_connector4 at Position(xpos = 1110, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h5_connector5 at Position(xpos = 1285, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h5_connector6 at Position(xpos = 1410, xanchor = 0, ypos = 425, yanchor = 0)
    show gram_h5_connector7 at Position(xpos = 1485, xanchor = 0, ypos = 425, yanchor = 0)


    #row5 21-27

    image gram_h5_slot3 = "1_1_grey.png"
    image gram_h5_slot4 = "1_1_grey.png"
    image gram_h5_slot5 = "1_1_grey.png"
    image gram_h5_slot6 = "1_1_grey.png"
    image gram_h5_slot7 = "1_1_grey.png"

    show gram_h5_slot3 at Position(xpos = 930, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h5_slot4 at Position(xpos = 1110, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h5_slot5 at Position(xpos = 1245, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h5_slot6 at Position(xpos = 1410, xanchor = 0, ypos = 500, yanchor = 0)
    show gram_h5_slot7 at Position(xpos = 1575, xanchor = 0, ypos = 500, yanchor = 0)
    
    
    #row6 28-34

    image gram_h5_connector8 = "leftTree.png"
    image gram_h5_connector9 = "rightTree.png"
    
    show gram_h5_connector8 at Position(xpos = 890, xanchor = 0, ypos = 600, yanchor = 0)
    show gram_h5_connector9 at Position(xpos = 1000, xanchor = 0, ypos = 600, yanchor = 0)
    
    
    #row6 35-41

    image gram_h5_slot8 = "1_1_grey.png"
    image gram_h5_slot9 = "1_1_grey.png"
    
    show gram_h5_slot8 at Position(xpos = 850, xanchor = 0, ypos = 675, yanchor = 0)
    show gram_h5_slot9 at Position(xpos = 1015, xanchor = 0, ypos = 675, yanchor = 0)
    
    image gram_h5_border1 = "letterBorder.png"
    image gram_h5_border2 = "letterBorder.png"
    image gram_h5_border3 = "letterBorder.png"
    image gram_h5_border4 = "letterBorder.png"
    image gram_h5_border5 = "letterBorder.png"
    image gram_h5_border6 = "letterBorder.png"
    
    show gram_h5_border1 at Position(xpos = 262, xanchor = 0, ypos = 582, yanchor = 0)
    show gram_h5_border2 at Position(xpos = 397, xanchor = 0, ypos = 582, yanchor = 0)
    show gram_h5_border3 at Position(xpos = 200, xanchor = 0, ypos = 668, yanchor = 0)
    show gram_h5_border4 at Position(xpos = 460, xanchor = 0, ypos = 668, yanchor = 0)
    show gram_h5_border5 at Position(xpos = 262, xanchor = 0, ypos = 758, yanchor = 0)
    show gram_h5_border6 at Position(xpos = 397, xanchor = 0, ypos = 758, yanchor = 0)
    
    image gram_h5_transparent1 = "letterK_gray.png"
    image gram_h5_transparent2 = "letterR_gray.png"
    image gram_h5_transparent3 = "letterA_gray.png"
    image gram_h5_transparent4 = "letterM_gray.png"
    image gram_h5_transparent5 = "letterJ_gray.png"
    image gram_h5_transparent6 = "letterT_gray.png"
    
    show gram_h5 transparent1 at Position(xpos = 275, xanchor = 0, ypos = 595, yanchor = 0)
    show gram_h5_transparent2 at Position(xpos = 410, xanchor = 0, ypos = 595, yanchor = 0)
    show gram_h5_transparent3 at Position(xpos = 213, xanchor = 0, ypos = 680, yanchor = 0)
    show gram_h5_transparent4 at Position(xpos = 473, xanchor = 0, ypos = 680, yanchor = 0)
    show gram_h5_transparent5 at Position(xpos = 275, xanchor = 0, ypos = 770, yanchor = 0)
    show gram_h5_transparent6 at Position(xpos = 410, xanchor = 0, ypos = 770, yanchor = 0)
    
    $startletterKx = 275
    $startletterKy = 595
    $startletterRx = 410
    $startletterRy = 595
    $startletterAx = 213
    $startletterAy = 680
    $startletterMx = 473
    $startletterMy = 680
    $startletterJx = 275
    $startletterJy = 770
    $startletterTx = 410
    $startletterTy = 770
    
    $letterK1x = startletterKx
    $letterK1y = startletterKy
    $letterK2x = startletterKx
    $letterK2y = startletterKy
    $letterK3x = startletterKx
    $letterK3y = startletterKy
    $letterK4x = startletterKx
    $letterK4y = startletterKy
    $letterRx = startletterRx
    $letterRy = startletterRy
    $letterAx = startletterAx
    $letterAy = startletterAy
    $letterMx = startletterMx
    $letterMy = startletterMy
    $letterJx = startletterJx
    $letterJy = startletterJy
    $letterTx = startletterTx
    $letterTy = startletterTy
    
    # gates
    $ gate1x = 1105 
    $ gate1y = 340
    $ gate2x = 1425
    $ gate2y = 340
    $ gate3x = 945 
    $ gate3y = 515
    $ gate4x = 1125
    $ gate4y = 515
    $ gate5x = 1260
    $ gate5y = 515
    $ gate6x = 1425 
    $ gate6y = 515
    $ gate7x = 1590 
    $ gate7y = 515
    $ gate8x = 865
    $ gate8y = 690
    $ gate9x = 1030 
    $ gate9y = 690
    
 #location conditions
    $letterK1in1 = False
    $letterK1in2 = False
    $letterK1in3 = False
    $letterK1in4 = False
    $letterK1in5 = False
    $letterK1in6 = False
    $letterK1in7 = False
    $letterK1in8 = False
    $letterK1in9 = False
    
    $letterK2in1 = False
    $letterK2in2 = False
    $letterK2in3 = False
    $letterK2in4 = False
    $letterK2in5 = False
    $letterK2in6 = False
    $letterK2in7 = False
    $letterK2in8 = False
    $letterK2in9 = False
    
    $letterK3in1 = False
    $letterK3in2 = False
    $letterK3in3 = False
    $letterK3in4 = False
    $letterK3in5 = False
    $letterK3in6 = False
    $letterK3in7 = False
    $letterK3in8 = False
    $letterK3in9 = False
    
    $letterK4in1 = False
    $letterK4in2 = False
    $letterK4in3 = False
    $letterK4in4 = False
    $letterK4in5 = False
    $letterK4in6 = False
    $letterK4in7 = False
    $letterK4in8 = False
    $letterK4in9 = False
    
    $letterRin1 = False
    $letterRin2 = False
    $letterRin3 = False
    $letterRin4 = False
    $letterRin5 = False
    $letterRin6 = False
    $letterRin7 = False
    $letterRin8 = False
    $letterRin9 = False
    
    $letterAin1 = False
    $letterAin2 = False
    $letterAin3 = False
    $letterAin4 = False
    $letterAin5 = False
    $letterAin6 = False
    $letterAin7 = False
    $letterAin8 = False
    $letterAin9 = False
    
    $letterMin1 = False
    $letterMin2 = False
    $letterMin3 = False
    $letterMin4 = False
    $letterMin5 = False
    $letterMin6 = False
    $letterMin7 = False
    $letterMin8 = False
    $letterMin9 = False
    
    $letterJin1 = False
    $letterJin2 = False
    $letterJin3 = False
    $letterJin4 = False
    $letterJin5 = False
    $letterJin6 = False
    $letterJin7 = False
    $letterJin8 = False
    $letterJin9 = False
    
    $letterTin1 = False
    $letterTin2 = False
    $letterTin3 = False
    $letterTin4 = False
    $letterTin5 = False
    $letterTin6 = False
    $letterTin7 = False
    $letterTin8 = False
    $letterTin9 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #attempts for players
    $ attempts = 20
    
    call gamefile_h5



label gamefile_h5:
    call screen logicGates_hard5

    #First Letter *******************************************************************************************
    if gate_name == "letterK1":
        if slot_name == "gate slot one":
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterK1x = gate1x
            $letterK1y = gate1y
            $letterK1in1 = True
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = False
            
        if slot_name == "gate slot two":
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterK1x = gate2x
            $letterK1y = gate2y
            $letterK1in1 = False
            $letterK1in2 = True
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = False
            
        if slot_name == "gate slot three":
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterK1x = gate3x
            $letterK1y = gate3y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = True
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = False
            
        if slot_name == "gate slot four":
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterK1x = gate4x
            $letterK1y = gate4y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = True
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = False
            
        if slot_name == "gate slot five":
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterK1x = gate5x
            $letterK1y = gate5y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = True
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = False
            
        if slot_name == "gate slot six":
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterK1x = gate6x
            $letterK1y = gate6y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = True
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = False
                        
        if slot_name == "gate slot seven":
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterK1x = gate7x
            $letterK1y = gate7y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = True
            $letterK1in8 = False
            $letterK1in9 = False
            
        if slot_name == "gate slot eight":
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterK1x = gate8x
            $letterK1y = gate8y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = True
            $letterK1in9 = False
            
        if slot_name == "gate slot nine":
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterK1x = gate9x
            $letterK1y = gate9y
            $letterK1in1 = False
            $letterK1in2 = False
            $letterK1in3 = False
            $letterK1in4 = False
            $letterK1in5 = False
            $letterK1in6 = False
            $letterK1in7 = False
            $letterK1in8 = False
            $letterK1in9 = True
    
    #Second Letter *******************************************************************************************
    if gate_name == "letterK2":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterK2x = gate1x
            $letterK2y = gate1y
            $letterK2in1 = True
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterK2x = gate2x
            $letterK2y = gate2y
            $letterK2in1 = False
            $letterK2in2 = True
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterK2x = gate3x
            $letterK2y = gate3y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = True
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterK2x = gate4x
            $letterK2y = gate4y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = True
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterK2x = gate5x
            $letterK2y = gate5y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = True
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterK2x = gate6x
            $letterK2y = gate6y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = True
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterK2x = gate7x
            $letterK2y = gate7y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = True
            $letterK2in8 = False
            $letterK2in9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterK2x = gate8x
            $letterK2y = gate8y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = True
            $letterK2in9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterK2x = gate9x
            $letterK2y = gate9y
            $letterK2in1 = False
            $letterK2in2 = False
            $letterK2in3 = False
            $letterK2in4 = False
            $letterK2in5 = False
            $letterK2in6 = False
            $letterK2in7 = False
            $letterK2in8 = False
            $letterK2in9 = True
    
    #Third Letter *******************************************************************************************
    if gate_name == "letterK3":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterK3x = gate1x
            $letterK3y = gate1y
            $letterK3in1 = True
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterK3x = gate2x
            $letterK3y = gate2y
            $letterK3in1 = False
            $letterK3in2 = True
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterK3x = gate3x
            $letterK3y = gate3y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = True
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterK3x = gate4x
            $letterK3y = gate4y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = True
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterK3x = gate5x
            $letterK3y = gate5y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = True
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterK3x = gate6x
            $letterK3y = gate6y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = True
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterK3x = gate7x
            $letterK3y = gate7y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = True
            $letterK3in8 = False
            $letterK3in9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterK3x = gate8x
            $letterK3y = gate8y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = True
            $letterK3in9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterK3x = gate9x
            $letterK3y = gate9y
            $letterK3in1 = False
            $letterK3in2 = False
            $letterK3in3 = False
            $letterK3in4 = False
            $letterK3in5 = False
            $letterK3in6 = False
            $letterK3in7 = False
            $letterK3in8 = False
            $letterK3in9 = True
    
    #Fourth Letter *******************************************************************************************
    if gate_name == "letterK4":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterK4x = gate1x
            $letterK4y = gate1y
            $letterK4in1 = True
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterK4x = gate2x
            $letterK4y = gate2y
            $letterK4in1 = False
            $letterK4in2 = True
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterK4x = gate3x
            $letterK4y = gate3y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = True
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterK4x = gate4x
            $letterK4y = gate4y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = True
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterK4x = gate5x
            $letterK4y = gate5y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = True
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterK4x = gate6x
            $letterK4y = gate6y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = True
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterK4x = gate7x
            $letterK4y = gate7y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = True
            $letterK4in8 = False
            $letterK4in9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterK4x = gate8x
            $letterK4y = gate8y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = True
            $letterK4in9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterK4x = gate9x
            $letterK4y = gate9y
            $letterK4in1 = False
            $letterK4in2 = False
            $letterK4in3 = False
            $letterK4in4 = False
            $letterK4in5 = False
            $letterK4in6 = False
            $letterK4in7 = False
            $letterK4in8 = False
            $letterK4in9 = True
    
    #Fifth Letter *******************************************************************************************
    if gate_name == "letterR":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterRx = gate1x
            $letterRy = gate1y
            $letterRin1 = True
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterRx = gate2x
            $letterRy = gate2y
            $letterRin1 = False
            $letterRin2 = True
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterRx = gate3x
            $letterRy = gate3y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = True
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterRx = gate4x
            $letterRy = gate4y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = True
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterRx = gate5x
            $letterRy = gate5y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = True
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterRx = gate6x
            $letterRy = gate6y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = True
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterRx = gate7x
            $letterRy = gate7y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = True
            $letterRin8 = False
            $letterRin9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterRx = gate8x
            $letterRy = gate8y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = True
            $letterRin9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterRx = gate9x
            $letterRy = gate9y
            $letterRin1 = False
            $letterRin2 = False
            $letterRin3 = False
            $letterRin4 = False
            $letterRin5 = False
            $letterRin6 = False
            $letterRin7 = False
            $letterRin8 = False
            $letterRin9 = True
    
    #Sixth Letter *******************************************************************************************
    if gate_name == "letterT":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterTx = gate1x
            $letterTy = gate1y
            $letterTin1 = True
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterTx = gate2x
            $letterTy = gate2y
            $letterTin1 = False
            $letterTin2 = True
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterTx = gate3x
            $letterTy = gate3y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = True
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterTx = gate4x
            $letterTy = gate4y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = True
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterTx = gate5x
            $letterTy = gate5y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = True
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterTx = gate6x
            $letterTy = gate6y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = True
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterTx = gate7x
            $letterTy = gate7y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = True
            $letterTin8 = False
            $letterTin9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterTx = gate8x
            $letterTy = gate8y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = True
            $letterTin9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterTx = gate9x
            $letterTy = gate9y
            $letterTin1 = False
            $letterTin2 = False
            $letterTin3 = False
            $letterTin4 = False
            $letterTin5 = False
            $letterTin6 = False
            $letterTin7 = False
            $letterTin8 = False
            $letterTin9 = True
    
    #Seventh Letter *******************************************************************************************
    if gate_name == "letterM":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
            #sets values for checks
            $letterMx = gate1x
            $letterMy = gate1y
            $letterMin1 = True
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
            #sets values for checks
            $letterMx = gate2x
            $letterMy = gate2y
            $letterMin1 = False
            $letterMin2 = True
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
            #sets values for checks
            $letterMx = gate3x
            $letterMy = gate3y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = True
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
            #sets values for checks
            $letterMx = gate4x
            $letterMy = gate4y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = True
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
            #sets values for checks
            $letterMx = gate5x
            $letterMy = gate5y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = True
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
            #sets values for checks
            $letterMx = gate6x
            $letterMy = gate6y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = True
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterMx = gate7x
            $letterMy = gate7y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = True
            $letterMin8 = False
            $letterMin9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
            #sets values for checks
            $letterMx = gate8x
            $letterMy = gate8y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = True
            $letterMin9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
            #sets values for checks
            $letterMx = gate9x
            $letterMy = gate9y
            $letterMin1 = False
            $letterMin2 = False
            $letterMin3 = False
            $letterMin4 = False
            $letterMin5 = False
            $letterMin6 = False
            $letterMin7 = False
            $letterMin8 = False
            $letterMin9 = True
    
    #Eighth Letter *******************************************************************************************
    if gate_name == "letterA":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterJin1 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            #sets values for checks
            $letterAx = gate1x
            $letterAy = gate1y
            $letterAin1 = True
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = False
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterJin2 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            #sets values for checks
            $letterAx = gate2x
            $letterAy = gate2y
            $letterAin1 = False
            $letterAin2 = True
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = False
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterJin3 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            #sets values for checks
            $letterAx = gate3x
            $letterAy = gate3y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = True
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = False
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterJin4 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            #sets values for checks
            $letterAx = gate4x
            $letterAy = gate4y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = True
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = False
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterJin5 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            #sets values for checks
            $letterAx = gate5x
            $letterAy = gate5y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = True
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = False
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterJin6 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            #sets values for checks
            $letterAx = gate6x
            $letterAy = gate6y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = True
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = False
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterJin7 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
            #sets values for checks
            $letterAx = gate7x
            $letterAy = gate7y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = True
            $letterAin8 = False
            $letterAin9 = False
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterJin8 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            #sets values for checks
            $letterAx = gate8x
            $letterAy = gate8y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = True
            $letterAin9 = False
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterJin9 == True:
                $letterJx = startletterJx
                $letterJy = startletterJy
                $letterJin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            #sets values for checks
            $letterAx = gate9x
            $letterAy = gate9y
            $letterAin1 = False
            $letterAin2 = False
            $letterAin3 = False
            $letterAin4 = False
            $letterAin5 = False
            $letterAin6 = False
            $letterAin7 = False
            $letterAin8 = False
            $letterAin9 = True
    
    #Ninth Letter *******************************************************************************************
    if gate_name == "letterJ":
        if slot_name == "gate slot one":
            if letterK1in1 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in1 = False
            if letterK2in1 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in1 = False
            if letterK3in1 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in1 = False
            if letterK4in1 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in1 = False
            if letterRin1 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin1 = False
            if letterTin1 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin1 = False
            if letterMin1 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin1 = False
            if letterAin1 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin1 = False
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
            
        if slot_name == "gate slot two":
            if letterK1in2 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in2 = False
            if letterK2in2 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in2 = False
            if letterK3in2 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in2 = False
            if letterK4in2 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in2 = False
            if letterRin2 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin2 = False
            if letterTin2 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin2 = False
            if letterMin2 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin2 = False
            if letterAin2 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin2 = False
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
            
        if slot_name == "gate slot three":
            if letterK1in3 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in3 = False
            if letterK2in3 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in3 = False
            if letterK3in3 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in3 = False
            if letterK4in3 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in3 = False
            if letterRin3 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin3 = False
            if letterTin3 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin3 = False
            if letterMin3 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin3 = False
            if letterAin3 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin3 = False
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
            
        if slot_name == "gate slot four":
            if letterK1in4 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in4 = False
            if letterK2in4 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in4 = False
            if letterK3in4 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in4 = False
            if letterK4in4 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in4 = False
            if letterRin4 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin4 = False
            if letterTin4 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin4 = False
            if letterMin4 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin4 = False
            if letterAin4 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin4 = False
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
            
        if slot_name == "gate slot five":
            if letterK1in5 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in5 = False
            if letterK2in5 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in5 = False
            if letterK3in5 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in5 = False
            if letterK4in5 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in5 = False
            if letterRin5 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin5 = False
            if letterTin5 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin5 = False
            if letterMin5 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin5 = False
            if letterAin5 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin5 = False
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
            
        if slot_name == "gate slot six":
            if letterK1in6 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in6 = False
            if letterK2in6 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in6 = False
            if letterK3in6 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in6 = False
            if letterK4in6 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in6 = False
            if letterRin6 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin6 = False
            if letterTin6 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin6 = False
            if letterMin6 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin6 = False
            if letterAin6 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin6 = False
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
                        
        if slot_name == "gate slot seven":
            if letterK1in7 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in7 = False
            if letterK2in7 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in7 = False
            if letterK3in7 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in7 = False
            if letterK4in7 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in7 = False
            if letterRin7 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin7 = False
            if letterTin7 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin7 = False
            if letterMin7 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin7 = False
            if letterAin7 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin7 = False
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
            
        if slot_name == "gate slot eight":
            if letterK1in8 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in8 = False
            if letterK2in8 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in8 = False
            if letterK3in8 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in8 = False
            if letterK4in8 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in8 = False
            if letterRin8 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin8 = False
            if letterTin8 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin8 = False
            if letterMin8 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin8 = False
            if letterAin8 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin8 = False
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
            
        if slot_name == "gate slot nine":
            if letterK1in9 == True:
                $letterK1x = startletterKx
                $letterK1y = startletterKy
                $letterK1in9 = False
            if letterK2in9 == True:
                $letterK2x = startletterKx
                $letterK2y = startletterKy
                $letterK2in9 = False
            if letterK3in9 == True:
                $letterK3x = startletterKx
                $letterK3y = startletterKy
                $letterK3in9 = False
            if letterK4in9 == True:
                $letterK4x = startletterKx
                $letterK4y = startletterKy
                $letterK4in9 = False
            if letterRin9 == True:
                $letterRx = startletterRx
                $letterRy = startletterRy
                $letterRin9 = False
            if letterTin9 == True:
                $letterTx = startletterTx
                $letterTy = startletterTy
                $letterTin9 = False
            if letterMin9 == True:
                $letterMx = startletterMx
                $letterMy = startletterMy
                $letterMin9 = False
            if letterAin9 == True:
                $letterAx = startletterAx
                $letterAy = startletterAy
                $letterAin9 = False
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
    
    #Attempts behavior ***************************************************************************************
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "letterK_gate_return" or slot_name == "letterT_gate_return" or slot_name == "letterJ_gate_return" or slot_name == "letterM_gate_return" or slot_name == "letterR_gate_return" or slot_name == "letterA_gate_return")):
       $ temp_slot = slot_name
       $ temp_gate = gate_name
       if temp_slot != "" and temp_gate != "":
           $ attempts -=1
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $attempts -=1
            $temp_slot = slot_name
            $temp_gate = gate_name

        #Dragbacks *******************************************************************************************
            if slot_name == "letterK_gate_return":
                $ attempts +=1
                if gate_name == "letterK1":
                    $ letterK1x = startletterKx
                    $ letterK1y = startletterKy
                    $ letterK1in1 = False
                    $ letterK1in2 = False
                    $ letterK1in3 = False
                    $ letterK1in4 = False
                    $ letterK1in5 = False
                    $ letterK1in6 = False
                    $ letterK1in7 = False
                    $ letterK1in8 = False
                    $ letterK1in9 = False
                if gate_name == "letterK2":
                    $ letterK2x = startletterKx
                    $ letterK2y = startletterKy
                    $ letterK2in1 = False
                    $ letterK2in2 = False
                    $ letterK2in3 = False
                    $ letterK2in4 = False
                    $ letterK2in5 = False
                    $ letterK2in6 = False
                    $ letterK2in7 = False
                    $ letterK2in8 = False
                    $ letterK2in9 = False
                if gate_name == "letterK3":
                    $ letterK3x = startletterKx
                    $ letterK3y = startletterKy
                    $ letterK3in1 = False
                    $ letterK3in2 = False
                    $ letterK3in3 = False
                    $ letterK3in4 = False
                    $ letterK3in5 = False
                    $ letterK3in6 = False
                    $ letterK3in7 = False
                    $ letterK3in8 = False
                    $ letterK3in9 = False
                if gate_name == "letterK4":
                    $ letterK4x = startletterKx
                    $ letterK4y = startletterKy
                    $ letterK4in1 = False
                    $ letterK4in2 = False
                    $ letterK4in3 = False
                    $ letterK4in4 = False
                    $ letterK4in5 = False
                    $ letterK4in6 = False
                    $ letterK4in7 = False
                    $ letterK4in8 = False
                    $ letterK4in9 = False
            if slot_name == "letterT_gate_return":
                $ attempts +=1
                if gate_name == "letterT":
                    $ letterTx = startletterTx
                    $ letterTy = startletterTy
                    $ letterTin1 = False
                    $ letterTin2 = False
                    $ letterTin3 = False
                    $ letterTin4 = False
                    $ letterTin5 = False
                    $ letterTin6 = False
                    $ letterTin7 = False
                    $ letterTin8 = False
                    $ letterTin9 = False
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
            if slot_name == "letterM_gate_return":
                $ attempts +=1
                if gate_name == "letterM":
                    $ letterMx = startletterMx
                    $ letterMy = startletterMy
                    $ letterMin1 = False
                    $ letterMin2 = False
                    $ letterMin3 = False
                    $ letterMin4 = False
                    $ letterMin5 = False
                    $ letterMin6 = False
                    $ letterMin7 = False
                    $ letterMin8 = False
                    $ letterMin9 = False
            if slot_name == "letterR_gate_return":
                $ attempts +=1
                if gate_name == "letterR":
                    $ letterRx = startletterRx
                    $ letterRy = startletterRy
                    $ letterRin1 = False
                    $ letterRin2 = False
                    $ letterRin3 = False
                    $ letterRin4 = False
                    $ letterRin5 = False
                    $ letterRin6 = False
                    $ letterRin7 = False
                    $ letterRin8 = False
                    $ letterRin9 = False
            if slot_name == "letterA_gate_return":
                $ attempts +=1
                if gate_name == "letterA":
                    $ letterAx = startletterAx
                    $ letterAy = startletterAy
                    $ letterAin1 = False
                    $ letterAin2 = False
                    $ letterAin3 = False
                    $ letterAin4 = False
                    $ letterAin5 = False
                    $ letterAin6 = False
                    $ letterAin7 = False
                    $ letterAin8 = False
                    $ letterAin9 = False
    
    #Logic Implementation *********************************************************************
    hide gram_h5_colorTile1
    hide gram_h5_colorTile2
    hide gram_h5_colorTile3
    hide gram_h5_colorTile4
    hide gram_h5_colorTile5
    hide gram_h5_colorTile6
    hide gram_h5_colorTile7
    hide gram_h5_colorTile8
    hide gram_h5_colorTile9
    hide gram_h5_colorTile10
    hide gram_h5_colorTile11
    hide gram_h5_colorTile12
    hide gram_h5_colorTile13
    hide gram_h5_colorTile14
    hide gram_h5_colorTile15
    hide gram_h5_colorTile16
    hide gram_h5_colorTile17
    hide gram_h5_colorTile18
    hide gram_h5_colorTile19
    hide gram_h5_colorTile20
    hide gram_h5_colorTile21
    hide gram_h5_colorTile22
    hide gram_h5_colorTile23
    hide gram_h5_colorTile24
    hide gram_h5_colorTile25
    hide gram_h5_colorTile26
    hide gram_h5_colorTile27
    hide gram_h5_colorTile28
    hide gram_h5_colorTile29
    hide gram_h5_colorTile30
    hide gram_h5_colorTile31
    hide gram_h5_colorTile32
    hide gram_h5_colorTile33
    hide gram_h5_colorTile34
    hide gram_h5_colorTile35
    hide gram_h5_colorTile36
    hide gram_h5_colorTile37
    hide gram_h5_colorTile38
    hide gram_h5_colorTile39
    hide gram_h5_colorTile40
    hide gram_h5_colorTile41
    hide gram_h5_colorTile42
    hide gram_h5_colorTile43
    hide gram_h5_colorTile44
    hide gram_h5_colorTile45
    hide gram_h5_colorTile46
    hide gram_h5_colorTile47
    hide gram_h5_colorTile48
    hide gram_h5_colorTile49
    hide gram_h5_colorTile50
    hide gram_h5_colorTile51
    hide gram_h5_colorTile52
    hide gram_h5_colorTile53
    hide gram_h5_colorTile54
    hide gram_h5_colorTile55
    hide gram_h5_colorTile56
    
    if (letterK1in1 or letterK2in1 or letterK3in1 or letterK4in1) and (letterK1in2 or letterK2in2 or letterK3in2 or letterK4in2):
        image gram_h5_colorTile1 = "leftTreegreenlong.png"
        show gram_h5_colorTile1 at Position(xpos = 1130, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h5_colorTile2 = "rightTreegreenlong.png"
        show gram_h5_colorTile2 at Position(xpos = 1320, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h5_colorTile3 = "1_1_green.png"
        show gram_h5_colorTile3 at Position(xpos = 1090, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h5_colorTile4 = "1_1_green.png"
        show gram_h5_colorTile4 at Position(xpos = 1410, xanchor = 0, ypos = 325, yanchor = 0)
        
        if letterRin3 and letterAin4:
            image gram_h5_colorTile9 = "leftTreegreenlong.png"
            show gram_h5_colorTile9 at Position(xpos = 970, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile10 = "treeGreen.png"
            show gram_h5_colorTile10 at Position(xpos = 1110, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile17 = "solutionLine.png"
            show gram_h5_colorTile17 at Position(xpos = 1110, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h5_colorTile18 = "solutionLine.png"
            show gram_h5_colorTile18 at Position(xpos = 1110, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h5_colorTile19 = "solutionLine.png"
            show gram_h5_colorTile19 at Position(xpos = 1110, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h5_colorTile11 = "1_1_green.png"
            show gram_h5_colorTile11 at Position(xpos = 930, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile12 = "1_1_green.png"
            show gram_h5_colorTile12 at Position(xpos = 1110, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile20 = "down.png"
            show gram_h5_colorTile20 at Position(xpos = 1090, xanchor = 0, ypos = 820, yanchor = 0)
            if letterTin8 and (letterK1in9 or letterK2in9 or letterK3in9 or letterK4in9):
                image gram_h5_colorTile21 = "leftTreegreen.png"
                show gram_h5_colorTile21 at Position(xpos = 890, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h5_colorTile22 = "rightTreegreen.png"
                show gram_h5_colorTile22 at Position(xpos = 1000, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h5_colorTile23 = "solutionLine.png"
                show gram_h5_colorTile23 at Position(xpos = 850, xanchor = 0, ypos = 770, yanchor = 0)
                image gram_h5_colorTile24 = "solutionLine.png"
                show gram_h5_colorTile24 at Position(xpos = 1015, xanchor = 0, ypos = 770, yanchor = 0)
                image gram_h5_colorTile25 = "1_1_green.png"
                show gram_h5_colorTile25 at Position(xpos = 850, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h5_colorTile26 = "1_1_green.png"
                show gram_h5_colorTile26 at Position(xpos = 1015, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h5_colorTile27 = "bow.png"
                show gram_h5_colorTile27 at Position(xpos = 770, xanchor = 0, ypos = 820, yanchor = 0)
                image gram_h5_colorTile28 = "epsilon.png"
                show gram_h5_colorTile28 at Position(xpos = 930, xanchor = 0, ypos = 820, yanchor = 0)
            elif ((letterK1in8 or letterK2in8 or letterK3in8 or letterK4in8 or letterRin8 or letterAin8 or letterMin8 or letterJin8 or letterTin8) and
                    (letterK1in9 or letterK2in9 or letterK3in9 or letterK4in9 or letterRin9 or letterAin9 or letterMin9 or letterJin9 or letterTin9)):
                image gram_h5_colorTile29 = "leftTreered.png"
                show gram_h5_colorTile29 at Position(xpos = 890, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h5_colorTile30 = "rightTreered.png"
                show gram_h5_colorTile30 at Position(xpos = 1000, xanchor = 0, ypos = 600, yanchor = 0)
                image gram_h5_colorTile31 = "1_1_red.png"
                show gram_h5_colorTile31 at Position(xpos = 850, xanchor = 0, ypos = 675, yanchor = 0)
                image gram_h5_colorTile32 = "1_1_red.png"
                show gram_h5_colorTile32 at Position(xpos = 1015, xanchor = 0, ypos = 675, yanchor = 0)
                
        elif ((letterK1in3 or letterK2in3 or letterK3in3 or letterK4in3 or letterRin3 or letterAin3 or letterMin3 or letterJin3 or letterTin3) and
            (letterK1in4 or letterK2in4 or letterK3in4 or letterK4in4 or letterRin4 or letterAin4 or letterMin4 or letterJin4 or letterTin4)):
            image gram_h5_colorTile13 = "leftTreeredlong.png"
            show gram_h5_colorTile13 at Position(xpos = 970, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile14 = "treeRed.png"
            show gram_h5_colorTile14 at Position(xpos = 1110, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile15 = "1_1_red.png"
            show gram_h5_colorTile15 at Position(xpos = 930, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile16 = "1_1_red.png"
            show gram_h5_colorTile16 at Position(xpos = 1110, xanchor = 0, ypos = 500, yanchor = 0)
            
        if (letterK1in5 or letterK2in5 or letterK3in5 or letterK4in5) and letterMin6 and letterJin7:
            image gram_h5_colorTile33 = "leftTreegreenlong.png"
            show gram_h5_colorTile33 at Position(xpos = 1285, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile34 = "treeGreen.png"
            show gram_h5_colorTile34 at Position(xpos = 1410, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile35 = "rightTreegreenlong.png"
            show gram_h5_colorTile35 at Position(xpos = 1485, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile36 = "solutionLine.png"
            show gram_h5_colorTile36 at Position(xpos = 1245, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h5_colorTile37 = "solutionLine.png"
            show gram_h5_colorTile37 at Position(xpos = 1245, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h5_colorTile38 = "solutionLine.png"
            show gram_h5_colorTile38 at Position(xpos = 1245, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h5_colorTile39 = "solutionLine.png"
            show gram_h5_colorTile39 at Position(xpos = 1410, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h5_colorTile40 = "solutionLine.png"
            show gram_h5_colorTile40 at Position(xpos = 1410, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h5_colorTile41 = "solutionLine.png"
            show gram_h5_colorTile41 at Position(xpos = 1410, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h5_colorTile42 = "solutionLine.png"
            show gram_h5_colorTile42 at Position(xpos = 1575, xanchor = 0, ypos = 590, yanchor = 0)
            image gram_h5_colorTile43 = "solutionLine.png"
            show gram_h5_colorTile43 at Position(xpos = 1575, xanchor = 0, ypos = 680, yanchor = 0)
            image gram_h5_colorTile44 = "solutionLine.png"
            show gram_h5_colorTile44 at Position(xpos = 1575, xanchor = 0, ypos = 770, yanchor = 0)
            image gram_h5_colorTile45 = "1_1_green.png"
            show gram_h5_colorTile45 at Position(xpos = 1245, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile46 = "1_1_green.png"
            show gram_h5_colorTile46 at Position(xpos = 1410, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile47 = "1_1_green.png"
            show gram_h5_colorTile47 at Position(xpos = 1575, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile48 = "epsilon.png"
            show gram_h5_colorTile48 at Position(xpos = 1250, xanchor = 0, ypos = 820, yanchor = 0)
            image gram_h5_colorTile49 = "to.png"
            show gram_h5_colorTile49 at Position(xpos = 1410, xanchor = 0, ypos = 820, yanchor = 0)
            image gram_h5_colorTile50 = "blue.png"
            show gram_h5_colorTile50 at Position(xpos = 1570, xanchor = 0, ypos = 820, yanchor = 0)
        elif ((letterK1in5 or letterK2in5 or letterK3in5 or letterK4in5 or letterRin5 or letterAin5 or letterMin5 or letterJin5 or letterTin5) and
                (letterK1in6 or letterK2in6 or letterK3in6 or letterK4in6 or letterRin6 or letterAin6 or letterMin6 or letterJin6 or letterTin6) and
                (letterK1in7 or letterK2in7 or letterK3in7 or letterK4in7 or letterRin7 or letterAin7 or letterMin7 or letterJin7 or letterTin7)):
            image gram_h5_colorTile51 = "leftTreeredlong.png"
            show gram_h5_colorTile51 at Position(xpos = 1285, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile52 = "treeRed.png"
            show gram_h5_colorTile52 at Position(xpos = 1410, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile53 = "rightTreeredlong.png"
            show gram_h5_colorTile53 at Position(xpos = 1485, xanchor = 0, ypos = 425, yanchor = 0)
            image gram_h5_colorTile54 = "1_1_red.png"
            show gram_h5_colorTile54 at Position(xpos = 1245, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile55 = "1_1_red.png"
            show gram_h5_colorTile55 at Position(xpos = 1410, xanchor = 0, ypos = 500, yanchor = 0)
            image gram_h5_colorTile56 = "1_1_red.png"
            show gram_h5_colorTile56 at Position(xpos = 1575, xanchor = 0, ypos = 500, yanchor = 0)
            
    elif ((letterK1in1 or letterK2in1 or letterK3in1 or letterK4in1 or letterRin1 or letterAin1 or letterMin1 or letterJin1 or letterTin1) and
            (letterK1in2 or letterK2in2 or letterK3in2 or letterK4in2 or letterRin2 or letterAin2 or letterMin2 or letterJin2 or letterTin2)):
        image gram_h5_colorTile5 = "leftTreeredlong.png"
        show gram_h5_colorTile5 at Position(xpos = 1130, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h5_colorTile6 = "rightTreeredlong.png"
        show gram_h5_colorTile6 at Position(xpos = 1320, xanchor = 0, ypos = 250, yanchor = 0)
        image gram_h5_colorTile7 = "1_1_red.png"
        show gram_h5_colorTile7 at Position(xpos = 1090, xanchor = 0, ypos = 325, yanchor = 0)
        image gram_h5_colorTile8 = "1_1_red.png"
        show gram_h5_colorTile8 at Position(xpos = 1410, xanchor = 0, ypos = 325, yanchor = 0)     
        
        
    #Win Condition ************************************************************************************
    if ((letterK1in1 or letterK2in1 or letterK3in1 or letterK4in1) and (letterK1in2 or letterK2in2 or letterK3in2 or letterK4in2) and letterRin3 and
            letterAin4 and (letterK1in5 or letterK2in5 or letterK3in5 or letterK4in5) and letterMin6 and letterJin7 and letterTin8 and
            (letterK1in9 or letterK2in9 or letterK3in9 or letterK4in9)):
        image gram_h3_letterK1 = "letterK.png"
        show gram_h3_letterK1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        image gram_h3_letterK2 = "letterK.png"
        show gram_h3_letterK2 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        image gram_h3_letterK3 = "letterK.png"
        show gram_h3_letterK3 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        image gram_h3_letterK4 = "letterK.png"
        show gram_h3_letterK4 at Position(xpos = gate9x, xanchor = 0, ypos = gate9y, yanchor = 0)
        image gram_h3_letterR = "letterR.png"
        show gram_h3_letterR at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        image gram_h3_letterA = "letterA.png"
        show gram_h3_letterA at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        image gram_h3_letterM = "letterM.png"
        show gram_h3_letterM at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        image gram_h3_letterJ = "letterJ.png"
        show gram_h3_letterJ at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        image gram_h3_letterT = "letterT.png"
        show gram_h3_letterT at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        
        "Access Gained"
        
        jump eng_gram_h5 #enggram_h5
        
    #Lose Condition ***********************************************************************************
    if attempts == 0:
        hide gram_h5_colorTile1
        hide gram_h5_colorTile2
        hide gram_h5_colorTile3
        hide gram_h5_colorTile4
        hide gram_h5_colorTile5
        hide gram_h5_colorTile6
        hide gram_h5_colorTile7
        hide gram_h5_colorTile8
        hide gram_h5_colorTile9
        hide gram_h5_colorTile10
        hide gram_h5_colorTile11
        hide gram_h5_colorTile12
        hide gram_h5_colorTile13
        hide gram_h5_colorTile14
        hide gram_h5_colorTile15
        hide gram_h5_colorTile16
        hide gram_h5_colorTile17
        hide gram_h5_colorTile18
        hide gram_h5_colorTile19
        hide gram_h5_colorTile20
        hide gram_h5_colorTile21
        hide gram_h5_colorTile22
        hide gram_h5_colorTile23
        hide gram_h5_colorTile24
        hide gram_h5_colorTile25
        hide gram_h5_colorTile26
        hide gram_h5_colorTile27
        hide gram_h5_colorTile28
        hide gram_h5_colorTile29
        hide gram_h5_colorTile30
        hide gram_h5_colorTile31
        hide gram_h5_colorTile32
        hide gram_h5_colorTile33
        hide gram_h5_colorTile34
        hide gram_h5_colorTile35
        hide gram_h5_colorTile36
        hide gram_h5_colorTile37
        hide gram_h5_colorTile38
        hide gram_h5_colorTile39
        hide gram_h5_colorTile40
        hide gram_h5_colorTile41
        hide gram_h5_colorTile42
        hide gram_h5_colorTile43
        hide gram_h5_colorTile44
        hide gram_h5_colorTile45
        hide gram_h5_colorTile46
        hide gram_h5_colorTile47
        hide gram_h5_colorTile48
        hide gram_h5_colorTile49
        hide gram_h5_colorTile50
        hide gram_h5_colorTile51
        hide gram_h5_colorTile52
        hide gram_h5_colorTile53
        hide gram_h5_colorTile54
        hide gram_h5_colorTile55
        hide gram_h5_colorTile56
    
        show gram_h3_letterK1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        show gram_h3_letterK2 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        show gram_h3_letterK3 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        show gram_h3_letterK4 at Position(xpos = gate9x, xanchor = 0, ypos = gate9y, yanchor = 0)
        show gram_h3_letterR at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        show gram_h3_letterA at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        show gram_h3_letterM at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        show gram_h3_letterJ at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        show gram_h3_letterT at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        
        "You Lose. Try Again."
        
        jump eng_gram_h5
        
    jump gamefile_h5


screen logicGates_hard5:
    draggroup:
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
                drag_name "letterK3"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK3x ypos letterK3y
        drag:
                drag_name "letterK4"
                child "letterK.png"
                droppable False
                dragged gate_dragged
                xpos letterK4x ypos letterK4y
        drag:
                drag_name "letterR"
                child "letterR.png"
                droppable False
                dragged gate_dragged
                xpos letterRx ypos letterRy
        drag:
                drag_name "letterA"
                child "letterA.png"
                droppable False
                dragged gate_dragged
                xpos letterAx ypos letterAy
        drag:
                drag_name "letterM"
                child "letterM.png"
                droppable False
                dragged gate_dragged
                xpos letterMx ypos letterMy
        drag:
                drag_name "letterJ"
                child "letterJ.png"
                droppable False
                dragged gate_dragged
                xpos letterJx ypos letterJy
        drag:
                drag_name "letterT"
                child "letterT.png"
                droppable False
                dragged gate_dragged
                xpos letterTx ypos letterTy
        
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

        #Gate Slots ******************************************************************************
        drag:
                drag_name "letterK_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 582

        drag:
                drag_name "letterR_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 582
                
        drag:
                drag_name "letterA_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 200 ypos 668

        drag:
                drag_name "letterM_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 460 ypos 668

        drag:
                drag_name "letterJ_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 262 ypos 758
        drag:
                drag_name "letterT_gate_return"
                child "letterBorder.png"
                draggable False
                xpos 397 ypos 758