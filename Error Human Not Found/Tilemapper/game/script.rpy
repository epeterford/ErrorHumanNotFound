label gamefile:
    
    #calls game screen
    call screen logicGates
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and2in1 == True:
               $ and2x = 50
               $ and2y = 250
               $ and2in1 = False
            if or1in1 == True:
               $ or1x = 175
               $ or1y = 125
               $ or1in2 = False
            #sets values for checks
            $ and1x = 625
            $ and1y = 525
            $ and1in1 = True
            $ and1in2 = False
            $ and1in3 = False
                
        #gate slot number 2********************************** 
        if slot_name == "gate slot two":
            if and2in2 == True:
               $ and2x = 50
               $ and2y = 250
               $ and2in2 = False
            if or1in2 == True:
               $ or1x = 175
               $ or1y = 125
               $ or1in2 = Flase
            #sets check values
            $ and1x = 925
            $ and1y = 325
            $ and1in1 = False
            $ and1in2 = True
            $ and1in3 = False
                
        #gate slot number three******************************
        if slot_name == "gate slot three":
            if and2in3 == True:
               $ and2x = 50
               $ and2y = 250
               $ and2in3 = False
            if or1in3 == True:
               $ or1x = 175
               $ or1y = 125
               $ or1in3 = False
            #sets values for the checks
            $ and1x = 1025
            $ and1y = 725
            $ and1in1 = False
            $ and1in2 = False
            $ and1in3 = True
            
    #the second and gate location**************************************************************************
    if gate_name == "and_gate1":
        #gate slot numeber one ********************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 50
               $ and1y = 125
               $ and1in1 = False
            if or1in1 == True:
               $ or1x = 175
               $ or1y = 125
               $ or1in1 = False
            #sets values for checks
            $ and2x = 625
            $ and2y = 525
            $ and2in1 = True
            $ and2in2 = False
            $ and2in3 = False
                
        #gate slot number 2*************************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 50
               $ and1y = 125
               $ and1in2 = False
            if or1in2 == True:
               $ or1x = 175
               $ or1y = 125
               $ or1in2 = False
            #sets values for checks
            $ and2x = 925
            $ and2y = 325
            $ and2in1 = False
            $ and2in2 = True
            $ and2in3 = False
        
        #gate slot number three********************************
        if slot_name == "gate slot three":
            if and1in3 == True:
               $ and1x = 50
               $ and1y = 125
               $ and1in3 = False
            if or1in3 == True:
               $ or1x = 175
               $ or1y = 125
               $ or1in3 = False
            #sets values for checks
            $ and2x = 1025
            $ and2y = 725
            $ and2in1 = False
            $ and2in2 = False
            $ and2in3 = True

            
    #the or gate location **********************************************************************************
    if gate_name == "or_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if and1in1 == True:
               $ and1x = 50
               $ and1y = 125
               $ and1in1 = False
            if and2in1 == True:
               $ and2x = 50
               $ and2y = 250
               $ and2in1 = False
            #sets values for checks
            $ or1x = 625
            $ or1y = 525
            $ or1in1 = True
            $ or1in2 = False
            $ or1in3 = False
            
        #gate slot number 2***********************************
        if slot_name == "gate slot two":
            if and1in2 == True:
               $ and1x = 50
               $ and1y = 125
               $ and1in2 = False
            if and2in2 == True:
               $ and2x = 50
               $ and2y = 250
               $ and2in2 = False
            #sets values for checks
            $ or1x = 925
            $ or1y = 325
            $ or1in1 = False
            $ or1in2 = True
            $ or1in3 = False
        
        #gate slot number three*********************************
        if and1in3 == False and and2in3 == False:
            if slot_name == "gate slot three":
                if and1in3 == True:
                   $ and1x = 50
                   $ and1y = 125
                   $ and1in3 = False
                if and2in3 == True:
                   $ and2x = 50
                   $ and2y = 250
                   $ and2in3 = False
                #sets values for checks
                $ or1x = 1025
                $ or1y = 725
                $ or1in1 = False
                $ or1in2 = False
                $ or1in3 = True


#*******************************************
#************image zone*********************
#*******************************************

