

label logicGate_easyC1:
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
    image EC1tile01_00 = "r_horizontal.png"
    image EC1tile01_01 = "r_horizontal.png"
    image EC1tile01_02 = "r_elbow_bl.png"
    image EC1tile01_04 = "r_elbow_br.png"
    image EC1tile01_05 = "r_horizontal.png"
    image EC1tile01_06 = "r_horizontal.png"
    image EC1tile01_07 = "r_elbow_bl.png"

    
    show EC1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show EC1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show EC1tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show EC1tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show EC1tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show EC1tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show EC1tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image EC1tile02_02 = "r_g.png"
    image EC1tile02_03 = "AND_Gate.png"
    image EC1tile02_04 = "r_elbow_tl.png"
    image EC1tile02_07 = "r_elbow_tr.png"
    image EC1tile02_08 = "r_horizontal.png"
    image EC1tile02_09 = "NONE_Gate.png"
    image EC1tile02_10 = "y_elbow_bl.png"
    
    show EC1tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show EC1tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show EC1tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show EC1tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show EC1tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show EC1tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show EC1tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image EC1tile03_00 = "g_horizontal.png"
    image EC1tile03_01 = "g_t_down.png"
    image EC1tile03_02 = "g_elbow_tl.png"
    image EC1tile03_04 = "g_elbow_br.png"
    image EC1tile03_05 = "NOT_Gate.png"
    image EC1tile03_06 = "r_horizontal.png"
    image EC1tile03_07 = "r_elbow_bl.png"
    image EC1tile03_10 = "y_vertical.png"
    image EC1tile03_13 = "y_elbow_br.png"
    
    show EC1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show EC1tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image EC1tile04_01 = "g_elbow_tr.png"
    image EC1tile04_02 = "g_horizontal.png"
    image EC1tile04_03 = "g_horizontal.png"
    image EC1tile04_04 = "g_elbow_tl.png"
    image EC1tile04_07 = "r_vertical.png"
    image EC1tile04_10 = "y_y.png"
    image EC1tile04_11 = "AND_Gate.png"
    image EC1tile04_12 = "y_horizontal.png"
    image EC1tile04_13 = "y_elbow_tl.png"
    
    show EC1tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    show EC1tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image EC1tile05_00 = "g_horizontal.png"
    image EC1tile05_01 = "g_elbow_bl.png"
    image EC1tile05_07 = "r_vertical.png"
    image EC1tile05_10 = "y_vertical.png"
    
    show EC1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show EC1tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show EC1tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show EC1tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image EC1tile06_01 = "g_vertical.png"
    image EC1tile06_07 = "r_vertical.png"
    image EC1tile06_10 = "y_vertical.png"
    
    show EC1tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show EC1tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show EC1tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image EC1tile07_00 = "g_elbow_bl.png"
    image EC1tile07_01 = "g_g.png"
    image EC1tile07_02 = "NONE_Gate.png"
    image EC1tile07_03 = "y_horizontal.png"
    image EC1tile07_04 = "y_elbow_bl.png"
    image EC1tile07_07 = "r_y.png"
    image EC1tile07_08 = "NONE_Gate.png"
    image EC1tile07_09 = "y_horizontal.png"
    image EC1tile07_10 = "y_elbow_tl.png"
    
    show EC1tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show EC1tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image EC1tile08_00 = "g_elbow_tr.png"
    image EC1tile08_01 = "g_elbow_tl.png"
    image EC1tile08_04 = "y_elbow_tr.png"
    image EC1tile08_05 = "y_horizontal.png"
    image EC1tile08_06 = "y_horizontal.png"
    image EC1tile08_07 = "y_elbow_tl.png"
    
    show EC1tile08_00 at Position(xpos = 436, xanchor = 0, ypos = 833, yanchor = 0)
    show EC1tile08_01 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show EC1tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show EC1tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show EC1tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show EC1tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)

    #start points
    image EC1start1 = "light_r_on.png"
    show EC1start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image EC1start2 = "light_g_on.png"
    show EC1start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image EC1start3 = "light_g_on.png"
    show EC1start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image EC1start4 = "light_g_on.png"
    show EC1start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image EC1end2 = "light_g_off.png"
    show EC1end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
    
    
    
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
 
    jump gamefileC1
    
    
label gamefileC1:
    
    #calls game screen
    call screen logicgatesC1
    
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
            $ and1x = 1111
            $ and1y = 383
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
            $ and1x = 586
            $ and1y = 758
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
            $ and1x = 1036
            $ and1y = 758
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = True
            
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
            $ or1x = 1111
            $ or1y = 383
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
            $ or1x = 586
            $ or1y = 758
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
            $ or1x = 1036
            $ or1y = 758
            $ or1in2 = False
            $ or1in1 = False
            $ or1in3 = True
            
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
            $ not1x = 1111
            $ not1y = 383
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
            $ not1x = 586
            $ not1y = 758
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
            $ not1x = 1036
            $ not1y = 758
            $ not1in2 = False
            $ not1in1 = False
            $ not1in3 = True


