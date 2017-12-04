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

label logicGate_mediumB2:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
   #row 1 (row has a light)
    image LGMB2tile01_00 = "r_horizontal.png"
    image LGMB2tile01_01 = "r_horizontal.png"
    image LGMB2tile01_02 = "r_elbow_bl.png"
    image LGMB2tile01_04 = "y_elbow_br.png"
    image LGMB2tile01_05 = "y_horizontal.png"
    image LGMB2tile01_06 = "y_elbow_bl.png"
    image LGMB2tile01_08 = "y_elbow_br.png"
    image LGMB2tile01_09 = "y_elbow_bl.png"

    
    show LGMB2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show LGMB2tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image LGMB2tile02_02 = "r_g.png"
    image LGMB2tile02_03 = "NONE_Gate.png"
    image LGMB2tile02_04 = "y_elbow_tl.png"
    image LGMB2tile02_06 = "y_g.png"
    image LGMB2tile02_07 = "NAND_Gate_blue.png"
    image LGMB2tile02_08 = "y_elbow_tl.png"
    image LGMB2tile02_09 = "y_r.png"
    image LGMB2tile02_10 = "NONE_Gate.png"
    image LGMB2tile02_11 = "y_elbow_bl.png"
    
    show LGMB2tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
    show LGMB2tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image LGMB2tile03_00 = "g_horizontal.png"
    image LGMB2tile03_01 = "g_horizontal.png"
    image LGMB2tile03_02 = "g_t_up.png"
    image LGMB2tile03_03 = "g_horizontal.png"
    image LGMB2tile03_04 = "g_horizontal.png"
    image LGMB2tile03_05 = "g_t_down.png"
    image LGMB2tile03_06 = "g_elbow_tl.png"
    image LGMB2tile03_09 = "r_vertical.png"
    image LGMB2tile03_11 = "y_y.png"
    image LGMB2tile03_12 = "OR_Gate_blue.png"
    image LGMB2tile03_13 = "y_horizontal.png"
    
    show LGMB2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show LGMB2tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image LGMB2tile04_05 = "g_vertical.png"
    image LGMB2tile04_09 = "r_vertical.png"
    image LGMB2tile04_11 = "y_vertical.png"
    

    show LGMB2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show LGMB2tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show LGMB2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image LGMB2tile05_00 = "g_horizontal.png"
    image LGMB2tile05_01 = "g_horizontal.png"
    image LGMB2tile05_02 = "g_elbow_bl.png"
    image LGMB2tile05_05 = "g_r.png"
    image LGMB2tile05_06 = "AND_Gate_blue.png"
    image LGMB2tile05_07 = "r_horizontal.png"
    image LGMB2tile05_08 = "r_horizontal.png"
    image LGMB2tile05_09 = "r_t_left.png"
    image LGMB2tile05_11 = "y_vertical.png"
    
    show LGMB2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show LGMB2tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image LGMB2tile06_02 = "g_g.png"
    image LGMB2tile06_03 = "NOR_Gate_blue.png"
    image LGMB2tile06_04 = "r_horizontal.png"
    image LGMB2tile06_05 = "r_elbow_tl.png"
    image LGMB2tile06_09 = "r_y.png"
    image LGMB2tile06_10 = "OR_Gate_blue.png"
    image LGMB2tile06_11 = "y_elbow_tl.png"
    
    show LGMB2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB2tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB2tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB2tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB2tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    show LGMB2tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image LGMB2tile07_00 = "g_horizontal.png"
    image LGMB2tile07_01 = "g_horizontal.png"
    image LGMB2tile07_02 = "g_t_up.png"
    image LGMB2tile07_03 = "g_horizontal.png"
    image LGMB2tile07_04 = "g_horizontal.png"
    image LGMB2tile07_05 = "g_horizontal.png"
    image LGMB2tile07_06 = "g_horizontal.png"
    image LGMB2tile07_07 = "NONE_Gate.png"
    image LGMB2tile07_08 = "y_horizontal.png"
    image LGMB2tile07_09 = "y_elbow_tl.png"
    
    show LGMB2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show LGMB2tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)

    #start points
    image LGB2Mstart1 = "light_r_on.png"
    show LGB2Mstart1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image LGB2Mstart2 = "light_g_on.png"
    show LGB2Mstart2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image LGB2Mstart3 = "light_g_on.png"
    show LGB2Mstart3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image LGB2Mstart4 = "light_g_on.png"
    show LGB2Mstart4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these

    image LGMB2tileend1 = "light_r_off.png"
    show LGMB2tileend1 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)

    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""

    #initial value assignment for dragables
    $ nand1x = 998
    $ nand1y = 88
    $ or1x = 848
    $ or1y = 88
    $ not1x = 548
    $ not1y = 88
    
    #gate values
    $ gate1x = 661
    $ gate1y = 383
    $ gate2x = 1186
    $ gate2y = 383
    $ gate3x = 961
    $ gate3y = 758
   
    # check conditons for locations
    $ nand1in1 = False
    $ or1in1 = False
    $ not1in1 = False
    $ nand1in2 = False
    $ or1in2 = False
    $ not1in2 = False
    $ nand1in3 = False
    $ or1in3 = False
    $ not1in3 = False
     
    #attempts for players
    $ attempts = 5
 
    jump gamefileMB2
    
    
