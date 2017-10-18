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

label logicGate_mediumA1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
    image MA1tile01_00 = "r_horizontal.png"
    image MA1tile01_01 = "r_elbow_bl.png"
    
    show MA1tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MA1tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image MA1tile02_01 = "r_r.png"
    image MA1tile02_02 = "NOR_Gate_blue.png"
    image MA1tile02_03 = "g_horizontal.png"
    image MA1tile02_04 = "g_elbow_bl.png"
    
    show MA1tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show MA1tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show MA1tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show MA1tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MA1tile03_00 = "r_horizontal.png"
    image MA1tile03_01 = "r_elbow_tl.png"
    image MA1tile03_04 = "g_vertical.png"
    
    show MA1tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MA1tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MA1tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MA1tile04_04 = "g_vertical.png"
    show MA1tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MA1tile05_00 = "g_elbow_bl.png"
    image MA1tile05_04 = "g_g.png"
    image MA1tile05_05 = "NAND_Gate_blue.png"
    image MA1tile05_06 = "r_horizontal.png"
    image MA1tile05_07 = "r_elbow_bl.png"
    
    show MA1tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MA1tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show MA1tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show MA1tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show MA1tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image MA1tile06_00 = "g_elbow_tr.png"
    image MA1tile06_01 = "g_t_down.png"
    image MA1tile06_02 = "g_horizontal.png"
    image MA1tile06_03 = "g_horizontal.png"
    image MA1tile06_04 = "g_elbow_tl.png"
    image MA1tile06_07 = "r_vertical.png"
    
    show MA1tile06_00 at Position(xpos = 436, xanchor = 0, ypos = 683, yanchor = 0)
    show MA1tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show MA1tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MA1tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MA1tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show MA1tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image tile07_00 = "g_elbow_bl.png"
    image tile07_01 = "g_vertical.png"
    image tile07_07 = "r_r.png"
    image tile07_08 = "NONE_Gate.png"
    image tile07_09 = "y_horizontal.png"
    image tile07_10 = "y_horizontal.png"
    image tile07_11 = "y_elbow_bl.png"
    image tile07_13 = "y_elbow_br.png"
    
    show tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image tile08_00 = "g_vertical.png"
    image tile08_01 = "g_g.png"
    image tile08_02 = "NAND_Gate_blue.png"
    image tile08_03 = "r_horizontal.png"
    image tile08_04 = "r_horizontal.png"
    image tile08_05 = "r_horizontal.png"
    image tile08_06 = "r_t_down.png"
    image tile08_07 = "r_elbow_tl.png"
    image tile08_11 = "y_r.png"
    image tile08_12 = "NONE_Gate.png"
    image tile08_13 = "y_elbow_tl.png"
    
    show tile08_00 at Position(xpos = 436, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_01 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_02 at Position(xpos = 586, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_12 at Position(xpos = 1336, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_13 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
    
    #row 9
    image tile09_00 = "g_elbow_tr.png"
    image tile09_01 = "g_elbow_tl.png"
    image tile09_06 = "r_elbow_tr.png"
    image tile09_07 = "r_horizontal.png"
    image tile09_08 = "r_horizontal.png"
    image tile09_09 = "r_horizontal.png"
    image tile09_10 = "r_horizontal.png"
    image tile09_11 = "r_elbow_tl.png"
    
    show tile09_00 at Position(xpos = 436, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_01 at Position(xpos = 511, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_06 at Position(xpos = 886, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_07 at Position(xpos = 961, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_08 at Position(xpos = 1036, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_09 at Position(xpos = 1111, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_10 at Position(xpos = 1186, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_11 at Position(xpos = 1261, xanchor = 0, ypos = 908, yanchor = 0)

    #start points
    image MA1start1 = "light_r_on.png"
    show MA1start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image MA1start2 = "light_r_on.png"
    show MA1start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image MA1start3 = "light_g_on.png"
    show MA1start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image MA1start4 = "light_g_on.png"
    show MA1start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these

    image MA1end4 = "light_g_off.png"
    show MA1end4 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)

    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    $ temp_slot = ""
    $ temp_gate = ""

    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
    $ nor1x = 1148
    $ nor1y = 88
    
    #gate values
    $ gate1x = 1036
    $ gate1y = 758
    $ gate2x = 1336
    $ gate2y = 833

   
    # check conditons for locations
    $ and1in1 = False
    $ nor1in1 = False
    $ and1in2 = False
    $ nor1in2 = False


     
    #attempts for players
    $ attempts = 3
 
    jump gamefileMA1
    
    
label gamefileMA1:
    
    #calls game screen
    call screen logicGatesMA1
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nor1in1 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in1 = False

            #sets values for checks
            $ and1x = gate1x
            $ and1y = gate1y
            $ and1in1 = True
            $ and1in2 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nor1in2 == True:
                $ nor1x = 1148
                $ nor1y = 88
                $ nor1in2 = False

            #sets values for checks
            $ and1x = gate2x
            $ and1y = gate2y
            $ and1in2 = True
            $ and1in1 = False
        
        if slot_name == "and return":
            $ and1x = 698
            $ and1y = 88
            $ and1in2 = False
            $ and1in1 = False
            
     #or gate section **********************************************************************       
    if gate_name == "nor_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False

            #sets values for checks
            $ nor1x = gate1x
            $ nor1y = gate1y
            $ nor1in1 = True
            $ nor1in2 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in2 = False

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
            if slot_name == "nor return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "nor_gate":
                $ attempts +=1
            if slot_name == "nor return" and gate_name == "and_gate":
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
        image MA11tile07_09 = "r_horizontal.png"
        image MA11tile07_10 = "r_horizontal.png"
        image MA11tile07_11 = "r_elbow_bl.png"
        show MA11tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show MA11tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        show MA11tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
        image MA11tile08_11 = "r_r.png"
        show MA11tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
    
    if and1in1 == False:
        hide MA11tile07_09
        hide MA11tile07_10
        hide MA11tile07_11
        hide MA11tile08_11

        
    if nor1in1 == True:
        image MA13tile07_09 = "g_horizontal.png"
        image MA13tile07_10 = "g_horizontal.png"
        image MA13tile07_11 = "g_elbow_bl.png"
        show MA13tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show MA13tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
        show MA13tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
        image MA13tile08_11 = "g_r.png"
        show MA13tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
        
    if nor1in1 == False:
        hide MA13tile07_09
        hide MA13tile07_10
        hide MA13tile07_11
        hide MA13tile08_11
        
    if and1in2 == True:
        if nor1in1 == True:
            image MA12tile08_13 = "r_elbow_tl.png"
            show MA12tile08_13 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
            image MA12tile07_13 = "r_elbow_br.png"
            show MA12tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)

    if and1in2 == False:
        hide MA12tile08_13
        hide MA12tile07_13
    if nor1in2 == True:
        if and1in1 == True:
            image MA14tile08_13 = "g_elbow_tl.png"
            show MA14tile08_13 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
            image MA14tile07_13 = "g_elbow_br.png"
            show MA14tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
            
    if nor1in2 == False:
        hide MA14tile08_13
        hide MA14tile07_13

        
#win conditions ********
    if and1in1 == True and nor1in2 == True: 
        image MA112tile07_02 = "and_Gate.png"
        show MA112tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MA112tile07_08 = "nor_Gate.png"
        show MA112tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        image MA18end2 = "light_g_on.png"
        show MA18end2 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        $lgMedA_solved = True
        jump lgMed_win

        
    if attempts == 0:
        image MA111tile07_02 = "and_Gate.png"
        show MA111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image MA111tile07_08 = "nor_Gate.png"
        show MA111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        $lgMed_attempts +=1
        jump lgMed_lose
    
    jump gamefileMA1

screen logicGatesMA1:
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
        action Jump("hints_lgMedA1")
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
                drag_name "nor_gate"
                child "nor_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nor1x ypos nor1y
                

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
                drag_name "and return"
                child "cover.png"
                draggable False
                xpos 698 ypos 88
           
            drag:
                drag_name "nor return"
                child "cover.png"
                draggable False
                xpos 1148 ypos 88
                
                