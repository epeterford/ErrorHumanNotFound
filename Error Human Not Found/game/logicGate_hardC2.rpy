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

label logicGate_hardC2:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #row 1 (row has a light)
    image HC2tile01_00 = "r_horizontal.png"
    image HC2tile01_01 = "r_elbow_bl.png"
    
    show HC2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HC2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    

    image HC2tile02_01 = "r_r.png"
    image HC2tile02_02 = "NOR_Gate_blue.png"
    image HC2tile02_03 = "g_horizontal.png"
    image HC2tile02_04 = "g_elbow_bl.png"

    show HC2tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show HC2tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show HC2tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HC2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HC2tile03_00 = "r_horizontal.png"
    image HC2tile03_01 = "r_t_left.png"
    image HC2tile03_04 = "g_g.png"
    image HC2tile03_05 = "NONE_Gate.png"
    image HC2tile03_06 = "y_horizontal.png"
    image HC2tile03_07 = "y_horizontal.png"
    image HC2tile03_08 = "y_horizontal.png"
    image HC2tile03_09 = "y_horizontal.png"
    image HC2tile03_10 = "y_elbow_bl.png"
    
    show HC2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HC2tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HC2tile04_01 = "r_g.png"
    image HC2tile04_02 = "NAND_Gate_blue.png"
    image HC2tile04_03 = "g_horizontal.png"
    image HC2tile04_04 = "g_t_left.png"
    image HC2tile04_10 = "y_y.png"
    image HC2tile04_11 = "AND_Gate_blue.png"
    image HC2tile04_12 = "y_elbow_bl.png"
    
    show HC2tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show HC2tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show HC2tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show HC2tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HC2tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show HC2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show HC2tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HC2tile05_00 = "g_horizontal.png"
    image HC2tile05_01 = "g_t_left.png"
    image HC2tile05_04 = "g_y.png"
    image HC2tile05_05 = "NONE_Gate.png"
    image HC2tile05_06 = "y_horizontal.png"
    image HC2tile05_07 = "y_horizontal.png"
    image HC2tile05_08 = "y_elbow_bl.png"
    image HC2tile05_10 = "y_vertical.png"
    image HC2tile05_12 = "y_elbow_tr.png"
    image HC2tile05_13 = "y_horizontal.png"
    
    show HC2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show HC2tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image HC2tile06_01 = "g_g.png"
    image HC2tile06_02 = "NONE_Gate.png"
    image HC2tile06_03 = "y_horizontal.png"
    image HC2tile06_04 = "y_elbow_tl.png"
    image HC2tile06_08 = "y_g.png"
    image HC2tile06_09 = "NONE_Gate.png"
    image HC2tile06_10 = "y_elbow_tl.png"
    
    show HC2tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show HC2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show HC2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show HC2tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show HC2tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show HC2tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    show HC2tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HC2tile07_00 = "g_horizontal.png"
    image HC2tile07_01 = "g_t_up.png"
    image HC2tile07_02 = "g_horizontal.png"
    image HC2tile07_03 = "g_horizontal.png"
    image HC2tile07_04 = "g_horizontal.png"
    image HC2tile07_05 = "g_horizontal.png"
    image HC2tile07_06 = "g_horizontal.png"
    image HC2tile07_07 = "g_horizontal.png"
    image HC2tile07_08 = "g_elbow_tl.png"
    
    show HC2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show HC2tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    

    #start points
    image HC2start1 = "light_r_on.png"
    show HC2start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HC2start2 = "light_r_on.png"
    show HC2start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HC2start3 = "light_g_on.png"
    show HC2start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HC2start4 = "light_g_on.png"
    show HC2start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image HC2end3 = "light_g_off.png"
    show HC2end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)



    
    
    
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
    $ xor1x = 1300
    $ xor1y = 88
    $ xor2x = 1300
    $ xor2y = 88
    
    #gate values
    $ gate1x = 811
    $ gate1y = 458
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 811
    $ gate3y = 608
    $ gate4x = 1111
    $ gate4y = 683
    
    # check conditons for locations
    $ and1in1 = False
    $ nor1in1 = False
    $ xor1in1 = False
    $ xor2in1 = False
    $ and1in2 = False
    $ nor1in2 = False
    $ xor1in2 = False
    $ xor2in2 = False
    $ and1in3 = False
    $ nor1in3 = False
    $ xor1in3 = False
    $ xor2in3 = False
    $ and1in4 = False
    $ nor1in4 = False
    $ xor1in4 = False
    $ xor2in4 = False   
    
    #attempts for players
    $ attempts = 6
 
    jump gamefileHC2
    
    
