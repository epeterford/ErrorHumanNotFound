init -100:
    python:
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

label loopLogic_easy3: #loopLogic_easy5
    $config.skipping=None
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLE_3_tile1 = "Start.png"
    show LLE_3_tile1 at Position(xpos = 330, xanchor = 0, ypos = 240, yanchor = 0)   

    #top right blue
    image LLE_3_tile2 = "W_horizontal.png"
    show LLE_3_tile2 at Position(xpos = 430, xanchor = 0, ypos = 275, yanchor = 0)
    image LLE_3_tile3 = "W_horizontal.png"
    show LLE_3_tile3 at Position(xpos = 505, xanchor = 0, ypos = 275, yanchor = 0)
    image LLE_3_tile4 = "W_horizontal.png"
    show LLE_3_tile4 at Position(xpos = 580, xanchor = 0, ypos = 275, yanchor = 0)
    image LLE_3_tile5 = "blank_node.png"
    show LLE_3_tile5 at Position(xpos = 655, xanchor = 0, ypos = 240, yanchor = 0)
    
    image LLE_3_tile6 = "W_horizontal.png"
    show LLE_3_tile6 at Position(xpos = 755, xanchor = 0, ypos = 275, yanchor = 0)
    image LLE_3_tile7 = "W_horizontal.png"
    show LLE_3_tile7 at Position(xpos = 830, xanchor = 0, ypos = 275, yanchor = 0)

    # end node
    image LLE_3_tile8 = "B_end_off.png"
    show LLE_3_tile8 at Position(xpos = 905, xanchor = 0, ypos = 239, yanchor = 0)

    #Start Down
    image LLE_3_tile9 = "G_vertical_ll.png"
    show LLE_3_tile9 at Position(xpos = 332, xanchor = 0, ypos = 340, yanchor = 0)
    image LLE_3_tile10 = "B_vertical.png"
    show LLE_3_tile10 at Position(xpos = 398, xanchor = 0, ypos = 340, yanchor = 0)
    image LLE_3_tile11 = "G_vertical_ll.png"
    show LLE_3_tile11 at Position(xpos = 332, xanchor = 0, ypos = 415, yanchor = 0)
    image LLE_3_tile12 = "B_vertical.png"
    show LLE_3_tile12 at Position(xpos = 398, xanchor = 0, ypos = 415, yanchor = 0)
    image LLE_3_tile13 = "W_connect_horizontal.png"
    show LLE_3_tile13 at Position(xpos = 330, xanchor = 0, ypos = 450, yanchor = 0)
    
    image LLE_3_tile14 = "W_vertical_short.png"
    show LLE_3_tile14 at Position(xpos = 335, xanchor = 0, ypos = 516, yanchor = 0)
    image LLE_3_tile15 = "W_vertical_short.png"
    show LLE_3_tile15 at Position(xpos = 399, xanchor = 0, ypos = 516, yanchor = 0)
    image LLE_3_tile16 = "blank_node.png"
    show LLE_3_tile16 at Position(xpos = 330, xanchor = 0, ypos = 565, yanchor = 0)
    image LLE_3_tile17 = "W_vertical.png"
    show LLE_3_tile17 at Position(xpos = 365, xanchor = 0, ypos = 670, yanchor = 0)
    
    # end node
    image LLE_3_tile18 = "G_end_off.png"
    show LLE_3_tile18 at Position(xpos = 332, xanchor = 0, ypos = 745, yanchor = 0)

    #Node going right

    image LLE_3_tile19 = "W_horizontal.png"
    show LLE_3_tile19 at Position(xpos = 428, xanchor = 0, ypos = 485, yanchor = 0)
    image LLE_3_tile20 = "W_horizontal.png"
    show LLE_3_tile20 at Position(xpos = 503, xanchor = 0, ypos = 485, yanchor = 0)
    image LLE_3_tile21 = "W_horizontal.png"
    show LLE_3_tile21 at Position(xpos = 578, xanchor = 0, ypos = 485, yanchor = 0)
    image LLE_3_tile22 = "blank_node.png"
    show LLE_3_tile22 at Position(xpos = 653, xanchor = 0, ypos = 455, yanchor = 0)

    image LLE_3_tile23 = "W_horizontal.png"
    show LLE_3_tile23 at Position(xpos = 753, xanchor = 0, ypos = 485, yanchor = 0)
    image LLE_3_tile24 = "W_horizontal.png"
    show LLE_3_tile24 at Position(xpos = 828, xanchor = 0, ypos = 485, yanchor = 0)

    image LLE_3_tile25 = "B_end_off.png"
    show LLE_3_tile25 at Position(xpos = 903, xanchor = 0, ypos = 454, yanchor = 0)




        
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1395
    $ if1y = 645

    $ if2x = 1525
    $ if2y = 645
    
    $ else1x = 1655
    $ else1y = 645
            
    #gate values
   # $ gate1x = 655
   # $ gate1y = 240
   # $ gate2x = 330
   # $ gate2y = 565
   # $ gate3x = 655
   # $ gate3y = 455

    $ gate1x = 655
    $ gate1y = 240
    $ gate2x = 330
    $ gate2y = 565
    $ gate3x = 655
    $ gate3y = 455

    image LLE_3_ifBT = "B_if_idle.png"
    image LLE_3_ifGT = "G_if_idle.png"
    image LLE_3_elseT = "G_else_idle.png"
    show LLE_3_ifBT at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLE_3_ifGT at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLE_3_elseT at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
   
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
    $ attempts = 4
 
    jump gamefile_lle3
    
    
