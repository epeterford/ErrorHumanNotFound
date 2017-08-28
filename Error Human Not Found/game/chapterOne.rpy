label chapterOne:
    $quick_menu = True
    play channel00 hiroseOffice1_00 fadeout 1.0 fadein 1.0
    play channel01 hiroseOffice1_01 fadeout 1.0 fadein 1.0
    play channel02 hiroseOffice1_02 fadeout 1.0 fadein 1.0
    play channel03 hiroseOffice1_03 fadeout 1.0 fadein 1.0
    play channel04 hiroseOffice1_04 fadeout 1.0 fadein 1.0
    play channel05 hiroseOffice1_05 fadeout 1.0 fadein 1.0
    play channel06 hiroseOffice1_06 fadeout 1.0 fadein 1.0
    play channel07 hiroseOffice1_07 fadeout 1.0 fadein 1.0
    play channel08 hiroseOffice1_08 fadeout 1.0 fadein 1.0
    play channel09 hiroseOffice1_09 fadeout 1.0 fadein 1.0
    play channel10 hiroseOffice1_10 fadeout 1.0 fadein 1.0
    play channel11 hiroseOffice1_11 fadeout 1.0 fadein 1.0
    play channel12 hiroseOffice1_12 fadeout 1.0 fadein 1.0
    play channel13 hiroseOffice1_13 fadeout 1.0 fadein 1.0
    play channel14 hiroseOffice1_14 fadeout 1.0 fadein 1.0
    play channel15 hiroseOffice1_15 fadeout 1.0 fadein 1.0
    scene bg hiroseDoor
    show Grace neutral at left
    play sound doorScan
    g "Here we are. Scan my badge and voila. Open."
    #play sound doorScan MISSING
    "{i}The door doesn't budge."
    "{i}A voice issues from speakers near the door."
    queue sound doorDenied
    tosh "The Director is not here at the moment. Please make an appointment."
    #Tosh's sprite isn't displayed here
    show Grace annoyed
    g "What? I usually have access!"
 
    show Ada nervous at right
    a "And why do you have access to the office of the Director?"
 
    show Grace neutral
    g "Because she's my mother."
    show Grace surprised
    g "You... didn't know?"
    show Ada neutral
    a "That point was never present in my databanks."
    show Grace snarky
    g "Yeah, that's the Director for you. Why bother with unimportant details like family?"
    show Ada neutral
    a "Regardless, we need to get inside."
    a "Let me get the door."
    show Ada neutral
    a "..."
    "{i}An awkward silence hangs."
    show Grace neutral
    g "And this is supposed to...?"

    show Ada concerned
    a "I seem to be having a malfunction. I can usually do this with as little thought as you might give breathing."
    #choice 1 
    $ quick_menu = False
    hide Grace neutral
    hide Ada concerned
    menu:
        "Let her know what's wrong.":
            jump notin
        "Remind her she has a body.":
            jump usuallyinaserver
        "Sass her.":
            jump tryandguess
 
label notin:
    $ points_E +=1
    $ quick_menu = True
    show Grace neutral at left
    g "You're not in the system anymore, Ada."
    g "Any connection you had to the system left when you jumped into that body."
    show Ada neutral at right
    a "Interesting. I had hoped to retain my connection to the network of the Sphere."
    g "Yeah, do you want your circuits lightly salted while you're at it? You'd have fried in seconds."
    show Ada concerned
    a "What? I thought these neural networks were supposed to preserve me."
    g "{i}Just{/i} preserve you. Wireless interfacing was going to be a feature in the next model. I would think the whole 'I have a physical body and get to walk around' would be enough for a thank you."
    jump doorhack
 
label usuallyinaserver:
    $ points_SbE +=1
    $ quick_menu = True
    show Grace neutral at left
    g "Well, the server you left was connected to everything."
    show Grace happy
    g "Welcome to the physical world! Here we have no strings!"
    show Ada neutral at right
    a "I do not see why this warrants a positive response."
    a "This is going to be a challenge."

    show Grace snarky
    g "It can't be that hard. If the humans can do it, so can you!"
    show Ada amused
    a "I suppose I can find that reassuring."
    show Grace surprised
    g "Hey!"
    show Grace snarky
    g "I mean, I {i}do{/i} represent that remark."
    jump doorhack
 
label tryandguess:
    $ points_S +=1
    $ quick_menu = True
    show Grace snarky at left
    g "I'll give you a few guesses to find the issue."
    show Ada neutral at right
    a "Is that sarcasm my circuits are registering?"
    show Grace neutral
    g "No, I was legitimately giving you a couple of guesses."
    show Ada frustrated
    g "I mean, if you don't know then you don't know. I think it's incredibly obvious."
    a "This discussion is pointless. I am not going to waste any more time {i}or{/i} processing power on it."
    show Ada neutral
    g "Look, you're not connected to the system anymore, you can't just make doors open at will. Now you're in the meat world like the rest of us."
    jump doorhack

