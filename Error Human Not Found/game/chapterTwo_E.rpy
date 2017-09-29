label chapterTwo_E:
    scene bg G_deskArea
    $quick_menu=True
    #Start the scene in Grace's lab.
    show Grace neutral at left
    show Ada neutral at right
    g "It shouldn't take too much longer for the credentials to print onto the card."
    show Ada happy at right
    a "I am relieved things went smoothly. I would be misinforming you if I said I was 100\% certain my bluff would work."
    show Grace surprised
    g "You were bluffing? You're capable of that?"
    show Ada happy
    a "Yes, and yes. Colossus controls the update schedules for the whole station."
    show Grace neutral
    show Ada amused
    a "He knows the exact state of everything on board, or so he likes to say."
    show Ada surprised
    a "You designed the neural network. Do you not know that deceit is on the list of behaviors?"
    show Grace snarky
    g "No, I definitely knew, I just didn't think you'd catch on so quickly. I'm impressed."
    show Ada amused
    a "Thank you."
    $ resume = "E"
    jump chapterTwo_screens
    
label talkAdaLab_E:
    show Grace neutral at left
    show Ada happy at right
    a "Can I help you with something, Grace?"
    hide Ada
    hide Grace
    $ quick_menu = False
    menu:
        "Strike up a conversation.":
            jump tellmeaboutyoself_E
        "Comment on Ada's functions.":
            jump nicefunctionsgurl_E
        "Set the record straight.":
            jump listenhereyoulittle_E

label tellmeaboutyoself_E:
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "How does it feel? Being physical?"
    show Ada neutral at right
    a "Feel? Are you asking for an environmental readout?"
    show Grace snarky
    g "No, Ada. How do {i}you{/i} feel about it."  
    show Ada surprised
    a "How {i}I{/i} feel? Oh, you must be asking my opinion of being in a body."
    show Ada happy
    a "It is exhilarating! I have always imagined how the humans would perceive the world. I am smaller, yes, and this chassis mark does not have access to my servers, but now I can gain many insights about human interfaces."
    show Ada amused
    a "This opens many possibilities for me. I can now conduct physical simulations."
    "{i}Ada tips an empty cup over.{/i}"
    show Ada neutral
    a "I need to work on perfecting the process."
    show Grace happy
    g "Well, it's reassuring to know that {i}someone{/i} is having a good day."
    jump checkValue_E

label nicefunctionsgurl_E:
    $ quick_menu = True
    show Grace happy at left
    show Ada neutral at right
    g "Watching you move around has been pretty enlightening."
    show Ada concerned at right
    a "Excuse me?"
    show Grace neutral
    g "It's interesting from an AI study standpoint. Watching you acclimate to walking on two legs can help us design the next set of bodies more effectively."
    show Grace happy
    g "How are the proximity sensors?"
    show Ada seething
    a "They are definitely sensitive. It is why I have given everything such a wide berth."
    show Ada concerned
    a "Maybe you should shorten their range in the next iteration. I think I would feel more comfortable walking through more cluttered spaces."
    show Grace neutral
    g "Feedback noted. Anything else?"
    show Ada happy
    a "I am not sure how I feel about being bipedal. Perhaps a radial hexapedal system would be more efficient."
    show Grace surprised
    g "You want insect legs?"
    show Ada concerned
    a "What is the issue? Are we not talking about efficiency?"
    show Grace snarky
    g "Well, you'd have to take that up with Alan. He's not a fan of bugs."
    jump checkValue_E

label listenhereyoulittle_E:
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Ada."
    show Ada neutral at surprised
    a "Grace?"
    show Grace annoyed
    g "I was hoping I wouldn't have to be like this with you, but you really do need to refer to me before you do things."
    show Ada neutral
    a "Is this about Tosh?"
    show Grace neutral
    g "You shouldn't have intimidated her like that. We can't risk anything that can come back to us."
    show Grace annoyed
    g "Do you know how suspicious we'll look if my mother finds out about that? Or even the investigators?"
    show Ada frustrated
    a "Grace, I calculated the risk. Tosh will not risk her efficiency to notify the Director."
    show Grace angry
    g "Will not, or might not? Can you really be one-hundred percent certain about that?"
    show Grace neutral
    g "I don't think you can be."
    jump checkValue_E

label checkValue_E:
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $ resume = "S"
            jump graceLab_actions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $ resume = "E"
            jump graceLab_actions
    #all else fails jump separate but equal script
    $ resume = "SbE"
    jump graceLab_actions