label gamefile_lle3:
    $config.skipping=None
    #calls game screen
    call screen loopLogic_easy3Scr




#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "B_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1395
                $ if1y = 645
                $ if1in1 = False
            if if2in1 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in1 = False
            if else1in1 == True:
                $ else1x = 1655
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
            if if1in2 == True:
                $ if1x = 1395
                $ if1y = 645
                $ if1in2 = False
            if if2in2 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in2 = False
            if else1in2 == True:
                $ else1x = 1655
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
            if if1in3 == True:
                $ if1x = 1395
                $ if1y = 645
                $ if1in3 = False
            if if2in3 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in3 = False
            if else1in3 == True:
                $ else1x = 1655
                $ else1y = 645
                $ else1in3 = False
            #sets values for checks
            $ if1x = gate3x
            $ if1y = gate3y
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = True

    #the first logic gate *******************************************************************************
    if gate_name == "G_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1395
                $ if1y = 645
                $ if1in1 = False
            if if2in1 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in1 = False
            if else1in1 == True:
                $ else1x = 1655
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
                $ if1x = 1395
                $ if1y = 645
                $ if1in2 = False
            if if2in2 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in2 = False
            if else1in2 == True:
                $ else1x = 1655
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
                $ if1x = 1395
                $ if1y = 645
                $ if1in3 = False
            if if2in3 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in3 = False
            if else1in3 == True:
                $ else1x = 1655
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
                $ if2x = 1525
                $ if2y = 645
                $ if2in1 = False
            if if1in1 == True:
                $ if1x = 1395
                $ if1y = 645
            if else1in1 == True:
                $ else1x = 1655
                $ else1y = 645
                $ else1in1 = False

            #sets values for checks
            $ else1x = gate1x
            $ else1y = gate1y
            $ else1in1 = True
            $ else1in2 = False
            $ else1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in2 = False
            if if1in2 == True:
                $ if1x = 1395
                $ if1y = 645
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1655
                $ else1y = 645
                $ else1in2 = False
            #sets values for checks
            $ else1x = gate2x
            $ else1y = gate2y
            $ else1in1 = False
            $ else1in2 = True
            $ else1in3 = False

            #if else1x == gate2x and else1y == gate2y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1525
                $ if2y = 645
                $ if2in3 = False
            if if1in3 == True:
                $ if1x = 1395
                $ if1y = 645
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1655
                $ else1y = 645
                $ else1in3 = False
            #sets values for checks
            $ else1x = gate3x
            $ else1y = gate3y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = True



    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "G_if_gate_return" or slot_name == "B_if_gate_return" or slot_name == "G_else_gate_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
      
    else:
        if slot_name != "null" and (temp_slot != slot_name or gate_name != temp_gate):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "B_if_gate_return":
                $ attempts +=1
                if gate_name == "B_if_gate":
                    $ if1x = 1395
                    $ if1y = 645
                    $ if1in1 = False
                    $ if1in2 = False
                    $ if1in3 = False
            if slot_name == "G_if_gate_return":
                $ attempts +=1
                if gate_name == "G_if_gate":
                    $ if2x = 1525
                    $ if2y = 645
                    $ if2in1 = False
                    $ if2in2 = False
                    $ if2in3 = False
            if slot_name == "G_else_gate_return":
                $ attempts +=1
                if gate_name == "G_else_gate":
                    $ else1x = 1655
                    $ else1y = 645
                    $ else1in1 = False
                    $ else1in2 = False
                    $ else1in3 = False


