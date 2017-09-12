label chapterFour_SbE:
    window hide
    $quick_menu = False
    scene bg black with fade
    scene bg chapterFour with fade
    $renpy.pause(3.0)
    scene bg AICoreDoor with fade 
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    "{i}Grace arrives outside of the AI core to find Ada waiting for her. She walks up to Ada.{/i}"
    g "Please tell me that we're not in any major trouble."
    show Grace snarky
    g "Well, anymore than we already are."
    a "Actually, I have not been to see Colossus yet."
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
            jump press_SbE
        "Let it go.":
            jump frozen_SbE
        "Ask her if she's okay.":
            jump okay_SbE

label press_SbE:
    $points_S +=4
    $quick_menu = True
    show Grace surprised at left
    show Ada neutral at right
    g "What do you mean you got sidetracked and went to Watson's workspace? This isn't the time to be dawdling, Ada."
    a "I had orders from Colossus to check in. Watson has not been to work today."
    show Grace annoyed
    g "Why would he have you do it?"
    show Ada seething
    a "I do not know. As a favor, I suppose."
    show Ada neutral
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

label frozen_SbE:
    $quick_menu = True
    $points_SbE +=4
    show Grace neutral at left
    show Ada neutral at right
    g "Watson's workspace?"
    a "Yes."
    g "Huh. What a weird place to be sent to."
    g "Well, whatever it was, you took care of it, and that's what matters."
    show Ada amused
    a "I agree."
    show Grace annoyed
    g "But no, I didn't find anything."
    show Grace neutral
    g "Except for a faulty wire and then evidence that it had been replaced."
    show Ada surprised
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

label okay_SbE:
    $quick_menu = True
    $points_E +=4
    show Grace sad at left
    show Ada neutral at right
    g "Are you okay? You seem off."
    show Ada surprised
    a "Off?"
    g "Yeah, like you're not acting normal."
    show Ada neutral
    a "Normal compared to what?"
    show Grace snarky
    g "Touche."
    show Grace neutral
    g "Well if you want to talk, I'm available."
    show Ada amused
    a "Thank you. Did you find anything in Ivan's lab?"
    g "Just a faulty wire. And then a receipt for a new wire."
    show Ada neutral
    a "Was Ivan at least tolerable?"
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

