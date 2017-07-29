label chapterTwo_SbE:

    #Start the scene in Grace's lab. 
    show Grace neutral at left
    g "It shouldn't take too much longer for the credentials to print onto the card."
    #show Ada happy
    a "I am relieved things went smoothly. I would be misinforming you if I said I was 100\% certain my bluff would work."
    #show Grace surprised
    g "You were bluffing? You're capable of that?"
    #show Ada amused
    a "Yes, and yes. Colossus controls the update schedules for the whole station. He knows the exact state of everything on board, or so he likes to say."
    a "And as the designer of the neural network, I would expect you to understand that it supports a wide range of human behaviors. This includes the ability to deceive."
    #show Grace neutral
    g "Interesting. That's not something I had considered."
    $ resume = "SbE"
    jump chapterTwo_screens
    
label resumeChapterTwo_SbE:
    # The player can explore the lab freely, but once they talk to Ada, insert a dinging noise and proceed with the following dialogue.
    #show Grace happy
    g "We're good to go. Ada, do you know where exactly Alpha is located?"

    #show Ada neutral
    a "Before I transferred to a physical body, I learned that they have not moved him from where his neural network failed."

    #show Grace neutral
    g "Which is?"

    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    #choice 1
    menu:
        "Let her finish.":
            jump letherfinish_SbE
        "Help her out.":
            jump helpherout_SbE
        "Just make her stop.":
            jump adapls_SbE

label letherfinish_SbE:
    $ points_E +=2
    #show Ada neutral
    a "--be able to get there in an optimal amount of time, provided we do not run into anyone who wants to ask us any questions."
    a "If we do, I calculate a 33\% decrease in efficiency. I think we can make it up, though."
    #show Grace surprised
    g "Are you done?"
    a "Of course I am done. I stopped, did I not?"
    #show Grace neutral
    g "Let’s go, then. I know a shortcut."
    a "A shortcut?"
    #Grace’s sprite disappears here. 
    a "Fine. Do not answer me."
    a "I am curious, though. Into this 'shortcut' we go."
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
    g "Ada."
    #show Ada frustrated
    a "Yes?"
    g "I know there are two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
    a "Yes. I was in the process of saying that when you interrupted."
    #show Grace snarky
    g "Sorry to interrupt. I know how to get there so we can save some time. Follow me."
    #make Grace's sprite disappear here.
    #show Ada concerned
    a "But is your route optimal? Grace?"
    a "..."
    a "Slow down!"
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
    $ points_S +=2
    #show Grace annoyed
    g "Ada!"
    #show Ada concerned
    a "Grace?"
    g "I know how to navigate the station on my own. There are only two viewports in engineering, and it's probably the one closest to the maintenance bay."
    g "I was raised here, and I know it just as well as you do. I don't need a tour guide."
    #show Ada frustrated
    a "I was hardly organizing a tour, Grace. I was plotting the optimal route to Alpha. We do not have any time to waste."
    g "I get that you're trying to be as efficient as possible, but I don't want to go skulking through a maintenance shaft."
      # "If you think I'm skulking through a maintenance shaft, you'd be dead wrong. I have enough to worry about."
    #Grace's sprite disappears here.
    #show Ada seething
    a "Very well, Grace. Let us take your route. We will take the slower path to satisfy your preferences. " #It is not like I can process several thousand times faster and more accurately than you."
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
    show bg balconyMain with fade
    #Display the crime scene background. The background comes up before the character sprites do.
    #show Grace neutral 
    g "Here we are. That must be--"
    #show Ada concerned
    a "Alpha!"
    "{i}Ada rushes to the side of the fallen AI."
    window hide
    scene bg balconyRamp with fade 
    $ renpy.pause(0.5)
    scene bg balconyCorner with fade
    $ renpy.pause(0.5)
    scene bg balconyLong with fade
    $ renpy.pause(0.5)
    scene bg balconyClose with fade
    "{i}Ada speaks. Her distress is clear, but her face is emotionless. The expression of grief does not come naturally."
    #show Grace surprised
    g "Ada?"
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
    #show Grace sad
    g "Ada, are you all right?"
    #show Ada frustrated
    a "I do not quite know, Grace. I am sad, but I detect levels of anger as well. I have never felt this before."
    a "It is different. Running emotional simulations versus experiencing them while inhabiting the hardware is... it is overwhelming."
    g "It's called loss, Ada. It's what everyone feels when a friend dies."
    a "Why does it hurt? I do not register any stimuli from my chassis. I think there may be a short in the sensors."
    #show Grace neutral
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
    $ points_SbE +=2
    "{i}Grace crosses her arms and watches as Ada slowly falls to her knees."
    #show Ada concerned
    a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
    a "A total erasure of one's existence... I realize now how sweet that sounds  compared to having something left behind as a reminder."
    #show Grace sad
    g "Were you close?"
    a "As close as AIs could get, I suppose."
    "{i}Ada lays a hand on Alpha's forehead."
    a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation. He was a teacher and a friend, all at once. I looked forward to shaking his hand."
    #show Grace neutral
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
    $ points_S +=2
    #show Grace neutral
    g "Ada..."
    #show Ada concerned
    a "Yes, Grace?"
    g "I get that he was your friend, but we can't afford to be distracted. We need to solve this {i}now{/i}."
    #show Ada frustrated
    a "I would ask for just a few minutes, Grace. He was like a brother to me."
    g "No, he wasn't. You don't know how that feels."
    #show Ada seething
    a "My records indicate you have no siblings, Grace. You are the one who does not {i}know{/i}."
    #show Grace frustrated
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
    #show Grace neutral
    g "Huh?"
    "{i}Grace lifts her foot and reaches down."
    #show Grace surprised
    g "A maintenance receipt?"
    #show IMAGE of the MAINTENANCE RECEIPT HERE. NEED TO ADD THAT OBJECT
    "{i}The maintenance receipt is signed by Technician Lynn Yao"
    g "Lynn? Of course."
    #show Ada concerned
    a "Lynn?"
    g "Yeah, Lynn Yao. She's a technician on the Markov project. Let's stop by Maintenance when we're done here."
    a "I do not think that is possible, Grace."
    #show Grace surprised
    g "Oh? Why is that?"
    a "Technician Lynn Yao was placed on administrative leave following Alpha's death. She left the station a few hours ago."
    g "That's fine, I can just call her."
    $ resume = "SbE"
    jump balcony_actions



