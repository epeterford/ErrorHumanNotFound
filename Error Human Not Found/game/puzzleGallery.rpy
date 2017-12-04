label pg_mainMenu:
    scene bg PG
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "Loop Logic Puzzles.":
            jump pg_llMain
        "Logic Gate Puzzles.":
            jump pg_lgMain
        "Binary Matching.":
            jump pg_binaryMain
        "Grammar Puzzles.":
            jump pg_gramMain
        "Main Menu.":
            jump exitPG
            
label pg_llMain:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "Easy.":
            jump pg_llEasy
        "Medium.":
            jump pg_llMed
        "Hard.":
            jump pg_llHard
        "Back.":
            jump pg_mainMenu
            
label pg_llEasy:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LLEasyHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    menu:
        "Puzzle variation 1.":
            jump loopLogic_easy1
        "Puzzle variation 2.":
            jump loopLogic_easy2
        "Puzzle variation 3.":
            jump loopLogic_easy3
        "Puzzle variation 4.":
            jump loopLogic_easy4
        "Puzzle variation 5.":
            jump loopLogic_easy5
        "Back.":
            jump pg_llMain
        
label pg_llMed:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LLMedHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    $light4Sound = 0
    $light5Sound = 0
    $light6Sound = 0
    $light7Sound = 0
    $charge1_sound1 = 0
    $charge1_sound2 = 0
    $charge2_sound1 = 0
    $charge2_sound2 = 0
    $charge3_sound1 = 0
    $charge3_sound2 = 0
    menu:
        "Puzzle variation 1.":
            jump loopLogic_med1
        "Puzzle variation 2.":
            jump loopLogic_med2
        "Puzzle variation 3.":
            jump loopLogic_med3
        "Puzzle variation 4.":
            jump loopLogic_med4
        "Puzzle variation 5.":
            jump loopLogic_med5
        "Back.":
            jump pg_llMain
    
label pg_llHard:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LLHardHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    $light4Sound = 0
    $light5Sound = 0
    $light6Sound = 0
    $light7Sound = 0
    $charge1_sound1 = 0
    $charge1_sound2 = 0
    $charge2_sound1 = 0
    $charge2_sound2 = 0
    $charge3_sound1 = 0
    $charge3_sound2 = 0
    menu:
        "Puzzle variation 1.":
            jump loopLogic_hard1
        "Puzzle variation 2.":
            jump loopLogic_hard2
        "Puzzle variation 3.":
            jump loopLogic_hard3
        "Puzzle variation 4.":
            jump loopLogic_hard4
        "Puzzle variation 5.":
            jump loopLogic_hard5
        "Back.":
            jump pg_llMain
            
label pg_lgMain:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "Easy.":
            jump pg_lgEasy
        "Medium.":
            jump pg_lgMed
        "Hard.":
            jump pg_lgHard
        "Back.":
            jump pg_mainMenu
            
label pg_lgEasy:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "A series.":
            jump pg_lgEasyA
        "B series.":
            jump pg_lgEasyB
        "C series.":
            jump pg_lgEasyC
        "Back.":
            jump pg_lgMain
            
label pg_lgEasyA:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGEasyHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    menu:
        "Variation A1.":
            jump logicGate_easyA1
        "Varition A2.":
            jump logicGate_easyA2
        "Variation A3.":
            jump logicGate_easyA3
        "Back.":
            jump pg_lgEasy
            
label pg_lgEasyB:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "Variation B1.":
            jump logicGate_easyB1
        "Variation B2.":
            jump logicGate_easyB2
        "Variation B3.":
            jump logicGate_easyB3
        "Back.":
            jump pg_lgEasy
            
label pg_lgEasyC:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "Variation C1.":
            jump logicGate_easyC1
        "Variation C2.":
            jump logicGate_easyC2
        "Variation C3.":
            jump logicGate_easyC3
        "Back.":
            jump pg_lgEasy
            
label pg_lgMed:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "A series.":
            jump pg_lgMedA
        "B series.":
            jump pg_lgMedB
        "C series.":
            jump pg_lgMedC
        "Back.":
            jump pg_lgMain
            
label pg_lgMedA:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGMedHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    menu:
        "Variation A1.":
            jump logicGate_mediumA1
        "Varition A2.":
            jump logicGate_mediumA2
        "Variation A3.":
            jump logicGate_mediumA3
        "Back.":
            jump pg_lgMed
            
label pg_lgMedB:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGMedHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    menu:
        "Variation B1.":
            jump logicGate_mediumB1
        "Variation B2.":
            jump logicGate_mediumB2
        "Variation B3.":
            jump logicGate_mediumB3
        "Back.":
            jump pg_lgMed
            
