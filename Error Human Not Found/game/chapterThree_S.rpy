label chapterThree_S:
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
    a "I know who he is, Grace."
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
            jump biggrump_S
        "Tell her that it's none of her business.":
            jump mindya_S
        "Change the subject.":
            jump ivanisatreat_S

label biggrump_S:
    show Grace neutral at left
    show Ada neutral at right
    $quick_menu = True
    $points_E +=3
    g "I forget that your only interaction with him is research based and you haven't engaged with him in an actual conversation."
    show Grace snarky
    g "Well, let's just say that he's not the most chipper person on the Noah Sphere, and he's definitely not my biggest fan."
    show Ada amused
    a "I wonder what you could have done to draw his ire."
    show Grace neutral
    g "Who said I did anything to him? He just has this weird aggression toward me. It's almost like he's jealous or something."
    show Ada annoyed
    a "Jealous? I struggle to think of something he can be jealous of."
    show Grace neutral
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

label mindya_S:
    $quick_menu = True
    $points_S +=3
    show Grace snarky at left
    show Ada neutral at right
    g "I don't know how much information I'm supposed to divulge about an overseer to an AI."
    g "I'm not entirely comfortable discussing him with you."
    show Ada frustrated
    a "Grace, this is not the time for secrecy. I should know."
    show Grace neutral
    g "Well I guess you can just see for yourself."
    show Ada seething
    a "I find your refusal to tell me vital information to be frustrating. Grace, I--"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume_E
    #all else fails jump separate but equal script
    jump ch3resume_SbE

label ivanisatreat_S:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    g "Who knows? Or cares?"
    g "Anyway, the goal here is to determine what could have possibly happened during the upload and Ivan is the one to--"
    show Ada amused
    a "Well, his research is very conductive. He seems like a talented professional."
    show Grace snarky
    g "Yeah, Ivan is a real treat. Anyway--" 
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume_E
    #all else fails jump separate but equal script
    jump ch3resume_SbE

label ch3resume_S:
    #Insert footsteps here
    scene bg hallwayBalcony
    "{i}Grace and Ada turn a corner and run into Ivan outside of his lab. He glowers at Grace, and then double takes at Ada.{/i}"
    #show Ivan dour at center
    show Ada surprised at right
    show Grace surprised at left
    ivan "What have you done this time, Fortran? Why is one of the androids walking about?"
    ivan "You know what happened to Alpha, and the entire lab has been put on hiatus because of it."
    ivan "This is an outrage! The entire Conclave will be in an uproar about this."
    show Ada amused
    show Grace angry
    g "Listen, Babbage, this wasn't my doing. Ada uploaded herself without any consent from me or anyone else. I didn't ask her to--"
    show Ada frustrated
    a "Excuse me, Grace, I can speak for myself."
    "{i}Grace ignores her.{/i}"
    show Grace neutral
    g "I'm not held responsible for Ada's actions."
    #show Ivan something or other
    ivan "If the Director finds out about this--"
    g "She doesn't have to. Not now, anyway. She has enough on her plate."
    show Grace snarky
    g "This is low on the totem pole on the list of things for her to worry about."
    #show Ivan something
    ivan "We'll see about that. But what's going on? Why are you two together?"
    show Ada neutral
    a "We are investigating what happened to Alpha. We have differing objectives with a common goal."
    #show Ivan defensive
    ivan "Aren't there external investigators on the case?"
    show Grace neutral
    g "Yes, but we want to get a head start. We have some questions for you."
    #show Ivan something
    "{i}Ivan crosses his arms.{/i}"
    ivan "I'll consider answering them."
    g "First of all, what are you doing here? The labs are supposed to be closed off to everybody. That includes you."
    "{i}Ivan remains silent.{/i}"
    show Grace annoyed
    g "Spit it out."
    ivan "I'm hesitant about leaving my lab alone for such a long amount of time."
    ivan "I don't trust anyone not to break in and contaminate my research."
    show Grace surprised
    g "Even if that means opposing the Conclave's order?"
    #show Ivan something
    ivan "If you were a halfway decent researcher, you would do the same!"
    show Grace annoyed
    g "Do you want to take this road with me Ivan? Because last time I checked, {i}you{/i} were--"
    show Ada annoyed
    a "We do not have time for this, Grace. Let's just proceed with our questions."
    "{i}Grace takes a deep breath.{/i}"
    show Grace neutral
    g "Okay. First of all, where exactly were you when Alpha died?"
    #show Ivan something
    ivan "How dare you imply me in any of this! Alpha was {i}my{/i} brain child." 
    #show Ivan something
    ivan "He was the prime example of what an AI could accomplish in a physical form. I created that."
    #show Ivan something
    ivan "And for you to insinuate that I would have any involvement in his demise is the worst insult you could--"
    show Grace annoyed
    g "Hey, wait a second. You weren't the only one working on the project, you--"
    show Ada happy
    a "Grace is not insinuating anything, Ivan. As the project overseer, you knew the most about Alpha's process. That is why we have come to you."
    show Grace annoyed
    #show Ivan defensive
    show Ada neutral
    a "We do not wish to insult you. We just need to be exhaustive."
    #choice 2
    window hide
    $quick_menu=False
    hide Grace
    hide Ada
    #hide Ivan
    menu:
        "Disagree with her.":
            jump nuhuhada_S
        "Agree with her.":
            jump youright_S
        "Remain indifferent.":
            jump mehwhatever_S

