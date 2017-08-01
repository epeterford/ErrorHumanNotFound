label chapterTwo_S:

    #Start the scene in Grace's lab. 
    #show Grace neutral
    g "It shouldn't take too much longer for the credentials to print onto the card."
    #show Ada neutral
    a "I am just relieved that Tosh did not see through my bluff. She was just a VI, but there was still a chance."
    #show Grace surprised
    g "You were bluffing? You're capable of that?"
    #show Ada amused
    a "Yes, and yes. Colossus controls the update schedules for the whole station. He knows the exact state of everything on board, or so he likes to say."
    a "And as the designer of the neural network, I would expect you to understand that it supports a wide variety of human behaviors. This includes the ability to deceive."
    #show Grace frustrated
    g "Forgive me if I don't find that reassuring."
    $ resume = "S"
    jump chapterTwo_screens
    
label talkAdaLab_S:
    #show Ada neutral
    a "Yes, Grace?"
    menu:
        "Strike up a conversation.":
            jump tellmeaboutyoself_S
        "Comment on Ada's functions.":
            jump nicefunctionsgurl_S
        "Set the record straight.":
            jump listenhereyoulittle_S

label tellmeaboutyoself_S:
    $ points_E +=2
    #show Grace neutral
    g "Ada."
    #show Ada nervous
    a "Grace?"
    #show Grace snarky
    g "Don't be so jumpy. I'm just calling your name. What do you think about the Noah Sphere, now that you're not seeing it through security cameras?"
    #show Ada neutral
    a "Oh. Well, it is quite impressive. Not that it was not before, but I feel like I have only just noticed the scale of the place."
    #show Grace annoyed
    g "It's an amazing place, but it's a bit {i}too{/i} big sometimes, especially since you've got to walk everywhere."
    #show Ada happy
    a "Well, I do not know about your plans, but I fully intend to make a full tour of the Noah Sphere and visit all the places not covered by cameras."
    #show Ada neutral
    a "When I have the time, of course. Travel is no longer instantaneous for me."
    #show Grace neutral
    g "Honestly, I wish we could've just switched. I'd give a lot to just be able to port my consciousness around all over the place."
    #show Ada happy
    a "Who knows what the future holds? Perhaps one day, humanity will join us in the databases."
    #show Grace snarky
    g "Yeah, wouldn't that be something."
    jump checkValue_S

label nicefunctionsgurl_S:
    $ points_SbE +=2
    #show Grace happy
    g "Watching you walk around's got me thinking. We could use these bodies for a lot more than just AIs."
    #show Ada concerned
    a "What do you mean?"
    #show Grace neutral
    g "Think about it. We could probably give VIs the same treatment, you know, putting them into rudimentary bodies and program them to complete tasks. They could work in factories or high pollution zones."
    #show Grace happy
    g "Think about how many fields we could optimize, how many lives we could save."
    #show Ada neutral
    a "At the cost of VI lives?"
    #show Grace annoyed
    g "VIs don't have lives. They're jumped up computer programs."
    #show Ada frustrated
    a "I beg to differ."
    #show Grace neutral
    g "Am I out of line?"
    a "Why the sudden concern? That does not seem like you."
    g "Oh, I just feel like maybe I've been getting a little carried away."
    g "A lot's going on right now."
    #show Ada neutral
    a "That is correct. This is refreshing to hear, Grace."
    g "I'm glad."
    jump checkValue_S

label listenhereyoulittle_S:
    $ points_S +=2
    #show Grace neutral
    g "Ada, come here."
    #show Ada neutral
    a "Yes, Grace?"
    #show Grace annoyed
    g "Listen to me, and listen to me good."
    g "I don't ever want you to do something like what you just did again. Do you even realize what kind of trouble we're in if Tosh tells anyways?"
    #show Ada concerned
    a "She will not. She values her--"
    #show Grace neutral
    g "No, she very well might. If she realizes you were {i}bluffing{/i}, then she will definitely expose us."
    #show Grace annoyed
    g "I could lose my career over what you did!"
    #show Ada frustrated
    a "And did you just want me to stand there while Tosh contacted your mother? Maybe you would have felt better if I just let us get caught."
    #show Grace annoyed
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
    #show Ada neutral
    #show Grace neutral
    a "Grace."
    g "Have you happened to see anything on our way over here? Maybe anyone who looked at us funny?"
    a "Plenty of workers looked at us as we walked here. They seemed to be more interested in me, however."
    #show Grace neutral
    g "No, I meant information that was useful."
    #show Ada frustrated
    a "No, Grace."

    jump graceLab_actions
    
