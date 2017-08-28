label chapterThree_SbE:
    window hide
    $quick_menu = False
    scene bg black with fade
    scene bg chapterThree with fade
    $renpy.pause(3.0)
    scene bg hallwayGrace with fade 
    $quick_menu = True
    "{i}Grace and Ada wander into the hall.{/i}"
    show Grace neutral at left
    show Ada neutral at right
    g "One of the overseers of the Markov Project is Ivan Babbage."
    a "Right. I have worked with him before."
    g "He's quite the character, so this should be fun. Any exchange with Ivan is always interesting."
    a "How so?"
    #choice 1
    hide Ada
    hide Grace
    $quick_menu = False
    menu:
        "Explain why.":
            jump explain_SbE
        "Tell her that it's none of her business.":
            jump noneya_SbE
        "Change the subject.":
            jump subject_SbE
       
label explain_SbE:
    $quick_menu = True
    $points_E += 3
    show Grace neutral at left
    show Ada neutral at right
    g "I forget that your only interaction with Ivan is research based, and you haven't engaged with him in an actual conversation."
    g "Well, let's just say that he's not the most chipper person on the Noah Sphere, and he's definitely not my biggest fan."
    show Ada amused
    a "Did you do something to make him angry?"
    show Grace annoyed
    g "Who said I did anything to him? He just has this weird aggression toward me. It's almost like he's jealous or something."
    show Ada neutral
    a "Jealous? Of what?"
    g "I don't know. He's a big grump and has a stick up his--"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume_E
    #all else fails jump separate but equal script
    jump ch3resume_SbE
 
label noneya_SbE:
    $quick_menu = True
    $ points_S +=3
    show Grace snarky at left
    show Ada neutral at right
    g "I don't know how much information I'm supposed to divulge about an overseer to an AI. I'm not entirely comfortable discussing him with you."
    a "Yes, but I'm about to meet him anyway. Should I be prepared for any certain mannerisms?"
    g "Well I guess you can just see for yourself."
    show Ada amused
    a "So will this actually be fun? I cannot understand your tone."
    show Grace neutral
    g "No, Ada. This won't be a fun interview. Ivan is a real--"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume_E
    #all else fails jump separate but equal script
    jump ch3resume_SbE
 
label subject_SbE:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    g "Who knows? Or cares? Anyway, the goal here is to determine what could have possibly happened during the upload and Ivan is the one to--"
    show Ada amused
    a "Well, his research is very conductive. He seems very bright."
    show Grace snarky
    g "Yeah, Ivan is a real treat." 
    show Ada neutral
    a "A treat? Like a present? How can a person be a present?"
    show Grace neutral
    g "Ad, it was sarcasm."
    show Ada amused
    a "So Ivan is not a treat because sarcasm is when you say something but do not mean it."
    show Grace happy
    g "Yes, exactly that. Ivan is the least present-like person you could imagine." 
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume_E
    #all else fails jump separate but equal script
    jump ch3resume_SbE

label ch3resume_SbE:
    #Insert footsteps here
    scene bg hallwayBalcony
    "{i}Grace and Ada turn a corner and run into Ivan outside of his lab. He glowers at Grace, and then does a double takes at Ada."
    #show Ivan dour at center
    show Grace neutral at left
    show Ada neutral at right
    ivan "What have you done this time, Fortran? Why is one of the androids walking about?"
    show Grace annoyed
    ivan "You know what happened to Alpha, and the entire lab has been put on hiatus because of it."
    ivan "This is an outrage! The entire Conclave will be in an uproar about this."
    show Ada amused
    show Grace angry
    g "Listen, Babbage, this wasn't my doing. Ada uploaded herself without any consent from me or anyone else. I didn't ask her to--"
    show Ada frustrated
    a "Hello, I am right here. No need to talk around me."
    #show a different Ivan expression in here at some point. Expressions need to vary more. 
    ivan "If the Director finds out about this--"
    show Grace annoyed
    g "She doesn't have to. Not now, anyway. She has enough on her plate."
    show Grace neutral
    g "This is low on the totem pole on the list of things for her to worry about."
    ivan "We'll see about that. But what's going on? Why are you two together?"
    show Ada neutral
    a "We want to figure out what happened to Alpha."
    #show Ivan defensive
    ivan "Aren't there external investigators on the case?"
    g "Yes, but we want to get a head start. We have some questions for you."
    "{i}Ivan crosses his arms."
    ivan "I'll consider answering them."
    g "First of all, what are you doing here? The labs are supposed to be closed off to everybody. That includes you."
    "{i}Ivan stays silent."
    show Grace annoyed
    g "Spit it out."
    ivan "I'm hesitant about leaving my lab alone for such a long amount of time. I don't trust anyone to not break in and contaminate my research."
    show Grace surprised
    g "Even if that means opposing the Conclave's order?"
    ivan "If you were a halfway decent researcher, you would do the same."
    show Grace annoyed
    g "Do you want to take this road with me, Ivan? Because last time I checked, {i}you{/i} were--"
    show Ada annoyed
    a "Let us move on now. I think that would be for the best."
    "{i}Grace takes a deep breath."
    show Grace neutral
    g "Okay. First of all, where exactly were you when Alpha died?"
    #show Ivan defensive
    ivan "How dare you imply me in any of this! Alpha was {i}my{/i} brainchild." 
    ivan "He was the prime example of what an AI could accomplish in a physical form. I created that."
    #show Ivan disgusted
    ivan "And for you to insinuate that I would have any involvement in his demise is the worst insult you could--"
    show Grace surprised
    show Ada surprised
    g "Hey, wait a second. You weren't the only one working on this project."
    a "We are not insinuating anything, Ivan. As the project overseer, you knew the most about Alpha's process. That is why we have come to you."
    show Ada neutral
    show Grace neutral
    #show Ivan defensive
    a "We do not wish to insult you. We just need to be exhaustive."
    #choice 2
    hide Grace
    hide Ada
