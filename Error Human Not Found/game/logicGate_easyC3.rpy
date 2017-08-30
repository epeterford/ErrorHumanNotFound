#init python:

#    #makes it so the game doesn't stop early
#    def gate_dragged(drags,drop):
#        if not drop:
#            store.gate_name = drags[0].drag_name
#            store.slot_name = "null"
#            return True
#        #checks to see the drop location and makes it snap        
#        if drop:
#            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
#            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
#            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
#            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
#                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop 
#                #this store the values for the if checks
#                store.gate_name = drags[0].drag_name
#                store.slot_name = drop.drag_name

#            return True
#        return True

label logicGate_easyC3: 
    $config.skipping=None
    $renpy.block_rollback()

    $quick_menu = False
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
    image EC3tile00_08 = "y_elbow_br.png"
    image EC3tile00_09 = "y_horizontal.png"
    image EC3tile00_10 = "y_horizontal.png"
    image EC3tile00_11 = "y_elbow_bl.png"
    
    show EC3tile00_08 at Position(xpos = 1036, xanchor = 0, ypos = 233, yanchor = 0)
    show EC3tile00_09 at Position(xpos = 1111, xanchor = 0, ypos = 233, yanchor = 0)
    show EC3tile00_10 at Position(xpos = 1186, xanchor = 0, ypos = 233, yanchor = 0)
    show EC3tile00_11 at Position(xpos = 1261, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image EC3tile01_00 = "r_horizontal.png"
    image EC3tile01_01 = "r_horizontal.png"
    image EC3tile01_02 = "NOT_Gate_blue.png"
    image EC3tile01_03 = "g_horizontal.png"
    image EC3tile01_04 = "g_horizontal.png"
    image EC3tile01_05 = "g_elbow_bl.png"
    image EC3tile01_08 = "y_vertical.png"
    image EC3tile01_11 = "y_y.png"
    image EC3tile01_12 = "AND_Gate_blue.png"
    image EC3tile01_13 = "y_horizontal.png"
    
    show EC3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
    show EC3tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image EC3tile02_05 = "g_r.png"
    image EC3tile02_06 = "NONE_Gate.png"
    image EC3tile02_07 = "y_horizontal.png"
    image EC3tile02_08 = "y_elbow_tl.png"
    image EC3tile02_11 = "y_vertical.png"
    
    show EC3tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show EC3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show EC3tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show EC3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show EC3tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image EC3tile03_00 = "r_horizontal.png"
    image EC3tile03_01 = "r_elbow_bl.png"
    image EC3tile03_05 = "r_vertical.png"
    image EC3tile03_11 = "y_vertical.png"
    
    show EC3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show EC3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show EC3tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show EC3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image EC3tile04_01 = "r_r.png"
    image EC3tile04_02 = "OR_Gate_blue.png"
    image EC3tile04_03 = "r_horizontal.png"
    image EC3tile04_04 = "r_horizontal.png"
    image EC3tile04_05 = "r_t_up.png"
    image EC3tile04_06 = "r_horizontal.png"
    image EC3tile04_07 = "r_elbow_bl.png"
    image EC3tile04_11 = "y_vertical.png"
    
    show EC3tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show EC3tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image EC3tile05_00 = "r_horizontal.png"
    image EC3tile05_01 = "r_t_up.png"
    image EC3tile05_02 = "r_horizontal.png"
    image EC3tile05_03 = "r_horizontal.png"
    image EC3tile05_04 = "r_elbow_bl.png"
    image EC3tile05_07 = "r_y.png"
    image EC3tile05_08 = "OR_Gate_blue.png"
    image EC3tile05_09 = "y_horizontal.png"
    image EC3tile05_10 = "NONE_Gate.png"
    image EC3tile05_11 = "y_elbow_tl.png"
    
    show EC3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show EC3tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image EC3tile06_04 = "r_g.png"
    image EC3tile06_05 = "NONE_Gate.png"
    image EC3tile06_06 = "y_horizontal.png"
    image EC3tile06_07 = "y_elbow_tl.png"
    
    show EC3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show EC3tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show EC3tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show EC3tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image EC3tile07_00 = "g_horizontal.png"
    image EC3tile07_01 = "g_horizontal.png"
    image EC3tile07_02 = "g_horizontal.png"
    image EC3tile07_03 = "g_horizontal.png"
    image EC3tile07_04 = "g_elbow_tl.png"
    
    show EC3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show EC3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show EC3tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show EC3tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show EC3tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    
    #start points
    image start1 = "light_r_on.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start2 = "light_r_on.png"
    show start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image start3 = "light_r_on.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image start4 = "light_g_on.png"
    show start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
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
    $ not1x = 548
    $ not1y = 88
    
    #gate values
    $ gate1x = 811
    $ gate1y = 683
    $ gate2x = 886
    $ gate2y = 383
    $ gate3x = 1186
    $ gate3y = 608
   
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
 
    jump gamefileC3
    
    
label gamefileC3:
    
    #calls game screen
    call screen logicGatesC3
    
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

    if not1in3 == True:
        if and1in1 == True:
            play sound pipeFlowG
            image EC36tile02_11 = "g_vertical.png"
            show EC36tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image EC36tile03_11 = "g_vertical.png"
            show EC36tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image EC36tile04_11 = "g_vertical.png"
            show EC36tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image EC36tile05_11 = "g_elbow_tl.png"
            show EC36tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image EC36tile01_11 = "y_g.png"
            show EC36tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            
        if or1in1 == True:
            play sound pipeFlowR
            image EC35tile02_11 = "r_vertical.png"
            show EC35tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image EC35tile03_11 = "r_vertical.png"
            show EC35tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image EC35tile04_11 = "r_vertical.png"
            show EC35tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image EC35tile05_11 = "r_elbow_tl.png"
            show EC35tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image EC35tile01_11 = "y_r.png"
            show EC35tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            
    if not1in3 == False or (and1in1 == False and or1in1 == False):
#        play sound pipeFlowN
        hide EC35tile02_11
        hide EC35tile03_11
        hide EC35tile04_11
        hide EC35tile05_11
        hide EC35tile01_11
        hide EC36tile02_11
        hide EC36tile03_11
        hide EC36tile04_11
        hide EC36tile05_11
        hide EC36tile01_11

    if and1in2 == True:
        play sound pipeFlowR
        image EC31tile00_08 = "r_elbow_br.png"
        image EC31tile00_09 = "r_horizontal.png"
        image EC31tile00_10 = "r_horizontal.png"
        image EC31tile00_11 = "r_elbow_bl.png"
        show EC31tile00_08 at Position(xpos = 1036, xanchor = 0, ypos = 233, yanchor = 0)
        show EC31tile00_09 at Position(xpos = 1111, xanchor = 0, ypos = 233, yanchor = 0)
        show EC31tile00_10 at Position(xpos = 1186, xanchor = 0, ypos = 233, yanchor = 0)
        show EC31tile00_11 at Position(xpos = 1261, xanchor = 0, ypos = 233, yanchor = 0)
        image EC31tile01_08 = "r_vertical.png"
        show EC31tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        image EC31tile01_11 = "r_y.png"
        show EC31tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image  EC31tile02_07 = "r_horizontal.png"
        image  EC31tile02_08 = "r_elbow_tl.png"
        show  EC31tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show  EC31tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        
    if and1in2 == False:
#        play sound pipeFlowN
        hide EC31tile00_08
        hide EC31tile00_09
        hide EC31tile00_10
        hide EC31tile00_11
        hide EC31tile01_08
        hide EC31tile01_11
        hide EC31tile02_07
        hide EC31tile02_08

    if or1in2 == True:
        play sound pipeFlowG
        image  EC32tile00_08 = "g_elbow_br.png"
        image EC32tile00_09 = "g_horizontal.png"
        image EC32tile00_10 = "g_horizontal.png"
        image EC32tile00_11 = "g_elbow_bl.png"
        show EC32tile00_08 at Position(xpos = 1036, xanchor = 0, ypos = 233, yanchor = 0)
        show EC32tile00_09 at Position(xpos = 1111, xanchor = 0, ypos = 233, yanchor = 0)
        show EC32tile00_10 at Position(xpos = 1186, xanchor = 0, ypos = 233, yanchor = 0)
        show EC32tile00_11 at Position(xpos = 1261, xanchor = 0, ypos = 233, yanchor = 0)
        image EC32tile01_08 = "g_vertical.png"
        show EC32tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
        image EC32tile01_11 = "g_y.png"
        show EC32tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image EC32tile02_07 = "g_horizontal.png"
        image EC32tile02_08 = "g_elbow_tl.png"
        show EC32tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show EC32tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
        
    if or1in2 == False:
#        play sound pipeFlowN
        hide EC32tile00_08
        hide EC32tile00_09
        hide EC32tile00_10
        hide EC32tile00_11
        hide EC32tile01_08
        hide EC32tile01_11
        hide EC32tile02_07
        hide EC32tile02_08
        
    if and1in1 == True:
        play sound pipeFlowR
        image EC33tile06_06 = "r_horizontal.png"
        image EC33tile06_07 = "r_elbow_tl.png"
        show EC33tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show EC33tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image EC33tile05_07 = "r_r.png"
        show EC33tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
        image EC33tile05_09 = "r_horizontal.png"
        show EC33tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        
    if and1in1 == False:
#        play sound pipeFlowN
        hide EC33tile06_06
        hide EC33tile06_07
        hide EC33tile05_07
        hide EC33tile05_09

    if or1in1 == True:
        play sound pipeFlowG
        image EC34tile06_06 = "g_horizontal.png"
        image EC34tile06_07 = "g_elbow_tl.png"
        show EC34tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show EC34tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        image EC34tile05_07 = "r_g.png"
        show EC34tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
        image EC34tile05_09 = "g_horizontal.png"
        show EC34tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    
    if or1in1 == False:
#        play sound pipeFlowN
        hide EC34tile06_06
        hide EC34tile06_07
        hide EC34tile05_07
        hide EC34tile05_09
        
    if not1in3 == True and and1in2 == True and or1in1 == True:
        play sound pipeFlowR
        image EC100tile01_13 = "r_horizontal.png"
        show EC100tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        image EC362tile01_11 = "r_r.png"
        show EC362tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
    else:
#        play sound pipeFlowN
        hide EC100tile01_13
        hide EC362tile01_11
        
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
    if and1in1 == True and or1in2 == True and not1in3 == True: 
        image tile01_13 = "g_horizontal.png"
        show tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        image EC361tile01_11 = "g_g.png"
        show EC361tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image EC312tile02_09 = "not_Gate.png"
        show EC312tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image EC312tile07_02 = "and_Gate.png"
        show EC312tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EC312tile07_08 = "or_Gate.png"
        show EC312tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image EC38end2 = "light_g_on.png"
        show EC38end2 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ solved_LG_easy = True
        $ hiroseOfficeComputer = True
        $ hiroseOfficeItems += 1
        #make to jump back to the game
        jump lgEasyDone

    if attempts == 0:
        image EC311tile02_09 = "not_Gate.png"
        show EC311tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
        image EC311tile07_02 = "and_Gate.png"
        show EC311tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EC311tile07_08 = "or_Gate.png"
        show EC311tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        play sound lgLose
        $renpy.pause(1.5)
        $ lgEasy_tries +=1
        jump repeatLGEasy
    
    jump gamefileC3

screen logicGatesC3:
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
        action Jump("LGEasyHintsC3")
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