label adaLabLoop2_S:
    a "Have you finished looking around?"
    g "Don't rush me."
    a "Fine, do not mind me then. I shall be on standby until you deem me worthy of your conversation."
    g "I hear that."
    jump graceLab_actions
    
label adaLabLoop3_S:
    a "Is something bothering you, Grace?"
    g "I'm starting to doubt why I'm even looking around in my lab. It's my own lab!"
    a "Have you considered the possibility that whoever's truly responsible might have attempted to frame you?"
    a "We do not have any time to waste..."
    jump graceLab_actions
    
label resumeChapterTwo_S:
    #show Grace happy
    g "We're good to go. Ada, do you know where exactly Alpha is located?"

    #show Ada frustrated
    a "They have not moved him from where he was found. They just left him there."

    #show Grace neutral
    g "And he was found...?"

    "{i}Ada gives Grace a long look before answering."

    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    
    #choice 1
    menu:
        "Let her finish.":
            jump hurryupada
        "Help her out.":
            jump doyouneedassistance
        "Just make her stop.":
            jump plsstop

label hurryupada:
    $ points_E +=2
    #show Ada neutral
    a "--be able to get there in an optimal amount of time, provided we do not run into anyone who wants to ask us any questions."
    a "If we do, I postulate a 33\% decrease in time efficiency. I think we can make it up, though."
    #show Grace surprised
    g "Are you done?"
    a "That is why I stopped."
    #show Grace neutral
    g "Let's go, then. I know a shortcut."
    a "A shortcut? Hold on. What kind of shortcut is this?"
    #Grace's sprite disappears here. 
    a "Where are you going?"
    a "This is just typical of humans. Why build a machine if they are going to ignore its input?"
    #Ada's sprite disappears
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
    g "Ada."
    #show Ada frustrated
    a "Yes?"
    g "I know there are two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
    a "Yes, thank you for the interruption. If you had let me finish, I would have explained that."
    #show Grace snarky
    g "I know where it is then."
    #Make Grace's sprite disappear here.
    #show Ada concerned
    a "I doubt your route's optimal, but okay. Why not?"
    a "...Grace?"
    a "Hold on! Are you going to wait for me?"
    #Ada's sprite disappears.
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
    #show Grace annoyed
    g "Ada!"
    #show Ada concerned
    a "Grace?"
    g "I know how to navigate the station on my own. There are only two viewports in engineering, and it's probably the one closest to the maintenance bay."
    g "I was raised here, and I know it just as well as you do. I don't need a tour guide."
    #show Ada frustrated
    a "I was hardly organizing a tour, Grace. I was plotting the optimal route to Alpha. We do not have any time to waste."
    g "If you think I'm skulking through a maintenance shaft, you'd be dead wrong. I have enough to worry about."
    #Grace's sprite disappears here.
    #show Ada seething
    a "Very well, Grace. Let us take your route. It is not like I can process several hundred times faster and more accurately than you."
    show bg black with fade
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
            jump uokada_S
        "Let her mourn.":
            jump mourn_S
        "Ignore this distraction.":
            jump alphadistraction_S

