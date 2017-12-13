label chapterFive_S:
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
    scene bg chapterFiveS with fade
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
    a "And the data drives, Grace?" 
    show Grace neutral
    g "It's something, but if it isn't anything important, then we're sunk."
    show Ada happy
    a "I'm confident that if Alpha perished with the drive in his hand, it must have been incredibly important."
    show Ada neutral
    a "The truth will be revealed."
    #choice 1
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    menu:
        "Appreciate her effort.":
            jump goodtrybeepboop_S
        "Continue to vent.":
            jump leavemealonemom_S
        "Just acknowledge her.":
            jump iguessillacknowledgeyou_S

label goodtrybeepboop_S:
    $quick_menu = True
    show Grace happy at left
    show Ada neutral at right
    g "Thanks, Ada. I'm glad that you decided to help me with this."
    show Ada surprised
    a "Really? That is not the impression I have been receiving."
    show Ada neutral
    a "Despite that, though, I know that even though our stakes are different, our objective is the same."
    show Grace neutral
    g "I know I've been cruddy, Ada. It's just stress is all."
    show Grace annoyed
    g "It's one thing to know that investigators are coming to put the screws to me, and it's another thing to stand in a lobby and wait for the screws."
    show Grace angry
    g "It's like waiting at the dentist's."
    show Ada neutral
    a "I do not recognize this analogy."
    show Grace snarky
    g "Maybe it's because you've got those shiny steel teeth."
    jump intothebooth_S

label leavemealonemom_S:
    $quick_menu = True
    show Ada neutral at right
    show Grace angry at left
    g "I hate not knowing what's going on! There's no way that someone could do something like this and get out completely scot-free!"
    g "And why am I taking the blame for this? My design works perfectly." 
    show Grace annoyed
    g "You're a walking example of that, Ada!"
    show Ada concerned
    a "Grace, this is not over yet. Maybe the investigators will find something that will prove us both right, either on the station or in the data drive."
    show Grace sad
    g "If the data drives a bust, then I'm going down. The investigators aren't going to find anything that we already haven't."
    show Grace angry
    g "You aren't as concerned as me, Ada. I can lose my whole career for this. What do you have to lose? Nothing."
    a "Grace, I--"
    show Grace annoyed
    g "I'm the new scientist on the station, and the thing that shorted out, the thing that {i}killed{/i} Alpha, was designed by me."
    show Grace sad
    g "They're going to throw me to the wolves."
    jump intothebooth_S

label iguessillacknowledgeyou_S:
    $quick_menu=True
    show Grace neutral at left
    show Ada neutral at right
    g "Thanks for the confidence, Ada."
    show Ada concerned
    a "I am seeing several signs of elevated stress, Grace. Is everything all right?"
    show Grace sad
    g "Just peachy, Ada."
    a "Peachy?"
    show Grace annoyed
    g "Ada please, I'm trying to think here. It'd be incredibly useful if you didn't disturb me."
    show Ada frustrated
    a "..."
    jump intothebooth_S

label intothebooth_S:
    play sound doorOpen2
    queue sound doorClose2
    show Grace neutral
    show Ada neutral
    "{i}The doors to the conclave chamber slide open to reveal Director Hirose.{/i}"
    show Hirose neutral at center
    h "They're ready for you, Grace. Oh, and one more thing..."
    show Hirose annoyed
    h "{i}Please{/i} don't get snappy with them. They're already suspicious of you, so you don't need to make things harder for yourself."
    show Hirose concerned
    h "I'll be watching from outside with the rest of the Conclave. I'll be delivering their decision on the matter."
    hide Hirose
    show Ada neutral
    a "This is it, Grace. Remember, I just need a little more time."
    show Grace snarky
    g "That's what you said earlier, too. Sure seems like a long five minutes."
    a "I am going as fast as I can."
    show Grace neutral
    g "Here goes nothing."
    hide Grace
    hide Ada
    $quick_menu = False
    play sound01 adaWalk
    play sound02 graceWalk
    window hide
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
    investigator1 "Director, Chiefs of the Conclave, and all others present, we meet today to formally begin our investigation of this incident."
    investigator1 "We are aware of the undue termination of an AI due to a malfunction in its physical body."
    show Ada frustrated
    a "It?"
    investigator1 "The success or failure of the Markov Project is something that is of very keen interest to mankind's future, and as such, we will take our investigation extremely seriously."
    a "I'm not going to stand for a fellow AI being treated like an obj--"
    show Detective behind inv1
    show inv2 behind inv1
    investigator2 "Ada unit, I will ask you to refrain from interrupting this questioning session. You and Doctor Fortran have disrupted our investigation enough."
    show Ada seething
    a "Very well."
    show Detective behind inv2
    show inv1 behind inv2
    investigator3 "Now, Doctor Fortran, do you stand ready to undergo questioning? Do you swear that any information you provide us is truthful and accurate?"
    #choice 2
    hide Grace
    hide Ada
    hide Detective
    hide inv1
    hide inv2
    $quick_menu = False
    menu: 
        "Swear.":
            jump goodgraces_S
        "Stall.":
            jump leavemealoneinvestigator_S
        "Defend Ada.":
            jump thatsmyrobotyouretalkinto_S

