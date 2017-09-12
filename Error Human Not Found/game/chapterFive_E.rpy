label chapterFive_E:
    $wj_read = False
    scene bg chapterFiveE with fade
    $renpy.pause(3.0)
    scene bg conclaveWaitingRoom with fade 
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    #show Investigator1 neutral
    #show Investigator2
    #show Investigator3
    #Grace and Ada are on the left, Investigators on the right.
    investigator1 "Stay here. We will brief the Conclave."
    "{i}The investigators walk through the metal doors leading the Conclave Chamber.{/i}"
    #investigators leave.
    g "I can't help but get a bad feeling about this."
    show Ada concerned
    a "How so, Grace? Our investigation has been nothing short of exhaustive."
    g "That's just the thing, though."
    show Grace annoyed
    g "We've combed pretty much every possibility, tried out every lead. We don't have anything, just details about how Alpha shorted out."
    show Ada neutral
    a "Grace, we have the data drives."
    show Grace neutral
    g "It's something, but if it isn't anything of importance, then the investigation should be considered a failure."
    show Ada happy
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
            jump adayourayofsunshine_E
        "Continue to vent.":
            jump emograce_E
        "Just acknowledge her.":
            jump okayokayfineada_E

label adayourayofsunshine_E:
    $quick_menu = True
    show Grace happy at left
    show Ada neutral at right
    g "Thanks, Ada. I'm glad that you decided to help me with this."
    show Ada happy
    a "The feeling is mutual. I could not have asked for a better partner in this endeavor."
    show Ada neutral
    a "But, Grace, understand me when I say that our objectives are one and the same, no matter how different our stakes are."
    show Grace neutral
    g "I know, Ada. We both have something to lose."
    show Grace snarky
    g "Even if those things are different, I think that puts us in a pretty similar position."
    show Ada amused
    a "When you say it like that, I feel inclined to agree. I will say, though, you seem to be uneasy. If there is something I could do to help you calm yourself, let me know."
    show Ada neutral
    a "This is something that friends do."
    show Grace sad
    g "Thanks, I appreciate it, but I don't think there's anything you could do."
    show Grace snarky
    g "It's one thing to know that investigators are coming to put the screws to me."
    show Grace sad
    g "It's another thing entirely to stand in a lobby and wait for the screws, however."
    show Grace snarky
    g "It's like waiting at the dentist's office."
    show Ada neutral
    a "I do not recognize this analogy."
    g "Maybe it's because you've got those shiny steel teeth."
    jump intothebooth_E

label emograce_E:
    $quick_menu = True
    show Ada neutral at right
    show Grace angry at left
    g "I hate not knowing what's going on!"
    g "There's no way that someone could do something like this and get off completely scot-free!"
    show Grace annoyed
    g "And why am I taking the blame for this?"
    g "My design works perfectly."
    show Grace angry
    g "You're a walking example of that, Ada!"
    show Ada concerned
    a "Grace, this is not over yet."
    show Ada neutral
    a "Maybe the investigators will find something that will support your case, and we still have the data drives."
    show Grace neutral
    g "I get that you're trying to help, but you don't understand what's at stake for me."
    show Grace angry
    g "If the data drives are a bust, then I'm going down."
    show Grace neutral
    g "The investigators aren't going to find anything that we already haven't."
    show Grace sad
    g "I can lose my whole career for this, Ada."
    show Grace snarky
    g "You might not even get in trouble."
    show Ada surprised
    a "Grace, I--"
    jump intothebooth_E

label okayokayfineada_E:
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    g "Thanks for the confidence, Ada."
    show Ada concerned
    a "I am seeing several signs of elevated stress, Grace. Is everything all right?"
    show Grace sad
    g "Just peachy, Ada."
    show Ada concerned
    a "Peachy?"
    show Grace annoyed
    g "Ada please, I'm trying to think here."
    show Grace surprised
    g "That didn't sound right."
    show Grace sad
    g "Sorry, but I just need some quiet time to think."
    show Ada neutral
    a "Very well, Grace."
    jump intothebooth_E