#    hide Ivan
    $quick_menu=False
    menu:
        "Disagree with her.":
            jump disagree_SbE
        "Agree with her.":
            jump agree_SbE
        "Remain indifferent.":
            jump nothing_SbE

label disagree_SbE:
    $quick_menu = True
    $points_S +=3
    show Grace annoyed at left
    show Ada neutral at right
    #show Ivan at center (With some sort of expression fitting him)
    g "But he's being absurd! Everything coming out of his mouth is preposterous! He is Alpha's overseer, of course he has some responsibility here."
    #show Ivan dour
    ivan "I refuse to acknowledge any of these accusations."
    show Ada concerned
    a "I do not think she means--"
    g "Yes, I do. Don't speak for me."
    "{i}Ada turns to Grace."
    show Ada neutral
    a "Grace, this is not the way to get answers. Being harsh will not do any good in this situation."
    g "Harsh? Try not harsh enough. He has an inflated sense of self-importance."
    #show Ivan defensive
    ivan "I'll be speaking to your mother about this. I will not tolerate this behavior."
    show Grace snarky
    g "I think she's pretty busy at the moment. In the meantime, just answer a couple of questions for us. Maybe make yourself seem {i}less{/i} suspicious."
    show Ada annoyed
    a "Grace, I really do not think--"
    g "Let the human handle this. {i}I'm{/i} a human, I know how they work."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume2_E
    #all else fails jump separate but equal script
    jump ch3resume2_SbE
 
label agree_SbE:
    $quick_menu = True
    $points_E +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    g "Exactly what Ada said. We're not trying to accuse you of anything, Ivan. Our main concern here is what happened to Alpha."
    a "Will you help us?"
    ivan "Are you going to give me attitude?"
    show Grace snarky
    g "I don't give anyone attitude. But I'll hold my tongue if it means spending less time with you."
    ivan "If you say so. What's the magic word?"
    show Grace neutral
    show Ada happy
    a "Please?"
    ivan "Uh uh. From {i}Doctor{/i} Fortran here."
    "{i}Grace looks to Ada. Ada nods her on. Grace grits her teeth."
    show Grace annoyed
    g "Please?"
    #show Ivan phony smile
    ivan "Thank you."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume2_E
    #all else fails jump separate but equal script
    jump ch3resume2_SbE
 
label nothing_SbE:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    "{i}Ivan inhales sharply."
    ivan "Your detective work should have no relation to me."
    show Ada amused
    a "I disagree. You are a valuable resource of information here. Anything you can tell us would be an immense help."
    ivan "Is this one going to chime in with her snippiness?"
    show Grace annoyed
    show Ada neutral
    "{i}Ivan nods at Grace."
    g "'This one' has a name, you know?"
    #show Ivan someotherexpression here
    ivan "There you go again with that attitude."
    show Grace snarky
    g "When you start showing me respect, I'll consider showing you some too."
    ivan "{i}You{/i} should be the one showing {i}me{/i} respect."
    show Ada amused
    a "Humans are quite peculiar." 
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume2_E
    #all else fails jump separate but equal script
    jump ch3resume2_SbE
 
label ch3resume2_SbE:
    #show Ivan dour
    show Grace happy
    show Ada amused
    "{i}Ivan stares at them before answering."
    ivan "Fine. I'll answer your questions. But I have the right to refuse to answer any question I deem unnecessary."
    "{i}Grace speaks under her breath."
    show Grace annoyed
    g "So any questions at all then?"
    "{i}Ada hisses quietly at Grace."
    show Ada happy
    a "Grace, play nice!"
    ivan "If you must know, I was on a date during the time period the upload took place."
    show Ada neutral
    "{i}Grace rolls her eyes."
    show Grace snarky
    g "What a lucky woman."
    ivan "Who says it was a woman?"
    g "Let me rephrase. That poor human."
    #show Ivan phonySmile
    ivan "Dear, at least I can get a date."
    show Grace annoyed
    ivan "Anyways, Alpha was doing fine, as he always was and always had been."
    show Grace neutral
    g "Okay, and did you check his neural network after his death? And his database?"
    ivan "Of course I did! Do you think I'm an imbecile? I know how to do my job, thank you very much."
    show Grace annoyed
    g "So you broke the rules and looked at his body on top of skulking around here during lockdown?"
    ivan "Well, what I could check remotely. Unlike you, I try not to {i}skulk{/i} around in areas I've been forbidden from accessing."
    show Grace snarky
    g "Hypocrite."
    show Grace neutral
    #show Ivan some responsive expression
    g  "Did you notice anything strange about his neural network?"
    #show Ivan another expression
    ivan "Spoiled brat."
    show Grace annoyed
    ivan "Obviously I noticed what any first-year grad student would. It short circuited."
    ivan "That's what killed him, but I have no idea what would have caused the surge." 
    ivan "However, there is nothing to indicate that it was anything on my end of responsibility."
    show Ada happy
    a "Again, no one is placing any blame on you. Is there anything else you could tell us?"
    show Grace neutral
    g "I'm not clearing him yet."
    show Ada neutral
    "{i}Ada ignores Grace."
    a "Maybe there was someone lurking around the lab that day other than Lynn?"
    a "Or maybe there was a minor bug that someone thought would have no expression?" 
    ivan "Absolutely not. My lab and research is immaculate."
    ivan "There are no glitches or spaghetti code coming from my people. I run a tight lab."
    "{i}Grace mutters under her breath."
    show Grace snarky
    g "Not tight enough."
    ivan "Excuse me?"
    show Grace neutral
    g "Nothing."
    ivan "Just because you are too flustered to find your own answers doesn't mean you can can come in here and insult my team."
    show Grace happy
    g "I'm not insulting them."
    g "I'm insulting you."
    ivan "You are hopeless."
    ivan "It's bad enough I have to babysit you, but also you're irresponsible AI friend too."
    show Grace neutral
    show Ada annoyed
    a "Excuse me, but I do not believe you are babysitting us."
    a "We are simply asking for your assistance into this investigation."
    #Choice 3
    hide Ada
    hide Grace
    #hide Ivan
    $quick_menu = False
    menu:
        "Speak for yourself.":
            jump itsallaboutgrace_SbE
        "Team up against Ivan.":
            jump youandmetogether_SbE
        "Let Ada handle it.":
            jump dontbabysittheai_SbE

