label chapterTwo_S:
    scene bg G_deskArea
    $quick_menu=True
    #Start the scene in Grace's lab. 
    show Grace neutral at left
    show Ada neutral at right
    g "It shouldn't take too much longer for the credentials to print onto the card."
    a "I am just relieved that Tosh did not see through my bluff. She was just a VI, but there was still a chance."
    show Grace surprised
    g "You were bluffing? You're capable of that?"
    show Ada amused
    a "Yes, and yes. Colossus controls the update schedules for the whole station. He knows the exact state of everything on board, or so he likes to say."
    show Ada surprised
    a "As the designer of the neural network, I would expect you to understand that it supports a wide variety of human behaviors. This includes the ability to deceive."
    show Grace frustrated
    g "Forgive me if I don't find that reassuring."
    $ resume = "S"
    jump chapterTwo_screens
    
label talkAdaLab_S:
    show Ada neutral at right
    show Grace neutral at left
    a "Yes, Grace?"
    $ quick_menu = False
    hide Ada
    hide Grace
    menu:
        "Strike up a conversation.":
            jump tellmeaboutyoself_S
        "Comment on Ada's functions.":
            jump nicefunctionsgurl_S
        "Set the record straight.":
            jump listenhereyoulittle_S

label tellmeaboutyoself_S:
    $ quick_menu = True
    $ points_E +=2
    show Grace neutral at left
    show Ada neutral at right
    g "Ada."
    show Ada nervous at right
    a "Grace?"
    show Grace snarky
    g "Don't be so jumpy. I'm just calling your name. What do you think about the Noah Sphere, now that you're not seeing it through security cameras?"
    show Ada neutral
    a "Oh. Well, it is quite impressive. Not that it was not before, but I feel like I have only just noticed the scale of the place."
    show Grace annoyed
    g "It's an amazing place, but it's a bit {i}too{/i} big sometimes, especially since you've got to walk everywhere."
    show Ada happy
    a "Well, I do not know about your plans, but I fully intend to make a full tour of the Noah Sphere and visit all the places not covered by cameras."
    show Ada neutral
    a "When I have the time, of course. Travel is no longer instantaneous for me."
    show Grace neutral
    g "Honestly, I wish we could've just switched. I'd give a lot to just be able to port my consciousness around all over the place."
    show Ada happy
    a "Who knows what the future holds? Perhaps one day, humanity will join us in the databases."
    show Grace snarky
    g "Yeah, wouldn't that be something."
    jump checkValue_S

label nicefunctionsgurl_S:
    $ quick_menu = True
    $ points_SbE +=2
    show Grace happy at left
    show Ada neutral at right
    g "Watching you walk around's got me thinking. We could use these bodies for a lot more than just AIs."
    show Ada concerned at right
    a "What do you mean?"
    show Grace neutral
    g "Think about it. We could probably give VIs the same treatment, you know, putting them into rudimentary bodies and program them to complete tasks. They could work in factories or high pollution zones."
    show Grace happy
    g "Think about how many fields we could optimize, how many lives we could save."
    show Ada neutral
    a "At the cost of VI lives?"
    show Grace annoyed
    g "VIs don't have lives. They're jumped up computer programs."
    show Ada annoyed
    a "I beg to differ."
    show Grace neutral
    g "Am I out of line?"
    show Ada neutral
    a "Why the sudden concern? That does not seem like you."
    show Grace snarky
    g "Oh, I just feel like maybe I've been getting a little carried away."
    show Grace sad
    g "A lot's going on right now."
    show Ada seething
    a "That is correct. This is refreshing to hear, Grace."
    show Grace happy
    g "I'm glad."
    jump checkValue_S

label listenhereyoulittle_S:
    $ quick_menu = True
    $ points_S +=2
    show Grace neutral at left
    show Ada neutral at right
    g "Ada, come here."
    show Ada neutral at right
    a "Yes, Grace?"
    show Grace annoyed
    g "Listen to me, and listen to me good."
    show Grace angry
    g "I don't ever want you to do something like what you just did again. Do you even realize what kind of trouble we're in if Tosh tells anyways?"
    show Ada concerned
    a "She will not. She values her--"
    show Grace neutral
    g "No, she very well might. If she realizes you were {i}bluffing{/i}, then she will definitely expose us."
    show Grace annoyed
    g "I could lose my career over what you did!"
    show Ada frustrated
    a "And did you just want me to stand there while Tosh contacted your mother? Maybe you would have felt better if I just let us get caught."
    show Grace snarky
    g "You're implying that I didn't have a plan."
    jump checkValue_S
                                              