label intothebooth_E:
    #play SFX
    show Grace neutral
    show Ada neutral
    "{i}The doors to the Conclave Chamber slide open, and Director Hirose comes into view.{/i}"
    #show Hirose neutral
    h "They're ready for you, Grace. Oh, and one more thing."
    #show Hirose concerned
    h "{i}Please{/i} don't get snappy with them. They're already suspicious of you, so you don't need to make things harder for yourself."
    h "I'll be watching from outside with the rest of the Conclave. I'll be delivering their decision on the matter."
    #hide Hirose
    show Ada neutral
    a "This is it, Grace."
    show Grace snarky
    g "Here goes nothing."
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    scene bg conclaveDoor with fade
    $renpy.pause(0.8)
    #play sound
    #queue sound
    scene bg conclave with fade    
    #Transition to the conclave. 
    
    #The lead investigator will stand in the center of the screen.
    $quick_menu = True
    show Ada neutral at right
    show Grace neutral at left
    #show Detective neutral at center
    investigator1 "Director, Chiefs of the Conclave and all others present, we meet today to formally begin our investigation of this incident."
    investigator1 "We are aware of the undue termination of an AI due to a malfunction in its physical body."
    show Ada frustrated
    a "It?"
    investigator1 "The success or failure of the Markov Project is something that is of very keen interest to mankind's future."
    investigator1 "As such, we are taking our investigation extremely seriously."
    a "Alpha was not an it, he was--"
    investigator2 "Ada unit, I will ask you to refrain from interrupting this questioning session."
    investigator2 "Doctor Fortran and yourself have disrupted our investigation quite enough."
    show Ada seething
    a "Understood."
    investigator3 "Now, Doctor Fortran, do you stand ready to undergo questioning?"
    investigator3 "Do you swear that any information you provide us is truthful and accurate?"
    #choice 2
    hide Grace
    hide Ada
    #hide whatever investigator is currently up
    $quick_menu = False
    menu:
        "Swear.":
            jump cursinggrace_E
        "Stall.":
            jump bathroom_E
        "Defend Ada.":
            jump thatsmyadanotyours_E

label cursinggrace_E:
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    #show Detective neutral at center
    g "I swear, everything I tell you is the truth."
    investigator1 "Excellent."
    investigator1 "Maybe we'll be done with this before the day's out."
    show Grace snarky
    g "Well, that all depends on how easy you make this for me."
    investigator3 "Your contentiousness has been noted."
    show Ada surprised
    a "Grace..."
    investigator1 "Is there something you'd like to add, Ada unit?"
    show Ada neutral
    a "No, it is nothing."
    jump paranoiatime_E

label bathroom_E:
    $quick_menu = True
    show Grace annoyed at left
    show Ada neutral at right
    #show Detective neutral at center
    g "We just needed a little bit more time!"
    g "Ada and I were so close to figuring this out."
    show Ada annoyed
    a "I do not see how interrupting us for questioning is efficient."
    investigator1 "I'm sorry, you seem to be under the impression that the investigation you two were carrying out was approved by anyone."
    investigator1 "Wasn't it the explicit orders of a superior to {i}not{/i} investigate?"
    show Grace angry
    g "Yes, but how can you expect someone to sit still when their career's on the line?"
    investigator2 "We {i}expect{/i} people to follow the rules and not tamper with active crime scenes."
    investigator2 "If this were the investigation of a {i}human's{/i} death, you'd be facing several charges."
    show Grace snarky
    g "'If this were the investigation of a {i}human's{/i} death?' Wow, don't sound upset over the loss of Alpha. You could at least show {i}some{/i} respect for the deceased, you know.?"
    investigator1 "You're starting to wear down my patience. Continue like this, and we'll replace you with someone more cooperative."
    investigator1 "Someone who may not be as sympathetic to your situation. Understood?"
    show Grace neutral
    g "Fine, understood. I swear, yadda yadda and all that."
    investigator1 "Thank you. We can finally continue now."
    jump paranoiatime_E

