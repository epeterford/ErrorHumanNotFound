label chapterFive_SbE:
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
    play music ch5BGM
    $wj_read = False
    scene bg chapterFiveSbE with fade
    $renpy.pause(3.0)
    scene bg conclaveWaitingRoom with fade 
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    show inv1
    show inv2
    show Detective
    #Grace and Ada are on the left, Investigators on the right.
    investigator1 "Stay here. We will brief the Conclave."
    "{i}The investigators walk through the metal doors leading the Conclave Chamber.{/i}"
    #investigators leave.
    hide inv1
    hide inv2
    hide Detective
    play sound doorOpen2
    queue sound doorClose2
    g "I can't help but get a bad feeling about this."
    show Ada concerned
    a "How so, Grace? Our investigation has been nothing short of exhaustive."
    g "That's just the thing, though."
    show Grace annoyed
    g "We've combed pretty much every possibility, tried out every lead. We don't have anything, just details about how Alpha shorted out."
    show Ada neutral
    a "And the data drives, Grace?" 
    show Grace neutral
    g "It's something, but if it isn't anything of importance, then the investigation should be considered a failure."
    show Ada seething
    a "I am confident that if Alpha perished with the drive in his hand, it must have been incredibly important."
    show Ada neutral
    a "I believe our efforts will bear results, Grace."
    #choice 1
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    menu:
        "Appreciate her effort.":
            jump imcheeredupnow_SbE
        "Continue to vent.":
            jump irefusetocheerup_SbE
        "Just acknowledge her.":
            jump yeahgeethanksada_SbE

label imcheeredupnow_SbE:
    $quick_menu = True
    show Grace happy at left
    show Ada neutral at right
    g "Thanks, Ada."
    g "I'm glad that you decided to help me with this."
    show Ada happy
    a "I know that our stakes in this are very different."
    show Ada neutral
    a "But, Grace, understand me when I say that our objectives are one and the same."
    show Grace neutral
    g "I know, Ada. It's just stress is all."
    show Grace snarky
    g "It's one thing to know that investigators are coming to put the screws to me."
    show Grace sad
    g "It's another thing entirely to stand in a lobby and wait for the screws, however."
    show Grace annoyed
    g "It's like waiting at the dentist's office."
    show Ada neutral
    a "I do not recognize this analogy."
    show Grace snarky
    g "Maybe it's because you've got those shiny steel teeth."
    jump intothebooth_SbE

label irefusetocheerup_SbE:
    $quick_menu = True
    show Ada neutral at right
    show Grace angry at left
    g "I hate not knowing what's going on! There's no way that someone could do something like this and get off completely scot-free!"
    show Grace annoyed
    g "And why am I taking the blame for this?"
    g "My design works perfectly." 
    show Grace angry
    g "You're a walking example of that, Ada!"
    show Ada concerned
    a "Grace, this is not over yet."
    show Ada neutral
    a "Maybe the investigators will find something that will support your case, and we still have the data drives."
    show Grace sad
    g "If the data drives are a bust, then I'm going down."
    show Grace neutral
    g "The investigators aren't going to find anything that we already haven't."
    show Grace annoyed
    g "You aren't as concerned as me, Ada."
    show Grace sad
    g "I can lose my whole career for this. What do you have to lose? Nothing."
    show Ada neutral
    a "Grace, I--"
    jump intothebooth_SbE

label yeahgeethanksada_SbE:
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Thanks for the confidence, Ada."
    show Ada concerned
    a "I am seeing several signs of elevated stress, Grace. Is everything all right?"
    show Grace sad
    g "Just peachy, Ada."
    show Ada surprised
    a "Peachy?"
    show Grace annoyed
    g "Ada please, I'm trying to think here."
    show Grace neutral
    g "Just give me some space."
    show Ada frustrated
    a "..."
    jump intothebooth_SbE

