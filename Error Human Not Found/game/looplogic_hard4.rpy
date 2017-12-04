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

label loopLogic_hard4: #start
    $config.skipping=None
    $quick_menu = False
    $game_menu = True
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg looplogic_bg

    #Left of Start
    image LLH_4_tile1 = "R_horizontal_ll.png"
    show LLH_4_tile1 at Position(xpos = 425, xanchor = 0, ypos = 660, yanchor = 0)
    image LLH_4_tile2 = "G_horizontal_ll.png"
    show LLH_4_tile2 at Position(xpos = 425, xanchor = 0, ypos = 690, yanchor = 0)
    image LLH_4_tile3 = "B_horizontal.png"
    show LLH_4_tile3 at Position(xpos = 425, xanchor = 0, ypos = 720, yanchor = 0)
    image LLH_4_tile4 = "R_horizontal_ll.png"
    show LLH_4_tile4 at Position(xpos = 350, xanchor = 0, ypos = 660, yanchor = 0)
    image LLH_4_tile5 = "G_horizontal_ll.png"
    show LLH_4_tile5 at Position(xpos = 350, xanchor = 0, ypos = 690, yanchor = 0)
    image LLH_4_tile6 = "B_horizontal.png"
    show LLH_4_tile6 at Position(xpos = 350, xanchor = 0, ypos = 720, yanchor = 0)

    #Right of Start
    image LLH_4_tile7 = "R_horizontal_ll.png"
    show LLH_4_tile7 at Position(xpos = 575, xanchor = 0, ypos = 660, yanchor = 0)
    image LLH_4_tile8 = "G_horizontal_ll.png"
    show LLH_4_tile8 at Position(xpos = 575, xanchor = 0, ypos = 690, yanchor = 0)
    image LLH_4_tile9 = "B_horizontal.png"
    show LLH_4_tile9 at Position(xpos = 575, xanchor = 0, ypos = 720, yanchor = 0)
    
    #Down of Left Blue End
    image LLH_4_tile10 = "W_vertical.png"
    show LLH_4_tile10 at Position(xpos = 135, xanchor = 0, ypos = 585, yanchor = 0)
    
    #Right of Gate Bottom from Left Blue End
    image LLH_4_tile11 = "W_horizontal.png"
    show LLH_4_tile11 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
    
    #Up of Gate Left of Start
    image LLH_4_tile12 = "W_vertical.png"
    show LLH_4_tile12 at Position(xpos = 285, xanchor = 0, ypos = 585, yanchor = 0)

    #Up of Start
    image LLH_4_tile13 = "R_vertical_ll.png"
    show LLH_4_tile13 at Position(xpos = 470, xanchor = 0, ypos = 585, yanchor = 0)
    image LLH_4_tile14 = "G_vertical_ll.png"
    show LLH_4_tile14 at Position(xpos = 507, xanchor = 0, ypos = 585, yanchor = 0)
    image LLH_4_tile15 = "B_vertical.png"
    show LLH_4_tile15 at Position(xpos = 550, xanchor = 0, ypos = 585, yanchor = 0)
    image LLH_4_tile61 = "W_vertical.png"
    show LLH_4_tile61 at Position(xpos = 470, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_4_tile62 = "G_vertical_ll.png"
    show LLH_4_tile62 at Position(xpos = 507, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_4_tile63 = "B_vertical.png"
    show LLH_4_tile63 at Position(xpos = 550, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_4_tile72 = "W_connect_pipe.png"
    show LLH_4_tile72 at Position(xpos = 480, xanchor = 0, ypos = 500, yanchor = 0)
    image LLH_4_tile73 = "W_connect_pipe.png"
    show LLH_4_tile73 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
    image LLH_4_tile21 = "W_vertical.png"
    show LLH_4_tile21 at Position(xpos = 470, xanchor = 0, ypos = 425, yanchor = 0)
    image LLH_4_tile22 = "W_vertical.png"
    show LLH_4_tile22 at Position(xpos = 510, xanchor = 0, ypos = 425, yanchor = 0)
    image LLH_4_tile23 = "W_vertical.png"
    show LLH_4_tile23 at Position(xpos = 550, xanchor = 0, ypos = 425, yanchor = 0)
    
    #Right of Left Red End
    image LLH_4_tile24 = "W_horizontal.png"
    show LLH_4_tile24 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
    image LLH_4_tile70 = "W_horizontal.png"
    show LLH_4_tile70 at Position(xpos = 325, xanchor = 0, ypos = 360, yanchor = 0)
    
    #Dotted Line
    image LLH_4_tile27 = "y_horizontal_short_off.png"
    show LLH_4_tile27 at Position(xpos = 320, xanchor = 0, ypos = 555, yanchor = 0)
    image LLH_4_tile28 = "y_horizontal_short_off.png"
    show LLH_4_tile28 at Position(xpos = 380, xanchor = 0, ypos = 555, yanchor = 0)
    image LLH_4_tile29 = "y_horizontal_short_off.png"
    show LLH_4_tile29 at Position(xpos = 440, xanchor = 0, ypos = 555, yanchor = 0)
    
    #Right of Gate Right of Start
    image LLH_4_tile30 = "W_horizontal_short.png"
    show LLH_4_tile30 at Position(xpos = 725, xanchor = 0, ypos = 665, yanchor = 0)
    image LLH_4_tile31 = "W_horizontal_short.png"
    show LLH_4_tile31 at Position(xpos = 725, xanchor = 0, ypos = 715, yanchor = 0)
    image LLH_4_tile32 = "W_connect_pipe_vertical.png"
    show LLH_4_tile32 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
    image LLH_4_tile33 = "W_horizontal_short.png"
    show LLH_4_tile33 at Position(xpos = 800, xanchor = 0, ypos = 665, yanchor = 0)
    image LLH_4_tile34 = "W_horizontal_short.png"
    show LLH_4_tile34 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
    
    #Left of Bottom Green End
    image LLH_4_tile35 = "W_horizontal.png"
    show LLH_4_tile35 at Position(xpos = 950, xanchor = 0, ypos = 690, yanchor = 0)
    
    #Up of Right Connector
    image LLH_4_tile36 = "W_vertical.png"
    show LLH_4_tile36 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
    image LLH_4_tile37 = "W_vertical.png"
    show LLH_4_tile37 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
    image LLH_4_tile38 = "W_corner_RB.png"
    show LLH_4_tile38 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
    image LLH_4_tile39 = "W_horizontal_short.png"
    show LLH_4_tile39 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
    
    #Left of Right Red End
    image LLH_4_tile40 = "W_horizontal.png"
    show LLH_4_tile40 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
    
    #Right of Top Connector Top of Start
    image LLH_4_tile67 = "W_horizontal.png"
    show LLH_4_tile67 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
    image LLH_4_tile69 = "W_vertical_short.png"
    show LLH_4_tile69 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
    image LLH_4_tile68 = "W_corner_LT.png"
    show LLH_4_tile68 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)

    #Left of Right Blue End
    image LLH_4_tile45 = "W_horizontal.png"
    show LLH_4_tile45 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
    image LLH_4_tile46 = "W_horizontal.png"
    show LLH_4_tile46 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
    
    #*********************************************************
    #********************* start points **********************
    #*********************************************************
    image LLH_4_Start = "Start.png"
    show LLH_4_Start at Position(xpos = 475, xanchor = 0, ypos = 655, yanchor = 0)
    
    #*********************************************************
    #********************** end points ***********************
    #*********************************************************    
    image LLH_4_BlueEnd1 = "B_end_off.png"
    show LLH_4_BlueEnd1 at Position(xpos = 850, xanchor = 0, ypos = 325, yanchor = 0)
    image LLH_4_BlueEnd2 = "B_end_off.png"
    show LLH_4_BlueEnd2 at Position(xpos = 100, xanchor = 0, ypos = 505, yanchor = 0)
    image LLH_4_GreenEnd = "G_end_off.png"
    show LLH_4_GreenEnd at Position(xpos = 1000, xanchor = 0, ypos = 655, yanchor = 0)
    image LLH_4_RedEnd1 = "R_end_off.png"
    show LLH_4_RedEnd1 at Position(xpos = 250, xanchor = 0, ypos = 325, yanchor = 0)
    image LLH_4_RedEnd2 = "R_end_off.png"
    show LLH_4_RedEnd2 at Position(xpos = 1000, xanchor = 0, ypos = 455, yanchor = 0)

    #*********************************************************
    #********************* connect nodes *********************
    #*********************************************************          
    #Top Connector Top of Start
    image LLH_4_tile64 = "W_connect_node.png"
    show LLH_4_tile64 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0)
    image LLH_4_tile65 = "W_connect_node.png"
    show LLH_4_tile65 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0)
    image LLH_4_tile66 = "W_connect_node.png"
    show LLH_4_tile66 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0)
    
    #While Connector
    image LLH_4_tile50 = "g_while_off.png"
    show LLH_4_tile50 at Position(xpos = 467, xanchor = 0, ypos = 555, yanchor = 0)
    
    #Right Connector
    image LLH_4_tile51 = "W_connect_node.png"
    show LLH_4_tile51 at Position(xpos = 773, xanchor = 0, ypos = 663, yanchor = 0)
    image LLH_4_tile52 = "W_connect_node.png"
    show LLH_4_tile52 at Position(xpos = 773, xanchor = 0, ypos = 715, yanchor = 0)
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    #initial value assignment for dragables
    $ whileGx = 1445
    $ whileGy = 500
    $ elsex = 1585
    $ elsey = 500
    $ ifRx = 1395
    $ ifRy = 645
    $ ifGx = 1525
    $ ifGy = 645
    $ ifB1x = 1655
    $ ifB1y = 645
    $ ifB2x = 1655
    $ ifB2y = 645
    $ ifGRx = 1445
    $ ifGRy = 790
    $ ifBGx = 1585
    $ ifBGy = 790
    

    $ gate1x = 475
    $ gate1y = 325
    $ gate2x = 625
    $ gate2y = 325
    $ gate3x = 850
    $ gate3y = 455
    $ gate4x = 250
    $ gate4y = 515
    $ gate5x = 100
    $ gate5y = 655
    $ gate6x = 250
    $ gate6y = 655
    $ gate7x = 625
    $ gate7y = 655
    $ gate8x = 850
    $ gate8y = 655
    
    image LLH_4_ifRT = "R_if_idle.png"
    image LLH_4_ifGT = "G_if_idle.png"
    image LLH_4_ifBT = "B_if_idle.png"
    image LLH_4_ifGRT = "RG_if_idle.png"
    image LLH_4_ifBGT = "BG_if_idle.png"
    image LLH_4_elseT = "G_else_idle.png"
    image LLH_4_whileGT = "G_while_idle.png"
    show LLH_4_ifRT at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_4_ifGT at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_4_ifBT at Position(xpos = ifB1x, xanchor = 0, ypos = ifB1y, yanchor = 0)
    show LLH_4_ifGRT at Position(xpos = ifGRx, xanchor = 0, ypos = ifGRy, yanchor = 0)
    show LLH_4_ifBGT at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
    show LLH_4_elseT at Position(xpos = elsex, xanchor = 0, ypos = elsey, yanchor = 0)
    show LLH_4_whileGT at Position(xpos = whileGx, xanchor = 0, ypos = whileGy, yanchor = 0)
    
   
    # check conditons for locations
    $ whileGin1 = False
    $ whileGin2 = False
    $ whileGin3 = False
    $ whileGin4 = False
    $ whileGin5 = False
    $ whileGin6 = False
    $ whileGin7 = False
    $ whileGin8 = False

    $ elsein1 = False
    $ elsein2 = False
    $ elsein3 = False
    $ elsein4 = False
    $ elsein5 = False
    $ elsein6 = False
    $ elsein7 = False
    $ elsein8 = False
    
    $ ifRin1 = False
    $ ifRin2 = False
    $ ifRin3 = False
    $ ifRin4 = False
    $ ifRin5 = False
    $ ifRin6 = False
    $ ifRin7 = False
    $ ifRin8 = False
    
    $ ifGin1 = False
    $ ifGin2 = False
    $ ifGin3 = False
    $ ifGin4 = False
    $ ifGin5 = False
    $ ifGin6 = False
    $ ifGin7 = False
    $ ifGin8 = False
    
    $ ifB1in1 = False
    $ ifB1in2 = False
    $ ifB1in3 = False
    $ ifB1in4 = False
    $ ifB1in5 = False
    $ ifB1in6 = False
    $ ifB1in7 = False
    $ ifB1in8 = False
    
    $ ifB2in1 = False
    $ ifB2in2 = False
    $ ifB2in3 = False
    $ ifB2in4 = False
    $ ifB2in5 = False
    $ ifB2in6 = False
    $ ifB2in7 = False
    $ ifB2in8 = False
    
    $ ifGRin1 = False
    $ ifGRin2 = False
    $ ifGRin3 = False
    $ ifGRin4 = False
    $ ifGRin5 = False
    $ ifGRin6 = False
    $ ifGRin7 = False
    $ ifGRin8 = False
    
    $ ifBGin1 = False
    $ ifBGin2 = False
    $ ifBGin3 = False
    $ ifBGin4 = False
    $ ifBGin5 = False
    $ ifBGin6 = False
    $ ifBGin7 = False
    $ ifBGin8 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
     
    #attempts for players
    $ attempts = 12    
    
    #*********************************************************
    #********************** show gates ***********************
    #*********************************************************  
    image LLH_4_tile53 = "blank_node.png"
    show LLH_4_tile53 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
    image LLH_4_tile54 = "blank_node.png"
    show LLH_4_tile54 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
    image LLH_4_tile55 = "blank_node.png"
    show LLH_4_tile55 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
    image LLH_4_tile56 = "blank_node.png"
    show LLH_4_tile56 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
    image LLH_4_tile57 = "blank_node.png"
    show LLH_4_tile57 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
    image LLH_4_tile58 = "blank_node.png"
    show LLH_4_tile58 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
    image LLH_4_tile59 = "blank_node.png"
    show LLH_4_tile59 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
    image LLH_4_tile60 = "blank_node.png"
    show LLH_4_tile60 at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
 
    jump gamefile_llh4
    
    
