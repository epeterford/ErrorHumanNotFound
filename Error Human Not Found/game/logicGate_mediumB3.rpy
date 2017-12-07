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

label logicGate_mediumB3:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
   #row 1 (row has a light)
    image LGMB3tile01_00 = "g_horizontal.png"
    image LGMB3tile01_01 = "g_t_down.png"
    image LGMB3tile01_02 = "g_horizontal.png"
    image LGMB3tile01_03 = "g_horizontal.png"
    image LGMB3tile01_04 = "g_horizontal.png"
    image LGMB3tile01_05 = "g_horizontal.png"
    image LGMB3tile01_06 = "g_elbow_bl.png"

    
    show LGMB3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB3tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB3tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB3tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB3tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB3tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)

    
    #row 2
    image LGMB3tile02_01 = "g_g.png"
    image LGMB3tile02_02 = "NAND_Gate_blue.png"
    image LGMB3tile02_03 = "r_elbow_bl.png"
    image LGMB3tile02_06 = "g_y.png"
    image LGMB3tile02_07 = "NONE_Gate.png"
    image LGMB3tile02_08 = "y_horizontal.png"
    image LGMB3tile02_09 = "y_horizontal.png"
    image LGMB3tile02_10 = "y_elbow_bl.png"
    
    show LGMB3tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB3tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image LGMB3tile03_00 = "g_horizontal.png"
    image LGMB3tile03_01 = "g_elbow_tl.png"
    image LGMB3tile03_03 = "r_g.png"
    image LGMB3tile03_04 = "NONE_Gate.png"
    image LGMB3tile03_05 = "y_horizontal.png"
    image LGMB3tile03_06 = "y_t_left.png"
    image LGMB3tile03_10 = "y_y.png"
    image LGMB3tile03_11 = "AND_Gate_blue.png"
    image LGMB3tile03_12 = "y_horizontal.png"
    image LGMB3tile03_13 = "y_horizontal.png"
    
    show LGMB3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB3tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image LGMB3tile04_03 = "g_vertical.png"
    image LGMB3tile04_06 = "y_elbow_tr.png"
    image LGMB3tile04_07 = "y_horizontal.png"
    image LGMB3tile04_08 = "y_elbow_bl.png"
    image LGMB3tile04_10 = "y_vertical.png"
    
    show LGMB3tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show LGMB3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show LGMB3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show LGMB3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show LGMB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image LGMB3tile05_00 = "g_horizontal.png"
    image LGMB3tile05_01 = "g_horizontal.png"
    image LGMB3tile05_02 = "g_horizontal.png"
    image LGMB3tile05_03 = "g_t_left.png"
    image LGMB3tile05_05 = "y_elbow_br.png"
    image LGMB3tile05_06 = "y_elbow_bl.png"
    image LGMB3tile05_08 = "y_y.png"
    image LGMB3tile05_09 = "OR_Gate_blue.png"
    image LGMB3tile05_10 = "y_elbow_tl.png"
    
    show LGMB3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image LGMB3tile06_03 = "g_g.png"
    image LGMB3tile06_04 = "NONE_Gate.png"
    image LGMB3tile06_05 = "y_elbow_tl.png"
    image LGMB3tile06_06 = "y_g.png"
    image LGMB3tile06_07 = "NOR_Gate_blue.png"
    image LGMB3tile06_08 = "y_elbow_tl.png"
    
    show LGMB3tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB3tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image LGMB3tile07_00 = "g_horizontal.png"
    image LGMB3tile07_01 = "g_horizontal.png"
    image LGMB3tile07_02 = "g_horizontal.png"
    image LGMB3tile07_03 = "g_t_up.png"
    image LGMB3tile07_04 = "g_horizontal.png"
    image LGMB3tile07_05 = "g_horizontal.png"
    image LGMB3tile07_06 = "g_elbow_tl.png"
    
    show LGMB3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB3tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB3tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB3tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB3tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB3tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)

    #start points
    image LGMB3start1 = "light_g_on.png"
    show LGMB3start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image LGMB3start2 = "light_g_on.png"
    show LGMB3start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image LGMB3start3 = "light_g_on.png"
    show LGMB3start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image LGMB3start4 = "light_g_on.png"
    show LGMB3start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    

    image LGMB3end1 = "light_g_off.png"
    show LGMB3end1 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)

    
    
    
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
    $ gate1x = 736
    $ gate1y = 458
    $ gate2x = 961
    $ gate2y = 383
    $ gate3x = 736
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
    $ attempts = 5
 
    jump gamefileMB3
    
    