label intothebooth_SbE:
    play sound doorOpen2
    queue sound doorClose2
    show Grace neutral
    show Ada neutral
    "{i}The doors to the Conclave Chamber slide open, and Director Hirose comes into view.{/i}"
    show Hirose neutral at center
    h "They're ready for you, Grace. Oh, and one more thing."
    show Hirose annoyed
    h "{i}Please{/i} don't get snappy with them. They're already suspicious of you, so you don't need to make things harder for yourself."
    show Hirose concerned
    h "I'll be watching from outside with the rest of the Conclave. I'll be delivering their decision on the matter."
    hide Hirose
    a "This is it, Grace."
    show Grace snarky
    g "Here goes nothing."
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    play sound01 adaWalk
    play sound02 graceWalk
    scene bg conclaveDoor with fade
    $renpy.pause(0.8)
    play sound doorOpen2
    queue sound doorClose2
    scene bg conclave with fade 
    stop sound01 fadeout 0.5
    stop sound02 fadeout 0.5
    #Transition to the conclave. 
    
    #The lead investigator will stand in the center of the screen. 
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Ada neutral at right
    show Grace neutral at left
    investigator1 "Director, Chiefs of the Conclave and all others present, we meet today to formally begin our investigation of this incident."
    investigator1 "We are aware of the undue termination of an AI due to a malfunction in its physical body."
    show Ada frustrated
    a "It?"
    investigator1 "The success or failure of the Markov Project is something that is of very keen interest to mankind's future."
    investigator1 "As such, we are taking our investigation extremely seriously."
    a "Alpha was not an it, he was--"
    show Detective behind inv1
    show inv2 behind inv1
    investigator2 "Ada unit, I will ask you to refrain from interrupting this questioning session."
    investigator2 "Doctor Fortran and yourself have disrupted our investigation quite enough."
    show Ada seething
    a "Understood."
    show Detective behind inv2
    show inv1 behind inv2
    investigator3 "Now, Doctor Fortran, do you stand ready to undergo questioning?"
    investigator3 "Do you swear that any information you provide us is truthful and accurate?"
    #choice 2
    hide Grace
    hide Ada
    hide Detective
    hide inv1
    hide inv2
    $quick_menu = False
    menu: 
        "Swear.":
            jump beagoodgirl_SbE
        "Stall.":
            jump beanaughtygirl_SbE
        "Defend Ada.":
            jump dontsassmyrobot_SbE

label beagoodgirl_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace neutral at left
    show Ada neutral at right
    g "I swear, everything I tell you is the truth."
    investigator1 "Excellent."
    investigator1 "Maybe we'll be done with this before the day's out."
    show Grace snarky
    g "Well, that all depends on how easy you make this for me."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Your contentiousness has been noted."
    jump paranoiatime_SbE

label beanaughtygirl_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace annoyed at left
    show Ada neutral at right
    g "We just needed a little bit more time!"
    g "Ada and I were so close to figuring this out."
    show Ada annoyed
    a "I do not see how interrupting us for questioning is efficient."
    investigator1 "I'm sorry, you seem to be under the impression that the investigation you two were carrying out was approved by anyone."
    investigator1 "Wasn't it the explicit orders of a superior to {i}not{/i} investigate?"
    show Grace angry
    g "Yes, but how can you expect someone to sit still when their career's on the line?"
    show Detective behind inv1
    show inv2 behind inv1
    investigator2 "We {i}expect{/i} people to follow the rules and not tamper with active crime scenes."
    investigator2 "If this were the investigation of a {i}human's{/i} death, you'd be facing several charges."
    show Grace annoyed
    g "Some respect for the deceased, {i}that{/i} is."
    show inv2 behind Detective
    show inv1 behind Detective
    investigator1 "You're starting to wear down my patience."
    investigator1 "Continue like this, and we'll replace you with someone more cooperative."
    investigator1 "Understood?"
    show Grace snarky
    g "Fine, understood. I swear, yadda yadda and all that."
    investigator1 "Thank you. We can finally continue now."
    jump paranoiatime_SbE

label dontsassmyrobot_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace angry at left
    show Ada surprised at right
    g "Hey, don't talk to Ada like that!"
    g "She was a big help, and I wouldn't have gotten as far as I did without her."
    investigator1 "My apologies."
    investigator1 "Perhaps I should treat your accomplice in crime with more respect."
    show Grace annoyed
    g "She just wants to find out why her friend died, all right? Leave her out of it."
    show Ada happy
    a "Thank you, Grace."
    show Detective behind inv1
    show inv2 behind inv1
    investigator2 "We're not here to make friends or to avoid offending machines, Doctor Fortran."
    investigator2 "We're here on {i}serious{/i} business. Now, answer my previous question."
    show Ada neutral
    a "Go ahead, Grace. Do not worry about me."
    show Grace neutral
    g "All right then. I swear that what I'll tell you is the truth."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Thank you."
    jump paranoiatime_SbE

