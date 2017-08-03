label prologue:
    stop channel00 
    stop channel01 
    stop channel02 
    stop channel03 
    stop channel04 
    stop channel05 
    stop channel06 
    stop channel07 
    stop channel08 
    stop channel09 
    stop channel10 
    stop channel11 
    stop channel12 
    #    play channel00 lab2_00
    #    play channel01 lab2_01
    #    play channel02 lab2_02
    #    play channel03 lab2_03
    #    play channel04 lab2_04
    #    play channel05 lab2_05
    #    play channel06 lab2_06
    #    play channel07 lab2_07
    #    play channel08 lab2_08
    #    play channel09 lab2_09
    window show
    $ date_ref = "November 17th, 2167"
    $ time_ref = "17:03"
    $ loc_ref = "Grace's Lab"
    #Grace types away at her computer
#    play sound 
    show Grace neutral at basicfade#left at basicfade #with fade
    #Insert SFX Typing here
    "{i}Grace types away at her computer.{/i}"
    "{i}Grace's bracelet beeps and flashes.{/i}"
    
    #Insert SFX here
    "{i}DING. DING."
 
    hide Grace neutral at basicfade
    show Grace annoyed at basicfade #at left with fade
    g "Hold on, I'm busy."
    #Insert SFX here
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
    "{i}Grace marches out of the room."
    jump chambers
 
label directChambers:
    $ quick_menu = True
    show Grace annoyed at left
    g "There's only one person who would call me at work after hours." 
    g "I suppose I should see what she wants."
    "{i}Grace shuts down her computer and exits the lab."
    jump chambers

label chambers:
    $ quick_menu = True
    scene bg conclaveWaitingRoom with fade #at basicfade 
    #Grace arrives at the chambers and is greeted by a secretary VI.
    show Tosh pleasant at right
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
    "{i}The secretary VI perks up and smiles at Grace."
    secretary "You are most welcome. Help yourself to some complimentary oolong tea."
    show other darken
    show image "objects/tea_closeup.png" at centerScreen
    "{i}A cup of warm oolong tea appears on a platter raised from the desk. This tea was brewed with leaves grown inside the Noah Sphere's oxygen garden."
    hide other darken
    hide image "objects/tea_closeup.png"
    "{i}Grace takes a sip."
    show Grace happy
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
    g "As long as it means you will stop talking to me."
    show other darken
    show image "objects/tea_closeup.png" at centerScreen
    "{i}A cup of warm oolong tea appears on a platter raised from the desk. This tea was brewed with leaves grown inside the Noah Sphere's oxygen garden."
    hide other darken
    hide image "objects/tea_closeup.png"
    show Grace happy
    g "Ah, freshly made tea."
    secretary "The oxygen garden workers reported that this was their best harvest to date."
    g "I can taste it!"
    jump prologueResume1 
 
