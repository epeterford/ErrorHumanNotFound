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

label logicGate_mediumB1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
 #row 1 (row has a light)
    image MB1tile01_00 = "g_horizontal.png"
    image MB1tile01_01 = "g_horizontal.png"
    image MB1tile01_02 = "nand_Gate_blue.png"
    image MB1tile01_03 = "r_horizontal.png"
    image MB1tile01_04 = "r_t_down.png"
    image MB1tile01_05 = "r_horizontal.png"
    image MB1tile01_06 = "r_horizontal.png"
    image MB1tile01_07 = "r_horizontal.png"
    image MB1tile01_08 = "r_elbow_bl.png"
    
    show MB1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show MB1tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image MB1tile02_04 = "r_vertical.png"
    image MB1tile02_08 = "r_y.png"
    image MB1tile02_09 = "OR_Gate_blue.png"
    image MB1tile02_10 = "y_horizontal.png"
    image MB1tile02_11 = "y_elbow_bl.png"
    
    show MB1tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show MB1tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show MB1tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show MB1tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
    show MB1tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MB1tile03_00 = "g_t_down.png"
    image MB1tile03_01 = "g_elbow_bl.png"
    image MB1tile03_04 = "r_y.png"
    image MB1tile03_05 = "NOR_Gate_blue.png"
    image MB1tile03_06 = "y_horizontal.png"
    image MB1tile03_07 = "y_horizontal.png"
    image MB1tile03_08 = "y_elbow_tl.png"
    image MB1tile03_11 = "y_y.png"
    image MB1tile03_12 = "NAND_Gate_blue.png"
    image MB1tile03_13 = "y_horizontal.png"
    
    show MB1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show MB1tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MB1tile04_00 = "g_vertical.png"
    image MB1tile04_01 = "g_r.png"
    image MB1tile04_02 = "NONE_Gate.png"
    image MB1tile04_03 = "y_horizontal.png"
    image MB1tile04_04 = "y_elbow_tl.png"
    image MB1tile04_08 = "y_elbow_br.png"
    image MB1tile04_09 = "y_elbow_bl.png"
    image MB1tile04_11 = "y_vertical.png"
    
    show MB1tile04_00 at Position(xpos = 436, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show MB1tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MB1tile05_00 = "g_jump_r.png"
    image MB1tile05_01 = "r_elbow_tl.png"
    image MB1tile05_08 = "y_vertical.png"
    image MB1tile05_09 = "y_g.png"
    image MB1tile05_10 = "NONE_Gate.png"
    image MB1tile05_11 = "y_elbow_tl.png"
    
    show MB1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MB1tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show MB1tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show MB1tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show MB1tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show MB1tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image MB1tile06_00 = "g_elbow_tr.png"
    image MB1tile06_01 = "g_horizontal.png"
    image MB1tile06_02 = "g_horizontal.png"
    image MB1tile06_03 = "g_horizontal.png"
    image MB1tile06_04 = "g_horizontal.png"
    image MB1tile06_05 = "g_horizontal.png"
    image MB1tile06_06 = "g_elbow_bl.png"
    image MB1tile06_08 = "y_vertical.png"
    image MB1tile06_09 = "g_vertical.png"
    
    show MB1tile06_00 at Position(xpos = 436, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show MB1tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image MB1tile07_00 = "g_elbow_bl.png"
    image MB1tile07_06 = "g_g.png"
    image MB1tile07_07 = "NONE_Gate.png"
    image MB1tile07_08 = "y_elbow_tl.png"
    image MB1tile07_09 = "g_vertical.png"
    
    show MB1tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show MB1tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
    show MB1tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show MB1tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show MB1tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)

    #row 8
    image MB1tile08_00 = "g_elbow_tr.png"
    image MB1tile08_01 = "g_horizontal.png"
    image MB1tile08_02 = "g_horizontal.png"
    image MB1tile08_03 = "g_horizontal.png"
    image MB1tile08_04 = "g_horizontal.png"
    image MB1tile08_05 = "g_horizontal.png"
    image MB1tile08_06 = "g_t_up.png"
    image MB1tile08_07 = "g_horizontal.png"
    image MB1tile08_08 = "g_horizontal.png"
    image MB1tile08_09 = "g_elbow_tl.png"

    show MB1tile08_00 at Position(xpos = 436, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_01 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_02 at Position(xpos = 586, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    show MB1tile08_09 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)


    #start points
    image MB1start1 = "light_g_on.png"
    show MB1start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image MB1start2 = "light_g_on.png"
    show MB1start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image MB1start3 = "light_r_on.png"
    show MB1start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image MB1start4 = "light_g_on.png"
    show MB1start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points 
    image end4 = "light_r_off.png"
    show end4 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)


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
    $ nand1x = 998
    $ nand1y = 88
    
    #gate values
    $ gate1x = 586
    $ gate1y = 533
    $ gate2x = 961
    $ gate2y = 758
    $ gate3x = 1186
    $ gate3y = 608
   
    # check conditons for locations
    $ and1in1 = False
    $ nor1in1 = False
    $ nand1in1 = False
    $ and1in2 = False
    $ nor1in2 = False
    $ nand1in2 = False
    $ and1in3 = False
    $ nor1in3 = False
    $ nand1in3 = False
     
    #attempts for players
    $ attempts = 5
 
    jump gamefileMB1
    
    
label gamefileMB1:
    
    #calls game screen
    call screen logicgatesMB1
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
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
            #sets values for checks
            $ and1x = gate1x
            $ and1y = gate1y
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            
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
            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
            $ and1in3 = False
        #gate slot number three*******************************        
        if slot_name == "gate slot three":
            if nor1in3 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in3 = False
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
        
        if slot_name == "and return":
            $ and1x = 698
            $ and1y = 88
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = False
            
     #or gate section **********************************************************************       
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
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
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
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
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
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
            
        if slot_name == "nor return":
            $ nor1x = 1148
            $ nor1y = 88
            $ nor1in2 = False
            $ nor1in1 = False
            $ nor1in3 = False
            
     #nand gate section **********************************************************************       
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
            #sets values for checks
            $ nand1x = gate1x
            $ nand1y = gate1y
            $ nand1in1 = True
            $ nand1in2 = False
            $ nand1in3 = False
            
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
            #sets values for checks
            $ nand1x = gate2x
            $ nand1y = gate2y
            $ nand1in2 = True
            $ nand1in1 = False
            $ nand1in3 = False
            
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
            #sets values for checks
            $ nand1x = gate3x
            $ nand1y = gate3y
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = True
            
        
        if slot_name == "nand return":
            $ nand1x = 998
            $ nand1y = 88
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = False
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null":
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
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "nand_gate":
                $ attempts +=1                
            if slot_name == "and return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "nor_gate":
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
    if nor1in1 == True:
        image MB14tile04_03 = "r_horizontal.png"
        image MB14tile04_04 = "r_elbow_tl.png"
        show MB14tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show MB14tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        image MB14tile03_04 = "r_r.png"
        show MB14tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        image MB14tile03_06 = "g_horizontal.png"
        image MB14tile03_07 = "g_horizontal.png"
        image MB14tile03_08 = "g_elbow_tl.png"
        show MB14tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show MB14tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show MB14tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        
        image MB14tile03_11 = "g_y.png"
        show MB14tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

        image MB14tile02_08 = "r_g.png"
        image MB14tile02_10 = "g_horizontal.png"
        image MB14tile02_11 = "g_elbow_bl.png"
        show MB14tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show MB14tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
        show MB14tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    if nor1in1 == False:
        hide MB14tile04_03
        hide MB14tile04_04
        hide MB14tile03_04
        hide MB14tile03_06
        hide MB14tile03_07
        hide MB14tile03_08
        hide MB14tile03_11
        hide MB14tile02_08
        hide MB14tile02_10
        hide MB14tile02_11
        
    if nor1in2 == True:
        image MB15tile07_08 = "r_elbow_tl.png"
        show MB15tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image MB15tile06_08 = "r_vertical.png"
        show MB15tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        image MB15tile05_08 = "r_vertical.png"
        image MB15tile05_09 = "r_g.png"
        show MB15tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show MB15tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MB15tile04_08 = "r_elbow_br.png"
        image MB15tile04_09 = "r_elbow_bl.png"
        show MB15tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show MB15tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    
    if nor1in2 == False:
        hide MB15tile07_08
        hide MB15tile06_08
        hide MB15tile05_08
        hide MB15tile05_09
        hide MB15tile04_08
        hide MB15tile04_09
        
    if nor1in3 == True and and1in2 == True:
        image MB16tile05_11 = "r_elbow_tl.png"
        show MB16tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MB16tile04_11 = "r_vertical.png"
        show MB16tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MB16tile03_11 = "y_r.png"
        show MB16tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

    if nor1in3 == False or and1in2 == False:
        hide MB16tile05_11
        hide MB16tile04_11
        hide MB16tile03_11
        
    if nor1in3 == True and nand1in2 == True:
        image MB161tile05_11 = "r_elbow_tl.png"
        show MB161tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MB161tile04_11 = "r_vertical.png"
        show MB161tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MB161tile03_11 = "y_r.png"
        show MB161tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

    if nor1in3 == False or nand1in2 == False:
        hide MB161tile05_11
        hide MB161tile04_11
        hide MB161tile03_11
        
    if and1in1 == True:
        image MB17tile04_03 = "r_horizontal.png"
        image MB17tile04_04 = "r_elbow_tl.png"
        show MB17tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show MB17tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        image MB17tile03_04 = "r_r.png"
        show MB17tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        image MB17tile03_06 = "g_horizontal.png"
        image MB17tile03_07 = "g_horizontal.png"
        image MB17tile03_08 = "g_elbow_tl.png"
        show MB17tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show MB17tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show MB17tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        
        image MB17tile03_11 = "g_y.png"
        show MB17tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

        image MB17tile02_08 = "r_g.png"
        image MB17tile02_10 = "g_horizontal.png"
        image MB17tile02_11 = "g_elbow_bl.png"
        show MB17tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show MB17tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
        show MB17tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    if and1in1 == False:
        hide MB17tile04_03
        hide MB17tile04_04
        hide MB17tile03_04
        hide MB17tile03_06
        hide MB17tile03_07
        hide MB17tile03_08
        hide MB17tile03_11
        hide MB17tile02_08
        hide MB17tile02_10
        hide MB17tile02_11
        
    if and1in2 == True:
        image MB18tile07_08 = "g_elbow_tl.png"
        show MB18tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image MB18tile06_08 = "g_vertical.png"
        show MB18tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        image MB18tile05_08 = "g_vertical.png"
        image MB18tile05_09 = "g_g.png"
        show MB18tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show MB18tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MB18tile04_08 = "g_elbow_br.png"
        image MB18tile04_09 = "g_elbow_bl.png"
        show MB18tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show MB18tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    
    if and1in2 == False:
        hide MB18tile07_08
        hide MB18tile06_08
        hide MB18tile05_08
        hide MB18tile05_09
        hide MB18tile04_08
        hide MB18tile04_09

    if and1in3 == True and nand1in2 == True:
        image MB19tile05_11 = "r_elbow_tl.png"
        show MB19tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MB19tile04_11 = "r_vertical.png"
        show MB19tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MB19tile03_11 = "y_r.png"
        show MB19tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        
    if and1in3 == False or nand1in2 == False:
        hide MB19tile05_11
        hide MB19tile04_11
        hide MB19tile03_11
        
    if and1in3 == True and nor1in2 == True:
        image MB191tile05_11 = "r_elbow_tl.png"
        show MB191tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MB191tile04_11 = "r_vertical.png"
        show MB191tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MB191tile03_11 = "y_r.png"
        show MB191tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        
    if and1in3 == False or nor1in2 == False:
        hide MB191tile05_11
        hide MB191tile04_11
        hide MB191tile03_11
        
    if nand1in1 == True:
        image MB111tile04_03 = "g_horizontal.png"
        image MB111tile04_04 = "g_elbow_tl.png"
        show MB111tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show MB111tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        image MB111tile03_04 = "r_g.png"
        show MB111tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        image MB111tile03_06 = "r_horizontal.png"
        image MB111tile03_07 = "r_horizontal.png"
        image MB111tile03_08 = "r_elbow_tl.png"
        show MB111tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show MB111tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show MB111tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        
        image MB111tile03_11 = "r_y.png"
        show MB111tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

        image MB111tile02_08 = "r_r.png"
        image MB111tile02_10 = "r_horizontal.png"
        image MB111tile02_11 = "r_elbow_bl.png"
        show MB111tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show MB111tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
        show MB111tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
    
    if nand1in1 == False:
        hide MB111tile04_03
        hide MB111tile04_04
        hide MB111tile03_04
        hide MB111tile03_06
        hide MB111tile03_07
        hide MB111tile03_08
        hide MB111tile03_11
        hide MB111tile02_08
        hide MB111tile02_10
        hide MB111tile02_11
        
    if nand1in2 == True:
        image MB112tile07_08 = "r_elbow_tl.png"
        show MB112tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        image MB112tile06_08 = "r_vertical.png"
        show MB112tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        image MB112tile05_08 = "r_vertical.png"
        image MB112tile05_09 = "r_g.png"
        show MB112tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show MB112tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MB112tile04_08 = "r_elbow_br.png"
        image MB112tile04_09 = "r_elbow_bl.png"
        show MB112tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show MB112tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    
    if nand1in2 == False:
        hide MB112tile07_08
        hide MB112tile06_08
        hide MB112tile05_08
        hide MB112tile05_09
        hide MB112tile04_08
        hide MB112tile04_09
        
    if nand1in3 == True and and1in2 == True:
        image MB113tile05_11 = "r_elbow_tl.png"
        show MB113tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MB113tile04_11 = "r_vertical.png"
        show MB113tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MB113tile03_11 = "y_r.png"
        show MB113tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    if nand1in3 == False or and1in2 == False:
        hide MB113tile05_11
        hide MB113tile04_11
        hide MB113tile03_11
        
    if nand1in3 == True and nor1in2 == True:
        image MB1131tile05_11 = "g_elbow_tl.png"
        show MB1131tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MB1131tile04_11 = "g_vertical.png"
        show MB1131tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MB1131tile03_11 = "y_g.png"
        show MB1131tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    if nand1in3 == False or nor1in2 == False:
        hide MB1131tile05_11
        hide MB1131tile04_11
        hide MB1131tile03_11       
        
    if and1in3 == True and nor1in2 == True and nand1in1 == True: 
        image MB11562tile03_11 = "r_r.png"
        show MB11562tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide MB11562tile03_11
    if and1in3 == True and nor1in1 == True and nand1in2 == True: 
        image MB21563tile03_11 = "g_r.png"
        show MB21563tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide MB21563tile03_11
    if and1in1 == True and nor1in2 == True and nand1in3 == True: 
        image MB31564tile03_11 = "g_g.png"
        show MB31564tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)  
    else:
        hide MB31564tile03_11
    if and1in2 == True and nor1in1 == True and nand1in3 == True: 
        image MB41564tile03_11 = "g_r.png"
        show MB41564tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide MB41564tile03_11
    if and1in2 == True and nor1in3 == True and nand1in1 == True: 
        image MB51564tile03_11 = "r_r.png"
        show MB51564tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0) 
    else:
        hide MB51564tile03_11
    if and1in1 == True and nor1in3 == True and nand1in2 == True:         
        image MB15644tile03_11 = "g_r.png"
        show MB15644tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide MB15644tile03_11

    if (and1in1 == True and nor1in3 == True and nand1in2 == True) or (and1in2 == True and nor1in3 == True and nand1in1 == True) or (and1in3 == True and nor1in2 == True and nand1in1 == True) or (and1in3 == True and nor1in1 == True and nand1in2 == True) or ( and1in2 == True and nor1in1 == True and nand1in3 == True):
        image nottheright = "g_horizontal.png"
        show nottheright at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0) 
    else:
        hide nottheright

        
#win conditions ********
    if and1in1 == True and nor1in2 == True and nand1in3 == True:   
        image MB199tile03_13 = "r_horizontal.png"
        show MB199tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)        
        image MB11tile02_09 = "nand_Gate.png"
        show MB11tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MB11tile07_02 = "and_Gate.png"
        show MB11tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MB11tile07_08 = "nor_Gate.png"
        show MB11tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MB11end2 = "light_r_on.png"
        show MB11end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        $lgMedB_solved = True
        jump lgMed_win

  
    if attempts == 0:
        image MB12tile02_09 = "nand_Gate.png"
        show MB12tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MB12tile07_02 = "and_Gate.png"
        show MB12tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MB12tile07_08 = "nor_Gate.png"
        show MB12tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        $lgMed_attempts +=1
        jump lgMed_lose
        
    jump gamefileMB1

screen logicgatesMB1:
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
        action Jump("hints_lgMedB1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty.png"
        xpos 1515
        ypos 890
    text "Moves" xpos 1550 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    text ": " xpos 1670 ypos 895 color "#0060db" font "Bitter-Bold.otf" size 42
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
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88