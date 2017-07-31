screen binaryMatch_med:
    grid 4 4 spacing 100 at Position(xpos=0.45, xanchor =0.0, ypos =0.2, yanchor = 0.0): 
        for card in cards_listMed:
            button:
                background None
                if card["c_chosen"]:        # shows the face of the card
                    #text card["c_value"]    # will show text
                    add card["c_value"]    # will show image
                    focus_mask card["c_value"]
                else:                       # shows the back of the card
                    #text "X"                # will show text
                    add "cardBack"                # will show image
                    focus_mask "cardBack"
                action If ( (card["c_chosen"] or not can_clickMed), None, [SetDict(cards_listMed[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
                
init:
#    python:
#        def cards_shuffle(x):
#            renpy.random.shuffle(x)
#            return x
        
    image A1_Med = "tileFront000.png"
    image A2_Med = "tileFront0.png"
    image B1_Med = "tileFront1.png"
    image B2_Med = "tileFront001.png"
    image C1_Med = "tileFront010.png"
    image C2_Med = "tileFront2.png"
    image D1_Med = "tileFront011.png"
    image D2_Med = "tileFront3.png"
    image E1_Med = "tileFront100.png"
    image E2_Med = "tileFront4.png"
    image F1_Med = "tileFront5.png"
    image F2_Med = "tileFront101.png"
    image G1_Med = "tileFront110.png"
    image G2_Med = "tileFront6.png"
    image H1_Med = "tileFront111.png"
    image H2_Med = "tileFront7.png"

label binaryMatchMedium:
    scene bg binary
    window hide
    $ quick_menu = False
    $ attempts = 12
    $ values_listMed = ["A1_Med", "A2_Med", "B1_Med", "B2_Med", "C1_Med", "C2_Med", "D1_Med", "D2_Med", "E1_Med", "E2_Med", "F1_Med", "F2_Med", "G1_Med", "G2_Med", "H1_Med", "H2_Med"]
    $ values_listMed = cards_shuffle(values_listMed)
    $ cards_listMed = []
    python:
        for i in range (0, len(values_listMed)):
            cards_listMed.append({"c_number":i, "c_value": values_listMed[i], "c_chosen":False} )
            
    show screen binaryMatch_med
    
    label binaryMatch_gameMed:
        $ can_clickMed = True
        $ turned_cards_numbersMed = []
        $ turned_cards_valuesMed = []
        $ turns_leftMed = 2
        
        label turns_loopMed:
            if turns_leftMed >0:
                $ result = ui.interact()
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
#        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
        if (match==True): 
            show binaryGreen at Position(xpos = 362, xanchor = 0, ypos = 899, yanchor = 0)
            $renpy.pause (1.0)
            hide binaryGreen
        
        if (match==False):
            $ renpy.pause (1.0) #, hard = True)
            python:
                for i in range (0, len(turned_cards_numbersMed) ):
                    cards_listMed[turned_cards_numbersMed[i]]["c_chosen"] = False
            show binaryRed at Position(xpos = 97, xanchor = 0, ypos = 899, yanchor = 0)
            $renpy.pause (1.0)
            hide binaryRed
        
            # If cards are matched, will check if player has opened all the cards
        if (attempts > 0):
            $ renpy.pause (1.0, hard = True)
            python: 
                for j in cards_listMed:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryMatch_gameMed")
                renpy.jump ("gameWin2")

        if (attempts ==0):
            $ renpy.pause (1.0, hard = True)
            python: 
                for j in cards_listMed:
                    if j["c_chosen"] == False:
                        renpy.jump ("gameLose2")
                renpy.jump ("gameWin2")
        jump binaryMatch_gameMed
        
label gameWin2:
    "You won!"
    hide A1_Med
    hide A2_Med
    hide B1_Med
    hide B2_Med
    hide C1_Med
    hide C2_Med
    hide D1_Med
    hide D2_Med
    hide E1_Med
    hide E2_Med
    hide F1_Med
    hide F2_Med
    hide G1_Med
    hide G2_Med 
    hide H1_Med 
    hide H2_Med
    jump doAgain
    
label gameLose2:
    "You lose."
    hide A1_Med
    hide A2_Med
    hide B1_Med
    hide B2_Med
    hide C1_Med
    hide C2_Med
    hide D1_Med
    hide D2_Med
    hide E1_Med
    hide E2_Med
    hide F1_Med
    hide F2_Med
    hide G1_Med
    hide G2_Med 
    hide H1_Med 
    hide H2_Med
    jump doAgain
                
