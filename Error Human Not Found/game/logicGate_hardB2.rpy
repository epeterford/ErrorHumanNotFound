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

label logicGate_hardB2:
    #loads background
    scene bg Logic_Gate
    
    image HB2tile00_05 = "y_elbow_br.png"
    image HB2tile00_06 = "y_elbow_bl.png"
    
    show HB2tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
    show HB2tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image HB2tile01_00 = "r_horizontal.png"
    image HB2tile01_01 = "r_elbow_bl.png"
    image HB2tile01_05 = "y_vertical.png"
    image HB2tile01_06 = "y_y.png"
    image HB2tile01_07 = "NONE_Gate.png"
    image HB2tile01_08 = "y_horizontal.png"
    image HB2tile01_09 = "y_horizontal.png"
    image HB2tile01_10= "y_horizontal.png"
    image HB2tile01_11 = "y_elbow_bl.png"
    
    show HB2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
    show HB2tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image HB2tile02_01 = "r_g.png"
    image HB2tile02_02 = "NONE_Gate.png"
    image HB2tile02_03 = "y_horizontal.png"
    image HB2tile02_04 = "y_t_down.png"
    image HB2tile02_05 = "y_elbow_tl.png"
    image HB2tile02_06 = "y_vertical.png"
    image HB2tile02_11 = "y_vertical.png"
    
    show HB2tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show HB2tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show HB2tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show HB2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show HB2tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show HB2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show HB2tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image HB2tile03_00 = "g_horizontal.png"
    image HB2tile03_01 = "g_t_up.png"
    image HB2tile03_02 = "g_horizontal.png"
    image HB2tile03_03 = "g_elbow_bl.png"
    image HB2tile03_04 = "y_vertical.png"
    image HB2tile03_06 = "y_vertical.png"
    image HB2tile03_11 = "y_y.png"
    image HB2tile03_12 = "NOR_Gate_blue.png"
    image HB2tile03_13 = "y_horizontal.png"
    
    show HB2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show HB2tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image HB2tile04_03 = "g_vertical.png"
    image HB2tile04_04 = "y_g.png"
    image HB2tile04_05 = "NONE_Gate.png"
    image HB2tile04_06 = "y_t_up.png"
    image HB2tile04_07 = "y_horizontal.png"
    image HB2tile04_08 = "y_horizontal.png"
    image HB2tile04_09 = "y_elbow_bl.png"
    image HB2tile04_11 = "y_vertical.png"
    show HB2tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
    show HB2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image HB2tile05_00 = "r_elbow_bl.png"
    image HB2tile05_03 = "g_elbow_tr.png"
    image HB2tile05_04 = "g_elbow_tl.png"
    image HB2tile05_09 = "y_y.png"
    image HB2tile05_10 = "OR_Gate_blue.png"
    image HB2tile05_11 = "y_elbow_tl.png"
    
    show HB2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show HB2tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show HB2tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show HB2tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show HB2tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show HB2tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image HB2tile06_00 = "r_r.png"
    image HB2tile06_01 = "NONE_Gate.png"
    image HB2tile06_02 = "y_horizontal.png"
    image HB2tile06_03 = "y_horizontal.png"
    image HB2tile06_04 = "y_horizontal.png"
    image HB2tile06_05 = "NOT_Gate_blue.png"
    image HB2tile06_06 = "y_horizontal.png"
    image HB2tile06_07 = "y_horizontal.png"
    image HB2tile06_08 = "y_horizontal.png"
    image HB2tile06_09 = "y_elbow_tl.png"
    
    show HB2tile06_00 at Position(xpos = 436, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    show HB2tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image HB2tile07_00 = "r_elbow_tl.png"
    
    show HB2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    

    #start points
    image start1 = "light_r_on.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start2 = "light_g_on.png"
    show start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image start3 = "light_r_on.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image start4 = "light_r_on.png"
    show start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image end2 = "light_g_off.png"
    show end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)

    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
   
    $ temp_slot = ""
    $ temp_gate = ""
    $ gate_name = ""
    $ slot_name = ""

    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ nand1x = 998
    $ nand1y = 88
    $ xor1x = 1298
    $ xor1y = 88
    $ xor2x = 1298
    $ xor2y = 88
    
    #gate values
    $ gate1x = 586
    $ gate1y = 383
    $ gate2x = 511
    $ gate2y = 683
    $ gate3x = 811
    $ gate3y = 533
    $ gate4x = 961
    $ gate4y = 308
    
    # check conditons for locations
    $ and1in1 = False
    $ nand1in1 = False
    $ xor1in1 = False
    $ xor2in1 = False
    $ and1in2 = False
    $ nand1in2 = False
    $ xor1in2 = False
    $ xor2in2 = False
    $ and1in3 = False
    $ nand1in3 = False
    $ xor1in3 = False
    $ xor2in3 = False
    $ and1in4 = False
    $ nand1in4 = False
    $ xor1in4 = False
    $ xor2in4 = False   
    
    #attempts for players
    $ attempts = 600
 
    jump gamefileHB2
    
    
