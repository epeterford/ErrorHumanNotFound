

label logicGate_easyC2: 
    $config.skipping=None
    $renpy.block_rollback()

    $quick_menu = False
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
    #row 1 (row has a light)
    image EC2tile01_00 = "r_horizontal.png"
    image EC2tile01_01 = "r_horizontal.png"
    image EC2tile01_02 = "r_elbow_bl.png"
    
    show EC2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show EC2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show EC2tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image EC2tile02_02 = "r_g.png"
    image EC2tile02_03 = "OR_Gate_blue.png"
    image EC2tile02_04 = "g_horizontal.png"
    image EC2tile02_05 = "g_elbow_bl.png"
    
    show EC2tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show EC2tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show EC2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show EC2tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image EC2tile03_00 = "r_elbow_bl.png"
    image EC2tile03_01 = "g_elbow_br.png"
    image EC2tile03_02 = "g_elbow_tl.png"
    image EC2tile03_05 = "g_vertical.png"
    
    show EC2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show EC2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show EC2tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show EC2tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image EC2tile04_00 = "r_elbow_tr.png"
    image EC2tile04_01 = "g_jump_r.png"
    image EC2tile04_02 = "r_horizontal.png"
    image EC2tile04_03 = "NONE_Gate.png"
    image EC2tile04_04 = "y_elbow_bl.png"
    image EC2tile04_05 = "g_y.png"
    image EC2tile04_06 = "NONE_Gate.png"
    image EC2tile04_07 = "y_horizontal.png"
    image EC2tile04_08 = "y_elbow_bl.png"
    
    show EC2tile04_00 at Position(xpos = 436, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show EC2tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image EC2tile05_00 = "g_horizontal.png"
    image EC2tile05_01 = "g_t_up.png"
    image EC2tile05_02 = "g_elbow_bl.png"
    image EC2tile05_04 = "y_elbow_tr.png"
    image EC2tile05_05 = "y_elbow_tl.png"
    image EC2tile05_08 = "y_vertical.png"
    image EC2tile05_10 = "y_elbow_br.png"
    image EC2tile05_11 = "NOT_Gate_blue.png"
    image EC2tile05_12 = "y_horizontal.png"
    image EC2tile05_13 = "y_horizontal.png"
    
    show EC2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show EC2tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image EC2tile06_02 = "g_g.png"
    image EC2tile06_03 = "AND_Gate_blue.png"
    image EC2tile06_04 = "g_elbow_bl.png"
    image EC2tile06_08 = "y_vertical.png"
    image EC2tile06_10 = "y_vertical.png"
    
    show EC2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show EC2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show EC2tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show EC2tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show EC2tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image EC2tile07_00 = "g_horizontal.png"
    image EC2tile07_01 = "g_horizontal.png"
    image EC2tile07_02 = "g_elbow_tl.png"
    image EC2tile07_04 = "g_vertical.png"
    image EC2tile07_08 = "y_g.png"
    image EC2tile07_09 = "NONE_Gate.png"
    image EC2tile07_10 = "y_elbow_tl.png"
    
    show EC2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show EC2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show EC2tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show EC2tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show EC2tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show EC2tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show EC2tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image EC2tile08_04 = "g_elbow_tr.png"
    image EC2tile08_05 = "g_horizontal.png"
    image EC2tile08_06 = "g_horizontal.png"
    image EC2tile08_07 = "g_horizontal.png"
    image EC2tile08_08 = "g_elbow_tl.png"

    show EC2tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show EC2tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show EC2tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show EC2tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show EC2tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)

    #start points
    image EC2start1 = "light_r_on.png"
    show EC2start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image EC2start2 = "light_r_on.png"
    show EC2start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image EC2start3 = "light_g_on.png"
    show EC2start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image EC2start4 = "light_g_on.png"
    show EC2start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image EC2end2 = "light_r_off.png"
    show EC2end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ or1x = 848
    $ or1y = 88
    $ not1x = 548
    $ not1y = 88
    
    #gate x and y positions
    $ gate1x = 661
    $ gate1y = 533
    $ gate2x = 886
    $ gate2y = 533
    $ gate3x = 1111
    $ gate3y = 758
   
    # check conditons for locations
    $ and1in1 = False
    $ or1in1 = False
    $ not1in1 = False
    $ and1in2 = False
    $ or1in2 = False
    $ not1in2 = False
    $ and1in3 = False
    $ or1in3 = False
    $ not1in3 = False
     
    #attempts for players
    $ attempts = 4
 
    jump gamefileC2
    
    