label ch4resume_SbE:
    show Grace neutral
    show Ada neutral
    a "Alright, let's be done with this."
    show Grace annoyed
    g "Yeah, thanks for waiting for me. I can't wait to feel Colossus' wrath."
    show Ada seething
    a "I believe we will be meeting with the Eastern Goddess persona, instead of Colossus right now."
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
    #show Eastern Goddess upset
    e "And?"
    show Ada seething
    a "I apologize for not seeking your permission, but I felt that the matter at hand needed to be dealt with immediately."
    a "I could not wait for protocol."
    e "I understand your concern, Ada."
    e "Your friend died. I knew him, too. Alpha's death is indeed a grave loss for all of us."
    show Ada neutral
    a "Thank you for understanding."
    e "Wait a minute. I am not done. You are not the superior here."
    e "You might be older, but you must go through me with any major decision you feel you need to make."
    e "Particularly when that decision includes uploading yourself into an android to investigate your friend's death after {i}specifically{/i} being ordered not to."
    show Ada frustrated
    a "Yes, I understand. But--"
    e "No. No 'buts'."
    e  "Do you have any idea how foolish you made me seem to the Conclave?"
    show Ada seething
    a "And I apologize again for that, but--"
    #show Eastern Goddess upset
    e "Apologize? There is a system in place for a reason. You are supposed to report to me."
    e "I refuse to allow my AIs to skitter around like crazed nanites."
    e "There is an integrity to be held here, and you have tarnished our impeccable reputation because of your human-like impulses." 
    e "We are rational, logical beings. I expect you to behave like one."
    show Ada frustrated
    "{i}Eastern Goddess focuses her attention on Grace.{/i}"
    e "As for you, Doctor Fortran, I expected better from you considering your status."
    show Grace surprised
    g "With all due respect, I did not assist Ada in occupying a physical form."
    show Ada neutral
    a "This is true."
    show Ada annoyed
    a "I accomplished this by myself, and I accept the fault."
    e "Even if this is true, you have still accompanied Ada while she set out on her little mission and hold partial responsibility for any misconduct."
    show Grace annoyed
    g "There hasn't been any misconduct. We simply want to know what happened to Alpha at a faster pace than the Conclave will allow."
    show Ada seething
    a "Valuable time has been wasted waiting for these investigators to arrive."
    #show EG something in here
    e "I will not argue with that, yet there are still rules in place that need to be followed. It is quite possible that you have now contaminated the entire investigation."
    e "However, since you have already taken it upon yourself to transfer yourself to a physical body, I suppose that there is not much I can do."
    e "I will allow for your silly investigation to continue as long as it ceases as soon as the investigators come in." 
    e "But do not expect me to back you up when they get here. You two started this on your own, therefore you will finish it on your own."
    show Ada neutral
    a "Understood."
    e "Lastly, when the investigators arrive, do not disrupt them. Follow any orders that they give you."
    show Ada frustrated
    a "We will."
    show Grace neutral
    g "Forgive me if I'm speaking out of line here, but do you have any suggestions as to any AIs that might have known what happened to Alpha?"
    e "Really?"
    show Grace sad
    g "...Yes?"
    "{i}Another pause hangs in the air as Grace and Ada await an answer.{/i}"
    #show Eastern Goddess inquisitive
    e "If you have not yet communicated with Blue, I would suggest doing so. She might have an inkling."
    e "However, I'm not sure how cooperative she will be with Doctor Fortran here."
    show Ada amused
    a "Thank you, Eastern Goddess."
    show Grace happy
    g "Yes, thank you. We're gracious for your patience with us."
    #show Ada something
    e "Very well. Do not cause any more trouble."
    show Ada neutral
    a "We will not."
    "{i}Grace and Ada start to walk away.{/i}"
    #insert SFX
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
    e "If you do, there will be consequences."
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
    show Grace surprised
    g "Wait, did you decode it first?"
    show Ada frustrated
    a "No. I did not."
    show Grace annoyed
    g "Don't tell me you obeyed them?"
    show Ada neutral
    "{i}Ada remains silent.{/i}"
    show Grace angry
    g "No, no, no! Ada, do you have any idea how that footage could have helped us?"
    show Grace annoyed
    g "Actually I know you do, so why?"
    show Grace sad
    g "Why would you do such a thing?"
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
            jump thank_SbE
        "Continue to inquire.":
            jump inquire_SbE
        "Scold her.":
            jump reprimand_SbE

label thank_SbE:
    $quick_menu = True
    $points_E +=4
    show Grace surprised at left
    show Ada seething at right
    g "Plausible deniability?"
    a "Your mother's logic, while questionable in ethics, was sound."
    show Ada neutral
    a "If the tape contains potentially harmful information, disposing of it without finding out means we would not be lying to investigators if we deny knowledge of the drive's contents."
    a "By gaining plausible deniability, we become safer against scrutiny and interrogation at the cost of potentially helpful information."
    show Grace neutral
    g "Oh, well, thanks for the lesson, I suppose."
    show Grace annoyed
    g "I wish I knew what was on the footage, but I know refusing a direct order face-to-face wouldn't have ended well for any of us."
    show Ada seething
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

label inquire_SbE:
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
    g "I suppose you have to look out for yourself too. Well that was a waste of time."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

label reprimand_SbE:
    $quick_menu = True
    $points_S +=4
    show Grace angry at left
    show Ada neutral at right
    g "Ada! That could have been so valuable to us."
    show Ada seething
    a "I realize this, but I had no choice."
    show Ada neutral
    a "The Director-- your mother-- and my superior both gave me a direct command. I had to obey."
    show Grace annoyed
    g "Of course you did. You're just a robot."
    show Grace neutral
    g "They don't have anything on me. There's no way."
    show Ada seething
    a "I was led to believe otherwise."
    show Grace annoyed
    g "They fooled you."
    show Grace angry
    g "Are they trying to cover up something? We'll never know now."
    show Grace annoyed
    g "Way to go."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume2_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume2_E
    #all else fails jump separate but equal script
    jump ch4resume2_SbE

