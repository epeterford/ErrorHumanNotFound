screen binaryMatch:
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("gameLose") ) repeat True
    text str(memo_timer) xalign 0.8 yalign 0.05
    grid 4 2 spacing 100 at Position(xpos=0.45, xanchor =0.0, ypos =0.4, yanchor = 0.0): 
        for card in cards_list:
            button:
#            imagebutton:
#                focus_mask True
                background None
                if card["c_chosen"]:        # shows the face of the card
                    #text card["c_value"]    # will show text
                    add card["c_value"]    # will show image
                    focus_mask card["c_value"]
#                    idle "[c_value]"
                    
                else:                       # shows the back of the card
                    #text "X"                # will show text
                    add "cardBack"                # will show image
                    focus_mask "cardBack"
#                    idle "cardBack"
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
                
init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x
        
    image A1 = "tileFront00.png"
    image A2 = "tileFront0.png"
    image B1 = "tileFront1.png"
    image B2 = "tileFront01.png"
    image C1 = "tileFront10.png"
    image C2 = "tileFront2.png"
    image D1 = "tileFront11.png"
    image D2 = "tileFront3.png"
    image cardBack = "tileBack.png"
    image binaryRed = "LightOff.png"
    image binaryGreen = "LightOn.png"
#    #would need nine images for easy, 17 for medium, 25 for hard

label binaryMatchEasy:
    window hide
    $ quick_menu = False
    $ attempts = 8
    scene bg binary
    $ values_list = ["A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2"]
    $ values_list = cards_shuffle(values_list)
    $ cards_list = []
    python:
        for i in range (0, len(values_list)):
            cards_list.append({"c_number":i, "c_value": values_list[i], "c_chosen":False} )
            
    show screen binaryMatch
    $ memo_timer = 20.0
    label binaryMatch_game:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = 2
        
        label turns_loop:
            if turns_left >0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
                
        $ attempts -=1
        $ can_click = False
        $ match = False
        # If not all the opened cards are matched, will turn them face down after pause
        if turned_cards_values[0]=="A1" and turned_cards_values[1]=="A2":
            $ match = True
        if turned_cards_values[0]=="A2" and turned_cards_values[1]=="A1":
            $ match = True
        if turned_cards_values[0]=="B1" and turned_cards_values[1]=="B2":
            $ match = True
        if turned_cards_values[0]=="B2" and turned_cards_values[1]=="B1":
            $ match = True
        if turned_cards_values[0]=="C1" and turned_cards_values[1]=="C2":
            $ match = True
        if turned_cards_values[0]=="C2" and turned_cards_values[1]=="C1":
            $ match = True
        if turned_cards_values[0]=="D1" and turned_cards_values[1]=="D2":
            $ match = True
        if turned_cards_values[0]=="D2" and turned_cards_values[1]=="D1":
            $ match = True
#        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
        if (match==True): 
            show binaryGreen at Position(xpos = 362, xanchor = 0, ypos = 899, yanchor = 0)
            $renpy.pause (1.0)
            hide binaryGreen
        
        if (match==False):
            show binaryRed at Position(xpos = 97, xanchor = 0, ypos = 899, yanchor = 0)
            $renpy.pause (1.0)
#            $ renpy.pause (1.0) #, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
#            show binaryRed at Position(xpos = 97, xanchor = 0, ypos = 899, yanchor = 0)
#            $renpy.pause (1.0)
            hide binaryRed
        
            # If cards are matched, will check if player has opened all the cards
        if (attempts > 0):
            $ renpy.pause (1.0, hard = True)
            python: 
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryMatch_game")
                renpy.jump ("gameWin")

        if (attempts ==0):
            $ renpy.pause (1.0, hard = True)
            python: 
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("gameLose")
                renpy.jump ("gameWin")
        jump binaryMatch_game
        
label gameWin:
    "You won!"
    hide A1
    hide A2
    hide B1
    hide B2
    hide C1
    hide C2
    hide D1
    hide D2
    jump doAgain
    
label gameLose:
    "You lose."
    hide A1
    hide A2
    hide B1
    hide B2
    hide C1
    hide C2
    hide D1
    hide D2
    jump doAgain
                