label paranoiatime_SbE:
    show Grace neutral
    show Ada neutral
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Now, onto the pressing issue."
    investigator1 "It's to my understanding you carried out your own investigation on this manner."
    show Grace neutral
    g "I did."
    show Detective behind inv1
    show inv2 behind inv1
    investigator2 "And you're fully aware of the consequences of disrupting an investigation this important with your meddling?"
    #choice 3
    hide Grace
    hide Ada
    hide Detective
    hide inv1
    hide inv2
    $quick_menu = False
    window hide
    menu:
        "Continue to give him attitude.":
            jump sassthepoliceman_SbE
        "Tell the truth.":
            jump beagoodnoodle_SbE
        "Continue to stall.":
            jump youreprobablygoingtospacejail_SbE

label sassthepoliceman_SbE:
    show Grace snarky at left
    show Ada neutral at right
    show inv1
    show inv2
    show Detective
    $quick_menu = True
    g "Oh, I didn't know anything about that."
    g "I was just trying to save my career. Nothing too important there."
    investigator1 "You're not the only one with a career, Doctor Fortran."
    investigator1 "But since you seem to care so much about your own, I'd much rather advise you not to give me anymore lip."
    show Grace annoyed
    g "Is that a threat, investigator?"
    investigator1 "I don't think I need to tell you whether it is or not. You seem smart enough."
    show Ada concerned
    a "Grace, I would not advise taking this any further."
    investigator1 "Your accomplice is right. You {i}really{/i} don't want to do this with me."
    investigator1 "Now, are you ready to start answering questions?"
    show Grace neutral
    g "If you are."
    jump butwaitthetapetho_SbE

label beagoodnoodle_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace neutral at left
    show Ada neutral at right
    g "I was, but I chose to do this anyways. I wanted to find out what had happened with my design."
    investigator1 "Hmm. I'd ask you a few other things, but it seems you're fully willing to admit this. You've got your convictions, I'll give you that much."
    show Grace sad
    g "You need to believe me when I say that I didn't do this with any malicious intent. I just wanted to make sure that all the angles were covered, for my sake and Ada's."
    investigator1 "And you believed that me and my team wouldn't cover all the angles?"
    show Grace snarky
    g "If it was your livelihood at risk, wouldn't you want the same?"
    investigator1 "..."
    investigator1 "Moving on."
    jump butwaitthetapetho_SbE

label youreprobablygoingtospacejail_SbE:
    show inv1
    show inv2
    show Detective
    show Grace happy at left
    show Ada neutral at right
    $quick_menu = True
    g "Actually, no. Could you kindly fill me in?"
    show Detective behind inv2
    show inv1 behind inv2
    investigator3 "Fingerprints all over the incident scene... Tampering with vital evidence... The list goes on."
    show Grace snarky
    g "But such a diligent team of investigators can just ignore my prints, right? Can't you tell how old they are? I mean, this isn't the twenty-first century."
    show Ada concerned
    a "These allegations are serious, Grace."
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Thank you for your concensus, Ada unit. I don't know how long you've set us back for, Doctor Fortran, but you {i}have{/i} set us back."
    g "I'm terribly sorry to hear that."
    show Detective behind inv1
    show inv2 behind inv1
    investigator2  "Yeah, I can tell."
    jump butwaitthetapetho_SbE

label butwaitthetapetho_SbE:
    show Grace neutral
    show Ada neutral
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Well, that concludes the preliminary questioning, now come the important ones."
    show Grace surprised
    g "What?"
    investigator1 "During the course of your completely unsanctioned investigation, did you actually manage to dig up anything useful?"
    #choice 4
    hide Grace
    hide Ada
    hide Detective
    hide inv1
    hide inv2
    $quick_menu = False
    window hide
    menu :
        "Fill him in.":
            jump givethetapeover_SbE
        "Just keep on stalling.":
            jump theywillnotbreakme_SbE
        "Hold back on the details.":
            jump notapeforyou_SbE

label givethetapeover_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace neutral at left
    show Ada neutral at right
    g "I'm going to be honest, there wasn't exactly a lot that me and Ada could find out in eighteen hours."
    investigator1 "I figured as much."
    show Grace annoyed
    g "Wait a second."
    show Grace snarky
    g "We were able to find out a few things about Alpha's death."
    show inv2 behind inv1
    show Detective behind inv1
    investigator2 "And these details of the Alpha unit's {i}termination{/i} are...?"
    show Grace neutral
    g "He shorted out. Something caused his neural network to draw almost double the requisite power. It must've happened during his maintenance."
    investigator1 "Was there anything unusual about its maintenance cycle?"
    show Ada seething
    a "No. As far as we know, {i}his{/i} maintenance was optimal."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Interesting. Was there anything else?"
    g "We also found a data drive on Alpha's person. It should be finished decoding, right, Ada?"
    show Ada neutral
    a "I finished it a few minutes ago, yes."
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Then there isn't any time to waste. Give us this drive immediately."
    jump thetape_SbE

