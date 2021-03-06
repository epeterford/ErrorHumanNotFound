﻿      
label logicGate_easyB1:
    $config.skipping=None
    $renpy.block_rollback()
    $quick_menu = False
    #loads background
    scene bg Logic_Gate
   
    #row 1 (row has a light)
    image EB1tile15 = "r_horizontal.png"
    image EB1tile16 = "r_horizontal.png"
    image EB1tile17 = "r_horizontal.png"
    image EB1tile18 = "r_horizontal.png"
    image EB1tile19 = "r_elbow_bl.png"
   
    show EB1tile15 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show EB1tile16 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show EB1tile17 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show EB1tile18 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show EB1tile19 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image EB1tile33 = "r_g.png"
    image EB1tile34 = "NONE_Gate.png"
    image EB1tile35 = "y_horizontal.png"
    image EB1tile37 = "y_elbow_bl.png"

    show EB1tile33 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show EB1tile34 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show EB1tile35 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show EB1tile37 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image EB1tile47 = "g_vertical.png"
    image EB1tile51 = "y_g.png"
    image EB1tile52 = "AND_Gate_blue.png"
    image EB1tile53 = "y_horizontal.png"
    image EB1tile54 = "y_elbow_bl.png"
    image EB1tile55 = "y_elbow_br.png"
    image EB1tile56 = "y_horizontal.png"

    show EB1tile47 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show EB1tile51 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show EB1tile52 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show EB1tile53 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show EB1tile54 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show EB1tile55 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show EB1tile56 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image EB1tile60 = "g_elbow_br.png"
    image EB1tile61 = "g_elbow_tl.png"
    image EB1tile65 = "g_vertical.png"
    image EB1tile67 = "y_y.png"
    image EB1tile68 = "AND_Gate_blue.png"
    image EB1tile69 = "y_elbow_tl.png"
    
    show EB1tile60 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show EB1tile61 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show EB1tile65 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show EB1tile67 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show EB1tile68 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show EB1tile69 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image EB1tile71 = "g_horizontal.png"
    image EB1tile72 = "g_t_down.png"
    image EB1tile73 = "g_horizontal.png"
    image EB1tile74 = "g_t_left.png"
    image EB1tile78 = "g_vertical.png"
    image EB1tile80 = "y_elbow_br.png"
    image EB1tile81 = "y_elbow_tl.png"
    
    show EB1tile71 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show EB1tile72 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show EB1tile73 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show EB1tile74 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show EB1tile78 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show EB1tile80 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show EB1tile81 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image EB1tile87 = "g_vertical.png"
    image EB1tile89 = "g_g.png"
    image EB1tile90 = "AND_Gate_blue.png"
    image EB1tile91 = "g_horizontal.png"
    image EB1tile92 = "g_horizontal.png"
    image EB1tile93 = "g_elbow_tl.png"
    image EB1tile95 = "y_vertical.png"
    
    show EB1tile87 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show EB1tile89 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show EB1tile90 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show EB1tile91 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show EB1tile92 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show EB1tile93 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show EB1tile95 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)

    #row 7 (row has a light)
    image EB1tile100 = "g_horizontal.png"
    image EB1tile101 = "g_jump_g.png"
    image EB1tile102 = "g_horizontal.png"
    image EB1tile103 = "g_t_up.png"
    image EB1tile104 = "g_horizontal.png"
    image EB1tile105 = "g_elbow_bl.png"
    image EB1tile109 = "y_vertical.png"

    show EB1tile100 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show EB1tile101 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show EB1tile102 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show EB1tile103 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show EB1tile104 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show EB1tile105 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show EB1tile109 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image EB1tile114 = "g_vertical.png"
    image EB1tile118 = "g_g.png"
    image EB1tile120 = "NONE_Gate.png"
    image EB1tile121 = "y_horizontal.png"
    image EB1tile122 = "y_horizontal.png"
    image EB1tile123 = "y_elbow_tl.png"

    show EB1tile114 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show EB1tile118 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show EB1tile120 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show EB1tile121 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show EB1tile122 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    show EB1tile123 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)

    #row 9
    image EB1tile128 = "g_elbow_tr.png"
    image EB1tile129 = "g_horizontal.png"
    image EB1tile130 = "g_horizontal.png"
    image EB1tile131 = "g_horizontal.png"
    image EB1tile132 = "g_elbow_tl.png"

    show EB1tile128 at Position(xpos = 511, xanchor = 0, ypos = 908, yanchor = 0)
    show EB1tile129 at Position(xpos = 586, xanchor = 0, ypos = 908, yanchor = 0)
    show EB1tile130 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
    show EB1tile131 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
    show EB1tile132 at Position(xpos = 811, xanchor = 0, ypos = 908, yanchor = 0)

    #logicGate_easyB1 points
    image logicGate_easyB11 = "light_r_on.png"
    show logicGate_easyB11 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image logicGate_easyB13 = "light_g_on.png"
    show logicGate_easyB13 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image logicGate_easyB14 = "light_g_on.png"
    show logicGate_easyB14 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end point
    image EB1end2 = "light_g_off.png"
    show EB1end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)

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
 
    jump gamefileB1
    