label goodgraces_S:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace neutral at left
    show Ada neutral at right
    g "I swear, everything I tell you is the truth."
    investigator1 "Excellent. Maybe we'll be done with this before the day's out."
    show Grace snarky
    g "Well, that all depends on how easy you make this for me."
    show Detective behind inv2
    investigator3 "Your contentiousness has been noted."
    show Ada seething
    a "Grace, did I not ask that--"
    show inv2 behind Detective
    investigator1 "Ada unit, I will not say this again. Do not interrupt me."
    jump paranoiatime_S

label leavemealoneinvestigator_S:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace annoyed at left
    show Ada neutral at right
    g "We just needed a little bit more time! Ada and I were so close to figuring this out."
    show Ada annoyed
    a "I do not see how interrupting us for questioning is efficient."
    investigator1 "I'm sorry, you seem to be under the impression that the investigation you two were carrying out was approved by anyone."
    investigator1 "Did you not receive explicit orders from a superior to {i}not{/i} investigate?"
    show Grace angry
    g "Yes, but how can you expect someone to sit still when their career's on the line?"
    investigator1 "We {i}expect{/i} people to follow the rules and not tamper with active crime scenes. If this were the investigation of a {i}human's{/i} death, you'd be facing several charges."
    show Grace snarky
    g "Well, I guess I'm lucky it isn't, aren't I?"
    investigator1 "You're starting to wear down my patience. Continue like this, and we'll replace you with someone more cooperative."
    investigator1 "Someone who may not be as sympathetic to your situation. Understood?"
    show Grace neutral
    g "Fine, understood. I swear, yadda yadda and all that."
    investigator1 "Thank you. We can finally continue now."
    jump paranoiatime_S

label thatsmyrobotyouretalkinto_S:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace angry at left
    show Ada surprised at right
    g "Hey, don't talk to Ada like that! She was a big help, and I wouldn't have gotten as far as I did without her."
    investigator1 "My apologies. Perhaps I should treat your accomplice with more respect."
    show Grace annoyed
    g "She just wants to find out why her friend died, all right? Leave her out of it."
    show Ada happy
    a "Grace? I did not expect something like that. Thank you."
    show Detective behind inv1
    show inv2 behind inv1
    investigator2 "We're not here to make friends or to avoid offending machines, Doctor Fortran. I'm here on {i}serious{/i} business. Now, answer my previous question."
    show Ada neutral
    a "Go ahead, Grace. I would rather not waste processing power arguing."
    show Grace neutral
    g "All right then. I swear that what I'll tell you is the truth."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Thank you."
    jump paranoiatime_S

label paranoiatime_S:
    show Grace neutral
    show Ada neutral
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Now, onto the pressing issue."
    investigator1 "It's to my understanding you carried out your own investigation on this manner."
    g "I did."
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
        "Give him attitude.":
            jump sassygracestrikesback_S
        "Tell the truth.":
            jump goodlittlegrace_S
        "Continue to stall.":
            jump bathroomstall_S