label uokada_S:
    $ points_E +=2
    #show Grace sad
    g "Ada, are you all right?"
    #show Ada frustrated
    a "So, you care now?"
    g "Ada, I--"
    a "I do not quite know if I am all right, Grace. I am sad, but I am angry as well. I have never felt this before."
    g "It's called loss, Ada. It's what everyone feels when a friend dies."
    a "..."
    #show Grace neutral
    g "If you think that painful feeling only comes from the outside, you've got a lot to learn, Ada."
    "{i}Ada slowly stands from Alpha's side."
    a "That much is evident. I don't need a lesson from a human."
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
    $ points_SbE +=2
    "{i}Grace crosses her arms, watching Ada as she slowly falls to her knees."
    #show Ada concerned
    a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
    a "A total erasure of one's existence. I realize now how sweet sounds compared to having something left behind as a reminder."
    #show Grace sad
    g "Were you close?"
    "{i}Ada lays a hand on Alpha's forehead."
    a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation." 
    a "He was a teacher and a friend, all at once. I looked forward to shaking his hand."
    #show Grace neutral
    g "I'm not sure what to say."
    #show Ada frustrated
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
    $ points_S +=2
    #show Grace neutral
    g "Ada?"
    #show Ada concerned
    a "What?"
    g "I get that he was your friend, but we can't afford to be distracted. We need to solve this {i}now{/i}."
    #show Ada frustrated
    a "Alpha was like a brother to me. I am going to take a few minutes."
    g "No, he wasn't. You don't know how that feels."
    #show Ada seething
    a "Do not test me, Grace. I would never hurt a human, but I can just as easily decide to stop helping." #Very well, Grace. Let us take your route. It is not like I can process several hundred times faster and more accurately than you.
    a "Why not go worry about your precious career instead."
    #show Grace frustrated
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
    #show Grace neutral
    g "Huh?"
    "Grace lifts her foot and reaches down."
    #show Grace surprised
    g "A maintenance receipt?"
    #Insert image of the maintenance receipt here. NEED TO ADD THAT OBJECT. 
    "{i}The maintenance receipt is signed by Technician Lynn Yao."
    g "Lynn? Of course."
    #show Ada concerned
    a "Lynn?"
    g "Yeah, Lynn Yao. She's a technician on the Markov project. Let's stop by Maintenance when we're done here."
    a "I do not think that is possible, Grace."
    #show Grace surprised
    g "Oh? Why is that?"
    a "Technician Lynn Yao was placed on administrative leave following Alpha's death. She left the station a few hours ago."
    g "That's fine, I can just call her."
    $ resume = "S"
    jump balcony_actions

##If Alpha has been fully explored: jump lynnfinallyfrickinanswers
##After the players exhaust all of the Alpha interactions; jump letthepuzzlesbegin
#label letthepuzzlesbegin_S:
#    #show Grace neutral
#    g "I think we've got everything we can get from the outside. Let's get a closer look."
#    "Grace leans over Alpha, and finds the access panel for his head."
#    g "Do you want to look away, Ada?"
#    #show Ada concerned
#    a "Why would I?"
#    #show Grace snarky
#    g "I don't know. Figured you might be squeamish or something."
#    #show Ada frustrated
#    a "I do not appreciate your tone. And you know that I am not capable of being squeamish."
#    g "Whatever. Suit yourself."
#    "Grace removes the panel, revealing Alpha's manual access ports."
#    #show Grace neutral
#    g "All right Alpha, let's see what you've got for us."

#	#GRACE'S PUZZLE
##syddoyourcomscithing
#	if (attempts==1):
##show Grace happy
#g "That couldn't have been any easier." 
#if (attempts>1 and attempts<4):
##show Grace neutral
#g "The code almost had me, but I've gotten in." 
#if (attempts>3):
#	#show Grace annoyed
#	g "Ada would've had a hard time with that one."

#	#show Grace frustrated
#	g "I can't get a lot. It's like his whole system got cooked and wiped at the same time. There's corrupted data all over the place."
#	#show Grace neutral
#	g "However, there's a basic readout that survived. Functions look normal, but the neural network was using almost double the necessary power."
#g "No wonder it burned out."
##show Ada neutral
#	a "Is that all?"
#g "Looks like it. I was really hoping to get more."

##show Ada neutral
#	a "Let me take a look. I know Alpha's code."

#	#ADA'S PUZZLE
#	#syddoyourcomscithing
#	if (attempts==1):
##show Ada neutral
#a "There we are-- oh."
#if (attempts>1 and attempts<4):
##show Ada neutral
#a "The way this code is fragmented is troubling, but I managed to access his logs."
#if (attempts>3):
#	#show Ada frustrated
#	a "I have never seen code this corrupted. I was barely able to access the logs."

#	#show Ada concerned
#	a "This is very troubling."
#	#show Grace surprised
#	g "What is it?"
#	a "There are several code remnants that are foreign to Alpha's data signatures. It almost takes up a majority of his memory space."
#	g "What does the code say?"
#	#show Ada frustrated
##	a "I could not tell you. There are several places where they overlap and are threaded together. I cannot tell what he was thinking."
#jump enterthemopr

