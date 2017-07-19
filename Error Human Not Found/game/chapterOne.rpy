label chapterOne:
    jump startChapterOne

label startChapterOne:
    scene bg hiroseDoor
    show Grace neutral at left
    g "Here we are. Scan my badge and voila. Open."
 
    "The door doesn't budge."
    "A voice issues from speakers near the door."
 
    tosh "The Director is not here at the moment. Please make an appointment."
    #Tosh's sprite isn't displayed here
    show Grace annoyed
    g "What? I usually have access!"
 
    show Ada nervous at right
    a "And why do you have access to the Director's office?"
 
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
    "An awkward silence hangs."
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
    a "Interesting. I had hoped to have retained my connection to the Sphere's network."
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
    a "This discussion is pointless. I am not going to waste anymore time {i}or{/i} processing power on it."
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
 
    #WITH PUZZLE IMPLEMENTED, need to test that these function. For now, they are commented out.
    #Also make sure to set quick_menu to False and set it back to true when done
    #begin door hacking puzzle here, (GRAMMAR PUZZLE ONE)resume script once the puzzle concludes.
#    if(attemptsLogicGate1==1):
#        show Grace happy
#        g "Yes! First try! Still got it. Nobody can touch these elite skills." 
#    if (attemptsLogicGate1>1 and attempts<4):
#        #show Grace happy
#        g "Hey, wasn't perfect. But the door is open, and we haven't been caught." 
#    if (attemptsLogicGate1>3):
#	#show Grace annoyed
#	g "Apparently my hacking skills have become subpar. Too much legitimate coding."

 
    #transition to Hirose's reception  with a fade.
    scene bg hiroseReception
 
    show Ada neutral at right
    a "Are you positive that being here is within protocol?"
 
    show Grace happy at left
    g "If it makes you feel better, this isn't the first time I've done this."
 
    show Ada neutral
    a "I feel that your statement requires some elaboration."
    
    show Grace snarky
    g "Let's just say that whoever updates key card access needs to do their job faster."
 
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
    scene bg hiroseOfficeMain  
    show Grace neutral at left
    g "It almost hurts to admit it, but I'm incredibly jealous of this office. Don't have the same view from my little lab."
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
    a "Now, let me see the computer. We do not have time to guess passwords."
    g "What are you doing?"
    a "I am going to access it directly."
    a "I have spent all of my existence manipulating code."
    a "It is about as difficult as moving building blocks."
    jump hiroseOffice_actions
 
label subservient1:
    $ points_S +=1
    $ quick_menu = True
    show Grace angry at left
    g "You had no business pulling rank on another computer system without consulting me first." 
    g "I\'m in charge here, not you."
    show Ada frustrated at right
    a "Another {i}computer system{/i}?"
    a "I am so much more than that. I am a synthetic intelligence transf--"
    g "I don\'t care, Ada."
    g "You could\'ve blown our cover, and I would\'ve lost my career if that happened."
    g "I don\'t even know what they would\'ve done to you."
    a "Fine, whatever you say."
    g "It's your turn to pull your weight. You can hack the computer."
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
    a "Grace, I had no intention of engaging Tosh. Besides, I do not think it would have been a very fair fight."
    a "Now, let us see the computer. This should not take me too long."
    jump hiroseOffice_actions
    
label exploreOffice:
    #Begin the sequence that allows the players to look around Hirose's office. 
    #3 items split 
    #Once the player clicks on the computer, actual puzzle fires.
    window hide
    $ quick_menu = False
    scene bg hiroseOfficeMain with fade
    call screen hiroseOffice1_scr
label hiroseOffice2:
    window hide
    $ quick_menu = False
    scene bg hiroseOfficeTransition with fade #at basicfade
    call screen hiroseOffice2_scr
#Buttons for the objects
label exploreHiroseOffice:
    scene bg hiroseOfficeDesk with fade #at basicfade
    $ quick_menu = False
    call screen investigateOffice

label hiroseTea_label:
    $ quick_menu = True
    $ hiroseTea_inv = True
    $ hiroseOfficeItems +=1
    show image "hiroseTea_closeup.png" at centerScreen
    window show
    "A cup containing the dregs of a hybrid floral tea."
    g "Roberta does drink some of the strangest teas. I'll stick to my coffee, thanks."
    a "Humans and their caffeine..."
    hide image "hiroseTea_closeup.png"
    window hide
    $ quick_menu = False
    jump exploreHiroseOffice

label hiroseSafe_label:
    $ quick_menu = True
    $ hiroseSafe_inv = True
    $ hiroseOfficeItems += 1
    show image "hiroseSafe_closeup.png" at centerScreen
    window show
    "A biometric locked safe."
    a "Grace, should you be poking around that?"
    g "Only as a last resort. Those kind of locks are a pain to circumvent anyways."
    hide image "hiroseSafe_closeup.png"
    window hide
    $ quick_menu = False
    jump exploreHiroseOffice
    