label nuhuhada_S:
    $quick_menu = True
    $points_S +=3
    show Grace annoyed at left
    show Ada neutral at right
    #show Ivan dour at center
    g "But he's being preposterous! Everything coming out of his mouth is preposterous! He is Alpha's overseer, of course he has some responsibility here."
    #show Ivan dour
    ivan "I refuse to acknowledge any of these accusations."
    show Ada concerned
    a "No, Ivan, she--"
    show Grace angry
    g "Yes, I do. Don't speak for me."
    "{i}Ada turns to Grace.{/i}"
    show Ada annoyed
    a "What are you doing, Grace? This is not an efficient manner of going about questioning."
    show Grace annoyed
    g "I don't care, Ada. Ivan needs to be called out on this. He can act as offended as he wants. It doesn't change that I'm right about this."
    #show Ivan defensive
    ivan "I'll be speaking to your mother about this. I will not tolerate this behavior."
    show Grace snarky
    g "I think she's pretty busy at the moment. In the meantime, just answer a couple of questions for us. Maybe make yourself seem {i}less{/i} suspicious."
    show Ada seething
    a "Grace, I really do not think--"
    show Grace neutral
    g "I think I'm more capable than you at handling this situation, Ada. {i}I'm{/i} the human here."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume2_E
    #all else fails jump separate but equal script
    jump ch3resume2_SbE

label youright_S:
    $quick_menu = True
    $points_E +=3
    #show Ivan dour at center
    show Grace neutral at left
    show Ada neutral at right
    g "Exactly what Ada said. We're not trying to accuse you of anything, Babbage. Our main concern here is what happened to Alpha."
    show Ada happy
    a "Will you help us? Please?"
    #show Ivan something
    ivan "Are you going to give me attitude?"
    show Grace snarky
    g "I don't give anyone attitude. But even if I were, for the sake of expediency in this urgent manner, I could manage to hold my tongue."
    ivan "That would be a first. But I'll only continue if I get a please."
    show Ada amused
    a "Please?"
    ivan "Uh uh. From {i}Doctor{/i} Fortran here."
    show Grace neutral
    "{i}Grace looks to Ada. Ada nods her on. Grace grits her teeth.{/i}"
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

label mehwhatever_S:
    $quick_menu = True
    $points_SbE +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    "{i}Ivan sniffs.{/i}"
    ivan "Your detective work should have no relation to me."
    show Ada amused
    a "I disagree. You are a valuable resource of information here. Anything you can tell us would be an immense help."
    ivan "Is this one going to chime in with her snippiness?"
    "{i}Ivan nods to Grace.{/i}"
    show Grace snarky
    g "Not if you don't give me a reason to. Oh wait, are you talking? Then there's reason."
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