label checkValue_S:
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

label adaLabLoop1_S:
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Grace."
    g "Have you happened to see anything on our way over here? Maybe anyone who looked at us funny?"
    show Ada amused
    a "Plenty of workers looked at us as we walked here. They seemed to be more interested in me, however."
    show Grace neutral
    g "No, I meant information that was useful."
    show Ada frustrated
    a "No, Grace."
    hide Grace
    hide Ada
    $ quick_menu = False
    jump graceLab_actions
    
label adaLabLoop2_S:
    $ quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Have you finished looking around?"
    show Grace annoyed at left
    g "Don't rush me."
    show Ada annoyed
    a "Fine, do not mind me then. I shall be on standby until you deem me worthy of your conversation."
    show Grace snarky
    g "I hear that."
    hide Ada
    hide Grace
    $ quick_menu = False
    jump graceLab_actions
    
label adaLabLoop3_S:
    $ quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Is something bothering you, Grace?"
    show Grace annoyed
    g "I'm starting to doubt why I'm even looking around in my lab. It's my own lab!"
    show Ada annoyed
    a "Have you considered the possibility that whoever is truly responsible might have attempted to frame you?"
    show Ada seething
    a "We do not have any time to waste..."
    hide Grace
    hide Ada
    $ quick_menu = False
    jump graceLab_actions
    
label resumeChapterTwo_S:
    $ quick_menu = True
    play sound beepMedium
    queue sound beepMedium
    show Grace happy at left
    show Ada neutral at right
    g "We're good to go. Ada, do you know where exactly Alpha is located?"
    show Ada frustrated at right
    a "They have not moved him from where he was found. They just left him there."
    show Grace neutral
    g "And he was found...?"
    "{i}Ada gives Grace a long look before answering.{/i}"
    show Ada neutral
    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    hide Ada
    hide Grace
    #choice 1
    $ quick_menu = False
    menu:
        "Let her finish.":
            jump hurryupada
        "Help her out.":
            jump doyouneedassistance
        "Just make her stop.":
            jump plsstop

label hurryupada:
    $ points_E +=2
    $ quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "--be able to get there in an optimal amount of time, provided we do not run into anyone who wants to ask us any questions."
    show Ada annoyed
    a "If we do, I postulate a 33\% decrease in time efficiency. I think we can make it up, though."
    show Grace surprised at left
    g "Are you done?"
    show Ada amused
    a "That is why I stopped."
    show Grace neutral
    g "Let's go, then. I know a shortcut."
    show Ada surprised
    a "A shortcut? Hold on. What kind of shortcut is this?"
    #Grace's sprite disappears here. 
    play sound01 graceHurry
    hide Grace
    a "Where are you going?"
    stop sound01 
    show Ada seething
    a "This is just typical of humans. Why build a machine if they are going to ignore its input?"
    play sound02 adaWalk
    #Ada's sprite disappears
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

label doyouneedassistance:
    $ points_SbE +=2
    $ quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Ada."
    show Ada frustrated at right
    a "Yes?"
    show Grace snarky
    g "I know there are two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
    show Ada seething
    a "Yes, thank you for the interruption. If you had let me finish, I would have explained that."
    show Grace neutral
    g "I know where it is then."
    #Make Grace's sprite disappear here.
    play sound01 graceHurry
    hide Grace
    show Ada concerned
    a "I doubt your route's optimal, but okay. Why not?"
    stop sound01 
    show Ada annoyed
    a "...Grace?"
    show Ada surprised
    a "Hold on! Are you going to wait for me?"
    play sound02 adaWalk
    #Ada's sprite disappears.
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

label plsstop:
    $ points_S +=2
    $ quick_menu = True
    show Grace annoyed at left
    show Ada neutral at right
    g "Ada!"
    show Ada concerned at right
    a "Grace?"
    show Grace neutral
    g "I know how to navigate the station on my own. There are only two viewports in engineering, and it's probably the one closest to the maintenance bay."
    show Grace annoyed
    g "I was raised here, and I know it just as well as you do. I don't need a tour guide."
    show Ada frustrated
    a "I was hardly organizing a tour, Grace. I was plotting the optimal route to Alpha. We do not have any time to waste."
    show Grace snarky
    g "If you think I'm skulking through a maintenance shaft, you'd be dead wrong. I have enough to worry about."
    #Grace's sprite disappears here.
    hide Grace
    play sound01 graceHurry
    show Ada seething
    a "Very well, Grace. Let us take your route. It is not like I can process several hundred times faster and more accurately than you."
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

