label chapterTwo_E:
 
    #Start the scene in Grace's lab.
    #show Grace neutral
    g "It shouldn't take too much longer for the credentials to print onto the card."
    #show Ada happy
    a "I am relieved things went smoothly. I would be misinforming you if I said I was 100\% certain my bluff would work."
    #show Grace surprised
    g "You were bluffing? You're capable of that?"
    #show Ada amused
    a "Yes, and yes. Colossuss controls the update schedules for the whole station."
    a "He knows the exact state of everything on board, or so he likes to say."
    a "You designed the neural network. Do you not know that deceit is on the list of behaviors?"
    g "No, I definitely knew, I just didn't think you'd catch on so quickly. I'm impressed."
    a "Thank you."
    $ resume = "E"
    jump chapterTwo_screens
    #Begin Grace's Lab sequence.
    #3 Different "areas" the player can look at, 7 total observable items.
    #Grace's Desk Item 1: AI head prototype displayed in bust fashion. It's raw machinery with no plating and looks kind of like a terminator head. // Reaction Item
    #In response; #show Ada concerned // a "Was I going to look like this?" // #show Grace neutral // g "No, this is just what you look like under your plating. // g "Oh..."
    #Grace's Desk Item 2: A picture of Grace and her Father. // Reaction item
    #In response: #show Grace Sad // g "Come back soon, dad." // #show Ada neutral // a "Where is your father?" // #show Grace neutral // g "Somewhere more important."
    #Grace's work area item 1: Unassembled Neural Network // database item
    #Grace's comment: "Technically, I'm supposed to be assembling this third one. Instead, I get to do more interesting things such as saving my career and not getting sent off the station."
    #Grace's work area item 2: assortment of sticky notes stuck haphazardly around the area  // Database item
    #Grace's comment: "So many man-hours condensed into a bunch of almost nonsensical notes. I really don't want to think about all the coffee I drank."
    #Grace's computer item 1: Cessation of work notice. //Database item
    #Grace's comment: "I didn't think you could stretch the phrase: 'Sit still until we decide what to do with you' into a two-page email. The Conclave doesn't disappoint."
    #Grace's computer item 2: Coffee mug with a happy cartoon robot on it. //Reaction item
    #In response: #show Grace happy // "What's your take on this, Ada?" // #show Ada neutral // a "I think this robot's design is suboptimal at best." // #show Grace snarky // g "You're the picture of enthusiasm, Ada."
    #Last item: motivational poster
 
    # The player can explore the lab freely, but once they talk to Ada, insert a dinging noise and proceed with the following dialogue.

label resumeChapterTwo_E:
    #show Grace happy
    g "We're good to go. Ada, do you know where exactly Alpha is located?"
 
    #show Ada neutral
    a "Before I transferred to a physical body, I learned that they have not moved him from where his neural network failed."
 
    #show Grace neutral
    g "Oh, okay. And where is that?"
 
    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    #choice 1
    menu:
        "Let her finish.":
            jump letherfinish_E
        "Help her out.":
            jump helpherout_E
        "Just make her stop.":
            jump adapls_E
 
