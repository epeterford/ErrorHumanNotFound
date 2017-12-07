﻿init python:

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

label logicGate_hardA2:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
   
    #row 1 (row has a light)
    image HA2tile01_00 = "r_horizontal.png"
    image HA2tile01_01 = "r_horizontal.png"
    image HA2tile01_02 = "r_horizontal.png"
    image HA2tile01_03 = "r_horizontal.png"
    image HA2tile01_04 = "r_horizontal.png"
    image HA2tile01_05 = "r_elbow_bl.png"
    image HA2tile01_12 = "y_elbow_br.png"
    image HA2tile01_13 = "y_horizontal.png"
    
    show HA2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
    show HA2tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image HA2tile02_05 = "r_g.png"
    image HA2tile02_06 = "NONE_Gate.png"
    image HA2tile02_07 = "y_horizontal.png"
    image HA2tile02_08 = "y_elbow_bl.png"
    image HA2tile02_12 = "y_vertical.png"
    
    show HA2tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show HA2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show HA2tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show HA2tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show HA2tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HA2tile03_00 = "g_horizontal.png"
    image HA2tile03_01 = "g_horizontal.png"
    image HA2tile03_02 = "g_horizontal.png"
    image HA2tile03_03 = "g_horizontal.png"
    image HA2tile03_04 = "g_t_down.png"
    image HA2tile03_05 = "g_elbow_tl.png"
    image HA2tile03_08 = "y_y.png"
    image HA2tile03_09 = "NOR_Gate_blue.png"
    image HA2tile03_10 = "y_horizontal.png"
    image HA2tile03_11 = "y_horizontal.png"
    image HA2tile03_12 = "y_elbow_tl.png"
    
    show HA2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show HA2tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HA2tile04_04 = "g_y.png"
    image HA2tile04_05 = "NONE_Gate.png"
    image HA2tile04_06 = "y_horizontal.png"
    image HA2tile04_07 = "NOT_Gate_blue.png"
    image HA2tile04_08 = "y_elbow_tl.png"
    
    show HA2tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HA2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show HA2tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HA2tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show HA2tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HA2tile05_00 = "g_horizontal.png"
    image HA2tile05_01 = "g_elbow_bl.png"
    image HA2tile05_03 = "y_elbow_br.png"
    image HA2tile05_04 = "y_elbow_tl.png"
    
    show HA2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HA2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HA2tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show HA2tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image HA2tile06_01 = "g_g.png"
    image HA2tile06_02 = "NONE_Gate.png"
    image HA2tile06_03 = "y_elbow_tl.png"
    
    show HA2tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show HA2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show HA2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HA2tile07_00 = "g_horizontal.png"
    image HA2tile07_01 = "g_elbow_tl.png"
    
    show HA2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HA2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    

    #start points
    image HA299start1 = "light_r_on.png"
    show HA299start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HA299start2 = "light_g_on.png"
    show HA299start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HA299start3 = "light_g_on.png"
    show HA299start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HA299start4 = "light_g_on.png"
    show HA299start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image H299end1 = "light_g_off.png"
    show H299end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
  
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""

    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ or1x = 848
    $ or1y = 88
    $ xor1x = 1299
    $ xor1y = 88
    
    #gate values
    $ gate1x = 886
    $ gate1y = 383
    $ gate2x = 586
    $ gate2y = 683
    $ gate3x = 811
    $ gate3y = 533    

    # check conditons for locations
    $ and1in1 = False
    $ or1in1 = False
    $ xor1in1 = False
    $ and1in2 = False
    $ or1in2 = False
    $ xor1in2 = False
    $ and1in3 = False
    $ or1in3 = False
    $ xor1in3 = False
    
    #attempts for players
    $ attempts = 5
 
    jump gamefileHA2
    
    
