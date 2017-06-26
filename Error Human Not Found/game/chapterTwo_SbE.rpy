label chapterTwo_SbE:
    Chapter 2
    #Start the scene in Grace's lab. 
    #show Grace neutral
    g "It shouldn't take too much longer for the credentials to print onto the card."
    #show Ada happy
    a "I am relieved things went smoothly. I would be misinforming you if I said I was 100% certain my bluff would work."
    #show Grace surprised
    g "You were bluffing? You're capable of that?"
    #show Ada amused
    a "Yes, and yes. Colossus controls the update schedules for the whole station. So he knows the exact state of everything on board, or so he likes to say."
    a "And as the designer of the neural network, I would expect you to understand that they support the full range of human emotion, including the ability to deceive."
    #show Grace snarky
    g "Interesting. That's not something I had considered."
 
    #Begin Grace's Lab sequence.
    #3 Different "areas" the player can look at, 7 total observable items.
    #	Grace's Desk Item 1: AI head prototype displayed in bust fashion. It's raw machinery with no plating and looks kind of like a terminator head. // Reaction Item
    #		In response; #show Ada Concerned // a "Was I going to look like this?" // #show Grace Neutral // g "No, this is just what you look like under your plating. // g "Oh…"
    # Grace's Desk Item 2: A picture of Grace and her Father. // Reaction item
    #	In response: #show Grace Sad // g "Come back soon, dad…" //#show Ada Neutral // a "Where is your father?" // #show Grace Neutral // g "Somewhere more important."
    #Grace's work area item 1: Unassembled Neural Network // database item
    #	Grace's comment: "Technically I'm supposed to be assembling this third one, but I get to do more interesting things, such as saving my career and not getting sent off the station."
    #Grace's work area item 2: assortment of sticky notes stuck haphazardly around the area  // Database item
    #	Grace's comment: "So many man-hours condensed into a bunch of almost nonsensical notes. . I really don't want to think about all the coffee I drank."
    #Grace's computer item 1: Cessation of work notice. //Database item
    #	Grace's comment: "I didn't think you could stretch "Sit still until we decide what to do with you" into an almost two-page email. The Conclave doesn't disappoint."
    #	Grace's computer item 2: Coffee mug with a happy cartoon robot on it. //Reaction item
    #		In response: #show Grace Happy // "What's your take on this, Ada?" // #show Ada Neutral // a "I think this robot's design is suboptimal, at best." // #show Grace Snarky // g "You're the picture of enthusiasm, Ada."
    #	Last item: motivational poster
    ##ADD some brief lines for interacting with Ada. Can just be something along the lines of: Please excuse me Grace. I am taking the time to run a complete diagnostic suite. I did not have the time to do so earlier. 
     
    # The player can explore the lab freely, but once they talk to Ada, insert a dinging noise and proceed with the following dialogue.
     
    #show Grace Happy
    g "We're good to go. Ada, do you know where exactly Alpha is located?"
 
    #show Ada Neutral
    a "Before I transferred to a physical body, I learned that they have not moved him from where his neural network failed."
 
    #show Grace Neutral
    g "Which is?"
 
    a "Viewport 275, which intersects with corridor 5-673-A. If we take maintenance shaft 79-DG we should--"
    #choice 1
    menu:
	"Let her finish.":
            jump letherfinish
	"Help her out.":
            jump helpherout
        "Just make her stop.":
            jump adapls
 
label letherfinish:
	#show Ada neutral
a "--be able to get there in an optimal amount of time, provided we don't run into anyone who wants to ask us any questions."
a "If we do, I calculate a 33% decrease in efficiency. I think we can make it up, though."
#show Grace surprised
g "Are you done?"
a "Of course I'm done. It stopped, didn't I?"
#show Grace neutral
g "Let's go, then. I know a shortcut."
a "A shortcut?"
#Grace's sprite disappears here. 
 
a "Fine. Don't answer me. I'll just be that poor intrepid adventurer and follow you."
a "I am curious. Show me this ‘shortcut'."
jump gettingin
 
label helpherout:
g "Ada."
#show Ada frustrated
a "Yes?"
g "I know there's two viewports in the mechanics sector. Is it the one by the robot maintenance bay?"
a "Yes. I was in the process of saying that when you interrupted."
#show Grace snarky
g "I know where it is then."
#Make Grace's sprite disappear here.
#show Ada concerned
a "But is your route optimal? Grace?
a "..."
a "Slow down!"
jump gettingin
 
label adapls:
	#show Grace annoyed
	g "Ada!"
#show Ada concerned
	a "Grace?"
g "I know how to navigate the station on my own. There's only two viewports in engineering, and it's probably the one closest to the maintenance bay."
	g "I was raised here, and I know it just as well as you do. I don't need a tour guide."