label gamefileHB2:
    
    #calls game screen
    call screen logicgatesHB2
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nand1in1 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in1 = False
            if xor1in1 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in1 = False
            if xor2in1 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in1 = False
                
            #sets values for checks
            $ and1x = gate1x
            $ and1y = gate1y
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
            $ and1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nand1in2 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in2 = False
            if xor1in2 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in2 = False
            if xor2in2 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in2 = False
                
            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = False
            
        #gate slot number three*******************************        
        if slot_name == "gate slot three":
            if nand1in3 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in3 = False
            if xor1in3 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in3 = False
                
            #sets values for checks
            $ and1x = gate3x
            $ and1y = gate3y
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = True
            $ and1in4 = False
            
        if slot_name == "gate slot four":
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
            if xor1in4 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in4 = False
                
            #sets values for checks
            $ and1x = gate4x
            $ and1y = gate4y
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = True
            
        if slot_name == "and return":
            $ and1x = 698
            $ and1y = 88
            $ and1in2 = False
            $ and1in1 = False
            $ and1in3 = False
            $ and1in4 = False
            
     #or gate section **********************************************************************       
    if gate_name == "nand_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
            if xor1in1 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in1 = False
            if xor2in1 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in1 = False
                
            #sets values for checks
            $ nand1x = gate1x
            $ nand1y = gate1y
            $ nand1in1 = True
            $ nand1in2 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            if xor1in2 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in2 = False
            if xor2in2 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in2 = False
                
            #sets values for checks
            $ nand1x = gate2x
            $ nand1y = gate2y
            $ nand1in2 = True
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
        #gate slot number three*******************************    
        if slot_name == "gate slot three":
            if and1in3 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in3 = False
            if xor1in3 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in3 = False
            if xor2in3 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in3 = False
                
            #sets values for checks
            $ nand1x = gate3x
            $ nand1y = gate3y
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = True
            $ nand1in4 = False
            
        if slot_name == "gate slot four":
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if xor1in4 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in4 = False
            if xor2in4 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in4 = False
                
            #sets values for checks
            $ nand1x = gate4x
            $ nand1y = gate4y
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = True
            
        if slot_name == "nand return":
            $ nand1x = 998
            $ nand1y = 88
            $ nand1in2 = False
            $ nand1in1 = False
            $ nand1in3 = False
            $ nand1in4 = False
            
     #nand gate section **********************************************************************       
    if gate_name == "xor_gate1":
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
            if xor2in1 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in1 = False                

            #sets values for checks
            $ xor1x = gate1x
            $ xor1y = gate1y
            $ xor1in1 = True
            $ xor1in2 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
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
            if xor2in2 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in2 = False  
                
            #sets values for checks
            $ xor1x = gate2x
            $ xor1y = gate2y
            $ xor1in2 = True
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False
            
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
            if xor2in3 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in3 = False
                
            #sets values for checks
            $ xor1x = gate3x
            $ xor1y = gate3y
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = True
            $ xor1in4 = False
            
        if slot_name == "gate slot four":
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
            if xor2in4 == True:
                $ xor2x = 1298
                $ xor2y = 88
                $ xor2in4 = False  
                
            #sets values for checks
            $ xor1x = gate4x
            $ xor1y = gate4y
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = True
        
        if slot_name == "xor return":
            $ xor1x = 1298
            $ xor1y = 88
            $ xor1in2 = False
            $ xor1in1 = False
            $ xor1in3 = False
            $ xor1in4 = False

    if gate_name == "xor_gate2":
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
            if xor1in1 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in1 = False                

            #sets values for checks
            $ xor2x = gate1x
            $ xor2y = gate1y
            $ xor2in1 = True
            $ xor2in2 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
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
            if xor1in2 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in2 = False  
                
            #sets values for checks
            $ xor2x = gate2x
            $ xor2y = gate2y
            $ xor2in2 = True
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
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
            if xor1in3 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in3 = False
                
            #sets values for checks
            $ xor2x = gate3x
            $ xor2y = gate3y
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = True
            $ xor2in4 = False
            
        if slot_name == "gate slot four":
            if and1in4 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in4 = False
            if nand1in4 == True:
                $ nand1x = 998
                $ nand1y = 88
                $ nand1in4 = False
            if xor2in4 == True:
                $ xor1x = 1298
                $ xor1y = 88
                $ xor1in4 = False  
                
            #sets values for checks
            $ xor2x = gate4x
            $ xor2y = gate4y
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = True
        
        if slot_name == "xor return":
            $ xor2x = 998
            $ xor2y = 88
            $ xor2in2 = False
            $ xor2in1 = False
            $ xor2in3 = False
            $ xor2in4 = False
            
    if temp_slot == "" and temp_gate == "" and slot_name != "null":
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
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "xor_gate2":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "xor_gate1":
                $ attempts +=1  
            if slot_name == "nand return" and gate_name == "xor_gate2":
                $ attempts +=1    
            if slot_name == "and return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "xor_gate1":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "xor_gate2":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "xor return" and gate_name == "nand_gate":
                $ attempts +=1

