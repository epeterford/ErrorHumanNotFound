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

label logicGate_hardB3:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
   
    #row 1 (row has a light)
    image HB3tile01_00 = "r_horizontal.png"
    image HB3tile01_01 = "r_horizontal.png"
    image HB3tile01_02 = "r_horizontal.png"
    image HB3tile01_03 = "r_elbow_bl.png"
    
    show HB3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HB3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show HB3tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show HB3tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image HB3tile02_03 = "r_r.png"
    image HB3tile02_04 = "NONE_Gate.png"
    image HB3tile02_05 = "y_horizontal.png"
    image HB3tile02_06 = "y_horizontal.png"
    image HB3tile02_07 = "y_horizontal.png"
    image HB3tile02_08 = "y_horizontal.png"
    image HB3tile02_09 = "y_elbow_bl.png"
    
    show HB3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HB3tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show HB3tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show HB3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show HB3tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show HB3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show HB3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HB3tile03_00 = "r_horizontal.png"
    image HB3tile03_01 = "r_t_down.png"
    image HB3tile03_02 = "r_horizontal.png"
    image HB3tile03_03 = "r_elbow_tl.png"
    image HB3tile03_09 = "y_y.png"
    image HB3tile03_10 = "NONE_Gate.png"
    image HB3tile03_11 = "y_elbow_bl.png"
    
    show HB3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HB3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HB3tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HB3tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show HB3tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show HB3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HB3tile04_01 = "r_g.png"
    image HB3tile04_02 = "NONE_Gate.png"
    image HB3tile04_03 = "y_t_down.png"
    image HB3tile04_04 = "y_horizontal.png"
    image HB3tile04_05 = "y_horizontal.png"
    image HB3tile04_06 = "y_elbow_bl.png"
    image HB3tile04_09 = "y_elbow_tr.png"
    image HB3tile04_10 = "y_elbow_bl.png"
    image HB3tile04_11 = "y_y.png"
    image HB3tile04_12 = "OR_Gate_blue.png"
    image HB3tile04_13 = "y_elbow_bl.png"
    
    show HB3tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    show HB3tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HB3tile05_00 = "g_horizontal.png"
    image HB3tile05_01 = "g_elbow_tl.png"
    image HB3tile05_03 = "y_vertical.png"
    image HB3tile05_06 = "y_y.png"
    image HB3tile05_07 = "AND_Gate_blue.png"
    image HB3tile05_08 = "y_horizontal.png"
    image HB3tile05_09 = "NOT_Gate_blue.png"
    image HB3tile05_10 = "y_t_up.png"
    image HB3tile05_11 = "y_elbow_tl.png"
    image HB3tile05_13 = "y_elbow_tr.png"
    
    show HB3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show HB3tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image HB3tile06_03 = "y_r.png"
    image HB3tile06_04 = "NONE_Gate.png"
    image HB3tile06_05 = "y_horizontal.png"
    image HB3tile06_06 = "y_elbow_tl.png"
    
    show HB3tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show HB3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show HB3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show HB3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HB3tile07_00 = "r_horizontal.png"
    image HB3tile07_01 = "r_horizontal.png"
    image HB3tile07_02 = "r_horizontal.png"
    image HB3tile07_03 = "r_elbow_tl.png"
    
    show HB3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HB3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show HB3tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show HB3tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    
    #start points
    image HB3start1 = "light_r_on.png"
    show HB3start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HB3start2 = "light_r_on.png"
    show HB3start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HB3start3 = "light_g_on.png"
    show HB3start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HB3start4 = "light_r_on.png"
    show HB3start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image HB3end3 = "light_r_off.png"
    show HB3end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)

    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    
    $ temp_slot = ""
    $ temp_gate = ""
    $ gate_name = ""
    $ slot_name = ""

    #initial value assignment for dragables
    $ nor1x = 1148
    $ nor1y = 88
    $ nand1x = 998
    $ nand1y = 88
    $ xor1x = 1299
    $ xor1y = 88
    $ xor2x = 1299
    $ xor2y = 88
    
    #gate values
    $ gate1x = 736
    $ gate1y = 383
    $ gate2x = 586
    $ gate2y = 533
    $ gate3x = 736
    $ gate3y = 683
    $ gate4x = 1186
    $ gate4y = 458
    
    # check conditons for locations
    $ nor1in1 = False
    $ nand1in1 = False
    $ xor1in1 = False
    $ xor2in1 = False
    $ nor1in2 = False
    $ nand1in2 = False
    $ xor1in2 = False
    $ xor2in2 = False
    $ nor1in3 = False
    $ nand1in3 = False
    $ xor1in3 = False
    $ xor2in3 = False
    $ nor1in4 = False
    $ nand1in4 = False
    $ xor1in4 = False
    $ xor2in4 = False   
    
    #attempts for players
    $ attempts = 6
 
    jump gamefileHB3
    
    