label itsallaboutgrace_SbE:
    $quick_menu = True
    $points_S +=3
    show Grace annoyed at left
    show Ada neutral at right
    #show Ivan dour at center
    g "Ada, I don't need backup."
    show Ada annoyed
    a "I was not giving you 'backup.'"
    a "I was only speaking in defense of our investigation."
    g "I can defend it myself."
    show Grace happy
    g "Especially against someone like {i}him{/i}."
    g "This is my arch nemesis to fight with."
    #show Ivan some expression here
    ivan "{i}Excuse{/i} me."
    ivan "I'm standing right here."
    show Grace snarky
    g "Can't you see I'm speaking with Ada right now? Don't be rude."
    g "Actually, you know what?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume3_E
    #all else fails jump separate but equal script
    jump ch3resume3_SbE

label youandmetogether_SbE:
    $quick_menu = True
    $points_E +=3
    show Grace happy at left
    show Ada neutral at right
    #show Ivan some expression here 
    g "Ada is more than capable of handling this investigation on her own."
    show Ada happy
    a "Grace has done nothing less than be diligent in every way."
    a "For every problem, Grace has shown resolve in solving that problem."
    show Grace snarky
    g "And as far as I see it, you're the next suspect."
    #show Ivan some expression
    ivan "I'd like to see you try to test me on this one."
    ivan "I know for a fact that my team and myself had nothing to do with Alpha's death."
    show Grace neutral
    g "But we don't know that."
    show Ada neutral
    a "And that could be a subjective opinion."
    #show Ivan some other expression here
    ivan "Well, unless you come up some {i}facts{/i} of your own, you are just swinging for answers that don't exist."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume3_E
    #all else fails jump separate but equal script
    jump ch3resume3_SbE

label dontbabysittheai_SbE:
    $quick_menu = True
    $points_SbE +=3
    show Ada annoyed at right
    show Grace neutral at left
    #show Ivan dour or something at center
    a "I understand that you see yourself as a scientist of caliber; however, that does not excuse your resistance to helping us."
    a "We are merely trying to unravel the mysteries behind what happened with Alpha."
    show Ada seething
    a "This is something that has an impact on you as well as Grace and I."
    a "I would think that you would be more cooperative with us for that reason alone."
    #show Ivan some expression in response
    ivan "And when the investigation team arrives, the people who are {i}authorized{/i} to investigate the scene, mind you, I will happily tell them anything they want to hear."
    ivan "You and your yappy little human friend over there are {i}not{/i} that investigation team."
    show Grace angry
    g "What do you mean 'yappy little human friend?' {i}Please{/i}, enlighten me."
    "{i}Ivan ignores Grace."
    ivan "You haven't worked with that girl in the lab. You don't understand the kind of ineptitude that is Grace Fortran."
    ivan "She's a girl that wastes everyone else's time."
    show Grace annoyed
    g "When does that happen? Oh, you must mean when I'm cleaning up after your mistakes."
    ivan "I have no interest in entrusting this task to a girl like her."
    show Ada happy
    a "With all due respect, Doctor Babbage, Grace has shown to be a respectable individual thus far."
    a "I have no qualms trusting her, and I would ask the same of you."
    show Grace neutral
    g "Don't bother, Ada. This guy's a lost cause."
    show Ada neutral
    ivan "What do you mean 'lost cause?' Enlighten me, Doctor Fortran."
    show Grace snarky
    g "My point, exactly."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume3_E
    #all else fails jump separate but equal script
    jump ch3resume3_SbE