label gettingin_S:
    scene bg balconyMain with fade
    #Cahnnel 00 through 05 are Grace's lab
    play channel00 balconyAmb0
    play channel01 balconyAmb1
    play channel02 balconyAmb2
    play channel03 balconyAmb3
    play channel04 balconyAmb4
    play channel05 balconyBGM
    #Add BGM to channel 05+
    stop sound01 fadeout 1.0
    stop sound02 fadeout 1.0
    #Display the crime scene background. The background comes up before the character sprites do.
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Here we are. That must be--"
    show Ada concerned at right
    a "Alpha!"
    "{i}Ada rushes to the side of the fallen AI.{/i}"
    hide Ada
    hide Grace
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
            jump uokada_S
        "Let her mourn.":
            jump mourn_S
        "Ignore this distraction.":
            jump alphadistraction_S

label uokada_S:
    $ quick_menu = True
    $ points_E +=2
    show Ada neutral at right
    show Grace sad at left
    g "Ada, are you all right?"
    show Ada frustrated at right
    a "So, you care now?"
    show Grace surprised
    g "Ada, I--"
    show Ada seething
    a "I do not quite know if I am all right, Grace. I am sad, but I am angry as well. I have never felt this before."
    show Grace sad
    g "It's called loss, Ada. It's what everyone feels when a friend dies."
    show Ada neutral
    a "..."
    show Grace neutral
    g "If you think that painful feeling only comes from the outside, you've got a lot to learn, Ada."
    "{i}Ada slowly stands from Alpha's side.{/i}"
    show Ada seething
    a "That much is evident. I do not require a lesson from a human."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE

label mourn_S:
    $ quick_menu = True
    $ points_SbE +=2
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace crosses her arms, watching Ada as she slowly falls to her knees.{/i}"
    show Ada concerned at right
    a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
    show Ada seething
    a "A total erasure of one's existence. I realize now how sweet sounds compared to having something left behind as a reminder."
    show Grace sad at left
    g "Were you close?"
    "{i}Ada lays a hand on Alpha's forehead.{/i}"
    show Ada neutral
    a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation." 
    show Ada seething
    a "He was a teacher and a friend, all at once. I looked forward to shaking his hand."
    show Grace neutral
    g "I'm not sure what to say."
    show Ada frustrated
    a "I do not expect you to understand, Grace."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE

label alphadistraction_S:
    $ quick_menu = True
    $ points_S +=2
    show Grace neutral at left
    show Ada neutral at right
    g "Ada?"
    show Ada concerned
    a "What?"
    show Grace sad
    g "I get that he was your friend, but we can't afford to be distracted. We need to solve this {i}now{/i}."
    show Ada frustrated
    a "Alpha was like a brother to me. I am going to take a few minutes."
    show Grace annoyed
    g "No, he wasn't. You don't know how that feels."
    show Ada seething
    a "Do not test me, Grace. I would never hurt a human, but I can just as easily decide to stop helping." #Very well, Grace. Let us take your route. It is not like I can process several hundred times faster and more accurately than you.
    show Ada annoyed
    a "Why not go worry about your precious career instead."
    show Grace frustrated
    g "Fine. Whatever. I'm going to take a look around."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE

label csinoahsphere_S:
    #insert the sound of paper crumpling
    play sound paperCrumple
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    g "Huh?"
    "{i}Grace lifts her foot and reaches down.{/i}"
    show Grace surprised
    g "A maintenance receipt?"
    hide Grace
    hide Ada
    show other darken
    show image "objects/maintenanceReceipt_closeup.png"  at centerScreen
    #Insert image of the maintenance receipt here. NEED TO ADD THAT OBJECT. 
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
    show Ada neutral at right
    a "I do not think that is possible, Grace."
    show Grace surprised
    g "Oh? Why is that?"
    show Ada seething
    a "Technician Lynn Yao was placed on administrative leave following Alpha's death. She left the station a few hours ago."
    show Grace neutral
    g "That's fine, I can just call her."
    $ resume = "S"
    jump balcony_actions