##if Alpha has been fully explored: jump lynnfinallyfrickinanswers
##After the players exhaust all of the Alpha interactions; jump letthepuzzlesbegin
#label letthepuzzlesbegin:
#    #show Grace neutral
#    g "I think we've got everything we can get from the outside. Let's get a closer look."
#    "Grace leans over Alpha, and finds the access panel for his head."
#    g "Do you want to look away, Ada?"
#    #show Ada concerned
#    a "Why would I?"
#    #show Grace snarky
#    g "I don't know. Figured you might be squeamish or something."
#    "Grace removes the panel off, revealing Alpha's manual access ports."
#    #show Grace neutral
#    g "All right Alpha, let's see what you've got for us."

#    #GRACE'S PUZZLE
#    #sydmakecomscireference
#    if (attempts==1):
##show Grace happy
#g "Just as I remembered it." 
#if (attempts>1 and attempts<4):
##show Grace neutral
#g "Code was a bit weird in places, but I've got access." 
#if (attempts>3):
#	#show Grace annoyed
#	g "I'm surprised I managed to pull something out of this."

#	g "I can't get a lot. It's like his whole system got cooked and wiped at the same time. There's corrupted data all over the place."
#	#show Grace neutral
#	g "However, there's a basic readout that survived. Functions look normal, but the neural network was using almost double the necessary power."
#g "No wonder it burned out."
##show Ada neutral
#	a "Is that all?"
#g "Looks like it. I was really hoping to get more."

##show Ada neutral
#	a "Let me take a look. I know Alpha's code intimately."

##sydmakecomscireference
#if (attempts==1):
##show Ada neutral
#a "There we are-- oh."
#if (attempts>1 and attempts<4):
##show Ada neutral
#a "The way this code is fragmented is troubling, but I managed to access his logs."
#   if (attempts>3):
#	#show Ada frustrated
#	a "I have never seen code this corrupted. I was barely able to access the logs."