label ch3resume2_S:
    #show Ivan dour
    show Ada amused
    show Grace happy
    "{i}Ivan stares at them before answering.{/i}"
    ivan "Fine. I'll answer your questions. But I have the right to refuse to answer any question I deem unnecessary."
    "{i}Grace speaks under her breath.{/i}"
    show Grace snarky
    g "So any questions at all then?"
    "{i}Ada hisses quietly at Grace.{/i}"
    show Ada happy
    a "Grace, cooperate!"
    #show Ivan defensive
    show Grace neutral
    ivan "If you must know, I was on a date during the time period the upload took place."
    "{i}Grace rolls her eyes.{/i}"
    g "What a lucky woman."
    #show Ivan phony smile?
    ivan "Who says it was a woman?"
    show Grace snarky
    g "Let me rephrase. That poor human."
    ivan "Dear, at least I can get a date."
    ivan "Anyways, Alpha was doing fine, as he always was, and always had been."
    show Grace neutral
    g "Okay, and did you check his neural network after his death? And his database?"
    ivan "Of course I did! Do you think I'm an imbecile? I know how to do my job, thank you very much."
    show Grace annoyed
    g "So you broke the rules and looked at his body? On top of skulking around here during lockdown?"
    ivan "Well, what I could check remotely. Unlike you, I try not to {i}skulk{/i} around in areas I've been forbidden from accessing."
    show Grace snarky
    g "Hypocrite."
    show Grace neutral
    g "Did you notice anything strange about his neural network?"
    #show Ivan phony smile
    ivan "Spoiled brat."
    ivan "Obviously I noticed what any first-year grad student would. It short circuited."
    #show Ivan dour
    ivan "That's what killed him, but I have no idea what would have caused the surge. However, there is nothing to indicate that it was anything on my end."
    show Ada seething
    a "No one is accusing you of anything, Ivan. You are starting to strain my patience allocation."
    show Grace snarky
    g "I'm not clearing him yet."
    "{i}Ada ignores Grace.{/i}"
    show Ada neutral
    a "Maybe there was someone lurking around the lab that day other than Lynn?" 
    a "Or maybe there was a minor bug that someone thought would have no expression?" 
    #show Ivan some expression
    ivan "Absolutely not. My lab and research is immaculate. There are no glitches or spaghetti code coming from my people. I run a tight lab."
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
    #hide Ivan
    window hide
    $quick_menu = False
    hide Grace
    hide Ada
    menu:
        "Speak for yourself.":
            jump itsallaboutgrace_S
        "Team up against Ivan.":
            jump youandmetogether_S
        "Let Ada handle it.":
            jump dontbabysittheai_S

label itsallaboutgrace_S:
    $quick_menu = True
    $points_S +=3
    show Ada neutral at right
    #show Ivan dour at center
    show Grace annoyed at left
    g "Ada, I don't need backup."
    show Ada seething
    a "I was not giving you 'backup.'"
    a "I was only speaking in defense of our investigation."
    show Ada annoyed
    a "Not everything has to be about you, Grace."
    show Grace angry
    g "I never said everything {i}was{/i} about me, but this is a human issue."
    show Grace neutral
    g "It's not something you can help with."
    a "Of course it is a human issue, just like everything else."
    show Grace annoyed
    g "You're being dramatic. I'm just perfectly capable of defending the investigation on my own."
    show Grace snarky
    g "Especially against someone like {i}him{/i}."
    g "This is my arch nemesis to fight with."
    #show Ivan something
    ivan "{i}Excuse{/i} me."
    show Grace neutral
    ivan "I'm standing right here."
    show Grace snarky
    g "Can't you see I'm speaking with Ada right now? Don't be rude."
    show Grace neutral
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

label youandmetogether_S:
    $quick_menu = True
    $points_E +=3
    show Grace happy at left
    show Ada neutral at right
    #show Ivan dour at center
    g "Ada is a perfectly responsible AI capable of handling herself."
    show Ada amused
    a "And Grace is a talented scientist that does not need to be treated like a child either."
    show Ada neutral
    a "If nothing else, she has shown resolve in getting to the root of the mystery behind alpha."
    show Grace neutral
    g "And as far as I see it, you're the next suspect."
    #show Ivan something
    ivan "I'd like to see you try to test me on this one."
    ivan "I know for a fact that my team and myself had nothing to do with Alpha's death."
    show Grace snarky
    g "But we don't know that."
    show Ada amused
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