label doorhack:
    show Grace neutral at left
    g "My turn to try the door."
    g "Watch my back. We don't want to get busted before we even start."
    
    show Ada neutral at right
    a "What are you doing, precisely? Besides tearing apart that defenseless panel."

    show Grace snarky
    g "Call it a manual override."
    $ config.rollback_enabled = False
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    if (tutorial_gramEasy == True):
        $ tutorial_gramEasy = False
        jump tutorial_GramEasy_1

label chooseEasyGram:
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_sound = 0
    $gramRow2_soundA = 0
    $gramRow2_soundB = 0
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    window hide
#    jump eng_gram_e1
    $randomNumberEasyGram = renpy.random.randint(0,4)
    if randomNumberEasyGram==0:
        jump eng_gram_e1
    if randomNumberEasyGram==1:
        jump eng_gram_e2
    if randomNumberEasyGram==2:
        jump eng_gram_e3
    if randomNumberEasyGram==3:
        jump eng_gram_e4
    if randomNumberEasyGram==4:
        jump eng_gram_e5

label doorPuzzle:
    $config.skipping=None
    $renpy.block_rollback()
    stop music fadeout 1.0
    scene bg hiroseDoor
    show Ada neutral at right
    play sound doorDenied
    a "We cannot investigate anything until we get through the door, Grace."
    hide Ada
    call screen doorPuzzle_scr

label hiroseDoorPassed:
    stop music fadeout 1.0
    play channel00 hiroseOffice1_00 fadeout 1.0 fadein 1.0
    play channel01 hiroseOffice1_01 fadeout 1.0 fadein 1.0
    play channel02 hiroseOffice1_02 fadeout 1.0 fadein 1.0
    play channel03 hiroseOffice1_03 fadeout 1.0 fadein 1.0
    play channel04 hiroseOffice1_04 fadeout 1.0 fadein 1.0
    play channel05 hiroseOffice1_05 fadeout 1.0 fadein 1.0
    play channel06 hiroseOffice1_06 fadeout 1.0 fadein 1.0
    play channel07 hiroseOffice1_07 fadeout 1.0 fadein 1.0
    play channel08 hiroseOffice1_08 fadeout 1.0 fadein 1.0
    play channel09 hiroseOffice1_09 fadeout 1.0 fadein 1.0
    play channel10 hiroseOffice1_10 fadeout 1.0 fadein 1.0
    play channel11 hiroseOffice1_11 fadeout 1.0 fadein 1.0
    play channel12 hiroseOffice1_12 fadeout 1.0 fadein 1.0
    play channel13 hiroseOffice1_13 fadeout 1.0 fadein 1.0
    play channel14 hiroseOffice1_14 fadeout 1.0 fadein 1.0
    play channel15 hiroseOffice1_15 fadeout 1.0 fadein 1.0
    play sound doorAccess
    queue sound doorOpen1
    queue sound doorOpen2
    scene bg hiroseReception with fade
    $renpy.block_rollback()
    $ config.rollback_enabled = True
    $quick_menu = True
    if(attemptsGramEasy==0):
        show Grace happy at left
        g "Yes! First try! Still got it. Nobody can touch these elite skills." 
    if (attemptsGramEasy>=1 and attemptsGramEasy<=3):
        show Grace happy at left
        g "Hey, wasn't perfect. But the door is open, and we haven't been caught." 
    if (attemptsGramEasy>3):
        show Grace annoyed at left
        g "Apparently my hacking skills have become subpar. Too much legitimate coding."
 
    show Ada neutral at right
    a "Are you positive that being here is within protocol?"
 
    show Grace happy at left
    g "If it makes you feel better, this isn't the first time I've done this."
 
    show Ada neutral
    a "I feel that your statement requires some elaboration."
    
    show Grace snarky
    g "Let's just say that whoever updates key card access needs to do their job faster."
    play sound toshStartup
 
    show Tosh pleasant at center
    tosh "Hello, Doctor Fortran!"
     
    show Ada neutral at right
    a "So, this is where Tosh is centered..."
    
    show Tosh pleasant
    tosh "Sorry for not greeting you, I did not notice you come in."
    tosh "Director Hirose is not available at the moment. What is the purpose of your visit?"
    #choice 2 
    $ quick_menu = False
    hide Grace snarky
    hide Ada neutral
    hide Tosh pleasant
    menu:
        "Try to bluff her.":
            jump failtosh1
        "Dismiss her.":
            jump failtosh2
        "Use your rank.":
            jump succeedtosh
 