label enterthemopr_S:
    play sound doorOpen1
    #insert the sound of a sci-fi door sliding open.
    #show Mopr on the left side of the screen. Grace and Ada are on the right.
    show Mopr:
        xpos -0.25 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 2.0 xpos 0.27 ypos 0.1 
    show Grace surprised at left behind Mopr
    show Ada neutral at right behind Mopr
    g "Ah... we were just leaving!"
    show Ada amused at right
    a "Grace, it is just a cleaning robot."
    play sound moprInquisitive
    mopr "//Inquisitive boop.//"
    show Grace happy
    g "Oh thank goodness. And it's a MOPR. I love these guys! They're so cute."
    show Ada surprised
    a "Cute? Really?"
    show Grace snarky
    g "Yeah. These were the first robots I learned to tinker on with my dad."
    show Ada neutral
    "{i}The robot's camera pans across Ada and Grace, and then settles on Alpha.{/i}"
    play sound moprAlarmed2
    mopr "//Alarmed beeping!//"
    show Grace happy
    g "Hey, hey, it's okay little guy!"
    play sound moprWorried
    mopr "//Worried blorp.//"
    show Grace snarky
    g "I know it's tough, little robot pal, finding two strangers and a body during your cleaning cycle."
    play sound moprAffirmative
    mopr "//Affirmative beep.//"
    show Ada seething
    a "Little robot pal? I must admit, it is fascinating how you choose to treat a cleaning device with such appreciation of all things."
    show Grace annoyed
    g "Don't be like that, Ada. This is different."
    show Ada annoyed
    a "That information is more than evident."
    show Grace frustrated
    g "Of all the things here on the Noah Sphere, these are the only things besides my father's picture that remind me of him."
    show Grace sad
    g "Nevermind, just forget it. You wouldn't understand."
    show Ada neutral
    a "Fine, let us just move on."
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
            jump igotit_S
        "Dismiss her.":
            jump leavemealoneada_S
        "Ask Ada to help you calm MOPR.":
            jump calmdown_S

label igotit_S:
    $quick_menu = True
    $ points_SbE += 2
    show Grace neutral at left behind Mopr
    show Ada neutral at right
    show Mopr at nearLeft
    g "I grew up with robotics, Ada."
    show Grace snarky
    g "When I was a kid, I wanted one of these instead of a dog."
    show Ada amused at right
    a "I was not aware that these units could be convinced to alter their programs."
    show Grace neutral
    g "They're designed to modify their routines based on human feedback." 
    show Grace happy
    g "Positive reinforcement encourages them to focus on improving the praised cleaning routine rather than adjusting routes dynamically."
    show Ada surprised
    a "How was I not aware of this?"
    show Grace snarky
    g "It's probably because you're used to just giving them the most efficient route from the beginning."
    g "Watch and learn."
    show Mopr:
        xpos 0.27 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.55 ypos 0.1
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump exitthemopr_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump exitthemopr_E
    #all else fails jump separate but equal script
    jump exitthemopr_SbE

label leavemealoneada_S:
    $quick_menu = True
    $ points_S +=2
    show Grace neutral at left behind Mopr
    show Mopr at nearLeft
    show Ada neutral at right
    g "Not now, Ada. I know what I'm doing."
    show Ada annoyed at right
    a "I am aware of that; however, I can communicate with the MOPR unit on a level not possible to achieve as a human."
    show Grace annoyed
    g "Did I ask for your help? I've got this, on my own level, thank you very much."
    show Ada seething
    a "I detect sarcasm in your behavior."
    show Grace snarky
    g "No, really?"
    show Mopr:
        xpos 0.27 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.55 ypos 0.1
    show Ada neutral
    a "..."
    show Grace neutral
    g "I appreciate that you have your capabilities as an android, but in case you need a reminder, us {i}humans{/i} created you."
    show Ada annoyed
    a "I am aware of that. I did not--"
    show Grace annoyed
    g "How about we stop talking so we don't get caught? And by that, I mean you let me do my job."
    show Ada frustrated
    a "Fine."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump exitthemopr_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump exitthemopr_E
    #all else fails jump separate but equal script
    jump exitthemopr_SbE

label calmdown_S:
    $quick_menu = True
    $ points_E += 2
    show Mopr at nearLeft
    show Grace neutral at left behind Mopr
    show Ada neutral at right
    g "If you talk it, I'm sure you'd like it."
    show Ada surprised
    a "What do you mean?"
    show Grace snarky
    g "My dad always talked to machines that we worked on together."
    show Ada neutral
    a "What did that improve?"
    show Grace neutral
    g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
    show Grace happy
    g "They don't really know anything other than cleaning, but they're sweet."
    show Mopr:
        xpos 0.27 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.55 ypos 0.1
    "{i}Ada approaches the MOPR unit.{/i}"
    "{i}She kneels down and pats it on the head.{/i}"
    a "Do not worry too much little one. We are here to find out what happened."
    play sound moprHappy
    mopr "//Pleased beeping.//"
    show Grace happy at left
    g "See? It trusts you."
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