label gamefileB1:
    
    #calls game screen
    call screen logicGatesB1
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in1 = False
            #sets values for checks
            $ and1x = 811
            $ and1y = 383
            $ and1in1 = True
            $ and1in2 = False
 
        if slot_name == "gate slot two":
            if or1in2 == True:
               $ or1x = 848
               $ or1y = 88
               $ or1in2 = False
            #sets values for checks
            $ and1x = 886
            $ and1y = 833
            $ and1in2 = True
            $ and1in1 = False
            
        if slot_name == "and return":
            $ and1x = 698
            $ and1y = 88
            $ and1in1 = False
            $ and1in2 = False
            
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 698
               $ and1y = 88
               $ and1in1 = False
            #sets values for checks
            $ or1x = 811
            $ or1y = 383
            $ or1in1 = True
            $ or1in2 = False
            
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 698
                $ and1y = 88
                $ and1in2 = False
            #sets values for checks
            $ or1x = 886
            $ or1y = 833
            $ or1in2 = True  
            $ or1in1 = False  
            
        if slot_name == "or return":
            $ or1x = 848
            $ or1y = 88
            $ or1in2 = False
            $ or1in1 = False  
            
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
#first slot for and 1
    if and1in1:
        image EB1tile133 = "r_horizontal.png"
        image EB1tile134 = "r_elbow_bl.png"
        image EB1tile135 = "r_g.png"
        image EB1tile136 = "r_horizontal.png"
        image EB1tile137 = "r_elbow_bl.png"
        image EB1tile138 = "r_y.png"

        #shows EB1tiles
        show EB1tile133 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show EB1tile134 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show EB1tile135 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show EB1tile136 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show EB1tile137 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show EB1tile138 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        
    if not(and1in1):
        hide EB1tile133
        hide EB1tile134
        hide EB1tile135
        hide EB1tile136
        hide EB1tile137
        hide EB1tile138
        
    if and1in2 or or1in2:
        image EB1tile139 = "g_horizontal.png"
        image EB1tile140 = "g_horizontal.png"
        image EB1tile141 = "g_elbow_tl.png"
        image EB1tile142 = "g_vertical.png"
        image EB1tile143 = "g_vertical.png"
        image EB1tile144 = "g_elbow_br.png"
        image EB1tile145 = "g_elbow_tl.png"
        image EB1tile146 = "y_g.png"

        #shows EB1tiles
        show EB1tile139 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show EB1tile140 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show EB1tile141 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
        show EB1tile142 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show EB1tile143 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show EB1tile144 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        show EB1tile145 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show EB1tile146 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    
    if not(and1in2 or or1in2):
        hide EB1tile139
        hide EB1tile140
        hide EB1tile141
        hide EB1tile142
        hide EB1tile143
        hide EB1tile144
        hide EB1tile145
        hide EB1tile146
        
#first slot for or 1
    if or1in1:
        image EB1tile147 = "g_horizontal.png"
        image EB1tile148 = "g_elbow_bl.png"
        image EB1tile149 = "g_g.png"
        image EB1tile150 = "g_horizontal.png"
        image EB1tile151 = "g_elbow_bl.png"
        image EB1tile152 = "g_y.png"

        #shows EB1tiles
        show EB1tile147 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show EB1tile148 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show EB1tile149 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show EB1tile150 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show EB1tile151 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show EB1tile152 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        
    if or1in1 == False:
        hide EB1tile147
        hide EB1tile148
        hide EB1tile149
        hide EB1tile150
        hide EB1tile151
        hide EB1tile152
    
        
    if or1in1 == True and and1in2 == True:
        image EB1tile161 = "g_g.png"
        image EB1tile162 = "g_elbow_tl.png"
        image EB1tile163 = "g_elbow_br.png"
        image EB1tile164 = "g_horizontal.png"
        image EB1tile200 = "AND_Gate.png"
        image EB1tile201 = "OR_Gate.png"
        
        image endWin_LGB1 = "light_g_on.png"
        show endWin_LGB1 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
        
        show EB1tile201 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)   
        show EB1tile200 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)   
        show EB1tile161 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)   
        show EB1tile162 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)   
        show EB1tile163 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)   
        show EB1tile164 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)  
        queue sound lgWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgEasyBWin
        $ Logic_B_solved = True
        #make to jump back to the game
        jump nextLGEasy

    else:
        hide EB1tile161
        hide EB1tile162
        hide EB1tile163
        hide EB1tile164

    if or1in2 == True and and1in1 == True:
        image EB1tile165 = "r_g.png"
        image EB1tile166 = "r_elbow_tl.png"
        image EB1tile167 = "r_elbow_br.png"
        image EB1tile168 = "r_horizontal.png"
        
        show EB1tile165 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)   
        show EB1tile166 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)   
        show EB1tile167 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)   
        show EB1tile168 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)   
        
    else:
        hide EB1tile165
        hide EB1tile166
        hide EB1tile167
        hide EB1tile168
        
    #keeps invalid moves from cancling game
    if (temp_slot == "" and temp_gate == "" and slot_name != "null") and not(slot_name=="and return" or slot_name=="or return"):
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
            if slot_name == "or return" and gate_name == "and_gate":
                $ attempts +=1
            if slot_name == "and return" and gate_name == "or_gate":
                $ attempts +=1
                
    if attempts == 0:
        image EB111tile07_02 = "and_Gate.png"
        show EB111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
        image EB111tile07_08 = "or_Gate.png"
        show EB111tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
        queue sound lgLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 1
            jump pg_lgEasyBLose
        $ lgEasy_tries +=1
        jump repeatLGEasy
    
    #games loop
    jump gamefileB1
    
screen logicGatesB1:
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
        action Jump("LGEasyHintsB1")
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
                child "OR_Gate.png"
                droppable False
                dragged gate_dragged
                xpos or1x ypos or1y

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos 811 ypos 383
                
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos 886 ypos 833

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
