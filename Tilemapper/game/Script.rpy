init:
    image bg Logic_Gate = "LOGIC_GATE_BG.png"

label start:

    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 1
    image tile11 = "GREEN-HORIZ-LINE.png"
    image tile12 = "GREEN-HORIZ-LINE.png"
    image tile13 = "GREEN-HORIZ-LINE.png"
    image tile14 = "GREEN-HORIZ-LINE.png"
    image tile15 = "GREEN-ELBOW - BL.png"

    show tile11 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show tile12 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show tile13 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show tile14 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show tile15 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)

    #row 2
    image tile25 = "GREEN-YELLOW.png"
    image tile26 = "NONE_Gate.png"
    image tile27 = "YELLOW-HORIZ-LINE.png"
    image tile28 = "YELLOW-ELBOW - BL.png"

    show tile25 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show tile26 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show tile27 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show tile28 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3
    image tile31 = "GREEN-HORIZ-LINE.png"
    image tile32 = "GREEN-ELBOW - BL.png"
    image tile35 = "YELLOW-VERT-LINE.png"
    image tile38 = "YELLOW-YELLOW.png"
    image tile39 = "AND_Gate.png"
    image tile40 = "YELLOW-HORIZ-LINE.png"
    image tile161 = "YELLOW-HORIZ-LINE.png"
    image tile162 = "YELLOW-HORIZ-LINE.png"
    image tile163 = "YELLOW-HORIZ-LINE.png"
    image tile164 = "YELLOW-HORIZ-LINE.png"
    
    show tile31 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show tile32 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show tile35 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show tile38 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
    show tile39 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show tile40 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show tile161 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show tile162 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
    show tile163 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
    show tile164 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4
    image tile42 = "GREEN-RED.png"
    image tile43 = "NONE_Gate.png"
    image tile44 = "YELLOW-T.png"
    image tile45 = "YELLOW-ELBOW - TL.png"
    image tile48 = "YELLOW-VERT-LINE.png"

    show tile42 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
    show tile43 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show tile44 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    show tile45 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show tile48 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)

    
    #row 5
    image tile51 = "RED-T.png"
    image tile52 = "RED-ELBOW - TL.png"
    image tile54 = "YELLOW-ELBOW - TR.png"
    image tile55 = "YELLOW-HORIZ-LINE.png"
    image tile56 = "YELLOW-ELBOW - BL.png"
    image tile58 = "YELLOW-VERT-LINE.png"

    show tile51 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show tile52 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show tile54 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show tile55 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show tile56 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show tile58 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)

    
    #row 6
    image tile61 = "RED-VERT-LINE.png"
    image tile66 = "YELLOW-RED.png"
    image tile67 = "NONE_Gate.png"
    image tile68 = "YELLOW-ELBOW - TL.png"

    show tile61 at Position(xpos = 436, xanchor = 0, ypos = 683, yanchor = 0)
    show tile66 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show tile67 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show tile68 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7
    image tile71 = "RED-ELBOW - TR.png"
    image tile72 = "RED-HORIZ-LINE.png"
    image tile73 = "RED-HORIZ-LINE.png"
    image tile74 = "RED-HORIZ-LINE.png"
    image tile75 = "RED-HORIZ-LINE.png"
    image tile76 = "RED-ELBOW - TL.png"

    show tile71 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show tile72 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show tile73 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show tile74 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show tile75 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show tile76 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
    
    #start and end points
    image start1 = "GREEN.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start2 = "GREEN.png"
    show start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image start3 = "RED.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image end = "YELLOW.png"
    show end at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
    
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
    $ and2x = 586
    $ and2y = 88
    $ or1x = 812
    $ or1y = 88
    # check conditons for locations
    $ and1in1 = False
    $ and1in2 = False
    $ and1in3 = False
    $ and2in1 = False
    $ and2in2 = False
    $ and2in3 = False
    $ or1in1 = False
    $ or1in2 = False
    $ or1in3 = False
    #attempts for players
    $ attempts = 6
 
    jump gamefile
    
    