label prologueResume1:
    scene bg conclaveDoor with fade #at basicfade
    #off screen dialogue from the Conclave ensues.
    "{i}Grace grows more and more impatient."
    show Grace annoyed at left
    g "What is taking so long?"
    "{i}Grace sets down her cup of tea and approaches the heavy door where the Conclave members meet."
    "{i}Voices can be heard from a crack in the door. Grace leans in to listen."
    hide Grace annoyed
    
    h "...with Alpha deceased, Ada is growing agitated and pushing for answers. We need to gain a grip on her and keep an eye on the other three elder AIs."
    h "Colossus is keeping everything quiet but there's only so much we can keep contained."
    h "Alpha was, after all, the first of them to acquire a physical form. There's the risk of an uproar. How is Blue responding to this?"
    knuth "Blue is concerned, but she's holding her own. No excessive disobedience." 
    knuth "Just curiosity, and I think anguish? It's hard to tell with her. She just flashed a sad face and then exploded with other random emoticons."
    h "I expected as much. And Watson?"
    knuth "Well, you know Watson. He's difficult to get in touch with." 
    knuth "Probably off gallivanting around in some system, having a grand old time and unaware of what's happening at home base. AWOL as usual."
    neva "Well at least we don't have to worry about him for now. He'd probably get in the way."
    h "He certainly would. When he resurfaces, however, we'll want to get in touch." 
    h "Let's not forget that point. We have the project leads suspended until further notice, correct?"
    cray "Yes, Director."
    h "When will the external investigators be here?"
    cray "Eighteen hours, Director."
    h "Good. Please ensure no one gets in their way. Speaking of, Grace should be here by now."
    
    #insert SFX here
    scene bg conclaveOccupied with fade #at basicfade
    "{i}The doors slide open. Grace stumbles into the room to be greeted by Director ROBERTA HIROSE, and the four Chiefs of different divisions on the Noah Sphere."
    h "Grace Ruby Fortran. Eavesdropping at the door? How very mature of you."
    show Grace frustrated at left
    show Nevalinna speaking at right
    neva "What is the meaning of this, Doctor Fortran?"
    hide Nevalinna
    show Godel speaking at right
    godel "You dare to eavesdrop on a Conclave meeting? Inconceivable!"
    show Cray speaking at center
    cray "Director, are you just going to allow--"
    h "Grace, you should know better than this. Our meetings are private for a reason. This is a breach of protocol."
    hide Godel
    g "I couldn't help but overhear. Especially with Cray's voice being so loud."
    cray "Excuse me, but--"
    g "What's going on? What happened to Alpha?"
    #show director neutral
    h "Once you take on a more reasonable tone, we'll discuss what occurred."
    g "My tone is always reasonable. I want to know what happened to the AI I was working with."
    godel "That's not the proper way you speak to the Director. Check your manners. "
    g "Mind your own business."
    show Godel speaking at right
    godel "Well, I've never!"
    g "Whatever, Godel."  
    h "That's enough, both of you."
    g "..."
    "{i}Hirose stares down Grace from her platform."
    g "Director, please inform me of current events involving Alpha."
    h "We are not exactly certain of the events that transpired at this time, but unfortunately Alpha is no longer with us."
    show Grace surprised
    g "But how? I tracked his transition. He was completely processed, and everything was working perfectly."
    show Cray speaking at center
    cray "That's what we don't understand, Alpha was--"
    h "Like I stated, we are not positive of the reason yet. We ordered a team of external investigators to inspect the situation."
    g "What? Why external investigators? We couldn't keep this among our own crew?"
    h "Almost everyone on the station worked with Alpha." 
    h "We need an unbiased examination of the crime scene. We also need to interrogate all those involved to truly determine what, or who, was at fault."
    g "Everything was running smoothly as of yesterday, including his neural network." 
    g "Any type of malfunction should have been caught in the system. I just can't believe something like this happened."
    g "All glitches were worked out with the prototype. This cannot be random chance."
    cray "We can't believe it either, we--"
    h "Grace, you were summoned today because of your involvement with Alpha's process."
    h "Your research shall be suspended until we have a clear idea of what happened."
    
    #choice 3 
    $ quick_menu = False
    hide Grace angry
    menu:
        "Continue asking questions.":
            jump lessobvious
        "Argue with Hirose.":
            jump sassy
 
label lessobvious:
    $ quick_menu = True
    show Grace angry at left
    g "So nobody has run any sort of diagnostics on his system or even a preliminary examination of the machine body?"
    h "No. While this is an urgent matter, we need unbiased eyes. Any work done by station crew would contaminate possible evidence."
    g "What? We have some of the highest trained professionals in any scientific field and you're waiting on a random team of investigators?"
    h "This isn't up for debate, Doctor Fortran. The lab is off limits. Remain in your living quarters until the investigation is over." 
    h "Until then you will have restricted access to the Conclave and labs."
    show Grace annoyed
    g "But did you check his charts? Did you search through his databanks at least?" 
    g "Did you look for anything that might suggest what could've occurred?"
    h "We're leaving that up to the investigators to figure out. As for you, please do as I instruct." 
    h " As difficult as it may be for you to believe, there are other people who are perfectly capable of answering what happened to Alpha."
    g "All right, fine. Keep me informed. I want to know what happened."
    jump prologueResume2
 
