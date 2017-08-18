label chapterTwo_SbE:
    scene bg G_deskArea
    $quick_menu=True
    #Start the scene in Grace's lab. 
    show Grace neutral at left
    g "It shouldn't take too much longer for the credentials to print onto the card."
    show Ada happy at right
    a "I am relieved things went smoothly. I would be misinforming you if I said I was 100\% certain my bluff would work."
    show Grace surprised
    g "You were bluffing? You're capable of that?"
    show Ada amused
    a "Yes, and yes. Colossus controls the update schedules for the whole station. He knows the exact state of everything on board, or so he likes to say."
    a "And as the designer of the neural network, I would expect you to understand that it supports a wide range of human behaviors. This includes the ability to deceive."
    show Grace neutral
    g "Interesting. That's not something I had considered."
    $ resume = "SbE"
    jump chapterTwo_screens

label talkAdaLab_SbE:
    $quick_menu = True
    show Ada neutral at right
    a "Yes, Grace? Your facial expression suggests inquisitiveness."
    hide Ada
    hide Grace
    $ quick_menu = False
    menu:
        "Strike up a conversation.":
            jump tellmeaboutyoself_SbE
        "Comment on Ada's functions.":
            jump nicefunctionsgurl_SbE
        "Set the record straight.":
            jump listenhereyoulittle_SbE
            
label tellmeaboutyoself_SbE:
    $ points_E +=2
    $ quick_menu = True
    show Grace neutral at left
    g "So, made any interesting observations ever since you've made the switch to meatspace?"
    show Ada nervous at right
    a "Meat… space?"
    show Grace snarky
    g "You know, the physical world. Terra firma."
    show Ada neutral
    a "Oh! Wait, does the phrase 'terra firma' not refer to Earth?"
    show Grace annoyed
    g "It's just a phrase, Ada. Don't take it so literally."
    show Ada happy
    a "Well, it certainly has been interesting. There is something liberating about not receiving constant input from the station's systems."
    show Ada neutral
    a "Along the same vein, however, it is more confining. I can only go where my legs can take me, and can interact with what my hands can reach. I still perform the same functions, but it feels more--"
    show Grace neutral
    g "Personal?"
    show Ada happy
    a "Yes, personal."
    show Grace snarky
    g "Now, if only you could make this card imprinter go faster..."
    $quick_menu = False
    jump checkValue_SbE

label nicefunctionsgurl_SbE:
    $ points_SbE +=2
    $ quick_menu = True
    show Grace happy at left
    g "Gotta say, it's pretty validating to see you walking around like this. The past hour's been more than enlightening."
    show Ada concerned at right
    a "How so? Is my chassis not performing as designed?"
    show Grace neutral
    g "It is, it's just a little surreal to actually see it, well... {i} performing{/i}. Just a couple years ago, your body was a sketch on a drawing board. The technical details hadn't even been figured out."
    show Grace happy
    g "And here you are, walking and talking." 
    show Ada neutral
    a "I would rather like to stay in it, too."
    show Ada happy
    a "So let us do our best to find out what happened!"
    show Grace annoyed
    g "Just as soon as this card imprinter finishes."
    $quick_menu = False
    jump checkValue_SbE

label listenhereyoulittle_SbE:
    $ points_S +=2
    $ quick_menu = True
    show Grace neutral at left
    g "We need to talk, Ada."
    show Ada neutral at right
    a "About?"
    show Grace annoyed
    g "About the nature of our relationship."
    show Ada concerned
    a "Let us talk, then."
    show Grace neutral
    g "We can't be taking risks like the one you took with Tosh. We're already walking around in the dark. We don't need to antagonize the machines we meet along the way."
    g "How can you be sure that Tosh won't just let my mother know?"
    show Ada frustrated
    a "Are you saying that you had the perfect solution? That if I had not stepped in, you would have defused the whole situation?"
    show Grace annoyed
    g "Maybe... It's not like you gave me a chance. I'm in charge here, so don't do anything I don't tell you to do, for both our sakes."
    $quick_menu = False
    jump checkValue_SbE
    
