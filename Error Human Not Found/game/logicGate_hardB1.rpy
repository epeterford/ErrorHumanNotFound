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

label logicGate_hardB1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
   
    #row 1 (row has a light)
    image HB1tile01_00 = "r_horizontal.png"
    image HB1tile01_01 = "r_elbow_bl.png"
    
    show HB1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HB1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image HB1tile02_01 = "r_g.png"
    image HB1tile02_02 = "NONE_Gate.png"
    image HB1tile02_03 = "y_horizontal.png"
    image HB1tile02_04 = "y_horizontal.png"
    image HB1tile02_05 = "y_horizontal.png"
    image HB1tile02_06 = "y_elbow_bl.png"
    
    show HB1tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show HB1tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show HB1tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HB1tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show HB1tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show HB1tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HB1tile03_00 = "g_horizontal.png"
    image HB1tile03_01 = "g_t_up.png"
    image HB1tile03_02 = "g_horizontal.png"
    image HB1tile03_03 = "g_horizontal.png"
    image HB1tile03_04 = "g_elbow_bl.png"
    image HB1tile03_06 = "y_y.png"
    image HB1tile03_07 = "NONE_Gate.png"
    image HB1tile03_08 = "y_horizontal.png"
    image HB1tile03_09 = "y_elbow_bl.png"
    image HB1tile03_13 = "y_elbow_br.png"
    
    show HB1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HB1tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HB1tile04_04 = "g_vertical.png"
    image HB1tile04_06 = "y_vertical.png"
    image HB1tile04_09 = "y_y.png"
    image HB1tile04_10 = "NAND_Gate_blue.png"
    image HB1tile04_11 = "y_horizontal.png"
    image HB1tile04_12 = "NOT_Gate_blue.png"
    image HB1tile04_13 = "y_elbow_tl.png"
    
    show HB1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HB1tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HB1tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show HB1tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show HB1tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show HB1tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    show HB1tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HB1tile05_00 = "r_horizontal.png"
    image HB1tile05_01 = "r_elbow_bl.png"
    image HB1tile05_04 = "g_y.png"
    image HB1tile05_05 = "NONE_Gate.png"
    image HB1tile05_06 = "y_t_up.png"
    image HB1tile05_07 = "y_horizontal.png"
    image HB1tile05_08 = "y_horizontal.png"
    image HB1tile05_09 = "y_elbow_tl.png"
    
    show HB1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show HB1tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image HB1tile06_01 = "r_r.png"
    image HB1tile06_02 = "NONE_Gate.png"
    image HB1tile06_03 = "y_horizontal.png"
    image HB1tile06_04 = "y_elbow_tl.png"
    show HB1tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show HB1tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show HB1tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show HB1tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HB1tile07_00 = "r_horizontal.png"
    image HB1tile07_01 = "r_elbow_tl.png"
    
    show HB1tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HB1tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)

    #start points
    image HB1start1 = "light_r_on.png"
    show HB1start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HB1start2 = "light_g_on.png"
    show HB1start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HB1start3 = "light_r_on.png"
    show HB1start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HB1start4 = "light_r_on.png"
    show HB1start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image HB1end2 = "light_g_off.png"
    show HB1end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)



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
    $ gate1x = 586
    $ gate1y = 383
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 811
    $ gate3y = 608
    $ gate4x = 961
    $ gate4y = 458
    
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
 
    jump gamefileHB1
    
    
