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

label logicGate_mediumC1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #row 0
    image MC1tile00_01 = "g_elbow_br.png"
    image MC1tile00_02 = "g_horizontal.png"
    image MC1tile00_03 = "g_horizontal.png"
    image MC1tile00_04 = "g_horizontal.png"
    image MC1tile00_05 = "g_horizontal.png"
    image MC1tile00_06 = "g_horizontal.png"
    image MC1tile00_07 = "g_horizontal.png"
    image MC1tile00_08 = "g_horizontal.png"
    image MC1tile00_09 = "g_elbow_bl.png"
    
    show MC1tile00_01 at Position(xpos = 511, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_02 at Position(xpos = 586, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_04 at Position(xpos = 736, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_07 at Position(xpos = 961, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_08 at Position(xpos = 1036, xanchor = 0, ypos = 233, yanchor = 0)
    show MC1tile00_09 at Position(xpos = 1111, xanchor = 0, ypos = 233, yanchor = 0)

   
    #row 1 (row has a light)
    image MC1tile01_00 = "g_horizontal.png"
    image MC1tile01_01 = "g_t_left.png"
    image MC1tile01_04 = "g_elbow_br.png"
    image MC1tile01_05 = "g_horizontal.png"
    image MC1tile01_06 = "g_elbow_bl.png"
    image MC1tile01_09 = "g_r.png"
    image MC1tile01_10= "NONE_Gate.png"
    image MC1tile01_11 = "y_elbow_bl.png"
    
    show MC1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
    show MC1tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)

    
    #row 2
    image MC1tile02_01 = "g_r.png"
    image MC1tile02_02 = "OR_Gate_blue.png"
    image MC1tile02_03 = "g_horizontal.png"
    image MC1tile02_04 = "g_elbow_tl.png"
    image MC1tile02_06 = "g_r.png"
    image MC1tile02_07 = "NOR_Gate_blue.png"
    image MC1tile02_08 = "r_horizontal.png"
    image MC1tile02_09 = "r_elbow_tl.png"
    image MC1tile02_11 = "y_vertical.png"
    
    show MC1tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show MC1tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MC1tile03_00 = "r_horizontal.png"
    image MC1tile03_01 = "r_t_up.png"
    image MC1tile03_02 = "r_horizontal.png"
    image MC1tile03_03 = "r_horizontal.png"
    image MC1tile03_04 = "r_horizontal.png"
    image MC1tile03_05 = "r_horizontal.png"
    image MC1tile03_06 = "r_elbow_tl.png"
    image MC1tile03_11 = "y_y.png"
    image MC1tile03_12 = "and_Gate_blue.png"
    image MC1tile03_13 = "y_horizontal.png"
    
    show MC1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show MC1tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MC1tile04_02 = "g_elbow_br.png"
    image MC1tile04_03 = "g_horizontal.png"
    image MC1tile04_04 = "g_horizontal.png"
    image MC1tile04_05 = "g_elbow_bl.png"
    image MC1tile04_11 = "y_vertical.png"
    
    show MC1tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show MC1tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show MC1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show MC1tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show MC1tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MC1tile05_00 = "g_horizontal.png"
    image MC1tile05_01 = "g_horizontal.png"
    image MC1tile05_02 = "g_t_left.png"
    image MC1tile05_05 = "g_r.png"
    image MC1tile05_06 = "NONE_Gate.png"
    image MC1tile05_07 = "y_t_down.png"
    image MC1tile05_08 = "y_horizontal.png"
    image MC1tile05_09 = "y_elbow_bl.png"
    image MC1tile05_11 = "y_vertical.png"
    
    show MC1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show MC1tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image MC1tile06_02 = "g_g.png"
    image MC1tile06_03 = "NAND_Gate_blue.png"
    image MC1tile06_04 = "r_horizontal.png"
    image MC1tile06_05 = "r_t_left.png"
    image MC1tile06_07 = "y_vertical.png"
    image MC1tile06_09 = "y_y.png"
    image MC1tile06_10 = "OR_Gate_blue.png"
    image MC1tile06_11 = "y_elbow_tl.png"
    
    show MC1tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    show MC1tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image MC1tile07_00 = "g_horizontal.png"
    image MC1tile07_01 = "g_horizontal.png"
    image MC1tile07_02 = "g_elbow_tl.png"
    image MC1tile07_05 = "r_vertical.png"
    image MC1tile07_07 = "y_r.png"
    image MC1tile07_08 = "NONE_Gate.png"
    image MC1tile07_09 = "y_elbow_tl.png"
    
    show MC1tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show MC1tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show MC1tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show MC1tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show MC1tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show MC1tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show MC1tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image MC1tile08_05 = "r_elbow_tr.png"
    image MC1tile08_06 = "r_horizontal.png"
    image MC1tile08_07 = "r_elbow_tl.png"
    
    show MC1tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show MC1tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show MC1tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    


    #start points
    image MC1start1 = "light_g_on.png"
    show MC1start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image MC1start2 = "light_r_on.png"
    show MC1start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image MC1start3 = "light_g_on.png"
    show MC1start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image MC1start4 = "light_g_on.png"
    show MC1start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image MC1end2 = "light_g_off.png"
    show MC1end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)

    
    
    
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
    $ gate1x = 1186
    $ gate1y = 308
    $ gate2x = 886
    $ gate2y = 608
    $ gate3x = 1036
    $ gate3y = 758
   
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
 
    jump gamefileMC1
    
    
label gamefileMC1:
    
    #calls game screen
    call screen logicGatesMC1
    
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
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name=="nor return" or slot_name=="and return" or slot_name=="nand return"):
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
    if and1in1 == True or nor1in1 == True:
        image MC12tile01_11 = "r_elbow_bl.png"
        show MC12tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image MC12tile02_11 = "r_vertical.png"
        show MC12tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MC12tile03_11 = "r_y.png"
        show MC12tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        
    if and1in1 == False and nor1in1 == False:
        hide MC12tile01_11
        hide MC12tile02_11
        hide MC12tile03_11
        
    if nand1in1 == True:
        image MC13tile01_11 = "g_elbow_bl.png"
        show MC13tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image MC13tile02_11 = "g_vertical.png"
        show MC13tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MC13tile03_11 = "g_y.png"
        show MC13tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

    if nand1in1 == False:
        hide MC13tile01_11
        hide MC13tile02_11
        hide MC13tile03_11
        

        
    if and1in2 == True or nor1in2 == True:
        image MC14tile05_07 = "r_t_down.png"
        image MC14tile05_08 = "r_horizontal.png"
        image MC14tile05_09 = "r_elbow_bl.png"
        show MC14tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
        show MC14tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show MC14tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC14tile06_07 = "r_vertical.png"
        image MC14tile06_09 = "r_y.png"
        show MC14tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show MC14tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        image MC14tile07_07 = "r_r.png"
        show MC14tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        
    if and1in2 == False and nor1in2 == False:
        hide MC14tile05_07
        hide MC14tile05_08
        hide MC14tile05_09
        hide MC14tile06_07
        hide MC14tile06_09
        hide MC14tile07_07
        
    if nand1in2 == True:
        image MC15tile05_07 = "g_t_down.png"
        image MC15tile05_08 = "g_horizontal.png"
        image MC15tile05_09 = "g_elbow_bl.png"
        show MC15tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
        show MC15tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show MC15tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image MC15tile06_07 = "g_vertical.png"
        image MC15tile06_09 = "g_y.png"
        show MC15tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show MC15tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        image MC15tile07_07 = "g_r.png"
        show MC15tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        
    if nand1in2 == False:
        hide MC15tile05_07
        hide MC15tile05_08
        hide MC15tile05_09
        hide MC15tile06_07
        hide MC15tile06_09
        hide MC15tile07_07
        
    if and1in3 == True:
        if nor1in2 == True:
            image MC16tile06_09 = "r_r.png"
            show MC16tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            image MC16tile07_09 = "r_elbow_tl.png"
            show MC16tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
            
            image MC16tile03_11 = "y_r.png"
            show MC16tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MC16tile04_11 = "r_vertical.png"
            show MC16tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MC16tile05_11 = "r_vertical.png"
            show MC16tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MC16tile06_11 = "r_elbow_tl.png"
            show MC16tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
                


    if and1in3 == False or nor1in2 == False:
        hide MC16tile06_09
        hide MC16tile07_09
        hide MC16tile04_11
        hide MC16tile03_11
        hide MC16tile05_11
        hide MC16tile06_11
        
    if and1in3 == True:
        if nand1in2 == True:
            image MC17tile06_09 = "g_r.png"
            show MC17tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            image MC17tile07_09 = "r_elbow_tl.png"
            show MC17tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        
            image MC17tile03_11 = "y_g.png"
            show MC17tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MC17tile04_11 = "g_vertical.png"
            show MC17tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MC17tile05_11 = "g_vertical.png"
            show MC17tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MC17tile06_11 = "g_elbow_tl.png"
            show MC17tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
            
    if and1in3 == False or nand1in2 == False:
        hide MC17tile06_09
        hide MC17tile07_09
        hide MC17tile03_11
        hide MC17tile04_11
        hide MC17tile05_11
        hide MC17tile06_11
        
    if nand1in3 == True:
        if nor1in2 == True:
            image MC18tile06_09 = "r_g.png"
            show MC18tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            image MC18tile07_09 = "g_elbow_tl.png"
            show MC18tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        
            image MC18tile03_11 = "y_g.png"
            show MC18tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MC18tile04_11 = "g_vertical.png"
            show MC18tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MC18tile05_11 = "g_vertical.png"
            show MC18tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MC18tile06_11 = "g_elbow_tl.png"
            show MC18tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
            
    if nand1in3 == False or nor1in2 == False:
        hide MC18tile06_09
        hide MC18tile07_09
        hide MC18tile03_11
        hide MC18tile04_11
        hide MC18tile05_11
        hide MC18tile06_11
        
    if nand1in3 == True:
        if and1in2 == True:
            image MC19tile06_09 = "r_g.png"
            show MC19tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            image MC19tile07_09 = "g_elbow_tl.png"
            show MC19tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        
            image MC19tile03_11 = "y_g.png"
            show MC19tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MC19tile04_11 = "g_vertical.png"
            show MC19tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MC19tile05_11 = "g_vertical.png"
            show MC19tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MC19tile06_11 = "g_elbow_tl.png"
            show MC19tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
            
    if nand1in3 == False or and1in2 == False:
        hide MC19tile06_09
        hide MC19tile07_09
        hide MC19tile03_11
        hide MC19tile04_11
        hide MC19tile05_11
        hide MC19tile06_11
        
    if nor1in3 == True:
        if and1in2 == True:
            image MC10tile06_09 = "r_g.png"
            show MC10tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            image MC10tile07_09 = "g_elbow_tl.png"
            show MC10tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
            
            image MC10tile03_11 = "y_g.png"
            show MC10tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MC10tile04_11 = "g_vertical.png"
            show MC10tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MC10tile05_11 = "g_vertical.png"
            show MC10tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MC10tile06_11 = "g_elbow_tl.png"
            show MC10tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
        
    if nor1in3 == False or and1in2 == False:
        hide MC10tile06_09
        hide MC10tile07_09
        hide MC10tile03_11
        hide MC10tile04_11
        hide MC10tile05_11
        hide MC10tile06_11
        
    if nor1in3 == True:
        if nand1in2 == True:
            image MC112tile06_09 = "g_r.png"
            show MC112tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            image MC112tile07_09 = "r_elbow_tl.png"
            show MC112tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        
            image MC112tile03_11 = "y_g.png"
            show MC112tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MC112tile04_11 = "g_vertical.png"
            show MC112tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MC112tile05_11 = "g_vertical.png"
            show MC112tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MC112tile06_11 = "g_elbow_tl.png"
            show MC112tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
            
    if nor1in3 == False or nand1in2 == False:
        hide MC112tile06_09
        hide MC112tile07_09
        hide MC112tile03_11
        hide MC112tile04_11
        hide MC112tile05_11
        hide MC112tile06_11
        

    if nand1in1 == True and and1in3 == True and nor1in2 == True:
        image MC1119tile03_11 = "g_r.png"
        image MC1119tile03_13 = "r_horizontal.png"
        show MC1119tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show MC1119tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide MC1119tile03_11
        hide MC1119tile03_13

        
    if (and1in1 == True and ((nor1in2 == True and nand1in3 == True) or (nand1in2 == True and nor1in3 == True))) or (nor1in1 == True and ((and1in2 == True and nand1in3) or (nand1in2 ==True and and1in3 == True))): 
        image MC1112tile03_11 = "r_g.png"
        image MC1112tile03_13 = "r_horizontal.png"
        show MC1112tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show MC1112tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide MC1112tile03_11
        hide MC1112tile03_13
        
        
        
  #win conditions ********      
    if nand1in1 == True and nor1in3 == True and and1in2 == True:
        image MC999tile03_11 = "g_g.png"
        image MC999tile03_13 = "g_horizontal.png"
        show MC999tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show MC999tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image MC1112tile02_09 = "nand_Gate.png"
        show MC1112tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MC1112tile07_02 = "and_Gate.png"
        show MC1112tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MC1112tile07_08 = "nor_Gate.png"
        show MC1112tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MC12end1 = "light_g_on.png"
        show MC12end1 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgMedCWin
        $lgMedC_solved = True
        jump lgMed_done

        
    if attempts == 0:
        image MC111tile02_09 = "nand_Gate.png"
        show MC111tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MC111tile07_02 = "and_Gate.png"
        show MC111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MC111tile07_08 = "nor_Gate.png"
        show MC111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_lgMedCLose
        $lgMed_attempts +=1
        jump lgMed_loseC
    
    jump gamefileMC1

screen logicGatesMC1:
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
        action Jump("hints_lgMedC1")
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