label pg_lgMedC:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGMedHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    menu:
        "Variation C1.":
            jump logicGate_mediumC1
        "Variation C2.":
            jump logicGate_mediumC2
        "Variation C3.":
            jump logicGate_mediumC3
        "Back.":
            jump pg_lgMed
            
label pg_lgHard:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "A series.":
            jump pg_lgHardA
        "B series.":
            jump pg_lgHardB
        "C series.":
            jump pg_lgHardC
        "Back.":
            jump pg_lgMain
            
label pg_lgHardA:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGHardHints =0
    $slot_name=""
    $gate_name = ""
    $temp_gate = ""
    $ temp_slot = ""
    menu:
        "Variation A1.":
            jump logicGate_hardA1
        "Varition A2.":
            jump logicGate_hardA2
        "Variation A3.":
            jump logicGate_hardA3
        "Back.":
            jump pg_lgHard
            
label pg_lgHardB:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGHardHints =0
    $slot_name=""
    $gate_name = ""
    $temp_gate = ""
    $ temp_slot = ""
    menu:
        "Variation B1.":
            jump logicGate_hardB1
        "Variation B2.":
            jump logicGate_hardB2
        "Variation B3.":
            jump logicGate_hardB3
        "Back.":
            jump pg_lgHard
            
label pg_lgHardC:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGHardHints =0
    $slot_name=""
    $gate_name = ""
    $temp_gate = ""
    $ temp_slot = ""
    menu:
        "Variation C1.":
            jump logicGate_hardC1
        "Variation C2.":
            jump logicGate_hardC2
        "Variation C3.":
            jump logicGate_hardC3
        "Back.":
            jump pg_lgHard
    
label pg_binaryMain:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $binaryHardHints = 0
    $binaryMedHints = 0
    $binaryEasyHints = 0
    menu:
        "Easy.":
            jump binaryMatchEasy
        "Medium.":
            jump binaryMatchMed
        "Hard.":
            jump binaryMatchHard
        "Back.":
            jump pg_mainMenu
    
label pg_gramMain:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    menu:
        "Easy.":
            jump pg_gramEasy
        "Medium.":
            jump pg_gramMed
        "Hard.":
            jump pg_gramHard
        "Back.":
            jump pg_mainMenu
            
label pg_gramEasy:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $LGEasyHints =0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_L_sound =0
    $gramRow1_R_sound = 0
    $gramRow1_C_sound = 0
    $gramRow1_C_sound_wrong1 = 0
    $gramRow1_C_sound_wrong2 = 0
    $gramRow1_C_sound_right1 = 0
    $gramRow1_C_sound_right2 = 0
    $gramRow2_L_sound = 0
    $gramRow2_L_sound_wrong1 = 0
    $gramRow2_L_sound_right1 = 0
    $gramRow2_L_sound_wrong2 = 0
    $gramRow2_L_sound_right2 = 0
    $gramRow2_R_sound = 0
    $gramRow2_R_sound_right1 = 0
    $gramRow2_R_sound_right2 = 0
    $gramRow2_R_sound_wrong1 = 0
    $gramRow2_R_sound_wrong2 = 0
    $gramRow2_C_sound = 0
    $gramRow2_C_sound_wrong1 = 0
    $gramRow2_C_sound_right1 = 0
    $gramRow2_C_sound_wrong2 = 0
    $gramRow2_C_sound_right2 = 0
    $gramRow3_L_sound = 0
    $gramRow3_L_sound_wrong1 = 0
    $gramRow3_L_sound_wrong2 = 0
    $gramRow3_L_sound_right1 = 0
    $gramRow3_L_sound_right2 = 0
    $gramRow3_R_sound = 0
    $gramRow3_R_sound_right1 = 0
    $gramRow3_R_sound_wrong1 = 0
    $gramRow3_R_sound_right2 = 0
    $gramRow3_R_sound_wrong2 = 0
    $gramRow3_C_sound = 0
    $gramRow3_C_sound_right1 = 0
    $gramRow3_C_sound_wrong1 = 0
    $gramRow3_C_sound_right2 = 0
    $gramRow3_C_sound_wrong2 = 0
    menu:
        "Puzzle variation 1.":
            jump eng_gram_e1
        "Puzzle variation 2.":
            jump eng_gram_e2
        "Puzzle variation 3.":
            jump eng_gram_e3
        "Puzzle variation 4.":
            jump eng_gram_e4
        "Puzzle variation 5.":
            jump eng_gram_e5
        "Back.":
            jump pg_gramMain
        
