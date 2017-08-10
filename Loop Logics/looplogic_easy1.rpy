init python:
    def gate_dragged(drags,drop):
        if not drop:
            store.gate_name = drags[0].drag_name
            store.slot_name = "null"
            return True
                
        if drop:
            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop
                
                store.gate_name = drags[0].drag_name
                store.slot_name = drop.drag_name
            
                return True
        return True 

init:
    image bg looplogic_bg = "LoopLogic_background.png"

label looplogic_easy1: #loopLogic_easy5
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
   
    image LLE_1_tile1 = "G_horizontal_ll.png"
    show LLE_1_tile1 at Position(xpos = 279, xanchor = 0, ypos = 251, yanchor = 0)
    image LLE_1_tile2 = "blank_node.png"
    show LLE_1_tile2 at Position(xpos = 180, xanchor = 0, ypos = 220, yanchor = 0)  
    image LLE_1_tile3 = "W_vertical.png"
    show LLE_1_tile3 at Position(xpos = 212, xanchor = 0, ypos = 320, yanchor = 0)
    image LLE_1_tile4 = "G_end_off.png"
    show LLE_1_tile4 at Position(xpos = 180, xanchor = 0, ypos = 397, yanchor = 0)
    image LLE_1_tile5 = "G_vertical_ll.png"
    show LLE_1_tile5 at Position(xpos = 376, xanchor = 0, ypos = 303, yanchor = 0)
    image LLE_1_tile6 = "G_vertical_ll.png"
    show LLE_1_tile6 at Position(xpos = 376, xanchor = 0, ypos = 378, yanchor = 0)
    image LLE_1_tile7 = "G_corner_LB.png"
    show LLE_1_tile7 at Position(xpos = 354, xanchor = 0, ypos = 228, yanchor = 0)

    image LLE_1_tile8 = "G_horizontal_ll.png"
    show LLE_1_tile8 at Position(xpos = 431, xanchor = 0, ypos = 512, yanchor = 0)
    image LLE_1_tile9 = "B_horizontal.png"
    show LLE_1_tile9 at Position(xpos = 446, xanchor = 0, ypos = 450, yanchor = 0)
    image LLE_1_tile10 = "B_horizontal_short.png"
    show LLE_1_tile10 at Position(xpos = 521, xanchor = 0, ypos = 450, yanchor = 0)
    #image LLE_1_tile2 = "blank_node.png"
    #show LLE_1_tile2 at Position(xpos = 336, xanchor = 0, ypos = 458, yanchor = 0)  
    


    
    image LLE_1_tile11 = "G_corner_LB.png"
    show LLE_1_tile11 at Position(xpos = 506, xanchor = 0, ypos = 489, yanchor = 0)
    image LLE_1_tile12 = "B_corner_LB.png"
    show LLE_1_tile12 at Position(xpos = 571, xanchor = 0, ypos = 427, yanchor = 0)
    
    image LLE_1_tile13 = "G_vertical_ll.png"
    show LLE_1_tile13 at Position(xpos = 528, xanchor = 0, ypos = 564, yanchor = 0) 
    image LLE_1_tile14 = "B_vertical_short.png"
    show LLE_1_tile14 at Position(xpos = 592, xanchor = 0, ypos = 502, yanchor = 0)
    image LLE_1_tile15 = "B_vertical.png"
    show LLE_1_tile15 at Position(xpos = 593, xanchor = 0, ypos = 552, yanchor = 0)  
    image LLE_1_tile16 = "W_connect_horizontal.png"
    show LLE_1_tile16 at Position(xpos = 528, xanchor = 0, ypos = 580, yanchor = 0)
    image LLE_1_tile17 = "start.png"
    show LLE_1_tile17 at Position(xpos = 346, xanchor = 0, ypos = 454, yanchor = 0) 
    image LLE_1_tile18 = "W_vertical_short.png"
    show LLE_1_tile18 at Position(xpos = 528, xanchor = 0, ypos = 640, yanchor = 0) 
    image LLE_1_tile19 = "W_vertical_short.png"
    show LLE_1_tile19 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0) 
    image LLE_1_tile20 = "blank_node.png"
    show LLE_1_tile20 at Position(xpos = 530, xanchor = 0, ypos = 680, yanchor = 0)
    image LLE_1_tile21 = "W_horizontal.png"
    show LLE_1_tile21 at Position(xpos = 455, xanchor = 0, ypos = 715, yanchor = 0)
    image LLE_1_tile22 = "W_horizontal.png"
    show LLE_1_tile22 at Position(xpos = 380, xanchor = 0, ypos = 715, yanchor = 0)
    image LLE_1_tile23 = "G_end_off.png"
    show LLE_1_tile23 at Position(xpos = 310, xanchor = 0, ypos = 680, yanchor = 0)


    image LLE_1_tile24 = "W_horizontal.png"
    show LLE_1_tile24 at Position(xpos = 628, xanchor = 0, ypos = 615, yanchor = 0)
    image LLE_1_tile25 = "W_horizontal.png"
    show LLE_1_tile25 at Position(xpos = 703, xanchor = 0, ypos = 615, yanchor = 0)
    image LLE_1_tile26 = "W_corner_LB.png"
    show LLE_1_tile26 at Position(xpos = 778, xanchor = 0, ypos = 592, yanchor = 0)
    image LLE_1_tile27 = "W_vertical_short.png"
    show LLE_1_tile27 at Position(xpos = 799, xanchor = 0, ypos = 667, yanchor = 0)
    image LLE_1_tile28 = "blank_node.png"
    show LLE_1_tile28 at Position(xpos = 770, xanchor = 0, ypos = 715, yanchor = 0)
    image LLE_1_tile29 = "W_horizontal.png"
    show LLE_1_tile29 at Position(xpos = 870, xanchor = 0, ypos = 745, yanchor = 0)
    image LLE_1_tile30 = "W_horizontal.png"
    show LLE_1_tile30 at Position(xpos = 945, xanchor = 0, ypos = 745, yanchor = 0)
    image LLE_1_tile31 = "B_end_off.png"
    show LLE_1_tile31 at Position(xpos = 1020, xanchor = 0, ypos = 715, yanchor = 0)

        
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1445
    $ if1y = 645
    
    $ else1x = 1625
    $ else1y = 645
    
    $ if2x = 1445
    $ if2y = 645
            
    #gate values
    $ gate1x = 182
    $ gate1y = 220
    $ gate2x = 530
    $ gate2y = 680
    $ gate3x = 770
    $ gate3y = 715
   
    # check conditons for locations
    $ if1in1 = False
    $ if1in2 = False
    $ if1in3 = False

    $ if2in1 = False
    $ if2in2 = False
    $ if2in3 = False

    $ else1in1 = False
    $ else1in2 = False
    $ else1in3 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

     
    #attempts for players
    $ attempts = 6
 
    jump gamefile_lle1
    
    