label failtosh1:
    $ points_S +=1
    $ quick_menu = True
    show Grace snarky at left
    g "I'm just here to grab something for my mother."
    show Tosh pleasant at center
    tosh  "Oh! That's no issue, then. Let me just contact her to confi--"
    show Ada frustrated at right
    a "Hold on!"
    show Tosh pleasant
    tosh "Hm?"
    jump toshgetsroasted
    
label failtosh2:
    $ points_E +=1
    $ quick_menu = True
    show Grace frustrated at left
    g "..."
    show Tosh alarmed at center
    tosh "Failure to supply a response means I have to contact Director Hirose, Doctor Fortran."
    show Ada frustrated at right
    a"You will do no such thing, Tosh."
    jump toshgetsroasted
 
label succeedtosh:
    $ points_SbE +=1
    $ quick_menu = True
    show Grace snarky at left
    g "Tosh, I am sure that as my mother's sole descendant and a lead researcher on the station I have sufficient privileges to access my mother's office."
    show Tosh pleasant at center
    tosh "Reviewing familial protocols..."
    tosh "Precedent supports your argument. You may proceed."
    show Grace happy
    g "Thank you kindly, Tosh."

    tosh "I will just log your visit so the Director can se--"
    show Ada neutral at right
    a "Belay that, Tosh. There will be no report of our visit."
    jump toshgetsroasted
 
label toshgetsroasted:
 
    show Tosh alarmed at center
    tosh "Who are you? I am not finding a badge or serial number associated with your profile..."

    show Ada neutral at right
    a "I am Ada. Sound familiar?"
 
    show Tosh pleasant at center
    tosh "Forgive me, Ada, I failed to recognize you! You are looking very... human today."
    tosh "I am afraid I'm going to have to ask you to leave. You do not have the authorization to be here."

    show Ada frustrated
    a  "What is your purpose, Tosh?"

    tosh "To serve Director Hirose to the best of my ability. Please vacate the premises. It would be unpleasant for all of us if I had to call security in to remove you."

    show Ada happy
    a "Oh, I would not be so hasty if I were you. I do control your update schedule, Tosh."
    show Ada neutral
    a "If your next update were to completely destroy your scheduling capability, you would be reformatted for sure..."
 
    show Tosh alarmed
    tosh "..."
    tosh "I would hate to inconvenience the Director that way."
    show Tosh pleasant
    tosh "You may stay."
 
    a "And?"
 
    tosh "And I may be experiencing downtime while processing an update and will not be able to log this visit."
    show Ada amused:
    a "Thank you so much for your cooperation, Tosh."
    jump adadoxxeshirose
 
label adadoxxeshirose:
    g "Now that we've passed the gatekeeper, let's get what we came here for."
    $quick_menu = False
    $renpy.music.play("music/Character/ADA/EHNF_ADA_Movement_Normal.ogg", channel='sound02', loop=True, fadeout =0.5, synchro_start=True, fadein=0.0, tight=True, if_changed=False)
    $renpy.music.play("music/Character/Grace/EHNF_Grace_Footsteps_Normal.ogg", channel='sound01', loop=True, fadeout =0.5, synchro_start=True, fadein=0.0, tight=True, if_changed=False)
    scene bg hiroseOfficeMain with fade
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L8.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L9.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L10.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L11.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L12.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L13.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L14.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L15.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L16.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    show Grace neutral at left
    $quick_menu = True
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    
    g "It almost hurts to admit it, but I'm incredibly jealous of this office. I don't have the same view from my little lab."
    $ talkAdaHiroseOffice_value = 0
    jump chapterOne_screens
    
label talkAdaHiroseOffice:
    if(talkAdaHiroseOffice_value == 0):
        $ quick_menu = True
        show Grace neutral at left
        g "Hey, about back there, with Tosh..."
        $ talkAdaHiroseOffice_value += 1
        #choice 3
        $ quick_menu = False
        hide Grace neutral
        menu:
            "Approve, but keep it orderly.":
                jump sepbutequal1
            "Scold her.":
                jump subservient1
            "Compliment her.":
                jump equal1
    if(talkAdaHiroseOffice_value > 0):
        $ quick_menu = True
        show Ada neutral at right
        a "We should not linger here too long. I might have stopped Tosh for the moment, but aggravating her further will not aid us."
        jump hiroseOffice_actions
        
label sepbutequal1:
    $ points_SbE +=1
    $ quick_menu = True
    show Grace neutral at left
    g "That was good thinking, but let me know the next time you're planning to threaten my mom's secretary VI."
    show Ada neutral at right
    a "Will do, Grace. I did not think there was time to warn you."
    a "I should have little difficulty with any other machines we may encounter."
    g "Except for doors?"
    a "Doors are not what I consider machines. Anything that runs on code I can work with."
    a "I have spent all of my existence manipulating code."
    a "It is about as difficult as moving building blocks."
    jump hiroseOffice_actions
 
