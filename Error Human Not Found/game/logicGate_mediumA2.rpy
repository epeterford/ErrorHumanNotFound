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

label logicGate_mediumA2:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #row 0
    image MA2tile00_01 = "r_elbow_br.png"
    image MA2tile00_02= "r_horizontal.png"
    image MA2tile00_03 = "r_horizontal.png"
    image MA2tile00_04 = "r_elbow_bl.png"
    show MA2tile00_01 at Position(xpos = 511, xanchor = 0, ypos = 233, yanchor = 0)
    show MA2tile00_02 at Position(xpos = 586, xanchor = 0, ypos = 233, yanchor = 0)
    show MA2tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
    show MA2tile00_04 at Position(xpos = 736, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image MA2tile01_00 = "r_horizontal.png"
    image MA2tile01_01 = "r_elbow_tl.png"
    image MA2tile01_04 = "r_r.png"
    image MA2tile01_05 = "NAND_Gate_blue.png"
    image MA2tile01_06 = "g_horizontal.png"
    image MA2tile01_07 = "g_horizontal.png"
    image MA2tile01_08 = "g_horizontal.png"
    image MA2tile01_09 = "g_elbow_bl.png"
    show MA2tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show MA2tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image MA2tile02_04 = "r_vertical.png"
    image MA2tile02_05 = "g_elbow_br.png"
    image MA2tile02_06 = "g_elbow_bl.png"
    image MA2tile02_09 = "g_y.png"
    image MA2tile02_10 = "NONE_Gate.png"
    image MA2tile02_11 = "y_elbow_bl.png"
    show MA2tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show MA2tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show MA2tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show MA2tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
    show MA2tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
    show MA2tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MA2tile03_00 = "r_horizontal.png"
    image MA2tile03_01 = "r_horizontal.png"
    image MA2tile03_02 = "r_horizontal.png"
    image MA2tile03_03 = "r_horizontal.png"
    image MA2tile03_04 = "r_elbow_tl.png"
    image MA2tile03_05 = "g_vertical.png"
    image MA2tile03_06 = "g_y.png"
    image MA2tile03_07 = "NAND_Gate_blue.png"
    image MA2tile03_08 = "y_horizontal.png"
    image MA2tile03_09 = "y_elbow_tl.png"
    image MA2tile03_11 = "y_vertical.png"
    show MA2tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show MA2tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MA2tile04_05 = "g_vertical.png"
    image MA2tile04_06 = "y_vertical.png"
    image MA2tile04_11 = "y_vertical.png"
    show MA2tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show MA2tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show MA2tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MA2tile05_00 = "g_horizontal.png"
    image MA2tile05_01 = "g_t_down.png"
    image MA2tile05_02 = "g_horizontal.png"
    image MA2tile05_03 = "g_horizontal.png"
    image MA2tile05_04 = "g_horizontal.png"
    image MA2tile05_05 = "g_elbow_tl.png"
    image MA2tile05_06 = "y_vertical.png"
    image MA2tile05_11 = "y_vertical.png"
    show MA2tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show MA2tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image MA2tile06_01 = "g_r.png"
    image MA2tile06_02 = "NONE_Gate.png"
    image MA2tile06_03 = "y_horizontal.png"
    image MA2tile06_04 = "y_horizontal.png"
    image MA2tile06_05 = "y_horizontal.png"
    image MA2tile06_06 = "y_elbow_tl.png"
    image MA2tile06_11 = "y_vertical.png"
    show MA2tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show MA2tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MA2tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MA2tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show MA2tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show MA2tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show MA2tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image MA2tile07_00 = "r_horizontal.png"
    image MA2tile07_01 = "r_elbow_tl.png"
    image MA2tile07_11 = "y_elbow_tr.png"
    image MA2tile07_12 = "NOT_Gate.png"
    image MA2tile07_13 = "y_horizontal.png"
    show MA2tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show MA2tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show MA2tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    show MA2tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
    show MA2tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)

    #start points
    image start1 = "light_r_on.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start2 = "light_r_on.png"
    show start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image start3 = "light_g_on.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image start4 = "light_r_on.png"
    show start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image end4 = "light_g_off.png"
    show end4 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

    #initial value assignment for dragables
    $ nor1x = 1148
    $ nor1y = 88
    $ or1x = 848
    $ or1y = 88

    #gate values
    $ gate1x = 586
    $ gate1y = 683
    $ gate2x = 1186
    $ gate2y = 383

    # check conditons for locations
    $ nor1in1 = False
    $ or1in1 = False
    $ nor1in2 = False
    $ or1in2 = False

    #attempts for players
    $ attempts = 3
 
    jump gamefileMA2
    
