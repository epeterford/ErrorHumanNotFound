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

label logicGate_mediumC2:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #row 0
    image MC2tile00_01 = "g_elbow_br.png"
    image MC2tile00_02 = "g_horizontal.png"
    image MC2tile00_03 = "g_horizontal.png"
    image MC2tile00_04 = "g_elbow_bl.png"
    
    show MC2tile00_01 at Position(xpos = 511, xanchor = 0, ypos = 233, yanchor = 0)
    show MC2tile00_02 at Position(xpos = 586, xanchor = 0, ypos = 233, yanchor = 0)
    show MC2tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
    show MC2tile00_04 at Position(xpos = 736, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image MC2tile01_00 = "g_horizontal.png"
    image MC2tile01_01 = "g_t_left.png"
    image MC2tile01_04 = "g_r.png"
    image MC2tile01_05 = "NONE_Gate.png"
    image MC2tile01_06 = "y_horizontal.png"
    image MC2tile01_07 = "y_elbow_bl.png"
    
    show MC2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MC2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show MC2tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show MC2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show MC2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show MC2tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image MC2tile02_01 = "g_r.png"
    image MC2tile02_02 = "NOR_Gate_blue.png"
    image MC2tile02_03 = "r_horizontal.png"
    image MC2tile02_04 = "r_elbow_tl.png"
    image MC2tile02_07 = "y_g.png"
    image MC2tile02_08 = "NAND_Gate_blue.png"
    image MC2tile02_09 = "y_elbow_bl.png"
    show MC2tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show MC2tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show MC2tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show MC2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show MC2tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show MC2tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show MC2tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MC2tile03_00 = "r_horizontal.png"
    image MC2tile03_01 = "r_t_left.png"
    image MC2tile03_07 = "g_vertical.png"
    image MC2tile03_09 = "y_y.png"
    image MC2tile03_10 = "NAND_Gate_blue.png"
    image MC2tile03_11 = "y_elbow_bl.png"
    
    show MC2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MC2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MC2tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show MC2tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show MC2tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show MC2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MC2tile04_01 = "r_vertical.png"
    image MC2tile04_04 = "g_elbow_br.png"
    image MC2tile04_05 = "g_horizontal.png"
    image MC2tile04_06 = "g_horizontal.png"
    image MC2tile04_07 = "g_elbow_tl.png"
    image MC2tile04_09 = "y_vertical.png"
    image MC2tile04_11 = "y_vertical.png"
    
    show MC2tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show MC2tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show MC2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show MC2tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show MC2tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show MC2tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show MC2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MC2tile05_00 = "g_horizontal.png"
    image MC2tile05_01 = "r_jump_g.png"
    image MC2tile05_02 = "g_horizontal.png"
    image MC2tile05_03 = "g_horizontal.png"
    image MC2tile05_04 = "g_t_left.png"
    image MC2tile05_06 = "y_elbow_br.png"
    image MC2tile05_07 = "y_elbow_bl.png"
    image MC2tile05_09 = "y_vertical.png"
    image MC2tile05_11 = "y_y.png"
    image MC2tile05_12 = "nand_Gate_blue.png"
    image MC2tile05_13 = "y_horizontal.png"
    
    show MC2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show MC2tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image MC2tile06_01 = "r_r.png"
    image MC2tile06_02 = "NONE_Gate.png"
    image MC2tile06_03 = "y_t_down.png"
    image MC2tile06_04 = "g_jump_y.png"
    image MC2tile06_05 = "y_horizontal.png"
    image MC2tile06_06 = "y_elbow_tl.png"
    image MC2tile06_07 = "y_y.png"
    image MC2tile06_08 = "NONE_Gate.png"
    image MC2tile06_09 = "y_t_up.png"
    image MC2tile06_10 = "y_horizontal.png"
    image MC2tile06_11 = "y_elbow_tl.png"
    
    show MC2tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    show MC2tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image MC2tile07_00 = "r_horizontal.png"
    image MC2tile07_01 = "r_elbow_tl.png"
    image MC2tile07_03 = "y_vertical.png"
    image MC2tile07_04 = "g_vertical.png"
    image MC2tile07_07 = "y_vertical.png"
    
    show MC2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show MC2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show MC2tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show MC2tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show MC2tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)

    
    #row 8
    image MC2tile08_03 = "y_vertical.png"
    image MC2tile08_04 = "g_y.png"
    image MC2tile08_05 = "OR_Gate_blue.png"
    image MC2tile08_06 = "y_horizontal.png"
    image MC2tile08_07 = "y_elbow_tl.png"

    show MC2tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
    show MC2tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show MC2tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show MC2tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show MC2tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)

    
    #row 9
    image MC2tile09_03 = "y_elbow_tr.png"
    image MC2tile09_04 = "y_elbow_tl.png"

    show MC2tile09_03 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
    show MC2tile09_04 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)


    #start points
    image MC2start1 = "light_g_on.png"
    show MC2start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image MC2start2 = "light_r_on.png"
    show MC2start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image MC2start3 = "light_g_on.png"
    show MC2start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image MC2start4 = "light_r_on.png"
    show MC2start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image MC2end3 = "light_r_off.png"
    show MC2end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)


    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""

        #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ nor1x = 1148
    $ nor1y = 88
    $ nand1x = 998
    $ nand1y = 88
    
    #gate values
    $ gate1x = 811
    $ gate1y = 308
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 1036
    $ gate3y = 683
   
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
    $ attempts = 6
 
    jump gamefileMC2
    
    