label gamefile:
    
    #calls game screen
    call screen logicGates
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and2in1 == True:
               $ and2x = 586
               $ and2y = 88
               $ and2in1 = False
            if or1in1 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in2 = False
            #sets values for checks
            $ and1x = 586
            $ and1y = 533
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
                
        #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and2in2 == True:
               $ and2x = 586
               $ and2y = 88
               $ and2in2 = False
            if or1in2 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in2 = False
            #sets check values
            $ and1x = 811
            $ and1y = 383
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
                
        #gate slot number three******************************
        if slot_name == "gate slot three":
            if and2in3 == True:
               $ and2x = 586
               $ and2y = 88
               $ and2in3 = False
            if or1in3 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in3 = False
            #sets values for the checks
            $ and1x = 886
            $ and1y = 683
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            
    #the second and gate location**************************************************************************
    if gate_name == "and_gate1":
        #gate slot numeber one ********************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in1 = False
            if or1in1 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in1 = False
            #sets values for checks
            $ and2x = 586
            $ and2y = 533
            $ and2in1 = True
            $ and2in2 = False
            $ and2in3 = False
                
        #gate slot number 2*************************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in2 = False
            if or1in2 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in2 = False
            #sets values for checks
            $ and2x = 811
            $ and2y = 383
            $ and2in1 = False
            $ and2in2 = True
            $ and2in3 = False
        
        #gate slot number three********************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in3 = False
            if or1in3 == True:
               $ or1x = 812
               $ or1y = 88
               $ or1in3 = False
            #sets values for checks
            $ and2x = 886
            $ and2y = 683
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = True

            
    #the or gate location **********************************************************************************
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in1 = False
            if and2in1 == True:
               $ and2x = 586
               $ and2y = 88
               $ and2in1 = False
            #sets values for checks
            $ or1x = 586
            $ or1y = 533
            $ or1in1 = True
            $ or1in2 = False
            $ or1in3 = False
            
        #gate slot number 2***********************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in2 = False
            if and2in2 == True:
               $ and2x = 586
               $ and2y = 88
               $ and2in2 = False
            #sets values for checks
            $ or1x = 811
            $ or1y = 383
            $ or1in1 = False
            $ or1in2 = True
            $ or1in3 = False
        
        #gate slot number three*********************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ and1x = 586
               $ and1y = 88
               $ and1in3 = False
            if and2in3 == True:
               $ and2x = 586
               $ and2y = 88
               $ and2in3 = False
            #sets values for checks
            $ or1x = 886
            $ or1y = 683
            $ or1in1 = False
            $ or1in2 = False
            $ or1in3 = True


#*******************************************
#************image zone*********************
#*******************************************

#first slot for and 1
    if and1in1 == True or and2in1 == True:
        image tile81 = "RED-T.png"
        image tile82 = "RED-ELBOW - TL.png"
        image tile83 = "RED-VERT-LINE.png"
        image tile84 = "GREEN-RED.png"
        image tile85 = "RED-ELBOW - TR.png"
        image tile86 = "RED-HORIZ-LINE.png"
        image tile88 = "RED-ELBOW - BL.png"
        image tile89 = "RED-RED.png"
        #shows tiles
        show tile81 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show tile82 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show tile83 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        show tile84 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show tile85 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show tile86 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        show tile88 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show tile89 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    if and1in1 == False and and2in1 == False:
        hide tile81
        hide tile82
        hide tile83
        hide tile84
        hide tile85
        hide tile86
        hide tile88
        hide tile89
        
#first slot for or
    if or1in1 == True:
        image tile135 = "GREEN-T.png"
        image tile136 = "GREEN-ELBOW - TL.png"
        image tile137 = "GREEN-VERT-LINE.png"
        image tile138 = "GREEN-GREEN.png"
        image tile139 = "GREEN-ELBOW - TR.png"
        image tile140 = "GREEN-HORIZ-LINE.png"
        image tile142 = "GREEN-ELBOW - BL.png"
        image tile143 = "GREEN-RED.png"
        #shows tile
        show tile135 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
        show tile136 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
        show tile137 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
        show tile138 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
        show tile139 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
        show tile140 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
        show tile142 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
        show tile143 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0) 
    if or1in1 == False:
        hide tile135
        hide tile136
        hide tile137
        hide tile138
        hide tile139
        hide tile140
        hide tile141
        hide tile142
        hide tile143
        
#second slot for and 1
    if and1in2 == True:
        if and2in1 == True:
            #declares the tiles to be used
            image tile90 = "RED-HORIZ-LINE.png"
            image tile91 = "RED-ELBOW - BL.png"
            #shows tiles
            show tile90 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile91 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            #checks to see which input gate to use
            if or1in3 == True:
                image tile93 = "RED-RED.png"
                show tile93 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            if or1in3 == False:
                image tile92 = "RED-YELLOW.png"
                show tile92 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
        #checks to see if the or gate is in the previous slot
        elif or1in1 == True:
            image tile94 = "GREEN-HORIZ-LINE.png"
            image tile95 = "GREEN-ELBOW - BL.png"
            #shows tiles
            show tile94 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile95 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            #checks to see which input gate to use
            if and2in3 == True:
                image tile97 = "GREEN-RED.png"
                show tile97 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            if and2in3 == False:
                image tile96 = "GREEN-YELLOW.png" 
                show tile96 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
    if and1in2 == False:
        hide tile90
        hide tile91
        hide tile92
        hide tile93
        hide tile94
        hide tile95
        hide tile96
        hide tile97