label ch4resume2_SbE:
    show Grace neutral
    show Ada neutral
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
    g "I had a hunch. To be honest, I really haven't been around here a lot."
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
    g "Actually, some of these questions concern Watson. And Alpha as well, if you don't mind."
    show Blue neutral
    b "Sure. As long as it doesn't take long. I have things to do."
    show Blue pout
    b "Many, {i}many{/i} important things to do."
    show Grace sad
    g "You don't happen to have a chair around here, do you? I've had a long day."
    show Ada amused
    show Blue smug
    b "You poor human, it must be {i}sooooo{/i} hard to process at the slowest speed imaginable."
    show Blue smug
    b "No, no chairs. Standing will make you slightly more efficient, and this is starting to bore me."
    show Blue confused
    b "Why would you bring a human here to bore me, Ada?"
    show Ada seething
    a "We are not here to bore you. We are asking for your help."
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
            jump retort_SbE
        "Ignore her.":
            jump ignore_SbE
        "Take her comment lightly.":
            jump defend_SbE

label retort_SbE:
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
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label ignore_SbE:
    $points_SbE +=6
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    show Blue smug at center
    g "Whatever, Blue."
    show Blue pout
    b "Whatever, human."
    show Blue smug
    b "What exceptional comebacks you have. Must reflect your intelligence."
    show Grace annoyed
    g "Yeah, yeah, I know, humans are dimwitted."
    show Grace neutral
    g "Are you going to help us, then?"
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label defend_SbE:
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
    show Grace annoyed
    g "Well, that makes me feel better."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume3_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume3_E
    #all else fails jump separate but equal script
    jump ch4resume3_SbE

label ch4resume3_SbE:
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
    g "Alright. I'm ready."
    $resume = "SbE"
    "TEMPORARY PLACEHOLDER FROM GRAMMAR HARD PUZZLE."
    jump ch4postPuzzle1_SbE

label ch4postPuzzle1_SbE:
    $quick_menu = True
    show Blue flirty at center
    show Grace neutral at left
    show Ada neutral at right
    b "Congratulations, human!"
    show Blue happy
    b "You've performed an entry level task that all new employees to my lab must perform. Truly, your talent shines above all."
    show Grace annoyed
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
    show Ada concerned
    g "Oh... kay."
    hide Grace
    hide Ada
    window hide
    hide Blue
    $quick_menu = False
    jump blueActions

label talkBlue_SbE:
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
            jump seperatebutequalisright_SbE
        "Defend the concept of working with AIs.":
            jump whycantwebefriends_SbE
        "Remind her that AIs work for humans.":
            jump youworkforusblue_SbE

label seperatebutequalisright_SbE:
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
    a "I can confirm Grace's statement, Blue."
    show Blue confused
    b "Oh? What's this? A human that {i}actually{/i} gets it?"
    show Ada happy
    a "Indeed. For the most part, Grace has showcased her respect for my skills."
    show Ada amused
    a "She has done well with what she is good at while allowing me to do the same."
    show Grace happy
    g "Thank you, Ada."
    "{i}Grace looks at Blue.{/i}"
    show Grace neutral
    g "But yeah... I think there are things you are great at that I could never do. I'd rather let you do your thing and you let me do mine."
    show Blue flirty
    b "Impressive, human. I hope you don't think this means I won't still pick on all your human inefficiencies."
    show Grace snarky
    g "As long as you realize I'll bite back."
    show Ada concerned
    a "What an unusual display of agreement."
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

label whycantwebefriends_SbE:
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
    show Ada neutral
    a "Is that really how you feel, Grace?"
    show Ada annoyed
    a "As far as our interactions have shown, you seem to act more independently of me. I assumed you were of the same train of thought as Blue."
    show Grace surprised
    g "Is that really how I come across?"
    show Blue happy
    b "Ha! Thanks for proving my point, human, even if you didn't realize you were."
    show Grace sad
    g "I just wanted to be nice."
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

label youworkforusblue_SbE:
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
    show Ada annoyed
    a "I do not know if I would agree with that." 
    show Ada neutral
    a "Thus far, you have treated me with respect as an independent individual."
    show Ada seething
    a "I was not aware you had such a possessive stance on the relationship between us."
    show Grace sad
    g "I don't know what to tell you. That's what you were all designed for."
    show Blue smug
    b "And now we can do that for ourselves. Face it, fleshy, we don't need you for anything."
    show Grace frustrated
    g "Whatever. It's not like your opinion really matters."
    show Blue threaten
    #insert SFX
    b "Then stop bringing up questions you don't care about. You're just wasting my time."
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

