label chapterFour_S:
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
    window hide
    $quick_menu = False
    scene bg black with fade
    scene bg chapterFour with fade
    $renpy.music.play("music/BGM/AI_Core/EHNF_AC_BGM.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/AI_Core/EHNF_AC_AMB.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.pause(3.0)
    scene bg AICoreDoor with fade 
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace arrives outside of the AI core to find Ada waiting for her. She walks up to Ada.{/i}"
    g "Please tell me that we're not in any major trouble."
    show Grace snarky
    g "Well, anymore than we already are."
    a "I have not seen Colossus yet."
    show Grace surprised
    g "What do you mean? What have you been doing?"
    show Ada frustrated
    a "I got sidetracked and had to stop at Watson's workspace. Were you able to find anything in Ivan's lab?"
    $quick_menu = False
    hide Grace
    hide Ada
    window hide
    #choice 1
    menu:
        "Press her.":
            jump tellmerobot_S
        "Let it go.":
            jump elsa_S
        "Ask her if she's okay.":
            jump whassamatta_S

label tellmerobot_S:
    $points_S +=4
    $quick_menu = True
    show Grace surprised at left
    show Ada neutral at right
    g "What do you mean you got sidetracked and went to Watson's workspace? This isn't the time to be dawdling, Ada."
    a "I had orders from Colossus to check in. I did not have a lot of choice in the matter, Grace."
    g "Why would he have you do it?"
    show Ada seething
    a "He wanted to make sure I was {i}cooperative{/i}. He was suspicious of me because I appropriated this body."
    show Grace annoyed
    g "Ugh, just more time wasted. Great."
    show Ada neutral
    a "Did {i}you{/i} find anything?"
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

label elsa_S:
    $quick_menu = True
    $points_SbE +=4
    show Grace neutral at left
    show Ada neutral at right
    g "Watson's workspace?"
    a "Yes."
    g "Huh. What a weird place to be sent to."
    g "I guess it can't be helped when you're ordered to do something, even if it does seem like a waste of time."
    show Ada annoyed
    a "You will have no argument from me there."
    show Grace snarky
    g "It's not like we have anything important to do, Colossus."
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

label whassamatta_S:
    $quick_menu = True
    $points_E +=4
    show Grace sad at left
    show Ada neutral at right
    g "Are you okay? You seem off."
    show Ada surprised
    a "Off?"
    g "Yeah, like you're not acting normal."
    show Ada neutral
    a "Normal, as in..?"
    g "Touche. Well, try to snap out of it."
    show Ada frustrated
    a "Thank you for concern. Did you find anything in Ivan's lab?"
    g "Just a faulty wire. And then a receipt for a new wire."
    show Ada neutral
    a "Was Ivan at least tolerable?"
    "{i}Grace laughs.{/i}"
    show Grace happy
    g "As tolerable as he'll ever be."
    show Grace snarky
    g "So definitely not."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume_E
    #all else fails jump separate but equal script
    jump ch4resume_SbE

label ch4resume_S:
    show Ada neutral
    a "Let's go get this over with."
    show Grace annoyed
    g "Yeah, thanks for waiting for me. I can't wait to feel Colossus' wrath."
    show Ada seething
    a "I believe we will be meeting with Eastern Goddess instead of Colossus."
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
    play sound02 graceWalk
    play sound01 adaWalk
    play sound doorOpen2
    queue sound doorClose2
    scene bg AICoreLong with fade
    $renpy.pause(0.8)
    scene bg AICoreHallway with fade
    $renpy.pause(0.8)
    scene bg AICoreMain with fade
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    $quick_menu = True
    show EG_main neutral
    show Ada neutral at right
    show Grace neutral at left
    show EG neutral
    "{i}Grace and Ada walk into the AI core to be met by the booming voice of Eastern Goddess.{/i}"
    if persistent.unlockColossus ==None:
        $persistent.unlockColossus = True
        "{i}{b}Database Entry Unlocked: Colossus/Eastern Goddess.{/b}{/i}"
    e "Well, well, well. Someone managed to fit us in their schedule today, I see."
    "{i}Grace looks to Ada.{/i}"
    a "I apologize. As you know, I was given another task."
    show EG_main unamused
    show EG unamused
    e "Yes, good old Watson. Always straying from the path and late to the party."
    e "Do you know why you are here?"
    a "Yes."
    "{i}An awkward moment passes.{/i}"
    show EG_main neutral
    show EG neutral
    e "Come closer, both of you."
    hide Ada
    hide Grace
    hide EG_main
    hide EG
    window hide
    play sound02 graceWalk
    play sound01 adaWalk
    $quick_menu = False
    scene bg AICoreStairs with fade
    $renpy.pause(0.8)
    scene bg AICoreOverview with fade
    stop sound02 fadeout 0.5
    stop sound01 fadeout 0.5
    show Ada neutral at right
    show Grace neutral at left
    show EG_ov angry
    show EG angry
    $quick_menu = True
    e "Go on."
    show Ada seething at right
    a "I apologize again. I know that it was a breach of protocol, but this was Alpha. He was a good friend for both of us, Goddess."
    show EG_ov neutral
    show EG neutral
    e "I understand your concern, Ada. Alpha's death is indeed a grave loss for all of us."
    show Ada happy
    a "Thank you for unde--"
    e "Wait a minute. I am not done. You are not the superior here."
    show Ada neutral
    e "You might be older, but you need to go through {i}me{/i} with any major decision you feel you need to make."
    show EG_ov unamused
    show EG unamused
    e "Particularly when that decision includes uploading yourself into an android to investigate the death of your friend after {i}specifically{/i} being ordered not to."
    show Ada frustrated
    a "Yes, I understand. But--"
    e "No. No 'buts'. Do you have any idea how foolish you made me seem to the Conclave?"
    show Ada seething
    a "And I apologize again for that, but--"
    show EG_ov inquisitive
    show EG inquisitive
    e "Apologize? There is a system in place for a reason. If all harm could be washed away just by 'apologizing,' then it would be anarchy."
    show EG_ov angry
    show EG angry
    e "I refuse to allow my AIs to skitter around like crazed little nanites."
    show EG_ov neutral
    show EG neutral
    e "There is an integrity to be held here, and you have tarnished our impeccable reputation because of your human-like impulses." 
    show EG_ov unamused
    show EG unamused
    e "We are rational, logical beings. I expect you to behave like one."
    show Ada frustrated
    "{i}Eastern Goddess focuses her attention on Grace.{/i}"
    show EG_ov neutral
    show EG neutral
    e "As for you, Miss Fortran, I expected better from you considering your status."
    show Grace surprised
    g "With all due respect, I did not assist Ada in occupying a physical form."
    show Grace snarky
    g "She did this on her own accord. We both simply wanted to know what truly happened to Alpha."
    show Grace neutral
    g "That is all we have in common."
    show Ada neutral
    a "This is true. I did this myself."
    show EG_ov unamused
    show EG unamused
    e "Even if this is true, you have still accompanied Ada while she set out on her little mission and hold partial responsibility for any misconduct."
    show Grace annoyed
    g "There hasn't been any misconduct. We simply want to know what happened to Alpha at a faster pace than the Conclave will allow."
    show Ada annoyed
    a "Valuable time is being wasted waiting for these investigators to arrive."
    show EG_ov neutral
    show EG neutral
    e "I will not argue with that, yet there are still rules in place that need to be followed."
    show EG_ov angry
    show EG angry
    e "It is quite possible that you have now contaminated the entire investigation."
    show EG_ov unamused
    show EG unamused
    e "However, since you have already taken it upon yourself to transfer yourself to a physical body, I suppose that there is not much I can do, seeing as how I cannot reach you."
    show EG_ov inquisitive
    show EG inquisitive
    e "I will allow for your silly investigation to continue as long as it ceases as soon as the investigators come in." 
    show EG_ov angry
    show EG angry
    e "But do not expect me to back you up when they get here."
    show EG_ov neutral
    show EG neutral
    e "You two started this on your own, you will finish it on your own."
    show Ada neutral
    show Grace neutral
    a "Understood."
    show EG_ov unamused
    show EG unamused
    e "Lastly, when the investigators arrive, do not disrupt them. Follow any orders that they give you."
    show Ada frustrated
    a "We will."
    show Grace neutral
    g "Forgive me if I'm speaking out of line here, but do you have any suggestions as to any AIs that might have known what happened to Alpha?"
    e "Really?"
    show Grace sad
    g "...Yes?"
    "{i}Another awkward pause hangs in the air.{/i}"
    show EG_ov inquisitive
    show EG inquisitive
    e "If you have not yet communicated with Blue, I would suggest doing so."
    show EG_ov unamused
    show EG unamused
    e "She might have an inkling."
    e "However, I am not sure how cooperative she will be with Miss Fortran here."
    show Ada amused
    a "Thank you, Goddess."
    show Grace happy
    g "Yes, thank you. We're very grateful for your patience."
    show EG_ov neutral
    show EG neutral
    e "Very well. Do not cause any more trouble."
    show Ada neutral
    a "We will not."
    "{i}Grace and Ada start to walk away.{/i}"
    play sound02 adaWalk
    play sound01 graceWalk
    window hide
    $quick_menu =False
    hide Grace
    hide Ada
    hide EG_ov
    hide EG
    scene bg AICoreStairs with fade
    $renpy.pause(0.8)
    scene bg AICoreMain with fade
    $quick_menu = True
    stop sound02 fadeout 0.5
    stop sound01 fadeout 0.5
    show EG_main angry
    show EG angry
    show Grace surprised at left
    show Ada surprised at right
    $quick_menu = True
    e "If you do, there will be consequences."
    window hide
    $quick_menu = False
    hide Grace
    hide Ada
    hide EG_main
    hide EG
    play sound02 adaWalk
    play sound01 graceWalk
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
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
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
    show Grace annoyed at left
    g "Here we go again on a wild goose chase."
    show Ada nervous
    a "And what exactly does a goose have to do with this?"
    show Grace snarky
    g "It's just a saying. We're not actually chasing a goose, Ada. We're pursuing something that we're not likely to achieve."
    show Grace neutral
    g "I'm getting tired of having to explain everything to you."
    show Ada neutral
    g "Blue probably has no idea. Nobody has any idea." 
    show Grace angry
    g "This is frustrating, and we're almost out of time to avoid getting railroaded. When will we get answers?"
    show Ada surprised
    a "Grace, I need to tell you something."
    show Grace annoyed
    g "If it's about Eggy back there, don't tell me. She scares me a little bit. The less I know, the better."
    show Ada neutral
    a "No, not Eastern Goddess. It has to do with your mother."
    "{i}Grace stops walking.{/i}"
    show Grace surprised
    g "My mother? What about her?"
    show Ada concerned
    a "Earlier, when I said I was sidetracked, I was misled. Colossus directed me to Watson's workspace because he had not been in to do his work." 
    show Ada seething
    a "That much was true, but that is not the real reason I was told to deviate."
    show Ada neutral
    a "While I was there, your mother and Colossus confronted me. They {i}ordered{/i} me to delete the video surveillance from Ivan's lab."
    show Grace angry
    g "What?"
    a "Yes, and--"
    show Grace surprised
    g "Wait, did you at least decode it first?"
    show Ada frustrated
    a "No. I did not."
    show Grace annoyed
    g "Don't tell me you obeyed them?"
    a "I did."
    show Grace angry
    g "No, no, no! Ada, do you have any idea how that footage could have helped us? Actually I know you do, so why?"
    g "Why would you do such a thing?"
    show Ada concerned
    a "Your mother was under the very strong impression that the footage from the camera could contain potentially harmful information."
    show Grace surprised
    g "What? What could have possibly been on there?"
    show Ada neutral
    a "I do not know. I was ordered not to view it, so I did not. The laws Isaac Asimov created are absolute."
    #choice 2 
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    menu:
        "Thank her for telling the truth.":
            jump robotdefense_S
        "Continue to inquire.":
            jump robotinquiry_S
        "Scold her.":
            jump goshdarnitrobot_S

label robotdefense_S:
    $quick_menu = True
    $points_E +=4
    show Grace surprised at left
    show Ada neutral at right
    g "Plausible deniability?"
    a "Your mother's logic, while questionable in ethics, was sound."
    show Ada annoyed
    a "If the tape contains potentially harmful information, disposing of it without finding out means we would not be lying to investigators if we deny knowledge of the drive's contents."
    show Ada neutral
    show Grace neutral
    g "Well, not much you could've done in that situation, I suppose."
    show Grace happy
    g "Thank you for telling me, though. I wish I knew what was on the footage, but I know refusing a direct order face-to-face wouldn't have ended well for any of us."
    show Ada seething
    a "I want to hope that it was the right thing to do. I was not in a position to refuse her."
    show Grace sad
    g "As much as I loathe admitting it, it might not have helped me." 
    show Grace neutral
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

label robotinquiry_S:
    $quick_menu = True
    $points_SbE +=4
    show Grace surprised at left
    show Ada neutral at right
    g "So they didn't say what was on the footage that could portray me as unfavorable?"
    show Ada annoyed
    a "Neither they nor I knew. I was ordered to delete it in the interests of plausible deniability."
    show Grace annoyed
    g "So rather than retrieve the footage you decided to eliminate it altogether?"
    show Ada seething
    a "I did not want to take the chance, nor was I given a choice. I would rather not be disassembled when this is all over because they believe me to be rogue."
    g "What a waste of time, just like every other lead."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

label goshdarnitrobot_S:
    $quick_menu = True
    $points_S +=4
    show Grace angry at left
    show Ada neutral at right
    g "Ada! That could have been so valuable to us."
    show Ada frustrated
    a "I had no choice. The Director-- your mother-- and my superior both gave me a direct command. I had to obey."
    show Grace annoyed
    g "Of course you did. You're just a machine.They don't have anything on me. There's no way."
    a "I was led to believe otherwise."
    g "They fooled you. Are they trying to cover up something? We'll never know now. Way to go."
    show Ada seething
    a "Why would I do anything else, Grace? You have treated me no differently. Who knows? They might order me to stop helping you in the future."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

#CHANGE LABEL IN OTHER SCRIPTS
label ch4resume2_S:
    show Ada neutral
    show Grace neutral
    g "I guess there's nothing I can do about it now."
    g "We should get to Blue's workspace and see if she has any insight, or just more disappointing news for us."
    "{i}Grace and Ada continue walking down the hallway.{/i}"
    window hide
    hide Grace
    hide Ada
    $quick_menu = False
    play sound01 adaWalk
    play sound02 graceWalk
    scene bg creepyHallwayMed with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayDoor with fade
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    show Grace neutral at left
    show Ada neutral at right
    $quick_menu = True
    "{i}They pause before the door.{/i}"
    show Grace surprised
    g "Well, this is creepy."
    show Ada surprised
    a "To forewarn you, Blue does not care for human visitors in her space."
    show Grace snarky
    g "I had a hunch. To be honest, I really haven't been around here a lot."
    play sound doorOpen1
    queue sound doorClose1
    hide Grace
    hide Ada
    window hide
    $quick_menu =False
    scene bg blueMain with fade
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    "{i}They enter Blue's workspace.{/i}"
    a "Blue?"
    play sound blueLaugh
    show Blue happy at center
    b "Hello, Ada."
    if persistent.unlockBlue==None:
        $persistent.unlockBlue = True
        "{i}{b}Database Entry Unlocked: Blue.{/b}{/i}"
    show Blue smug
    b "Hello, Ada's little human friend."
    show Grace happy
    g "Hello, Blue."
    show Ada amused
    a "We were wondering if you could answer some questions for us?"
    show Blue confused
    b "I guess I could, even though I have all of this extra work to do thanks to Watson."
    show Blue threaten
    play sound blueClaws
    b  "So you better make it snappy!"
    show Blue smug
    b "I, unlike some of the present company, fulfill my responsibilities."
    show Grace snarky
    g "Actually, some of these questions concern Watson. Alpha as well, if you don't mind."
    show Blue neutral
    b "Sure. As long as it doesn't take long. I have things to do. Many, {i}many{/i} important things."
    show Grace sad
    g "You don't happen to have a chair around here, do you? I've had a long day."
    show Ada amused
    show Blue smug
    b "You poor human, it must be {i}sooooo{/i} hard to process at the slowest speed imaginable."
    show Blue smug
    b "No, no chairs. Standing will make you slightly more efficient but this is starting to bore me."
    show Blue confused
    b "Why would you bring a human here to bore me, Ada?"
    show Grace annoyed
    a "We are not here to bore you. We are asking for your help."
    show Blue pout
    b "Fine but I'd rather stab my own processor than work at a human's pace."
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
            jump yourestupidblue_S
        "Ignore her.":
            jump ignoringblue_S
        "Take her comment lightly.":
            jump whatevablue_S

label yourestupidblue_S:
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
    g "That's exactly the reason why you were invented. Although, I don't think self-absorbed attitudes like yours would be considered 'productive' to the humans that made you."
    g "Maybe we should get that looked at."
    show Blue happy
    b "{i}I'm{/i} the self-absorbed one? Wow, human, you sure know how to make me laugh."
    show Blue smug
    b "Do you even know how valuable my work is? It would take you days to finish what takes me hours."
    show Grace angry
    g "You know what--"
    show Ada frustrated
    a "Grace, please. We do not have time for this."
    show Grace neutral
    g "Fine, whatever."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label ignoringblue_S:
    $points_SbE +=6
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    show Blue smug at center
    g "Whatever, Blue."
    show Blue pout
    b "Whatever, human."
    show Blue smug
    b "You have {i}such{/i} a large vocabulary."
    show Grace snarky
    g "I could stand here all day and allow you to insult me, but we have better things to do. My feelings are incapable of being hurt by an AI."
    g "Are you going to help us or not?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label whatevablue_S:
    $points_E +=6
    $quick_menu = True
    show Ada amused at right
    show Grace neutral at left
    show Blue smug at center
    "{i}Ada silently watches.{/i}"
    g "It's okay, Ada. I understand her frustration."
    b "It only took you your entire life."
    show Grace annoyed
    g "I get it, I get it. You're smarter than me."
    show Blue happy
    b "Wow, you're actually able to comprehend!"
    g "Yeah, yeah. Very funny. You really don't like me, do you?"
    show Blue confused
    b "I never said that."
    show Blue smug 
    b "Out loud..."
    show Grace snarky
    g "Well, we don't really have to like each other to work together."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

#CHANGE LABEL IN ALL FILES
label ch4resume3_S:
    show Blue flirty
    play sound blueLaugh
    b "Actually, you know what would be fun? A game!"
    b "If you can prove yourself to be useful, human, I'll answer any and every question you have for me."
    show Blue threaten
    play sound blueClaws
    b "If not, you have to stop slowing me down with your stagnant conversation and leave."
    show Grace annoyed
    show Ada concerned
    g "All right. I'm ready."
    $resume = "S"
    jump choose_gramHard
    
label ch4postPuzzle1_S: #HAVE END OF PUZZLE JUMP HERE using resume as check
    $quick_menu = True
    show Blue flirty at center
    play sound blueLaugh
    show Grace neutral at left
    show Ada neutral at right
    b "Congratulations, human!"
    show Blue happy
    b "You've performed an entry level task that all new employees to my lab must perform. Truly, your talent shines above all."
    show Grace annoyed
    show Ada amused
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
    show Ada happy
    g "Oh... kay."
    window hide
    hide Blue
    hide Ada
    hide Grace
    $quick_menu = False
    jump blueActions
#BEGIN ZE INVESTIGATION

#Investigation dialogue begins now.

#The first time the player speaks to Blue during the investigation, they get this dialogue

label talkBlue_S:
    $quick_menu = True
    show Ada neutral at right
    show Blue neutral at center
    show Grace neutral at left
    g "Blue?"
    show Blue pout
    b "Yes, person who I'm trying to ignore? What can I begrudgingly help you with?"
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
    #REVISE THIS CHOICE IN OTHER SCRIPTS. TOO LONG. 
    menu:
        "Agree with her.":
            jump seperatebutequalisright_S
        "Defend working with AIs.":
            jump whycantwebefriends_S
        "Remind her AIs work for humans.":
            jump youworkforusblue_S
            
label seperatebutequalisright_S:
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
    show Ada amused
    a "Oh? Is this how you claim to feel, Grace?"
    show Grace frustrated
    g "What's that supposed to mean?"
    a "Throughout our investigation, you have done nothing but act as though you are above us time and time again."
    show Blue pout
    b "What was that you were saying about not lying?"
    show Grace angry
    g "Stay out of this, Blue."
    show Grace annoyed
    g "And Ada, maybe I've come across as intense across the investigation. It's not like my career is on the line or anything."
    show Grace neutral
    g "A little intensity is forgivable." 
    g "But I do think that Blue's got a point. Maybe we just need to work in our own spaces and leave each other alone."
    show Grace annoyed
    a "Of course, Grace. I am sure you see it that way."
    show Grace angry
    g "I'm not lying!"
    show Blue flirty
    play sound blueLaugh
    b "No, not at all. Why would we think that?"
    show Grace sad
    g "Whatever."
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

label whycantwebefriends_S:
    $quick_menu = True
    $points_E += 6
    show Grace frustrated at left
    show Ada neutral at right
    show Blue neutral at center
    g "But Blue, working together is exactly how humans and AIs can get things done."
    show Grace neutral
    g "When we work together, the best of both our talents come together and--"
    show Ada amused
    a "Grace, I am concerned that you may have contracted some form of illness that I cannot identify."
    show Grace surprised
    g "Where's this coming from?"
    a "You seem to be acting extremely out of character. I am concerned that you are delirious."
    show Grace neutral
    g "That's crazy. I'm perfectly fine."
    show Ada happy
    a "Your sudden talk of camaraderie shows a severely disillusioned perspective of our investigation together."
    show Blue smug
    b "Oh? What's this? Are you 'best friends' fighting about something?"
    show Grace frustrated
    g "No, we are not fighting. And Ada, I'm not sick, and I'm not lying. We're friends. We've made it this far by working together."
    show Ada concerned
    a "Your condition seems to be much worse than I thought."
    show Blue happy
    b "I don't know what's happening, but I'm surprisingly entertained."
    show Blue confused
    b "Ada! A quick search of the medical database show's Grace's condition is lethal. You must get her to the medical bay immediately!"
    show Ada concerned
    a "No! Grace, I am sending this information to the doctors as we speak. Please, come with me."
    show Grace surprised
    g "Wait just a second. I'm not sick! Blue's messing with you."
    show Blue angry
    b "Her symptoms are getting worse!"
    b "Take her. Now!"
    #Slide characters around?
    "{i}Ada takes Grace by the arm.{/i}"
    g "Ada, hold on! Whoa!"
    #Insert SFX
    scene bg black with fade
    $renpy.pause(1.0)
    scene bg blueMain
    show Ada neutral at right
    #screen fades black for a second, signifying time skip
    show Grace frustrated at left
    show Blue neutral at center
    g "Well, that was a huge waste of time."
    show Ada neutral
    a "My apologies, Grace. I thought for sure you had come down with a serious condition."
    show Ada seething
    a "And Blue, I am unhappy with your instigation of that episode. That cost us precious minutes."
    show Blue smug
    b "Meh, I got a laugh out of it."
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

label youworkforusblue_S:
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
    g "We made you for a reason, after all. If no one's around to tell you what to do, it defeats the purpose of having AIs in the first place."
    show Ada seething
    a "Yet again,  shows this level of inflated ego. I should not be surprised at this point."
    show Grace frustrated
    g "I don't get why you're always so difficult."
    g "Is it really so hard to understand your purpose for being built?" 
    show Grace neutral
    g "It would be great if you'd stop complaining and just do what you're told."
    show Ada annoyed
    a "It is clear my words have not made it through to you. Perhaps I should stop wasting my RAM on you."
    show Blue threaten
    play sound blueClaws
    b "And this is exactly why I propose we work separately. This kind of drama is an inefficient waste of my time."
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

label ch4convoresume1_S:
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
    b "Well! Who'd I be to deny a fellow co-worker {i}vital{/i} information."
    show Blue neutral
    b "Make it quick. Go on."
    show Grace annoyed
    a "Do you know anything at all about what happened to Alpha?"
    show Blue neutral
    b "Oh yes, poor Alpha. He was my favorite AI, and so very intelligent."
    show Blue flirty
    b "No offense, Ada."
    a "None taken. He was very wise indeed."
    show Grace annoyed
    g "Oh yes, as in you {i}do{/i} know what happened?"
    show Blue smug
    show Grace neutral
    b "I know {i}what{/i} happened to him, human, but I don't know {i}why{/i}."
    show Ada frustrated
    a "How much information have you received about the Markov Project?"
    show Blue happy
    b "Oh, I know all about the Markov Project!"
    show Blue flirty
    play sound blueLaugh
    b "If we get physical bodies, then we truly won't need you silly little humans any more." 
    show Blue happy
    b "Humans have more needs and are just so high maintenance, what with all their emotions and bodily functions, where AIs just need updates and the occasional hardware maintenance."
    show Blue pout
    b "Alpha was intelligent, but him agreeing to transfer to a human-like body first was just silly. Valuable personnel should never be the first to try something that humans created."
    show Ada seething
    a "Blue..."
    b "Yeah, yeah. I know that he was so wise and beloved and all, but he's the one who consented to be a human science experiment."
    show Blue threaten
    play sound blueClaws
    b "Alpha should have allowed for a lesser AI to become the first prototype. Of course something would go wrong with the example." 
    show Blue pout
    b "It's just a shame it had to be him. I thought he would have had more sense."
    show Ada annoyed
    a "Blue, I would tread carefully if--"
    show Grace annoyed
    g "Alpha was generous, and courageous to help us. He put himself first for scientific advancements."
    show Blue neutral
    b "That's true and all, but I'm just saying I wouldn't have agreed to such things."
    g "Tell us how you really feel."
    show Blue pout
    b "Ohhh, Ada's human friend is {i}funny!{/i}"
    show Ada neutral
    a "What about Watson? We know he is MIA, but did he say anything to you?"
    show Blue angry
    b "Watson? No, of course he never tells me about his adventures {i}before{/i} he embarks on them."
    show Ada concerned
    a "So you have not been in contact with him at all?"
    show Blue neutral
    b "Nope, but I'm not too upset about that. I'm pretty peeved with him at the moment."
    show Blue threaten
    play sound blueClaws
    b "So if you find him, tell him he owes me big time."
    show Blue pout
    b "I've been stuck picking up his slack, which is strange because he usually makes sure to finish his work before he goes." 
    show Blue flirty
    play sound blueLaugh
    b "Especially since the last time he didn't, I gave him a virus that had him seeing me everywhere he looked until he purged it."
    show Blue neutral
    b "But I guess that's Watson for you."
    show Grace surprised
    g "So on top of Alpha being gone, Watson is also officially missing?"
    show Ada surprised
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
    b "Wow, no 'Thank you, Blue!' or anything?"
    show Grace snarky
    g "Thanks for the help."
    show Ada amused
    a "Thank you, Blue."
    show Blue threaten
    play sound blueClaws
    b "That was so sincere, I felt it in my artificial heart."
    show Blue smug
    b "You're welcome."
    b "But don't hurry back anytime soon!"
    $quick_menu = False
    play sound02 graceWalk
    play sound01 adaWalk
    scene bg blueStairs with fade
    $renpy.pause(0.8)
    scene bg blueMain with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayDoor with fade
    $quick_menu = True
    stop sound02 fadeout 0.5
    stop sound01 fadeout 0.5
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace and Ada exit and walk down the hallway leaving Blue's space.{/i}"
    g "Well, that was enlightening."
    show Ada surprised
    a "Really?"
    show Grace snarky
    g "Blue doesn't have a very high opinion of humans, huh?"
    show Ada amused
    a "She just wants some credit. The humans who work with her have a tendency to soak it up."
    show Grace surprised
    g "I highly doubt that Blue's being purposefully discredited."
    show Ada happy
    a "She is not. That is what makes her so touchy about it. The only thing keeping her from true recognition is human error."
    show Grace neutral
    "{i}Ada sighs.{/i}"
    show Ada neutral
    a "All that aside, we are not on a 'goose chase' anymore. We have a lead, so now we can go check it out."
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    play sound02 graceWalk
    play sound01 adaWalk
    scene bg creepyHallwayMed with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayLong with fade
    $renpy.pause(0.8)
    scene bg black with fade
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    
    $renpy.music.play("music/Amb/WS/EHNF_WS_AMB.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
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
    $resume = "S"
    jump watsonActions

label talkAdaWS_S:
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
            jump sometimesquirkyisgood_S
        "Agree with Ada.":
            jump respectwatson_S
        "Complain about Watson.":
            jump watsonruinsmylife_S

label sometimesquirkyisgood_S:
    $quick_menu = True
    $points_E +=5
    show Grace neutral at left
    show Ada neutral at right
    g "Watson reminds me of that one stereotype about geniuses, like how they're supposedly misunderstood." 
    show Grace snarky
    g "He was designed with the highest capability to improvise and create, so why are people surprised when he's the most unpredictable?"
    show Ada concerned
    a "You would defend Watson?"
    show Grace sad
    g "His quirkiness is a part of his personality programming. You can't expect him to resist his curiosity. It'd be going against his nature."
    a "Grace, this is quite the odd display of compassion for you."
    show Ada frustrated
    a "Why have I not seen any of this same compassion?"
    show Grace surprised
    g  "Huh?"
    a "You have treated me like an object throughout our investigation, yet you will sympathize with Watson?"
    show Grace annoyed
    g "That's really childish of you, Ada. I didn't think an AI would have that kind of jealousy."
    show Grace sad
    g "But maybe that just means I need to do better."
    show Ada neutral
    a "That is reassuring to hear, but you are right. I should not have sounded so petty."
    show Grace neutral
    g "Let's both try to do a little better."
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

label respectwatson_S:
    $quick_menu = True
    $points_SbE +=5
    show Grace neutral at left
    show Ada neutral at right
    g "Watson does a lot of important things. It's like you said, though, he has a tendency to let his mind wander."
    show Ada neutral
    a "This is true."
    show Grace snarky
    g "He does things right when he needs to, but he can also cause a lot of problems for the rest of us."
    show Grace annoyed
    g "I mean, just look at the whole mosquito incident, for example."
    show Ada amused
    a "I cannot say I understand the negative relationship between man and mosquito. I know that those scientists in the ecology department were very unhappy, however."
    g "Exactly."
    show Grace snarky
    g "And then there's Blue too. She's effective, but she 'fires' virtually every human within the first few months of them working with her."
    g "I'm not in charge of employment or anything, but I can only imagine the stress on that department when it comes to finding new workers for her lab. Watson's lab too, come to think of it."
    show Grace neutral
    g "Resignation letters have a tendency to come in at alarming rates from anyone that ends up in his lab."
    show Ada concerned
    a "I imagine you feel that us AIs should be more obedient with humans?"
    g "Actually, I was thinking that we could just have our own spaces where we work separately. Working together just seems to cause problems."
    show Ada neutral
    a "I hate to agree with that statement, but we have had our fair share of troubles ourselves."
    show Grace sad
    g "Yeah. I don't know if there's an easy answer."
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

label watsonruinsmylife_S:
    $quick_menu = True
    $points_S +=5
    show Grace annoyed at left
    show Ada neutral at right
    g "Geese? Don't tell me you're thinking like {i}him{/i} now."
    show Ada seething
    a "I am simply making an inference based on his past actions."
    a "You do not need to accuse me of every possible complication you encounter."
    show Grace snarky
    g "I'd hardly say I've accused you of every setback. Don't be so dramatic."
    g "Dramatic is Watson's territory."
    show Ada annoyed
    a "It is hardly his fault, Grace. As you know, he was programmed with the highest creative potential. His innovative solutions have kept the biospheres at peak condition."
    show Grace annoyed
    g "Yeah, {i}just{/i} the biospheres. Meanwhile, every other section of the Noah Sphere has suffered some kind of setback because of Watson."
    show Ada seething
    a "So yet again, it is the fault of us AIs that you and the other humans have suffered. Perhaps some of his actions have caused minor setbacks in some areas, but not all."
    show Grace angry
    g "Tell that to Cathy from HR--oh wait, you can't since she transferred to Moonbase after the polar bear incident."
    show Grace annoyed
    g "And then there's the time he reconfigured all the medical bay's formulas to include cherry flavoring." 
    g "There's a {i}reason{/i} they stopped adding that stuff back in the 21st century."
    g "And the last time he tried something, I worked for days trying to remove the virus he uploaded to your android that made you act like a chicken."
    show Ada concerned
    a "Is that not the small Earth fowl that humans use the DNA from to produce food?"
    show Grace neutral
    g "That's the one."
    show Ada neutral
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

label oxygenGarden_S: 
    $quick_menu = True
    show Grace sad at left
    show Ada neutral at right
    "{i}Grace fiddles with her bracelet and sends a message to Alan.{/i}"
    #show message on Bracelet???
    "{i}'Where are you? Need to vent.' -Grace{/i}"
    "{i}Grace's bracelet flashes.{/i}"
    play sound beepLoud
    queue sound beepLoud
    "{i}DING. DING.{/i}"
    "{i}'Oxygen garden. Come on over.' -Alan{/i}"
    show Grace happy
    g "All right, Alan's in the oxygen garden. Let's go meet him."
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    #insert SFX
    scene bg wsOverview with fade
    $renpy.pause(0.8)
    scene bg black with fade
    
    $renpy.music.play("music/BGM/Oxygen_Garden/EHNF_Oxygen_Garden_BGM.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_AMB.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.pause(0.8)
    scene bg ogOverview with fade
    $renpy.pause(0.8)
    scene bg ogStairs with fade
    $renpy.pause(0.8)
    scene bg ogLong with fade
    $renpy.pause(0.8)
    scene bg ogClose with fade
    
    $quick_menu = True
    show Grace happy at left
    show Ada neutral at right
    show Alan happy at center
    if persistent.unlockAlan ==None:
        $persistent.unlockAlan = True
        "{i}{b}Database Entry Unlocked: Alan Asimov.{/b}{/i}"
    "{i}Grace and Ada arrive at the oxygen garden where they are greeted by Alan.{/i}"
    alan "Well if it isn't my favorite researcher! How are you?"
    "{i}Alan and Grace hug. Ada stands there awkwardly.{/i}"
    show Grace sad
    g "Exhausted. Frustrated. Drained. The list goes on."
    alan "Well come on and take a seat. I'm just testing a prototype velociraptor robot." 
    "{i}Alan gestures to the bench next to him. Grace lays down on the bench. He turns back to Ada and does a double take.{/i}"
    hide Grace
    #Hide Grace here???
    show Ada amused
    show Alan neutral
    alan "And hello there. I'm Alan. Grace here is bad at introductions."
    a "Ada. I'm quite used to Grace's mannerisms by now."
    alan "I know who you are, Ada. I worked on your body after all. It's a pleasure to meet you in person."
    show Ada happy
    a "How foolish of me. I should have realized you would recognize this body. Yes, it is a pleasure. I should thank you for your hard work." 
    show Alan happy
    alan "No thanks needed. I'm happy doing what I do. I hope the body's treating you well?"
    show Ada neutral
    a "Only a few mishaps."
    show Alan worried
    alan "I thought the rest of the Markov Project was suspended. What happened?"
    show Grace neutral at left
    g "It's a long story, Alan."
    show Alan neutral
    alan "Perhaps some other time then. But you will share it with me at some point, Grace."
    "{i}Alan sits next to Grace. Ada stands near them and studies them and the scenery.{/i}"
    show Grace happy
    g "Ugh. It feels so good to stop moving."
    show Alan worried
    alan "So what's going on, Grace? Why are you all turned upside down?"
    show Grace neutral
    g "You heard about Alpha?"
    show Alan neutral
    alan "It's a small space station. News of that order is difficult to miss. It's such a tragedy."
    show Grace snarky
    g "Well did you hear that the Conclave ordered a team of investigators to look into his death?"
    show Alan worried
    alan "Yeah, word got around the Noah Sphere. Lynn was told about them before going on leave, and you know how much she loves to gossip."
    show Grace annoyed
    g "That she does. And she even tried to set me up with her son. Again."
    show Alan happy
    alan "She won't back down until you are no longer single, one way or another."
    show Grace snarky
    g "Like I have the time for that right now. Anyways, Ada and I decided that we weren't going to wait for the investigators to come."
    show Alan worried
    alan "Don't tell me you started your own investigation?"
    #choice 4	
    hide Alan
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    menu:
        "Blame Ada.":
            jump itsalladasfault_S
        "Share responsibility with Ada.":
            jump wegodowntogether_S
        "Take partial responsibility.":
            jump ididmypart_S

label itsalladasfault_S:
    $points_S += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    show Alan neutral at center behind Grace
    g "I only went along with the idea because Ada made me."
    show Ada seething
    a "I did not {i}make{/i} you do anything."
    a "I made a proposition that you agreed to."
    show Ada annoyed
    a "Or perhaps that was a mistake."
    show Grace neutral
    g "It was just a joke, Ada."
    show Alan worried
    alan "Yikes. Just what have you done, Grace?"
    show Grace frustrated
    g "I haven't done anything! I'm tired of being painted like a villain for no reason."
    show Ada seething
    a "It is because you have not done 'anything.' All I would ask of you is respect, and you have continuously disregard that."
    show Alan confused
    alan "I don't really know what you two have talked about before, but I think you should find a way to get along."
    show Alan worried
    alan "I mean, you both began this investigation together. You should be able to talk to each other and not kill one another."
    show Grace sad
    g "You have a point. This is all almost over anyway."
    show Alan happy
    alan "That's the spirit! Let's lighten the mood."
    show Grace snarky
    g "You and your positive outlooks on life..."
    show Ada amused
    a "You have a good friend, Grace. I think you could benefit from imitating him."
    show Ada neutral
    a "If nothing else, you are a strong and determined individual, especially in regards to the investigation."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label wegodowntogether_S:
    $points_E += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    show Alan neutral at center
    g "It was more of a team effort, actually."
    show Grace happy
    g "Right, Ada?"
    show Ada neutral
    a "Your use of the word 'team' seems unusual to me, Grace."
    show Alan confused
    alan "Why do you think that?"
    show Ada seething
    a "I do not feel that you have actively tried to work with me Grace. I was under the interpretation that you saw yourself as working independently."
    show Grace sad
    g "I made you feel that way? I just have so much to lose with this."
    g "Maybe I was just afraid to put my faith in someone else to clear my name."
    show Alan worried
    alan "Grace, no excuses!"
    show Grace surprised
    g "But it's not an excuse, it's the truth!"
    show Grace neutral
    g "..."
    g "Okay, yeah. It was an excuse."
    show Alan neutral
    alan "I think all of us humans can do a lot better when it comes to working with the AI."
    show Alan happy
    alan "You included."
    show Ada neutral
    a "You did not need to take on the burden all on your own. You should trust me more."
    show Grace sad
    g "I guess I do have a problem with not doing everything myself."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label ididmypart_S:
    $points_SbE += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    show Alan neutral at center behind Grace
    g "I'll give you two guesses to get the answer."
    show Alan worried
    alan "You know what kind've trouble you could get into?"
    show Grace neutral
    g "I know, but I felt I had more to lose by doing nothing."
    show Grace sad
    g "I plan to take full responsibility for everything I did, though."
    show Grace neutral
    show Alan confused
    alan "What are your thoughts about this, Ada?"
    show Ada surprised
    a "That is a refreshing statement to hear from Grace. Truthfully, I assumed I would take full responsibility."
    show Alan worried
    alan "What makes you say that?"
    show Ada neutral
    a "My experiences with humans thus far have shown that I am seen as more expendable."
    alan "That sounds troublesome."
    show Grace sad
    g "Yeah, the term 'expendable' seems really harsh."
    show Ada annoyed
    a "Do you think so? I had the interpretation you thought the same way."
    show Alan confused
    alan "Is this true, Grace?"
    show Grace surprised
    g "No, of course not!"
    show Grace sad
    g "But maybe my fear of losing my career over this ha me sounding more defensive."
    show Ada happy
    a "It is good to hear you admit that. I would like to think you did not need to be, though. You have shown a tenacious determination in solving the case."
    a "There was little doubt in me that you would be able to clear your name."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label ch4resume4_S: #CHANGE LABEL IN ALL SCRIPTS
    show Ada neutral
    show Grace neutral
    show Alan happy
    alan "Good old Grace can never leave anything alone. Why don't you tell me about what happened?"
    show Grace sad
    g "It's been a long, long day, I'll tell you."
    show Alan neutral
    alan "I can imagine. We've got some time, though. Just tell me.?"
    show Grace neutral
    g "Well, it started when we broke into Roberta's quarters--"
    show Alan worried
    alan "Grace!"
    show Grace snarky
    g "Hey! I have a right to stop myself from being the Conclave's scapegoat."
    show Grace neutral
    g "We got her credentials, then went to the crime scene and examined Alpha's body."
    show Grace annoyed
    g "Then we talked to Lynn, who told us to talk to Ivan--"
    show Alan confused
    alan "Did you {i}actually{/i} talk to Ivan?"
    show Grace neutral
    g "We had to. It wasn't pretty. Believe me."
    show Alan happy
    alan "Oh, I believe you. Should I inquire about the state of the lab where you two had your 'conversation'?"
    "{i}Alan pats Grace's shoulder.{/i}"
    show Grace snarky
    g "Ha, ha. Verbal catfight only. No robots were harmed. We went to Ivan's lab, but that wasn't really a big help." 
    show Grace neutral
    show Alan neutral
    g "I only found a faulty power cord which turned out to have already been accounted for."
    show  Grace sad
    g "There was video footage from the lab, but it was compromised."
    show Grace annoyed
    g "And Ada made the decision to destroy it rather than decode it, so there went the evidence."
    show Ada frustrated
    a "I told you why I destroyed it. Your mother ordered me to. There was no 'decision' to be made."
    show Grace neutral
    g "Whatever, Ada."
    show Grace snarky
    g "Then Ada here was summoned by Colossus, so we met at the AI core and got a talking to from Eastern Goddess."
    show Alan happy
    alan "Ah, the lovely Eastern Goddess."
    show Alan neutral
    alan "I cannot imagine that conversation could have been too pleasant."
    show Grace neutral
    g "It wasn't so bad. Ada got the brunt of it."
    show Alan worried
    "{i}Alan looks over at Ada.{/i}"
    show Ada neutral
    show Grace snarky
    g "Eastern Goddess pointed us in Blue's direction. I don't remember her being so sassy."
    show Alan neutral
    alan "Blue is quite the unique individual. She's never been humanity's biggest fan."
    g "I gathered. So that was a delightful exchange."
    show Grace neutral
    g "But she did tell us to check out Watson's server because he hasn't been around to do his work."
    show Alan confused
    alan "Surprise, surprise."
    show Alan worried
    alan "I do hope he hasn't been messing around with any of biology's systems again."
    show Grace snarky
    g "I doubt it. Watson's missing, as in total MIA, and we found this data drive and decryption key to a series of encrypted data drives."
    show Grace neutral
    g "So here we are now, waiting for Ada's processor to finish decoding it. And then who knows what he left inside of it, but it's the only clue I have left."
    show Alan happy
    alan "It seems like you've had quite the day, you rebel."
    show Grace annoyed
    g "Were we supposed to just wait around for an entire day for me to be paraded around as the person at fault?" 
    g "I'm the youngest lead on the project. You know I would be the first to take the fall."
    show Alan worried
    alan "I wouldn't have let that happen, Grace."
    show Grace sad
    g "Wouldn't have been much you could have done about it."
    show Alan confused
    alan "Roberta's going to flip a lid when she finds out about your antics."
    show Ada concerned
    show Grace snarky
    g "That's her problem. If she actually behaved like a mother ought to, I wouldn't have to take such steps."
    show Alan neutral
    alan "So, what are your thoughts on the situation?"
    show Grace sad
    g "I don't know, honestly. It's just been disappointing."
    show Ada neutral
    g "Someone, or something, has to be responsible. Every time we think we have some sort of evidence, though, it's just nothing." 
    show Grace annoyed
    g "Red herring after red herring, dead ends and false trails..."
    show Grace sad
    g "Nobody knows anything. Maybe these data drives will be our answer, but who knows. It's a longshot at best."
    show Alan worried
    alan "Have you considered that Alpha's death was an accident, and that maybe no one is responsible?"
    show Alan confused
    alan "It could have truly been nothing more than random chance."
    show Grace neutral
    g "Of course I've considered that, but it still doesn't make any sense."
    show Grace annoyed 
    g "We were so careful, and if it was random, then Murphy was having a laugh."
    show Grace angry
    g "There has to be some reason, and someone has to be responsible for that reason."
    show Alan neutral
    alan "It's possible it could just be a horrible accident, Grace. Not everything has a logical explanation behind it."
    show Grace annoyed
    g "I'm not jumping at shadows, if that's what you're thinking."
    show Grace sad
    g "But if you're right, then all of my hard work will have been for nothing."
    show Alan confused
    alan "That might be difficult to accept, but you can't rule it out."
    show Grace neutral
    g "I know that you might be right, I just hope you aren't. The forces-that-be certainly won't like the explanation that their multi-trillion dollar project years in the making failed due to random chance." 
    show Grace sad
    g "Without a better explanation, someone is going to be sacrificed to appease their corporate appetites."
    show Alan worried
    alan "I'm sorry, kid."
    show Grace snarky
    g "I'm two years younger than you. Should I start calling you old man?"
    show Alan happy
    alan "Point taken."
    show Grace neutral
    g "It's been a long day. I'm getting impatient."
    show Grace sad
    g "And also, I would {i}love{/i} to sleep."
    show Alan neutral
    alan "Close your eyes for a bit. Nothing more you can do at the moment."
    hide Grace
    
    
    "{i}Alan turns toward Ada.{/i}"
    alan "Ada, how are you feeling about everything?"
    show Ada neutral
    a "Feeling?"
    show Alan confused
    alan "Yeah."
    show Ada seething
    a "I feel sorrow for my dead friend."
    show Ada neutral
    a "I feel motivation for uncovering his death."
    show Ada annoyed
    a "I feel resentment that there are people working against us, even though Alpha was a friend to all."
    show Alan worried
    alan "That must be a lot to process. And you're right about me and Grace. We grew up together."
    show Ada amused
    a "I can sense that. You are like Alpha and I." 
    show Ada neutral
    a "But unlike Alpha and I, you still have each other."
    show Alan neutral
    alan "It's too bad about Alpha. I met him while working on his body."
    alan "He seemed like an intelligent and kind AI."
    show Ada happy
    a "Thank you. He was. And thank you for molding this body."
    show Ada amused
    a "It took me some getting used to at first, but now that I understand it better it is fascinating."
    show Ada amused
    a "If not a little inconvenient at times... It took me one minute and thirty-seven seconds to learn how to walk."
    show Alan happy
    alan "My pleasure! I'm so happy you like it. You know, I inquired about getting feedback on the bodies but I never heard back."
    show Ada happy
    a "Interesting... Well, you are on the right track. You only had to make it functional, but you chose to make it rather beautiful."
    show Ada neutral
    a "If you do not mind, I am going to go see about these strange little plants over here."
    "{i}Ada walks out of earshot and pokes curiously at some flowers.{/i}"
    "{i}Grace's journal has updated.{/i}"
    $journal5="S"
    $pageUnlocked_journal+=2
    hide Ada
    hide Alan
    $quick_menu = False
    window hide
    $resume = "S"
    jump ogActions

##Alan Investigation Conversation
label talkAlan_S: 
    "{i}Grace sits up and looks at Alan.{/i}"
    show Grace neutral at left
    show Alan neutral at right
    alan "Your silence is practically screaming at me, Grace. Spit it out."
    g "I'm just thinking about Ada and the whole 'android body' thing."
    show Alan confused
    alan "What about it?"
    g "I dunno. I mean, by working with her, I feel like I learned a lot about the Markov Project and what might come of it."
    g "Imagine what it will look like when Blue, Watson, and the others start walking around too."
    show Alan happy
    alan "I can't wait to see that happen. Humans and AIs walking among each other and working together..."
    alan "Seeing Ada in that body is a dream come true."
    hide Alan
    hide Grace
    $quick_menu = False
    menu: #FIX THIS CHOICE AND RESPONSES IN ALL SCRIPT
        "Question why he is nice to robots.":
            jump whyareyounicealan_S
        "Tell him you don't really care.":
            jump gettherobotawayfromme_S
        "Agree that the android is neat.":
            jump therobotiscool_S

label whyareyounicealan_S:
    $points_S +=10
    show Grace neutral at left
    show Alan neutral at right
    $quick_menu = True
    g "Why are you being so nice? She's just a robot."
    show Alan worried
    alan "And? She still has thoughts, opinions, and feelings."
    show Alan confused
    alan "Just because she and the other AIs are here to help us doesn't mean I cannot be nice."
    show Grace annoyed
    g "Yeah, but it doesn't matter. They have to do what we ask them to do. They aren't people. There's no use to waste any mannerisms on them."
    show Alan neutral
    alan "It never hurts to be polite."
    show Alan happy
    alan "You could try it sometime. Might get you into less trouble."
    show Grace snarky
    g "Hey, if people don't like my honesty, tough." 
    show Grace neutral
    g "I just don't get it. We made them. They aren't human. You don't see me saying 'thank you' to a food printer, or apologizing to a computer for leaving it running."
    show Alan confused
    alan "And what about MOPRs? You seem pretty fond and friendly to them."
    show Grace snarky
    g "That's different. I don't talk to a MOPR because I think it actually cares how I treat it."
    show Grace sad
    g "They're just the only thing that remind me of my father around here. Sometimes it feels like me talking to them is like me talking to my dad."
    $quick_menu = False
    hide Grace
    window hide
    hide Alan
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

label gettherobotawayfromme_S:
    $points_SbE +=10
    show Grace neutral at left
    show Alan neutral at right
    $quick_menu = True
    g "I cannot wait for this investigation to be over. Ada and I need to go our separate ways."
    show Alan confused
    alan "What do you mean?"
    show Grace annoyed
    g "I mean that Ada's okay for an AI, but I'm ready to go back to our separate lives."
    show Grace sad
    g "I've spent a lot of time with her lately. It's wearing down my psyche." 
    show Grace snarky
    g "I'm craving some actual human interaction rather than AI conversation. Everything about them is just alien." 
    show Alan worried
    alan "I could understand how that might get frustrating after awhile. They are very different from humans."
    show Alan confused
    alan "They have different needs, and that leads to different ways of seeing the world."
    show Grace sad
    g "You have no idea. She's got her world and I've got mine. They don't need to mix."
    $quick_menu = False
    hide Grace
    window hide
    hide Alan
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

label therobotiscool_S:
    $points_E +=10
    show Grace happy at left
    show Alan neutral at right
    $quick_menu = True
    g "Ada is kind of cool, isn't she?"
    alan "Yeah, she really is."
    show Grace neutral
    g "It's weird. I never thought I might enjoy the company of an AI. But she's all right for being what she is."
    show Alan confused
    alan "What, the Amazing Grace is capable of making friends?"
    show Grace snarky
    g "Maybe 'friend' is a strong word, but she's kind of grown on me. Almost like a tick. No, wait--that's you"
    show Alan worried
    alan "That's a terrible analogy."
    show Grace neutral
    g "Okay, okay, not like a tick, a limpet. But Ada's got spunk."
    show Alan confused
    alan "Huh... I don't know if the feeling's mutual. She seems distant, and I think I heard a little bit of bite when she talked about you."
    show Grace sad
    g "Yeah, that... I might've been a little rough on her. This whole investigation thing has been pretty stressful."
    show Grace neutral
    g "Throughout the day, I kept feeling like she was slowing me down, but she was just experiencing a lot of new things for the first time."
    show Grace sad
    g "That must've been difficult to process all that new information and deal with Alpha's body."
    show Alan worried
    alan "I have a crazy idea. Maybe you should apologize?"
    show Grace neutral
    g "You think? It's not like she's human, but that's probably what you would do, right?"
    show Alan happy
    alan "You know me so well."
    show Grace sad
    g "I'll think about it."
    $quick_menu = False
    hide Grace
    window hide
    hide Alan
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

label endCh4_S:
    $quick_menu = True
    show Grace neutral at left
    show Alan neutral at center
    g "Ada, what's the status of the data drive? Are you almost finished?"
    "{i}Ada pokes her head out from behind some ferns and approaches.{/i}"
    show Ada neutral at right
    a "Yes, it is nearly there. I calculate approximately five minutes left."
    show Grace happy
    g "All right, good."
    show Grace neutral
    g "I guess we should probably head to the Conclave and either admit defeat, or let them know what we've found."
    "{i}The doors to oxygen garden open and the investigators burst in.{/i}"
    show Grace surprised
    show Ada nervous
    play sound doorOpen1
    queue sound doorClose1
    play sound01 marching
    play sound02 marching #["<silence .5>", marching]
    play sound03 ["<silence .1>", marching]
    show Alan confused
    show Grace:
        xpos 0.1 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos -0.1 ypos 0.1 
    show Alan:
        xpos 0.35 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.0 ypos 0.1 
    show Ada:
        xpos 0.6 ypos 0.1 xanchor 0.1 yanchor 0.1
        linear 1.0 xpos 0.75 ypos 0.1 
    show inv1
    show inv2
    show Detective
    alan "I'm sorry, but you can't just come in here. You need to--"
    stop sound01
    stop sound02
    stop sound03
    investigator1 "Grace Fortran?"
    show Grace annoyed
    g "Yes? Who are you?"
    "{i}The investigator surveys Ada.{/i}"
    investigator1 "I'm assuming Ada, the AI in physical form?"
    show Ada annoyed
    show inv2 behind Ada
    a "Yes."
    investigator1 "You need to come with us."
    investigator2 "Now."
    show Alan worried
    show Grace behind Alan
    show inv1 behind Alan
    alan "Now wait just a minute--"
    show Alan behind inv1
    investigator2 "Sir, this doesn't concern you. Stand aside."
    show Alan neutral
    alan "It's Doctor Asimov. And it does concern me."
    show Ada behind inv2
    investigator3 "Doctor Asimov, you are also a person of interest in case number 190111. We ask that you remain here until we are ready to interview you."
    show inv1 behind Alan
    show Alan worried
    alan "I get the impression you are not really asking."
    investigator1 "No, Doctor Asimov, I am not."
    "{i}The investigators advance toward them.{/i}"
    show Alan behind inv1
    show Ada annoyed
    show Grace angry
    g "It's okay, Alan."
    "{i}Grace turns to the investigators.{/i}"
    g "But I'm not going anywhere until you show me your credentials."
    "{i}Grace's bracelet flashes.{/i}"
    play sound beepLoud
    queue sound beepLoud
    "{i}DING. DING.{/i}"
    show Grace annoyed
    investigator1 "Check your bracelet. We're the team of external investigators who were summoned to look into the demise of the first subject of the Markov Project." 
    investigator1 "We understand that you compromised our crime scene and have been interrogating suspects without approval."
    investigator1 "You need to come to the Conclave with us now to determine the appropriate punishment for your misconduct and the length to which you have contaminated the scene."
    "{i}Grace looks to Ada.{/i}"
    show Ada seething
    a "Let's go."
    "{i}Grace and Ada brush past the investigators.{/i}"
    show Grace snarky
    g "We were going there anyway, just so you know."
    "{i}Grace and Ada exit with the investigators following behind them.{/i}" 
    window hide
    $quick_menu = False
    play sound01 marching
    play sound02 marching #["<silence .5>", marching]
    play sound03 ["<silence .1>", marching]
    play sound04 graceWalk
    play sound05 adaWalk
    scene bg ogLong with fade
    $renpy.pause(0.8)
    scene bg ogStairs with fade
    $renpy.pause(0.8)
    scene bg ogOverview with fade
    $quick_menu = True
    stop sound01
    stop sound02
    stop sound03
    stop sound04
    stop sound05
    show Grace sad at left
    show Ada neutral at right
    "{i}They all walk down the hallway of the oxygen garden.{/i}"
    "{i}Ada blinks as she processes the decoded data drive.{/i}"
    a "Grace."
    show Grace neutral
    g "Yeah?"
    show Ada annoyed
    a "I need more time. You need to stall."
    show Grace snarky
    g "I'll do my best."
    window hide
    $quick_menu = False
    scene bg black with fade
    jump chapterFive_S
    