label gamefileHC2:
    
    #calls game screen
    call screen logicgatesHC2
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False
            if xor1in1 == True:
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in1 = False
            if xor2in1 == True:
                $ xor2x = 1300
                $ xor2y = 88
                $ xor2in1 = False
                
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
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in2 = False
            if xor2in2 == True:
                $ xor2x = 1300
                $ xor2y = 88
                $ xor2in2 = False
                
            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = False
            
        #gate slot nuHCer three*******************************        
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor1in3 == True:
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1300
                $ xor2y = 88
                $ xor2in3 = False
                
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
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1300
                $ xor2y = 88
                $ xor2in4 = False
                
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
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in1 = False
            if xor2in1 == True:
                $ xor2x = 1300
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
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if xor1in2 == True:
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in2 = False
            if xor2in2 == True:
                $ xor2x = 1300
                $ xor2y = 88
                $ xor2in2 = False
                
            #sets values for checks
            $ nor1x = gate2x
            $ nor1y = gate2y
            $ nor1in2 = True
            $ nor1in1 = False
            $ nor1in3 = False
            $ nor1in4 = False
            
        #gate slot nuHCer three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if xor1in3 == True:
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1300
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
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if xor1in4 == True:
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1300
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
            if xor2in1 == True:
                $ xor2x = 1300
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
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if xor2in2 == True:
                $ xor2x = 1300
                $ xor2y = 88
                $ xor2in2 = False  
                
            #sets values for checks
            $ xor1x = gate2x
            $ xor1y = gate2y
            $ xor1in2 = True
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
        #gate slot nuHCer three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1300
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
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1300
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
            $ xor1x = 1300
            $ xor1y = 88
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False

    if gate_name == "xor_gate2":
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
                $ xor1x = 1300
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
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False
            if xor1in2 == True:
                $ xor1x = 1300
                $ xor1y = 88
                $ xor1in2 = False  
                
            #sets values for checks
            $ xor2x = gate2x
            $ xor2y = gate2y
            $ xor2in2 = True
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
        #gate slot nuHCer three*******************************    
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
                $ xor1x = 1300
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
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if nor1in4 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in4 = False
            if xor2in4 == True:
                $ xor1x = 1300
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
            $ xor2x = 1300
            $ xor2y = 88
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "and return" or slot_name == "nor return" or slot_name == "xor return"):
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
            if slot_name == "xor return" and gate_name == "xor_gate2":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "xor_gate1":
                $ attempts +=1  
            if slot_name == "nor return" and gate_name == "xor_gate2":
                $ attempts +=1    
            if slot_name == "and return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "xor_gate2":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nor_gate":
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
        
    if and1in1 == True:
        image HC21tile03_06 = "g_horizontal.png"
        image HC21tile03_07 = "g_horizontal.png"
        image HC21tile03_08 = "g_horizontal.png"
        image HC21tile03_09 = "g_horizontal.png"
        image HC21tile03_10 = "g_elbow_bl.png"
        show HC21tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show HC21tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show HC21tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HC21tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show HC21tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        image HC21tile04_10 = "g_y.png"
        show HC21tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC21tile03_06
        hide HC21tile03_07
        hide HC21tile03_08
        hide HC21tile03_09
        hide HC21tile03_10
        hide HC21tile04_10
        
    if nor1in1 == True:
        image HC22tile03_06 = "r_horizontal.png"
        image HC22tile03_07 = "r_horizontal.png"
        image HC22tile03_08 = "r_horizontal.png"
        image HC22tile03_09 = "r_horizontal.png"
        image HC22tile03_10 = "r_elbow_bl.png"
        show HC22tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show HC22tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show HC22tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HC22tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show HC22tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        image HC22tile04_10 = "r_y.png"
        show HC22tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC22tile03_06
        hide HC22tile03_07
        hide HC22tile03_08
        hide HC22tile03_09
        hide HC22tile03_10
        hide HC22tile04_10
        
    if xor1in1 == True or xor2in1:
        image HC23tile03_06 = "r_horizontal.png"
        image HC23tile03_07 = "r_horizontal.png"
        image HC23tile03_08 = "r_horizontal.png"
        image HC23tile03_09 = "r_horizontal.png"
        image HC23tile03_10 = "r_elbow_bl.png"
        show HC23tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show HC23tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show HC23tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HC23tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show HC23tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        image HC23tile04_10 = "r_y.png"
        show HC23tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC23tile03_06
        hide HC23tile03_07
        hide HC23tile03_08
        hide HC23tile03_09
        hide HC23tile03_10
        hide HC23tile04_10
        
    if and1in2 == True:
        image HC21tile06_03 = "g_horizontal.png"
        image HC21tile06_04 = "g_elbow_tl.png"
        show HC21tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC21tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HC21tile05_04 = "g_g.png"
        show HC21tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        if nor1in3 == True:
            image HC24tile06_08 = "r_g.png"
            show HC24tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC24tile05_06 = "r_horizontal.png"
            image HC24tile05_07 = "r_horizontal.png"
            image HC24tile05_08 = "r_elbow_bl.png"
            show HC24tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC24tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC24tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if xor1in4 == True or xor2in4 == True:
                image HC26tile06_10 = "g_elbow_tl.png"
                show HC26tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC26tile05_10 = "g_vertical.png"
                show HC26tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC26tile04_10 = "y_g.png"
                show HC26tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC26tile06_10
                hide HC26tile05_10
                hide HC26tile04_10    
        else:
            hide HC24tile06_08
            hide HC24tile05_06
            hide HC24tile05_07
            hide HC24tile05_08
            hide HC26tile06_10
            hide HC26tile05_10
            hide HC26tile04_10    
            
        if xor1in3 == True or xor2in3 == True:
            image HC25tile06_08 = "r_g.png"
            show HC25tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC25tile05_06 = "r_horizontal.png"
            image HC25tile05_07 = "r_horizontal.png"
            image HC25tile05_08 = "r_elbow_bl.png"
            show HC25tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC25tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC25tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if nor1in4 == True:
                image HC27tile06_10 = "r_elbow_tl.png"
                show HC27tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC27tile05_10 = "r_vertical.png"
                show HC27tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC27tile04_10 = "y_r.png"
                show HC27tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC27tile06_10
                hide HC27tile05_10
                hide HC27tile04_10
            if xor1in4 == True or xor2in4 == True:
                image HC28tile06_10 = "g_elbow_tl.png"
                show HC28tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC28tile05_10 = "g_vertical.png"
                show HC28tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC28tile04_10 = "y_g.png"
                show HC28tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC28tile06_10
                hide HC28tile05_10
                hide HC28tile04_10        
        else:
            hide HC25tile06_08
            hide HC25tile05_06
            hide HC25tile05_07
            hide HC25tile05_08
            hide HC27tile06_10
            hide HC27tile05_10
            hide HC27tile04_10
            hide HC28tile06_10
            hide HC28tile05_10
            hide HC28tile04_10
    else:
        hide HC21tile06_03
        hide HC21tile06_04
        hide HC21tile05_04
        hide HC25tile06_08
        hide HC25tile05_06
        hide HC25tile05_07
        hide HC25tile05_08
        hide HC24tile06_08
        hide HC24tile05_06
        hide HC24tile05_07
        hide HC24tile05_08
        hide HC26tile06_10
        hide HC26tile05_10
        hide HC26tile04_10    
        hide HC27tile06_10
        hide HC27tile05_10
        hide HC27tile04_10
        hide HC28tile06_10
        hide HC28tile05_10
        hide HC28tile04_10

    if nor1in2 == True:
        image HC22tile06_03 = "r_horizontal.png"
        image HC22tile06_04 = "r_elbow_tl.png"
        show HC22tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC22tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HC22tile05_04 = "g_r.png"
        show HC22tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        if and1in3 == True:
            image HC29tile06_08 = "r_g.png"
            show HC29tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC29tile05_06 = "r_horizontal.png"
            image HC29tile05_07 = "r_horizontal.png"
            image HC29tile05_08 = "r_elbow_bl.png"
            show HC29tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC29tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC29tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if xor1in4 == True or xor2in4 == True:
                image HC210tile06_10 = "g_elbow_tl.png"
                show HC210tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC210tile05_10 = "g_vertical.png"
                show HC210tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC210tile04_10 = "y_g.png"
                show HC210tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC210tile06_10
                hide HC210tile05_10
                hide HC210tile04_10
        else:
            hide HC29tile06_08
            hide HC29tile05_06
            hide HC29tile05_07
            hide HC29tile05_08
            hide HC210tile06_10
            hide HC210tile05_10
            hide HC210tile04_10
            
        if xor1in3 == True or xor2in3 == True:
            image HC211tile06_08 = "g_g.png"
            show HC211tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC211tile05_06 = "g_horizontal.png"
            image HC211tile05_07 = "g_horizontal.png"
            image HC211tile05_08 = "g_elbow_bl.png"
            show HC211tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC211tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC211tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if and1in4 == True:
                image HC212tile06_10 = "g_elbow_tl.png"
                show HC212tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC212tile05_10 = "g_vertical.png"
                show HC212tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC212tile04_10 = "y_g.png"
                show HC212tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC212tile06_10
                hide HC212tile05_10
                hide HC212tile04_10
            if xor1in4 == True or xor2in4 == True:
                image HC213tile06_10 = "r_elbow_tl.png"
                show HC213tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC213tile05_10 = "r_vertical.png"
                show HC213tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC213tile04_10 = "y_r.png"
                show HC213tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC213tile06_10
                hide HC213tile05_10
                hide HC213tile04_10        
        else:
            hide HC211tile06_08
            hide HC211tile05_06
            hide HC211tile05_07
            hide HC211tile05_08
            hide HC213tile06_10
            hide HC213tile05_10
            hide HC213tile04_10
            hide HC212tile06_10
            hide HC212tile05_10
            hide HC212tile04_10
    else:
        hide HC22tile06_03
        hide HC22tile06_04
        hide HC22tile05_04
        hide HC29tile06_08
        hide HC29tile05_06
        hide HC29tile05_07
        hide HC29tile05_08
        hide HC210tile06_10
        hide HC210tile05_10
        hide HC210tile04_10
        hide HC211tile06_08
        hide HC211tile05_06
        hide HC211tile05_07
        hide HC211tile05_08
        hide HC213tile06_10
        hide HC213tile05_10
        hide HC213tile04_10
        hide HC212tile06_10
        hide HC212tile05_10
        hide HC212tile04_10  

    if xor1in2 == True or xor2in2 == True:
        image HC23tile06_03 = "r_horizontal.png"
        image HC23tile06_04 = "r_elbow_tl.png"
        show HC23tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HC23tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HC23tile05_04 = "g_r.png"
        show HC23tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        if and1in3 == True:
            image HC214tile06_08 = "r_g.png"
            show HC214tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC214tile05_06 = "r_horizontal.png"
            image HC214tile05_07 = "r_horizontal.png"
            image HC214tile05_08 = "r_elbow_bl.png"
            show HC214tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC214tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC214tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if nor1in4 == True:
                image HC216tile06_10 = "r_elbow_tl.png"
                show HC216tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC216tile05_10 = "r_vertical.png"
                show HC216tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC216tile04_10 = "y_r.png"
                show HC216tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC216tile06_10
                hide HC216tile05_10
                hide HC216tile04_10
            if xor1in4 == True or xor2in4 == True:
                image HC217tile06_10 = "g_elbow_tl.png"
                show HC217tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC217tile05_10 = "g_vertical.png"
                show HC217tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC217tile04_10 = "y_g.png"
                show HC217tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC217tile06_10
                hide HC217tile05_10
                hide HC217tile04_10
        else:
            hide HC214tile06_08
            hide HC214tile05_06
            hide HC214tile05_07
            hide HC214tile05_08
            hide HC217tile06_10
            hide HC217tile05_10
            hide HC217tile04_10
            hide HC216tile06_10
            hide HC216tile05_10
            hide HC216tile04_10
        if nor1in3 == True:
            image  HC21415tile06_08 = "r_g.png"
            show  HC21415tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image  HC21415tile05_06 = "r_horizontal.png"
            image  HC21415tile05_07 = "r_horizontal.png"
            image  HC21415tile05_08 = "r_elbow_bl.png"
            show  HC21415tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show  HC21415tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show  HC21415tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if and1in4 == True:
                image HC218tile06_10 = "r_elbow_tl.png"
                show HC218tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC218tile05_10 = "r_vertical.png"
                show HC218tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC218tile04_10 = "y_r.png"
                show HC218tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC218tile06_10
                hide HC218tile05_10
                hide HC218tile04_10
            if xor1in4 == True or xor2in4 == True:
                image HC219tile06_10 = "g_elbow_tl.png"
                show HC219tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC219tile05_10 = "g_vertical.png"
                show HC219tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC219tile04_10 = "y_g.png"
                show HC219tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC219tile06_10
                hide HC219tile05_10
                hide HC219tile04_10
        else:
            hide  HC21415tile06_08
            hide  HC21415tile05_06
            hide  HC21415tile05_07
            hide  HC21415tile05_08
            hide HC219tile06_10
            hide HC219tile05_10
            hide HC219tile04_10
            hide HC218tile06_10
            hide HC218tile05_10
            hide HC218tile04_10
        if xor1in3 == True or xor2in3 == True:
            image HC215tile06_08 = "g_g.png"
            show HC215tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            image HC215tile05_06 = "g_horizontal.png"
            image HC215tile05_07 = "g_horizontal.png"
            image HC215tile05_08 = "g_elbow_bl.png"
            show HC215tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HC215tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HC215tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            if and1in4 == True:
                image HC220tile06_10 = "g_elbow_tl.png"
                show HC220tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC220tile05_10 = "g_vertical.png"
                show HC220tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC220tile04_10 = "y_g.png"
                show HC220tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC220tile06_10
                hide HC220tile05_10
                hide HC220tile04_10

            if nor1in4 == True:
                image HC221tile06_10 = "r_elbow_tl.png"
                show HC221tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
                image HC221tile05_10 = "r_vertical.png"
                show HC221tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                image HC221tile04_10 = "y_r.png"
                show HC221tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            else:
                hide HC221tile06_10
                hide HC221tile05_10
                hide HC221tile04_10
        else:
            hide HC215tile06_08
            hide HC215tile05_06
            hide HC215tile05_07
            hide HC215tile05_08
            hide HC221tile06_10
            hide HC221tile05_10
            hide HC221tile04_10
            hide HC220tile06_10
            hide HC220tile05_10
            hide HC220tile04_10
    else:
        hide HC23tile06_03
        hide HC23tile06_04
        hide HC23tile05_04
        hide HC214tile06_08
        hide HC214tile05_06
        hide HC214tile05_07
        hide HC214tile05_08
        hide HC217tile06_10
        hide HC217tile05_10
        hide HC217tile04_10
        hide HC216tile06_10
        hide HC216tile05_10
        hide HC216tile04_10
        hide  HC21415tile06_08
        hide  HC21415tile05_06
        hide  HC21415tile05_07
        hide  HC21415tile05_08
        hide HC219tile06_10
        hide HC219tile05_10
        hide HC219tile04_10
        hide HC218tile06_10
        hide HC218tile05_10
        hide HC218tile04_10
        hide HC215tile06_08
        hide HC215tile05_06
        hide HC215tile05_07
        hide HC215tile05_08
        hide HC221tile06_10
        hide HC221tile05_10
        hide HC221tile04_10
        hide HC220tile06_10
        hide HC220tile05_10
        hide HC220tile04_10
    
        
    if and1in1 == True and nor1in2 == True and (xor1in3 == True or xor2in3 == True) and (xor1in4 == True or xor2in4 == True):
        image HC233tile04_12 = "r_elbow_bl.png"
        show HC233tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC233tile05_12 = "r_elbow_tr.png"
        image HC233tile05_13 = "r_horizontal.png"
        show HC233tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC233tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC233tile04_10 = "g_r.png"
        show HC233tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC233tile04_10
        hide HC233tile04_12
        hide HC233tile05_12
        hide HC233tile05_13  
    if and1in1 == True and nor1in3 == True and (xor1in2 == True or xor2in2 == True) and (xor1in4 == True or xor2in4 == True):
        image HC232tile04_12 = "g_elbow_bl.png"
        show HC232tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC232tile05_12 = "g_elbow_tr.png"
        image HC232tile05_13 = "g_horizontal.png"
        show HC232tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC232tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC232tile04_10 = "g_g.png"
        show HC232tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC232tile04_10
        hide HC232tile04_12
        hide HC232tile05_12
        hide HC232tile05_13  
    if and1in1 == True and nor1in4 == True and (xor1in3 == True or xor2in3 == True) and (xor1in2 == True or xor2in2 == True):
        image HC231tile04_12 = "r_elbow_bl.png"
        show HC231tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC231tile05_12 = "r_elbow_tr.png"
        image HC231tile05_13 = "r_horizontal.png"
        show HC231tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC231tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC231tile04_10 = "g_r.png"
        show HC231tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC231tile04_10
        hide HC231tile04_12
        hide HC231tile05_12
        hide HC231tile05_13  
    if and1in2 == True and nor1in1 == True and (xor1in3 == True or xor2in3 == True) and (xor1in4 == True or xor2in4 == True):
        image HC230tile04_12 = "r_elbow_bl.png"
        show HC230tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC230tile05_12 = "r_elbow_tr.png"
        image HC230tile05_13 = "r_horizontal.png"
        show HC230tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC230tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC230tile04_10 = "r_g.png"
        show HC230tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC230tile04_10
        hide HC230tile04_12
        hide HC230tile05_12
        hide HC230tile05_13  
    if and1in2 == True and nor1in3 == True and (xor1in1 == True or xor2in1 == True) and (xor1in4 == True or xor2in4 == True):
        image HC229tile04_12 = "r_elbow_bl.png"
        show HC229tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC229tile05_12 = "r_elbow_tr.png"
        image HC229tile05_13 = "r_horizontal.png"
        show HC229tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC229tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC229tile04_10 = "r_g.png"
        show HC229tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC229tile04_10
        hide HC229tile04_12
        hide HC229tile05_12
        hide HC229tile05_13  
    if and1in2 == True and nor1in4 == True and (xor1in3 == True or xor2in3 == True) and (xor1in1 == True or xor2in1 == True):
        image HC228tile04_12 = "r_elbow_bl.png"
        show HC228tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC228tile05_12 = "r_elbow_tr.png"
        image HC228tile05_13 = "r_horizontal.png"
        show HC228tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC228tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC228tile04_10 = "r_r.png"
        show HC228tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC228tile04_10
        hide HC228tile04_12
        hide HC228tile05_12
        hide HC228tile05_13  
    if and1in3 == True and nor1in2 == True and (xor1in1 == True or xor2in1 == True) and (xor1in4 == True or xor2in4 == True):
        image HC227tile04_12 = "r_elbow_bl.png"
        show HC227tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC227tile05_12 = "r_elbow_tr.png"
        image HC227tile05_13 = "r_horizontal.png"
        show HC227tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC227tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC227tile04_10 = "r_g.png"
        show HC227tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC227tile04_12
        hide HC227tile05_12
        hide HC227tile05_13  
        hide HC227tile04_10
    if and1in3 == True and nor1in1 == True and (xor1in2 == True or xor2in2 == True) and (xor1in4 == True or xor2in4 == True):
        image HC226tile04_12 = "r_elbow_bl.png"
        show HC226tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC226tile05_12 = "r_elbow_tr.png"
        image HC226tile05_13 = "r_horizontal.png"
        show HC226tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC226tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC226tile04_10 = "r_g.png"
        show HC226tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC226tile04_10
        hide HC226tile04_12
        hide HC226tile05_12
        hide HC226tile05_13  
    if and1in3 == True and nor1in4 == True and (xor1in2 == True or xor2in2 == True) and (xor1in1 == True or xor2in1 == True):
        image HC225tile04_12 = "r_elbow_bl.png"
        show HC225tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC225tile05_12 = "r_elbow_tr.png"
        image HC225tile05_13 = "r_horizontal.png"
        show HC225tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC225tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC225tile04_10 = "r_r.png"
        show HC225tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC225tile04_10
        hide HC225tile04_12
        hide HC225tile05_12
        hide HC225tile05_13  
    if and1in4 == True and nor1in2 == True and (xor1in3 == True or xor2in3 == True) and (xor1in1 == True or xor2in1 == True):
        image HC224tile04_12 = "r_elbow_bl.png"
        show HC224tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC224tile05_12 = "r_elbow_tr.png"
        image HC224tile05_13 = "r_horizontal.png"
        show HC224tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC224tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC224tile04_10 = "r_g.png"
        show HC224tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC224tile04_10
        hide HC224tile04_12
        hide HC224tile05_12
        hide HC224tile05_13  
    if and1in4 == True and nor1in3 == True and (xor1in2 == True or xor2in2 == True) and (xor1in1 == True or xor2in1 == True):
        image HC223tile04_12 = "r_elbow_bl.png"
        show HC223tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC223tile05_12 = "r_elbow_tr.png"
        image HC223tile05_13 = "r_horizontal.png"
        show HC223tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC223tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC223tile04_10 = "r_r.png"
        show HC223tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC223tile04_10
        hide HC223tile04_12
        hide HC223tile05_12
        hide HC223tile05_13  
    if and1in4 == True and nor1in1 == True and (xor1in3 == True or xor2in3 == True) and (xor1in2 == True or xor2in2 == True): 
        image HC222tile04_12 = "r_elbow_bl.png"
        show HC222tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        image HC222tile05_12 = "r_elbow_tr.png"
        image HC222tile05_13 = "r_horizontal.png"
        show HC222tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show HC222tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image HC222tile04_10 = "r_g.png"
        show HC222tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HC222tile04_10
        hide HC222tile04_12
        hide HC222tile05_12
        hide HC222tile05_13  

#win conditions ********
    if and1in1 and nor1in3 and (xor1in2 or xor2in2) and (xor1in4 or xor2in4):         
        image HC1290tile02_09 = "xor_Gate.png"
        show HC1290tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HC1290tile02_10 = "xor_Gate.png"
        show HC1290tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image HC1190tile07_02 = "and_Gate.png"
        show HC1190tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HC1190tile07_08 = "nor_Gate.png"
        show HC1190tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image HC1190end2 = "light_g_on.png"
        show HC1190end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardCWin
        $lgHardC_solved = True
        jump lgHard_done

  
    if attempts == 0:
        image HC1290tile02_09 = "xor_Gate.png"
        show HC1290tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HC1290tile02_10 = "xor_Gate.png"
        show HC1290tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image HC1290tile07_02 = "and_Gate.png"
        show HC1290tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HC1290tile07_08 = "nor_Gate.png"
        show HC1290tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_lgHardCLose
        $lgHard_attempts +=1
        jump lgHard_lose3
    
    jump gamefileHC2

screen logicgatesHC2:
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
        action Jump("hints_lgHardC2")
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
                xpos 1300 ypos 88