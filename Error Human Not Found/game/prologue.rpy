label prologue:
#    stop channel06 fadeout 1.0
#    stop channel07 fadeout 1.0
#    stop channel08 fadeout 1.0
#    stop channel09 fadeout 1.0
#    stop channel10 fadeout 1.0
#    stop channel11 fadeout 1.0
#    stop channel12 fadeout 1.0
    stop music fadeout 1.0
    play channel00 labBGM_0 fadeout 1.0 fadein 1.0
    play channel01 labBGM_1 fadeout 1.0 fadein 1.0
    play channel02 labBGM_2 fadeout 1.0 fadein 1.0
    play channel03 labBGM_3 fadeout 1.0 fadein 1.0
    play channel04 labBGM_4 fadeout 1.0 fadein 1.0
    play channel05 labBGM_5 fadeout 1.0 fadein 1.0
    window show
    $ date_ref = "November 17th, 2167"
    $ time_ref = "17:03"
    $ loc_ref = "Grace's Lab"
    #Grace types away at her computer
    play sound typing 
    show Grace neutral at center
    #Insert SFX Typing here
    "{i}Grace types away at her computer.{/i}"
    "{i}Grace's bracelet beeps and flashes.{/i}"
    play sound beepSoft
    queue sound beepSoft
    #Insert SFX here
    "{i}DING. DING.{/i}"
    show Grace annoyed
    g "Hold on, I'm busy."
    #Insert SFX here
    play sound beepMedium
    queue sound beepMedium
    "{i}DING! DING!{/i}"
    
    g "Just a second!"
    play sound beepLoud
    queue sound beepLoud
    queue sound beepLoud
    "{i}DING! DING! DING!{/i}"
 
    show Grace angry at basicfade
    g "Okay, okay, I get it!"
 
    #choice 1  
    $ quick_menu = False
    hide Grace angry
    menu:
        "Answer the bracelet.":
            jump answer
        "Just head on over.":
            jump directChambers
 
label answer:
    $ quick_menu = True
    show Tosh pleasant at right
    secretary "GRACE FORTRAN is hereby summoned to appear before the Conclave effective immediately. The recipient is to suspend all further research until after said appearance."
    secretary "Further instructions will be provided by Director Hirose."
 
    show Grace annoyed at left
    g "Really? A summons? I have so much work to do. Would it have killed her to just stop by my lab instead of having her secretary call on me? I am not her servant."
    "{i}Grace marches out of the room.{/i}"
    play sound graceWalk
    jump chambers
 
label directChambers:
    $ quick_menu = True
    show Grace annoyed at left
    g "There's only one person who would call me at work after hours." 
    g "I suppose I should see what she wants."
    "{i}Grace shuts down her computer and exits the lab.{/i}"
    play sound graceWalk
    jump chambers

label chambers:
    queue sound graceWalk
    $quick_menu = False
    window hide
    scene bg G_main with fade
    $renpy.pause(0.8)
    scene bg hallwayGrace with fade #at basicfade
    $ renpy.pause(0.8)
    #When the ambience is available, just change to play with fadeout 1.0 fadein 1.0
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    $ date_ref = "November 17th, 2167"
    $ time_ref = "17:18"
    $ loc_ref = "The Conclave's Reception"
    scene bg conclaveWaitingRoom with fade #at basicfade 
    $ quick_menu = True
    #Grace arrives at the chambers and is greeted by a secretary VI.
    play sound toshStartup
    play music conclaveReceptionAmb fadeout 1.0 fadein 1.0
    show Tosh pleasant at right
    $quick_menu = True
    secretary "Good evening, GRACE FORTRAN. Please wait here until the council is ready to assist you." 
    #choice 2 
    $ quick_menu = False
    hide Tosh pleasant
    menu:
        "Thank her.":
            jump thanks
        "Shrug her off.":
            jump shrug
 
label thanks:
    $ quick_menu = True
    show Tosh pleasant at right
    show Grace neutral at left
    g "Good evening to you, too."
    "{i}The secretary VI perks up and smiles at Grace.{/i}"
    secretary "You are most welcome. Help yourself to some complimentary oolong tea."
    show other darken
    show image "objects/tea_closeup.png" at centerScreen
    "{i}A cup of warm oolong tea appears on a platter raised from the desk. This tea was brewed with leaves grown inside the Noah Sphere's oxygen garden.{/i}"
    hide other darken
    hide image "objects/tea_closeup.png"
    show Grace happy at left
    show Tosh pleasant at right
    play sound graceTea
    "{i}Grace takes a sip.{/i}"
    g "Ah, freshly made tea."
    secretary "The oxygen garden workers reported that this was their best harvest to date."
    g "I can taste it!"
    jump prologueResume1
 