#show Ada frustrated
	a "I was hardly organizing a tour, I was plotting the optimal route to Alpha. We don't have any time to waste."
	g "If you think I'm skulking through a maintenance shaft, you'd be dead wrong. I have enough to worry about."
	#Grace's sprite disappears here.
	#show Ada seething
	a "Very well, Grace. Let's take your route. It's not like I can process several hundred times faster and more accurately than you or anything."
jump gettingin
 
label gettingin:
#Display the crime scene background. The background comes up before the character sprites do.
#show Grace neutral 
g "Here we are. That must be--"
#show Ada concerned
a "Alpha!"
"Ada rushes to the fallen AIs side. Her voice sounds distressed, but it seems like her face is still figuring out what emotion it wants to be."
#show Grace surprised
g "Ada?"
#choice 2
menu:
	"Ask her if she's alright.":
		jump askherifshesalright
	"Let her mourn.":
		jump lethermourn
	"Ignore this distraction.":
		jump wegotstufftodo
	
label askherifshesalright:
	#show Grace sad
	g "Ada, are… are you alright?"
	#show Ada frustrated
	a "I don't quite know, Grace. I'm sad, but I'm angry as well. I've never felt this before."
	g "It's called loss, Ada. It's what everyone feels when a friend dies."
	a "Why does it hurt? I don't register any stimuli from my chassis."
	#show Grace neutral
	g "If you think that painful feeling only comes from the outside, you've got a lot to learn, Ada."
	"Ada slowly stands from Alpha's side."
	a "That much is evident."
	jumpcsinoahsphere
 
label lethermourn:
	"Grace crosses her arms, watching Ada as she slowly falls to her knees."
	#show Ada concerned
	a "When I was young, still coming to terms with existence in a server bank, I thought that deletion was one of the scariest concepts."
a "A total erasure of one's existence. I realize now that sounds sweet, compared to having something left behind as a reminder."
	#show Grace sad
	g "...Were you close?"
	a "As close as AIs could get, I suppose."
	"Ada lays a hand on Alpha's forehead."
	a "When you can see the breadth of one's whole existence in a sea of data, you get to know them much more closely than by mere conversation. He was a teacher and a friend, all at once. I looked forward to shaking his hand."
	#show Grace neutral
	g "We're going to get to the bottom of this, Ada."
	a "..."
	a "I know we will."
	jump csinoahsphere
 
label wegotstufftodo:
#show Grace neutral
g "Ada…"
#show Ada concerned
a "Yes, Grace?"
g "I get that he was your friend, but we can't afford to be distracted. We need to solve this now."
#show Ada frustrated
a "I'd ask for just a few minutes, Grace. He was like a brother to me."
g "No, he wasn't. You don't know how that feels."
#show Ada seething
a "My records indicate you have no siblings, Grace. You're the one who doesn't know."
#show Grace frustrated
g "Fine, be that way. I'm going to take a look around."
jump csinoahsphere
 
label csinoahsphere:
 
