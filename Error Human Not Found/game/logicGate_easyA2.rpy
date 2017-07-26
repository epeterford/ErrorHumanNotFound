
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

label logicGate_easyA2:  #logicGate_easyA2
    $renpy.block_rollback()
    $quick_menu = False
    #loads background
    scene bg Logic_Gate 
    

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 1
    image ea1tile1 = "g_horizontal.png"
    image ea1tile2 = "g_horizontal.png"
    image ea1tile3 = "g_horizontal.png"
    image ea1tile4 = "g_horizontal.png"
    image ea1tile5 = "g_elbow_bl.png"
    
    show ea1tile1 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show ea1tile2 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show ea1tile3 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show ea1tile4 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show ea1tile5 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)

    #row 2
    image ea1tile6 = "g_g.png"
    image ea1tile7 = "AND_Gate.png"
    image ea1tile8 = "g_horizontal.png"
    image ea1tile9 = "g_horizontal.png"
    image ea1tile10 = "g_elbow_bl.png"

    show ea1tile6 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show ea1tile7 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show ea1tile8 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show ea1tile9 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show ea1tile10 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
 
    #row 3
    image ea1tile11 = "g_horizontal.png"
    image ea1tile12 = "g_horizontal.png"
    image ea1tile13 = "g_t_down.png"
    image ea1tile14 = "g_horizontal.png"
   
    image eahelpme = "g_elbow_tl.png"
    image ea1tile16 = "g_vertical.png"
    
    show ea1tile11 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show ea1tile12 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show ea1tile13 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show ea1tile14 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show eahelpme at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show ea1tile16 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4
    image ea1tile17 = "g_vertical.png"
    image ea1tile18 = "g_vertical.png"
    
    show ea1tile17 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show ea1tile18 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5
    image ea1tile19 = "g_elbow_tr.png"
    image ea1tile20 = "g_horizontal.png"
    image ea1tile21 = "g_elbow_bl.png"
    image ea1tile22 = "g_r.png"
    image ea1tile28 = "NONE_Gate.png"
    image ea1tile29 = "y_horizontal.png"
    image ea1tile30 = "y_horizontal.png"
    image ea1tile31 = "y_horizontal.png"
    image ea1tile32 = "y_horizontal.png"
    
    show ea1tile19 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile20 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile21 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile22 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile28 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile29 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile30 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile31 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show ea1tile32 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row6
    image ea1tile23 = "g_r.png"
    image ea1tile24 = "AND_Gate.png"
    image ea1tile25 = "r_horizontal.png"
    image ea1tile26 = "r_horizontal.png"
    image ea1tile27 = "r_elbow_tl.png"
    
    show ea1tile23 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show ea1tile24 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show ea1tile25 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show ea1tile26 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show ea1tile27 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row7
    image ea1tile34 = "r_horizontal.png"
    image ea1tile35 = "r_horizontal.png"
    image ea1tile36 = "r_horizontal.png"
    image ea1tile37 = "r_horizontal.png"
    image ea1tile38 = "r_elbow_tl.png"
    
    show ea1tile34 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show ea1tile35 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show ea1tile36 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show ea1tile37 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show ea1tile38 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    
    #logicGate_easyA1 and end points
    image logicGate_easyA21 = "light_g_on.png"
    show logicGate_easyA21 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image logicGate_easyA22 = "light_g_on.png"
    show logicGate_easyA22 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image logicGate_easyA23 = "light_r_on.png"
    show logicGate_easyA23 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    image end2 = "light_g_off.png"
    show end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************



    #initial value assignment for dragables
    $ and1x = 848
    $ and1y = 88
   
    # check conditons for locations
    $ and1in1 = False
   
    #attempts for players
    $ attempts = 3
 
    jump gamefileA2
    
    
label gamefileA2:
    
    #calls game screen
    call screen logicGatesEasyA2
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #sets values for checks
            $ and1x = 1111
            $ and1y = 608
            $ and1in1 = True


#*******************************************
#************image zone********************* 
#*******************************************

#first slot for and 1
    if and1in1 == True:
        play sound pipeFlowG
        image ea1tile39 = "g_horizontal.png"
        image ea1tile40 = "g_horizontal.png"
        image ea1tile41 = "g_horizontal.png"
        image ea1tile42 = "g_horizontal.png"
        image ea1end2 = "light_g_on.png"

        #shows tiles
        show ea1tile39 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show ea1tile40 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        show ea1tile41 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show ea1tile42 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        show ea1end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        
        
    if slot_name == "null":
        $attempts +=1
        
#win conditions ********
    if and1in1 == True: 
        image ea1tile100 = "OR_Gate.png"
        show ea1tile100 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ Logic_A_solved = True
        jump nextLGEasy
        #jump logicGate_easyA2

        
    $ attempts -= 1
    if attempts == 0:
        "you lose try again"
        jump exploreHiroseOffice
    
    jump gamefileA2
    
#area for dragables
screen logicGatesEasyA2:
    key 'h' action Hide("")
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 240
        ypos 890
        focus_mask True
        action Jump("LGEasyHintsA2")
        hover_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty.png"
        xpos 1515
        ypos 890
    text "Attempts" xpos 1530 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    text ": " xpos 1716 ypos 895 color "#0060db" font "Bitter-Bold.otf" size 42
    text "[attempts]" xpos 1735 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    
    #drags and drop location
    draggroup:
            #and gates
            drag:
                drag_name "and_gate"
                child "OR_Gate.png"
                droppable False
                dragged gate_dragged
                xpos and1x ypos and1y


            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos 1111 ypos 608
