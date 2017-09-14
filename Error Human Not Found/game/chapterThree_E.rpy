label chapterThree_E:
    window hide
    $quick_menu = False
    scene bg black with fade
    scene bg chapterThree with fade
    $renpy.pause(3.0)
    scene bg hallwayGrace with fade 
    $quick_menu = True
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    $renpy.music.play("music/Amb/Hallway/EHNF_Amb_Scene_Hallway_Norm.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    "{i}Grace and Ada wander into the hall.{/i}"
    show Grace neutral at left
    show Ada neutral at right
    g "The overseer of the project is Ivan Babbage."
    a "Right. I have worked with him before."
    show Grace snarky
    g "He's quite the character, so this should be fun. Any exchange with Ivan is always interesting."
    show Ada amused
    a "How so?"
    #choice 1
    hide Grace
    window hide
    hide Ada
    $quick_menu = False
    menu:
        "Explain why.":
            jump adadoesntknow_E
        "Tell her that it's none of her business.":
            jump business_E
        "Change the subject.":
            jump fahggetaboutit_E

label adadoesntknow_E:
    show Grace neutral at left
    show Ada neutral at right
    $quick_menu = True
    $points_E +=3
    g "I forget that your only interaction with Ivan is research based, and you haven't engaged with him in an actual conversation."
    show Grace snarky
    g "Well, let's just say that he's not the most chipper person on the Noah Sphere, and he's definitely not my biggest fan."
    show Ada amused
    a "Really? You seem like a pleasant individual, in my opinion. "
    show Grace happy
    g "Thanks, Ada. It's refreshing to hear a compliment from someone other than just Alan."
    show Ada neutral
    a "Alan is the man who constructed this body, correct?"
    g "Yeah. The two of us are good friends. He's probably the friendliest guy on the Noah Sphere."
    a "And people like this 'Ivan' are not so friendly?"
    show Grace annoyed
    g "Definitely not. He's a big grump and has a stick up his--"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume_E
    #all else fails jump separate but equal script
    jump ch3resume_SbE

label business_E:
    $quick_menu = True
    $points_S +=3
    show Grace snarky at left
    show Ada neutral at right
    g "Uh... No offense, but I don't know how much information I'm supposed to divulge about an overseer to an AI. I probably shouldn't say anything."
    a "Yes, I understand, but I am about to meet him anyway. Should I be prepared for any certain mannerisms?"
    g "Well I guess you can just see for yourself."
    show Ada amused
    a "So will this actually be fun? I cannot understand your tone."
    show Grace annoyed
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

label fahggetaboutit_E:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    g "Who knows? Or cares? Anyway, the goal here is to determine what could have possibly happened during the upload and Ivan is the one to--"
    show Ada happy
    a "Well, his research is very conductive. He seems very bright."
    show Grace snarky
    g "Yeah, Ivan is a real treat."
    show Ada neutral
    a "A treat? Like a present? How can a person be a present?"
    show Grace neutral
    g "Sorry, Ada. That must've sounded confusing. I was using sarcasm."
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

label ch3resume_E:
    #Insert footsteps here
    scene bg hallwayBalcony
    "{i}Grace and Ada turn a corner and run into Ivan outside of his lab. He glowers at Grace, and then double takes at Ada.{/i}"
    #show Ivan dour at center
    show Ada surprised at right
    show Grace surprised at left
    ivan "What have you done this time, Fortran? Why is one of the androids walking about?"
    ivan "You know what happened to Alpha, and the entire lab has been put on hiatus because of it."
    ivan "This is an outrage! The entire Conclave will be in an uproar about this."
    show Ada frustrated
    show Grace annoyed
    a "If you are going to accuse anybody of anything, you should accuse me, not Grace."
    show Grace surprised
    g "Ada, you don't have to--"
    show Ada seething
    show Grace neutral
    a "He is insulting your intelligence and integrity. I uploaded myself. Grace here is merely accompanying me while I investigate."
    a "Surely you could understand my concern for my friend as well as my urge to solve his death?"
    #show Ivan dour
    ivan "Well, yes. No offense, Ada, but {i}Doctor Fortran{/i} here should know better than to accompany an AI while the whole Noah Sphere is on lockdown."
    show Ada annoyed
    a "Any blame you place on her can be doubled to me."
    show Grace happy
    g "Ada, thank you."
    show Ada happy
    a "No problem. Thank you for helping me."
    "{i}Ada addresses Ivan.{/i}"
    show Ada neutral
    show Grace neutral
    a "We are looking for justice. Not trouble."
    #show Ivan phony smile
    ivan "That's sweet. But I'm afraid if the Director finds out about this--"
    g "She doesn't have to. Not now, anyway. She has enough on her plate."
    show Grace snarky
    g "This is low on the totem pole on the list of things for her to worry about."
    #show Ivan some expression here
    ivan "We'll see about that. But what exactly is going on here? Get into specifics. Now."
    show Grace neutral
    a "To be short, we want to figure out what happened to Alpha."
    #show Ivan defensive
    ivan "Everybody does. Aren't there external investigators on the case?"
    g "Yes, but we want to get a head start. We have some questions for you, if you don't mind."
    "{i}Ivan crosses his arms.{/i}"
    #Ensure he does NOT have crossed arms before this, change sprite here
    ivan "I'll consider answering them."
    g "First of all, what are you doing here? The labs are supposed to be closed off to everybody. That includes you."
    "{i}Ivan stays silent.{/i}"
    show Grace annoyed
    g "Spit it out."
    ivan "I'm hesitant about leaving my lab alone for such a long amount of time. I don't trust anyone not to break in and contaminate my research."
    show Grace surprised
    g "Even if that means opposing the Conclave's order?"
    #show Ivan expression here
    ivan "If you were a halfway decent researcher, you would do the same."
    show Grace annoyed
    g "Do you want to take this road with me, Ivan? Because last time I checked, {i}you{/i} were--"
    show Ada annoyed
    a "Grace, it is not worth it. Let us move on now. I think that would be for the best."
    "{i}Grace takes a deep breath.{/i}"
    show Grace neutral
    g "Okay. First of all, where exactly were you when Alpha died?"
    #show Ivan defensive
    ivan "How dare you imply me in any of this! Alpha was {i}my{/i} brain child."
    ivan "He was the prime example of what an AI could accomplish in a physical form. I created that."
    #show Ivan disgusted
    ivan "And for you to insinuate that I would have any involvement in his demise is the worst insult you could--"
    show Grace angry
    g "Hey, wait a second. You weren't the only one working on this project."
    show Ada neutral
    a "We are not insinuating anything, Ivan. As the project overseer, you knew the most about Alpha's process. That's why we have come to you."
    show Grace annoyed
    #show Ivan defensive
    a "We do not wish to insult you. We just need to be exhaustive."
    #choice 2
    hide Grace
    hide Ada
    #hide Ivan
    window hide
    $quick_menu = False
    menu:
        "Disagree with her.":
            jump trymeada_E
        "Agree with her.":
            jump fineiagree_E
        "Remain indifferent.":
            jump blahoksure_E

label trymeada_E:
    $quick_menu = True
    $points_S +=3
    #show Ivan dour at center
    show Grace annoyed at left
    show Ada neutral at right
    g "But he's being absurd! Everything coming out of his mouth is preposterous! He is Alpha's overseer, of course he has some responsibility here."
    #show Ivan dour
    ivan "I refuse to acknowledge any of these accusations."
    show Ada concerned
    a "I do not think she means--"
    g "I know exactly what I mean."
    show Ada annoyed
    "{i}Ada turns to Grace.{/i}"
    a "Grace, this is not the way to get answers. Being harsh will not do any good in this situation."
    show Grace angry
    g "Harsh? Try not harsh enough. He has an inflated sense of self-importance."
    #show Ivan defensive
    ivan "I'll be speaking to your mother about this. I will not tolerate this behavior."
    show Grace snarky
    g "I think she's pretty busy at the moment. In the meantime, just answer a couple of questions for us. Maybe make yourself seem {i}less{/i} suspicious."
    show Ada seething
    a "Grace, I really do not think--"
    show Grace neutral
    g "Ada, I've got this."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume2_E
    #all else fails jump separate but equal script
    jump ch3resume2_SbE

label fineiagree_E:
    $quick_menu = True
    $points_E +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    g "Exactly what Ada said. We're not trying to accuse you of anything, Ivan. Our main concern here is what happened to Alpha."
    #show Ada neutral
    show Ada happy
    a "Will you help us?"
    #show Ivan comething
    ivan "Are you going to give me attitude?"
    show Grace snarky
    g "I don't give anyone {i}attitude{/i}. But I'll hold my tongue if it means spending less time with you."
    ivan "If you say so. What's the magic word?"
    a "Please?"
    ivan "Uh uh. From {i}Doctor{/i} Fortran here."
    show Grace annoyed
    g "You keep saying that."
    ivan "That isn't the magic word."
    "{i}Grace looks to Ada. Ada nods at her. Grace grits her teeth.{/i}"
    show Grace happy
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

label blahoksure_E:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    "{i}Ivan inhales sharply.{/i}"
    ivan "Your detective work should have no relation to me."
    show Ada happy
    a "I disagree. You are a valuable resource of information here. Anything you can tell us would be an immense help."
    g "Ada's right, Ivan. Anything you can tell us could be useful."
    ivan "What's this? No snappy remark?"
    show Grace snarky
    g "Not if you don't give me a reason for one. Oh wait, are you talking? Then there's reason."
    ivan "There you go again with that attitude."
    g "What can I say? You bring out my charm."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume2_E
    #all else fails jump separate but equal script
    jump ch3resume2_SbE

label ch3resume2_E:
    show Grace happy
    show Ada amused
    #show Ivan dour
    "{i}Ivan glares at them before answering.{/i}"
    ivan "Fine. I'll answer your questions. But I have the right to refuse to answer any question I deem unnecessary."
    "{i}Grace speaks under her breath.{/i}"
    g "So any questions at all then?"
    show Ada amused
    a "Ha, ha, ha."
    show Grace happy
    g "That laugh was better!"
    a "Thank you. I tried to insert more gusto, as you said."
    "{i}Ivan glares at them.{/i}"
    show Ada neutral
    show Grace neutral
    ivan "It warms my heart to see that Grace here has found her humor counterpart in an AI. {i}Not{/i}."
    ivan "Are you done with your buffoonery?"
    show Grace snarky
    g "The only buffoon here is you. So, answer the question. Where were you?"
    #show Ivan defensive
    ivan "If you must know, I was on a date during the time period the upload took place."
    "{i}Grace rolls her eyes.{/i}"
    g "What a lucky woman."
    ivan "Who says it was a woman?"
    g "Let me rephrase. That poor soul. Do they have brain damage? I can only assume so."
    ivan "Dear, at least I can get a date."
    show Ada concerned
    a "Is a date important? If I recall correctly, Lynn seemed to know of someone also in need of a date."
    show Grace surprised
    "{i}An awkward moment passes.{/i}"
    show Grace neutral
    g "No, Ada, I'm fine. I don't need a date, {i}especially{/i} with Lynn's son."
    show Ada neutral
    a "I do not understand."
    g "And that's okay. You really don't have to."
    ivan "Anyways, Alpha was doing fine, as he always was, and always had been."
    g "Okay, and did you check his neural network after his death? And his database?"
    ivan "Of course I did! Do you think I'm an imbecile? I know how to do my job, thank you very much."
    a "There is no need to snap."
    show Grace annoyed
    g "You broke the Conclave's rules more than you already have and looked at his body?"
    ivan "Well, what I could check remotely. Unlike you, I try not to {i}skulk{/i} around in areas I've been forbidden from accessing."
    show Grace snarky
    g "Hypocrite."
    show Grace neutral
    g "Did you notice anything strange about his neural network?"
    #show Ivan phony smile
    ivan "Spoiled brat."
    show Grace neutral
    #show Ivan dour
    ivan "Obviously I noticed what any first-year grad student would. It short circuited."
    ivan "That's what killed him, but I have no idea what would have caused the surge."
    #show Ivan defensive
    ivan "However, there is nothing to indicate that it was anything on my end."
    a "Again, no one is placing any blame on you. Is there anything else you could tell us?"
    show Grace snarky
    g "I'm not clearing him yet."
    "{i}Ada ignores Grace.{/i}"
    a "Maybe there was someone lurking around the lab that day other than Lynn?"
    a "Or maybe there was a minor bug that someone thought would have no expression?"
    #show Ivan disgusted
    ivan "Absolutely not. My lab and research is immaculate."
    #show Ivan defensive
    ivan "There are no glitches or spaghetti code coming from my people. I run a tight lab."
    "{i}Grace mutters under her breath.{/i}"
    show Grace snarky
    g "Not tight enough."
    ivan "Excuse me?"
    show Grace neutral
    g "Nothing."
    ivan "Just because you are too flustered to find your own answers doesn't mean you can can come in here and insult my team."
    g "I'm not insulting them."
    show Grace happy
    g "I'm insulting you."
    ivan "You are hopeless."
    ivan "It's bad enough I have to babysit you, but also you're irresponsible AI friend too."
    show Ada annoyed
    a "Excuse me, but I do not believe you are babysitting us."
    show Ada neutral
    a "We are simply asking for your assistance into this investigation."
    #choice 3
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    #hide Ivan
    menu:
        "Speak for yourself.":
            jump itsallaboutgrace_E
        "Team up against Ivan.":
            jump youandmetogether_E
        "Let Ada handle it.":
            jump dontbabysittheai_E

label itsallaboutgrace_E:
    $quick_menu = True
    $points_S +=3
    show Grace annoyed at left
    show Ada neutral at right
    #show Ivan dour at center
    g "Ada, I don't need backup."
    a "I was merely trying to assist you, Grace."
    show Ada annoyed
    a "We are a team, and both of us are responsible for defending our investigation."
    show Grace neutral
    g "That's nice and all, but I can defend it myself."
    show Grace annoyed
    g "Especially against someone like {i}him{/i}."
    show Grace snarky
    g "This is my arch nemesis to fight with."
    show Ada neutral
    a "If you say so."
    ivan "{i}Excuse{/i} me."
    #show Ivan some expression
    ivan "I'm standing right here."
    show Grace neutral
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

label youandmetogether_E:
    $quick_menu = True
    $points_E +=3
    show Grace snarky at left
    show Ada happy at right
    #show Ivan dour at center
    g "Ada is more than capable of handling this investigation on her own."
    a "And Grace has done nothing less than be diligent in every way."
    a "For every problem, Grace has shown resolve in solving that problem."
    g "With the two of us working together, we will definitely solve this mystery before the investigators even get here."
    g "Because of our combined effort, we found that you're the next suspect."
    show Grace happy
    g "Nice, Ada! We were so in synch right there."
    show Ada amused
    a "Yes, that was impressive."
    ivan "How {i}adorable{/i}. The child and her AI friend are working together."
    #show Ivan some expression
    ivan "When you're both done celebrating the joys of friendship or whatever, can we get back to the fact that you're both assaulting my integrity as a scientist?"
    ivan "I know for a fact that my team and myself had nothing to do with Alpha's death."
    show Grace neutral
    g "But we don't know that."
    show Ada neutral
    a "And that could be a subjective opinion."
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

label dontbabysittheai_E:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada annoyed at right
    #show Ivan dour at center
    a "I understand that you see yourself as a scientist of caliber; however, that does not excuse your resistance to helping us."
    a "We are merely trying to unravel the mysteries behind what happened with Alpha."
    show Ada seething
    a "This is something that has an impact on you as well as Grace and I."
    a "I would think that you would be more cooperative with us for that reason alone."
    #show Ivan someexpression
    show Ada neutral
    ivan "And when the investigation team arrives, the people who are {i}authorized{/i} to investigate the scene, mind you, I will happily tell them anything they want to hear."
    ivan "You and your yappy little human friend over there are {i}not{/i} that investigation team."
    show Grace angry
    g "What do you mean 'yappy little human friend?' {i}Please{/i}, enlighten me."
    "{i}Ivan ignores Grace.{/i}"
    ivan "You haven't worked with that girl in the lab. You don't understand the kind of ineptitude that is Grace Fortran. She's a girl that wastes everyone else's time."
    show Grace snarky
    g "When does that happen? Oh, you must mean when I'm cleaning up after your mistakes."
    ivan "I have no interest in entrusting this task to a girl like her."
    show Ada annoyed
    a "With all due respect, Doctor Babbage, Grace has shown to be a kind and respectable ally. I would appreciate it if you not belittle her talents in front of me."
    show Ada happy
    a "Additionally, I am proud to be working alongside her, and I would ask the same of you."
    show Grace annoyed
    g "Don't bother, Ada. This guy's a lost cause."
    show Ada neutral
    #show Ivan some expression
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

label ch3resume3_E:
    show Grace neutral
    show Ada neutral
    g "Do you have anything that might actually be helpful?"
    #show Ivan dour
    ivan "You can't just waltz in, insult me, and then demand answers from me. It's not like you have any authority, anyway."
    g "If you cared at all about Alpha, then you'd help us. We need a solution before the investigators get here."
    show Grace annoyed
    g "We seem to be the only ones who care and time is ticking."
    show Ada seething
    a "If there is anything else you can think of, please let us know."
    ivan "Well, I do have video surveillance of the lab at the time of Alpha's death."
    show Grace surprised
    g "Great news!"
    show Ada surprised
    show Grace happy
    "{i}Grace takes Ada's hand, holds it in the air, and high fives it.{/i}"
    g "That's a high five, Ada. It expresses excitement."
    show Ada happy
    a "What a strange sensation."
    show Grace snarky
    show Ada neutral
    g "Anyway, that footage would be extremely helpful. Where is it located?"
    show Grace annoyed
    g "And why didn't you mention this earlier?"
    ivan "I'm not sure how helpful it could be."
    show Grace neutral
    ivan "An error occurred in the camera system during Alpha's death, so the footage has a high chance of being compromised."
    show Grace angry
    show Ada frustrated
    g "You couldn't have started out with that before I got my hopes up?"
    #show Ivan phony smile
    ivan "So sorry. Did that annoy you?"
    ivan "Now you know how I've felt throughout this entire conversation."
    show Grace neutral
    g "Just show us what you have, Babbage."
    g "Then we'll get out of that mop you call your hair."
    "{i}Ivan guides Grace and Ada inside of his lab.{/i}"
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
    stop channel00 fadeout 1.0
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L8.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L9.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L10.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L11.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    "{i}Ivan accesses a tablet and locates the video surveillance from the day Alpha died.{/i}"
    #insert typing SFX
    "There is a clear picture of Alpha in the lab but then..."
    #insert: STATIC sound effect
    ivan "Just as I suspected."
    show Grace annoyed
    "{i}Ada moves toward the computer.{/i}"
    a "Do you mind if I take a look?"
    #choice 4
    hide Grace
    hide Ada
    $quick_menu=False
    #hide Ivan
    window hide
    menu:
        "Tell her to get a move on.":
            jump hurryitupada_E
        "Wait to see what she can do.":
            jump whatcanyoudo_E
        "Ask her if she can repair it.":
            jump yougotthisada_E

label hurryitupada_E:
    $quick_menu = True
    $points_S +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    g "Ada? Time is ticking."
    show Grace snarky
    g "You realize that you have an internal process that could potentially restore the video, right?"
    show Ada annoyed
    a "Yes, Grace, I am aware. I was going to--"
    g "Can you use it now? We're in a hurry here."
    show Ada nervous
    a "The inflection of your tone suggests that--"
    show Grace annoyed
    g "Please don't analyze my tone right now."
    show Grace neutral
    g "Can you please analyze that video? We could be watching it right now instead of wasting time by talking."
    show Ada frustrated
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

label whatcanyoudo_E:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    "{i}Grace waits, looking around the lab for more clues.{/i}"
    show Ada seething
    a "I believe that I may be able to produce some reconstructed footage if I spend some time trying."
    show Grace surprised  
    g "Really? That would be great. Let me know if I can help in any way."
    show Ada amused
    a "I should be fine. We both have our own skills, after all."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume4_E
    #all else fails jump separate but equal script
    jump ch3resume4_SbE

label yougotthisada_E:
    $quick_menu = True
    $points_E +=3
    show Grace snarky at left
    show Ada neutral at right
#    show Ivan dour at center
    g "Ada, let's use that amazing android power of yours and see if we can recover something useful from this video!"
    show Ada amused
    a "That was my plan, Grace."
    a "It may take some time and processing power, but your infectious enthusiasm is encouraging. I will reconstruct it as fast as I can."
    show Grace happy
    g "What are friends for?"
    g "Whatever you get will definitely be more helpful than what we have now.."
    show Ada happy
    g "Maybe we can finally make some progress!"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume4_E
    #all else fails jump separate but equal script
    jump ch3resume4_SbE

label ch3resume4_E:
    show Grace neutral
    show Ada neutral
    #show Ivan dour 
    "{i}Ivan backs away from the computer.{/i}"
    ivan "Be my guest."
    a "Careful Ivan. It almost sounds like you know how to be civil."
    #insert SFX here
    "{i}Grace's bracelet flashes.{/i}"
    #insert animation/visual here?
    "{i}DING. DING.{/i}"
    show Grace surprised
    g "Oh, this can't be good."
    show Grace neutral
    "{i}Grace checks the bracelet as Ada takes over the computer.{/i}"
    "{i}Ivan keeps an eye on Ada.{/i}"
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
    show Grace neutral
    g "Do you want me to come with you?"
    show Ada neutral
    a "I fear that might further negatively affect our time. Thank you for the offer."
    g "Are you sure?"
    a "Yes, your time would be better spent here."
    show Grace snarky
    g "You're right. I'll try to take a crack at this while you're away."
    ivan "Take a crack?"
    ivan "You're not going to be cracking anything in here!"
    show Grace neutral
    g "It's a saying, calm down. Are you okay with that, Ada?"
    show Ada happy
    a "I am what you would call a 'big girl'."
    a "I can take care of myself when it comes to Colossus."
    show Ada amused
    a "He may be my superior, but I have seniority."
    show Ada neutral
    a "Besides, I knew that this was a possibility when I decided to upload myself."
    show Grace happy
    g "I know. I just wanted to check. This is your first time by yourself with your new body."
    a "I have a better handle on it now. I think. We will find out."
    show Grace neutral
    a "Our investigation cannot stall while I deal with Colossus."
    show Ada neutral
    a "I will be fine as long as you can try to secure any information you can here."
    #choice 5
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    #hide Ivan
    menu:
        "Brush her off.":
            jump gracedoesntcare_E
        "Assure her that you will.":
            jump youcantrustme_E
        "Inform her that you're fine solo.":
            jump weregoodbye_E

label gracedoesntcare_E:
    show Grace neutral at left
    show Ada neutral at right
    $quick_menu = True
    $points_S +=3
    #show Ivan dour at center
    g "Yeah, okay. You'll probably just be sitting around the lab processing the video in your head anyways."
    g "I'll be fine."
    a "This is true."
    g "I know what I have to do and I'll get it done."
    g "I'm confident that you'll do the same."
    a "Of course. I appreciate your trust."
    g "Naturally. Just try to keep the situation with Colossus alleviated. We just need a little more time."
    a "Got it."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label youcantrustme_E:
    $quick_menu = True
    $points_E +=3
    show Grace snarky at left
    show Ada neutral at right
    #show Ivan dour at center
    g "I'll do as much as I can here given that our gracious host allows me to do what I need to do."
    #show Ivan some expression
    ivan "I'm going to pretend that I didn't hear the sarcasm in your voice."
    show Grace happy
    g "What sarcasm?"
    "{i}Grace turns back to Ada.{/i}"
    show Grace neutral
    g "But yeah, I've got this covered. Don't worry."
    g "Go ahead, see Colossus, and get in touch with me when you're done."
    g "I'm curious to hear what he has to say."
    show Grace snarky
    g "Oh, and let me know if we're in trouble."
    g "But, uh, maybe try to hurry?"
    g "I'm afraid if I spend too much time with Ivan, he might start to rub off on me."
    show Ada amused
    a "Perhaps it is Ivan who is in danger of your infectious personality."
    show Grace happy
    g "Wow, Ivan. Look at that. Kindness and appreciation... Maybe you could learn from the AIs."
    #show Ivan some expression
    ivan "Ada, don't you have somewhere to be?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label weregoodbye_E:
    $quick_menu = True
    $points_SbE +=3
    show Grace snarky at left
    show Ada neutral at right
    #show Ivan dour at center
    g "I'm also a big girl and can handle it here."
    g "I don't really need your assistance at the moment."
    a "I just wanted to be sure."
    show Grace neutral
    g "Go on and worry about Colossus."
    show Grace snarky
    g "I'll be just fine, especially when I only have to deal with this cheerful cupcake."
    a "I do not see a cupcake."
    "{i}Grace throws her hands up in exasperation.{/i}"
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

label ch3resume5_E:
    show Ada neutral
    show Grace neutral
    a "Okay. We shall reconvene when my meeting is over."
    a "I am going to take the footage with me and work on it while I walk."
    "{i}Ada downloads the footage to her neural network.{/i}"
    show Grace happy
    g "Good luck."
    "{i}Ada leaves.{/i}"
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
    #Fade into a hallway scenestop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    $renpy.music.play("music/Amb/Hallway/EHNF_Amb_Scene_Hallway_Norm.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    show Ada neutral at right
    $quick_menu = True
    a "Colossus will understand. Alpha was his friend too."
    a "..."
    show Ada surprised
    a "Am I talking to myself now? Maybe I should take some processing away from working on the video footage, it could be--"
    #insert speaker crackle
    "{i}A calm, almost monotone voice issues from speakers in the ceiling.{/i}"
    #show Colossus ???
    show Ada neutral
    c "Ada. My cameras indicate you are nearing Watson's sector."
    a "I am, Colossus."
    a "From here, it should not take me too long to get to the core."
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
    #start the scene in front of a door.
    #show Ada neutralwindow hide
    $quick_menu = False
    scene bg black with fade
    $renpy.pause(1.0)
    scene bg door2 with fade
    #start the scene in front of a door.
    show Ada neutral at right 
    $quick_menu = True
    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
    play channel01 wwAmb1 fadeout 1.0 fadein 1.0
    play channel02 wwAmb2 fadeout 1.0 fadein 1.0
    play channel03 wwAmb3 fadeout 1.0 fadein 1.0
    play channel04 wwAmb4 fadeout 1.0 fadein 1.0
    play channel05 wwAmb5 fadeout 1.0 fadein 1.0
    play channel06 wwAmb6 fadeout 1.0 fadein 1.0
    a "Here we are."
    a "I hope I can take care of this bef--"
    #Insert SFX here
    show Ada surprised with hpunch
    show bg door2 with hpunch
    "{i}Ada walks straight into the door, and recoils from the impact.{/i}"
    #can we put in some screen shake here?
    a "Wh-how? What?"
    a "Is the scanner broken?"
    show Ada neutral
    #insert SFX here
    "{i}Ada looks at the door's sensor, which seems to be in perfect working condition.{/i}"
    a "Maybe it does not recognize me."
    a "Well, it is nothing a 'manual override' cannot solve."
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
    "{i}The door's sensor powers down and then comes back online.{/i}"
    "{i}Ada steps in front of it, and the door slides open.{/i}"
    play sound doorOpen2
    queue sound doorClose2
    scene bg wwLongCrit with fade
    show Ada neutral at right
    a "All right Colossus, I am in Habitat Control."
    a "What did you need me to do exactly?"
    #show Colossus???
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
    scene bg wwCritical with fade
    show Ada neutral at right
    $quick_menu=True
    a "Now, let us see... wow."
    show Ada surprised
    a "It is true. Nothing has been done."
    show Ada annoyed
    a "It could take me hours to do all this, unless..."
    $quick_menu = False
    $resume = "E"
    jump binaryMed

label postBinaryMed_E:
    show Ada neutral at right
    a "There we go. All balanced and ready to go."
    show Ada amused
    a "Top that, Watson."
    "{i}Ada turns to leave.{/i}"
    window hide
    $quick_menu = False
    scene bg wwWorkArea with fade
    $renpy.pause(1.0)
    scene bg wwMedNom with fade
    show Ada surprised at right
    $quick_menu = True
    #insert SFX
#    show Hirose pleased
    h "Hello, Ada."
    a "Director Hirose?"
    show Ada annoyed
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
    "{i}Hirose holds a hand up, silencing Ada.{/i}"
    h "Please, spare me your flimsy excuses."
    show Ada neutral
    h "Normally, I wouldn't care. I know my daughter. She was going to investigate anyway."
    h "There's only so much I can do to stop her without locking her in her room."
    h "She's not a little girl anymore, so she needs to learn how to make her own mistakes."
    h "But..."
    #show Hirose some changes in that block
    show Ada concerned
    h "We know that you took something from Alpha."
    h "It looked like a data drive from what we saw."
    h "We also know you recovered encrypted video footage from Ivan's lab."
    show Ada neutral
    a "Director, I would like to defend these--"
    c "I am sorry, Ada, but your appeal has been denied."
    c "The data drive will be dealt with when the investigators arrive, but I am afraid I must order you to delete that video footage."
    show Ada surprised
    a "What?"
    show Ada seething
    a "Are you asking me to delete video evidence that might exonerate Grace?"
    "{i}Hirose sighs.{/i}"
    
    #show Hirose irritated
    h "Oh, the data on that video might very well clear Grace's name."
    h "However, I suspect the data on that drive will prove to be more {i}harmful{/i} than anticipated, and we're better off not even knowing what's on there."
    show Ada surprised
    a "Director Hirose, this seems--"
    h "Suspicious? Ill-advised? I don't care."
    show Ada neutral
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
    $resume = "E"
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    jump lab2_inv
    #Investigation portion.

label talkIvanLab2_E:
    $talkIvan_count +=1
    show Grace neutral at left
    #show Ivan dour at center
    g "Hey, Ivan..."
    #show ivan dour
    ivan "What is it that you could possibly gain from wanting to talk to me?"
    ivan "More importantly, why should I even care?"
    show Grace angry
    g "I haven't even said anything yet!"
    ivan "You don't need to. I already know whatever you have to say will give me {i}another{/i} headache."
    show Grace annoyed
    g "Tch..."
    window hide
    hide Grace
    #hide Ivan
    $quick_menu = False
    menu:
        "Brag about working with Ada.":
            jump adaisbetterthanyou_E
        "Complain about Ada.":
            jump adaisfrustratingme_E
        "Ask Ivan's thoughts about AIs.":
            jump becivilwithivan_E

label adaisbetterthanyou_E:
    $quick_menu = True
    $points_E +=5
    show Grace sad at left
    #show Ivan at right
    g "All I can think about now is how horrible this would be if {i}you{/i} were the one helping me instead of Ada."
    #show Ivan defensive
    ivan "You wish you had my expertise backing your childish and impromptu escapade."
    #show Ivan phony smile
    ivan "But believe me, the feeling is mutual."
    show Grace neutral
    g "If only you were more like Ada."
    show Grace happy
    g "There aren't many people here that I'd call a friend, but she's definitely one of them."
    g "She's smart, nice, level-headed, and an all-around team player. She's a person of true quality."
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

label adaisfrustratingme_E:
    $quick_menu = True
    $points_S +=5
    show Grace neutral at left
    #show Ivan dour at right
    g "I'm just craving some human interaction."
    show Grace sad
    g "Dealing with Ada is... I hate to say it, but difficult."
    g "I get that she's trying, but it's becoming more and more clear how {i}not{/i} human she is."
    #show Ivan phony smile
    ivan "And why, exactly, are you telling {i}me{/i} this?"
    ivan "You and I both know I care about your problems about as much as I care about cleaning up after the night shift's messes."
    show Grace annoyed
    g "Maybe all this time around Ada really is making me crazy."
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

label becivilwithivan_E:
    $quick_menu = True
    $points_SbE +=5
    show Grace neutral at left
    #show Ivan dour at right
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
    show Grace snarky
    g "I'm pretty sure spending time with Ada has been a lot more engaging than if I were spending time with Ivan's cat."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3convoresume1_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3convoresume1_E
    #all else fails jump separate but equal script
    jump ch3convoresume1_SbE

label ch3convoresume1_E:
    show Grace neutral
    g "So, Ivan, what other resources are you willing to make available to me?" 
    #show Ivan phony smile
    ivan "So it seems you and Ada have grown close in the few hours you've spent together."
    show Grace annoyed
    g "What amazing deductive skills you have. You're such a bright researcher. Not that it's any of your business."
    ivan "You're one to talk after shoving your snout all up in my business."
    show Grace snarky
    g "For investigative purposes. You're just being nosey."
    show Grace annoyed
    g "You can keep your slimy, oily nose pointed away from me, thank you very much."
    #show Ivan something
    ivan "I'm simply making an observation. It's strange to see such closeness between a human and AI."
    show Grace neutral
    g "It's not that irregular. Creators have relationships with their AI."
    #show Ivan something
    ivan "Yet {i}you{/i} are not a creator."
    g "Ada and I are bonded by a common desire. Plus, she was made to be likeable. So what if I happen to enjoy her company?"
    ivan "Have I ever mentioned how strange you are?"
    show Grace snarky
    g "Have I ever mentioned how ugly you are? Let's get back on task here."
    show Grace neutral
    g "What other resources are you willing to make available to me?" 
    #show Ivan phony smile
    ivan "Well, I suppose I could give you access to our entire research database. That's really all I can think of."
    "{i}Ivan enters a password, and a flood of data crosses over the screen.{/i}"
    #Insert SFX
    show bg lab2Ivan_unlocked
    $ivanComp_lock = False
    "{i}Ivan looks at Grace and smiles.{/i}"
    show Grace surprised
    g "Have you ever heard of a sort function?"
    g "It'll take me weeks to just get through all this data!"
    #show Ivan disgusted
    ivan "Wow, that must be awful for you."
    show Grace annoyed
    ivan "Maybe you should have thought twice before going all rogue with an AI and butting your nose where it doesn't belong."
    show Grace snarky
    g "I wouldn't be here if Alpha's neural network hadn't been hijacked on your watch."
    #show Ivan defensive
    ivan "Just do what you need to do and get out."
    ivan "Your presence is not good for my health."
    show Grace neutral
    g "All right, all right."
    g "I'll just write a quick algorithm so, for both of our sakes, I'm out of here sooner rather than later."
    g "All I'm looking for is some discrepancy in the logs."
    $resume = "E"
    jump choose_llMed

label finishGPuzzle1_E:
    "{i}Ivan hovers over Grace.{/i}"
    #show Ivan dour at right
    show Grace annoyed at left
    g "Nothing? This cannot be another dead end."
    g "Someone had to at least fudge their hours, use old equipment-- something!"
    ivan "Like I said a thousand times, it was nothing on my or my team's end."
    g "Ugh. Can you stop breathing down my neck? That doesn't help."
    if(lab2Items<2):
        ivan "Finish your snooping and then you can go bother someone else."
        g "Fine. I will."
        ivan "Talk to me when you are finished. I don't trust that you'll leave without disturbing more of my lab when you're done."
        show Grace annoyed
        g "Jeez, paranoid much?"
        ivan "My lab, my rules."
        jump lab2_inv
    else:
        jump finishLab2Inv_E
        
label finishLab2Inv_E:
    $resume = "E"
    show Grace annoyed at left
    g "There's gotta be something around here."
    g "There just has to be some sort of proof."
    show Grace neutral
    "{i}Grace walks around the room.{/i}"
    #play SFX here
    show bg lab2Table_locked
    #show Ivan defensive
    ivan "What are you doing?"
    show Grace annoyed
    g "I'm running out of time, and this-- I know it wasn't my work that caused Alpha's demise."
    ivan "I assured you before, Fortran. We're thorough. Nothing would have gotten past us."
    ivan "I have nothing more for you to put your grubby paws on."
    "{i}He shuffles some tablets off a desk.{/i}"
    #Insert SFX
    show bg lab2_cord
    ivan "Really, if the night shift followed my protocols, this lab would be far better off."
    show Grace surprised
    "{i}Grace's eye catches on something behind the papers.{/i}"
    jump lab2Table
        
label endCh3_E:
    "{i}Grace's bracelet flashes.{/i}"
    #Insert SFX
    "{i}DING. DING.{/i}"
    "{i}'Meet me at the AI core stat.'- Ada{/i}"
    jump chapterFour_E