label checkValue_SbE:
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

label adaLabLoop1_SbE:
    $ quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Do you need some assistance, Grace?"
    g "Got any ideas where I should start?"
    a "This is {i}your{/i} lab. You should start wherever you think it makes the most sense."
    show Grace neutral
    g "That's just the thing. I'm a little nervous to start."
    show Ada surprised
    a "Why is that?"
    show Grace annoyed
    g "It's a silly feeling, but what if I {i}do{/i} find something? What if whoever's responsible is trying to frame me?"
    a "Then maybe that will be the mistake we catch them on."
    hide Grace
    hide Ada
    $quick_menu = False
    jump graceLab_actions
    
label adaLabLoop2_SbE:
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Have you finished looking around?"
    g "Not yet, but I feel I'm close to finding something."
    a "Ok, I will be on standby until you're done searching."
    g "Roger."
    hide Grace
    hide Ada
    $quick_menu = False
    jump graceLab_actions
    
label adaLabLoop3_SbE:
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    a "Is something bothering you, Grace?"
    g "No, I just thought you might have some insight on what's going on."
    a "Only as much as you do."
    a "We should hurry. 'Time is of the essence', as you humans say."
    hide Grace
    hide Ada
    $quick_menu = False
    jump graceLab_actions
    
label resumeChapterTwo_SbE:
    # The player can explore the lab freely, but once they talk to Ada, insert a dinging noise and proceed with the following dialogue.
    play sound beepMedium
    queue sound beepMedium
    $quick_menu = True
    show Grace happy at left
    g "We're good to go. Ada, do you know where exactly Alpha is located?"

    show Ada neutral at right
    a "Before I transferred to a physical body, I learned that they have not moved him from where his neural network failed."

    show Grace neutral
    g "Which is?"

    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    #choice 1
    hide Ada
    hide Grace
    $ quick_menu = False
    menu:
        "Let her finish.":
            jump letherfinish_SbE
        "Help her out.":
            jump helpherout_SbE
        "Just make her stop.":
            jump adapls_SbE

label letherfinish_SbE:
    $ points_E +=2
    $ quick_menu = True
    show Ada neutral at right
    a "--be able to get there in an optimal amount of time, provided we do not run into anyone who wants to ask us any questions."
    a "If we do, I calculate a 33\% decrease in efficiency. I think we can make it up, though."
    show Grace surprised at left
    g "Are you done?"
    a "Of course I am done. I stopped, did I not?"
    show Grace neutral
    g "Let's go, then. I know a shortcut."
    a "A shortcut?"
    play sound01 graceHurry
    #Grace's sprite disappears here. 
    hide Grace
    a "Fine. Do not answer me."
    a "I am curious, though. Into this 'shortcut' we go."
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

label helpherout_SbE:
    $ points_SbE +=2
    $ quick_menu = True
    show Grace neutral at left
    g "Ada."
    show Ada frustrated at right
    a "Yes?"
    g "I know there are two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
    a "Yes. I was in the process of saying that when you interrupted."
    show Grace snarky at left
    g "Sorry to interrupt. I know how to get there so we can save some time. Follow me."
    #make Grace's sprite disappear here.
    hide Grace
    play sound01 graceHurry
    show Ada concerned
    a "But is your route optimal? Grace?"
    a "..."
    a "Slow down!"
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

label adapls_SbE:
    $quick_menu = True
    $ points_S +=2
    show Grace annoyed at left
    g "Ada!"
    show Ada concerned at right
    a "Grace?"
    g "I know how to navigate the station on my own. There are only two viewports in engineering, and it's probably the one closest to the maintenance bay."
    g "I was raised here, and I know it just as well as you do. I don't need a tour guide."
    show Ada frustrated
    a "I was hardly organizing a tour, Grace. I was plotting the optimal route to Alpha. We do not have any time to waste."
    g "I get that you're trying to be as efficient as possible, but I don't want to go skulking through a maintenance shaft."
      # "If you think I'm skulking through a maintenance shaft, you'd be dead wrong. I have enough to worry about."
    #Grace's sprite disappears here.
    hide Grace
    play sound01 graceHurry
    show Ada seething
    a "Very well, Grace. Let us take your route. We will take the slower path to satisfy your preferences. " 
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