label gamefileHB3:
    
    #calls game screen
    call screen logicgatesHB3
    
    #the first logic gate *******************************************************************************
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False
            if xor2in1 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in1 = False
                
            #sets values for checks
            $ nor1x = gate1x
            $ nor1y = gate1y
            $ nor1in1 = True
            $ nor1in2 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nand1in2 == True:
                $ nand1x =998
                $ nand1y = 88
                $ nand1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False
            if xor2in2 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in2 = False
                
            #sets values for checks
            $ nor1x = gate2x
            $ nor1y = gate2y
            $ nor1in2 = True
            $ nor1in1 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot nuHBer three*******************************        
        if slot_name == "gate slot three":
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in3 = False
                
            #sets values for checks
            $ nor1x = gate3x
            $ nor1y = gate3y
            $ nor1in2 = False
            $ nor1in1 = False
            $ nor1in3 = True
            $ nor1in4 = False
            
        if slot_name == "gate slot four":
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in4 = False
                
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
            
     #or gate section **********************************************************************       
    if gate_name == "nand_gate":
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
            if xor2in1 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in1 = False
                
            #sets values for checks
            $ nand1x = gate1x
            $ nand1y = gate1y
            $ nand1in1 = True
            $ nand1in2 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
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
            if xor2in2 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in2 = False
                
            #sets values for checks
            $ nand1x = gate2x
            $ nand1y = gate2y
            $ nand1in2 = True
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
        #gate slot nuHBer three*******************************    
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in3 = False
                
            #sets values for checks
            $ nand1x = gate3x
            $ nand1y = gate3y
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = True
            $ nand1in4 = False
            
        if slot_name == "gate slot four":
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in4 = False
                
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
            
     #nand gate section **********************************************************************       
    if gate_name == "xor_gate1":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False
            if xor2in1 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in1 = False                

            #sets values for checks
            $ xor1x = gate1x
            $ xor1y = gate1y
            $ xor1in1 = True
            $ xor1in2 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False
            if xor2in2 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in2 = False  
                
            #sets values for checks
            $ xor1x = gate2x
            $ xor1y = gate2y
            $ xor1in2 = True
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot nuHBer three*******************************    
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
            if xor2in3 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in3 = False
                
            #sets values for checks
            $ xor1x = gate3x
            $ xor1y = gate3y
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = True
            $ xor1in4 = False
            
        if slot_name == "gate slot four":
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
            if xor2in4 == True:
                $ xor2x = 1299
                $ xor2y = 88
                $ xor2in4 = False  
                
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

    if gate_name == "xor_gate2":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False                

            #sets values for checks
            $ xor2x = gate1x
            $ xor2y = gate1y
            $ xor2in1 = True
            $ xor2in2 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False  
                
            #sets values for checks
            $ xor2x = gate2x
            $ xor2y = gate2y
            $ xor2in2 = True
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
        #gate slot nuHBer three*******************************    
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
                
            #sets values for checks
            $ xor2x = gate3x
            $ xor2y = gate3y
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = True
            $ xor2in4 = False
            
        if slot_name == "gate slot four":
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
            if xor2in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False  
                
            #sets values for checks
            $ xor2x = gate4x
            $ xor2y = gate4y
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = True
        
        if slot_name == "xor return":
            $ xor2x = 1299
            $ xor2y = 88
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "nand return" or slot_name == "nor return" or slot_name == "xor return"):
       $ temp_slot = slot_name
       $ temp_gate = gate_name
       if temp_slot != "" and temp_gate != "":
           $ attempts -=1

       
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            if slot_name == "nor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate2":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "xor_gate1":
                $ attempts +=1  
            if slot_name == "nand return" and gate_name == "xor_gate2":
                $ attempts +=1    
            if slot_name == "nor return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "xor_gate2":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nand_gate":
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
        
    if nand1in1 == True:
        image HB31tile02_05 = "g_horizontal.png"
        image HB31tile02_06 = "g_horizontal.png"
        image HB31tile02_07 = "g_horizontal.png"
        image HB31tile02_08 = "g_horizontal.png"
        image HB31tile02_09 = "g_elbow_bl.png"
        show HB31tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB31tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show HB31tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show HB31tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show HB31tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image HB31tile03_09 = "g_y.png"
        show HB31tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB31tile02_05
        hide HB31tile02_06
        hide HB31tile02_08
        hide HB31tile02_07
        hide HB31tile02_09
        hide HB31tile03_09

    if nor1in1 == True:
        image HB33tile02_05 = "g_horizontal.png"
        image HB33tile02_06 = "g_horizontal.png"
        image HB33tile02_07 = "g_horizontal.png"
        image HB33tile02_08 = "g_horizontal.png"
        image HB33tile02_09 = "g_elbow_bl.png"
        show HB33tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB33tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show HB33tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show HB33tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show HB33tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image HB33tile03_09 = "g_y.png"
        show HB33tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB33tile02_05
        hide HB33tile02_06
        hide HB33tile02_08
        hide HB33tile02_07
        hide HB33tile02_09
        hide HB33tile03_09
        
    if xor1in1 == True or xor2in1 == True:
        image HB35tile02_05 = "r_horizontal.png"
        image HB35tile02_06 = "r_horizontal.png"
        image HB35tile02_07 = "r_horizontal.png"
        image HB35tile02_08 = "r_horizontal.png"
        image HB35tile02_09 = "r_elbow_bl.png"
        show HB35tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB35tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show HB35tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show HB35tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show HB35tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image HB35tile03_09 = "r_y.png"
        show HB35tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB35tile02_05
        hide HB35tile02_06
        hide HB35tile02_08
        hide HB35tile02_07
        hide HB35tile02_09
        hide HB35tile03_09
        
        
    if nand1in2 == True:
        image HB32tile04_03 = "g_t_down.png"
        image HB32tile04_04 = "g_horizontal.png"
        image HB32tile04_05 = "g_horizontal.png"
        image HB32tile04_06 = "g_elbow_bl.png"
        show HB32tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show HB32tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show HB32tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show HB32tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        image HB32tile05_03 = "g_vertical.png"
        image HB32tile05_06 = "g_y.png"
        show HB32tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show HB32tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image HB32tile06_03 = "g_r.png"
        show HB32tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        if nor1in3 == True:
            image HB310tile06_05 = "r_horizontal.png"
            image HB310tile06_06 = "r_elbow_tl.png"
            show HB310tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB310tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB310tile05_06 = "g_r.png"
            show HB310tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB310tile05_08 = "r_horizontal.png"
            image HB310tile05_10 = "g_t_up.png"
            image HB310tile05_11 = "g_elbow_tl.png"
            show HB310tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB310tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB310tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB310tile04_09 = "g_elbow_tr.png"
            image HB310tile04_10 = "g_elbow_bl.png"
            image HB310tile04_11 = "y_g.png"
            show HB310tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB310tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB310tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB310tile03_09 = "y_g.png"
            show HB310tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB310tile06_05
            hide HB310tile06_06
            hide HB310tile05_06
            hide HB310tile05_08
            hide HB310tile05_11
            hide HB310tile05_10
            hide HB310tile04_09
            hide HB310tile04_10
            hide HB310tile04_11
            hide HB310tile03_09 
        if xor1in3 == True or xor2in3 == True:
            image HB312tile06_05 = "g_horizontal.png"
            image HB312tile06_06 = "g_elbow_tl.png"
            show HB312tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB312tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB312tile05_06 = "g_g.png"
            show HB312tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB312tile05_08 = "g_horizontal.png"
            image HB312tile05_10 = "r_t_up.png"
            image HB312tile05_11 = "r_elbow_tl.png"
            show HB312tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB312tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB312tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB312tile04_09 = "r_elbow_tr.png"
            image HB312tile04_10 = "r_elbow_bl.png"
            image HB312tile04_11 = "y_r.png"
            show HB312tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB312tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB312tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB312tile03_09 = "y_r.png"
            show HB312tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB312tile06_05
            hide HB312tile06_06
            hide HB312tile05_06
            hide HB312tile05_08
            hide HB312tile05_11
            hide HB312tile05_10
            hide HB312tile04_09
            hide HB312tile04_10
            hide HB312tile04_11
            hide HB312tile03_09  

    else:
        hide HB32tile04_03
        hide HB32tile04_04
        hide HB32tile04_06
        hide HB32tile04_05
        hide HB32tile05_03
        hide HB32tile05_06
        hide HB32tile06_03
        hide HB310tile06_05
        hide HB310tile06_06
        hide HB310tile05_06
        hide HB310tile05_08
        hide HB310tile05_11
        hide HB310tile05_10
        hide HB310tile04_09
        hide HB310tile04_10
        hide HB310tile04_11
        hide HB310tile03_09 
        hide HB312tile06_05
        hide HB312tile06_06
        hide HB312tile05_06
        hide HB312tile05_08
        hide HB312tile05_11
        hide HB312tile05_10
        hide HB312tile04_09
        hide HB312tile04_10
        hide HB312tile04_11
        hide HB312tile03_09
        
        
    if nor1in2 == True:
        image HB34tile04_03 = "r_t_down.png"
        image HB34tile04_04 = "r_horizontal.png"
        image HB34tile04_05 = "r_horizontal.png"
        image HB34tile04_06 = "r_elbow_bl.png"
        show HB34tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show HB34tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show HB34tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show HB34tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        image HB34tile05_03 = "r_vertical.png"
        image HB34tile05_06 = "r_y.png"
        show HB34tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show HB34tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image HB34tile06_03 = "r_r.png"
        show HB34tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        if nand1in3 == True:
            image HB38tile06_05 = "g_horizontal.png"
            image HB38tile06_06 = "g_elbow_tl.png"
            show HB38tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB38tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB38tile05_06 = "r_g.png"
            show HB38tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB38tile05_08 = "r_horizontal.png"
            image HB38tile05_10 = "g_t_up.png"
            image HB38tile05_11 = "g_elbow_tl.png"
            show HB38tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB38tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB38tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB38tile04_09 = "g_elbow_tr.png"
            image HB38tile04_10 = "g_elbow_bl.png"
            image HB38tile04_11 = "y_g.png"
            show HB38tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB38tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB38tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB38tile03_09 = "y_g.png"
            show HB38tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB38tile06_05
            hide HB38tile06_06
            hide HB38tile05_06
            hide HB38tile05_08
            hide HB38tile05_11
            hide HB38tile05_10
            hide HB38tile04_09
            hide HB38tile04_10
            hide HB38tile04_11
            hide HB38tile03_09  
        if xor1in3 == True or xor2in3 == True:
            image HB311tile06_05 = "r_horizontal.png"
            image HB311tile06_06 = "r_elbow_tl.png"
            show HB311tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB311tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB311tile05_06 = "r_r.png"
            show HB311tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB311tile05_08 = "r_horizontal.png"
            image HB311tile05_10 = "g_t_up.png"
            image HB311tile05_11 = "g_elbow_tl.png"
            show HB311tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB311tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB311tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB311tile04_09 = "g_elbow_tr.png"
            image HB311tile04_10 = "g_elbow_bl.png"
            image HB311tile04_11 = "y_g.png"
            show HB311tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB311tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB311tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB311tile03_09 = "y_g.png"
            show HB311tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB311tile06_05
            hide HB311tile06_06
            hide HB311tile05_06
            hide HB311tile05_08
            hide HB311tile05_11
            hide HB311tile05_10
            hide HB311tile04_09
            hide HB311tile04_10
            hide HB311tile04_11
            hide HB311tile03_09  
    else:
        hide HB34tile04_03
        hide HB34tile04_04
        hide HB34tile04_06
        hide HB34tile04_05
        hide HB34tile05_03
        hide HB34tile05_06
        hide HB34tile06_03
        hide HB38tile06_05
        hide HB38tile06_06
        hide HB38tile05_06
        hide HB38tile05_08
        hide HB38tile05_11
        hide HB38tile05_10
        hide HB38tile04_09
        hide HB38tile04_10
        hide HB38tile04_11
        hide HB38tile03_09  
        hide HB311tile06_05
        hide HB311tile06_06
        hide HB311tile05_06
        hide HB311tile05_08
        hide HB311tile05_11
        hide HB311tile05_10
        hide HB311tile04_09
        hide HB311tile04_10
        hide HB311tile04_11
        hide HB311tile03_09 
        
    if xor1in2 == True or xor2in2 == True:
        image HB36tile04_03 = "g_t_down.png"
        image HB36tile04_04 = "g_horizontal.png"
        image HB36tile04_05 = "g_horizontal.png"
        image HB36tile04_06 = "g_elbow_bl.png"
        show HB36tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show HB36tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show HB36tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show HB36tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        image HB36tile05_03 = "g_vertical.png"
        image HB36tile05_06 = "g_y.png"
        show HB36tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show HB36tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image HB36tile06_03 = "g_r.png"
        show HB36tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        if nand1in3 == True:
            image HB37tile06_05 = "g_horizontal.png"
            image HB37tile06_06 = "g_elbow_tl.png"
            show HB37tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB37tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB37tile05_06 = "g_g.png"
            show HB37tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB37tile05_08 = "g_horizontal.png"
            image HB37tile05_10 = "r_t_up.png"
            image HB37tile05_11 = "r_elbow_tl.png"
            show HB37tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB37tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB37tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB37tile04_09 = "r_elbow_tr.png"
            image HB37tile04_10 = "r_elbow_bl.png"
            image HB37tile04_11 = "y_r.png"
            show HB37tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB37tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB37tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB37tile03_09 = "y_r.png"
            show HB37tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB37tile06_05
            hide HB37tile06_06
            hide HB37tile05_06
            hide HB37tile05_08
            hide HB37tile05_11
            hide HB37tile05_10
            hide HB37tile04_09
            hide HB37tile04_10
            hide HB37tile04_11
            hide HB37tile03_09  
        if nor1in3 == True:
            image HB39tile06_05 = "r_horizontal.png"
            image HB39tile06_06 = "r_elbow_tl.png"
            show HB39tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB39tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB39tile05_06 = "g_r.png"
            show HB39tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB39tile05_08 = "r_horizontal.png"
            image HB39tile05_10 = "g_t_up.png"
            image HB39tile05_11 = "g_elbow_tl.png"
            show HB39tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB39tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB39tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB39tile04_09 = "g_elbow_tr.png"
            image HB39tile04_10 = "g_elbow_bl.png"
            image HB39tile04_11 = "y_g.png"
            show HB39tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB39tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB39tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB39tile03_09 = "y_g.png"
            show HB39tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB39tile06_05
            hide HB39tile06_06
            hide HB39tile05_06
            hide HB39tile05_08
            hide HB39tile05_11
            hide HB39tile05_10
            hide HB39tile04_09
            hide HB39tile04_10
            hide HB39tile04_11
            hide HB39tile03_09  
        if xor1in3 == True or xor2in3 == True:
            image HB313tile06_05 = "g_horizontal.png"
            image HB313tile06_06 = "g_elbow_tl.png"
            show HB313tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
            show HB313tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            image HB313tile05_06 = "g_g.png"
            show HB313tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)    
            image HB313tile05_08 = "g_horizontal.png"
            image HB313tile05_10 = "r_t_up.png"
            image HB313tile05_11 = "r_elbow_tl.png"
            show HB313tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB313tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show HB313tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image HB313tile04_09 = "r_elbow_tr.png"
            image HB313tile04_10 = "r_elbow_bl.png"
            image HB313tile04_11 = "y_r.png"
            show HB313tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            show HB313tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show HB313tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)   
            image HB313tile03_09 = "y_r.png"
            show HB313tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB313tile06_05
            hide HB313tile06_06
            hide HB313tile05_06
            hide HB313tile05_08
            hide HB313tile05_11
            hide HB313tile05_10
            hide HB313tile04_09
            hide HB313tile04_10
            hide HB313tile04_11
            hide HB313tile03_09  


    else:
        hide HB36tile04_03
        hide HB36tile04_04
        hide HB36tile04_06
        hide HB36tile04_05
        hide HB36tile05_03
        hide HB36tile05_06
        hide HB36tile06_03
        hide HB37tile06_05
        hide HB37tile06_06
        hide HB37tile05_06
        hide HB37tile05_08
        hide HB37tile05_11
        hide HB37tile05_10
        hide HB37tile04_09
        hide HB37tile04_10
        hide HB37tile04_11
        hide HB37tile03_09 
        hide HB39tile06_05
        hide HB39tile06_06
        hide HB39tile05_06
        hide HB39tile05_08
        hide HB39tile05_11
        hide HB39tile05_10
        hide HB39tile04_09
        hide HB39tile04_10
        hide HB39tile04_11
        hide HB39tile03_09 
        
        
    if nand1in1 == True and nor1in2 == True and (xor1in3 == True or xor2in3 == True):
        image HB314tile03_09 = "g_g.png"
        show HB314tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if (xor1in4 == True or xor2in4 == True):
            image HB314tile04_11= "r_g.png"
            show HB314tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB314tile03_11 = "r_elbow_bl.png"
            show HB314tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB314tile05_13 = "g_elbow_tr.png"
            show HB314tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB314tile04_13 = "g_elbow_bl.png"
            show HB314tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB314tile04_11
            hide HB314tile03_11
            hide HB314tile05_13
            hide HB314tile04_13
    else:
        hide HB314tile03_09
        hide HB314tile04_11
        hide HB314tile03_11
        hide HB314tile05_13
        hide HB314tile04_13   
        
        
    if nand1in1 == True and nor1in3 == True and (xor1in2 == True or xor2in2 == True):
        image HB315tile03_09 = "g_g.png"
        show HB315tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if (xor1in4 == True or xor2in4 == True):
            image HB315tile04_11 = "r_g.png"
            show HB315tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB315tile03_11 = "r_elbow_bl.png"
            show HB315tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB315tile05_13 = "g_elbow_tr.png"
            show HB315tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB315tile04_13 = "g_elbow_bl.png"
            show HB315tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB315tile04_11
            hide HB315tile03_11
            hide HB315tile05_13
            hide HB315tile04_13
    else:
        hide HB315tile03_09
        hide HB315tile04_11
        hide HB315tile03_11
        hide HB315tile05_13
        hide HB315tile04_13
      
        
    if nand1in2 == True and nor1in1 == True and (xor1in3 == True or xor2in3 == True):   
        image HB316tile03_09 = "g_r.png"
        show HB316tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if (xor1in4 == True or xor2in4 == True):
            image HB316tile04_11 = "g_r.png"
            show HB316tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB316tile03_11 = "g_elbow_bl.png"
            show HB316tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB316tile05_13 = "g_elbow_tr.png"
            show HB316tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB316tile04_13 = "g_elbow_bl.png"
            show HB316tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB316tile04_11
            hide HB316tile03_11
            hide HB316tile05_13
            hide HB316tile04_13
    else:
        hide HB316tile03_09
        hide HB316tile04_11
        hide HB316tile03_11
        hide HB316tile05_13
        hide HB316tile04_13
       
        
    if nand1in2 == True and nor1in3 == True and (xor1in1 == True or xor2in1 == True):
        image HB317tile03_09 = "r_g.png"
        show HB317tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if (xor1in4 == True or xor2in4 == True):
            image HB317tile04_11 = "g_g.png"
            show HB317tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB317tile03_11 = "g_elbow_bl.png"
            show HB317tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB317tile05_13 = "g_elbow_tr.png"
            show HB317tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB317tile04_13 = "g_elbow_bl.png"
            show HB317tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB317tile04_11
            hide HB317tile03_11
            hide HB317tile05_13
            hide HB317tile04_13
    else:
        hide HB317tile03_09
        hide HB317tile04_11
        hide HB317tile03_11
        hide HB317tile05_13
        hide HB317tile04_13
        
        
    if nand1in3 == True and nor1in1 == True and (xor1in2 == True or xor2in2 == True): 
        image HB318tile03_09 = "g_r.png"
        show HB318tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if (xor1in4 == True or xor2in4 == True):
            image HB318tile04_11 = "g_r.png"
            show HB318tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB318tile03_11 = "g_elbow_bl.png"
            show HB318tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB318tile05_13 = "g_elbow_tr.png"
            show HB318tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB318tile04_13 = "g_elbow_bl.png"
            show HB318tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB318tile04_11
            hide HB318tile03_11
            hide HB318tile05_13
            hide HB318tile04_13
    else:
        hide HB318tile03_09
        hide HB318tile04_11
        hide HB318tile03_11
        hide HB318tile05_13
        hide HB318tile04_13
       
        
    if nand1in3 == True and nor1in2 == True and (xor1in1 == True or xor2in1 == True):
        image HB319tile03_09 = "r_g.png"
        show HB319tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if (xor1in4 == True or xor2in4 == True):
            image HB319tile04_11 = "g_g.png"
            show HB319tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB319tile03_11 = "g_elbow_bl.png"
            show HB319tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB319tile05_13 = "g_elbow_tr.png"
            show HB319tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB319tile04_13 = "g_elbow_bl.png"
            show HB319tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB319tile04_11
            hide HB319tile03_11
            hide HB319tile05_13
            hide HB319tile04_13
    else:
        hide HB319tile03_09
        hide HB319tile04_11
        hide HB319tile03_11
        hide HB319tile05_13
        hide HB319tile04_13
      