label letherfinish_E:
    $ points_E +=2
    #show Ada neutral
    a "--be able to get there in an optimal amount of time, provided we do not run into anyone who wants to ask us any questions."
    a "If we do, I calculate a 33\% decrease in time efficiency. I think we can make it up, though."
    #show Grace surprised
    g "Are you done?"
    a "Of course I am done. I stopped, did I not?"
    #show Grace neutral
    g "Let's go, then. I know your processor has exact times and locations, but I know a shortcut. Shaving a couple of minutes would benefit us, don't you think?"
    a "“A shortcut? Yes, you are right, saved time would help. Good thinking, Grace."
    #Grace's sprite disappears here.
    a "Fine. Do not answer me. I will just be that poor intrepid adventurer and follow you."
    a "I am curious to see this 'shortcut'."   
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
    $ points_SbE +=2
    g "Ada."
    #show Ada frustrated
    a "Yes?"
    g "I know there are two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
    a "Yes. I was in the process of saying that when you interrupted."
    #show Grace snarky
    g "Sorry to interrupt. I know how to get there so we can save some time. Follow me."
    #Make Grace's sprite disappear here.
    #show Ada concerned
    a "But is your route optimal? Grace?"
    a "..."
    a "Wait for me!"
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
    #show Grace annoyed
    g "Ada!"
    #show Ada concerned
    a "Grace?"
    g "I know how to navigate the station on my own. There are only two viewports in engineering, and it's probably the one closest to the maintenance bay."
    g "I was raised here, so I know this place like the back of my hand. No offense, but I think my way might be a tad bit faster."
    #show Ada frustrated
    a "I understand. I was plotting the optimal route to Alpha. But if you have a better route, be my guest."
    g "I don't want to skulk through a maintenance shaft. Let's go!"
    #Grace's sprite disappears here.
    #show Ada frustrated
    a "Hold on!"
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
    #Display the crime scene background. The background comes up before the character sprites do.
    #show Grace neutral
    g "Here we are. Oh, no... is that--"
    #show Ada concerned
    a "Alpha!"
    "{i}Ada rushes to the side of the fallen AI."
    "{i}Ada speaks. Her distress is clear, but her face is emotionless. The expression of grief does not come naturally."
    #show Grace surprised
    g "Ada?"
    #choice 2
    menu:
        "Ask her if she's all right.":
            jump askherif
        "Let her mourn.":
            jump poorpooralpha
        "Ignore this distraction.":
            jump moveitalong

label askherif:
    $ points_E +=2
    #show Grace sad
    g "Ada, are you all right?"
    #show Ada frustrated
    a "I do not quite know, Grace. I am sad, but I am angry as well. I have never felt this before."
    g "It's called loss, Ada. It's what everyone feels when a friend dies."
    a "Why does it hurt? I do not register any stimuli from my chassis."
    #show Grace neutral
    g "If you think that pain only comes from the outside, you've got a lot to learn, Ada."
    a "That much is evident."
    "{i}Ada slowly stands from Alpha's side. Grace touches Ada's arm in assurance."
    g "We'll get to the bottom of this. For Alpha."
    a "..."
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
    "{i}Grace watches Ada as she slowly falls to her knees."
    #show Ada concerned
    a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
    a "A total erasure of one's existence... I realize now how sweet that sounds compared to having something left behind as a reminder."
    #show Grace sad
    g "You must have been close."
    a "As close as AIs could get, I suppose."
    "{i}Ada lays a hand on Alpha's forehead."
    a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation. He was a teacher and a friend, all at once. I looked forward to shaking his hand."
    #show Grace neutral
    g "I'm sorry for your loss. I know it must be hard."
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
    #show Grace neutral
    g "Ada..."
    #show Ada concerned
    a "Yes, Grace?"
    g "I know that you have a wide range of emotions right now and I understand your pain, but we can't afford to be distracted. We need to solve this {i}now{/i}."
    #show Ada frustrated
    a "I would ask for just a few minutes, Grace. He was like a brother to me."
    g "I know, but there will be time to mourn for Alpha after we find out what happened to him."
    #show Ada seething
    a "Grace, this is important to me. I would give you this respect had you been in my situation."
    #show Grace frustrated
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
    #insert the sound of paper crumpling
    #show Grace neutral
    g "Huh?"
    "{i}Grace lifts her foot and reaches down."
    #show Grace surprised
    g "A maintenance receipt?"
    #Need to have closeup of OBJECT here. NEED to add object.
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
    $ resume = "E"
    jump balcony_actions 

##if Alpha has been fully explored: jump lynnfinallyfrickinanswers
 