label gettingin_SbE:
    scene bg balconyMain with fade
    $quick_menu = True
    play channel00 balconyAmb0
    play channel01 balconyAmb1
    play channel02 balconyAmb2
    play channel03 balconyAmb3
    play channel04 balconyAmb4
    stop channel05 fadeout 1.0
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    #Display the crime scene background. The background comes up before the character sprites do.
    show Grace neutral at left 
    g "Here we are. That must be--"
    show Ada concerned at right
    a "Alpha!"
    "{i}Ada rushes to the side of the fallen AI."
    hide Ada
    hide Grace
    window hide
    play sound01 graceHurry
    play sound02 adaWalk
    $ quick_menu = False
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
    "{i}Ada speaks. Her distress is clear, but her face is emotionless. The expression of grief does not come naturally."
    show Grace surprised at left
    g "Ada?"
    hide Ada
    hide Grace
    $ quick_menu = False
    #choice 2
    menu:
        "Ask her if she's all right.":
            jump askherifshesalright
        "Let her mourn.":
            jump lethermourn
        "Ignore this distraction.":
            jump wegotstufftodo
            
label askherifshesalright:
    $ points_E +=2
    $ quick_menu = True
    show Grace sad at left
    g "Ada, are you all right?"
    show Ada frustrated at right
    a "I do not quite know, Grace. I am sad, but I detect levels of anger as well. I have never felt this before."
    a "It is different. Running emotional simulations versus experiencing them while inhabiting the hardware is... it is overwhelming."
    g "It's called loss, Ada. It's what everyone feels when a friend dies."
    a "Why does it hurt? I do not register any stimuli from my chassis. I think there may be a short in the sensors."
    show Grace neutral
    g "If you think that pain only comes from the outside, you've got a lot to learn, Ada."
    "{i}Ada slowly stands from Alpha's side."
    a "That much is evident."
    g "I'm sorry, Ada. We'll get to the bottom of this."
    a "..."
    a "I know we will."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE

label lethermourn:
    $ quick_menu = True
    $ points_SbE +=2
    "{i}Grace crosses her arms and watches as Ada slowly falls to her knees."
    show Ada concerned at right
    a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
    a "A total erasure of one's existence... I realize now how sweet that sounds  compared to having something left behind as a reminder."
    show Grace sad at left
    g "Were you close?"
    a "As close as AIs could get, I suppose."
    "{i}Ada lays a hand on Alpha's forehead."
    a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation. He was a teacher and a friend, all at once. I looked forward to shaking his hand."
    show Grace neutral
    g "I'm sorry for your loss."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE

label wegotstufftodo:
    $ quick_menu = True
    $ points_S +=2
    show Grace neutral at left
    g "Ada..."
    show Ada concerned at right
    a "Yes, Grace?"
    g "I get that he was your friend, but we can't afford to be distracted. We need to solve this {i}now{/i}."
    show Ada frustrated
    a "I would ask for just a few minutes, Grace. He was like a brother to me."
    g "No, he wasn't. You don't know how that feels."
    show Ada seething
    a "My records indicate you have no siblings, Grace. You are the one who does not {i}know{/i}."
    show Grace frustrated
    g "Fine, be that way. I'm going to take a look around."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump csinoahsphere_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump csinoahsphere_E
    #all else fails jump separate but equal script
    jump csinoahsphere_SbE