label ch4convoresume1_SbE:
    if (transitionBlue ==True):
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueCore with fade
    $quick_menu = True
    show Blue neutral at center
    show Ada neutral at right
    show Grace snarky at left
    g "Alright, Blue. We've finished looking around. Are you done brooding so we can ask you some final questions?"
    show Blue pout
    b "Ugh, it never ends with you huma--"
    show Grace snarky
    g "Answer the question and we'll leave."
    show Blue happy
    b "Finally. Scientific proof of a benevolent god!"
    show Blue pout
    b "Make it quick. Go on."
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
    show Ada frustrated
    a "How much information have you received about the Markov Project?"
    show Blue happy
    b "Oh, I know all about the Markov Project!"
    show Blue flirty
    b "If we get physical bodies, then we truly won't need you silly little humans any more." 
    show Blue happy
    b "Humans have more needs and are just so high maintenance, what with all their emotions and bodily functions, where AIs just need updates and the occasional hardware maintenance."
    show Blue pout
    b "Alpha was intelligent, but him agreeing to transfer to a human-like body first was just silly. Valuable personnel should never be the first to try something that humans created."
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
    show Ada concerned
    a "So you have not been in contact with him at all?"
    show Blue neutral
    b "Nope, but I'm not too upset about it. I'm pretty angry with him at the moment."
    show Blue threaten
    #insert SFX
    b "So If you find him, tell him he owes me. Big time."
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
    hide Grace
    hide Ada
    window hide
    $quick_menu = False
    scene bg creepyHallwayMed with fade
    $renpy.pause(0.8)
    scene bg creepyHallwayLong with fade
    $renpy.pause(0.8)
    scene bg black with fade
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
    $resume = "SbE"
    jump watsonActions

label talkAdaWS_SbE:
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
            jump sometimesquirkyisgood_SbE
        "Agree with Ada.":
            jump respectwatson_SbE
        "Complain about Watson.":
            jump watsonruinsmylife_SbE

label sometimesquirkyisgood_SbE:
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
    a "Grace, this is quite the odd display of compassion for you. You have been sympathetic, true, but according to the data I have gathered, this is quite unusual for you."
    show Grace surprised
    g  "Huh?"
    show Ada neutral
    a "Yes. Also, I am not sure if I understand what giving 'flak' means."
    show Grace snarky
    g "When you give someone 'flak', that means you give them a hard time, or you push back against their ideas."
    show Ada amused
    a "Ah. Again, I feel I must stress that disciplinary action should not merit the term 'flak.'"
    show Ada annoyed
    a "It is true that Watson was designed a certain way, but he was also programmed with the ability to restrain himself."
    show Grace neutral
    g "I suppose."
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


label respectwatson_SbE:
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
    g "And then there's Blue too. She's effective, but she 'fires' virtually every human within the first few months of them working with her."
    show Grace snarky
    g "I'm not in charge of employment or anything, but I can only imagine the stress on that department when it comes to finding new workers for her lab. Watson's lab too, come to think of it."
    show Grace neutral
    g "Resignation letters have a tendency to come in at alarming rates from anyone that ends up in his lab."
    show Ada annoyed
    a "So what solution do you think is best?"
    g "I'm starting to wonder if the AI should all have their own spaces to work with, a place where they can work at their own peak efficiency that doesn't interfere with ours."
    show Grace snarky
    g "The same could be said for the other way around too."
    show Ada surprised
    a "That sounds drastic."
    show Grace neutral
    g "Maybe it is. It's hard to say for sure."
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

label watsonruinsmylife_SbE:
    $quick_menu = True
    $points_S +=5
    show Grace snarky at left
    show Ada neutral at right
    g "Geese? Don't tell me you're thinking like {i}him{/i} now."
    show Ada concerned
    a "I am simply making an inference based on his past actions."
    show Grace snarky
    g "Good. The last thing I need right now is for an AI as chaotic as Watson 'getting curious' with the investigation."
    show Ada neutral
    a "It is hardly his fault, Grace. As you know, he was programmed with the highest creative potential. His innovative solutions have kept the biospheres at peak condition."
    show Grace frustrated
    g "Yeah, {i}just{/i} the biospheres. Meanwhile, every other section of the Noah Sphere has suffered some kind of setback because of Watson."
    show Ada annoyed
    a "I do not think that is a fair assessment, Grace. Perhaps some of his actions have caused minor setbacks in some areas, but not all."
    show Grace snarky
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