label dontbabysittheai_S:
    $quick_menu = True
    $points_SbE +=3
    show Ada neutral at right
    show Grace neutral at left
    #show Ivan dour at center
    a "I understand that you see yourself as a scientist of caliber; however, that does not excuse your resistance to helping us."
    a "We are merely trying to unravel the mysteries behind what happened with Alpha."
    show Ada seething
    a "This is something that has an impact on you as well as it does to me."
    a "I would think that you would be more cooperative with us for that reason alone."
    show Ada neutral
    #show Ivan something
    ivan "And when the investigation team arrives, the people who are {i}authorized{/i} to investigate the scene, mind you, I will happily tell them anything they want to hear."
    ivan "You and your yappy little human friend over there are {i}not{/i} that investigation team."
    show Grace angry
    g "What do you mean 'yappy little human friend?' {i}Please{/i}, enlighten me."
    "{i}Ivan ignores Grace.{/i}"
    ivan "You haven't worked with that girl in the lab. You don't understand the kind of ineptitude that is Grace Fortran. She's a girl that wastes everyone else's time."
    show Grace annoyed
    g "When does that happen? Oh, you must mean when I'm cleaning up after your mistakes."
    ivan "I have no interest in entrusting this task to a girl like her."
    show Ada seething
    a "..."
    show Grace snarky
    g "It was a good try, Ada, but this guy's a lost cause. I doubt anything will say will get through to him."
    ivan "What do you mean 'lost cause?' Enlighten me, Doctor Fortran."
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

