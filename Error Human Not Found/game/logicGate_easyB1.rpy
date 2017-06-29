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

label logicGate_easyB1:
    #loads background
    scene bg Logic_Gate
   
    #row 1 (row has a light)
    image tile15 = "r_horizontal.png"
    image tile16 = "r_horizontal.png"
    image tile17 = "r_horizontal.png"
    image tile18 = "r_horizontal.png"
    image tile19 = "r_elbow_bl.png"
   
    show tile15 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show tile16 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show tile17 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show tile18 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show tile19 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
    image tile33 = "r_g.png"
    image tile34 = "NONE_Gate.png"
    image tile35 = "y_horizontal.png"
    image tile37 = "y_elbow_bl.png"

    show tile33 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show tile34 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show tile35 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show tile37 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image tile47 = "g_vertical.png"
    image tile51 = "y_g.png"
    image tile52 = "AND_Gate.png"
    image tile53 = "y_horizontal.png"
    image tile54 = "y_elbow_bl.png"
    image tile55 = "y_elbow_br.png"
    image tile56 = "y_horizontal.png"

    show tile47 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show tile51 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show tile52 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show tile53 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show tile54 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show tile55 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show tile56 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
    image tile60 = "g_elbow_br.png"
    image tile61 = "g_elbow_tl.png"
    image tile65 = "g_vertical.png"
    image tile67 = "y_y.png"
    image tile68 = "AND_Gate.png"
    image tile69 = "y_elbow_tl.png"
    
    show tile60 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show tile61 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show tile65 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show tile67 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show tile68 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
    show tile69 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image tile71 = "g_horizontal.png"
    image tile72 = "g_t_down.png"
    image tile73 = "g_horizontal.png"
    image tile74 = "g_t_left.png"
    image tile78 = "g_vertical.png"
    image tile80 = "y_elbow_br.png"
    image tile81 = "y_elbow_tl.png"
    
    show tile71 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show tile72 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show tile73 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show tile74 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show tile78 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show tile80 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show tile81 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
    image tile87 = "g_vertical.png"
    image tile89 = "g_g.png"
    image tile90 = "AND_Gate.png"
    image tile91 = "g_horizontal.png"
    image tile92 = "g_horizontal.png"
    image tile93 = "g_elbow_tl.png"
    image tile95 = "y_vertical.png"
    
    show tile87 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show tile89 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show tile90 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show tile91 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show tile92 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show tile93 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show tile95 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)

    #row 7 (row has a light)
    image tile100 = "g_horizontal.png"
    image tile101 = "g_jump_g.png"
    image tile102 = "g_horizontal.png"
    image tile103 = "g_t_up.png"
    image tile104 = "g_horizontal.png"
    image tile105 = "g_elbow_bl.png"
    image tile109 = "y_vertical.png"

    show tile100 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show tile101 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show tile102 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show tile103 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show tile104 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show tile105 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    show tile109 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
    image tile114 = "g_vertical.png"
    image tile118 = "g_g.png"
    image tile120 = "NONE_Gate.png"
    image tile121 = "y_horizontal.png"
    image tile122 = "y_horizontal.png"
    image tile123 = "y_elbow_tl.png"

    show tile114 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show tile118 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show tile120 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show tile121 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show tile122 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
    show tile123 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)

    #row 9
    image tile128 = "g_elbow_tr.png"
    image tile129 = "g_horizontal.png"
    image tile130 = "g_horizontal.png"
    image tile131 = "g_horizontal.png"
    image tile132 = "g_elbow_tl.png"

    show tile128 at Position(xpos = 511, xanchor = 0, ypos = 908, yanchor = 0)
    show tile129 at Position(xpos = 586, xanchor = 0, ypos = 908, yanchor = 0)
    show tile130 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
    show tile131 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
    show tile132 at Position(xpos = 811, xanchor = 0, ypos = 908, yanchor = 0)

    #logicGate_easyB1 points
    image logicGate_easyB11 = "light_r_on.png"
    show logicGate_easyB11 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image logicGate_easyB13 = "light_g_on.png"
    show logicGate_easyB13 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image logicGate_easyB14 = "light_g_on.png"
    show logicGate_easyB14 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end point
    image end2 = "light_g_off.png"
    show end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
    
    #makes gray backgrounds for tiles
    image and_gray = "AND_Gray.png"
    image or_gray = "OR_Gray.png"
    image nand_gray = "NAND_Gray.png"
    image nor_gray = "NOR_Gray.png"
    show and_gray at Position(xpos = 586, xanchor = 0, ypos = 88, yanchor = 0)
    show or_gray at Position(xpos = 812, xanchor = 0, ypos = 88, yanchor = 0)
    show nand_gray at Position(xpos = 1035, xanchor = 0, ypos = 88, yanchor = 0)
    show nor_gray at Position(xpos = 1261, xanchor = 0, ypos = 88, yanchor = 0)

    #initial value assignment for dragables
    $ and1x = 586
    $ and1y = 88
    $ or1x = 812
    $ or1y = 88
   
    # check conditons for locations
    $ and1in1 = False
    $ and1in2 = False
    $ or1in1 = False
    $ or1in2 = False
   
    #attempts for players
    $ attempts = 6
 
    jump gamefile2
    