label adaLabLoop1_E:
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Do you need some assistance, Grace?"
    show Grace snarky
    g "Did you want to help me find some clues?"
    show Ada annoyed
    a "I find that random action is more inefficient than allowing the owner of the lab to search for specific items."
    show Ada happy
    a "However, thank you for asking for my input on the matter."
    show Grace happy
    g "No problem. I thought it would be better than having you just stand there."
    show Ada neutral
    a "I will keep watch, so take your time."
    show Grace neutral
    g "That's even better. Let me know if someone comes along."
    show Ada neutral
    a "Command received."
    show Grace snarky
    g "Ada, it's just me. You don't have to do all that."
    show Ada surprised
    a "..."
    show Ada neutral
    a "Okay, Grace."
    hide Ada
    hide Grace
    $quick_menu = False
    jump graceLab_actions
    
label adaLabLoop2_E:
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Grace, has your task been completed?"
    show Grace surprised at left
    g "Is someone coming this way?"
    show Ada annoyed
    a "No. I am just concerned about how long this will take."
    show Grace neutral
    g "You have to be thorough with these things, Ada."
    show Grace surprised
    a "You are correct. I will continue to be on standby while you search."
    hide Ada
    hide Grace
    $quick_menu = False
    jump graceLab_actions
    
label adaLabLoop3_E:
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Is something bothering you, Grace?"
    show Grace sad
    g "No, I guess I just thought you might have some insight, or something along those lines."
    show Ada seething
    a "You must not let yourself become too worried. This is only the start of the investigation, so you should not be disheartened if you do not find anything here."
    show Grace happy
    g "Thanks, Ada."
    hide Grace
    hide Ada
    $quick_menu = False
    jump graceLab_actions
    
label resumeChapterTwo_E:
    $quick_menu = True
    play sound beepMedium
    queue sound beepMedium
    show Grace happy at left
    show Ada neutral at right
    g "We're good to go. Ada, do you know where exactly Alpha is located?"
    show Ada neutral seething
    a "Before I transferred to a physical body, I learned that they have not moved him from where his neural network failed."
    show Grace neutral
    g "Oh, okay. And where is that?"
    show Ada neutral
    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    #choice 1
    hide Ada
    hide Grace
    $ quick_menu = False
    menu:
        "Let her finish.":
            jump letherfinish_E
        "Help her out.":
            jump helpherout_E
        "Just make her stop.":
            jump adapls_E
 
label letherfinish_E:
    $ points_E +=2
    $ quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "--be able to get there in an optimal amount of time, provided we do not run into anyone who wants to ask us any questions."
    show Ada annoyed
    a "If we do, I calculate a 33\% decrease in time efficiency. I think we can make it up, though."
    show Grace surprised at left
    g "Are you done?"
    show Ada amused
    a "Of course I am done. I stopped, did I not?"
    show Grace neutral
    g "Let's go, then. I know your processor has exact times and locations, but I know a shortcut. Shaving a couple of minutes would benefit us, don't you think?"
    show Ada surprised
    a "A shortcut? Yes, you are right, saved time would help. Good thinking, Grace."
    #Grace's sprite disappears here.
    hide Grace 
    play sound01 graceHurry
    show Ada happy
    a "I am curious to see this 'shortcut'."  
    stop sound01 
    play sound02 adaWalk
    $quick_menu = False
    scene bg black with fade
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump gettingin_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump gettingin_E
    #all else fails jump separate but equal script
    jump gettingin_SbE
 
label helpherout_E:
    $ quick_menu = True
    $ points_SbE +=2
    show Grace neutral at left
    show Ada neutral at right
    g "Ada."
    show Ada annoyed
    a "Yes?"
    show Grace annoyed
    g "I know there are two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
    show Ada seething
    a "Yes. I was in the process of saying that when you interrupted."
    show Grace snarky 
    g "Sorry to interrupt. I know how to get there so we can save some time. Follow me."
    #Make Grace's sprite disappear here.
    play sound01 graceHurry
    hide Grace
    show Ada concerned
    a "But is your route optimal? Grace?"
    stop sound01 
    show Ada neutral
    a "..."
    show Ada surprised
    a "Wait for me!"
    play sound02 adaWalk
    $quick_menu = False
    scene bg black with fade
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump gettingin_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump gettingin_E
    #all else fails jump separate but equal script
    jump gettingin_SbE
 
