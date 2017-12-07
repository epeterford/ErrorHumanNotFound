init python:

    #makes it so the game doesn't stop early
    def gate_dragged(drags,drop):
        if not drop:
            store.gate_name = drags[0].drag_name
            store.slot_name = "null"
            return True
        #checks to see the drop location and makes it snap        
        if drop:
            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop 
                #this store the values for the if checks
                store.gate_name = drags[0].drag_name
                store.slot_name = drop.drag_name

            return True
        return True

init:
    image bg Logic_Gate = "LOGIC_GATE_BG.png"

label logicGate_hardC1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    image HC1tile00_03 = "g_elbow_br.png"
    image HC1tile00_04 = "g_elbow_bl.png"
    
    show HC1tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
    show HC1tile00_04 at Position(xpos = 736, xanchor = 0, ypos = 233, yanchor = 0)
   
    image HC1tile01_00 = "g_horizontal.png"
    image HC1tile01_01 = "g_elbow_bl.png"
    image HC1tile01_03 = "g_vertical.png"
    image HC1tile01_04 = "g_r.png"
    image HC1tile01_05 = "NONE_Gate.png"
    image HC1tile01_06 = "y_horizontal.png"
    image HC1tile01_07 = "y_elbow_bl.png"
    
    show HC1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HC1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show HC1tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show HC1tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show HC1tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show HC1tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show HC1tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    
    image HC1tile02_01 = "g_r.png"
    image HC1tile02_02 = "XOR_Gate_blue.png"
    image HC1tile02_03 = "g_elbow_tl.png"
    image HC1tile02_04 = "r_vertical.png"
    image HC1tile02_07 = "y_vertical.png"
    
    show HC1tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show HC1tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show HC1tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HC1tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show HC1tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HC1tile03_00 = "r_horizontal.png"
    image HC1tile03_01 = "r_t_up.png"
    image HC1tile03_02 = "r_horizontal.png"
    image HC1tile03_03 = "r_horizontal.png"
    image HC1tile03_04 = "r_t_left.png"
    image HC1tile03_07 = "y_y.png"
    image HC1tile03_08 = "OR_Gate_blue.png"
    image HC1tile03_09 = "y_horizontal.png"
    image HC1tile03_10 = "y_horizontal.png"
    image HC1tile03_11 = "y_elbow_bl.png"
    
    show HC1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show HC1tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    image HC1tile04_04 = "r_vertical.png"
    image HC1tile04_07 = "y_vertical.png"
    image HC1tile04_11 = "y_vertical.png"
    
    show HC1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HC1tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show HC1tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HC1tile05_00 = "g_horizontal.png"
    image HC1tile05_01 = "g_elbow_bl.png"
    image HC1tile05_04 = "r_y.png"
    image HC1tile05_05 = "NONE_Gate.png"
    image HC1tile05_06 = "y_horizontal.png"
    image HC1tile05_07 = "y_t_up.png"
    image HC1tile05_08 = "y_elbow_bl.png"
    image HC1tile05_11 = "y_y.png"
    image HC1tile05_12 = "NOR_Gate_blue.png"
    image HC1tile05_13 = "y_horizontal.png"
    
    show HC1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show HC1tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    image HC1tile06_01 = "g_g.png"
    image HC1tile06_02 = "NONE_Gate.png"
    image HC1tile06_03 = "y_horizontal.png"
    image HC1tile06_04 = "y_t_up.png"
    image HC1tile06_05 = "y_horizontal.png"
    image HC1tile06_06 = "y_elbow_bl.png"
    image HC1tile06_08 = "y_vertical.png"
    image HC1tile06_11 = "y_vertical.png"
    
    show HC1tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show HC1tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HC1tile07_00 = "g_horizontal.png"
    image HC1tile07_01 = "g_elbow_tl.png"
    image HC1tile07_06 = "y_vertical.png"
    image HC1tile07_08 = "y_y.png"
    image HC1tile07_09 = "NONE_Gate.png"
    image HC1tile07_10 = "y_horizontal.png"
    image HC1tile07_11 = "y_elbow_tl.png"
    
    show HC1tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HC1tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show HC1tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
    show HC1tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show HC1tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show HC1tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show HC1tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    
    image HC1tile08_06 = "y_elbow_tr.png"
    image HC1tile08_07 = "y_horizontal.png"
    image HC1tile08_08 = "y_elbow_tl.png"
    
    show HC1tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show HC1tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show HC1tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    


    #start points
    image HC1start1 = "light_g_on.png"
    show HC1start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HC1start2 = "light_r_on.png"
    show HC1start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HC1start3 = "light_g_on.png"
    show HC1start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HC1start4 = "light_g_on.png"
    show HC1start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these

    image HC1end3 = "light_g_off.png"
    show HC1end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)


    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""
    $ gate_name = ""
    $ slot_name = ""

    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ nor1x = 1148
    $ nor1y = 88
    $ xor1x = 1299
    $ xor1y = 88
    $ nand1x = 998
    $ nand1y = 88
    
    #gate values
    $ gate1x = 811
    $ gate1y = 308
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 811
    $ gate3y = 608
    $ gate4x = 1111
    $ gate4y = 758
    
    # check conditons for locations
    $ and1in1 = False
    $ nor1in1 = False
    $ xor1in1 = False
    $ nand1in1 = False
    $ and1in2 = False
    $ nor1in2 = False
    $ xor1in2 = False
    $ nand1in2 = False
    $ and1in3 = False
    $ nor1in3 = False
    $ xor1in3 = False
    $ nand1in3 = False
    $ and1in4 = False
    $ nor1in4 = False
    $ xor1in4 = False
    $ nand1in4 = False   
    
    #attempts for players
    $ attempts = 6
 
    jump gamefileHC1
    
    
label gamefileHC1:
    
    #calls game screen
    call screen logicgatesHC1
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False
                
            #sets values for checks
            $ and1x = gate1x
            $ and1y = gate1y
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False
                
            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = False
            
        #gate slot number three*******************************        
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
                
            #sets values for checks
            $ and1x = gate3x
            $ and1y = gate3y
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = True
            $ and1in4 = False
            
        if slot_name == "gate slot four":
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
                
            #sets values for checks
            $ and1x = gate4x
            $ and1y = gate4y
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = True
            
        if slot_name == "and return":
            $ and1x = 698
            $ and1y = 88
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = False
            
     #or gate section **********************************************************************       
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False
                
            #sets values for checks
            $ nor1x = gate1x
            $ nor1y = gate1y
            $ nor1in1 = True
            $ nor1in2 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False
                
            #sets values for checks
            $ nor1x = gate2x
            $ nor1y = gate2y
            $ nor1in2 = True
            $ nor1in1 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
                
            #sets values for checks
            $ nor1x = gate3x
            $ nor1y = gate3y
            $ nor1in2 = False
            $ nor1in1 = False
            $ nor1in3 = True
            $ nor1in4 = False
            
        if slot_name == "gate slot four":
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
                
            #sets values for checks
            $ nor1x = gate4x
            $ nor1y = gate4y
            $ nor1in2 = False
            $ nor1in1 = False
            $ nor1in3 = False
            $ nor1in4 = True
            
        if slot_name == "nor return":
            $ nor1x = 1148
            $ nor1y = 88
            $ nor1in2 = False
            $ nor1in1 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
     #nand gate section **********************************************************************       
    if gate_name == "xor_gate1":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in1 = False
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False                

            #sets values for checks
            $ xor1x = gate1x
            $ xor1y = gate1y
            $ xor1in1 = True
            $ xor1in2 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False  
                
            #sets values for checks
            $ xor1x = gate2x
            $ xor1y = gate2y
            $ xor1in2 = True
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
                
            #sets values for checks
            $ xor1x = gate3x
            $ xor1y = gate3y
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = True
            $ xor1in4 = False
            
        if slot_name == "gate slot four":
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False  
                
            #sets values for checks
            $ xor1x = gate4x
            $ xor1y = gate4y
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = True
        
        if slot_name == "xor return":
            $ xor1x = 1299
            $ xor1y = 88
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False

    if gate_name == "nand_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in1 = False
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False                

            #sets values for checks
            $ nand1x = gate1x
            $ nand1y = gate1y
            $ nand1in1 = True
            $ nand1in2 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False  
                
            #sets values for checks
            $ nand1x = gate2x
            $ nand1y = gate2y
            $ nand1in2 = True
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
                
            #sets values for checks
            $ nand1x = gate3x
            $ nand1y = gate3y
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = True
            $ nand1in4 = False
            
        if slot_name == "gate slot four":
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False  
                
            #sets values for checks
            $ nand1x = gate4x
            $ nand1y = gate4y
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = True
        
        if slot_name == "nand return":
            $ nand1x = 998
            $ nand1y = 88
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "and return" or slot_name == "nor return" or slot_name == "xor return" or slot_name == "nand return"):
       $ temp_slot = slot_name
       $ temp_gate = gate_name
       if temp_slot != "" and temp_gate != "":
           $ attempts -=1

       
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            if slot_name == "and return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
                
            if slot_name == "nor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "xor_gate1":
                $ attempts +=1  
            if slot_name == "nor return" and gate_name == "nand_gate":
                $ attempts +=1    
                
            if slot_name == "and return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "nand_gate":
                $ attempts +=1
                
            if slot_name == "xor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nand_gate":
                $ attempts +=1
                
            if slot_name == "nand return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "and_gate":
                $ attempts +=1