label gamefileMB2:
    
    #calls game screen
    call screen logicgatesMB2
    
    #the first logic gate *******************************************************************************
    if gate_name == "nand_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
            if not1in1 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in1 = False
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
            if not1in2 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in2 = False
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
            if not1in3 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in3 = False
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
            
     #or gate section **********************************************************************       
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nand1in1 == True:
               $ nand1x = 998
               $ nand1y = 88
               $ nand1in1 = False
            if not1in1 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in1 = False
                
            #sets values for checks
            $ or1x = gate1x
            $ or1y = gate1y
            $ or1in1 = True
            $ or1in2 = False
            $ or1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nand1in2 == True:
               $ nand1x = 998
               $ nand1y = 88
               $ nand1in2 = False
            if not1in2 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in2 = False
                
            #sets values for checks
            $ or1x = gate2x
            $ or1y = gate2y
            $ or1in2 = True
            $ or1in1 = False
            $ or1in3 = False
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
            if not1in3 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in3 = False
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
            
     #not gate section **********************************************************************       
    if gate_name == "not_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nand1in1 == True:
               $ nand1x = 998
               $ nand1y = 88
               $ nand1in1 = False
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
            #sets values for checks
            $ not1x = gate1x
            $ not1y = gate1y
            $ not1in1 = True
            $ not1in2 = False
            $ not1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
            #sets values for checks
            $ not1x = gate2x

            $ not1y = gate2y
            $ not1in2 = True
            $ not1in1 = False
            $ not1in3 = False
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
            if or1in3 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in3 = False
            #sets values for checks
            $ not1x = gate3x
            $ not1y = gate3y
            $ not1in2 = False
            $ not1in1 = False
            $ not1in3 = True
            
        if slot_name == "not return":
            $ not1x = 548
            $ not1y = 88
            $ not1in2 = False
            $ not1in1 = False
            $ not1in3 = False
            
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name=="or return" or slot_name=="nand return" or slot_name=="not return"):
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
            if slot_name == "not return" and gate_name == "not_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "not return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "not return" and gate_name == "nand_gate":
                $ attempts +=1                
            if slot_name == "or return" and gate_name == "not_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "not_gate":
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
        image oLGMB2tile01_04 = "g_elbow_br.png"
        image oLGMB2tile01_05 = "g_horizontal.png"
        image oLGMB2tile01_06 = "g_elbow_bl.png"
        image oLGMB2tile01_08 = "r_elbow_br.png"
        image oLGMB2tile01_09 = "r_elbow_bl.png"
        show oLGMB2tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
        show oLGMB2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
        show oLGMB2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show oLGMB2tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        show oLGMB2tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
        image oLGMB2tile02_04 = "g_elbow_tl.png"
        image oLGMB2tile02_06 = "g_g.png"
        image oLGMB2tile02_08 = "r_elbow_tl.png"
        image oLGMB2tile02_09 = "r_r.png"
        show oLGMB2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show oLGMB2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show oLGMB2tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show oLGMB2tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        
    if or1in1 == False:
        hide oLGMB2tile01_04
        hide oLGMB2tile01_05
        hide oLGMB2tile01_06
        hide oLGMB2tile01_08
        hide oLGMB2tile01_09
        hide oLGMB2tile02_04
        hide oLGMB2tile02_06
        hide oLGMB2tile02_08
        hide oLGMB2tile02_09
        
    if nand1in1 == True:
        image nLGMB2tile01_04 = "g_elbow_br.png"
        image nLGMB2tile01_05 = "g_horizontal.png"
        image nLGMB2tile01_06 = "g_elbow_bl.png"
        image nLGMB2tile01_08 = "r_elbow_br.png"
        image nLGMB2tile01_09 = "r_elbow_bl.png"
        show nLGMB2tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
        show nLGMB2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
        show nLGMB2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show nLGMB2tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        show nLGMB2tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
        image nLGMB2tile02_04 = "g_elbow_tl.png"
        image nLGMB2tile02_06 = "g_g.png"
        image nLGMB2tile02_08 = "r_elbow_tl.png"
        image nLGMB2tile02_09 = "r_r.png"
        show nLGMB2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show nLGMB2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show nLGMB2tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        show nLGMB2tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        
    if nand1in1 == False:
        hide nLGMB2tile01_04
        hide nLGMB2tile01_05
        hide nLGMB2tile01_06
        hide nLGMB2tile01_08
        hide nLGMB2tile01_09
        hide nLGMB2tile02_04
        hide nLGMB2tile02_06
        hide nLGMB2tile02_08
        hide nLGMB2tile02_09

    if or1in2 == True and nand1in1 == True:
        image oLGMB2tile02_11 = "r_elbow_bl.png"
        show oLGMB2tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image oLGMB2tile03_11 = "r_y.png"
        show oLGMB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        
    if or1in2 == False or nand1in1 == False: 
        hide oLGMB2tile02_11
        hide oLGMB2tile03_11
        
    if nand1in2 == True and or1in1 == True:
        image nLGMB2tile02_11 = "g_elbow_bl.png"
        show nLGMB2tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image nLGMB2tile03_11 = "g_y.png"
        show nLGMB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        
    if nand1in2 == False or or1in1 == False: 
        hide nLGMB2tile02_11
        hide nLGMB2tile03_11
     
    if not1in3 == True:
        image noLGMB2tile03_11 = "y_r.png"
        show noLGMB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image noLGMB2tile04_11 = "r_vertical.png"
        show noLGMB2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image noLGMB2tile05_11 = "r_vertical.png"    
        show noLGMB2tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image noLGMB2tile06_09 = "r_r.png"
        image noLGMB2tile06_11 = "r_elbow_tl.png"
        show noLGMB2tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show noLGMB2tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        image noLGMB2tile07_08 = "r_horizontal.png"
        image noLGMB2tile07_09 = "r_elbow_tl.png"
        show noLGMB2tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        show noLGMB2tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)

    if not1in3 == False:
        hide noLGMB2tile03_11
        hide noLGMB2tile04_11
        hide noLGMB2tile05_11
        hide noLGMB2tile06_09
        hide noLGMB2tile06_11
        hide noLGMB2tile07_08
        hide noLGMB2tile07_09
        
    if not1in3 == True and (nand1in2 == True and or1in1 == True):  
        image ifLGMB2tile03_13 = "g_horizontal.png"
        show ifLGMB2tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image ifLGMB2tile03_11 = "g_r.png"
        show ifLGMB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide ifLGMB2tile03_13
        hide ifLGMB2tile03_11
        