label gamefile_lle1:
    
    #calls game screen
    call screen logicGatesMA1
    



#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "G_if_gate1":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in1 = False

            #sets values for checks
            $ if1x = gate1x
            $ if1y = gate1y
            $ if1in1 = True
            $ if1in2 = False
            $ if1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in2 = False
            #sets values for checks
            $ if1x = gate2x
            $ if1y = gate2y
            $ if1in1 = False
            $ if1in2 = True
            $ if1in3 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in3 = False
            #sets values for checks
            $ if1x = gate3x
            $ if1y = gate3y
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = True
            
    #the first logic gate *******************************************************************************
    if gate_name == "G_if_gate2":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in1 = False

            #sets values for checks
            $ if2x = gate1x
            $ if2y = gate1y
            $ if2in1 = True
            $ if2in2 = False
            $ if2in3 = False
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in2 = False
            #sets values for checks
            $ if2x = gate2x
            $ if2y = gate2y
            $ if2in1 = False
            $ if2in2 = True
            $ if2in3 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in3 = False
            #sets values for checks
            $ if2x = gate3x
            $ if2y = gate3y
            $ if2in1 = False
            $ if2in2 = False
            $ if2in3 = True
            
    #the third logic gate *******************************************************************************
    if gate_name == "G_else_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in1 = False
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in1 = False

            #sets values for checks
            $ else1x = gate1x
            $ else1y = gate1y
            $ else1in1 = True
            $ else1in2 = False
            $ else1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in2 = False
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in2 = False
            #sets values for checks
            $ else1x = gate2x
            $ else1y = gate2y
            $ else1in1 = False
            $ else1in2 = True
            $ else1in3 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in3 = False
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in3 = False
            #sets values for checks
            $ else1x = gate3x
            $ else1y = gate3y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = True


    #"[gate_name] [slot_name] [temp_slot] [temp_gate]"
    if temp_slot == "" and temp_gate == "" and slot_name != "":
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            $ attempts -=1
            #"empty"
    else:
        if slot_name != "":
            if (temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate):
                $ attempts -=1
                $ temp_slot = slot_name
                $ temp_gate = gate_name
                #"main loop"




#*******************************************
#************image zone********************* 
#*******************************************