#first slot for and 1
    if and1in1 == True:
        image tile81 = "horizontalR.png"
        image tile82 = "cornRLT.png"
        image tile83 = "verticalR.png"
        image tile84 = "inputBR.png"
        image tile85 = "cornRTR.png"
        image tile86 = "horizontalR.png"
        image tile87 = "horizontalR.png"
        image tile88 = "cornRLB.png"
        image tile89 = "inputRR.png"
        #shows tiles
        show tile81 at Position(xpos = 725, xanchor = 0, ypos = 525, yanchor = 0)
        show tile82 at Position(xpos = 825, xanchor = 0, ypos = 525, yanchor = 0)
        show tile83 at Position(xpos = 825, xanchor = 0, ypos = 425, yanchor = 0)
        show tile84 at Position(xpos = 825, xanchor = 0, ypos = 325, yanchor = 0)
        show tile85 at Position(xpos = 725, xanchor = 0, ypos = 625, yanchor = 0)
        show tile86 at Position(xpos = 825, xanchor = 0, ypos = 625, yanchor = 0)
        show tile87 at Position(xpos = 925, xanchor = 0, ypos = 625, yanchor = 0)
        show tile88 at Position(xpos = 925, xanchor = 0, ypos = 625, yanchor = 0)
        show tile89 at Position(xpos = 925, xanchor = 0, ypos = 725, yanchor = 0)
    if and1in1 == False:
        hide tile81
        hide tile82
        hide tile83
        hide tile84
        hide tile85
        hide tile86
        hide tile87
        hide tile88
        hide tile89
        
#first slot for and 2
    if and2in1 == True:
        image tile108 = "horizontalR.png"
        image tile109 = "cornRLT.png"
        image tile110 = "verticalR.png"
        image tile111 = "inputBR.png"
        image tile112 = "cornRTR.png"
        image tile113 = "horizontalR.png"
        image tile114 = "horizontalR.png"
        image tile115 = "cornRLB.png"
        image tile116 = "inputRR.png"
        #shows tiles
        show tile108 at Position(xpos = 725, xanchor = 0, ypos = 525, yanchor = 0)
        show tile109 at Position(xpos = 825, xanchor = 0, ypos = 525, yanchor = 0)
        show tile110 at Position(xpos = 825, xanchor = 0, ypos = 425, yanchor = 0)
        show tile111 at Position(xpos = 825, xanchor = 0, ypos = 325, yanchor = 0)
        show tile112 at Position(xpos = 725, xanchor = 0, ypos = 625, yanchor = 0)
        show tile113 at Position(xpos = 825, xanchor = 0, ypos = 625, yanchor = 0)
        show tile114 at Position(xpos = 925, xanchor = 0, ypos = 625, yanchor = 0)
        show tile115 at Position(xpos = 925, xanchor = 0, ypos = 625, yanchor = 0)
        show tile116 at Position(xpos = 925, xanchor = 0, ypos = 725, yanchor = 0)
    if and2in1 == False: 
        hide tile108
        hide tile109
        hide tile110
        hide tile111
        hide tile112
        hide tile113
        hide tile114
        hide tile115
        hide tile116
        
#first slot for or
    if or1in1 == True:
        image tile135 = "horizontalB.png"
        image tile136 = "cornBLT.png"
        image tile137 = "verticalB.png"
        image tile138 = "inputBB.png"
        image tile139 = "cornBTR.png"
        image tile140 = "horizontalB.png"
        image tile141 = "horizontalB.png"
        image tile142 = "cornBLB.png"
        image tile143 = "inputBR.png"
        #shows tile
        show tile135 at Position(xpos = 725, xanchor = 0, ypos = 525, yanchor = 0)
        show tile136 at Position(xpos = 825, xanchor = 0, ypos = 525, yanchor = 0)
        show tile137 at Position(xpos = 825, xanchor = 0, ypos = 425, yanchor = 0)
        show tile138 at Position(xpos = 825, xanchor = 0, ypos = 325, yanchor = 0)
        show tile139 at Position(xpos = 725, xanchor = 0, ypos = 625, yanchor = 0)
        show tile140 at Position(xpos = 825, xanchor = 0, ypos = 625, yanchor = 0)
        show tile141 at Position(xpos = 925, xanchor = 0, ypos = 625, yanchor = 0)
        show tile142 at Position(xpos = 925, xanchor = 0, ypos = 625, yanchor = 0)
        show tile143 at Position(xpos = 925, xanchor = 0, ypos = 725, yanchor = 0) 
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
            image tile90 = "horizontalR.png"
            image tile91 = "cornRLB.png"
            image tile92 = "inputRG.png"
            #shows tiles
            show tile90 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile91 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            show tile92 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input gate to use
            if or1in3 == True:
                hide tile92
                image tile93 = "inputRR.png"
                show tile93 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
        #checks to see if the or gate is in the previous slot
        elif or1in1 == True:
            image tile94 = "horizontalB.png"
            image tile95 = "cornBLB.png"
            image tile96 = "inputBG.png" 
            #shows tiles
            show tile94 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile95 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            show tile96 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input gate to use
            if and2in3 == True:
                hide tile96
                image tile97 = "inputBR.png"
                show tile97 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)       
        
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
            image tile117 = "horizontalR.png"
            image tile118 = "cornRLB.png"
            image tile119 = "inputRG.png"
            #show tiles
            show tile117 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile118 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            show tile119 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input tile needs to be called
            if or1in3 == True:
                hide tile119
                image tile120 = "inputRR.png"
                show tile120 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
        #checks to see if or1 is in the slot before
        elif or1in1 == True:
            #declares tiles to be shown
            image tile121 = "horizontalB.png"
            image tile122 = "cornBLB.png"
            image tile123 = "inputBG.png" 
            #show tiles
            show tile121 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile122 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            show tile123 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input needs to be called
            if and2in3 == True:
                hide tile123
                image tile124 = "inputBR.png"
                show tile124 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)   
    
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
            image tile144 = "horizontalB.png"
            image tile145 = "cornBLB.png"
            image tile146 = "inputBG.png"
            #show tiles
            show tile144 at Position(xpos = 1025, xanchor = 0, ypos = 325, yanchor = 0)
            show tile145 at Position(xpos = 1125, xanchor = 0, ypos = 325, yanchor = 0)
            show tile146 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks which input should be called
            if and1in3 == True and and2in1 == True:
                hide tile146
                image tile147 = "inputBR.png"
                show tile147 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            elif and2in3 == True and and1in1 == True:
                hide tile146
                image tile147 = "inputBR.png"
                show tile147 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            else:
                hide tile147
    
    if or1in2 == False:
        hide tile144
        hide tile145
        hide tile146
        hide tile147
        
