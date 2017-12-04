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

label logicGate_mediumA3:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
    image MA3tile00_08 = "g_elbow_br.png"
    image MA3tile00_09 = "g_horizontal.png"
    image MA3tile00_10 = "g_horizontal.png"
    image MA3tile00_11 = "g_elbow_bl.png"
    
    show MA3tile00_08 at Position(xpos = 1036, xanchor = 0, ypos = 233, yanchor = 0)
    show MA3tile00_09 at Position(xpos = 1111, xanchor = 0, ypos = 233, yanchor = 0)
    show MA3tile00_10 at Position(xpos = 1186, xanchor = 0, ypos = 233, yanchor = 0)
    show MA3tile00_11 at Position(xpos = 1261, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image MA3tile01_00 = "r_horizontal.png"
    image MA3tile01_01 = "r_elbow_bl.png"
    image MA3tile01_08 = "g_vertical.png"
    image MA3tile01_11 = "g_y.png"
    image MA3tile01_12 = "NONE_Gate.png"
    image MA3tile01_13 = "y_horizontal.png"
    
    show MA3tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show MA3tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show MA3tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
    show MA3tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
    show MA3tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
    show MA3tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image MA3tile02_01 = "r_r.png"
    image MA3tile02_02 = "NOR_Gate_blue.png"
    image MA3tile02_03 = "g_horizontal.png"
    image MA3tile02_04 = "g_horizontal.png"
    image MA3tile02_05 = "g_horizontal.png"
    image MA3tile02_06 = "g_horizontal.png"
    image MA3tile02_07 = "g_horizontal.png"
    image MA3tile02_08 = "g_t_left.png"
    image MA3tile02_11 = "y_vertical.png"
    
    show MA3tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show MA3tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image MA3tile03_00 = "r_horizontal.png"
    image MA3tile03_01 = "r_elbow_tl.png"
    image MA3tile03_02 = "g_elbow_br.png"
    image MA3tile03_03 = "g_horizontal.png"
    image MA3tile03_04 = "g_elbow_bl.png"
    image MA3tile03_08 = "g_g.png"
    image MA3tile03_09 = "NONE_Gate.png"
    image MA3tile03_10 = "y_horizontal.png"
    image MA3tile03_11 = "y_elbow_tl.png"
    
    show MA3tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show MA3tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image MA3tile04_02 = "g_vertical.png"
    image MA3tile04_04 = "g_r.png"
    image MA3tile04_05 = "OR_Gate_blue.png"
    image MA3tile04_06 = "g_horizontal.png"
    image MA3tile04_07 = "g_horizontal.png"
    image MA3tile04_08 = "g_elbow_tl.png"
    
    show MA3tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show MA3tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show MA3tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show MA3tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show MA3tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show MA3tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image MA3tile05_00 = "g_horizontal.png"
    image MA3tile05_01 = "g_t_down.png"
    image MA3tile05_02 = "g_elbow_tl.png"
    image MA3tile05_04 = "r_vertical.png"
    
    show MA3tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show MA3tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show MA3tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show MA3tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)

    
    #row 6
    image MA3tile06_01 = "g_g.png"
    image MA3tile06_02 = "NAND_Gate_blue.png"
    image MA3tile06_03 = "r_horizontal.png"
    image MA3tile06_04 = "r_elbow_tl.png"

    show MA3tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show MA3tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show MA3tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show MA3tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)

    
    #row 7 (row has a light)
    image MA3tile07_00 = "g_horizontal.png"
    image MA3tile07_01 = "g_elbow_tl.png"

    
    show MA3tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show MA3tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)


    #start points
    image MA3start1 = "light_r_on.png"
    show MA3start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image MA3start2 = "light_r_on.png"
    show MA3start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image MA3start3 = "light_g_on.png"
    show MA3start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image MA3start4 = "light_g_on.png"
    show MA3start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
    image MA3end1 = "light_g_off.png"
    show MA3end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)

    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
       
    #initial value assignment for dragables
    $ nand1x = 998
    $ nand1y = 88
    $ or1x = 848
    $ or1y = 88

    #gate values
    $ gate1x = 1111
    $ gate1y = 458
    $ gate2x = 1336
    $ gate2y = 308

    # check conditons for locations
    $ nand1in1 = False
    $ or1in1 = False
    $ nand1in2 = False
    $ or1in2 = False

    #attempts for players
    $ attempts = 3
 
    jump gamefileMA3
    
