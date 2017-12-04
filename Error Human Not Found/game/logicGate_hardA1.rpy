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

label logicGate_hardA1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
   
    #row 1 (row has a light)
    image HA1tile01_00 = "r_horizontal.png"
    image HA1tile01_01 = "NOT_Gate_blue.png"
    image HA1tile01_02 = "g_horizontal.png"
    image HA1tile01_03 = "g_horizontal.png"
    image HA1tile01_04 = "g_horizontal.png"
    image HA1tile01_05 = "g_horizontal.png"
    image HA1tile01_06 = "g_horizontal.png"
    image HA1tile01_07 = "g_horizontal.png"
    image HA1tile01_08 = "g_horizontal.png"
    image HA1tile01_09 = "g_elbow_bl.png"
    
    show HA1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show HA1tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image HA1tile02_09 = "g_vertical.png"
    
    show HA1tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HA1tile03_00 = "g_horizontal.png"
    image HA1tile03_01 = "g_horizontal.png"
    image HA1tile03_02 = "g_elbow_bl.png"
    image HA1tile03_09 = "g_vertical.png"
    image HA1tile03_13 = "y_elbow_br.png"
    
    show HA1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HA1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HA1tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HA1tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show HA1tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HA1tile04_02 = "g_g.png"
    image HA1tile04_03 = "NONE_Gate.png"
    image HA1tile04_04 = "y_horizontal.png"
    image HA1tile04_05 = "y_horizontal.png"
    image HA1tile04_06 = "y_elbow_bl.png"
    image HA1tile04_09 = "g_y.png"
    image HA1tile04_10 = "NONE_Gate.png"
    image HA1tile04_11 = "y_horizontal.png"
    image HA1tile04_12 = "NOT_Gate_blue.png"
    image HA1tile04_13 = "y_elbow_tl.png"
    
    show HA1tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    show HA1tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HA1tile05_00 = "g_horizontal.png"
    image HA1tile05_01 = "g_horizontal.png"
    image HA1tile05_02 = "g_elbow_tl.png"
    image HA1tile05_06 = "y_vertical.png"
    image HA1tile05_09 = "y_vertical.png"
    
    show HA1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HA1tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show HA1tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show HA1tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show HA1tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)

    
    #row 6
    image HA1tile06_06 = "y_r.png"
    image HA1tile06_07 = "NONE_Gate.png"
    image HA1tile06_08 = "y_horizontal.png"
    image HA1tile06_09 = "y_elbow_tl.png"

    show HA1tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show HA1tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show HA1tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show HA1tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)

    
    #row 7 (row has a light)
    image HA1tile07_00 = "r_horizontal.png"
    image HA1tile07_01 = "r_horizontal.png"
    image HA1tile07_02 = "r_horizontal.png"
    image HA1tile07_03 = "r_horizontal.png"
    image HA1tile07_04 = "r_horizontal.png"
    image HA1tile07_05 = "r_horizontal.png"
    image HA1tile07_06 = "r_elbow_tl.png"
    
    show HA1tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show HA1tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show HA1tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show HA1tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show HA1tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show HA1tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show HA1tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)

    


    #start points
    image HA199start1 = "light_r_on.png"
    show HA199start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image HA199start2 = "light_g_on.png"
    show HA199start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image HA199start3 = "light_g_on.png"
    show HA199start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image HA199start4 = "light_r_on.png"
    show HA199start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image HA199end2 = "light_g_off.png"
    show HA199end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)


    
    
    
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
    $ gate1y = 533
    $ gate2x = 961
    $ gate2y = 683
    $ gate3x = 1186
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
 
    jump gamefileHA1
    
    