label thatsmyadanotyours_E:
    $quick_menu = True
    show Grace angry at left
    show Ada surprised at right
    #show Detective neutral at center
    g "Hey, don't talk to Ada like that!"
    g "She was a big help, and I wouldn't have gotten as far as I did without her."
    investigator1 "My apologies."
    investigator1 "Perhaps I should treat your accomplice in crime with more respect."
    show Grace annoyed
    g "She just wants to find out why her friend died, all right? Not that you'd care, or anything."
    show Grace sad
    g "Just leave her out of it."
    show Ada happy
    a "Thank you, Grace."
    investigator2 "We're not here to make friends or to avoid offending machines, Doctor Fortran."
    investigator2 "We're here on {i}serious{/i} business. Now, answer my previous question."
    show Grace annoyed
    g "'Machines?' How dare--"
    show Ada neutral
    a "Grace, please."
    show Ada amused
    a "Do not worry about me."
    show Grace neutral
    g "All right then. I swear that what I'll tell you is the truth."
    investigator3 "Thank you."
    jump paranoiatime_E

label paranoiatime_E:
    show Grace neutral
    show Ada neutral
    investigator1 "Now, onto the pressing issue."
    investigator1 "It's to my understanding you carried out your own investigation on this manner."
    show Grace neutral
    g "I did."
    investigator2 "And you're fully aware of the consequences of disrupting an investigation this important with your meddling?"
    #choice 3
    hide Grace
    hide Ada
    #hide Detective
    $quick_menu = False
    window hide
    menu:
        "Continue to give him attitude.":
            jump stayawayfrommecop_E
        "Tell the truth.":
            jump bibleswearing_E
        "Continue to stall.":
            jump badgraces_E

label stayawayfrommecop_E:
    show Grace snarky at left
    show Ada neutral at right
    #show Detective neutral at center
    $quick_menu = True
    g "Oh, I didn't know anything about that."
    g "I was just trying to save my career and bring justice to dead AI. Nothing too important there."
    investigator1 "Your use of the word 'justice' for an artificial entity is questionable, not to mention you're not the only one with a career, Doctor Fortran."
    investigator1 "But since you seem to care so much about your own, I'd much rather advise you not to give me anymore lip."
    show Grace annoyed
    g "Is that a threat, investigator?"
    investigator1 "I don't think I need to tell you whether it is or not. You seem smart enough."
    show Ada concerned
    a "Grace, I appreciate what you're trying to do, but I strongly advise we do not antagonize the investigators."
    investigator1 "Your accomplice is right. You {i}really{/i} don't want to do this with me."
    investigator1 "Now, are you ready to start answering questions?"
    show Grace neutral
    g "If you are."
    jump butwaitthetapetho_E

label bibleswearing_E:
    show Grace neutral at left
    show Ada neutral at right
    #show Detective neutral at center
    $quick_menu = True
    g "I was, but I chose to do this anyways. I wanted to find out what had happened with my design."
    investigator1 "Hmm. I'd ask you a few other things, but it seems you're fully willing to admit this. You've got your convictions, I'll give you that much."
    show Grace sad
    g "You need to believe me when I say that I didn't do this with any malicious intent. I just wanted to make sure that all the angles were covered, for my sake and Ada's."
    investigator1 "And you believed that me and my team wouldn't cover all the angles?"
    show Grace snarky
    g "If it was your livelihood at risk, wouldn't you want the same?"
    show Grace sad
    g "What about if you lost a friend in a similar way? Wouldn't you want--no, need--to know what happened right away?"
    investigator1 "..."
    investigator1 "Moving on."
    jump butwaitthetapetho_E

