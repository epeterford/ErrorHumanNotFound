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

label logicGate_hardC3:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
   
    image HC3tile01_00 = "r_horizontal.png"
    image HC3tile01_01 = "r_elbow_bl.png"
    
    show HC3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HC3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    
    image HC3tile02_01 = "r_r.png"
    image HC3tile02_02 = "XOR_Gate_blue.png"
    image HC3tile02_03 = "r_horizontal.png"
    image HC3tile02_04 = "r_horizontal.png"
    image HC3tile02_05 = "r_t_down.png"
    image HC3tile02_06 = "r_horizontal.png"
    image HC3tile02_07 = "r_horizontal.png"
    image HC3tile02_08 = "r_horizontal.png"
    image HC3tile02_09 = "r_elbow_bl.png"

    show HC3tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show HC3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HC3tile03_00 = "r_horizontal.png"
    image HC3tile03_01 = "r_elbow_tl.png"
    image HC3tile03_05 = "r_vertical.png"
    image HC3tile03_09 = "r_y.png"
    image HC3tile03_10 = "OR_Gate_blue.png"
    image HC3tile03_11 = "y_elbow_bl.png"
    
    show HC3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HC3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HC3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show HC3tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HC3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show HC3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    image HC3tile04_05 = "r_r.png"
    image HC3tile04_06 = "NONE_Gate.png"
    image HC3tile04_07 = "y_horizontal.png"
    image HC3tile04_08 = "y_horizontal.png"
    image HC3tile04_09 = "y_elbow_tl.png"
    image HC3tile04_11 = "y_vertical.png"

    show HC3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show HC3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HC3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show HC3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show HC3tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show HC3tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HC3tile05_00 = "r_horizontal.png"
    image HC3tile05_01 = "r_t_down.png"
    image HC3tile05_02 = "r_horizontal.png"
    image HC3tile05_03 = "r_horizontal.png"
    image HC3tile05_04 = "r_horizontal.png"
    image HC3tile05_05 = "r_t_up.png"
    image HC3tile05_06 = "r_horizontal.png"
    image HC3tile05_07 = "r_horizontal.png"
    image HC3tile05_08 = "r_elbow_bl.png"
    image HC3tile05_11 = "y_y.png"
    image HC3tile05_12 = "AND_Gate_blue.png"
    image HC3tile05_13 = "y_horizontal.png"
    
    show HC3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show HC3tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    image HC3tile06_01 = "r_g.png"
    image HC3tile06_02 = "NONE_Gate.png"
    image HC3tile06_03 = "y_horizontal.png"
    image HC3tile06_04 = "y_horizontal.png"
    image HC3tile06_05 = "y_elbow_bl.png"
    image HC3tile06_08 = "r_vertical.png"
    image HC3tile06_11 = "y_vertical.png"
    
    show HC3tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show HC3tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show HC3tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show HC3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show HC3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show HC3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show HC3tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HC3tile07_00 = "g_horizontal.png"
    image HC3tile07_01 = "g_t_up.png"
    image HC3tile07_02 = "g_elbow_bl.png"
    image HC3tile07_05 = "y_vertical.png"
    image HC3tile07_08 = "r_y.png"
    image HC3tile07_09 = "NONE_Gate.png"
    image HC3tile07_10 = "y_horizontal.png"
    image HC3tile07_11 = "y_elbow_tl.png"
    
    show HC3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show HC3tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    
    image HC3tile08_02 = "g_vertical.png"
    image HC3tile08_05 = "y_g.png"
    image HC3tile08_06 = "NONE_Gate.png"
    image HC3tile08_07 = "y_horizontal.png"
    image HC3tile08_08 = "y_elbow_tl.png"
    
    show HC3tile08_02 at Position(xpos = 586, xanchor = 0, ypos = 833, yanchor = 0)
    show HC3tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show HC3tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show HC3tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show HC3tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    

    image HC3tile09_02 = "g_elbow_tr.png"
    image HC3tile09_03 = "g_horizontal.png"
    image HC3tile09_04 = "g_horizontal.png"
    image HC3tile09_05 = "g_elbow_tl.png"
    
    show HC3tile09_02 at Position(xpos = 586, xanchor = 0, ypos = 908, yanchor = 0)
    show HC3tile09_03 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
    show HC3tile09_04 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
    show HC3tile09_05 at Position(xpos = 811, xanchor = 0, ypos = 908, yanchor = 0)

    #start points
    image HC3start1 = "light_r_on.png"
    show HC3start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HC3start2 = "light_r_on.png"
    show HC3start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HC3start3 = "light_r_on.png"
    show HC3start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HC3start4 = "light_g_on.png"
    show HC3start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image HC3end3 = "light_g_off.png"
    show HC3end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)


    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""
    $ gate_name = ""
    $ slot_name = ""

    #initial value assignment for dragables
    $ or1x = 998
    $ or1y = 88
    $ nor1x = 1148
    $ nor1y = 88
    $ xor1x = 1299
    $ xor1y = 88
    $ nor2x = 1148
    $ nor2y = 88
    
    #gate values
    $ gate1x = 886
    $ gate1y = 533
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 886
    $ gate3y = 833
    $ gate4x = 1111
    $ gate4y = 758
    
    # check conditons for locations
    $ or1in1 = False
    $ nor1in1 = False
    $ xor1in1 = False
    $ nor2in1 = False
    $ or1in2 = False
    $ nor1in2 = False
    $ xor1in2 = False
    $ nor2in2 = False
    $ or1in3 = False
    $ nor1in3 = False
    $ xor1in3 = False
    $ nor2in3 = False
    $ or1in4 = False
    $ nor1in4 = False
    $ xor1in4 = False
    $ nor2in4 = False   
    
    #attempts for players
    $ attempts = 6
 
    jump gamefileHC3
    
    