label adaActualPuzzle1:
    scene bg hiroseOfficeDesk
    $ quick_menu = True
    window show
    "Hirose's work computer. Grace and Ada are currently unable to access it."
    show image "hiroseOfficialComputer_closeup.png" at centerScreen
    $ renpy.pause(0.5)
    if (tutorial_LGEasy == True):
        $ tutorial_LGEasy = False
        jump tutorial_LGEasy_1
    window hide 
    if Logic_A_solved == False:
        jump logicGate_easyA1
    if Logic_B_solved == False:
        jump logicGate_easyB1
    hide image "hiroseOfficialComputer_closeup.png"
#    if (solved_LG_easy == True):
#        $ hiroseOfficeItems += 1
    window hide
    $ quick_menu = False
    jump exploreHiroseOffice
#    if (attemptsBinary1==1):
#        #show Ada amused
#        a "I did not even have to suspend any normal running processes to crack that."
#    if (attemptsBinary1>1 and attemptsBinary1<4):
#        #show Ada happy
#        a "Well played, personal computer, but the AI always comes out on top." 
#    if (attemptsBinary1>3):
#	#show Ada annoyed
#	a "I can process yottaFLOPS but a simple password causes me this much difficulty? I have to question the definition of state-of-the-art hardware."
        
label wegotthedeets:
    $ quick_menu = True
    show Ada neutral at right
    a "Grace, your mother does not appear to keep any personal or secure information on this terminal."
    show Grace annoyed at left
    g "Of course not. That would be too easy."
    hide Grace annoyed
    hide Ada neutral
    "Grace looks around, thinking."
    show Grace neutral at left
    g "She's got a personal computer. I'd wager it's probably there."
    scene bg hirosePersonalArea with fade #at basicfade
    show Ada afraid at right
    a "We cannot hack this one. One incorrect guess and we will be locked out."
    g "Let's look around. Maybe something here will tell us what to try."
    jump hirosePersonalArea_actions
    
label hirosePersonalArea_actions: 
    #insert exploration here. Must pick up photo before being able to open computer.
    window hide
    $ quick_menu = False
    scene bg hirosePersonalArea
    call screen hirosePersonalArea_scr
        
label hirosePersonalArea_inv:
    $ quick_menu = False
    scene bg hirosePersonalArea with fade #at basicfade
    window hide
    call screen hirosePersonalArea_invScr
    #should get password from photo
    show Grace happy at left
 
label hirosePersonalComputer:
    $ quick_menu = False
    scene bg hirosePersonalComputer with fade #at basicfade
    call screen investigateHirosePC

label hiroseBed:
    $ quick_menu = False
    scene bg hirosePersonalBed with fade #at basicfade
    call screen investigateHiroseBed

    
label gotHirosePassword:
    $ quick_menu = True
    show Grace happy at left
    g "We've got it!"
    show Grace neutral at left
    g "Let's get back to my lab. We've got some work to do before we can use this."
    $ quick_menu = False
    window hide
    scene bg hirosePersonalArea with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg hiroseOfficeMain with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg hiroseReception with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg hallwayGrace with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg G_main with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg G_deskArea with fade #at basicfade
    $ renpy.pause(0.8)
    scene bg G_right with fade #at basicfade
    $ renpy.pause(0.8)
    window show
    $ quick_menu = True
    #Transition to Grace's Lab here
    "Grace inserts her keycard into her terminal. It boots up, and she runs an update program."
    show Grace happy on left
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
        menu:
            "Comment on her expression.":
                jump sortaroastada
            "Be dismissive.":
                jump actuallyroastada
            "Crack a joke.":
                jump toshgotwrecked
    else:
        a "Humans lack the capacity to retrieve stored information perfectly. It is likely your mother left some reminder of a password somewhere."
        g "I think you underestimate how much like a robot she is."
        window hide
        $ quick_menu = False
        jump hirosePersonalArea_actions
                
label sortaroastada:
    $ points_SbE +=2
    $ quick_menu = True
    show Grace surprised on left
    g "Did you enjoy that?"
    show Ada neutral on right
    a "Hm?"
    show Grace snarky
    g "Talking down to Tosh like that. I can't help but notice the giant grin on your face."
    "Ada pauses, and she reaches up to touch her face."
    show Ada concerned
    a "I did not realize. I was not trying to be cruel, Grace."
    g "I didn't say you were cruel."
    g "Well, I guess even machines like pecking downwards every once in awhile."
    a "I am not familiar with that colloquialism."
    g "Just observe my mother for long enough. She does the same thing."
    $ quick_menu = False
    window hide
    jump hirosePersonalArea_actions
    
