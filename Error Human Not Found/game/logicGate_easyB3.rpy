
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

label logicGate_easyB3: #logicGate_easyB3
    $config.skipping=None
    $renpy.block_rollback()

    $quick_menu = False
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
    image EB3tile00_00 = "r_elbow_br.png"
    image EB3tile00_01 = "r_horizontal.png"
    image EB3tile00_02= "r_horizontal.png"
    image EB3tile00_03 = "r_elbow_bl.png"
    
    show EB3tile00_00 at Position(xpos = 436, xanchor = 0, ypos = 233, yanchor = 0)
    show EB3tile00_01 at Position(xpos = 511, xanchor = 0, ypos = 233, yanchor = 0)
    show EB3tile00_02 at Position(xpos = 586, xanchor = 0, ypos = 233, yanchor = 0)
    show EB3tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image EB3tile01_00 = "r_elbow_tl.png"
    image EB3tile01_03 = "r_r.png"
    image EB3tile01_04 = "and_gate.png"
    image EB3tile01_05 = "r_horizontal.png"
    image EB3tile01_06 = "r_elbow_bl.png"
    
    show EB3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show EB3tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show EB3tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show EB3tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show EB3tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image EB3tile02_03 = "r_vertical.png"
    image EB3tile02_06 = "r_elbow_tr.png"
    image EB3tile02_07 = "r_horizontal.png"
    image EB3tile02_08 = "r_horizontal.png"
    image EB3tile02_09 = "r_horizontal.png"
    image EB3tile02_10 = "r_elbow_bl.png"
    
    show EB3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show EB3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show EB3tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show EB3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show EB3tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show EB3tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image EB3tile03_03 = "r_vertical.png"
    image EB3tile03_10 = "r_y.png"
    image EB3tile03_11 = "and_gate"
    image EB3tile03_12 = "y_elbow_bl.png"
    
    show EB3tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show EB3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show EB3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show EB3tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)

    #row 4 
    image EB3tile04_01 = "r_elbow_br.png"
    image EB3tile04_02 = "r_horizontal.png"
    image EB3tile04_03 = "r_elbow_tl.png"
    image EB3tile04_04 = "g_elbow_br.png"
    image EB3tile04_05 = "g_horizontal.png"
    image EB3tile04_06 = "g_elbow_bl.png"
    image EB3tile04_08 = "y_elbow_br.png"
    image EB3tile04_09 = "y_horizontal.png"
    image EB3tile04_10 = "y_elbow_tl.png"
    image EB3tile04_12 = "y_vertical.png"
    
    show EB3tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show EB3tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image EB3tile05_00 = "r_horizontal.png"
    image EB3tile05_01 = "r_t_up.png"
    image EB3tile05_02 = "r_elbow_bl.png"
    image EB3tile05_04 = "g_vertical.png"
    image EB3tile05_06 = "g_g.png"
    image EB3tile05_07 = "NONE_Gate.png"
    image EB3tile05_08 = "y_t_left.png"
    image EB3tile05_12 = "y_vertical.png"
    
    show EB3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show EB3tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image EB3tile06_02 = "r_vertical.png"
    image EB3tile06_04 = "g_vertical.png"
    image EB3tile06_06 = "g_vertical.png"
    image EB3tile06_08 = "y_vertical.png"
    image EB3tile06_12 = "y_vertical.png"
    
    show EB3tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show EB3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show EB3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show EB3tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show EB3tile06_12 at Position(xpos = 1336, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image EB3tile07_00 = "g_horizontal.png"
    image EB3tile07_01 = "g_t_down.png"
    image EB3tile07_02 = "r_jump_g.png"
    image EB3tile07_03 = "g_horizontal.png"
    image EB3tile07_04 = "g_elbow_tl.png"
    image EB3tile07_06 = "g_vertical.png"
    image EB3tile07_08 = "y_vertical.png"
    image EB3tile07_10 = "y_elbow_br.png"
    image EB3tile07_11 = "y_horizontal.png"
    image EB3tile07_12 = "y_elbow_tl.png"
    image EB3tile07_13 = "y_elbow_br.png"
    
    show EB3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
    show EB3tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image EB3tile08_01 = "g_vertical.png"
    image EB3tile08_02 = "r_g.png"
    image EB3tile08_03 = "or_gate.png"
    image EB3tile08_04 = "g_horizontal.png"
    image EB3tile08_05 = "g_horizontal.png"
    image EB3tile08_06 = "g_elbow_tl.png"
    image EB3tile08_08 = "y_vertical.png"
    image EB3tile08_10 = "y_y.png"
    image EB3tile08_11 = "none_gate.png"
    image EB3tile08_12 = "y_horizontal.png"
    image EB3tile08_13 = "y_elbow_tl.png"
    
    show EB3tile08_01 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_02 at Position(xpos = 586, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_12 at Position(xpos = 1336, xanchor = 0, ypos = 833, yanchor = 0)
    show EB3tile08_13 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
    
    #row 9
    image EB3tile09_01 = "g_elbow_tr.png"
    image EB3tile09_02 = "g_elbow_tl.png"
    image EB3tile09_08 = "y_elbow_tr.png"
    image EB3tile09_09 = "y_horizontal.png"
    image EB3tile09_10 = "y_elbow_tl.png"
    
    show EB3tile09_01 at Position(xpos = 511, xanchor = 0, ypos = 908, yanchor = 0)
    show EB3tile09_02 at Position(xpos = 586, xanchor = 0, ypos = 908, yanchor = 0)
    show EB3tile09_08 at Position(xpos = 1036, xanchor = 0, ypos = 908, yanchor = 0)
    show EB3tile09_09 at Position(xpos = 1111, xanchor = 0, ypos = 908, yanchor = 0)
    show EB3tile09_10 at Position(xpos = 1186, xanchor = 0, ypos = 908, yanchor = 0)

    #start points
    image start1 = "light_r_on.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start3 = "light_r_on.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image start4 = "light_g_on.png"
    show start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image end4 = "light_g_off.png"
    show end4 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)

    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ or1x = 848
    $ or1y = 88
   
    # check conditons for locations
    $ and1in1 = False
    $ or1in1 = False
    $ and1in2 = False
    $ or1in2 = False
   
    #attempts for players
    $ attempts = 3
 
    jump gamefileB3
    
    
label gamefileB3:
    
    #calls game screen
    call screen logicGatesB3
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in1 = False
            #sets values for checks
            $ and1x = 961
            $ and1y = 608
            $ and1in1 = True
            $ and1in2 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in2 = False
            #sets values for checks
            $ and1x = 1261
            $ and1y = 833
            $ and1in2 = True
            $ and1in1 = False
            
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
            #sets values for checks
            $ or1x = 961
            $ or1y = 608
            $ or1in1 = True
            $ or1in2 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in2 = False
            #sets values for checks
            $ or1x = 1261
            $ or1y = 833
            $ or1in2 = True
            $ or1in1 = False
            
#*******************************************
#************image zone********************* 
#*******************************************
    if and1in1 == True:
        play sound pipeFlowG
        image EB3TILE2 = "r_g.png"
        image EB3TILE1  = "r_elbow_bl.png"
        image EB3TILE11 = "g_elbow_br.png"
        image EB3TILE12 = "g_horizontal.png"
        image EB3TILE13 = "g_elbow_tl.png"
        image EB3TILE14 = "r_vertical.png"
        image EB3TILE15 = "g_t_left.png"
        image EB3TILE16 = "r_vertical.png"
        image EB3TILE17 = "g_vertical.png"
        image EB3TILE18 = "r_vertical.png"
        image EB3TILE19 = "g_vertical.png"
        image EB3TILE111 = "r_elbow_br.png"
        image EB3TILE112 = "r_horizontal.png"
        image EB3TILE113 = "r_elbow_tl.png"
        image EB3TILE114 = "g_vertical.png"
        image EB3TILE115 = "r_g.png"
        image EB3TILE116 = "g_elbow_tr.png"
        image EB3TILE117 = "g_horizontal.png"
        image EB3TILE118 = "g_elbow_tl.png"
        
        show EB3TILE2 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show EB3TILE1 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        show EB3TILE11 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE12 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE13 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE14 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE15 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show EB3TILE16 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show EB3TILE17 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        show EB3TILE18 at Position(xpos = 1336, xanchor = 0, ypos = 683, yanchor = 0)
        show EB3TILE19 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE111 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE112 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE113 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE114 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show EB3TILE115 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
        show EB3TILE116 at Position(xpos = 1036, xanchor = 0, ypos = 908, yanchor = 0)
        show EB3TILE117 at Position(xpos = 1111, xanchor = 0, ypos = 908, yanchor = 0)
        show EB3TILE118 at Position(xpos = 1186, xanchor = 0, ypos = 908, yanchor = 0)
    
    if and1in1 == False:
#        play sound pipeFlowN
        hide EB3TILE2
        hide EB3TILE1
        hide EB3TILE11
        hide EB3TILE12
        hide EB3TILE13
        hide EB3TILE14
        hide EB3TILE15
        hide EB3TILE16
        hide EB3TILE17
        hide EB3TILE18
        hide EB3TILE19
        hide EB3TILE111
        hide EB3TILE112
        hide EB3TILE113
        hide EB3TILE114
        hide EB3TILE115
        hide EB3TILE116
        hide EB3TILE117
        hide EB3TILE118
        
    if and1in2 == True:
        if or1in1 == True:
            play sound pipeFlowR
            image EB3TILE141 = "r_horizontal.png"
            image EB3TILE142 = "r_elbow_tl.png"
            image EB3TILE143 = "r_elbow_br.png"
            
            show EB3TILE143 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
            show EB3TILE141 at Position(xpos = 1336, xanchor = 0, ypos = 833, yanchor = 0)
            show EB3TILE142 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
            
    if and1in2 == False:
#        play sound pipeFlowN
        hide EB3TILE143
        hide EB3TILE141
        hide EB3TILE142
        
    if or1in1 == True:
        play sound pipeFlowG
        image EB3TILE21 = "r_g.png"
        image EB3TILE120  = "r_elbow_bl.png"
        image EB3TILE121 = "g_elbow_br.png"
        image EB3TILE122 = "g_horizontal.png"
        image EB3TILE123 = "g_elbow_tl.png"
        image EB3TILE124 = "r_vertical.png"
        image EB3TILE125 = "g_t_left.png"
        image EB3TILE126 = "r_vertical.png"  
        image EB3TILE127 = "g_vertical.png"
        image EB3TILE128 = "r_vertical.png"       
        image EB3TILE129 = "g_vertical.png"
        image EB3TILE130 = "r_elbow_br.png"
        image EB3TILE131 = "r_horizontal.png"
        image EB3TILE132 = "r_elbow_tl.png"
        image EB3TILE135 = "g_elbow_tr.png"
        image EB3TILE136 = "g_horizontal.png"
        image EB3TILE137 = "g_elbow_tl.png"
        image EB3TILE133 = "g_vertical.png"
        image EB3TILE134 = "r_g.png"
        
        show EB3TILE127 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        show EB3TILE128 at Position(xpos = 1336, xanchor = 0, ypos = 683, yanchor = 0)
        show EB3TILE125 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
        show EB3TILE126 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show EB3TILE121 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE122 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE123 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE124 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
        show EB3TILE120 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
        show EB3TILE21 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)   
        show EB3TILE129 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE130 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE131 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE132 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
        show EB3TILE133 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show EB3TILE134 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
        show EB3TILE135 at Position(xpos = 1036, xanchor = 0, ypos = 908, yanchor = 0)
        show EB3TILE136 at Position(xpos = 1111, xanchor = 0, ypos = 908, yanchor = 0)
        show EB3TILE137 at Position(xpos = 1186, xanchor = 0, ypos = 908, yanchor = 0)
        
    if or1in1 == False:
#        play sound pipeFlowN
        hide EB3TILE127
        hide EB3TILE128
        hide EB3TILE129
        hide EB3TILE123
        hide EB3TILE125
        hide EB3TILE126
        hide EB3TILE121
        hide EB3TILE122
        hide EB3TILE124
        hide EB3TILE120
        hide EB3TILE21
        hide EB3TILE131
        hide EB3TILE132
        hide EB3TILE133
        hide EB3TILE134
        hide EB3TILE135
        hide EB3TILE136
        hide EB3TILE137
        hide EB3TILE130
 
    if or1in2 == True:
        if and1in1 == True:
            play sound pipeFlowG
            image EB3TILE138 = "g_horizontal.png"
            image EB3TILE139 = "g_elbow_tl.png"
            image EB3TILE140 = "g_elbow_br.png"
            
            show EB3TILE138 at Position(xpos = 1336, xanchor = 0, ypos = 833, yanchor = 0)
            show EB3TILE139 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
            show EB3TILE140 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
            
    if or1in2 == False:
#        play sound pipeFlowN
        hide EB3TILE138
        hide EB3TILE139
        hide EB3TILE140

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
    if and1in1 == True and or1in2 == True: 
        image EB3tile200 = "and_Gate.png"
        show EB3tile200 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
        image EB3tile220 = "or_gate.png"
        show EB3tile220 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        image EB3tile225 = "light_g_on.png"
        show EB3tile225 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ Logic_B_solved = True
        #make to jump back to the game
        jump nextLGEasy

    if attempts == 0:
        image EB311tile07_02 = "and_Gate.png"
        show EB311tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EB311tile07_08 = "or_Gate.png"
        show EB311tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        play sound lgLose
        $ lgEasy_tries +=1
        jump repeatLGEasy
    
    jump gamefileB3

screen logicGatesB3:
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
        action Jump("LGEasyHintsB3")
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
                
            drag:
                drag_name "or_gate"
                child "or_Gate.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y


            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos 961 ypos 608
           
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos 1261 ypos 833