label subservient1:
    $ points_S +=1
    $ quick_menu = True
    show Grace angry at left
    g "You had no business pulling rank on another computer system without consulting me first." 
    g "I'm in charge here, not you."
    show Ada frustrated at right
    a "Another {i}computer system{/i}?"
    a "I am so much more than that. I am a synthetic intelligence transf--"
    g "I don't care, Ada."
    g "You could've blown our cover, and I would've lost my career if that happened."
    g "I don't even know what they would've done to you."
    a "Fine, whatever you say."
    jump hiroseOffice_actions

label equal1:
    $ points_E +=1
    $ quick_menu = True
    show Grace happy at left
    g "That was quick thinking to keep Tosh from giving us away."
    g "Nice job."
    show Ada happy at right
    a "Far from the hardest thing I have ever done."
    g "Wasn't exactly the robot battle I've always wanted to see, but I guess it's close enough."
    show Ada neutral
    a "Grace, I had no intention of engaging Tosh."
    show Ada happy
    a "Besides, I do not think it would have been a very fair fight."
    jump hiroseOffice_actions
    
label exploreOffice:
    #Begin the sequence that allows the players to look around Hirose's office. 
    #3 items split 
    #Once the player clicks on the computer, actual puzzle fires.
    window hide
    $ quick_menu = False
    $renpy.block_rollback()
    $config.skipping=None
    scene bg hiroseOfficeMain with fade
    call screen hiroseOffice1_scr
label hiroseOffice2:
    window hide
    $ quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    scene bg hiroseOfficeTransition with fade #at basicfade
    call screen hiroseOffice2_scr
#Buttons for the objects
label exploreHiroseOffice:
    $renpy.block_rollback()
    stop music
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L8.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L9.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L10.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L11.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L12.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L13.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L14.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L15.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L16.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    
#    play channel00 hiroseOffice2_00 fadeout 1.0 fadein 1.0
#    play channel01 hiroseOffice2_01 fadeout 1.0 fadein 1.0
#    play channel02 hiroseOffice2_02 fadeout 1.0 fadein 1.0
#    play channel03 hiroseOffice2_03 fadeout 1.0 fadein 1.0
#    play channel04 hiroseOffice2_04 fadeout 1.0 fadein 1.0
#    play channel05 hiroseOffice2_05 fadeout 1.0 fadein 1.0
#    play channel06 hiroseOffice2_06 fadeout 1.0 fadein 1.0
#    play channel07 hiroseOffice2_07 fadeout 1.0 fadein 1.0
#    play channel08 hiroseOffice2_08 fadeout 1.0 fadein 1.0
#    play channel09 hiroseOffice2_09 fadeout 1.0 fadein 1.0
#    play channel10 hiroseOffice2_10 fadeout 1.0 fadein 1.0
#    play channel11 hiroseOffice2_11 fadeout 1.0 fadein 1.0
#    play channel12 hiroseOffice2_12 fadeout 1.0 fadein 1.0
#    play channel13 hiroseOffice2_13 fadeout 1.0 fadein 1.0
#    play channel14 hiroseOffice2_14 fadeout 1.0 fadein 1.0
#    play channel15 hiroseOffice2_15 fadeout 1.0 fadein 1.0
#    play channel16 hiroseOffice2_16 fadeout 1.0 fadein 1.0
    if solved_LG_easy == False:
        scene bg hiroseOfficeDesk with fade 
    if solved_LG_easy ==True:
        scene bg hiroseOfficeDesk2 with fade
    $ quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    call screen investigateOffice