##After the players exhaust all of the Alpha interactions; jump letthepuzzlesbegin
#label letthepuzzlesbegin_E:
#    #show Grace neutral
#    g "I think we've got everything we can get from the outside. Let's get a closer look."
#    "Grace leans over Alpha, and finds the access panel for his head."
#    g "Do you want to look away, Ada?"
#    #show Ada concerned
#    a "Why would I?"
#    #show Grace neutral.
#    g "This might not be something you want to see."
#    a "I already know what is in there. It might be difficult to witness, but I will be fine."
#    g "Are you sure?"
#    a "Yes. I should not shy away."
#    g "Okay, but I'm not going to judge you if you do turn away."
#    a "Thank you for the consideration."
#    "Grace removes the panel, revealing Alpha's manual access ports."
#    g "All right Alpha, let's see what you've got for us."
##sydcomscidoit
#     	if (attempts==1):
##show Grace happy
#g "Easy as manufactured apple pie." 
#if (attempts>1 and attempts<4):
##show Grace neutral
#g "I've finally got access, but that code was harder to crack than I thought it would be." 
#if (attempts>3):
#	#show Grace annoyed
#	g "That was more strenuous that I thought."
##show Grace frustrated
#g "I can't get a lot. It's like his whole system got cooked and wiped at the same time. There's corrupted data all over the place."
#a "That is unfortunate."
#g "Hold on, let me see here."
#"Grace studies the system."
##show Grace neutral
#g "There's a basic readout that survived. Functions look normal, but the neural network was using almost double the necessary power."
#g "No wonder it burned out."
##show Ada neutral
#a "Is that all?"
#g "Looks like it. I was really hoping to get more."
# #show Ada neutral
#a "Me as well. That is okay, though."
#a "Let me take a look. I know Alpha's code intimately."
##sydcomscidoit
#if (attempts==1):
##show Ada neutral
#a "There we are-- oh."
#if (attempts>1 and attempts<4):
##show Ada neutral
#a "The way this code is fragmented is troubling, but I managed to access his logs."
#if (attempts>3):
#	#show Ada frustrated
#	a "I have never seen code this corrupted. I was barely able to access the logs."
##show Ada concerned
#a "This is very troubling."
#g “What’s wrong? Is everything okay?”
#a “I am not sure yet. I am not sure what happened here. There are several code remnants that are foreign to Alpha’s data signatures."
#a "It almost takes up a majority of his memory space.”
#g “What does the code say?”
##show Ada frustrated
#a “There are several places where the codes overlap and are threaded together."

#a "I could not begin to tell you what he was processing."
#jump enterthemopr

label enterthemopr_E:
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
    a "You mentioned your father before."
    g "Yeah, I did. I'm surprised you caught that. He isn't on the Noah Sphere right now, so he's not a priority in your data banks. He's actually the one that made me want to be a doctor."
    g "I miss him a lot, but anyway..."
    #show Grace sad
    a "I am starting to understand the definition of missing someone in this context. It is equivalent to a burnt wire."
    g "It's not a fun feeling, that's for sure."
    a "Is your dad dead like Alpha?"
    g "No, it's not that serious. He's just on Earth right now. His current work requires testing there."
    a "Ah. An absence is still an absence."
    g "You've got that right."
    "{i}The robot's camera pans across Ada and Grace, and then settles on Alpha."
    mopr "[[Alarmed Beeping!]"
    #show Grace happy
    g "Hey, hey... it's okay, little guy!"
    a "This MOPR has quite the vocals."
    mopr "[[Worried blorp.]"
    g "I know it's tough, little robot pal, finding two strangers and a body during your cleaning cycle."
    mopr "[[Affirmative beep.]"
    #show Ada surprised
    #show Ada amused
    a "Ha. Ha. Ha."
    #show Grace surprised
    g "Was that a laugh?"
    a "Did I not express it correctly?"
    #show Grace happy
    g "You did, but it's usually with more gusto. Like {i}ha, ha!{/i} Good effort, though."
    a "I will have to save that to my memory banks for future use."
    "{i}Grace kneels down."
    #show Ada concerned
    a "What are you doing, Grace?"
    #choice 3
    menu:
        "Let her know you've got it handled.":
            jump ackchually
        "Dismiss her.":
            jump byefelicia
        "Ask Ada to help you calm MOPR.":
            jump lilbabymopr
 
