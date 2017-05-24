label prologue:
    $ date_ref = "November 17th, 2167"
    $ time_ref = "17:03"
    $ loc_ref = "Grace's Lab"
    #Grace types away at her computer
    #show Grace neutral
    #BRACELET lights up
 
    "DING. DING."
    #Insert sound effect to play with bracelet chime
    
    #show Grace annoyed
    g "Hold on, I'm busy."
 
    "DING! DING! DING!"
 
    #show Grace angry
    g "Okay, okay, I get it!"
 
    menu:
        "Answer the bracelet.":
            jump answer
        "Head to the council chambers.":
            jump chambers
 
label answer:
    "GRACE FORTRAN is hereby summoned to appear before the Conclave effective immediately. The recipient is to suspend all further research until they have reported to the Conclave.
    Further instructions will be imparted by Director Hirose."

    #show Grace annoyed
    g "Really? A summons? I have work to do. Would it have killed her to just stop by my lab instead of calling on me like a maid?"
    #Grace walks out of the room.
    jump chambers
 
label chambers:
    show Tosh neutral
    $ time_ref = "17:16"
    $ loc_ref = "Conclave Reception"
    show bg conclaveWaitingRoom
    with fade
    #Grace arrives in the chambers and is greeted by a secretary VI.
    secretary "Welcome, GRACE FORTRAN. Please wait here until the council is ready to assist you."
 
    menu:
        "Thank her.":
            jump thanks
        "Shrug her off.":
            jump shrug
 
label thanks:
    g "Okay! Thanks."
    #secretary perks up and smiles at Grace
    secretary "You are most welcome. Help yourself to some complimentary tea."
    #cup of tea appears
    #cup of tea description: The leaves were picked from the lush atmosphere inside of the Noah Sphere's bio dome.
    #maybe another term other than bio dome?
    #Grace takes a sip
    g "Thank you."
    jump prologueResume1
 
label shrug:
    #show Grace snarky
    g "Yeah, like I've never been here before. I know the drill."
    #Grace walks away and takes a seat
    secretary "Um..."
    #show Grace annoyed
    g "What?"
    secretary "Please enjoy a complimentary tea!"
    g "As long as you stop talking to me."
    #cup of tea appears
    #cup of tea description: The leaves were picked from the lush atmosphere inside of the Noah Sphere's bio dome.
    #maybe another term other than bio dome?
    #Grace takes a sip
    jump prologueResume1
 
label prologueResume1:
    #off screen dialogue from the conclave ensues.
    show bg conclaveDoor
    with fade
    h "...with Alpha deceased, Ada is growing agitated and pushing for answers. We need to gain a grip on her and keep an eye on the other three elder AI's."
    h "Colossus is keeping everything quiet but there's only so much we can keep the lid on."
    h "Alpha was, after all, the first of them to acquire a physical form. There's the risk of an upset. How is Blue handling this?"
    knuth "Blue is concerned, but she's holding her own. No excessive misdoings or demands for justice." 
    knuth "Just curiosity and I think anguish, but it's hard to tell with her. She just expressed a sad face and then exploded with other random emoticons."
    h "I expected as much. And Watson?"
    knuth "Well, you know Watson. He's difficult to get in touch with." 
    knuth "Probably off gallivanting in some system, having a grand old time and unaware of what's happening at home base. AWOL as usual."
    neva "Well at least we don't have to worry about him for now. He'd probably get in the way somehow."
    h "He certainly would. When he resurfaces, however, we'll want to get in touch." 
    h "Don't forget. And we have the project leads suspended until further notice, correct?"
    cray "Yes, Director."
    h "When will the investigators be here?"
    cray "Twenty-four hours, madame."
    h "Right. Please ensure that no one will get in their way. Speaking of, Grace should be here by now."
 
    #the doors open. Grace stumbles into the room to be greeted by the Director and the four chiefs
    #show hirose neutral (?)
    $ time_ref = "17:24"
    $ loc_ref = "The Conclave"
    show bg conclave
    with fade
    h "Ah, hello, Grace. Eavesdropping at the door? How mature of you."
    
    #show Grace frustrated
    g "What's going on? What happened to Alpha?"
    
    h "Once your tone takes on a less hysterical note, we'll discuss."
    
    g "Don't tell me what to do. I want to know what happened to the AI I was working with."
    #show godel neutral
    godel "That's not the proper way you speak to the Director."
    g "Mind your business."
    godel "Well, I never."
    g "Yeah, yeah. Tell me what's going on."  
    #show hirose annoyed (?)
    h "That's enough. We are not exactly certain of the events that transpired at this time, but unfortunately Alpha is no longer with us."

    #show grace surprised/sad
    g "But how? I tracked his transition, he was completely processed, everything was working perfectly..."
    
    #show cray neutral
    cray "That's what we don't understand, Alpha was--"
    h "Like I stated, we are not positive of the reason yet. We are having a team of external investigators coming to inspect the situation."
    g "What? Why external investigators? We couldn't keep this among our own?"
    h "Almost everyone on the station worked with Alpha." 
    h "We need an unbiased examination of the crime scene and interrogation of all those involved to truly determine what, or who, was at fault."
    g "His neural network was fine yesterday. Was there a glitch somewhere?" 
    g "Any type of malfunction should have been caught in the system. I just can't believe it."
    cray "We can't either, we--"
    h "Grace, you were summoned today because of your involvement with Alpha's process."
    h "Your research shall be suspended until we have a clearer image of what happened to Alpha."
    #show grace angry
 
    menu:
        "Continue asking questions.":
            jump lessobvious
        "Argue with Hirose.":
            jump sassy
 