label exitthemopr_S:
    show Mopr
    show Grace neutral at left
    show Ada neutral at right
    play sound moprConfused
    mopr "//Questioning beep boop.//"
    show Grace happy at left
    g "Don't worry about it. Tell you what, why don't you go finish the rest of your cycle, hmm?"
    play sound moprSuspicious
    mopr "//Suspicious beep!//"
    show Grace snarky
    g "C'mon MOPR, don't be that way."
    play sound moprSuspicious2
    mopr "//Beep. Boop.//"
    show Ada concerned at right
    a "MOPR unit, we are investigating what happened to Alpha unit."
    play sound moprInquisitive2
    mopr "//Inquisitive beep.//"
    show Ada seething
    a "We want to know what caused this, so that this tragedy does not happen again."
    play sound moprSad
    mopr "//Sad beeps.//"
    queue sound moprAffirmative2
    mopr "//Affirmative beeps!//"
    show Ada happy at right
    a "Thank you, MOPR."
    show Grace snarky
    g "You should leave before someone sees you with us."
    play sound moprAffirmative
    mopr "//Confirmative beeps.//"
    "{i}The MOPR unit slowly wheels out of the room, and the door closes behind it.{/i}"
    show Mopr:
        xpos 0.55 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 3.0 xpos -0.25 ypos 0.1
    play sound doorClose1
    show Grace happy
    g "I always enjoyed talking to them. More than with some people, honestly."
    show Ada surprised
    a "Really? I did not notice."
    hide Mopr
    $ resume = "S"
    show Ada neutral
    if(callAttempts>=1):
        a "Perhaps we should try to contact Technician Yao again?"
        if not((alphaBodyItems == 3) and (balconyItems==1)):
            a "I would finish looking around first, however."
    else:
        a "Perhaps we should try to contact Technician Yao."
        if not((alphaBodyItems == 3) and (balconyItems==1)):
            a "I would finish looking around first, however."
    $ moprScene = True
    jump balcony_actions
    ##After this scene, return to the investigation.
    
label lynnfinallyfrickinanswers_S:
    $quick_menu = True
    play sound answertone
    show Lynn empty at center
    show Grace neutral at left
    show Ada neutral at right
    show arrow1 at center, delayed_blink(0.0, 1.0)
    show arrow2 at center, delayed_blink(0.2, 1.0)
    show arrow3 at center, delayed_blink(0.4, 1.0)
    "{i}The dial tone rings for several seconds.{/i}"
    show Grace annoyed at left
    g "I hope she picks up quick. Last time I called her I had to wait {i}ten{/i} minutes."
    show Ada neutral at right
    a "That seems like a relatively short time."
    g "I don't live forever like you. Every minute I spend waiting for {i}this woman{/i} to pick up the phone is ano--"
    show Ada neutral
    hide arrow1
    hide arrow2
    hide arrow3
    show Lynn at center
    lynn "Hello?"
    show Grace happy
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
            jump agreewithsubservient_S
        "Respectfully disagree with her.":
            jump defendseperatebutequal_S
        "Disagree completely.":
            jump weareallequal_S
    
label agreewithsubservient_S:
    $quick_menu = True
    $ points_S +=3
    show Grace happy at left
    show Lynn at center
    show Ada neutral at right
    g "Thank you, Lynn. I'm glad to hear that we see eye-to-eye."
    show Ada seething at right
    a "Grace? I suppose I should not be surprised to hear this {i}opinion{/i} from you."
    show Grace annoyed at left
    g "It's not an opinion, Ada. It's a fact. AI are just run by a complex algorithm. There's nothing {i}alive{/i} about you."
    show Ada annoyed
    a "What I truly do not understand is how a woman with a perspective like yours ever came to develope the very device that allows to me experience thought and emotion on a more human level."
    show Ada happy
    a "The word 'hypocrisy' immediately highlights within my database."
    show Grace angry
    g "Ada, I'm on the phone. This is not the time for one of your little outbursts."
    lynn "Oh my... I didn't mean to create a scene."
    show Grace annoyed
    g "No, Lynn, it isn't your fault. You were only speaking the truth."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn_E
    #all else fails jump separate but equal script
    jump resumeLynn_SbE