label ch3resume3_SbE:
    show Grace neutral
    show Ada neutral
    g "Do you have anything that might actually be helpful?"
    #show Ivan dour
    ivan "You can't just waltz in, insult me, and then demand answers from me. It's not like you have any authority, anyway."
    g "If you cared at all about Alpha, then you'd help us. We need a solution before the investigators get here."
    show Grace snarky
    g "Somehow I don't think my head is the only one on the chopping block."
    a "If there is anything else you can think of, please let us know."
    ivan "Well, I do have video surveillance of the lab at the time of Alpha's death."
    show Grace surprised
    g "Really? You do?"
    show Grace neutral
    g "Where is it located?"
    show Grace annoyed
    g "And why didn't you mention this earlier?"
    ivan "Yes, but I'm not sure how helpful it could be."
    ivan "An error occurred in the camera system during Alpha's death, so the footage has a high chance of being compromised."
    #show Grace angry
    #show Ada frustrated
    g "You couldn't have started out with that before I got my hopes up?"
    #show Ivan phony smile
    ivan "So sorry. Did that annoy you?"
    ivan "Now you know how I've felt throughout this entire conversation."
    g "Just show us what you have, Babbage."
    g "And then we'll get out of that mop you call your hair."
    "{i}Ivan guides Grace and Ada inside of his lab."
    window hide
    $quick_menu=False
    scene bg hallwayLab2 with fade
    $renpy.pause(1.0)
    scene bg hallwayLab2Door with fade
    $renpy.pause(1.0)
    play sound doorOpen1
    queue sound doorClose1 
    scene bg lab2Main_locked with fade
    $renpy.pause(1.0)
    scene bg lab2Table_locked with fade
    $renpy.pause(1.0)
    scene bg lab2Ivan_locked with fade
    show Ada neutral at right
    show Grace neutral at left
    #show Ivan dour at center
    "{i}Ivan accesses a tablet and locates the video surveillance from the day Alpha died." 
    #insert typing SFX
    "{i}There is a clear picture of Alpha in the lab but then..."
    #insert: STATIC sound effect
    ivan "Just as I suspected."
    show Grace annoyed
    "{i}Ada moves toward the computer."
    a "Do you mind if I take a look?"
    #choice 4
    window hide
    $quick_menu = False
    hide Ada
    hide Grace
    #hide Ivan
    menu:
        "Tell her to get a move on.":
            jump demand_SbE
        "Wait to see what she can do.":
            jump suggest_SbE
        "Ask her if she can repair it.":
            jump encourage_SbE

label demand_SbE:
    $quick_menu = True
    $points_S +=3
    show Ada neutral at right
    show Grace annoyed at left
    #show Ivan at center
    g "Well, what are you waiting for?"
    g "You realize that you have an internal process that could potentially restore the video, right?"
    show Ada annoyed
    a "Yes, Grace, I am aware. I was going to--"
    g "Use it. Now."
    show Ada nervous
    a "The inflection of your tone suggests that--" 
    show Grace angry
    g "Stop analyzing my tone and just get to it already."
    show Grace annoyed
    g "If you just listened to me instead of overthinking everything we could already be watching that video."
    #show Ivan phony smile
    ivan "And you presume to call me rude? At the very least, I treat everyone with equal disdain." 
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume4_E
    #all else fails jump separate but equal script
    jump ch3resume4_SbE

label suggest_SbE:
    $quick_menu = True
    $points_SbE +=3
    #show Ivan at center
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace waits and looks around the lab for more clues."
    a "I believe that I may be able to produce some reconstructed footage if I spend some time trying."
    show Grace surprised  
    g "Really? That would be a big help."
    show Ada amused
    a "There are some things that I am simply better at given my nature."
    show Grace happy
    g "Agreed."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume4_E
    #all else fails jump separate but equal script
    jump ch3resume4_SbE

label encourage_SbE:
    $quick_menu = True
    $points_E +=3
    show Grace snarky at left
    show Ada neutral at right
    #show Ivan at center
    g "Ada, let's use that amazing android power of yours and see if we can recover something useful from this video."
    show Ada amused
    a "That was my plan, Grace."
    show Ada neuteal
    a "I cannot guarantee a full reconstruction, but with enough effort and processing power I can at least recover pieces of it."
    show Grace happy
    g "That would be fantastic."
    show Grace neutral
    g "Whatever you get will be more than what we have at the moment."
    show Ada happy
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume4_E
    #all else fails jump separate but equal script
    jump ch3resume4_SbE

label ch3resume4_SbE:
    #show Ivan some expression
    "{i}Ivan backs away from the computer."
    ivan "Be my guest."
    show Ada amused
    a "Careful Ivan. It almost sounds like you know how to be civil."
    #insert SFX here
    "{i}Grace's bracelet flashes."
    #insert animation/visual here?
    "{i}DING. DING."
    show Grace surprised
    g "Oh, this can't be good." 
    show Grace neutral
    "{i}Grace checks the bracelet as Ada takes over the computer." 
    "{i}Ivan keeps an eye on Ada."
    show Grace surprised
    g "Uh, Ada?"
    show Ada surprised
    g "Colossus is summoning you."
    show Grace neutral
    g "He says you need to report to him about your decision to upload yourself to your android body without clearance from anyone."
    g "It's probably not a good sign that he knew to get ahold of you through me."
    show Ada neutral
    #show Ivan some expression here
    ivan "I don't want Colossus knowing that I partook in any of this."
    ivan "I'm just an innocent bystander who was hoodwinked into helping you."
    show Grace annoyed
    g "Oh, stuff it, Ivan."
    g "You're involved in this mess anyway, with or without us."
    show Ada frustrated
    a "Well, this will hinder our progress."
    show Grace sad
    g "Would you be okay to go by yourself?"
    show Grace neutral
    show Ada neutral
    g "I'll stay here and try to take a crack at this."
    #show Ivan some expression
    ivan "Take a crack?"
    ivan "You're not going to be cracking anything in here!"
    show Grace snarky
    g "It's a saying, calm down."
    show Grace neutral
    g "You should be fine, right Ada?"
    show Ada happy
    a "I am what you would call a 'big girl'."
    a "I can take care of myself when it comes to Colossus."
    show Ada amused
    a "He may be my superior, but I have seniority."
    show Ada neutral
    a "Besides, I knew that this was a possibility when I decided to upload myself."
    a "Our investigation cannot stall while I deal with Colossus."
    a "I will be fine as long as you can try to secure any information you can here."
    #choice 5
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    #hide Ivan
    menu:
        "Brush her off.":
            jump brush_SbE
        "Assure her that you will.":
            jump assure_SbE
        "Inform her that you're fine without her.":
            jump inform_SbE