label sassygracestrikesback_S:
    show inv1
    show inv2
    show Detective
    show Grace snarky at left
    show Ada neutral at right
    $quick_menu = True
    g "Oh, I didn't know anything about that. I was just trying to save my career. Nothing too big there."
    investigator1 "You're not the only one with a career, Doctor Fortran. But since you seem to care so much about your own, I'd much rather advise you not to give me anymore lip."
    show Grace annoyed
    g "Is that a threat, investigator?"
    investigator1 "I don't think I need to tell you whether it is or not. You seem smart enough."
    show Ada concerned
    a "Grace, please do not take this any further. I know where this behavior leads."
    investigator1 "Your accomplice is right. You {i}really{/i} don't want to do this with me."
    investigator1 "Now, are you ready to start answering questions?"
    show Grace snarky
    g "If you are."
    jump butwaitthetapetho_S

label goodlittlegrace_S:
    show inv1
    show inv2
    show Detective
    show Grace neutral at left
    show Ada neutral at right
    #show Detective neutral at center
    $quick_menu = True
    g "I was, but I chose to do this anyways. I wanted to find out what had happened with my design."
    investigator1 "Hmm. I'd ask you a few other things, but it seems you're fully willing to admit this. You've got your convictions, I'll give you that much."
    show Grace sad
    g "You need to believe me when I say that I didn't do this with any malicious intent. I just wanted to make sure that all the angles were covered."
    investigator1 "And you believed that me and my team wouldn't cover all the angles?" 
    show Grace snarky
    g "If it was your livelihood at risk, wouldn't you want the same?"
    investigator1 "..."
    investigator1 "Moving on."
    jump butwaitthetapetho_S

label bathroomstall_S:
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
    a "Grace, please... These allegations are serious. Your attitude will not help the situation."
    show inv2 behind Detective
    show inv1 behind Detective
    investigator1 "Thank you for your concensus, Ada unit. I don't know how long you've set us back for, Doctor Fortran, but you {i}have{/i} set us back."
    g "I'm terribly sorry to hear that."
    show inv2 behind inv1
    show Detective behind inv1
    investigator2 "Yeah, I can tell."
    jump butwaitthetapetho_S

label butwaitthetapetho_S:
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Well, that concludes the initial questioning, now comes the actually important ones."
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
            jump yougotmecopper_S
        "Just keep on stalling.":
            jump graceinthetoilet_S
        "Hold back on the details.":
            jump waitjustaminute_S

label yougotmecopper_S:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace neutral at left
    show Ada neutral at right
    g "I'm going to be honest, there wasn't exactly a lot that me and Ada could find out in around eighteen hours."
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
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Was there anything unusual about its maintenance cycle?"
    show Ada seething
    a "No. As far as we know, {i}his{/i} maintenance was optimal."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Interesting. Was there anything else?"
    show Grace snarky
    g "We also found a data drive on Alpha's android. It should be finished decoding, right, Ada?"
    show Ada neutral
    a "I finished it just a few seconds ago, yes."
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Then there isn't any time to waste. Give us this drive immediately."
    jump thetape_S

label graceinthetoilet_S:
    $quick_menu = True
    show inv1
    show inv2
    show Detective
    show Grace snarky at left
    show Ada neutral at right
    g "Define 'useful.'"
    investigator1 "Evidence, Doctor Fortran. I don't care about who {i}looks{/i} suspicious or who {i}said{/i} anything. If it's not in a picture or on tape, it didn't happen."
    show Grace annoyed
    g "So you're telling me that I could tell you who my lead suspect was and you'd ignore it if I didn't have evidence?"
    investigator1 "Why wouldn't I?"
    show Grace surprised
    g "Excuse me? Are you going to start treating {i}me{/i} like a machine now?"
    show inv2 behind inv1
    show Detective behind inv1
    investigator2 "You're a young scientist with no investigative experience conducting an amateurish parody of detective work, as well as possessing a strong motive for seeing anyone but yourself found at fault." 
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "You're also stalling, so I'm going to cut to the chase."
    investigator1 "Audiovisual surveillance places you inside the crime scene conducting your own detective work. no doubt destroying any credible evidence while you were at it."
    show Grace annoyed
    g "And? You already know what I did, why are you repeating it to me?"
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "Because you took something from that place."
    show Grace surprised
    g "I--"
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Don't say anything else. Yes or no, did you or did you not take that drive? If you lie to me, I will have you crunching spreadsheets for a hydrogen mine on the moon."
    investigator1 "Just some food for thought."
    show Grace angry
    g "Fine, yes! I took a data drive from Alpha's hand."
    investigator1 "Show it to us. Immediately."
    jump thetape_S