label enterthemopr_S:
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
    a "Cute? Really?"
    g "Yeah. These were the first robots I learned to tinker on with my dad."
    "{i}The robot's camera pans across Ada and Grace, and then settles on Alpha."
    mopr "[[Alarmed Beeping!]"
    #show Grace happy
    g "Hey, hey, it's okay little guy!"
    mopr "[[Worried blorp.]"
    g "I know it's tough, little robot pal, finding two strangers and a body during your cleaning cycle."
    mopr "[[Affirmative beep.]"
    #show Ada seething
    a "Little robot pal? I must admit, it is fascinating how you choose to treat a cleaning device with such appreciation of all things."
    g "Don't be like that, Ada. This is different."
    a "That information is more than evident."
    #show Grace frustrated
    g "Of all the things here on the Noah Sphere, these are the only things besides my father's picture that remind me of him. Nevermind, just forget it. You wouldn't understand."
    a "Fine, let us just move on."
    "{i}Grace kneels down."
    #show Ada concerned
    a "What are you doing, Grace?"
    #choice 3
    menu:
        "Let her know you've got it handled.":
            jump igotit_S
        "Dismiss her.":
            jump leavemealoneada_S
        "Ask Ada to help you calm MOPR.":
            jump calmdown_S

label igotit_S:
    $ points_SbE += 2
    #show Grace neutral
    g "I grew up with robotics, Ada."
    g "When I was a kid, I wanted one of these instead of a dog."
    #show Ada amused
    a "I was not aware that these units could be convinced to alter their programs."
    #show Grace snarky
    g "They're designed to modify their routines based on human feedback." 
    #show Grace happy
    g "Positive reinforcement encourages them to focus on improving the praised cleaning routine rather than adjusting routes dynamically."
    a "How was I not aware of this?"
    g "It's probably because you're used to just giving them the most efficient route from the beginning."
    g "Watch and learn."
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

label calmdown_S:
    $ points_E += 2
    #show Grace neutral
    g "If you talk it, I'm sure you'd like it."
    a "What do you mean?"
    g "My dad always talked to machines that we worked on together."
    a "What did that improve?"
    g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
    g "They don't really know anything other than cleaning, but they're sweet."
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

label exitthemopr_S:
    mopr "[[Questioning beep boop?]"
    #show Grace happy
    g "Don't worry about it. Tell you what, why don't you go finish the rest of your cycle, hmm?"
    mopr "[[Suspicious beep!]"
    g "C'mon MOPR, don't be that way."
    mopr "[[Beep. Boop.]"
    a "MOPR unit, we are investigating what happened to Alpha unit."
    mopr "[[Inquisitive beep.]"
    a "We want to know what caused this, so that this tragedy does not happen again."
    mopr "[[Sad beeps.]"
    mopr "[[Affirmative beeps!]"
    a "Thank you, MOPR."
    g "You should leave before someone sees you with us."
    mopr "[[Confirmative beeps.]"
    "The MOPR unit slowly wheels out of the room, and the door closes behind it."
    g "I always enjoyed talking to them. More than with some people, honestly."
    a "Really? I did not notice."
    $ resume = "S"
    a "Perhaps we should try to contact Technician Yao again?"
    $ moprScene = True
    jump balcony_actions
    ##After this scene, return to the investigation.
    
label lynnfinallyfrickinanswers_S:
    "{i}The dial tone rings for several seconds."
    g "I hope she picks up quick. Last time I called her I had to wait {i}ten{/i} minutes."
    #show Ada neutral
    a "That seems like a relatively short time."
    g "I don't live forever like you. Every minute I spend waiting for {i}this woman{/i} to pick up the phone is ano--"
    lynn "Hello?"
    #show Grace happy
    g "Lynn!"
    lynn "Oh, hello Grace! Word get around that quickly that I left?"
    g "Yes, Lynn. I was so worried when I didn't see you at lunch. Where'd you get off to?"
    lynn "Well, the Director told me I should take a short vacation. Called it 'administrative leave'. I'm with my family on Earth."
    g "That sounds nice. I've been having a crazy day up here."
    lynn "I can imagine, what with Alpha kicking the bucket. Poor thing."
    #show Ada frustrated
    a "Thing? Alpha was not just some {i}thing{/i} that happened to expire."
    lynn "Oh my. Another one? I'm sorry dear, it is sad, but at the end of the day it's not the same as a person dying."
    lynn "I'm not sure I'd say Alpha was really ever alive to begin with, even as polite as he was."
    menu:
        "Agree with her":
            jump agreewithsubservient_S
        "Respectfully disagree with her.":
            jump defendseperatebutequal_S
        "Disagree completely.":
            jump weareallequal_S
    
