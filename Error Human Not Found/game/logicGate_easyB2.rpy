
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

label logicGate_easyB2: #logicGate_easyB2
    $config.skipping=None
    $renpy.block_rollback()
    $quick_menu = False
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
    image EB2tile00_05 = "g_elbow_br.png"
    image EB2tile00_06 = "g_elbow_bl.png"
    
    show EB2tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
    show EB2tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image EB2tile01_00 = "r_horizontal.png"
    image EB2tile01_01 = "r_horizontal.png"
    image EB2tile01_02 = "r_elbow_bl.png"
    image EB2tile01_05 = "g_vertical.png"
    image EB2tile01_06 = "g_y.png"
    image EB2tile01_07 = "NONE_Gate.png"
    image EB2tile01_08 = "y_horizontal.png"
    image EB2tile01_09 = "y_horizontal.png"
    image EB2tile01_10= "y_elbow_bl.png"
    image EB2tile01_13 = "y_elbow_br.png"
    
    show EB2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
    show EB2tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image EB2tile02_02 = "r_g.png"
    image EB2tile02_03 = "OR_Gate.png"
    image EB2tile02_04 = "g_horizontal.png"
    image EB2tile02_05 = "g_elbow_tl.png"
    image EB2tile02_06 = "y_vertical.png"
    image EB2tile02_10 = "y_vertical.png"
    image EB2tile02_13 = "y_vertical.png"
    
    show EB2tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show EB2tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show EB2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show EB2tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show EB2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show EB2tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
    show EB2tile02_13 at Position(xpos = 1411, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image EB2tile03_00 = "g_horizontal.png"
    image EB2tile03_01 = "g_horizontal.png"
    image EB2tile03_02 = "g_t_left.png"
    image EB2tile03_06 = "y_vertical.png"
    image EB2tile03_10 = "y_vertical.png"
    image EB2tile03_13 = "y_vertical.png"
    
    show EB2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show EB2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show EB2tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show EB2tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show EB2tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show EB2tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image EB2tile04_02 = "g_r.png"
    image EB2tile04_03 = "NONE_Gate.png"
    image EB2tile04_04 = "y_horizontal.png"
    image EB2tile04_05 = "y_t_down.png"
    image EB2tile04_06 = "y_elbow_tl.png"
    image EB2tile04_10 = "y_y.png"
    image EB2tile04_11 = "OR_Gate.png"
    image EB2tile04_12 = "y_horizontal.png"
    image EB2tile04_13 = "y_elbow_tl.png"
    
    show EB2tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    show EB2tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image EB2tile05_00 = "r_horizontal.png"
    image EB2tile05_01 = "r_t_down.png"
    image EB2tile05_02 = "r_elbow_tl.png"
    image EB2tile05_05 = "y_vertical.png"
    image EB2tile05_10 = "y_vertical.png"
    
    show EB2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show EB2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show EB2tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show EB2tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show EB2tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    
    #typing error EB2tile 85 doesnt exisit nor is it needed
    
    #row 6
    image EB2tile06_01 = "r_vertical.png"
    image EB2tile06_05 = "y_elbow_tr.png"
    image EB2tile06_06 = "y_horizontal.png"
    image EB2tile06_07 = "y_elbow_bl.png"
    image EB2tile06_10 = "y_vertical.png"
    
    show EB2tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show EB2tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show EB2tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show EB2tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show EB2tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image EB2tile07_01 = "r_vertical.png"
    image EB2tile07_07 = "y_r.png"
    image EB2tile07_08 = "AND_Gate.png"
    image EB2tile07_09 = "y_horizontal.png"
    image EB2tile07_10 = "y_elbow_tl.png"
    
    show EB2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show EB2tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show EB2tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show EB2tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show EB2tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image EB2tile08_01 = "r_elbow_tr.png"
    image EB2tile08_02 = "r_horizontal.png"
    image EB2tile08_03 = "r_horizontal.png"
    image EB2tile08_04 = "r_horizontal.png"
    image EB2tile08_05 = "r_horizontal.png"
    image EB2tile08_06 = "r_horizontal.png"
    image EB2tile08_07 = "r_elbow_tl.png"
    
    show EB2tile08_01 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show EB2tile08_02 at Position(xpos = 586, xanchor = 0, ypos = 833, yanchor = 0)
    show EB2tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
    show EB2tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show EB2tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show EB2tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show EB2tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    
    #row 9

    #start points
    image start1 = "light_r_on.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start2 = "light_g_on.png"
    show start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image start3 = "light_r_on.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    
    #end points (only use one of these
    image end1 = "light_g_off.png"
    show end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
    
    
    
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
    $ and1in2 = False
    $ or1in1 = False
    $ or1in2 = False
   
    #attempts for players
    $ attempts = 3
 
    jump gamefileB2
    
    
label gamefileB2:
    
    #calls game screen
    call screen logicGatesB2
    
    #the and logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in1 = False
            #sets values for checks
            $ and1x = 661
            $ and1y = 533
            $ and1in1 = True
            $ and1in2 = False
 
        if slot_name == "gate slot two":
            if or1in2 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in2 = False
            #sets values for checks
            $ and1x = 961
            $ and1y = 308
            $ and1in2 = True
            $ and1in1 = False
            
    # the or logic gate************************************************************************
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
            #sets values for checks
            $ or1x = 661
            $ or1y = 533
            $ or1in1 = True
            $ or1in2 = False
            
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            #sets values for checks
            $ or1x = 961
            $ or1y = 308
            $ or1in2 = True  
            $ or1in1 = False        



#*******************************************
#************image zone********************* 
#*******************************************
    if and1in1 == True:
        play sound pipeFlowR
        image EB22tile01_06 = "g_r.png"
        image EB22tile03_06 = "r_vertical.png"
        image EB22tile02_06 = "r_vertical.png"
        image EB22tile04_04 = "r_horizontal.png"
        image EB22tile04_05 = "r_t_down.png"
        image EB22tile04_06 = "r_elbow_tl.png"
        image EB22tile04_10 = "y_r.png"
        image EB22tile05_05 = "r_vertical.png"
        image EB22tile05_10 = "r_vertical.png"       
        image EB22tile06_05 = "r_elbow_tr.png"
        image EB22tile06_06 = "r_horizontal.png"
        image EB22tile06_07 = "r_elbow_bl.png"
        image EB22tile06_10 = "r_vertical.png"
        image EB22tile07_07 = "r_r.png"      
        image EB22tile07_09 = "r_horizontal.png"
        image EB22tile07_10 = "r_elbow_tl.png"
        
        show EB22tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show EB22tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show EB22tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show EB22tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show EB22tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show EB22tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        show EB22tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        show EB22tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show EB22tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show EB22tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show EB22tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show EB22tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show EB22tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show EB22tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show EB22tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show EB22tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        
    if and1in1 == False:
#        play sound pipeFlowN
        hide EB22tile02_06
        hide EB22tile01_06
        hide EB22tile03_06
        hide EB22tile04_04
        hide EB22tile04_05
        hide EB22tile04_06
        hide EB22tile04_10
        hide EB22tile05_05
        hide EB22tile05_10
        hide EB22tile06_05
        hide EB22tile06_06
        hide EB22tile06_07
        hide EB22tile06_10
        hide EB22tile07_07
        hide EB22tile07_09
        hide EB22tile07_10            
        
    if or1in1 == True:
        play sound pipeFlowG
        image EB23tile01_06 = "g_g.png"
        image EB23tile03_06 = "g_vertical.png"
        image EB23tile02_06 = "g_vertical.png"
        image EB23tile04_04 = "g_horizontal.png"
        image EB23tile04_05 = "g_t_down.png"
        image EB23tile04_06 = "g_elbow_tl.png"
        image EB23tile04_10 = "y_r.png"
        image EB23tile05_05 = "g_vertical.png"
        image EB23tile05_10 = "r_vertical.png"       
        image EB23tile06_05 = "g_elbow_tr.png"
        image EB23tile06_06 = "g_horizontal.png"
        image EB23tile06_07 = "g_elbow_bl.png"
        image EB23tile06_10 = "r_vertical.png"
        image EB23tile07_07 = "g_r.png"      
        image EB23tile07_09 = "r_horizontal.png"
        image EB23tile07_10 = "r_elbow_tl.png"
        
        show EB23tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show EB23tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        show EB23tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        show EB23tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show EB23tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
        show EB23tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        show EB23tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        show EB23tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show EB23tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show EB23tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show EB23tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show EB23tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show EB23tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
        show EB23tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
        show EB23tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show EB23tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        
    if or1in1 == False:
#        play sound pipeFlowN
        hide EB23tile02_06
        hide EB23tile01_06
        hide EB23tile03_06
        hide EB23tile04_04
        hide EB23tile04_05
        hide EB23tile04_06
        hide EB23tile04_10
        hide EB23tile05_05
        hide EB23tile05_10
        hide EB23tile06_05
        hide EB23tile06_06
        hide EB23tile06_07
        hide EB23tile06_10
        hide EB23tile07_07
        hide EB23tile07_09
        hide EB23tile07_10

    if and1in2 == True:
        if or1in1 == True:
            play sound pipeFlowG
            image EB24tile01_08 = "g_horizontal.png"
            image EB24tile01_09 = "g_horizontal.png"
            image EB24tile01_10= "g_elbow_bl.png"
            image EB24tile01_13 = "g_elbow_br.png"
            image EB24tile02_10 = "g_vertical.png"
            image EB24tile02_13 = "g_vertical.png"
            image EB24tile03_10 = "g_vertical.png"
            image EB24tile03_13 = "g_vertical.png"
            image EB24tile04_10 = "g_r.png"
            image EB24tile04_12 = "g_horizontal.png"
            image EB24tile04_13 = "g_elbow_tl.png"
           
            show EB24tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
            show EB24tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
            show EB24tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show EB24tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show EB24tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show EB24tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
            show EB24tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
            show EB24tile02_13 at Position(xpos = 1411, xanchor = 0, ypos = 383, yanchor = 0)
            show EB24tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
            show EB24tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            show EB24tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
            
    if or1in2 == True:
        if and1in1 == True:
            play sound pipeFlowG
            image EB25tile01_08 = "g_horizontal.png"
            image EB25tile01_09 = "g_horizontal.png"
            image EB25tile01_10= "g_elbow_bl.png"
            image EB25tile01_13 = "g_elbow_br.png"
            image EB25tile02_10 = "g_vertical.png"
            image EB25tile02_13 = "g_vertical.png"
            image EB25tile03_10 = "g_vertical.png"
            image EB25tile03_13 = "g_vertical.png"
            image EB25tile04_10 = "g_r.png"
            image EB25tile04_12 = "g_horizontal.png"
            image EB25tile04_13 = "g_elbow_tl.png"
           
            show EB25tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
            show EB25tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)            
            show EB25tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show EB25tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show EB25tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show EB25tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
            show EB25tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
            show EB25tile02_13 at Position(xpos = 1411, xanchor = 0, ypos = 383, yanchor = 0)
            show EB25tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
            show EB25tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
            show EB25tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)


        
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
    if and1in2 == True and or1in1 == True: 
        image EB22end1 = "light_g_on.png"
        show EB22end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
        image EB22tile04_03 = "or_Gate.png"
        show EB22tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        image EB22tile01_07 = "and_Gate.png"
        show EB22tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ Logic_B_solved = True
        #make to jump back to the game
        jump nextLGEasy
        
        
    if and1in1 == True and or1in2 == True:
        image EB25end1 = "light_g_on.png"
        show EB25end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
        image EB25tile04_03 = "and_Gate.png"
        show EB25tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        image EB25tile01_07 = "or_Gate.png"
        show EB25tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ Logic_B_solved = True
        #make to jump back to the game
        jump nextLGEasy

    if attempts == 0:
        image EB211tile07_02 = "and_Gate.png"
        show EB211tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EB211tile07_08 = "or_Gate.png"
        show EB211tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        play sound lgLose
        $ lgEasy_tries +=1
        jump repeatLGEasy
    
    jump gamefileB2

screen logicGatesB2:
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
        action Jump("LGEasyHintsB2")
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
                child "OR_Gate.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos 661 ypos 533
                
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos 961 ypos 308