#winner scenario******************************************************************************************************************
    if nand1in1 == True and (xor1in2 == True or xor2in2 == True) and (xor1in3 == True or xor2in3 == True):
        image HB320tile03_09 = "g_r.png"
        show HB320tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if nor1in4 == True:
            image HB320tile04_11 = "r_r.png"
            show HB320tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB320tile03_11 = "r_elbow_bl.png"
            show HB320tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB320tile05_13 = "r_elbow_tr.png"
            show HB320tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB320tile04_13 = "r_elbow_bl.png"
            show HB320tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB320tile04_11
            hide HB320tile03_11
            hide HB320tile05_13
            hide HB320tile04_13
    else:
        hide HB320tile03_09
        hide HB320tile04_11
        hide HB320tile03_11
        hide HB320tile05_13
        hide HB320tile04_13
       
        
    if nand1in2 == True and (xor1in1 == True or xor2in1 == True) and (xor1in3 == True or xor2in3 == True):
        image HB321tile03_09 = "r_r.png"
        show HB321tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if nor1in4 == True:
            image HB321tile04_11 = "g_r.png"
            show HB321tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB321tile03_11 = "g_elbow_bl.png"
            show HB321tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB321tile05_13 = "g_elbow_tr.png"
            show HB321tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB321tile04_13 = "g_elbow_bl.png"
            show HB321tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB321tile04_11
            hide HB321tile03_11
            hide HB321tile05_13
            hide HB321tile04_13
    else:
        hide HB321tile04_11
        hide HB321tile03_09
        hide HB321tile03_11
        hide HB321tile05_13
        hide HB321tile04_13  
        
        
    if nand1in3 == True and (xor1in2 == True or xor2in2 == True) and (xor1in1 == True or xor2in1 == True):
        image HB322tile03_09 = "r_r.png"
        show HB322tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if nor1in4 == True:
            image HB322tile04_11= "g_r.png"
            show HB322tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB322tile03_11 = "g_elbow_bl.png"
            show HB322tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB322tile05_13 = "g_elbow_tr.png"
            show HB322tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB322tile04_13 = "g_elbow_bl.png"
            show HB322tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB322tile04_11
            hide HB322tile03_11
            hide HB322tile05_13
            hide HB322tile04_13
    else:
        hide HB322tile04_11
        hide HB322tile03_09
        hide HB322tile03_11
        hide HB322tile05_13
        hide HB322tile04_13
        
        
    if (xor1in2 == True or xor2in2 == True) and nor1in1 == True and (xor1in3 == True or xor2in3 == True):
        image HB323tile03_09 = "g_r.png"
        show HB323tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if nand1in4 == True:
            image HB323tile04_11 = "g_r.png"
            show HB323tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB323tile03_11 = "g_elbow_bl.png"
            show HB323tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB323tile05_13 = "g_elbow_tr.png"
            show HB323tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB323tile04_13 = "g_elbow_bl.png"
            show HB323tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB323tile04_11
            hide HB323tile03_11
            hide HB323tile05_13
            hide HB323tile04_13
    else:
        hide HB323tile04_11
        hide HB323tile03_09
        hide HB323tile03_11
        hide HB323tile05_13
        hide HB323tile04_13
      
        
    if (xor1in1 == True or xor2in1 == True) and nor1in2 == True and (xor1in3 == True or xor2in3 == True):
        image HB324tile03_09 = "r_g.png"
        show HB324tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if nand1in4 == True:
            image HB324tile04_11 = "g_g.png"
            show HB324tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB324tile03_11 = "g_elbow_bl.png"
            show HB324tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB324tile05_13 = "g_elbow_tr.png"
            show HB324tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB324tile04_13 = "g_elbow_bl.png"
            show HB324tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB324tile04_11
            hide HB324tile03_11
            hide HB324tile05_13
            hide HB324tile04_13
    else:
        hide HB324tile04_11
        hide HB324tile03_09
        hide HB324tile03_11
        hide HB324tile05_13
        hide HB324tile04_13
     
        
    if (xor1in1 == True or xor2in1 == True) and nor1in3 == True and (xor1in2 == True or xor2in2 == True):
        image HB325tile03_09 = "r_g.png"
        show HB325tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        if nand1in4 == True:
            image HB325tile04_11 = "g_g.png"
            show HB325tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0) 
            image HB325tile03_11 = "g_elbow_bl.png"
            show HB325tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
            image HB325tile05_13 = "g_elbow_tr.png"
            show HB325tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
            image HB325tile04_13 = "g_elbow_bl.png"
            show HB325tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB325tile04_11
            hide HB325tile03_11
            hide HB325tile05_13
            hide HB325tile04_13
    else:
        hide HB325tile04_11
        hide HB325tile03_09
        hide HB325tile03_11
        hide HB325tile05_13
        hide HB325tile04_13
       
    