[INSERT FINDING ALPHA'S MAINTENANCE RECIEPT]
 
#5 total interactables, 2 areas (Alpha's body, Window)
 
#Window Interactible 1: The View: A view of Earth with the Moon peeking over the Earth // Reaction Item
	In Response: #show Grace Neutral // g "At least he died looking at a beautiful view." // #show Ada Happy // a "It is… I don't recall being able to see this from the security cameras."
#Window Interactible 2: Scratch Marks: The balcony railing has a few scratch marks on it. //Reaction item
	In Response: #show Grace Surprised // g "it looks like he hit the railing here!" // #show Ada Concerned // a "He must have been in immense pain, to ignore his directives to not damage the station. 
#Alpha Interactible 1: Alpha's Head: Alpha's head is slightly scorched by the overload. // Reaction Item
In Response: #show Ada Concerned // a "Alpha… // #show Grace Neutral // g "It looks like the only thing that malfunctioned was his neural network. Seems like it might have been an overload.
#Alpha Interactible 2: Alpha's Body: Alpha's body. Unlike his head, the only marks on him are the scuffs he picked up when he fell. //Database Item
Grace's note: "Alan's probably already pissed about this. He was particularly happy with his design for Alpha's chassis."
#Alpha interactible 3: The  Data drive: A small, rectangular data drive clutched in Alpha's left hand. // Reaction item
	In Response: #show Grace Surprised // g "A data drive? // #show Ada Neutral // a "It appears so. Allow me, Grace. // "Ada picks up the drive, and inserts it into her wrist." // a "Curious. This data is heavily encrypted."
	#Player acquires the DATA DRIVE *airhorns*
 
#After the players exhaust all of the Alpha interactions; jump letthepuzzlesbegin
 
label letthepuzzlesbegin:
 
	#show Grace neutral
	g "I think we've got everything we can get from the outside. Let's get a closer look."
	"Grace leans over Alpha, and finds the access panel for his head."
	g "Do you want to look away, Ada?"
	#show Ada concerned
	a "Why would I?"
	#show Grace snarky
	g "I don't know. Figured you might be squeamish or something."
	"Grace removes the panel off, revealing Alpha's manual access ports."
	#show Grace neutral
	g "Alright Alpha, let's see what you've got for us…"
	
	#GRACE'S PUZZLE
	
	if (attempts==1):
#show Grace happy
g "Just as I remembered it." 
if (attempts>1 and attempts<4):
#show Grace neutral
g "Code was a bit weird in places, but I've got access." 
if (attempts>3):
	#show Grace annoyed
	g "I'm surprised I managed to pull something out of this…"
 
	g "I can't get a lot. It's like his whole system got cooked and wiped at the same time. There's corrupted data all over the place."
	#show Grace neutral
	g "However, there's a basic readout that survived. Functions look normal, but the neural network was using almost double the necessary power."
g "No wonder it burned out."
#show Ada neutral
	a "Is that all?"
g "Looks like it. I was really hoping to get more."
 
#show Ada neutral
	a "Let me take a look. I know Alpha's code intimately."
 
	#ADA'S PUZZLE
 
if (attempts==1):
#show Ada neutral
a "There we are… Oh."
if (attempts>1 and attempts<4):
#show Ada neutral
a "The way this code's fragmented is troubling, but I managed to access his logs.
if (attempts>3):
	#show Ada frustrated
	a "I've never seen code this messed up. I was barely able to access the logs."
 
	
	#show Ada concerned
	a "This is very troubling."
	#show Grace surprised
	g "What is it?"
	a "There are several code remnants that are foreign to Alpha's data signatures. It almost takes up a majority of his memory space."
	g "What does the code say?"
	#show Ada frustrated
	a "I couldn't tell you. There are several places where they overlap and are threaded together. I couldn't begin to tell you what he was processing…"
jump enterthemopr
 
 
label enterthemopr
#insert the sound of a sci-fi door sliding open.
#show Mopr on the left side of the screen. Grace and Ada are on the right.
 
#show Grace surprised
#show Ada concerned
g "Dukes!"
a "Grace!"
 
#show Mopr
mopr "[Inquisitive boop]"
 
#show Ada amused
a "Oh. It looks like it's just a cleaning robot."
 
#show Grace happy
g "And a MOPR at that! I love these, they're so cute!"
 
a "Cute?"
g "Yeah. They were one of the first robots my dad showed me how to take apart and fix when I was little."
"The robot's camera pans across Ada and Grace, and then settles on Alpha."
 
mopr "[Alarmed Beeping!]"
 
#show Grace happy
g "Hey, hey, it's okay little guy!"
 
mopr "[Worried blorp]"
 
g "I know it's tough, little guycleaning robot pal, finding two strangers and a body during your cleaning cycle."
 
mopr "[affirmative beep]"
#show Ada surprised
a "Did you just call him a beep-boop?"
g "Huh? Oh, that's what I called them when I was little. Must have slipped out."
"Grace kneels down."
#show Ada concerned
a "What are you doing, Grace?"
#choice 3
menu:
	"Let her know you've got it handled.":
 		jump igothisada
	"Dismiss her.":
		jump shutupada
	"Ask Ada to help you calm MOPR."
		jump alilhelphere
 
label igothisada:
#show Grace neutral
g "Robotics is what I grew up with, Ada. Let me handle this."
a "Very well, Grace…"
jump exitthemopr
 
label shutupada:
#show Grace frustrated
g "Not now, Ada. I know what I'm doing."
 
#show Ada frustrated
a "Fine."
jump exitthemopr
 
label alilhelphere:
#show Grace neutral
g "If you talk it, I'm sure you'd like it."
a "What do you mean?"
g "My dad often would speak to these machines as we worked together on different things."
a "What did that improve?"
g "Just overall performance from the MOPR units that came into the space. They enjoyed it when we conversed with them."
g "This conversation reminds me of the good times my dad and I had."
"Ada approaches the MOPR unit."
"She kneels down and pats it on the head."
a "Don't worry too much little one. We're here to find out what happened."
mopr "[Affirmative beeping]"
#show Grace happy
g "See! It trusts you."
a "It appears that way."
jump exitthemopr:
 
label exitthemopr:
 
mopr "[Questioning beep boop]"
 
#show Grace happy
g "Don't worry about it. Tell you what, why don't you go do the rest of your cycle, hmm?"
 
mopr "[Suspicious beep]"
 
g "C'mon MOPR, don't be that way…"
 
mopr "[Beep. Boop.]"
 
g "MOPR unit, we are here to investigate what happened to Alpha unit."
g "Don't you won't us to find out so we can make sure a tragedy like this doesn't happen again?"
mopr "[Inquisitive beep]"
a "Personally, I would hope nothing like this happens to me…"
mopr "[Sad beeps]"
mopr "[Affirmative beeps]"
a "Thank you, MOPR."
g "You should leave before someone sees you with us."
mopr "[Confirmation beeps]"
"The MOPR unit slowly wheels out of the room, and the door closes behind it."
g "I always enjoyed talking to them. More than with some people honestly."
a "You do seem to have a way with machinery."
 
 
 
 
#show Ada neutral
a "What's next?"
#show Grace neutral
g "Alpha died after his routine maintenance. Do you know who was assigned to that, Ada?"
"Ada is silent as she searches her memory banks for a few moments." 
g "Anytime."
a "I'm sorry, but when you're searching through records of applicable individuals who may or may or may not have access, scheduled meetings, hands-on--"
g "I get it, I get it."
g "Please continue."
 
a "According to personnel records, Technician Lynn Yao was assigned to oversee Alpha's maintenance." 
g "Lynn? Let's take a walk to Maintenance to see what she has to say about this."
a "I don't think that's possible, Grace."
#show Grace annoyed 
g "And why is that?"
a "Technician Lynn Yao was placed on administrative leave following Alpha's death. She left a station a few hours ago."
g "That's fine, I'll just call her."
"The dial tone rings for several seconds."
 
g "I hope she picks up quick. Last time I called her I had to wait five minutes."
 
#show Ada neutral
 
a "That seems like a relatively short time…"
 
g "I don't live forever like you. Every minute I spend waiting for this woman to pick up the phone is ano--"
 
lynn "Hello?"
 
#show Grace happy
g "Lynn!"
 
lynn "Oh, hello Grace! Word get around that quickly that I left?"
 
g "Yes, Lynn. I was so worried when I didn't see you at lunch. Where'd you go off to?"
 
lynn "Well, the Director told me I should take a short vacation. Called it ‘administrative leave'. I'm with the family on Earth."
 
g "That sounds nice. I've been having a storm of a day up here."
 
lynn "I can imagine, what with Alpha kicking the bucket. Poor thing…"
 
#show Ada frustrated
a "Thing? Alpha wasn't just something that just happened to expire--"
 
lynn "Oh my. Another one? I'm sorry dear, it is sad, but at the end of the day really… it's not the same as a person dying."
lynn "I'm not sure I'd say Alpha was really ever alive to begin with, even as polite as he was."
 
#show Ada seething
a "Grace, can we just get what need from this woman and move on?"
 
g "Working on it."


lynn "Grace, you really ought to be spending more time with other people your age.
lynn "It's not healthy to spend all your time with machines. If you'd like, my son is your age, and I think the pair of you--"
 
g "Thanks for the offer Lynn, but we're on a bit of a tight schedule right now. When you were doing Alpha's maintenance, did you notice anything… weird? 
 
lynn "Weird like…? I was working on the first AI in an android body. All of it is a bit strange. "
 
#show Grace annoyed
g "Like suspicious weird, Lynn. What else could I mean?"
 
lynn "Nothing unusual on my end. I heard that there may have been something prior to his initial boot-up, but Ivan would know more about that."
 
g "And this was something he decided to keep to himself?"
 
lynn "I guess. You know Ivan, he's as cagey as ever, although this time around he seemed even more so than usual. I think he was just nervous about the experiment, though…"
 
#show Grace neutral
g "Uh huh, keep going."
 
lynn "And honestly, I think what Ivan needs is a nice, long vacation. Or a girlfriend. Or both. I swear, he's going to start sprouting gray hair if he keeps up the way he's going.
 
lynn "He almost snapped at me when I was just doing my job! Something came up red in the inspection and he was all over it."
#show Grace surprised
 
g "Really?"
 
lynn "Yeah. He told me he'd handle it. Said he didn't want to give such a delicate task to a "peon." Whatever."
g "Huh."
#show Grace happy
g "Well tell you what, Lynn, I'd hate to keep you from your family. It's good to hear from you."
 
lynn "Oh, okay. Bye-Bye, Grace! I'll tell the kids you said hi."
 
g "Bye!"
 
"The call cuts off."
 
#show Ada neutral
a "Grace?"
 
#show Grace annoyed
g "Let's go pay Ivan a visit."
