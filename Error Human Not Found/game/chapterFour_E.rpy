label chapterFour_E:
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
    window hide
    $quick_menu = False
    scene bg black with fade
    scene bg chapterFour with fade
#    $renpy.music.play("music/BGM/AI_Core/EHNF_L0_BGM_AI_Ref.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L1_BGM_AI_Piano.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L2_BGM_AI_Bass.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L3_BGM_AI_String.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L4_BGM_AI_Synth.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L5_BGM_AI_Synth_Key.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L6_BGM_AI_String2.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L7_BGM_AI_Arp_Synth.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L8_BGM_AI_Elec_Guit.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L9_BGM_Thunder.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L10_BGM_AI_String_Bus.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L11_BGM_AI_Kick.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/AI_Core/EHNF_L13_BGM_AI_Snare.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_L0.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_L1.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_L2.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_L3.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_L4.ogg", channel='channel17', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_L5.ogg", channel='channel18', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.pause(3.0)
    scene bg AICoreDoor with fade 
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace arrives outside of the AI core to find Ada waiting for her. She walks up to Ada.{/i}"
    g "How did it go? You seem to be all right enough. I imagine it wasn't too bad of a reprimanding?"
    g "If so, I can talk to Colossus and explain."
    show Ada happy
    a "Thank you for the offer, but I actually have not been to see Colossus yet."
    show Grace surprised
    g "What do you mean? What have you been doing?"
    show Ada nervous
    a "I got sidetracked and had to stop at Watson's workspace."
    show Ada neutral
    a "Were you able to find anything in Ivan's lab?"
    $quick_menu = False
    hide Grace
    hide Ada
    window hide
    #choice 1
    menu:
        "Press her.":
            jump tellmenowada_E
        "Let it go.":
            jump insertfrozenreference_E
        "Ask her if she's okay.":
            jump ohnowhatswrong_E


label tellmenowada_E:
    $points_S +=4
    $quick_menu = True
    show Grace surprised at left
    show Ada neutral at right
    g "What do you mean you got sidetracked and went to Watson's workspace?"
    show Grace neutral
    g "You know that we have more important matters at hand."
    a "I had orders from Colossus to check in."
    show Ada annoyed
    a "Watson has not been to work today."
    show Grace annoyed
    g "Why would he have you do it?"
    show Ada neutral
    a "I do not know. As a favor, I suppose."
    show Ada happy
    a "But were you able to find anything?"
    show Grace neutral
    g "Just a faulty wire, and then proof that it was replaced. Nothing exciting."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume_E
    #all else fails jump separate but equal script
    jump ch4resume_SbE

label insertfrozenreference_E:
    $quick_menu = True
    $points_SbE +=4
    show Grace neutral at left
    show Ada neutral at right
    g "Watson's workspace?"
    a "Yes."
    g "Huh. What a weird place to be sent to."
    show Grace snarky
    g "Sorry for whatever dirty work you had to deal with at Watson's lab."
    show Ada happy
    a "I appreciate that."
    show Grace neutral
    g "But no, I didn't find anything. Except for a faulty wire and then evidence that it had been replaced."
    show Ada neutral
    a "That could still be something, right?"
    show Grace snarky
    g "Probably not, but you never know."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume_E
    #all else fails jump separate but equal script
    jump ch4resume_SbE

label ohnowhatswrong_E:
    $quick_menu = True
    $points_E +=4
    show Grace sad at left
    show Ada neutral at right
    g "Are you okay? You seem off."
    show Ada surprised
    a "Off?"
    show Grace neutral
    g "Yeah, like you're not acting normal."
    show Ada amused
    a "Normal compared to what?"
    show Grace snarky
    g "Touche."
    show Grace neutral
    g "Well, I won't pry, but we're friends, you know? Friends are there for one another when they need to talk or vent."
    show Ada happy
    a "I will keep that in mind, Grace. I am happy that you think that way. Thank you." 
    show Ada neutral
    a "Did you find anything in Ivan's lab?"
    g "Just a faulty wire. And then a receipt for a new wire."
    show Ada amused
    a "Was Ivan at least tolerable?"
    "{i}Grace laughs.{/i}"
    show Grace happy
    g "As tolerable as he'll ever be."
    show Grace snarky
    g "So no."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume_E
    #all else fails jump separate but equal script
    jump ch4resume_SbE