#*******************************************
#************image zone********************* 
#*******************************************
    
    $lgNormal = renpy.random.randint(0,2)
    if (lgNormal==0):
        play sound pipeFlowR
    if (lgNormal==1):
        play sound pipeFlowG
    if (lgNormal==2):
        play sound pipeFlowN
        
    if and1in1 or nor1in1:
        image HC11tile01_06 = "r_horizontal.png"
        image HC11tile01_07 = "r_elbow_bl.png"
        show HC11tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show HC11tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        image HC11tile02_07 = "r_vertical.png"
        show HC11tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        image HC11tile03_07 = "r_y.png"
        show HC11tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    
    else:
        hide HC11tile01_06
        hide HC11tile01_07
        hide HC11tile02_07
        hide HC11tile03_07
        
    if nand1in1 or xor1in1:
        image HC12tile01_06 = "g_horizontal.png"
        image HC12tile01_07 = "g_elbow_bl.png"
        show HC12tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show HC12tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        image HC12tile02_07 = "g_vertical.png"
        show HC12tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        image HC12tile03_07 = "g_y.png"
        show HC12tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    
    else:
        hide HC12tile01_06
        hide HC12tile01_07
        hide HC12tile02_07
        hide HC12tile03_07
        
    if and1in2 == True:
        image HC15tile08_06 = "g_elbow_tr.png"
        image HC15tile08_07 = "g_horizontal.png"
        image HC15tile08_08 = "g_elbow_tl.png"
        show HC15tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show HC15tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HC15tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        image HC15tile07_06 = "g_vertical.png"
        image HC15tile07_08 = "y_g.png"
        show HC15tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        show HC15tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image HC15tile06_03 = "g_horizontal.png"
        image HC15tile06_04 = "g_t_up.png"
        image HC15tile06_05 = "g_horizontal.png"
        image HC15tile06_06 = "g_elbow_bl.png"
        show HC15tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC15tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC15tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show HC15tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        image HC15tile05_04 = "r_g.png"
        show HC15tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        if nand1in3 == True:
            image HC110tile03_07 = "y_g.png"
            show HC110tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC110tile04_07 = "g_vertical.png"  
            show HC110tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC110tile05_06 = "g_horizontal.png"
            image HC110tile05_07 = "g_t_up.png"
            image HC110tile05_08 = "g_elbow_bl.png"
            show HC110tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC110tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC110tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC110tile06_08 = "g_vertical.png"
            show HC110tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC110tile07_08 = "g_g.png"
            show HC110tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if nor1in4 == True:
                image HC11199tile06_11 = "r_vertical.png"
                show HC11199tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC11199tile07_10 = "r_horizontal.png"
                image HC11199tile07_11 = "r_elbow_tl.png"
                show HC11199tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC11199tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC11199tile05_11 = "y_r.png"
                show HC11199tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC11199tile06_11
                hide HC11199tile07_10
                hide HC11199tile07_11
                hide HC11199tile05_11        
                
                
            if xor1in4 == True:
                image HC111tile06_11 = "r_vertical.png"
                show HC111tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC111tile07_10 = "r_horizontal.png"
                image HC111tile07_11 = "r_elbow_tl.png"
                show HC111tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC111tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC111tile05_11 = "y_r.png"
                show HC111tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC111tile06_11
                hide HC111tile07_10
                hide HC111tile07_11
                hide HC111tile05_11      
            
        else:
            hide HC110tile03_07
            hide HC110tile04_07
            hide HC110tile05_06
            hide HC110tile05_07
            hide HC110tile05_08
            hide HC110tile06_08
            hide HC110tile07_08
            hide HC11199tile06_11
            hide HC11199tile07_10
            hide HC11199tile07_11
            hide HC11199tile05_11         
            hide HC111tile06_11
            hide HC111tile07_10
            hide HC111tile07_11
            hide HC111tile05_11   
        if nor1in3 == True:
            image HC114tile03_07 = "y_r.png"
            show HC114tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC114tile04_07 = "r_vertical.png"  
            show HC114tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC114tile05_06 = "r_horizontal.png"
            image HC114tile05_07 = "r_t_up.png"
            image HC114tile05_08 = "r_elbow_bl.png"
            show HC114tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC114tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC114tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC114tile06_08 = "r_vertical.png"
            show HC114tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC114tile07_08 = "r_g.png"
            show HC114tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if nand1in4 == True:
                image HC112tile06_11 = "g_vertical.png"
                show HC112tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC112tile07_10 = "g_horizontal.png"
                image HC112tile07_11 = "g_elbow_tl.png"
                show HC112tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC112tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC112tile05_11 = "y_g.png"
                show HC112tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC112tile06_11
                hide HC112tile07_10
                hide HC112tile07_11
                hide HC112tile05_11    
                
                
            if xor1in4 == True:
                image HC113tile06_11 = "g_vertical.png"
                show HC113tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC113tile07_10 = "g_horizontal.png"
                image HC113tile07_11 = "g_elbow_tl.png"
                show HC113tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC113tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC113tile05_11 = "y_g.png"
                show HC113tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC113tile06_11
                hide HC113tile07_10
                hide HC113tile07_11
                hide HC113tile05_11      
            
        else:
            hide HC114tile03_07
            hide HC114tile04_07
            hide HC114tile05_06
            hide HC114tile05_07
            hide HC114tile05_08
            hide HC114tile06_08
            hide HC114tile07_08
            hide HC113tile06_11
            hide HC113tile07_10
            hide HC113tile07_11
            hide HC113tile05_11      
            hide HC112tile06_11
            hide HC112tile07_10
            hide HC112tile07_11
            hide HC112tile05_11 
        if xor1in3 == True:
            image HC117tile03_07 = "y_g.png"
            show HC117tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC117tile04_07 = "g_vertical.png"  
            show HC117tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC117tile05_06 = "g_horizontal.png"
            image HC117tile05_07 = "g_t_up.png"
            image HC117tile05_08 = "g_elbow_bl.png"
            show HC117tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC117tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC117tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC117tile06_08 = "g_vertical.png"
            show HC117tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC117tile07_08 = "g_g.png"
            show HC117tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
                        
            if nand1in4 == True:
                image HC115tile06_11 = "r_vertical.png"
                show HC115tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC115tile07_10 = "r_horizontal.png"
                image HC115tile07_11 = "r_elbow_tl.png"
                show HC115tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC115tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC115tile05_11 = "y_r.png"
                show HC115tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC115tile06_11
                hide HC115tile07_10
                hide HC115tile07_11
                hide HC115tile05_11        
            if nor1in4 == True:
                image HC116tile06_11 = "r_vertical.png"
                show HC116tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC116tile07_10 = "r_horizontal.png"
                image HC116tile07_11 = "r_elbow_tl.png"
                show HC116tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC116tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC116tile05_11 = "y_r.png"
                show HC116tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC116tile06_11
                hide HC116tile07_10
                hide HC116tile07_11
                hide HC116tile05_11    
                
        else:
            hide HC117tile03_07
            hide HC117tile04_07
            hide HC117tile05_06
            hide HC117tile05_07
            hide HC117tile05_08
            hide HC117tile06_08
            hide HC117tile07_08  
            hide HC116tile06_11
            hide HC116tile07_10
            hide HC116tile07_11
            hide HC116tile05_11    
            hide HC115tile06_11
            hide HC115tile07_10
            hide HC115tile07_11
            hide HC115tile05_11 
    else:
        hide HC15tile08_06
        hide HC15tile08_07
        hide HC15tile08_08
        hide HC15tile07_06
        hide HC15tile07_08
        hide HC15tile06_03
        hide HC15tile06_04
        hide HC15tile06_05
        hide HC15tile06_06
        hide HC15tile05_04
        hide HC110tile03_07
        hide HC110tile04_07
        hide HC110tile05_06
        hide HC110tile05_07
        hide HC110tile05_08
        hide HC110tile06_08
        hide HC110tile07_08
        hide HC11199tile06_11
        hide HC11199tile07_10
        hide HC11199tile07_11
        hide HC11199tile05_11         
        hide HC111tile06_11
        hide HC111tile07_10
        hide HC111tile07_11
        hide HC111tile05_11  
        hide HC114tile03_07
        hide HC114tile04_07
        hide HC114tile05_06
        hide HC114tile05_07
        hide HC114tile05_08
        hide HC114tile06_08
        hide HC114tile07_08
        hide HC113tile06_11
        hide HC113tile07_10
        hide HC113tile07_11
        hide HC113tile05_11      
        hide HC112tile06_11
        hide HC112tile07_10
        hide HC112tile07_11
        hide HC112tile05_11 
        hide HC117tile03_07
        hide HC117tile04_07
        hide HC117tile05_06
        hide HC117tile05_07
        hide HC117tile05_08
        hide HC117tile06_08
        hide HC117tile07_08  
        hide HC116tile06_11
        hide HC116tile07_10
        hide HC116tile07_11
        hide HC116tile05_11    
        hide HC115tile06_11
        hide HC115tile07_10
        hide HC115tile07_11
        hide HC115tile05_11 
            
            
    if nand1in2 == True:
        image HC16tile08_06 = "r_elbow_tr.png"
        image HC16tile08_07 = "r_horizontal.png"
        image HC16tile08_08 = "r_elbow_tl.png"
        show HC16tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show HC16tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HC16tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        image HC16tile07_06 = "r_vertical.png"
        image HC16tile07_08 = "y_r.png"
        show HC16tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        show HC16tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image HC16tile06_03 = "r_horizontal.png"
        image HC16tile06_04 = "r_t_up.png"
        image HC16tile06_05 = "r_horizontal.png"
        image HC16tile06_06 = "r_elbow_bl.png"
        show HC16tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC16tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC16tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show HC16tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        image HC16tile05_04 = "r_r.png"
        show HC16tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        
        if and1in3 == True:
            image HC120tile03_07 = "y_r.png"
            show HC120tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC120tile04_07 = "r_vertical.png"  
            show HC120tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC120tile05_06 = "r_horizontal.png"
            image HC120tile05_07 = "r_t_up.png"
            image HC120tile05_08 = "r_elbow_bl.png"
            show HC120tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC120tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC120tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC120tile06_08 = "r_vertical.png"
            show HC120tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC120tile07_08 = "r_r.png"
            show HC120tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
                   
            
            if nor1in4 == True:
                image HC118tile06_11 = "g_vertical.png"
                show HC118tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC118tile07_10 = "g_horizontal.png"
                image HC118tile07_11 = "g_elbow_tl.png"
                show HC118tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC118tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC118tile05_11 = "y_g.png"
                show HC118tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC118tile06_11
                hide HC118tile07_10
                hide HC118tile07_11
                hide HC118tile05_11        
                
                
            if xor1in4 == True:
                image HC119tile06_11 = "r_vertical.png"
                show HC119tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC119tile07_10 = "r_horizontal.png"
                image HC119tile07_11 = "r_elbow_tl.png"
                show HC119tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC119tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC119tile05_11 = "r_r.png"
                show HC119tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC119tile06_11
                hide HC119tile07_10
                hide HC119tile07_11
                hide HC119tile05_11      
            
        else:
            hide HC120tile03_07
            hide HC120tile04_07
            hide HC120tile05_06
            hide HC120tile05_07
            hide HC120tile05_08
            hide HC120tile06_08
            hide HC120tile07_08
            hide HC118tile06_11
            hide HC118tile07_10
            hide HC118tile07_11
            hide HC118tile05_11        
            hide HC119tile06_11
            hide HC119tile07_10
            hide HC119tile07_11
            hide HC119tile05_11  
                
        if nor1in3 == True:
            image HC123tile03_07 = "y_g.png"
            show HC123tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC123tile04_07 = "g_vertical.png"  
            show HC123tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC123tile05_06 = "g_horizontal.png"
            image HC123tile05_07 = "g_t_up.png"
            image HC123tile05_08 = "g_elbow_bl.png"
            show HC123tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC123tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC123tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC123tile06_08 = "g_vertical.png"
            show HC123tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC123tile07_08 = "g_r.png"
            show HC123tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            
            if and1in4 == True:
                image HC121tile06_11 = "r_vertical.png"
                show HC121tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC121tile07_10 = "r_horizontal.png"
                image HC121tile07_11 = "r_elbow_tl.png"
                show HC121tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC121tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC121tile05_11 = "y_r.png"
                show HC121tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC121tile06_11
                hide HC121tile07_10
                hide HC121tile07_11
                hide HC121tile05_11
                
                
            if xor1in4 == True:
                image HC122tile06_11 = "g_vertical.png"
                show HC122tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC122tile07_10 = "g_horizontal.png"
                image HC122tile07_11 = "g_elbow_tl.png"
                show HC122tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC122tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC122tile05_11 = "y_g.png"
                show HC122tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC122tile06_11
                hide HC122tile07_10
                hide HC122tile07_11
                hide HC122tile05_11      
            
            
        else:
            hide HC123tile03_07
            hide HC123tile04_07
            hide HC123tile05_06
            hide HC123tile05_07
            hide HC123tile05_08
            hide HC123tile06_08
            hide HC123tile07_08
            hide HC121tile06_11
            hide HC121tile07_10
            hide HC121tile07_11
            hide HC121tile05_11
            hide HC122tile06_11
            hide HC122tile07_10
            hide HC122tile07_11
            hide HC122tile05_11 
            
        if xor1in3 == True:
            image HC126tile03_07 = "y_r.png"
            show HC126tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC126tile04_07 = "r_vertical.png"  
            show HC126tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC126tile05_06 = "r_horizontal.png"
            image HC126tile05_07 = "r_t_up.png"
            image HC126tile05_08 = "r_elbow_bl.png"
            show HC126tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC126tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC126tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC126tile06_08 = "r_vertical.png"
            show HC126tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC126tile07_08 = "r_r.png"
            show HC126tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            
            
            if and1in4 == True:
                image HC124tile06_11 = "r_vertical.png"
                show HC124tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC124tile07_10 = "r_horizontal.png"
                image HC124tile07_11 = "r_elbow_tl.png"
                show HC124tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC124tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC124tile05_11 = "y_r.png"
                show HC124tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC124tile06_11
                hide HC124tile07_10
                hide HC124tile07_11
                hide HC124tile05_11

                
            if nor1in4 == True:
                image HC125tile06_11 = "g_vertical.png"
                show HC125tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC125tile07_10 = "g_horizontal.png"
                image HC125tile07_11 = "g_elbow_tl.png"
                show HC125tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC125tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC125tile05_11 = "y_g.png"
                show HC125tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC125tile06_11
                hide HC125tile07_10
                hide HC125tile07_11
                hide HC125tile05_11          
            
            
        else:
            hide HC126tile03_07
            hide HC126tile04_07
            hide HC126tile05_06
            hide HC126tile05_07
            hide HC126tile05_08
            hide HC126tile06_08
            hide HC126tile07_08        
            hide HC125tile06_11
            hide HC125tile07_10
            hide HC125tile07_11
            hide HC125tile05_11          
            hide HC124tile06_11
            hide HC124tile07_10
            hide HC124tile07_11
            hide HC124tile05_11
        
    else:
        hide HC16tile08_06
        hide HC16tile08_07
        hide HC16tile08_08
        hide HC16tile07_06
        hide HC16tile07_08
        hide HC16tile06_03
        hide HC16tile06_04
        hide HC16tile06_05
        hide HC16tile06_06
        hide HC16tile05_04
        hide HC126tile03_07
        hide HC126tile04_07
        hide HC126tile05_06
        hide HC126tile05_07
        hide HC126tile05_08
        hide HC126tile06_08
        hide HC126tile07_08        
        hide HC125tile06_11
        hide HC125tile07_10
        hide HC125tile07_11
        hide HC125tile05_11          
        hide HC124tile06_11
        hide HC124tile07_10
        hide HC124tile07_11
        hide HC124tile05_11
        hide HC123tile03_07
        hide HC123tile04_07
        hide HC123tile05_06
        hide HC123tile05_07
        hide HC123tile05_08
        hide HC123tile06_08
        hide HC123tile07_08
        hide HC121tile06_11
        hide HC121tile07_10
        hide HC121tile07_11
        hide HC121tile05_11
        hide HC122tile06_11
        hide HC122tile07_10
        hide HC122tile07_11
        hide HC122tile05_11 
        hide HC120tile03_07
        hide HC120tile04_07
        hide HC120tile05_06
        hide HC120tile05_07
        hide HC120tile05_08
        hide HC120tile06_08
        hide HC120tile07_08
        hide HC118tile06_11
        hide HC118tile07_10
        hide HC118tile07_11
        hide HC118tile05_11        
        hide HC119tile06_11
        hide HC119tile07_10
        hide HC119tile07_11
        hide HC119tile05_11 
            
    if nor1in2 == True:
        image HC17tile08_06 = "r_elbow_tr.png"
        image HC17tile08_07 = "r_horizontal.png"
        image HC17tile08_08 = "r_elbow_tl.png"
        show HC17tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show HC17tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HC17tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        image HC17tile07_06 = "r_vertical.png"
        image HC17tile07_08 = "y_r.png"
        show HC17tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        show HC17tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image HC17tile06_03 = "r_horizontal.png"
        image HC17tile06_04 = "r_t_up.png"
        image HC17tile06_05 = "r_horizontal.png"
        image HC17tile06_06 = "r_elbow_bl.png"
        show HC17tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC17tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC17tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show HC17tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        image HC17tile05_04 = "r_r.png"
        show HC17tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        
        if and1in3 == True:
            image HC128tile03_07 = "y_r.png"
            show HC128tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC128tile04_07 = "r_vertical.png"  
            show HC128tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC128tile05_06 = "r_horizontal.png"
            image HC128tile05_07 = "r_t_up.png"
            image HC128tile05_08 = "r_elbow_bl.png"
            show HC128tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC128tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC128tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC128tile06_08 = "r_vertical.png"
            show HC128tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC128tile07_08 = "r_r.png"
            show HC128tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if nand1in4 == True:
                image HC127tile06_11 = "g_vertical.png"
                show HC127tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC127tile07_10 = "g_horizontal.png"
                image HC127tile07_11 = "g_elbow_tl.png"
                show HC127tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC127tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC127tile05_11 = "y_g.png"
                show HC127tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC127tile06_11
                hide HC127tile07_10
                hide HC127tile07_11
                hide HC127tile05_11        
                
                
            if xor1in4 == True:
                image HC129tile06_11 = "r_vertical.png"
                show HC129tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC129tile07_10 = "r_horizontal.png"
                image HC129tile07_11 = "r_elbow_tl.png"
                show HC129tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC129tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC129tile05_11 = "y_r.png"
                show HC129tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC129tile06_11
                hide HC129tile07_10
                hide HC129tile07_11
                hide HC129tile05_11      
            
        else:
            hide HC128tile03_07
            hide HC128tile04_07
            hide HC128tile05_06
            hide HC128tile05_07
            hide HC128tile05_08
            hide HC128tile06_08
            hide HC128tile07_08
            hide HC127tile06_11
            hide HC127tile07_10
            hide HC127tile07_11
            hide HC127tile05_11        
            hide HC129tile06_11
            hide HC129tile07_10
            hide HC129tile07_11
            hide HC129tile05_11  
            
        if nand1in3 == True:
            image HC132tile03_07 = "y_g.png"
            show HC132tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC132tile04_07 = "g_vertical.png"  
            show HC132tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC132tile05_06 = "g_horizontal.png"
            image HC132tile05_07 = "g_t_up.png"
            image HC132tile05_08 = "g_elbow_bl.png"
            show HC132tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC132tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC132tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC132tile06_08 = "g_vertical.png"
            show HC132tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC132tile07_08 = "g_r.png"
            show HC132tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if and1in4 == True:
                image HC130tile06_11 = "r_vertical.png"
                show HC130tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC130tile07_10 = "r_horizontal.png"
                image HC130tile07_11 = "r_elbow_tl.png"
                show HC130tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC130tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC130tile05_11 = "y_r.png"
                show HC130tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC130tile06_11
                hide HC130tile07_10
                hide HC130tile07_11
                hide HC130tile05_11    
                
            if xor1in4 == True:
                image HC131tile06_11 = "g_vertical.png"
                show HC131tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC131tile07_10 = "g_horizontal.png"
                image HC131tile07_11 = "g_elbow_tl.png"
                show HC131tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC131tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC131tile05_11 = "y_g.png"
                show HC131tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC131tile06_11
                hide HC131tile07_10
                hide HC131tile07_11
                hide HC131tile05_11      
            
        else:
            hide HC132tile03_07
            hide HC132tile04_07
            hide HC132tile05_06
            hide HC132tile05_07
            hide HC132tile05_08
            hide HC132tile06_08
            hide HC132tile07_08
            hide HC130tile06_11
            hide HC130tile07_10
            hide HC130tile07_11
            hide HC130tile05_11    
            hide HC131tile06_11
            hide HC131tile07_10
            hide HC131tile07_11
            hide HC131tile05_11
            
        if xor1in3 == True:
            image HC135tile03_07 = "y_r.png"
            show HC135tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC135tile04_07 = "r_vertical.png"  
            show HC135tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC135tile05_06 = "r_horizontal.png"
            image HC135tile05_07 = "r_t_up.png"
            image HC135tile05_08 = "r_elbow_bl.png"
            show HC135tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC135tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC135tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC135tile06_08 = "r_vertical.png"
            show HC135tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC135tile07_08 = "r_r.png"
            show HC135tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if and1in4 == True:
                image HC133tile06_11 = "r_vertical.png"
                show HC133tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC133tile07_10 = "r_horizontal.png"
                image HC133tile07_11 = "r_elbow_tl.png"
                show HC133tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC133tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC133tile05_11 = "y_r.png"
                show HC133tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC133tile06_11
                hide HC133tile07_10
                hide HC133tile07_11
                hide HC133tile05_11
                
            if nand1in4 == True:
                image HC134tile06_11 = "g_vertical.png"
                show HC134tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC134tile07_10 = "g_horizontal.png"
                image HC134tile07_11 = "g_elbow_tl.png"
                show HC134tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC134tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC134tile05_11 = "y_g.png"
                show HC134tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC134tile06_11
                hide HC134tile07_10
                hide HC134tile07_11
                hide HC134tile05_11        
            
        else:
            hide HC135tile03_07
            hide HC135tile04_07
            hide HC135tile05_06
            hide HC135tile05_07
            hide HC135tile05_08
            hide HC135tile06_08
            hide HC135tile07_08        
            hide HC134tile06_11
            hide HC134tile07_10
            hide HC134tile07_11
            hide HC134tile05_11 
            hide HC133tile06_11
            hide HC133tile07_10
            hide HC133tile07_11
            hide HC133tile05_11
    else:
        hide HC17tile08_06
        hide HC17tile08_07
        hide HC17tile08_08
        hide HC17tile07_06
        hide HC17tile07_08
        hide HC17tile06_03
        hide HC17tile06_04
        hide HC17tile06_05
        hide HC17tile06_06
        hide HC17tile05_04
        hide HC135tile03_07
        hide HC135tile04_07
        hide HC135tile05_06
        hide HC135tile05_07
        hide HC135tile05_08
        hide HC135tile06_08
        hide HC135tile07_08        
        hide HC134tile06_11
        hide HC134tile07_10
        hide HC134tile07_11
        hide HC134tile05_11 
        hide HC133tile06_11
        hide HC133tile07_10
        hide HC133tile07_11
        hide HC133tile05_11
        hide HC132tile03_07
        hide HC132tile04_07
        hide HC132tile05_06
        hide HC132tile05_07
        hide HC132tile05_08
        hide HC132tile06_08
        hide HC132tile07_08
        hide HC130tile06_11
        hide HC130tile07_10
        hide HC130tile07_11
        hide HC130tile05_11    
        hide HC131tile06_11
        hide HC131tile07_10
        hide HC131tile07_11
        hide HC131tile05_11
        hide HC128tile03_07
        hide HC128tile04_07
        hide HC128tile05_06
        hide HC128tile05_07
        hide HC128tile05_08
        hide HC128tile06_08
        hide HC128tile07_08
        hide HC127tile06_11
        hide HC127tile07_10
        hide HC127tile07_11
        hide HC127tile05_11        
        hide HC129tile06_11
        hide HC129tile07_10
        hide HC129tile07_11
        hide HC129tile05_11 
        
    if xor1in2 == True:
        image HC18tile08_06 = "r_elbow_tr.png"
        image HC18tile08_07 = "r_horizontal.png"
        image HC18tile08_08 = "r_elbow_tl.png"
        show HC18tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show HC18tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HC18tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        image HC18tile07_06 = "r_vertical.png"
        image HC18tile07_08 = "y_r.png"
        show HC18tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        show HC18tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image HC18tile06_03 = "r_horizontal.png"
        image HC18tile06_04 = "r_t_up.png"
        image HC18tile06_05 = "r_horizontal.png"
        image HC18tile06_06 = "r_elbow_bl.png"
        show HC18tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC18tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC18tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show HC18tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        image HC18tile05_04 = "r_r.png"
        show HC18tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        
        
        if and1in3 == True:
            image HC168tile03_07 = "y_r.png"
            show HC168tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC168tile04_07 = "r_vertical.png"  
            show HC168tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC168tile05_06 = "r_horizontal.png"
            image HC168tile05_07 = "r_t_up.png"
            image HC168tile05_08 = "r_elbow_bl.png"
            show HC168tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC168tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC168tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC168tile06_08 = "r_vertical.png"
            show HC168tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC168tile07_08 = "r_r.png"
            show HC168tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if nand1in4 == True:
                image HC136tile06_11 = "g_vertical.png"
                show HC136tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC136tile07_10 = "g_horizontal.png"
                image HC136tile07_11 = "g_elbow_tl.png"
                show HC136tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC136tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC136tile05_11 = "y_g.png"
                show HC136tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC136tile06_11
                hide HC136tile07_10
                hide HC136tile07_11
                hide HC136tile05_11        
                
                
            if nor1in4 == True:
                image HC137tile06_11 = "g_vertical.png"
                show HC137tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC137tile07_10 = "g_horizontal.png"
                image HC137tile07_11 = "g_elbow_tl.png"
                show HC137tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC137tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC137tile05_11 = "y_g.png"
                show HC137tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC137tile06_11
                hide HC137tile07_10
                hide HC137tile07_11
                hide HC137tile05_11             
            
        else:
            hide HC168tile03_07
            hide HC168tile04_07
            hide HC168tile05_06
            hide HC168tile05_07
            hide HC168tile05_08
            hide HC168tile06_08
            hide HC168tile07_08
            hide HC137tile06_11
            hide HC137tile07_10
            hide HC137tile07_11
            hide HC137tile05_11             
            hide HC136tile06_11
            hide HC136tile07_10
            hide HC136tile07_11
            hide HC136tile05_11 
        if nand1in3 == True:
            image HC167tile03_07 = "y_g.png"
            show HC167tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC167tile04_07 = "g_vertical.png"  
            show HC167tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC167tile05_06 = "g_horizontal.png"
            image HC167tile05_07 = "g_t_up.png"
            image HC167tile05_08 = "g_elbow_bl.png"
            show HC167tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC167tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC167tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC167tile06_08 = "g_vertical.png"
            show HC167tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC167tile07_08 = "g_r.png"
            show HC167tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if and1in4 == True:
                image HC138tile06_11 = "r_vertical.png"
                show HC138tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC138tile07_10 = "r_horizontal.png"
                image HC138tile07_11 = "r_elbow_tl.png"
                show HC138tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC138tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC138tile05_11 = "y_r.png"
                show HC138tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC138tile06_11
                hide HC138tile07_10
                hide HC138tile07_11
                hide HC138tile05_11       
                
            if nor1in4 == True:
                image HC139tile06_11 = "r_vertical.png"
                show HC139tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC139tile07_10 = "r_horizontal.png"
                image HC139tile07_11 = "r_elbow_tl.png"
                show HC139tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC139tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC139tile05_11 = "y_r.png"
                show HC139tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC139tile06_11
                hide HC139tile07_10
                hide HC139tile07_11
                hide HC139tile05_11        
     
        else:
            hide HC167tile03_07
            hide HC167tile04_07
            hide HC167tile05_06
            hide HC167tile05_07
            hide HC167tile05_08
            hide HC167tile06_08
            hide HC167tile07_08
            hide HC138tile06_11
            hide HC138tile07_10
            hide HC138tile07_11
            hide HC138tile05_11       
            hide HC139tile06_11
            hide HC139tile07_10
            hide HC139tile07_11
            hide HC139tile05_11 
            
        if nor1in3 == True:
            image HC166tile03_07 = "y_g.png"
            show HC166tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            image HC166tile04_07 = "g_vertical.png"  
            show HC166tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            image HC166tile05_06 = "g_horizontal.png"
            image HC166tile05_07 = "g_t_up.png"
            image HC166tile05_08 = "g_elbow_bl.png"
            show HC166tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC166tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC166tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            image HC166tile06_08 = "g_vertical.png"
            show HC166tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC166tile07_08 = "g_r.png"
            show HC166tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            
            if and1in4 == True:
                image HC140tile06_11 = "r_vertical.png"
                show HC140tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC140tile07_10 = "r_horizontal.png"
                image HC140tile07_11 = "r_elbow_tl.png"
                show HC140tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC140tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC140tile05_11 = "y_r.png"
                show HC140tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC140tile06_11
                hide HC140tile07_10
                hide HC140tile07_11
                hide HC140tile05_11
                
            if nand1in4 == True:
                image HC141tile06_11 = "g_vertical.png"
                show HC141tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC141tile07_10 = "g_horizontal.png"
                image HC141tile07_11 = "g_elbow_tl.png"
                show HC141tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC141tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                image HC141tile05_11 = "y_g.png"
                show HC141tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
            else:
                hide HC141tile06_11
                hide HC141tile07_10
                hide HC141tile07_11
                hide HC141tile05_11        

        else:
            hide HC166tile03_07
            hide HC166tile04_07
            hide HC166tile05_06
            hide HC166tile05_07
            hide HC166tile05_08
            hide HC166tile06_08
            hide HC166tile07_08
            hide HC141tile06_11
            hide HC141tile07_10
            hide HC141tile07_11
            hide HC141tile05_11  
            hide HC140tile06_11
            hide HC140tile07_10
            hide HC140tile07_11
            hide HC140tile05_11
    else:
        hide HC18tile08_06
        hide HC18tile08_07
        hide HC18tile08_08
        hide HC18tile07_06
        hide HC18tile07_08
        hide HC18tile06_03
        hide HC18tile06_04
        hide HC18tile06_05
        hide HC18tile06_06
        hide HC18tile05_04
        hide HC166tile03_07
        hide HC166tile04_07
        hide HC166tile05_06
        hide HC166tile05_07
        hide HC166tile05_08
        hide HC166tile06_08
        hide HC166tile07_08
        hide HC141tile06_11
        hide HC141tile07_10
        hide HC141tile07_11
        hide HC141tile05_11  
        hide HC140tile06_11
        hide HC140tile07_10
        hide HC140tile07_11
        hide HC140tile05_11
        hide HC167tile03_07
        hide HC167tile04_07
        hide HC167tile05_06
        hide HC167tile05_07
        hide HC167tile05_08
        hide HC167tile06_08
        hide HC167tile07_08
        hide HC138tile06_11
        hide HC138tile07_10
        hide HC138tile07_11
        hide HC138tile05_11       
        hide HC139tile06_11
        hide HC139tile07_10
        hide HC139tile07_11
        hide HC139tile05_11 
        hide HC168tile03_07
        hide HC168tile04_07
        hide HC168tile05_06
        hide HC168tile05_07
        hide HC168tile05_08
        hide HC168tile06_08
        hide HC168tile07_08
        hide HC137tile06_11
        hide HC137tile07_10
        hide HC137tile07_11
        hide HC137tile05_11             
        hide HC136tile06_11
        hide HC136tile07_10
        hide HC136tile07_11
        hide HC136tile05_11


    if and1in1 == True:
        if nand1in2 == True and nor1in3 == True:
                image HC180tile03_09 = "g_horizontal.png"
                image HC180tile03_10 = "g_horizontal.png"
                image HC180tile03_11 = "g_elbow_bl.png"
                show HC180tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC180tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC180tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC180tile04_11 = "g_vertical.png"
                show HC180tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC180tile05_11 = "g_y.png"
                show HC180tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC180tile03_07 = "r_g.png"
                show HC180tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if xor1in4 == True:
                    image HC1811tile05_13 = "r_horizontal.png"
                    show HC1811tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC1811tile05_11 = "g_g.png"
                    show HC1811tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC1811tile05_13
                    hide HC1811tile05_11
            
        else:
            hide HC180tile03_09
            hide HC180tile03_10
            hide HC180tile03_11
            hide HC180tile04_11
            hide HC180tile05_11
            hide HC180tile03_07
            hide HC1811tile05_13
            hide HC1811tile05_11
                    
        if nand1in2 == True and xor1in3 == True:
                image HC181tile03_09 = "r_horizontal.png"
                image HC181tile03_10 = "r_horizontal.png"
                image HC181tile03_11 = "r_elbow_bl.png"
                show HC181tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC181tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC181tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC181tile04_11 = "r_vertical.png"
                show HC181tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC181tile05_11 = "r_y.png"
                show HC181tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC181tile03_07 = "r_r.png"
                show HC181tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nor1in4 == True:
                    image HC143tile05_13 = "r_horizontal.png"
                    show HC143tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC143tile05_11 = "r_g.png"
                    show HC143tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC143tile05_13
                    hide HC143tile05_11
            
        else:
            hide HC181tile03_09
            hide HC181tile03_10
            hide HC181tile03_11
            hide HC181tile04_11
            hide HC181tile05_11
            hide HC181tile03_07
            hide HC143tile05_13
            hide HC143tile05_11    
            
        if nor1in2 == True and xor1in3 == True:
                image HC182tile03_09 = "r_horizontal.png"
                image HC182tile03_10 = "r_horizontal.png"
                image HC182tile03_11 = "r_elbow_bl.png"
                show HC182tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC182tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC182tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC182tile04_11 = "r_vertical.png"
                show HC182tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC182tile05_11 = "r_y.png"
                show HC182tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC182tile03_07 = "r_r.png"
                show HC182tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nand1in4 == True:
                    image HC144tile05_13 = "r_horizontal.png"
                    show HC144tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC144tile05_11 = "r_g.png"
                    show HC144tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC144tile05_13
                    hide HC144tile05_11
        else:
            hide HC182tile03_09
            hide HC182tile03_10
            hide HC182tile03_11
            hide HC182tile04_11
            hide HC182tile05_11
            hide HC182tile03_07
            hide HC144tile05_13
            hide HC144tile05_11  

                    
        if nor1in2 == True and nand1in3 == True:
                image HC183tile03_09 = "g_horizontal.png"
                image HC183tile03_10 = "g_horizontal.png"
                image HC183tile03_11 = "g_elbow_bl.png"
                show HC183tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC183tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC183tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC183tile04_11 = "g_vertical.png"
                show HC183tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC183tile05_11 = "g_y.png"
                show HC183tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC183tile03_07 = "r_g.png"
                show HC183tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if xor1in4 == True:
                    image HC145tile05_13 = "r_horizontal.png"
                    show HC145tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC145tile05_11 = "g_g.png"
                    show HC145tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC145tile05_13
                    hide HC145tile05_11
                    
        else:
            hide HC183tile03_09
            hide HC183tile03_10
            hide HC183tile03_11
            hide HC183tile04_11
            hide HC183tile05_11
            hide HC183tile03_07
            hide HC145tile05_13
            hide HC145tile05_11    

        
        if xor1in2 == True and nand1in3 == True:
                image HC184tile03_09 = "g_horizontal.png"
                image HC184tile03_10 = "g_horizontal.png"
                image HC184tile03_11 = "g_elbow_bl.png"
                show HC184tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC184tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC184tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC184tile04_11 = "g_vertical.png"
                show HC184tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC184tile05_11 = "g_y.png"
                show HC184tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC184tile03_07 = "r_g.png"
                show HC184tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nor1in4 == True:
                    image HC146tile05_13 = "r_horizontal.png"
                    show HC146tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC146tile05_11 = "g_r.png"
                    show HC146tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
                else:
                    hide HC146tile05_13
                    hide HC146tile05_11
        else:
            hide HC184tile03_09
            hide HC184tile03_10
            hide HC184tile03_11
            hide HC184tile04_11
            hide HC184tile05_11
            hide HC184tile03_07
            hide HC146tile05_13
            hide HC146tile05_11

        
        if xor1in2 == True and nor1in3 == True:
                image HC185tile03_09 = "g_horizontal.png"
                image HC185tile03_10 = "g_horizontal.png"
                image HC185tile03_11 = "g_elbow_bl.png"
                show HC185tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC185tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC185tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC185tile04_11 = "g_vertical.png"
                show HC185tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC185tile05_11 = "g_y.png"
                show HC185tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC185tile03_07 = "r_g.png"
                show HC185tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nand1in4 == True:
                    image HC147tile05_13 = "r_horizontal.png"
                    show HC147tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC147tile05_11 = "g_g.png"
                    show HC147tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC147tile05_13
                    hide HC147tile05_11
        else:
            hide HC185tile03_09
            hide HC185tile03_10
            hide HC185tile03_11
            hide HC185tile04_11
            hide HC185tile05_11
            hide HC185tile03_07
            hide HC147tile05_13
            hide HC147tile05_11    
    else:
        hide HC185tile03_09
        hide HC185tile03_10
        hide HC185tile03_11
        hide HC185tile04_11
        hide HC185tile05_11
        hide HC185tile03_07
        hide HC147tile05_13
        hide HC147tile05_11    
        hide HC180tile03_09
        hide HC180tile03_10
        hide HC180tile03_11
        hide HC180tile04_11
        hide HC180tile05_11
        hide HC180tile03_07
        hide HC1811tile05_13
        hide HC1811tile05_11
        hide HC181tile03_09
        hide HC181tile03_10
        hide HC181tile03_11
        hide HC181tile04_11
        hide HC181tile05_11
        hide HC181tile03_07
        hide HC143tile05_13
        hide HC143tile05_11    
        hide HC182tile03_09
        hide HC182tile03_10
        hide HC182tile03_11
        hide HC182tile04_11
        hide HC182tile05_11
        hide HC182tile03_07
        hide HC144tile05_13
        hide HC144tile05_11  
        hide HC183tile03_09
        hide HC183tile03_10
        hide HC183tile03_11
        hide HC183tile04_11
        hide HC183tile05_11
        hide HC183tile03_07
        hide HC145tile05_13
        hide HC145tile05_11    
        hide HC184tile03_09
        hide HC184tile03_10
        hide HC184tile03_11
        hide HC184tile04_11
        hide HC184tile05_11
        hide HC184tile03_07
        hide HC146tile05_13
        hide HC146tile05_11   
    
    
    if nand1in1 == True:
        if and1in2 == True and nor1in3 == True:
                image HC186tile03_09 = "g_horizontal.png"
                image HC186tile03_10 = "g_horizontal.png"
                image HC186tile03_11 = "g_elbow_bl.png"
                show HC186tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC186tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC186tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC186tile04_11 = "g_vertical.png"
                show HC186tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC186tile05_11 = "g_y.png"
                show HC186tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC186tile03_07 = "g_r.png"
                show HC186tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if xor1in4 == True:
                    image HC148tile05_13 = "r_horizontal.png"
                    show HC148tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC148tile05_11 = "g_g.png"
                    show HC148tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC148tile05_13
                    hide HC148tile05_11
        else:
            hide HC186tile03_09
            hide HC186tile03_10
            hide HC186tile03_11
            hide HC186tile04_11
            hide HC186tile05_11
            hide HC186tile03_07
            hide HC148tile05_13
            hide HC148tile05_11
  
                    
        if and1in2 == True and xor1in3 == True:
                image HC190tile03_09 = "g_horizontal.png"
                image HC190tile03_10 = "g_horizontal.png"
                image HC190tile03_11 = "g_elbow_bl.png"
                show HC190tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC190tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC190tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC190tile04_11 = "g_vertical.png"
                show HC190tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC190tile05_11 = "g_y.png"
                show HC190tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC190tile03_07 = "g_g.png"
                show HC190tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nor1in4 == True:
                    image HC149tile05_13 = "r_horizontal.png"
                    show HC149tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC149tile05_11 = "g_r.png"
                    show HC149tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC149tile05_13
                    hide HC149tile05_11
        else:
            hide HC190tile03_09
            hide HC190tile03_10
            hide HC190tile03_11
            hide HC190tile04_11
            hide HC190tile05_11
            hide HC190tile03_07
            hide HC149tile05_13
            hide HC149tile05_11  
 
                    
        if nor1in2 == True and xor1in3 == True:
                image HC191tile03_09 = "g_horizontal.png"
                image HC191tile03_10 = "g_horizontal.png"
                image HC191tile03_11 = "g_elbow_bl.png"
                show HC191tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC191tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC191tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC191tile04_11 = "g_vertical.png"
                show HC191tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC191tile05_11 = "g_y.png"
                show HC191tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC191tile03_07 = "g_r.png"
                show HC191tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if and1in4 == True:
                    image HC14919tile05_13 = "r_horizontal.png"
                    show HC14919tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC14919tile05_11 = "g_r.png"
                    show HC14919tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC14919tile05_13
                    hide HC14919tile05_11
        else:
            hide HC191tile03_09
            hide HC191tile03_10
            hide HC191tile03_11
            hide HC191tile04_11
            hide HC191tile05_11
            hide HC191tile03_07
            hide HC14919tile05_13
            hide HC14919tile05_11
                    
        if nor1in2 == True and and1in3 == True:
                image HC192tile03_09 = "g_horizontal.png"
                image HC192tile03_10 = "g_horizontal.png"
                image HC192tile03_11 = "g_elbow_bl.png"
                show HC192tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC192tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC192tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC192tile04_11 = "g_vertical.png"
                show HC192tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC192tile05_11 = "g_y.png"
                show HC192tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC192tile03_07 = "g_r.png"
                show HC192tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if xor1in4 == True:
                    image HC151tile05_13 = "r_horizontal.png"
                    show HC151tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC151tile05_11 = "g_r.png"
                    show HC151tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC151tile05_13
                    hide HC151tile05_11
        else:
            hide HC192tile03_09
            hide HC192tile03_10
            hide HC192tile03_11
            hide HC192tile04_11
            hide HC192tile05_11
            hide HC192tile03_07
            hide HC151tile05_13
            hide HC151tile05_11 

        
        if xor1in2 == True and and1in3 == True:
                image HC193tile03_09 = "g_horizontal.png"
                image HC193tile03_10 = "g_horizontal.png"
                image HC193tile03_11 = "g_elbow_bl.png"
                show HC193tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC193tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC193tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC193tile04_11 = "g_vertical.png"
                show HC193tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC193tile05_11 = "g_y.png"
                show HC193tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC193tile03_07 = "g_r.png"
                show HC193tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nor1in4 == True:
                    image HC152tile05_13 = "r_horizontal.png"
                    show HC152tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC152tile05_11 = "g_g.png"
                    show HC152tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC152tile05_13
                    hide HC152tile05_11
        else:
            hide HC193tile03_09
            hide HC193tile03_10
            hide HC193tile03_11
            hide HC193tile04_11
            hide HC193tile05_11
            hide HC193tile03_07
            hide HC152tile05_13
            hide HC152tile05_11 
 
        
        if xor1in2 == True and nor1in3 == True:
                image HC194tile03_09 = "g_horizontal.png"
                image HC194tile03_10 = "g_horizontal.png"
                image HC194tile03_11 = "g_elbow_bl.png"
                show HC194tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC194tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC194tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC194tile04_11 = "g_vertical.png"
                show HC194tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC194tile05_11 = "g_y.png"
                show HC194tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC194tile03_07 = "g_g.png"
                show HC194tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if and1in4 == True:
                    image HC153tile05_13 = "r_horizontal.png"
                    show HC153tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC153tile05_11 = "g_r.png"
                    show HC153tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC153tile05_13
                    hide HC153tile05_11
        else:
            hide HC194tile03_09
            hide HC194tile03_10
            hide HC194tile03_11
            hide HC194tile04_11
            hide HC194tile05_11
            hide HC194tile03_07
            hide HC153tile05_13
            hide HC153tile05_11
    else:
        hide HC194tile03_09
        hide HC194tile03_10
        hide HC194tile03_11
        hide HC194tile04_11
        hide HC194tile05_11
        hide HC194tile03_07
        hide HC153tile05_13
        hide HC153tile05_11 
        hide HC193tile03_09
        hide HC193tile03_10
        hide HC193tile03_11
        hide HC193tile04_11
        hide HC193tile05_11
        hide HC193tile03_07
        hide HC152tile05_13
        hide HC152tile05_11      
        hide HC192tile03_09
        hide HC192tile03_10
        hide HC192tile03_11
        hide HC192tile04_11
        hide HC192tile05_11
        hide HC192tile03_07
        hide HC151tile05_13
        hide HC151tile05_11  
        hide HC191tile03_09
        hide HC191tile03_10
        hide HC191tile03_11
        hide HC191tile04_11
        hide HC191tile05_11
        hide HC191tile03_07
        hide HC14919tile05_13
        hide HC14919tile05_11
        hide HC190tile03_09
        hide HC190tile03_10
        hide HC190tile03_11
        hide HC190tile04_11
        hide HC190tile05_11
        hide HC190tile03_07
        hide HC149tile05_13
        hide HC149tile05_11  
        hide HC186tile03_09
        hide HC186tile03_10
        hide HC186tile03_11
        hide HC186tile04_11
        hide HC186tile05_11
        hide HC186tile03_07
        hide HC148tile05_13
        hide HC148tile05_11
            
            
            
    if nor1in1 == True:
        if nand1in2 == True and and1in3 == True:  #winner *************************************************************
                image HC195tile03_09 = "r_horizontal.png"
                image HC195tile03_10 = "r_horizontal.png"
                image HC195tile03_11 = "r_elbow_bl.png"
                show HC195tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC195tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC195tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC195tile04_11 = "r_vertical.png"
                show HC195tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC195tile05_11 = "r_y.png"
                show HC195tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC195tile03_07 = "r_r.png"
                show HC195tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if xor1in4 == True:
                    image HC154tile05_13 = "g_horizontal.png"
                    show HC154tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC154tile05_11 = "r_r.png"
                    show HC154tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC154tile05_13
                    hide HC154tile05_11
        else:
            hide HC195tile03_09
            hide HC195tile03_10
            hide HC195tile03_11
            hide HC195tile04_11
            hide HC195tile05_11
            hide HC195tile03_07
            hide HC154tile05_13
            hide HC154tile05_11  


                    
        if nand1in2 == True and xor1in3 == True: #winner *******************************************************
                image HC196tile03_09 = "r_horizontal.png"
                image HC196tile03_10 = "r_horizontal.png"
                image HC196tile03_11 = "r_elbow_bl.png"
                show HC196tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC196tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC196tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC196tile04_11 = "r_vertical.png"
                show HC196tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC196tile05_11 = "r_y.png"
                show HC196tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC196tile03_07 = "r_r.png"
                show HC196tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if and1in4 == True:
                    image HC155tile05_13 = "g_horizontal.png"
                    show HC155tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC155tile05_11 = "r_r.png"
                    show HC155tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
                else:
                    hide HC155tile05_13
                    hide HC155tile05_11
                
        else:
            hide HC196tile03_09
            hide HC196tile03_10
            hide HC196tile03_11
            hide HC196tile04_11
            hide HC196tile05_11
            hide HC196tile03_07
            hide HC155tile05_13
            hide HC155tile05_11
                    
        if and1in2 == True and xor1in3 == True:
            image HC197tile03_09 = "g_horizontal.png"
            image HC197tile03_10 = "g_horizontal.png"
            image HC197tile03_11 = "g_elbow_bl.png"
            show HC197tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            show HC197tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
            show HC197tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image HC197tile04_11 = "g_vertical.png"
            show HC197tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image HC197tile05_11 = "g_y.png"
            show HC197tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HC197tile03_07 = "r_g.png"
            show HC197tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
            if nand1in4 == True:
                image HC156tile05_13 = "r_horizontal.png"
                show HC156tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                image HC156tile05_11 = "g_r.png"
                show HC156tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            else:
                hide HC156tile05_13
                hide HC156tile05_11
        else:
            hide HC197tile03_09
            hide HC197tile03_10
            hide HC197tile03_11
            hide HC197tile04_11
            hide HC197tile05_11
            hide HC197tile03_07
            hide HC156tile05_13
            hide HC156tile05_11

                
        if and1in2 == True and nand1in3 == True:
                image HC198tile03_09 = "g_horizontal.png"
                image HC198tile03_10 = "g_horizontal.png"
                image HC198tile03_11 = "g_elbow_bl.png"
                show HC198tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC198tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC198tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC198tile04_11 = "g_vertical.png"
                show HC198tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC198tile05_11 = "g_y.png"
                show HC198tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC198tile03_07 = "r_g.png"
                show HC198tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if xor1in4 == True:
                    image HC157tile05_13 = "r_horizontal.png"
                    show HC157tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC157tile05_11 = "g_r.png"
                    show HC157tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC157tile05_13
                    hide HC157tile05_11
        else:
            hide HC198tile03_09
            hide HC198tile03_10
            hide HC198tile03_11
            hide HC198tile04_11
            hide HC198tile05_11
            hide HC198tile03_07
            hide HC157tile05_13
            hide HC157tile05_11

        if xor1in2 == True and nand1in3 == True:
                image HC199tile03_09 = "g_horizontal.png"
                image HC199tile03_10 = "g_horizontal.png"
                image HC199tile03_11 = "g_elbow_bl.png"
                show HC199tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC199tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC199tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC199tile04_11 = "g_vertical.png"
                show HC199tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC199tile05_11 = "g_y.png"
                show HC199tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC199tile03_07 = "r_g.png"
                show HC199tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if and1in4 == True:
                    image HC158tile05_13 = "r_horizontal.png"
                    show HC158tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC158tile05_11 = "g_r.png"
                    show HC158tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
                else:
                    hide HC158tile05_13
                    hide HC158tile05_11
        else:
            hide HC199tile03_09
            hide HC199tile03_10
            hide HC199tile03_11
            hide HC199tile04_11
            hide HC199tile05_11
            hide HC199tile03_07
            hide HC158tile05_13
            hide HC158tile05_11

        
        if xor1in2 == True and and1in3 == True:
                image HC1100tile03_09 = "r_horizontal.png"
                image HC1100tile03_10 = "r_horizontal.png"
                image HC1100tile03_11 = "r_elbow_bl.png"
                show HC1100tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1100tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1100tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1100tile04_11 = "r_vertical.png"
                show HC1100tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1100tile05_11 = "r_y.png"
                show HC1100tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1100tile03_07 = "r_r.png"
                show HC1100tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nand1in4 == True:
                    image HC159tile05_13 = "r_horizontal.png"
                    show HC159tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC159tile05_11 = "r_g.png"
                    show HC159tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)   
                else:
                    hide HC159tile05_13
                    hide HC159tile05_11
        else:
            hide HC1100tile03_09
            hide HC1100tile03_10
            hide HC1100tile03_11
            hide HC1100tile04_11
            hide HC1100tile05_11
            hide HC1100tile03_07
            hide HC159tile05_13
            hide HC159tile05_11
            
    else:
        hide HC1100tile03_09
        hide HC1100tile03_10
        hide HC1100tile03_11
        hide HC1100tile04_11
        hide HC1100tile05_11
        hide HC1100tile03_07
        hide HC159tile05_13
        hide HC159tile05_11
        hide HC199tile03_09
        hide HC199tile03_10
        hide HC199tile03_11
        hide HC199tile04_11
        hide HC199tile05_11
        hide HC199tile03_07
        hide HC158tile05_13
        hide HC158tile05_11
        hide HC198tile03_09
        hide HC198tile03_10
        hide HC198tile03_11
        hide HC198tile04_11
        hide HC198tile05_11
        hide HC198tile03_07
        hide HC157tile05_13
        hide HC157tile05_11
        hide HC197tile03_09
        hide HC197tile03_10
        hide HC197tile03_11
        hide HC197tile04_11
        hide HC197tile05_11
        hide HC197tile03_07
        hide HC156tile05_13
        hide HC156tile05_11
        hide HC196tile03_09
        hide HC196tile03_10
        hide HC196tile03_11
        hide HC196tile04_11
        hide HC196tile05_11
        hide HC196tile03_07
        hide HC155tile05_13
        hide HC155tile05_11
        hide HC195tile03_09
        hide HC195tile03_10
        hide HC195tile03_11
        hide HC195tile04_11
        hide HC195tile05_11
        hide HC195tile03_07
        hide HC154tile05_13
        hide HC154tile05_11 
            
            
    if xor1in1 == True:
        if nand1in2 == True and nor1in3 == True:
                image HC1101tile03_09 = "g_horizontal.png"
                image HC1101tile03_10 = "g_horizontal.png"
                image HC1101tile03_11 = "g_elbow_bl.png"
                show HC1101tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1101tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1101tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1101tile04_11 = "g_vertical.png"
                show HC1101tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1101tile05_11 = "g_y.png"
                show HC1101tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1101tile03_07 = "g_g.png"
                show HC1101tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if and1in4 == True:
                    image HC160tile05_13 = "r_horizontal.png"
                    show HC160tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC160tile05_11 = "g_r.png"
                    show HC160tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
                else:
                    hide HC160tile05_13
                    hide HC160tile05_11
        else:
            hide HC1101tile03_09
            hide HC1101tile03_10
            hide HC1101tile03_11
            hide HC1101tile04_11
            hide HC1101tile05_11
            hide HC1101tile03_07
            hide HC160tile05_13
            hide HC160tile05_11 

                    
        if nand1in2 == True and and1in3 == True:
                image HC1102tile03_09 = "g_horizontal.png"
                image HC1102tile03_10 = "g_horizontal.png"
                image HC1102tile03_11 = "g_elbow_bl.png"
                show HC1102tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1102tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1102tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1102tile04_11 = "g_vertical.png"
                show HC1102tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1102tile05_11 = "g_y.png"
                show HC1102tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1102tile03_07 = "g_r.png"
                show HC1102tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nor1in4 == True:
                    image HC161tile05_13 = "r_horizontal.png"
                    show HC161tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC161tile05_11 = "g_g.png"
                    show HC161tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
                else:
                    hide HC161tile05_13
                    hide HC161tile05_11
        else:
            hide HC1102tile03_09
            hide HC1102tile03_10
            hide HC1102tile03_11
            hide HC1102tile04_11
            hide HC1102tile05_11
            hide HC1102tile03_07
            hide HC161tile05_13
            hide HC161tile05_11
                    
        if nor1in2 == True and and1in3 == True:
                image HC1103tile03_09 = "g_horizontal.png"
                image HC1103tile03_10 = "g_horizontal.png"
                image HC1103tile03_11 = "g_elbow_bl.png"
                show HC1103tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1103tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1103tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1103tile04_11 = "g_vertical.png"
                show HC1103tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1103tile05_11 = "g_y.png"
                show HC1103tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1103tile03_07 = "g_r.png"
                show HC1103tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nand1in4 == True:
                    image HC162tile05_13 = "r_horizontal.png"
                    show HC162tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC162tile05_11 = "g_g.png"
                    show HC162tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                else:
                    hide HC162tile05_13
                    hide HC162tile05_11
        else:
            hide HC1103tile03_09
            hide HC1103tile03_10
            hide HC1103tile03_11
            hide HC1103tile04_11
            hide HC1103tile05_11
            hide HC1103tile03_07
            hide HC162tile05_13
            hide HC162tile05_11 

                    
        if nor1in2 == True and nand1in3 == True:
                image HC1104tile03_09 = "g_horizontal.png"
                image HC1104tile03_10 = "g_horizontal.png"
                image HC1104tile03_11 = "g_elbow_bl.png"
                show HC1104tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1104tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1104tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1104tile04_11 = "g_vertical.png"
                show HC1104tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1104tile05_11 = "g_y.png"
                show HC1104tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1104tile03_07 = "g_g.png"
                show HC1104tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if and1in4 == True:
                    image HC163tile05_13 = "r_horizontal.png"
                    show HC163tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC163tile05_11 = "g_r.png"
                    show HC163tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0) 
                else:
                    hide HC163tile05_13
                    hide HC163tile05_11
        else:
            hide HC1104tile03_09
            hide HC1104tile03_10
            hide HC1104tile03_11
            hide HC1104tile04_11
            hide HC1104tile05_11
            hide HC1104tile03_07
            hide HC163tile05_13
            hide HC163tile05_11  

        
        if and1in2 == True and nand1in3 == True:
                image HC1105tile03_09 = "g_horizontal.png"
                image HC1105tile03_10 = "g_horizontal.png"
                image HC1105tile03_11 = "g_elbow_bl.png"
                show HC1105tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1105tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1105tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1105tile04_11 = "g_vertical.png"
                show HC1105tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1105tile05_11 = "g_y.png"
                show HC1105tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1105tile03_07 = "g_g.png"
                show HC1105tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nor1in4 == True:
                    image HC164tile05_13 = "r_horizontal.png"
                    show HC164tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC164tile05_11 = "g_r.png"
                    show HC164tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
                else:
                    hide HC164tile05_13
                    hide HC164tile05_11
        else:
            hide HC1105tile03_09
            hide HC1105tile03_10
            hide HC1105tile03_11
            hide HC1105tile04_11
            hide HC1105tile05_11
            hide HC1105tile03_07
            hide HC164tile05_13
            hide HC164tile05_11 

        
        if and1in2 == True and nor1in3 == True:
                image HC1106tile03_09 = "g_horizontal.png"
                image HC1106tile03_10 = "g_horizontal.png"
                image HC1106tile03_11 = "g_elbow_bl.png"
                show HC1106tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1106tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
                show HC1106tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
                image HC1106tile04_11 = "g_vertical.png"
                show HC1106tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                image HC1106tile05_11 = "g_y.png"
                show HC1106tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC1106tile03_07 = "g_r.png"
                show HC1106tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
                if nand1in4 == True:
                    image HC165tile05_13 = "r_horizontal.png"
                    show HC165tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
                    image HC165tile05_11 = "g_g.png"
                    show HC165tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)   
                else:
                    hide HC165tile05_13
                    hide HC165tile05_11
        else:
            hide HC1106tile03_09
            hide HC1106tile03_10
            hide HC1106tile03_11
            hide HC1106tile04_11
            hide HC1106tile05_11
            hide HC1106tile03_07
            hide HC165tile05_13
            hide HC165tile05_11 
    else:
            hide HC1106tile03_09
            hide HC1106tile03_10
            hide HC1106tile03_11
            hide HC1106tile04_11
            hide HC1106tile05_11
            hide HC1106tile03_07
            hide HC165tile05_13
            hide HC165tile05_11 
            hide HC1105tile03_09
            hide HC1105tile03_10
            hide HC1105tile03_11
            hide HC1105tile04_11
            hide HC1105tile05_11
            hide HC1105tile03_07
            hide HC164tile05_13
            hide HC164tile05_11 
            hide HC1104tile03_09
            hide HC1104tile03_10
            hide HC1104tile03_11
            hide HC1104tile04_11
            hide HC1104tile05_11
            hide HC1104tile03_07
            hide HC163tile05_13
            hide HC163tile05_11  
            hide HC1103tile03_09
            hide HC1103tile03_10
            hide HC1103tile03_11
            hide HC1103tile04_11
            hide HC1103tile05_11
            hide HC1103tile03_07
            hide HC162tile05_13
            hide HC162tile05_11 
            hide HC1101tile03_09
            hide HC1101tile03_10
            hide HC1101tile03_11
            hide HC1101tile04_11
            hide HC1101tile05_11
            hide HC1101tile03_07
            hide HC160tile05_13
            hide HC160tile05_11 
            hide HC1102tile03_09
            hide HC1102tile03_10
            hide HC1102tile03_11
            hide HC1102tile04_11
            hide HC1102tile05_11
            hide HC1102tile03_07
            hide HC161tile05_13
            hide HC161tile05_11
            
            