label gamefileHC3:
    
    #calls game screen
    call screen logicgatesHC3
    
    #the first logic gate *******************************************************************************
    if gate_name == "or_gate":
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
            if nor2in1 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in1 = False
                
            #sets values for checks
            $ or1x = gate1x
            $ or1y = gate1y
            $ or1in1 = True
            $ or1in2 = False
            $ or1in3 = False
            $ or1in4 = False
            
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
            if nor2in2 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in2 = False
                
            #sets values for checks
            $ or1x = gate2x
            $ or1y = gate2y
            $ or1in2 = True
            $ or1in1 = False
            $ or1in3 = False
            $ or1in4 = False
            
        #gate slot nuHCer three*******************************        
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
            if nor2in3 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in3 = False
                
            #sets values for checks
            $ or1x = gate3x
            $ or1y = gate3y
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = True
            $ or1in4 = False
            
        if slot_name == "gate slot four":
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False
            if nor2in4 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in4 = False
                
            #sets values for checks
            $ or1x = gate4x
            $ or1y = gate4y
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = False
            $ or1in4 = True
            
        if slot_name == "or return":
            $ or1x = 698
            $ or1y = 88
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = False
            $ or1in4 = False
            
     #or gate section **********************************************************************       
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
               $ or1x = 698
               $ or1y = 88
               $ or1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False
            if nor2in1 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in1 = False
                
            #sets values for checks
            $ nor1x = gate1x
            $ nor1y = gate1y
            $ nor1in1 = True
            $ nor1in2 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False
            if nor2in2 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in2 = False
                
            #sets values for checks
            $ nor1x = gate2x
            $ nor1y = gate2y
            $ nor1in2 = True
            $ nor1in1 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot nuHCer three*******************************    
        if slot_name == "gate slot three":
            if or1in3 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
            if nor2in3 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in3 = False
                
            #sets values for checks
            $ nor1x = gate3x
            $ nor1y = gate3y
            $ nor1in2 = False
            $ nor1in1 = False
            $ nor1in3 = True
            $ nor1in4 = False
            
        if slot_name == "gate slot four":
            if or1in4 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False
            if nor2in4 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in4 = False
                
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
            if or1in1 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in1 = False
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if nor2in1 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in1 = False                

            #sets values for checks
            $ xor1x = gate1x
            $ xor1y = gate1y
            $ xor1in1 = True
            $ xor1in2 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in2 = False
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if nor2in2 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in2 = False  
                
            #sets values for checks
            $ xor1x = gate2x
            $ xor1y = gate2y
            $ xor1in2 = True
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot nuHCer three*******************************    
        if slot_name == "gate slot three":
            if or1in3 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in3 = False
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if nor2in3 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in3 = False
                
            #sets values for checks
            $ xor1x = gate3x
            $ xor1y = gate3y
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = True
            $ xor1in4 = False
            
        if slot_name == "gate slot four":
            if or1in4 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in4 = False
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if nor2in4 == True:
                $ nor2x = 1148
                $ nor2y = 88
                $ nor2in4 = False  
                
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

    if gate_name == "nor_gate2":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in1 = False
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False                

            #sets values for checks
            $ nor2x = gate1x
            $ nor2y = gate1y
            $ nor2in1 = True
            $ nor2in2 = False
            $ nor2in3 = False
            $ nor2in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in2 = False
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False  
                
            #sets values for checks
            $ nor2x = gate2x
            $ nor2y = gate2y
            $ nor2in2 = True
            $ nor2in1 = False
            $ nor2in3 = False
            $ nor2in4 = False
            
        #gate slot nuHCer three*******************************    
        if slot_name == "gate slot three":
            if or1in3 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in3 = False
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
                
            #sets values for checks
            $ nor2x = gate3x
            $ nor2y = gate3y
            $ nor2in2 = False
            $ nor2in1 = False
            $ nor2in3 = True
            $ nor2in4 = False
            
        if slot_name == "gate slot four":
            if or1in4 == True:
                $ or1x = 698
                $ or1y = 88
                $ or1in4 = False
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor1in4 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in4 = False  
                
            #sets values for checks
            $ nor2x = gate4x
            $ nor2y = gate4y
            $ nor2in2 = False
            $ nor2in1 = False
            $ nor2in3 = False
            $ nor2in4 = True
        
        if slot_name == "nor return":
            $ nor2x = 1148
            $ nor2y = 88
            $ nor2in2 = False
            $ nor2in1 = False
            $ nor2in3 = False
            $ nor2in4 = False
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "or return" or slot_name == "nor return" or slot_name == "xor return"):
       $ temp_slot = slot_name
       $ temp_gate = gate_name
       if temp_slot != "" and temp_gate != "":
           $ attempts -=1

       
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            if slot_name == "or return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "nor_gate2":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "xor_gate1":
                $ attempts +=1   
            if slot_name == "or return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "nor_gate2":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nor_gate2":
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
        
    if or1in1:
        image HC31tile03_09 = "r_r.png"
        image HC31tile03_11 = "r_elbow_bl.png"
        show HC31tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show HC31tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image HC31tile04_07 = "r_horizontal.png"
        image HC31tile04_08 = "r_horizontal.png"
        image HC31tile04_09 = "r_elbow_tl.png"
        image HC31tile04_11 = "r_vertical.png"
        show HC31tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show HC31tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show HC31tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        show HC31tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HC31tile05_11 = "r_y.png"
        show HC31tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC31tile03_09
        hide HC31tile03_11
        hide HC31tile04_07
        hide HC31tile04_08
        hide HC31tile04_09
        hide HC31tile04_11
        hide HC31tile05_11    
        
    if xor1in1 == True:
        image HC33tile03_09 = "r_r.png"
        image HC33tile03_11 = "r_elbow_bl.png"
        show HC33tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show HC33tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image HC33tile04_07 = "r_horizontal.png"
        image HC33tile04_08 = "r_horizontal.png"
        image HC33tile04_09 = "r_elbow_tl.png"
        image HC33tile04_11 = "r_vertical.png"
        show HC33tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show HC33tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show HC33tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        show HC33tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HC33tile05_11 = "r_y.png"
        show HC33tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC33tile03_09
        hide HC33tile03_11
        hide HC33tile04_07
        hide HC33tile04_08
        hide HC33tile04_09
        hide HC33tile04_11
        hide HC33tile05_11
        
    if nor1in1 == True or nor2in1 == True:
        image HC35tile03_09 = "r_g.png"
        image HC35tile03_11 = "g_elbow_bl.png"
        show HC35tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show HC35tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image HC35tile04_07 = "g_horizontal.png"
        image HC35tile04_08 = "g_horizontal.png"
        image HC35tile04_09 = "g_elbow_tl.png"
        image HC35tile04_11 = "g_vertical.png"
        show HC35tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show HC35tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show HC35tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        show HC35tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HC35tile05_11 = "g_y.png"
        show HC35tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC35tile03_09
        hide HC35tile03_11
        hide HC35tile04_07
        hide HC35tile04_08
        hide HC35tile04_09
        hide HC35tile04_11
        hide HC35tile05_11

    if or1in2 == True:
        image HC32tile06_03 = "g_horizontal.png"
        image HC32tile06_04 = "g_horizontal.png"
        image HC32tile06_05 = "g_elbow_bl.png"
        show HC32tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC32tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC32tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        image HC32tile07_05 = "g_vertical.png"
        show HC32tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
        image HC32tile08_05 = "g_g.png"
        show HC32tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        if xor1in3 == True:
            image HC37tile07_08 = "r_R.png"
            show HC37tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC37tile08_07 = "R_horizontal.png"
            image HC37tile08_08 = "R_elbow_tl.png"
            show HC37tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC37tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if nor1in4 == True or nor2in4 == True:
                image HC39tile05_11 = "y_G.png"
                show HC39tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC39tile06_11 = "g_vertical.png"
                show HC39tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC39tile07_10 = "g_horizontal.png"
                image HC39tile07_11 = "g_elbow_tl.png"
                show HC39tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC39tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
                
            else:
                hide HC39tile05_11
                hide HC39tile06_11
                hide HC39tile07_10
                hide HC39tile07_11
        else:
            hide HC37tile07_08
            hide HC37tile08_07
            hide HC37tile08_08
            hide HC39tile05_11
            hide HC39tile06_11
            hide HC39tile07_10
            hide HC39tile07_11            
            
        if nor1in3 == True or nor2in3 == True:
            image HC38tile07_08 = "r_r.png"
            show HC38tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC38tile08_07 = "r_horizontal.png"
            image HC38tile08_08 = "r_elbow_tl.png"
            show HC38tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC38tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if nor1in4 == True or nor2in4 == True:
                image HC310tile05_11 = "y_g.png"
                show HC310tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC310tile06_11 = "g_vertical.png"
                show HC310tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC310tile07_10 = "g_horizontal.png"
                image HC310tile07_11 = "g_elbow_tl.png"
                show HC310tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC310tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC310tile05_11
                hide HC310tile06_11
                hide HC310tile07_10
                hide HC310tile07_11
            if xor1in4 == True:
                image HC311tile05_11 = "y_r.png"
                show HC311tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC311tile06_11 = "r_vertical.png"
                show HC311tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC311tile07_10 = "r_horizontal.png"
                image HC311tile07_11 = "r_elbow_tl.png"
                show HC311tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC311tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC311tile05_11
                hide HC311tile06_11
                hide HC311tile07_10
                hide HC311tile07_11
        else:
            hide HC38tile07_08
            hide HC38tile08_07
            hide HC38tile08_08
            hide HC310tile05_11
            hide HC310tile06_11
            hide HC310tile07_10
            hide HC310tile07_11
            hide HC311tile05_11
            hide HC311tile06_11
            hide HC311tile07_10
            hide HC311tile07_11
    else:
        hide HC37tile07_08
        hide HC37tile08_07
        hide HC37tile08_08
        hide HC32tile06_03
        hide HC32tile06_04
        hide HC32tile06_05
        hide HC32tile07_05
        hide HC32tile08_05
        hide HC38tile07_08
        hide HC38tile08_07
        hide HC38tile08_08
        hide HC39tile05_11
        hide HC39tile06_11
        hide HC39tile07_10
        hide HC39tile07_11
        hide HC310tile05_11
        hide HC310tile06_11
        hide HC310tile07_10
        hide HC310tile07_11
        hide HC311tile05_11
        hide HC311tile06_11
        hide HC311tile07_10
        hide HC311tile07_11
        
    if xor1in2 == True:
        image HC34tile06_03 = "g_horizontal.png"
        image HC34tile06_04 = "g_horizontal.png"
        image HC34tile06_05 = "g_elbow_bl.png"
        show HC34tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC34tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC34tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        image HC34tile07_05 = "g_vertical.png"
        show HC34tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
        image HC34tile08_05 = "g_g.png"
        show HC34tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        if or1in3 == True:
            image HC312tile07_08 = "r_g.png"
            show HC312tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC312tile08_07 = "g_horizontal.png"
            image HC312tile08_08 = "g_elbow_tl.png"
            show HC312tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC312tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if nor1in4 == True or nor2in4 == True:
                image HC314tile05_11 = "y_r.png"
                show HC314tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC314tile06_11 = "r_vertical.png"
                show HC314tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC314tile07_10 = "r_horizontal.png"
                image HC314tile07_11 = "r_elbow_tl.png"
                show HC314tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC314tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC314tile05_11
                hide HC314tile06_11
                hide HC314tile07_10
                hide HC314tile07_11
        else:
            hide HC312tile07_08
            hide HC312tile08_07
            hide HC312tile08_08
            hide HC314tile05_11
            hide HC314tile06_11
            hide HC314tile07_10
            hide HC314tile07_11
            
            
        if nor1in3 == True or nor2in3 == True:
            image HC313tile07_08 = "r_r.png"
            show HC313tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC313tile08_07 = "r_horizontal.png"
            image HC313tile08_08 = "r_elbow_tl.png"
            show HC313tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC313tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if nor1in4 == True or nor2in4 == True:
                image HC3145tile05_11 = "y_g.png"
                show HC3145tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC3145tile06_11 = "g_vertical.png"
                show HC3145tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC3145tile07_10 = "g_horizontal.png"
                image HC3145tile07_11 = "g_elbow_tl.png"
                show HC3145tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC3145tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC3145tile05_11
                hide HC3145tile06_11
                hide HC3145tile07_10
                hide HC3145tile07_11
            if or1in4 == True:
                image HC315tile05_11 = "y_r.png"
                show HC315tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC315tile06_11 = "r_vertical.png"
                show HC315tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC315tile07_10 = "r_horizontal.png"
                image HC315tile07_11 = "r_elbow_tl.png"
                show HC315tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC315tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC315tile05_11
                hide HC315tile06_11
                hide HC315tile07_10
                hide HC315tile07_11
        else:
            hide HC313tile07_08
            hide HC313tile08_07
            hide HC313tile08_08
            hide HC3145tile05_11
            hide HC3145tile06_11
            hide HC3145tile07_10
            hide HC3145tile07_11
            hide HC315tile05_11
            hide HC315tile06_11
            hide HC315tile07_10
            hide HC315tile07_11
    else:
        hide HC34tile06_03
        hide HC34tile06_04
        hide HC34tile06_05
        hide HC34tile07_05
        hide HC34tile08_05
        hide HC312tile07_08
        hide HC312tile08_07
        hide HC312tile08_08
        hide HC314tile05_11
        hide HC314tile06_11
        hide HC314tile07_10
        hide HC314tile07_11
        hide HC313tile07_08
        hide HC313tile08_07
        hide HC313tile08_08
        hide HC3145tile05_11
        hide HC3145tile06_11
        hide HC3145tile07_10
        hide HC3145tile07_11
        hide HC315tile05_11
        hide HC315tile06_11
        hide HC315tile07_10
        hide HC315tile07_11

    if nor1in2 == True or nor2in2 == True:
        image HC36tile06_03 = "r_horizontal.png"
        image HC36tile06_04 = "r_horizontal.png"
        image HC36tile06_05 = "r_elbow_bl.png"
        show HC36tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC36tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HC36tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        image HC36tile07_05 = "r_vertical.png"
        show HC36tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
        image HC36tile08_05 = "r_g.png"
        show HC36tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        if or1in3 == True:
            image HC316tile07_08 = "r_g.png"
            show HC316tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC316tile08_07 = "g_horizontal.png"
            image HC316tile08_08 = "g_elbow_tl.png"
            show HC316tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC316tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if xor1in4 == True:
                image HC322tile05_11 = "y_g.png"
                show HC322tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC322tile06_11 = "g_vertical.png"
                show HC322tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC322tile07_10 = "g_horizontal.png"
                image HC322tile07_11 = "g_elbow_tl.png"
                show HC322tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC322tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC322tile05_11
                hide HC322tile06_11
                hide HC322tile07_10
                hide HC322tile07_11
            if nor1in4 == True or nor2in4 == True:
                image HC324tile05_11 = "y_r.png"
                show HC324tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC324tile06_11 = "r_vertical.png"
                show HC324tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC324tile07_10 = "r_horizontal.png"
                image HC324tile07_11 = "r_elbow_tl.png"
                show HC324tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC324tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC324tile05_11
                hide HC324tile06_11
                hide HC324tile07_10
                hide HC324tile07_11
        else:
            hide HC316tile07_08
            hide HC316tile08_07
            hide HC316tile08_08
            hide HC324tile05_11
            hide HC324tile06_11
            hide HC324tile07_10
            hide HC324tile07_11
            hide HC322tile05_11
            hide HC322tile06_11
            hide HC322tile07_10
            hide HC322tile07_11
            
        if nor1in3 == True or nor2in3 == True:
            image HC317tile07_08 = "r_r.png"
            show HC317tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC317tile08_07 = "r_horizontal.png"
            image HC317tile08_08 = "r_elbow_tl.png"
            show HC317tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC317tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if or1in4 == True:
                image HC320tile05_11 = "y_r.png"
                show HC320tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC320tile06_11 = "r_vertical.png"
                show HC320tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC320tile07_10 = "r_horizontal.png"
                image HC320tile07_11 = "r_elbow_tl.png"
                show HC320tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC320tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC320tile05_11
                hide HC320tile06_11
                hide HC320tile07_10
                hide HC320tile07_11
            if xor1in4 == True:
                image HC321tile05_11 = "y_r.png"
                show HC321tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC321tile06_11 = "r_vertical.png"
                show HC321tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC321tile07_10 = "r_horizontal.png"
                image HC321tile07_11 = "r_elbow_tl.png"
                show HC321tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC321tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC321tile05_11
                hide HC321tile06_11
                hide HC321tile07_10
                hide HC321tile07_11
        else:
            hide HC317tile07_08
            hide HC317tile08_07
            hide HC317tile08_08
            hide HC321tile05_11
            hide HC321tile06_11
            hide HC321tile07_10
            hide HC321tile07_11
            hide HC320tile05_11
            hide HC320tile06_11
            hide HC320tile07_10
            hide HC320tile07_11
            
        if xor1in3 == True:
            image HC318tile07_08 = "r_g.png"
            show HC318tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)   
            image HC318tile08_07 = "g_horizontal.png"
            image HC318tile08_08 = "g_elbow_tl.png"
            show HC318tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
            show HC318tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
            if or1in4 == True:
                image HC319tile05_11 = "y_g.png"
                show HC319tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC319tile06_11 = "g_vertical.png"
                show HC319tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC319tile07_10 = "g_horizontal.png"
                image HC319tile07_11 = "g_elbow_tl.png"
                show HC319tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC319tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC319tile05_11
                hide HC319tile06_11
                hide HC319tile07_10
                hide HC319tile07_11
            if nor1in4 == True or nor2in4 == True:
                image HC323tile05_11 = "y_r.png"
                show HC323tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
                image HC323tile06_11 = "r_vertical.png"
                show HC323tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                image HC323tile07_10 = "r_horizontal.png"
                image HC323tile07_11 = "r_elbow_tl.png"
                show HC323tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
                show HC323tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            else:
                hide HC323tile05_11
                hide HC323tile06_11
                hide HC323tile07_10
                hide HC323tile07_11
        else:
            hide HC318tile07_08
            hide HC318tile08_07
            hide HC318tile08_08
            hide HC323tile05_11
            hide HC323tile06_11
            hide HC323tile07_10
            hide HC323tile07_11
            hide HC319tile05_11
            hide HC319tile06_11
            hide HC319tile07_10
            hide HC319tile07_11
    
    else:
        hide HC36tile06_03
        hide HC36tile06_04
        hide HC36tile06_05
        hide HC36tile07_05
        hide HC36tile08_05
        hide HC316tile07_08
        hide HC316tile08_07
        hide HC316tile08_08
        hide HC324tile05_11
        hide HC324tile06_11
        hide HC324tile07_10
        hide HC324tile07_11
        hide HC322tile05_11
        hide HC322tile06_11
        hide HC322tile07_10
        hide HC322tile07_11
        hide HC318tile07_08
        hide HC318tile08_07
        hide HC318tile08_08
        hide HC323tile05_11
        hide HC323tile06_11
        hide HC323tile07_10
        hide HC323tile07_11
        hide HC319tile05_11
        hide HC319tile06_11
        hide HC319tile07_10
        hide HC319tile07_11
        hide HC317tile07_08
        hide HC317tile08_07
        hide HC317tile08_08
        hide HC321tile05_11
        hide HC321tile06_11
        hide HC321tile07_10
        hide HC321tile07_11
        hide HC320tile05_11
        hide HC320tile06_11
        hide HC320tile07_10
        hide HC320tile07_11
        
        
    if or1in1 == True and xor1in2 == True and (nor1in3 == True or nor2in3 == True) and (nor1in4 == True or nor2in4 == True):
        image HC325tile05_11 = "r_g.png"
        show HC325tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC325tile05_13 = "r_horizontal.png"
        show HC325tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC325tile05_11
        hide HC325tile05_13

    if or1in1 == True and xor1in3 == True and (nor1in2 == True or nor2in2 == True) and (nor1in4 == True or nor2in4 == True):
        image HC326tile05_11 = "r_r.png"
        show HC326tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC326tile05_13 = "r_horizontal.png"
        show HC326tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC326tile05_11
        hide HC326tile05_13
    
    if or1in1 == True and xor1in4 == True and (nor1in3 == True or nor2in3 == True) and (nor1in2 == True or nor2in2 == True):
        image HC327tile05_11 = "r_r.png"
        show HC327tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC327tile05_13 = "r_horizontal.png"
        show HC327tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC327tile05_11
        hide HC327tile05_13

    if or1in2 == True and xor1in1 == True and (nor1in3 == True or nor2in3 == True) and (nor1in4 == True or nor2in4 == True):
        image HC328tile05_11 = "r_g.png"
        show HC328tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC328tile05_13 = "y_horizontal.png"
        show HC328tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC328tile05_11
        hide HC328tile05_13

    if or1in2 == True and xor1in3 == True and (nor1in1 == True or nor2in1 == True) and (nor1in4 == True or nor2in4 == True):
        image HC329tile05_11 = "g_g.png"
        show HC329tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC329tile05_13 = "g_horizontal.png"
        show HC329tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC329tile05_11
        hide HC329tile05_13

    if or1in2 == True and xor1in4 == True and (nor1in3 == True or nor2in3 == True) and (nor1in1 == True or nor2in1 == True):
        image HC330tile05_11 = "g_r.png"
        show HC330tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC330tile05_13 = "r_horizontal.png"
        show HC330tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC330tile05_11
        hide HC330tile05_13

    if or1in3 == True and xor1in2 == True and (nor1in1 == True or nor2in1 == True) and (nor1in4 == True or nor2in4 == True):
        image HC331tile05_11s = "g_r.png"
        show HC331tile05_11s at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC331tile05_13 = "r_horizontal.png"
        show HC331tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC331tile05_11s
        hide HC331tile05_13

    if or1in3 == True and xor1in1 == True and (nor1in2 == True or nor2in2 == True) and (nor1in4 == True or nor2in4 == True):
        image HC332tile05_11 = "r_r.png"
        show HC332tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC332tile05_13 = "r_horizontal.png"
        show HC332tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC332tile05_11
        hide HC332tile05_13

    if or1in3 == True and xor1in4 == True and (nor1in1 == True or nor2in1 == True) and (nor1in2 == True or nor2in2 == True):
        image HC333tile05_11 = "g_g.png"
        show HC333tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC333tile05_13 = "g_horizontal.png"
        show HC333tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC333tile05_11
        hide HC333tile05_13

    if or1in4 == True and xor1in2 == True and (nor1in1 == True or nor2in1 == True) and (nor1in3 == True or nor2in3 == True):
        image HC334tile05_11 = "g_r.png"
        show HC334tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC334tile05_13 = "r_horizontal.png"
        show HC334tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC334tile05_11
        hide HC334tile05_13

    if or1in4 == True and xor1in1 == True and (nor1in2 == True or nor2in2 == True) and (nor1in3 == True or nor2in3 == True):
        image HC335tile05_11 = "r_r.png"
        show HC335tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC335tile05_13 = "r_horizontal.png"
        show HC335tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC335tile05_11
        hide HC335tile05_13

    if or1in4 == True and xor1in3 == True and (nor1in1 == True or nor2in1 == True) and (nor1in2 == True or nor2in2 == True):
        image HC336tile05_11 = "g_g.png"
        show HC336tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HC336tile05_13 = "g_horizontal.png"
        show HC336tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HC336tile05_11
        hide HC336tile05_13

        
        