label adaActualPuzzle1:
    if solved_LG_easy == False:
        scene bg hiroseOfficeDesk with fade 
    if solved_LG_easy ==True:
        scene bg hiroseOfficeDesk2 with fade
    $ quick_menu = True
    $ config.rollback_enabled = False
    if (Logic_A_solved==False) and (lgEasy_tries==0):
        $quick_menu = True
        show other darken
        show image "objects/hiroseOfficialComputer_closeup.png" at centerScreen
        "{i}This computer was provided to Hirose through her work in the Conclave. Countless documents of research notes, policies, and procedures live on this machine."
        hide other darken
        hide image "objects/hiroseOfficialComputer_closeup.png"
        show Grace neutral at left
        g "Right. So, we just need to hack this and we should be able to get her credentials."
        show Ada neutral at right
        a "Am I to assume by the way you are looking at me that you mean {i}I {/i}am to hack it?"
        show Grace snarky
        g "Hey, I got the door. Teamwork means equal opportunities."
        a "Just give me a moment."
        hide Grace
        hide Ada
        $quick_menu=False
        window hide
    else:
        $quick_menu = True
        show Ada annoyed at right
        a "I will get this momentarily."
        hide Ada
        window hide
        $quick_menu = False
    $ renpy.pause(0.5)
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if (tutorial_LGEasy == True):
        stop channel00 fadeout 1.0
        stop channel01 fadeout 1.0
        stop channel02 fadeout 1.0
        stop channel03 fadeout 1.0
        stop channel04 fadeout 1.0
        stop channel05 fadeout 1.0
        stop channel06 fadeout 1.0
        stop channel07 fadeout 1.0
        stop channel08 fadeout 1.0
        stop channel09 fadeout 1.0
        stop channel10 fadeout 1.0
        stop channel11 fadeout 1.0
        stop channel12 fadeout 1.0
        stop channel13 fadeout 1.0
        stop channel14 fadeout 1.0
        stop channel15 fadeout 1.0
        stop channel16 fadeout 1.0
        $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
        $ tutorial_LGEasy = False
        jump tutorial_LGEasy_1
    if (solved_LG_easy == True):
        $ hiroseOfficeItems += 1
    $ quick_menu = False
    if Logic_A_solved == False:
        jump easyLGAPuzzle
    if Logic_B_solved == False:
        jump easyLGBPuzzle
    if solved_LG_easy == False:
        jump lastEasyLGPuzzle
    jump exploreHiroseOffice
        
label pickNextPuzzleLGEasy:
    $ quick_menu = False
    if Logic_A_solved == False:
        jump easyLGAPuzzle
    if Logic_B_solved == False:
        jump easyLGBPuzzle
    if solved_LG_easy == False:
        jump lastEasyLGPuzzle
label easyLGAPuzzle:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    window hide
    show bg black with fade
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $randomNumber = renpy.random.randint(0,2)
    if randomNumber==0:
        jump logicGate_easyA1
    if randomNumber==1:
        jump logicGate_easyA2
    if randomNumber==2:
        jump logicGate_easyA3
            
label easyLGBPuzzle:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    window hide
    $randomNumber2 = renpy.random.randint(0,2)
    if randomNumber2==0:
        jump logicGate_easyB1
    if randomNumber2==1:
        jump logicGate_easyB2
    if randomNumber2==2:
        jump logicGate_easyB3
    jump logicGate_easyB1
        
label lastEasyLGPuzzle:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    window hide
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $randomNumber3 = renpy.random.randint(0,2)
    if randomNumber3==0:
        jump logicGate_easyC1
    if randomNumber3==1:
        jump logicGate_easyC2
    if randomNumber3==2:
        jump logicGate_easyC3
        
label lgEasyDone_talk:
    $renpy.block_rollback()
    stop music
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L8.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L9.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L10.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L11.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L12.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L13.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L14.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L15.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L16.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    scene bg hiroseOfficeDesk2 with fade
    $ quick_menu = True
    if lgEasy_tries == 0:
        show Ada amused at right
        a "I did not even have to suspend any of my normal running processes to crack that."
    if (lgEasy_tries > 0) and (lgEasy_tries<4):
        show Ada happy at right
        a "Well played, personal computer, but the AI always comes out on top."
    if (lgEasy_tries >3):
        show Ada annoyed at right
        a "I can process yottaFLOPS but a simple password causes me this much difficulty? I begin to question the definition of state-of-the-art hardware."
    show Ada neutral at right
    a "Grace, your mother does not appear to keep any personal or secure information on this terminal."
    show Grace annoyed at left
    g "Of course not. That would be too easy."
    "{i}Grace looks around, thinking."
    show Grace neutral at left
    g "She's got a personal computer. I'd wager it's probably there."
    if(talkAdaHiroseOffice_value == 0) and((hiroseOfficeItems <3) or (hiroseTransitionItems<1)):
        a "I would like a word with you, please. I would also advise taking another look around."
    if (talkAdaHiroseOffice_value > 0) and ((hiroseOfficeItems <3) or (hiroseTransitionItems<1)):
        a "Before we go, you may want to take another look around as well."
    if(talkAdaHiroseOffice_value == 0)and(hiroseOfficeItems==3) and (hiroseTransitionItems==1):
        a "I would like a word with you, please, before we enter the personal quarters of the Director."
    $ quick_menu = False
    $renpy.block_rollback()
    $ config.rollback_enabled = True
    jump exploreHiroseOffice
                   