#    #if 1 section*******************************************************************************************     
    if if1in2 == True or if2in2 == True:
        image LLE_1_tile34 = "G_vertical_short.png"
        show LLE_1_tile34 at Position(xpos = 528, xanchor = 0, ypos = 640, yanchor = 0)
        image LLE_1_tile35 = "G_horizontal_ll.png"
        show LLE_1_tile35 at Position(xpos = 455, xanchor = 0, ypos = 715, yanchor = 0)
        image LLE_1_tile36 = "G_horizontal_ll.png"
        show LLE_1_tile36 at Position(xpos = 380, xanchor = 0, ypos = 715, yanchor = 0)
        image LLE_1_tile37 = "G_end_on.png"
        show LLE_1_tile37 at Position(xpos = 310, xanchor = 0, ypos = 680, yanchor = 0)
        
        if else1in3 == True:
            image LLE_1_tile38 = "B_connect_node.png"
            show LLE_1_tile38 at Position(xpos = 595, xanchor = 0, ypos = 615, yanchor = 0)
            #show LLE_1_tile38 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLE_1_tile39 = "B_horizontal.png"
            show LLE_1_tile39 at Position(xpos = 628, xanchor = 0, ypos = 615, yanchor = 0)
            image LLE_1_tile40 = "B_horizontal.png"
            show LLE_1_tile40 at Position(xpos = 703, xanchor = 0, ypos = 615, yanchor = 0)
            image LLE_1_tile41 = "B_corner_LB.png"
            show LLE_1_tile41 at Position(xpos = 778, xanchor = 0, ypos = 592, yanchor = 0)
            image LLE_1_tile42 = "B_vertical_short.png"
            show LLE_1_tile42 at Position(xpos = 799, xanchor = 0, ypos = 667, yanchor = 0)
            image LLE_1_tile43 = "B_horizontal.png"
            show LLE_1_tile43 at Position(xpos = 870, xanchor = 0, ypos = 745, yanchor = 0)
            image LLE_1_tile44 = "B_horizontal.png"
            show LLE_1_tile44 at Position(xpos = 945, xanchor = 0, ypos = 745, yanchor = 0)
            image LLE_1_tile45 = "B_end_on.png"
            show LLE_1_tile45 at Position(xpos = 1020, xanchor = 0, ypos = 715, yanchor = 0)

        if else1in3 == False:
            hide LLE_1_tile38
            hide LLE_1_tile39
            hide LLE_1_tile40
            hide LLE_1_tile41
            hide LLE_1_tile42
            hide LLE_1_tile43
            hide LLE_1_tile44
            hide LLE_1_tile45
   
    if if1in2 == False and if2in2 == False:
        hide LLE_1_tile34
        hide LLE_1_tile35
        hide LLE_1_tile36
        hide LLE_1_tile37
        hide LLE_1_tile38
        hide LLE_1_tile39
        hide LLE_1_tile40
        hide LLE_1_tile41
        hide LLE_1_tile42
        hide LLE_1_tile43
        hide LLE_1_tile44
        hide LLE_1_tile45


    if if2in1 == True or if1in1 == True:
        image LLE_1_tile46 = "G_vertical_ll.png"
        show LLE_1_tile46 at Position(xpos = 212, xanchor = 0, ypos = 320, yanchor = 0)
        image LLE_1_tile47 = "G_end_on.png"
        show LLE_1_tile47 at Position(xpos = 180, xanchor = 0, ypos = 397, yanchor = 0)
        
    if if2in1 == False and if1in1 == False:
        hide LLE_1_tile46
        hide LLE_1_tile47

        
    #if slot_name == "null":
     #   $attempts +=1
        
#win conditions ********
    if (if1in2 == True or if2in2 == True) and else1in3 == True and (if2in1 == True or if1in1 == True):
        image LLE_1_tile48 = "G_end_on.png"
        show LLE_1_tile48 at Position(xpos = 310, xanchor = 0, ypos = 680, yanchor = 0)
        image LLE_1_tile49 = "B_end_on.png"
        show LLE_1_tile49 at Position(xpos = 1020, xanchor = 0, ypos = 715, yanchor = 0)
        image LLE_1_tile50 = "G_end_on.png"
        show LLE_1_tile50 at Position(xpos = 180, xanchor = 0, ypos = 397, yanchor = 0)
        image LLE_1_tile51 = "G_if.png"
        show LLE_1_tile51 at Position(xpos = 180, xanchor = 0, ypos = 220, yanchor = 0)
        image LLE_1_tile52 = "G_if.png"
        show LLE_1_tile52 at Position(xpos = 530, xanchor = 0, ypos = 680, yanchor = 0)
        image LLE_1_tile53 = "G_else.png"
        show LLE_1_tile53 at Position(xpos = 770, xanchor = 0, ypos = 715, yanchor = 0)

        "game"
        jump looplogic_easy1

        
    #$ attempts -= 1
    if attempts == 0:


        "you lose try again"
        jump looplogic_easy1
    
    jump gamefile_lle1

screen logicGatesMA1:
    
    #drags and drop location
    draggroup:
            #if gates
            drag:
                drag_name "G_if_gate1"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos if1x ypos if1y
            drag:
                drag_name "G_if_gate2"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos if2x ypos if2y  
            #else gate
            drag:
                drag_name "G_else_gate"
                child "G_else.png"
                droppable False
                dragged gate_dragged
                xpos else1x ypos else1y

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