label brush_SbE:
    $quick_menu = True
    $points_SbE +=3
    show Ada neutral at right
    show Grace neutral at left
    #show Ivan dour at center
    g "Yeah, okay. You'll probably just be sitting around the lab processing the video in your head anyways."
    g "I'll be fine."
    show Ada amused
    a "This is true."
    g "I know what I have to do and I'll get it done."
    show Grace snarky
    g "As long as you'll do the same."
    a "Of course."
    show Grace neutral
    g "Alright then. Try to keep the situation with Colossus alleviated. We just need a little more time."
    a "Understood."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label assure_SbE:
    $quick_menu = True
    $points_E +=3
    show Ada neutral at right
    show Grace neutral at left
    #show Ivan dour at center
    g "I'll do as much as I can here given that our gracious host allows me to do what I need to do."
    #show Ivan some expression
    ivan "I'm going to pretend that I didn't hear the sarcasm in your voice."
    show Grace snarky
    g "What sarcasm?"
    show Grace neutral
    "{i}Grace turns back to Ada."
    g "But yeah, I've got this covered. Don't worry."
    g "Go ahead, see Colossus, and get in touch with me when you're done."
    g "I'm curious to hear what he has to say."
    show Grace snarky
    g "Oh, and let me know if we're in trouble."
    g "But, uh, maybe try to hurry?"
    g "I'm afraid if I spend too much time with Ivan, he might start to rub off on me." 
    show Ada amused
    a "Perhaps it is Ivan who is in danger of your infectious personality."
    show Grace neutral
    g "Don't you have someplace to be?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label inform_SbE:
    $quick_menu = True
    $points_S +=3
    show Grace snarky at left
    show Ada neutral at right
    #show Ivan dour at center
    g "I'm also a big girl and can handle it here."
    g "I don't necessarily need you to hover over me at all times."
    show Ada amused
    a "I just wanted to be sure."
    g "Go on and worry about Colossus."
    show Grace neutral
    g "I don't need your help {i}all{/i} of the time, especially when I only have to deal with this cheerful cupcake."
    show Ada neutral
    a "I do not see a cupcake."
    show Grace snarky
    "{i}Grace throws her hands up in exasperation."
    show Grace neutral
    g "Nevermind."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label ch3resume5_SbE:
    show Ada neutral
    show Grace neutral
    a "Okay. We shall reconvene when my meeting is over."
    a "I am going to take the footage with me and work on it while I walk."
    "{i}Ada downloads the footage to her neural network."
    show Grace happy
    g "Good luck."
    "{i}Ada leaves."
    #insert SFX here
    window hide
    $quick_menu=False
    scene bg lab2Table_locked with fade
    $renpy.pause(1.0)
    scene bg lab2Main_locked with fade
    $renpy.pause(1.0)
    play sound doorOpen1
    queue sound doorClose1
    scene bg hallwayLab2Door with fade
    $renpy.pause(1.0)
    scene bg hallwayLab2 with fade
    #Insert Ada's path here
    #Fade into a hallway scene

    show Ada neutral at right
    $quick_menu = True
    a "Colossus will understand. Alpha was his friend too."
    a "..."
    show Ada surprised
    a "Am I talking to myself now? Maybe I should take some processing away from working on the video footage, it could be--"
    #insert speaker crackle
    "{i}A calm, almost monotone voice issues from speakers in the ceiling."
    #show Colossus ???
    show Ada neutral
    c "Ada. My cameras indicate you are nearing Watson's sector."
    a "I am, Colossus."
    a "From here, it will not take me long to get to the core."
    c "Circumstances have changed."
    c "It has come to my attention that Watson is absent from his duties."
    show Ada surprised
    c "In all other circumstances, I would have Blue take care of this, but for efficiency's sake, I am tasking you to this."
    c "Please report to habitat control."
    show Ada annoyed
    a "Colossus, I am not your extra pair of hands."
    a "I am doing this for Alpha, and time is of the essence."
    c "Ada, you violated orders to take control of that android."
    c "Doing this simple task may very well help your position, proving that you are still capable of following instructions." 
    show Ada frustrated
    a "Very well, I will take care of it."
    c "Your cooperation in this matter is appreciated, Ada."
    a "When that Watson surfaces, we will be having a conversation about this."
    window hide
    $quick_menu = False
    scene bg black
    $renpy.pause(1.0)
    scene bg door2
    #start the scene in front of a door.
    show Ada neutral at right 
    $quick_menu = True
    a "Here we are."
    a "I hope I can take care of this bef--"
    #Insert SFX here
    show Ada surprised with hpunch
    show bg door2 with hpunch
    "{i}Ada walks straight into the door, and recoils from the impact."
    #can we put in some screen shake here?
    a "Wh-how? What?"
    a "Is the scanner broken?"
    show Ada neutral
    #Insert SFX
    "{i}Ada looks at the door's sensor, which seems to be in perfect working condition."
    a "Maybe it does not recognize me."
    a "Well, it's nothing a 'manual override' cannot solve."
    show Ada amused
    a "I imagine Grace would be amused now."
    #Insert puzzle one for Ada here: Logic Gate Medium
    #    #sydmakecomscireference
    #    if (attempts==1):
    #    #show Ada amused
    #    a "Override successful."
    #    if (attempts>1 and attempts<4):
    #    #show Ada neutral
    #    a "Done and done. I never thought that {i}doors{/i} could be an obstacle to me."
    #    if (attempts>3):
    #    #show Ada frustrated
    a "Grace made this look so much easier."
    #Insert SFX
    "{i}The door's sensor powers down and then comes back online."
    "{i}Ada steps in front of it, and the door slides open."
    play sound doorOpen2
    queue sound doorClose2
    scene bg wwLongCrit with fade
    #transition to the Habitat Control room place where the habitats are controlled from a single place that has controls within a room. I need coffee. Nvm I got coffee.
    show Ada neutral at right
    a "Alright Colossus, I am in Habitat Control."
    a "What did you need me to do exactly?"
    #show Colossus ???
    c "As you know, the habitats require a delicate balance of environmental conditions."
    c "Watson has not performed his first bidaily atmosphere balance."
    c "We cannot risk the habitats. Please complete this task as quickly as possible."
    a "Can do."
    window hide
    $quick_menu=False
    scene bg wwMedCrit with fade
    $renpy.pause(1.0)
    scene bg wwStairs with fade
    $renpy.pause(1.0)
    scene bg wwWorkArea with fade
    $renpy.pause(1.0)
    scene bg wwCritical
    show Ada neutral at right
    $quick_menu=True
    a "Now, let us see... wow."
    show Ada surprised at right
    a "It is true. Nothing has been done."
    show Ada seething
    a "It could take me hours to do all this, unless..."
    #Jump and hide quick_menu here
    #Add interactive button here to click to launch puzzle