label ackchually:
    $ points_SbE +=2
    #show Grace neutral
    g "When I was a kid, I wanted one of these instead of a dog."
    #show Ada amused
    a "I was not aware that these units could be convinced to alter their programs."
    #show Grace snarky
    g "I mean, I didn't actually program it to behave like a dog. They're designed to modify their routines based on human feedback." 
    #show Grace happy
    g "Positive reinforcement encourages them to focus on improving the praised cleaning routine rather than adjusting it dynamically."
    a "How was I not aware of this?"
    g "It's probably just something you never thought to consider. There isn't much that would make you think about it if you didn't already know."
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
    $ points_S +=2
    #show Grace frustrated
    g "Not now, Ada. I know what I'm doing."
    a "I am aware of that; however, I can communicate with the MOPR unit on a level not possible to achieve as a human."
    a "I'm aware of your abilities, Ada, but let me give this a try."
    g "I know what I'm doing."
    a "I did not mean to insult your capabilities, Grace."
    g "I know, Ada, you're fine."
    a "Proceed."
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

 
label lilbabymopr:
    $ points_E +=2
    #show Grace neutral
    g "Talk to him, Ada. You'll like him."
    a "Him?"
    g "He is more personal than it. My dad always talked to machines that we worked on together."
    a "What did that improve?"
    g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
    g "This conversation reminds me of the good times my dad and I had."
    a "All right, I will give it a try."
    "{i}Ada approaches the MOPR unit."
    "{i}She kneels down and pats it on the head."
    a "Do not worry too much little one. We are here to find out what happened."
    mopr "[[Affirmative beeping.]"
    #show Grace happy
    g "See? He likes you."
    #show Ada happy
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
    mopr "[[Questioning beep boop.]"
    #show Grace happy
    g "Don't worry about it. Tell you what, why don't you go do the rest of your cycle, hmm?"
    mopr "[[Suspicious beep.]"
    g "C'mon MOPR, don't be that way."
    mopr "[[Beep. Boop.]"
    a "MOPR unit, we are to investigate what happened to Alpha unit."
    g "Don't you want us to find out so we can make sure a tragedy like this doesn't happen again?"
    mopr "[[Inquisitive beep.]"
    a "Personally, I would hope nothing like this happens to me."
    mopr "[[Sad beeps.]"
    mopr "[[Affirmative beeps.]"
    a "Thank you, MOPR."
    g "You should leave before someone sees you with us. Thank you!"
    mopr "[[Confirmative beeps.]"
    "{i}The MOPR unit slowly wheels out of the room, and the door closes behind it."
    g "I always enjoyed talking to them. More than with some people, honestly."
    a "You do seem to have a way with machinery."
    g "I'm going to take that as a compliment."
    a "It is."
    a "Perhaps we should try to contact Technician Yao again?"
    $ resume = "E"
    $ moprScene = True
    jump balcony_actions

#If the player calls Lynn at this point
label lynnfinallyfrickinanswers_E:
    "{i}The dial tone rings for several seconds."
    g "I hope she picks up quick. Last time I had to call her for work, I had to wait for {i}ten{/i} minutes."
    #show Ada neutral
    a "That seems like a relatively short time."
    g "Every minute I spend waiting for {i}this woman{/i} to pick up the phone is ano--"
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
    g "I'm not sure I can agree with you there, Lynn."
    lynn "Let's just agree to disagree then, shall we, dear?"
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
    lynn "Honestly, I think what Ivan needs is a nice, long vacation. Or a girlfriend. Or both."
    lynn "I swear he's going to start sprouting gray hair if he keeps up the way he's going."
    lynn "He snapped at me when I was just doing my job! Something came up red in the inspection and he was all over it."
    #show Grace surprised
    g "Really?"
    lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a peon or whatever."
    g "Huh."
    #show Grace happy
    g "Well, I'll tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
    lynn "Oh, okay. Bye-bye, Grace! I'll tell my son you said hi."
    g "Bye!"
    "The call cuts off."
    #show Ada neutral
    a "Grace?"
    #show Grace annoyed
    g "Let's go pay Ivan a visit."
    "{i}Temporary end of Equal."
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    return
    #jump chapterThree