label gamefile_llh4:
    
    #calls game screen
    call screen loopLogicHard_4Scr




#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "if_R_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ ifRx = gate1x
            $ ifRy = gate1y
            $ ifRin1 = True
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ ifRx = gate2x
            $ ifRy = gate2y
            $ ifRin1 = False
            $ ifRin2 = True
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ ifRx = gate3x
            $ ifRy = gate3y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = True
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ ifRx = gate4x
            $ ifRy = gate4y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = True
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ ifRx = gate5x
            $ ifRy = gate5y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = True
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ ifRx = gate6x
            $ ifRy = gate6y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = True
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ ifRx = gate7x
            $ ifRy = gate7y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = True
            $ ifRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ ifRx = gate8x
            $ ifRy = gate8y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = True
      
      
    #the second logic gate *******************************************************************************
    if gate_name == "if_G_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ ifGx = gate1x
            $ ifGy = gate1y
            $ ifGin1 = True
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ ifGx = gate2x
            $ ifGy = gate2y
            $ ifGin1 = False
            $ ifGin2 = True
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ ifGx = gate3x
            $ ifGy = gate3y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = True
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ ifGx = gate4x
            $ ifGy = gate4y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = True
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ ifGx = gate5x
            $ ifGy = gate5y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = True
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ ifGx = gate6x
            $ ifGy = gate6y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = True
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ ifGx = gate7x
            $ ifGy = gate7y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = True
            $ ifGin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ ifGx = gate8x
            $ ifGy = gate8y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = True
            
            
    #the third logic gate *******************************************************************************
    if gate_name == "if_B1_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ ifB1x = gate1x
            $ ifB1y = gate1y
            $ ifB1in1 = True
            $ ifB1in2 = False
            $ ifB1in3 = False
            $ ifB1in4 = False
            $ ifB1in5 = False
            $ ifB1in6 = False
            $ ifB1in7 = False
            $ ifB1in8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ ifB1x = gate2x
            $ ifB1y = gate2y
            $ ifB1in1 = False
            $ ifB1in2 = True
            $ ifB1in3 = False
            $ ifB1in4 = False
            $ ifB1in5 = False
            $ ifB1in6 = False
            $ ifB1in7 = False
            $ ifB1in8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ ifB1x = gate3x
            $ ifB1y = gate3y
            $ ifB1in1 = False
            $ ifB1in2 = False
            $ ifB1in3 = True
            $ ifB1in4 = False
            $ ifB1in5 = False
            $ ifB1in6 = False
            $ ifB1in7 = False
            $ ifB1in8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ ifB1x = gate4x
            $ ifB1y = gate4y
            $ ifB1in1 = False
            $ ifB1in2 = False
            $ ifB1in3 = False
            $ ifB1in4 = True
            $ ifB1in5 = False
            $ ifB1in6 = False
            $ ifB1in7 = False
            $ ifB1in8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ ifB1x = gate5x
            $ ifB1y = gate5y
            $ ifB1in1 = False
            $ ifB1in2 = False
            $ ifB1in3 = False
            $ ifB1in4 = False
            $ ifB1in5 = True
            $ ifB1in6 = False
            $ ifB1in7 = False
            $ ifB1in8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ ifB1x = gate6x
            $ ifB1y = gate6y
            $ ifB1in1 = False
            $ ifB1in2 = False
            $ ifB1in3 = False
            $ ifB1in4 = False
            $ ifB1in5 = False
            $ ifB1in6 = True
            $ ifB1in7 = False
            $ ifB1in8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ ifB1x = gate7x
            $ ifB1y = gate7y
            $ ifB1in1 = False
            $ ifB1in2 = False
            $ ifB1in3 = False
            $ ifB1in4 = False
            $ ifB1in5 = False
            $ ifB1in6 = False
            $ ifB1in7 = True
            $ ifB1in8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ ifB1x = gate8x
            $ ifB1y = gate8y
            $ ifB1in1 = False
            $ ifB1in2 = False
            $ ifB1in3 = False
            $ ifB1in4 = False
            $ ifB1in5 = False
            $ ifB1in6 = False
            $ ifB1in7 = False
            $ ifB1in8 = True

    #the fourth logic gate *******************************************************************************
    if gate_name == "if_B2_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ ifB2x = gate1x
            $ ifB2y = gate1y
            $ ifB2in1 = True
            $ ifB2in2 = False
            $ ifB2in3 = False
            $ ifB2in4 = False
            $ ifB2in5 = False
            $ ifB2in6 = False
            $ ifB2in7 = False
            $ ifB2in8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ ifB2x = gate2x
            $ ifB2y = gate2y
            $ ifB2in1 = False
            $ ifB2in2 = True
            $ ifB2in3 = False
            $ ifB2in4 = False
            $ ifB2in5 = False
            $ ifB2in6 = False
            $ ifB2in7 = False
            $ ifB2in8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ ifB2x = gate3x
            $ ifB2y = gate3y
            $ ifB2in1 = False
            $ ifB2in2 = False
            $ ifB2in3 = True
            $ ifB2in4 = False
            $ ifB2in5 = False
            $ ifB2in6 = False
            $ ifB2in7 = False
            $ ifB2in8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ ifB2x = gate4x
            $ ifB2y = gate4y
            $ ifB2in1 = False
            $ ifB2in2 = False
            $ ifB2in3 = False
            $ ifB2in4 = True
            $ ifB2in5 = False
            $ ifB2in6 = False
            $ ifB2in7 = False
            $ ifB2in8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ ifB2x = gate5x
            $ ifB2y = gate5y
            $ ifB2in1 = False
            $ ifB2in2 = False
            $ ifB2in3 = False
            $ ifB2in4 = False
            $ ifB2in5 = True
            $ ifB2in6 = False
            $ ifB2in7 = False
            $ ifB2in8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ ifB2x = gate6x
            $ ifB2y = gate6y
            $ ifB2in1 = False
            $ ifB2in2 = False
            $ ifB2in3 = False
            $ ifB2in4 = False
            $ ifB2in5 = False
            $ ifB2in6 = True
            $ ifB2in7 = False
            $ ifB2in8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ ifB2x = gate7x
            $ ifB2y = gate7y
            $ ifB2in1 = False
            $ ifB2in2 = False
            $ ifB2in3 = False
            $ ifB2in4 = False
            $ ifB2in5 = False
            $ ifB2in6 = False
            $ ifB2in7 = True
            $ ifB2in8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ ifB2x = gate8x
            $ ifB2y = gate8y
            $ ifB2in1 = False
            $ ifB2in2 = False
            $ ifB2in3 = False
            $ ifB2in4 = False
            $ ifB2in5 = False
            $ ifB2in6 = False
            $ ifB2in7 = False
            $ ifB2in8 = True

    #the fifth logic gate *******************************************************************************
    if gate_name == "if_GR_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ ifGRx = gate1x
            $ ifGRy = gate1y
            $ ifGRin1 = True
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ ifGRx = gate2x
            $ ifGRy = gate2y
            $ ifGRin1 = False
            $ ifGRin2 = True
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ ifGRx = gate3x
            $ ifGRy = gate3y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = True
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ ifGRx = gate4x
            $ ifGRy = gate4y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = True
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ ifGRx = gate5x
            $ ifGRy = gate5y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = True
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ ifGRx = gate6x
            $ ifGRy = gate6y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = True
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ ifGRx = gate7x
            $ ifGRy = gate7y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = True
            $ ifGRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ ifGRx = gate8x
            $ ifGRy = gate8y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = True
            
            
    #the sixth logic gate *******************************************************************************
    if gate_name == "if_BG_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ ifBGx = gate1x
            $ ifBGy = gate1y
            $ ifBGin1 = True
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ ifBGx = gate2x
            $ ifBGy = gate2y
            $ ifBGin1 = False
            $ ifBGin2 = True
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ ifBGx = gate3x
            $ ifBGy = gate3y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = True
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ ifBGx = gate4x
            $ ifBGy = gate4y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = True
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ ifBGx = gate5x
            $ ifBGy = gate5y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = True
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ ifBGx = gate6x
            $ ifBGy = gate6y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = True
            $ ifBGin7 = False
            $ ifBGin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ ifBGx = gate7x
            $ ifBGy = gate7y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = True
            $ ifBGin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ ifBGx = gate8x
            $ ifBGy = gate8y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = True
            
            
    #the seventh logic gate *******************************************************************************
    if gate_name == "else_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileGin1 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin1 = False

            #sets values for checks
            $ elsex = gate1x
            $ elsey = gate1y
            $ elsein1 = True
            $ elsein2 = False
            $ elsein3 = False
            $ elsein4 = False
            $ elsein5 = False
            $ elsein6 = False
            $ elsein7 = False
            $ elsein8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileGin2 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin2 = False

            #sets values for checks
            $ elsex = gate2x
            $ elsey = gate2y
            $ elsein1 = False
            $ elsein2 = True
            $ elsein3 = False
            $ elsein4 = False
            $ elsein5 = False
            $ elsein6 = False
            $ elsein7 = False
            $ elsein8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileGin3 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin3 = False

            #sets values for checks
            $ elsex = gate3x
            $ elsey = gate3y
            $ elsein1 = False
            $ elsein2 = False
            $ elsein3 = True
            $ elsein4 = False
            $ elsein5 = False
            $ elsein6 = False
            $ elsein7 = False
            $ elsein8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileGin4 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin4 = False

            #sets values for checks
            $ elsex = gate4x
            $ elsey = gate4y
            $ elsein1 = False
            $ elsein2 = False
            $ elsein3 = False
            $ elsein4 = True
            $ elsein5 = False
            $ elsein6 = False
            $ elsein7 = False
            $ elsein8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileGin5 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin5 = False

            #sets values for checks
            $ elsex = gate5x
            $ elsey = gate5y
            $ elsein1 = False
            $ elsein2 = False
            $ elsein3 = False
            $ elsein4 = False
            $ elsein5 = True
            $ elsein6 = False
            $ elsein7 = False
            $ elsein8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileGin6 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin6 = False

            #sets values for checks
            $ elsex = gate6x
            $ elsey = gate6y
            $ elsein1 = False
            $ elsein2 = False
            $ elsein3 = False
            $ elsein4 = False
            $ elsein5 = False
            $ elsein6 = True
            $ elsein7 = False
            $ elsein8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileGin7 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin7 = False

            #sets values for checks
            $ elsex = gate7x
            $ elsey = gate7y
            $ elsein1 = False
            $ elsein2 = False
            $ elsein3 = False
            $ elsein4 = False
            $ elsein5 = False
            $ elsein6 = False
            $ elsein7 = True
            $ elsein8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileGin8 == True:
                $ whileGx = 1445
                $ whileGy = 500
                $ whileGin8 = False

            #sets values for checks
            $ elsex = gate8x
            $ elsey = gate8y
            $ elsein1 = False
            $ elsein2 = False
            $ elsein3 = False
            $ elsein4 = False
            $ elsein5 = False
            $ elsein6 = False
            $ elsein7 = False
            $ elsein8 = True


    #the eighth logic gate *******************************************************************************
    if gate_name == "while_G_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifB1in1 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in1 = False
            if ifB2in1 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if elsein1 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein1 = False

            #sets values for checks
            $ whileGx = gate1x
            $ whileGy = gate1y
            $ whileGin1 = True
            $ whileGin2 = False
            $ whileGin3 = False
            $ whileGin4 = False
            $ whileGin5 = False
            $ whileGin6 = False
            $ whileGin7 = False
            $ whileGin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifB1in2 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in2 = False
            if ifB2in2 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if elsein2 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein2 = False

            #sets values for checks
            $ whileGx = gate2x
            $ whileGy = gate2y
            $ whileGin1 = False
            $ whileGin2 = True
            $ whileGin3 = False
            $ whileGin4 = False
            $ whileGin5 = False
            $ whileGin6 = False
            $ whileGin7 = False
            $ whileGin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifB1in3 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in3 = False
            if ifB2in3 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if elsein3 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein3 = False

            #sets values for checks
            $ whileGx = gate3x
            $ whileGy = gate3y
            $ whileGin1 = False
            $ whileGin2 = False
            $ whileGin3 = True
            $ whileGin4 = False
            $ whileGin5 = False
            $ whileGin6 = False
            $ whileGin7 = False
            $ whileGin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifB1in4 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in4 = False
            if ifB2in4 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if elsein4 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein4 = False

            #sets values for checks
            $ whileGx = gate4x
            $ whileGy = gate4y
            $ whileGin1 = False
            $ whileGin2 = False
            $ whileGin3 = False
            $ whileGin4 = True
            $ whileGin5 = False
            $ whileGin6 = False
            $ whileGin7 = False
            $ whileGin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifB1in5 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in5 = False
            if ifB2in5 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if elsein5 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein5 = False

            #sets values for checks
            $ whileGx = gate5x
            $ whileGy = gate5y
            $ whileGin1 = False
            $ whileGin2 = False
            $ whileGin3 = False
            $ whileGin4 = False
            $ whileGin5 = True
            $ whileGin6 = False
            $ whileGin7 = False
            $ whileGin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifB1in6 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in6 = False
            if ifB2in6 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if elsein6 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein6 = False

            #sets values for checks
            $ whileGx = gate6x
            $ whileGy = gate6y
            $ whileGin1 = False
            $ whileGin2 = False
            $ whileGin3 = False
            $ whileGin4 = False
            $ whileGin5 = False
            $ whileGin6 = True
            $ whileGin7 = False
            $ whileGin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifB1in7 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in7 = False
            if ifB2in7 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if elsein7 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein7 = False

            #sets values for checks
            $ whileGx = gate7x
            $ whileGy = gate7y
            $ whileGin1 = False
            $ whileGin2 = False
            $ whileGin3 = False
            $ whileGin4 = False
            $ whileGin5 = False
            $ whileGin6 = False
            $ whileGin7 = True
            $ whileGin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifB1in8 == True:
                $ ifB1x = 1655
                $ ifB1y = 645
                $ ifB1in8 = False
            if ifB2in8 == True:
                $ ifB2x = 1655
                $ ifB2y = 645
                $ ifB2in8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if elsein8 == True:
                $ elsex = 1585
                $ elsey = 500
                $ elsein8 = False

            #sets values for checks
            $ whileGx = gate8x
            $ whileGy = gate8y
            $ whileGin1 = False
            $ whileGin2 = False
            $ whileGin3 = False
            $ whileGin4 = False
            $ whileGin5 = False
            $ whileGin6 = False
            $ whileGin7 = False
            $ whileGin8 = True





    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "if_R_gate_return" or slot_name == "if_G_gate_return" or slot_name == "if_B_gate_return" or slot_name == "if_GR_gate_return" or
        slot_name == "if_BG_gate_return" or slot_name == "else_gate_return" or slot_name == "while_G_gate_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
            
      
    else:
        if slot_name != "null" and (temp_slot != slot_name or gate_name != temp_gate):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "if_R_gate_return":
                $ attempts +=1
                if gate_name == "if_R_gate":
                    $ ifRx = 1395
                    $ ifRy = 645
                    $ ifRin1 = False
                    $ ifRin2 = False
                    $ ifRin3 = False
                    $ ifRin4 = False
                    $ ifRin5 = False
                    $ ifRin6 = False
                    $ ifRin7 = False
                    $ ifRin8 = False
            if slot_name == "if_G_gate_return":
                $ attempts +=1
                if gate_name == "if_G_gate":
                    $ ifGx = 1525
                    $ ifGy = 645
                    $ ifGin1 = False
                    $ ifGin2 = False
                    $ ifGin3 = False
                    $ ifGin4 = False
                    $ ifGin5 = False
                    $ ifGin6 = False
                    $ ifGin7 = False
                    $ ifGin8 = False
            if slot_name == "if_B_gate_return":
                $ attempts +=1
                if gate_name == "if_B1_gate":
                    $ ifB1x = 1655
                    $ ifB1y = 645
                    $ ifB1in1 = False
                    $ ifB1in2 = False
                    $ ifB1in3 = False
                    $ ifB1in4 = False
                    $ ifB1in5 = False
                    $ ifB1in6 = False
                    $ ifB1in7 = False
                    $ ifB1in8 = False
            if slot_name == "if_B_gate_return":
                $ attempts +=1
                if gate_name == "if_B2_gate":
                    $ ifB2x = 1655
                    $ ifB2y = 645
                    $ ifB2in1 = False
                    $ ifB2in2 = False
                    $ ifB2in3 = False
                    $ ifB2in4 = False
                    $ ifB2in5 = False
                    $ ifB2in6 = False
                    $ ifB2in7 = False
                    $ ifB2in8 = False
            if slot_name == "if_GR_gate_return":
                $ attempts +=1
                if gate_name == "if_GR_gate":
                    $ ifGRx = 1445
                    $ ifGRy = 790
                    $ ifGRin1 = False
                    $ ifGRin2 = False
                    $ ifGRin3 = False
                    $ ifGRin4 = False
                    $ ifGRin5 = False
                    $ ifGRin6 = False
                    $ ifGRin7 = False
                    $ ifGRin8 = False
            if slot_name == "if_BG_gate_return":
                $ attempts +=1
                if gate_name == "if_BG_gate":
                    $ ifBGx = 1585
                    $ ifBGy = 790
                    $ ifBGin1 = False
                    $ ifBGin2 = False
                    $ ifBGin3 = False
                    $ ifBGin4 = False
                    $ ifBGin5 = False
                    $ ifBGin6 = False
                    $ ifBGin7 = False
                    $ ifBGin8 = False
            if slot_name == "else_gate_return":
                $ attempts +=1
                if gate_name == "else_gate":
                    $ elsex = 1585
                    $ elsey = 500
                    $ elsein1 = False
                    $ elsein2 = False
                    $ elsein3 = False
                    $ elsein4 = False
                    $ elsein5 = False
                    $ elsein6 = False
                    $ elsein7 = False
                    $ elsein8 = False
            if slot_name == "while_G_gate_return":
                $ attempts +=1
                if gate_name == "while_G_gate":
                    $ whileGx = 1445
                    $ whileGy = 500
                    $ whileGin1 = False
                    $ whileGin2 = False
                    $ whileGin3 = False
                    $ whileGin4 = False
                    $ whileGin5 = False
                    $ whileGin6 = False
                    $ whileGin7 = False
                    $ whileGin8 = False
                    