#*******************************************
#************image zone********************* 
#*******************************************

    if not1in1 == True:
        play sound pipeFlowG
        image EC12tile02_10 = "g_elbow_bl.png"
        image EC12tile03_10 = "g_vertical.png"
        image EC12tile04_10 = "g_y.png"
        
        show EC12tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        show EC12tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show EC12tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
        
    if not1in1 == False:
        #play sound pipeFlowN
        hide EC12tile04_10
        hide EC12tile03_10
        hide EC12tile02_10
    
    if and1in2 == True:
        play sound pipeFlowG
        image EC13tile07_03 = "g_horizontal.png"
        image EC13tile07_04 = "g_elbow_bl.png"
        image EC13tile07_07 = "r_g.png"
        image EC13tile08_04 = "g_elbow_tr.png"
        image EC13tile08_05 = "g_horizontal.png"
        image EC13tile08_06 = "g_horizontal.png"
        image EC13tile08_07 = "g_elbow_tl.png"
        
        show EC13tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        show EC13tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
        show EC13tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show EC13tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show EC13tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        show EC13tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show EC13tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
   
    if and1in2 == False:
        #play sound pipeFlowN
        hide EC13tile07_03
        hide EC13tile07_04
        hide EC13tile07_07
        hide EC13tile08_04
        hide EC13tile08_05
        hide EC13tile08_06
        hide EC13tile08_07

    if or1in2 == True:
        play sound pipeFlowG
        image EC14tile07_03 = "g_horizontal.png"
        image EC14tile07_04 = "g_elbow_bl.png"
        image EC14tile07_07 = "r_g.png"
        image EC14tile08_04 = "g_elbow_tr.png"
        image EC14tile08_05 = "g_horizontal.png"
        image EC14tile08_06 = "g_horizontal.png"
        image EC14tile08_07 = "g_elbow_tl.png"
        
        show EC14tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
        show EC14tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
        show EC14tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show EC14tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
        show EC14tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
        show EC14tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
        show EC14tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
   
    if or1in2 == False:
        #play sound pipeFlowN
        hide EC14tile07_03
        hide EC14tile07_04
        hide EC14tile07_07
        hide EC14tile08_04
        hide EC14tile08_05
        hide EC14tile08_06
        hide EC14tile08_07

    if and1in3 == True:
        if or1in2 == True:
            play sound pipeFlowR
            image EC15tile07_09 = "r_horizontal.png"
            image EC15tile07_10 = "r_elbow_tl.png"
            image EC15tile04_10 = "y_r.png"
            image EC15tile05_10 = "r_vertical.png"
            image EC15tile06_10 = "r_vertical.png"
            
            show EC15tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            show EC15tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            show EC15tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
            show EC15tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show EC15tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0) 
    
    if and1in3 == False or or1in2 == False:
       # play sound pipeFlowN
        hide EC15tile04_10
        hide EC15tile06_10
        hide EC15tile07_09
        hide EC15tile07_10
        hide EC15tile05_10


    if or1in3 == True:
        if and1in2 == True:
            play sound pipeFlowG
            image EC16tile07_09 = "g_horizontal.png"
            image EC16tile07_10 = "g_elbow_tl.png"
            image EC16tile04_10 = "y_g.png"
            image EC16tile05_10 = "g_vertical.png" 
            image EC16tile06_10 = "g_vertical.png"
            
            show EC16tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
            show EC16tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
            show EC16tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
            show EC16tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
            show EC16tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    
    if or1in3 == False or and1in2 == False:
        #play sound pipeFlowN
        hide EC16tile06_10
        hide EC16tile07_09
        hide EC16tile05_10
        hide EC16tile07_10
        hide EC16tile04_10

    if and1in3 == True and or1in2 == True and not1in1 == True:
        play sound pipeFlowR
        image EC16tile03_13 = "r_elbow_br.png"
        image EC16tile04_12 = "r_horizontal.png"
        image EC16tile04_13 = "r_elbow_tl.png"
        image EC17tile04_10 = "g_r.png"
        
        show EC17tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        show EC16tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        show EC16tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        show EC16tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        
    if and1in3 == False or or1in2 == False or not1in1 == False:
        #play sound pipeFlowN
        hide EC17tile04_10
        hide EC16tile04_12
        hide EC16tile04_13
        hide EC16tile03_13
        
    if (temp_slot == "" and temp_gate == "" and slot_name != "null"):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
      
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
        
#win conditions ********
    if and1in2 == True and or1in3 == True and not1in1 == True: 
        image EC11tile02_09 = "not_Gate.png"
        show EC11tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image EC11tile07_02 = "and_Gate.png"
        show EC11tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EC11tile07_08 = "or_Gate.png"
        show EC11tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image EC11tile03_13 = "g_elbow_br.png"
        show EC11tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image EC11tile04_12 = "g_horizontal.png"
        image EC11tile04_13 = "g_elbow_tl.png"
        show EC11tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        show EC11tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
        image EC11tile04_10 = "g_g.png"
        show EC11tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        image EC18end2 = "light_g_on.png"
        show EC18end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ solved_LG_easy = True
        $ hiroseOfficeComputer = True
        $ hiroseOfficeItems += 1
        #make to jump back to the game
        jump lgEasyDone


    if attempts == 0:
        image EC111tile02_09 = "not_Gate.png"
        show EC111tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image EC111tile07_02 = "and_Gate.png"
        show EC111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EC111tile07_08 = "or_Gate.png"
        show EC111tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        play sound lgLose
        $renpy.pause(1.5)
        $ lgEasy_tries +=1
        jump repeatLGEasy
    
    jump gamefileC1

screen logicgatesC1:
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
        action Jump("LGEasyHintsC1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty.png"
        xpos 1515
        ypos 890
    text "Attempts" xpos 1530 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    text ": " xpos 1720 ypos 895 color "#0060db" font "Bitter-Bold.otf" size 42
    text "[attempts]" xpos 1735 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    
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
                xpos 1111 ypos 383
           
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos 586 ypos 758
                
            drag:
                drag_name "gate slot three"
                child "cover.png"
                draggable False
                xpos 1036 ypos 758