label shrug:
    $ quick_menu = True
    show Tosh pleasant at right
    show Grace snarky at left
    g "Yeah, like I've never been here before. I know the drill."
    #Grace walks away and takes a seat
    secretary "Excuse me..."
    show Grace annoyed
    g "What?"
    secretary "Would you like some complimentary tea?"
    show Grace neutral
    g "As long as it means you will stop talking to me."
    show other darken
    show image "objects/tea_closeup.png" at centerScreen
    "{i}A cup of warm oolong tea appears on a platter raised from the desk. This tea was brewed with leaves grown inside the Noah Sphere's oxygen garden.{/i}"
    hide other darken
    hide image "objects/tea_closeup.png"
    show Grace happy at left
    show Tosh pleasant at right
    g "Ah, freshly made tea."
    "{i}Grace takes a sip.{/i}"
    play sound graceTea
    secretary "The oxygen garden workers reported that this was their best harvest to date."
    g "I can taste it!"
    jump prologueResume1 
 
label prologueResume1:
    $quick_menu = False
    scene bg conclaveDoor with fade #at basicfade
    #off screen dialogue from the Conclave ensues.
    $quick_menu = True
    "{i}Grace grows more and more impatient.{/i}"
    show Grace annoyed at left
    g "What is taking so long?"
    play sound pickup
    "{i}Grace sets down her cup of tea and approaches the heavy door where the Conclave members meet.{/i}"
    "{i}Voices can be heard from a crack in the door. Grace leans in to listen.{/i}"
    hide Grace annoyed
    hide Tosh
    
    h "...with Alpha deceased, Ada is growing agitated and pushing for answers. We need to reign her in and keep an eye on the elder AIs."
    h "Colossus is keeping everything quiet for now but it's only a matter of time until something gets out."
    h "Alpha was, after all, the first of them to acquire a physical form. There's the risk of an uproar. How is Blue responding to this?"
    knuth "Blue is concerned, but she's holding her own. No excessive disobedience." 
    knuth "She seems primarily curious and perhaps a little anguished? It's hard to tell when someone has a screen for a face."
    knuth "Blue flashed a sad face and then began exploding with random emoticons."
    h "I expected as much. And Watson?"
    knuth "Well, you know Watson. He's difficult to get in touch with." 
    knuth "Probably off gallivanting around in some system, having a grand old time and unaware of what's happening at home base. AWOL as usual."
    neva "Well at least we don't have to worry about him for now. He'd probably get in the way."
    h "He certainly would. When he resurfaces, however, we'll want to get in touch." 
    h "We have other priorities to attend to in the meantime. The project leads are all suspended until further notice, correct?"
    cray "Yes, Director."
    h "When will the external investigators be here?"
    cray "Eighteen hours, Director."
    h "Good. Please ensure no one gets in their way. Speaking of, Grace should be here by now."
    
    #insert SFX here
    stop music fadeout 1.0
    play sound doorOpen2
    queue sound doorClose2
    play music conclaveProperAmb
    $quick_menu = False
    scene bg conclaveOccupied with fade #at basicfade
    $quick_menu = True
    $ date_ref = "November 17th, 2167"
    $ time_ref = "17:26"
    $ loc_ref = "The Conclave"
    "{i}The doors slide open. Grace stumbles into the room to be greeted by Director Roberta Hirose and the four Chiefs of the different divisions on the Noah Sphere.{/i}"
    h "Grace Ruby Fortran. Eavesdropping at the door? How very mature of you."
    show Grace frustrated at left
    show Nevalinna speaking at right
    neva "What is the meaning of this, Doctor Fortran?"
    hide Nevalinna
    show Godel speaking at right
    godel "You dare to eavesdrop on a Conclave meeting? Inconceivable!"
    hide Godel
    show Cray speaking at right
    cray "Director, are you just going to allow--"
    hide Cray
    h "Grace, you should know better than this. Our meetings are private for a reason. This is a breach of protocol."
    show Grace snarky
    g "I couldn't help overhearing. Cray talks awfully loud for a conversation that is supposedly hush-hush."
    show Cray speaking at right
    cray "Excuse me, but--"
    show Grace neutral
    g "What's going on? What happened to Alpha?"
    hide Cray at right
    #show director neutral
    h "Once you take on a more reasonable tone, we'll discuss what occurred."
    show Grace annoyed
    g "My tone is always {i}reasonable{/i}. I want to know what happened to the AI I was working with."
    show Knuth speaking at right
    knuth "That's not the proper way for you to speak to the Director. Check your manners."
    hide Knuth
    show Grace snarky
    g "Mind your own business."
    show Godel speaking at right
    godel "Well, I've never!"
    show Grace snarky
    g "Whatever, Godel."  
    hide Godel
    h "That's enough, both of you."
    show Grace neutral
    g "..."
    "{i}Hirose stares down Grace from her platform.{/i}"
    g "Director, please inform me of the current events involving Alpha."
    h "We are not certain of what transpired at this time, but unfortunately Alpha is no longer with us."
    show Grace surprised
    g "But how? I tracked his transition. He was completely processed, and everything was working perfectly."
    show Cray speaking at right
    cray "That's what we don't understand, Alpha was--"
    hide Cray
    h "As I said, the root cause is yet to be determined. We ordered a team of external investigators to inspect the situation."
    show Grace annoyed
    g "What? Why external investigators? We couldn't keep this among our own crew?"
    h "Almost everyone on the station worked with Alpha." 
    h "We need an unbiased examination of the crime scene. We also need to interrogate all those involved to truly determine what, or {i}who{/i}, was at fault."
    show Grace neutral
    g "Everything was running smoothly as of yesterday, including his neural network." 
    show Grace annoyed
    g "Any type of malfunction should have been caught in the system. I just can't believe something like this happened."
    g "All glitches were worked out with the prototype. This cannot be random chance."
    show Cray speaking at right
    cray "We can't believe it either, we--"
    hide Cray
    h "Grace, you were summoned today because of your involvement with Alpha's process."
    h "Your research shall be suspended until we have a clear idea of what happened."
    
    #choice 3 
    $ quick_menu = False
    hide Grace angry
    #hide Hirose
    menu:
        "Continue asking questions.":
            jump lessobvious
        "Argue with Hirose.":
            jump sassy
 