label actuallyroastada:
    $ points_S +=2
    $ quick_menu = True
    show Grace annoyed on left
    g "You did your job. Nothing more."
    g "I could've done that by myself, if I'd been so inclined."
    show Ada frustrated on right
    a "I beg to differ. I do not have to help you here, Grace."
    "Grace sighs."
    show Grace neutral
    g "I didn't ask for you to help. You're the one who wanted to come along."
    show Ada Seething
    a "Noted."
    $ quick_menu = False
    window hide
    jump hirosePersonalArea_actions
 
label toshgotwrecked:
    $ points_E +=2
    $ quick_menu = True
    show Grace happy on left
    g "I've got to say, I never liked that VI."
    show Ada amused on right
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
    jump hirosePersonalArea_actions

#end the chapter here, go to Chapter 2
label endChapterOne:
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
    show image "hirosePhoto_closeup.png" at centerScreen
    window show
    "A family portrait of Hirose, a young Grace, and Grace's father."
    a "Is that your family?"
    g "Technically. My mother only half-counts."
    a "You were cute as a kid. What happened?"
    g "Ha. Funny."
    "Grace starts to put the photo back."
    a "Grace, I would look at the back of the photo."
    g "Why?"
    a "A calculated guess."
    #show image "hirosePhoto_closeupBack.png" at centerScreen
    g "The password is on the back of a photo. How original."
    a "Those numbers appear to correspond with your birthdate."
    g "At least it's good for something."
    hide image "hirosePhoto_closeup.png"
    #hide image "hirosePhoto_closeupBack.png" 
    window hide
    $ quick_menu = False
    jump hiroseBed

label hiroseBed_label:
    $ quick_menu = True
    $ hiroseBed_inv = True
    $ hirosePersonalItems_value += 1
    show other darken
    show image "objects/hiroseBed_closeup.png" at centerScreen
    window show
    "A sizeable bed in Hirose's office. A control panel by the edge of the bed platform allows a user to inflate a memory foam mattress out of the center of the bed and customize it to their needs."
    hide other darken
    hide image "objects/hiroseBed_closeup.png"
    show Ada amused at right
    a "This room layout hardly seems standard."
    show Grace snarky at left
    g "I wonder what tipped it off."
    show Ada neutral
    a "Well, these sleeping arrangements are placed in a work area, for one."
    show Grace neutral
    g "That's Hirose for you. Dad and I used to be worried when she wouldn't come home from work."
    g "We learned that there's other places she'd rather be, apparently."
    $ quick_menu = False
    window hide
    jump hiroseBed
    
label hiroseWindow_label:
    $ quick_menu = True
    $ hiroseWindow_inv = True
    $ hirosePersonalItems_value += 1
    show other darken
    show image "objects/hiroseWindow_closeup.png" at centerScreen
    window show
    "An expansive view of the vibrant nebula. Only some of the offices on the Noah Sphere have windows facing out into the galaxy."
    hide image "objects/hiroseWindow_closeup.png"
    hide other darken
    show Grace happy at left
    g "The view from up here never gets old."
    g "If it's got a bed in it, I suppose even an office can be a room with a view."
    show Ada amused at right
    a "It already has windows, Grace. Isn't it already a room with a view?"
    show Grace snarky
    g "All this time around humans, and no ear for metaphors?" 
    show Ada neutral
    a "My memory banks are far from exhaustive, Grace."
    show Grace neutral
    g "Right Hotel metaphors remain the exclusive domain of humans for the forseeable future."
#    g "I suppose the perks of being the head of the station is the view."
#    a "I would concur, but posit that all these windows seem rather unsafe."
#    g "We're humans. Hardly anything we do is textbook safe."
#    a "I am beginning to see that."
    window hide
    $ quick_menu = False
    jump hiroseBed
    
label hirosePC_label:
    show image "objects/hiroseComputer_closeup.png" at centerScreen
    window show
    $ quick_menu = True
    if hirosePhoto_inv == True and hirosePersonalItems_value == 3:
        g "Alright, I'll just log in, copy her credentials, and then we can leave."
        # show image "hiroseComputerLogged.png"
        #play SFX typing
        hide image "hiroseComputer_closeup.png"
        #hide image "hiroseComputerLogged.png"
        jump gotHirosePassword
    elif hirosePhoto_inv == True and hirosePersonalItems_value < 3:
        a "We have the password. Are you sure you are ready? After we get the credentials we should not linger."
        g "I suppose I shsould take another look around."
        hide image "hirosePhoto_closeup.png"
        window hide
        $ quick_menu = False
        jump hirosePersonalComputer
    else:
        a "Grace, if we attempt to log on without a concrete idea of the password, we will alert security to a breach."
        g "Right. I suppose I'll take another look around."
        g "Writing down a password kind of ruins the point of having one, though."
        a "Your mother is on the elderly side of the human age spectrum. Memory problems become more common."
        g "Please do tell her that. Make sure I'm there when you do."
        g "Come on, let's keep looking."
        hide image "hirosePhoto_closeup.png"
        window hide
        $ quick_menu = False
        jump hirosePersonalComputer