label theywillnotbreakme_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace snarky at left
    show Ada neutral at right
    g "Define 'useful.'"
    investigator1 "Evidence, Doctor Fortran. I don't care about who {i}looks{/i} suspicious or who {i}said{/i} anything. If it's not in a picture or on tape, it didn't happen."
    show Grace annoyed
    g "So you're telling me I could tell you who my lead suspect was and you'd ignore it if I didn't have evidence?"
    investigator1 "Why wouldn't I?"
    show Grace surprised
    g "Excuse me?"
    show inv2 behind inv1
    show Detective behind inv1
    investigator2 "You're a young scientist with no investigative experience conducting an amateurish parody of detective work, as well as possessing a strong motive for seeing anyone but yourself found at fault." 
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "You're also stalling, so I'm going to cut to the chase. Audiovisual surveillance places you inside the crime scene conducting your own detective work. No doubt destroying any credible evidence while you were at it."
    show Grace annoyed
    g "And? You already know what I did, why are you repeating it to me?"
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Because you took something from that place."
    show Grace surprised
    g "I--"
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Don't say anything else. Yes or no, did you or did you not take that drive? If you lie to me, I will have you crunching spreadsheets for a hydrogen mine on the moon. Just some food for thought."
    show Grace angry
    g "Fine, yes! I took a data drive from Alpha's hand."
    investigator1 "Show it to us. Immediately."
    jump thetape_SbE

label notapeforyou_SbE:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace annoyed at left
    show Ada neutral at right
    g "It's barely anything. No leads, no suspects... Just a shorted out neural network."
    investigator1 "Do you know what caused it to short?"
    show Ada seething
    a "A power usage irregularity. The only thing we know is that it was almost double."
    investigator1 "So far, it sounds like a design issue, unless you've got something else?"
    show Grace neutral
    g "No, there's nothing else."
    show inv2 behind inv1
    show Detective behind inv1
    investigator2 "Absolutely nothing else?"
    show Grace annoyed
    g "No."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "So if I we showed you security footage of you picking a data drive off of the Alpha unit's chassis, you'd give me the same answer?"
    show Grace surprised
    g "I, erm..."
    show Grace annoyed
    g "No, sir."
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Hand it over, then. Your attempt to conceal this information has been noted."
    show Ada annoyed
    a "Grace, you are smarter than this. I do not understand."
    jump thetape_SbE

label thetape_SbE:
    "{i}Grace hands the lead investigator Alpha's thumbdrive.{/i}"
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Let's see here..."
    $resume = "SbE"
    hide Grace
    hide Detective 
    hide inv1
    hide inv2
    hide Ada
    $quick_menu = False
    window hide
    jump watsonJournal_1