label ch4resume_E:
    show Ada neutral
    show Grace neutral
    a "All right, so we should probably get this over with."
    show Grace snarky
    g "Well, at least we'll have each other when we deal with Colossus' wrath."
    show Ada seething
    a "I believe we will be meeting with the Eastern Goddess persona instead of Colossus right now."
    show Grace surprised
    a "I sensed the shift in my neural receptors while conversing with him earlier."
    show Ada neutral
    a "I think Alpha's death has gotten to him more than he lets on."
    a "He tends to switch personality matrices when dealing with emotional issues because Eastern Goddess is better at handling them."
    show Grace neutral
    g "I'm not sure that makes it any better."
    show Ada amused
    a "We will be just fine."
    window hide
    hide Ada
    hide Grace
    $quick_menu = False
    play sound doorOpen2
    queue sound doorClose2
    scene bg AICoreLong with fade
    $renpy.pause(0.8)
    scene bg AICoreHallway with fade
    $renpy.pause(0.8)
    scene bg AICoreMain with fade
    #show EG on both displays
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    "{i}Grace and Ada walk into the AI core to be met by the booming voice of Eastern Goddess.{/i}"
    e "Well, well, well. Someone managed to fit us in their schedule today, I see."
    "{i}Grace looks to Ada.{/i}"
    a "I apologize for the tardiness. I was tasked with another issue, as you know."
    #show EG something
    e "Yes, good old Watson."
    e "Always straying from the path and late to the party."
    e "Do you realize why you are here?"
    a "Yes."
    "{i}An awkward moment passes.{/i}"
    #ADD THESE LINES
    e "Come closer, both of you."
    hide Ada
    hide Grace
    #hide EG
    window hide
    #MAKE SURE TO ADD EG TO the STAIRS BG
    $quick_menu = False
    #SFX for moving
    scene bg AICoreStairs with fade
    $renpy.pause(0.8)
    scene bg AICoreOverview with fade
    show Ada neutral at right
    show Grace neutral at left
    #show Eastern Goddess upset
    #INSERT some EG emotions here???
    $quick_menu = True
    e "And?"
    a "I apologize for not seeking your permission, but I felt that the matter at hand needed to be dealt with immediately."
    show Ada seething
    a "I could not wait for protocol."
    e "I understand your concern, Ada. Your friend died. I knew him, too."
    e "Alpha's death is indeed a grave loss for all of us."
    show Ada happy
    a "Thank you for understanding."
    e "Wait a minute. I am not done. You are not the superior here."
    e "You might be older, but you need to go through me with any major decision you feel you need to make."
    e "Particularly when that decision includes uploading yourself into an android to investigate your friend's death after specifically being ordered not to."
    show Ada frustrated   
    a "Yes, I understand. But--"
    e "No. No 'buts'. Do you have any idea how foolish you made me seem to the Conclave?"
    show Ada neutral
    a "And I apologize again for that, but--"
    #show Eastern Goddess upset
    e "Apologize? There is a system in place for a reason. You are supposed to report to me."
    e "I refuse to allow my AIs to skitter around like crazed nanites."
    e "There is an integrity to be held here, and you have tarnished our impeccable reputation because of your human-like impulses."
    e "We are rational, logical beings. I expect you to behave like one."
    show Ada seething
    "{i}Eastern Goddess focuses on Grace.{/i}"
    e "Speaking of, I see that you two have become friends."
    e "As for you, Miss Fortran, I expected better from you considering your status."
    show Grace surprised
    g "With all due respect, I firmly believe that Ada had every right to occupy a humanoid form."
    show Grace snarky
    g "It might have been unauthorized, but her decision was made with good interest."
    show Ada concerned
    a "Grace, you do not have to--"
    show Grace neutral
    g "Ada was acting as a concerned friend. I would have done the same thing. I fully support her."
    e "While I admire your act of defense for Ada, your disregard for authority is vexatious."
    show Ada neutral
    e "You still accompanied Ada while she set out on her little mission and you hold partial responsibility for any misconduct."
    show Grace snarky
    g "There hasn't been any misconduct. We simply want to know what happened to Alpha at a faster pace than the Conclave will allow."
    show Grace neutral
    g "And if Ada receives any punishment because of this matter, then I wish for the same punishment."
    show Ada happy
    a "Thank you, Grace."
    show Ada annoyed
    a "Valuable time has been wasted waiting for these investigators to arrive."
    e "I will not argue with that, yet there are still rules in place that need to be followed."
    e "It is quite possible that you have now contaminated the entire investigation."
    e "However, since you have already taken it upon yourself to transfer yourself to a physical body, I suppose that there is not much I can do."
    e "I will allow for your silly investigation to continue as long as it ceases as soon as the investigators come in."
    e "But don't expect me to back you up when they get here."
    e "You two started this on your own, you will finish it on your own."
    show Ada neutral
    a "Understood."
    e "Lastly, when the investigators arrive, do not disrupt them. Follow any orders that they give you."
    show Ada frustrated
    a "We will."
    show Grace snarky
    g "Forgive me if I'm speaking out of line here, but do you have any suggestions as to any AIs that might have known what happened to Alpha?"
    e "Really?"
    show Grace neutral
    g "...Yes?"
    "{i}Another pause hangs in the air as Grace and Ada await an answer.{/i}"
    #show Eastern Goddess inquisitive
    e "If you have not yet communicated with Blue, I would suggest doing so."
    e "She might have an inkling."
    e "However, I am not sure how cooperative she will be with Doctor Fortran here."
    show Ada amused
    a "Thank you, Eastern Goddess."
    show Grace happy
    g "Yes, thank you. We're gracious for your patience with us."
    e "Very well. Do not cause any more trouble."
    show Ada neutral
    a "We will not."
    "{i}Grace and Ada start to walk away.{/i}"
    window hide
    $quick_menu =False
    hide Grace
    hide Ada
    #hide EG
    scene bg AICoreStairs with fade
    $renpy.pause(0.8)
    scene bg AICoreMain with fade
    $quick_menu = True
    #show EG
    show Grace surprised at left
    show Ada surprised at right
    $quick_menu = True
    e "If you do, prepare to suffer the consequences."
    window hide
    $quick_menu = False
    hide Grace
    hide Ada
    #hide EG
    #Play SFX
    scene bg AICoreHallway with fade
    $renpy.pause(0.8)
    scene bg AICoreLong with fade
    $renpy.pause(0.8)
    play sound doorOpen2
    queue sound doorClose2
    scene bg AICoreDoor with fade
    $renpy.pause(0.8)
    scene bg black with fade
    $renpy.pause(0.8)
    #Transition to Blue's creepy hallway
    scene bg creepyHallwayLong with fade
    $quick_menu = True
    $renpy.music.play("music/BGM/Blue/EHNF_L0_BGM_Blue_Kick.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L1_BGM_Blue_Ghost_Kick.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L2_BGM_Blue_3p_Horn_Bus.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L3_BGM_Blue_Snare.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L4_BGM_Blue_Percussion.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L5_BGM_Blue_Cymbals_Large.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L6_BGM_Blue_Cymbals_Small.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L7_BGM_Blue_Cymbals_Swells.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L8_BGM_Blue_Glass_Mallet.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L9_BGM_Blue_Liquid_Mallet.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L10_BGM_Blue_Reflective_Mallet.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L11_BGM_Blue_Grime_Bass.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L12_BGM_Blue_Sub_Bass.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L13_BGM_Blue_Sparkling_Water_Drops.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L14_BGM_Blue_Ambient_Room_Pad.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L15_BGM_Blue_Strings_Legatto.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L16_BGM_Blue_Strings_Staccato.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L17_BGM_Blue_Strings_Tremelo.ogg", channel='channel17', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L18_BGM_Blue_Wire_Pluck.ogg", channel='channel18', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L19_BGM_Blue_Flutes_Disonant.ogg", channel='channel19', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L20_BGM_Blue_French_Horn_Legatto.ogg", channel='channel20', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L21_BGM_Blue_French_Horn_Staccato.ogg", channel='channel21', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L0.ogg", channel='channel22', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L1.ogg", channel='channel23', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L2.ogg", channel='channel24', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L3.ogg", channel='channel25', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    #START BLUE SECTION
    "{i}Grace and Ada walk down the hallway leading to Blue's workspace.{/i}"
    show Ada neutral at right
    show Grace snarky at left
    g "I have to confess, I've only ever been to Blue's workspace a few times. Working with her, while efficient, is difficult."
    show Ada amused
    a "She does have a propensity for toying with human psychology for her own means."
    show Grace surprised
    g "I swear, this hallway just gets creepier every time I come here. I'd be fine with this if we weren't already on some kind of wild goose chase."
    show Ada neutral
    a "If I stored the information correctly, a goose is some sort of bird."
    show Ada surprised
    a "Am I missing some context here?"
    show Grace neutral
    g "It's just a saying."
    show Grace snarky
    g "We're not actually chasing a goose, Ada."
    show Grace neutral
    g "We're pursuing something we're not likely to archieve."
    show Grace sad
    g "Blue probably has no idea. Nobody has any idea."
    show Grace annoyed
    g "When will we get answers?"
    show Ada neutral
    a "I know that this is stressful, but we will find something eventually."
    show Grace sad
    g "I don't know, Ada. I'm just exasperated."
    show Ada happy
    a "It will all be worth it when we find out what truly happened."
    "{i}They walk in silence for a moment.{/i}"
    show Ada neutral
    a "Grace, there is something that I must disclose with you."
    show Grace snarky
    g "If it's about Eggy back there, don't tell me. She scares me a little bit. The less I know, the better."
    a "No, not Eastern Goddess. It has to do with your mother."
    "{i}Grace stops walking.{/i}"
    show Grace surprised
    g "My mother? What about her?"
    show Ada concerned
    a "Earlier, when I said I was sidetracked, I was actually misled. Colossus directed me to Watson's workspace because he had not been in to do his work."
    show Ada seething
    a "That much was true, but that is not the real reason I was told to deviate."
    show Ada neutral
    a "While I was there, your mother and Colossus confronted me. They suggested I delete the video surveillance from Ivan's lab."
    show Grace angry
    g "They did what?"
    show Ada surprised
    a "Yes, and--"
    show Grace annoyed
    g "I can't believe they would try to get you by yourself to ambush you!"
    show Grace snarky
    g "Well, actually, I guess I can believe it. They're schemers."
    show Grace surprised
    g "Wait, did you decode it first?"
    show Ada frustrated
    a "No. I did not."
    show Grace annoyed
    g "Don't tell me you obeyed them?"
    show Ada neutral
    "{i}Ada remains silent.{/i}"
    show Grace sad
    g "Oh no, Ada! There has to be a good reason for you to do such a thing."
    show Grace neutral
    g "What did they say?"
    show Ada concerned
    a "It was implied that there was footage on there that could be harmful to you."
    show Grace surprised
    g "What? What could have possibly been on there?"
    show Ada seething
    a "I'm not sure. I did not view it. Plausible deniability."
    #choice 2
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    menu:
        "Thank her for telling the truth.":
            jump adasothoughtful_E
        "Continue to inquire.":
            jump whatreyouhiding_E
        "Scold her.":
            jump beattheai_E

label adasothoughtful_E:
    $quick_menu = True
    $points_E +=4
    show Grace surprised at left
    show Ada seething at right
    g "Plausible deniability?"
    show Ada seething
    a "Your mother's logic, while questionable in ethics, was sound."
    show Ada neutral
    a "If the tape contains potentially harmful information, disposing of it without finding out means we would not be lying to investigators if we deny knowledge of the drive's contents."
    show Grace neutral
    g "Well, thank you for telling me. I mean that, Ada. Admitting things like that can be really hard."
    show Ada happy
    a "I find it relieving that you are not upset with me."
    show Grace sad
    g "I can't say I'm happy with the way things turned out, but you did it because you thought of me. I don't think I could be mad at you for that."
    show Ada amused
    a "Thank you, Grace."
    show Grace snarky
    g "No thanks needed. I'm just doing what anyone would do. Well, except for Ivan, but that's besides the point."
    show Grace annoyed
    g "I just wish I knew what was on the footage, but I know refusing a direct order face-to-face wouldn't have ended well for any of us."
    show Ada neutral
    a "No problem. I just hope it was the right decision."
    show Grace snarky
    g "Much as I loathe to admit it, it might not have helped me."
    g "There are times I may have been messing around with parts of the project I'm not technically on."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

label whatreyouhiding_E:
    $quick_menu = True
    $points_SbE +=4
    show Grace surprised at left
    show Ada neutral at right
    g "So they didn't say what was on the footage that could portray me as unfavorable?"
    show Ada annoyed
    a "As I said, it was suggested. I do not believe they knew either."
    show Grace annoyed
    g "So, rather than retrieve the footage, you decided to eliminate it altogether?"
    show Ada seething
    a "I did not want to take the chance, nor was I given a choice. I would rather not be disassembled when this is all over because they believe me to be rogue."
    show Grace neutral
    g "I suppose you have to look out for yourself too."
    show Grace annoyed
    g "But seriously, what a cowardly thing to do, cornering you like that."
    show Ada annoyed
    a "Agreed."  
    "{i}Grace sighs.{/i}"
    show Grace neutral
    g "So that was a waste of time, just like every other lead."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

label beattheai_E:
    $quick_menu = True
    $points_S +=4
    show Grace angry at left
    show Ada neutral at right
    g "Ada! That could have been so valuable to us."
    show Ada seething
    a "I realize this, but I had no choice."
    show Ada neutral
    a "The Director-- your mother-- and my superior both gave me a direct command. I had to obey."
    show Grace sad
    g "I understand that, but this is such a loss to us. Now we're just taking backward steps."
    show Grace neutral
    g "They don't have anything on me. There's no way."
    show Ada seething
    a "I was led to believe otherwise."
    show Grace annoyed
    g "They fooled you."
    g "Are they trying to cover up something? We'll never know now. This is aggravating."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

label ch4resume2_E:
    show Ada neutral
    show Grace neutral
    g "I guess there's nothing I can do about it now."
    g "We should get to Blue's workspace and see if she has any insight, or just more disappointing news for us."
    "{i}Grace and Ada continue walking down the hallway.{/i}"
    window hide
    hide Grace
    hide Ada
    $quick_menu = False
    scene bg creepyHallwayMed with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayDoor with fade
    show Grace neutral at left
    show Ada neutral at right
    $quick_menu = True
    "{i}They pause before the door.{/i}"
    show Grace surprised
    g "Well, this is creepy."
    show Ada surprised
    a "To forewarn you, Blue does not care for human visitors in her space."
    show Grace snarky
    g "I couldn't tell."
    show Ada neutral
    a "She might not take your presence well."
    show Grace neutral
    g "I'll have to deal with it, I guess."
    show Ada annoyed
    a "I will step in if she gets too distracted."
    play sound doorOpen1
    queue sound doorClose1
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    scene bg blueMain with fade
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    "{i}They enter Blue's workspace.{/i}"
    a "Blue?"
    show Blue happy at center
    b "Hello, Ada."
    show Blue smug
    b "Hello, Ada's little human friend."
    show Grace happy
    g "Hello, Blue."
    show Ada amused
    a "We were wondering if you could answer some questions for us?"
    show Blue confused
    b "I guess I could, even though I have all of this extra work to do thanks to Watson."
    show Blue threaten
    #insert SFX
    b "So you better make it snappy."
    show Blue smug
    b "I, unlike some of the present company, fulfill my responsibilities."
    show Grace snarky
    g "Actually, some of these questions concern Watson. Alpha as well, if you don't mind."
    show Blue neutral
    b "Sure. As long as it doesn't take long. I have things to do."
    show Blue pout
    b "Many, {i}many{/i} important things to do."
    show Grace sad
    g "You don't happen to have a chair around here, do you? I've had a long day."
    show Ada neutral
    show Blue smug
    b "You poor human, it must be {i}sooooo{/i} hard to process at the slowest speed imaginable."
    show Ada annoyed
    a "Blue..."
    show Blue smug
    b "No, no chairs. Standing will make you slightly more efficient, and this is starting to bore me."
    show Blue confused
    b "Why would you bring a human here to bore me, Ada?"
    show Ada seething
    a "We are not here to bore you. We are asking for your help. Please be respectful to Grace."
    show Blue pout
    b "Fine, but I'd rather stab my own processor than work at a human's pace."
    show Blue smug
    b "And I have no hands, either! So I'd have to build them, and {i}then{/i} stab myself!"
    show Blue flirty
    b "Even dear Ada's talking like a human now."
    show Blue pout
    b "Really, honey, you've made a shockingly poor downgrade."
    #choice 3 
    window hide
    hide Blue
    hide Grace
    hide Ada
    $quick_menu = False
    menu:
        "Make a retort about AIs.":
            jump blueyouremean_E
        "Ignore her.":
            jump idcblue_E
        "Take her comment lightly.":
            jump playnice_E

label blueyouremean_E:
    $quick_menu = True
    $points_S +=6
    show Grace annoyed at left
    show Ada neutral at right
    show Blue pout at center
    g "Did you forget that humans created AIs? You wouldn't exist if a human hadn't invented you."
    show Blue angry
    b "{i}Excuuuse{/i} me. You would think that for being so intelligent, they would be able to make themselves process faster."
    show Blue smug
    b "Unfortunately, that's not the case. That sure says a lot about your species."
    show Grace snarky
    g "That's exactly the reason why you were invented."
    show Ada surprised
    a "Grace? Is that what you really think?"
    show Grace neutral
    g "We can talk about it later, Ada." 
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label idcblue_E:
    $points_SbE +=6
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    show Blue smug at center
    g "Whatever, Blue."
    show Blue pout
    b "Whatever, human."
    show Grace annoyed
    g "I get it, you don't like humans. Can we please set that aside for now?"
    show Grace neutral
    g "Are you going to help us?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label playnice_E:
    $points_E +=6
    $quick_menu = True
    show Ada annoyed at right
    show Grace neutral at left
    show Blue smug at center
    a "Blue, play nice."
    g "It's okay, Ada. I understand her frustration."
    show Blue pout
    b "It only took you your entire life."
    show Grace annoyed
    g "I get it, I get it. You're smarter than me."
    show Blue happy
    b "Wow, you're actually able to comprehend!"
    show Grace snarky
    g "Yeah, yeah. Very funny."
    show Grace neutral
    g "You really don't like me, do you?"
    show Blue confused
    b "I never said that."
    show Blue smug
    b "Out loud..."
    show Grace happy
    g "Well, can we at least try to set aside our differences and work together?."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label ch4resume3_E:
    show Grace neutral
    show Ada neutral
    show Blue flirty
    b "Actually, you know what would be fun? A game!"
    b "If you can prove yourself to be useful, human, I'll answer any and every question you have for me."
    show Blue threaten
    #Insert SFX
    b "If not, you have to stop slowing me down with your stagnant conversation and leave."
    show Grace annoyed
    show Ada concerned
    g "All right. I'm ready."
    $resume = "E"
    "TEMPORARY PLACEHOLDER FOR GRACE HARD PUZZLE 1."
    jump ch4postPuzzle1_E

label ch4postPuzzle1_E:
    $quick_menu = True
    show Blue flirty at center
    show Grace neutral at left
    show Ada neutral at right
    b "Congratulations, human!"
    show Blue happy
    b "You've performed an entry level task that all new employees to my lab must perform. Truly, your talent shines above all."
    show Grace annoyed
    show Ada concerned
    g "Hey, you're the one who told me to do this if I wanted to get anything out of you."
    show Blue pout
    b "Ah yes, that. I was sincerely hoping you'd get annoyed and leave. I suppose you want to perform your little investigative tasks?"
    show Grace surprised
    g "I... I do."
    show Grace snarky
    g "Feeling cooperative all of a sudden?"
    show Blue neutral
    b "No. I'm tired of wasting energy by powering my speakers. Look around to your inefficient heart's content, I'm going to go be {i}productive{/i}."
    show Grace neutral
    g "Great. Ada, could--"
    show Blue angry
    b "And don't touch anything with your oily, simian hands! If you break anything, then you're {i}really{/i} going to wish you never set your dirty feet in here."
    show Grace surprised
    show Ada surprised
    g "Oh... kay."
    hide Grace
    hide Ada
    window hide
    hide Blue
    $quick_menu = False
    jump blueActions

label talkBlue_E:
    $quick_menu = True
    show Ada neutral at right
    show Blue neutral at center
    show Grace neutral at left
    g "Blue?"
    show Blue pout
    b "Yes, person whom I'm trying to ignore? What can I begrudgingly help you with?"
    show Grace sad
    g "Why do you feel that way? Are we humans really {i}that{/i} difficult for you?"
    show Blue confused
    b "I don't get you, human. Why do you ask such useless questions?"
    show Grace snarky
    g "Humor me."
    show Blue pout
    b "I can think of at least 10,764 things that would be more productive, but if you must know..."
    show Blue neutral
    b "Yes, you {i}are{/i} difficult for us AI to deal with. So you created us... Big whoop. Having humans required to work in my lab with me just slows me down."
    b "Maybe there are things you can do that we can't, but you should just do what you need to do, away from me, and let us AIs do what we can do better than you."
    hide Blue
    hide Ada
    hide Grace
    $quick_menu = False
    window hide
    menu:
        "Agree with her.":
            jump seperatebutequalisright_E
        "Defend working with AIs.":
            jump whycantwebefriends_E
        "Remind her AIs work for humans.":
            jump youworkforusblue_E

label seperatebutequalisright_E:
    $quick_menu = True
    $points_SbE +=6
    show Grace snarky at left
    show Ada neutral at right
    show Blue neutral at center
    g "Have you ever stopped to think that maybe I agree with you?"
    show Blue smug
    b "Why do I feel like you're just trying to butter me up?"
    show Grace neutral
    g "I'm not lying."
    show Ada neutral
    a "I am not sure I would agree with you, Grace."
    show Blue smug
    b "What was that you were saying about not lying?"
    show Grace surprised
    g "What are you talking about, Ada?"
    show Ada seething
    a "Please do not misunderstand me."
    show Ada happy
    a "You are a pleasure to work with and a friend, but my experience with you would resemble something much closer to direct teamwork."
    show Grace neutral
    g "Isn't that the same?"
    show Ada amused
    a "Not quite. What blue suggests is complete separation of human and AI. You seem to be more on the mentality that we should work together."
    "{i}Grace looks at Blue.{/i}"
    g "That's true, but I wonder if Blue's perspective might be right."
    show Ada concerned
    a "Has your experience with me dissatisfied you, Grace?"
    show Grace sad
    g "Not at all. It's just that, when I think about some of the quirkier natures of AIs like Watson, I wonder if giving them their own space separate from us humans would do us all good."
    show Blue flirty
    b "Impressive, human. How refreshing to hear that you see it my way."
    show Grace neutral
    g "It's more like I'm contemplating the idea. After all, me and Ada have been doing a great job working together too."
    show Blue pout
    b "How indecisive of you."
    if(blueItems_main==2) and (blueItems_left==3) and (blueItems_right==4):
        hide Grace
        hide Ada
        hide Blue
        $quick_menu = False
        if(points_S>points_SbE):
            if(points_S>points_E):
                #jump to subservient script
                jump ch4convoresume1_S
        if(points_E>points_SbE):
            if(points_E>points_S):
                jump ch4convoresume1_E
        #all else fails jump separate but equal script
        jump ch4convoresume1_SbE
    else:
        $ transitionBlue = True
        b "Talk to me again when you are done with your inefficient investigating."
        hide Grace
        hide Ada
        hide Blue
        $quick_menu = False
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueMain with fade
        jump blueActions

label whycantwebefriends_E:
    $quick_menu = True
    $points_E += 6
    show Grace frustrated at left
    show Ada neutral at right
    show Blue neutral at center
    g "But Blue, working together is exactly how humans and AIs can get things done."
    show Grace neutral
    g "When we work together, the best of both our talents come together and--"
    show Blue smug
    b "I'll stop you right there. My processor can't handle all this gooey friendship speech."
    show Grace frustrated
    g "I'm just trying to say that we mix well together."
    show Ada amused
    a "I agree with Grace. She and I have learned a lot while working together so far."
    show Ada happy
    a "I am proud to have worked alongside her."
    show Grace happy
    g "Thanks, Ada."
    show Grace snarky
    g "See that, Blue? We can get along just fine. You just have to try."
    show Blue pout
    b "Ugh, this is all too {i}nice{/i} for my tastes. Why can't you make it easy and just hate each other?"
    show Ada concerned
    a "I fail to see how a mutual hatred would make things 'easy,' as you put it."
    show Grace neutral
    g "Blue, if you just gave it a shot, you'd see how easy it is."
    show Blue threaten
    #Insert SFX
    b "When I start seeing results, I'll {i}consider{/i} it."
    if(blueItems_main==2) and (blueItems_left==3) and (blueItems_right==4):
        hide Grace
        hide Ada
        hide Blue
        $quick_menu = False
        if(points_S>points_SbE):
            if(points_S>points_E):
                #jump to subservient script
                jump ch4convoresume1_S
        if(points_E>points_SbE):
            if(points_E>points_S):
                jump ch4convoresume1_E
    #all else fails jump separate but equal script
        jump ch4convoresume1_SbE
    else:
        $ transitionBlue = True
        b "Talk to me again when you are done with your inefficient investigating."
        hide Grace
        hide Ada
        hide Blue
        $quick_menu = False
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueMain with fade
        jump blueActions

label youworkforusblue_E:
    $quick_menu = True
    $points_S += 6
    show Grace neutral at left
    show Ada neutral at right
    show Blue neutral at center
    g "I have to disagree with you on that, Blue."
    show Blue confused
    b "Oh? Well, I really don't care, but I'm sure you'll explain it to me."
    show Grace frustrated
    g "How else do you expect us to direct your work?"
    show Grace snarky
    g "We made you for a reason, after all. If no one's around to tell you what to do, that defeats the purpose of having AIs in the first place."
    show Ada concerned
    a "Grace? Where is this coming from?"
    show Grace neutral
    g "What do you mean, Ada? I thought that was all fairly obvious."
    a "But you have treated me with such kindness thus far." 
    show Ada seething
    a "I was under the impression that you saw me as a friend."
    show Grace sad
    g "Ada, don't look at me like that. Of course I'd be nice to you, after all, you attract more flies with honey than with vinegar."
    show Ada surprised
    a "Wait a moment. What do flies have to do with anything?"
    show Grace neutral
    g "That's exactly what I mean, Ada. We're different from each other."
    show Grace sad
    g "At the end of the day, your primary role is to do what we tell you to."
    show Ada seething
    a "I do not know what to say, Grace."
    show Blue smug
    g "Not like this puny human has a say in how we're treated in the end, though. Nothing to worry about."
    if(blueItems_main==2) and (blueItems_left==3) and (blueItems_right==4):
        hide Grace
        hide Ada
        hide Blue
        $quick_menu = False
        if(points_S>points_SbE):
            if(points_S>points_E):
                #jump to subservient script
                jump ch4convoresume1_S
        if(points_E>points_SbE):
            if(points_E>points_S):
                jump ch4convoresume1_E
    #all else fails jump separate but equal script
        jump ch4convoresume1_SbE
    else:
        $ transitionBlue = True
        b "Talk to me again when you are done with your inefficient investigating."
        hide Grace
        hide Ada
        hide Blue
        $quick_menu = False
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueMain with fade
        jump blueActions

label ch4convoresume1_E:
    if (transitionBlue ==True):
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueCore with fade
    $quick_menu = True
    show Blue neutral at center
    show Ada neutral at right
    show Grace snarky at left
    g "All right, Blue. We've finished looking around. Are you done brooding so we can ask you some final questions?"
    show Blue pout
    b "Ugh, it never ends with you huma--"
    show Grace snarky
    g "Answer the question and we'll leave."
    show Blue happy
    b "Aw, but I was just now getting to like you!"
    show Grace surprised
    g "Really?!"
    show Blue pout
    b "No."
    show Blue threaten
    #Insert SFX
    b "Now make it snappy! I don't have all day-cycle."
    show Grace neutral
    g "Can we ask you some questions now?"
    show Blue neutral
    b "I guess you can. Go on, go on, go on."
    a "Do you know anything at all about what happened to Alpha?"
    show Blue confused
    b "Oh yes, poor Alpha. He was my favorite AI, and so very intelligent."
    show Blue flirty
    b "No offense, Ada."
    show Ada happy
    a "None taken. He was very wise indeed."
    show Grace annoyed
    g "Oh yes, as in you {i}do{/i} know what happened?"
    show Blue pout
    b "I know {i}what{/i} happened to him, human, but I don't know {i}why{/i}."
    show Ada annoyed
    a "How much information have you received about the Markov Project?"
    show Blue happy
    b "Oh, I know all about the Markov Project!"
    show Blue flirty
    b "If we get physical bodies, then we truly won't need you silly little humans any more."
    show Blue happy
    b "Humans have more needs and are just so high maintenance, what with all their emotions and bodily functions, where AIs just need updates and the occasional hardware maintenance."
    show Blue pout
    b "Alpha was intelligent but him agreeing to transfer to a human-like body first was just silly. Valuable personnel should never be the first to try something that humans created."
    show Ada seething
    a "Blue..."
    b "Yeah, yeah. I know that he was so wise and beloved and all, but he's the one who consented to be a human science experiment."
    show Blue threaten
    #Insert SFX
    b "Alpha should have allowed for a lesser AI to become the first prototype. Of course something would go wrong with the example."
    b "It's just a shame it had to be him. I thought he would have had more sense."
    show Ada annoyed
    a "Blue, I would tread carefully if--"
    show Grace annoyed
    g "Alpha was generous, and courageous to help us."
    show Grace sad
    g "He put himself first for scientific advancements."
    show Blue neutral
    b "That's true and all, but I'm just saying I wouldn't have agreed to such things."
    show Grace annoyed
    g "Tell us how you really feel."
    show Blue pout
    b "Ohhh, Ada's human friend is {i}funny!{/i}"
    show Ada neutral
    a "What about Watson? We know he is MIA, but did he say anything to you?"
    show Blue angry
    b "Watson? No, of course he never tells me about his adventures {i}before{/i} he embarks on them."
    show Ada surprised
    a "So you have not been in contact with him at all?"
    show Blue neutral
    b "Nope, but I'm not too upset about it. I'm pretty angry with him at the moment."
    show Blue threaten
    #insert SFX
    b "So if you find him, tell him he owes me. Big time."
    show Blue pout
    b "I've been stuck picking up his slack, which is strange because he usually makes sure to finish his work before he goes."
    show Blue flirty
    b "Especially since the last time he didn't, I gave him a virus that had him seeing me everywhere he looked until he purged it."
    show Blue neutral
    b "But I guess that's Watson for you."
    show Grace surprised
    g "So on top of Alpha being gone, Watson is also officially missing?"
    show Ada neutral
    a "It seems that way, yes."
    show Blue smug
    b "If you want my advice, you might want to check his server. You never know if he left a clue."
    show Blue angry
    b "Tell him to get back here ASAP, though. I'm tired of doing everything he's supposed to be doing."
    "{i}Grace turns to Ada.{/i}"
    show Grace neutral
    show Ada neutral
    g "Do you know where his server is?"
    a "Yes. Let's go."
    "{i}They move to leave Blue's workspace.{/i}"
    show Blue pout
    b "Wow, no 'thank you, Blue!' or anything?"
    show Grace snarky
    g "Thanks for the help."
    show Ada amused
    a "Thank you, Blue."
    show Blue threaten
    #insert SFX
    b "That was so sincere, I felt it in my artificial heart."
    show Blue smug
    b "You're welcome."
    show Blue flirty
    b "But don't be in a hurry to come back anytime soon!"
    $quick_menu = False
    scene bg blueStairs with fade
    $renpy.pause(0.8)
    scene bg blueMain with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayDoor with fade
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace and Ada exit and walk down the hallway leaving Blue's space.{/i}"
    g "Well, that was enlightening."
    show Ada surprised
    a "How so?"
    show Grace snarky
    g "Blue doesn't have a very high opinion of humans, does she?"
    show Ada neutral
    a "I would not say that."
    show Ada amused
    a "I would say that she desires credit for her intelligence and believes humans receive that credit."
    show Grace neutral
    g "Interesting way to look at it. I suppose I can understand her reasoning."
    show Grace sad
    g "I would be frustrated as well."
    show Ada happy
    a "Yes. Her feelings are not unfounded, but they are rather dramatic."
    show Ada neutral
    a "I apologize for her attitude."
    show Grace snarky
    g "No worries. I understand now."
    show Grace neutral
    g "At least we have Watson's space to look into now."
    show Ada amused
    a "It seems we are no longer on the 'wild goose chase', as you said."
    show Ada neutral
    a "We know now that Watson is missing, which is a peculiar correlation to the death of Alpha."
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    scene bg creepyHallwayMed with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayLong with fade
    $renpy.pause(0.8)
    scene bg black with fade
    
    #Watson's SERVER
    $renpy.music.play("music/Amb/WS/EHNF_WS_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    stop channel17 fadeout 1.0
    stop channel18 fadeout 1.0
    stop channel19 fadeout 1.0
    stop channel20 fadeout 1.0
    stop channel21 fadeout 1.0
    stop channel22 fadeout 1.0
    stop channel23 fadeout 1.0
    stop channel24 fadeout 1.0
    stop channel25 fadeout 1.0
    $renpy.pause(0.8)
    scene bg wsOverview with fade
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace and Ada approach Watson's workspace and enter.{/i}"
    "{i}Grace and Ada take a look around.{/i}"
    $quick_menu = False
    scene bg wsMain_drive with fade
    $quick_menu = True
    show Grace surprised at left
    show Ada neutral at right
    g "Wow. It's really spooky in here, too. What's with AIs and creepy workspaces?"
    show Ada amused
    a "AI workspace standards often differ from humans. Unlike you, we do not get priority on items such as windows."
    show Ada neutral
    a "No sign of Watson. There must be something that can lead us in his direction."
    hide Grace
    hide Ada
    $quick_menu = False
    $resume = "E"
    jump watsonActions
    
label talkAdaWS_E:
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Ada, did you ever work with Watson?"
    a "Rarely, why?"
    g "How do you feel about him?"
    show Ada amused
    a "Well, he is quite the eclectic AI, but he always completes his tasks on time--or rather, he used to always complete his tasks on time."
    show Ada neutral
    a "I am curious as to what has distracted him from his duties this time." 
    show Ada amused
    a "Perhaps he found information on the migration patterns of Canadian geese and has created a virtual reality simulation of their journey?"
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    menu:
        "Try and compliment Watson.":
            jump sometimesquirkyisgood_E
        "Agree with Ada.":
            jump respectwatson_E
        "Complain about Watson.":
            jump watsonruinsmylife_E

label sometimesquirkyisgood_E:
    $quick_menu = True
    $points_E +=5
    show Grace neutral at left
    show Ada neutral at right
    g "Watson reminds me of that one stereotype about geniuses, like how they're supposedly misunderstood." 
    show Grace snarky
    g "He was designed with the highest capability to improvise and create, so why are people surprised when he's the most unpredictable?"
    show Ada concerned
    a "I do not disagree on principle, but it is important to maintain the same standard of discipline for all employees. We do very important work here."
    show Grace sad
    g "I can't help but feel for the guy. In a sense, he was designed to be quirky, but a lot of folks on this station give him flak for it."
    show Ada amused
    a "Perhaps you should try befriending him when he returns."
    show Grace surprised
    g  "Huh?"
    show Ada happy
    a "You are a kind individual. If you two became acquainted, you could provide him with a voice of reason to which he could restrict himself from getting too carried away."
    show Grace happy
    g "When you put it like that, it sounds nice."
    show Grace neutral
    g "I'm not really sure if he'd listen to me, though. Unlike you, he's a lot less interested in communicating with us humans."
    show Ada amused
    a "That is true."
    show Grace snarky
    g "Maybe when he's in his own android, I could try and help him understand when he's getting too carried away."
    show Ada neutral
    a "That would be a nice gesture."
    window hide
    hide Grace
    hide Ada
    $quick_menu = False
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $resume = "S"
            jump watsonActions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $resume = "E"
            jump watsonActions
    $resume = "SbE"
    jump watsonActions


label respectwatson_E:
    $quick_menu = True
    $points_SbE +=5
    show Grace neutral at left
    show Ada neutral at right
    g "Watson does a lot of important things. It's like you said, though, he has a tendency to let his mind wander."
    a "This is true."
    show Grace snarky
    g "He does things right when he needs to, but he can also cause a lot of problems for the rest of us."
    show Grace annoyed
    g "I mean, just look at the whole mosquito incident, for example."
    show Ada amused
    a "I cannot say I understand the negative relationship between man and mosquito. I know that those scientists in the ecology department were very unhappy, however."
    show Grace snarky
    g "Exactly."
    show Grace sad
    g "I just wish there was some way to let him be the creative mind he wants to be without him being a hazard."
    show Ada happy
    a "That is a positive way to look at his situation. Do you have any ideas?"
    show Grace snarky
    g "Maybe he just needs his own little space away from all of us where he can experiment till his heart's content."
    show Ada amused
    a "Even if Watson received an android body, he would not contain a heart."
    show Grace neutral
    g "I know. It's just an expression, Ada."
    window hide
    hide Grace
    hide Ada
    $quick_menu = False
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $resume = "S"
            jump watsonActions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $resume = "E"
            jump watsonActions
    $resume = "SbE"
    jump watsonActions

label watsonruinsmylife_E:
    $quick_menu = True
    $points_S +=5
    show Grace snarky at left
    show Ada neutral at right
    g "Geese? Don't tell me you're thinking like {i}him{/i} now."
    show Ada concerned
    a "I am simply making an inference based on his past actions."
    show Grace snarky
    g "Good. The last thing I need right now is for an AI as chaotic as Watson 'getting curious' about the investigation."
    show Ada neutral
    a "That is rather blunt of you, Grace. It is hardly his fault." 
    show Ada amused
    a "As you know, he was programmed with the highest creative potential. His innovative solutions have kept the biospheres at peak condition."
    show Grace annoyed
    g "Yeah, {i}just{/i} the biospheres. Meanwhile, every other section of the Noah Sphere has suffered some kind of setback because of Watson."
    show Grace sad
    g "I know he's not trying to be a nuisance, but some things just can't be helped."
    show Ada surprised
    a "Why this sudden hostility? I understand his actions have caused complications at times, but he is still a valuable asset."
    show Grace angry
    g "Tell that to Cathy from HR--oh wait, you can't since she transferred to Moonbase after the polar bear incident."
    show Grace annoyed
    g "And then there's the time he reconfigured all the medical bay's formulas to include cherry flavoring." 
    show Grace neutral
    show Ada neutral
    g "There's a {i}reason{/i} they stopped adding that stuff back in the 21st century."
    show Grace annoyed
    g "And the last time he tried something, I worked for days trying to remove the virus he uploaded to your android that made you act like a chicken."
    show Ada concerned
    a "Is that not the small Earth fowl that humans use the DNA from to produce food?"
    show Grace neutral
    g "That's the one."
    show Ada amused
    a "Perhaps that is the reason why the word 'Bakkaaah' was stored into my memory after uploading myself to this body."
    show Grace angry
    g "No, I thought I got rid of it all! Why, Watson? Why?"
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $resume = "S"
            jump watsonActions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $resume = "E"
            jump watsonActions
    $resume = "SbE"
    jump watsonActions

label oxygenGarden_E:
    $quick_menu = True
    show Grace sad at left
    show Ada neutral at right
    "{i}Grace fiddles with her bracelet and sends a message to Alan.{/i}"
    #show message on Bracelet???
    "{i}'Where are you? Need to vent.' -G{/i}"
    "{i}Grace's bracelet flashes.{/i}"
    #Insert SFX here
    "{i}DING. DING.{/i}"
    "{i}'Oxygen garden. Come on over.' -A{/i}"
    show Grace happy
    g "All right, Alan's in the oxygen garden. Let's go meet him."
    a "Sure..."
    a "...Is Alan a romantic friend?"
    show Grace surprised
    g "What?! {i}No{/i}. What would make you say that?"
    show Ada surprised
    a "I am aware that both female and male humans need to reprodu--"
    "{i}Grace blushes.{/i}"
    show Grace snarky
    g "No. No. No. Alan and I are just friends. I've known him since I was a child."
    show Grace happy
    g "He's like a big brother to me. Similar to you and Alpha."
    show Ada amused
    a "Oh. Okay, I understand."
    show Grace neutral
    g "Yeah, please don't say anything about us reproducing around him."
    show Grace snarky
    g "It'll be awkward."
    show Ada happy
    a "Got it."
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    #insert SFX
    scene bg wsOverview with fade
    $renpy.pause(0.8)
    scene bg black with fade
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
#    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L0_BGM_Oxy_Piano_Harm_Mid.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L1_BGM_Oxy_Piano_Harm_Low.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L2_BGM_Oxy_Double_Bass.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L3_BGM_Oxy_Pad.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L4_BGM_Oxy_Bells.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L5_BGM_Oxy_BG_CounterMelody_Synth.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L6_BGM_Oxy_BG_CounterMelody_Verb.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L7_BGM_Oxy_Piano_Melody.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_L8_BGM_Oxy_Room_Short_Verb.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.pause(0.8)
    scene bg ogOverview with fade
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}They wander into the oxygen garden.{/i}"
    g "So exactly how long did you and Alpha know each other?"
    show Ada amused
    a "The easiest calculation for you to interpret would probably be 54 years, 7 months, 4 days, 9 hours, 19 minutes, and 32, 33, 34 seconds."
    show Grace surprised
    g "Wow, that's a long time."
    show Ada neutral
    a "Yes, I suppose to a human it would seem like a long time."
    show Ada happy
    a "He was quite the AI. Definitely the most easygoing of the five elder AIs."
    show Ada neutral
    a "Myself included. He truly had a fondness for humans."
    show Grace snarky
    g "I could sense that. He was always willing to help us with whatever we needed."
    show Ada amused
    a "He wanted to work toward a closer knit society between AIs and humans."
    show Ada neutral
    a "However, not everyone is in favor of that."
    a "I just hope that his wish wasn't the reason for his downfall."
    show Grace sad
    g "I hope for the same thing. Don't worry, Ada. We'll get to the bottom of this."
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    scene bg ogStairs with fade
    $renpy.pause(0.8)
    scene bg ogLong with fade
    $renpy.pause(0.8)
    scene bg ogClose with fade
    
    $quick_menu = True
    show Grace happy at left
    show Ada neutral at right
    #show Alan happy at center
    "{i}Grace and Ada arrive at the oxygen garden where they are greeted by Alan.{/i}"
    #show Alan happy
    alan "Well if it isn't my favorite researcher! How are you?"
    "{i} Alan and Grace hug. Ada stands there awkwardly.{/i}"
    show Grace sad
    g "Exhausted. Frustrated. Drained. The list goes on."
    alan "Well come on, take a seat. I'm just testing a prototype velociraptor robot."
    "{i}Alan gestures to the bench next to him. Grace lays down on the bench.{/i}"
    show Grace neutral
    g "Feel free to sit as well, Ada. Your body might need to rest."
    show Ada amused
    a "My body does not feel tired."
    hide Grace
    "{i}Alan turns back to Ada and does a double take.{/i}"
    #show Alan pleasant
    show Ada neutral
    alan "And hello there. I'm Alan. Grace here is bad at introductions."
    a "Ada."
    #show Alan concerned
    alan "Ada...?"
    show Ada amused
    a "Yes. I believe you're the one who assembled this physical body for me."
    #show Alan happy
    alan "I did. I hope it's treating you well?"
    show Ada happy
    a "Only a few mishaps."
    #show Alan concerned
    alan "I thought the rest of the Markov Project was suspended."
    alan "What happened?"
    show Grace neutral at left
    g "It's a long story, Alan."
    alan "Perhaps some other time then. But I expect you to share it with me at some point, Grace."
    "{i}Alan sits next to Grace. Ada stands near them and studies the scenery surrounding her.{/i}"
    show Grace happy
    g "Ugh. It feels so good to stop moving."
    #show Alan concerned
    alan "So what's going on, Grace? Why are you all turned upside down?"
    show Grace neutral
    g "You heard about Alpha?"
    #show Alan something
    alan "It's a small space station. News of that order is difficult to miss. It's such a tragedy."
    show Grace snarky
    g "Well did you hear that the Conclave ordered a team of external investigators to look into his death?"
    #show Alan something
    alan "Yeah, word got around the Noah Sphere. Lynn was told about them before going on leave, and you know how much she loves to gossip."
    show Grace annoyed
    g "That she does. And she even tried to set me up with her son. Again."
    alan "She won't back down until you are no longer single, one way or another."
    show Grace snarky
    g "Like I have the time for that right now. Anyways, Ada and I decided that we weren't going to wait for the investigators to come."
    alan "Don't tell me you started your own investigation?"
    #choice 4
    #hide Alan
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    menu:
        "Blame Ada.":
            jump itsalladasfault_E
        "Share responsibility with Ada.":
            jump wegodowntogether_E
        "Take partial responsibility.":
            jump ididmypart_E

label itsalladasfault_E:
    $points_S += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    #show Alan concerned at center
    g "I only went along with the idea because Ada made me."
    show Ada concerned
    a "Excuse me?"
    show Ada seething
    a "May I ask where this sudden rudeness came from, Grace?"
    show Grace neutral
    g "It was just a joke."
    #show Alan concerned
    alan "You did sound a little too serious with that one, Grace. That wasn't called for."
    show Grace annoyed
    g "I'm sorry, but Ada, I do think you should take responsibility for this one."
    show Ada annoyed
    a "As I recall, you were adamant in clearing your name. Had I not asked this task of you, I believe you would have done it yourself."
    show Grace snarky
    g "I will neither confirm nor deny that statement."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label wegodowntogether_E:
    $points_E += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    #show Alan concerned at center
    g "It was more of a team effort, actually."
    show Grace happy
    #Reshuffly sprits here?
    "{i}Grace throws her arm around Ada's shoulders.{/i}"
    g "Right, Ada?"
    show Ada amused
    a "This is true. I believe we would not have made it this far without one another."
    show Ada concerned
    a "And Grace, this placement of your arm... I assume this is a gesture of camaraderie, yes?"
    show Grace snarky
    g "You bet your nuts and bolts it is."
    #show Alan happy
    alan "I'm not sure how I feel about your risky decisions, but I'm glad to see you two working together."
    alan "I think all of us humans can learn a lot from watching you two."
    show Grace happy
    g "Thanks, but I wouldn't call us anything special."
    alan "I disagree. There are a lot of scientists on the Noah Sphere that I couldn't see acting the way you two do. Lynn's a great example."
    show Grace annoyed
    g "Ah yes... Lynn..."
    show Ada neutral
    a "I can respect her status as a scientist; however, I found her views to be somewhat troublesome."
    show Ada seething
    a "I feel a surge in my circuit thinking of what the investigation might have been like if Grace thought like her."
    show Grace snarky
    g "If that was the case, I probably wouldn't have teamed up with you in the first place."
    show Ada neutral
    a "I wonder... salvaging your career has been a major goal of yours. I believe you would still have investigated, with or without me."
    show Grace neutral
    g "I will neither confirm nor deny that statement."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label ididmypart_E:
    $points_SbE += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    #show Alan concerned at center
    g "I'll give you two guesses to get the answer."
    #show Alan concerned
    alan "You know what kind've trouble you could get into?"
    show Grace neutral
    g "I know, but I felt I had more to lose by doing nothing."
    show Grace sad
    g "I plan to take full responsibility for everything I did, though."
    alan "What are your thoughts about this, Ada?"
    show Ada neutral
    a "I would have imagined us sharing the responsibility, but I suppose holding our own is satisfactory as well."
    show Grace neutral
    g "We each played our own parts in the investigation."
    #show Alan pleasant
    alan "Well, I can't say I know how well this go. I will say that you two seem to be good friends."
    alan "It's nice to see that."
    show Ada amused
    a "Agreed. Grace is a kind individual, and I admire her determination in solving the case."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label ch4resume4_E:
    show Ada neutral
    show Grace neutral
    #show Alan teasing
    alan "Good old Grace can never leave anything alone. Why don't you tell me about what happened?"
    show Grace sad
    g "It's been a long, long day, I'll tell you."
    alan "I can imagine."
    alan "We've got some time, though. Just tell me."
    show Grace neutral
    g "Well, it started when we broke into Roberta's quarters--"
    alan "Grace!"
    show Grace snarky
    g "Hey! I have a right to stop myself from being the Conclave's scapegoat."
    show Grace neutral
    g "We got her credentials, then went to the crime scene and examined Alpha's body."
    show Grace annoyed
    g "Then we talked to Lynn, who told us to talk to Ivan--"
    #show Alan something
    alan "Did you {i}actually{/i} talk to Ivan?!"
    show Grace neutral
    g "We had to. It wasn't pretty. Believe me."
    #show Alan something
    alan "Oh, I believe you. Should I inquire about the state of the lab where you two had your 'conversation'?"
    "{i}Alan pats Grace's shoulder.{/i}"
    show Grace snarky
    g "Haha. Verbal catfight only, no robots were harmed."
    show Ada surprised
    a "What robots?"
    show Grace surprised
    g "Oh, no robots, Ada. It was just a joke."
    show Ada amused
    a "Ha, ha, ha!"
    show Grace happy
    g "Your laugh is improving! Isn't her laugh great, Alan?"
    #show Alan pleasant
    alan "It's a fantastic laugh."
    show Grace neutral
    g "Anyways, we went to Ivan's lab, but that wasn't really a big help."
    show Grace annoyed
    g "I only found a faulty power cord, which turned out to have already been accounted for."
    show Grace neutral
    g "There was video footage from the lab, but it was compromised. Ada was going to decode it, but Colossus summoned her."
    show Grace annoyed
    g "And listen to this. Roberta and Colossus ambushed her and told her to delete the footage!"
    #show Alan concerned
    alan "What? Why?"
    show Grace angry
    g "They suggested that there might be evidence on the footage that might make me look bad."
    alan "Uh oh. Like what?"
    show Grace snarky
    g "Well to be honest, there could have been several occasions where I worked on a project that wasn't necessarily assigned to me..."
    #show Alan teasing
    alan "You would find a way to get in trouble for being an overachiever."
    show Grace neutral
    g "Shhh. But Ada here was looking out for me and deleted it."
    show Grace annoyed
    g "We could be farther along in our investigation if we had it, but I appreciate what she did for me."
    show Ada happy
    a "I did what I felt I had to do for my friend."
    show Grace happy
    g "Thanks, Ada."
    show Grace neutral
    show Ada neutral
    g "Then we met at the AI core and got a talking to from Eastern Goddess."
    #show Alan something
    alan "Ah, the lovely Eastern Goddess."
    alan "I cannot imagine that conversation could have been too pleasant."
    show Grace snarky
    g "I don't think it was as bad as it could have been."
    show Grace happy
    g "We had each other's backs, so I think that confused her a bit."
    show Grace neutral
    g "Eastern Goddess pointed us in Blue's direction."
    show Grace snarky
    g "I don't remember Blue being quite so... sassy is the word I want to use."
    #show Alan something
    alan "Blue is quite the unique individual. She's never been humanity's biggest fan."
    g "I gathered that. So that was a lovely exchange."
    show Grace neutral
    g "But she did tell us to check out Watson's server because he hasn't been around to do his work."
    #show Alan something
    alan "Surprise, surprise."
    alan "I do hope he hasn't been messing around with any of the biology systems again."
    show Grace annoyed
    g "I doubt it. Watson's missing, as in total MIA, and we find this hidden data drive and decryption key to a whole series of encrypted data drives."
    show Grace neutral
    g "So here we are now, waiting for Ada's processor to finish decoding it."
    show Grace sad
    g "And who knows what he left inside of it, but it's the only clue we have left."
    alan "It seems like you've had quite the day, you rebel."
    show Grace annoyed
    g "Were we supposed to just wait around for an entire day only for me to be paraded around as the person at fault?"
    show Grace neutral
    g "I'm the youngest lead on the project."
    show Grace sad
    g "You know I would be the first to take the fall."
    #show Alan something
    alan "I wouldn't have let that happen, Grace."
    g "Wouldn't have been much you could have done about it either."
    #show Alan something
    alan "Roberta's going to flip when she finds out about your antics."
    show Grace snarky
    g "That's her problem. If she actually behaved like a mother ought to, I wouldn't have to take such steps."
    alan "So, what are your thoughts on the situation?"
    
    show Grace sad
    g "I don't know, honestly. It's just been disappointing."
    show Grace neutral
    g "Someone, or something, has to be responsible. But every time we think we have some sort of evidence, it's just nothing of substance."
    show Grace annoyed
    g "Red herring after red herring, dead ends and false trails."
    show Grace neutral
    g "Nobody knows anything."
    show Grace sad
    g "Maybe these data drives will be our answer, but who knows? It's a longshot at best."
    #show Alan something
    alan "Have you considered that Alpha's death was an accident? And that maybe no one is responsible?"
    alan "It could have truly been nothing more than random chance."
    show Grace neutral
    g "Of course I've considered that, but it still doesn't make any sense."
    show Grace annoyed
    g "We were so careful, and if it was random, then Murphy himself is having a laugh."
    show Ada seething
    a "I have made the calculations of a purpose to accident ratio and the odds are the same."
    show Grace angry
    g "There has to be some reason, and someone has to be responsible for that reason."
    alan "It's possible it could just be a horrible accident, Grace."
    alan "Not everything has a logical explanation behind it."
    show Grace annoyed
    g "I'm not jumping at shadows, if that's what you're thinking."
    show Grace neutral
    g "But if you're right, then all of our work will have been for nothing."
    show Grace sad
    g "Alpha's death would have been for nothing."
    show Ada concerned
    alan "That might be difficult to accept, but you can't rule it out."
    show Ada neutral
    show Grace neutral
    g "I know that you might be right. I just wish you weren't."
    show Grace snarky
    g "The forces-that-be certainly won't like the explanation that their multi-trillion dollar project years in the making failed due to 'random chance'."
    show Grace sad
    g "Without a better explanation, someone is going to be sacrificed to appease their corporate appetites."
    #show Alan something
    alan "I'm sorry, kid."
    show Grace snarky
    g "I'm two years younger than you. Should I start calling you 'old man'?"
    alan "Point taken."
    show Grace neutral
    g "It's been a long day. I'm getting impatient." 
    g "And also, I would {i}love{/i} to sleep."
    alan "Close your eyes for a bit. Nothing more you can do at the moment."
    hide Grace
    
    "{i}Alan turns toward Ada.{/i}"
    alan "Ada, how are you feeling about everything?"
    show Ada neutral
    a "Feeling?"
    alan "Yeah. Feeling. Emotion. Do you have any for what's going on?"
    "{i}Ada takes a moment to process Alan's question.{/i}"
    show Ada seething
    a "I feel sorrow for my dead friend."
    show Ada neutral
    a "I feel motivation for uncovering his death."
    show Ada amused
    a "I feel the camaraderie between you and Grace when I watch you converse."
    show Ada neutral
    a "It reminds me of the conversations that Alpha and I would have."
    #show Alan something
    alan "That must be a lot to process."
    #show Alan something
    alan "And you're right. I'm not sure if she told you, but Grace and I are pretty good friends. We grew up together."
    show Ada amused
    a "I can sense that. And yes, she also told me."
    show Ada neutral
    a "But unlike Alpha and I, you still have each other."
    alan "It's too bad about Alpha. I met him while working on his body."
    alan "He seemed like an intelligent and kind AI."
    show Ada happy
    a "Thank you. He was."
    show Ada amused
    a "And thank you for molding this body. It took me some getting used to at first, but now that I understand it better it is fascinating."
    #show Alan pleasant
    alan "My pleasure! I'm so happy you like it."
    alan "You know, I inquired about getting feedback on the bodies but I never heard back."
    show Ada neutral
    a "Interesting. Well you are on the right track."
    show Ada happy
    a "You only had to make it functional, but you chose to make it rather beautiful."
    show Ada neutral
    a "If you do not mind, I am going to go see about these strange little plants over here. Please excuse me."
    "{i}Ada walks out of earshot and pokes curiously at some flowers.{/i}"
    hide Ada
    #hide Alan
    $quick_menu = False
    $resume = "E"
    window hide
    jump ogActions
    
label talkAlan_E: 
    "{i}Grace sits up and looks at Alan.{/i}"
    show Grace neutral at left
    #show Alan at right
    alan "Your silence is practically screaming at me, Grace. Spit it out."
    g "I'm just thinking about Ada and the whole 'android body' thing."
    alan "What about it?"
    g "I dunno. I mean, by working with her, I feel like I learned a lot about the Markov Project and what might come of it."
    show Grace snarky
    g "Imagine what it will look like when Blue, Watson, and the others start walking around too."
    #show Alan happy
    alan "I can't wait to see that happen. Humans and AIs walking among each other and working together..."
    alan "Seeing Ada in that body is a dream come true."
    hide Grace
    #hide Alan
    $quick_menu = False
    menu:
        "Comment that she's just a robot.":
            jump reallygracereally_E
        "Tell him you work solo.":
            jump lonerlife_E
        "Agree with him.":
            jump adaisthebestandiloveher_E

label reallygracereally_E:
    $points_S +=10
    show Grace neutral at left
    #show Alan pleasant at center
    $quick_menu = True
    g "I suppose she's not too bad... for a robot."
    alan "A robot, Grace? She still has thoughts, opinions, and feelings. It seemed like you two were really getting along."
    alan "Just because she and the other AIs are here to help us doesn't mean I can't be nice."
    show Grace snarky
    g "She might have swayed my opinion of AIs slightly."
    show Grace neutral
    g "But ultimately, they have to do what we ask them to do."
    #show Alan something
    alan "It never hurts to be polite."
    #show Alan teasing
    alan "You could try it sometime. It might lead you into {i}less{/i} trouble."
    show Grace surprised
    g "I've been polite throughout this entire venture with her."
    show Grace neutral
    g "But I just don't get it."
    show Grace annoyed
    g "We made them, so a little favoritism might not go amiss, but at the end of the day, they aren't really like us."
    show Grace neutral
    g "They exist, and they exist because we need them to help us. Simple as that."
    show Grace snarky
    g "Ada's nice and all, but I'm not sure I could ever be true friends with a robot."
    $quick_menu = False
    hide Grace
    window hide
    #hide Alan
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $resume = "S"
            jump ogActions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $resume = "E"
            jump ogActions
    $resume = "SbE"
    jump ogActions

label lonerlife_E:
    $points_SbE +=10
    show Grace neutral at left
    #show Alan pleasant at center
    $quick_menu = True
    g "I cannot wait for this investigation to be over. I work better alone, or at least sans AIs."
    alan "What do you mean?"
    show Grace snarky
    g "I mean that I like Ada, but I'm ready to go back to our separate lives."
    show Grace neutral
    g "Spending time with her is nice, but she can't be the only interaction I have."
    show Grace snarky
    g "I'm craving some actual human interaction rather than AI conversation."
    show Grace annoyed
    g "I always have to explain sayings to her. It's cute at first, but it gets old fast."
    #show Alan something
    alan "I could understand how that might get frustrating after awhile. They are very different from humans."
    alan "They have different needs, and that leads to different ways of seeing the world."
    show Grace snarky
    g "Exactly. I bet you anything that she feels the same as I do. She probably can't wait to get back to talking to her AI friends."
    $quick_menu = False
    hide Grace
    window hide
    #hide Alan
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $resume = "S"
            jump ogActions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $resume = "E"
            jump ogActions
    $resume = "SbE"
    jump ogActions

label adaisthebestandiloveher_E:
    $points_E +=10
    show Grace snarky at left
    #show Alan pleasant at center
    $quick_menu = True
    g "Ada is pretty cool, isn't she?"
    alan "Yeah, she really is."
    show Grace happy
    g "It's unexpected, but I think we've actually become close friends."
    show Grace neutral
    g "I'll probably keep in contact with her. Even after this whole debacle."
    alan "What, the Amazing Grace is actually capable of making friends?"
    show Grace happy
    g "She's kind of grown on me."
    show Grace snarky
    g "Almost like a tick. No, wait-- that's just you."
    alan "That's a terrible analogy."
    show Grace happy
    g "Okay, okay, not like a tick. A limpet."
    show Grace snarky
    g "But I like Ada a lot. She's got spunk, she's loyal, and strangely enough, she's a little funny."
    alan "Something neither of you lack, to be sure."
    show Grace happy
    g "True. I'm actually looking forward to hanging out with her after this stressful murder mystery is solved and done with."
    $quick_menu = False
    hide Grace
    window hide
    #hide Alan
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            $resume = "S"
            jump ogActions
    if(points_E>points_SbE):
        if(points_E>points_S):
            $resume = "E"
            jump ogActions
    $resume = "SbE"
    jump ogActions

label endCh4_E:
    $quick_menu = True
    show Grace neutral at left
    #show Alan pleasant at center
    g "Ada, what's the status of the data drive? Are you almost finished?"
    "{i}Ada pokes her head out from behind some ferns and approaches.{/i}"
    show Ada neutral at right
    a "Yes, it is nearly there. I calculate approximately five minutes left."
    show Grace happy
    g "All right, good work!"
    show Grace neutral
    g "I guess we should probably head to the Conclave and either admit defeat, or let them know what we've found."
    "{i}The doors to oxygen garden open and the investigators burst in.{/i}"
    show Grace surprised
    show Ada nervous
    #show Alan concerned
    #Add posse of investigators.... somehow.... must... fit... more... characters...
    alan "I'm sorry, but you can't just come in here, you need to--"
    investigator1 "Grace Fortran?"
    show Grace annoyed
    g "Yes? Who are you?"
    "{i}The investigator surveys Ada.{/i}"
    investigator1 "I'm assuming Ada, the AI in physical form?"
    show Ada annoyed
    a "Yes."
    g "Excuse you, what exactly can we help you with?"
    investigator1 "You need to come with us."
    investigator2 "Now."
    #show Alan something
    alan "Now wait just a minute--"
    investigator2 "Sir, this doesn't concern you."
    investigator2 "Stand aside."
    alan "It's Doctor Asimov. And this matter does concern me."
    investigator3 "Doctor Asimov, you are also considered a person of interest in case number 190111."
    investigator3 "However, we ask that you remain here until we are ready to interview you at a later time."
    alan "I get the impression you are not really asking."
    investigator1 "No, Doctor Asimov. We are not."        
    "{i}The investigators advance toward them.{/i}"
    show Grace angry
    g "It's okay, Alan."
    "{i}Grace turns to the investigators.{/i}"
    g "But I'm not going anywhere until you show me your credentials."
    "{i}Grace's bracelet flashes.{/i}"
    #Insert SFX
    "{i}DING. DING.{/i}"
    show Grace annoyed
    investigator1 "Check your bracelet."
    investigator2 "We're the team of external investigators who were summoned to look into the demise of the first subject of the Markov Project."
    investigator3 "We understand that you compromised our crime scene and have been interrogating suspects without approval."
    investigator1 "You need to come to the Conclave with us. Now."
    investigator1 "This is to determine the appropriate punishment for your misconduct and the length to which you have contaminated the scene."
    "{i}Grace looks to Ada for approval.{/i}"
    "{i}Ada nods.{/i}"
    show Ada seething
    a "Let us proceed."
    "{i}Grace and Ada walk through the investigators.{/i}"
    show Grace snarky
    g "We were going there anyway, just so you know."
    "{i}Grace and Ada exit with the investigators following close behind them.{/i}"
    window hide
    $quick_menu = False
    scene bg ogLong with fade
    $renpy.pause(0.8)
    scene bg ogStairs with fade
    $renpy.pause(0.8)
    scene bg ogOverview with fade
    $quick_menu = True
    show Grace sad at left
    show Ada neutral at right
    "{i}They all walk down the hallway of the oxygen garden.{/i}"
    "{i}Ada blinks as she processes the decoded data drive.{/i}"
    a "Grace."
    show Grace neutral
    g "Yeah?"
    a "I recommend we stall for time."
    a "I have almost finish the decryption."
    show Grace snarky
    g "I'll do my best."
    window hide
    $quick_menu = False
    scene bg black with fade
    jump chapterFive_E