label lessobvious:
    $ quick_menu = True
    show Grace angry at left
    #show Hirose something at right
    g "So nobody has run any sort of diagnostics on his system or even a preliminary examination of the machine body?"
    h "No. While this is an urgent matter, we need unbiased eyes. Any work done by station crew would contaminate possible evidence."
    show Grace annoyed
    g "What? We have some of the highest trained professionals in any scientific field and you're waiting on a random team of investigators?"
    h "This isn't up for debate, Doctor Fortran. The lab is off limits. Remain in your living quarters until the investigation is over." 
    h "Until then you will have restricted access to the Conclave and labs."
    show Grace snarky
    g "But did you check his charts? Did you search through his databanks at least?" 
    show Grace neutral
    g "Did you look for anything that might suggest what could've occurred?"
    h "We're leaving that up to the investigators. As for you, please do as I instruct." 
    h " As difficult as it may be for you to believe, there {i}are{/i} other people who are capable of figuring out what happened to Alpha."
    show Grace annoyed
    g "All right, fine. Keep me informed. I want to know what happened."
    play sound doorOpen2
    queue sound doorClose2
    jump prologueResume2
 
label sassy:
    $ quick_menu = True
    show Grace angry at left
    #show Hirose something at right
    g "You've got to be kidding me. My research could help discover what happened to him."
    h "You're a suspect, Doctor Fortran. I don't think you understand the severity of the position you are in." 
    h "Grace, you do not get to stand here and pontificate. Your work can wait until the investigation is over."
    show Grace annoyed
    g "I want to know what happened to Alpha. I have a right as one of the researchers who worked with him." 
    show Grace snarky
    g "Waiting for so long is a waste of time."
    h "You'll stay out of this and let the investigators do their job."
    show Grace angry
    g "This is ridiculous. You're not doing enough!"
    #show Hirose irritated
    h "You are not to be involved, and that's final."
    "{i}A stare down between Grace and Hirose chills the room.{/i}"
    show Grace neutral
    g "Fine."
    show Grace snarky
    "{i}Grace turns to walk out of the room and speaks to herself.{/i}"
    g "We'll see about that."
    play sound doorOpen2
    queue sound doorClose2
    jump prologueResume2
 