#*******************************************
#************image zone********************* 
#*******************************************

    if and1in1 == True:
        image HB21tile00_05 = "r_elbow_br.png"
        image HB21tile00_06 = "r_elbow_bl.png"
        show HB21tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
        show HB21tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
        image HB21tile01_05 = "r_vertical.png"
        image HB21tile01_06 = "r_y.png"
        show HB21tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
        show HB21tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        image HB21tile02_03 = "r_horizontal.png"
        image HB21tile02_04 = "r_t_down.png"
        image HB21tile02_05 = "r_elbow_tl.png"
        show HB21tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB21tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB21tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        image HB21tile03_04 = "r_vertical.png"        
        show HB21tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)  
        image HB21tile04_04 = "r_g.png"
        show HB21tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HB21tile00_05
        hide HB21tile00_06
        hide HB21tile01_05
        hide HB21tile01_06
        hide HB21tile02_03
        hide HB21tile02_04
        hide HB21tile02_05
        hide HB21tile03_04
        hide HB21tile04_04

    if nand1in1 == True:
        image HB23tile00_05 = "r_elbow_br.png"
        image HB23tile00_06 = "r_elbow_bl.png"
        show HB23tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
        show HB23tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
        image HB23tile01_05 = "r_vertical.png"
        image HB23tile01_06 = "r_y.png"
        show HB23tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
        show HB23tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        image HB23tile02_03 = "r_horizontal.png"
        image HB23tile02_04 = "r_t_down.png"
        image HB23tile02_05 = "r_elbow_tl.png"
        show HB23tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB23tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB23tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        image HB23tile03_04 = "r_vertical.png"        
        show HB23tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)  
        image HB23tile04_04 = "r_g.png"
        show HB23tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HB23tile00_05
        hide HB23tile00_06
        hide HB23tile01_05
        hide HB23tile01_06
        hide HB23tile02_03
        hide HB23tile02_04
        hide HB23tile02_05
        hide HB23tile03_04
        hide HB23tile04_04

    if xor1in1 == True or xor2in1 == True:
        image HB25tile00_05 = "g_elbow_br.png"
        image HB25tile00_06 = "g_elbow_bl.png"
        show HB25tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
        show HB25tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
        image HB25tile01_05 = "g_vertical.png"
        image HB25tile01_06 = "g_y.png"
        show HB25tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
        show HB25tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
        image HB25tile02_03 = "g_horizontal.png"
        image HB25tile02_04 = "g_t_down.png"
        image HB25tile02_05 = "g_elbow_tl.png"
        show HB25tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
        show HB25tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show HB25tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
        image HB25tile03_04 = "g_vertical.png"        
        show HB25tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)  
        image HB25tile04_04 = "g_g.png"
        show HB25tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    else:
        hide HB25tile00_05
        hide HB25tile00_06
        hide HB25tile01_05
        hide HB25tile01_06
        hide HB25tile02_03
        hide HB25tile02_04
        hide HB25tile02_05
        hide HB25tile03_04
        hide HB25tile04_04

    
    if and1in2 == True:
        image HB22tile06_02 = "r_horizontal.png"
        image HB22tile06_03 = "r_horizontal.png"
        image HB22tile06_04 = "r_horizontal.png"
        image HB22tile06_06 = "g_horizontal.png"
        image HB22tile06_07 = "g_horizontal.png"
        image HB22tile06_08 = "g_horizontal.png"
        image HB22tile06_09 = "g_elbow_tl.png"
        show HB22tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
        show HB22tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB22tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HB22tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show HB22tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show HB22tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        show HB22tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        image HB22tile05_09 = "y_g.png"
        show HB22tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        
    else:
        hide HB22tile06_02
        hide HB22tile06_03
        hide HB22tile06_04
        hide HB22tile06_06
        hide HB22tile06_07
        hide HB22tile06_08
        hide HB22tile06_09
        hide HB22tile05_09
        
    if nand1in2 == True:
        image HB24tile06_02 = "g_horizontal.png"
        image HB24tile06_03 = "g_horizontal.png"
        image HB24tile06_04 = "g_horizontal.png"
        image HB24tile06_06 = "r_horizontal.png"
        image HB24tile06_07 = "r_horizontal.png"
        image HB24tile06_08 = "r_horizontal.png"
        image HB24tile06_09 = "r_elbow_tl.png"
        show HB24tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
        show HB24tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB24tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HB24tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show HB24tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show HB24tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        show HB24tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        image HB24tile05_09 = "y_r.png"
        show HB24tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        
    else:
        hide HB24tile06_02
        hide HB24tile06_03
        hide HB24tile06_04
        hide HB24tile06_06
        hide HB24tile06_07
        hide HB24tile06_08
        hide HB24tile06_09
        hide HB24tile05_09

    if xor1in2 == True or xor2in2 == True:
        image HB26tile06_02 = "r_horizontal.png"
        image HB26tile06_03 = "r_horizontal.png"
        image HB26tile06_04 = "r_horizontal.png"
        image HB26tile06_06 = "g_horizontal.png"
        image HB26tile06_07 = "g_horizontal.png"
        image HB26tile06_08 = "g_horizontal.png"
        image HB26tile06_09 = "g_elbow_tl.png"
        show HB26tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
        show HB26tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show HB26tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show HB26tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
        show HB26tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
        show HB26tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
        show HB26tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        image HB26tile05_09 = "y_g.png"
        show HB26tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        
    else:
        hide HB26tile06_02
        hide HB26tile06_03
        hide HB26tile06_04
        hide HB26tile06_06
        hide HB26tile06_07
        hide HB26tile06_08
        hide HB26tile06_09
        hide HB26tile05_09

            
    if and1in3 == True:
        if nand1in1 == True:
            image HB27tile01_06 = "r_r.png"
            show HB27tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB27tile02_06 = "r_vertical.png"
            show HB27tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB27tile03_06 = "r_vertical.png"
            show HB27tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB27tile04_06 = "r_t_up.png"
            image HB27tile04_07 = "r_horizontal.png"
            image HB27tile04_08 = "r_horizontal.png"
            image HB27tile04_09 = "r_elbow_bl.png"
            show HB27tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB27tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB27tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB27tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB27tile05_09 = "r_y.png"    
            show HB27tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB27tile01_06
            hide HB27tile02_06
            hide HB27tile03_06
            hide HB27tile04_06
            hide HB27tile04_07
            hide HB27tile04_08
            hide HB27tile04_09
            hide HB27tile05_09

        if xor1in1 == True or xor2in1 == True:
            image HB28tile01_06 = "g_g.png"
            show HB28tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB28tile02_06 = "g_vertical.png"
            show HB28tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB28tile03_06 = "g_vertical.png"
            show HB28tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB28tile04_06 = "g_t_up.png"
            image HB28tile04_07 = "g_horizontal.png"
            image HB28tile04_08 = "g_horizontal.png"
            image HB28tile04_09 = "g_elbow_bl.png"
            show HB28tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB28tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB28tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB28tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB28tile05_09 = "g_y.png"    
            show HB28tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB28tile01_06
            hide HB28tile02_06
            hide HB28tile03_06
            hide HB28tile04_06
            hide HB28tile04_07
            hide HB28tile04_08
            hide HB28tile04_09
            hide HB28tile05_09

    else:
        hide HB27tile01_06
        hide HB27tile02_06
        hide HB27tile03_06
        hide HB27tile04_06
        hide HB27tile04_07
        hide HB27tile04_08
        hide HB27tile04_09
        hide HB27tile05_09
        hide HB28tile01_06
        hide HB28tile02_06
        hide HB28tile03_06
        hide HB28tile04_06
        hide HB28tile04_07
        hide HB28tile04_08
        hide HB28tile04_09
        hide HB28tile05_09
        
    if nand1in3 == True:
        if and1in1 == True:
            image HB29tile01_06 = "r_g.png"
            show HB29tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB29tile02_06 = "g_vertical.png"
            show HB29tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB29tile03_06 = "g_vertical.png"
            show HB29tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB29tile04_06 = "g_t_up.png"
            image HB29tile04_07 = "g_horizontal.png"
            image HB29tile04_08 = "g_horizontal.png"
            image HB29tile04_09 = "g_elbow_bl.png"
            show HB29tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB29tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB29tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB29tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB29tile05_09 = "g_y.png"    
            show HB29tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB29tile01_06
            hide HB29tile02_06
            hide HB29tile03_06
            hide HB29tile04_06
            hide HB29tile04_07
            hide HB29tile04_08
            hide HB29tile04_09
            hide HB29tile05_09

        if xor1in1 == True or xor2in1 == True:
            image HB210tile01_06 = "g_r.png"
            show HB210tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB210tile02_06 = "r_vertical.png"
            show HB210tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB210tile03_06 = "r_vertical.png"
            show HB210tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB210tile04_06 = "r_t_up.png"
            image HB210tile04_07 = "r_horizontal.png"
            image HB210tile04_08 = "r_horizontal.png"
            image HB210tile04_09 = "r_elbow_bl.png"
            show HB210tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB210tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB210tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB210tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB210tile05_09 = "r_y.png"    
            show HB210tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB210tile01_06
            hide HB210tile02_06
            hide HB210tile03_06
            hide HB210tile04_06
            hide HB210tile04_07
            hide HB210tile04_08
            hide HB210tile04_09
            hide HB210tile05_09

    else:
        hide HB29tile01_06
        hide HB29tile02_06
        hide HB29tile03_06
        hide HB29tile04_06
        hide HB29tile04_07
        hide HB29tile04_08
        hide HB29tile04_09
        hide HB29tile05_09  
        hide HB210tile01_06
        hide HB210tile02_06
        hide HB210tile03_06
        hide HB210tile04_06
        hide HB210tile04_07
        hide HB210tile04_08
        hide HB210tile04_09
        hide HB210tile05_09
            
    if xor1in3 == True or xor2in3 == True:
        if nand1in1 == True:
            image HB211tile01_06 = "r_g.png"
            show HB211tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB211tile02_06 = "g_vertical.png"
            show HB211tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB211tile03_06 = "g_vertical.png"
            show HB211tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB211tile04_06 = "g_t_up.png"
            image HB211tile04_07 = "g_horizontal.png"
            image HB211tile04_08 = "g_horizontal.png"
            image HB211tile04_09 = "g_elbow_bl.png"
            show HB211tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB211tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB211tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB211tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB211tile05_09 = "g_y.png"    
            show HB211tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB211tile01_06
            hide HB211tile02_06
            hide HB211tile03_06
            hide HB211tile04_06
            hide HB211tile04_07
            hide HB211tile04_08
            hide HB211tile04_09
            hide HB211tile05_09

        if and1in1 == True:
            image HB212tile01_06 = "r_g.png"
            show HB212tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB212tile02_06 = "g_vertical.png"
            show HB212tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB212tile03_06 = "g_vertical.png"
            show HB212tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB212tile04_06 = "g_t_up.png"
            image HB212tile04_07 = "g_horizontal.png"
            image HB212tile04_08 = "g_horizontal.png"
            image HB212tile04_09 = "g_elbow_bl.png"
            show HB212tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB212tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB212tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB212tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB212tile05_09 = "g_y.png"    
            show HB212tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB212tile01_06
            hide HB212tile02_06
            hide HB212tile03_06
            hide HB212tile04_06
            hide HB212tile04_07
            hide HB212tile04_08
            hide HB212tile04_09
            hide HB212tile05_09
        if xor1in1 == True or xor2in1 == True:
            image HB225tile01_06 = "g_r.png"
            show HB225tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
            image HB225tile02_06 = "r_vertical.png"
            show HB225tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
            image HB225tile03_06 = "r_vertical.png"
            show HB225tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            image HB225tile04_06 = "r_t_up.png"
            image HB225tile04_07 = "r_horizontal.png"
            image HB225tile04_08 = "r_horizontal.png"
            image HB225tile04_09 = "r_elbow_bl.png"
            show HB225tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show HB225tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
            show HB225tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
            show HB225tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
            image HB225tile05_09 = "r_y.png"    
            show HB225tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        else:
            hide HB225tile01_06
            hide HB225tile02_06
            hide HB225tile03_06
            hide HB225tile04_06
            hide HB225tile04_07
            hide HB225tile04_08
            hide HB225tile04_09
            hide HB225tile05_09

    else:
        hide HB211tile01_06
        hide HB211tile02_06
        hide HB211tile03_06
        hide HB211tile04_06
        hide HB211tile04_07
        hide HB211tile04_08
        hide HB211tile04_09
        hide HB211tile05_09  
        hide HB212tile01_06
        hide HB212tile02_06
        hide HB212tile03_06
        hide HB212tile04_06
        hide HB212tile04_07
        hide HB212tile04_08
        hide HB212tile04_09
        hide HB212tile05_09
        hide HB225tile01_06
        hide HB225tile02_06
        hide HB225tile03_06
        hide HB225tile04_06
        hide HB225tile04_07
        hide HB225tile04_08
        hide HB225tile04_09
        hide HB225tile05_09
            
    if nand1in1 == True and (xor1in3 == True or xor2in3 == True):
        if and1in4 == True:
            image HB213tile01_08 = "r_horizontal.png"
            image HB213tile01_09 = "r_horizontal.png"
            image HB213tile01_10= "r_horizontal.png"
            image HB213tile01_11 = "r_elbow_bl.png"
            show HB213tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB213tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB213tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB213tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB213tile02_11 = "r_vertical.png"    
            show HB213tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB213tile03_11 = "r_y.png"
            show HB213tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB213tile01_08
            hide HB213tile01_09
            hide HB213tile01_10
            hide HB213tile01_11
            hide HB213tile02_11
            hide HB213tile03_11
    else:
        hide HB213tile01_08
        hide HB213tile01_09
        hide HB213tile01_10
        hide HB213tile01_11
        hide HB213tile02_11
        hide HB213tile03_11
        
    if (xor1in1 == True or xor2in1 == True) and (xor1in3 == True or xor2in3 == True):
        if and1in4 == True:
            image HB223tile01_08 = "r_horizontal.png"
            image HB223tile01_09 = "r_horizontal.png"
            image HB223tile01_10= "r_horizontal.png"
            image HB223tile01_11 = "r_elbow_bl.png"
            show HB223tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB223tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB223tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB223tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB223tile02_11 = "r_vertical.png"    
            show HB223tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB223tile03_11 = "r_y.png"
            show HB223tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB223tile01_08
            hide HB223tile01_09
            hide HB223tile01_10
            hide HB223tile01_11
            hide HB223tile02_11
            hide HB223tile03_11
    else:
        hide HB223tile01_08
        hide HB223tile01_09
        hide HB223tile01_10
        hide HB223tile01_11
        hide HB223tile02_11
        hide HB223tile03_11

            
    if nand1in3 == True and (xor1in1 == True or xor2in1 == True):
        if and1in4 == True:
            image HB214tile01_08 = "r_horizontal.png"
            image HB214tile01_09 = "r_horizontal.png"
            image HB214tile01_10= "r_horizontal.png"
            image HB214tile01_11 = "r_elbow_bl.png"
            show HB214tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB214tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB214tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB214tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB214tile02_11 = "r_vertical.png"    
            show HB214tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB214tile03_11 = "r_y.png"
            show HB214tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB214tile01_08
            hide HB214tile01_09
            hide HB214tile01_10
            hide HB214tile01_11
            hide HB214tile02_11
            hide HB214tile03_11
    else:
        hide HB214tile01_08
        hide HB214tile01_09
        hide HB214tile01_10
        hide HB214tile01_11
        hide HB214tile02_11
        hide HB214tile03_11
            
    if and1in1 == True and (xor1in3 == True or xor2in3 == True):
        if nand1in4 == True:
            image HB215tile01_08 = "g_horizontal.png"
            image HB215tile01_09 = "g_horizontal.png"
            image HB215tile01_10= "g_horizontal.png"
            image HB215tile01_11 = "g_elbow_bl.png"
            show HB215tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB215tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB215tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB215tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB215tile02_11 = "g_vertical.png"    
            show HB215tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB215tile03_11 = "g_y.png"
            show HB215tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB215tile01_08
            hide HB215tile01_09
            hide HB215tile01_10
            hide HB215tile01_11
            hide HB215tile02_11
            hide HB215tile03_11
    else:
        hide HB215tile01_08
        hide HB215tile01_09
        hide HB215tile01_10
        hide HB215tile01_11
        hide HB215tile02_11
        hide HB215tile03_11
            
    if and1in3 == True and (xor1in1 == True or xor2in1 == True):
        if nand1in4 == True:
            image HB216tile01_08 = "r_horizontal.png"
            image HB216tile01_09 = "r_horizontal.png"
            image HB216tile01_10= "r_horizontal.png"
            image HB216tile01_11 = "r_elbow_bl.png"
            show HB216tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB216tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB216tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB216tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB216tile02_11 = "r_vertical.png"    
            show HB216tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB216tile03_11 = "r_y.png"
            show HB216tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB216tile01_08
            hide HB216tile01_09
            hide HB216tile01_10
            hide HB216tile01_11
            hide HB216tile02_11
            hide HB216tile03_11
    else:
        hide HB216tile01_08
        hide HB216tile01_09
        hide HB216tile01_10
        hide HB216tile01_11
        hide HB216tile02_11
        hide HB216tile03_11
        
    if (xor1in1 == True or xor2in1 == True) and (xor1in3 == True or xor2in3 == True):
        if nand1in4 == True:
            image HB224tile01_08 = "r_horizontal.png"
            image HB224tile01_09 = "r_horizontal.png"
            image HB224tile01_10= "r_horizontal.png"
            image HB224tile01_11 = "r_elbow_bl.png"
            show HB224tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB224tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB224tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB224tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB224tile02_11 = "r_vertical.png"    
            show HB224tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB224tile03_11 = "r_y.png"
            show HB224tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB224tile01_08
            hide HB224tile01_09
            hide HB224tile01_10
            hide HB224tile01_11
            hide HB224tile02_11
            hide HB224tile03_11
    else:
        hide HB224tile01_08
        hide HB224tile01_09
        hide HB224tile01_10
        hide HB224tile01_11
        hide HB224tile02_11
        hide HB224tile03_11

            
    if and1in3 == True and nand1in1 == True:
        if (xor1in4 == True or xor2in4 == True):
            image HB217tile01_08 = "r_horizontal.png"
            image HB217tile01_09 = "r_horizontal.png"
            image HB217tile01_10= "r_horizontal.png"
            image HB217tile01_11 = "r_elbow_bl.png"
            show HB217tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB217tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB217tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB217tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB217tile02_11 = "r_vertical.png"    
            show HB217tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB217tile03_11 = "r_y.png"
            show HB217tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB217tile01_08
            hide HB217tile01_09
            hide HB217tile01_10
            hide HB217tile01_11
            hide HB217tile02_11
            hide HB217tile03_11
    else:
        hide HB217tile01_08
        hide HB217tile01_09
        hide HB217tile01_10
        hide HB217tile01_11
        hide HB217tile02_11
        hide HB217tile03_11

    if and1in1 == True and nand1in3 == True:
        if (xor1in4 == True or xor2in4 == True):
            image HB218tile01_08 = "g_horizontal.png"
            image HB218tile01_09 = "g_horizontal.png"
            image HB218tile01_10= "g_horizontal.png"
            image HB218tile01_11 = "g_elbow_bl.png"
            show HB218tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB218tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB218tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB218tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB218tile02_11 = "g_vertical.png"    
            show HB218tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB218tile03_11 = "g_y.png"
            show HB218tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB218tile01_08
            hide HB218tile01_09
            hide HB218tile01_10
            hide HB218tile01_11
            hide HB218tile02_11
            hide HB218tile03_11
    else:
        hide HB218tile01_08
        hide HB218tile01_09
        hide HB218tile01_10
        hide HB218tile01_11
        hide HB218tile02_11
        hide HB218tile03_11
        
    if and1in3 == True and (xor1in1 == True or xor2in1 == True):
        if (xor1in4 == True or xor2in4 == True):
            image HB219tile01_08 = "g_horizontal.png"
            image HB219tile01_09 = "g_horizontal.png"
            image HB219tile01_10= "g_horizontal.png"
            image HB219tile01_11 = "g_elbow_bl.png"
            show HB219tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB219tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB219tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB219tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB219tile02_11 = "g_vertical.png"    
            show HB219tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB219tile03_11 = "g_y.png"
            show HB219tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB219tile01_08
            hide HB219tile01_09
            hide HB219tile01_10
            hide HB219tile01_11
            hide HB219tile02_11
            hide HB219tile03_11
    else:
        hide HB219tile01_08
        hide HB219tile01_09
        hide HB219tile01_10
        hide HB219tile01_11
        hide HB219tile02_11
        hide HB219tile03_11

        
    if (xor1in1 == True or xor2in1 == True) and nand1in3 == True:
        if (xor1in4 == True or xor2in4 == True):
            image HB220tile01_08 = "g_horizontal.png"
            image HB220tile01_09 = "g_horizontal.png"
            image HB220tile01_10= "g_horizontal.png"
            image HB220tile01_11 = "g_elbow_bl.png"
            show HB220tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB220tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB220tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB220tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB220tile02_11 = "g_vertical.png"    
            show HB220tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB220tile03_11 = "g_y.png"
            show HB220tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB220tile01_08
            hide HB220tile01_09
            hide HB220tile01_10
            hide HB220tile01_11
            hide HB220tile02_11
            hide HB220tile03_11
    else:
        hide HB220tile01_08
        hide HB220tile01_09
        hide HB220tile01_10
        hide HB220tile01_11
        hide HB220tile02_11
        hide HB220tile03_11

    if and1in1 == True and (xor1in3 == True or xor2in3 == True):
        if (xor1in4 == True or xor2in4 == True):
            image HB221tile01_08 = "g_horizontal.png"
            image HB221tile01_09 = "g_horizontal.png"
            image HB221tile01_10= "g_horizontal.png"
            image HB221tile01_11 = "g_elbow_bl.png"
            show HB221tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB221tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB221tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB221tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB221tile02_11 = "g_vertical.png"    
            show HB221tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB221tile03_11 = "g_y.png"
            show HB221tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB221tile01_08
            hide HB221tile01_09
            hide HB221tile01_10
            hide HB221tile01_11
            hide HB221tile02_11
            hide HB221tile03_11
    else:
        hide HB221tile01_08
        hide HB221tile01_09
        hide HB221tile01_10
        hide HB221tile01_11
        hide HB221tile02_11
        hide HB221tile03_11

        
    if (xor1in3 == True or xor2in3 == True) and nand1in1 == True:
        if (xor1in4 == True or xor2in4 == True):
            image HB222tile01_08 = "g_horizontal.png"
            image HB222tile01_09 = "g_horizontal.png"
            image HB222tile01_10= "g_horizontal.png"
            image HB222tile01_11 = "g_elbow_bl.png"
            show HB222tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
            show HB222tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
            show HB222tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
            show HB222tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
            image HB222tile02_11 = "g_vertical.png"    
            show HB222tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image HB222tile03_11 = "g_y.png"
            show HB222tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        else:
            hide HB222tile01_08
            hide HB222tile01_09
            hide HB222tile01_10
            hide HB222tile01_11
            hide HB222tile02_11
            hide HB222tile03_11
    else:
        hide HB222tile01_08
        hide HB222tile01_09
        hide HB222tile01_10
        hide HB222tile01_11
        hide HB222tile02_11
        hide HB222tile03_11

    if and1in1 == True and nand1in2 == True and (xor1in3 == True or xor2in3 ==True):
        image HB241tile04_11 = "g_vertical.png"
        show HB241tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB241tile05_11 = "g_elbow_tl.png"
        show HB241tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB241tile05_09 = "g_r.png"
        show HB241tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0) 
        image HB241tile03_11 = "y_g.png"
        show HB241tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB241tile04_11
        hide HB241tile05_11
        hide HB241tile05_09
        hide HB241tile03_11
        
    if and1in2 == True and nand1in1 == True and (xor1in3 == True or xor2in3 ==True):
        image HB242tile04_11 = "g_vertical.png"
        show HB242tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB242tile05_11 = "g_elbow_tl.png"
        show HB242tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB242tile05_09 = "g_g.png"
        show HB242tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB242tile03_11 = "y_g.png"
        show HB242tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB242tile04_11
        hide HB242tile05_11
        hide HB242tile05_09  
        hide HB242tile03_11
        
    if and1in3 == True and nand1in2 == True and (xor1in1 == True or xor2in1 ==True):
        image HB243tile04_11 = "g_vertical.png"
        show HB243tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB243tile05_11 = "g_elbow_tl.png"
        show HB243tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB243tile05_09 = "g_r.png"
        show HB243tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB243tile03_11 = "y_g.png"
        show HB243tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB243tile04_11
        hide HB243tile05_11
        hide HB243tile05_09
        hide HB243tile03_11
        
    if and1in3 == True and nand1in1 == True and (xor1in2 == True or xor2in2 ==True):
        image HB244tile04_11 = "g_vertical.png"
        show HB244tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB244tile05_11 = "g_elbow_tl.png"
        show HB244tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB244tile05_09 = "r_g.png"
        show HB244tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB244tile03_11 = "y_g.png"
        show HB244tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB244tile04_11
        hide HB244tile05_11
        hide HB244tile05_09
        hide HB244tile03_11
        
    if and1in1 == True and nand1in3 == True and (xor1in2 == True or xor2in2 ==True):
        image HB245tile04_11 = "g_vertical.png"
        show HB245tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB245tile05_11 = "g_elbow_tl.png"
        show HB245tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB245tile05_09 = "g_g.png"
        show HB245tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB245tile03_11 = "y_g.png"
        show HB245tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB245tile04_11
        hide HB245tile05_11
        hide HB245tile05_09
        hide HB245tile03_11
    
    if and1in2 == True and nand1in3 == True and (xor1in1 == True or xor2in1 ==True):
        image HB246tile04_11 = "g_vertical.png"
        show HB246tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB246tile05_11 = "g_elbow_tl.png"
        show HB246tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB246tile05_09 = "r_g.png"
        show HB246tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB246tile03_11 = "y_g.png"
        show HB246tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB246tile04_11
        hide HB246tile05_11
        hide HB246tile05_09
        hide HB246tile03_11
        
    if and1in2 == True and (xor1in3 == True or xor2in3 ==True) and (xor1in1 == True or xor2in1 ==True):
        image HB252tile04_11 = "g_vertical.png"
        show HB252tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB252tile05_11 = "g_elbow_tl.png"
        show HB252tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB252tile05_09 = "r_g.png"
        show HB252tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB252tile03_11 = "y_g.png"
        show HB252tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB252tile04_11
        hide HB252tile05_11
        hide HB252tile05_09
        hide HB252tile03_11

        
    if (xor1in2 == True or xor2in2 ==True) and nand1in3 == True and (xor1in1 == True or xor2in1 ==True):
        image HB251tile04_11 = "g_vertical.png"
        show HB251tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB251tile05_11 = "g_elbow_tl.png"
        show HB251tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB251tile05_09 = "r_g.png"
        show HB251tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB251tile03_11 = "y_g.png"
        show HB251tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB251tile04_11
        hide HB251tile05_11
        hide HB251tile05_09
        hide HB251tile03_11

    if and1in3 == True and (xor1in2 == True or xor2in2 ==True) and (xor1in1 == True or xor2in1 ==True):
        image HB250tile04_11 = "g_vertical.png"
        show HB250tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB250tile05_11 = "g_elbow_tl.png"
        show HB250tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB250tile05_09 = "g_g.png"
        show HB250tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB250tile03_11 = "y_g.png"
        show HB250tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB250tile04_11
        hide HB250tile05_11
        hide HB250tile05_09
        hide HB250tile03_11

        
    if (xor1in3 == True or xor2in3 ==True) and nand1in2 == True and (xor1in1 == True or xor2in1 ==True):
        image HB249tile04_11 = "r_vertical.png"
        show HB249tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB249tile05_11 = "r_elbow_tl.png"
        show HB249tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB249tile05_09 = "r_r.png"
        show HB249tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB249tile03_11 = "y_r.png"
        show HB249tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB249tile04_11
        hide HB249tile05_11
        hide HB249tile05_09
        hide HB249tile03_11

        
    if and1in1 == True and (xor1in2 == True or xor2in2 ==True) and (xor1in3 == True or xor2in3 ==True):
        image HB248tile04_11 = "g_vertical.png"
        show HB248tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB248tile05_11 = "g_elbow_tl.png"
        show HB248tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB248tile05_09 = "g_g.png"
        show HB248tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB248tile03_11 = "y_g.png"
        show HB248tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB248tile04_11
        hide HB248tile05_11
        hide HB248tile05_09
        hide HB248tile03_11

        
    if (xor1in3 == True or xor2in3 ==True) and nand1in1 == True and (xor1in2 == True or xor2in2 ==True):
        image HB247tile04_11 = "g_vertical.png"
        show HB247tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
        image HB247tile05_11 = "g_elbow_tl.png"
        show HB247tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        image HB247tile05_09 = "g_g.png"
        show HB247tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        image HB247tile03_11 = "y_g.png"
        show HB247tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB247tile04_11
        hide HB247tile05_11
        hide HB247tile05_09
        hide HB247tile03_11

        
    if and1in1 == True and nand1in2 == True and (xor1in3 == True or xor2in3 == True) and ( xor1in4 == True or xor2in4): 
        image HB229tile03_13 = "r_horizontal.png"
        show HB229tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB229tile03_11 = "g_g.png"
        show HB229tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB229tile03_13
        hide HB229tile03_11
        
    if and1in1 == True and nand1in3 == True and (xor1in2 == True or xor2in2 == True) and ( xor1in4 == True or xor2in4): 
        image HB230tile03_13 = "r_horizontal.png"
        show HB230tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB230tile03_11 = "g_g.png"
        show HB230tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB230tile03_13
        hide HB230tile03_11
        
    if and1in1 == True and nand1in4 == True and (xor1in3 == True or xor2in3 == True) and ( xor1in2 == True or xor2in2): 
        image HB231tile03_13 = "r_horizontal.png"
        show HB231tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB231tile03_11 = "g_g.png"
        show HB231tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB231tile03_13
        hide HB231tile03_11 

    if and1in3 == True and nand1in1 == True and (xor1in2 == True or xor2in2 == True) and ( xor1in4 == True or xor2in4):
        image HB232tile03_13 = "r_horizontal.png"
        show HB232tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB232tile03_11 = "r_g.png"
        show HB232tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB232tile03_13
        hide HB232tile03_11
        
    if and1in3 == True and nand1in2 == True and (xor1in1 == True or xor2in1 == True) and ( xor1in4 == True or xor2in4): 
        image HB233tile03_13 = "r_horizontal.png"
        show HB233tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB233tile03_11 = "g_g.png"
        show HB233tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB233tile03_13
        hide HB233tile03_11
        
    if and1in3 == True and nand1in4 == True and (xor1in1 == True or xor2in1 == True) and ( xor1in2 == True or xor2in2): 
        image HB234tile03_13 = "r_horizontal.png"
        show HB234tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB234tile03_11 = "r_g.png"
        show HB234tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB234tile03_13
        hide HB234tile03_11

    if and1in4 == True and nand1in1 == True and (xor1in3 == True or xor2in3 == True) and ( xor1in2 == True or xor2in2):
        image HB235tile03_13 = "r_horizontal.png"
        show HB235tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB235tile03_11 = "r_g.png"
        show HB235tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB235tile03_13
        hide HB235tile03_11
        
    if and1in4 == True and nand1in2 == True and (xor1in1 == True or xor2in1 == True) and ( xor1in3 == True or xor2in3): 
        image HB236tile03_13 = "g_horizontal.png"
        show HB236tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB236tile03_11 = "r_r.png"
        show HB236tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB236tile03_13
        hide HB236tile03_11
        
    if and1in4 == True and nand1in3 == True and (xor1in1 == True or xor2in1 == True) and ( xor1in2 == True or xor2in2): 
        image HB237tile03_13 = "r_horizontal.png"
        show HB237tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB237tile03_11 = "r_g.png"
        show HB237tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB237tile03_13
        hide HB237tile03_11
  
    if and1in2 == True and nand1in1 == True and (xor1in3 == True or xor2in3 == True) and ( xor1in4 == True or xor2in4): 
        image HB238tile03_13 = "r_horizontal.png"
        show HB238tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB238tile03_11 = "g_g.png"
        show HB238tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB238tile03_13
        hide HB238tile03_11
        
    if and1in2 == True and nand1in3 == True and (xor1in1 == True or xor2in1 == True) and ( xor1in4 == True or xor2in4): 
        image HB239tile03_13 = "r_horizontal.png"
        show HB239tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB239tile03_11 = "g_g.png"
        show HB239tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB239tile03_13
        hide HB239tile03_11
        
    if and1in2 == True and nand1in4 == True and (xor1in3 == True or xor2in3 == True) and ( xor1in1 == True or xor2in1): 
        image HB240tile03_13 = "r_horizontal.png"
        show HB240tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
        image HB240tile03_11 = "r_g.png"
        show HB240tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    else:
        hide HB240tile03_13
        hide HB240tile03_11
   