label pg_gramMed:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $gramMedHints =0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_L_sound =0
    $gramRow1_R_sound = 0
    $gramRow1_C_sound = 0
    $gramRow1_C_sound_wrong1 = 0
    $gramRow1_C_sound_wrong2 = 0
    $gramRow1_C_sound_right1 = 0
    $gramRow1_C_sound_right2 = 0
    $gramRow2_L_sound = 0
    $gramRow2_L_sound_wrong1 = 0
    $gramRow2_L_sound_right1 = 0
    $gramRow2_L_sound_wrong2 = 0
    $gramRow2_L_sound_right2 = 0
    $gramRow2_R_sound = 0
    $gramRow2_R_sound_right1 = 0
    $gramRow2_R_sound_right2 = 0
    $gramRow2_R_sound_wrong1 = 0
    $gramRow2_R_sound_wrong2 = 0
    $gramRow2_C_sound = 0
    $gramRow2_C_sound_wrong1 = 0
    $gramRow2_C_sound_right1 = 0
    $gramRow2_C_sound_wrong2 = 0
    $gramRow2_C_sound_right2 = 0
    $gramRow3_L_sound = 0
    $gramRow3_L_sound_wrong1 = 0
    $gramRow3_L_sound_wrong2 = 0
    $gramRow3_L_sound_right1 = 0
    $gramRow3_L_sound_right2 = 0
    $gramRow3_R_sound = 0
    $gramRow3_R_sound_right1 = 0
    $gramRow3_R_sound_wrong1 = 0
    $gramRow3_R_sound_right2 = 0
    $gramRow3_R_sound_wrong2 = 0
    $gramRow3_C_sound = 0
    $gramRow3_C_sound_right1 = 0
    $gramRow3_C_sound_wrong1 = 0
    $gramRow3_C_sound_right2 = 0
    $gramRow3_C_sound_wrong2 = 0
    menu:
        "Puzzle variation 1.":
            jump gram_m1
        "Puzzle variation 2.":
            jump gram_m2
        "Puzzle variation 3.":
            jump gram_m3
        "Puzzle variation 4.":
            jump gram_m4
        "Puzzle variation 5.":
            jump gram_m5
        "Back.":
            jump pg_gramMain
    
label pg_gramHard:
    scene bg PG
    window hide
    $quick_menu = False
    show screen disable_hide
    $gramHardHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_L_sound =0
    $gramRow1_R_sound = 0
    
    $gramRow1_C_sound = 0
    $gramRow1_C_sound_wrong1 = 0
    $gramRow1_C_sound_wrong2 = 0
    $gramRow1_C_sound_right1 = 0
    $gramRow1_C_sound_right2 = 0
    
    $gramRow2_L_sound = 0
    $gramRow2_L_sound_wrong1 = 0
    $gramRow2_L_sound_right1 = 0
    $gramRow2_L_sound_wrong2 = 0
    $gramRow2_L_sound_right2 = 0
    
    $gramRow2_R_sound = 0
    $gramRow2_R_sound_right1 = 0
    $gramRow2_R_sound_right2 = 0
    $gramRow2_R_sound_wrong1 = 0
    $gramRow2_R_sound_wrong2 = 0
    
    $gramRow2_C_sound = 0
    $gramRow2_C_sound_wrong1 = 0
    $gramRow2_C_sound_right1 = 0
    $gramRow2_C_sound_wrong2 = 0
    $gramRow2_C_sound_right2 = 0
    
    $gramRow3_L_sound = 0
    $gramRow3_L_sound_wrong1 = 0
    $gramRow3_L_sound_wrong2 = 0
    $gramRow3_L_sound_right1 = 0
    $gramRow3_L_sound_right2 = 0
    
    $gramRow3_R_sound = 0
    $gramRow3_R_sound_right1 = 0
    $gramRow3_R_sound_wrong1 = 0
    $gramRow3_R_sound_right2 = 0
    $gramRow3_R_sound_wrong2 = 0
    
    $gramRow3_C_sound = 0
    $gramRow3_C_sound_right1 = 0
    $gramRow3_C_sound_wrong1 = 0
    $gramRow3_C_sound_right2 = 0
    $gramRow3_C_sound_wrong2 = 0
    menu:
        "Puzzle variation 1.":
            jump eng_gram_h1
        "Puzzle variation 2.":
            jump eng_gram_h2
        "Puzzle variation 3.":
            jump eng_gram_h3
        "Puzzle variation 4.":
            jump eng_gram_h4
        "Puzzle variation 5.":
            jump eng_gram_h5
        "Back.":
            jump pg_gramMain

label exitPG:
    $puzzleGallery = False
    return