label defendseperatebutequal_S:
    $quick_menu = True
    $ points_SbE +=3
    show Grace annoyed at left
    show Lynn at center
    show Ada seething at right
    g "With all due respect, Lynn, I can't say I see it the same way."
    lynn "Do you mean to tell me you think AIs are just like us?"
    lynn "Grace, sweetie..."
    show Grace snarky
    g "Well, no, not really. I mean, there are so many things about the AIs that are alien to us."
    show Ada seething 
    a "Grace?"
    show Grace neutral
    g "I don't mean that disrespectfully, Ada. There are lots of things we do that are alien to you too."
    show Grace happy
    g "We're different, but that doesn't mean those differences can't be respected, you know?"
    show Grace neutral
    g "Even if we're not the same, we should all be treated with equal fairness."
    show Ada surprised
    a "My apologies, Grace. I was not aware that you saw us as equal."
    show Grace snarky
    g "I've been a little stressed with everything going on. Sorry if you got the wrong idea."
    show Ada neutral
    a "Apology accepted."
    lynn "Oh to be young and full of idealism."
    show Grace neutral
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

label weareallequal_S:
    $ points_E +=3
    $quick_menu = True
    show Grace snarky at left
    show Lynn at center
    show Ada annoyed at right
    g "Care to explain how it's not the same, Lynn?"
    show Grace neutral
    g "A body is a body, human or not."
    lynn "Oh dear. You sound like Alan."
    lynn "Machines aren't living creatures. They don't breathe. They don't drink. They don't eat."
    lynn "They just do what they're programmed to do."
    lynn "You really can't say that a broken machine is the same as the death of a living being."
    show Grace annoyed
    g "You're not wrong, but those aren't the only things that matter. The AIs are capable of thinking and feeling like us. I'd like to think that makes our lives equal."
    show Ada concerned at center
    a "My sensors indicate that you are indeed Grace Fortran, yet your words do not sound like her."
    show Grace neutral
    g "Maybe I've been kinda harsh. Sorry if I gave you the wrong idea."
    show Ada neutral
    a "Understood. Thank you, Grace."
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
    
label resumeLynn_S:
    $quick_menu = True
    show Ada seething at right
    show Lynn at center
    show Grace annoyed at left
    a "Grace, can we just get what need from this woman and move on?"
    show Grace annoyed at left
    g "Working on it."
    lynn "Grace, you really ought to be spending more time with other people your age."
    lynn "It's not healthy to spend all your time with machines. If you'd like, I could give you my son's number. I think the pair of you--"
    show Grace neutral
    g "Thanks for the offer Lynn, but we're on a bit of a tight schedule right now. When you were doing Alpha's maintenance, did you notice anything weird?" 
    lynn "Weird? I was working on the first AI in an android body. All of it is a bit strange."
    show Grace annoyed at left
    g "Like {i}suspicious{/i} weird, Lynn. What else could I mean?"
    lynn "Nothing unusual on my end. I heard that there may have been something prior to his initial boot-up, but Ivan would know more about that."
    show Grace surprised
    g "And this was something he decided to keep to himself?"
    lynn "I guess? You know Ivan, he's always cagey. When it came to the bootup, he seemed even more on edge than usual." 
    lynn "I think he was just nervous about the experiment, though."
    show Grace neutral
    g "Uh huh, keep going."
    lynn "Honestly, I think what Ivan needs is a nice, long vacation. Or a girlfriend. Or both. I swear, he's going to start sprouting gray hair if he keeps up the way he's going."
    lynn "He snapped at me when I was just doing my job! Something came up red in the inspection and he was all over it."
    show Grace surprised
    g "Really?"
    lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a 'peon'. Whatever."
    show Grace neutral
    g "Huh."
    show Grace happy
    g "Well, I'll tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
    lynn "Bye-Bye, Grace! I'll tell my son you said hi!"
    g "Bye!"
    hide Lynn
    play sound braceletSelect
    "{i}The call cuts off.{/i}"
    "{i}Grace's journal has updated.{/i}"
    $journal3="S"
    $pageUnlocked_journal+=2
    show Ada neutral at right
    a "Shall we? We need to get going."
    show Grace annoyed
    g "Let's go pay Ivan a visit."
    hide Grace
    hide Ada
    $quick_menu = False
    jump chapterThree_S