label sassy:
    $ quick_menu = True
    show Grace angry at left
    g "You've got to be kidding me. My research could help discover what happened to him."
    h "You're a suspect, Doctor Fortran. I don't think you understand the severity of the position you are in." 
    h "This isn't something you get to stand here and pontificate about. Your work can wait until the investigation is over."
    g "I want to know what happened to Alpha. I have the right as one of the researchers who worked with him and his android body." 
    g "Waiting for so long is a waste of time."
    h "You'll stay out of this and let the investigators do their job."
    g "This is ridiculous. You're not doing enough!"
    #show Hirose irritated
    h "You are not to be involved, and that's final."
    "A stare down between Grace and Hirose chills the room."
    g "Fine."
    show Grace snarky
    "{i}Grace turns to walk out of the room and speaks to herself."
    g "We'll see about that."
    jump prologueResume2
 
label prologueResume2:
    window hide
    $ quick_menu = False
    scene bg hallwayGrace with fade #at basicfade
    $ renpy.pause(0.5)
    #SFX
    scene bg G_main with fade #at basicfade
    window show
    $ quick_menu = True
    "{i}Grace enters her lab to be greeted with the sight of an android."
    show Grace surprised at left
     
    g "What the... Who are you? And what do you think you're doing in my lab?"
    show Ada neutral at right
    a "Grace, it is I, Ada." 
    a "I have uploaded myself into a physical form to solve the death of my friend."
    a "However, I cannot hope to accomplish as much as I would have liked without the physical advantage you humans possess."
    show Grace annoyed
    g "Oh, give me a break. Alpha just died, and now you're in my office?" 
    g "I've got enough on my plate right now. If someone finds you in here--"
    a "I am not sure that I care. Alpha was not just my associate, he was my friend. Alpha's now dead and I need to know what happened to him."
    show Grace surprised
    g "Yeah, I understand that his death is unnerving, but a lot is happening right now. The Conclave is shutting down the labs and everything."
    g "They're bringing outside investigators to find out what happened to him. I want to know what happened too, but we've got strict orders from the Director-"
    show Ada concerned
    a "When do the investigators come?"
    g "Eighteen hours."
    a "That is more than adequate time."
    g "Time for what? What are you planning?"
    a "If you wish to help me understand the circumstances that led to Alpha's death, then we'll find a way around the Conclave's orders. Are you with me?"
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
    g "Okay, but you follow my lead. And to be clear, if we get caught, I'm not taking the fall for you."
    show Ada frustrated at right
    a "That is acceptable. I was not expecting you to anyway."
    g "While we're on the subject, don't expect anything from me outside of this investigation. I'll do the same for you."
    a "If that is what you wish, then fine."
    g "Good, because that is what I wish."
    a "Good."
    jump prologueResume3
 
label together:
    $ quick_menu = True
    show Grace neutral at left
    g "Yeah. Let's work together to figure this out."
    g "If I don't do this with you, I know I'll regret it. Alpha deserved better than a delayed investigation."
    show Ada happy at right
    a "My thoughts exactly. I was not able to be there for him then, but I want to be here for him now."
    g "Who better to look into this than an AI and a researcher that knows this place like the back of her hand?"
    a "Humans memorize the backs of their hands?"
    "{i}Ada studies her hand."
    g "No--nevermind."
    a "Shall we get to it then? No point in waiting around to get caught."
    g "Absolutely."
    a "After you."
    jump prologueResume3
 
label reluctant:
    $ quick_menu = True
    show Grace neutral at left
    g "I guess we could do that. But you know that a human, i.e. me, is going to get the axe rather than the sidekick robot."
    show Ada seething at right
    a "Excuse me? A robot? I'll have you know that I can process faster than you or any robot can think." 
    a "I am an AI inhabiting an android body, not the equivalent of a toaster. I am no one's sidekick."
    show Grace surprised
    g "Okay, okay. Calm down."
    a "I am the epitome of calm."
    g "I think you've got thin skin, Ada."
    a "Grace, my aluminic steel chassis is markedly thicker than the human epidermis. I do not understand this claim you are making."
    g "That... wasn't what I was talking about. But we should get started ."
    jump prologueResume3
 
 
label prologueResume3:
    show Grace neutral at left
    g "First things first, we need credentials. I think that the best place to start would be the Director's residence." 
    g "We need to acquire her credentials to access the crime scene."
    "{i}The two start to leave." 
    "{i}Ada stumbles."
    g "Err... are you going to be all right?"
    show Ada amused at right
    a "It might take me a moment to get used to walking. But if a hominid like yourself could figure it out, then I anticipate little difficulty in doing so as well."
    jump chapterOne


#End of prologue.
