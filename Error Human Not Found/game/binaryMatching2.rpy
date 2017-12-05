screen binaryMatch:
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
    grid 4 2 spacing 100 at Position(xpos=0.45, xanchor =0.0, ypos =0.4, yanchor = 0.0): 
        for card in cards_list:
            button:
                background None
                if card["c_chosen"]:        # shows the face of the card
                    add card["c_value"]    # will show image
                    focus_mask card["c_value"]
                else:                       # shows the back of the card
                    add "cardBack"                # will show image
                    focus_mask "cardBack"
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 275
        ypos 720
        focus_mask True
        action Jump("binaryEasyHints")
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
        idle "binaryEasyInstructions.png"
        xpos 0
        ypos 0
    
init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x
        
    image A1 = "tileFront0000.png"
    image A2 = "tileFront0.png"
    image B1 = "tileFront1.png"
    image B2 = "tileFront0001.png"
    image C1 = "tileFront0010.png"
    image C2 = "tileFront2.png"
    image D1 = "tileFront0011.png"
    image D2 = "tileFront3.png"
    image cardBack = "tileBack.png"
    image binaryRed = "LightOff.png"
    image binaryGreen = "LightOn.png"

label binaryMatchEasy:
    $config.skipping=None
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
    label binaryMatch_game:
        $config.skipping=None
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = 2
        
        label turns_loop:
            if turns_left >0:
                $ can_click = True
                $ result = ui.interact()
                $tileFlipSound = renpy.random.randint(0,2)
                if (tileFlipSound==0):
                    play soundP01 tileFlip1
                if (tileFlipSound==1):
                    play soundP01 tileFlip2
                if (tileFlipSound==2):
                    play soundP01 tileFlip3
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
        if (match==True): 
            show binaryGreen at Position(xpos = 362, xanchor = 0, ypos = 899, yanchor = 0) 
            play sound binaryRight
            $renpy.pause (1.0)
            hide binaryGreen
        
        if (match==False):
            show binaryRed at Position(xpos = 97, xanchor = 0, ypos = 899, yanchor = 0)
            play sound binaryWrong
            $renpy.pause (1.0)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
            hide card["[c_value]"] 
            hide binaryRed
        
            # If cards are matched, will check if player has opened all the cards
        if (attempts > 0):
            python: 
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryMatch_game")
                renpy.jump ("binaryEasyWin_pre")

        if (attempts ==0):
            $ renpy.pause (1.0, hard = True)
            python: 
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("binaryEasyLose_pre")
                renpy.jump ("binaryEasyWin_pre")
        jump binaryMatch_game
    
label binaryEasyWin_pre:
    queue sound binaryWin
    $renpy.pause(1.0)
    if(puzzleGallery):
        jump pg_binaryEasyWin
    jump binaryEasyWin
    
label binaryEasyLose_pre:
    queue sound binaryLose
    $renpy.pause(1.5)
    if(puzzleGallery):
        jump pg_binaryEasyLose
    jump binaryEasyLose