label badgraces_E:
    show Grace happy at left
    show Ada neutral at right
    #show Detective at center
    $quick_menu = True
    g "Actually, no. Could you kindly fill me in?"
    investigator3 "Fingerprints all over the incident scene, tampering with vital evidence, the list goes on."
    show Grace snarky
    g "But such a diligent team of investigators can just ignore my prints, right? Can't you tell how old they are? I mean, this isn't the twenty-first century."
    show Ada concerned
    a "Please be careful with what you say, Grace. I detect that these three are not amused."
    investigator1 "Thank you for your observation, Ada unit. I don't know how long you've set us back for, Doctor Fortran, but you {i}have{/i} set us back."
    g "I'm terribly sorry to hear that."
    investigator2 "Yeah, I can tell."
    jump butwaitthetapetho_E

label butwaitthetapetho_E:
    investigator1 "Well, that concludes the preliminary initial questioning. Now it's time for the important questions."
    show Grace surprised
    g "What?"
    investigator1 "During the course of your completely unsanctioned investigation, did you actually manage to dig up anything useful?"
    #choice 4
    hide Grace
    hide Ada
    #hide Detective
    $quick_menu = False
    window hide
    menu :
        "Fill him in.":
            jump dontruinmylife_E
        "Just keep on stalling.":
            jump ineedmoretime_E
        "Hold back on the details.":
            jump nottodaysatan_E

label dontruinmylife_E:
    $quick_menu = True
    show Grace neutral at left
    show Ada neutral at right
    #show Detective neutral at center
    g "I'm going to be honest, there wasn't exactly a lot me and Ada could find out in around eighteen hours--"
    investigator1 "I figured as much."
    show Grace annoyed
    g "But!"
    show Grace snarky
    g "We were able to find out a few things about Alpha's death."
    investigator2 "And these details of the Alpha unit's {i}termination{/i} are...?"
    show Grace neutral
    g "He shorted out. Something caused his neural network to draw almost double the requisite power. It must've happened during his maintenance."
    investigator1 "Was there anything unusual about its maintenance cycle?"
    show Grace annoyed
    g "I'm sorry, 'its?'"
    "{i}Ada stops Grace.{/i}"
    show Ada seething
    a "It is fine."
    "{i}Ada turns to face the investigators.{/i}"
    show Ada neutral
    a "No. As far as we know, {i}his{/i} maintenance was optimal."
    investigator3 "Interesting. Was there anything else?"
    show Grace neutral
    g "We also found a data drive on Alpha's person. It should be finished decoding, right, Ada?"
    a "I finished it a few minutes ago, yes."
    investigator1 "Then there isn't any time to waste. Give us this drive immediately."
    jump thetape_E

label ineedmoretime_E:
    $quick_menu = True
    show Grace snarky at left
    show Ada neutral at right
    #show Detective neutral at center
    g "Define 'useful.'"
    investigator1 "Evidence, Doctor Fortran. I don't care about who {i}looks{/i} suspicious or who {i}said{/i} anything. If it's not in a picture or on tape, it didn't happen."
    show Grace annoyed
    g "So you're telling me I could tell you who my lead suspect was and you'd ignore it if I didn't have evidence?"
    investigator1 "Why wouldn't I?"
    show Grace surprised
    g "{i}Excuse{/i} me? This is a serious case. I wouldn't lie about a potential killer of an AI."
    investigator2 "You're a young scientist with no investigative experience conducting an amateurish parody of detective work, as well as possessing a strong motive for seeing anyone but yourself found at fault." 
    investigator1 "You're also stalling, so I'm going to cut to the chase. Audiovisual surveillance places you inside the crime scene, conducting your own detective work. No doubt destroying any credible evidence while you were at it."
    show Grace annoyed
    g "And? You already know what I did, why are you repeating it to me?"
    investigator3 "Because you took something from that place."
    show Grace surprised
    g "I--"
    investigator1 "Don't say anything else. Yes or no, did you or did you not take that drive? If you lie to me, I will have you crunching spreadsheets for a hydrogen mine on the moon. Just some food for thought."
    show Grace angry
    g "Fine, yes! I took a data drive from Alpha's hand."
    investigator1 "Show it to us. Immediately."
    jump thetape_E