label gamefileHA2:
    
    #calls game screen
    call screen logicGatesHA2
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False
                
            #sets values for checks
            $ and1x = gate1x
            $ and1y = gate1y
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False

            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
            $ and1in3 = False
            
        if slot_name == "gate slot three":
            if or1in3 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False

            #sets values for checks
            $ and1x = gate3x
            $ and1y = gate3y
            $ and1in3 = True
            $ and1in1 = False
            $ and1in2 = False
        
        if slot_name == "and return":
            $ and1x = 698
            $ and1y = 88
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = False
            
     #or gate section **********************************************************************       
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
            if xor1in1 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in1 = False
                
            #sets values for checks
            $ or1x = gate1x
            $ or1y = gate1y
            $ or1in1 = True
            $ or1in2 = False
            $ or1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in2 = False
            if xor1in2 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in2 = False
                
            #sets values for checks
            $ or1x = gate2x
            $ or1y = gate2y
            $ or1in2 = True
            $ or1in1 = False
            $ or1in3 = False
            
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in3 = False
            if xor1in3 == True:
                $ xor1x = 1299
                $ xor1y = 88
                $ xor1in3 = False
                
            #sets values for checks
            $ or1x = gate3x
            $ or1y = gate3y
            $ or1in3 = True
            $ or1in1 = False
            $ or1in2 = False
            
        if slot_name == "or return":
            $ or1x = 848
            $ or1y = 88
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = False
      #xor gate section **********************************************************************       
    if gate_name == "xor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in1 = False
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
                
            #sets values for checks
            $ xor1x = gate1x
            $ xor1y = gate1y
            $ xor1in1 = True
            $ xor1in2 = False
            $ xor1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
                
            #sets values for checks
            $ xor1x = gate2x
            $ xor1y = gate2y
            $ xor1in2 = True
            $ xor1in1 = False
            $ xor1in3 = False
            
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in3 = False
            if or1in3 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in3 = False
                
            #sets values for checks
            $ xor1x = gate3x
            $ xor1y = gate3y
            $ xor1in3 = True
            $ xor1in1 = False
            $ xor1in2 = False
            
        if slot_name == "xor return":
            $ xor1x = 1299
            $ xor1y = 88
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = False
            
    if (temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "and return" or slot_name == "or return" or slot_name == "xor return")):
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
            if slot_name == "or return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "or_gate":
                $ attempts +=1   
            if slot_name == "or return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "xor_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "xor_gate":
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
        image HA21tile02_07 = "r_horizontal.png"
        image HA21tile02_08 = "r_elbow_bl.png"
        show HA21tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show HA21tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        image HA21tile03_08 = "r_y.png"
        show HA21tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    
    if and1in1 == False:
        hide HA21tile02_07
        hide HA21tile02_08
        hide HA21tile03_08
        
    if or1in1 == True:
        image HA22tile02_07 = "g_horizontal.png"
        image HA22tile02_08 = "g_elbow_bl.png"
        show HA22tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show HA22tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        image HA22tile03_08 = "g_y.png"
        show HA22tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        
    if or1in1 == False:
        hide HA22tile02_07
        hide HA22tile02_08
        hide HA22tile03_08
        
    if xor1in1 == True:
        image HA23tile02_07 = "g_horizontal.png"
        image HA23tile02_08 = "g_elbow_bl.png"
        show HA23tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show HA23tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        image HA23tile03_08 = "g_y.png"
        show HA23tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        
    if xor1in1 == False:
        hide HA23tile02_07
        hide HA23tile02_08
        hide HA23tile03_08
    
    if and1in2 == True:
        image HA24tile05_03 = "g_elbow_br.png"
        image HA24tile05_04 = "g_elbow_tl.png"
    
        show HA24tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show HA24tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    
        image HA24tile06_03 = "g_elbow_tl.png"
        show HA24tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        image HA24tile04_04 = "g_g.png"
        show HA24tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        if or1in3 == True:
            image HA27tile04_06 = "g_horizontal.png"
            image HA27tile04_08 = "r_elbow_tl.png"
        
            show HA27tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HA27tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            image HA27tile03_08 = "y_r.png"
            show HA27tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HA27tile04_06
            hide HA27tile04_08
            hide HA27tile03_08
            
        if xor1in3 == True:
            image HA28tile04_06 = "r_horizontal.png"
            image HA28tile04_08 = "g_elbow_tl.png"
        
            show HA28tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HA28tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            image HA28tile03_08 = "y_g.png"
            show HA28tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HA28tile04_06
            hide HA28tile04_08
            hide HA28tile03_08
        
    else:
        hide HA24tile05_03
        hide HA24tile05_04
        hide HA24tile06_03
        hide HA24tile04_04
        hide HA27tile04_06
        hide HA27tile04_08
        hide HA27tile03_08
        hide HA28tile04_06
        hide HA28tile04_08
        hide HA28tile03_08
        
    if or1in2 == True:
        image HA25tile05_03 = "g_elbow_br.png"
        image HA25tile05_04 = "g_elbow_tl.png"
    
        show HA25tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show HA25tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    
        image HA25tile06_03 = "g_elbow_tl.png"
        show HA25tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        image HA25tile04_04 = "g_g.png"
        show HA25tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        if and1in3 == True:
            image HA29tile04_06 = "g_horizontal.png"
            image HA29tile04_08 = "r_elbow_tl.png"
        
            show HA29tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HA29tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            image HA29tile03_08 = "y_r.png"
            show HA29tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HA29tile04_06
            hide HA29tile04_08
            hide HA29tile03_08
        if xor1in3 == True:
            image HA20tile04_06 = "r_horizontal.png"
            image HA20tile04_08 = "g_elbow_tl.png"
        
            show HA20tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HA20tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            image HA20tile03_08 = "y_g.png"
            show HA20tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HA20tile04_06
            hide HA20tile04_08
            hide HA20tile03_08
        
    else:
        hide HA25tile05_03
        hide HA25tile05_04
        hide HA25tile06_03
        hide HA25tile04_04
        hide HA29tile04_06
        hide HA29tile04_08
        hide HA29tile03_08
        hide HA20tile04_06
        hide HA20tile04_08
        hide HA20tile03_08
        
    if xor1in2 == True:
        image HA26tile05_03 = "r_elbow_br.png"
        image HA26tile05_04 = "r_elbow_tl.png"
    
        show HA26tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show HA26tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    
        image HA26tile06_03 = "r_elbow_tl.png"
        show HA26tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        image HA26tile04_04 = "g_r.png"
        show HA26tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        if and1in3 == True:
            image HA211tile04_06 = "r_horizontal.png"
            image HA211tile04_08 = "g_elbow_tl.png"
        
            show HA211tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HA211tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            image HA211tile03_08 = "y_g.png"
            show HA211tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HA211tile04_06
            hide HA211tile04_08
            hide HA211tile03_08
        if or1in3 == True:
            image HA212tile04_06 = "g_horizontal.png"
            image HA212tile04_08 = "r_elbow_tl.png"
        
            show HA212tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HA212tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            image HA212tile03_08 = "y_r.png"
            show HA212tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HA212tile04_06
            hide HA212tile04_08
            hide HA212tile03_08
        
    else:
        hide HA26tile05_03
        hide HA26tile05_04
        hide HA26tile06_03
        hide HA26tile04_04
        hide HA211tile04_06
        hide HA211tile04_08
        hide HA211tile03_08  
        hide HA212tile04_06
        hide HA212tile04_08
        hide HA212tile03_08
        
    # not winning
    if (and1in3 and or1in1 and xor1in2) or (and1in2 and or1in1 and xor1in3):
        image HA213tile01_12 = "r_elbow_br.png"
        image HA213tile01_13 = "r_horizontal.png"
        show HA213tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
        show HA213tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        image HA213tile02_12 = "r_vertical.png"
        show HA213tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)
        image HA213tile03_08 = "g_g.png"
        image HA213tile03_10 = "r_horizontal.png"
        image HA213tile03_11 = "r_horizontal.png"
        image HA213tile03_12 = "r_elbow_tl.png"
        show HA213tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HA213tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show HA213tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show HA213tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HA213tile01_12
        hide HA213tile01_13
        hide HA213tile02_12
        hide HA213tile03_08
        hide HA213tile03_10
        hide HA213tile03_11
        hide HA213tile03_12
    
    if (and1in1 and or1in2 and xor1in3):
        image HA214tile01_12 = "r_elbow_br.png"
        image HA214tile01_13 = "r_horizontal.png"
        show HA214tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
        show HA214tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        image HA214tile02_12 = "r_vertical.png"
        show HA214tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)
        image HA214tile03_08 = "r_r.png"
        image HA214tile03_10 = "r_horizontal.png"
        image HA214tile03_11 = "r_horizontal.png"
        image HA214tile03_12 = "r_elbow_tl.png"
        show HA214tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)  
    else:
        hide HA214tile03_08
        
    if (and1in2 and or1in3 and xor1in1) or (xor1in1 and or1in2 and and1in3):
        show HA214tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
        show HA214tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        show HA214tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)
        image HA214tile03_08S = "g_r.png"
        show HA214tile03_08S at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HA214tile03_08S
        
    if (and1in1 and or1in2 and xor1in3):
        show HA214tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
        show HA214tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        show HA214tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)
        image HA214tile03_08Sx = "r_g.png"
        show HA214tile03_08Sx at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show HA214tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HA214tile03_08Sx
        
    if not((and1in2 and or1in3 and xor1in1) or (and1in1 and or1in2 and xor1in3) or (and1in1 and or1in2 and xor1in3) or (xor1in1 and or1in2 and and1in3)):
        hide HA214tile01_12
        hide HA214tile01_13
        hide HA214tile02_12
        hide HA214tile03_10
        hide HA214tile03_11
        hide HA214tile03_12 
        
    #winning
    if (and1in1 and xor1in2 and or1in3):
        image HA215tile01_12 = "g_elbow_br.png"
        image HA215tile01_13 = "g_horizontal.png"
        show HA215tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
        show HA215tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        image HA215tile02_12 = "g_vertical.png"
        show HA215tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)
        image HA215tile03_08 = "r_r.png"
        image HA215tile03_10 = "g_horizontal.png"
        image HA215tile03_11 = "g_horizontal.png"
        image HA215tile03_12 = "g_elbow_tl.png"
        show HA215tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show HA215tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show HA215tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        show HA215tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        image HA215tile07_02 = "and_Gate.png"
        show HA215tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HA215tile07_09 = "or_Gate.png"
        show HA215tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HA215tile07_08 = "xor_Gate.png"
        show HA215tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HA215end = "light_g_on.png"
        show HA215end at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardAWin
        $lgHardA_solved = True
        jump lgHard_win

        
    if attempts == 0:
        image HA216tile07_02 = "and_Gate.png"
        show HA216tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HA216tile07_09 = "or_Gate.png"
        show HA216tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HA216tile07_08 = "xor_Gate.png"
        show HA216tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_lgHardALose
        $lgHard_attempts +=1
        jump lgHard_lose
    
    jump gamefileHA2

screen logicGatesHA2:
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
        action Jump("hints_lgHardA2")
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
                drag_name "or_gate"
                child "or_Gate.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y

            #xor gates
            drag:
                drag_name "xor_gate"
                child "xor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos xor1x ypos xor1y

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
                drag_name "or return"
                child "cover.png"
                draggable False
                xpos 848 ypos 88
            
            drag:
                drag_name "xor return"
                child "cover.png"
                draggable False
                xpos 1299 ypos 88