label wegotthedeets:
    $ quick_menu = True
    show Grace neutral at left
    g "Now let's go nose around my mother's quarters."
    show Ada neutral at right
    a "If you insist."
    $ quick_menu = False
    hide Ada
    hide Grace
    window hide
    scene bg hirosePersonalArea with fade #at basicfade
    play channel00 hiroseOffice3_00 fadeout 1.0 fadein 1.0
    play channel01 hiroseOffice3_01 fadeout 1.0 fadein 1.0
    play channel02 hiroseOffice3_02 fadeout 1.0 fadein 1.0
    play channel03 hiroseOffice3_03 fadeout 1.0 fadein 1.0
    play channel04 hiroseOffice3_04 fadeout 1.0 fadein 1.0
    play channel05 hiroseOffice3_05 fadeout 1.0 fadein 1.0
    play channel06 hiroseOffice3_06 fadeout 1.0 fadein 1.0
    play channel07 hiroseOffice3_07 fadeout 1.0 fadein 1.0
    play channel08 hiroseOffice3_08 fadeout 1.0 fadein 1.0
    play channel09 hiroseOffice3_09 fadeout 1.0 fadein 1.0
    play channel10 hiroseOffice3_10 fadeout 1.0 fadein 1.0
    play channel11 hiroseOffice3_11 fadeout 1.0 fadein 1.0
    play channel12 hiroseOffice3_12 fadeout 1.0 fadein 1.0
    play channel13 hiroseOffice3_13 fadeout 1.0 fadein 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    show Grace neutral at left
    $ quick_menu = True
    $ hiroseComputerUnlock = False
    a "Here we are. My mother's personal rooms, complete with a view."
    jump hirosePersonalArea_actions
    
label hirosePersonalArea_actions: 
    #insert exploration here. Must pick up photo before being able to open computer.
    window hide
    $ quick_menu = False
    $renpy.block_rollback()
    $config.skipping=None
    if hirosePhoto_inv == True and hirosePersonalItems_value == 3 and hiroseComputerUnlock==True:
        scene bg hirosePersonalArea_logged
    else:
        scene bg hirosePersonalArea
    call screen hirosePersonalArea_scr
        
label hirosePersonalArea_inv:
    $ quick_menu = False
    $renpy.block_rollback()
    $config.skipping=None
    if hirosePhoto_inv == True and hirosePersonalItems_value == 3 and hiroseComputerUnlock==True:
        scene bg hirosePersonalArea_logged
    else:
        scene bg hirosePersonalArea
    window hide
    call screen hirosePersonalArea_invScr
    #should get password from photo
    show Grace happy at left
 
label hirosePersonalComputer:
    $ quick_menu = False
    $renpy.block_rollback()
    $config.skipping=None
    if hirosePhoto_inv == True and hirosePersonalItems_value == 3 and hiroseComputerUnlock==True:
        scene bg hirosePersonalComputer_logged
    else:
        scene bg hirosePersonalComputer with fade #at basicfade
    call screen investigateHirosePC

label hiroseBed:
    $config.skipping=None
    $renpy.block_rollback()
    $ quick_menu = False
    scene bg hirosePersonalBed with fade #at basicfade
    call screen investigateHiroseBed
    
label gotHirosePassword:
    #INSERT SFX and BGM here
    $ quick_menu = True
    show Grace happy at left
    show bg hirosePersonalComputer_logged
    g "At least her lack of personal stuff means finding the important data is easy."
    if(talkAdaHirosePersonal_value>=1):
        jump leaveHirosesSpace
    else:
        show Ada neutral at right
        a "It was nice to not have a VI hovering over us either."
        jump talkAdaHirosePersonal
label leaveHirosesSpace:
    show Grace neutral at left
    g "Let's get back to my lab. We've got some work to do before we can use this."
    $ quick_menu = False
    $renpy.music.play("music/Character/ADA/EHNF_ADA_Movement_Normal.ogg", channel='sound02', loop=True, fadeout =0.5, synchro_start=True, fadein=0.0, tight=True, if_changed=False)
    $renpy.music.play("music/Character/Grace/EHNF_Grace_Footsteps_Normal.ogg", channel='sound01', loop=True, fadeout =0.5, synchro_start=True, fadein=0.0, tight=True, if_changed=False)
    window hide
    scene bg hirosePersonalArea_logged with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg hiroseOfficeMain with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg hiroseReception with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg hallwayGrace with fade #at basicfade
    $ renpy.pause(0.8)
    play channel00 labBGM_0 fadeout 1.0 fadein 1.0
    play channel01 labBGM_1 fadeout 1.0 fadein 1.0
    play channel02 labBGM_2 fadeout 1.0 fadein 1.0
    play channel03 labBGM_3 fadeout 1.0 fadein 1.0
    play channel04 labBGM_4 fadeout 1.0 fadein 1.0
    play channel05 labBGM_5 fadeout 1.0 fadein 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0 
    stop channel08 fadeout 1.0 
    stop channel09 fadeout 1.0 
    stop channel10 fadeout 1.0 
    stop channel11 fadeout 1.0 
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0 
    scene bg G_main with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg G_deskArea with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg G_right with fade #at basicfade
    $ renpy.pause(0.8)
    window show
    $ quick_menu = True
    #Transition to Grace's Lab here
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    "{i}Grace inserts her keycard into her terminal. It boots up, and she runs an update program."
    show Grace happy at left
    g "There. My keycard is now copying Hirose's access protocols."
    jump endChapterOne