label gamefileMC2:
    
    #calls game screen
    call screen logicGatesMC2
    
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
    if and1in1 == True:
        image MC21tile01_06 = "r_horizontal.png"
        image MC21tile01_07 = "r_elbow_bl.png"
        show MC21tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show MC21tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        image MC21tile02_07 = "r_g.png"
        image MC21tile02_09 = "g_elbow_bl.png"
        show MC21tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show MC21tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image MC21tile03_09 = "g_y.png"
        show MC21tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        
    if and1in1 == False:
        hide MC21tile01_06
        hide MC21tile01_07
        hide MC21tile02_07
        hide MC21tile02_09
        hide MC21tile03_09

    if nand1in1 == True:
        image MC22tile01_06 = "g_horizontal.png"
        image MC22tile01_07 = "g_elbow_bl.png"
        show MC22tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show MC22tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        image MC22tile02_07 = "g_g.png"
        image MC22tile02_09 = "r_elbow_bl.png"
        show MC22tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show MC22tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image MC22tile03_09 = "r_y.png"
        show MC22tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
 
    if nand1in1 == False:
        hide MC22tile01_06
        hide MC22tile01_07
        hide MC22tile02_07
        hide MC22tile02_09
        hide MC22tile03_09
        
    if nor1in1 == True:
        image MC23tile01_06 = "r_horizontal.png"
        image MC23tile01_07 = "r_elbow_bl.png"
        show MC23tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show MC23tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        image MC23tile02_07 = "r_g.png"
        image MC23tile02_09 = "g_elbow_bl.png"
        show MC23tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show MC23tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image MC23tile03_09 = "g_y.png"
        show MC23tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    
    if nor1in1 == False:
        hide MC23tile01_06
        hide MC23tile01_07
        hide MC23tile02_07
        hide MC23tile02_09
        hide MC23tile03_09
        
    if and1in2 == True:
        image MC24tile07_03 = "r_vertical.png"
        image MC24tile07_07 = "g_vertical.png"
        show MC24tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        show MC24tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        image MC24tile08_03 = "r_vertical.png"
        image MC24tile08_04 = "g_r.png"
        image MC24tile08_06 = "g_horizontal.png"
        image MC24tile08_07 = "g_elbow_tl.png"
        show MC24tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
        show MC24tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show MC24tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show MC24tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        image MC24tile09_03 = "r_elbow_tr.png"
        image MC24tile09_04 = "r_elbow_tl.png"
        show MC24tile09_03 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
        show MC24tile09_04 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
        image MC24tile06_03 = "r_t_down.png"
        image MC24tile06_04 = "g_jump_r.png"
        image MC24tile06_05 = "r_horizontal.png"
        image MC24tile06_06 = "r_elbow_tl.png"
        image MC24tile06_07 = "r_g.png"
        show MC24tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show MC24tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show MC24tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show MC24tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show MC24tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image MC24tile05_06 = "r_elbow_br.png"
        image MC24tile05_07 = "r_elbow_bl.png"
        show MC24tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        show MC24tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)

            
    if and1in2 == False:
        hide MC24tile07_03
        hide MC24tile07_07
        hide MC24tile08_03
        hide MC24tile08_04
        hide MC24tile08_06
        hide MC24tile08_07
        hide MC24tile09_03
        hide MC24tile09_04
        hide MC24tile06_03
        hide MC24tile06_04
        hide MC24tile06_05
        hide MC24tile06_06
        hide MC24tile06_07
        hide MC24tile05_06
        hide MC24tile05_07
        
    if nand1in2 == True:
        image MC25tile07_03 = "g_vertical.png"
        image MC25tile07_07 = "g_vertical.png"
        show MC25tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        show MC25tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        image MC25tile08_03 = "g_vertical.png"
        image MC25tile08_04 = "g_g.png"
        image MC25tile08_06 = "g_horizontal.png"
        image MC25tile08_07 = "g_elbow_tl.png"
        show MC25tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
        show MC25tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show MC25tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show MC25tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        image MC25tile09_03 = "g_elbow_tr.png"
        image MC25tile09_04 = "g_elbow_tl.png"
        show MC25tile09_03 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
        show MC25tile09_04 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
        image MC25tile06_03 = "g_t_down.png"
        image MC25tile06_04 = "g_jump_g.png"
        image MC25tile06_05 = "g_horizontal.png"
        image MC25tile06_06 = "g_elbow_tl.png"
        image MC25tile06_07 = "g_g.png"
        show MC25tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show MC25tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show MC25tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show MC25tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show MC25tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image MC25tile05_06 = "g_elbow_br.png"
        image MC25tile05_07 = "g_elbow_bl.png"
        show MC25tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        show MC25tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)

    if nand1in2 == False:
        hide MC25tile07_03
        hide MC25tile07_07
        hide MC25tile08_03
        hide MC25tile08_04
        hide MC25tile08_06
        hide MC25tile08_07
        hide MC25tile09_03
        hide MC25tile09_04
        hide MC25tile06_03
        hide MC25tile06_04
        hide MC25tile06_05
        hide MC25tile06_06
        hide MC25tile06_07
        hide MC25tile05_06
        hide MC25tile05_07
        
    if nor1in2 == True:
        image MC26tile07_03 = "g_vertical.png"
        image MC26tile07_07 = "g_vertical.png"
        show MC26tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        show MC26tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        image MC26tile08_03 = "g_vertical.png"
        image MC26tile08_04 = "g_g.png"
        image MC26tile08_06 = "g_horizontal.png"
        image MC26tile08_07 = "g_elbow_tl.png"
        show MC26tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
        show MC26tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show MC26tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show MC26tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        image MC26tile09_03 = "g_elbow_tr.png"
        image MC26tile09_04 = "g_elbow_tl.png"
        show MC26tile09_03 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
        show MC26tile09_04 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
        image MC26tile06_03 = "g_t_down.png"
        image MC26tile06_04 = "g_jump_g.png"
        image MC26tile06_05 = "g_horizontal.png"
        image MC26tile06_06 = "g_elbow_tl.png"
        image MC26tile06_07 = "g_g.png"
        show MC26tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show MC26tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show MC26tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show MC26tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show MC26tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image MC26tile05_06 = "g_elbow_br.png"
        image MC26tile05_07 = "g_elbow_bl.png"
        show MC26tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        show MC26tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)

    if nor1in2 == False:
        hide MC26tile07_03
        hide MC26tile07_07
        hide MC26tile08_03
        hide MC26tile08_04
        hide MC26tile08_06
        hide MC26tile08_07
        hide MC26tile09_03
        hide MC26tile09_04
        hide MC26tile06_03
        hide MC26tile06_04
        hide MC26tile06_05
        hide MC26tile06_06
        hide MC26tile06_07
        hide MC26tile05_06
        hide MC26tile05_07

    if and1in3 == True and nand1in2 == True:
        image MC201tile04_09 = "g_vertical.png"
        show MC201tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image MC201tile06_09 = "g_t_up.png"
        image MC201tile06_10 = "g_horizontal.png"
        image MC201tile06_11 = "g_elbow_tl.png"
        show MC201tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show MC201tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show MC201tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC201tile05_09 = "g_vertical.png"
        show MC201tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC201tile03_09 = "y_g.png"
        show MC201tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC201tile05_11 = "y_g.png"
        show MC201tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        
    if and1in3 == False or nand1in2 == False:
        hide MC201tile04_09
        hide MC201tile06_09
        hide MC201tile06_10
        hide MC201tile06_11
        hide MC201tile05_09
        hide MC201tile03_09
        hide MC201tile05_11
        
    if and1in3 == True and nor1in2 == True:
        image MC29tile04_09 = "g_vertical.png"
        show MC29tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image MC29tile06_09 = "g_t_up.png"
        image MC29tile06_10 = "g_horizontal.png"
        image MC29tile06_11 = "g_elbow_tl.png"
        show MC29tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show MC29tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show MC29tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC29tile05_09 = "g_vertical.png"
        show MC29tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC29tile03_09 = "y_g.png"
        show MC29tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC29tile05_11 = "y_g.png"
        show MC29tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        
    if and1in3 == False or nor1in2 == False:
        hide MC29tile04_09
        hide MC29tile06_09
        hide MC29tile06_10
        hide MC29tile06_11
        hide MC29tile05_09
        hide MC29tile03_09
        hide MC29tile05_11
            
    if nand1in3 == True and and1in2 == True:
        image MC202tile04_09 = "g_vertical.png"
        show MC202tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image MC202tile06_09 = "g_t_up.png"
        image MC202tile06_10 = "g_horizontal.png"
        image MC202tile06_11 = "g_elbow_tl.png"
        show MC202tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show MC202tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show MC202tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC202tile05_09 = "g_vertical.png"
        show MC202tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC202tile03_09 = "y_g.png"
        show MC202tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC202tile05_11 = "y_g.png"
        show MC202tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)  
   
    else:
        hide MC202tile04_09
        hide MC202tile06_09
        hide MC202tile06_10
        hide MC202tile06_11
        hide MC202tile05_09
        hide MC202tile03_09
        hide MC202tile05_11
        
    if nand1in3 == True and nor1in2 == True:
        image MC27tile04_09 = "r_vertical.png"
        show MC27tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image MC27tile06_09 = "r_t_up.png"
        image MC27tile06_10 = "r_horizontal.png"
        image MC27tile06_11 = "r_elbow_tl.png"
        show MC27tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show MC27tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show MC27tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC27tile05_09 = "r_vertical.png"
        show MC27tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC27tile03_09 = "y_r.png"
        show MC27tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC27tile05_11 = "y_r.png"
        show MC27tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)    
    
    else:
        hide MC27tile04_09
        hide MC27tile06_09
        hide MC27tile06_10
        hide MC27tile06_11
        hide MC27tile05_09
        hide MC27tile03_09
        hide MC27tile05_11
        
    if nor1in3 == True and and1in2 == True:
        image MC20tile04_09 = "r_vertical.png"
        show MC20tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image MC20tile06_09 = "r_t_up.png"
        image MC20tile06_10 = "r_horizontal.png"
        image MC20tile06_11 = "r_elbow_tl.png"
        show MC20tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show MC20tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show MC20tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC20tile05_09 = "r_vertical.png"
        show MC20tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC20tile03_09 = "y_r.png"
        show MC20tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC20tile05_11 = "y_r.png"
        show MC20tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    else:
        hide MC20tile04_09
        hide MC20tile06_09
        hide MC20tile06_10
        hide MC20tile06_11
        hide MC20tile05_09
        hide MC20tile03_09
        hide MC20tile05_11
        
    if nor1in3 == True and nand1in2 == True:
        image MC28tile04_09 = "r_vertical.png"
        show MC28tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        image MC28tile06_09 = "r_t_up.png"
        image MC28tile06_10 = "r_horizontal.png"
        image MC28tile06_11 = "r_elbow_tl.png"
        show MC28tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show MC28tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show MC28tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC28tile05_09 = "r_vertical.png"
        show MC28tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC28tile03_09 = "y_r.png"
        show MC28tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC28tile05_11 = "y_r.png"
        show MC28tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    else:
        hide MC28tile04_09
        hide MC28tile06_09
        hide MC28tile06_10
        hide MC28tile06_11
        hide MC28tile05_09
        hide MC28tile03_09
        hide MC28tile05_11
        
    if nor1in1 == True and ((and1in2 == True and nand1in3 == True) or (nand1in2 == True and and1in3 == True)):
        image MC203tile03_09 = "g_g.png"
        show MC203tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC203tile05_11 = "r_g.png"
        show MC203tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC203tile05_13 = "g_horizontal.png"
        show MC203tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image MC203tile03_11 = "r_elbow_bl.png"
        show MC203tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC203tile04_11 = "r_vertical.png"
        show MC203tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    else:
        hide MC203tile03_09
        hide MC203tile05_11
        hide MC203tile05_13
        hide MC203tile03_11
        hide MC203tile04_11
        
    if and1in1 == True and ((nor1in2 == True and nand1in3 == True) or (nand1in2 == True and nor1in3 == True)):
        image MC204tile03_09 = "g_r.png"
        show MC204tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC204tile05_11 = "g_r.png"
        show MC204tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC204tile05_13 = "g_horizontal.png"
        show MC204tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image MC204tile03_11 = "g_elbow_bl.png"
        show MC204tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC204tile04_11 = "g_vertical.png"
        show MC204tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
   
    else:
        hide MC204tile03_09
        hide MC204tile05_11
        hide MC204tile05_13
        hide MC204tile03_11
        hide MC204tile04_11
        
    if nand1in1 == True and nor1in3 == True and and1in2 == True:
        image MC206tile03_09 = "r_r.png"
        show MC206tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC206tile05_11 = "g_r.png"
        show MC206tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC206tile05_13 = "g_horizontal.png"
        show MC206tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image MC206tile03_11 = "g_elbow_bl.png"
        show MC206tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC206tile04_11 = "g_vertical.png"
        show MC206tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
   
    else:
        hide MC206tile03_09
        hide MC206tile05_11
        hide MC206tile05_13
        hide MC206tile03_11
        hide MC206tile04_11
        
#win conditions ********
    if nand1in1 == True and nor1in2 == True and and1in3 == True:
        image MC205tile03_09 = "r_g.png"
        show MC205tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MC205tile05_11 = "g_g.png"
        show MC205tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC205tile05_13 = "r_horizontal.png"
        show MC205tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        image MC205tile03_11 = "g_elbow_bl.png"
        show MC205tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC205tile04_11 = "g_vertical.png"
        show MC205tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MC211tile02_09 = "nand_Gate.png"
        show MC211tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MC211tile07_02 = "and_Gate.png"
        show MC211tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MC211tile07_08 = "nor_Gate.png"
        show MC211tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MC2end1 = "light_r_on.png"
        show MC2end1 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        $lgMedC_solved = True
        jump lgMed_done

    if attempts == 0:
        image MC2111tile02_09 = "nand_Gate.png"
        show MC2111tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MC2111tile07_02 = "and_Gate.png"
        show MC2111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MC2111tile07_08 = "nor_Gate.png"
        show MC2111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        $lgMed_attempts +=1
        jump lgMed_lose
        
    jump gamefileMC2

screen logicGatesMC2:
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
        action Jump("hints_lgMedC2")
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
                
            #not gate
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