label gamefileMA3:
    
    #calls game screen
    call screen logicgatesMA3
    
    #the first logic gate *******************************************************************************
    if gate_name == "nand_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in1 = False
            #sets values for checks
            $ nand1x = gate1x
            $ nand1y = gate1y
            $ nand1in1 = True
            $ nand1in2 = False

            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if or1in2 == True:
                $ or1x = 848
                $ or1y = 88
                $ or1in2 = False
            #sets values for checks
            $ nand1x = gate2x
            $ nand1y = gate2y
            $ nand1in2 = True
            $ nand1in1 = False
            
        if slot_name == "nand return":
            $ nand1x = 998
            $ nand1y = 88
            $ nand1in2 = False
            $ nand1in1 = False

     #or gate section **********************************************************************       
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if nand1in1 == True:
               $ nand1x = 998
               $ nand1y = 88
               $ nand1in1 = False
            #sets values for checks
            $ or1x = gate1x
            $ or1y = gate1y
            $ or1in1 = True
            $ or1in2 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if nand1in2 == True:
               $ nand1x = 998
               $ nand1y = 88
               $ nand1in2 = False
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


    if temp_slot == "" and temp_gate == "" and slot_name != "null" and not(slot_name == "nand return" or slot_name == "or return"):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
       
    else:
       if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            if slot_name == "nand return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "or_gate":
                $ attempts +=1
            if slot_name == "or return" and gate_name == "nand_gate":
                $ attempts +=1
            if slot_name == "nand return" and gate_name == "or_gate":
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
    if nand1in1 == True:
        image MA31tile01_11 = "g_r.png"
        show MA31tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image MA31tile02_11 = "r_vertical.png"
        show MA31tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MA31tile03_10 = "r_horizontal.png"
        image MA31tile03_11 = "r_elbow_tl.png"
        show MA31tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show MA31tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)

    if nand1in1 == False:
        hide MA31tile01_11
        hide MA31tile02_11
        hide MA31tile03_10
        hide MA31tile03_11
        
    if nand1in2 == True and or1in1 == True:
        image MA32tile01_13 = "r_horizontal.png"
        show MA32tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        
    if nand1in2 == False or or1in1 == False: 
        hide MA32tile01_13
        
    if or1in1 == True:
        image MA33tile01_11 = "g_g.png"
        show MA33tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
        image MA33tile02_11 = "g_vertical.png"
        show MA33tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
        image MA33tile03_10 = "g_horizontal.png"
        image MA33tile03_11 = "g_elbow_tl.png"
        show MA33tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show MA33tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
        
    if or1in1 == False:    
        hide MA33tile01_11
        hide MA33tile02_11
        hide MA33tile03_10
        hide MA33tile03_11
        
    if or1in2 == False and nand1in1 == False:
        image MA34tile01_13 = "g_horizontal.png"
        show MA34tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
        
    if or1in2 == False or nand1in1 == False:
        hide MA34tile01_13

#win conditions ********
    if nand1in1 == True and or1in2 == True: 
        image MA35tile07_02 = "nand_Gate.png"
        show MA35tile07_02 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MA35tile07_08 = "or_Gate.png"
        show MA35tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        image MA3end2 = "light_g_on.png"
        show MA3end2 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
        queue sound lgWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgMedAWin
        $lgMedA_solved = True
        jump lgMed_win

    if attempts == 0:
        image MA36tile07_02 = "nand_Gate.png"
        show MA36tile07_02 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
        image MA36tile07_08 = "or_Gate.png"
        show MA36tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 3
            jump pg_lgMedALose
        $lgMed_attempts +=1
        jump lgMed_lose
    
    jump gamefileMA3

screen logicgatesMA3:
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
        action Jump("hints_lgMedA3")
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
                drag_name "nand_gate"
                child "NAND_Gate.png"
                droppable False
                dragged gate_dragged
                xpos nand1x ypos nand1y
                
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
                drag_name "nand return"
                child "cover.png"
                draggable False
                xpos 998 ypos 88
                                