label gamefileMB3:
    
    #calls game screen
    call screen logicgatesMB3
    
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
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "nand return" or slot_name == "and return" or slot_name == "nor return"):
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
    if nand1in1:
        image aLGMB3tile02_06 = "g_g.png"
        show aLGMB3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        image aLGMB3tile03_05 = "g_horizontal.png"
        image aLGMB3tile03_06 = "g_t_left.png"
        show aLGMB3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
        show aLGMB3tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        image aLGMB3tile04_06 = "g_elbow_tr.png"
        image aLGMB3tile04_07 = "g_horizontal.png"
        image aLGMB3tile04_08 = "g_elbow_bl.png"
        show aLGMB3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        show aLGMB3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show aLGMB3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        image aLGMB3tile05_08 = "g_y.png"
        show aLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        
    if nand1in1 == False:
        hide aLGMB3tile02_06
        hide aLGMB3tile03_05
        hide aLGMB3tile03_06
        hide aLGMB3tile04_06
        hide aLGMB3tile04_07
        hide aLGMB3tile04_08
        hide aLGMB3tile05_08

    if and1in1 == True or nor1in1 == True:
        image nLGMB3tile02_06 = "g_r.png"
        show nLGMB3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        image nLGMB3tile03_05 = "r_horizontal.png"
        image nLGMB3tile03_06 = "r_t_left.png"
        show nLGMB3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
        show nLGMB3tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        image nLGMB3tile04_06 = "r_elbow_tr.png"
        image nLGMB3tile04_07 = "r_horizontal.png"
        image nLGMB3tile04_08 = "r_elbow_bl.png"
        show nLGMB3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        show nLGMB3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show nLGMB3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        image nLGMB3tile05_08 = "r_y.png"
        show nLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        
    if and1in1 == False and nor1in1 == False:
        hide nLGMB3tile02_06
        hide nLGMB3tile03_05
        hide nLGMB3tile03_06
        hide nLGMB3tile04_08
        hide nLGMB3tile05_08
        hide nLGMB3tile04_06
        hide nLGMB3tile04_07
        
    if and1in2 == True:
        if nand1in1:
            image aLGMB3tile02_08S = "g_horizontal.png"
            image a2LGMB3tile02_09S = "g_horizontal.png"
            image aLGMB3tile02_10S = "g_elbow_bl.png"
            show aLGMB3tile02_08S at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
            show a2LGMB3tile02_09S at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
            show aLGMB3tile02_10S at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
            image aLGMB3tile03_10S = "g_y.png"
            show aLGMB3tile03_10S at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
            
        if nor1in1:
            image aLGMB3tile02_08 = "r_horizontal.png"
            image a2LGMB3tile02_09 = "r_horizontal.png"
            image aLGMB3tile02_10 = "r_elbow_bl.png"
            show aLGMB3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
            show a2LGMB3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
            show aLGMB3tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
            image aLGMB3tile03_10 = "r_y.png"
            show aLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
            
    if and1in2 == False or (nand1in1 == False):
        hide aLGMB3tile02_08S
        hide aLGMB3tile02_10S
        hide aLGMB3tile03_10S
        hide a2LGMB3tile02_09S
        
    if and1in2== False or (nor1in1 == False):
        hide aLGMB3tile02_08
        hide aLGMB3tile02_10
        hide aLGMB3tile03_10
        hide a2LGMB3tile02_09
        
    if nand1in2:
        if nor1in1 or and1in1:
            image nLGMB3tile02_08 = "g_horizontal.png"
            image nLGMB3tile02_09 = "g_horizontal.png"
            image nLGMB3tile02_10 = "g_elbow_bl.png"
            show nLGMB3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
            show nLGMB3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
            show nLGMB3tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
            image nLGMB3tile03_10 = "g_y.png"
            show nLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    if nand1in2 == False or (nor1in1 == False and and1in1==False):
        hide nLGMB3tile02_08
        hide nLGMB3tile02_09
        hide nLGMB3tile02_10
        hide nLGMB3tile03_10
            
    if nor1in2 == True:
        if and1in1 or nand1in1:
            image noLGMB3tile02_08 = "r_horizontal.png"
            image no2LGMB3tile02_09 = "r_horizontal.png"
            image noLGMB3tile02_10 = "r_elbow_bl.png"
            show noLGMB3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
            show no2LGMB3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
            show noLGMB3tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
            image noLGMB3tile03_10 = "r_y.png"
            show noLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    
    if nor1in2 == False or (and1in1 == False and nand1in1 == False):
        hide noLGMB3tile02_08
        hide no2LGMB3tile02_09
        hide noLGMB3tile02_10
        hide noLGMB3tile03_10  
            
    if and1in3 == True:
        image aLGMB3tile05_05 = "g_elbow_br.png"
        image aLGMB3tile05_06 = "g_elbow_bl.png"
        show aLGMB3tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show aLGMB3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image aLGMB3tile06_05 = "g_elbow_tl.png"
        image aLGMB3tile06_06 = "g_g.png"
        image aLGMB3tile06_08 = "r_elbow_tl.png"
        show aLGMB3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show aLGMB3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show aLGMB3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        image a3LGMB3tile05_08 = "y_r.png"
        show a3LGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    if and1in3 == False:
        hide aLGMB3tile05_05
        hide aLGMB3tile05_06
        hide aLGMB3tile06_05
        hide aLGMB3tile06_06
        hide aLGMB3tile06_08
        hide a3LGMB3tile05_08
        
    if nand1in3 == True:
        image nLGMB3tile05_05 = "r_elbow_br.png"
        image nLGMB3tile05_06 = "r_elbow_bl.png"
        show nLGMB3tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show nLGMB3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image nLGMB3tile06_05 = "r_elbow_tl.png"
        image nLGMB3tile06_06 = "r_g.png"
        image nLGMB3tile06_08 = "r_elbow_tl.png"
        show nLGMB3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show nLGMB3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show nLGMB3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        image n3LGMB3tile05_08 = "y_r.png"
        show n3LGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    if nand1in3 == False:
        hide nLGMB3tile05_05
        hide nLGMB3tile05_06
        hide nLGMB3tile06_05
        hide nLGMB3tile06_06
        hide nLGMB3tile06_08
        hide n3LGMB3tile05_08
        
    if nor1in3 == True:
        image oLGMB3tile05_05 = "r_elbow_br.png"
        image oLGMB3tile05_06 = "r_elbow_bl.png"
        show oLGMB3tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show oLGMB3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image oLGMB3tile06_05 = "r_elbow_tl.png"
        image oLGMB3tile06_06 = "r_g.png"
        image oLGMB3tile06_08 = "r_elbow_tl.png"
        show oLGMB3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show oLGMB3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show oLGMB3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        image o3LGMB3tile05_08 = "y_r.png"
        show o3LGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    if nor1in3 == False:
        hide oLGMB3tile05_05
        hide oLGMB3tile05_06
        hide oLGMB3tile06_05
        hide oLGMB3tile06_06
        hide oLGMB3tile06_08
        hide o3LGMB3tile05_08        
        
    if (and1in1 == True and (nor1in3 or nand1in3)):
        image anoLGMB3tile04_10 = "r_vertical.png"
        show anoLGMB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image anoLGMB3tile05_08 = "r_r.png"
        image anoLGMB3tile05_10 = "r_elbow_tl.png"
        show anoLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show anoLGMB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image 9onaLGMB3tile03_10 = "y_r.png"
        show 9onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        
    else:
        hide anoLGMB3tile04_10
        hide anoLGMB3tile05_08
        hide anoLGMB3tile05_10
        hide 9onaLGMB3tile03_10
    
    if (nand1in3 == True and nor1in1 == True):
        image nanoLGMB3tile04_10 = "r_vertical.png"
        show nanoLGMB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image nanoLGMB3tile05_08 = "r_r.png"
        image nanoLGMB3tile05_10 = "r_elbow_tl.png"
        show nanoLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show nanoLGMB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image 11onaLGMB3tile03_10 = "y_r.png"
        show 11onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        
    else:
        hide nanoLGMB3tile04_10
        hide nanoLGMB3tile05_08
        hide nanoLGMB3tile05_10
        hide 11onaLGMB3tile03_10
        
    if (nand1in1 == True and nor1in3 == True):
        image 1nanoLGMB3tile04_10 = "g_vertical.png"
        show 1nanoLGMB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image 1nanoLGMB3tile05_08 = "g_r.png"
        image 1nanoLGMB3tile05_10 = "g_elbow_tl.png"
        show 1nanoLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show 1nanoLGMB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image 8onaLGMB3tile03_10 = "y_g.png"
        show 8onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide 1nanoLGMB3tile04_10
        hide 1nanoLGMB3tile05_08
        hide 1nanoLGMB3tile05_10
        hide 8onaLGMB3tile03_10
        
    if (and1in3 == True and nor1in1 == True):
        image 2nanoLGMB3tile04_10 = "r_vertical.png"
        show 2nanoLGMB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image 2nanoLGMB3tile05_08 = "r_r.png"
        image 2nanoLGMB3tile05_10 = "r_elbow_tl.png"
        show 2nanoLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show 2nanoLGMB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image 7onaLGMB3tile03_10 = "y_r.png"
        show 7onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide 2nanoLGMB3tile04_10
        hide 2nanoLGMB3tile05_08
        hide 2nanoLGMB3tile05_10
        hide 7onaLGMB3tile03_10
    if (and1in3 == True and nand1in1 ==True):
        image 3nanoLGMB3tile04_10 = "g_vertical.png"
        show 3nanoLGMB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image 3nanoLGMB3tile05_08 = "g_r.png"
        image 3nanoLGMB3tile05_10 = "g_elbow_tl.png"
        show 3nanoLGMB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show 3nanoLGMB3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image 6onaLGMB3tile03_10 = "y_g.png"
        show 6onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide 3nanoLGMB3tile04_10
        hide 3nanoLGMB3tile05_08
        hide 3nanoLGMB3tile05_10
        hide 6onaLGMB3tile03_10
        
    if (and1in1 and nand1in2 and nor1in3)or (nor1in1 and nand1in2 and and1in3):
        image onaLGMB3tile03_12 = "r_horizontal.png"
        image onaLGMB3tile03_13 = "r_horizontal.png"
        show onaLGMB3tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        show onaLGMB3tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image onaLGMB3tile03_10 = "g_r.png"
        show onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide onaLGMB3tile03_12
        hide onaLGMB3tile03_13
        hide onaLGMB3tile03_10

    if (and1in1 and nand1in3 and nor1in2) or (nor1in1 and and1in2 and nand1in3):
        image 1onaLGMB3tile03_12 = "r_horizontal.png"
        image 1onaLGMB3tile03_13 = "r_horizontal.png"
        show 1onaLGMB3tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        show 1onaLGMB3tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image 1onaLGMB3tile03_10 = "r_r.png"
        show 1onaLGMB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide 1onaLGMB3tile03_12
        hide 1onaLGMB3tile03_13
        hide 1onaLGMB3tile03_10
        
    if (nand1in1 and nor1in2 and and1in3):
        image 1onaLGMB3tile03_12S = "r_horizontal.png"
        image 1onaLGMB3tile03_13S = "r_horizontal.png"
        show 1onaLGMB3tile03_12S at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        show 1onaLGMB3tile03_13S at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image 1onaLGMB3tile03_10S = "r_g.png"
        show 1onaLGMB3tile03_10S at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide 1onaLGMB3tile03_12S
        hide 1onaLGMB3tile03_13S
        hide 1onaLGMB3tile03_10S
        