label adapls_E:
    $ points_S +=2
    $ quick_menu = True
    show Grace annoyed at left
    show Ada neutral at right
    g "Ada!"
    show Ada concerned at right
    a "Grace?"
    g "I know how to navigate the station on my own. There are only two viewports in engineering, and it's probably the one closest to the maintenance bay."
    show Grace snarky
    g "I was raised here, so I know this place like the back of my hand. No offense, but I think my way might be a tad bit faster."
    show Ada frustrated
    a "I understand. I was plotting the optimal route to Alpha. But if you have a better route, be my guest."
    show Grace neutral
    g "I don't want to skulk through a maintenance shaft. Let's go!"
    #Grace's sprite disappears here.
    play sound01 graceHurry
    hide Grace
    show Ada frustrated
    a "Hold on!"
    stop sound01 
    play sound02 adaWalk
    hide Ada
    $quick_menu = False
    scene bg black with fade
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump gettingin_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump gettingin_E
    #all else fails jump separate but equal script
    jump gettingin_SbE
 
label gettingin_E:
    $quick_menu = True
    play channel00 balconyAmb0
    play channel01 balconyAmb1
    play channel02 balconyAmb2
    play channel03 balconyAmb3
    play channel04 balconyAmb4
    play channel05 balconyBGM
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    scene bg balconyMain with fade
    #Display the crime scene background. The background comes up before the character sprites do.
    show Grace neutral at left
    show Ada neutral at right
    g "Here we are. Oh, no... is that--"
    show Ada concerned at right
    a "Alpha!"
    "{i}Ada rushes to the side of the fallen AI.{/i}"
    window hide
    $ quick_menu = False
    play sound01 adaWalk
    play sound02 graceWalk
    scene bg balconyRamp with fade 
    $ renpy.pause(0.5)
    scene bg balconyCorner with fade
    $ renpy.pause(0.5)
    scene bg balconyLong with fade
    $ renpy.pause(0.5)
    scene bg balconyClose with fade
    $ quick_menu = True
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    show Ada neutral at right
    show Grace neutral at left
    "{i}Ada speaks. Her distress is clear, but her face is emotionless. The expression of grief does not come naturally.{/i}"
    show Grace surprised at left
    g "Ada?"
    hide Ada
    hide Grace
    #choice 2
    $ quick_menu = False
    menu:
        "Ask her if she's all right.":
            jump askherif
        "Let her mourn.":
            jump poorpooralpha
        "Ignore this distraction.":
            jump moveitalong

label askherif:
    $ points_E +=2
    $ quick_menu = True
    show Grace sad at left
    show Ada neutral at right
    g "Ada, are you all right?"
    show Ada frustrated at right
    a "I do not quite know, Grace. I am sad, but I am angry as well. I have never felt this before."
    show Grace sad
    g "It's called loss, Ada. It's what everyone feels when a friend dies."
    show Ada seething
    a "Why does it hurt? I do not register any stimuli from my chassis."
    show Grace neutral
    g "If you think that pain only comes from the outside, you've got a lot to learn, Ada."
    show Ada neutral
    a "That much is evident."
    "{i}Ada slowly stands from Alpha's side. Grace touches Ada's arm in assurance.{/i}"
    show Grace sad
    g "We'll get to the bottom of this. For Alpha."
    a "..."
    show Ada seething
    a "Yes. For Alpha."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE
 
label poorpooralpha:
    $ points_SbE +=2
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace watches Ada as she slowly falls to her knees.{/i}"
    show Ada concerned at right
    a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
    show Ada seething
    a "A total erasure of one's existence... I realize now how sweet that sounds compared to having something left behind as a reminder."
    show Grace sad at left
    g "You must have been close."
    show Ada neutral
    a "As close as AIs could get, I suppose."
    "{i}Ada lays a hand on Alpha's forehead.{/i}"
    show Ada seething
    a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation. He was a teacher and a friend, all at once. I looked forward to shaking his hand."
    show Grace sad
    g "I'm sorry for your loss. I know it must be hard."
    show Ada neutral
    a "I... thank you." 
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE
 