#win conditions ********
    if (nor1in1 == True and nand1in2 == True and and1in3 == True and xor1in4 == True) or (nor1in1 == True and nand1in2 == True and xor1in3 == True and and1in4 == True):         
        image HB1295tile02_09 = "xor_Gate.png"
        show HB1295tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HB1295tile02_10 = "nand_Gate.png"
        show HB1295tile02_10 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image HB1195tile07_02 = "and_Gate.png"
        show HB1195tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HB1195tile07_08 = "nor_Gate.png"
        show HB1195tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image HB1195end2 = "light_g_on.png"
        show HB1195end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardCWin
        $lgHardC_solved = True
        jump lgHard_done

  
    if attempts == 0:
        image HB1295tile02_09 = "xor_Gate.png"
        show HB1295tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HB1295tile02_10 = "nand_Gate.png"
        show HB1295tile02_10 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image HB1295tile07_02 = "and_Gate.png"
        show HB1295tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HB1295tile07_08 = "nor_Gate.png"
        show HB1295tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_lgHardCLose
        $lgHard_attempts +=1
        jump lgHard_lose3
    
    jump gamefileHC1

screen logicgatesHC1:
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
        xpos 240
        ypos 890
        focus_mask True
        action Jump("hints_lgHardC1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty.png"
        xpos 1515
        ypos 890
    text "Moves" xpos 1550 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    text ": " xpos 1675 ypos 895 color "#0060db" font "Bitter-Bold.otf" size 40
    text "[attempts]" xpos 1705 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #and gates
            drag:
                drag_name "and_gate"
                child "AND_Gate.png"
                droppable False
                dragged gate_dragged
                xpos and1x ypos and1y
                
            #or gates
            drag:
                drag_name "nor_gate"
                child "nor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nor1x ypos nor1y
                
            #nand gate
            drag:
                drag_name "xor_gate1"
                child "xor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos xor1x ypos xor1y
                
            drag:
                drag_name "nand_gate"
                child "nand_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nand1x ypos nand1y

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos gate1x ypos gate1y
           
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos gate2x ypos gate2y
                
            drag:
                drag_name "gate slot three"
                child "cover.png"
                draggable False
                xpos gate3x ypos gate3y
                
            drag:
                drag_name "gate slot four"
                child "cover.png"
                draggable False
                xpos gate4x ypos gate4y
                
            drag:
                drag_name "and return"
                child "cover.png"
                draggable False
                xpos 698 ypos 88
           
            drag:
                drag_name "nor return"
                child "cover.png"
                draggable False
                xpos 1148 ypos 88
                
            drag:
                drag_name "xor return"
                child "cover.png"
                draggable False
                xpos 1299 ypos 88
                
            drag:
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88