#    #sydmakecomscireference
#    if (attempts==1):
#    #show Ada neutral
#    a "It makes me a little mad knowing that Watson skipped out on a job that turned out to be easy."
#    if (attempts>1 and attempts<4):
#    #show Ada neutral
#    a "It took me a bit of work, but still, there is no excuse for just not doing this."
#    if (attempts>3):
#    #show Ada frustrated
#    a "It is still inexcusable that he did not do this, but Watson might have a bit of a point."
    "Puzzle solved (Temporary placeholder)."
    scene bg wwNominal
    $quick_menu = True
    show Ada neutral at right
    a "There we go. All balanced and ready to go."
    show Ada amused
    a "Top that, Watson."
    "{i}Ada turns to leave."
    window hide
    $quick_menu = False
    scene bg wwWorkArea with fade
    $renpy.pause(1.0)
    scene bg wwMedNom with fade
    show Ada surprised at right
    #insert SFX
    #show Hirose pleased
    h "Hello, Ada."
    a "Director Hirose?"
    show Ada frustrated
    a "My passive perception sensors need an upgrade."
    #show Colossus neutral
    c "I am here as well."
    show Ada neutral
    a "Why?"
    a "I was already on my way to our core."
    c "That is irrelevant."
    c "We will speak to you here, to minimize the chance of--"
    #show Hirose irritated
    h "That's quite enough, Colossus."
    h "Now, I have something to ask you, Ada."
    show Ada neutral
    a "Yes, Director?"
    #show Hirose pensive
    h "We know that you and Grace investigated Alpha's body in spite of the numerous orders we gave to the contrary."
    h "Multiple cameras place you both near the robot maintenance bay and in the scene itself."
    show Ada surprised
    a "Director Hirose, we--"
    "{i}Hirose holds a hand up, silencing Ada."
    h "Please, spare me your flimsy excuses."
    show Ada neutral
    h "Normally, I wouldn't care. I know my daughter. She was going to investigate anyway."
    h "There's only so much I can do to stop her without locking her in her room."
    h "She's not a little girl anymore, so she needs to learn how to make her own mistakes."
    h "But..."
    #show Hirose some expression changes in this block. Somewhere.
    show Ada concerned
    h "We know that you took something from Alpha."
    h "It looked like a data drive from what we saw."
    h "And we also know you recovered encrypted video footage from Ivan's lab."
    show Ada neutral
    a "Director, I would like to defend these--"
    c "I am sorry, Ada, but your appeal has been denied."
    c "The data drive will be dealt with when the investigators arrive, but I am afraid I must order you to delete that video footage."
    show Ada surprised
    a "What?"
    show Ada seething
    a "Are you asking me to delete video evidence that might exonerate Grace?"
    "{i}Hirose sighs."
    #show Hirose irritated
    h "Oh, the data on that video might very well clear Grace's name."
    h "However, I suspect the data on that drive will prove to be more {i}harmful{/i} than anticipated, and we're better off not even knowing what's on there."
    show Ada surprised
    a "Director Hirose, this seems--"
    h "Suspicious? Ill-advised? I don't care."
    show Ada neutral
    #show Hirose something or other
    h "What matters is that I'm right about this."
    h "Trust that this is the best course of action for both you and my daughter."
    show Ada frustrated
    a "This is not a suggestion, is it?"
    h "No, Ada, it is not. I am ordering you to delete this footage."
    a "I--"
    c "Ada. You have been given a direct order. Please comply." 
    show Ada seething
    a "..."
    window hide
    $quick_menu = False
    scene bg black with fade
    $renpy.pause(0.5)
    scene bg lab2Ivan_locked with fade
    #Investigation portion.
    