#win conditions ********
    if (and1in2 and nand1in1 and nor1in3): 
        image 1onaLGMB3tile03_12Sx = "g_horizontal.png"
        image 1onaLGMB3tile03_13Sx = "g_horizontal.png"
        show 1onaLGMB3tile03_12Sx at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        show 1onaLGMB3tile03_13Sx at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image 1onaLGMB3tile03_10Sx = "g_g.png"
        show 1onaLGMB3tile03_10Sx at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        image wLGMB3tile02_09 = "nand_Gate.png"
        show wLGMB3tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image wLGMB3tile07_02 = "and_Gate.png"
        show wLGMB3tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image wLGMB3tile07_08 = "nor_Gate.png"
        show wLGMB3tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image wLGMB3end2 = "light_g_on.png"
        show wLGMB3end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgMedBWin
        $lgMedB_solved = True
        jump lgMed_winB


    if attempts == 0:
        image fLGMB3tile02_09 = "nand_Gate.png"
        show fLGMB3tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image fLGMB3tile07_02 = "and_Gate.png"
        show fLGMB3tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image fLGMB3tile07_08 = "nor_Gate.png"
        show fLGMB3tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_lgMedBLose
        $lgMed_attempts +=1
        jump lgMed_loseB
    
    jump gamefileMB3

screen logicgatesMB3:
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
        action Jump("hints_lgMedB3")
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