label gamefileC2:
    
    #calls game screen
    call screen logicGateC2
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
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
            if not1in2 == True:
                $ not1x = 548
                $ not1y = 88
                $ not1in2 = False
            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
            $ and1in3 = False
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
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
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
            if and1in2 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in2 = False
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
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
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
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
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
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
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
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
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
    if not1in1 == True:
        image EC22tile04_04 = "g_elbow_bl.png"
        image EC22tile04_05 = "g_g.png"
        image EC22tile05_04 = "g_elbow_tr.png"
        image EC22tile05_05 = "g_elbow_tl.png"
        
        show EC22tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        show EC22tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show EC22tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show EC22tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    if not1in1 == False:
        hide EC22tile05_04
        hide EC22tile05_05
        hide EC22tile04_04
        hide EC22tile04_05
        
    if and1in2:
        if not1in1:
            image EC23tile04_07 = "g_horizontal.png"
            image EC23tile04_08 = "g_elbow_bl.png"
            image EC23tile07_08 = "g_g.png"
            image EC23tile06_08 = "g_vertical.png"
            image EC23tile05_08 = "g_vertical.png"
            
            show EC23tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show EC23tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show EC23tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)    
            show EC23tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show EC23tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)

    if and1in2 == False:
        hide EC23tile04_07
        hide EC23tile04_08
        hide EC23tile07_08
        hide EC23tile06_08
        hide EC23tile05_08
        
    if or1in2:
        if not1in1:
            image EC24tile04_07 = "g_horizontal.png"
            image EC24tile04_08 = "g_elbow_bl.png"
            image EC24tile07_08 = "g_g.png"
            image EC24tile06_08 = "g_vertical.png"
            image EC24tile05_08 = "g_vertical.png"
            
            show EC24tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
            show EC24tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
            show EC24tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
            show EC24tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show EC24tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            
    if or1in2 == False:
        hide EC24tile04_07
        hide EC24tile04_08
        hide EC24tile07_08
        hide EC24tile06_08
        hide EC24tile05_08       
        
    if and1in3 == True:
        if or1in2 == True:
            if not1in1 == True:
                image EC25tile07_10 = "g_elbow_tl.png"
                show EC25tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)

                image EC25tile06_10 = "g_vertical.png"
                show EC25tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)

                image EC25tile05_10 = "g_elbow_br.png"
                image EC25tile05_12 = "r_horizontal.png"
                image EC25tile05_13 = "r_horizontal.png"
                show EC25tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                show EC25tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
                show EC25tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)

                image EC25tile04_07 = "g_horizontal.png"
                image EC25tile04_08 = "g_elbow_bl.png"
                show EC25tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
                show EC25tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)

    
    if or1in2 == False or and1in3 == False:
        hide EC25tile04_08
        hide EC25tile04_07
        hide EC25tile05_13
        hide EC25tile05_12
        hide EC25tile05_10
        hide EC25tile06_10
        hide EC25tile07_10
        
    if or1in3:
        if and1in2:
            if not1in1:
                image EC26tile07_10 = "g_elbow_tl.png"
                show EC26tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)

                image EC26tile06_10 = "g_vertical.png"
                show EC26tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)

                image EC26tile05_10 = "g_elbow_br.png"
                image EC26tile05_12 = "r_horizontal.png"
                image EC26tile05_13 = "r_horizontal.png"
                show EC26tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
                show EC26tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
                show EC26tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)

                image EC26tile04_07 = "g_horizontal.png"
                image EC26tile04_08 = "g_elbow_bl.png"
                show EC26tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
                show EC26tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            
            
    if or1in3 == False or and1in2 == False:
        hide EC26tile04_08
        hide EC26tile04_07
        hide EC26tile05_13
        hide EC26tile05_12
        hide EC26tile05_10
        hide EC26tile06_10
        hide EC26tile07_10
        
        
    if (temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name =="and return" or slot_name =="or return" or slot_name=="not return"):
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
            if slot_name == "not return" and gate_name == "not_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "not_gate":
                $ attempts +=1                
            if slot_name == "and return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "not_gate":
                $ attempts +=1
            if slot_name == "not return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "not return" and gate_name == "or_gate":
                $ attempts +=1
                
#win conditions ********
    if (and1in2 == True and or1in3 == True and not1in1 == True) or (and1in3 == True and or1in2 == True and not1in1 == True): 
        image EC21tile02_09 = "not_Gate.png"
        show EC21tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image EC21tile07_02 = "and_Gate.png"
        show EC21tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EC21tile07_08 = "or_Gate.png"
        show EC21tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image EC21end2 = "light_r_on.png"
        show EC21end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgEasyCWin
        $ solved_LG_easy = True
        $ hiroseOfficeComputer = True
        $ hiroseOfficeItems += 1
        #make to jump back to the game
        jump lgEasyDone

    if attempts == 0:
        image EC211tile02_09 = "not_Gate.png"
        show EC211tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image EC211tile07_02 = "and_Gate.png"
        show EC211tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EC211tile07_08 = "or_Gate.png"
        show EC211tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_lgEasyCLose
        $ lgEasy_tries +=1
        jump repeatLGEasy
    
    jump gamefileC2

screen logicGateC2:
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
        action Jump("LGEasyHintsC2")
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
                drag_name "not return"
                child "cover.png"
                draggable False
                xpos 548 ypos 88