#second slot for and 2       
    if and2in2 == True:
        if and1in1 == True:
            #declares tile to be shown
            image tile117 = "RED-HORIZ-LINE.png"
            image tile118 = "RED-ELBOW - BL.png"
            #show tiles
            show tile117 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile118 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            #checks to see which input tile needs to be called
            if or1in3 == True:
                image tile120 = "RED-RED.png"
                show tile120 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            if or1in3 == False:
                image tile119 = "RED-YELLOW.png"
                show tile119 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
        #checks to see if or1 is in the slot before
        elif or1in1 == True:
            #declares tiles to be shown
            image tile121 = "GREEN-HORIZ-LINE.png"
            image tile122 = "GREEN-ELBOW - BL.png"
            #show tiles
            show tile121 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile122 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            #checks to see which input needs to be called
            if and2in3 == True:
                image tile124 = "GREEN-RED.png"
                show tile124 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0) 
            if and2in3 == False:
                image tile123 = "GREEN-YELLOW.png"
                show tile123 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
    
    if and2in2 == False:
        hide tile117
        hide tile118
        hide tile119
        hide tile120
        hide tile121
        hide tile122
        hide tile123
        hide tile124

#second slot for or 1
    if or1in2 == True:
        if and1in1 == True or and2in1 == True:
            #declares tile to be shown
            image tile144 = "GREEN-HORIZ-LINE.png"
            image tile145 = "GREEN-ELBOW - BL.png"
            image tile146 = "GREEN-YELLOW.png"
            #show tiles
            show tile144 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile145 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            show tile146 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks which input should be called
            if and1in3 == True and and2in1 == True or and2in3 == True and and1in1 == True :
                hide tile146
                image tile147 = "GREEN-RED.png"
                show tile147 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)

    
    if or1in2 == False:
        hide tile144
        hide tile145
        hide tile146
        hide tile147
        
#third slot for and 1
    if and1in3 ==True:
        if and2in1 == True:
            #declares the tiles to be used
            image tile98 = "RED-ELBOW - TL.png"
            image tile99 = "RED-VERT-LINE.png"
            image tile100 = "RED-VERT-LINE.png"
            image tile101 = "YELLOW-RED.png"
            #shows tiles
            show tile98 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile99 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile100 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            show tile101 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input gate to use
        if or1in1 == True:
            #declares the tiles to be used
            image tile103 = "RED-ELBOW - TL.png"
            image tile104 = "RED-VERT-LINE.png"
            image tile105 = "RED-VERT-LINE.png"
            #shows tiles
            show tile103 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile104 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile105 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            #checks to see which input gate to use
            if and2in2 == True:
                image tile107 = "GREEN-RED.png"
                show tile107 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            if and2in2 == False:
                image tile106 = "YELLOW-RED.png"
                show tile106 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)

    if and1in3 == False:
        hide tile98
        hide tile99
        hide tile100
        hide tile101
        hide tile102
        hide tile103
        hide tile104
        hide tile105
        hide tile106
        hide tile107
    
#third slot for and 2
    if and2in3 == True:
        if and1in1 == True:
            #declares tiles to be called
            image tile125 = "RED-ELBOW - TL.png"
            image tile126 = "RED-VERT-LINE.png"
            image tile127 = "RED-VERT-LINE.png"
            #showss tiles
            show tile125 at Position(xpos = 886, xanchor = 0, ypos = 725, yanchor = 0)
            show tile126 at Position(xpos = 886, xanchor = 0, ypos = 625, yanchor = 0)
            show tile127 at Position(xpos = 886, xanchor = 0, ypos = 525, yanchor = 0)
            if or1in2 == False:
                image tile128 = "YELLOW-RED.png"
                show tile128 at Position(xpos = 886, xanchor = 0, ypos = 425, yanchor = 0)
            elif or1in2 == True:
                image tile160 = "GREEN-RED.png"
                show tile160 at Position(xpos = 886, xanchor = 0, ypos = 425, yanchor = 0)
        elif or1in1 == True:
            #images being declared to use
            image tile130 = "RED-ELBOW - TL.png"
            image tile131 = "RED-VERT-LINE.png"
            image tile132 = "RED-VERT-LINE.png"
            #shows tiles
            show tile130 at Position(xpos = 886, xanchor = 0, ypos = 725, yanchor = 0)
            show tile131 at Position(xpos = 886, xanchor = 0, ypos = 625, yanchor = 0)
            show tile132 at Position(xpos = 886, xanchor = 0, ypos = 525, yanchor = 0)
            #checks to see which input to use
            if and1in2 == True:
                image tile134 = "GREEN-RED.png"
                show tile134 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            elif and1in2 == False:
                image tile133 = "YELLOW-RED.png"
                show tile133 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
    if and2in3 == False:
        hide tile125
        hide tile126
        hide tile127
        hide tile128
        hide tile129
        hide tile130
        hide tile131
        hide tile132
        hide tile133
        hide tile134
        hide tile160
            