label ch5_SbE_resume:
    hide other darken
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace surprised at left
    show Ada seething at right
    a "Watson? It was Watson the entire time?"
    show Grace annoyed
    g "It explains a lot. Like why he was absent."
    investigator1 "I don't know what to say. This is quite unprecedented."
    show Ada annoyed
    a "But why would he do this? Yes, he said he wanted a body, but he {i}knew{/i} he would be getting one once his turn came up."
    investigator1 "Is this the first sign of its deviation?"
    play sound doorOpen2
    queue sound doorClose2
    show inv1 at invLeft
    show inv2 at invRight
    show Hirose thoughtful at nearLeft
    show Ada at right
    show Detective at invLeft
    h "I will answer that."
    investigator1 "Director Hirose? You were instructed to wait outside--"
    show Hirose angry
    h "You are on {i}my{/i} space station, as a courtesy, Detective. You do not give {i}me{/i} instructions. Besides, we have made our judgement."
    show Hirose neutral
    h "The Watson unit has a history of putting his responsibilities in second place to his curiosities. This isn't the first time he's gone missing, but he always performs his tasks on time."
    investigator1 "Director, this is troubling news for us."
    show Hirose pleased
    h "I suppose it would be to those who have not worked with AIs for years."
    show Hirose thoughtful
    h "Given the current events, the Conclave have deemed humans and AIs unfit for complete coexistence. We acknowledge that the life of an AI is just as valuable as a human's, but we simply do not mix."
    show Hirose neutral
    h "This situation with Alpha and Watson has proven to the Conclave that AIs would be best independent from humans. Our observations of how Doctor Fortran and Ada worked together on this also informed our opinion."
    show Hirose annoyed
    h "AIs are intelligent life-forms, capable of self-governing. However, because of our differences, trying to apply our laws to them is simply not reasonable."
    show Grace surprised
    g "And the Markov Project?"
    "{i}Hirose sighs.{/i}"
    show Hirose concerned
    h "The project will continue. AIs and humans will continue to work together, but AIs will be given a separate home of their own to live in, a place they can govern that will be treated like it's own sovereign state."
    show Ada surprised
    a "Where?"
    show Hirose neutral
    h "Well, we were thinking about one of the planets up on the rotation for terraforming. It would be somewhere close enough where we could observe what was happening and engage in trade, but far enough so that the AIs have their space."
    investigator1 "Very well."
    investigator1 "Doctor Fortran, Ada unit, you're dismissed. It seems this investigation's solved itself."
    show Grace snarky
    g "What about the ladies who helped solve it?"
    investigator1 "You compromised a potential investigation scene and tampered with evidence. However, you also provided the means to solve the investigation. I rule that it balances out to absolute zero."
    show Grace neutral
    g "But--"
    investigator1 "Be thankful. We will continue to investigate in case something else comes up, but for the most part, this investigation is over."
    h "Thank you for your time, officers. Grace, Ada, outside the Conclave. Now."
    hide Ada
    hide Hirose
    hide inv1
    hide inv2
    #Hirose disappears. Ada goes with her.
    investigator1 "Heh. Sounds like she's going to give you a worse reaming than I did."
    show Grace snarky
    g "You don't know the half of it."

    $quick_menu = False
    play sound01 graceWalk
    play sound doorOpen2
    queue sound doorClose2
    scene bg conclaveDoor with fade
    $renpy.pause(0.8)
    scene bg conclaveWaitingRoom with fade 
    show Hirose angry at center
    show Grace neutral at left
    show Ada neutral at right
    stop sound01
    #Ada and Grace are on the same side
    $quick_menu = True
    h "Grace, I gave you very specific instructions!"
    show Grace annoyed
    g "Did you honestly think I was going to just sit in my lab and do nothing?"
    show Hirose annoyed
    h "No, but to mess with the scene... Grace, do you know how much trouble you could've been in?"
    show Grace sad
    g "I thought it was worth the risk."
    "{i}Hirose sighs.{/i}"
    show Hirose thoughtful
    h "Okay. Okay. I'm just glad this is over, Grace. I was worried. I really was."
    show Ada neutral
    a "What happens now?"
    show Hirose pleased
    h "Just relax. Enjoy the rest of your day. The project's going to be on pause anyways, because of this investigation."
    show Hirose annoyed
    h "And whatever you do, try not to do anything that the Conclave will hear about, at least for a day or two. I need a break."    #Hirose leaves
    hide Hirose
    show Grace neutral
    g "So I guess we have our answer."
    show Ada seething
    a "I still cannot believe it was Watson. I thought I knew him."
    show Grace sad
    g "It happens to all of us, Ada. So, do you think you're going to leave the Noah Sphere with the rest of the AIs."
    show Ada neutral
    a "Perhaps. I feel like it would be nice to make something with my fellow AIs."
    show Grace happy
    g "That sounds nice, not having to worry about making money to eat or to have a bed to sleep on."
    show Ada happy
    a "It would be a most efficient society, yes."
    show Grace snarky
    g "I'd bet. Month-long congressional debates, all resolved in a few seconds by quantum processors. Just promise not to make us look too bad, all right?"
    show Ada surprised
    a "I am not sure I understand this sentiment. Why would we hold the desire to subvert humans?"
    show Grace happy
    "{i}Grace laughs.{/i}"
    show Grace snarky
    g "Don't mind me. I've seen too many old movies."
    g "I'm gonna go hang out with Alan. Wanna come?"
    show Ada neutral
    a "That sounds like an inefficient use of our time."
    g "Exactly."
    show Ada amused
    a "Well, I suppose it would not do that much harm."
    "{i}Ada and Grace leave.{/i}"
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    "{i}Grace's journal has updated.{/i}"
    $achievement.Sync()
    $achievement.sync()
    $achievement.grant("ACH_SEP")
    $achievement.Sync()
    $achievement.sync()
    $journal6="SbE"
    $pageUnlocked_journal+=2
    jump credits