#win conditions ********
    if nand1in1 and (xor1in2 or xor2in2) and (xor1in3 or xor2in3) and nor1in4:         
        image HB12tile02_09 = "xor_Gate.png"
        show HB12tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HB12tile02_10 = "xor_Gate.png"
        show HB12tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image HB11tile07_02 = "nor_Gate.png"
        show HB11tile07_02 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image HB11tile07_08 = "nand_Gate.png"
        show HB11tile07_08 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image HB11end2 = "light_r_on.png"
        show HB11end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardBWin
        $lgHardB_solved = True
        jump lgHard_win2

  
    if attempts == 0:
        image HB12tile02_09 = "xor_Gate.png"
        show HB12tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HB12tile02_10 = "xor_Gate.png"
        show HB12tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image HB12tile07_02 = "nor_Gate.png"
        show HB12tile07_02 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image HB12tile07_08 = "nand_Gate.png"
        show HB12tile07_08 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_lgHardBLose
        $lgHard_attempts +=1
        jump lgHard_lose2
    
    jump gamefileHB3

screen logicgatesHB3:
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
        action Jump("hints_lgHardB3")
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
                drag_name "nor_gate"
                child "nor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nor1x ypos nor1y
                
            #or gates
            drag:
                drag_name "nand_gate"
                child "nand_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nand1x ypos nand1y
                
            #nand gate
            drag:
                drag_name "xor_gate1"
                child "xor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos xor1x ypos xor1y
                
            drag:
                drag_name "xor_gate2"
                child "xor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos xor2x ypos xor2y

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
                drag_name "nor return"
                child "cover.png"
                draggable False
                xpos 1148 ypos 88
           
            drag:
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88
                
            drag:
                drag_name "xor return"
                child "cover.png"
                draggable False
                xpos 1299 ypos 88