label gamefileMA2:
    
    #calls game screen
    call screen logicGatesMA2
    
    #the first logic gate *******************************************************************************
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False

            #sets values for checks
            $ nor1x = gate1x
            $ nor1y = gate1y
            $ nor1in1 = True
            $ nor1in2 = False

        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
            #sets values for checks
            $ nor1x = gate2x
            $ nor1y = gate2y
            $ nor1in2 = True
            $ nor1in1 = False
            
        if slot_name == "nor return":
            $ nor1x = 1148
            $ nor1y = 88
            $ nor1in2 = False
            $ nor1in1 = False

     #or gate section **********************************************************************       
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nor1in1 == True:
                $ nor1x = 698
                $ nor1y = 88
                $ nor1in1 = False
                
            #sets values for checks
            $ or1x = gate1x
            $ or1y = gate1y
            $ or1in1 = True
            $ or1in2 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nor1in2 == True:
               $ nor1x = 698
               $ nor1y = 88
               $ nor1in2 = False

            #sets values for checks
            $ or1x = gate2x
            $ or1y = gate2y
            $ or1in2 = True
            $ or1in1 = False
            
        if slot_name == "or return":
            $ or1x = 848
            $ or1y = 88
            $ or1in2 = False
            $ or1in1 = False

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
            if slot_name == "nor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "nor_gate":
                $ attempts +=1                
            if slot_name == "nor return" and gate_name == "or_gate":
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
    if nor1in1 == True:
        image MA21tile02_09 = "g_g.png"
        show MA21tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image MA21tile03_06 = "g_r.png"
        show MA21tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        image MA21tile03_08 = "g_horizontal.png"
        image MA21tile03_09 = "g_elbow_tl.png"
        show MA21tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show MA21tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MA21tile04_06 = "r_vertical.png"
        show MA21tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        image MA21tile05_06 = "r_vertical.png"
        show MA21tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image MA21tile06_03 = "r_horizontal.png"
        image MA21tile06_04 = "r_horizontal.png"
        image MA21tile06_05 = "r_horizontal.png"
        image MA21tile06_06 = "r_elbow_tl.png"
        show MA21tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show MA21tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show MA21tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show MA21tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)

    if nor1in1 == False:
        hide MA21tile02_09
        hide MA21tile03_06
        hide MA21tile03_08
        hide MA21tile03_09
        hide MA21tile04_06
        hide MA21tile05_06
        hide MA21tile06_03
        hide MA21tile06_04
        hide MA21tile06_05
        hide MA21tile06_06

    if nor1in2 == True:
        if or1in1 == True:
            image MA22tile02_11 = "r_elbow_bl.png"
            show MA22tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image MA22tile03_11 = "r_vertical.png"
            show MA22tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MA22tile04_11 = "r_vertical.png"
            show MA22tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MA22tile05_11 = "r_vertical.png"
            show MA22tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MA22tile06_11 = "r_vertical.png"
            show MA22tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
            image MA22tile07_11 = "r_elbow_tr.png"
            image MA22tile07_13 = "g_horizontal.png"
            show MA22tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            show MA22tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
            
    if nor1in2 == False or or1in1 == False:
        hide MA22tile02_11
        hide MA22tile03_11
        hide MA22tile04_11
        hide MA22tile05_11
        hide MA22tile06_11
        hide MA22tile07_11
        hide MA22tile07_13
        
    if or1in1 == True:
        image MA23tile02_09 = "g_r.png"
        show MA23tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
        image MA23tile03_06 = "g_g.png"
        show MA23tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
        image MA23tile03_08 = "r_horizontal.png"
        image MA23tile03_09 = "r_elbow_tl.png"
        show MA23tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
        show MA23tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        image MA23tile04_06 = "g_vertical.png"
        show MA23tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
        image MA23tile05_06 = "g_vertical.png"
        show MA23tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
        image MA23tile06_03 = "g_horizontal.png"
        image MA23tile06_04 = "g_horizontal.png"
        image MA23tile06_05 = "g_horizontal.png"
        image MA23tile06_06 = "g_elbow_tl.png"
        show MA23tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
        show MA23tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
        show MA23tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
        show MA23tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)  
    
    if or1in1 == False:
        hide MA23tile02_09
        hide MA23tile03_06
        hide MA23tile03_08
        hide MA23tile03_09
        hide MA23tile04_06
        hide MA23tile05_06
        hide MA23tile06_03
        hide MA23tile06_04
        hide MA23tile06_05
        hide MA23tile06_06        
        
    if or1in2 == True:
        if nor1in1 == True:
            image MA24tile02_11 = "g_elbow_bl.png"
            show MA24tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
            image MA24tile03_11 = "g_vertical.png"
            show MA24tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
            image MA24tile04_11 = "g_vertical.png"
            show MA24tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
            image MA24tile05_11 = "g_vertical.png"
            show MA24tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
            image MA24tile06_11 = "g_vertical.png"
            show MA24tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
            image MA24tile07_11 = "g_elbow_tr.png"
            image MA24tile07_13 = "r_horizontal.png"
            show MA24tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
            show MA24tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)     
    
    if or1in2 == False or nor1in1 == False:
        hide MA24tile02_11
        hide MA24tile03_11
        hide MA24tile04_11
        hide MA24tile05_11
        hide MA24tile06_11
        hide MA24tile07_11
        hide MA24tile07_13

#win conditions ********
    if nor1in2 == True and or1in1 == True: 
        image MA299tile07_02 = "nor_Gate.png"
        show MA299tile07_02 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MA298tile07_08 = "or_Gate.png"
        show MA298tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image MA297end2 = "light_g_on.png"
        show MA297end2 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        $lgMedA_solved = True
        jump lgMed_win

    if attempts == 0:
        image MA297tile07_02 = "nor_Gate.png"
        show MA297tile07_02 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MA296tile07_08 = "or_Gate.png"
        show MA296tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        $lgMed_attempts +=1
        jump lgMed_lose
    
    jump gamefileMA2

screen logicGatesMA2:
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
        action Jump("hints_lgMedA2")
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
                drag_name "nor_gate"
                child "nor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nor1x ypos nor1y
                
            #or gates
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
                xpos gate1x ypos gate1y
           
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos gate2x ypos gate2y

            drag:
                drag_name "or return"
                child "cover.png"
                draggable False
                xpos 848 ypos 88
           
            drag:
                drag_name "nor return"
                child "cover.png"
                draggable False
                xpos 1148 ypos 88