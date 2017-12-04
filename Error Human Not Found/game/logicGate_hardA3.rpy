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
        return 

init:
    image bg Logic_Gate = "LOGIC_GATE_BG.png"

label logicGate_hardA3:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate

    #row 1 (row has a light)
    image HA3tile01_00 = "g_horizontal.png"
    image HA3tile01_01 = "g_horizontal.png"
    image HA3tile01_02 = "g_elbow_bl.png"
    
    show HA3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HA3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show HA3tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image HA3tile02_02 = "g_g.png"
    image HA3tile02_03 = "NONE_Gate.png"
    image HA3tile02_04 = "y_elbow_bl.png"
    
    show HA3tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show HA3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HA3tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HA3tile03_00 = "g_horizontal.png"
    image HA3tile03_01 = "g_horizontal.png"
    image HA3tile03_02 = "g_elbow_tl.png"
    image HA3tile03_04 = "y_elbow_tr.png"
    image HA3tile03_05 = "y_elbow_bl.png"
    
    show HA3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HA3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HA3tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HA3tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show HA3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HA3tile04_05 = "y_g.png"
    image HA3tile04_06 = "XOR_Gate_blue.png"
    image HA3tile04_07 = "y_horizontal.png"
    image HA3tile04_08 = "y_horizontal.png"
    image HA3tile04_09 = "NOT_Gate_blue.png"
    image HA3tile04_10 = "y_elbow_bl.png"
    
    show HA3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show HA3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HA3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show HA3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show HA3tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show HA3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HA3tile05_00 = "r_horizontal.png"
    image HA3tile05_01 = "NOT_Gate_blue.png"
    image HA3tile05_02 = "g_horizontal.png"
    image HA3tile05_03 = "g_horizontal.png"
    image HA3tile05_04 = "g_t_down.png"
    image HA3tile05_05 = "g_elbow_tl.png"
    image HA3tile05_10 = "y_vertical.png"
    
    show HA3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HA3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HA3tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show HA3tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show HA3tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show HA3tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show HA3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image HA3tile06_04 = "g_r.png"
    image HA3tile06_05 = "NONE_Gate.png"
    image HA3tile06_06 = "y_horizontal.png"
    image HA3tile06_07 = "y_elbow_bl.png"
    image HA3tile06_10 = "y_vertical.png"
    
    show HA3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show HA3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show HA3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show HA3tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show HA3tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HA3tile07_00 = "r_horizontal.png"
    image HA3tile07_01 = "r_horizontal.png"
    image HA3tile07_02 = "r_horizontal.png"
    image HA3tile07_03 = "r_horizontal.png"
    image HA3tile07_04 = "r_elbow_tl.png"
    image HA3tile07_07 = "y_vertical.png"
    image HA3tile07_10 = "y_y.png"
    image HA3tile07_11 = "NONE_Gate.png"
    image HA3tile07_12 = "y_horizontal.png"
    image HA3tile07_13 = "y_horizontal.png"
    
    show HA3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
    show HA3tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image HA3tile08_07 = "y_elbow_tr.png"
    image HA3tile08_08 = "y_horizontal.png"
    image HA3tile08_09 = "y_horizontal.png"
    image HA3tile08_10 =  "y_elbow_tl.png"
    
    show HA3tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show HA3tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    show HA3tile08_09 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
    show HA3tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
    

    #start points
    image HA399start1 = "light_g_on.png"
    show HA399start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HA399start2 = "light_g_on.png"
    show HA399start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HA399start3 = "light_r_on.png"
    show HA399start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HA399start4 = "light_r_on.png"
    show HA399start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image HA399end4 = "light_g_off.png"
    show HA399end4 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)

    
    
    
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
    $ xor1x = 1300
    $ xor1y = 88
    
    #gate values
    $ gate1x = 661
    $ gate1y = 383
    $ gate2x = 811
    $ gate2y = 683
    $ gate3x = 1261
    $ gate3y = 758    

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
 
    jump gamefileHA3
    
    