#third slot for or 1
    if or1in3 == True:
        if and1in1 == True or and2in1 == True:
            #declares tiles to be called
            image tile148 = "RED-ELBOW - TL.png"
            image tile149 = "RED-VERT-LINE.png"
            image tile150 = "RED-VERT-LINE.png"
            image tile151 = "YELLOW-RED.png"
            #showss tiles
            show tile148 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
            show tile149 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
            show tile150 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
            show tile151 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            #checks which input should be called
            if and1in2 == True and and2in1 == True:
                hide tile151
                image tile152 = "RED-RED.png"
                show tile152 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
            elif and2in2 == True and and1in1 == True:
                hide tile151
                image tile152 = "RED-RED.png"
                show tile152 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
                
    if or1in3 == False:
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152 
        
# hide statement needed for all parts that require a pre filled slot****
    if and1in1 == False and and2in1 == False and or1in1 == False:
        hide tile90
        hide tile91
        hide tile92
        hide tile93
        hide tile94
        hide tile95
        hide tile96
        hide tile97
        hide tile98
        hide tile99
        hide tile100
        hide tile101
        hide tile102
        hide tile103
        hide tile104
        hide tile105
        hide tile106
        hide tile107
        hide tile117
        hide tile118
        hide tile119
        hide tile120
        hide tile121
        hide tile122
        hide tile123
        hide tile124
        hide tile125
        hide tile126
        hide tile127
        hide tile128
        hide tile129
        hide tile130
        hide tile131
        hide tile132
        hide tile133
        hide tile134
        hide tile144
        hide tile145
        hide tile146
        hide tile147
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152 
       
        
#win conditions ********
    if and1in2 == True and and2in1 == True and or1in3 == True or and1in1 == True and and2in2 == True and or1in3 == True: 
        image tile153 = "RED-HORIZ-LINE.png"
        show tile153 at Position(xpos = 1325, xanchor = 0, ypos = 425, yanchor = 0)
        "you win 1"
        hide tile81
        hide tile82
        hide tile83
        hide tile84
        hide tile85
        hide tile86
        hide tile87
        hide tile88
        hide tile89
        hide tile90
        hide tile91
        hide tile92
        hide tile93
        hide tile94
        hide tile95
        hide tile96
        hide tile97
        hide tile117
        hide tile118
        hide tile119
        hide tile120
        hide tile121
        hide tile122
        hide tile123
        hide tile124
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152 
        hide tile153
        
        jump start
    if slot_name == "null":
        $attempts +=1
        
    $ attempts -= 1
    if attempts == 0:
        "you lose try again"
        hide tile81
        hide tile82
        hide tile83
        hide tile84
        hide tile85
        hide tile86
        hide tile87
        hide tile88
        hide tile89
        hide tile90
        hide tile91
        hide tile92
        hide tile93
        hide tile94
        hide tile95
        hide tile96
        hide tile97
        hide tile98
        hide tile99
        hide tile100
        hide tile101
        hide tile102
        hide tile103
        hide tile104
        hide tile105
        hide tile106
        hide tile107
        hide tile117
        hide tile118
        hide tile119
        hide tile120
        hide tile121
        hide tile122
        hide tile123
        hide tile124
        hide tile125
        hide tile126
        hide tile127
        hide tile128
        hide tile129
        hide tile130
        hide tile131
        hide tile132
        hide tile133
        hide tile134
        hide tile135
        hide tile136
        hide tile137
        hide tile138
        hide tile139
        hide tile140
        hide tile141
        hide tile142
        hide tile143
        hide tile144
        hide tile145
        hide tile146
        hide tile147
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152 
        jump start
    
    jump gamefile