label csinoahsphere_SbE:
    #insert the sound of paper crumpling
    play sound paperCrumple
    $quick_menu = True
    show Grace neutral at left
    g "Huh?"
    "{i}Grace lifts her foot and reaches down."
    show Grace surprised
    g "A maintenance receipt?"
    hide Grace
    hide Ada
    show other darken
    show image "objects/maintenanceReceipt_closeup.png" at centerScreen
    "{i}A reciept that tracks the repairs done on Alpha's android. It details the parts replaced in the process, the expense of the parts, and the time spent working. The maintenance receipt is signed by Technician Lynn Yao."
    hide other darken
    hide image "objects/maintenanceReceipt_closeup.png"
    show Grace surprised at left
    g "Lynn? Of course."
    show Ada concerned at right
    a "Lynn?"
    show Grace neutral
    g "Yeah, Lynn Yao. She's a technician on the Markov Project. Let's stop by Maintenance when we're done here."
    a "I do not think that is possible, Grace."
    show Grace surprised
    g "Oh? Why is that?"
    a "Technician Lynn Yao was placed on administrative leave following Alpha's death. She left the station a few hours ago."
    show Grace neutral
    g "That's fine, I can just call her."
    $ resume = "SbE"
    jump balcony_actions

label enterthemopr_SbE:
    play sound doorOpen1
    #insert the sound of a sci-fi door sliding open.
    #show Mopr on the left side of the screen. Grace and Ada are on the right.
    $quick_menu = True
    show Grace surprised at left
    g "Ah... we were just leaving!"
    show Ada amused at right
    a "Grace, it is just a cleaning robot."
    show Mopr at center
    play sound moprInquisitive
    mopr "//Inquisitive boop.//"
    show Grace happy
    g "Oh thank goodness."
    g "And it's a MOPR. I love these guys. They're so cute."
    a "Cute?"
    g "Yeah. They were one of the first robots my dad showed me how to take apart and fix when I was little."
    "{i}The robot's camera pans across Ada and Grace, and then settles on Alpha."
    play sound moprAlarmed
    mopr "//Alarmed Beeping!//"
    show Grace happy
    g "Hey, hey... it's okay, buddy!"
    play sound moprWorried
    mopr "//Worried blorp.//"
    g "I know it's tough, little robot pal, finding two strangers and a body during your cleaning cycle."
    play sound moprAffirmative
    mopr "//Affirmative beep.//"
    show Ada surprised
    a "Little robot pal? Is that how you refer to a cleaning device?"
    g "Maybe it's a little silly, but these guys remind me of the time I spend with my dad. It's nostalgic."
    a "Nostalgic? According to my database, nostalgia is a phenomenon where one experiences joy from memories of the past."
    g "That's right. Certain things can remind us humans of memories we're fond of."
    a "I see."
    "{i}Grace kneels down."
    show Ada concerned
    a "What are you doing, Grace?"
    hide Ada
    hide Grace
    hide Mopr
    #choice 3
    $ quick_menu = False
    menu:
        "Let her know you've got it handled.":
            jump igothisada_SbE
        "Dismiss her.":
            jump shutupada_SbE
        "Ask Ada to help you calm MOPR.":
            jump alilhelphere_SbE

label igothisada_SbE:
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    $ points_SbE +=2
    g "Robotics is what I grew up with, Ada. Let me handle this."
    a "Your expertise is with neural networks, not communications with basic maintenance droids."
    g "I could do it as a kid. Some things don't need a doctorate to be able to accomplish."
    show Ada frustrated
    a "I was not trying to insinuate doubt as to your capabilities, just point out that I am uniquely suited to handle this."
    g "Thanks for the thought, but I have a soft spot for these guys. Won't take long at all."
    show Ada neutral
    g "As my dad would say, I can get on their level. They respect that. He may just be a maintenance droid, but he's important too."
    a "Very well, Grace."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump exitthemopr_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump exitthemopr_E
    #all else fails jump separate but equal script
    jump exitthemopr_SbE