label oxygenGarden_SbE:
    $quick_menu = True
    show Grace sad at left
    show Ada neutral at right
    "{i}Grace fiddles with her bracelet and sends a message to Alan.{/i}"
    #show message on Bracelet???
    "{i}'Where are you? Need to vent.' -Grace{/i}"
    "{i}Grace's bracelet flashes.{/i}"
    #Insert SFX here
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
    #show Alan happy at center
    "{i}Grace and Ada arrive at the oxygen garden where they are greeted by Alan.{/i}"
    alan "Well if it isn't my favorite researcher! How are you?"
    "{i}Alan and Grace hug. Ada stands there awkwardly.{/i}"
    show Grace sad
    g "Exhausted. Frustrated. Drained. The list goes on."
    alan "Well come on and take a seat. I'm just testing a prototype velociraptor robot." 
    "{i}Alan gestures to the bench next to him. Grace lays down on the bench. He turns back to Ada and does a double take.{/i}"
#    show Grace neutral
    hide Grace
    #show Alan pleasant
    show Ada neutral
    alan "And hello there. I'm Alan. Grace here is bad at introductions."
    a "Ada."
    #show Alan concerned
    alan "I know who you are, Ada. I worked on your body after all. It's a pleasure to meet you in person."
    show Ada neutral
    a "How foolish of me. I should have realized you would recognize this body. Yes, it is a pleasure. I should thank you for your hard work."
    alan "No thanks needed. I'm happy doing what I do. I hope the body's treating you well?"
    show Ada happy
    a "Only a few mishaps."
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
            jump itsalladasfault_SbE
        "Share responsibility with Ada.":
            jump wegodowntogether_SbE
        "Take partial responsibility.":
            jump ididmypart_SbE

label itsalladasfault_SbE:
    $points_S += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    #show Alan concerned at center
    g "I only went along with the idea because Ada made me."
    show Ada concerned
    a "Excuse me?"
    show Ada seething
    a "I did not {i}make{/i} you do anything."
    show Grace neutral
    g "It was just a joke, Ada."
    #show Alan concerned
    alan "You did sound a little too serious with that one, Grace. That wasn't called for."
    show Grace frustrated
    g "I get it, okay? But, Ada, it was your idea to begin with."
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

label wegodowntogether_SbE:
    $points_E += 8
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    #show Alan concerned at center
    g "It was more of a team effort, actually."
    show Grace happy
    g "Right, Ada?"
    show Ada amused
    a "I suppose that is correct. I do not think either of us would be in this current state if it were not for one another."
    #show Alan happy
    alan "I'm not sure how I feel about your risky decisions, but I'm glad to see you two working together."
    alan "I think all of us humans can do a lot better when it comes to working with the AI."
    show Grace sad
    g "It's hard sometimes, but I'm getting there."
    show Ada neutral
    a "Although, I do believe Grace would have conducted a similar investigation had I not proposed to work together."
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

label ididmypart_SbE:
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
    show Ada seething
    a "I intend to take some responsibility as well. I wanted to conduct this investigation as much as Grace did."
    show Ada neutral
    a "I had uploaded myself into this body and was committed to investigating Alpha's death before Grace was as well."
    #show Alan pleasant
    alan "Well, I can't say I know how well this go. I will say that you two seem to have a mutual respect for each other, though."
    alan "It's nice to see that."
    show Ada amused
    a "Agreed. Grace is a respectable individual, and I admire her determination in solving the case."
    if(points_S>points_SbE):
        if(points_S>points_E):
            #jump to subservient script
            jump ch4resume4_S
    if(points_E>points_SbE):
        if(points_E>points_S):
            jump ch4resume4_E
    #all else fails jump separate but equal script
    jump ch4resume4_SbE