#*******************************************
#************image zone********************* 
#*******************************************
    $LLH_4_node1 = "None"
    $LLH_4_node2 = "None"
    $LLH_4_node3 = "None"
    $LLH_4_node4 = "None"
    $LLH_4_node5 = "None"
    
    $LLH_4_BEnd1 = "Off"
    $LLH_4_BEnd2 = "Off"
    $LLH_4_GEnd = "Off"
    $LLH_4_REnd1 = "Off"
    $LLH_4_REnd2 = "Off"
    
    $LLH_4_GWhileNode = "Off"
    hide LLH_4_colorTile1
    hide LLH_4_colorTile2
    hide LLH_4_colorTile4
    hide LLH_4_colorTile5
    hide LLH_4_colorTile6
    hide LLH_4_colorTile7
    hide LLH_4_colorTile8
    hide LLH_4_colorTile9
    hide LLH_4_colorTile10
    hide LLH_4_colorTile11
    hide LLH_4_colorTile12
    hide LLH_4_colorTile13
    hide LLH_4_colorTile14
    hide LLH_4_colorTile15
    hide LLH_4_colorTile16
    hide LLH_4_colorTile17
    hide LLH_4_colorTile18
    hide LLH_4_colorTile19
    hide LLH_4_colorTile20
    hide LLH_4_colorTile21
    hide LLH_4_colorTile22
    hide LLH_4_colorTile23
    hide LLH_4_colorTile24
    hide LLH_4_colorTile25
    hide LLH_4_colorTile26
    hide LLH_4_colorTile27
    hide LLH_4_colorTile28
    hide LLH_4_colorTile29
    hide LLH_4_colorTile30
    hide LLH_4_colorTile31
    hide LLH_4_colorTile32
    hide LLH_4_colorTile33
    hide LLH_4_colorTile34
    hide LLH_4_colorTile35
    hide LLH_4_colorTile36
    hide LLH_4_colorTile37
    hide LLH_4_colorTile39
    hide LLH_4_colorTile40
    hide LLH_4_colorTile41
    hide LLH_4_colorTile42
    hide LLH_4_colorTile43
    hide LLH_4_colorTile46
    hide LLH_4_colorTile47
    hide LLH_4_colorTile48
    hide LLH_4_colorTile49
    hide LLH_4_colorTile50
    hide LLH_4_colorTile51
    hide LLH_4_colorTile52
    hide LLH_4_colorTile53
    hide LLH_4_colorTile54
    hide LLH_4_colorTile55
    hide LLH_4_colorTile56
    hide LLH_4_colorTile58
    hide LLH_4_colorTile59
    hide LLH_4_colorTile60
    hide LLH_4_colorTile61
    hide LLH_4_colorTile62
    hide LLH_4_colorTile68
    hide LLH_4_colorTile71
    hide LLH_4_colorTile72
    hide LLH_4_colorTile77
    hide LLH_4_colorTile78
    hide LLH_4_colorTile79
    hide LLH_4_colorTile80
    hide LLH_4_colorTile82
    hide LLH_4_colorTile83
    hide LLH_4_colorTile84
    hide LLH_4_colorTile85
    hide LLH_4_colorTile86
    hide LLH_4_colorTile87
    hide LLH_4_colorTile88
    hide LLH_4_colorTile89
    hide LLH_4_colorTile90
    hide LLH_4_colorTile91
    hide LLH_4_colorTile92
    hide LLH_4_colorTile93
    hide LLH_4_colorTile96
    hide LLH_4_colorTile97 
    hide LLH_4_colorTile98
    hide LLH_4_colorTile99
    hide LLH_4_colorTile100
    hide LLH_4_colorTile101
    hide LLH_4_colorTile102
    hide LLH_4_colorTile103
    hide LLH_4_colorTile104
    hide LLH_4_colorTile105
    hide LLH_4_colorTile106
    hide LLH_4_colorTile107
    hide LLH_4_colorTile108
    hide LLH_4_colorTile109
    hide LLH_4_colorTileBr50
    hide LLH_4_colorTileBr98
    hide LLH_4_colorTileBr99
    hide LLH_4_colorTileBr101
    hide LLH_4_colorTileBr102
    hide LLH_4_colorTileBr104
    hide LLH_4_colorTileBr68
    hide LLH_4_colorTileT78
    hide LLH_4_colorTileT79
    hide LLH_4_colorTileT50
    hide LLH_4_colorTileT68
    hide LLH_4_colorTileT102
    hide LLH_4_colorTileT101
    hide LLH_4_colorTileT99
    hide LLH_4_colorTileT98
    hide LLH_4_colorTileP98
    hide LLH_4_colorTileP99
    hide LLH_4_colorTileP101
    hide LLH_4_colorTileP102
    hide LLH_4_colorTileGr98
    hide LLH_4_colorTileGr99
    hide LLH_4_colorTileGr101
    hide LLH_4_colorTileGr102
    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    if ifGRin7:
        image LLH_4_colorTile1 = "R_horizontal_short.png"
        show LLH_4_colorTile1 at Position(xpos = 725, xanchor = 0, ypos = 665, yanchor = 0)
        image LLH_4_colorTile2 = "G_horizontal_short.png"
        show LLH_4_colorTile2 at Position(xpos = 725, xanchor = 0, ypos = 715, yanchor = 0)
        
        if ifGin8:
            image LLH_4_colorTile4 = "G_horizontal_short.png"
            show LLH_4_colorTile4 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
            image LLH_4_colorTile5 = "G_horizontal_ll.png"
            show LLH_4_colorTile5 at Position(xpos = 950, xanchor = 0, ypos = 690, yanchor = 0)
            $LLH_4_GEnd = "On"
            if (elsein3):
                $LLH_4_node4 = "Red"
                image LLH_4_colorTile6 = "R_vertical_ll.png"
                show LLH_4_colorTile6 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
                image LLH_4_colorTile7 = "R_vertical_ll.png"
                show LLH_4_colorTile7 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
                image LLH_4_colorTile8 = "R_horizontal_short.png"
                show LLH_4_colorTile8 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile9 = "R_horizontal_ll.png"
                show LLH_4_colorTile9 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile19 = "W_corner_RB.png"
                show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
                $LLH_4_REnd2 = "On"
        if ifRin3:
            $LLH_4_node4 = "Red"
            show LLH_4_colorTile6 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile7 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile8 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile9 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
            $LLH_4_REnd2 = "On"
        if ifRin8:
            image LLH_4_colorTile10 = "R_horizontal_short.png"
            show LLH_4_colorTile10 at Position(xpos = 800, xanchor = 0, ypos = 665, yanchor = 0)
            image LLH_4_colorTile11 = "R_horizontal_ll.png"
            show LLH_4_colorTile11 at Position(xpos = 950, xanchor = 0, ypos = 690, yanchor = 0) 
            
            if (elsein3 == True):
                $LLH_4_node4 = "Green"
                $LLH_4_node5 = "Green"
                image LLH_4_colorTile12 = "G_vertical_ll.png"
                show LLH_4_colorTile12 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
                image LLH_4_colorTile13 = "G_vertical_ll.png"
                show LLH_4_colorTile13 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
                image LLH_4_colorTile14 = "G_horizontal_short.png"
                show LLH_4_colorTile14 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile15 = "G_horizontal_ll.png"
                show LLH_4_colorTile15 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile16 = "G_connect_pipe_vertical.png"
                show LLH_4_colorTile16 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
                show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifGin3:
            $LLH_4_node4 = "Green"
            $LLH_4_node5 = "Green"
            show LLH_4_colorTile12 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile13 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile14 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile15 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile16 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
            show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifBGin3: 
            $LLH_4_node4 = "Green"
            $LLH_4_node5 = "Green"
            show LLH_4_colorTile12 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile13 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile14 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile16 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
            show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifBGin8:
            image LLH_4_colorTile82 = "G_horizontal_short.png"
            show LLH_4_colorTile82 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)

    if ifBGin7:
        image LLH_4_colorTile17 = "G_horizontal_short.png"
        show LLH_4_colorTile17 at Position(xpos = 725, xanchor = 0, ypos = 665, yanchor = 0)
        image LLH_4_colorTile18 = "B_horizontal_short.png"
        show LLH_4_colorTile18 at Position(xpos = 725, xanchor = 0, ypos = 715, yanchor = 0)
            
        if ifGin8:
            image LLH_4_colorTile20 = "G_horizontal_short.png"
            show LLH_4_colorTile20 at Position(xpos = 800, xanchor = 0, ypos = 665, yanchor = 0)
            image LLH_4_colorTile21 = "G_horizontal_ll.png"
            show LLH_4_colorTile21 at Position(xpos = 950, xanchor = 0, ypos = 690, yanchor = 0)
            $LLH_4_GEnd = "On"
            
            if (elsein3):
                $LLH_4_node4 = "Blue"
                $LLH_4_node5 = "Blue"
                image LLH_4_colorTile22 = "B_vertical.png"
                show LLH_4_colorTile22 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
                image LLH_4_colorTile23 = "B_vertical.png"
                show LLH_4_colorTile23 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
                image LLH_4_colorTile24 = "B_horizontal_short.png"
                show LLH_4_colorTile24 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile25 = "B_horizontal.png"
                show LLH_4_colorTile25 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile26 = "B_connect_pipe_vertical.png"
                show LLH_4_colorTile26 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
                image LLH_4_colorTile43 = "W_corner_RB.png"
                show LLH_4_colorTile43 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if (ifB1in3 or ifB2in3):
            $LLH_4_node4 = "Blue"
            $LLH_4_node5 = "Blue"
            show LLH_4_colorTile22 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile23 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile24 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile25 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile26 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
            show LLH_4_colorTile43 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
            
        if ifB1in8 or ifB2in8:
            image LLH_4_colorTile27 = "B_horizontal_short.png"
            show LLH_4_colorTile27 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
            image LLH_4_colorTile28 = "B_horizontal.png"
            show LLH_4_colorTile28 at Position(xpos = 950, xanchor = 0, ypos = 690, yanchor = 0) 
            
            if (elsein3):
                $LLH_4_node4 = "Green"
                image LLH_4_colorTile29 = "G_vertical_ll.png"
                show LLH_4_colorTile29 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
                image LLH_4_colorTile30 = "G_vertical_ll.png"
                show LLH_4_colorTile30 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
                image LLH_4_colorTile31 = "G_horizontal_short.png"
                show LLH_4_colorTile31 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile32 = "G_horizontal_ll.png"
                show LLH_4_colorTile32 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
                image LLH_4_colorTile84 = "W_corner_RB.png"
                show LLH_4_colorTile84 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifGin3:
            $LLH_4_node4 = "Green"
            show LLH_4_colorTile29 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile30 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile31 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile32 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile84 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)     
                
        if ifGRin8:
            image LLH_4_colorTile83 = "G_horizontal_short.png"
            show LLH_4_colorTile83 at Position(xpos = 800, xanchor = 0, ypos = 665, yanchor = 0)
        if ifGRin3:
            $LLH_4_node4 = "Green"
            show LLH_4_colorTile12 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile13 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile14 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
    if ifGin7:
        show LLH_4_colorTile2 at Position(xpos = 725, xanchor = 0, ypos = 715, yanchor = 0)
        if ifBGin3:
            $LLH_4_node4 = "Green"
            $LLH_4_node5 = "Green"
            show LLH_4_colorTile12 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile13 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile14 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile16 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
        if ifBGin8:
            show LLH_4_colorTile82 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
        if ifGRin3:
            $LLH_4_node4 = "Green"
            $LLH_4_node5 = "Green"
            show LLH_4_colorTile12 at Position(xpos = 772, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile13 at Position(xpos = 772, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile14 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile16 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
        if ifGRin8:
            show LLH_4_colorTile82 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
            
    if ifB1in7 or ifB2in7:
        show LLH_4_colorTile18 at Position(xpos = 725, xanchor = 0, ypos = 715, yanchor = 0)
        if ifBGin3:
            $LLH_4_node4 = "Blue"
            $LLH_4_node5 = "Blue"
            show LLH_4_colorTile22 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile23 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile24 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile26 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
            show LLH_4_colorTile43 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifBGin8:
            show LLH_4_colorTile27 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
        if ifB1in3 or ifB2in3:
            $LLH_4_node4 = "Blue"
            $LLH_4_node5 = "Blue"
            show LLH_4_colorTile22 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile23 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile24 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile25 at Position(xpos = 925, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile26 at Position(xpos = 785, xanchor = 0, ypos = 681, yanchor = 0)
            show LLH_4_colorTile43 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifB1in8 or ifB2in8:
            show LLH_4_colorTile27 at Position(xpos = 800, xanchor = 0, ypos = 715, yanchor = 0)
            show LLH_4_colorTile28 at Position(xpos = 950, xanchor = 0, ypos = 690, yanchor = 0) 
    if ifRin7:
        show LLH_4_colorTile1 at Position(xpos = 725, xanchor = 0, ypos = 665, yanchor = 0)
        if ifGRin3:
            $LLH_4_node4 = "Red"
            show LLH_4_colorTile6 at Position(xpos = 775, xanchor = 0, ypos = 595, yanchor = 0)
            show LLH_4_colorTile7 at Position(xpos = 775, xanchor = 0, ypos = 520, yanchor = 0)
            show LLH_4_colorTile8 at Position(xpos = 825, xanchor = 0, ypos = 490, yanchor = 0)
            show LLH_4_colorTile19 at Position(xpos = 748, xanchor = 0, ypos = 465, yanchor = 0)
        if ifGRin8:
            show LLH_4_colorTile10 at Position(xpos = 800, xanchor = 0, ypos = 665, yanchor = 0)
#############################END RIGHT SECTION##############################################
    if ifRin4 and ifGRin6:
        image LLH_4_colorTile87 = "R_vertical_ll.png"
        show LLH_4_colorTile87 at Position(xpos = 285, xanchor = 0, ypos = 580, yanchor = 0) 
    if ifGRin4 and ifRin6:
        show LLH_4_colorTile87 at Position(xpos = 285, xanchor = 0, ypos = 580, yanchor = 0)
    if ifGin4 and (ifGRin6 or ifBGin6):
        image LLH_4_colorTile88 = "G_vertical_ll.png"
        show LLH_4_colorTile88 at Position(xpos = 282, xanchor = 0, ypos = 580, yanchor = 0) 
    if (ifGRin4 or ifBGin4) and ifGin6:
        show LLH_4_colorTile88 at Position(xpos = 282, xanchor = 0, ypos = 580, yanchor = 0) 
    if (ifB1in4 or ifB2in4) and ifBGin6:
        image LLH_4_colorTile89 = "B_vertical.png"
        show LLH_4_colorTile89 at Position(xpos = 285, xanchor = 0, ypos = 580, yanchor = 0) 
        
    if ifGRin6 and ifBGin4:
        show LLH_4_colorTile88 at Position(xpos = 282, xanchor = 0, ypos = 580, yanchor = 0)
        
    if ifGRin4 and ifBGin6:
        show LLH_4_colorTile88 at Position(xpos = 282, xanchor = 0, ypos = 580, yanchor = 0)
        
    if ((ifB1in4 or ifB2in4) and (ifB2in6 or ifB1in6)):
        show LLH_4_colorTile89 at Position(xpos = 285, xanchor = 0, ypos = 580, yanchor = 0)
        
    if ((ifB1in6 or ifB2in6) and ifBGin4):
        show LLH_4_colorTile89 at Position(xpos = 285, xanchor = 0, ypos = 580, yanchor = 0)
        
    if whileGin4:
        if (ifGRin6 or ifBGin6 or ifGin6):
            $LLH_4_GWhileNode = "On"
            image LLH_4_colorTile33 = "G_vertical_ll.png"
            show LLH_4_colorTile33 at Position(xpos = 282, xanchor = 0, ypos = 580, yanchor = 0)  
            image LLH_4_colorTile34 = "y_horizontal_short_on.png"
            show LLH_4_colorTile34 at Position(xpos = 320, xanchor = 0, ypos = 555, yanchor = 0)  
            image LLH_4_colorTile35 = "y_horizontal_short_on.png"
            show LLH_4_colorTile35 at Position(xpos = 380, xanchor = 0, ypos = 555, yanchor = 0)  
            image LLH_4_colorTile36 = "y_horizontal_short_on.png"
            show LLH_4_colorTile36 at Position(xpos = 440, xanchor = 0, ypos = 555, yanchor = 0)  
            image LLH_4_colorTile37 = "R_vertical_ll.png"
            show LLH_4_colorTile37 at Position(xpos = 470, xanchor = 0, ypos = 505, yanchor = 0)      
        
    if ifGRin6:
        if ifRin5:
            image LLH_4_colorTile39 = "R_horizontal_ll.png"
            show LLH_4_colorTile39 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
            image LLH_4_colorTile40 = "R_vertical_ll.png"
            show LLH_4_colorTile40 at Position(xpos = 135, xanchor = 0, ypos = 580, yanchor = 0)
        
        if ifGin5:
            image LLH_4_colorTile41 = "G_horizontal_ll.png"
            show LLH_4_colorTile41 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
            image LLH_4_colorTile42 = "G_vertical_ll.png"
            show LLH_4_colorTile42 at Position(xpos = 132, xanchor = 0, ypos = 580, yanchor = 0)
        if ifBGin5:
            show LLH_4_colorTile41 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
            
    if (ifB1in6 or ifB2in6) and (ifB1in5 or ifB2in5):
        $LLH_4_BEnd2 = "On"
        show LLH_4_colorTile46 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
        show LLH_4_colorTile47 at Position(xpos = 135, xanchor = 0, ypos = 580, yanchor = 0)
        
    if (ifB1in6 or ifB2in6) and ifBGin5:
        show LLH_4_colorTile46 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
        
    if ifRin6 and ifGRin5:
        show LLH_4_colorTile39 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
        
    if ifGin6 and ifGRin5:
        show LLH_4_colorTile41 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
        
    if ifGin6 and ifBGin5:
        show LLH_4_colorTile41 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
        
    if ifBGin6:
        if ifGin5:
            show LLH_4_colorTile41 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
            show LLH_4_colorTile42 at Position(xpos = 132, xanchor = 0, ypos = 580, yanchor = 0)
        
        if (ifB1in5 or ifB2in5):
            $LLH_4_BEnd2 = "On"
            image LLH_4_colorTile46 = "B_horizontal.png"
            show LLH_4_colorTile46 at Position(xpos = 200, xanchor = 0, ypos = 695, yanchor = 0)
            image LLH_4_colorTile47 = "B_vertical.png"
            show LLH_4_colorTile47 at Position(xpos = 135, xanchor = 0, ypos = 580, yanchor = 0)
##########################end left portion############################################
    if ifRin1:
        if whileGin4 and (ifGRin6 or ifBGin6 or ifGin6):
            $LLH_4_REnd1 = "On"
            image LLH_4_colorTile48 = "R_vertical_ll.png"
            show LLH_4_colorTile48 at Position(xpos = 470, xanchor = 0, ypos = 415, yanchor = 0)
            image LLH_4_colorTile49 = "R_vertical_ll.png"
            show LLH_4_colorTile49 at Position(xpos = 470, xanchor = 0, ypos = 330, yanchor = 0)
            image LLH_4_colorTile50 = "R_horizontal_ll.png"
            show LLH_4_colorTile50 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
            image LLH_4_colorTile68 = "R_horizontal_ll.png"
            show LLH_4_colorTile68 at Position(xpos = 325, xanchor = 0, ypos = 360, yanchor = 0)
        
    if ifGin1:
        image LLH_4_colorTile51 = "G_vertical_ll.png"
        show LLH_4_colorTile51 at Position(xpos = 507, xanchor = 0, ypos = 415, yanchor = 0)
        image LLH_4_colorTile52 = "G_vertical_ll.png"
        show LLH_4_colorTile52 at Position(xpos = 507, xanchor = 0, ypos = 330, yanchor = 0)
        image LLH_4_colorTile53 = "G_horizontal_ll.png"
        show LLH_4_colorTile53 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
        image LLH_4_colorTile71 = "G_horizontal_ll.png"
        show LLH_4_colorTile71 at Position(xpos = 325, xanchor = 0, ypos = 360, yanchor = 0)
        
    if (ifB1in1 == True or ifB2in1 == True):
        image LLH_4_colorTile54 = "B_vertical.png"
        show LLH_4_colorTile54 at Position(xpos = 550, xanchor = 0, ypos = 415, yanchor = 0)
        image LLH_4_colorTile55 = "B_vertical.png"
        show LLH_4_colorTile55 at Position(xpos = 550, xanchor = 0, ypos = 330, yanchor = 0)
        image LLH_4_colorTile56 = "B_horizontal.png"
        show LLH_4_colorTile56 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
        image LLH_4_colorTile72 = "B_horizontal.png"
        show LLH_4_colorTile72 at Position(xpos = 325, xanchor = 0, ypos = 360, yanchor = 0)
        
    if ifGRin1:
        image LLH_4_colorTile92 = "G_vertical_ll.png"
        show LLH_4_colorTile92 at Position(xpos = 507, xanchor = 0, ypos = 415, yanchor = 0)
        image LLH_4_colorTile93 = "G_vertical_ll.png"
        show LLH_4_colorTile93 at Position(xpos = 507, xanchor = 0, ypos = 330, yanchor = 0)
        if whileGin4 and (ifBGin6 or ifGin6):
            image LLH_4_colorTile90 = "R_vertical_ll.png"
            show LLH_4_colorTile90 at Position(xpos = 470, xanchor = 0, ypos = 415, yanchor = 0)
            image LLH_4_colorTile91 = "R_vertical_ll.png"
            show LLH_4_colorTile91 at Position(xpos = 470, xanchor = 0, ypos = 330, yanchor = 0)
            image LLH_4_colorTileBr50 = "Br_horizontal_ll.png"
            show LLH_4_colorTileBr50 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
            image LLH_4_colorTileBr68 = "Br_horizontal_ll.png"
            show LLH_4_colorTileBr68 at Position(xpos = 325, xanchor = 0, ypos = 360, yanchor = 0)
    if ifBGin1:
        image LLH_4_colorTile85 = "G_vertical_ll.png"
        show LLH_4_colorTile85 at Position(xpos = 507, xanchor = 0, ypos = 415, yanchor = 0)
        image LLH_4_colorTile86 = "G_vertical_ll.png"
        show LLH_4_colorTile86 at Position(xpos = 507, xanchor = 0, ypos = 330, yanchor = 0)
        image LLH_4_colorTile96 = "B_vertical.png"
        show LLH_4_colorTile96 at Position(xpos = 550, xanchor = 0, ypos = 415, yanchor = 0)
        image LLH_4_colorTile97 = "B_vertical.png"
        show LLH_4_colorTile97 at Position(xpos = 550, xanchor = 0, ypos = 330, yanchor = 0)
        image LLH_4_colorTileT50 = "T_horizontal_ll.png"
        show LLH_4_colorTileT50 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
        image LLH_4_colorTileT68 = "T_horizontal_ll.png"
        show LLH_4_colorTileT68 at Position(xpos = 325, xanchor = 0, ypos = 360, yanchor = 0)
    if elsein2:
        if ifRin1 and whileGin4 and (ifGRin6 or ifBGin6 or ifGin6):
            $LLH_4_node2 = "Green"
            $LLH_4_node3 = "Turq"
            show LLH_4_colorTile77 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
            image LLH_4_colorTile104 = "R_connect_pipe.png"
            show LLH_4_colorTile104 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
            image LLH_4_colorTileT98 = "T_horizontal_ll.png"
            show LLH_4_colorTileT98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
            image LLH_4_colorTileT99 = "T_vertical_short.png"
            show LLH_4_colorTileT99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
            show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
            image LLH_4_colorTileT101 = "T_horizontal_ll.png"
            show LLH_4_colorTileT101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
            image LLH_4_colorTileT102 = "T_horizontal_ll.png"
            show LLH_4_colorTileT102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
            image LLH_4_colorTile100 = "W_corner_LT.png"
            
        if ifGin1:
            $LLH_4_node3 = "Blue"
            if not(whileGin4 and (ifGRin6 or ifBGin6 or ifGin6)):
                $LLH_4_BEnd1 = "On"
                image LLH_4_colorTile98 = "B_horizontal.png"
                show LLH_4_colorTile98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
                image LLH_4_colorTile99 = "B_vertical_short.png"
                show LLH_4_colorTile99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
                show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
                image LLH_4_colorTile101 = "B_horizontal.png"
                show LLH_4_colorTile101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
                image LLH_4_colorTile102 = "B_horizontal.png"
                show LLH_4_colorTile102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
            if whileGin4 and (ifGRin6 or ifBGin6 or ifGin6):
                $LLH_4_node1 = "Red"
                $LLH_4_node2 = "Red"
                $LLH_4_node3 = "Purp"
                show LLH_4_colorTile103 at Position(xpos = 480, xanchor = 0, ypos = 500, yanchor = 0)
                show LLH_4_colorTile104 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
                image LLH_4_colorTileP98 = "P_horizontal_ll.png"
                show LLH_4_colorTileP98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
                image LLH_4_colorTileP99 = "P_vertical_short.png"
                show LLH_4_colorTileP99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
                show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
                image LLH_4_colorTileP101 = "P_horizontal_ll.png"
                show LLH_4_colorTileP101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
                image LLH_4_colorTileP102 = "P_horizontal_ll.png"
                show LLH_4_colorTileP102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
        if (ifB1in1 or ifB2in1):
            $LLH_4_node2 = "Green"
            if whileGin4 and (ifGRin6 or ifBGin6 or ifGin6):
                $LLH_4_node1 = "Red"
                $LLH_4_node2 = "Brown"
                $LLH_4_node3 = "Brown"
                image LLH_4_colorTile103 = "R_connect_pipe.png"
                show LLH_4_colorTile103 at Position(xpos = 480, xanchor = 0, ypos = 500, yanchor = 0)
                image LLH_4_colorTileBr104 = "Br_connect_pipe.png"
                show LLH_4_colorTileBr104 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
                image LLH_4_colorTileBr98 = "Br_horizontal_ll.png"
                show LLH_4_colorTileBr98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
                image LLH_4_colorTileBr99 = "Br_vertical_short.png"
                show LLH_4_colorTileBr99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
                show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
                image LLH_4_colorTileBr101 = "Br_horizontal_ll.png"
                show LLH_4_colorTileBr101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
                image LLH_4_colorTileBr102 = "Br_horizontal_ll.png"
                show LLH_4_colorTileBr102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
                
            if not(whileGin4 and (ifGRin6 or ifBGin6 or ifGin6)):
                $LLH_4_node2 = "Green"
                $LLH_4_node3 = "Green"
                show LLH_4_colorTile77 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
                image LLH_4_colorTileGr98 = "G_horizontal_ll.png"
                show LLH_4_colorTileGr98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
                image LLH_4_colorTileGr99 = "G_vertical_short.png"
                show LLH_4_colorTileGr99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
                show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
                image LLH_4_colorTileGr101 = "G_horizontal_ll.png"
                show LLH_4_colorTileGr101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
                image LLH_4_colorTileGr102 = "G_horizontal_ll.png"
                show LLH_4_colorTileGr102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
                
        if ifGRin1:
            if whileGin4 and (ifBGin6 or ifGin6):
                $LLH_4_node3 = "Blue"
                $LLH_4_BEnd1 = "On"
                show LLH_4_colorTile98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
                show LLH_4_colorTile99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
                show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
                show LLH_4_colorTile101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
                show LLH_4_colorTile102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
            if not(whileGin4 and (ifBGin6 or ifGin6)):
                $LLH_4_node3 = "Blue"
                $LLH_4_BEnd1 = "On"
                show LLH_4_colorTile98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
                show LLH_4_colorTile99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
                show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
                show LLH_4_colorTile101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
                show LLH_4_colorTile102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
                
        if ifBGin1 and whileGin4 and (ifGRin6 or ifGin6):
            $LLH_4_node1 = "Red"
            $LLH_4_node2 = "Red"
            $LLH_4_node3 = "Red"
            image LLH_4_colorTile103 = "R_connect_pipe.png"
            show LLH_4_colorTile103 at Position(xpos = 480, xanchor = 0, ypos = 500, yanchor = 0)
            image LLH_4_colorTile104 = "R_connect_pipe.png"
            show LLH_4_colorTile104 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
            image LLH_4_colorTile105 = "R_horizontal_ll.png"
            show LLH_4_colorTile105 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
            image LLH_4_colorTile106 = "R_vertical_short.png"
            show LLH_4_colorTile106 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
            image LLH_4_colorTile107 = "W_corner_LT.png"
            show LLH_4_colorTile107 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
            image LLH_4_colorTile108 = "R_horizontal_ll.png"
            show LLH_4_colorTile108 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)  
            image LLH_4_colorTile109 = "R_horizontal_ll.png"
            show LLH_4_colorTile109 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)          
            
    if ifRin2:
        if whileGin4 and (ifBGin6 or ifGRin6 or ifGin6):
            $LLH_4_node1 = "Red"
            $LLH_4_node2 = "Red"
            $LLH_4_node3 = "Red"
            show LLH_4_colorTile103 at Position(xpos = 480, xanchor = 0, ypos = 500, yanchor = 0)
            show LLH_4_colorTile104 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
            show LLH_4_colorTile105 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
            show LLH_4_colorTile106 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
            show LLH_4_colorTile107 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
            show LLH_4_colorTile108 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)  
            show LLH_4_colorTile109 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)  
            
    if ifGin2:
        image LLH_4_colorTile77 = "G_connect_pipe.png"
        show LLH_4_colorTile77 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
        image LLH_4_colorTile78 = "G_horizontal_ll.png"
        show LLH_4_colorTile78 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
        image LLH_4_colorTile79 = "G_vertical_short.png"
        show LLH_4_colorTile79 at Position(xpos = 657, xanchor = 0, ypos = 420, yanchor = 0)
        image LLH_4_colorTile80 = "W_corner_LT.png"
        show LLH_4_colorTile80 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)

    if ifB1in2 or ifB2in2:
        $LLH_4_BEnd1 = "On"
        $LLH_4_node3 = "Blue"
        image LLH_4_colorTile58 = "B_horizontal.png"
        show LLH_4_colorTile58 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
        image LLH_4_colorTile59 = "B_vertical_short.png"
        show LLH_4_colorTile59 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
        image LLH_4_colorTile60 = "W_corner_LT.png"
        show LLH_4_colorTile60 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
        image LLH_4_colorTile61 = "B_horizontal.png"
        show LLH_4_colorTile61 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
        image LLH_4_colorTile62 = "B_horizontal.png"
        show LLH_4_colorTile62 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
        
    if ifBGin2:
        show LLH_4_colorTile77 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
        image LLH_4_colorTileT78 = "T_horizontal_ll.png"
        show LLH_4_colorTileT78 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
        image LLH_4_colorTileT79 = "T_vertical_short.png"
        show LLH_4_colorTileT79 at Position(xpos = 657, xanchor = 0, ypos = 420, yanchor = 0)
        show LLH_4_colorTile80 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
        
    if ifGRin2:
        if(whileGin4 and (ifBGin6 or ifGin6)):
            $LLH_4_node1 = "Red"
            $LLH_4_node2 = "Brown"
            $LLH_4_node3 = "Brown"
            show LLH_4_colorTile103 at Position(xpos = 480, xanchor = 0, ypos = 500, yanchor = 0)
            show LLH_4_colorTileBr104 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
            show LLH_4_colorTileBr98 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
            show LLH_4_colorTileBr99 at Position(xpos = 660, xanchor = 0, ypos = 420, yanchor = 0)
            show LLH_4_colorTile100 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
            show LLH_4_colorTileBr101 at Position(xpos = 725, xanchor = 0, ypos = 360, yanchor = 0)
            show LLH_4_colorTileBr102 at Position(xpos = 800, xanchor = 0, ypos = 360, yanchor = 0)
            
        if (not(whileGin4 and (ifBGin6 or ifGin6))):
            show LLH_4_colorTile77 at Position(xpos = 520, xanchor = 0, ypos = 500, yanchor = 0)
            show LLH_4_colorTile78 at Position(xpos = 575, xanchor = 0, ypos = 492, yanchor = 0)
            show LLH_4_colorTile79 at Position(xpos = 657, xanchor = 0, ypos = 420, yanchor = 0)
            show LLH_4_colorTile80 at Position(xpos = 638, xanchor = 0, ypos = 470, yanchor = 0)
    ###############################################Other sounds here#########################3
    if (whileGin4 and (ifGRin6 or ifGin6 or ifBGin6)):
        if charge1_sound1 ==0:
            play soundP08 llCharge
            $charge1_sound1 +=1
    if not(whileGin4 and (ifGRin6 or ifGin6 or ifBGin6)):
        if charge1_sound1 ==1:
            $charge1_sound1 -=1
            
    if ((ifB1in5 or ifB2in5) and (ifB1in6 or ifB2in6 or ifBGin6)):
        if light1Sound ==0:
            queue soundP01 llLightOn1
            $light1Sound +=1
    if(not((ifB1in5 or ifB2in5) and (ifB1in6 or ifB2in6 or ifBGin6))):
        if light1Sound ==1:
            queue soundP01 llLightOff1
            $light1Sound -=1
            
    if((whileGin4 and (ifGRin6 or ifGin6 or ifBGin6)) and (ifRin1)):
        if light2Sound ==0:
            queue soundP02 llLightOn2
            $light2Sound +=1
    if (not((whileGin4 and (ifGRin6 or ifGin6 or ifBGin6)) and (ifRin1))):
        if light2Sound ==1:
            queue soundP02 llLightOff2
            $light2Sound -=1
            
    if(ifB1in2 or ifB2in2 or (elsein2 and ifGRin1) or ((not(whileGin4 and (ifGRin6 or ifGin6 or ifBGin6))) and elsein2 and ifGin1)):
        if light3Sound ==0:
            queue soundP03 llLightOn1
            $light3Sound +=1
    if not((ifB1in2 or ifB2in2 or (elsein2 and ifGRin1) or ((not(whileGin4 and (ifGRin6 or ifGin6 or ifBGin6))) and elsein2 and ifGin1))):
        if light3Sound ==1:
            queue soundP03 llLightOff1
            $light3Sound -=1
            
    if(ifGRin7 and (ifRin3 or (elsein3 and ifGin8))):
        if light4Sound ==0:
            queue soundP04 llLightOn2
            $light4Sound +=1
    if (not(ifGRin7 and (ifRin3 or (elsein3 and ifGin8)))):
        if light4Sound ==1:
            queue soundP04 llLightOff2
            $light4Sound -=1
    if(ifGin8 and (ifGRin7 or ifBGin7)):
        if light5Sound ==0:
            queue soundP05 llLightOn3
            $light5Sound +=1
    if (not(ifGin8 and (ifGRin7 or ifBGin7))):
        if light5Sound ==1:
            queue soundP05 llLightOff3
            $light5Sound -=1
    #Redraw Connect Nodes *********************************************************************
    hide LLH_4_WNode1
    hide LLH_4_WNode2
    hide LLH_4_WNode3
    hide LLH_4_WNode4
    hide LLH_4_WNode5
    hide LLH_4_RNode1
    hide LLH_4_RNode2
    hide LLH_4_RNode3
    hide LLH_4_RNode4
    hide LLH_4_RNode5
    hide LLH_4_GNode1
    hide LLH_4_GNode2
    hide LLH_4_GNode3
    hide LLH_4_GNode4
    hide LLH_4_GNode5
    hide LLH_4_BNode1
    hide LLH_4_BNode2
    hide LLH_4_BNode3
    hide LLH_4_BNode4
    hide LLH_4_BNode5
    hide LLH_4_TNode1
    hide LLH_4_TNode2
    hide LLH_4_TNode3
    hide LLH_4_PNode1
    hide LLH_4_PNode2
    hide LLH_4_PNode3
    hide LLH_4_BrNode1
    hide LLH_4_BrNode2
    hide LLH_4_BrNode3
    
    image LLH_4_WNode1 = "W_connect_node.png"
    image LLH_4_WNode2 = "W_connect_node.png"
    image LLH_4_WNode3 = "W_connect_node.png"
    image LLH_4_WNode4 = "W_connect_node.png"
    image LLH_4_WNode5 = "W_connect_node.png"
    image LLH_4_RNode1 = "R_connect_node.png"
    image LLH_4_RNode2 = "R_connect_node.png"
    image LLH_4_RNode3 = "R_connect_node.png"
    image LLH_4_RNode4 = "R_connect_node.png"
    image LLH_4_RNode5 = "R_connect_node.png"
    image LLH_4_GNode1 = "G_connect_node.png"
    image LLH_4_GNode2 = "G_connect_node.png"
    image LLH_4_GNode3 = "G_connect_node.png"
    image LLH_4_GNode4 = "G_connect_node.png"
    image LLH_4_GNode5 = "G_connect_node.png"
    image LLH_4_BNode1 = "B_connect_node.png"
    image LLH_4_BNode2 = "B_connect_node.png"
    image LLH_4_BNode3 = "B_connect_node.png"
    image LLH_4_BNode4 = "B_connect_node.png"
    image LLH_4_BNode5 = "B_connect_node.png"
    image LLH_4_TNode1 = "T_connect_node.png"
    image LLH_4_TNode2 = "T_connect_node.png"
    image LLH_4_TNode3 = "T_connect_node.png"
    image LLH_4_PNode1 = "P_connect_node.png"
    image LLH_4_PNode2 = "P_connect_node.png"
    image LLH_4_PNode3 = "P_connect_node.png" 
    image LLH_4_BrNode1 = "Br_connect_node.png"
    image LLH_4_BrNode2 = "Br_connect_node.png"
    image LLH_4_BrNode3 = "Br_connect_node.png"
    
    if LLH_4_node1 == "None":
        show LLH_4_WNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node1 == "Red":
        show LLH_4_RNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node1 == "Green":
        show LLH_4_GNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node1 == "Blue":
        show LLH_4_BNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node1 == "Turq":
         show LLH_4_TNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0)
    elif LLH_4_node1 == "Purp":
         show LLH_4_PNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0)
    elif LLH_4_node1 == "Brown":
         show LLH_4_BrNode1 at Position(xpos = 467, xanchor = 0, ypos = 490, yanchor = 0)
        
    if LLH_4_node2 == "None":
        show LLH_4_WNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node2 == "Red":
        show LLH_4_RNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node2 == "Green":
        show LLH_4_GNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node2 == "Blue":
        show LLH_4_BNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node2 == "Turq":
        show LLH_4_TNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0)
    elif LLH_4_node2 == "Purp":
        show LLH_4_PNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0)
    elif LLH_4_node2 == "Brown":
        show LLH_4_BrNode2 at Position(xpos = 507, xanchor = 0, ypos = 490, yanchor = 0)
        
    if LLH_4_node3 == "None":
        show LLH_4_WNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node3 == "Red":
        show LLH_4_RNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node3 == "Green":
        show LLH_4_GNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node3 == "Blue":
        show LLH_4_BNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0) 
    elif LLH_4_node3 == "Turq":
        show LLH_4_TNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0)
    elif LLH_4_node3 == "Purp":
        show LLH_4_PNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0)
    elif LLH_4_node3 == "Brown":
        show LLH_4_BrNode3 at Position(xpos = 547, xanchor = 0, ypos = 490, yanchor = 0)
        
    if LLH_4_node4 == "None":
        show LLH_4_WNode4 at Position(xpos = 773, xanchor = 0, ypos = 663, yanchor = 0) 
    elif LLH_4_node4 == "Red":
        show LLH_4_RNode4 at Position(xpos = 773, xanchor = 0, ypos = 663, yanchor = 0) 
    elif LLH_4_node4 == "Green":
        show LLH_4_GNode4 at Position(xpos = 773, xanchor = 0, ypos = 663, yanchor = 0) 
    elif LLH_4_node4 == "Blue":
        show LLH_4_BNode4 at Position(xpos = 773, xanchor = 0, ypos = 663, yanchor = 0) 
        
    if LLH_4_node5 == "None":
        show LLH_4_WNode5 at Position(xpos = 773, xanchor = 0, ypos = 715, yanchor = 0) 
    elif LLH_4_node5 == "Red":
        show LLH_4_RNode5 at Position(xpos = 773, xanchor = 0, ypos = 715, yanchor = 0) 
    elif LLH_4_node5 == "Green":
        show LLH_4_GNode5 at Position(xpos = 773, xanchor = 0, ypos = 715, yanchor = 0) 
    elif LLH_4_node5 == "Blue":
        show LLH_4_BNode5 at Position(xpos = 773, xanchor = 0, ypos = 715, yanchor = 0) 
        
    #Redraw Ends *******************************************************************************
    hide LLH_4_BlueEnd1_Off
    hide LLH_4_BlueEnd2_Off
    hide LLH_4_GreenEnd_Off
    hide LLH_4_RedEnd1_Off
    hide LLH_4_RedEnd2_Off
    hide LLH_4_BlueEnd1_On
    hide LLH_4_BlueEnd2_On
    hide LLH_4_GreenEnd_On
    hide LLH_4_RedEnd1_On
    hide LLH_4_RedEnd2_On
    
    image LLH_4_BlueEnd1_Off = "B_end_off.png"
    image LLH_4_BlueEnd2_Off = "B_end_off.png"
    image LLH_4_GreenEnd_Off = "G_end_off.png"
    image LLH_4_RedEnd1_Off = "R_end_off.png"
    image LLH_4_RedEnd2_Off = "R_end_off.png"
    image LLH_4_BlueEnd1_On = "B_end_on.png"
    image LLH_4_BlueEnd2_On = "B_end_on.png"
    image LLH_4_GreenEnd_On = "G_end_on.png"
    image LLH_4_RedEnd1_On = "R_end_on.png"
    image LLH_4_RedEnd2_On = "R_end_on.png"
    
    if LLH_4_BEnd1 == "Off":
        show LLH_4_BlueEnd1_Off at Position(xpos = 850, xanchor = 0, ypos = 325, yanchor = 0)
    elif LLH_4_BEnd1 == "On":
        show LLH_4_BlueEnd1_On at Position(xpos = 850, xanchor = 0, ypos = 325, yanchor = 0)
        
    if LLH_4_BEnd2 == "Off":
        show LLH_4_BlueEnd2_Off at Position(xpos = 100, xanchor = 0, ypos = 505, yanchor = 0)
    elif LLH_4_BEnd2 == "On":
        show LLH_4_BlueEnd2_On at Position(xpos = 100, xanchor = 0, ypos = 505, yanchor = 0)
        
    if LLH_4_GEnd == "Off":
        show LLH_4_GreenEnd_Off at Position(xpos = 1000, xanchor = 0, ypos = 655, yanchor = 0)
    elif LLH_4_GEnd == "On":
        show LLH_4_GreenEnd_On at Position(xpos = 1000, xanchor = 0, ypos = 655, yanchor = 0)
        
    if LLH_4_REnd1 == "Off":
        show LLH_4_RedEnd1_Off at Position(xpos = 250, xanchor = 0, ypos = 325, yanchor = 0)
    elif LLH_4_REnd1 == "On":
        show LLH_4_RedEnd1_On at Position(xpos = 250, xanchor = 0, ypos = 325, yanchor = 0)
    
    if LLH_4_REnd2 == "Off":
        show LLH_4_RedEnd2_Off at Position(xpos = 1000, xanchor = 0, ypos = 455, yanchor = 0)
    elif LLH_4_REnd2 == "On":
        show LLH_4_RedEnd2_On at Position(xpos = 1000, xanchor = 0, ypos = 455, yanchor = 0)
        
    #Redraw While Nodes ***************************************************************************
    hide LLH_4_Green_While_Node_Off
    hide LLH_4_Green_While_Node_On
    
    image LLH_4_Green_While_Node_Off = "g_while_off.png"
    image LLH_4_Green_While_Node_On = "g_while_on.png"
    
    if LLH_4_GWhileNode == "Off":
        show LLH_4_Green_While_Node_Off at Position(xpos = 467, xanchor = 0, ypos = 555, yanchor = 0)
    elif LLH_4_GWhileNode == "On":
        show LLH_4_Green_While_Node_On at Position(xpos = 467, xanchor = 0, ypos = 555, yanchor = 0)
    
    #*********************************************************
    #********************* redraw gates **********************
    #*********************************************************  
    hide LLH_4_tile53
    hide LLH_4_tile54
    hide LLH_4_tile55
    hide LLH_4_tile56
    hide LLH_4_tile57
    hide LLH_4_tile58
    hide LLH_4_tile59
    hide LLH_4_tile60
    show LLH_4_tile53 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
    show LLH_4_tile54 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
    show LLH_4_tile55 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
    show LLH_4_tile56 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
    show LLH_4_tile57 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
    show LLH_4_tile58 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
    show LLH_4_tile59 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
    show LLH_4_tile60 at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)    

