screen binaryMatch_med:
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
    grid 4 4 spacing 100 at Position(xpos=0.45, xanchor =0.0, ypos =0.2, yanchor = 0.0): 
        for card in cards_listMed:
            button:
                background None
                if card["c_chosen"]:        # shows the face of the card
                    add card["c_value"]    # will show image
                    focus_mask card["c_value"]
                else:                       # shows the back of the card
                    add "cardBack"                # will show image
                    focus_mask "cardBack"
                action If ( (card["c_chosen"] or not can_clickMed), None, [SetDict(cards_listMed[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 275
        ypos 720
        focus_mask True
        action Jump("binaryMediumHints")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 185
        ypos 795
    text "Attempts" xpos 195 ypos 815 color "#0060db" font "United Kingdom DEMO.otf" size 24
    text ": " xpos 370 ypos 804 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 385 ypos 813 color "#0060db" font "United Kingdom DEMO.otf" size 27
    imagebutton:
        idle "binaryMedInstructions.png"
        xpos 0
        ypos 0
        
init:
    image A1_Med = "tileFront0000.png"
    image A2_Med = "tileFront0.png"
    image B1_Med = "tileFront1.png"
    image B2_Med = "tileFront0001.png"
    image C1_Med = "tileFront0010.png"
    image C2_Med = "tileFront2.png"
    image D1_Med = "tileFront0011.png"
    image D2_Med = "tileFront3.png"
    image E1_Med = "tileFront0100.png"
    image E2_Med = "tileFront4.png"
    image F1_Med = "tileFront5.png"
    image F2_Med = "tileFront0101.png"
    image G1_Med = "tileFront0110.png"
    image G2_Med = "tileFront6.png"
    image H1_Med = "tileFront0111.png"
    image H2_Med = "tileFront7.png"

label binaryMatchMed:
    $config.skipping=None
    scene bg binary
    window hide
    $ quick_menu = False
    $ attempts = 18
    $ values_listMed = ["A1_Med", "A2_Med", "B1_Med", "B2_Med", "C1_Med", "C2_Med", "D1_Med", "D2_Med", "E1_Med", "E2_Med", "F1_Med", "F2_Med", "G1_Med", "G2_Med", "H1_Med", "H2_Med"]
    $ values_listMed = cards_shuffle(values_listMed)
    $ cards_listMed = []
    python:
        for i in range (0, len(values_listMed)):
            cards_listMed.append({"c_number":i, "c_value": values_listMed[i], "c_chosen":False} )
            
    show screen binaryMatch_med
    label binaryMatch_gameMed:
        $config.skipping=None
        $ can_clickMed = True
        $ turned_cards_numbersMed = []
        $ turned_cards_valuesMed = []
        $ turns_leftMed = 2
        
        label turns_loopMed:
            if turns_leftMed >0:
                $ can_clickMed = True
                $ result = ui.interact()
                $tileFlipSound = renpy.random.randint(0,2)
                if (tileFlipSound==0):
                    play soundP01 tileFlip1
                if (tileFlipSound==1):
                    play soundP01 tileFlip2
                if (tileFlipSound==2):
                    play soundP01 tileFlip3
                $ turned_cards_numbersMed.append (cards_listMed[result]["c_number"])
                $ turned_cards_valuesMed.append (cards_listMed[result]["c_value"])
                $ turns_leftMed -= 1
                jump turns_loopMed
                
        $ attempts -=1
        $ can_clickMed = False
        $ match = False
        # If not all the opened cards are matched, will turn them face down after pause
        if turned_cards_valuesMed[0]=="A1_Med" and turned_cards_valuesMed[1]=="A2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="A2_Med" and turned_cards_valuesMed[1]=="A1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="B1_Med" and turned_cards_valuesMed[1]=="B2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="B2_Med" and turned_cards_valuesMed[1]=="B1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="C1_Med" and turned_cards_valuesMed[1]=="C2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="C2_Med" and turned_cards_valuesMed[1]=="C1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="D1_Med" and turned_cards_valuesMed[1]=="D2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="D2_Med" and turned_cards_valuesMed[1]=="D1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="E1_Med" and turned_cards_valuesMed[1]=="E2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="E2_Med" and turned_cards_valuesMed[1]=="E1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="F1_Med" and turned_cards_valuesMed[1]=="F2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="F2_Med" and turned_cards_valuesMed[1]=="F1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="G1_Med" and turned_cards_valuesMed[1]=="G2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="G2_Med" and turned_cards_valuesMed[1]=="G1_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="H1_Med" and turned_cards_valuesMed[1]=="H2_Med":
            $ match = True
        if turned_cards_valuesMed[0]=="H2_Med" and turned_cards_valuesMed[1]=="H1_Med":
            $ match = True
        if (match==True): 
            show binaryGreen at Position(xpos = 362, xanchor = 0, ypos = 899, yanchor = 0)
            play sound binaryRight
            $renpy.pause (1.0)
            hide binaryGreen
        
        if (match==False):
            show binaryRed at Position(xpos = 97, xanchor = 0, ypos = 899, yanchor = 0)
            play sound binaryWrong
            $renpy.pause (1.5)
            python:
                for i in range (0, len(turned_cards_numbersMed) ):
                    cards_listMed[turned_cards_numbersMed[i]]["c_chosen"] = False
            hide card["[c_value]"] 
            hide binaryRed
        
            # If cards are matched, will check if player has opened all the cards
        if (attempts > 0):
            python: 
                for j in cards_listMed:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryMatch_gameMed")
                renpy.jump ("binaryMedWin_pre")

        if (attempts ==0):
            python: 
                for j in cards_listMed:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryMedLose_pre")
                renpy.jump ("binaryMedWin_pre")
        jump binaryMatch_gameMed
        
label binaryMedWin_pre:
    queue sound binaryWin
    $renpy.pause(1.0)
    if(puzzleGallery):
        jump pg_binaryMedWin
    jump binaryMedWin
    
label binaryMedLose_pre:
    queue sound binaryLose
    $renpy.pause(1.5)
    if(puzzleGallery):
        jump pg_binaryMedLose
    jump binaryMedLose
                