label gamefileHB1:
    
    #calls game screen
    call screen logicgatesHB1
    
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
            
        #gate slot nuHBer three*******************************        
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
            
        #gate slot nuHBer three*******************************    
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
                $ and1in4 = False
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
            
        #gate slot nuHBer three*******************************    
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
            
        #gate slot nuHBer three*******************************    
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
        image HB11tile02_03 = "r_horizontal.png"
        image HB11tile02_04 = "r_horizontal.png"
        image HB11tile02_05 = "r_horizontal.png"
        image HB11tile02_06 = "r_elbow_bl.png"
        show HB11tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB11tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB11tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB11tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)

        image HB11tile03_06 = "r_y.png"
        show HB11tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        
    else:
        hide HB11tile02_03
        hide HB11tile02_04
        hide HB11tile02_05
        hide HB11tile02_06
        hide HB11tile03_06
        

    if nor1in1 == True:
        image HB13tile02_03 = "r_horizontal.png"
        image HB13tile02_04 = "r_horizontal.png"
        image HB13tile02_05 = "r_horizontal.png"
        image HB13tile02_06 = "r_elbow_bl.png"
        show HB13tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB13tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB13tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB13tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)

        image HB13tile03_06 = "r_y.png"
        show HB13tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        
    else:
        hide HB13tile02_03
        hide HB13tile02_04
        hide HB13tile02_05
        hide HB13tile02_06
        hide HB13tile03_06    

    
    if xor1in1 == True:
        image HB15tile02_03 = "g_horizontal.png"
        image HB15tile02_04 = "g_horizontal.png"
        image HB15tile02_05 = "g_horizontal.png"
        image HB15tile02_06 = "g_elbow_bl.png"
        show HB15tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB15tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB15tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB15tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)

        image HB15tile03_06 = "g_y.png"
        show HB15tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)

    else:
        hide HB15tile02_03
        hide HB15tile02_04
        hide HB15tile02_05
        hide HB15tile02_06
        hide HB15tile03_06


    if xor2in1 == True:
        image HB17tile02_03 = "g_horizontal.png"
        image HB17tile02_04 = "g_horizontal.png"
        image HB17tile02_05 = "g_horizontal.png"
        image HB17tile02_06 = "g_elbow_bl.png"
        show HB17tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB17tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB17tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        show HB17tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)

        image HB17tile03_06 = "g_y.png"
        show HB17tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        
    else:
        hide HB17tile02_03
        hide HB17tile02_04
        hide HB17tile02_05
        hide HB17tile02_06
        hide HB17tile03_06

        
    if and1in2 == True:
        image HB12tile06_03 = "r_horizontal.png"
        image HB12tile06_04 = "r_elbow_tl.png"
        show HB12tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB12tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HB12tile05_04 = "g_r.png"
        show HB12tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HB12tile06_03
        hide HB12tile06_04
        hide HB12tile05_04    

    if nor1in2 == True:
        image HB14tile06_03 = "g_horizontal.png"
        image HB14tile06_04 = "g_elbow_tl.png"
        show HB14tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB14tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HB14tile05_04 = "g_g.png"
        show HB14tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HB14tile06_03
        hide HB14tile06_04
        hide HB14tile05_04

    if xor1in2 == True:
        image HB16tile06_03 = "r_horizontal.png"
        image HB16tile06_04 = "r_elbow_tl.png"
        show HB16tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB16tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HB16tile05_04 = "g_r.png"
        show HB16tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HB16tile06_03
        hide HB16tile06_04
        hide HB16tile05_04

    if xor2in2 == True:
        image HB18tile06_03 = "r_horizontal.png"
        image HB18tile06_04 = "r_elbow_tl.png"
        show HB18tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB18tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        image HB18tile05_04 = "g_r.png"
        show HB18tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    else:
        hide HB18tile06_03
        hide HB18tile06_04
        hide HB18tile05_04
        

    if and1in3 == True:
        if nor1in2 == True:
            image HB19tile05_06 = "g_t_up.png"
            image HB19tile05_07 = "g_horizontal.png"
            image HB19tile05_08 = "g_horizontal.png"
            image HB19tile05_09 = "g_elbow_tl.png"
            show HB19tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HB19tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HB19tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB19tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            image HB19tile04_06 = "g_vertical.png"
            image HB19tile04_09 = "y_g.png"
            show HB19tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB19tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB19tile03_06 = "y_g.png"
            show HB19tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB19tile05_06
            hide HB19tile05_07
            hide HB19tile05_08
            hide HB19tile05_09
            hide HB19tile04_06
            hide HB19tile04_09
            hide HB19tile03_06
            
        if xor1in2 == True or xor2in2 == True:
            image HB110tile05_06 = "r_t_up.png"
            image HB110tile05_07 = "r_horizontal.png"
            image HB110tile05_08 = "r_horizontal.png"
            image HB110tile05_09 = "r_elbow_tl.png"
            show HB110tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HB110tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HB110tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB110tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            image HB110tile04_06 = "r_vertical.png"
            image HB110tile04_09 = "y_r.png"
            show HB110tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB110tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB110tile03_06 = "y_r.png"
            show HB110tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB110tile05_06
            hide HB110tile05_07
            hide HB110tile05_08
            hide HB110tile05_09
            hide HB110tile04_06
            hide HB110tile04_09
            hide HB110tile03_06
    else:
        hide HB110tile05_06
        hide HB110tile05_07
        hide HB110tile05_08
        hide HB110tile05_09
        hide HB110tile04_06
        hide HB110tile04_09
        hide HB110tile03_06
        hide HB19tile05_06
        hide HB19tile05_07
        hide HB19tile05_08
        hide HB19tile05_09
        hide HB19tile04_06
        hide HB19tile04_09
        hide HB19tile03_06     
        
    if nor1in3 == True and (and1in2 == True or xor1in2 == True or xor2in2 == True):
        image HB111tile05_06 = "r_t_up.png"
        image HB111tile05_07 = "r_horizontal.png"
        image HB111tile05_08 = "r_horizontal.png"
        image HB111tile05_09 = "r_elbow_tl.png"
        show HB111tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        show HB111tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
        show HB111tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show HB111tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB111tile04_06 = "r_vertical.png"
        image HB111tile04_09 = "y_r.png"
        show HB111tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        show HB111tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image HB111tile03_06 = "y_r.png"
        show HB111tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB111tile05_06
        hide HB111tile05_07
        hide HB111tile05_08
        hide HB111tile05_09
        hide HB111tile04_06
        hide HB111tile04_09
        hide HB111tile03_06

    
    if xor1in3 == True or xor2in3 == True:
        if and1in2 == True:
            image HB112tile05_06 = "g_t_up.png"
            image HB112tile05_07 = "g_horizontal.png"
            image HB112tile05_08 = "g_horizontal.png"
            image HB112tile05_09 = "g_elbow_tl.png"
            show HB112tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HB112tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HB112tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB112tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            image HB112tile04_06 = "g_vertical.png"
            image HB112tile04_09 = "y_g.png"
            show HB112tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB112tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB112tile03_06 = "y_g.png"
            show HB112tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB112tile05_06
            hide HB112tile05_07
            hide HB112tile05_08
            hide HB112tile05_09
            hide HB112tile04_06
            hide HB112tile04_09
            hide HB112tile03_06

        
        if nor1in2 == True:
            image HB113tile05_06 = "r_t_up.png"
            image HB113tile05_07 = "r_horizontal.png"
            image HB113tile05_08 = "r_horizontal.png"
            image HB113tile05_09 = "r_elbow_tl.png"
            show HB113tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HB113tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HB113tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB113tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            image HB113tile04_06 = "r_vertical.png"
            image HB113tile04_09 = "y_r.png"
            show HB113tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB113tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB113tile03_06 = "y_r.png"
            show HB113tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            
            hide HB113tile05_06
            hide HB113tile05_07
            hide HB113tile05_08
            hide HB113tile05_09
            hide HB113tile04_06
            hide HB113tile04_09
            hide HB113tile03_06
            
        if xor1in2 == True or xor2in2 == True:
            image HB114tile05_06 = "g_t_up.png"
            image HB114tile05_07 = "g_horizontal.png"
            image HB114tile05_08 = "g_horizontal.png"
            image HB114tile05_09 = "g_elbow_tl.png"
            show HB114tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show HB114tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
            show HB114tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show HB114tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            image HB114tile04_06 = "g_vertical.png"
            image HB114tile04_09 = "y_g.png"
            show HB114tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB114tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB114tile03_06 = "y_g.png"
            show HB114tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB114tile05_06
            hide HB114tile05_07
            hide HB114tile05_08
            hide HB114tile05_09
            hide HB114tile04_06
            hide HB114tile04_09
            hide HB114tile03_06
    else:
        hide HB112tile05_06
        hide HB112tile05_07
        hide HB112tile05_08
        hide HB112tile05_09
        hide HB112tile04_06
        hide HB112tile04_09
        hide HB112tile03_06
        hide HB113tile05_06
        hide HB113tile05_07
        hide HB113tile05_08
        hide HB113tile05_09
        hide HB113tile04_06
        hide HB113tile04_09
        hide HB113tile03_06
        hide HB114tile05_06
        hide HB114tile05_07
        hide HB114tile05_08
        hide HB114tile05_09
        hide HB114tile04_06
        hide HB114tile04_09
        hide HB114tile03_06
        
    if (and1in1 == True and nor1in2 == True and (xor1in3 == True or xor2in3 == True)) or (and1in1 == True and nor1in3 == True and (xor1in2 == True or xor2in2 == True)) or (and1in3 == True and nor1in1 == True and (xor1in2 == True or xor2in2 == True)):
        image HB115tile03_06 = "r_r.png"
        show HB115tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if xor1in4 == True or xor2in4 == True:
            image HB115tile03_08 = "r_horizontal.png"
            image HB115tile03_09 = "r_elbow_bl.png"
            show HB115tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB115tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB115tile04_09 = "r_r.png"
            show HB115tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB115tile03_13 = "r_elbow_br.png"
            show HB115tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB115tile04_11 = "g_horizontal.png"
            image HB115tile04_13 = "r_elbow_tl.png"
            show HB115tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB115tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB115tile03_08
            hide HB115tile03_09
            hide HB115tile04_09 
            hide HB115tile04_13
            hide HB115tile04_11
            hide HB115tile03_13
    else:
        hide HB115tile03_08
        hide HB115tile03_09
        hide HB115tile04_09 
        hide HB115tile04_13
        hide HB115tile04_11
        hide HB115tile03_13
        hide HB115tile03_06
            
    if (and1in2 == True and nor1in1 == True and (xor1in3 == True or xor2in3 == True)):
        image HB116tile03_06 = "r_g.png"
        show HB116tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if xor1in4 == True or xor2in4 == True:
            image HB116tile03_08 = "g_horizontal.png"
            image HB116tile03_09 = "g_elbow_bl.png"
            show HB116tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB116tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB116tile04_09 = "g_g.png"
            show HB116tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB116tile03_13 = "g_elbow_br.png"
            show HB116tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB116tile04_11 = "r_horizontal.png"
            image HB116tile04_13 = "g_elbow_tl.png"
            show HB116tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB116tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB116tile03_08
            hide HB116tile03_09
            hide HB116tile04_09 
            hide HB116tile04_13
            hide HB116tile04_11
            hide HB116tile03_13
    else:
        hide HB116tile03_08
        hide HB116tile03_09
        hide HB116tile04_09 
        hide HB116tile04_13
        hide HB116tile04_11
        hide HB116tile03_13
        hide HB116tile03_06
    
    if (and1in2 == True and nor1in3 == True and (xor1in1 == True or xor2in1 == True)):   
        image HB117tile03_06 = "G_R.png"
        show HB117tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if xor1in4 == True or xor2in4 == True:
            image HB117tile03_08 = "g_horizontal.png"
            image HB117tile03_09 = "g_elbow_bl.png"
            show HB117tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB117tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB117tile04_09 = "g_r.png"
            show HB117tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB117tile03_13 = "r_elbow_br.png"
            show HB117tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB117tile04_11 = "g_horizontal.png"
            image HB117tile04_13 = "r_elbow_tl.png"
            show HB117tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB117tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB117tile03_08
            hide HB117tile03_09
            hide HB117tile04_09 
            hide HB117tile04_13
            hide HB117tile04_11
            hide HB117tile03_13
    else:
        hide HB117tile03_08
        hide HB117tile03_09
        hide HB117tile04_09 
        hide HB117tile04_13
        hide HB117tile04_11
        hide HB117tile03_13    
        hide HB117tile03_06

    if (and1in3 == True and nor1in2 == True and (xor1in1 == True or xor2in1 == True)):   
        image HB118tile03_06 = "G_g.png"
        show HB118tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if xor1in4 == True or xor2in4 == True:
            image HB118tile03_08 = "r_horizontal.png"
            image HB118tile03_09 = "r_elbow_bl.png"
            show HB118tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB118tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB118tile04_09 = "r_g.png"
            show HB118tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB118tile03_13 = "r_elbow_br.png"
            show HB118tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB118tile04_11 = "g_horizontal.png"
            image HB118tile04_13 = "r_elbow_tl.png"
            show HB118tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB118tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB118tile03_08
            hide HB118tile03_09
            hide HB118tile04_09 
            hide HB118tile04_13
            hide HB118tile04_11
            hide HB118tile03_13
    else:
        hide HB118tile03_08
        hide HB118tile03_09
        hide HB118tile04_09 
        hide HB118tile04_13
        hide HB118tile04_11
        hide HB118tile03_13  
        hide HB118tile03_06

    if ((xor1in1 == True or xor2in1 == True) and nor1in3 == True and (xor1in2 == True or xor2in2 == True)) or ((xor1in1 == True or xor2in1 == True) and nor1in2 == True and (xor1in3 == True or xor2in3 == True)):   
        image HB119tile03_06 = "G_r.png"
        show HB119tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if and1in4 == True:
            image HB119tile03_08 = "r_horizontal.png"
            image HB119tile03_09 = "r_elbow_bl.png"
            show HB119tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB119tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB119tile04_09 = "r_r.png"
            show HB119tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB119tile03_13 = "r_elbow_br.png"
            show HB119tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB119tile04_11 = "g_horizontal.png"
            image HB119tile04_13 = "r_elbow_tl.png"
            show HB119tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB119tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB119tile03_08
            hide HB119tile03_09
            hide HB119tile04_09 
            hide HB119tile04_13
            hide HB119tile04_11
            hide HB119tile03_13
    else:
        hide HB119tile03_06
        hide HB119tile03_08
        hide HB119tile03_09
        hide HB119tile04_09 
        hide HB119tile04_13
        hide HB119tile04_11
        hide HB119tile03_13

    if ((xor1in2 == True or xor2in2 == True) and nor1in1 == True and (xor1in3 == True or xor2in3 == True)):   
        image HB120tile03_06 = "r_g.png"
        show HB120tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if and1in4 == True:
            image HB120tile03_08 = "r_horizontal.png"
            image HB120tile03_09 = "r_elbow_bl.png"
            show HB120tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB120tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB120tile04_09 = "r_g.png"
            show HB120tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB120tile03_13 = "r_elbow_br.png"
            show HB120tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB120tile04_11 = "g_horizontal.png"
            image HB120tile04_13 = "r_elbow_tl.png"
            show HB120tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB120tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB120tile03_08
            hide HB120tile03_09
            hide HB120tile04_09 
            hide HB120tile04_13
            hide HB120tile04_11
            hide HB120tile03_13
    else:
        hide HB120tile03_08
        hide HB120tile03_09
        hide HB120tile04_09 
        hide HB120tile04_13
        hide HB120tile04_11
        hide HB120tile03_13
        hide HB120tile03_06
            
    if ((xor1in2 == True or xor2in2 == True) and and1in1 == True and (xor1in3 == True or xor2in3 == True)):   
        image HB121tile03_06 = "r_g.png"
        show HB121tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if nor1in4 == True:
            image HB121tile03_08 = "r_horizontal.png"
            image HB121tile03_09 = "r_elbow_bl.png"
            show HB121tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB121tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB121tile04_09 = "r_g.png"
            show HB121tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB121tile03_13 = "r_elbow_br.png"
            show HB121tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB121tile04_11 = "g_horizontal.png"
            image HB121tile04_13 = "r_elbow_tl.png"
            show HB121tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB121tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB121tile03_08
            hide HB121tile03_09
            hide HB121tile04_09 
            hide HB121tile04_13
            hide HB121tile04_11
            hide HB121tile03_13
    else:
        hide HB121tile03_08
        hide HB121tile03_09
        hide HB121tile04_09 
        hide HB121tile04_13
        hide HB121tile04_11
        hide HB121tile03_13
        hide HB121tile03_06
            
    if ((xor1in1 == True or xor2in1 == True) and and1in2 == True and (xor1in3 == True or xor2in3 == True)):   
        image HB122tile03_06 = "g_g.png"
        show HB122tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if nor1in4 == True:
            image HB122tile03_08 = "r_horizontal.png"
            image HB122tile03_09 = "r_elbow_bl.png"
            show HB122tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB122tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB122tile04_09 = "r_g.png"
            show HB122tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB122tile03_13 = "r_elbow_br.png"
            show HB122tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB122tile04_11 = "g_horizontal.png"
            image HB122tile04_13 = "r_elbow_tl.png"
            show HB122tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB122tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB122tile03_08
            hide HB122tile03_09
            hide HB122tile04_09 
            hide HB122tile04_13
            hide HB122tile04_11
            hide HB122tile03_13
    else:
        hide HB122tile03_08
        hide HB122tile03_09
        hide HB122tile04_09 
        hide HB122tile04_13
        hide HB122tile04_11
        hide HB122tile03_13
        hide HB122tile03_06
        
    if ((xor1in1 == True or xor2in1 == True) and and1in3 == True and (xor1in2 == True or xor2in2 == True)):   
        image HB123tile03_06 = "g_r.png"
        show HB123tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0) 
        if nor1in4 == True:
            image HB123tile03_08 = "r_horizontal.png"
            image HB123tile03_09 = "r_elbow_bl.png"
            show HB123tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
            show HB123tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
            image HB123tile04_09 = "r_r.png"
            show HB123tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB123tile03_13 = "r_elbow_br.png"
            show HB123tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            image HB123tile04_11 = "g_horizontal.png"
            image HB123tile04_13 = "r_elbow_tl.png"
            show HB123tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            show HB123tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        else:
            hide HB123tile03_08
            hide HB123tile03_09
            hide HB123tile04_09 
            hide HB123tile04_13
            hide HB123tile04_11
            hide HB123tile03_13
    else:
        hide HB123tile03_08
        hide HB123tile03_09
        hide HB123tile04_09 
        hide HB123tile04_13
        hide HB123tile04_11
        hide HB123tile03_13  
        hide HB123tile03_06


#win conditions ********
    if (and1in2 == True and nor1in1 == True and (xor1in3 == True or xor2in3 == True) and (xor1in4 == True or xor2in4 == True)):         
        image HB1250tile02_09 = "xor_Gate.png"
        show HB1250tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HB1250tile02_10 = "xor_Gate.png"
        show HB1250tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image HB1150tile07_02 = "and_Gate.png"
        show HB1150tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HB1150tile07_08 = "nor_Gate.png"
        show HB1150tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image HB1150end2 = "light_g_on.png"
        show HB1150end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardBWin
        $lgHardB_solved = True
        jump lgHard_win2

  
    if attempts == 0:
        image HB1250tile02_09 = "xor_Gate.png"
        show HB1250tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HB1250tile02_10 = "xor_Gate.png"
        show HB1250tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image HB1250tile07_02 = "and_Gate.png"
        show HB1250tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HB1250tile07_08 = "nor_Gate.png"
        show HB1250tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_lgHardBLose
        $lgHard_attempts +=1
        jump lgHard_lose2
    
    jump gamefileHB1

screen logicgatesHB1:
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
        action Jump("hints_lgHardB1")
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