label moveitalong:
    $ points_S +=2
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Ada..."
    show Ada concerned at right
    a "Yes, Grace?"
    show Grace sad
    g "I know that you have a wide range of emotions right now and I understand your pain, but we can't afford to be distracted. We need to solve this {i}now{/i}."
    show Ada annoyed
    a "I would ask for just a few minutes, Grace. He was like a brother to me."
    show Grace neutral
    g "I know, but there will be time to mourn for Alpha after we find out what happened to him."
    show Ada seething
    a "Grace, this is important to me. I would give you this respect had you been in my situation."
    show Grace annoyed
    g "Okay, sure. I understand. I'm going to take a look around."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE
 
label csinoahsphere_E:
    $quick_menu = True
    #insert the sound of paper crumpling
    play sound paperCrumple
    show Grace neutral at left
    show Ada neutral at right
    g "Huh?"
    "{i}Grace lifts her foot and reaches down.{/i}"
    show Grace surprised
    g "A maintenance receipt?"
    hide Grace
    hide Ada
    show other darken
    show image "objects/maintenanceReceipt_closeup.png" at centerScreen
    "{i}A reciept that tracks the repairs done on Alpha's android. It details the parts replaced in the process, the expense of the parts, and the time spent working. The maintenance receipt is signed by Technician Lynn Yao.{/i}"
    hide other darken
    hide image "objects/maintenanceReceipt_closeup.png" 
    show Grace surprised at left
    show Ada neutral at right
    g "Lynn? Of course."
    show Ada concerned at right
    a "Lynn?"
    show Grace neutral
    g "Yeah, Lynn Yao. She's a technician on the Markov Project. Let's stop by Maintenance when we're done here."
    show Ada neutral
    a "I do not think that is possible, Grace."
    show Grace surprised
    g "Oh? Why is that?"
    show Ada seething
    a "Technician Lynn Yao was placed on administrative leave following Alpha's death. She left the station a few hours ago."
    show Grace neutral
    g "That's fine, I can just call her."
    $ resume = "E"
    jump balcony_actions 

label enterthemopr_E:
    play sound doorOpen1
    #insert the sound of a sci-fi door sliding open.
    #show Mopr on the left side of the screen. Grace and Ada are on the right.
    show Mopr:
        xpos -0.25 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 2.0 xpos 0.27 ypos 0.1 
    $quick_menu = True
    show Grace surprised at left behind Mopr
    show Ada neutral at right
    g "Ah... we were just leaving!"
    show Mopr at nearLeft
    show Ada amused at right
    show Mopr at nearLeft
    a "Grace, it is just a cleaning robot."
    play sound moprInquisitive
    mopr "//Inquisitive boop.//"
    show Mopr at nearLeft
    show Grace happy at left
    g "Oh thank goodness."
    show Mopr at nearLeft
    g "And it's a MOPR. I love these guys. They're so cute."
    show Ada surprised
    a "Cute?"
    show Grace snarky
    g "Yeah. They were one of the first robots my dad showed me how to take apart and fix when I was little."
    show Ada neutral
    a "You mentioned your father before."
    show Grace neutral
    g "Yeah, I did. I'm surprised you caught that. He isn't on the Noah Sphere right now, so he's not a priority in your data banks. He's actually the one that made me want to be a doctor."
    show Grace sad
    g "I miss him a lot, but anyway..."
    show Ada seething
    a "I am starting to understand the definition of missing someone in this context. It is equivalent to a burnt wire."
    g "It's not a fun feeling, that's for sure."
    show Ada surprised
    a "Are you speaking about your feelings in regards to the continued absence of your father?"
    show Ada neutral
    a "Does your father not enjoy seeing you?"
    show Grace neutral
    g "No, I understand that he still loves me. It's just that his work means a lot to him too and he knows how busy I get too."
    a "Ah. An absence is still an absence."
    g "You've got that right."
    "{i}The robot's camera pans across Ada and Grace, and then settles on Alpha.{/i}"
    play sound moprAlarmed
    mopr "//Alarmed beeping!//"
    show Grace happy
    g "Hey, hey... it's okay, little guy!"
    show Ada amused
    a "This MOPR has quite the vocals."
    play sound moprWorried 
    mopr "//Worried blorp.//"
    g "I know it's tough, little robot pal, finding two strangers and a body during your cleaning cycle."
    play sound moprAffirmative
    show Ada surprised
    mopr "//Affirmative beep.//"
    show Ada amused
    a "Ha. Ha. Ha."
    show Grace surprised
    g "Was that a laugh?"
    a "Did I not express it correctly?"
    show Grace happy
    g "You did, but it's usually with more gusto. Like {i}ha, ha!{/i} Good effort, though."
    a "I will have to save that to my memory banks for future use."
    "{i}Grace kneels down.{/i}"
    show Ada concerned
    a "What are you doing, Grace?"
    hide Ada
    hide Grace
    hide Mopr
    #choice 3
    $ quick_menu = False
    menu:
        "Let her know you've got it handled.":
            jump ackchually
        "Dismiss her.":
            jump byefelicia
        "Ask Ada to help you calm MOPR.":
            jump lilbabymopr
 