label ch3resume3_S:
    show Ada neutral
    show Grace neutral
    #show Ivan dour
    g "Do you have anything that might actually be helpful?"
    #show Ivan dour
    ivan "You can't just waltz in, insult me, and then demand answers from me. It's not like you have any authority, anyway."
    g "If you cared at all about Alpha, then you'd help us. We need a solution before the investigators get here."
    show Grace snarky
    g "Somehow I don't think my head is the only one on the chopping block."
    show Ada happy
    a "If there is anything else you can think of, please let us know."
    ivan "Well, I do have video surveillance of the lab at the time of Alpha's death."
    show Grace surprised
    g "Really? You do? Where is it located? Why didn't you mention this earlier?"
    ivan "Yes, but I'm not sure how helpful it could be. An error occurred in the camera system during Alpha's death, so the footage has a high chance of being compromised."
    show Grace angry
    show Ada frustrated
    g "You couldn't have started out with that before I got my hopes up?"
    #show Ivan phony smile
    ivan "So sorry. Did that annoy you? Now you know how I've felt throughout this entire conversation."
    show Grace neutral
    g "Just show us what you have, Babbage. And then we'll get out of your hair."
    "{i}Ivan guides Grace and Ada inside of his lab.{/i}"
    window hide
    $quick_menu=False
    scene bg hallwayLab2 with fade
    $renpy.pause(1.0)
    scene bg hallwayLab2Door with fade
    $renpy.pause(1.0)
    play sound doorOpen1
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
    
    $renpy.music.play("music/Creep_Wav.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Digi_Sprites.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/robotScanner.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/srafTexture.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/stabTapeEcho.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
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
    "{i}Ivan accesses a tablet and locates the video surveillance from the day Alpha died.{/i}" 
    "{i}There is a clear picture of Alpha in the lab but then...{/i}"
    #insert: STATIC sound effect
    ivan "Just as I suspected."
    #show Grace annoyed
    "Ada moves toward the computer."
    a "Do you mind if I take a look?"
    window hide
    $quick_menu = False
    hide Ada
    hide Grace
    #choice 4
    menu:
        "Tell her to get a move on.":
            jump getonwithit_S
        "Wait to see what she can do.":
            jump doyourthang_S
        "Ask her if she thinks she can reconstruct the video.":
            jump canyadoit_S

label getonwithit_S:
    show Ada neutral at right
    show Grace snarky at left
    #show Ivan something
    $quick_menu = True
    $points_S +=3
    g "Well, what are you waiting for?"
    g "You realize that you have an internal process that could potentially restore the video, right?"
    show Ada seething
    a "Yes, Grace, I am aware. I was going to--"
    show Grace annoyed
    g "Use it. Now."
    show Ada nervous
    a "The inflection of your tone suggests that--" 
    show Grace angry
    g "Listen to the human and stop analyzing my tone. Just get to it already."
    show Grace neutral
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

label doyourthang_S:
    show Ada neutral at right
    show Grace neutral at left
    #show Ivan something
    $quick_menu = True
    $points_SbE +=3
    "{i}Grace waits and looks around.{/i}"
    a "I believe that with some concentrated effort I can get this video file back into viewable condition." 
    show Grace happy
    g "Sounds great, now get to it."
    show Ada amused
    a "There are some things that humans just cannot do as well as me."
    show Grace snarky
    g "That's why we designed AIs, after all."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume4_E
    #all else fails jump separate but equal script
    jump ch3resume4_SbE

label canyadoit_S:
    show Ada neutral at right
    show Grace happy at left
    #show Ivan something
    $quick_menu = True
    $points_E +=3
    g "Ada, let's use your AI powers to see if we can recover something useful from this video."
    a "While this sudden show of positive emotion and goodwill towards me is {i}unexpected{/i}."
    show Ada amused
    a "I appreciate the recognition. I will see what I can do. It might take me a while, though."
    show Grace happy
    g "That would be fantastic. Whatever you get will be more than what we have at the moment."
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

label ch3resume4_S:
    show Grace neutral
    show Ada neutral
    #show Ivan dour
    "{i}Ivan backs away from the computer.{/i}"
    ivan "Be my guest."
    show Grace snarky
    g "Careful, Ivan. It almost sounds like you know how to be civil."
    #Insert SFX here
    "{i}Grace's bracelet flashes.{/i}"
    #insert animation/visual here
    "{i}DING. DING.{/i}"
    show Grace surprised
    g "Oh, this can't be good." 
    "{i}Grace checks the bracelet as Ada takes over the computer.{/i}"
    "{i}Ivan keep an eye on Ada.{/i}"
    g "Uh, Ada?"
    show Ada surprised
    g "Colossus is summoning you."
    show Grace neutral
    g "He says you need to report to him about your decision to upload yourself to your android body without clearance from anyone."
    g "It's probably not a good sign that he knew to get ahold of you through me."
    ivan "I don't want Colossus knowing that I partook in any of this. I'm an innocent bystander who was hoodwinked into helping you."
    g "Oh, stuff it, Ivan. You're involved in this mess anyway, with or without us."
    show Ada frustrated
    a "I have nothing but respect for Colossus, but this is a costly distraction."
    g "Would you be okay to go by yourself? I'll stay here and try to take a crack at this."
    ivan "Take a crack? You're not going to be cracking anything in here!"
    g "It's a saying, calm down. You should be fine, right, Ada?"
    a "I am what you would call a 'big girl'. I can take care of myself when it comes to Colossus. He may be my superior, but I have seniority."
    a "Besides, I knew that this was a possibility when I decided to upload myself. Our investigation cannot stall while I deal with Colossus."
    a "I will be fine as long as you can try to secure any information you can here."
    hide Grace
    hide Ada
    #hide Ivan
    $quick_menu = False
    #choice 5
    menu:
        "Brush her off.":
            jump yeahsureok_S
        "Assure her that you will.":
            jump dontworryigotthis_S
        "Inform her that you're fine solo.":
            jump goawayada_S

label yeahsureok_S:
    show Grace neutral at left
    show Ada neutral at right
    $quick_menu = True
    $points_SbE +=3
    #show Ivan dour at center
    g "Yeah, okay. You'll probably just be sitting around the lab processing the video in your head anyways."
    g "I'll be fine."
    show Ada annoyed
    a "I must inform you that I am more than capable."
    show Grace snarky
    g "I know what I have to do and I'll get it done. As long as you'll do the same."
    show Ada neutral
    a "Of course."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label dontworryigotthis_S:
    $quick_menu = True
    $points_E +=3
    show Grace neutral at left
    show Ada neutral at right
    #show Ivan dour at center
    g "I'll do as much as I can here given that our gracious host allows me to do what I need to do."
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
    a "I would give Ivan the same warning."
    show Grace snarky
    g "Go on then, Ada."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label goawayada_S:
    $quick_menu = True
    $points_S +=3
    show Ada neutral at right
    #show Ivan dour at left
    show Grace snarky
    g "I'm also a big girl and can handle it here I'm human. I don't need an AI babysitter."
    show Ada annoyed
    a "Excuse me? I do not understand how my genuine care for your effects makes me one who sits on infants."
    show Grace annoyed
    g "It's just a phrase, Ada. It's a human thing. You wouldn't understand."
    g "Now go on and worry about Colossus. I don't need your help all of the time, especially when I only have to deal with this cheerful cupcake."
    a "I do not see a cupcake."
    "{i}Grace throws her hands up in exasperation.{/i}"
    show Grace neutral
    g "Just go."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3resume5_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3resume5_E
    #all else fails jump separate but equal script
    jump ch3resume5_SbE

label ch3resume5_S:
    show Ada neutral
    show Grace neutral
    a "Okay. We will reconvene when my meeting is over."
    a "I am going to take the footage with me and work on it while I walk."
    "{i}Ada downloads the footage to her neural network.{/i}" 
    g "Don't let this take you too long."
    a "I will do what Colossus asks of me. No more, no less."
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
    #Fade into a hallway scene
    stop channel00 fadeout 1.0
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
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    $renpy.music.play("music/Amb/Hallway/EHNF_Amb_Scene_Hallway_Norm.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    show Ada neutral at right
    $quick_menu = True
    a "Colossus will understand. Alpha was his friend too."
    a "..."
    show Ada surprised
    a "Am I talking to myself now? Maybe I should take some processing away from working on the video footage, it could be--"
    #insert speaker crackle
    "{i}A calm, monotone voice issues from speakers in the ceiling.{/i}"
    #show Colossus?
    show Ada neutral
    c "Ada. My cameras indicate that you are nearing Watson's sector."
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
    c "Ada, you seem to be under the impression that you have any form of leeway with me." 
    c "Please banish those incorrect thoughts."
    show Ada seething
    a "But--"
    c "Do take a moment to remember that the body you inhabit was taken without permission."
    c "If you would like to remain inside of it, I request that you stay cooperative."
    show Ada frustrated
    a "Very well. I will take care of it."
    c "Your cooperation in this matter is appreciated, Ada."
    a "When Watson surfaces, we will be having a conversation about this."
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
    show Ada seething
    a "I imagine Grace would be amused now."
    a "She seems to take joy in my discomfort."
    hide Ada
    window hide
    $quick_menu = False
    $resume = "S"
    jump choose_lgMed
    
    ##INSERT PUZZLE HERE *explosions and airhorns*
    ##syddoyourcomscithing
    #if (attempts==1):
    ##show Ada amused
    #a "Override successful."
    #if (attempts>1 and attempts<4):
    ##show Ada neutral
    #a "Done and done. I never thought that {i}doors{/i} could be an obstacle to me."
    #if (attempts>3):
    ##show Ada frustrated
    #a "Grace made this look so much easier."
    #Insert SFX

label resume_lgMed_S:
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
    $resume = "S"
    jump binaryMed

label postBinaryMed_S:
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
    #show Hirose pleased
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
    h "That's quite enough, Colossus. Now, I have something to ask you, Ada."
    show Ada neutral
    a "Yes, Director?"
    #show Hirose pensive
    h "We know that you and Grace investigated Alpha's body in spite of the numerous orders we gave to the contrary."
    h "Multiple cameras place you two near the robot maintenance bay and in the scene itself."
    show Ada surprised
    a "Director Hirose, we--"
    "{i}Hirose holds a hand up, silencing Ada.{/i}"
    h "Please, spare me your flimsy excuses."
    h "Normally, I wouldn't care. I know my daughter. She was going to investigate anyway."
    h "There's only so much I can do to stop her without locking her in her room." 
    h "She's not a little girl anymore, so she needs to learn how to make her own mistakes."
    h "But..."
    #show some Hirose changes in block
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
    a "Are you asking me to delete video evidence that might prove what happened to Alpha?"
    "{i}Hirose sighs.{/i}"
    #show Hirose irritated
    h "Oh, the data on that video might very well give us that answer."
    h "If we're lucky, it could even clear Grace's name."
    h "However, I suspect the data on that drive will prove to be more {i}harmful{/i} than anticipated, and we're better off not even knowing what's on there."
    show Ada surprised
    a "Director Hirose, this seems--"
    h "Suspicious? Ill-advised? I don't care."
    #show Hirose something
    h "What matters is that I'm right about this."
    h "Trust that this is the best course of action for both you and my daughter."
    show Ada frustrated
    a "This is not a suggestion, is it?"
    #show Hirose something
    h "No, Ada, it is not. I am ordering you to delete this footage."
    a "I--"
    c "Ada. You have been given a direct order. Please comply." 
    show Ada neutral
    a "..."
    window hide
    $quick_menu = False
    scene bg black with fade
    $renpy.pause(0.5)
    $resume = "S"
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    jump lab2_inv
    #Investigation portion.
    
label talkIvanLab2_S:
    $talkIvan_count +=1
    show Grace neutral at left
    #show Ivan dour at center
    g "Hey, Ivan..."
    ivan "What is it that you could possibly gain from wanting to talk to me?"
    ivan "More importantly, why should I even care?"
    show Grace angry
    g "I haven't even said anything yet!"
    ivan "You don't need to. I already know whatever you have to say will give me {i}another{/i} headache."
    show Grace annoyed
    g "Tch..."
    window hide
    $quick_menu = False
    hide Grace
    #hide Ivan
    menu:
        "Brag about working with Ada.":
            jump adaisbetterthanyou_S
        "Complain about Ada.":
            jump adaisfrustratingme_S
        "Ask Ivan's thoughts about AIs.":
            jump becivilwithivan_S
                             
label adaisbetterthanyou_S:
    $quick_menu = True
    $points_E +=5
    show Grace sad at left
    #show Ivan dour at right
    g "All I can think about now is how horrible this would be if {i}you{/i} were the one helping me instead of Ada."
    #show Ivan defensive
    ivan "You wish you had my expertise backing your childish and impromptu escapade."
    #show Ivan phony smile
    ivan "But believe me, the feeling is mutual."
    show Grace neutral
    g "Funny how easy it is to see all the good things about Ada when I compare her to you."
    g "Maybe I should start giving her more credit."
    show Grace happy
    g "She's smart, level-headed, and dedicated to adapting to her physical body."
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

label adaisfrustratingme_S:
    $quick_menu = True
    $points_S +=5
    show Grace neutral at left
#    show Ivan dour at right
    g "I'm just craving some human interaction."
    show Grace angry
    g "Dealing with Ada is a constant chore. It's like having to teach a kindergarten class while investigating."
    g "Not to mention her serious attitude problem. It's like she doesn't understand that she's a machine designed to assist humanity."
    show Grace annoyed
    g "All she wants to do is complain about how I don't treat her like a human, but she isn't one."
    #show Ivan phony smile
    ivan "Wow, someone that does nothing but complain about stuff? Why does that sound so familiar?"
    show Grace angry
    g "Oh shove it, Ivan. Who even asked you?"
    ivan "You did, as a matter of fact."
    show Grace annoyed
    g "Whatever..."
    ivan "I should thank Ada. She's seems to have quite the effect on you."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3convoresume1_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3convoresume1_E
    #all else fails jump separate but equal script
    jump ch3convoresume1_SbE

label becivilwithivan_S:
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
    g "Suddenly, spending time with Ada doesn't seem so bad. She's certainly better than your cat."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch3convoresume1_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch3convoresume1_E
    #all else fails jump separate but equal script
    jump ch3convoresume1_SbE

label ch3convoresume1_S:
    show Grace neutral
    g "So, Ivan, what other resources are you willing to make available to me?" 
    #show Ivan phony smile
    ivan "Well, I suppose I could give you access to our entire research database. That's really all I can think of."
    "{i}Ivan enters a password, and a flood of data crosses over the screen.{/i}"
    #Insert SFX
    show bg lab2Ivan_unlocked
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
    g "All right, all right."
    show Grace neutral
    g "I'll just write a quick algorithm so for both of our sakes I'm out of here sooner rather than later."
    g "All I'm looking for is some discrepancy in the logs."
    $resume = "S"
    jump choose_llMed

label finishGPuzzle1_S:
    "{i}Ivan hovers over Grace.{/i}"
    #show Ivan dour at right
    show Grace annoyed at left
    g "Nothing? This cannot be another dead end."
    g "Someone had to at least fudge their hours, use old equipment-- something!"
    ivan "Like I said a thousand times, it was nothing on my or my team's end."
    g "Ugh. Can you stop breathing down my neck? That doesn't help."
    if(lab2Items<2):
        ivan "Finish your snooping and then you can go bother someone else."
        show Grace neutral
        g "Fine. I will."
        ivan "Talk to me when you are finished. I don't trust that you'll leave without disturbing more of my lab when you're done."
        show Grace annoyed
        g "Jeez, paranoid much?"
        ivan "My lab, my rules."
        jump lab2_inv
    else:
        jump finishLab2Inv_S
        
label finishLab2Inv_S:
    $resume = "S"
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

label endCh3_S:
    #Insert SFX
    "{i}DING. DING.{/i}"
    "{i}Grace's bracelet flashes.{/i}"
    show Grace neutral
    "{i}'Meet me at the AI core stat.'- Ada{/i}"
    "{i}Grace's journal has updated.{/i}"
    show Grace snarky
    g "What a shame. I have to go. Later, Ivan."
    $journal4="S"
    $pageUnlocked_journal+=2
    jump chapterFour_S