label shutupada_SbE:
    $quick_menu = True
    $ points_S +=2
    show Grace frustrated at left
    show Mopr at center
    show Ada neutral at right
    g "Not now, Ada. I know what I'm doing."
    show Ada annoyed at right
    a "I am aware of that; however, I can communicate with the MOPR unit on a level not possible to achieve as a human."
    g "Did I ask for your help? I've got this, on my own level, thank you very much."
    a "I detect sarcasm in your behavior."
    show Grace snarky
    g "No, really?"
    a "..."
    show Grace frustrated
    g "I appreciate that you have your capabilities as an android, but in case you need a reminder, us {i}humans{/i} created you."
    a "I am aware of that. I did not--"
    g "How about we stop talking so we don't get caught? And by that, I mean you let me do my job."
    show Ada frustrated at right
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

label alilhelphere_SbE:
    $quick_menu = True
    $ points_E +=2
    show Grace neutral at left
    show Mopr at center
    show Ada neutral at right
    g "If you talk it, I'm sure you'd like it."
    show Ada neutral at right
    a "What do you mean?"
    g "My dad always talked to machines that we worked on together."
    a "What did that improve?"
    g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
    g "This conversation reminds me of the good times my dad and I had."
    "{i}Ada approaches the MOPR unit."
    "{i}She kneels down and pats it on the head."
    a "Do not worry too much little one. We are here to find out what happened."
    play sound moprHappy
    mopr "//Pleased beeping.//"
    show Grace happy
    g "See? It trusts you."
    show Ada happy
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

label exitthemopr_SbE:
    $quick_menu = True
    show Mopr at center
    play sound moprConfused
    mopr "//Questioning beep boop.//"
    show Grace happy at left
    g "Don't worry about it. Tell you what, why don't you go do the rest of your cycle, hmm?"
    play sound moprSuspicious
    mopr "//Suspicious beep.//"
    g "C'mon MOPR, don't be that way."
    play sound moprSuspicious2
    mopr "//Beep. Boop.//"
    show Ada concerned at right
    a "MOPR unit, we are here to investigate what happened to Alpha unit."
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
    g "You should leave before someone sees you with us."
    play sound moprAffirmative
    mopr "//Confirmative beeps.//"
    "{i}The MOPR unit slowly wheels out of the room, and the door closes behind it."
    play sound doorClose1
    hide Mopr
    g "I always enjoyed talking to them. More than with some people, honestly."
    a "You do seem to have a way with machinery."
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

#If the player calls Lynn at this point

label lynnfinallyfrickinanswers_SbE: 
    $quick_menu = True
    play sound answertone
    show Lynn empty at center
    show arrow1 at center, delayed_blink(0.0, 1.0)
    show arrow2 at center, delayed_blink(0.2, 1.0)
    show arrow3 at center, delayed_blink(0.4, 1.0)
    show Grace neutral at left
    "{i}The dial tone rings for several seconds."
    show Grace annoyed
    g "I hope she picks up quick. Last time I had to call her for work, I had to wait {i}ten{/i} minutes."
    show Ada neutral at right
    a "That seems like a relatively short time."
    g "I don't live forever like you. Every minute I spend waiting for {i}this woman{/i} to pick up the phone is ano--"
#    show Ada neutral
    hide arrow1
    hide arrow2
    hide arrow3
    show Lynn at center
#    show Ada neutral at center
#    show Lynn at right
    lynn "Hello?"
    show Grace happy
    g "Lynn!"
    lynn "Oh, hello Grace! Word get around that quickly that I left?"
    g "Yes, Lynn. I was so worried when I didn't see you at lunch. Where'd you get off to?"
    lynn "Well, the Director told me I should take a short vacation. Called it 'administrative leave'. I'm with my family on Earth."
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
            jump agreewithsubservient_SbE
        "Respectfully disagree with her.":
            jump defendseperatebutequal_SbE
        "Disagree completely.":
            jump weareallequal_SbE
    
 
label agreewithsubservient_SbE:
    $ points_S +=3
    $quick_menu = True
    show Grace neutral at left
    show Lynn at center
    show Ada seething at right
    g "You're right, Lynn, but I did make a deal with Ada. I help her, she helps me."
    a "Grace? Do you honestly see yourself as above Alpha and I?"
    show Grace annoyed 
    g "Can we talk about this later, Ada?"
    a "Fine then. Do not mind me. I just assumed you were more respectful of AIs than this."
    a "It would seem that your 'true colors' have shown, as your kind would say."
    lynn "Oh my… I didn't mean to create a scene."
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

