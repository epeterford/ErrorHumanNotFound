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

label loopLogic_hard3: #start
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg looplogic_bg
    

    #*********************************************************
    #************************* pipes *************************
    #*********************************************************     

    image LLH_3_start_top1 = "W_vertical_short.png"
    show LLH_3_start_top1 at Position(xpos = 600, xanchor = 0, ypos = 420, yanchor = 0)
    image LLH_3_start_top2 = "W_vertical_short.png"
    show LLH_3_start_top2 at Position(xpos = 635, xanchor = 0, ypos = 420, yanchor = 0)
    
    image LLH_3_start_bottom1 = "W_vertical_short.png"
    show LLH_3_start_bottom1 at Position(xpos = 588, xanchor = 0, ypos = 565, yanchor = 0)
    image LLH_3_start_bottom2 = "W_vertical.png"
    show LLH_3_start_bottom2 at Position(xpos = 615, xanchor = 0, ypos = 565, yanchor = 0)
    image LLH_3_start_bottom3 = "W_vertical.png"
    show LLH_3_start_bottom3 at Position(xpos = 643, xanchor = 0, ypos = 565, yanchor = 0)
    image LLH_3_start_bottom4 = "W_vertical_short.png"
    show LLH_3_start_bottom4 at Position(xpos = 615, xanchor = 0, ypos = 640, yanchor = 0)
    image LLH_3_start_bottom5 = "W_vertical_short.png"
    show LLH_3_start_bottom5 at Position(xpos = 643, xanchor = 0, ypos = 640, yanchor = 0)
    image LLH_3_start_bottom7 = "W_horizontal.png"
    show LLH_3_start_bottom7 at Position(xpos = 500, xanchor = 0, ypos = 637, yanchor = 0)
    image LLH_3_start_bottom8 = "W_horizontal.png"
    show LLH_3_start_bottom8 at Position(xpos = 405, xanchor = 0, ypos = 637, yanchor = 0)
    image LLH_3_start_bottom10 = "W_vertical_short.png"
    show LLH_3_start_bottom10 at Position(xpos = 366, xanchor = 0, ypos = 675, yanchor = 0)
    
    image LLH_3_start_bottom6 = "W_corner_LT.png"
    show LLH_3_start_bottom6 at Position(xpos = 566, xanchor = 0, ypos = 616, yanchor = 0)
    image LLH_3_start_bottom9 = "W_corner_RB.png"
    show LLH_3_start_bottom9 at Position(xpos = 340, xanchor = 0, ypos = 611, yanchor = 0)
    
    image LLH_3_start_bottom11 = "W_horizontal.png"
    show LLH_3_start_bottom11 at Position(xpos = 255, xanchor = 0, ypos = 760, yanchor = 0)
    
    image LLH_3_start_right_top1 = "R_horizontal_ll.png"
    show LLH_3_start_right_top1 at Position(xpos = 680, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_3_start_right_mid1 = "G_horizontal_ll.png"
    show LLH_3_start_right_mid1 at Position(xpos = 680, xanchor = 0, ypos = 505, yanchor = 0)
    image LLH_3_start_right_bottom1 = "B_horizontal.png"
    show LLH_3_start_right_bottom1 at Position(xpos = 680, xanchor = 0, ypos = 540, yanchor = 0)
    image LLH_3_start_right_top2 = "W_horizontal.png"
    show LLH_3_start_right_top2 at Position(xpos = 754, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_3_start_right_mid2 = "G_horizontal_ll.png"
    show LLH_3_start_right_mid2 at Position(xpos = 754, xanchor = 0, ypos = 505, yanchor = 0)
    image LLH_3_start_right_bottom2 = "W_horizontal.png"
    show LLH_3_start_right_bottom2 at Position(xpos = 754, xanchor = 0, ypos = 540, yanchor = 0)
    image LLH_3_start_right_top3 = "W_horizontal.png"
    show LLH_3_start_right_top3 at Position(xpos = 850, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_3_start_right_mid3 = "W_horizontal.png"
    show LLH_3_start_right_mid3 at Position(xpos = 850, xanchor = 0, ypos = 505, yanchor = 0)
    image LLH_3_start_right_bottom3 = "W_horizontal.png"
    show LLH_3_start_right_bottom3 at Position(xpos = 850, xanchor = 0, ypos = 540, yanchor = 0)
    
    image LLH_3_rightifBGPipe1 = "W_vertical.png"
    show LLH_3_rightifBGPipe1 at Position(xpos = 823, xanchor = 0, ypos = 405, yanchor = 0)
    image LLH_3_rightifBGPipe3 = "W_horizontal.png"
    show LLH_3_rightifBGPipe3 at Position(xpos = 860, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_3_rightifBGPipe2 = "W_corner_RB.png"
    show LLH_3_rightifBGPipe2 at Position(xpos = 797, xanchor = 0, ypos = 344, yanchor = 0)
    
    image LLH_3_BlueEndPipe1 = "W_horizontal_short.png"
    show LLH_3_BlueEndPipe1 at Position(xpos = 1010, xanchor = 0, ypos = 515, yanchor = 0)

    image LLH_3_greenEndPipe = "W_vertical.png"
    show LLH_3_greenEndPipe at Position(xpos = 971, xanchor = 0, ypos = 265, yanchor = 0)
    
    image LLH_3_redEnd2Pipe = "W_vertical.png"
    show LLH_3_redEnd2Pipe at Position(xpos = 956, xanchor = 0, ypos = 565, yanchor = 0)
    
    image LLH_3_start_left_top1 = "R_horizontal_ll.png"
    show LLH_3_start_left_top1 at Position(xpos = 510, xanchor = 0, ypos = 485, yanchor = 0)
    image LLH_3_start_left_mid1 = "G_horizontal_ll.png"
    show LLH_3_start_left_mid1 at Position(xpos = 510, xanchor = 0, ypos = 515, yanchor = 0)
    image LLH_3_start_left_bottom1 = "B_horizontal.png"
    show LLH_3_start_left_bottom1 at Position(xpos = 510, xanchor = 0, ypos = 545, yanchor = 0)
    image LLH_3_start_left_top2 = "W_horizontal.png"
    show LLH_3_start_left_top2 at Position(xpos = 435, xanchor = 0, ypos = 485, yanchor = 0)
    image LLH_3_start_left_mid2 = "G_horizontal_ll.png"
    show LLH_3_start_left_mid2 at Position(xpos = 435, xanchor = 0, ypos = 515, yanchor = 0)
    image LLH_3_start_left_bottom2 = "B_horizontal.png"
    show LLH_3_start_left_bottom2 at Position(xpos = 435, xanchor = 0, ypos = 545, yanchor = 0)
    image LLH_3_start_left_top3 = "W_horizontal_short.png"
    show LLH_3_start_left_top3 at Position(xpos = 385, xanchor = 0, ypos = 485, yanchor = 0)
    image LLH_3_start_left_mid3 = "G_horizontal_short.png"
    show LLH_3_start_left_mid3 at Position(xpos = 385, xanchor = 0, ypos = 515, yanchor = 0)
    image LLH_3_start_left_bottom3 = "B_horizontal_short.png"
    show LLH_3_start_left_bottom3 at Position(xpos = 385, xanchor = 0, ypos = 545, yanchor = 0)
    image LLH_3_start_left_top4 = "W_horizontal_short.png"
    show LLH_3_start_left_top4 at Position(xpos = 315, xanchor = 0, ypos = 485, yanchor = 0)
    image LLH_3_start_left_mid4 = "W_horizontal_short.png"
    show LLH_3_start_left_mid4 at Position(xpos = 315, xanchor = 0, ypos = 515, yanchor = 0)
    image LLH_3_start_left_bottom4 = "W_horizontal_short.png"
    show LLH_3_start_left_bottom4 at Position(xpos = 315, xanchor = 0, ypos = 545, yanchor = 0)
    
    image LLH_3_greenEnd2Pipe = "W_horizontal_short.png"
    show LLH_3_greenEnd2Pipe at Position(xpos = 195, xanchor = 0, ypos = 515, yanchor = 0)
    
    image LLH_3_ifRBLeftPipe1 = "W_vertical.png"
    show LLH_3_ifRBLeftPipe1 at Position(xpos = 358, xanchor = 0, ypos = 410, yanchor = 0)

    image LLH_3_redEnd3Pipe = "W_vertical.png"
    show LLH_3_redEnd3Pipe at Position(xpos = 237, xanchor = 0, ypos = 405, yanchor = 0)
    
    image LLH_3_blueEnd2Pipe = "W_vertical_short.png"
    show LLH_3_blueEnd2Pipe at Position(xpos = 352, xanchor = 0, ypos = 280, yanchor = 0)

    image LLH_3_WhileLine1 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine1 at Position(xpos = 531, xanchor = 0, ypos = 755, yanchor = 0)
    image LLH_3_WhileLine2 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine2 at Position(xpos = 481, xanchor = 0, ypos = 755, yanchor = 0)
    image LLH_3_WhileLine3 = "y_vertical_short_off.png"
    show LLH_3_WhileLine3 at Position(xpos = 477, xanchor = 0, ypos = 663, yanchor = 0)
    image LLH_3_WhileLine4 = "y_vertical_short_off.png"
    show LLH_3_WhileLine4 at Position(xpos = 477, xanchor = 0, ypos = 713, yanchor = 0)
    
    image LLH_3_WhileLine14 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine14 at Position(xpos = 535, xanchor = 0, ypos = 350, yanchor = 0)
    image LLH_3_WhileLine15 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine15 at Position(xpos = 485, xanchor = 0, ypos = 350, yanchor = 0)
    image LLH_3_WhileLine16 = "y_vertical_short_off.png"
    show LLH_3_WhileLine16 at Position(xpos = 481, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_3_WhileLine17 = "y_vertical_short_off.png"
    show LLH_3_WhileLine17 at Position(xpos = 481, xanchor = 0, ypos = 430, yanchor = 0)
    
    image LLH_3_WhileLine5 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine5 at Position(xpos = 675, xanchor = 0, ypos = 720, yanchor = 0)
    image LLH_3_WhileLine6 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine6 at Position(xpos = 720, xanchor = 0, ypos = 720, yanchor = 0)
    image LLH_3_WhileLine7 = "y_vertical_short_off.png"
    show LLH_3_WhileLine7 at Position(xpos = 748, xanchor = 0, ypos = 675, yanchor = 0)
    image LLH_3_WhileLine8 = "y_vertical_short_off.png"
    show LLH_3_WhileLine8 at Position(xpos = 748, xanchor = 0, ypos = 625, yanchor = 0)
    image LLH_3_WhileLine9 = "y_vertical_short_off.png"
    show LLH_3_WhileLine9 at Position(xpos = 748, xanchor = 0, ypos = 575, yanchor = 0)
    
    image LLH_3_WhileLine10 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine10 at Position(xpos = 675, xanchor = 0, ypos = 340, yanchor = 0)
    image LLH_3_WhileLine11 = "y_horizontal_short_off.png"
    show LLH_3_WhileLine11 at Position(xpos = 720, xanchor = 0, ypos = 340, yanchor = 0)
    image LLH_3_WhileLine12 = "y_vertical_short_off.png"
    show LLH_3_WhileLine12 at Position(xpos = 748, xanchor = 0, ypos = 360, yanchor = 0)
    image LLH_3_WhileLine13 = "y_vertical_short_off.png"
    show LLH_3_WhileLine13 at Position(xpos = 748, xanchor = 0, ypos = 410, yanchor = 0)
    

    
    
    #*********************************************************
    #********************* start points **********************
    #*********************************************************
    image start = "Start.png"
    show start at Position(xpos = 580, xanchor = 0, ypos = 470, yanchor = 0)
    
    #*********************************************************
    #************************* gates *************************
    #*********************************************************
    
    image LLH_3_Opengate1 = "blank_node.png"
    show LLH_3_Opengate1 at Position (xpos = 580, xanchor = 0, ypos = 320, yanchor = 0)
    image LLH_3_Opengate2 = "blank_node.png"
    show LLH_3_Opengate2 at Position (xpos = 580, xanchor = 0, ypos = 692, yanchor = 0)
    image LLH_3_Opengate3 = "blank_node.png"
    show LLH_3_Opengate3 at Position (xpos = 330, xanchor = 0, ypos = 725, yanchor = 0)
    image LLH_3_Opengate4 = "blank_node.png"
    show LLH_3_Opengate4 at Position (xpos = 920, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_3_Opengate5 = "blank_node.png"
    show LLH_3_Opengate5 at Position (xpos = 935, xanchor = 0, ypos = 330, yanchor = 0)
    image LLH_3_Opengate6 = "blank_node.png"
    show LLH_3_Opengate6 at Position (xpos = 225, xanchor = 0, ypos = 480, yanchor = 0)
    image LLH_3_Opengate7 = "blank_node.png"
    show LLH_3_Opengate7 at Position (xpos = 315, xanchor = 0, ypos = 310, yanchor = 0)

    
    #*********************************************************
    #********************** end points ***********************
    #*********************************************************    
    image LLH_3_RedEnd1 = "R_end_off.png"
    show LLH_3_RedEnd1 at Position(xpos = 155, xanchor = 0, ypos = 725, yanchor = 0)
    image LLH_3_RedEnd2 = "R_end_off.png"
    show LLH_3_RedEnd2 at Position(xpos = 935, xanchor = 0, ypos = 170, yanchor = 0)
    image LLH_3_RedEnd3 = "R_end_off.png"
    show LLH_3_RedEnd3 at Position(xpos = 200, xanchor = 0, ypos = 310, yanchor = 0)
    image LLH_3_GreenEnd = "G_end_off.png"
    show LLH_3_GreenEnd at Position(xpos = 920, xanchor = 0, ypos = 630, yanchor = 0)
    image LLH_3_GreenEnd2 = "G_end_off.png"
    show LLH_3_GreenEnd2 at Position(xpos = 315, xanchor = 0, ypos = 180, yanchor = 0)
    image LLH_3_BlueEnd1 = "B_end_off.png"
    show LLH_3_BlueEnd1 at Position(xpos = 1050, xanchor = 0, ypos = 480, yanchor = 0)
    image LLH_3_BlueEnd2 = "B_end_off.png"
    show LLH_3_BlueEnd2 at Position(xpos = 95, xanchor = 0, ypos = 480, yanchor = 0) 

    
    #*********************************************************
    #********************** conectors ************************
    #*********************************************************    
    
    image LLH_3_start_connector_bottom_left = "B_While_off.png"
    show LLH_3_start_connector_bottom_left at Position(xpos = 475, xanchor = 0, ypos = 635, yanchor = 0)
    image LLH_3_start_connector_right_top_while = "G_While_off.png"
    show LLH_3_start_connector_right_top_while at Position(xpos = 745, xanchor = 0, ypos = 468, yanchor = 0)
    image LLH_3_start_connector_right_bottom_while = "G_While_off.png"
    show LLH_3_start_connector_right_bottom_while at Position(xpos = 745, xanchor = 0, ypos = 539, yanchor = 0)
    image LLH_3_start_connector_left_top_while = "R_While_off.png"
    show LLH_3_start_connector_left_top_while at Position(xpos = 480, xanchor = 0, ypos = 483, yanchor = 0)
    
    image LLH_3_Connect_Pipe1 = "W_connect_pipe_vertical.png"
    show LLH_3_Connect_Pipe1 at Position(xpos = 831, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_3_Connect_Pipe2 = "W_connect_pipe_vertical.png"
    show LLH_3_Connect_Pipe2 at Position(xpos = 831, xanchor = 0, ypos = 505, yanchor = 0)
    
    image LLH_3_connector1 = "W_connect_node.png"
    show LLH_3_connector1 at Position(xpos = 820, xanchor = 0, ypos = 467, yanchor = 0)
    image LLH_3_connector2 = "W_connect_node.png"
    show LLH_3_connector2 at Position(xpos = 820, xanchor = 0, ypos = 503, yanchor = 0)
    image LLH_3_connector3 = "W_connect_node.png"
    show LLH_3_connector3 at Position(xpos = 820, xanchor = 0, ypos = 539, yanchor = 0)
    image LLH_3_connector4 = "W_connect_node.png"
    image LLH_3_connector7 = "W_connect_node.png"
    show LLH_3_connector7 at Position(xpos = 355, xanchor = 0, ypos = 483, yanchor = 0)
    image LLH_3_connector8 = "W_connect_node.png"
    show LLH_3_connector8 at Position(xpos = 355, xanchor = 0, ypos = 513, yanchor = 0)
    image LLH_3_connector9 = "W_connect_node.png"
    show LLH_3_connector9 at Position(xpos = 355, xanchor = 0, ypos = 543, yanchor = 0)
    image LLH_3_connector10 = "W_connect_node.png"



#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    
    $ ifRx = 1385
    $ ifRy = 550
    
    $ ifGx = 1675
    $ ifGy = 550
    
    $ ifR2x = 1385
    $ ifR2y = 550

    $ ifRBx = 1525
    $ ifRBy = 550
    
    $ whileRGx = 1525
    $ whileRGy = 720
    
    $ whileBGx = 1675
    $ whileBGy = 720
    
    $ ifBGx = 1385
    $ ifBGy = 720

    $ gate1x = 580
    $ gate1y = 320

    $ gate2x = 580
    $ gate2y = 692

    $ gate3x = 330
    $ gate3y = 725

    $ gate4x = 920
    $ gate4y = 470
   
    $ gate5x = 935
    $ gate5y = 330

    $ gate6x = 225
    $ gate6y = 480

    $ gate7x = 315
    $ gate7y = 310
    
    image LLH_3_ifRT = "R_T_if.png"
    image LLH_3_ifGT = "G_T_if.png"
    image LLH_3_ifRBT = "RB_T_if.png"
    image LLH_3_ifBGT = "BG_T_if.png"
    image LLH_3_whileRGT = "RG_T_while.png"
    image LLH_3_whileBGT = "BG_T_while.png"
    show LLH_3_ifRT at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_3_ifGT at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_3_ifRBT at Position(xpos = ifRBx, xanchor = 0, ypos = ifRBy, yanchor = 0)
    show LLH_3_ifBGT at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
    show LLH_3_whileRGT at Position(xpos = whileRGx, xanchor = 0, ypos = whileRGy, yanchor = 0)
    show LLH_3_whileBGT at Position(xpos = whileBGx, xanchor = 0, ypos = whileBGy, yanchor = 0)
    
    # check conditons for locations
    $ ifRBin1 = False
    $ ifRBin2 = False
    $ ifRBin3 = False
    $ ifRBin4 = False
    $ ifRBin5 = False
    $ ifRBin6 = False
    $ ifRBin7 = False


    $ ifBGin1 = False
    $ ifBGin2 = False
    $ ifBGin3 = False
    $ ifBGin4 = False
    $ ifBGin5 = False
    $ ifBGin6 = False
    $ ifBGin7 = False
    
    $ whileRGin1 = False
    $ whileRGin2 = False
    $ whileRGin3 = False
    $ whileRGin4 = False
    $ whileRGin5 = False
    $ whileRGin6 = False
    $ whileRGin7 = False
    
    $ ifRin1 = False
    $ ifRin2 = False
    $ ifRin3 = False
    $ ifRin4 = False
    $ ifRin5 = False
    $ ifRin6 = False
    $ ifRin7 = False
    
    $ ifGin1 = False
    $ ifGin2 = False
    $ ifGin3 = False
    $ ifGin4 = False
    $ ifGin5 = False
    $ ifGin6 = False
    $ ifGin7 = False
    
    $ ifBin1 = False
    $ ifBin2 = False
    $ ifBin3 = False
    $ ifBin4 = False
    $ ifBin5 = False
    $ ifBin6 = False
    $ ifBin7 = False
    
    $ ifR2in1 = False
    $ ifR2in2 = False
    $ ifR2in3 = False
    $ ifR2in4 = False
    $ ifR2in5 = False
    $ ifR2in6 = False
    $ ifR2in7 = False
    
    $ whileBGin1 = False
    $ whileBGin2 = False
    $ whileBGin3 = False
    $ whileBGin4 = False
    $ whileBGin5 = False
    $ whileBGin6 = False
    $ whileBGin7 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
     
    #attempts for players
    $ attempts = 10
    
    # Color of each connect node
    $LLH_3_node1 = "None"
    $LLH_3_node2 = "None"
    $LLH_3_node3 = "None"
    $LLH_3_node4 = "None"
    $LLH_3_node5 = "None"
    $LLH_3_node6 = "None"
 
    jump gamefile_llh3
    
    
label gamefile_llh3:
    
    #calls game screen
    call screen loopLogicHard_3Scr

#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "if_R_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifGin1 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin1 = False
            if ifR2in1 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in1 = False
            if whileBGin1 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin1 = False
            if whileRGin1 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin1 = False

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
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifGin2 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin2 = False
            if ifR2in2 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in2 = False
            if whileBGin2 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin2 = False
            if whileRGin2 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin2 = False

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
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifGin3 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin3 = False
            if ifR2in3 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in3 = False
            if whileBGin3 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin3 = False
            if whileRGin3 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin3 = False

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

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifGin4 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin4 = False
            if ifR2in4 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in4 = False
            if whileBGin4 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin4 = False
            if ifRBin4 == True:
                $ ifRBx= 1425
                $ ifRBy = 550
                $ ifRBin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin4 = False
            if whileRGin4 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin4 = False

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
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifGin5 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin5 = False
            if ifR2in5 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in5 = False
            if whileBGin5 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin5 = False
            if whileRGin5 == True:
                $ whileRGx = 1385
                $ whileRGy = 720
                $ whileRGin5 = False

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
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifGin6 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin6 = False
            if ifR2in6 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in6 = False
            if whileBGin6 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin6 = False
            if whileRGin6 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin6 = False

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
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifGin7 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin7 = False
            if ifR2in7 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in7 = False
            if whileBGin7 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin7 = False
            if whileRGin7 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin7 = False

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
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1425
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ ifRx = gate7x
#            $ ifRy = gate7y
#            $ ifRin1 = False
#            $ ifRin2 = False
#            $ ifRin3 = False
#            $ ifRin4 = False
#            $ ifRin5 = False
#            $ ifRin6 = False
#            $ ifRin7 = False
#            $ ifRin7 = True
      
      
    #the second logic gate *******************************************************************************
    if gate_name == "if_G_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin1 = False
            if ifBin1 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin1 = False
            if ifR2in1 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in1 = False
            if whileBGin1 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin1 = False
            if whileRGin1 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin1 = False

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
 
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin2 = False
            if ifBin2 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin2 = False
            if ifR2in2 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in2 = False
            if whileBGin2 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin2 = False
            if whileRGin2 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin2 = False

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
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin3 = False
            if ifBin3 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin3 = False
            if ifR2in3 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in3 = False
            if whileBGin3 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin3 = False
            if whileRGin3 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin3 = False

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
            $ ifGin7 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin4 = False
            if ifBin4 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin4 = False
            if ifR2in4 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in4 = False
            if whileBGin4 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin4 = False
            if whileRGin4 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin4 = False

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
            $ ifGin7 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin5 = False
            if ifBin5 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin5 = False
            if ifR2in5 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in5 = False
            if whileBGin5 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin5 = False
            if whileRGin5 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin5 = False

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
            $ ifGin7 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin6 = False
            if ifBin6 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin6 = False
            if ifR2in6 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in6 = False
            if whileBGin6 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1435
                $ ifRBy = 550
                $ ifRBin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin6 = False
            if whileRGin6 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin6 = False

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
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin7 = False
            if ifBin7 == True:
                $ ifBx = 1525
                $ ifBy = 500
                $ ifBin7 = False
            if ifR2in7 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in7 = False
            if whileBGin7 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin7 = False
            if whileRGin7 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin7 = False

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
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ ifGx = gate7x
#            $ ifGy = gate7y
#            $ ifGin1 = False
#            $ ifGin2 = False
#            $ ifGin3 = False
#            $ ifGin4 = False
#            $ ifGin5 = False
#            $ ifGin6 = False
#            $ ifGin7 = False
#            $ ifGin7 = True
            
            
    #the third logic gate *******************************************************************************
#    if gate_name == "if_B_gate":
#        #gate slot numeber one *******************************
#        if slot_name == "gate slot one":
#            if ifRin1 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin1 = False
#            if ifGin1 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin1 = False
#            if ifR2in1 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in1 = False
#            if whileBGin1 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin1 = False
#            if ifRBin1 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin1 = False
#            if ifBGin1 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin1 = False
#            if whileRGin1 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin1 = False

#            #sets values for checks
#            $ ifBx = gate1x
#            $ ifBy = gate1y
#            $ ifBin1 = True
#            $ ifBin2 = False
#            $ ifBin3 = False
#            $ ifBin4 = False
#            $ ifBin5 = False
#            $ ifBin6 = False
#            $ ifBin7 = False
            
#        #gate slot numeber two *******************************
#        if slot_name == "gate slot two":
#            if ifRin2 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin2 = False
#            if ifGin2 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin2 = False
#            if ifR2in2 == True:
#                $ ifR2x = 1425
#                $ ifR2y = 550
#                $ ifR2in2 = False
#            if whileBGin2 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin2 = False
#            if ifRBin2 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin2 = False
#            if ifBGin2 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin2 = False
#            if whileRGin2 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin2 = False

#            #sets values for checks
#            $ ifBx = gate2x
#            $ ifBy = gate2y
#            $ ifBin1 = False
#            $ ifBin2 = True
#            $ ifBin3 = False
#            $ ifBin4 = False
#            $ ifBin5 = False
#            $ ifBin6 = False
#            $ ifBin7 = False
            
#        #gate slot numeber three *******************************
#        if slot_name == "gate slot three":
#            if ifRin3 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin3 = False
#            if ifGin3 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin3 = False
#            if ifR2in3 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in3 = False
#            if whileBGin3 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin3 = False
#            if ifRBin3 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin3 = False
#            if ifBGin3 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin3 = False
#            if whileRGin3 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin3 = False

#            #sets values for checks
#            $ ifBx = gate3x
#            $ ifBy = gate3y
#            $ ifBin1 = False
#            $ ifBin2 = False
#            $ ifBin3 = True
#            $ ifBin4 = False
#            $ ifBin5 = False
#            $ ifBin6 = False
#            $ ifBin7 = False

#        #gate slot numeber four *******************************
#        if slot_name == "gate slot four":
#            if ifRin4 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin4 = False
#            if ifGin4 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin4 = False
#            if ifR2in4 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in4 = False
#            if whileBGin4 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin4 = False
#            if ifRBin4 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin4 = False
#            if ifBGin4 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin4 = False
#            if whileRGin4 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin4 = False

#            #sets values for checks
#            $ ifBx = gate4x
#            $ ifBy = gate4y
#            $ ifBin1 = False
#            $ ifBin2 = False
#            $ ifBin3 = False
#            $ ifBin4 = True
#            $ ifBin5 = False
#            $ ifBin6 = False
#            $ ifBin7 = False
            
#        #gate slot numeber five *******************************
#        if slot_name == "gate slot five":
#            if ifRin5 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin5 = False
#            if ifGin5 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin5 = False
#            if ifR2in5 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in5 = False
#            if whileBGin5 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin5 = False
#            if ifRBin5 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin5 = False
#            if ifBGin5 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin5 = False
#            if whileRGin5 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin5 = False

#            #sets values for checks
#            $ ifBx = gate5x
#            $ ifBy = gate5y
#            $ ifBin1 = False
#            $ ifBin2 = False
#            $ ifBin3 = False
#            $ ifBin4 = False
#            $ ifBin5 = True
#            $ ifBin6 = False
#            $ ifBin7 = False
            
#        #gate slot numeber six *******************************
#        if slot_name == "gate slot six":
#            if ifRin6 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin6 = False
#            if ifGin6 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin6 = False
#            if ifR2in6 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in6 = False
#            if whileBGin6 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin6 = False
#            if ifRBin6 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin6 = False
#            if ifBGin6 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin6 = False
#            if whileRGin6 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin6 = False

#            #sets values for checks
#            $ ifBx = gate6x
#            $ ifBy = gate6y
#            $ ifBin1 = False
#            $ ifBin2 = False
#            $ ifBin3 = False
#            $ ifBin4 = False
#            $ ifBin5 = False
#            $ ifBin6 = True
#            $ ifBin7 = False
            
#        #gate slot numeber seven *******************************
#        if slot_name == "gate slot seven":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ ifBx = gate7x
#            $ ifBy = gate7y
#            $ ifBin1 = False
#            $ ifBin2 = False
#            $ ifBin3 = False
#            $ ifBin4 = False
#            $ ifBin5 = False
#            $ ifBin6 = False
#            $ ifBin7 = True
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ ifBx = gate7x
#            $ ifBy = gate7y
#            $ ifBin1 = False
#            $ ifBin2 = False
#            $ ifBin3 = False
#            $ ifBin4 = False
#            $ ifBin5 = False
#            $ ifBin6 = False
#            $ ifBin7 = False
#            $ ifBin7 = True


    #the third logic gate *******************************************************************************
    if gate_name == "if_R2_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin1 = False
#            if ifBin1 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin1 = False
            if whileBGin1 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin1 = False
            if whileRGin1 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin1 = False

            #sets values for checks
            $ ifR2x = gate1x
            $ ifR2y = gate1y
            $ ifR2in1 = True
            $ ifR2in2 = False
            $ ifR2in3 = False
            $ ifR2in4 = False
            $ ifR2in5 = False
            $ ifR2in6 = False
            $ ifR2in7 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin2 = False
#            if ifBin2 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin2 = False
            if whileBGin2 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin2 = False
            if whileRGin2 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin2 = False

            #sets values for checks
            $ ifR2x = gate2x
            $ ifR2y = gate2y
            $ ifR2in1 = False
            $ ifR2in2 = True
            $ ifR2in3 = False
            $ ifR2in4 = False
            $ ifR2in5 = False
            $ ifR2in6 = False
            $ ifR2in7 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin3 = False
#            if ifBin3 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin3 = False
            if whileBGin3 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin3 = False
            if whileRGin3 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin3 = False

            #sets values for checks
            $ ifR2x = gate3x
            $ ifR2y = gate3y
            $ ifR2in1 = False
            $ ifR2in2 = False
            $ ifR2in3 = True
            $ ifR2in4 = False
            $ ifR2in5 = False
            $ ifR2in6 = False
            $ ifR2in7 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin4 = False
#            if ifBin4 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin4 = False
            if whileBGin4 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin4 = False
            if whileRGin4 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin4 = False

            #sets values for checks
            $ ifR2x = gate4x
            $ ifR2y = gate4y
            $ ifR2in1 = False
            $ ifR2in2 = False
            $ ifR2in3 = False
            $ ifR2in4 = True
            $ ifR2in5 = False
            $ ifR2in6 = False
            $ ifR2in7 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin5 = False
#            if ifBin5 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin5 = False
            if whileBGin5 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin5 = False
            if whileRGin5 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin5 = False

            #sets values for checks
            $ ifR2x = gate5x
            $ ifR2y = gate5y
            $ ifR2in1 = False
            $ ifR2in2 = False
            $ ifR2in3 = False
            $ ifR2in4 = False
            $ ifR2in5 = True
            $ ifR2in6 = False
            $ ifR2in7 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin6 = False
#            if ifBin6 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin6 = False
            if whileBGin6 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin6 = False
            if whileRGin6 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin6 = False

            #sets values for checks
            $ ifR2x = gate6x
            $ ifR2y = gate6y
            $ ifR2in1 = False
            $ ifR2in2 = False
            $ ifR2in3 = False
            $ ifR2in4 = False
            $ ifR2in5 = False
            $ ifR2in6 = True
            $ ifR2in7 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
            if whileBGin7 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin7 = False
            if whileRGin7 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin7 = False

            #sets values for checks
            $ ifR2x = gate7x
            $ ifR2y = gate7y
            $ ifR2in1 = False
            $ ifR2in2 = False
            $ ifR2in3 = False
            $ ifR2in4 = False
            $ ifR2in5 = False
            $ ifR2in6 = False
            $ ifR2in7 = True
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ ifR2x = gate7x
#            $ ifR2y = gate7y
#            $ ifR2in1 = False
#            $ ifR2in2 = False
#            $ ifR2in3 = False
#            $ ifR2in4 = False
#            $ ifR2in5 = False
#            $ ifR2in6 = False
#            $ ifR2in7 = False
#            $ ifR2in7 = True
            
            
    #the fourth logic gate *******************************************************************************
    if gate_name == "while_BG_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin1 = False
#            if ifBin1 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin1 = False
            if ifR2in1 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in1 = False
            if ifRBin1 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin1 = False
            if whileRGin1 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin1 = False

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
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin2 = False
#            if ifBin2 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin2 = False
            if ifR2in2 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in2 = False
            if ifRBin2 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin2 = False
            if whileRGin2 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin2 = False

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
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin3 = False
#            if ifBin3 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin3 = False
            if ifR2in3 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in3 = False
            if ifRBin3 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin3 = False
            if whileRGin3 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin3 = False

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

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin4 = False
#            if ifBin4 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin4 = False
            if ifR2in4 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in4 = False
            if ifRBin4 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin4 = False
            if whileRGin4 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin4 = False

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
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin5 = False
#            if ifBin5 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin5 = False
            if ifR2in5 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in5 = False
            if ifRBin5 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin5 = False
            if whileRGin5 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin5 = False

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
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin6 = False
#            if ifBin6 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin6 = False
            if ifR2in6 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in6 = False
            if ifRBin6 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin6 = False
            if whileRGin6 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin6 = False

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
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
            if ifR2in7 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in7 = False
            if ifRBin7 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin7 = False
            if whileRGin7 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin7 = False

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
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ whileBGx = gate7x
#            $ whileBGy = gate7y
#            $ whileBGin1 = False
#            $ whileBGin2 = False
#            $ whileBGin3 = False
#            $ whileBGin4 = False
#            $ whileBGin5 = False
#            $ whileBGin6 = False
#            $ whileBGin7 = False
#            $ whileBGin7 = True
            
            
    #the fifth logic gate *******************************************************************************
    if gate_name == "if_BG_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin1 = False
#            if ifBin1 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin1 = False
            if ifR2in1 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in1 = False
            if whileBGin1 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin1 = False
            if whileRGin1 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin1 = False

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
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin2 = False
#            if ifBin2 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin2 = False
            if ifR2in2 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in2 = False
            if whileBGin2 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin2 = False
            if whileRGin2 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin2 = False

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
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin3 = False
#            if ifBin3 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin3 = False
            if ifR2in3 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in3 = False
            if whileBGin3 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin3 = False
            if whileRGin3 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin3 = False

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

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin4 = False
#            if ifBin4 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin4 = False
            if ifR2in4 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in4 = False
            if whileBGin4 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin4 = False
            if whileRGin4 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin4 = False

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
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin5 = False
#            if ifBin5 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin5 = False
            if ifR2in5 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in5 = False
            if whileBGin5 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin5 = False
            if whileRGin5 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin5 = False

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
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin6 = False
#            if ifBin6 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin6 = False
            if ifR2in6 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in6 = False
            if whileBGin6 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin6 = False
            if whileRGin6 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin6 = False

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
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
            if ifR2in7 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in7 = False
            if whileBGin7 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin7 = False
            if whileRGin7 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin7 = False

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
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if whileRGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False

#            #sets values for checks
#            $ ifBGx = gate7x
#            $ ifBGy = gate7y
#            $ ifBGin1 = False
#            $ ifBGin2 = False
#            $ ifBGin3 = False
#            $ ifBGin4 = False
#            $ ifBGin5 = False
#            $ ifBGin6 = False
#            $ ifBGin7 = False
#            $ ifBGin7 = True


    #the sixth logic gate *******************************************************************************
    if gate_name == "while_RG_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin1 = False
#            if ifBin1 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin1 = False
            if ifR2in1 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in1 = False
            if whileBGin1 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin1 = False
            if ifRBin1 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin1 = False

            #sets values for checks
            $ whileRGx = gate1x
            $ whileRGy = gate1y
            $ whileRGin1 = True
            $ whileRGin2 = False
            $ whileRGin3 = False
            $ whileRGin4 = False
            $ whileRGin5 = False
            $ whileRGin6 = False
            $ whileRGin7 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin2 = False
#            if ifBin2 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
                $ ifBin2 = False
            if ifR2in2 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in2 = False
            if whileBGin2 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin2 = False
            if ifRBin2 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin2 = False

            #sets values for checks
            $ whileRGx = gate2x
            $ whileRGy = gate2y
            $ whileRGin1 = False
            $ whileRGin2 = True
            $ whileRGin3 = False
            $ whileRGin4 = False
            $ whileRGin5 = False
            $ whileRGin6 = False
            $ whileRGin7 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin3 = False
#            if ifBin3 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin3 = False
            if ifR2in3 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in3 = False
            if whileBGin3 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin3 = False
            if ifRBin3 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin3 = False

            #sets values for checks
            $ whileRGx = gate3x
            $ whileRGy = gate3y
            $ whileRGin1 = False
            $ whileRGin2 = False
            $ whileRGin3 = True
            $ whileRGin4 = False
            $ whileRGin5 = False
            $ whileRGin6 = False
            $ whileRGin7 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin4 = False
#            if ifBin4 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin4 = False
            if ifR2in4 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in4 = False
            if whileBGin4 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin4 = False
            if ifRBin4 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin4 = False

            #sets values for checks
            $ whileRGx = gate4x
            $ whileRGy = gate4y
            $ whileRGin1 = False
            $ whileRGin2 = False
            $ whileRGin3 = False
            $ whileRGin4 = True
            $ whileRGin5 = False
            $ whileRGin6 = False
            $ whileRGin7 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin5 = False
#            if ifBin5 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin5 = False
            if ifR2in5 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in5 = False
            if whileBGin5 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin5 = False
            if ifRBin5 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin5 = False

            #sets values for checks
            $ whileRGx = gate5x
            $ whileRGy = gate5y
            $ whileRGin1 = False
            $ whileRGin2 = False
            $ whileRGin3 = False
            $ whileRGin4 = False
            $ whileRGin5 = True
            $ whileRGin6 = False
            $ whileRGin7 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin6 = False
#            if ifBin6 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin6 = False
            if ifR2in6 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in6 = False
            if whileBGin6 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin6 = False
            if ifRBin6 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin6 = False

            #sets values for checks
            $ whileRGx = gate6x
            $ whileRGy = gate6y
            $ whileRGin1 = False
            $ whileRGin2 = False
            $ whileRGin3 = False
            $ whileRGin4 = False
            $ whileRGin5 = False
            $ whileRGin6 = True
            $ whileRGin7 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
            if ifR2in7 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in7 = False
            if whileBGin7 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin7 = False
            if ifRBin7 == True:
                $ ifRBx = 1525
                $ ifRBy = 550
                $ ifRBin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin7 = False

            #sets values for checks
            $ whileRGx = gate7x
            $ whileRGy = gate7y
            $ whileRGin1 = False
            $ whileRGin2 = False
            $ whileRGin3 = False
            $ whileRGin4 = False
            $ whileRGin5 = False
            $ whileRGin6 = False
            $ whileRGin7 = True
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifRBin7 == True:
#                $ ifRBx = 1525
#                $ ifRBy = 550
#                $ ifRBin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False

#            #sets values for checks
#            $ whileRGx = gate7x
#            $ whileRGy = gate7y
#            $ whileRGin1 = False
#            $ whileRGin2 = False
#            $ whileRGin3 = False
#            $ whileRGin4 = False
#            $ whileRGin5 = False
#            $ whileRGin6 = False
#            $ whileRGin7 = False
#            $ whileRGin7 = True


    #the seventh logic gate *******************************************************************************
    if gate_name == "if_RB_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin1 = False
#            if ifBin1 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin1 = False
            if ifR2in1 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in1 = False
            if whileBGin1 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin1 = False
            if whileRGin1 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin1 = False

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
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin2 = False
#            if ifBin2 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin2 = False
            if ifR2in2 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in2 = False
            if whileBGin2 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin2 = False
            if whileRGin2 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin2 = False

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
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin3 = False
#            if ifBin3 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin3 = False
            if ifR2in3 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in3 = False
            if whileBGin3 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin3 = False
            if whileRGin3 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin3 = False

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

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin4 = False
#            if ifBin4 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin4 = False
            if ifR2in4 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in4 = False
            if whileBGin4 == True:
                $ whileBGx = 1675
                $ whileBGy = 710
                $ whileBGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin4 = False
            if whileRGin4 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin4 = False

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
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin5 = False
#            if ifBin5 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin5 = False
            if ifR2in5 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in5 = False
            if whileBGin5 == True:
                $ whileBGx = 1675
                $ whileBGy = 710
                $ whileBGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin5 = False
            if whileRGin5 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin5 = False

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
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin6 = False
#            if ifBin6 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin6 = False
            if ifR2in6 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in6 = False
            if whileBGin6 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin6 = False
            if whileRGin6 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin6 = False

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
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1385
                $ ifRy = 550
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1675
                $ ifGy = 550
                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
            if ifR2in7 == True:
                $ ifR2x = 1385
                $ ifR2y = 550
                $ ifR2in7 = False
            if whileBGin7 == True:
                $ whileBGx = 1675
                $ whileBGy = 720
                $ whileBGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1385
                $ ifBGy = 720
                $ ifBGin7 = False
            if whileRGin7 == True:
                $ whileRGx = 1525
                $ whileRGy = 720
                $ whileRGin7 = False

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
            
#        #gate slot numeber eight *******************************
#        if slot_name == "gate slot eight":
#            if ifRin7 == True:
#                $ ifRx = 1385
#                $ ifRy = 550
#                $ ifRin7 = False
#            if ifGin7 == True:
#                $ ifGx = 1675
#                $ ifGy = 550
#                $ ifGin7 = False
#            if ifBin7 == True:
#                $ ifBx = 1525
#                $ ifBy = 500
#                $ ifBin7 = False
#            if ifR2in7 == True:
#                $ ifR2x = 1385
#                $ ifR2y = 550
#                $ ifR2in7 = False
#            if whileBGin7 == True:
#                $ whileBGx = 1675
#                $ whileBGy = 720
#                $ whileBGin7 = False
#            if ifBGin7 == True:
#                $ ifBGx = 1385
#                $ ifBGy = 720
#                $ ifBGin7 = False
#            if whileRGin7 == True:
#                $ whileRGx = 1525
#                $ whileRGy = 720
#                $ whileRGin7 = False

#            #sets values for checks
#            $ ifRBx = gate7x
#            $ ifRBy = gate7y
#            $ ifRBin1 = False
#            $ ifRBin2 = False
#            $ ifRBin3 = False
#            $ ifRBin4 = False
#            $ ifRBin5 = False
#            $ ifRBin6 = False
#            $ ifRBin7 = False
#            $ ifRBin7 = True

    
    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "R_if_gate_return" or slot_name == "G_if_gate_return" or slot_name == "if_RB_gate_return" or
        slot_name == "BG_if_gate_return" or slot_name == "RG_while_return" or slot_name == "BG_while_return")):
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
                    $ ifRy = 550
                    $ ifRin1 = False
                    $ ifRin2 = False
                    $ ifRin3 = False
                    $ ifRin4 = False
                    $ ifRin5 = False
                    $ ifRin6 = False
                    $ ifRin7 = False
                if gate_name == "if_R2_gate":
                    $ ifR2x = 1385
                    $ ifR2y = 550
                    $ ifR2in1 = False
                    $ ifR2in2 = False
                    $ ifR2in3 = False
                    $ ifR2in4 = False
                    $ ifR2in5 = False
                    $ ifR2in6 = False
                    $ ifR2in7 = False
            if slot_name == "G_if_gate_return":
                $ attempts +=1
                if gate_name == "if_G_gate":
                    $ ifGx = 1675
                    $ ifGy = 550
                    $ ifGin1 = False
                    $ ifGin2 = False
                    $ ifGin3 = False
                    $ ifGin4 = False
                    $ ifGin5 = False
                    $ ifGin6 = False
                    $ ifGin7 = False

            if slot_name == "if_RB_gate_return":
                $ attempts +=1
                if gate_name == "if_RB_gate":
                    $ ifRBx = 1525
                    $ ifRBy = 550
                    $ ifRBin1 = False
                    $ ifRBin2 = False
                    $ ifRBin3 = False
                    $ ifRBin4 = False
                    $ ifRBin5 = False
                    $ ifRBin6 = False
                    $ ifRBin7 = False

            if slot_name == "BG_if_gate_return":
                $ attempts +=1
                if gate_name == "if_BG_gate":
                    $ ifBGx = 1385
                    $ ifBGy = 720
                    $ ifBGin1 = False
                    $ ifBGin2 = False
                    $ ifBGin3 = False
                    $ ifBGin4 = False
                    $ ifBGin5 = False
                    $ ifBGin6 = False
                    $ ifBGin7 = False
            if slot_name == "RG_while_return":
                $ attempts +=1
                if gate_name == "while_RG_gate":
                    $ whileRGx = 1525
                    $ whileRGy = 720
                    $ whileRGin1 = False
                    $ whileRGin2 = False
                    $ whileRGin3 = False
                    $ whileRGin4 = False
                    $ whileRGin5 = False
                    $ whileRGin6 = False
                    $ whileRGin7 = False
            if slot_name == "BG_while_return":
                $ attempts +=1
                if gate_name == "while_BG_gate":
                    $ whileBGx = 1675
                    $ whileBGy = 720
                    $ whileBGin1 = False
                    $ whileBGin2 = False
                    $ whileBGin3 = False
                    $ whileBGin4 = False
                    $ whileBGin5 = False
                    $ whileBGin6 = False
                    $ whileBGin7 = False



#*******************************************
#************image zone********************* 
#*******************************************
    $LLH_3_node1 = "None"
    $LLH_3_node2 = "None"
    $LLH_3_node3 = "None"
    $LLH_3_node4 = "None"
    $LLH_3_node5 = "None"
    $LLH_3_node6 = "None"
    $LLH_3_node7 = "None"
    $LLH_3_node8 = "None"
    $LLH_3_node9 = "None"
    $LLH_3_node10 = "None"
    $LLH_3_node11 = "None"
    $LLH_3_node12 = "None"
    
    $LLH_3_BEnd1 = "Off"
    $LLH_3_BEnd2 = "Off"
    $LLH_3_GEnd1 = "Off"
    $LLH_3_GEnd2 = "Off"
    $LLH_3_REnd1 = "Off"
    $LLH_3_REnd2 = "Off"
    $LLH_3_REnd3 = "Off"
    
    $LLH_3_RWhileNode = "Off"
    $LLH_3_BWhileNode = "Off"
    $LLH_3_GWhileNode = "Off"
    $LLH_3_GWhileNode2 = "Off"


# ifBG in gate 1 cases **************************************************************************            
   
    if whileRGin1 == True:
        image LLH_3_color_pipe1 = "R_vertical_short.png"
        show LLH_3_color_pipe1 at Position(xpos = 600, xanchor = 0, ypos = 420, yanchor = 0)
        image LLH_3_color_pipe2 = "G_vertical_short.png"
        show LLH_3_color_pipe2 at Position(xpos = 633, xanchor = 0, ypos = 420, yanchor = 0)
        
        image LLH_3_OnWhileLine1 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine1 at Position(xpos = 675, xanchor = 0, ypos = 340, yanchor = 0)
        image LLH_3_OnWhileLine2 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine2 at Position(xpos = 720, xanchor = 0, ypos = 340, yanchor = 0)
        image LLH_3_OnWhileLine3 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine3 at Position(xpos = 748, xanchor = 0, ypos = 360, yanchor = 0)
        image LLH_3_OnWhileLine4 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine4 at Position(xpos = 748, xanchor = 0, ypos = 410, yanchor = 0)
        
        image LLH_3_OnWhileLine18 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine18 at Position(xpos = 535, xanchor = 0, ypos = 350, yanchor = 0)
        image LLH_3_OnWhileLine19 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine19 at Position(xpos = 485, xanchor = 0, ypos = 350, yanchor = 0)
        image LLH_3_OnWhileLine20 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine20 at Position(xpos = 481, xanchor = 0, ypos = 370, yanchor = 0)
        image LLH_3_OnWhileLine21 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine21 at Position(xpos = 481, xanchor = 0, ypos = 430, yanchor = 0)
        
        image LLH_3_color_pipe4 = "R_horizontal_ll.png"
        show LLH_3_color_pipe4 at Position(xpos = 754, xanchor = 0, ypos = 470, yanchor = 0)
        
        image LLH_3_color_pipe19 = "R_horizontal_ll.png"
        show LLH_3_color_pipe19 at Position(xpos = 435, xanchor = 0, ypos = 485, yanchor = 0)
        image LLH_3_color_pipe20 = "R_horizontal_short.png"
        show LLH_3_color_pipe20 at Position(xpos = 385, xanchor = 0, ypos = 485, yanchor = 0)
        
        $LLH_3_RWhileNode = "On"
        $LLH_3_GWhileNode = "On"
        
        hide LLH_3_color_pipe3
        hide LLH_3_color_pipe5
        hide LLH_3_color_pipe6
        hide LLH_3_color_pipe7
    elif whileRGin1 == False:
        hide LLH_3_color_pipe1
        hide LLH_3_color_pipe2
        hide LLH_3_OnWhileLine1
        hide LLH_3_OnWhileLine2
        hide LLH_3_OnWhileLine3
        hide LLH_3_OnWhileLine4
        hide LLH_3_OnWhileLine18
        hide LLH_3_OnWhileLine19
        hide LLH_3_OnWhileLine20
        hide LLH_3_OnWhileLine21
        hide LLH_3_color_pipe4
        hide LLH_3_color_pipe19
        hide LLH_3_color_pipe20
        hide LLH_3_color_pipe39
        hide LLH_3_color_pipe40
        
        if whileBGin1 == True:
            image LLH_3_color_pipe11 = "B_vertical_short.png"
            show LLH_3_color_pipe11 at Position(xpos = 600, xanchor = 0, ypos = 420, yanchor = 0)
            image LLH_3_color_pipe3 = "G_vertical_short.png"
            show LLH_3_color_pipe3 at Position(xpos = 633, xanchor = 0, ypos = 420, yanchor = 0)
            image LLH_3_OnWhileLine5 = "y_horizontal_short_on.png"
            show LLH_3_OnWhileLine5 at Position(xpos = 675, xanchor = 0, ypos = 340, yanchor = 0)
            image LLH_3_OnWhileLine6 = "y_horizontal_short_on.png"
            show LLH_3_OnWhileLine6 at Position(xpos = 720, xanchor = 0, ypos = 340, yanchor = 0)
            image LLH_3_OnWhileLine7 = "y_vertical_short_on.png"
            show LLH_3_OnWhileLine7 at Position(xpos = 748, xanchor = 0, ypos = 360, yanchor = 0)
            image LLH_3_OnWhileLine8 = "y_vertical_short_on.png"
            show LLH_3_OnWhileLine8 at Position(xpos = 748, xanchor = 0, ypos = 410, yanchor = 0)
            
            image LLH_3_color_pipe5 = "R_horizontal_ll.png"
            show LLH_3_color_pipe5 at Position(xpos = 754, xanchor = 0, ypos = 470, yanchor = 0)
            
            $LLH_3_GWhileNode = "On"
            
        elif whileBGin1 == False:
            hide LLH_3_color_pipe3
            hide LLH_3_color_pipe11
            hide LLH_3_OnWhileLine5
            hide LLH_3_OnWhileLine6
            hide LLH_3_OnWhileLine7
            hide LLH_3_OnWhileLine8
            hide LLH_3_color_pipe5
            hide LLH_3_color_pipe41
            hide LLH_3_color_pipe42
        
        if ifGin1 == True:
            image LLH_3_color_pipe6 = "G_vertical_short.png"
            show LLH_3_color_pipe6 at Position(xpos = 633, xanchor = 0, ypos = 420, yanchor = 0)
        elif ifGin1 == False:
            hide LLH_3_color_pipe6
            
        if ifRin1 or ifR2in1 == True:
            image LLH_3_color_pipe7 = "R_vertical_short.png"
            show LLH_3_color_pipe7 at Position(xpos = 598, xanchor = 0, ypos = 420, yanchor = 0)
        elif ifRin1 == False:
            hide LLH_3_color_pipe7
        elif ifR2in1 == False:
            hide LLH_3_color pipe7
            
        if ifBGin1 == True:
            image LLH_3_color_pipe9 = "B_vertical_short.png"
            show LLH_3_color_pipe9 at Position(xpos = 600, xanchor = 0, ypos = 420, yanchor = 0)
            image LLH_3_color_pipe10 = "G_vertical_short.png"
            show LLH_3_color_pipe10 at Position(xpos = 633, xanchor = 0, ypos = 420, yanchor = 0)
        elif ifBGin1 == False:
            hide LLH_3_color_pipe9
            hide LLH_3_color_pipe10
            
        if ifRBin1 == True:
            image LLH_3_color_pipe12 = "R_vertical_short.png"
            show LLH_3_color_pipe12 at Position(xpos = 600, xanchor = 0, ypos = 420, yanchor = 0)
            image LLH_3_color_pipe13 = "B_vertical_short.png"
            show LLH_3_color_pipe13 at Position(xpos = 635, xanchor = 0, ypos = 420, yanchor = 0)
        elif ifBGin1 == False:
            hide LLH_3_color_pipe12
            hide LLH_3_color_pipe13
            
    if whileBGin2 == True:
        image LLH_3_color_pipe14 = "G_vertical_ll.png"
        show LLH_3_color_pipe14 at Position(xpos = 613, xanchor = 0, ypos = 568, yanchor = 0)
        image LLH_3_color_pipe15 = "B_vertical.png"
        show LLH_3_color_pipe15 at Position(xpos = 643, xanchor = 0, ypos = 568, yanchor = 0)
        image LLH_3_color_pipe16 = "G_vertical_short.png"
        show LLH_3_color_pipe16 at Position(xpos = 613, xanchor = 0, ypos = 642, yanchor = 0)
        image LLH_3_color_pipe17 = "B_vertical_short.png"
        show LLH_3_color_pipe17 at Position(xpos = 643, xanchor = 0, ypos = 642, yanchor = 0)
        
        image LLH_3_OnWhileLine9 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine9 at Position(xpos = 531, xanchor = 0, ypos = 755, yanchor = 0)
        image LLH_3_OnWhileLine10 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine10 at Position(xpos = 481, xanchor = 0, ypos = 755, yanchor = 0)
        image LLH_3_OnWhileLine11 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine11 at Position(xpos = 477, xanchor = 0, ypos = 663, yanchor = 0)
        image LLH_3_OnWhileLine12 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine12 at Position(xpos = 477, xanchor = 0, ypos = 713, yanchor = 0)
        image LLH_3_OnWhileLine13 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine13 at Position(xpos = 675, xanchor = 0, ypos = 720, yanchor = 0)
        image LLH_3_OnWhileLine14 = "y_horizontal_short_on.png"
        show LLH_3_OnWhileLine14 at Position(xpos = 720, xanchor = 0, ypos = 720, yanchor = 0)
        image LLH_3_OnWhileLine15 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine15 at Position(xpos = 748, xanchor = 0, ypos = 675, yanchor = 0)
        image LLH_3_OnWhileLine16 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine16 at Position(xpos = 748, xanchor = 0, ypos = 625, yanchor = 0)
        image LLH_3_OnWhileLine17 = "y_vertical_short_on.png"
        show LLH_3_OnWhileLine17 at Position(xpos = 748, xanchor = 0, ypos = 575, yanchor = 0)
        
        image LLH_3_color_pipe18 = "B_horizontal.png"
        show LLH_3_color_pipe18 at Position(xpos = 754, xanchor = 0, ypos = 540, yanchor = 0)
        
        $LLH_3_BWhileNode = "On"
        $LLH_3_GWhileNode2 = "On"
        
    elif whileBGin2 == False:
        hide LLH_3_color_pipe14
        hide LLH_3_color_pipe15
        hide LLH_3_color_pipe16
        hide LLH_3_color_pipe17
        hide LLH_3_color_pipe18
        hide LLH_3_color_pipe43
        hide LLH_3_color_pipe44
        hide LLH_3_OnWhileLine9
        hide LLH_3_OnWhileLine10
        hide LLH_3_OnWhileLine11
        hide LLH_3_OnWhileLine12
        hide LLH_3_OnWhileLine13
        hide LLH_3_OnWhileLine14
        hide LLH_3_OnWhileLine15
        hide LLH_3_OnWhileLine16
        hide LLH_3_OnWhileLine17
        
        if ifBGin2 == True:
            image LLH_3_color_pipe22 = "G_vertical_ll.png"
            show LLH_3_color_pipe22 at Position(xpos = 613, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe23 = "B_vertical.png"
            show LLH_3_color_pipe23 at Position(xpos = 643, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe24 = "G_vertical_short.png"
            show LLH_3_color_pipe24 at Position(xpos = 613, xanchor = 0, ypos = 642, yanchor = 0)
            image LLH_3_color_pipe25 = "B_vertical_short.png"
            show LLH_3_color_pipe25 at Position(xpos = 643, xanchor = 0, ypos = 642, yanchor = 0)
        elif ifBGin2 == False:
            hide LLH_3_color_pipe22
            hide LLH_3_color_pipe23
            hide LLH_3_color_pipe24
            hide LLH_3_color_pipe25
            
        if ifRBin2 == True:
            image LLH_3_color_pipe26 = "R_vertical_ll.png"
            show LLH_3_color_pipe26 at Position(xpos = 615, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe27 = "B_vertical.png"
            show LLH_3_color_pipe27 at Position(xpos = 643, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe28 = "R_vertical_short.png"
            show LLH_3_color_pipe28 at Position(xpos = 615, xanchor = 0, ypos = 642, yanchor = 0)
            image LLH_3_color_pipe29 = "B_vertical_short.png"
            show LLH_3_color_pipe29 at Position(xpos = 643, xanchor = 0, ypos = 642, yanchor = 0)
        elif ifRBin2 == False:
            hide LLH_3_color_pipe26
            hide LLH_3_color_pipe27
            hide LLH_3_color_pipe28
            hide LLH_3_color_pipe29
            
        if ifRin2 or ifR2in2 == True:
            image LLH_3_color_pipe30 = "R_vertical_ll.png"
            show LLH_3_color_pipe30 at Position(xpos = 615, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe31 = "R_vertical_short.png"
            show LLH_3_color_pipe31 at Position(xpos = 615, xanchor = 0, ypos = 642, yanchor = 0)
        elif ifRin2 == False:
            hide LLH_3_color_pipe30
            hide LLH_3_color_pipe31
        elif ifR2in2 == False:
            hide LLH_3_color_pipe30
            hide LLH_3_color_pipe31
        
        if ifGin2 == True:
            image LLH_3_color_pipe32 = "G_vertical_ll.png"
            show LLH_3_color_pipe32 at Position(xpos = 613, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe33 = "G_vertical_short.png"
            show LLH_3_color_pipe33 at Position(xpos = 613, xanchor = 0, ypos = 642, yanchor = 0)
        elif ifGin2 == False:
            hide LLH_3_color_pipe32
            hide LLH_3_color_pipe33
        
        if whileRGin2 == True:
            image LLH_3_color_pipe34 = "G_vertical_ll.png"
            show LLH_3_color_pipe34 at Position(xpos = 613, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe35 = "R_vertical_ll.png"
            show LLH_3_color_pipe35 at Position(xpos = 643, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_3_color_pipe36 = "G_vertical_short.png"
            show LLH_3_color_pipe36 at Position(xpos = 613, xanchor = 0, ypos = 642, yanchor = 0)
            image LLH_3_color_pipe37 = "R_vertical_short.png"
            show LLH_3_color_pipe37 at Position(xpos = 643, xanchor = 0, ypos = 642, yanchor = 0)
            
            image LLH_3_OnWhileLine22 = "y_horizontal_short_on.png"
            show LLH_3_OnWhileLine22 at Position(xpos = 675, xanchor = 0, ypos = 720, yanchor = 0)
            image LLH_3_OnWhileLine23 = "y_horizontal_short_on.png"
            show LLH_3_OnWhileLine23 at Position(xpos = 720, xanchor = 0, ypos = 720, yanchor = 0)
            image LLH_3_OnWhileLine24 = "y_vertical_short_on.png"
            show LLH_3_OnWhileLine24 at Position(xpos = 748, xanchor = 0, ypos = 675, yanchor = 0)
            image LLH_3_OnWhileLine25 = "y_vertical_short_on.png"
            show LLH_3_OnWhileLine25 at Position(xpos = 748, xanchor = 0, ypos = 625, yanchor = 0)
            image LLH_3_OnWhileLine26 = "y_vertical_short_on.png"
            show LLH_3_OnWhileLine26 at Position(xpos = 748, xanchor = 0, ypos = 575, yanchor = 0)
            
            image LLH_3_color_pipe38 = "B_horizontal.png"
            show LLH_3_color_pipe38 at Position(xpos = 754, xanchor = 0, ypos = 540, yanchor = 0)
            
            $LLH_3_GWhileNode2 = "On"
        elif whileRGin2 == False:
            hide LLH_3_color_pipe34
            hide LLH_3_color_pipe35
            hide LLH_3_color_pipe36
            hide LLH_3_color_pipe37
            hide LLH_3_color_pipe38
            hide LLH_3_color_pipe45
            hide LLH_3_color_pipe46
            hide LLH_3_OnWhileLine22
            hide LLH_3_OnWhileLine23
            hide LLH_3_OnWhileLine24
            hide LLH_3_OnWhileLine25
            hide LLH_3_OnWhileLine26
            
    if ifRin3 == True or ifR2in3 == True:
        image LLH_3_color_pipe47 = "R_vertical_short.png"
        show LLH_3_color_pipe47 at Position(xpos = 588, xanchor = 0, ypos = 565, yanchor = 0)
        image LLH_3_color_pipe48 = "R_horizontal_ll.png"
        show LLH_3_color_pipe48 at Position(xpos = 500, xanchor = 0, ypos = 637, yanchor = 0)
        image LLH_3_color_pipe54 = "W_corner_LT.png"
        show LLH_3_color_pipe54 at Position(xpos = 566, xanchor = 0, ypos = 616, yanchor = 0)
        if whileBGin2 == True:
            image LLH_3_color_pipe49 = "R_horizontal_ll.png"
            show LLH_3_color_pipe49 at Position(xpos = 405, xanchor = 0, ypos = 637, yanchor = 0)
            image LLH_3_color_pipe50 = "R_vertical_short.png"
            show LLH_3_color_pipe50 at Position(xpos = 366, xanchor = 0, ypos = 675, yanchor = 0)
            
            image LLH_3_color_pipe51 = "W_corner_LT.png"
            show LLH_3_color_pipe51 at Position(xpos = 566, xanchor = 0, ypos = 616, yanchor = 0)
            image LLH_3_color_pipe52 = "W_corner_RB.png"
            show LLH_3_color_pipe52 at Position(xpos = 340, xanchor = 0, ypos = 611, yanchor = 0)
            
            image LLH_3_color_pipe53 = "R_horizontal_ll.png"
            show LLH_3_color_pipe53 at Position(xpos = 255, xanchor = 0, ypos = 760, yanchor = 0)
            
            $LLH_3_REnd1 = "On"
        elif whileBGin2 == False:
            hide LLH_3_color_pipe49
            hide LLH_3_color_pipe50
            hide LLH_3_color_pipe51
            hide LLH_3_color_pipe52
            hide LLH_3_color_pipe53
    elif ifRin3 == False and ifR2in3 == False:
        hide LLH_3_color_pipe47
        hide LLH_3_color_pipe48
        hide LLH_3_color_pipe54
        hide LLH_3_color_pipe49
        hide LLH_3_color_pipe50
        hide LLH_3_color_pipe51
        hide LLH_3_color_pipe52
        hide LLH_3_color_pipe53

        if ifGin3 == True:
            image LLH_3_color_pipe55 = "G_vertical_short.png"
            show LLH_3_color_pipe55 at Position(xpos = 586, xanchor = 0, ypos = 565, yanchor = 0)
            image LLH_3_color_pipe56 = "G_horizontal_ll.png"
            show LLH_3_color_pipe56 at Position(xpos = 500, xanchor = 0, ypos = 637, yanchor = 0)
            image LLH_3_color_pipe57 = "W_corner_LT.png"
            show LLH_3_color_pipe57 at Position(xpos = 566, xanchor = 0, ypos = 616, yanchor = 0)
            if whileBGin2 == True:
                image LLH_3_color_pipe58 = "G_horizontal_ll.png"
                show LLH_3_color_pipe58 at Position(xpos = 405, xanchor = 0, ypos = 637, yanchor = 0)
                image LLH_3_color_pipe59 = "G_vertical_short.png"
                show LLH_3_color_pipe59 at Position(xpos = 364, xanchor = 0, ypos = 675, yanchor = 0)
                
                image LLH_3_color_pipe60 = "W_corner_LT.png"
                show LLH_3_color_pipe60 at Position(xpos = 566, xanchor = 0, ypos = 616, yanchor = 0)
                image LLH_3_color_pipe61 = "W_corner_RB.png"
                show LLH_3_color_pipe61 at Position(xpos = 340, xanchor = 0, ypos = 611, yanchor = 0)
                
                image LLH_3_color_pipe62 = "G_horizontal_ll.png"
                show LLH_3_color_pipe62 at Position(xpos = 255, xanchor = 0, ypos = 760, yanchor = 0)
                
            elif whileBGin2 == False:
                hide LLH_3_color_pipe58
                hide LLH_3_color_pipe59
                hide LLH_3_color_pipe60
                hide LLH_3_color_pipe61
                hide LLH_3_color_pipe62
        elif ifGin3 == False:
            hide LLH_3_color_pipe55
            hide LLH_3_color_pipe56
            hide LLH_3_color_pipe57
            hide LLH_3_color_pipe58
            hide LLH_3_color_pipe59
            hide LLH_3_color_pipe60
            hide LLH_3_color_pipe61
            hide LLH_3_color_pipe62
    
    if ifBGin4 == True:
        image LLH_3_color_pipe64 = "G_horizontal_ll.png"
        show LLH_3_color_pipe64 at Position(xpos = 850, xanchor = 0, ypos = 505, yanchor = 0)
        hide LLH_3_color_pipe69
        hide LLH_3_color_pipe70
        hide LLH_3_color_pipe71
        hide LLH_3_color_pipe72
        hide LLH_3_color_pipe73
        hide LLH_3_color_pipe74
        hide LLH_3_color_pipe75
        hide LLH_3_color_pipe76
        hide LLH_3_color_pipe68
        if whileBGin2 == True or whileRGin2 == True:
            image LLH_3_color_pipe65 = "B_horizontal.png"
            show LLH_3_color_pipe65 at Position(xpos = 848, xanchor = 0, ypos = 540, yanchor = 0)
            image LLH_3_color_pipe66 = "B_horizontal_short.png"
            show LLH_3_color_pipe66 at Position(xpos = 1020, xanchor = 0, ypos = 515, yanchor = 0)
            image LLH_3_color_pipe67 = "G_vertical_ll.png"
            show LLH_3_color_pipe67 at Position(xpos = 954, xanchor = 0, ypos = 565, yanchor = 0)
            
            $LLH_3_BEnd1 = "On"
            $LLH_3_GEnd1 = "On"
        elif whileBGin2 == False and whileRGin2 == False:
            hide LLH_3_color_pipe65
            hide LLH_3_color_pipe66
            hide LLH_3_color_pipe67
    elif ifBGin4 == False:
        hide LLH_3_color_pipe64
        hide LLH_3_color_pipe65
        hide LLH_3_color_pipe66
        hide LLH_3_color_pipe67
    
    if whileBGin1 == True or whileRGin1 == True:
        if ifRin4 == True or ifR2in4 == True:
            image LLH_3_color_pipe68 = "R_horizontal_ll.png"
            show LLH_3_color_pipe68 at Position(xpos = 850, xanchor = 0, ypos = 470, yanchor = 0)
        elif ifRin4 == False and ifR2in4 == False:
            hide LLH_3_color_pipe68
    elif whileBGin1 == False and whileRGin1 == False:
        hide LLH_3_color_pipe68
            
    if ifGin4 == True:
        image LLH_3_color_pipe93 = "G_horizontal_ll.png"
        show LLH_3_color_pipe93 at Position(xpos = 850, xanchor = 0, ypos = 505, yanchor = 0)
        image LLH_3_color_pipe94 = "G_vertical_ll.png"
        show LLH_3_color_pipe94 at Position(xpos = 953, xanchor = 0, ypos = 565, yanchor = 0)
        
        $LLH_3_GEnd1 = "On"
    elif ifGin4 == False:
        hide LLH_3_color_pipe93
        hide LLH_3_color_pipe94
        
    if ifRBin4 == True:
        if whileBGin1 == True and whileRGin2 == True:
            image LLH_3_color_pipe69 = "R_horizontal_ll.png"
            show LLH_3_color_pipe69 at Position(xpos = 848, xanchor = 0, ypos = 470, yanchor = 0)
            image LLH_3_color_pipe70 = "B_horizontal.png"
            show LLH_3_color_pipe70 at Position(xpos = 848, xanchor = 0, ypos = 540, yanchor = 0)
            image LLH_3_color_pipe71 = "B_horizontal_short.png"
            show LLH_3_color_pipe71 at Position(xpos = 1020, xanchor = 0, ypos = 515, yanchor = 0)
            image LLH_3_color_pipe72 = "R_vertical_ll.png"
            show LLH_3_color_pipe72 at Position(xpos = 956, xanchor = 0, ypos = 565, yanchor = 0)
            $LLH_3_BEnd1 = "On"
        elif whileBGin1 == False or whileRGin2 == False:
            hide LLH_3_color_pipe69
            hide LLH_3_color_pipe70
            hide LLH_3_color_pipe71
            hide LLH_3_color_pipe72
        if whileBGin2 == True and whileRGin1 == True:
            image LLH_3_color_pipe73 = "R_horizontal_ll.png"
            show LLH_3_color_pipe73 at Position(xpos = 848, xanchor = 0, ypos = 470, yanchor = 0)
            image LLH_3_color_pipe74 = "B_horizontal.png"
            show LLH_3_color_pipe74 at Position(xpos = 848, xanchor = 0, ypos = 540, yanchor = 0)
            image LLH_3_color_pipe75 = "B_horizontal_short.png"
            show LLH_3_color_pipe75 at Position(xpos = 1020, xanchor = 0, ypos = 515, yanchor = 0)
            image LLH_3_color_pipe76 = "R_vertical_ll.png"
            show LLH_3_color_pipe76 at Position(xpos = 956, xanchor = 0, ypos = 565, yanchor = 0)
            $LLH_3_BEnd1 = "On"
        elif whileBGin2 == False or whileRGin1 == False:
            hide LLH_3_color_pipe73
            hide LLH_3_color_pipe74
            hide LLH_3_color_pipe75
            hide LLH_3_color_pipe76
    elif ifRBin4 == False:
        hide LLH_3_color_pipe69
        hide LLH_3_color_pipe70
        hide LLH_3_color_pipe71
        hide LLH_3_color_pipe72
        hide LLH_3_color_pipe73
        hide LLH_3_color_pipe74
        hide LLH_3_color_pipe75
        hide LLH_3_color_pipe76
    
    if whileBGin1 == True or whileRGin1 == True:
        if ifRin5 == True or ifR2in5 == True:
            image LLH_3_color_pipe77 = "R_vertical_ll.png"
            show LLH_3_color_pipe77 at Position(xpos = 823, xanchor = 0, ypos = 405, yanchor = 0)
            image LLH_3_color_pipe78 = "R_horizontal_ll.png"
            show LLH_3_color_pipe78 at Position(xpos = 860, xanchor = 0, ypos = 370, yanchor = 0)
            image LLH_3_color_pipe79 = "W_corner_RB.png"
            show LLH_3_color_pipe79 at Position(xpos = 797, xanchor = 0, ypos = 344, yanchor = 0)
            image LLH_3_color_pipe80 = "R_vertical_ll.png"
            show LLH_3_color_pipe80 at Position(xpos = 970, xanchor = 0, ypos = 255, yanchor = 0)
            
            $LLH_3_REnd2 = "On"
            $LLH_3_node1 = "Red"
        elif ifRin5 == False and ifR2in5 == False:
            hide LLH_3_color_pipe77
            hide LLH_3_color_pipe78
            hide LLH_3_color_pipe79
            hide LLH_3_color_pipe80

    if ifGin5 == True:
        if ifBGin4 == True or ifRBin4 == True or ifRin4 == True or ifR2in4 == True:
            image LLH_3_color_pipe81 = "G_vertical_ll.png"
            show LLH_3_color_pipe81 at Position(xpos = 821, xanchor = 0, ypos = 405, yanchor = 0)
            image LLH_3_color_pipe82 = "G_horizontal_ll.png"
            show LLH_3_color_pipe82 at Position(xpos = 860, xanchor = 0, ypos = 370, yanchor = 0)
            image LLH_3_color_pipe83 = "W_corner_RB.png"
            show LLH_3_color_pipe83 at Position(xpos = 797, xanchor = 0, ypos = 344, yanchor = 0)
            image LLH_3_color_pipe84 = "G_vertical_ll.png"
            show LLH_3_color_pipe84 at Position(xpos = 968, xanchor = 0, ypos = 255, yanchor = 0)
                
            $LLH_3_node1 = "Green"
            $LLH_3_node2 = "Green"
        elif ifBGin4 == False and ifRBin4 == False and ifRin4 == False and ifR2in4 == False:
            hide LLH_3_color_pipe81
            hide LLH_3_color_pipe82
            hide LLH_3_color_pipe83
            hide LLH_3_color_pipe84    
    elif ifGin5 == False:
        hide LLH_3_color_pipe81
        hide LLH_3_color_pipe82
        hide LLH_3_color_pipe83
        hide LLH_3_color_pipe84
        
    if whileRGin1 == True:
        if ifRBin6 == True:
            image LLH_3_color_pipe85 = "R_horizontal_short.png"
            show LLH_3_color_pipe85 at Position(xpos = 325, xanchor = 0, ypos = 485, yanchor = 0)
            image LLH_3_color_pipe86 = "B_horizontal_short.png"
            show LLH_3_color_pipe86 at Position(xpos = 325, xanchor = 0, ypos = 545, yanchor = 0)
            image LLH_3_color_pipe87 = "B_horizontal_short.png"
            show LLH_3_color_pipe87 at Position(xpos = 175, xanchor = 0, ypos = 515, yanchor = 0)
            image LLH_3_color_pipe88 = "R_vertical_ll.png"
            show LLH_3_color_pipe88 at Position(xpos = 236, xanchor = 0, ypos = 405, yanchor = 0)
            
            $LLH_3_REnd3 = "On"
            $LLH_3_BEnd2 = "On"
        elif ifRBin6 == False:
            hide LLH_3_color_pipe85
            hide LLH_3_color_pipe86
            hide LLH_3_color_pipe87
            hide LLH_3_color_pipe88
    elif whileRGin1 == False:
        hide LLH_3_color_pipe85
        hide LLH_3_color_pipe86
        hide LLH_3_color_pipe87
        hide LLH_3_color_pipe88
       
        
    if whileRGin1 == True:
        if ifRin6 == True or ifR2in6 == True:
                image LLH_3_color_pipe96 = "R_horizontal_short.png"
                show LLH_3_color_pipe96 at Position(xpos = 325, xanchor = 0, ypos = 485, yanchor = 0)
                image LLH_3_color_pipe97 = "R_vertical_ll.png"
                show LLH_3_color_pipe97 at Position(xpos = 236, xanchor = 0, ypos = 405, yanchor = 0)
                $LLH_3_REnd3 = "On"
        elif ifRin6 == False and ifR2in6 == False:
                hide LLH_3_color_pipe96
                hide LLH_3_color_pipe97
    elif whileRGin1 == False:
        hide LLH_3_color_pipe96
        hide LLH_3_color_pipe97
    
    if ifBGin6 == True:
        image LLH_3_color_pipe89 = "B_horizontal_short.png"
        show LLH_3_color_pipe89 at Position(xpos = 325, xanchor = 0, ypos = 545, yanchor = 0)
        image LLH_3_color_pipe90 = "B_horizontal_short.png"
        show LLH_3_color_pipe90 at Position(xpos = 175, xanchor = 0, ypos = 515, yanchor = 0)
        image LLH_3_color_pipe91 = "G_horizontal_short.png"
        show LLH_3_color_pipe91 at Position(xpos = 325, xanchor = 0, ypos = 515, yanchor = 0)
        image LLH_3_color_pipe92 = "G_vertical_ll.png"
        show LLH_3_color_pipe92 at Position(xpos = 234, xanchor = 0, ypos = 405, yanchor = 0)
        
        $LLH_3_BEnd2 = "On"
    
    elif ifBGin6 == False:
        hide LLH_3_color_pipe89
        hide LLH_3_color_pipe90
        hide LLH_3_color_pipe91
        hide LLH_3_color_pipe92
    
    if ifGin6 == True:
        image LLH_3_color_pipe95 = "G_horizontal_short.png"
        show LLH_3_color_pipe95 at Position(xpos = 325, xanchor = 0, ypos = 515, yanchor = 0)
    elif ifGin6 == False:
        hide LLH_3_color_pipe95
        
    if whileRGin1 == True:
        if ifRin7 == True or ifR2in7 == True:
            image LLH_3_color_pipe98 = "R_vertical_ll.png"
            show LLH_3_color_pipe98 at Position(xpos = 357, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_3_color_pipe99 = "R_vertical_short.png"
            show LLH_3_color_pipe99 at Position(xpos = 352, xanchor = 0, ypos = 260, yanchor = 0)
            
            $LLH_3_node4 = "Red"
        elif ifRin7 == False and ifR2in7 == False:
            hide LLH_3_color_pipe98
            hide LLH_3_color_pipe99
    elif whileRGin1 == False:
        hide LLH_3_color_pipe98
        hide LLH_3_color_pipe99
        
    if ifGin7 == True:
        image LLH_3_color_pipe100 = "G_vertical_ll.png"
        show LLH_3_color_pipe100 at Position(xpos = 355, xanchor = 0, ypos = 410, yanchor = 0)
        image LLH_3_color_pipe101 = "G_vertical_short.png"
        show LLH_3_color_pipe101 at Position(xpos = 350, xanchor = 0, ypos = 260, yanchor = 0)
        
        $LLH_3_node4 = "Green"
        $LLH_3_node5 = "Green"
        $LLH_3_GEnd2 = "On"
    elif ifGin7 == False:
        hide LLH_3_color_pipe100
        hide LLH_3_color_pipe101
        
                
            

            
    #Redraw Connect Nodes *********************************************************************
    
    hide LLH_3_WNode1
    hide LLH_3_WNode2
    hide LLH_3_WNode3
    hide LLH_3_WNode4
    hide LLH_3_WNode5
    hide LLH_3_WNode6
    hide LLH_3_RNode1
    hide LLH_3_RNode2
    hide LLH_3_RNode3
    hide LLH_3_RNode4
    hide LLH_3_RNode5
    hide LLH_3_RNode6
    hide LLH_3_GNode1
    hide LLH_3_GNode2
    hide LLH_3_GNode3
    hide LLH_3_GNode4
    hide LLH_3_GNode5
    hide LLH_3_GNode6
    hide LLH_3_BNode1
    hide LLH_3_BNode2
    hide LLH_3_BNode3
    hide LLH_3_BNode4
    hide LLH_3_BNode5
    hide LLH_3_BNode6

    
    image LLH_3_WNode1 = "W_connect_node.png"
    image LLH_3_WNode2 = "W_connect_node.png"
    image LLH_3_WNode3 = "W_connect_node.png"
    image LLH_3_WNode4 = "W_connect_node.png"
    image LLH_3_WNode5 = "W_connect_node.png"
    image LLH_3_WNode6 = "W_connect_node.png"
    image LLH_3_RNode1 = "R_connect_node.png"
    image LLH_3_RNode2 = "R_connect_node.png"
    image LLH_3_RNode3 = "R_connect_node.png"
    image LLH_3_RNode4 = "R_connect_node.png"
    image LLH_3_RNode5 = "R_connect_node.png"
    image LLH_3_RNode6 = "R_connect_node.png"
    image LLH_3_GNode1 = "G_connect_node.png"
    image LLH_3_GNode2 = "G_connect_node.png"
    image LLH_3_GNode3 = "G_connect_node.png"
    image LLH_3_GNode4 = "G_connect_node.png"
    image LLH_3_GNode5 = "G_connect_node.png"
    image LLH_3_GNode6 = "G_connect_node.png"
    image LLH_3_BNode1 = "B_connect_node.png"
    image LLH_3_BNode2 = "B_connect_node.png"
    image LLH_3_BNode3 = "B_connect_node.png"
    image LLH_3_BNode4 = "B_connect_node.png"
    image LLH_3_BNode5 = "B_connect_node.png"
    image LLH_3_BNode6 = "B_connect_node.png"

    
    if LLH_3_node1 == "None":
        show LLH_3_WNode1 at Position(xpos = 820, xanchor = 0, ypos = 467, yanchor = 0) 
    elif LLH_3_node1 == "Red":
        show LLH_3_RNode1 at Position(xpos = 820, xanchor = 0, ypos = 467, yanchor = 0) 
    elif LLH_3_node1 == "Green":
        show LLH_3_GNode1 at Position(xpos = 820, xanchor = 0, ypos = 467, yanchor = 0) 
    elif LLH_3_node1 == "Blue":
        show LLH_3_BNode1 at Position(xpos = 820, xanchor = 0, ypos = 467, yanchor = 0) 
        
    if LLH_3_node2 == "None":
        show LLH_3_WNode2 at Position(xpos = 820, xanchor = 0, ypos = 503, yanchor = 0) 
    elif LLH_3_node2 == "Red":
        show LLH_3_RNode2 at Position(xpos = 820, xanchor = 0, ypos = 503, yanchor = 0) 
    elif LLH_3_node2 == "Green":
        show LLH_3_GNode2 at Position(xpos = 820, xanchor = 0, ypos = 503, yanchor = 0) 
    elif LLH_3_node2 == "Blue":
        show LLH_3_BNode2 at Position(xpos = 820, xanchor = 0, ypos = 503, yanchor = 0) 
        
    if LLH_3_node3 == "None":
        show LLH_3_WNode3 at Position(xpos = 820, xanchor = 0, ypos = 539, yanchor = 0) 
    elif LLH_3_node3 == "Red":
        show LLH_3_RNode3 at Position(xpos = 820, xanchor = 0, ypos = 539, yanchor = 0) 
    elif LLH_3_node3 == "Green":
        show LLH_3_GNode3 at Position(xpos = 820, xanchor = 0, ypos = 539, yanchor = 0) 
    elif LLH_3_node3 == "Blue":
        show LLH_3_BNode3 at Position(xpos = 820, xanchor = 0, ypos = 539, yanchor = 0)
    
    if LLH_3_node4 == "None":
        show LLH_3_WNode4 at Position(xpos = 355, xanchor = 0, ypos = 483, yanchor = 0)
    elif LLH_3_node4 == "Red":
        show LLH_3_RNode4 at Position(xpos = 355, xanchor = 0, ypos = 483, yanchor = 0)
    elif LLH_3_node4 == "Green":
        show LLH_3_GNode4 at Position(xpos = 355, xanchor = 0, ypos = 483, yanchor = 0) 
    elif LLH_3_node4 == "Blue":
        show LLH_3_BNode4 at Position(xpos = 355, xanchor = 0, ypos = 483, yanchor = 0)
        
    if LLH_3_node5 == "None":
        show LLH_3_WNode5 at Position(xpos = 355, xanchor = 0, ypos = 513, yanchor = 0)
    elif LLH_3_node5 == "Red":
        show LLH_3_RNode5 at Position(xpos = 355, xanchor = 0, ypos = 513, yanchor = 0)
    elif LLH_3_node5 == "Green":
        show LLH_3_GNode5 at Position(xpos = 355, xanchor = 0, ypos = 513, yanchor = 0)
    elif LLH_3_node5 == "Blue":
        show LLH_3_BNode5 at Position(xpos = 355, xanchor = 0, ypos = 513, yanchor = 0)
        
    if LLH_3_node6 == "None":
        show LLH_3_WNode6 at Position(xpos = 355, xanchor = 0, ypos = 543, yanchor = 0)
    elif LLH_3_node6 == "Red":
        show LLH_3_RNode6 at Position(xpos = 355, xanchor = 0, ypos = 543, yanchor = 0)
    elif LLH_3_node6 == "Green":
        show LLH_3_GNode6 at Position(xpos = 355, xanchor = 0, ypos = 543, yanchor = 0) 
    elif LLH_3_node6 == "Blue":
        show LLH_3_BNode6 at Position(xpos = 355, xanchor = 0, ypos = 543, yanchor = 0)
        
    
    #Redraw Ends *******************************************************************************
    hide LLH_3_BlueEnd1_Off
    hide LLH_3_BlueEnd2_Off
    hide LLH_3_GreenEnd1_Off
    hide LLH_3_GreenEnd2_Off
    hide LLH_3_RedEnd1_Off
    hide LLH_3_RedEnd2_Off
    hide LLH_3_RedEnd3_Off
    hide LLH_3_BlueEnd1_On
    hide LLH_3_BlueEnd2_On
    hide LLH_3_GreenEnd1_On
    hide LLH_3_GreenEnd2_On
    hide LLH_3_RedEnd1_On
    hide LLH_3_RedEnd2_On
    hide LLH_3_RedEnd3_On
    
    
    image LLH_3_BlueEnd1_Off = "B_end_off.png"
    image LLH_3_BlueEnd2_Off = "B_end_off.png"
    image LLH_3_GreenEnd1_Off = "G_end_off.png"
    image LLH_3_GreenEnd2_Off = "G_end_off.png"
    image LLH_3_RedEnd1_Off = "R_end_off.png"
    image LLH_3_RedEnd2_Off = "R_end_off.png"
    image LLH_3_RedEnd3_Off = "R_end_off.png"
    image LLH_3_BlueEnd1_On = "B_end_on.png"
    image LLH_3_BlueEnd2_On = "B_end_on.png"
    image LLH_3_GreenEnd1_On = "G_end_on.png"
    image LLH_3_GreenEnd2_On = "G_end_on.png"
    image LLH_3_RedEnd1_On = "R_end_on.png"
    image LLH_3_RedEnd2_On = "R_end_on.png"
    image LLH_3_RedEnd3_On = "R_end_on.png"
    
    if LLH_3_BEnd1 == "Off":
        show LLH_3_BlueEnd1_Off at Position(xpos = 1050, xanchor = 0, ypos = 480, yanchor = 0)
    elif LLH_3_BEnd1 == "On":
        show LLH_3_BlueEnd1_On at Position(xpos = 1050, xanchor = 0, ypos = 480, yanchor = 0)
       
    if LLH_3_BEnd2 == "Off":
        show LLH_3_BlueEnd2_Off at Position(xpos = 95, xanchor = 0, ypos = 480, yanchor = 0)
    elif LLH_3_BEnd2 == "On":
        show LLH_3_BlueEnd2_On at Position(xpos = 95, xanchor = 0, ypos = 480, yanchor = 0)
        
    if LLH_3_GEnd1 == "Off":
        show LLH_3_GreenEnd1_Off at Position(xpos = 920, xanchor = 0, ypos = 630, yanchor = 0)
    elif LLH_3_GEnd1 == "On":
        show LLH_3_GreenEnd1_On at Position(xpos = 920, xanchor = 0, ypos = 630, yanchor = 0)
        
    if LLH_3_GEnd2 == "Off":
        show LLH_3_GreenEnd2_Off at Position(xpos = 315, xanchor = 0, ypos = 180, yanchor = 0)
    elif LLH_3_GEnd2 == "On":
        show LLH_3_GreenEnd2_On at Position(xpos = 315, xanchor = 0, ypos = 180, yanchor = 0)
        
    if LLH_3_REnd1 == "Off":
        show LLH_3_RedEnd1_Off at Position(xpos = 155, xanchor = 0, ypos = 725, yanchor = 0)
    elif LLH_3_REnd1 == "On":
        show LLH_3_RedEnd1_On at Position(xpos = 155, xanchor = 0, ypos = 725, yanchor = 0)
        
    if LLH_3_REnd2 == "Off":
        show LLH_3_RedEnd2_Off at Position(xpos = 935, xanchor = 0, ypos = 170, yanchor = 0)
    elif LLH_3_REnd2 == "On":
        show LLH_3_RedEnd2_On at Position(xpos = 935, xanchor = 0, ypos = 170, yanchor = 0)
        
    if LLH_3_REnd3 == "Off":
        show LLH_3_RedEnd3_Off at Position(xpos = 200, xanchor = 0, ypos = 310, yanchor = 0)
    elif LLH_3_REnd3 == "On":
        show LLH_3_RedEnd3_On at Position(xpos = 200, xanchor = 0, ypos = 310, yanchor = 0)
    
    #Redraw While Nodes ***************************************************************************

    hide LLH_3_Blue_While_Node_Off
    hide LLH_3_Blue_While_Node_On
    hide LLH_3_Green_While_Node_Off
    hide LLH_3_Green_While_Node_On
    hide LLH_3_Green_While_Node2_Off
    hide LLH_3_Green_While_Node2_On
    hide LLH_3_Red_While_Node_Off
    hide LLH_3_Red_While_Node_On
    
    image LLH_3_Blue_While_Node_Off = "b_while_off.png"
    image LLH_3_Blue_While_Node_On = "b_while_on.png"
    image LLH_3_Green_While_Node_Off = "g_while_off.png"
    image LLH_3_Green_While_Node_On = "g_while_on.png"
    image LLH_3_Green_While_Node2_Off = "g_while_off.png"
    image LLH_3_Green_While_Node2_On = "g_while_on.png"
    image LLH_3_Red_While_Node_Off = "r_while_off.png"
    image LLH_3_Red_While_Node_On = "r_while_on.png"
    
    
    if LLH_3_GWhileNode == "Off":
        show LLH_3_Green_While_Node_Off at Position(xpos = 745, xanchor = 0, ypos = 468, yanchor = 0)
    elif LLH_3_GWhileNode == "On":
        show LLH_3_Green_While_Node_On at Position(xpos = 745, xanchor = 0, ypos = 468, yanchor = 0)
        
    if LLH_3_RWhileNode == "Off":
        show LLH_3_Red_While_Node_Off at Position(xpos = 480, xanchor = 0, ypos = 483, yanchor = 0)
    elif LLH_3_RWhileNode == "On":
        show LLH_3_Red_While_Node_On at Position(xpos = 480, xanchor = 0, ypos = 483, yanchor = 0)
        
    if LLH_3_BWhileNode == "Off":
        show LLH_3_Blue_While_Node_Off at Position(xpos = 475, xanchor = 0, ypos = 635, yanchor = 0)
    elif LLH_3_BWhileNode == "On":
        show LLH_3_Blue_While_Node_On at Position(xpos = 475, xanchor = 0, ypos = 635, yanchor = 0)
        
    if LLH_3_GWhileNode2 == "Off":
        show LLH_3_Green_While_Node2_Off at Position(xpos = 745, xanchor = 0, ypos = 539, yanchor = 0)
    elif LLH_3_GWhileNode2 == "On":
        show LLH_3_Green_While_Node2_On at Position(xpos = 745, xanchor = 0, ypos = 539, yanchor = 0)
    
#win conditions ********
    if whileRGin1 == True and whileBGin2 == True and (ifRin3 == True or ifR2in3 == True) and ifBGin4 == True and (ifRin5 == True or ifR2in5 == True) and ifRBin6 == True and ifGin7 == True:
        image LLH_3_ifR = "R_if.png"
        show LLH_3_ifR at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        image LLH_3_ifG = "G_if.png"
        show LLH_3_ifG at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        image LLH_3_ifR2 = "R_if.png"
        show LLH_3_ifR2 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        image LLH_3_whileBG = "BG_while.png"
        show LLH_3_whileBG at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        image LLH_3_ifBG = "BG_if.png"
        show LLH_3_ifBG at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        image LLH_3_whileRG = "RG_while.png"
        show LLH_3_whileRG at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        image LLH_3_ifRB = "RB_if.png"
        show LLH_3_ifRB at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)

        image LLH_3_ifRBorder = "placeholder3.png"
        show LLH_3_ifRBorder at Position(xpos = 1375, xanchor = 0, ypos = 540, yanchor = 0)
        image LLH_3_ifGBorder = "placeholder3.png"
        show LLH_3_ifGBorder at Position(xpos = 1665, xanchor = 0, ypos = 540, yanchor = 0)
        image LLH_3_ifRBBorder = "placeholder3.png"
        show LLH_3_ifRBBorder at Position(xpos = 1515, xanchor = 0, ypos = 540, yanchor = 0)
        image LLH_3_ifBGBorder = "placeholder3.png"
        show LLH_3_ifBGBorder at Position(xpos = 1375, xanchor = 0, ypos = 710, yanchor = 0)
        image LLH_3_whileRGBorder = "placeholder3.png"
        show LLH_3_whileRGBorder at Position(xpos = 1515, xanchor = 0, ypos = 710, yanchor = 0)
        image LLH_3_whileBGBorder = "placeholder3.png"
        show LLH_3_whileBGBorder at Position(xpos = 1665, xanchor = 0, ypos = 710, yanchor = 0)

        "You Win!"
        jump loopLogic_hard3

    if attempts == 0:
        
#        image LLH_3_gate1 = "blank_node.png"
#        show LLH_3_gate1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
#        image LLH_3_gate2 = "blank_node.png"
#        show LLH_3_gate2 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
#        image LLH_3_gate3 = "blank_node.png"
#        show LLH_3_gate3 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
#        image LLH_3_gate4 = "blank_node.png"
#        show LLH_3_gate4 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
#        image LLH_3_gate5 = "blank_node.png"
#        show LLH_3_gate5 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
#        image LLH_3_gate6 = "blank_node.png"
#        show LLH_3_gate6 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
#        image LLH_3_gate7 = "blank_node.png"
#        show LLH_3_gate7 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        
        show LLH_3_ifR at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        show LLH_3_ifG at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        show LLH_3_ifR2 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        show LLH_3_whileBG at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        show LLH_3_ifBG at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        show LLH_3_whileRG at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        show LLH_3_ifRB at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
            
        show LLH_3_ifRBorder at Position(xpos = 1375, xanchor = 0, ypos = 540, yanchor = 0)
        show LLH_3_ifGBorder at Position(xpos = 1665, xanchor = 0, ypos = 540, yanchor = 0)
        show LLH_3_ifRBBorder at Position(xpos = 1515, xanchor = 0, ypos = 540, yanchor = 0)
        show LLH_3_ifBGBorder at Position(xpos = 1375, xanchor = 0, ypos = 710, yanchor = 0)
        show LLH_3_whileRGBorder at Position(xpos = 1515, xanchor = 0, ypos = 710, yanchor = 0)
        show LLH_3_whileBGBorder at Position(xpos = 1665, xanchor = 0, ypos = 710, yanchor = 0)
            
        "You lose. Try again!"
        jump loopLogic_hard3
    
    jump gamefile_llh3

screen loopLogicHard_3Scr:
    
    #drags and drop location
    draggroup:
            #if gates
#            drag:
#                drag_name "if_B_gate"
#                child "B_if.png"
#                droppable False
#                dragged gate_dragged
#                xpos ifBx ypos ifBy
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
                drag_name "if_R2_gate"
                child "R_if.png"
                droppable False
                dragged gate_dragged
                xpos ifR2x ypos ifR2y
            
            drag:
                drag_name "if_RB_gate"
                child "RB_if.png"
                droppable False
                dragged gate_dragged
                xpos ifRBx ypos ifRBy
                
            drag:
                drag_name "if_BG_gate"
                child "BG_if.png"
                droppable False
                dragged gate_dragged
                xpos ifBGx ypos ifBGy

            #while gate
            drag:
                drag_name "while_RG_gate"
                child "RG_while.png"
                droppable False
                dragged gate_dragged
                xpos whileRGx ypos whileRGy 
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
                drag_name "R_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1375 ypos 540

            drag:
                drag_name "G_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1665 ypos 540
            drag:
                drag_name "BG_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1375 ypos 710
            drag:
                drag_name "if_RB_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 540
            drag:
                drag_name "RG_while_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 710
            drag:
                drag_name "BG_while_return"
                child "placeholder3.png"
                draggable False
                xpos 1665 ypos 710