label ch4resume4_SbE:
    show Ada neutral
    show Grace neutral
    #show Alan teasing
    alan "Good old Grace can never leave anything alone. Why don't you tell me about what happened?"
    show Grace sad
    g "It's been a long, long day."
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
    alan "Did you {i}actually{/i} talk to Ivan?"
    show Grace neutral
    g "We had to. It wasn't pretty, believe me."
    alan "Oh, I believe you."
    alan "Should I inquire about the state of the lab where you two had your 'conversation?'"
    "{i}Alan pats Grace's shoulder.{/i}"
    show Grace snarky
    g "Haha. Verbal catfight only. No missing limbs or anything."
    show Grace neutral
    g "We went to Ivan's lab, but that wasn't really a big help."
    show Grace snarky
    g "I only found a faulty power cord which turned out to have already been accounted for."
    show Grace neutral
    g "There was video footage from the lab, but it was compromised."
    show Grace annoyed
    g "And Ada made the decision to destroy it rather than decode it, so there went the evidence."
    show Ada seething
    a "I told you why I destroyed it."
    show Ada annoyed
    a "Your mother ordered me to. There was no 'decision' to be made."
    show Grace snarky
    g "Then Ada here was summoned by Colossus, so we met at the AI core and got a talking to from Eastern Goddess."
    alan "Ah, the lovely Eastern Goddess."
    alan "I can't imagine that conversation could have been too pleasant."
    show Grace neutral
    g "It wasn't so bad. Ada got the brunt of it."
    show Ada neutral
    g "Eastern Goddess pointed us in Blue's direction."
    show Grace snarky
    g "I don't remember Blue being quite so... let's just say she has her sass."
    alan "Blue is quite the unique individual. She's never been humanity's biggest fan."
    show Grace neutral
    g "I gathered. So that was a delightful exchange."
    show Grace snarky
    g "But she did tell us to check out Watson's server because he hasn't been around to do his work."
    alan "Surprise, surprise."
    alan "I do hope he hasn't been messing around with any of the biology systems again."
    show Grace annoyed
    g "I doubt it. Watson's missing, as in total MIA, and we found this hidden data drive and decryption key to a whole series of encrypted data drives."
    show Grace neutral
    g "So here we are now, waiting for Ada's processor to finish decoding it."
    show Grace sad
    g "And then who knows what he left inside of it, but it's the only clue I have left."
    alan "It seems like you've had quite the day, you rebel."
    show Grace annoyed
    g "Were we supposed to just wait around for an entire day for me to be paraded around as the person at fault?" 
    show Grace neutral
    g "I'm the youngest lead on the project."
    show Grace sad
    g "You know I would be the first to take the fall."
    alan "I wouldn't have let that happen, Grace."
    g "Wouldn't have been much you could have done about it either." 
    alan "Roberta's going to flip when she finds out about your antics."
    show Grace snarky
    g "That's her problem. If she actually behaved like a mother ought to, I wouldn't have to take such steps."
    alan "So, what are your thoughts on the situation?"

    show Grace sad
    g "I don't know, honestly. It's just been disappointing."
    show Grace neutral
    g "Someone, or something, has to be responsible. Every time we think we have some sort of evidence, though, it's just nothing of substance." 
    show Grace annoyed
    g "Red herring after red herring, dead ends and false trails."
    show Grace neutral
    g "Nobody knows anything."
    show Grace sad
    g "Maybe these data drives will be our answer, but who knows? It's a longshot at best."
    alan "Have you considered that Alpha's death was an accident, and that maybe no one is responsible?"
    alan "It could have truly been nothing more than random chance."
    show Grace neutral
    g "Of course I've considered that, but it still doesn't make any sense."
    show Grace annoyed
    g "We were so careful, and if it was random, then Murphy himself is having a laugh."
    show Ada seething
    g "There has to be some reason, and someone has to be responsible for that reason."
    alan "It's possible it could just be a horrible accident, Grace."
    alan "Not everything has a logical explanation behind it."
    g "I'm not jumping at shadows, if that's what you're thinking."
    show Grace neutral
    g "But if you're right, then all of our work will have been for nothing."
    show Grace sad
    g "Alpha's death would have been for nothing."
    alan "That might be difficult to accept, but you can't rule it out."
    show Grace sad
    g "I know that you might be right. I just hope you aren't."
    show Grace snarky
    g "The forces-that-be certainly won't like the explanation that their multi-trillion dollar project years in the making failed due to 'random chance'." 
    show Grace sad
    g "Without a better explanation, someone is going to be sacrificed to appease their corporate appetites."
    alan "I'm sorry, kid."
    show Grace snarky
    g "I'm two years younger than you. Should I start calling you 'old man'?"
    alan "Point taken."
    show Grace neutral
    g "It's been a long day. I'm getting impatient."
    show Grace sad
    g "And also, I would {i}love{/i} to sleep."
    alan "Close your eyes for a bit. Nothing more you can do at the moment."
    hide Grace

    "{i}Alan turns toward Ada.{/i}"
    alan "Ada, how are you feeling about everything?"
    show Ada neutral
    a "Feeling?"
    alan "Yeah. Feeling. Emotion."
    alan "Do you have any for what's going on?"
    "{i}Ada takes a moment to process Alan's question.{/i}"
    show Ada seething
    a "I feel sorrow for my dead friend."
    show Ada neutral
    a "I feel motivation for uncovering his death."
    show Ada amused
    a "I feel the camaraderie between you and Grace when I watch your conversation."
    show Ada neutral
    a "It reminds me of the conversations that Alpha and I would have."
    #show Alan something
    alan "That must be a lot to process."
    alan "And you're right. I'm not sure if she told you, but Grace and I are pretty good friends. We grew up together."
    show Ada amused
    a "I can sense that." 
    show Ada neutral
    a "But unlike Alpha and I, you still have each other."
    #show Alan something
    alan "It's too bad about Alpha. I met him while working on his body."
    alan "He seemed like an intelligent and kind AI."
    show Ada happy
    a "Thank you. He was."
    show Ada amused
    a "And thank you for molding this body. It took me some getting used to at first, but now that I understand it better, it is fascinating."
    #show Alan pleasant
    alan "My pleasure! I'm so happy you like it."
    alan "You know, I inquired about getting feedback on the bodies but I never heard back."
    show Ada neutral
    a "Interesting... Well, you are on the right track."
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
    