#win conditions ********
    if nand1in1 == True and not1in3 == True and or1in2 == True: 
        image wLGMB2tile03_11 = "r_r.png"
        show wLGMB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        image wLGMB2tile03_13 = "r_horizontal.png"
        show wLGMB2tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image wLGMB2tile02_09 = "not_Gate.png"
        show wLGMB2tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image wLGMB2tile07_02 = "nand_Gate.png"
        show wLGMB2tile07_02 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image wLGMB2tile07_08 = "or_Gate.png"
        show wLGMB2tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image wLGMB2tileend = "light_r_on.png"
        show wLGMB2tileend at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgMedBWin
        $lgMedB_solved = True
        jump lgMed_winB

    if attempts == 0:
        image lLGMB2tile02_09 = "not_Gate.png"
        show lLGMB2tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image lLGMB2tile07_02 = "nand_Gate.png"
        show lLGMB2tile07_02 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image lLGMB2tile07_08 = "or_Gate.png"
        show lLGMB2tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_lgMedBLose
        $lgMed_attempts +=1
        jump lgMed_loseB
    
    jump gamefileMB2

screen logicgatesMB2:
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
        action Jump("hints_lgMedB2")
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
                drag_name "nand_gate"
                child "nAND_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nand1x ypos nand1y
                
            #or gates
            drag:
                drag_name "or_gate"
                child "or_Gate.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y
                
            #not gate
            drag:
                drag_name "not_gate"
                child "not_Gate.png"
                droppable False
                dragged gate_dragged
                xpos not1x ypos not1y

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
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88
           
            drag:
                drag_name "not return"
                child "cover.png"
                draggable False
                xpos 548 ypos 88
                
            drag:
                drag_name "or return"
                child "cover.png"
                draggable False
                xpos 848 ypos 88