label gamefile2:
    
    #calls game screen
    call screen logicGates2
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if or1in1 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in1 = False
            #sets values for checks
            $ and1x = 811
            $ and1y = 383
            $ and1in1 = True
            $ and1in2 = False
 
        if slot_name == "gate slot two":
            if or1in2 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in2 = False
            #sets values for checks
            $ and1x = 886
            $ and1y = 833
            $ and1in2 = True
            $ and1in1 = False
            
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in1 = False
            #sets values for checks
            $ or1x = 811
            $ or1y = 383
            $ or1in1 = True
            $ or1in2 = False
            
        if slot_name == "gate slot two":
            if and1in2 == True:
                $ and1x = 586
                $ and1y = 88
                $ and1in2 = False
            #sets values for checks
            $ or1x = 886
            $ or1y = 833
            $ or1in2 = True  
            $ or1in1 = False        

#*******************************************
#************image zone********************* 
#*******************************************

#first slot for and 1
    if and1in1 == True:
        image tile133 = "r_horizontal.png"
        image tile134 = "r_elbow_bl.png"
        image tile135 = "r_g.png"
        image tile136 = "r_horizontal.png"
        image tile137 = "r_elbow_bl.png"
        image tile138 = "r_y.png"

        #shows tiles
        show tile133 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show tile134 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show tile135 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show tile136 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show tile137 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show tile138 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        
    if and1in1 == False:
        hide tile133
        hide tile134
        hide tile135
        hide tile136
        hide tile137
        hide tile138
        
    if and1in2 == True:
        image tile139 = "g_horizontal.png"
        image tile140 = "g_horizontal.png"
        image tile141 = "g_elbow_tl.png"
        image tile142 = "g_vertical.png"
        image tile143 = "g_vertical.png"
        image tile144 = "g_elbow_br.png"
        image tile145 = "g_elbow_tl.png"
        image tile146 = "y_g.png"

        #shows tiles
        show tile139 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show tile140 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show tile141 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
        show tile142 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show tile143 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show tile144 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        show tile145 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show tile146 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    
    if and1in2 == False:
        hide tile139
        hide tile140
        hide tile141
        hide tile142
        hide tile143
        hide tile144
        hide tile145
        hide tile146
        
#first slot for or 1
    if or1in1 == True:
        image tile147 = "g_horizontal.png"
        image tile148 = "g_elbow_bl.png"
        image tile149 = "g_g.png"
        image tile150 = "g_horizontal.png"
        image tile151 = "g_elbow_bl.png"
        image tile152 = "g_y.png"

        #shows tiles
        show tile147 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
        show tile148 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
        show tile149 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
        show tile150 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
        show tile151 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
        show tile152 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
        
    if or1in1 == False:
        hide tile147
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152
        
    if or1in2 == True:
        image tile153 = "g_horizontal.png"
        image tile154 = "g_horizontal.png"
        image tile155 = "g_elbow_tl.png"
        image tile156 = "g_vertical.png"
        image tile157 = "g_vertical.png"
        image tile158 = "g_elbow_br.png"
        image tile159 = "g_elbow_tl.png"
        image tile160 = "y_g.png"

        #shows tiles
        show tile153 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
        show tile154 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
        show tile155 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
        show tile156 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
        show tile157 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
        show tile158 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        show tile159 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show tile160 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    
    if or1in2 == False:
        hide tile153
        hide tile154
        hide tile155
        hide tile156
        hide tile157
        hide tile158
        hide tile159
        hide tile160
        
    if or1in1 == True and and1in2 == True:
        image tile161 = "g_g.png"
        image tile162 = "g_elbow_tl.png"
        image tile163 = "g_elbow_br.png"
        image tile164 = "g_horizontal.png"
        
        show tile161 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)   
        show tile162 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)   
        show tile163 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)   
        show tile164 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)   
        #"YOU WIN"
        $ Logic_B_solved = True
        $ solved_LG_easy = True
        #make to jump back to the game
        jump exploreHiroseOffice
    else:
        hide tile161
        hide tile162
        hide tile163
        hide tile164

    if or1in2 == True and and1in1 == True:
        image tile165 = "r_g.png"
        image tile166 = "r_elbow_tl.png"
        image tile167 = "r_elbow_br.png"
        image tile168 = "r_horizontal.png"
        
        show tile165 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)   
        show tile166 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)   
        show tile167 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)   
        show tile168 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)   
        
    else:
        hide tile165
        hide tile166
        hide tile167
        hide tile168
        
    #keeps invalid moves from cancling game
    if slot_name == "null":
        $attempts +=1
        
    #subtracts attempts    
    $ attempts -= 1
    if attempts == 0:
        "you lose try again"
        jump exploreHiroseOffice
    
    #games loop
    jump gamefile2
    
screen logicGates2:
    
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