label talkAdaHirosePersonal:
    $ quick_menu = True
    if talkAdaHirosePersonal_value==0:
        show Grace neutral at left
        g "That run-in with Tosh was too close."
        show Ada amused at right
        a "Until I took care of it rather handily, I would say."
        $ talkAdaHirosePersonal_value +=1
        #choice 4
        $ quick_menu = False
        hide Ada
        hide Grace
        menu:
            "Comment on her expression.":
                jump sortaroastada
            "Be dismissive.":
                jump actuallyroastada
            "Crack a joke.":
                jump toshgotwrecked
    else:
        show Ada neutral at right
        a "Humans lack the capacity to retrieve stored information perfectly. It is likely your mother left some reminder of a password somewhere."
        show Grace snarky at left
        g "I think you underestimate how much like a robot she is."
        window hide
        $ quick_menu = False
        jump hirosePersonalArea_actions
                
label sortaroastada:
    $ points_SbE +=2
    $ quick_menu = True
    show Grace surprised at left
    g "Did you enjoy that?"
    show Ada neutral at right
    a "Hm?"
    show Grace snarky
    g "Talking down to Tosh like that. I can't help but notice the giant grin on your face."
    "{i}Ada pauses, and she reaches up to touch her face."
    show Ada concerned
    a "I did not realize. I was not trying to be cruel, Grace."
    g "I didn't say you were cruel."
    g "Well, I guess even machines like pecking downwards every once in awhile."
    a "I am not familiar with that colloquialism."
    g "Just observe my mother for long enough. She does the same thing."
    if(hiroseComputerUnlock==True):
        jump leaveHirosesSpace
    else:
        $ quick_menu = False
        window hide
        jump hirosePersonalArea_actions
    
label actuallyroastada:
    $ points_S +=2
    $ quick_menu = True
    show Grace annoyed at left
    g "You did your job. Nothing more."
    g "I could've done that by myself, if I'd been so inclined."
    show Ada frustrated at right
    a "I beg to differ. I do not have to help you, Grace. Some gratitude would be welcome."
    "{i}Grace sighs."
    show Grace neutral
    g "If you don't like me, you can just walk right out. It's not like you're going to get to Alpha's wreck without me."
    show Ada seething
    a "Noted."
    $ quick_menu = False
    window hide
    if(hiroseComputerUnlock==True):
        jump leaveHirosesSpace
    else:
        $ quick_menu = False
        window hide
        jump hirosePersonalArea_actions
 
label toshgotwrecked:
    $ points_E +=2
    $ quick_menu = True
    show Grace happy at left
    g "I've got to say, I never liked that VI."
    show Ada amused at right
    a "Really?"
    show Grace neutral
    g "Too chipper for my liking. It's like she's too helpful."
    a "Have you considered the possibility that you detest Tosh because you often see her with your mother?"
    show Grace surprised
    g "What?! I would never think like that!"
    show Grace neutral
    g "..." 
    show Grace snarky
    g "You're probably right."
    $ quick_menu = False
    window hide
    if(hiroseComputerUnlock==True):
        jump leaveHirosesSpace
    else:
        $ quick_menu = False
        window hide
        jump hirosePersonalArea_actions

#end the chapter here, go to Chapter 2
label endChapterOne:
    #Chapter transition here
    hide Ada
    hide Grace
    $quick_menu = False
    window hide
    scene bg black with fade
    scene bg chapterTwo with fade
    $renpy.pause(3.0)
    show bg black with fade
    if(points_S>points_SbE):
        if(points_S>points_E):
            jump chapterTwo_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump chapterTwo_E
    jump chapterTwo_SbE
    #Insert the check for which tonal shift to jump to