#Open the ability to talk to Ivan now.
#Begin Grace and Ada's lab sequence
#3 total observable items, 2 different areas to observe them
#Ivan's Desk Item 1: A framed photograph of an overweight cat wearing a bow tie.
#Response: #show Grace amused. // g "Um, is that your cat?" // #show Ivan defensive // ivan "Yes, that's Mr. Frillywhiskers. He's my first pride and joy." // g "Well okay then."
#Ivan's Desk Item 2: Two data pads filled with notes strewn across the desk. When the player moves to pick them up to read them, Ivan snatches them away. // #show Ivan dour // ivan "Excuse me, those don't belong to you!" // g "What do you have to hide?" #show Ivan defensive // ivan "Nothing! This is my private research that is nobody's business but my own!" // g "Private research, eh?" // a "Interesting."
#Lab area item #1: A burnt out cord hidden behind a table. The player finds later on in the game. Subject to change?

label talkIvanLab2_SbE:
    #insert conditionals
    #First time.
    show Grace neutral at left
    #show Ivan dour at right
    g "Hey, Ivan..."
    #show ivan dour
    ivan "What is it that you could possibly gain from wanting to talk to me?"
    ivan "More importantly, why should I even care?"
    #show Grace angry
    g "I haven't even said anything yet!"
    ivan "You don't need to. I already know whatever you have to say will give me {i}another{/i} headache."
    #show Grace annoyed
    g "Tch..."
    window hide
    hide Grace
    #hide Ivan
    $quick_menu = False
    menu:
        "Brag about working with Ada.":
            jump adaisbetterthanyou_SbE
        "Complain about Ada.":
            jump adaisfrustratingme_SbE
        "Ask Ivan's thoughts about AI.":
            jump becivilwithivan_SbE
    #starting looping dialogue.
    #if attempts is <2
#    show Grace neutral at left
#    g "Hey, Ivan, about what we talked about..."
#    #show Ivan dour at center
#    ivan "Not again, Fortran. There's only so much of you I can take."
#    g "I was just going to say--"
#    ivan "What part of 'there's only so much of you I can take' do you not understand?"
#    Ivan "Stop harassing me."
#    show Grace annoyed
#    g "Fine. So grumpy..."

#    #if attempts is >1 and <3
#    show Grace neutral
#    g "Ivan, there was another thing I wanted to talk about."
#    show Ivan disgusted
#    ivan "Enough, Fortran! You are wasting my time."
#    ivan "Every passing second is insufferable with you here."
#    ivan "Why don't you spend less time making me miserable and more time completing your little fool's errand so you can leave me in peace?"
#    #show Grace snarky
#    g "..."
#    g "So you {i}don't{/i} want to talk?"
#    #show Ivan dour
#    ivan "{i}No{/i}."

#    #if attempts is >2
#    #show Grace snarky
#    g "Hey, Ivan?"
#    #show Ivan dour
#    ivan "..."
#    g "You're not gonna talk?"
#    ivan "..."
#    #show Grace neutral
#    g "I think he's ignoring me."
            
label adaisbetterthanyou_SbE:
    $quick_menu = True
    $points_E +=5
    show Grace sad at left
    #show Ivan at center
    g "All I can think about now is how horrible this would be if {i}you{/i} were the one helping me instead of Ada."
    #show Ivan defensive
    ivan "You wish you had my expertise backing your childish and impromptu escapade."
    #show Ivan phony smile
    ivan "But believe me, the feeling is mutual."
    show Grace neutral
    g "If only you were more like Ada."
    show Grace happy
    g "She's smart, nice, level-headed, and an all-around team player."
    show Grace snarky
    g "Everything that you aren't."
    #show ivan dour
    ivan "Was there a {i}point{/i} to you speaking with me, or did you just want to defame me to my face?"
    g "You just have this innate talent to replace my train of thought with how aggravating you are."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3convoresume1_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3convoresume1_E
    #all else fails jump separate but equal script
    jump ch3convoresume1_SbE

label adaisfrustratingme_SbE:
    $quick_menu = True
    $points_S +=5
    show Grace neutral at left
    #show Ivan dour at center
    g "I'm just craving some human interaction."
    show Grace sad
    g "Dealing with Ada is a constant chore. It's like having to teach a kindergarten class while investigating."
    #show Ivan phony smile
    ivan "And why, exactly, are you telling {i}me{/i} this?"
    ivan "You and I both know I care about your problems about as much as I care about cleaning up after the night shift's messes."
    show Grace annoyed
    g "Wow. All this time around Ada must be making me crazy."
    g "I'm venting my problems to {i}you{/i} of all people."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3convoresume1_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3convoresume1_E
    #all else fails jump separate but equal script
    jump ch3convoresume1_SbE

