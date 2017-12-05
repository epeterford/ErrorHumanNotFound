screen binaryMatch_hard:
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $config.skipping=None
    grid 4 8 spacing 70 at Position(xpos=0.5, xanchor =0.0, ypos =0.05, yanchor = 0.0): 
        for card in cards_listHard:
            button:
                background None
                if card["c_chosen"]:        # shows the face of the card
                    add card["c_value"]    # will show image
                    focus_mask card["c_value"]
                else:                       # shows the back of the card
                    add "cardBack"                # will show image
                    focus_mask "cardBack"
                action If ( (card["c_chosen"] or not can_clickHard), None, [SetDict(cards_listHard[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 275
        ypos 720
        focus_mask True
        action Jump("binaryHardHints")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 185
        ypos 795
    text "Attempts" xpos 193 ypos 815 color "#0060db" font "United Kingdom DEMO.otf" size 24
    text ": " xpos 362 ypos 804 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 376 ypos 813 color "#0060db" font "United Kingdom DEMO.otf" size 27
    imagebutton:
        idle "binaryHardInstructions.png"
        xpos 0
        ypos 0
                
init:
    image A1_Hard = "tileFront0000.png"
    image A2_Hard = "tileFront0.png"
    image B1_Hard = "tileFront1.png"
    image B2_Hard = "tileFront0001.png"
    image C1_Hard = "tileFront0010.png"
    image C2_Hard = "tileFront2.png"
    image D1_Hard = "tileFront0011.png"
    image D2_Hard = "tileFront3.png"
    image E1_Hard = "tileFront0100.png"
    image E2_Hard = "tileFront4.png"
    image F1_Hard = "tileFront5.png"
    image F2_Hard = "tileFront0101.png"
    image G1_Hard = "tileFront0110.png"
    image G2_Hard = "tileFront6.png"
    image H1_Hard = "tileFront0111.png"
    image H2_Hard = "tileFront7.png"
    image I1_Hard = "tileFront1000.png"
    image I2_Hard = "tileFront8.png"
    image J1_Hard = "tileFront9.png"
    image J2_Hard = "tileFront1001.png"
    image K1_Hard = "tileFront1010.png"
    image K2_Hard = "tileFrontTen.png"
    image L1_Hard = "tileFront1011.png"
    image L2_Hard = "tileFrontEleven.png"
    image M1_Hard = "tileFront1100.png"
    image M2_Hard = "tileFront12.png"
    image N1_Hard = "tileFront13.png"
    image N2_Hard = "tileFront1101.png"
    image O1_Hard = "tileFront1110.png"
    image O2_Hard = "tileFront14.png"
    image P1_Hard = "tileFront1111.png"
    image P2_Hard = "tileFront15.png"

label binaryMatchHard:
    $config.skipping=None
    scene bg binary
    window hide
    $ quick_menu = False
    $ attempts = 60
    $ values_listHard = ["A1_Hard", "A2_Hard", "B1_Hard", "B2_Hard", "C1_Hard", "C2_Hard", "D1_Hard", "D2_Hard", "E1_Hard", "E2_Hard", "F1_Hard", "F2_Hard", "G1_Hard", "G2_Hard", "H1_Hard", "H2_Hard", "I1_Hard", "I2_Hard", "J1_Hard", "J2_Hard", "K1_Hard", "K2_Hard", "L1_Hard", "L2_Hard", "M1_Hard", "M2_Hard", "N1_Hard", "N2_Hard", "O1_Hard", "O2_Hard", "P1_Hard", "P2_Hard"]
    $ values_listHard = cards_shuffle(values_listHard)
    $ cards_listHard = []
    python:
        for i in range (0, len(values_listHard)):
            cards_listHard.append({"c_number":i, "c_value": values_listHard[i], "c_chosen":False} )
            
    show screen binaryMatch_hard
    label binaryMatch_gameHard:
        $config.skipping=None
        $ can_clickHard = True
        $ turned_cards_numbersHard = []
        $ turned_cards_valuesHard = []
        $ turns_leftHard = 2
        
        label turns_loopHard:
            if turns_leftHard >0:
                $ can_clickHard = True
                $ result = ui.interact()
                $tileFlipSound = renpy.random.randint(0,2)
                if (tileFlipSound==0):
                    play soundP01 tileFlip1
                if (tileFlipSound==1):
                    play soundP01 tileFlip2
                if (tileFlipSound==2):
                    play soundP01 tileFlip3
                $ turned_cards_numbersHard.append (cards_listHard[result]["c_number"])
                $ turned_cards_valuesHard.append (cards_listHard[result]["c_value"])
                $ turns_leftHard -= 1
                jump turns_loopHard
                
        $ attempts -=1
        $ can_clickHard = False
        $ match = False
        # If not all the opened cards are matched, will turn them face down after pause
        if turned_cards_valuesHard[0]=="A1_Hard" and turned_cards_valuesHard[1]=="A2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="A2_Hard" and turned_cards_valuesHard[1]=="A1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="B1_Hard" and turned_cards_valuesHard[1]=="B2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="B2_Hard" and turned_cards_valuesHard[1]=="B1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="C1_Hard" and turned_cards_valuesHard[1]=="C2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="C2_Hard" and turned_cards_valuesHard[1]=="C1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="D1_Hard" and turned_cards_valuesHard[1]=="D2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="D2_Hard" and turned_cards_valuesHard[1]=="D1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="E1_Hard" and turned_cards_valuesHard[1]=="E2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="E2_Hard" and turned_cards_valuesHard[1]=="E1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="F1_Hard" and turned_cards_valuesHard[1]=="F2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="F2_Hard" and turned_cards_valuesHard[1]=="F1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="G1_Hard" and turned_cards_valuesHard[1]=="G2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="G2_Hard" and turned_cards_valuesHard[1]=="G1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="H1_Hard" and turned_cards_valuesHard[1]=="H2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="H2_Hard" and turned_cards_valuesHard[1]=="H1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="I1_Hard" and turned_cards_valuesHard[1]=="I2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="I2_Hard" and turned_cards_valuesHard[1]=="I1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="J1_Hard" and turned_cards_valuesHard[1]=="J2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="J2_Hard" and turned_cards_valuesHard[1]=="J1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="K1_Hard" and turned_cards_valuesHard[1]=="K2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="K2_Hard" and turned_cards_valuesHard[1]=="K1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="L1_Hard" and turned_cards_valuesHard[1]=="L2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="L2_Hard" and turned_cards_valuesHard[1]=="L1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="M1_Hard" and turned_cards_valuesHard[1]=="M2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="M2_Hard" and turned_cards_valuesHard[1]=="M1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="N1_Hard" and turned_cards_valuesHard[1]=="N2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="N2_Hard" and turned_cards_valuesHard[1]=="N1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="O1_Hard" and turned_cards_valuesHard[1]=="O2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="O2_Hard" and turned_cards_valuesHard[1]=="O1_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="P1_Hard" and turned_cards_valuesHard[1]=="P2_Hard":
            $ match = True
        if turned_cards_valuesHard[0]=="P2_Hard" and turned_cards_valuesHard[1]=="P1_Hard":
            $ match = True
        if (match==True): 
            show binaryGreen at Position(xpos = 362, xanchor = 0, ypos = 899, yanchor = 0)
            play sound binaryRight
            $renpy.pause (1.5)
            hide binaryGreen
        
        if (match==False):
            show binaryRed at Position(xpos = 97, xanchor = 0, ypos = 899, yanchor = 0)
            play sound binaryWrong
            $renpy.pause (1.75)
            python:
                for i in range (0, len(turned_cards_numbersHard) ):
                    cards_listHard[turned_cards_numbersHard[i]]["c_chosen"] = False
            hide card["[c_value]"] 
            hide binaryRed
        
            # If cards are matched, will check if player has opened all the cards
        if (attempts > 0):
            python: 
                for j in cards_listHard:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryMatch_gameHard")
                renpy.jump ("binaryHardWin_pre")

        if (attempts ==0):
            python: 
                for j in cards_listHard:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryHardLose_pre")
                renpy.jump ("binaryHardWin_pre")
        jump binaryMatch_gameHard
        
label binaryHardWin_pre:
    queue sound binaryWin
    $renpy.pause(1.0)
    if(puzzleGallery):
        jump pg_binaryHardWin
    jump binaryHardWin
    
label binaryHardLose_pre:
    queue sound binaryLose
    $renpy.pause(1.5)
    if(puzzleGallery):
        jump pg_binaryHardLose
    jump binaryHardLose