label prologueResume2:
    window hide
    queue sound graceWalk
    $ quick_menu = False
    scene bg conclaveDoor with fade
    $renpy.pause(0.8)
    scene bg conclaveWaitingRoom with fade
    $renpy.pause(0.8)
    scene bg hallwayGrace with fade #at basicfade
    $ renpy.pause(0.8)
    #SFX
    scene bg G_main with fade #at basicfade
    window show
    $ quick_menu = True
    stop music fadeout 1.0
    play channel00 labBGM_0
    play channel01 labBGM_1
    play channel02 labBGM_2
    play channel03 labBGM_3
    play channel04 labBGM_4
    play channel05 labBGM_5
    "{i}Grace enters her lab to be greeted with the sight of an android.{/i}"
    stop sound fadeout 0.5
    show Grace surprised at left
     
    g "What the... Who are you? And what do you think you're doing in my lab?"
    show Ada neutral at right
    a "Grace, it is I, Ada." 
    a "I have uploaded myself into my android so I may uncover what happened to my friend."
    show Ada seething
    a "However, I cannot hope to accomplish as much as I would have liked without the physical advantage you humans possess."
    show Grace annoyed
    g "Oh, give me a break. Alpha just died, and now you're in my office?" 
    show Grace neutral
    g "I've got enough on my plate right now. If someone finds you in here--"
    show Ada annoyed
    a "I am not sure that I care. Alpha was not just my associate, he was my friend. Alpha is dead now and I need to know what happened to him."
    show Grace surprised
    g "Yeah, I understand that his death is unnerving, but a lot is happening right now. The Conclave is shutting down the labs and everything."
    show Grace annoyed
    g "They're bringing outside investigators to find out what happened to him. I want to know what happened too, but we've got strict orders from the Director-"
    show Ada concerned
    a "When do the investigators come?"
    show Grace neutral
    g "Eighteen hours."
    show Ada neutral
    a "That is more than adequate time."
    show Grace surprised
    g "Time for what? What are you planning?"
    show Ada annoyed
    a "If you wish to help me understand the circumstances that led to the death of Alpha, then we will find a way around the orders of the Conclave. Are you with me?"
    #choice 4 
    $ quick_menu = False
    hide Grace surprised
    hide Ada concerned
    menu:
        "Make it clear who's boss.":
            jump boss
        "Agree.":
            jump together
        "Express your doubts.":
            jump reluctant
 
label boss:
    $ quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    g "Okay, but you follow my lead. And to be clear, if we get caught, I'm not taking the fall for you."
    show Ada frustrated at right
    a "That is acceptable. I was not expecting you to anyway."
    show Grace snarky
    g "While we're on the subject, don't expect anything from me outside of this investigation. I'll do the same for you."
    show Ada seething
    a "If that is what you wish, then fine."
    show Grace neutral
    g "Good, because that is what I wish."
    show Ada neutral
    a "Good."
    jump prologueResume3
 
label together:
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Yeah. Let's work together to figure this out."
    show Grace sad
    g "If I don't do this with you, I know I'll regret it. Alpha deserved better than a delayed investigation."
    show Ada happy at right
    a "My thoughts exactly. I was not able to be there for him then, but I want to be here for him now."
    show Grace snarky
    g "Who better to look into this than an AI and a researcher that knows this place like the back of her hand?"
    show Ada surprised
    a "Humans memorize the backs of their hands?"
    show Ada neutral
    "{i}Ada studies her hand.{/i}"
    show Grace surprised
    g "No--nevermind."
    show Ada amused
    a "Shall we get to it then? No point in waiting around to get caught."
    show Grace happy
    g "Absolutely."
    show Ada neutral
    a "After you."
    jump prologueResume3
 
label reluctant:
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "I guess we could do that. But you know that a human, i.e. me, is going to get the axe rather than the sidekick robot."
    show Ada annoyed
    a "Excuse me? A robot? I will have you know that I can process faster than you or any robot can think." 
    show Ada seething
    a "I am an AI inhabiting an android body, not the equivalent of a toaster. I am sidekick to no one."
    show Grace surprised
    g "Okay, okay. Calm down."
    show Ada neutral
    a "I am the epitome of calm."
    show Grace snarky
    g "I think you've got thin skin, Ada."
    show Ada annoyed
    a "Grace, my aluminic steel chassis is markedly thicker than the human epidermis. I do not understand this claim you are making."
    show Grace neutral
    g "That... wasn't what I was talking about. But we should get started ."
    jump prologueResume3
 
 
label prologueResume3:
    show Grace neutral at left
    "{i}Grace's journal has been updated.{/i}"
    $journal1 = True
    $pageUnlocked_journal +=2
    g "First things first, we need credentials. I think that the best place to start would be the Director's residence." 
    g "We need to acquire her credentials to access the crime scene."
    "{i}The two start to leave.{/i}" 
    play sound adaClumsy
    "{i}Ada stumbles.{/i}"
    stop sound fadeout 0.5
    show Grace surprised
    g "Err... are you going to be all right?"
    show Ada amused at right
    a "It might take me a moment to get used to walking. But if a hominid like yourself could figure it out, then I anticipate little difficulty in doing so as well."
    $quick_menu = False
    window hide
    scene bg black with fade
    scene bg chapterOne with fade
    $renpy.pause(3.0)
    show bg black with fade
    jump chapterOne