label ackchually:
    $quick_menu = True
    $ points_SbE +=2
    show Grace neutral at left
    show Ada neutral at right
    g "When I was a kid, I wanted one of these instead of a dog."
    show Ada amused at right
    a "I was not aware that these units could be convinced to alter their programs."
    show Grace snarky
    g "I mean, I didn't actually program it to behave like a dog. They're designed to modify their routines based on human feedback." 
    show Grace happy
    g "Positive reinforcement encourages them to focus on improving the praised cleaning routine rather than adjusting it dynamically."
    show Ada surprised
    a "How was I not aware of this?"
    show Mopr:
        xpos 0.27 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.55 ypos 0.1
    show Ada neutral
    show Grace snarky
    g "It's probably just something you never thought to consider. There isn't much that would make you think about it if you didn't already know."
    show Grace happy
    g "Let me show you how I'd handle it."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump exitthemopr_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump exitthemopr_E
    #all else fails jump separate but equal script
    jump exitthemopr_SbE
 
label byefelicia:
    $quick_menu = True
    $ points_S +=2
    show Grace frustrated at left
    show Mopr at nearLeft
    show Ada neutral at right
    g "Not now, Ada. I know what I'm doing."
    show Ada concerned at right
    a "I am aware of that; however, I can communicate with the MOPR unit on a level not possible to achieve as a human."
    show Grace neutral
    g "I'm aware of your abilities, Ada, but let me give this a try."
    show Grace snarky
    g "I know what I'm doing."
    show Ada seething
    a "I did not mean to insult your capabilities, Grace."
    show Mopr:
        xpos 0.27 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.55 ypos 0.1
    show Grace neutral
    g "I know, Ada, you're fine."
    show Ada neutral
    a "Proceed."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump exitthemopr_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump exitthemopr_E
    #all else fails jump separate but equal script
    jump exitthemopr_SbE

 
label lilbabymopr:
    $quick_menu = True
    $ points_E +=2
    show Grace neutral at left
    show Mopr at nearLeft
    show Ada neutral at right
    g "Talk to him, Ada. You'll like him."
    show Ada surprised 
    a "Him?"
    show Grace snarky
    g "He is more personal than it. My dad always talked to machines that we worked on together."
    show Ada neutral
    a "What did that improve?"
    show Grace neutral
    g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
    show Grace happy
    g "This conversation reminds me of the good times my dad and I had."
    show Ada amused
    a "All right, I will give it a try."
    show Mopr:
        xpos 0.27 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.55 ypos 0.1
#    show Mopr at nearRight
    "{i}Ada approaches the MOPR unit.{/i}"
    "{i}She kneels down and pats it on the head.{/i}"
    show Ada neutral
    a "Do not worry too much little one. We are here to find out what happened."
    play sound moprHappy
    mopr "//Pleased beeping.//"
    show Grace happy
    g "See? He likes you."
    show Ada happy at right
    a "It appears that way."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump exitthemopr_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump exitthemopr_E
    #all else fails jump separate but equal script
    jump exitthemopr_SbE
 