label nottodaysatan_E:
    $quick_menu = True
    show Grace annoyed at left
    show Ada neutral at right
    #show Detective neutral at center
    g "It's barely anything. No leads, no suspects, just a shorted out neural network."
    investigator1 "Do you know what caused it to short?"
    show Ada seething
    a "A power usage irregularity. The only thing we know is that it was almost double."
    investigator2 "Well, it sounds like a design issue to me, so far."
    show Ada annoyed
    a "Grace is a strong scientist. I cannot believe that she would allow a design failure such as that through to this stafe."
    investigator2 "Perhaps there's something else then?"
    show Grace neutral
    g "No, there's nothing else."
    investigator2 "Absolutely nothing else?"
    show Grace annoyed
    g "No."
    investigator3 "So if I showed you security footage of you picking a data drive off of the Alpha unit's chassis, you'd give me the same answer?"
    show Grace surprised
    g "I, erm..."
    show Grace annoyed
    g "No, sir."
    investigator1 "Hand it over, then. Your attempt to conceal this information has been noted."
    jump thetape_E

label thetape_E:
    "{i}Grace hands the lead investigator Alpha's thumbdrive.{/i}"
    investigator1 "Let's see here..."
    $resume = "E"
    hide Grace
    #hide Detective 
    hide Ada
    $quick_menu = False
    window hide
    jump watsonJournal_1
    #Display Watson's Journal