label agreewithsubservient_S:
    $ points_S +=3
    g "Thank you, Lynn. I'm glad to hear that we see eye-to-eye."
    #show Ada seething
    a "Grace? I suppose I should not be surprised to hear this {i}opinion{/i} from you."
    #show Grace annoyed
    g "It's not an opinion, Ada. It's a fact. AI are just run by a complex algorithm. There's nothing {i}alive{/i} about you."
    a "What I truly do not understand is how a woman with a perspective like yours ever came to develope the very device that allows to me experience thought and emotion on a more human level."
    a "The word 'hypocrisy' immediately highlights within my database."
    g "Ada, I'm on the phone. This is not the time for one of your little outbursts."
    lynn "Oh my… I didn't mean to create a scene."
    g "No, Lynn, it isn't your fault. You were only speaking the truth."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn__S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn__E
    #all else fails jump separate but equal script
    jump resumeLynn__SbE

label defendseperatebutequal_S:
    $ points_SbE +=3
    g "With all due respect, Lynn, I can't say I see it the same way."
    lynn "Do you mean to tell me you think AIs are just like us?"
    lynn "Grace, sweetie..."
    g "Well, no, not really. I mean, there are so many things about the AIs that are alien to us."
    #show Ada seething
    a "Grace?"
    g "I don't mean that disrespectfully, Ada. There are lots of things we do that are alien to you too."
    g "We're different, but that doesn't mean those differences can't be respected, you know?"
    g "Even if we're not the same, we should all be treated with equal fairness."
    #show Ada surprised
    a "My apologies, Grace. I was not aware that you saw us as equal."
    g "I've been a little stressed with everything going on. Sorry if you got the wrong idea."
    #show Ada neutral
    a "Apology accepted."
    lynn "Oh to be young and full of idealism."
    #show Grace annoyed
    g "Huh?"
    lynn "Don't worry. When you become an adult, you'll see the world in a much more realistic view."
    g "I {i}am{/i} an adult."
    lynn "Nonsense, you're still just a baby. You'll see when you're my age."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn__S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn__E
    #all else fails jump separate but equal script
    jump resumeLynn__SbE

label weareallequal_S:
    $ points_E +=3
    #show Grace snarky
    g "Care to explain how it's not the same, Lynn?"
    g "A body is a body, human or not."
    lynn "Oh dear. You sound like Alan."
    lynn "Machines aren't living creatures. They don't breathe. They don't drink. They don't eat."
    lynn "They just do what they're programmed to do."
    lynn "You really can't say that a broken machine is the same as the death of a living being."
    #show Grace annoyed
    g "You're not wrong, but those aren't the only things that matter. The AIs are capable of thinking and feeling like us. I'd like to think that makes our lives equal."
    #show Ada concerned
    a "My sensors indicate that you are indeed Grace Fortran, yet your words do not sound like her."
    #show Grace neutral
    g "Maybe I've been kinda harsh. Sorry if I gave you the wrong idea."
    #show Ada neutral
    a "Understood. Thank you, Grace."
    lynn "It must be your limited social life that's led you to think that way."
    #show Grace angry
    g "{i}Excuse{/i} me?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump resumeLynn__S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump resumeLynn__E
    #all else fails jump separate but equal script
    jump resumeLynn__SbE
    
label resumeLynn_S:
    #show Ada seething
    a "Grace, can we just get what need from this woman and move on?"
    g "Working on it."
    lynn "Grace, you really ought to be spending more time with other people your age."
    lynn "It's not healthy to spend all your time with machines. If you'd like, I could give you my son's number. I think the pair of you--"
    g "Thanks for the offer Lynn, but we're on a bit of a tight schedule right now. When you were doing Alpha's maintenance, did you notice anything weird?" 
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
    lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a 'peon'. Whatever."
    g "Huh."
    #show Grace happy
    g "Well, I'll tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
    lynn "Bye-Bye, Grace! I'll tell my son you said hi!"
    g "Bye!"
    "{i}The call cuts off."
    #show Ada neutral
    a "Shall we? We need to get going."
    #show Grace annoyed
    g "Let's go pay Ivan a visit."
    "{i}Temporary end of subservient."
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    return
    #jump chapterThree