#	#show Ada concerned
#	a "This is very troubling."
#	#show Grace surprised
#	g "What is it?"
#	a "There are several code remnants that are foreign to Alpha's data signatures. It almost takes up a majority of his memory space."
#	g "What does the code say?"
#	#show Ada frustrated
#	a "I could not tell you. There are several places where they overlap and are threaded together. I could not begin to tell you what he was processing."
#jump enterthemopr

label enterthemopr_SbE:
    #insert the sound of a sci-fi door sliding open.
    #show Mopr on the left side of the screen. Grace and Ada are on the right.
    #show Grace surprised
    g "Ah... we were just leaving!"
    #show Ada amused
    a "Grace, it is just a cleaning robot."
    #show Mopr
    mopr "[[Inquisitive boop.]"
    #show Grace happy
    g "Oh thank goodness."
    g "And it's a MOPR. I love these guys. They're so cute."
    a "Cute?"
    g "Yeah. They were one of the first robots my dad showed me how to take apart and fix when I was little."
    "{i}The robot's camera pans across Ada and Grace, and then settles on Alpha."
    mopr "[[Alarmed Beeping!]"
    #show Grace happy
    g "Hey, hey... it's okay, buddy!"
    mopr "[[Worried blorp.]"
    g "I know it's tough, little robot pal, finding two strangers and a body during your cleaning cycle."
    mopr "[[Affirmative beep.]"
    #show Ada surprised
    a "Little robot pal? Is that how you refer to a cleaning device?"
    g "Maybe it's a little silly, but these guys remind me of the time I spend with my dad. It's nostalgic."
    a "Nostalgic? According to my database, nostalgia is a phenomenon where one experiences joy from memories of the past."
    g "That's right. Certain things can remind us humans of memories we're fond of."
    a "I see."
    "{i}Grace kneels down."
    #show Ada concerned
    a "What are you doing, Grace?"
    #choice 3
    menu:
        "Let her know you've got it handled.":
            jump igothisada_SbE
        "Dismiss her.":
            jump shutupada_SbE
        "Ask Ada to help you calm MOPR.":
            jump alilhelphere_SbE

label igothisada_SbE:
    #show Grace neutral
    $ points_SbE +=2
    g "Robotics is what I grew up with, Ada. Let me handle this."
    a "Your expertise is with neural networks, not communications with basic maintenance droids."
    g "I could do it as a kid. Some things don't need a doctorate to be able to accomplish."
    a "I was not trying to insinuate doubt as to your capabilities, just point out that I am uniquely suited to handle this."
    g "Thanks for the thought, but I have a soft spot for these guys. Won't take long at all."
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
    $ points_S +=2
    #show Grace frustrated
    g "Not now, Ada. I know what I'm doing."
    a "I am aware of that; however, I can communicate with the MOPR unit on a level not possible to achieve as a human."
    g "Did I ask for your help? I've got this, on my own level, thank you very much."
    a "I detect sarcasm in your behavior."
    g "No, really?"
    a "..."
    g "I appreciate that you have your capabilities as an android, but in case you need a reminder, us {i}humans{/i} created you."
    a "I am aware of that. I did not--"
    g "How about we stop talking so we don't get caught? And by that, I mean you let me do my job."
    #show Ada frustrated
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
    $ points_E +=2
    #show Grace neutral
    g "If you talk it, I'm sure you'd like it."
    a "What do you mean?"
    g "My dad always talked to machines that we worked on together."
    a "What did that improve?"
    g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
    g "This conversation reminds me of the good times my dad and I had."
    "{i}Ada approaches the MOPR unit."
    "{i}She kneels down and pats it on the head."
    a "Do not worry too much little one. We are here to find out what happened."
    mopr "[[Affirmative beeping.]"
    #show Grace happy
    g "See? It trusts you."
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
    mopr "[[Questioning beep boop?]"
    #show Grace happy
    g "Don't worry about it. Tell you what, why don't you go do the rest of your cycle, hmm?"
    mopr "[[Suspicious beep.]"
    g "C'mon MOPR, don't be that way."
    mopr "[[Beep. Boop.]"
    a "MOPR unit, we are here to investigate what happened to Alpha unit."
    g "Don't you want us to find out so we can make sure a tragedy like this doesn't happen again?"
    mopr "[[Inquisitive beep.]"
    a "Personally, I would hope nothing like this happens to me."
    mopr "[[Sad beeps.]"
    mopr "[[Affirmative beeps.]"
    a "Thank you, MOPR."
    g "You should leave before someone sees you with us."
    mopr "[[Confirmative beeps.]"
    "{i}The MOPR unit slowly wheels out of the room, and the door closes behind it."
    g "I always enjoyed talking to them. More than with some people, honestly."
    a "You do seem to have a way with machinery."
    a "Perhaps we should try to contact Technician Yao again?"
    $ moprScene = True
    jump balcony_actions