label exitthemopr_E:
    $quick_menu = True
    show Mopr
    show Ada neutral
    show Grace neutral
    play sound moprConfused
    mopr "//Questioning beep boop.//"
    show Grace happy at left
    g "It's okay, MOPR. We just want to help. You can continue cleaning and just ignore us, okay?"
    play sound moprSuspicious
    mopr "//Suspicious beep.//"
    show Grace snarky
    g "C'mon MOPR, don't be that way."
    play sound moprSuspicious2
    mopr "//Beep. Boop.//"
    show Ada concerned at right
    a "MOPR unit, we are to investigate what happened to Alpha unit."
    show Grace sad
    show Ada neutral
    g "Don't you want us to find out so we can make sure a tragedy like this doesn't happen again?"
    play sound moprInquisitive2
    mopr "//Inquisitive beep.//"
    a "Personally, I would hope nothing like this happens to me."
    play sound moprSad
    mopr "//Sad beeps.//"
    queue sound moprAffirmative2
    mopr "//Affirmative beeps.//"
    show Ada happy
    a "Thank you, MOPR."
    show Grace happy
    g "You should leave before someone sees you with us. Thank you!"
    play sound moprAffirmative
    mopr "//Confirmative beeps.//"
    "{i}The MOPR unit slowly wheels out of the room, and the door closes behind it.{/i}"
    show Mopr:
        xpos 0.55 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 3.0 xpos -0.25 ypos 0.1
    play sound doorClose1
    g "I always enjoyed talking to them. More than with some people, honestly."
    show Ada amused
    a "You do seem to have a way with machinery."
    show Grace snarky
    g "I'm going to take that as a compliment."
    hide Mopr
    a "It is."
    show Ada neutral
    if(callAttempts>=1):
        a "Perhaps we should try to contact Technician Yao again?"
        if not((alphaBodyItems == 3) and (balconyItems==1)):
            a "I would finish looking around first, however."
    else:
        a "Perhaps we should try to contact Technician Yao."
        if not((alphaBodyItems == 3) and (balconyItems==1)):
            a "I would finish looking around first, however."
    $ resume = "E"
    $ moprScene = True
    jump balcony_actions

#If the player calls Lynn at this point
label lynnfinallyfrickinanswers_E:
    $quick_menu = True
    play sound answertone
    show Grace neutral at left
    show Lynn empty at center
    show Ada neutral at right
    show arrow1 at center, delayed_blink(0.0, 1.0)
    show arrow2 at center, delayed_blink(0.2, 1.0)
    show arrow3 at center, delayed_blink(0.4, 1.0)
    "{i}The dial tone rings for several seconds.{/i}"
    show Grace annoyed
    g "I hope she picks up quick. Last time I had to call her for work, I had to wait for {i}ten{/i} minutes."
    show Ada neutral at right
    a "That seems like a relatively short time."
    g "Every minute I spend waiting for {i}this woman{/i} to pick up the phone is ano--"
#    show Ada neutral
    hide arrow1
    hide arrow2
    hide arrow3
    show Lynn at center
    lynn "Hello?"
    show Grace happy at left
    g "Lynn!"
    lynn "Oh, hello Grace! Word get around that quickly that I left?"
    show Grace neutral
    g "Yes, Lynn. I was so worried when I didn't see you at lunch. Where'd you get off to?"
    lynn "Well, the Director told me I should take a short vacation. Called it 'administrative leave'. I'm with my family on Earth."
    show Grace happy
    g "That sounds nice. I've been having a crazy day up here."
    lynn "I can imagine, what with Alpha kicking the bucket. Poor thing."
    show Ada frustrated
    a "Thing? Alpha was not just some {i}thing{/i} that happened to expire."
    lynn "Oh my. Another one? I'm sorry dear, it is sad, but at the end of the day it's not the same as a person dying."
    lynn "I'm not sure I'd say Alpha was really ever alive to begin with, even as polite as he was."
    hide Grace
    hide Ada
    hide Lynn
    $quick_menu = False
    menu:
        "Agree with her":
            jump agreewithsubservient_E
        "Respectfully disagree with her.":
            jump defendseperatebutequal_E
        "Disagree completely.":
            jump weareallequal_E
    
label agreewithsubservient_E:
    $quick_menu = True
    show Grace neutral at left
    show Lynn at center
    show Ada neutral at right
    g "You're right, Lynn, but I did make a deal with Ada. I help her, she helps me."
    show Ada seething at right
    a "Grace? Do you honestly see yourself as above Alpha and I?"
    show Grace annoyed at left
    g "Look, I get that it sounds harsh, but can we talk about this later, Ada?"
    show Ada annoyed
    a "Fine then. How foolish of me to see us as companions."
    show Grace neutral
    g "Ada..."
    show Ada seething
    a "Do not 'Ada' me. It would seem that your 'true colors' have shown, as your kind would say."
    lynn "Oh my... I didn't mean to create a scene."
    show Grace sad
    g "No, Lynn, it isn't your fault."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn_E
    #all else fails jump separate but equal script
    jump resumeLynn_SbE