#third slot for and 1
    if and1in3 ==True:
        if and2in1 == True:
            #declares the tiles to be used
            image tile98 = "cornRLT.png"
            image tile99 = "verticalR.png"
            image tile100 = "verticalR.png"
            image tile101 = "inputGR.png"
            #shows tiles
            show tile98 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile99 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile100 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            show tile101 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input gate to use
        if or1in1 == True:
            #declares the tiles to be used
            image tile103 = "cornRLT.png"
            image tile104 = "verticalR.png"
            image tile105 = "verticalR.png"
            image tile106 = "inputGR.png"
            #shows tiles
            show tile103 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile104 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile105 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            show tile106 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input gate to use
            if and2in2 == True:
                hide tile106
                image tile107 = "inputBR.png"
                show tile107 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)

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
            image tile125 = "cornRLT.png"
            image tile126 = "verticalR.png"
            image tile127 = "verticalR.png"
            image tile128 = "inputGR.png"
            #showss tiles
            show tile125 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile126 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile127 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            show tile128 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks which input should be called
        elif or1in1 == True:
            #images being declared to use
            image tile130 = "cornRLT.png"
            image tile131 = "verticalR.png"
            image tile132 = "verticalR.png"
            image tile133 = "inputGR.png"
            #shows tiles
            show tile130 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile131 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile132 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            show tile133 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks to see which input to use
            if and1in2 == True:
                hide tile133
                image tile134 = "inputBR.png"
                show tile134 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
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
            
#third slot for or 1
    if or1in3 == True:
        if and1in1 == True or and2in1 == True:
            #declares tiles to be called
            image tile148 = "cornRLT.png"
            image tile149 = "verticalR.png"
            image tile150 = "verticalR.png"
            image tile151 = "inputGR.png"
            #showss tiles
            show tile148 at Position(xpos = 1125, xanchor = 0, ypos = 725, yanchor = 0)
            show tile149 at Position(xpos = 1125, xanchor = 0, ypos = 625, yanchor = 0)
            show tile150 at Position(xpos = 1125, xanchor = 0, ypos = 525, yanchor = 0)
            show tile151 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            #checks which input should be called
            if and1in2 == True and and2in1 == True:
                hide tile151
                image tile152 = "inputRR.png"
                show tile152 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
            elif and2in2 == True and and1in1 == True:
                hide tile151
                image tile152 = "inputRR.png"
                show tile152 at Position(xpos = 1125, xanchor = 0, ypos = 425, yanchor = 0)
                
    if or1in3 == False:
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152 
        
# hide statement needed for all parts that require a pre filled slot****
    if and1in1 == False and and2in1 == False and or1in1 == False:
        hide tile148
        hide tile149
        hide tile150
        hide tile151
        hide tile152 
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
        hide tile144
        hide tile145
        hide tile146
        hide tile147
        
#win conditions ********
    if and1in2 == True and and2in1 == True and or1in3 == True: 
        image tile153 = "horizontalR.png"
        show tile153 at Position(xpos = 1325, xanchor = 0, ypos = 425, yanchor = 0)
        "you win 1"
        jump start
    if and1in1 == True and and2in2 == True and or1in3 == True: 
        image tile153 = "horizontalR.png"
        show tile153 at Position(xpos = 1325, xanchor = 0, ypos = 425, yanchor = 0)
        "you win 2"
        jump start
        
        
    $ attempts -= 1
    if attempts == 0:
        "you lose try again"
        jump start
    
    jump gamefile