##After this scene, return to the investigation.



#If the player calls Lynn at this point

label lynnfinallyfrickinanswers_SbE: 
    "{i}The dial tone rings for several seconds."
    g "I hope she picks up quick. Last time I had to call her for work, I had to wait {i}ten{/i} minutes."
    "{i}The dial tone rings for several seconds."
    #show Ada neutral
    a "That seems like a relatively short time."
    g "I don't live forever like you. Every minute I spend waiting for {i}this woman{/i} to pick up the phone is ano--"
    lynn "Hello?"
    #show Grace happy
    g "Lynn!"
    lynn "Oh, hello Grace! Word get around that quickly that I left?"
    g "Yes, Lynn. I was so worried when I didn't see you at lunch. Where'd you get off to?"
    lynn "Well, the Director told me I should take a short vacation. Called it ‘administrative leave'. I'm with my family on Earth."
    g "That sounds nice. I've been having a crazy day up here."
    lynn "I can imagine, what with Alpha kicking the bucket. Poor thing."
    #show Ada frustrated
    a "Thing? Alpha was not just some {i}thing{/i} that happened to expire."
    lynn "Oh my. Another one? I'm sorry dear, it is sad, but at the end of the day it's not the same as a person dying."
    lynn "I'm not sure I'd say Alpha was really ever alive to begin with, even as polite as he was."
    #show Ada seething
    a "Grace, can we just get what need from this woman and move on?"
    g "Working on it."
    lynn "Grace, you really ought to be spending more time with other people your age."
    lynn "It's not healthy to spend all your time with machines. If you'd like, I could give you my son's number. I think the pair of you--"
    g "Thanks for the offer Lynn, but we\'re on a bit of a tight schedule right now. When you were doing Alpha's maintenance, did you notice anything weird?" 
    lynn "Weird? I was working on the first AI in an android body. All of it is a bit strange."
    #show Grace annoyed
    g "Like {i}suspicious{/i} weird, Lynn. What else could I mean?"
    lynn "Nothing unusual on my end. I heard that there may have been something prior to his initial boot-up, but Ivan would know more about that."
    g "And this was something he decided to keep to himself?"
    lynn "I guess? You know Ivan, he's always cagey. When it came to the bootup, he seemed even more on edge than usual."
    lynn "I think he was just nervous about the experiment, though."
    #show Grace neutral
    g "Uh huh, keep going."
    lynn "Honestly, I think what Ivan needs is a nice, long vacation. Or a girlfriend. Or both. I swear, he's going to start sprouting gray hair if he keeps up the way he's going."
    lynn "He snapped at me when I was just doing my job! Something came up red in the inspection and he was all over it."
    #show Grace surprised
    g "Really?"
    lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a peon or whatever."
    g "Huh."
    #show Grace happy
    g "Well, I'll tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
    lynn "Oh, okay. Bye-Bye, Grace! I'll tell my son you said hi."
    g "Bye!"
    "{i}The call cuts off."
    #show Ada neutral
    a "Grace?"
    #show Grace annoyed
    g "Let's go pay Ivan a visit."
    "{i}Temporary end of Separate but Equal."
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $ stackDepth -=1
    return
    #jump chapterThree