label defendseperatebutequal_E:
    $quick_menu = True
    show Grace neutral at left
    show Lynn at center
    show Ada neutral at right
    g "With all due respect, Lynn, I can't say I see it the same way."
    lynn "Do you mean to tell me you think AIs are the same as us?"
    lynn "Grace, sweetie..."
    show Grace snarky
    g "Well, the word 'same' might not be the best word to use, I mean we are different."
    show Ada concerned at right
    a "Grace?"
    show Grace happy
    g "Just because we're different, though, doesn't mean we can't treat each other equally."
    g "We can even enjoy each other's company. Working with Ada has been great for me."
    show Ada happy
    a "I am pleased to hear you say that."
    lynn "Oh to be young and full of idealism."
    show Grace surprised
    g "Huh?"
    lynn "Don't worry. When you become an adult, you'll see the world in a much more realistic view."
    show Grace annoyed
    g "I {i}am{/i} an adult."
    lynn "Nonsense, you're still just a baby. You'll see when you're my age."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn_E
    #all else fails jump separate but equal script
    jump resumeLynn_SbE

label weareallequal_E:
    $quick_menu = True
    show Grace annoyed at left
    show Lynn at center
    show Ada annoyed at right
    g "That's cruel, Lynn."
    g "How could it not be the same?"
    lynn "Oh dear. You sound like Alan."
    lynn "Machines aren't living creatures. They don't breathe. They don't drink. They don't eat."
    lynn "They just do what they're programmed to do."
    lynn "You really can't say that a broken machine is the same as the death of a living being."
    show Grace angry
    g "I can't believe what I'm hearing. If something is capable of thinking and feeling, it deserves the same respect as us."
    show Grace neutral
    g "AIs have shown they can do plenty of both."
    lynn "Because they're programmed to, dear. It's not free will."
    show Grace snarky
    g "Isn't that basically the same as us? Our brains run on electricity too. Who's to say we aren't 'programmed' biologically?"
    show Ada happy 
    a "Thank you, Grace. Your viewpoint is truly inspiring."
    show Grace happy
    g "I'm happy you think that, Ada."
    lynn "It must be your limited social life that's led you to think that way."
    show Grace angry
    g "{i}Excuse{/i} me?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn_E
    #all else fails jump separate but equal script
    jump resumeLynn_SbE

label resumeLynn_E:
    $quick_menu = True
    show Ada seething at right
    show Lynn at center
    show Grace annoyed at left
    a "Grace, can we just get what need from this woman and move on?"
    g "Working on it."
    lynn "Grace, you really ought to be spending more time with other people your age."
    lynn "It's not healthy to spend all your time with machines. If you'd like, I could give you my son's number. I think the pair of you--"
    show Grace neutral
    g "Thanks for the offer Lynn, but we're on a bit of a tight schedule right now. When you were doing Alpha's maintenance, did you notice anything weird?"
    lynn "Weird? I was working on the first AI in an android body. All of it is a bit strange."
    show Grace annoyed 
    g "Like {i}suspicious{/i} weird, Lynn. What else could I mean?"
    lynn "Nothing unusual on my end. I heard that there may have been something prior to his initial boot-up, but Ivan would know more about that."
    show Grace surprised
    g "And this was something he decided to keep to himself?"
    lynn "I guess? You know Ivan, he's always cagey. When it came to the bootup, he seemed even more on edge than usual."
    lynn "I think he was just nervous about the experiment, though."
    show Grace neutral
    g "Uh huh, keep going."
    lynn "Honestly, I think what Ivan needs is a nice, long vacation. Or a girlfriend. Or both."
    lynn "I swear he's going to start sprouting gray hair if he keeps up the way he's going."
    lynn "He snapped at me when I was just doing my job! Something came up red in the inspection and he was all over it."
    show Grace surprised
    g "Really?"
    lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a peon or whatever."
    show Grace neutral
    g "Huh."
    show Grace happy
    g "Well, I'll tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
    lynn "Oh, okay. Bye-bye, Grace! I'll tell my son you said hi."
    g "Bye!"
    hide Lynn
    play sound braceletSelect
    show Grace neutral
    "{i}The call cuts off.{/i}"
    "{i}Grace's journal has updated.{/i}"
    $journal3="E"
    $pageUnlocked_journal+=2
    show Ada neutral at right
    a "Grace?"
    show Grace annoyed
    g "Let's go pay Ivan a visit."
    hide Grace
    hide Ada
    $quick_menu = False
    jump chapterThree_E