#*******************************************
#************image zone********************* 
#*******************************************

#    #if 1 section*******************************************************************************************     
    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    
    if if2in2 == True:
        image LLE_3_tile34 = "G_vertical_short.png"
        show LLE_3_tile34 at Position(xpos = 331, xanchor = 0, ypos = 516, yanchor = 0)
        image LLE_3_tile35 = "G_vertical_ll.png"
        show LLE_3_tile35 at Position(xpos = 365, xanchor = 0, ypos = 670, yanchor = 0)
        image LLE_3_tile36 = "G_end_on.png"
        show LLE_3_tile36 at Position(xpos = 332, xanchor = 0, ypos = 745, yanchor = 0)
        if (light2Sound ==0):
            play soundP02 llLightOn2
            $light2Sound +=1
        
        if else1in3 == True:
            image LLE_3_tile37 = "B_connect_node.png"
            show LLE_3_tile37 at Position(xpos = 398, xanchor = 0, ypos = 482, yanchor = 0)
            #show LLE_2_tile38 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLE_3_tile38 = "B_horizontal.png"
            show LLE_3_tile38 at Position(xpos = 429, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile39 = "B_horizontal.png"
            show LLE_3_tile39 at Position(xpos = 503, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile40 = "B_horizontal.png"
            show LLE_3_tile40 at Position(xpos = 578, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile41 = "B_horizontal.png"
            show LLE_3_tile41 at Position(xpos = 753, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile42 = "B_horizontal.png"
            show LLE_3_tile42 at Position(xpos = 828, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile43 = "B_end_on.png"
            show LLE_3_tile43 at Position(xpos = 903, xanchor = 0, ypos = 454, yanchor = 0)
            if (light3Sound ==0):
                play soundP03 llLightOn3
                $light3Sound+=1

        if else1in3 == False:
            hide LLE_3_tile37
            hide LLE_3_tile38
            hide LLE_3_tile39
            hide LLE_3_tile40
            hide LLE_3_tile41
            hide LLE_3_tile42
            hide LLE_3_tile43
            if (light3Sound ==1):
                play soundP03 llLightOff3
                $light3Sound -=1
                
        if if1in3 == True:
            image LLE_3_tile71 = "B_connect_node.png"
            show LLE_3_tile71 at Position(xpos = 398, xanchor = 0, ypos = 482, yanchor = 0)
            image LLE_3_tile67 = "B_horizontal.png"
            show LLE_3_tile67 at Position(xpos = 429, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile68 = "B_horizontal.png"
            show LLE_3_tile68 at Position(xpos = 503, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile69 = "B_horizontal.png"
            show LLE_3_tile69 at Position(xpos = 578, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile81 = "B_horizontal.png"
            show LLE_3_tile81 at Position(xpos = 753, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile82 = "B_horizontal.png"
            show LLE_3_tile82 at Position(xpos = 828, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile83 = "B_end_on.png"
            show LLE_3_tile83 at Position(xpos = 903, xanchor = 0, ypos = 454, yanchor = 0)
            if (light3Sound ==0):
                play soundP03 llLightOn3
                $light3Sound+=1
                
        if if1in3 == False:
            hide LLE_3_tile71
            hide LLE_3_tile67
            hide LLE_3_tile68
            hide LLE_3_tile69
            hide LLE_3_tile81
            hide LLE_3_tile82
            hide LLE_3_tile83
            if (light3Sound ==1):
                play soundP03 llLightOff3
                $light3Sound -=1
                
    if if2in2 == False:
        hide LLE_3_tile34
        hide LLE_3_tile35
        hide LLE_3_tile36
        hide LLE_3_tile37
        hide LLE_3_tile38
        hide LLE_3_tile39
        hide LLE_3_tile40
        hide LLE_3_tile41
        hide LLE_3_tile42
        hide LLE_3_tile43
        hide LLE_3_tile71
        hide LLE_3_tile67
        hide LLE_3_tile68
        hide LLE_3_tile69
        hide LLE_3_tile81
        hide LLE_3_tile82
        hide LLE_3_tile83
        if (light2Sound ==1):
            play soundP02 llLightOff2
            $light2Sound -=1

    if if1in1 == True:
        image LLE_3_tile46 = "B_horizontal.png"
        show LLE_3_tile46 at Position(xpos = 755, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile47 = "B_horizontal.png"
        show LLE_3_tile47 at Position(xpos = 830, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile48 = "B_end_on.png"
        show LLE_3_tile48 at Position(xpos = 905, xanchor = 0, ypos = 240, yanchor = 0)
        image LLE_3_tile49 = "B_horizontal.png"
        show LLE_3_tile49 at Position(xpos = 430, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile50 = "B_horizontal.png"
        show LLE_3_tile50 at Position(xpos = 505, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile51 = "B_horizontal.png"
        show LLE_3_tile51 at Position(xpos = 580, xanchor = 0, ypos = 275, yanchor = 0)
        if (light1Sound ==0):
            play soundP01 llLightOn1
            $light1Sound +=1
            
    if if1in1 == False:
        hide LLE_3_tile46
        hide LLE_3_tile47
        hide LLE_3_tile48
        hide LLE_3_tile49
        hide LLE_3_tile50
        hide LLE_3_tile51

    if if2in1 == True:
        image LLE_3_tile61 = "G_horizontal_ll.png"
        show LLE_3_tile61 at Position(xpos = 430, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile62 = "G_horizontal_ll.png"
        show LLE_3_tile62 at Position(xpos = 505, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile63 = "G_horizontal_ll.png"
        show LLE_3_tile63 at Position(xpos = 580, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile90 = "G_horizontal_ll.png"
        show LLE_3_tile90 at Position(xpos = 755, xanchor = 0, ypos = 275, yanchor = 0)
        image LLE_3_tile91 = "G_horizontal_ll.png"
        show LLE_3_tile91 at Position(xpos = 830, xanchor = 0, ypos = 275, yanchor = 0)
        
    if if2in1 == False:
        hide LLE_3_tile61
        hide LLE_3_tile62
        hide LLE_3_tile63
        hide LLE_3_tile90
        hide LLE_3_tile91
        if (light1Sound ==1):
            play soundP01 llLightOff1
            $light1Sound -=1
            
    if if1in2 == True:
        image LLE_3_tile70 = "B_vertical_short.png"
        show LLE_3_tile70 at Position(xpos = 397, xanchor = 0, ypos = 516, yanchor = 0)
        image LLE_3_tile92 = "B_vertical.png"
        show LLE_3_tile92 at Position(xpos = 365, xanchor = 0, ypos = 670, yanchor = 0)

        if if2in3 == True or else1in3 == True:
            image LLE_3_tile64 = "G_horizontal_ll.png"
            show LLE_3_tile64 at Position(xpos = 430, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile65 = "G_horizontal_ll.png"
            show LLE_3_tile65 at Position(xpos = 505, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile66 = "G_horizontal_ll.png"
            show LLE_3_tile66 at Position(xpos = 580, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile72 = "G_connect_node.png"
            show LLE_3_tile72 at Position(xpos = 397, xanchor = 0, ypos = 483, yanchor = 0)
            image LLE_3_tile73 = "G_connect_pipe.png"
            show LLE_3_tile73 at Position(xpos = 353, xanchor = 0, ypos = 495, yanchor = 0)
            image LLE_3_tile74 = "G_connect_node.png"
            show LLE_3_tile74 at Position(xpos = 329, xanchor = 0, ypos = 483, yanchor = 0)
            image LLE_3_tile93 = "G_horizontal_ll.png"
            show LLE_3_tile93 at Position(xpos = 753, xanchor = 0, ypos = 485, yanchor = 0)
            image LLE_3_tile94 = "G_horizontal_ll.png"
            show LLE_3_tile94 at Position(xpos = 828, xanchor = 0, ypos = 485, yanchor = 0)
        
        if if2in3 == False and else1in3 == False:
            hide LLE_3_tile64
            hide LLE_3_tile65
            hide LLE_3_tile66
            hide LLE_3_tile72
            hide LLE_3_tile73
            hide LLE_3_tile74
            hide LLE_3_tile93
            hide LLE_3_tile94

    if if1in2 == False:
        hide LLE_3_tile70
        hide LLE_3_tile64
        hide LLE_3_tile65
        hide LLE_3_tile66
        hide LLE_3_tile72
        hide LLE_3_tile73
        hide LLE_3_tile74
        hide LLE_3_tile92
        hide LLE_3_tile93
        hide LLE_3_tile94


        
#win conditions ********
    if (if2in2 == True) and else1in3 == True and (if1in1 == True):
        image LLE_3_tile55 = "G_end_on.png"
        show LLE_3_tile55 at Position(xpos = 332, xanchor = 0, ypos = 745, yanchor = 0)
        image LLE_3_tile56 = "B_end_on.png"
        show LLE_3_tile56 at Position(xpos = 906, xanchor = 0, ypos = 454, yanchor = 0)
        image LLE_3_tile57 = "B_end_on.png"
        show LLE_3_tile57 at Position(xpos = 906, xanchor = 0, ypos = 239, yanchor = 0)
        image LLE_3_tile58 = "B_if.png"
        show LLE_3_tile58 at Position(xpos = 655, xanchor = 0, ypos = 240, yanchor = 0)
        image LLE_3_tile59 = "G_if.png"
        show LLE_3_tile59 at Position(xpos = 330, xanchor = 0, ypos = 565, yanchor = 0)
        image LLE_3_tile60 = "G_else.png"
        show LLE_3_tile60 at Position(xpos = 655, xanchor = 0, ypos = 455, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        hide LLE_3_tile55
        hide LLE_3_tile56
        hide LLE_3_tile57
        hide LLE_3_tile58
        hide LLE_3_tile59
        hide LLE_3_tile60
        jump llEasyWin
    
    if attempts == 0:
        show LLE_3_tile58 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLE_3_tile59 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLE_3_tile60 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        $loopLogicEasy_tries +=1
        hide LLE_3_tile58
        hide LLE_3_tile59
        hide LLE_3_tile60
        jump llEasyLose
    
    jump gamefile_lle3

screen loopLogic_easy3Scr:
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
        xpos 1545
        ypos 220
        focus_mask True
        action Jump("loopLogic_EasyHints3")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 1463
        ypos 295
    text "Moves" xpos 1480 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1605 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1640 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #if gates
            drag:
                drag_name "B_if_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos if1x ypos if1y
            drag:
                drag_name "G_if_gate"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos if2x ypos if2y  
            #else gate
            drag:
                drag_name "G_else_gate"
                child "G_Else.png"
                droppable False
                dragged gate_dragged
                xpos else1x ypos else1y

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover2.png" 
                #child "Placeholder2.png"
                draggable False
                xpos gate1x-25 ypos gate1y-25
           
            drag:
                drag_name "gate slot two"
                child "cover2.png" 
                #child "Placeholder2.png"
                draggable False
                xpos gate2x-25 ypos gate2y-25
                
            drag:
                drag_name "gate slot three"
                child "cover2.png" 
                #child "Placeholder2.png"
                draggable False
                xpos gate3x-25 ypos gate3y-25

            drag:
                drag_name "B_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1385 ypos 634
          
            drag:
                drag_name "G_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 634

            drag:
                drag_name "G_else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1645 ypos 634