#win conditions ********
    if ifRin1 and (ifB1in2 or ifB2in2) and elsein3 and whileGin4 and (ifB1in5 or ifB2in5) and ifBGin6 == True and ifGRin7 == True and ifGin8 == True:
        image LLH_4_ifR = "R_if.png"
        show LLH_4_ifR at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        image LLH_4_ifG = "G_if.png"
        show LLH_4_ifG at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        image LLH_4_ifB1 = "B_if.png"
        show LLH_4_ifB1 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        image LLH_4_ifB2 = "B_if.png"
        show LLH_4_ifB2 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        image LLH_4_ifGR = "GR_if.png"
        show LLH_4_ifGR at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        image LLH_4_ifBG = "BG_if.png"
        show LLH_4_ifBG at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        image LLH_4_else = "G_else.png"
        show LLH_4_else at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        image LLH_4_whileG = "G_while.png"
        show LLH_4_whileG at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)

        image LLH_4_ifRBorder = "placeholder3.png"
        show LLH_4_ifRBorder at Position(xpos = 1385, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_4_ifGBorder = "placeholder3.png"
        show LLH_4_ifGBorder at Position(xpos = 1515, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_4_ifBBorder = "placeholder3.png"
        show LLH_4_ifBBorder at Position(xpos = 1645, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_4_ifGRBorder = "placeholder3.png"
        show LLH_4_ifGRBorder at Position(xpos = 1435, xanchor = 0, ypos = 780, yanchor = 0)
        image LLH_4_ifBGBorder = "placeholder3.png"
        show LLH_4_ifBGBorder at Position(xpos = 1575, xanchor = 0, ypos = 780, yanchor = 0)
        image LLH_4_elseBorder = "placeholder3.png"
        show LLH_4_elseBorder at Position(xpos = 1575, xanchor = 0, ypos = 490, yanchor = 0)
        image LLH_4_whileGBorder = "placeholder3.png"
        show LLH_4_whileGBorder at Position(xpos = 1435, xanchor = 0, ypos = 490, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_llHardWin
        jump llHardWin

#lose conditions ********
    if attempts == 0:
        
        show LLH_4_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
        show LLH_4_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
        show LLH_4_ifB1 at Position(xpos = ifB1x, xanchor = 0, ypos = ifB1y, yanchor = 0)
        show LLH_4_ifB2 at Position(xpos = ifB2x, xanchor = 0, ypos = ifB2y, yanchor = 0)
        show LLH_4_ifGR at Position(xpos = ifGRx, xanchor = 0, ypos = ifGRy, yanchor = 0)
        show LLH_4_ifBG at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
        show LLH_4_else at Position(xpos = elsex, xanchor = 0, ypos = elsey, yanchor = 0)
        show LLH_4_whileG at Position(xpos = whileGx, xanchor = 0, ypos = whileGy, yanchor = 0)
        
        show LLH_4_ifRBorder at Position(xpos = 1385, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_4_ifGBorder at Position(xpos = 1515, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_4_ifBBorder at Position(xpos = 1645, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_4_ifGRBorder at Position(xpos = 1435, xanchor = 0, ypos = 780, yanchor = 0)
        show LLH_4_ifBGBorder at Position(xpos = 1575, xanchor = 0, ypos = 780, yanchor = 0)
        show LLH_4_elseBorder at Position(xpos = 1575, xanchor = 0, ypos = 490, yanchor = 0)
        show LLH_4_whileGBorder at Position(xpos = 1435, xanchor = 0, ypos = 490, yanchor = 0)
        
        queue sound llLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            jump pg_llHardLose4
        $llHard_attempts +=1
        jump llHardLose
    
    jump gamefile_llh4

screen loopLogicHard_4Scr:
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
        idle "button_empty2.png"
        xpos 1463
        ypos 295
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 1545
        ypos 220
        focus_mask True
        action Jump("hints_llHard_4")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    text "Moves" xpos 1480 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1605 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1640 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover2.png"
                draggable False
                xpos gate1x ypos gate1y
           
            drag:
                drag_name "gate slot two"
                child "cover2.png"
                draggable False
                xpos gate2x ypos gate2y
                
            drag:
                drag_name "gate slot three"
                child "cover2.png"
                draggable False
                xpos gate3x ypos gate3y

            drag:
                drag_name "gate slot four"
                child "cover2.png"
                draggable False
                xpos gate4x ypos gate4y
                
            drag:
                drag_name "gate slot five"
                child "cover2.png"
                draggable False
                xpos gate5x ypos gate5y
           
            drag:
                drag_name "gate slot six"
                child "cover2.png"
                draggable False
                xpos gate6x ypos gate6y
                
            drag:
                drag_name "gate slot seven"
                child "cover2.png"
                draggable False
                xpos gate7x ypos gate7y

            drag:
                drag_name "gate slot eight"
                child "cover2.png"
                draggable False
                xpos gate8x ypos gate8y

            #Gate Slots
            drag:
                drag_name "while_G_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 490

            drag:
                drag_name "else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1575 ypos 490
                
            drag:
                drag_name "if_R_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1385 ypos 635

            drag:
                drag_name "if_G_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 635

            drag:
                drag_name "if_B_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1645 ypos 635
                
            drag:
                drag_name "if_GR_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 780

            drag:
                drag_name "if_BG_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1575 ypos 780
                
            #if gates
            drag:
                drag_name "if_R_gate"
                child "R_if.png"
                droppable False
                dragged gate_dragged
                xpos ifRx ypos ifRy
                
            drag:
                drag_name "if_G_gate"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos ifGx ypos ifGy
                
            drag:
                drag_name "if_B1_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos ifB1x ypos ifB1y

            drag:
                drag_name "if_B2_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos ifB2x ypos ifB2y    
                
            drag:
                drag_name "if_GR_gate"
                child "GR_if.png"
                droppable False
                dragged gate_dragged
                xpos ifGRx ypos ifGRy
                
            drag:
                drag_name "if_BG_gate"
                child "BG_if.png"
                droppable False
                dragged gate_dragged
                xpos ifBGx ypos ifBGy       
                
            #else gate
            drag:
                drag_name "else_gate"
                child "G_else.png"
                droppable False
                dragged gate_dragged
                xpos elsex ypos elsey

            #while gate
            drag:
                drag_name "while_G_gate"
                child "G_while.png"
                droppable False
                dragged gate_dragged
                xpos whileGx ypos whileGy  