label lessobvious:
    g "But how long is it going to take for the investigators to come? This is time sensitive."
    h "We are aware of the sensitivity of the matter, believe me. They are scheduled to come in approximately 18 hours."
    g "What?!"
    h "This isn't up for debate, Grace. You will stay out of your lab and remain in your living quarters until the investigation is over." 
    h "Until then you will have restricted access to the conclave and labs."
    #show Grace annoyed
    g "But did you check his charts? Did you search through his databanks?" 
    g "Did you look for anything that might suggest what could've occurred?"
    h "We're leaving that up to the investigators to figure out. As for you, please heed my advice and do as I say." 
    h "Stay out of this and leave it to the professionals."
    g "Alright, fine. Keep me informed, though. I want to know what happened."
    jump prologueResume2
 
label sassy:
    g "You've got to be kidding me. My research could help discover what happened to him."
    h "You're a suspect. This isn't an argument. Your work can wait until the investigation is over."
    #show Grace angry
    g "I want to know what happened to Alpha. I have a right as one of the researchers who worked with him as well as on his cyborg body." 
    g "This isn't fair. Waiting for such a long amount of time is wasted resources."
    h "You'll stay out of this and let the investigators do their job."
    g "This is ridiculous. You're not doing enough!"
    #show director irritated
    h "Grace. You are not to be involved, and that's final."
    #stare down between Grace and Hirose
    g "Okay, fine."
    #show Grace snarky
    #under her breath
    g "{i}We'll see about that.{/i}"
    jump prologueResume2
 
label prologueResume2:
    #Grace exits room
    #Grace enters her lab to be greeted with the sight of ADA in humanoid form
    #show Grace surprised
 
    g "What the... Who are you? And what do you think you're doing in my lab?"
    #show Ada neutral
    a "Grace, it's Ada. You know, the other AI you've been working with." 
    a "The one who isn't dead. I've uploaded myself into a physical form to solve the destruction of my friend."
    a "I cannot accomplish as much as I would've liked without the physical advantage you humans have."
    #show Grace annoyed
    g "Oh, give me a break. An AI just died, and now I've got another one in my office?" 
    g "Do you know how much trouble I'm gonna be in if someone finds you in here? I've got enough on my plate right now."
    a "I'm not sure I care. That AI wasn't just my associate, but my friend. Alpha's dead and I need to know what happened to him."
    #show Grace surprised
    g "Yeah, I understand that his death is a tragedy, but a lot is going on right now. The conclave is shutting down the lab and everything."
    g "They're bringing outside investigators to find out what happened to him. I wanna know what happened too, but we've got strict orders from Hirose-"
    #show Ada concerned
    a "When do the investigators come?"
    g "18 hours."
    a "That's more than enough time."
    g "Time for what? What are you thinking?"
    a "If you wish to help me, then we'll find a way to go around them. Are you with me?"
 
    menu:
        "Agree, but make it clear Ada knows who's boss.":
            jump boss
        "Agree.":
            jump together
        "Agree reluctantly.":
            jump reluctant
            
label boss:
    g "Alright, but I'll lead this. I'm not taking the fall for you if we happen to get caught."
    #show Ada frustrated
    a "Well okay then. I don't know how that's relevant as I wouldn't expect you to anyway."
    g "Good."
    a "Good."
    jump prologueResume3
 
label together:
    g "Yeah. Let's work together to figure this mess out."
    a "Shall we get to work then?"
    g "Absolutely."
    a "Alright. Let's get to it."
    jump prologueResume3
 
label reluctant:
    g "I guess we could do that. But you know that a human, AKA me, is going to get the boot rather than the sidekick robot."
    #show ada seething
    a "Excuse me? A robot? I'll have you know that I can process faster than you can think. And I'm no one's sidekick."
    g "Okay, okay. Calm down."
    a "I'm the epitome of calm."
    g "Whatever you say."
    jump prologueResume3
 
label prologueResume3:
    #show Grace neutral
    g "First things first, we need credentials. I think that the best place to start would be Director Hirose's residence."
    g "We need to acquire her credentials to access the crime scene."
    #They start to leave. Ada stumbles.
    #Have SFX here
    a "It might take me a moment to get used to walking."

    #End of prologue
    jump chapterOne
    # ... more code goes here ...