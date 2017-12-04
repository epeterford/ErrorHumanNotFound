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

label loopLogic_hard5:
    $config.skipping=None
    $quick_menu = False
    $game_menu = True
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg looplogic_bg
    

    #*********************************************************
    #************************* pipes *************************
    #*********************************************************     

    image LLH_5_pipe1 = "R_horizontal_ll.png"
    show LLH_5_pipe1 at Position(xpos = 571, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_5_pipe2 = "G_horizontal_ll.png"
    show LLH_5_pipe2 at Position(xpos = 571, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_5_pipe3 = "B_horizontal.png"
    show LLH_5_pipe3 at Position(xpos = 571, xanchor = 0, ypos = 450, yanchor = 0)
    image LLH_5_pipe4 = "G_horizontal_ll.png"
    show LLH_5_pipe4 at Position(xpos = 646, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_5_pipe5 = "W_horizontal_short.png"
    show LLH_5_pipe5 at Position(xpos = 721, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_5_pipe6 = "W_horizontal_short.png"
    show LLH_5_pipe6 at Position(xpos = 721, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_5_pipe7 = "W_horizontal_short.png"
    show LLH_5_pipe7 at Position(xpos = 721, xanchor = 0, ypos = 450, yanchor = 0)
    
    image LLH_5_pipe8 = "W_horizontal_short.png"
    show LLH_5_pipe8 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_5_pipe9 = "W_horizontal_short.png"
    show LLH_5_pipe9 at Position(xpos = 185, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_5_pipe10 = "W_horizontal_short.png"
    show LLH_5_pipe10 at Position(xpos = 320, xanchor = 0, ypos = 410, yanchor = 0)

    image LLH_5_pipe11 = "W_vertical.png"
    show LLH_5_pipe11 at Position(xpos = 475, xanchor = 0, ypos = 473, yanchor = 0)
    image LLH_5_pipe12 = "W_vertical.png"
    show LLH_5_pipe12 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
    image LLH_5_pipe13 = "W_vertical.png"
    show LLH_5_pipe13 at Position(xpos = 475, xanchor = 0, ypos = 548, yanchor = 0)
    image LLH_5_pipe14 = "W_vertical.png"
    show LLH_5_pipe14 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
    image LLH_5_pipe15 = "W_vertical.png"
    show LLH_5_pipe15 at Position(xpos = 475, xanchor = 0, ypos = 623, yanchor = 0)
    image LLH_5_pipe16 = "W_vertical.png"
    show LLH_5_pipe16 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)

    image LLH_5_pipe17 = "W_vertical.png"
    show LLH_5_pipe17 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
    image LLH_5_pipe18 = "W_vertical.png"
    show LLH_5_pipe18 at Position(xpos = 540, xanchor = 0, ypos = 473, yanchor = 0)
    image LLH_5_pipe19 = "W_vertical.png"
    show LLH_5_pipe19 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
    image LLH_5_pipe20 = "W_vertical_short.png"
    show LLH_5_pipe20 at Position(xpos = 540, xanchor = 0, ypos = 548, yanchor = 0)
    image LLH_5_pipe21 = "W_horizontal_short.png"
    show LLH_5_pipe21 at Position(xpos = 565, xanchor = 0, ypos = 622, yanchor = 0)
    image LLH_5_pipe22 = "W_horizontal.png"
    show LLH_5_pipe22 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
    image LLH_5_pipe23 = "W_corner_RT.png"
    show LLH_5_pipe23 at Position(xpos = 515, xanchor = 0, ypos = 600, yanchor = 0)
    image LLH_5_pipe24 = "W_corner_RT.png"
    image LLH_5_pipe24p = "W_corner_RT.png"
    image LLH_5_pipe23p = "W_corner_RT.png"
    show LLH_5_pipe24 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)

    image LLH_5_pipe25 = "W_vertical.png"
    show LLH_5_pipe25 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)
    image LLH_5_pipe26 = "W_vertical.png"
    show LLH_5_pipe26 at Position(xpos = 515, xanchor = 0, ypos = 300, yanchor = 0)
    
    image LLH_5_pipe27 = "W_vertical.png"
    show LLH_5_pipe27 at Position(xpos = 723, xanchor = 0, ypos = 310, yanchor = 0)
    image LLH_5_pipe28 = "W_vertical_short.png"
    show LLH_5_pipe28 at Position(xpos = 723, xanchor = 0, ypos = 260, yanchor = 0)
    image LLH_5_pipe29 = "W_horizontal.png"
    show LLH_5_pipe29 at Position(xpos = 770, xanchor = 0, ypos = 231, yanchor = 0)
    image LLH_5_pipe30 = "W_corner_RB.png"
    image LLH_5_pipe30p = "W_corner_RB.png"
    show LLH_5_pipe30 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
    image LLH_5_pipe31 = "W_horizontal_short.png"
    show LLH_5_pipe31 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)

    image LLH_5_pipe32 = "W_horizontal.png"
    show LLH_5_pipe32 at Position(xpos = 850, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_5_pipe33 = "W_horizontal_short.png"
    show LLH_5_pipe33 at Position(xpos = 925, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_5_pipe34 = "W_horizontal.png"
    show LLH_5_pipe34 at Position(xpos = 850, xanchor = 0, ypos = 450, yanchor = 0)
    image LLH_5_pipe35 = "W_horizontal_short.png"
    show LLH_5_pipe35 at Position(xpos = 925, xanchor = 0, ypos = 450, yanchor = 0)
    
    image LLH_5_pipe36 = "W_horizontal.png"
    show LLH_5_pipe36 at Position(xpos = 1020, xanchor = 0, ypos = 355, yanchor = 0)
    
    image LLH_5_pipe37 = "W_horizontal.png"
    show LLH_5_pipe37 at Position(xpos = 1020, xanchor = 0, ypos = 465, yanchor = 0) 
    
    image LLH_5_line1 = "y_horizontal_short_off.png"
    show LLH_5_line1 at Position(xpos = 410, xanchor = 0, ypos = 720, yanchor = 0)    
    image LLH_5_line2 = "y_vertical_short_off.png"
    show LLH_5_line2 at Position(xpos = 403, xanchor = 0, ypos = 670, yanchor = 0)
    image LLH_5_line3 = "y_vertical_short_off.png"
    show LLH_5_line3 at Position(xpos = 403, xanchor = 0, ypos = 610, yanchor = 0)    
    image LLH_5_line4 = "y_vertical_short_off.png"
    show LLH_5_line4 at Position(xpos = 403, xanchor = 0, ypos = 550, yanchor = 0)
    image LLH_5_line5 = "y_vertical_short_off.png"
    show LLH_5_line5 at Position(xpos = 403, xanchor = 0, ypos = 490, yanchor = 0)
    image LLH_5_line6 = "y_vertical_short_off.png"
    show LLH_5_line6 at Position(xpos = 403, xanchor = 0, ypos = 430, yanchor = 0)
    
    image LLH_5_line7 = "y_horizontal_short_off.png"
    show LLH_5_line7 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
    image LLH_5_line8 = "y_horizontal_short_off.png"
    show LLH_5_line8 at Position(xpos = 365, xanchor = 0, ypos = 750, yanchor = 0)
    image LLH_5_line9 = "y_vertical_short_off.png"
    show LLH_5_line9 at Position(xpos = 348, xanchor = 0, ypos = 720, yanchor = 0)
    image LLH_5_line10 = "y_vertical_short_off.png"
    show LLH_5_line10 at Position(xpos = 348, xanchor = 0, ypos = 667, yanchor = 0)
    image LLH_5_line11 = "y_vertical_short_off.png"
    show LLH_5_line11 at Position(xpos = 348, xanchor = 0, ypos = 608, yanchor = 0)
    image LLH_5_line12 = "y_vertical_short_off.png"
    show LLH_5_line12 at Position(xpos = 348, xanchor = 0, ypos = 548, yanchor = 0)
    image LLH_5_line13 = "y_vertical_short_off.png"
    show LLH_5_line13 at Position(xpos = 348, xanchor = 0, ypos = 488, yanchor = 0)
    image LLH_5_line14 = "y_vertical_short_off.png"
    show LLH_5_line14 at Position(xpos = 348, xanchor = 0, ypos = 428, yanchor = 0)
    
    image LLH_5_line15 = "y_horizontal_short_off.png"
    show LLH_5_line15 at Position(xpos = 580, xanchor = 0, ypos = 260, yanchor = 0)
    image LLH_5_line16 = "y_vertical_short_off.png"
    show LLH_5_line16 at Position(xpos = 623, xanchor = 0, ypos = 270, yanchor = 0)
    image LLH_5_line17 = "y_vertical_short_off.png"
    show LLH_5_line17 at Position(xpos = 623, xanchor = 0, ypos = 325, yanchor = 0)
    
    image LLH_5_line18 = "y_horizontal_short_off.png"
    show LLH_5_line18 at Position(xpos = 580, xanchor = 0, ypos = 210, yanchor = 0)
    image LLH_5_line19 = "y_horizontal_short_off.png"
    show LLH_5_line19 at Position(xpos = 630, xanchor = 0, ypos = 210, yanchor = 0)
    image LLH_5_line20 = "y_vertical_short_off.png"
    show LLH_5_line20 at Position(xpos = 673, xanchor = 0, ypos = 218, yanchor = 0)
    image LLH_5_line21 = "y_vertical_short_off.png"
    show LLH_5_line21 at Position(xpos = 673, xanchor = 0, ypos = 270, yanchor = 0)
    image LLH_5_line22 = "y_vertical_short_off.png"
    show LLH_5_line22 at Position(xpos = 673, xanchor = 0, ypos = 325, yanchor = 0)
    
    image LLH_5_line23 = "y_vertical_short_off.png"
    show LLH_5_line23 at Position(xpos = 623, xanchor = 0, ypos = 485, yanchor = 0)
    image LLH_5_line24 = "y_vertical_short_off.png"
    show LLH_5_line24 at Position(xpos = 623, xanchor = 0, ypos = 540, yanchor = 0)
    
    image LLH_5_line25 = "y_vertical_short_off.png"
    show LLH_5_line25 at Position(xpos = 673, xanchor = 0, ypos = 485, yanchor = 0)
    image LLH_5_line26 = "y_vertical_short_off.png"
    show LLH_5_line26 at Position(xpos = 673, xanchor = 0, ypos = 540, yanchor = 0)
     
    
    #*********************************************************
    #********************* start points **********************
    #*********************************************************
    image LLH_5_start = "Start.png"
    show LLH_5_start at Position(xpos = 470, xanchor = 0, ypos = 375, yanchor = 0)
    
    #*********************************************************
    #************************* gates *************************
    #*********************************************************
    
    image LLH_5_Gate1 = "blank_node.png"
    show LLH_5_Gate1 at Position (xpos = 220, xanchor = 0, ypos = 375, yanchor = 0)
    image LLH_5_Gate2 = "blank_node.png"
    show LLH_5_Gate2 at Position (xpos = 450, xanchor = 0, ypos = 698, yanchor = 0)
    image LLH_5_Gate3 = "blank_node.png"
    show LLH_5_Gate3 at Position (xpos = 470, xanchor = 0, ypos = 200, yanchor = 0)
    image LLH_5_Gate4 = "blank_node.png"
    show LLH_5_Gate4 at Position (xpos = 610, xanchor = 0, ypos = 595, yanchor = 0)
    image LLH_5_Gate5 = "blank_node.png"
    show LLH_5_Gate5 at Position (xpos = 770, xanchor = 0, ypos = 375, yanchor = 0)
    image LLH_5_Gate6 = "blank_node.png"
    show LLH_5_Gate6 at Position (xpos = 944, xanchor = 0, ypos = 320, yanchor = 0)
    image LLH_5_Gate7 = "blank_node.png"
    show LLH_5_Gate7 at Position (xpos = 944, xanchor = 0, ypos = 430, yanchor = 0)
    image LLH_5_Gate8 = "blank_node.png"
    show LLH_5_Gate8 at Position (xpos = 830, xanchor = 0, ypos = 195, yanchor = 0)

    
    #*********************************************************
    #********************** end points ***********************
    #*********************************************************    
    image LLH_5_BlueEnd1 = "B_end_off.png"
    show LLH_5_BlueEnd1 at Position(xpos = 1080, xanchor = 0, ypos = 320, yanchor = 0)
    image LLH_5_RedEnd1 = "R_end_off.png"
    show LLH_5_RedEnd1 at Position(xpos = 1080, xanchor = 0, ypos = 430, yanchor = 0)
    image LLH_5_GreenEnd1 = "G_end_off.png"
    show LLH_5_GreenEnd1 at Position(xpos = 90, xanchor = 0, ypos = 375, yanchor = 0)
    image LLH_5_GreenEnd2 = "G_end_off.png"
    show LLH_5_GreenEnd2 at Position(xpos = 980, xanchor = 0, ypos = 195, yanchor = 0)

    
    #*********************************************************
    #********************** conectors ************************
    #*********************************************************    
    image LLH_5_Connect_Pipe1 = "W_horizontal_short.png"
    show LLH_5_Connect_Pipe1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_5_Connect_Pipe2 = "W_horizontal_short.png"
    show LLH_5_Connect_Pipe2 at Position(xpos = 637, xanchor = 0, ypos = 368, yanchor = 0)
    image LLH_5_Connect_Pipe3 = "W_horizontal_short.png"
    show LLH_5_Connect_Pipe3 at Position(xpos = 687, xanchor = 0, ypos = 368, yanchor = 0)
    image LLH_5_Connect_Pipe4 = "W_horizontal_short.png"
    show LLH_5_Connect_Pipe4 at Position(xpos = 637, xanchor = 0, ypos = 450, yanchor = 0)
    image LLH_5_Connect_Pipe5 = "W_horizontal_short.png"
    show LLH_5_Connect_Pipe5 at Position(xpos = 687, xanchor = 0, ypos = 450, yanchor = 0)

    image LLH_5_Connect_Pipe6 = "W_connect_pipe_vertical.png"
    show LLH_5_Connect_Pipe6 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
    image LLH_5_Connect_Pipe7 = "W_connect_pipe_vertical.png"
    show LLH_5_Connect_Pipe7 at Position(xpos = 732, xanchor = 0, ypos = 420, yanchor = 0)

    image LLH_5_connector1 = "R_While_off.png"
    show LLH_5_connector1 at Position(xpos = 400, xanchor = 0, ypos = 408, yanchor = 0)
    image LLH_5_connector2 = "G_While_off.png"
    show LLH_5_connector2 at Position(xpos = 345, xanchor = 0, ypos = 408, yanchor = 0)
   
    image LLH_5_connector3 = "B_While_off.png"
    show LLH_5_connector3 at Position(xpos = 620, xanchor = 0, ypos = 367, yanchor = 0)
    image LLH_5_connector4 = "G_While_off.png"
    show LLH_5_connector4 at Position(xpos = 670, xanchor = 0, ypos = 367, yanchor = 0)
    image LLH_5_connector5 = "B_While_off.png"
    show LLH_5_connector5 at Position(xpos = 620, xanchor = 0, ypos = 447, yanchor = 0)
    image LLH_5_connector6 = "R_While_off.png"
    show LLH_5_connector6 at Position(xpos = 670, xanchor = 0, ypos = 447, yanchor = 0)
    image LLH_5_connector7 = "W_connect_node.png"
    show LLH_5_connector7 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0)
    image LLH_5_connector8 = "W_connect_node.png"
    show LLH_5_connector8 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0)
    image LLH_5_connector9 = "W_connect_node.png"
    show LLH_5_connector9 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0)

    image LLH_5_Transparent1 = "B_if_idle.png"
    show LLH_5_Transparent1 at Position(xpos = 1525, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_5_Transparent2 = "R_if_idle.png"
    show LLH_5_Transparent2 at Position(xpos = 1385, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_5_Transparent3 = "G_if_idle.png"
    show LLH_5_Transparent3 at Position(xpos = 1665, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_5_Transparent4 = "RB_if_idle.png"
    show LLH_5_Transparent4 at Position(xpos = 1435, xanchor = 0, ypos = 635, yanchor = 0)
    image LLH_5_Transparent5 = "BR_while_idle.png"
    show LLH_5_Transparent5 at Position(xpos = 1665, xanchor = 0, ypos = 760, yanchor = 0)
    image LLH_5_Transparent6 = "GR_while_idle.png"
    show LLH_5_Transparent6 at Position(xpos = 1525, xanchor = 0, ypos = 760, yanchor = 0)
    image LLH_5_Transparent7 = "BG_while_idle.png"
    show LLH_5_Transparent7 at Position(xpos = 1385, xanchor = 0, ypos = 760, yanchor = 0)
    image LLH_5_Transparent8 = "G_else_idle.png"
    show LLH_5_Transparent8 at Position(xpos = 1610, xanchor = 0, ypos = 635, yanchor = 0)

    image LLH_5_Border1 = "Placeholder3.png"
    show LLH_5_Border1 at Position(xpos = 1515, xanchor = 0, ypos = 500, yanchor = 0)
    image LLH_5_Border2 = "Placeholder3.png"
    show LLH_5_Border2 at Position(xpos = 1375, xanchor = 0, ypos = 500, yanchor = 0)
    image LLH_5_Border3 = "Placeholder3.png"
    show LLH_5_Border3 at Position(xpos = 1655, xanchor = 0, ypos = 500, yanchor = 0)
    image LLH_5_Border4 = "Placeholder3.png"
    show LLH_5_Border4 at Position(xpos = 1425, xanchor = 0, ypos = 625, yanchor = 0)
    image LLH_5_Border5 = "Placeholder3.png"
    show LLH_5_Border5 at Position(xpos = 1600, xanchor = 0, ypos = 625, yanchor = 0)
    image LLH_5_Border6 = "Placeholder3.png"
    show LLH_5_Border6 at Position(xpos = 1655, xanchor = 0, ypos = 750, yanchor = 0)
    image LLH_5_Border7 = "Placeholder3.png"
    show LLH_5_Border7 at Position(xpos = 1515, xanchor = 0, ypos = 750, yanchor = 0)
    image LLH_5_Border8 = "Placeholder3.png"
    show LLH_5_Border8 at Position(xpos = 1375, xanchor = 0, ypos = 750, yanchor = 0)

#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    #initial value assignment for dragables
    $ ifBx = 1525
    $ ifBy = 510
    
    $ ifRx = 1385
    $ ifRy = 510
    
    $ ifGx = 1665
    $ ifGy = 510
    
    $ ifRBx = 1435
    $ ifRBy = 635

    $ whileBRx = 1665
    $ whileBRy = 760
    
    $ whileGRx = 1525
    $ whileGRy = 760
    
    $ whileBGx = 1385
    $ whileBGy = 760
    
    $ elsex = 1610
    $ elsey = 635

    $ gate1x = 220
    $ gate1y = 375

    $ gate2x = 450
    $ gate2y = 698

    $ gate3x = 470
    $ gate3y = 200

    $ gate4x = 610
    $ gate4y = 595
   
    $ gate5x = 770
    $ gate5y = 375

    $ gate6x = 944
    $ gate6y = 320

    $ gate7x = 944
    $ gate7y = 430

    $ gate8x = 830
    $ gate8y = 195
    
   
    # check conditons for locations
    $ whileBRin1 = False
    $ whileBRin2 = False
    $ whileBRin3 = False
    $ whileBRin4 = False
    $ whileBRin5 = False
    $ whileBRin6 = False
    $ whileBRin7 = False
    $ whileBRin8 = False

    $ elsein1 = False
    $ elsein2 = False
    $ elsein3 = False
    $ elsein4 = False
    $ elsein5 = False
    $ elsein6 = False
    $ elsein7 = False
    $ elsein8 = False
    
    $ whileGRin1 = False
    $ whileGRin2 = False
    $ whileGRin3 = False
    $ whileGRin4 = False
    $ whileGRin5 = False
    $ whileGRin6 = False
    $ whileGRin7 = False
    $ whileGRin8 = False
    
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
    
    $ ifBin1 = False
    $ ifBin2 = False
    $ ifBin3 = False
    $ ifBin4 = False
    $ ifBin5 = False
    $ ifBin6 = False
    $ ifBin7 = False
    $ ifBin8 = False
    
    $ ifRBin1 = False
    $ ifRBin2 = False
    $ ifRBin3 = False
    $ ifRBin4 = False
    $ ifRBin5 = False
    $ ifRBin6 = False
    $ ifRBin7 = False
    $ ifRBin8 = False
    
    $ whileBGin1 = False
    $ whileBGin2 = False
    $ whileBGin3 = False
    $ whileBGin4 = False
    $ whileBGin5 = False
    $ whileBGin6 = False
    $ whileBGin7 = False
    $ whileBGin8 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
     
    #attempts for players
    $ attempts = 12
    
    # Color of each connect node
    $LLH_5_node1 = "None"
    $LLH_5_node2 = "None"
    $LLH_5_node3 = "None"
    $LLH_5_node4 = "None"
    $LLH_5_node5 = "None"
 
    jump gamefile_llh5
    
    
label gamefile_llh5:
    
    #calls game screen
    call screen loopLogicHard_5Scr

#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "if_R_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1385
                $ ifRBy = 760
                $ ifRBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if whileBRin4 == True:
                $ whileBRx= 1425
                $ whileBRy = 760
                $ whileBRin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False
            if whileGRin5 == True:
                $ whileGRx = 1385
                $ whileGRy = 760
                $ whileGRin5 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

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
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1425
                $ whileBGy = 760
                $ whileBGin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False
            if whileGRin8 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin8 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if whileBRin4 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False
            if whileGRin5 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin5 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1435
                $ whileBRy = 760
                $ whileBRin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False
            if whileGRin8 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin8 = False

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
    if gate_name == "if_B_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1425
                $ ifRBy = 635
                $ ifRBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

            #sets values for checks
            $ ifBx = gate1x
            $ ifBy = gate1y
            $ ifBin1 = True
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1425
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

            #sets values for checks
            $ ifBx = gate2x
            $ ifBy = gate2y
            $ ifBin1 = False
            $ ifBin2 = True
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

            #sets values for checks
            $ ifBx = gate3x
            $ ifBy = gate3y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = True
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if whileBRin4 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

            #sets values for checks
            $ ifBx = gate4x
            $ ifBy = gate4y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = True
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False
            if whileGRin5 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin5 = False

            #sets values for checks
            $ ifBx = gate5x
            $ ifBy = gate5y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = True
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

            #sets values for checks
            $ ifBx = gate6x
            $ ifBy = gate6y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = True
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

            #sets values for checks
            $ ifBx = gate7x
            $ ifBy = gate7y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = True
            $ ifBin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False
            if whileGRin8 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin8 = False

            #sets values for checks
            $ ifBx = gate8x
            $ ifBy = gate8y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = True


    #the fourth logic gate *******************************************************************************
    if gate_name == "if_RB_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1425
                $ whileBRy = 760
                $ whileBRin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

            #sets values for checks
            $ ifRBx = gate1x
            $ ifRBy = gate1y
            $ ifRBin1 = True
            $ ifRBin2 = False
            $ ifRBin3 = False
            $ ifRBin4 = False
            $ ifRBin5 = False
            $ ifRBin6 = False
            $ ifRBin7 = False
            $ ifRBin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

            #sets values for checks
            $ ifRBx = gate2x
            $ ifRBy = gate2y
            $ ifRBin1 = False
            $ ifRBin2 = True
            $ ifRBin3 = False
            $ ifRBin4 = False
            $ ifRBin5 = False
            $ ifRBin6 = False
            $ ifRBin7 = False
            $ ifRBin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

            #sets values for checks
            $ ifRBx = gate3x
            $ ifRBy = gate3y
            $ ifRBin1 = False
            $ ifRBin2 = False
            $ ifRBin3 = True
            $ ifRBin4 = False
            $ ifRBin5 = False
            $ ifRBin6 = False
            $ ifRBin7 = False
            $ ifRBin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if whileBRin4 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

            #sets values for checks
            $ ifRBx = gate4x
            $ ifRBy = gate4y
            $ ifRBin1 = False
            $ ifRBin2 = False
            $ ifRBin3 = False
            $ ifRBin4 = True
            $ ifRBin5 = False
            $ ifRBin6 = False
            $ ifRBin7 = False
            $ ifRBin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False
            if whileGRin5 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin5 = False

            #sets values for checks
            $ ifRBx = gate5x
            $ ifRBy = gate5y
            $ ifRBin1 = False
            $ ifRBin2 = False
            $ ifRBin3 = False
            $ ifRBin4 = False
            $ ifRBin5 = True
            $ ifRBin6 = False
            $ ifRBin7 = False
            $ ifRBin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

            #sets values for checks
            $ ifRBx = gate6x
            $ ifRBy = gate6y
            $ ifRBin1 = False
            $ ifRBin2 = False
            $ ifRBin3 = False
            $ ifRBin4 = False
            $ ifRBin5 = False
            $ ifRBin6 = True
            $ ifRBin7 = False
            $ ifRBin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

            #sets values for checks
            $ ifRBx = gate7x
            $ ifRBy = gate7y
            $ ifRBin1 = False
            $ ifRBin2 = False
            $ ifRBin3 = False
            $ ifRBin4 = False
            $ ifRBin5 = False
            $ ifRBin6 = False
            $ ifRBin7 = True
            $ ifRBin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False
            if whileGRin8 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin8 = False

            #sets values for checks
            $ ifRBx = gate8x
            $ ifRBy = gate8y
            $ ifRBin1 = False
            $ ifRBin2 = False
            $ ifRBin3 = False
            $ ifRBin4 = False
            $ ifRBin5 = False
            $ ifRBin6 = False
            $ ifRBin7 = False
            $ ifRBin8 = True
            
            
    #the fifth logic gate *******************************************************************************
    if gate_name == "while_BG_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

            #sets values for checks
            $ whileBGx = gate1x
            $ whileBGy = gate1y
            $ whileBGin1 = True
            $ whileBGin2 = False
            $ whileBGin3 = False
            $ whileBGin4 = False
            $ whileBGin5 = False
            $ whileBGin6 = False
            $ whileBGin7 = False
            $ whileBGin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

            #sets values for checks
            $ whileBGx = gate2x
            $ whileBGy = gate2y
            $ whileBGin1 = False
            $ whileBGin2 = True
            $ whileBGin3 = False
            $ whileBGin4 = False
            $ whileBGin5 = False
            $ whileBGin6 = False
            $ whileBGin7 = False
            $ whileBGin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

            #sets values for checks
            $ whileBGx = gate3x
            $ whileBGy = gate3y
            $ whileBGin1 = False
            $ whileBGin2 = False
            $ whileBGin3 = True
            $ whileBGin4 = False
            $ whileBGin5 = False
            $ whileBGin6 = False
            $ whileBGin7 = False
            $ whileBGin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBRin4 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

            #sets values for checks
            $ whileBGx = gate4x
            $ whileBGy = gate4y
            $ whileBGin1 = False
            $ whileBGin2 = False
            $ whileBGin3 = False
            $ whileBGin4 = True
            $ whileBGin5 = False
            $ whileBGin6 = False
            $ whileBGin7 = False
            $ whileBGin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False
            if whileGRin5 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin5 = False

            #sets values for checks
            $ whileBGx = gate5x
            $ whileBGy = gate5y
            $ whileBGin1 = False
            $ whileBGin2 = False
            $ whileBGin3 = False
            $ whileBGin4 = False
            $ whileBGin5 = True
            $ whileBGin6 = False
            $ whileBGin7 = False
            $ whileBGin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

            #sets values for checks
            $ whileBGx = gate6x
            $ whileBGy = gate6y
            $ whileBGin1 = False
            $ whileBGin2 = False
            $ whileBGin3 = False
            $ whileBGin4 = False
            $ whileBGin5 = False
            $ whileBGin6 = True
            $ whileBGin7 = False
            $ whileBGin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

            #sets values for checks
            $ whileBGx = gate7x
            $ whileBGy = gate7y
            $ whileBGin1 = False
            $ whileBGin2 = False
            $ whileBGin3 = False
            $ whileBGin4 = False
            $ whileBGin5 = False
            $ whileBGin6 = False
            $ whileBGin7 = True
            $ whileBGin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False
            if whileGRin8 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin8 = False

            #sets values for checks
            $ whileBGx = gate8x
            $ whileBGy = gate8y
            $ whileBGin1 = False
            $ whileBGin2 = False
            $ whileBGin3 = False
            $ whileBGin4 = False
            $ whileBGin5 = False
            $ whileBGin6 = False
            $ whileBGin7 = False
            $ whileBGin8 = True
            
            
    #the sixth logic gate *******************************************************************************
    if gate_name == "else_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if whileBRin4 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if whileGRin5 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin5 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

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
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if whileGRin8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False

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


    #the seventh logic gate *******************************************************************************
    if gate_name == "while_GR_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if whileBRin1 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False

            #sets values for checks
            $ whileGRx = gate1x
            $ whileGRy = gate1y
            $ whileGRin1 = True
            $ whileGRin2 = False
            $ whileGRin3 = False
            $ whileGRin4 = False
            $ whileGRin5 = False
            $ whileGRin6 = False
            $ whileGRin7 = False
            $ whileGRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if whileBRin2 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False

            #sets values for checks
            $ whileGRx = gate2x
            $ whileGRy = gate2y
            $ whileGRin1 = False
            $ whileGRin2 = True
            $ whileGRin3 = False
            $ whileGRin4 = False
            $ whileGRin5 = False
            $ whileGRin6 = False
            $ whileGRin7 = False
            $ whileGRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if whileBRin3 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False

            #sets values for checks
            $ whileGRx = gate3x
            $ whileGRy = gate3y
            $ whileGRin1 = False
            $ whileGRin2 = False
            $ whileGRin3 = True
            $ whileGRin4 = False
            $ whileGRin5 = False
            $ whileGRin6 = False
            $ whileGRin7 = False
            $ whileGRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if whileBRin4 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False

            #sets values for checks
            $ whileGRx = gate4x
            $ whileGRy = gate4y
            $ whileGRin1 = False
            $ whileGRin2 = False
            $ whileGRin3 = False
            $ whileGRin4 = True
            $ whileGRin5 = False
            $ whileGRin6 = False
            $ whileGRin7 = False
            $ whileGRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if whileBRin5 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False

            #sets values for checks
            $ whileGRx = gate5x
            $ whileGRy = gate5y
            $ whileGRin1 = False
            $ whileGRin2 = False
            $ whileGRin3 = False
            $ whileGRin4 = False
            $ whileGRin5 = True
            $ whileGRin6 = False
            $ whileGRin7 = False
            $ whileGRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if whileBRin6 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False

            #sets values for checks
            $ whileGRx = gate6x
            $ whileGRy = gate6y
            $ whileGRin1 = False
            $ whileGRin2 = False
            $ whileGRin3 = False
            $ whileGRin4 = False
            $ whileGRin5 = False
            $ whileGRin6 = True
            $ whileGRin7 = False
            $ whileGRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if whileBRin7 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False

            #sets values for checks
            $ whileGRx = gate7x
            $ whileGRy = gate7y
            $ whileGRin1 = False
            $ whileGRin2 = False
            $ whileGRin3 = False
            $ whileGRin4 = False
            $ whileGRin5 = False
            $ whileGRin6 = False
            $ whileGRin7 = True
            $ whileGRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin8 = False
            if whileBRin8 == True:
                $ whileBRx = 1665
                $ whileBRy = 760
                $ whileBRin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False

            #sets values for checks
            $ whileGRx = gate8x
            $ whileGRy = gate8y
            $ whileGRin1 = False
            $ whileGRin2 = False
            $ whileGRin3 = False
            $ whileGRin4 = False
            $ whileGRin5 = False
            $ whileGRin6 = False
            $ whileGRin7 = False
            $ whileGRin8 = True


    #the fourth logic gate *******************************************************************************
    if gate_name == "while_BR_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin1 = False
            if elsein1 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein1 = False
            if whileGRin1 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin1 = False

            #sets values for checks
            $ whileBRx = gate1x
            $ whileBRy = gate1y
            $ whileBRin1 = True
            $ whileBRin2 = False
            $ whileBRin3 = False
            $ whileBRin4 = False
            $ whileBRin5 = False
            $ whileBRin6 = False
            $ whileBRin7 = False
            $ whileBRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin2 = False
            if elsein2 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein2 = False
            if whileGRin2 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin2 = False

            #sets values for checks
            $ whileBRx = gate2x
            $ whileBRy = gate2y
            $ whileBRin1 = False
            $ whileBRin2 = True
            $ whileBRin3 = False
            $ whileBRin4 = False
            $ whileBRin5 = False
            $ whileBRin6 = False
            $ whileBRin7 = False
            $ whileBRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin3 = False
            if elsein3 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein3 = False
            if whileGRin3 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin3 = False

            #sets values for checks
            $ whileBRx = gate3x
            $ whileBRy = gate3y
            $ whileBRin1 = False
            $ whileBRin2 = False
            $ whileBRin3 = True
            $ whileBRin4 = False
            $ whileBRin5 = False
            $ whileBRin6 = False
            $ whileBRin7 = False
            $ whileBRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin4 = False
            if elsein4 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein4 = False
            if whileGRin4 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin4 = False

            #sets values for checks
            $ whileBRx = gate4x
            $ whileBRy = gate4y
            $ whileBRin1 = False
            $ whileBRin2 = False
            $ whileBRin3 = False
            $ whileBRin4 = True
            $ whileBRin5 = False
            $ whileBRin6 = False
            $ whileBRin7 = False
            $ whileBRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin5 = False
            if elsein5 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein5 = False
            if whileGRin5 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin5 = False

            #sets values for checks
            $ whileBRx = gate5x
            $ whileBRy = gate5y
            $ whileBRin1 = False
            $ whileBRin2 = False
            $ whileBRin3 = False
            $ whileBRin4 = False
            $ whileBRin5 = True
            $ whileBRin6 = False
            $ whileBRin7 = False
            $ whileBRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin6 = False
            if elsein6 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein6 = False
            if whileGRin6 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin6 = False

            #sets values for checks
            $ whileBRx = gate6x
            $ whileBRy = gate6y
            $ whileBRin1 = False
            $ whileBRin2 = False
            $ whileBRin3 = False
            $ whileBRin4 = False
            $ whileBRin5 = False
            $ whileBRin6 = True
            $ whileBRin7 = False
            $ whileBRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin7 = False
            if elsein7 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein7 = False
            if whileGRin7 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin7 = False

            #sets values for checks
            $ whileBRx = gate7x
            $ whileBRy = gate7y
            $ whileBRin1 = False
            $ whileBRin2 = False
            $ whileBRin3 = False
            $ whileBRin4 = False
            $ whileBRin5 = False
            $ whileBRin6 = False
            $ whileBRin7 = True
            $ whileBRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1385
                $ ifRy = 510
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1665
                $ ifGy = 510
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1525
                $ ifBy = 510
                $ ifBin8 = False
            if ifRBin8 == True:
                $ ifRBx = 1435
                $ ifRBy = 635
                $ ifRBin8 = False
            if whileBGin8 == True:
                $ whileBGx = 1385
                $ whileBGy = 760
                $ whileBGin8 = False
            if elsein8 == True:
                $ elsex = 1610
                $ elsey = 635
                $ elsein8 = False
            if whileGRin8 == True:
                $ whileGRx = 1525
                $ whileGRy = 760
                $ whileGRin8 = False

            #sets values for checks
            $ whileBRx = gate8x
            $ whileBRy = gate8y
            $ whileBRin1 = False
            $ whileBRin2 = False
            $ whileBRin3 = False
            $ whileBRin4 = False
            $ whileBRin5 = False
            $ whileBRin6 = False
            $ whileBRin7 = False
            $ whileBRin8 = True



    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "R_if_gate_return" or slot_name == "G_if_gate_return" or slot_name == "B_if_gate_return" or slot_name == "BG_while_gate_return" or
        slot_name == "GR_while_gate_return" or slot_name == "BR_while_gate_return" or slot_name == "else_gate_return" or slot_name == "RB_if_gate_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
            
      
    else:
        if slot_name != "null" and (temp_slot != slot_name or gate_name != temp_gate):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "R_if_gate_return":
                $ attempts +=1
                if gate_name == "if_R_gate":
                    $ ifRx = 1385
                    $ ifRy = 510
                    $ ifRin1 = False
                    $ ifRin2 = False
                    $ ifRin3 = False
                    $ ifRin4 = False
                    $ ifRin5 = False
                    $ ifRin6 = False
                    $ ifRin7 = False
                    $ ifRin8 = False
            if slot_name == "G_if_gate_return":
                $ attempts +=1
                if gate_name == "if_G_gate":
                    $ ifGx = 1665
                    $ ifGy = 510
                    $ ifGin1 = False
                    $ ifGin2 = False
                    $ ifGin3 = False
                    $ ifGin4 = False
                    $ ifGin5 = False
                    $ ifGin6 = False
                    $ ifGin7 = False
                    $ ifGin8 = False
            if slot_name == "B_if_gate_return":
                $ attempts +=1
                if gate_name == "if_B_gate":
                    $ ifBx = 1525
                    $ ifBy = 510
                    $ ifBin1 = False
                    $ ifBin2 = False
                    $ ifBin3 = False
                    $ ifBin4 = False
                    $ ifBin5 = False
                    $ ifBin6 = False
                    $ ifBin7 = False
                    $ ifBin8 = False
            if slot_name == "BG_while_gate_return":
                $ attempts +=1
                if gate_name == "while_BG_gate":
                    $ whileBGx = 1385
                    $ whileBGy = 760
                    $ whileBGin1 = False
                    $ whileBGin2 = False
                    $ whileBGin3 = False
                    $ whileBGin4 = False
                    $ whileBGin5 = False
                    $ whileBGin6 = False
                    $ whileBGin7 = False
                    $ whileBGin8 = False
            if slot_name == "GR_while_gate_return":
                $ attempts +=1
                if gate_name == "while_GR_gate":
                    $ whileGRx = 1525
                    $ whileGRy = 760
                    $ whileGRin1 = False
                    $ whileGRin2 = False
                    $ whileGRin3 = False
                    $ whileGRin4 = False
                    $ whileGRin5 = False
                    $ whileGRin6 = False
                    $ whileGRin7 = False
                    $ whileGRin8 = False
            if slot_name == "BR_while_gate_return":
                $ attempts +=1
                if gate_name == "while_BR_gate":
                    $ whileBRx = 1665
                    $ whileBRy = 760
                    $ whileBRin1 = False
                    $ whileBRin2 = False
                    $ whileBRin3 = False
                    $ whileBRin4 = False
                    $ whileBRin5 = False
                    $ whileBRin6 = False
                    $ whileBRin7 = False
                    $ whileBRin8 = False
            if slot_name == "else_gate_return":
                $ attempts +=1
                if gate_name == "else_gate":
                    $ elsex = 1610
                    $ elsey = 635
                    $ elsein1 = False
                    $ elsein2 = False
                    $ elsein3 = False
                    $ elsein4 = False
                    $ elsein5 = False
                    $ elsein6 = False
                    $ elsein7 = False
                    $ elsein8 = False
            if slot_name == "RB_if_gate_return":
                $ attempts +=1
                if gate_name == "if_RB_gate":
                    $ ifRBx = 1435
                    $ ifRBy = 635
                    $ ifRBin1 = False
                    $ ifRBin2 = False
                    $ ifRBin3 = False
                    $ ifRBin4 = False
                    $ ifRBin5 = False
                    $ ifRBin6 = False
                    $ ifRBin7 = False
                    $ ifRBin8 = False


#*******************************************
#************image zone********************* 
#*******************************************
    $LLH_5_node1 = "None"
    $LLH_5_node2 = "None"
    $LLH_5_node3 = "None"
    
    $LLH_5_BEnd1 = "Off"
    $LLH_5_GEnd1 = "Off"
    $LLH_5_GEnd2 = "Off"
    $LLH_5_REnd = "Off"
    
    $LLH_5_RWhileNode = "Off"
    $LLH_5_BWhileNode = "Off"
    $LLH_5_GWhileNode = "Off"
    $LLH_5_BWhileNode2 = "Off"
    $LLH_5_GWhileNode2 = "Off"
    $LLH_5_RWhileNode2 = "Off"

# Else in gate 1 cases **************************************************************************            
    hide LLH_5_colorTile1
    hide LLH_5_colorTile2
    hide LLH_5_colorTileLC1
    hide LLH_5_colorTileLG1
    hide LLH_5_colorTileLG3
    hide LLH_5_colorTile115
    hide LLH_5_colorTile116
    hide LLH_5_colorTileLCB1
    hide LLH_5_colorTileLB1
    hide LLH_5_colorTileLB3
    hide LLH_5_colorTile115
    hide LLH_5_colorTile116
    hide LLH_5_colorTileLCB1
    hide LLH_5_colorTileLB1
    hide LLH_5_colorTileLR3
    hide LLH_5_colorTile117
    hide LLH_5_colorTile118
    hide LLH_5_colorTileLCR1
    hide LLH_5_colorTileLR1
    hide LLH_5_colorTile4
    hide LLH_5_colorTile5
    hide LLH_5_colorTile6
    hide LLH_5_colorTile7
    hide LLH_5_colorTile8
    hide LLH_5_colorTile9
    hide LLH_5_OnLine1
    hide LLH_5_OnLine2
    hide LLH_5_OnLine3
    hide LLH_5_OnLine4
    hide LLH_5_OnLine5
    hide LLH_5_OnLine6
    hide LLH_5_OnLine7
    hide LLH_5_OnLine8
    hide LLH_5_OnLine9
    hide LLH_5_OnLine10
    hide LLH_5_OnLine11
    hide LLH_5_OnLine12
    hide LLH_5_OnLine13
    hide LLH_5_OnLine14
    hide LLH_5_colorTileLG1
    hide LLH_5_colorTileLC1
    hide LLH_5_colorTileB4
    hide LLH_5_colorTileB5
    hide LLH_5_colorTileB6
    hide LLH_5_colorTileB7
    hide LLH_5_colorTileB8
    hide LLH_5_colorTileB9
    hide LLH_5_colorTile10
    hide LLH_5_colorTile11
    hide LLH_5_colorTile22
    hide LLH_5_colorTile23
    hide LLH_5_OnLine15
    hide LLH_5_OnLine16
    hide LLH_5_OnLine17
    hide LLH_5_OnLine18
    hide LLH_5_OnLine19
    hide LLH_5_OnLine20
    hide LLH_5_OnLine21
    hide LLH_5_OnLine22
    hide LLH_5_colorTileR10
    hide LLH_5_colorTileR11
    hide LLH_5_colorTile12
    hide LLH_5_colorTile13
    hide LLH_5_colorTile14
    hide LLH_5_colorTileG12
    hide LLH_5_colorTileG13
    hide LLH_5_colorTileG14
    hide LLH_5_colorTile15
    hide LLH_5_colorTile16
    hide LLH_5_colorTile17
    hide LLH_5_colorTileG15
    hide LLH_5_colorTileG16
    hide LLH_5_colorTileG17
    hide LLH_5_colorTile19
    hide LLH_5_colorTile20
    hide LLH_5_OnLine23
    hide LLH_5_OnLine24
    hide LLH_5_OnLine25
    hide LLH_5_OnLine26
    hide LLH_5_colorTile18
    hide LLH_5_colorTile21
    hide LLH_5_colorTile74
    hide LLH_5_colorTile24
    hide LLH_5_colorTile26
    hide LLH_5_colorTile27
    hide LLH_5_colorTile29
    hide LLH_5_colorTile30
    hide LLH_5_colorTile31
    hide LLH_5_colorTile32
    hide LLH_5_colorTile33
    hide LLH_5_colorTile34
    hide LLH_5_colorTile44
    hide LLH_5_colorTile53
    hide LLH_5_colorTile51
    hide LLH_5_colorTile35
    hide LLH_5_colorTile37
    hide LLH_5_colorTileBr30
    hide LLH_5_colorTileBr31
    hide LLH_5_colorTileBr32
    hide LLH_5_colorTileBr33
    hide LLH_5_colorTileBr34
    hide LLH_5_colorTileP30
    hide LLH_5_colorTileP31
    hide LLH_5_colorTileP32
    hide LLH_5_colorTileP33
    hide LLH_5_colorTileT30
    hide LLH_5_colorTileT31
    hide LLH_5_colorTileT32
    hide LLH_5_colorTileT33
    hide LLH_5_colorTileT34
    hide LLH_5_colorTileB30
    hide LLH_5_colorTileB31
    hide LLH_5_colorTileB32
    hide LLH_5_colorTileB33
    hide LLH_5_colorTileB34
    hide LLH_5_colorTileR30
    hide LLH_5_colorTileR31
    hide LLH_5_colorTileR32
    hide LLH_5_colorTileR33
    hide LLH_5_pipe30p
    hide LLH_5_pipe24p
    hide LLH_5_pipe23p
    hide LLH_5_colorTile74
    hide LLH_5_colorTile1P
    hide LLH_5_colorTile2P
    hide LLH_5_colorTileLC1P
    hide LLH_5_colorTileLG1P
    hide LLH_5_colorTileLG3P
    hide LLH_5_colorTileB40
    #START SOUNDS HERE
    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    if ifGin1:
        image LLH_5_colorTileLG3 = "G_horizontal_short.png"
        show LLH_5_colorTileLG3 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
        if whileGRin2:
            image LLH_5_colorTile1 = "G_horizontal_short.png"
            show LLH_5_colorTile1 at Position(xpos = 172, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTile2 = "G_horizontal_short.png"
            show LLH_5_colorTile2 at Position(xpos = 320, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTileLG1 = "G_horizontal_short.png"
            show LLH_5_colorTileLG1 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTileLC1 = "G_horizontal_short.png"
            show LLH_5_colorTileLC1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            $LLH_5_GEnd1 = "On"
        if whileBRin2:
            show LLH_5_colorTileLG1 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTileLC1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            
    if ifRBin1:
        image LLH_5_colorTileLG3P = "P_horizontal_short.png"
        show LLH_5_colorTileLG3P at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
        if whileGRin2:
            image LLH_5_colorTile1P = "P_horizontal_short.png"
            image LLH_5_colorTileLC1P = "P_horizontal_short.png"
            image LLH_5_colorTile2P = "P_horizontal_short.png"
            image LLH_5_colorTileLG1P = "P_horizontal_short.png"
            show LLH_5_colorTile1P at Position(xpos = 172, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTile2P at Position(xpos = 320, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTileLG1P at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTileLC1P at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
        if whileBRin2:
            show LLH_5_colorTileLG1P at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTileLC1P at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            
    if ifBin1:
        image LLH_5_colorTileLB3 = "B_horizontal_short.png"
        show LLH_5_colorTileLB3 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
        if whileGRin2:
            image LLH_5_colorTile115 = "B_horizontal_short.png"
            show LLH_5_colorTile115 at Position(xpos = 172, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTile116 = "B_horizontal_short.png"
            show LLH_5_colorTile116 at Position(xpos = 320, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTileLB1 = "B_horizontal_short.png"
            show LLH_5_colorTileLB1 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTileLCB1 = "B_horizontal_short.png"
            show LLH_5_colorTileLCB1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
        if whileBRin2:
            show LLH_5_colorTileLB1 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTileLCB1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            
    if ifRin1:
        image LLH_5_colorTileLR3 = "R_horizontal_short.png"
        show LLH_5_colorTileLR3 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
        if whileGRin2:
            image LLH_5_colorTile117 = "R_horizontal_short.png"
            show LLH_5_colorTile117 at Position(xpos = 172, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTile118 = "R_horizontal_short.png"
            show LLH_5_colorTile118 at Position(xpos = 320, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTileLR1 = "R_horizontal_short.png"
            show LLH_5_colorTileLR1 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_5_colorTileLCR1 = "R_horizontal_short.png"
            show LLH_5_colorTileLCR1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
        if whileBRin2:
            show LLH_5_colorTileLR1 at Position(xpos = 420, xanchor = 0, ypos = 410, yanchor = 0)
            show LLH_5_colorTileLCR1 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
    
    if whileGRin2:
        image LLH_5_colorTile4 = "R_vertical_ll.png"
        image LLH_5_colorTile5 = "R_vertical_ll.png"
        image LLH_5_colorTile6 = "R_vertical_ll.png"
        show LLH_5_colorTile4 at Position(xpos = 472, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile5 at Position(xpos = 472, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile6 at Position(xpos = 472, xanchor = 0, ypos = 623, yanchor = 0)
        
        image LLH_5_colorTile7 = "G_vertical_ll.png"
        image LLH_5_colorTile8 = "G_vertical_ll.png"
        image LLH_5_colorTile9 = "G_vertical_ll.png"
        show LLH_5_colorTile7 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile8 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile9 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)
        
        image LLH_5_OnLine1 = "y_horizontal_short_on.png"
        image LLH_5_OnLine2 = "y_vertical_short_on.png"
        image LLH_5_OnLine3 = "y_vertical_short_on.png"
        image LLH_5_OnLine4 = "y_vertical_short_on.png"
        image LLH_5_OnLine5 = "y_vertical_short_on.png"
        image LLH_5_OnLine6 = "y_vertical_short_on.png"
        show LLH_5_OnLine1 at Position(xpos = 410, xanchor = 0, ypos = 720, yanchor = 0)    
        show LLH_5_OnLine2 at Position(xpos = 403, xanchor = 0, ypos = 670, yanchor = 0)
        show LLH_5_OnLine3 at Position(xpos = 403, xanchor = 0, ypos = 610, yanchor = 0)    
        show LLH_5_OnLine4 at Position(xpos = 403, xanchor = 0, ypos = 550, yanchor = 0)
        show LLH_5_OnLine5 at Position(xpos = 403, xanchor = 0, ypos = 490, yanchor = 0)
        show LLH_5_OnLine6 at Position(xpos = 403, xanchor = 0, ypos = 430, yanchor = 0)

        image LLH_5_OnLine7 = "y_horizontal_short_on.png"
        image LLH_5_OnLine8 = "y_horizontal_short_on.png"
        image LLH_5_OnLine9 = "y_vertical_short_on.png"
        image LLH_5_OnLine10 = "y_vertical_short_on.png"
        image LLH_5_OnLine11 = "y_vertical_short_on.png"
        image LLH_5_OnLine12 = "y_vertical_short_on.png"
        image LLH_5_OnLine13 = "y_vertical_short_on.png"
        image LLH_5_OnLine14 = "y_vertical_short_on.png"
        
        show LLH_5_OnLine7 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
        show LLH_5_OnLine8 at Position(xpos = 365, xanchor = 0, ypos = 750, yanchor = 0)
        show LLH_5_OnLine9 at Position(xpos = 348, xanchor = 0, ypos = 720, yanchor = 0)
        show LLH_5_OnLine10 at Position(xpos = 348, xanchor = 0, ypos = 667, yanchor = 0)
        show LLH_5_OnLine11 at Position(xpos = 348, xanchor = 0, ypos = 608, yanchor = 0)
        show LLH_5_OnLine12 at Position(xpos = 348, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_OnLine13 at Position(xpos = 348, xanchor = 0, ypos = 488, yanchor = 0)
        show LLH_5_OnLine14 at Position(xpos = 348, xanchor = 0, ypos = 428, yanchor = 0)
        
        $LLH_5_RWhileNode = "On"
        $LLH_5_GWhileNode = "On"
        
#    if not(whileGRin2): 
#        $LLH_5_RWhileNode = "Off"
#        $LLH_5_GWhileNode = "Off"
        
    if whileBRin2:
        show LLH_5_colorTile4 at Position(xpos = 472, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile5 at Position(xpos = 472, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile6 at Position(xpos = 472, xanchor = 0, ypos = 623, yanchor = 0)
        show LLH_5_OnLine1 at Position(xpos = 410, xanchor = 0, ypos = 720, yanchor = 0)    
        show LLH_5_OnLine2 at Position(xpos = 403, xanchor = 0, ypos = 670, yanchor = 0)
        show LLH_5_OnLine3 at Position(xpos = 403, xanchor = 0, ypos = 610, yanchor = 0)    
        show LLH_5_OnLine4 at Position(xpos = 403, xanchor = 0, ypos = 550, yanchor = 0)
        show LLH_5_OnLine5 at Position(xpos = 403, xanchor = 0, ypos = 490, yanchor = 0)
        show LLH_5_OnLine6 at Position(xpos = 403, xanchor = 0, ypos = 430, yanchor = 0)
        
        image LLH_5_colorTileB7 = "B_vertical.png"
        image LLH_5_colorTileB8 = "B_vertical.png"
        image LLH_5_colorTileB9 = "B_vertical.png"
        show LLH_5_colorTileB7 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTileB8 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTileB9 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)
        
        $LLH_5_RWhileNode = "On"
#    if(not(whileBRin2)):
#        $LLH_5_RWhileNode = "Off"
        
    if whileBGin2 == True:
        show LLH_5_colorTile7 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile8 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile9 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)

        image LLH_5_colorTileB4 = "B_vertical.png"
        image LLH_5_colorTileB5 = "B_vertical.png"
        image LLH_5_colorTileB6 = "B_vertical.png"
        show LLH_5_colorTileB4 at Position(xpos = 472, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTileB5 at Position(xpos = 472, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTileB6 at Position(xpos = 472, xanchor = 0, ypos = 623, yanchor = 0)
        
        show LLH_5_OnLine7 at Position(xpos = 410, xanchor = 0, ypos = 750, yanchor = 0)
        show LLH_5_OnLine8 at Position(xpos = 365, xanchor = 0, ypos = 750, yanchor = 0)
        show LLH_5_OnLine9 at Position(xpos = 348, xanchor = 0, ypos = 720, yanchor = 0)
        show LLH_5_OnLine10 at Position(xpos = 348, xanchor = 0, ypos = 667, yanchor = 0)
        show LLH_5_OnLine11 at Position(xpos = 348, xanchor = 0, ypos = 608, yanchor = 0)
        show LLH_5_OnLine12 at Position(xpos = 348, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_OnLine13 at Position(xpos = 348, xanchor = 0, ypos = 488, yanchor = 0)
        show LLH_5_OnLine14 at Position(xpos = 348, xanchor = 0, ypos = 428, yanchor = 0)
        
        $LLH_5_GWhileNode = "On"
#    elif not(whileBGin2):
#        $LLH_5_GWhileNode = "Off"

    if ifGin2:
        show LLH_5_colorTile7 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile8 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile9 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)
        
    if ifRin2:
        show LLH_5_colorTile4 at Position(xpos = 472, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile5 at Position(xpos = 472, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile6 at Position(xpos = 472, xanchor = 0, ypos = 623, yanchor = 0)
            
    if ifRBin2:
        show LLH_5_colorTile4 at Position(xpos = 472, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile5 at Position(xpos = 472, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile6 at Position(xpos = 472, xanchor = 0, ypos = 623, yanchor = 0)
        
        show LLH_5_colorTileB7 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTileB8 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTileB9 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)
        
    if ifBin2:
        show LLH_5_colorTileB7 at Position(xpos = 495, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTileB8 at Position(xpos = 495, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTileB9 at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)
        
    if whileBGin3:
        image LLH_5_colorTile10 = "G_vertical_ll.png"
        show LLH_5_colorTile10 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)
        
        image LLH_5_colorTile11 = "B_vertical.png"
        show LLH_5_colorTile11 at Position(xpos = 515, xanchor = 0, ypos = 300, yanchor = 0)
        
        image LLH_5_colorTile22 = "R_horizontal_short.png"
        image LLH_5_colorTile23 = "R_horizontal_short.png"
        show LLH_5_colorTile22 at Position(xpos = 637, xanchor = 0, ypos = 368, yanchor = 0)
        show LLH_5_colorTile23 at Position(xpos = 687, xanchor = 0, ypos = 368, yanchor = 0)
        
        image LLH_5_OnLine15 = "y_horizontal_short_on.png"
        image LLH_5_OnLine16 = "y_vertical_short_on.png"
        image LLH_5_OnLine17 = "y_vertical_short_on.png"
        show LLH_5_OnLine15 at Position(xpos = 580, xanchor = 0, ypos = 260, yanchor = 0)
        show LLH_5_OnLine16 at Position(xpos = 623, xanchor = 0, ypos = 270, yanchor = 0)
        show LLH_5_OnLine17 at Position(xpos = 623, xanchor = 0, ypos = 325, yanchor = 0)
    
        image LLH_5_OnLine18 = "y_horizontal_short_on.png"
        image LLH_5_OnLine19 = "y_horizontal_short_on.png"
        image LLH_5_OnLine20 = "y_vertical_short_on.png"
        image LLH_5_OnLine21 = "y_vertical_short_on.png"
        image LLH_5_OnLine22 = "y_vertical_short_on.png"
        show LLH_5_OnLine18 at Position(xpos = 580, xanchor = 0, ypos = 210, yanchor = 0)
        show LLH_5_OnLine19 at Position(xpos = 630, xanchor = 0, ypos = 210, yanchor = 0)
        show LLH_5_OnLine20 at Position(xpos = 673, xanchor = 0, ypos = 218, yanchor = 0)
        show LLH_5_OnLine21 at Position(xpos = 673, xanchor = 0, ypos = 270, yanchor = 0)
        show LLH_5_OnLine22 at Position(xpos = 673, xanchor = 0, ypos = 325, yanchor = 0)
        
        $LLH_5_BWhileNode = "On"
        $LLH_5_GWhileNode2 = "On"
        
    if not(whileBGin3):
        $LLH_5_BWhileNode = "Off"
        $LLH_5_GWhileNode2 = "Off"
        
        if whileBRin3:
            image LLH_5_colorTileR10 = "R_vertical_ll.png"
            show LLH_5_colorTileR10 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)
            show LLH_5_colorTile11 at Position(xpos = 515, xanchor = 0, ypos = 300, yanchor = 0)
            show LLH_5_OnLine15 at Position(xpos = 580, xanchor = 0, ypos = 260, yanchor = 0)
            show LLH_5_OnLine16 at Position(xpos = 623, xanchor = 0, ypos = 270, yanchor = 0)
            show LLH_5_OnLine17 at Position(xpos = 623, xanchor = 0, ypos = 325, yanchor = 0)
            show LLH_5_colorTile22 at Position(xpos = 637, xanchor = 0, ypos = 368, yanchor = 0)
        
            $LLH_5_BWhileNode = "On"

        if whileGRin3:
            image LLH_5_colorTileR11 = "R_vertical_ll.png"
            show LLH_5_colorTileR11 at Position(xpos = 515, xanchor = 0, ypos = 300, yanchor = 0)
            show LLH_5_colorTile10 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)
            
            show LLH_5_OnLine18 at Position(xpos = 580, xanchor = 0, ypos = 210, yanchor = 0)
            show LLH_5_OnLine19 at Position(xpos = 630, xanchor = 0, ypos = 210, yanchor = 0)
            show LLH_5_OnLine20 at Position(xpos = 673, xanchor = 0, ypos = 218, yanchor = 0)
            show LLH_5_OnLine21 at Position(xpos = 673, xanchor = 0, ypos = 270, yanchor = 0)
            show LLH_5_OnLine22 at Position(xpos = 673, xanchor = 0, ypos = 325, yanchor = 0)
            
            $LLH_5_GWhileNode2 = "On"
        
        if ifRBin3:
            show LLH_5_colorTileR10 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)
            show LLH_5_colorTile11 at Position(xpos = 515, xanchor = 0, ypos = 300, yanchor = 0)
        
        if ifBin3:
            show LLH_5_colorTile11 at Position(xpos = 515, xanchor = 0, ypos = 300, yanchor = 0)
        
        if ifGin3:
            show LLH_5_colorTile10 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)

        if ifRin3:
            show LLH_5_colorTileR10 at Position(xpos = 495, xanchor = 0, ypos = 300, yanchor = 0)
            
    if whileBRin4:
        image LLH_5_colorTile12 = "B_vertical.png"
        image LLH_5_colorTile13 = "B_vertical.png"
        image LLH_5_colorTile14 = "B_horizontal.png"
        show LLH_5_colorTile12 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile13 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
        show LLH_5_colorTile14 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
            
        image LLH_5_colorTile15 = "R_vertical_ll.png"
        image LLH_5_colorTile16 = "R_horizontal_short.png"
        image LLH_5_colorTile17 = "R_vertical_short.png"
        show LLH_5_colorTile15 at Position(xpos = 540, xanchor = 0, ypos = 473, yanchor = 0)
        show LLH_5_colorTile16 at Position(xpos = 565, xanchor = 0, ypos = 622, yanchor = 0)
        show LLH_5_colorTile17 at Position(xpos = 540, xanchor = 0, ypos = 548, yanchor = 0)
        
        image LLH_5_OnLine23 = "y_vertical_short_on.png"
        image LLH_5_OnLine24 = "y_vertical_short_on.png"
        show LLH_5_OnLine23 at Position(xpos = 623, xanchor = 0, ypos = 485, yanchor = 0)
        show LLH_5_OnLine24 at Position(xpos = 623, xanchor = 0, ypos = 540, yanchor = 0)
    
        image LLH_5_OnLine25 = "y_vertical_short_on.png"
        image LLH_5_OnLine26 = "y_vertical_short_on.png"
        show LLH_5_OnLine25 at Position(xpos = 673, xanchor = 0, ypos = 485, yanchor = 0)
        show LLH_5_OnLine26 at Position(xpos = 673, xanchor = 0, ypos = 540, yanchor = 0)

        image LLH_5_colorTile19 = "B_horizontal_short.png"
        image LLH_5_colorTile20 = "B_horizontal_short.png"
        show LLH_5_colorTile19 at Position(xpos = 637, xanchor = 0, ypos = 450, yanchor = 0)
        show LLH_5_colorTile20 at Position(xpos = 687, xanchor = 0, ypos = 450, yanchor = 0)
        
        $LLH_5_BWhileNode2 = "On"
        $LLH_5_RWhileNode2 = "On"
        
    elif whileBRin4 == False:
        $LLH_5_BWhileNode2 = "Off"
        $LLH_5_RWhileNode2 = "Off"
        
        if ifRBin4 == True:
            show LLH_5_colorTile12 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTile13 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
            show LLH_5_colorTile14 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
                
            show LLH_5_colorTile15 at Position(xpos = 540, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTile16 at Position(xpos = 565, xanchor = 0, ypos = 622, yanchor = 0)
            show LLH_5_colorTile17 at Position(xpos = 540, xanchor = 0, ypos = 548, yanchor = 0)
            
        if ifBin4:
            show LLH_5_colorTile12 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTile13 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
            show LLH_5_colorTile14 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
            
        if whileBGin4:
            show LLH_5_colorTile12 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTile13 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
            show LLH_5_colorTile14 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
            show LLH_5_colorTile19 at Position(xpos = 637, xanchor = 0, ypos = 450, yanchor = 0)
            
            show LLH_5_OnLine23 at Position(xpos = 623, xanchor = 0, ypos = 485, yanchor = 0)
            show LLH_5_OnLine24 at Position(xpos = 623, xanchor = 0, ypos = 540, yanchor = 0)
            
            image LLH_5_colorTileG15 = "G_vertical_ll.png"
            image LLH_5_colorTileG16 = "G_horizontal_short.png"
            image LLH_5_colorTileG17 = "G_vertical_short.png"
            show LLH_5_colorTileG15 at Position(xpos = 540, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTileG16 at Position(xpos = 565, xanchor = 0, ypos = 622, yanchor = 0)
            show LLH_5_colorTileG17 at Position(xpos = 540, xanchor = 0, ypos = 548, yanchor = 0)
        
            $LLH_5_BWhileNode2 = "On"
        
        if ifRin4:
            show LLH_5_colorTile15 at Position(xpos = 540, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTile16 at Position(xpos = 565, xanchor = 0, ypos = 622, yanchor = 0)
            show LLH_5_colorTile17 at Position(xpos = 540, xanchor = 0, ypos = 548, yanchor = 0)
        if whileGRin4:
            $LLH_5_RWhileNode2 = "On"
            show LLH_5_colorTile15 at Position(xpos = 540, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTile16 at Position(xpos = 565, xanchor = 0, ypos = 622, yanchor = 0)
            show LLH_5_colorTile17 at Position(xpos = 540, xanchor = 0, ypos = 548, yanchor = 0)
            show LLH_5_OnLine25 at Position(xpos = 673, xanchor = 0, ypos = 485, yanchor = 0)
            show LLH_5_OnLine26 at Position(xpos = 673, xanchor = 0, ypos = 540, yanchor = 0)
            image LLH_5_colorTileG12 = "G_vertical_ll.png"
            image LLH_5_colorTileG13 = "G_vertical_ll.png"
            image LLH_5_colorTileG14 = "G_horizontal_ll.png"
            show LLH_5_colorTileG12 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTileG13 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
            show LLH_5_colorTileG14 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
            
        if ifGin4:
            show LLH_5_colorTileG12 at Position(xpos = 520, xanchor = 0, ypos = 473, yanchor = 0)
            show LLH_5_colorTileG13 at Position(xpos = 520, xanchor = 0, ypos = 548, yanchor = 0)
            show LLH_5_colorTileG14 at Position(xpos = 540, xanchor = 0, ypos = 645, yanchor = 0)
            
    #################################GATE 5,6,7, and 8########################################
    if ifRBin5:
        if whileBRin4:
            image LLH_5_colorTile18 = "B_horizontal_short.png"
            show LLH_5_colorTile18 at Position(xpos = 721, xanchor = 0, ypos = 450, yanchor = 0)
        if whileBGin3:
            image LLH_5_colorTile21 = "R_horizontal_short.png"
            show LLH_5_colorTile21 at Position(xpos = 721, xanchor = 0, ypos = 370, yanchor = 0)
        if whileBRin4 and whileBGin3:
            if ifRin6:
                image LLH_5_colorTile35 = "R_horizontal_ll.png"
                show LLH_5_colorTile35 at Position(xpos = 870, xanchor = 0, ypos = 370, yanchor = 0)
                image LLH_5_colorTile37 = "R_horizontal_short.png"
                show LLH_5_colorTile37 at Position(xpos = 1044, xanchor = 0, ypos = 355, yanchor = 0)
            if ifBin6:
                image LLH_5_colorTile24 = "B_horizontal.png"
                show LLH_5_colorTile24 at Position(xpos = 870, xanchor = 0, ypos = 370, yanchor = 0)
                image LLH_5_colorTile26 = "B_horizontal_short.png"
                show LLH_5_colorTile26 at Position(xpos = 1044, xanchor = 0, ypos = 355, yanchor = 0)
                $LLH_5_BEnd1 = "On"
            if ifRin7:
                image LLH_5_colorTile27 = "R_horizontal_ll.png"
                show LLH_5_colorTile27 at Position(xpos = 870, xanchor = 0, ypos = 450, yanchor = 0)
                image LLH_5_colorTile29 = "R_horizontal_short.png"
                show LLH_5_colorTile29 at Position(xpos = 1044, xanchor = 0, ypos = 465, yanchor = 0)
                $LLH_5_REnd = "On"
            if ifBin7:
                image LLH_5_colorTile51 = "B_horizontal.png"
                show LLH_5_colorTile51 at Position(xpos = 870, xanchor = 0, ypos = 450, yanchor = 0)
                image LLH_5_colorTile53 = "B_horizontal_short.png"
                show LLH_5_colorTile53 at Position(xpos = 1044, xanchor = 0, ypos = 465, yanchor = 0)
            if elsein8:
                image LLH_5_colorTile30 = "G_vertical_ll.png"
                show LLH_5_colorTile30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
                image LLH_5_colorTile31 = "G_vertical_short.png"
                show LLH_5_colorTile31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
                image LLH_5_colorTile32 = "G_horizontal_ll.png"
                show LLH_5_colorTile32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
                image LLH_5_colorTile33 = "G_horizontal_short.png"
                show LLH_5_colorTile33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
                image LLH_5_colorTile34 = "G_connect_pipe_vertical.png"
                show LLH_5_colorTile34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
                image LLH_5_colorTile44 = "W_corner_RB.png"
                show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
                $LLH_5_GEnd2 = "On"
                $LLH_5_node1 = "Green"
                $LLH_5_node2 = "Green"
    if ifGin8:
        show LLH_5_colorTile30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
        show LLH_5_colorTile31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
        show LLH_5_colorTile32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
        show LLH_5_colorTile33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
        show LLH_5_colorTile34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
        show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
        $LLH_5_GEnd2 = "On"
        $LLH_5_node1 = "Green"
        $LLH_5_node2 = "Green"
                
    if ifRin8 and whileBGin3:
        $LLH_5_node1 = "Red"
        image LLH_5_colorTileR30 = "R_vertical_ll.png"
        show LLH_5_colorTileR30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
        image LLH_5_colorTileR31 = "R_vertical_short.png"
        show LLH_5_colorTileR31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
        image LLH_5_colorTileR32 = "R_horizontal_ll.png"
        show LLH_5_colorTileR32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
        image LLH_5_colorTileR33 = "R_horizontal_short.png"
        show LLH_5_colorTileR33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
        show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
    
    if ifBin8 and whileBRin4:
        $LLH_5_node1 = "Blue"
        $LLH_5_node2 = "Blue"
        $LLH_5_node3 = "Blue"
        image LLH_5_colorTileB30 = "B_vertical.png"
        show LLH_5_colorTileB30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
        image LLH_5_colorTileB31 = "B_vertical_short.png"
        show LLH_5_colorTileB31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
        image LLH_5_colorTileB32 = "B_horizontal.png"
        show LLH_5_colorTileB32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
        image LLH_5_colorTileB33 = "B_horizontal_short.png"
        show LLH_5_colorTileB33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
        image LLH_5_colorTileB34 = "B_connect_pipe_vertical.png"
        show LLH_5_colorTileB34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
        image LLH_5_colorTileB40 = "B_connect_pipe_vertical.png"
        show LLH_5_colorTileB40 at Position(xpos = 732, xanchor = 0, ypos = 405, yanchor = 0)
        show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
    if ifRBin8 and whileBRin4 and whileBGin3:
        $LLH_5_node1 = "Purp"
        $LLH_5_node2 = "Blue"
        $LLH_5_node3 = "Blue"
        image LLH_5_colorTileP30 = "P_vertical_ll.png"
        show LLH_5_colorTileP30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
        image LLH_5_colorTileP31 = "P_vertical_short.png"
        show LLH_5_colorTileP31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
        image LLH_5_colorTileP32 = "P_horizontal_ll.png"
        show LLH_5_colorTileP32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
        image LLH_5_colorTileP33 = "P_horizontal_short.png"
        show LLH_5_colorTileP33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
        show LLH_5_colorTileB34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
        show LLH_5_colorTileB40 at Position(xpos = 732, xanchor = 0, ypos = 405, yanchor = 0)
        show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
        
    if ifGin5:
        image LLH_5_colorTile74 = "G_horizontal_short.png"
        show LLH_5_colorTile74 at Position(xpos = 721, xanchor = 0, ypos = 410, yanchor = 0)
        if elsein8:
            $LLH_5_node1 = "Purp"
            $LLH_5_node2 = "Blue"
            $LLH_5_node3 = "Blue"
            image LLH_5_colorTileP30 = "P_vertical_ll.png"
            show LLH_5_colorTileP30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
            image LLH_5_colorTileP31 = "P_vertical_short.png"
            show LLH_5_colorTileP31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
            image LLH_5_colorTileP32 = "P_horizontal_ll.png"
            show LLH_5_colorTileP32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
            image LLH_5_colorTileP33 = "P_horizontal_short.png"
            show LLH_5_colorTileP33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
            show LLH_5_colorTileB34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
            show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
            show LLH_5_colorTileB40 at Position(xpos = 732, xanchor = 0, ypos = 405, yanchor = 0)
            
    if (ifRin5):
        if whileBGin3:
            show LLH_5_colorTile21 at Position(xpos = 721, xanchor = 0, ypos = 370, yanchor = 0)           
        if elsein8 and whileBRin4:
            $LLH_5_node1 = "Turq"
            $LLH_5_node2 = "Turq"
            $LLH_5_node3 = "Blue"
            image LLH_5_colorTileT30 = "T_vertical_ll.png"
            show LLH_5_colorTileT30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
            image LLH_5_colorTileT31 = "T_vertical_short.png"
            show LLH_5_colorTileT31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
            image LLH_5_colorTileT32 = "T_horizontal_ll.png"
            show LLH_5_colorTileT32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
            image LLH_5_colorTileT33 = "T_horizontal_short.png"
            show LLH_5_colorTileT33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
            image LLH_5_colorTileT34 = "T_connect_pipe_vertical.png"
            show LLH_5_colorTileT34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
            show LLH_5_colorTileB40 at Position(xpos = 732, xanchor = 0, ypos = 405, yanchor = 0)
            show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
            
    if ifBin5:
        if whileBRin4:
            show LLH_5_colorTile18 at Position(xpos = 721, xanchor = 0, ypos = 450, yanchor = 0)
        if elsein8 and whileBGin3:
            $LLH_5_node2 = "Green"
            $LLH_5_node1 = "Brown"
            image LLH_5_colorTileBr30 = "Br_vertical_ll.png"
            show LLH_5_colorTileBr30 at Position(xpos = 720, xanchor = 0, ypos = 310, yanchor = 0)
            image LLH_5_colorTileBr31 = "Br_vertical_short.png"
            show LLH_5_colorTileBr31 at Position(xpos = 720, xanchor = 0, ypos = 260, yanchor = 0)
            image LLH_5_colorTileBr32 = "Br_horizontal_ll.png"
            show LLH_5_colorTileBr32 at Position(xpos = 760, xanchor = 0, ypos = 231, yanchor = 0)
            image LLH_5_colorTileBr33 = "Br_horizontal_short.png"
            show LLH_5_colorTileBr33 at Position(xpos = 930, xanchor = 0, ypos = 230, yanchor = 0)
            image LLH_5_colorTileBr34 = "Br_connect_pipe_vertical.png"
            show LLH_5_colorTileBr34 at Position(xpos = 732, xanchor = 0, ypos = 380, yanchor = 0)
            show LLH_5_colorTile44 at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)

    show LLH_5_pipe30p at Position(xpos = 696, xanchor = 0, ypos = 205, yanchor = 0)
    show LLH_5_pipe24p at Position(xpos = 495, xanchor = 0, ypos = 623, yanchor = 0)
    show LLH_5_pipe23p at Position(xpos = 515, xanchor = 0, ypos = 600, yanchor = 0)
            
    #Redraw Connect Nodes *********************************************************************
    hide LLH_5_WNode1
    hide LLH_5_WNode2
    hide LLH_5_WNode3
    hide LLH_5_RNode1
    hide LLH_5_RNode2
    hide LLH_5_RNode3
    hide LLH_5_GNode1
    hide LLH_5_GNode2
    hide LLH_5_GNode3
    hide LLH_5_BNode1
    hide LLH_5_BNode2
    hide LLH_5_BNode3
    hide LLH_5_TNode1
    hide LLH_5_TNode2
    hide LLH_5_TNode3
    hide LLH_5_PNode1
    hide LLH_5_PNode2
    hide LLH_5_PNode3
    hide LLH_5_BrNode1
    hide LLH_5_BrNode2
    hide LLH_5_BrNode3
    
    image LLH_5_WNode1 = "W_connect_node.png"
    image LLH_5_WNode2 = "W_connect_node.png"
    image LLH_5_WNode3 = "W_connect_node.png"
    image LLH_5_RNode1 = "R_connect_node.png"
    image LLH_5_RNode2 = "R_connect_node.png"
    image LLH_5_RNode3 = "R_connect_node.png"
    image LLH_5_GNode1 = "G_connect_node.png"
    image LLH_5_GNode2 = "G_connect_node.png"
    image LLH_5_GNode3 = "G_connect_node.png"
    image LLH_5_BNode1 = "B_connect_node.png"
    image LLH_5_BNode2 = "B_connect_node.png"
    image LLH_5_BNode3 = "B_connect_node.png"
    image LLH_5_BrNode1 = "Br_connect_node.png"
    image LLH_5_BrNode2 = "Br_connect_node.png"
    image LLH_5_BrNode3 = "Br_connect_node.png"
    image LLH_5_TNode1 = "T_connect_node.png"
    image LLH_5_TNode2 = "T_connect_node.png"
    image LLH_5_TNode3 = "T_connect_node.png"
    image LLH_5_PNode1 = "P_connect_node.png"
    image LLH_5_PNode2 = "P_connect_node.png"
    image LLH_5_PNode3 = "P_connect_node.png"
    
    
    if LLH_5_node1 == "None":
        show LLH_5_WNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0) 
    elif LLH_5_node1 == "Red":
        show LLH_5_RNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0) 
    elif LLH_5_node1 == "Green":
        show LLH_5_GNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0) 
    elif LLH_5_node1 == "Blue":
        show LLH_5_BNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0) 
    elif LLH_5_node1 == "Turq":
         show LLH_5_TNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0)
    elif LLH_5_node1 == "Purp":
         show LLH_5_PNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0)
    elif LLH_5_node1 == "Brown":
         show LLH_5_BrNode1 at Position(xpos = 720, xanchor = 0, ypos = 367, yanchor = 0)
    
    if LLH_5_node2 == "None":
        show LLH_5_WNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_5_node2 == "Red":
        show LLH_5_RNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_5_node2 == "Green":
        show LLH_5_GNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_5_node2 == "Blue":
        show LLH_5_BNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_5_node2 == "Turq":
        show LLH_5_TNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0)
    elif LLH_5_node2 == "Purp":
        show LLH_5_PNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0)
    elif LLH_5_node2 == "Brown":
        show LLH_5_BrNode2 at Position(xpos = 720, xanchor = 0, ypos = 407, yanchor = 0)
        
    if LLH_5_node3 == "None":
        show LLH_5_WNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
    elif LLH_5_node3 == "Red":
        show LLH_5_RNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
    elif LLH_5_node3 == "Green":
        show LLH_5_GNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
    elif LLH_5_node3 == "Blue":
        show LLH_5_BNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
    elif LLH_5_node3 == "Turq":
        show LLH_5_TNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
    elif LLH_5_node3 == "Purp":
        show LLH_5_PNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
    elif LLH_5_node3 == "Brown":
        show LLH_5_BrNode3 at Position(xpos = 720, xanchor = 0, ypos = 447, yanchor = 0) 
 
    
    #Redraw Ends *******************************************************************************
    hide LLH_5_BlueEnd1_Off
    hide LLH_5_BlueEnd2_Off
    hide LLH_5_GreenEnd1_Off
    hide LLH_5_GreenEnd2_Off
    hide LLH_5_RedEnd_Off
    hide LLH_5_BlueEnd1_On
    hide LLH_5_BlueEnd2_On
    hide LLH_5_GreenEnd1_On
    hide LLH_5_GreenEnd2_On
    hide LLH_5_RedEnd_On
    
    image LLH_5_BlueEnd1_Off = "B_end_off.png"
    image LLH_5_BlueEnd2_Off = "B_end_off.png"
    image LLH_5_GreenEnd1_Off = "G_end_off.png"
    image LLH_5_GreenEnd2_Off = "G_end_off.png"
    image LLH_5_RedEnd_Off = "R_end_off.png"
    image LLH_5_BlueEnd1_On = "B_end_on.png"
    image LLH_5_BlueEnd2_On = "B_end_on.png"
    image LLH_5_GreenEnd1_On = "G_end_on.png"
    image LLH_5_GreenEnd2_On = "G_end_on.png"
    image LLH_5_RedEnd_On = "R_end_on.png"
    
    if LLH_5_BEnd1 == "Off":
        show LLH_5_BlueEnd1_Off at Position(xpos = 1080, xanchor = 0, ypos = 320, yanchor = 0)
    elif LLH_5_BEnd1 == "On":
        show LLH_5_BlueEnd1_On at Position(xpos = 1080, xanchor = 0, ypos = 320, yanchor = 0)
        
    if LLH_5_GEnd1 == "Off":
        show LLH_5_GreenEnd1_Off at Position(xpos = 90, xanchor = 0, ypos = 375, yanchor = 0)
    elif LLH_5_GEnd1 == "On":
        show LLH_5_GreenEnd1_On at Position(xpos = 90, xanchor = 0, ypos = 375, yanchor = 0)
        
    if LLH_5_GEnd2 == "Off":
        show LLH_5_GreenEnd2_Off at Position(xpos = 980, xanchor = 0, ypos = 195, yanchor = 0)
    elif LLH_5_GEnd2 == "On":
        show LLH_5_GreenEnd2_On at Position(xpos = 980, xanchor = 0, ypos = 195, yanchor = 0)
        
    if LLH_5_REnd == "Off":
        show LLH_5_RedEnd_Off at Position(xpos = 1080, xanchor = 0, ypos = 430, yanchor = 0)
    elif LLH_5_REnd == "On":
        show LLH_5_RedEnd_On at Position(xpos = 1080, xanchor = 0, ypos = 430, yanchor = 0)
    
    #Redraw While Nodes ***************************************************************************
    hide LLH_5_Red_While_Node_Off
    hide LLH_5_Red_While_Node_On
    hide LLH_5_Blue_While_Node_Off
    hide LLH_5_Blue_While_Node_On
    hide LLH_5_Green_While_Node_Off
    hide LLH_5_Green_While_Node_On
    hide LLH_5_Red_While_Node2_Off
    hide LLH_5_Red_While_Node2_On
    hide LLH_5_Blue_While_Node2_Off
    hide LLH_5_Blue_While_Node2_On
    hide LLH_5_Green_While_Node2_Off
    hide LLH_5_Green_While_Node2_On
    
    image LLH_5_Red_While_Node_Off = "r_while_off.png"
    image LLH_5_Red_While_Node_On = "r_while_on.png"
    image LLH_5_Blue_While_Node_Off = "b_while_off.png"
    image LLH_5_Blue_While_Node_On = "b_while_on.png"
    image LLH_5_Green_While_Node_Off = "g_while_off.png"
    image LLH_5_Green_While_Node_On = "g_while_on.png"
    image LLH_5_Red_While_Node2_Off = "r_while_off.png"
    image LLH_5_Red_While_Node2_On = "r_while_on.png"
    image LLH_5_Blue_While_Node2_Off = "b_while_off.png"
    image LLH_5_Blue_While_Node2_On = "b_while_on.png"
    image LLH_5_Green_While_Node2_Off = "g_while_off.png"
    image LLH_5_Green_While_Node2_On = "g_while_on.png"
    
    if LLH_5_RWhileNode == "Off":
        show LLH_5_Red_While_Node_Off at Position(xpos = 400, xanchor = 0, ypos = 408, yanchor = 0)
    elif LLH_5_RWhileNode == "On":
        show LLH_5_Red_While_Node_On at Position(xpos = 400, xanchor = 0, ypos = 408, yanchor = 0)
    
    if LLH_5_GWhileNode == "Off":
        show LLH_5_Green_While_Node_Off at Position(xpos = 345, xanchor = 0, ypos = 408, yanchor = 0)
    elif LLH_5_GWhileNode == "On":
        show LLH_5_Green_While_Node_On at Position(xpos = 345, xanchor = 0, ypos = 408, yanchor = 0)
        
    if LLH_5_BWhileNode == "Off":
        show LLH_5_Blue_While_Node_Off at Position(xpos = 620, xanchor = 0, ypos = 367, yanchor = 0)
    elif LLH_5_BWhileNode == "On":
        show LLH_5_Blue_While_Node_On at Position(xpos = 620, xanchor = 0, ypos = 367, yanchor = 0)
        
    if LLH_5_RWhileNode2 == "Off":
        show LLH_5_Red_While_Node2_Off at Position(xpos = 670, xanchor = 0, ypos = 447, yanchor = 0)
    elif LLH_5_RWhileNode2 == "On":
        show LLH_5_Red_While_Node2_On at Position(xpos = 670, xanchor = 0, ypos = 447, yanchor = 0)
    
    if LLH_5_GWhileNode2 == "Off":
        show LLH_5_Green_While_Node2_Off at Position(xpos = 670, xanchor = 0, ypos = 367, yanchor = 0)
    elif LLH_5_GWhileNode2 == "On":
        show LLH_5_Green_While_Node2_On at Position(xpos = 670, xanchor = 0, ypos = 367, yanchor = 0)
        
    if LLH_5_BWhileNode2 == "Off":
        show LLH_5_Blue_While_Node2_Off at Position(xpos = 620, xanchor = 0, ypos = 447, yanchor = 0)
    elif LLH_5_BWhileNode2 == "On":
        show LLH_5_Blue_While_Node2_On at Position(xpos = 620, xanchor = 0, ypos = 447, yanchor = 0)
    
    ######SOUND NOISES#####################################
    if (whileBRin2 or whileBGin2):
        if charge1_sound1 ==0:
            play soundP08 llCharge
            $charge1_sound1 +=1
    if (not(whileGRin2 or whileBRin2 or whileBGin2)):
        if charge1_sound1 ==1:
            $charge1_sound1 -=1
            
    if (whileGRin3 or whileBRin3):
        if charge2_sound1 ==0:
            play soundP09 llCharge
            $charge2_sound1 +=1
    if (not(whileGRin3 or whileBRin3 or whileBGin3)):
        if charge2_sound1 ==1:
            $charge2_sound1 -=1
    
    if (whileGRin4 or whileBGin4):
        if charge3_sound1 ==0:
            play soundP10 llCharge
            $charge3_sound1 +=1
    if (not(whileGRin4 or whileBRin4 or whileBGin4)):
        if charge3_sound1 ==1:
            $charge3_sound1 -=1
            
    if (whileGRin2):
        if charge1_sound2 ==0:
            play soundP11 llCharge
            $charge1_sound2 +=1
    if (not(whileGRin2)):
        if charge1_sound2 ==1:
            $charge1_sound2 -=1
            
    if (whileBGin3):
        if charge2_sound2 ==0:
            play soundP07 llCharge
            $charge2_sound2 +=1
    if (not(whileBGin3)):
        if charge2_sound2 ==1:
            $charge2_sound2 -=1
    
    if (whileBRin4):
        if charge3_sound2 ==0:
            play soundP06 llCharge
            $charge3_sound2 +=1
    if (not(whileBRin4)):
        if charge3_sound2 ==1:
            $charge3_sound2 -=1
            
    if(whileGRin2 and ifGin1):
        if light1Sound ==0:
            $light1Sound +=1
            queue soundP01 llLightOn1
    if not(whileGRin2 and ifGin1):
        if light1Sound ==1:
            $light1Sound -=1
            queue sound llLightOff1
            
    if(ifGin8 or (whileBGin3 and whileBRin4 and (ifRBin5 and elsein8))):
        if light2Sound ==0:
            $light2Sound +=1
            queue soundP02 llLightOn1
    if (not(ifGin8 or (whileBGin3 and whileBRin4 and (ifRBin5 and elsein8)))):
        if light2Sound ==1:
            $light2Sound -=1
            queue soundP02 llLightOff1
    
    if(whileBGin3 and whileBRin4 and ifRBin5 and ifBin6):
        if light3Sound ==0:
            $light3Sound +=1
            queue soundP03 llLightOn2
    if (not(whileBGin3 and whileBRin4 and ifRBin5 and ifBin6)):
        if light3Sound ==1:
            $light3Sound -=1
            queue soundP03 llLightOff2
            
    if(whileBGin3 and whileBRin4 and ifRBin5 and ifRin7):
        if light4Sound ==0:
            $light4Sound +=1
            queue soundP04 llLightOn3
    if (not(whileBGin3 and whileBRin4 and ifRBin5 and ifRin7)):
        if light4Sound ==1:
            $light4Sound -=1
            queue soundP04 llLightOff3
    
    
#win conditions ********
    if (ifGin1 and whileGRin2 and whileBGin3 and whileBRin4 and ifRBin5 and ifBin6 and ifRin7 and elsein8):
        image LLH_5_ifR = "R_if.png"
        show LLH_5_ifR at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        image LLH_5_ifG = "G_if.png"
        show LLH_5_ifG at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        image LLH_5_ifB = "B_if.png"
        show LLH_5_ifB at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        image LLH_5_ifRB = "RB_if.png"
        show LLH_5_ifRB at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        image LLH_5_whileBG = "BG_while.png"
        show LLH_5_whileBG at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        image LLH_5_else = "G_else.png"
        show LLH_5_else at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        image LLH_5_whileGR = "GR_while.png"
        show LLH_5_whileGR at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        image LLH_5_whileBR = "BR_while.png"
        show LLH_5_whileBR at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_llHardWin
        jump llHardWin

    if attempts == 0:
        show LLH_5_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
        show LLH_5_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
        show LLH_5_ifB at Position(xpos = ifBx, xanchor = 0, ypos = ifBy, yanchor = 0)
        show LLH_5_ifRB at Position(xpos = ifRBx, xanchor = 0, ypos = ifRBy, yanchor = 0)
        show LLH_5_whileBG at Position(xpos = whileBGx, xanchor = 0, ypos = whileBGy, yanchor = 0)
        show LLH_5_else at Position(xpos = elsex, xanchor = 0, ypos = elsey, yanchor = 0)
        show LLH_5_whileGR at Position(xpos = whileGRx, xanchor = 0, ypos = whileGRy, yanchor = 0)
        show LLH_5_whileBR at Position(xpos = whileBRx, xanchor = 0, ypos = whileBRy, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            jump pg_llHardLose5
        $llHard_attempts +=1
        jump llHardLose
    
    jump gamefile_llh5

screen loopLogicHard_5Scr:
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
        action Jump("hints_llHard_5")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    text "Moves" xpos 1480 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1605 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1640 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #if gates
            drag:
                drag_name "if_B_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos ifBx ypos ifBy
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
                drag_name "if_RB_gate"
                child "RB_if.png"
                droppable False
                dragged gate_dragged
                xpos ifRBx ypos ifRBy
                
            #else gate
            drag:
                drag_name "else_gate"
                child "G_Else.png"
                droppable False
                dragged gate_dragged
                xpos elsex ypos elsey

            #while gate
            drag:
                drag_name "while_BR_gate"
                child "BR_while.png"
                droppable False
                dragged gate_dragged
                xpos whileBRx ypos whileBRy
            drag:
                drag_name "while_GR_gate"
                child "GR_while.png"
                droppable False
                dragged gate_dragged
                xpos whileGRx ypos whileGRy 
            drag:
                drag_name "while_BG_gate"
                child "BG_while.png"
                droppable False
                dragged gate_dragged
                xpos whileBGx ypos whileBGy 
              
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
            #Returns########################################
            drag:
                drag_name "B_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 500

            drag:
                drag_name "R_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1375 ypos 500

            drag:
                drag_name "G_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1655 ypos 500
            drag:
                drag_name "RB_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1425 ypos 625
            drag:
                drag_name "else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1600 ypos 625
            drag:
                drag_name "BR_while_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1655 ypos 750
            drag:
                drag_name "GR_while_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 750
            drag:
                drag_name "BG_while_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1375 ypos 750