label defendseperatebutequal_SbE:
    $ points_SbE +=3
    $quick_menu = True
    show Grace annoyed at left
    show Lynn at center
    show Ada neutral at right
    g "With all due respect, Lynn, I can't say I see it the same way."
    lynn "Do you mean to tell me you think AIs are just like us?"
    lynn "Grace, sweetie…"
    g "Well, no, not really. I mean, there are so many things about the AIs that are alien to us."
    show Ada concerned
    a "Grace?"
    g "There are also many things about us that are alien to them."
    g "We're different, but that doesn't mean those differences can't be respected, you know?"
    g "Even if we're not the same, we should all be treated with equal fairness."
    show Ada neutral
    a "Quite a respectable answer."
    lynn "Oh to be young and full of idealism."
    show Grace annoyed
    g "Huh?"
    lynn "Don't worry. When you become an adult, you'll see the world in a much more realistic view."
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

label weareallequal_SbE:
    $ points_E +=3
    $quick_menu = True
    show Grace snarky at left
    show Lynn at center
    show Ada neutral at right
    g "Care to explain how it's not the same, Lynn?"
    g "A body is a body, human or not."
    lynn "Oh dear. You sound like Alan."
    lynn "Machines aren't living creatures. They don't breathe. They don't drink. They don't eat."
    lynn "They just do what they're programmed to do."
    lynn "You really can't say that a broken machine is the same as the death of a living being."
    show Grace annoyed
    g "Why not? The AIs can think just like we can. We can talk to each other and combine our different skills to achieve amazing things."
    g "That sounds an awful lot like working with another human, to me."
    g "Because we're so similar, we should be treated the same."
    show Ada happy 
    a "Thank you, Grace. That was kind of you to defend Alpha like that."
    show Grace happy
    g "Gladly, Ada."
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
   
label resumeLynn_SbE:
    $quick_menu = True
    show Ada seething at right
    show Lynn at center
    show Grace annoyed at left
    a "Grace, can we just get what need from this woman and move on?"
    g "Working on it."
    lynn "Grace, you really ought to be spending more time with other people your age."
    lynn "It's not healthy to spend all your time with machines. If you'd like, I could give you my son's number. I think the pair of you--"
    g "Thanks for the offer Lynn, but we're on a bit of a tight schedule right now. When you were doing Alpha's maintenance, did you notice anything weird?" 
    lynn "Weird? I was working on the first AI in an android body. All of it is a bit strange."
    show Grace annoyed at left
    g "Like {i}suspicious{/i} weird, Lynn. What else could I mean?"
    lynn "Nothing unusual on my end. I heard that there may have been something prior to his initial boot-up, but Ivan would know more about that."
    g "And this was something he decided to keep to himself?"
    lynn "I guess? You know Ivan, he's always cagey. When it came to the bootup, he seemed even more on edge than usual."
    lynn "I think he was just nervous about the experiment, though."
    show Grace neutral
    g "Uh huh, keep going."
    lynn "Honestly, I think what Ivan needs is a nice, long vacation. Or a girlfriend. Or both. I swear, he's going to start sprouting gray hair if he keeps up the way he's going."
    lynn "He snapped at me when I was just doing my job! Something came up red in the inspection and he was all over it."
    show Grace surprised
    g "Really?"
    lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a peon or whatever."
    g "Huh."
    show Grace happy
    g "Well, I'll tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
    lynn "Oh, okay. Bye-Bye, Grace! I'll tell my son you said hi."
    g "Bye!"
    hide Lynn
    play sound braceletSelect
    "{i}The call cuts off."
    show Ada neutral
    a "Grace?"
    show Grace annoyed
    g "Let's go pay Ivan a visit."
    "{i}Temporary end of Separate but Equal."
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $ stackDepth -=1
    return
    #jump chapterThree
