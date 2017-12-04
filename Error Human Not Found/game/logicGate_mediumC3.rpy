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

label logicGate_mediumC3:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
   #row 0
    image MC3tile00_01 = "r_elbow_br.png"
    image MC3tile00_02 = "r_horizontal.png"
    image MC3tile00_03 = "r_horizontal.png"
    image MC3tile00_04 = "r_horizontal.png"
    image MC3tile00_05 = "r_elbow_bl.png"
    
    show MC3tile00_01 at Position(xpos = 511, xanchor = 0, ypos = 233, yanchor = 0)
    show MC3tile00_02 at Position(xpos = 586, xanchor = 0, ypos = 233, yanchor = 0)
    show MC3tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
    show MC3tile00_04 at Position(xpos = 736, xanchor = 0, ypos = 233, yanchor = 0)
    show MC3tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image MC3tile01_00 = "r_horizontal.png"
    image MC3tile01_01 = "r_t_left.png"
    image MC3tile01_05 = "r_r.png"
    image MC3tile01_06 = "NONE_Gate.png"
    image MC3tile01_07 = "y_horizontal.png"
    image MC3tile01_08 = "y_horizontal.png"
    image MC3tile01_09 = "y_elbow_bl.png"
    
    show MC3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MC3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show MC3tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show MC3tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show MC3tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show MC3tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show MC3tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image MC3tile02_01 = "r_g.png"
    image MC3tile02_02 = "AND_Gate_blue.png"
    image MC3tile02_03 = "r_horizontal.png"
    image MC3tile02_04 = "r_t_down.png"
    image MC3tile02_05 = "r_elbow_tl.png"
    image MC3tile02_09 = "y_g.png"
    image MC3tile02_10 = "AND_Gate_blue.png"
    image MC3tile02_11 = "y_elbow_bl.png"
    
    show MC3tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
    show MC3tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MC3tile03_00 = "g_horizontal.png"
    image MC3tile03_01 = "g_t_left.png"
    image MC3tile03_04 = "r_vertical.png"
    image MC3tile03_05 = "g_elbow_br.png"
    image MC3tile03_06 = "g_horizontal.png"
    image MC3tile03_07 = "g_horizontal.png"
    image MC3tile03_08 = "g_horizontal.png"
    image MC3tile03_09 = "g_elbow_tl.png"
    image MC3tile03_11 = "y_vertical.png"
    
    show MC3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show MC3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MC3tile04_01 = "g_elbow_tr.png"
    image MC3tile04_02 = "g_horizontal.png"
    image MC3tile04_03 = "g_horizontal.png"
    image MC3tile04_04 = "r_jump_g.png"
    image MC3tile04_05 = "g_t_up.png"
    image MC3tile04_06 = "NOT_Gate_blue.png"
    image MC3tile04_07 = "r_horizontal.png"
    image MC3tile04_08 = "r_elbow_bl.png"
    image MC3tile04_11 = "y_vertical.png"
    
    show MC3tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show MC3tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MC3tile05_00 = "g_horizontal.png"
    image MC3tile05_01 = "g_elbow_bl.png"
    image MC3tile05_04 = "r_vertical.png"
    image MC3tile05_08 = "r_vertical.png"
    image MC3tile05_11 = "y_vertical.png"
    
    show MC3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MC3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show MC3tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show MC3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show MC3tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image MC3tile06_01 = "g_r.png"
    image MC3tile06_02 = "NONE_Gate.png"
    image MC3tile06_03 = "y_elbow_bl.png"
    image MC3tile06_04 = "r_elbow_tr.png"
    image MC3tile06_05 = "r_horizontal.png"
    image MC3tile06_06 = "r_elbow_bl.png"
    image MC3tile06_08 = "r_y.png"
    image MC3tile06_09 = "NAND_Gate_blue.png"
    image MC3tile06_10 = "y_elbow_bl.png"
    image MC3tile06_11 = "y_vertical.png"
    
    show MC3tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    show MC3tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image MC3tile07_00 = "r_horizontal.png"
    image MC3tile07_01 = "r_elbow_tl.png"
    image MC3tile07_03 = "y_vertical.png"
    image MC3tile07_06 = "r_y.png"
    image MC3tile07_07 = "NONE_Gate.png"
    image MC3tile07_08 = "y_elbow_tl.png"
    image MC3tile07_10 = "y_vertical.png"
    image MC3tile07_11 = "y_y.png"
    image MC3tile07_12 = "AND_Gate_blue.png"
    image MC3tile07_13 = "y_horizontal.png"
    
    show MC3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
    show MC3tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image MC3tile08_03 = "y_elbow_tr.png"
    image MC3tile08_04 = "y_horizontal.png"
    image MC3tile08_05 = "y_horizontal.png"
    image MC3tile08_06 = "y_elbow_tl.png"
    image MC3tile08_10 =  "y_elbow_tr.png"
    image MC3tile08_11 = "y_elbow_tl.png"
    
    show MC3tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
    show MC3tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show MC3tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show MC3tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show MC3tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
    show MC3tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
    

    #start points
    image MC3start1 = "light_r_on.png"
    show MC3start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image MC3start2 = "light_g_on.png"
    show MC3start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image MC3start3 = "light_g_on.png"
    show MC3start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image MC3start4 = "light_r_on.png"
    show MC3start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image MC3end4 = "light_g_off.png"
    show MC3end4 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)

    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""

    #initial value assignment for dragables
    $ or1x = 848
    $ or1y = 88
    $ nor1x = 1148
    $ nor1y = 88
    $ nand1x = 998
    $ nand1y = 88
    
    #gate values
    $ gate1x = 886
    $ gate1y = 308
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 961
    $ gate3y = 758
   
    # check conditons for locations
    $ or1in1 = False
    $ nor1in1 = False
    $ nand1in1 = False
    $ or1in2 = False
    $ nor1in2 = False
    $ nand1in2 = False
    $ or1in3 = False
    $ nor1in3 = False
    $ nand1in3 = False
     
    #attempts for players
    $ attempts = 6
 
    jump gamefileMC3
    
    