label gamefileHA3:
    
    #calls game screen
    call screen logicGatesHA3
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
            if xor1in1 == True:
                $ xor1x = 1300
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
                $ xor1x = 1300
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
                $ xor1x = 1300
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
                $ xor1x = 1300
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
                $ xor1x = 1300
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
                $ xor1x = 1300
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
            $ xor1x = 1300
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
        image HA31tile02_04 = "g_elbow_bl.png"
        show HA31tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        image HA31tile03_04 = "g_elbow_tr.png"
        image HA31tile03_05 = "g_elbow_bl.png"
        show HA31tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        show HA31tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
        image HA31tile04_05 = "g_g.png"
        show HA31tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        image HA31tile04_07 = "r_horizontal.png"
        image HA31tile04_08 = "r_horizontal.png"
        image HA31tile04_10 = "g_elbow_bl.png"
        show HA31tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show HA31tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show HA31tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image HA31tile05_10 = "g_vertical.png"
        show HA31tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image HA31tile06_10 = "g_vertical.png"
        show HA31tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        image HA31tile07_10 = "g_y.png"
        show HA31tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        
    else:
        hide HA31tile02_04
        hide HA31tile03_04
        hide HA31tile03_05
        hide HA31tile04_05
        hide HA31tile04_07
        hide HA31tile04_08
        hide HA31tile04_10
        hide HA31tile05_10
        hide HA31tile06_10
        hide HA31tile07_10
        
    if xor1in1 == True:
        image HA32tile02_04 = "r_elbow_bl.png"
        show HA32tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        image HA32tile03_04 = "r_elbow_tr.png"
        image HA32tile03_05 = "r_elbow_bl.png"
        show HA32tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        show HA32tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
        image HA32tile04_05 = "r_g.png"
        show HA32tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        image HA32tile04_07 = "g_horizontal.png"
        image HA32tile04_08 = "g_horizontal.png"
        image HA32tile04_10 = "r_elbow_bl.png"
        show HA32tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show HA32tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show HA32tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image HA32tile05_10 = "r_vertical.png"
        show HA32tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image HA32tile06_10 = "r_vertical.png"
        show HA32tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        image HA32tile07_10 = "r_y.png"
        show HA32tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        
    else:
        hide HA32tile02_04
        hide HA32tile03_04
        hide HA32tile03_05
        hide HA32tile04_05
        hide HA32tile04_07
        hide HA32tile04_08
        hide HA32tile04_10
        hide HA32tile05_10
        hide HA32tile06_10
        hide HA32tile07_10
        
    if or1in1 == True:
        image HA33tile02_04 = "g_elbow_bl.png"
        show HA33tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        image HA33tile03_04 = "g_elbow_tr.png"
        image HA33tile03_05 = "g_elbow_bl.png"
        show HA33tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        show HA33tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
        image HA33tile04_05 = "g_g.png"
        show HA33tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        image HA33tile04_07 = "r_horizontal.png"
        image HA33tile04_08 = "r_horizontal.png"
        image HA33tile04_10 = "g_elbow_bl.png"
        show HA33tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
        show HA33tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show HA33tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image HA33tile05_10 = "g_vertical.png"
        show HA33tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        image HA33tile06_10 = "g_vertical.png"
        show HA33tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        image HA33tile07_10 = "g_y.png"
        show HA33tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        
    else:
        hide HA33tile02_04
        hide HA33tile03_04
        hide HA33tile03_05
        hide HA33tile04_05
        hide HA33tile04_07
        hide HA33tile04_08
        hide HA33tile04_10
        hide HA33tile05_10
        hide HA33tile06_10
        hide HA33tile07_10
        
        
    if and1in2 == True:
        image HA34tile06_06 = "r_horizontal.png"
        image HA34tile06_07 = "r_elbow_bl.png"
        show HA34tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show HA34tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image HA34tile07_07 = "r_vertical.png"
        image HA34tile07_10 = "y_r.png"
        show HA34tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show HA34tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        image HA34tile08_07 = "r_elbow_tr.png"
        image HA34tile08_08 = "r_horizontal.png"
        image HA34tile08_09 = "r_horizontal.png"
        image HA34tile08_10 =  "r_elbow_tl.png"
        show HA34tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HA34tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show HA34tile08_09 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
        show HA34tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)

    else:
        hide HA34tile06_06
        hide HA34tile06_07
        hide HA34tile07_07
        hide HA34tile07_10
        hide HA34tile08_07
        hide HA34tile08_08
        hide HA34tile08_09
        hide HA34tile08_10

    if or1in2 == True:
        image HA35tile06_06 = "g_horizontal.png"
        image HA35tile06_07 = "g_elbow_bl.png"
        show HA35tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show HA35tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image HA35tile07_07 = "g_vertical.png"
        image HA35tile07_10 = "y_g.png"
        show HA35tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show HA35tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        image HA35tile08_07 = "g_elbow_tr.png"
        image HA35tile08_08 = "g_horizontal.png"
        image HA35tile08_09 = "g_horizontal.png"
        image HA35tile08_10 =  "g_elbow_tl.png"
        show HA35tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HA35tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show HA35tile08_09 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
        show HA35tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)

    else:
        hide HA35tile06_06
        hide HA35tile06_07
        hide HA35tile07_07
        hide HA35tile07_10
        hide HA35tile08_07
        hide HA35tile08_08
        hide HA35tile08_09
        hide HA35tile08_10
        
    if xor1in2 == True:
        image HA36tile06_06 = "g_horizontal.png"
        image HA36tile06_07 = "g_elbow_bl.png"
        show HA36tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show HA36tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image HA36tile07_07 = "g_vertical.png"
        image HA36tile07_10 = "y_g.png"
        show HA36tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show HA36tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        image HA36tile08_07 = "g_elbow_tr.png"
        image HA36tile08_08 = "g_horizontal.png"
        image HA36tile08_09 = "g_horizontal.png"
        image HA36tile08_10 =  "g_elbow_tl.png"
        show HA36tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show HA36tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show HA36tile08_09 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
        show HA36tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)

    else:
        hide HA36tile06_06
        hide HA36tile06_07
        hide HA36tile07_07
        hide HA36tile07_10
        hide HA36tile08_07
        hide HA36tile08_08
        hide HA36tile08_09
        hide HA36tile08_10
        
     #double green red   
    if (and1in1 == True and or1in2 == True):
        image HA37tile07_10 = "g_g.png"
        show HA37tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0) 
    else:
        hide HA37tile07_12
        hide HA37tile07_13
        hide HA37tile07_10
        
      #double green green
    if (and1in1 == True and xor1in2 == True) or (or1in1 == True and xor1in2 == True):
        image HA310tile07_10 = "g_g.png"
        show HA310tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)  
    else:
        hide HA310tile07_10
        
    #green red Green
    if (and1in2 == True and or1in1 == True):
        image HA30tile07_10 = "g_r.png"
        show HA30tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)  
    else:
        hide HA30tile07_10

    #double red red
    if (and1in2 == True and xor1in1 == True):
        image HA38tile07_10 = "r_r.png"
        show HA38tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0) 
    else:
        hide HA38tile07_10
    
    #red green red
    if (or1in2 == True and xor1in1 == True):
        image HA39tile07_10 = "r_g.png"
        show HA39tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0) 
    else:
        hide HA39tile07_10
        
        
    #red
    if (and1in3 == True and or1in2 == True and xor1in1 == True) or (and1in2 == True and or1in3 == True and xor1in1 == True) or (and1in1 == True and or1in2 == True and xor1in3 == True):
        image HA37tile07_12 = "r_horizontal.png"
        image HA37tile07_13 = "r_horizontal.png"
        show HA37tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
        show HA37tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
    else:
        hide HA37tile07_12
        hide HA37tile07_13
        
#win conditions ********
    if (and1in1 == True and or1in3 == True and xor1in2 == True) or (and1in3 == True and or1in1 == True and xor1in2 == True) or (and1in2 == True and or1in1 == True and xor1in3 == True) : 
        image HA311tile07_12 = "g_horizontal.png"
        image HA311tile07_13 = "g_horizontal.png"
        show HA311tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
        show HA311tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
        image HA399tile07_02 = "and_Gate.png"
        show HA399tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HA399tile07_09 = "or_Gate.png"
        show HA399tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HA399tile07_08 = "xor_Gate.png"
        show HA399tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HA399end = "light_g_on.png"
        show HA399end at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardAWin
        $lgHardA_solved = True
        jump lgHard_win

        
    if attempts == 0:
        image HA399tile07_02 = "and_Gate.png"
        show HA399tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HA399tile07_09 = "or_Gate.png"
        show HA399tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HA399tile07_08 = "xor_Gate.png"
        show HA399tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_lgHardALose
        $lgHard_attempts +=1
        jump lgHard_lose
    
    jump gamefileHA3

screen logicGatesHA3:
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
        action Jump("hints_lgHardA3")
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
                xpos 1300 ypos 88