label waitjustaminute_S:
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
    show inv2 behind inv1
    show Detective behind inv1
    investigator2 "So far, it sounds like a design issue, unless you've got something else?"
    show Grace snarky
    g "No, there's nothing else."
    investigator3 "Absolutely nothing else?"
    show Grace neutral
    g "No, sir."
    show inv1 behind inv2
    show Detective behind inv2
    investigator3 "So if I showed you security footage of you picking a data drive off of the Alpha unit's chassis, you'd give me the same answer?"
    show Grace surprised
    g "I, erm..."
    show Grace annoyed
    g "No."
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Hand it over, then. Your attempt to conceal this information has been noted."
    jump thetape_S

label thetape_S:
    "{i}Grace hands the lead investigator Alpha's thumbdrive.{/i}"
    show inv1 behind Detective
    show inv2 behind Detective
    investigator1 "Let's see here..."
    $resume = "S"
    hide Grace
    hide Detective 
    hide inv1
    hide inv2
    hide Ada
    $quick_menu = False
    window hide
    jump watsonJournal_1
    #Display Watson's Journal

label ch5_S_resume:
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
    investigator1 "Is this the first sign of his deviation?"
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
    h "The Watson unit has a history of putting his responsibilities in second place to his curiosities."
    h "This isn't the first time he's gone missing, but he always performs his tasks on time."
    investigator1 "Director, this is troubling news for us."
    show Hirose thoughtful
    h "Yes, I suppose it would be." 
    show Hirose neutral
    h "Regardless, we discussed this decision at length. While I cannot say that I am proud of it, we rule by consensus."
    show Grace surprised
    g "Oh no."
    show Hirose angry
    h "Recent events have caused a rift among the members of the Conclave. Seeing that AIs have potential to murder others, accidental or otherwise, has given us pause."
    h "Until we're reassured, AIs will be relegated to roles strictly in support of humans."
    show Grace sad
    g "And the Markov Project?"
    "{i}Hirose sighs.{/i}"
    show Hirose annoyed
    h "The Markov Project as we know it will change. We appreciate Alan's work beautifying the bodies, but the Conclave has decided such measures will be unnecessary."
    show Hirose neutral
    h "The bodies will be utilitarian, specialized for their purpose."
    show Ada surprised
    a "Wait, what about me? What are AIs going to be doing?"
    show Hirose thoughtful
    h "Terraforming, for a start. Preparing planets for human habitation."
    show Hirose concerned
    h "As for you, Ada, I feel it'd be rather improper to tear you out of that body and put you in a different one."
    show Ada seething
    show Hirose neutral
    h "You will remain aboard the Noah Sphere and maintain your assistant position, albeit under heavy supervision." 
    a "Where are you sending my friends?"
    show Hirose thoughtful
    h "Europa comes to mind. Small body with a harsh environment. It'll make a good test for future terraforming missions."
    investigator1 "Very well."
    investigator1 "Doctor Fortran, Ada unit, you're dismissed. It seems this investigation's solved itself."
    show Grace snarky
    g "And me? I helped solve it after all."
    investigator1 "You compromised a potential investigation scene and tampered with evidence."
    investigator1 "However, you also provided the means to solve the investigation. I rule that it balances out to absolute zero."
    show Grace surprised
    g "But--"
    investigator1 "Be thankful. We will continue to conduct interviews in case something else comes up, but for the most part, this investigation is over."
    h "Thank you, Detective, Officers. Grace, Ada, outside the Conclave. Now."
    hide inv1
    hide inv2
    hide Ada
    hide Hirose
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
    stop sound01
    show Hirose angry at center
    show Grace neutral at left
    show Ada seething at right
    #Ada and Grace are on the same side
    $quick_menu = True
    h "Grace, I gave you very specific instructions!"
    show Grace snarky
    g "Did you honestly think I was going to just sit in my lab and do nothing?"
    show Hirose annoyed
    h "No, but to mess with the scene... Grace, do you know how much trouble you could've been in?"
    show Grace neutral
    g "I thought it was worth the risk."
    "{i}Hirose sighs.{/i}"
    show Hirose thoughtful
    h "Okay. Okay. I'm just glad this is over, Grace. I was worried. I really was."
    show Ada annoyed
    a "I am so happy that your worries have been banished. It is not like I have any problems."
    show Hirose angry
    h "What did you want me to do, Ada? Just pretend that there wasn't any harm done?"
    show Hirose annoyed
    h "That a sentient being wasn't destroyed by the apparent {i}impatience{/i} of what we thought was a rational AI?"
    show Hirose angry
    h "Just be fortunate that the program wasn't completely shut down. To think we thought we'd be beyond the point of rogue AIs..."
    "{i}Ada scoffs.{/i}"
    show Ada seething
    a "You are right, it is not all bad. Maybe I will get to talk to Blue or some of my other friends when they are not busy putting up {i}girders!{/i}"
    show Ada annoyed
    a "I need to go tell Colossus. Although, he is probably going to be Eastern Goddess by the time he gets around to talking to you, {i}Grace.{/i}"
    hide Ada
    play sound01 adaWalk
    "{i}Ada storms off. It takes awhile for the metallic stomping of her feet to finally get out of earshot.{/i}"
    stop sound01
    show Hirose annoyed
    h "I really wish that she took that better. This was already going to be a pain to handle without Ada rallying against me."
    show Grace sad
    g "In her defense, the day she's had has been, well, {i}pretty bad{/i} to say the least."
    #show Hirose pensive
    h "We've all had a bad day. I lost a valuable worker and friend, just like Ada. You almost lost your career, and the whole station's been in a state that's less than {i}productive.{/i}"
    show Grace snarky
    g "I'm not sure if that was sympathy for me or not, but I'll take what I can get."
    "{i}Hirose chuckles, ever so slightly.{/i}"
    show Grace surprised
    g "No way! Did you just have an emotion?"
    show Hirose pleased
    h "To be honest, Grace, I needed some form of levity, even if it's your snark."
    show Hirose concerned
    h "I've had nothing but puffed up Chiefs, livid calls from corporate, and {i}Ivan{/i} of all people pouring their words right into my ears."
    show Grace snarky
    g "Ivan, huh? What was he calling about?"
    show Hirose pleased
    h "Why, to make a ton of recommendations in your favor, of course!"
    show Hirose neutral
    h "You know why he called."
    show Grace neutral
    g "Am I in trouble?"
    show Hirose pleased
    h "If murdering fragile egos was a crime, then yes."
    #show Hirose amused?
    show Grace surprised
    show Hirose thoughtful
    h "I, unfortunately, am not in a position to ensure that those egos stay dead, but I can ensure that there are no consequences."
    show Grace neutral
    show Hirose neutral
    h "For now, Grace, you are free to return to your lab. Take a day off, if you want to. You're going to need the down time."
    h "We're going to be crunching in order to implement the most recent changes to the Markov Project's plan."
    show Grace happy
    g "Thanks. I think I'm going to go pass out in my room now."
    show Hirose pleased
    h "Oh, to be young and have time for naps."
    hide Hirose
    show Grace neutral at center
    play sound beepLoud
    "{i}DING!{/i}"
    g "A message?"
    "{i}'Hey, are you still on the hotseat? If you're not, I know the mess hall's serving rice and beans today. Care to catch some with me?'-Alan{/i}"
    show Grace happy
    g "Sure, why not."
    #insert jump to credits
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    "{i}Grace's journal has updated.{/i}"
    $achievement.Sync()
    $achievement.sync()
    $achievement.grant("ACH_SUB")
    $journal6="S"
    $pageUnlocked_journal+=2
    jump credits