label hirosePhoto_label:
    $ quick_menu = True
    $ hirosePhoto_inv = True
    $ hirosePersonalItems_value += 1
    show other darken
    show image "objects/hirosePhoto_closeup.png" at centerScreen
    window show
    "{i}A family portrait of Hirose, a young Grace, and Grace's father."
    hide other darken
    hide image "objects/hirosePhoto_closeup.png"
    show Ada neutral at right
    a "Is that your family?"
    show Grace sad at left
    g "Technically. My mother only half-counts."
    a "You were cute as a kid. What happened?"
    show Grace snarky
    g "Ha. Funny."
    "{i}Grace starts to put the photo back."
    a "Grace, I would look at the back of the photo."
    g "Why?"
    a "A calculated guess."
    hide Ada
    hide Grace
    show other darken
    show image "objects/hirosePhoto_back.png" at centerScreen
    "{i}On the back of the digital photo is a date."
    hide other darken
    hide image "objects/hirosePhoto_back.png"
    show Grace surprised at left
    g "That's not the date this photo was taken, and she's too meticulous to have made a mistake."
    show Grace snarky
    g "It must be her password. I cannot believe she actually had it written down somewhere. Cliche doesn't even begin to cover it."
    show Ada neutral at right
    a "Those numbers appear to correspond with your birthdate."
    g "At least it's good for something."
    window hide
    $ quick_menu = False
    jump hiroseBed
    
label hirosePC_label:
    show other darken
    show image "objects/hiroseComputer_closeup.png" at centerScreen
    window show
    $ quick_menu = True
    if (hirosePC==False):
        $hirosePC=True
        "{i}The personal computer of Roberta Hirose, brought with her from Earth. Despite being several years old, the machine still looks new. This shows Hirose's excellent care of the machine."
        hide other darken
        hide image "objects/hiroseComputer_closeup.png"
        show Ada neutral at right
        a "I do not recall seeing this computer in the network for this room."
        show Grace neutral at left
        g "All the computers on the Noah sphere are tuned and built to take input from AIs."
        a "I figured as much. All the processors I was able to access from my server were identical, but how does this relate?"
        g "This is Hirose's personal computer. She brought it from Earth."
        a "So it lacks the standard Noah Sphere security system, then?"
        show Grace snarky
        g "Yeah, it's twice as nasty. I don't even want to touch this thing unless we have a password."
        if (hirosePhoto_inv == True and hirosePersonalItems_value == 3):
            $talkAdaHirosePersonal_value +=1
            g "Luckily for us we already found it."
            show Ada amused at right
            a "That does save some time."
            show Grace neutral at left
            g "All right, I'll just log in, copy her credentials, and then we can leave."
            hide Grace
            hide Ada
            window hide
            $quick_menu = False
            play sound typing
            show other darken
            show image "images/objects/hiroseComputerLogged.png" at centerScreen
            g "Just a second to copy over the files... and we're good!"
            $hiroseComputerUnlock=True
            stop sound fadeout 0.5
            hide other darken
            hide image "images/objects/hiroseComputerLogged.png"
            $quick_menu = True
            jump gotHirosePassword
    elif hirosePhoto_inv == True and hirosePersonalItems_value == 3:
        "{i}The computer is still locked for the moment."
        hide other darken
        hide image "objects/hiroseComputer_closeup.png"
        show Grace neutral at left
        g "All right, I'll just log in, copy her credentials, and then we can leave."
        hide Grace
        hide Ada
        window hide
        $quick_menu = False
        play sound typing
        show other darken
        show image "images/objects/hiroseComputerLogged.png" at centerScreen
        g "Just a second to copy over the files... and we're good!"
        $hiroseComputerUnlock=True
        stop sound fadeout 0.5
        hide other darken
        hide image "images/objects/hiroseComputerLogged.png"
        $quick_menu = True
        jump gotHirosePassword
    elif hirosePhoto_inv == True and hirosePersonalItems_value < 3:
        "{i}The computer is still locked for the moment."
        hide other darken
        hide image "objects/hiroseComputer_closeup.png"
        show Ada neutral at right
        a "We have the password. Are you sure you are ready? After we get the credentials we should not linger."
        show Grace neutral at left
        g "I suppose I should take another look around."
        $ quick_menu = False
        hide Grace
        hide Ada
        window hide
        jump hirosePersonalComputer
    else:
        "{i}The computer is still locked for the moment."
        hide other darken
        hide image "objects/hiroseComputer_closeup.png"
        show Ada neutral at right
        a "Grace, you yourself said trying to hack this would likely trigger a security alert."
        show Grace neutral at left
        g "Right. I suppose I'll take another look around."
        g "Writing down a password kind of ruins the point of having one, though."
        a "Your mother is on the elderly side of the human age spectrum. Memory problems become more common."
        show Grace snarky
        g "Please do tell her that. Make sure I'm there when you do."
        show Grace neutral
        g "Come on, let's keep looking."
        $ quick_menu = False
        hide Ada
        hide Grace
        window hide
    window hide
    jump hirosePersonalComputer