label gamefileHA1:
    
    #calls game screen
    call screen logicGatesHA1
    
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
        image HA11tile05_06 = "g_vertical.png"
        show HA11tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)

        image HA11tile06_06 = "g_r.png"
        show HA11tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        
        image HA11tile04_04 = "g_horizontal.png"
        image HA11tile04_05 = "g_horizontal.png"
        image HA11tile04_06 = "g_elbow_bl.png"
        show HA11tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show HA11tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show HA11tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        
    if and1in1 == False:
        hide HA11tile05_06
        hide HA11tile06_06
        hide HA11tile04_05
        hide HA11tile04_06
        hide HA11tile04_04
        
        
    if or1in1 == True:
        image HA14tile05_06 = "g_vertical.png"
        show HA14tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)

        image HA14tile06_06 = "g_r.png"
        show HA14tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        
        image HA14tile04_04 = "g_horizontal.png"
        image HA14tile04_05 = "g_horizontal.png"
        image HA14tile04_06 = "g_elbow_bl.png"
        show HA14tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show HA14tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show HA14tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)

        
    if or1in1 == False:
        hide HA14tile05_06
        hide HA14tile06_06
        hide HA14tile04_05
        hide HA14tile04_06
        hide HA14tile04_04

    if xor1in1 == True:
        image HA15tile05_06 = "r_vertical.png"
        show HA15tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)

        image HA15tile06_06 = "r_r.png"
        show HA15tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        
        image HA15tile04_04 = "r_horizontal.png"
        image HA15tile04_05 = "r_horizontal.png"
        image HA15tile04_06 = "r_elbow_bl.png"
        show HA15tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show HA15tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show HA15tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        
    if xor1in1 == False:
        hide HA15tile05_06
        hide HA15tile06_06
        hide HA15tile04_05
        hide HA15tile04_06
        hide HA15tile04_04


    if and1in2 == True:
        if xor1in1 == True:
            image HA12tile06_08 = "r_horizontal.png"
            image HA12tile06_09 = "r_elbow_tl.png"

            show HA12tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show HA12tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            
            image HA12tile05_09 = "r_vertical.png"
            show HA12tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            
            image HA12tile04_09 = "g_r.png"
            show HA12tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            
            if or1in3 == True:
                image HA104tile03_13 = "r_elbow_br.png"
                show HA104tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
                image HA104tile04_11 = "g_horizontal.png"
                image HA104tile04_13 = "r_elbow_tl.png"
                show HA104tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                show HA104tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    if and1in2 == False or xor1in1 == False or or1in3 == False:
        hide HA104tile03_13
        hide HA104tile04_11
        hide HA104tile04_13
     
    if and1in2 == True:
        if or1in1 == True:
            image HA12tile06_08 = "r_horizontal.png"
            image HA12tile06_09 = "r_elbow_tl.png"

            show HA12tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show HA12tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            
            image HA12tile05_09 = "r_vertical.png"
            show HA12tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            
            image HA12tile04_09 = "g_r.png"
            show HA12tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            if xor1in3 == True:
                image HA103tile03_13 = "r_elbow_br.png"
                show HA103tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
                image HA103tile04_11 = "g_horizontal.png"
                image HA103tile04_13 = "r_elbow_tl.png"
                show HA103tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                show HA103tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    if and1in2 == False or xor1in3 == False or or1in1 == False:
        hide HA103tile03_13
        hide HA103tile04_11
        hide HA103tile04_13
   
    if and1in2 == False or (xor1in1 == False and or1in1 == False):
        hide HA12tile06_08
        hide HA12tile06_09
        hide HA12tile05_09
        hide HA12tile04_09
        
    if and1in2 == False or (xor1in1 == False and or1in1 == False):
        hide HA13tile03_13
        hide HA13tile04_11
        hide HA13tile04_13

    if xor1in2 == True:
        if or1in1 == True:
            image HA16tile06_08 = "g_horizontal.png"
            image HA16tile06_09 = "g_elbow_tl.png"

            show HA16tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show HA16tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            
            image HA16tile05_09 = "g_vertical.png"
            show HA16tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            
            image HA16tile04_09 = "g_g.png"
            show HA16tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            if and1in3 == True:
                image HA102tile03_13 = "r_elbow_br.png"
                show HA102tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
                image HA102tile04_11 = "g_horizontal.png"
                image HA102tile04_13 = "r_elbow_tl.png"
                show HA102tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                show HA102tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    if and1in3 == False or xor1in2 == False or or1in1 == False:
        hide HA102tile04_11
        hide HA102tile04_11
        hide HA102tile04_13
            #***************************************************************winner
    if xor1in2 == True:
        if and1in1 == True:
            image HA17tile06_08 = "g_horizontal.png"
            image HA17tile06_09 = "g_elbow_tl.png"

            show HA17tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show HA17tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            
            image HA17tile05_09 = "g_vertical.png"
            show HA17tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            
            image HA17tile04_09 = "g_g.png"
            show HA17tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            if or1in3 == True:
                image HA101tile03_13 = "r_elbow_br.png"
                show HA101tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
                image HA101tile04_11 = "g_horizontal.png"
                image HA101tile04_13 = "r_elbow_tl.png"
                show HA101tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                show HA101tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    if and1in1 == False or xor1in2 == False or or1in3 == False:
        hide HA101tile03_13
        hide HA101tile04_11
        hide HA101tile04_13
   
    if xor1in2 == False or or1in1 == False :
        hide HA16tile06_08
        hide HA16tile06_09
        hide HA16tile05_09
        hide HA16tile04_09
        
    if xor1in2 == False or and1in1 == False :
        hide HA17tile06_08
        hide HA17tile06_09
        hide HA17tile05_09
        hide HA17tile04_09
        #***************************************************************winner
    if or1in2 == True:
        if xor1in1 == True:
            image HA18tile06_08 = "r_horizontal.png"
            image HA18tile06_09 = "r_elbow_tl.png"

            show HA18tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show HA18tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            
            image HA18tile05_09 = "r_vertical.png"
            show HA18tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            
            image HA18tile04_09 = "g_r.png"
            show HA18tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            if and1in3 == True:
                image HA13tile03_13 = "g_elbow_br.png"
                show HA13tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
                image HA13tile04_11 = "r_horizontal.png"
                image HA13tile04_13 = "g_elbow_tl.png"
                show HA13tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                show HA13tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    if and1in1 == False or xor1in2 == False or or1in2 == False:
        hide HA13tile03_13
        hide HA13tile04_11
        hide HA13tile04_13
            #***************************************************************winner
    if or1in2 == True:
        if and1in1 == True:
            image HA19tile06_08 = "g_horizontal.png"
            image HA19tile06_09 = "g_elbow_tl.png"

            show HA19tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show HA19tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
            
            image HA19tile05_09 = "g_vertical.png"
            show HA19tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
            
            image HA19tile04_09 = "g_g.png"
            show HA19tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            
            if xor1in3 == True:
                image HA108tile03_13 = "g_elbow_br.png"
                show HA108tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
                image HA108tile04_11 = "r_horizontal.png"
                image HA108tile04_13 = "g_elbow_tl.png"
                show HA108tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
                show HA108tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    if and1in1 == False or xor1in3 == False or or1in2 == False:
        hide HA108tile03_13
        hide HA108tile04_11
        hide HA108tile04_13
   
    if or1in2 == False or xor1in1 == False :
        hide HA18tile06_08
        hide HA18tile06_09
        hide HA18tile05_09
        hide HA18tile04_09
        
    if or1in2 == False or and1in1 == False :
        hide HA19tile06_08
        hide HA19tile06_09
        hide HA19tile05_09
        hide HA19tile04_09



        
#win conditions ********
    if (and1in1 == True and or1in2 == True and xor1in3 == True) or ( xor1in1 == True and or1in2 == True and and1in3 == True) : 
        image HA199tile07_02 = "and_Gate.png"
        show HA199tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HA199tile07_09 = "or_Gate.png"
        show HA199tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HA199tile07_08 = "xor_Gate.png"
        show HA199tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image HA199end = "light_g_on.png"
        show HA199end at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgHardAWin
        $lgHardA_solved = True
        jump lgHard_win

        
    if attempts == 0:
        image HA199tile07_02 = "and_Gate.png"
        show HA199tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image HA199tile07_09 = "or_Gate.png"
        show HA199tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image HA199tile07_08 = "xor_Gate.png"
        show HA199tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_lgHardALose
        $lgHard_attempts +=1
        jump lgHard_lose
    
    jump gamefileHA1

screen logicGatesHA1:
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
        action Jump("hints_lgHardA1")
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
                