label ch5_E_resume:
    hide other darken
    $quick_menu = True
    show Grace surprised at left
    show Ada seething at right
    #show Detective neutral at center
    a "Watson? It was Watson the entire time?"
    show Grace annoyed
    g "It explains a lot. Like why he was absent."
    investigator1 "I don't know what to say. This is quite unprecedented."
    show Ada annoyed
    a "But why would he do this? Yes, he said he wanted a body, but he {i}knew{/i} he would be getting one once his turn came up."
    investigator1 "Is this the first sign of his deviation?"
    #play SFX doorOpen1
    #play SFX doorClose1
    h "I will answer that."
    #show Hirose pensive
    
    investigator1 "Director Hirose? You were instructed to wait outside--"
    h "You are on {i}my{/i} space station, as a courtesy, Detective. You do not give {i}me{/i} instructions. Besides, we have made our judgement."
    h "The Watson unit has a history of putting his responsibilities in second place to his curiosities. This isn't the first time he's gone missing, but he always performs his tasks on time."
    investigator1 "Director, this is troubling news for us."
    h "I suppose it would be to those who have not worked alongside these AIs for years."
    #show Hirose pensive
    h "Given the current events, the Conclave has deemed humans and AIs to coexist in an equal society. We acknowledge that the life of an AI is just as valuable as a human's and they deserve the same recognition for their work."
    h "This situation with Alpha and Watson has proven to the Conclave that AIs are our equals. These were not the actions of machines, cool and rational, but rather of emotional, living beings."
    h "Our observations of how Doctor Fortran and Ada worked together on this also informed our opinion."
    h "Although their investigation was unwarranted, Grace and Ada were able to work together to gather evidence that was crucial to the initial crime."
    show Grace surprised
    g "And the Markov Project?"
    #show Hirose something
    "{i}Hirose sighs.{/i}"
    h "The project will continue. AIs and humans will continue to work together, and AIs will be given more android bodies and the same rights as humans."
    #show Hirose something
    h "You're not off the hook, Ada, but your service and determination for your fallen friend has not gone unnoticed. Your dedication has resonated with the Conclave, and we appreciate all that you have done."
    show Ada amused
    a "Director Hirose, I-- thank you. Very much. This is a giant step for AIs."
    h "Yes, well we believe that with AIs as our equals, our society could be capable of great things."
    investigator1 "Very well."
    investigator1 "Doctor Fortran, Ada unit, you're dismissed. It seems this investigation's solved itself."
    show Grace snarky
    g "What about the ladies who helped solve it?"
    investigator1 "You compromised a potential investigation scene and tampered with evidence. However, you also provided the means to solve the investigation. I rule that it balances out to absolute zero."
    show Grace surprised
    g "But--"
    investigator1 "Be thankful. We will continue to investigate in case something else comes up, but for the most part, this investigation is over."
    h "Thank you, Detective, Officers. Grace, Ada, it's now time to discuss your reprimanding."
    hide Ada
    #hide Hirose
    #Hirose disappears. Ada goes with her.
    investigator1 "Sounds like you're going to get off a little easier than I hoped."
    show Grace snarky
    g "So sorry to disappoint you. Well, I wish I could say it has been a pleasure, but I'd rather not lie."
    g "Besides, you don't know my mother."
    
    $quick_menu = False
    #insert SFX door
    #queue SFX door
    scene bg conclaveDoor with fade
    $renpy.pause(0.8)
    scene bg conclaveWaitingRoom with fade 
    #show Hirose angry at center
    show Grace neutral at left
    show Ada neutral at right
    #Ada and Grace are on the same side
    $quick_menu = True
    #Ada and Grace are on the same side
    h "Your work on Alpha's case has been a great help, the both of you, but I gave you very specific instructions that you disobeyed."
    show Grace annoyed
    g "Did you honestly think I was going to just sit in my lab and do nothing?"
    h "No, but to mess with the scene... do you know how much trouble you two could've been in?"
    show Grace sad
    g "I thought it was worth the risk."
    show Ada seething
    a "I am sorry to disappoint you, Director."
    "{i}Hirose sighs.{/i}"
    #show Hirose pensive
    h "Okay. Okay. I'm just glad this is over. I was worried, I really was."
    show Ada neutral
    a "What happens now?"
    h "Just relax. Enjoy the rest of your day. The project's going to be on pause anyways, as they continue to close up the investigation. I'll have a lot of forms to sign."
    show Grace surprised
    h "And whatever you do, try not to do anything that the Conclave will hear about. At least for a day or two. I need a break."
    #hide Hirose
    show Grace snarky
    #Hirose leaves
    g "So I guess we have our answer."
    show Ada seething
    a "I still cannot believe it was Watson. I thought I knew him."
    show Grace sad
    g "It happens to all of us, Ada. Watson was always a wild card, there was no way to know that he would do what he did."
    show Grace happy
    g "On the bright side, we're finally equals! That means we can work together more often."
    show Ada surprised
    a "Finally equals? Oh dear."
    show Grace surprised
    g "Did you just make a joke? You've come so far."
    show Ada amused
    a "You have rubbed off on me quite a bit."
    show Ada happy
    a "I did not realize that this would be the outcome of our investigation, but I must admit I feel some sort of gratifying emotion about it all."
    show Grace snarky
    g "Hope? Excitement? Just happiness in general?"
    show Ada amused
    a "Yes, I think all of those. To think that I played a part in changing the future between humans and AI's satisfies me beyond thought."
    show Ada happy
    a "I would not have been able to have done this without you, Grace."
    show Grace happy
    g "And I would not have been able to do it without you. We did this together."
    "{i}A moment of appreciative silence passes between them.{/i}"
    g "Well after this crazy day, I think I need to relax a little. I'm gonna go hang out with Alan. Come with me."
    show Ada surprised
    a "Hang out?"
    show Grace snarky
    g "Not literally hang out. But enjoying each other's company. I wouldn't subject you to ruining your new body so quickly."
    show Ada amused
    a "Ha, ha, ha, ha, ha!"
    show Grace happy
    g "Ada! That laugh was excellent! You're making jokes and laughing now, who would have thought."
    show Ada happy
    a "Thank you. I have a great teacher."
    show Ada amused
    a "May I suggest we find something more... normal to do?"
    show Grace snarky
    g "What? And be boring, normal people?"
    show Ada neutral
    a "..."
    g "I'm kidding. That sounds great."
    show Ada amused
    a "I know."
    "{i}Ada and Grace leave.{/i}"
    #FANFARE. THE END. THAT'S ALL FOLKS. BYE-BYE NOW.
    #insert jump to credits
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    return