#win conditions ********
    if and1in4 == True and nand1in2 == True and (xor1in1 == True or xor2in1 == True) and ( xor1in3 == True or xor2in3):         
        image MB1260tile02_09 = "xor_Gate.png"
        show MB1260tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image MB1260tile02_10 = "xor_Gate.png"
        show MB1260tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image MB1160tile07_02 = "and_Gate.png"
        show MB1160tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MB1160tile07_08 = "nand_Gate.png"
        show MB1160tile07_08 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MB1160end2 = "light_g_on.png"
        show MB1160end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        "game"
        jump start

  
    if attempts == 0:
        image MB1260tile02_09 = "xor_Gate.png"
        show MB1260tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
        image MB1260tile02_10 = "xor_Gate.png"
        show MB1260tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
        image MB1260tile07_02 = "and_Gate.png"
        show MB1260tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MB1260tile07_08 = "nand_Gate.png"
        show MB1260tile07_08 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)

        "you lose try again"
        jump start
    
    jump gamefileHB2

screen logicgatesHB2:
    
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
                drag_name "nand_gate"
                child "nand_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nand1x ypos nand1y
                
            #nand gate
            drag:
                drag_name "xor_gate1"
                child "xor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos xor1x ypos xor1y
                
            drag:
                drag_name "xor_gate2"
                child "xor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos xor2x ypos xor2y

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
                drag_name "gate slot four"
                child "cover.png"
                draggable False
                xpos gate4x ypos gate4y
                
            drag:
                drag_name "and return"
                child "cover.png"
                draggable False
                xpos 698 ypos 88
           
            drag:
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88
                
            drag:
                drag_name "xor return"
                child "cover.png"
                draggable False
                xpos 1298 ypos 88