label gamefileMC3:
    
    #calls game screen
    call screen logicGatesMC3
    
    #the first logic gate *******************************************************************************
    if gate_name == "or_gate":
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
            $ or1x = gate1x
            $ or1y = gate1y
            $ or1in1 = True
            $ or1in2 = False
            $ or1in3 = False
            
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
            $ or1x = gate2x
            $ or1y = gate2y
            $ or1in2 = True
            $ or1in1 = False
            $ or1in3 = False
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
            $ or1x = gate3x
            $ or1y = gate3y
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = True
        
        if slot_name == "or return":
            $ or1x = 848
            $ or1y = 88
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = False
            
     #or gate section **********************************************************************       
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in1 = False
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
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
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
            if or1in3 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in3 = False
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
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
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
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
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
            if or1in3 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in3 = False
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
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "nand return" or slot_name == "or return" or slot_name == "nor return"):
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
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "nand_gate":
                $ attempts +=1                
            if slot_name == "or return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "or_gate":
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
    if or1in1 == True:
        image MC31tile01_07 = "r_horizontal.png"
        image MC31tile01_08 = "r_horizontal.png"
        image MC31tile01_09 = "r_elbow_bl.png"
        show MC31tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        show MC31tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        show MC31tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
        image MC31tile02_09 = "r_g.png"
        image MC31tile02_11 = "r_elbow_bl.png"
        show MC31tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        show MC31tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MC31tile03_11 = "r_vertical.png"
        show MC31tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC31tile04_11 = "r_vertical.png"
        show MC31tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MC31tile05_11 = "r_vertical.png"
        show MC31tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC31tile06_11 = "r_vertical.png"
        show MC31tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC31tile07_11 = "r_y.png"
        show MC31tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
  
    if or1in1 == False:
        hide MC31tile01_07
        hide MC31tile01_08
        hide MC31tile01_09
        hide MC31tile02_09
        hide MC31tile02_11
        hide MC31tile03_11
        hide MC31tile04_11
        hide MC31tile05_11
        hide MC31tile06_11
        hide MC31tile07_11
        
    if nor1in1 == True:
        image MC32tile01_07 = "g_horizontal.png"
        image MC32tile01_08 = "g_horizontal.png"
        image MC32tile01_09 = "g_elbow_bl.png"
        show MC32tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        show MC32tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        show MC32tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
        image MC32tile02_09 = "g_g.png"
        image MC32tile02_11 = "g_elbow_bl.png"
        show MC32tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        show MC32tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MC32tile03_11 = "g_vertical.png"
        show MC32tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC32tile04_11 = "g_vertical.png"
        show MC32tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MC32tile05_11 = "g_vertical.png"
        show MC32tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC32tile06_11 = "g_vertical.png"
        show MC32tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC32tile07_11 = "g_y.png"
        show MC32tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
  
    if nor1in1 == False:
        hide MC32tile01_07
        hide MC32tile01_08
        hide MC32tile01_09
        hide MC32tile02_09
        hide MC32tile02_11
        hide MC32tile03_11
        hide MC32tile04_11
        hide MC32tile05_11
        hide MC32tile06_11
        hide MC32tile07_11
        
    if nand1in1 == True:
        image MC33tile01_07 = "g_horizontal.png"
        image MC33tile01_08 = "g_horizontal.png"
        image MC33tile01_09 = "g_elbow_bl.png"
        show MC33tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        show MC33tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        show MC33tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
        image MC33tile02_09 = "g_g.png"
        image MC33tile02_11 = "g_elbow_bl.png"
        show MC33tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        show MC33tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MC33tile03_11 = "g_vertical.png"
        show MC33tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image MC33tile04_11 = "g_vertical.png"
        show MC33tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image MC33tile05_11 = "g_vertical.png"
        show MC33tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image MC33tile06_11 = "g_vertical.png"
        show MC33tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image MC33tile07_11 = "g_y.png"
        show MC33tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
  
    if nand1in1 == False:
        hide MC33tile01_07
        hide MC33tile01_08
        hide MC33tile01_09
        hide MC33tile02_09
        hide MC33tile02_11
        hide MC33tile03_11
        hide MC33tile04_11
        hide MC33tile05_11
        hide MC33tile06_11
        hide MC33tile07_11
        
    if or1in2 == True:
        image MC34tile06_03 = "g_elbow_bl.png"
        show MC34tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        image MC34tile07_03 = "g_vertical.png"
        show MC34tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        image MC34tile07_06 = "r_g.png"
        show MC34tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        image MC34tile08_03 = "g_elbow_tr.png"
        image MC34tile08_04 = "g_horizontal.png"
        image MC34tile08_05 = "g_horizontal.png"
        image MC34tile08_06 = "g_elbow_tl.png"
        show MC34tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
        show MC34tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show MC34tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        show MC34tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        
    if or1in2 == False:
        hide MC34tile06_03
        hide MC34tile07_03
        hide MC34tile07_06
        hide MC34tile08_03
        hide MC34tile08_04
        hide MC34tile08_05
        hide MC34tile08_06
        
    if nor1in2 == True:
        image MC35tile06_03 = "r_elbow_bl.png"
        show MC35tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        image MC35tile07_03 = "r_vertical.png"
        show MC35tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        image MC35tile07_06 = "r_r.png"
        show MC35tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        image MC35tile08_03 = "r_elbow_tr.png"
        image MC35tile08_04 = "r_horizontal.png"
        image MC35tile08_05 = "r_horizontal.png"
        image MC35tile08_06 = "r_elbow_tl.png"
        show MC35tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
        show MC35tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show MC35tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        show MC35tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nor1in2 == False:
        hide MC35tile06_03
        hide MC35tile07_03
        hide MC35tile07_06
        hide MC35tile08_03
        hide MC35tile08_04
        hide MC35tile08_05
        hide MC35tile08_06
        
    if nand1in2 == True:
        image MC36tile06_03 = "g_elbow_bl.png"
        show MC36tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        image MC36tile07_03 = "g_vertical.png"
        show MC36tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        image MC36tile07_06 = "r_g.png"
        show MC36tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
        image MC36tile08_03 = "g_elbow_tr.png"
        image MC36tile08_04 = "g_horizontal.png"
        image MC36tile08_05 = "g_horizontal.png"
        image MC36tile08_06 = "g_elbow_tl.png"
        show MC36tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
        show MC36tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show MC36tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        show MC36tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nand1in2 == False:
        hide MC36tile06_03
        hide MC36tile07_03
        hide MC36tile07_06
        hide MC36tile08_03
        hide MC36tile08_04
        hide MC36tile08_05
        hide MC36tile08_06
        
    if or1in3 == True:
        if nand1in2 == True:
            image MC37tile06_08 = "r_g.png"
            image MC37tile06_10 = "g_elbow_bl.png"
            show MC37tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show MC37tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            image MC37tile07_08 = "g_elbow_tl.png"
            image MC37tile07_10 = "g_vertical.png"
            image MC37tile07_11 = "y_g.png"
            show MC37tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show MC37tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show MC37tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            image MC37tile08_10 =  "g_elbow_tr.png"
            image MC37tile08_11 = "g_elbow_tl.png"
            show MC37tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
            show MC37tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        
    if or1in3 == False or nand1in2 == False:
        hide MC37tile06_08
        hide MC37tile06_10
        hide MC37tile07_08
        hide MC37tile07_10
        hide MC37tile07_11
        hide MC37tile08_10
        hide MC37tile08_11
        
    if or1in3 == True:
        if nor1in2 == True:
            image MC38tile06_08 = "r_r.png"
            image MC38tile06_10 = "g_elbow_bl.png"
            show MC38tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show MC38tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            image MC38tile07_08 = "r_elbow_tl.png"
            image MC38tile07_10 = "g_vertical.png"
            image MC38tile07_11 = "y_g.png"
            show MC38tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show MC38tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show MC38tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            image MC38tile08_10 =  "g_elbow_tr.png"
            image MC38tile08_11 = "g_elbow_tl.png"
            show MC38tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
            show MC38tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
            
    if or1in3 == False or nor1in2 == False:
        hide MC38tile06_08
        hide MC38tile06_10
        hide MC38tile07_08
        hide MC38tile07_10
        hide MC38tile07_11
        hide MC38tile08_10
        hide MC38tile08_11
        
    if nor1in3 == True:
        if or1in2 == True:
            image MC39tile06_08 = "r_r.png"
            image MC39tile06_10 = "g_elbow_bl.png"
            show MC39tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show MC39tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            image MC39tile07_08 = "r_elbow_tl.png"
            image MC39tile07_10 = "g_vertical.png"
            image MC39tile07_11 = "y_g.png"
            show MC39tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show MC39tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show MC39tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            image MC39tile08_10 =  "g_elbow_tr.png"
            image MC39tile08_11 = "g_elbow_tl.png"
            show MC39tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
            show MC39tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nor1in3 == False or or1in2 == False:
        hide MC39tile06_08
        hide MC39tile06_10
        hide MC39tile07_08
        hide MC39tile07_10
        hide MC39tile07_11
        hide MC39tile08_10
        hide MC39tile08_11
        
    if nor1in3 == True:
        if nand1in2 == True:
            image MC30tile06_08 = "r_r.png"
            image MC30tile06_10 = "g_elbow_bl.png"
            show MC30tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show MC30tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            image MC30tile07_08 = "r_elbow_tl.png"
            image MC30tile07_10 = "g_vertical.png"
            image MC30tile07_11 = "y_g.png"
            show MC30tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show MC30tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show MC30tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            image MC30tile08_10 =  "g_elbow_tr.png"
            image MC30tile08_11 = "g_elbow_tl.png"
            show MC30tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
            show MC30tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nor1in3 == False or nand1in2 == False:
        hide MC30tile06_08
        hide MC30tile06_10
        hide MC30tile07_08
        hide MC30tile07_10
        hide MC30tile07_11
        hide MC30tile08_10
        hide MC30tile08_11
        
    if nand1in3 == True:
        if or1in2 == True:
            image MC301tile06_08 = "r_g.png"
            image MC301tile06_10 = "g_elbow_bl.png"
            show MC301tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show MC301tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            image MC301tile07_08 = "g_elbow_tl.png"
            image MC301tile07_10 = "g_vertical.png"
            image MC301tile07_11 = "y_g.png"
            show MC301tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show MC301tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show MC301tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            image MC301tile08_10 =  "g_elbow_tr.png"
            image MC301tile08_11 = "g_elbow_tl.png"
            show MC301tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
            show MC301tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nand1in3 == False or or1in2 == False:
        hide MC301tile06_08
        hide MC301tile06_10
        hide MC301tile07_08
        hide MC301tile07_10
        hide MC301tile07_11
        hide MC301tile08_10
        hide MC301tile08_11
        
    if nand1in3 == True:
        if nor1in2 == True:
            image MC302tile06_08 = "r_g.png"
            image MC302tile06_10 = "g_elbow_bl.png"
            show MC302tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show MC302tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            image MC302tile07_08 = "g_elbow_tl.png"
            image MC302tile07_10 = "g_vertical.png"
            image MC302tile07_11 = "y_g.png"
            show MC302tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show MC302tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show MC302tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            image MC302tile08_10 =  "g_elbow_tr.png"
            image MC302tile08_11 = "g_elbow_tl.png"
            show MC302tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
            show MC302tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nand1in3 == False or nor1in2 == False:
        hide MC302tile06_08
        hide MC302tile06_10
        hide MC302tile07_08
        hide MC302tile07_10
        hide MC302tile07_11
        hide MC302tile08_10
        hide MC302tile08_11
        
        
    if or1in1 == True and ((nor1in2 == True and nand1in3 == True) or (nand1in2 == True and nor1in3 == True)):
        image MC303tile07_13 = "r_horizontal.png"
        show MC303tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
        image MC303tile07_11 = "r_g.png"
        show MC303tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    else:
        hide MC303tile07_13
        hide MC303tile07_11