#win conditions ********
    if (or1in2 and xor1in3 and (nor1in1 or nor2in1) and (nor1in4 or nor2in4 )) or (or1in3 and xor1in4 and (nor1in1 or nor2in1) and (nor1in2 or nor2in2)) or (or1in4 and xor1in3 and (nor1in1 or nor2in1) and (nor1in2 or nor2in2)):         
        image HC1270tile02_09 = "xor_Gate.png"
        show HC1270tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HC1270tile02_10 = "nor_Gate.png"
        show HC1270tile02_10 at Position(xpos = nor2x, xanchor = 0, ypos = nor2y, yanchor = 0)
        image HC1170tile07_02 = "or_Gate.png"
        show HC1170tile07_02 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HC1170tile07_08 = "nor_Gate.png"
        show HC1170tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image HC1170end2 = "light_g_on.png"
        show HC1170end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardCWin
        $lgHardC_solved = True
        jump lgHard_done

  
    if attempts == 0:
        image HC1270tile02_09 = "xor_Gate.png"
        show HC1270tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HC1270tile02_10 = "nor_Gate.png"
        show HC1270tile02_10 at Position(xpos = nor2x, xanchor = 0, ypos = nor2y, yanchor = 0)
        image HC1270tile07_02 = "or_Gate.png"
        show HC1270tile07_02 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HC1270tile07_08 = "nor_Gate.png"
        show HC1270tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_lgHardCLose
        $lgHard_attempts +=1
        jump lgHard_lose3
    
    jump gamefileHC3

screen logicgatesHC3:
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
        action Jump("hints_lgHardC3")
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
                drag_name "or_gate"
                child "or_Gate.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y
                
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
                drag_name "nor_gate2"
                child "nor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nor2x ypos nor2y

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
                drag_name "or return"
                child "cover.png"
                draggable False
                xpos 848 ypos 88
           
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