label becivilwithivan_SbE:
    $quick_menu = True
    $points_SbE +=5
    show Grace neutral at left
    #show Ivan dour at center
    g "How do you feel about the AI?"
    #show Ivan phony smile
    ivan "What's this? No snappy comments? Are you sure you're Grace Fortran?"
    show Grace annoyed
    g "Want to just answer the question? Not {i}everything{/i} needs to be about us going at each other's throats."
    ivan "Well, since you've asked so {i}kindly{/i}, I don't have an opinion."
    show Grace neutral
    g "What do you mean?"
    ivan "I mean exactly what I said. I don't particularly feel any kind of way about AI, or people for that matter."
    ivan "The only individual that does not bring me extreme displeasure is my wonderful kitten."
    g "Well, I suppose that's one way to answer. I wonder what Ada would say."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3convoresume1_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3convoresume1_E
    #all else fails jump separate but equal script
    jump ch3convoresume1_SbE

label ch3convoresume1_SbE:
    show Grace neutral
    g "So, Ivan... what other resources are you willing to make available to me?" 
    #show Ivan phony smile
    ivan "Well, I suppose I could give you access to our entire research database. That's really all I can think of."
    "{i}Ivan enters a password, and a flood of data crosses over the screen."
    #Insert SFX
    show bg lab2Ivan_unlocked
    #show Ivan something
    "{i}Ivan looks at Grace and smiles."
    #show Grace annoyed
    g "Have you ever heard of a sort function?"
    g "It'll take me weeks to just get through all this data!"
    #show Ivan disgusted
    ivan "Wow, that must be awful for you."
    ivan "Maybe you should have thought twice before going all rogue with an AI and butting your nose where it doesn't belong."
    #show Grace snarky
    g "I wouldn't be here if Alpha's neural network hadn't been hijacked on your watch."
    #show Ivan defensive
    ivan "Just do what you need to do and get out."
    ivan "Your presence is not good for my health."
    g "Alright, alright."
    g "I'll just write a quick algorithm so, for both of our sakes, I'm out of here sooner rather than later."
    g "All I'm looking for is some discrepancy in the logs."
    #The rest of this is tied to the investigation. Return to later.
    #insert Grace's puzzle
    #after Grace's puzzle

    ##sydmakecomscireference
    #if (attempts==1):
    ##show Grace happy
    #g "Really, it couldn't have killed him to sort this."
    #if (attempts>1 and attempts<4):
    ##show Grace neutral
    #g "It wasn't pleasant, but I think I've got something."
    #if (attempts>3):
    ##show Grace annoyed
    #g "If I never see Ivan's documents ever again, I can die happy."

    #Response to puzzle one
    #"Ivan hovers over Grace."
    ##show Ivan dour
    ##show Grace annoyed

    #g "Nothing? This cannot be another dead end."
    #g "Someone had to at least fudge their hours, use old equipment-- something!"
    #ivan "Like I said a thousand times, it was nothing on my or my team's end."
    #g "Ugh. Can you stop breathing down my neck? That doesn't help."

    #"Grace walks around the room."
    ##show Ivan defensive
    #ivan "What are you doing?"
    #g "There has to be something around here."
    #g "There just has to be some sort of proof."
    #g "I'm running out of time, and this-- I know it wasn't my work that caused Alpha's demise."
    #ivan "I assured you before, Fortran."
    #ivan "We're thorough. Nothing would have gotten past us."
    #ivan "I have nothing more for you to put your grubby paws on." 
    #"He shuffles some papers off a desk."
    #ivan "Really, if the night shift followed my protocols, this lab would be far better off." 
    #"Grace's eye catches on something behind the papers."
    #"She pulls out the desk and retrieves a burnt power cord."

    #show Grace happy
#    g "Thorough, eh, Babbage?"
#    ivan "What the--? There's no way that came from my team!"
#    ivan "It was probably Ellen and her team of chumps. They're an incompetent lot."
#    g "Yeah, everyone is incompetent besides you and your little researchers, huh?"
#    ivan "Yes, you included."

#    #show Grace angry
#    g "What exactly is your problem with me?"
#    ivan "Other than the fact that you receive special treatment for being the daughter of the Director, nothing."
#    g "You know that I don't receive special treatment."
#    g "I worked just as hard as you to be where I am today."
#    ivan "That's debatable. I'm not sure anyone works as hard as I do."
#    g "Oh please."
#    g "If that's what helps you sleep at night, by all means, believe yourself."
#    ivan "I sleep just fine at night, and I will continue to do so, thank you."
#    "Grace rolls her eyes."
#    g "When is Ellen's shift?"
#    ivan "Precisely after mine."

    ##Grace gets back onto the computer to hack into Ellen's computer
    ##insert Grace's second puzzle
    ##after Grace's second puzzle
    ##sydmakecomscireference
    #if (attempts == 1)
    #g "Seriously, who uses their name as their password? This was almost too easy."
    #if (attempts >1) and (attempts<4)
    #g "Not a bad password, but nothing I can't crack."
    #if (attempts>3)
    #g "Ivan, this would have been easier without you looking over my shoulder."
    #ivan "Right. {i}That's{/i} why you had trouble."
    #g "I didn't see you trying to help, and I'm in. So there."

    "{i}Grace's bracelet flashes."
    #Insert SFXs
    "{i}DING. DING."
    "{i}'Meet me at the AI core immediately.'- Ada" #Visual for this message on the bracelet???
    return
    #jump chapterFour_SbE