#win conditions ********
    if (nor1in1 == True and ((or1in2 == True and nand1in3 == True) or (nand1in2 == True and or1in3 == True))) or (nand1in1 == True and ((or1in2 == True and nor1in3 == True) or (nor1in2 == True and or1in3 == True))): 
        image MC304tile07_13 = "g_horizontal.png"
        show MC304tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
        image MC304tile07_11 = "g_g.png"
        show MC304tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
        image MC311tile02_09 = "nand_Gate.png"
        show MC311tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MC311tile07_02 = "or_Gate.png"
        show MC311tile07_02 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image MC311tile07_08 = "nor_Gate.png"
        show MC311tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MC3end1 = "light_g_on.png"
        show MC3end1 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgMedCWin
        $lgMedC_solved = True
        jump lgMed_done

        

    if attempts == 0:
        image MC3111tile02_09 = "nand_Gate.png"
        show MC3111tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MC3111tile07_02 = "or_Gate.png"
        show MC3111tile07_02 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image MC3111tile07_08 = "nor_Gate.png"
        show MC3111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)

        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_lgMedCLose
        $lgMed_attempts +=1
        jump lgMed_loseC
    
    jump gamefileMC3

screen logicGatesMC3:
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
        action Jump("hints_lgMedC3")
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
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88