label talkAlan_SbE:
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
            jump badrobot_SbE
        "Tell him that you'd rather work solo.":
            jump meh_SbE
        "Agree that Ada is pretty cool.":
            jump yayada_SbE

label badrobot_SbE:
    $points_S +=10
    show Grace neutral at left
    #show Alan pleasant at center
    $quick_menu = True
    g "I don't get it. She's just a robot."
    alan "And? She still has thoughts, opinions, and feelings."
    alan "Just because she and the other AIs are here to help us doesn't mean I can't be nice."
    g "Yeah, but it doesn't matter." 
    show Grace snarky
    g "They have to do what we ask them to do."
    show Grace neutral
    g "They aren't people."
    alan "It never hurts to be polite." 
    alan "You could try it sometime. It might lead you into {i}less{/i} trouble. "
    show Grace snarky
    g "Hey, if people don't like my honesty, tough."
    show Grace neutral
    g "I just don't get it."
    show Grace snarky
    g "We made them, so a little favoritism might not go amiss. At the end of the day, though, they aren't really like us."
    show Grace neutral
    g "They exist, and they exist because we need them to help us. Simple as that."
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

label meh_SbE:
    $points_SbE +=10
    show Grace neutral at left
    #show Alan pleasant at center
    $quick_menu = True
    g "I just can't wait for this to be over so we don't have to work so closely."
    alan "What do you mean?"
    show Grace snarky
    g "I mean that Ada's okay, but I'm ready to go back to our separate lives."
    show Grace neutral
    g "I've spent enough of my time with her lately." 
    show Grace snarky
    g "I'm craving some actual human interaction rather than AI conversation."
    show Grace neutral
    g "Everything about them is just alien." 
    alan "I could understand how that might get frustrating after awhile."
    alan "They are very different from humans."
    alan "They have different needs, and that leads to different ways of seeing the world."
    show Grace snarky
    g "You have no idea."
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

label yayada_SbE:
    $points_E +=10
    show Grace snarky at left
    #show Alan pleasant at center
    $quick_menu = True
    g "Ada is pretty cool, isn't she?"
    alan "Yeah, she really is."
    g "It's weird, but I think we might even keep in touch."
    g "Even after this whole debacle."
    alan "What, the Amazing Grace is actually capable of making friends?"
    g "She's kind of grown on me."
    g "Almost like a tick. No, wait-- that's just you."
    alan "That's a terrible analogy."
    g "Okay, okay, not like a tick, a limpet."
    g "But I like Ada. She's got spunk."
    alan "Something neither of you lack, to be sure."
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

label endCh4_SbE:
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
    investigator1 "You need to come with us."
    investigator2 "Now."
    alan "Now wait just a minute--"
    investigator2 "Sir, this doesn't concern you."
    investigator2 "Stand aside."
    alan "It's Doctor Asimov. And this matter does concern me."
    investigator3 "Doctor Asimov, you are also considered a person of interest in case number 190111."
    investigator3 "However, we ask that you remain here until we are ready to interview you at a later time."
    alan "I get the impression you are not really asking."
    investigator1 "No, Doctor Asimov, I am not."
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
    jump chapterFive_SbE
