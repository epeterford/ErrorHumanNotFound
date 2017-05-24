label chapterOne:
    #show Grace Neutral
    g "Here we are. Open."

    "The door does not budge."

    tosh "The Director is not here at the moment. Please make an appointment."
    #Tosh's sprite isn't displayed here

    #show Grace annoyed
    g "What? I usually have access!"

    #show Ada nervous
    a "And why do you have access to the Director's office?"

    #show Grace neutral
    g "Because she's my mother."
    #show Grace surprised
    g "You… didn't know?"

    #show Ada neutral
    a "That point was never present in my databanks."

    #show Grace snarky
    g "Yeah, that's mom for you. Why bother with unimportant details like family?"

    #show Ada neutral
    a "Regardless, we need to get inside."
    a "Let me get the door."

    #show Ada neutral
    a "..."

    #show Grace neutral
    g "And this is supposed to…?"

    #show Ada concerned
    a "I seem to be having a malfunction. I can usually do this with a thought…"

    menu:
        "Let her know what's wrong.":
            jump notin
        "Remind her she has a body.":
            jump usuallyinaserver
        "Sass her.":
            jump tryandguess

label notin:
    #show Grace neutral
    g "You're not in the system anymore, Ada."
    g "Any connection you had to the system left with you."

    #show Ada neutral
    a "Interesting. I'd hoped to have retained my connection to the sphere's network."
    g "Yeah, do you want your circuits lightly salted while you're at it? You'd have fried in seconds."
    #show Ada Concerned
    a "What? I thought these neural networks were supposed to preserve me."
    g "Just preserve you. Wireless interfacing was going to be a feature in the next model."
    jump doorhack

label usuallyinaserver:
    #show Grace neutral
    g "Well, the server you left was connected to everything."
    #show Grace happy
    g "Welcome to the physical world!"
    
    #show Ada neutral
    a "I do not see why this warrants a positive response."
    a "This is going to be a challenge."

    #show Grace Snarky
    g "well, it can't be that hard. The humans can do it, so you can too!"
    #show Ada Amused
    a "I suppose I can find that reassuring."
    #show Grace Surprised
    g "Hey!"
    jump doorhack

label tryandguess:
    #show grace snarky
    g "I'll give you a few guesses to find the issue."
    
    #show Ada neutral
    a "Is that sarcasm I'm detecting?"
    
    #show Grace neutral
    g "No, I was legitimately giving you a couple of guesses."
    
    #show Ada Frustrated
    a "I am not sure if I appreciate this affordance."
    g "I mean, if you don't know then you don't know. I think it's incredibly obvious."
    a "This discussion is pointless. I'm not going to waste anymore time or processing space on it."
    #show Ada Neutral
    jump doorhack

label doorhack:
    #Show Grace Neutral
    g "Let me try the door."
    g "Watch my back."
    
    #Show Ada Neutral
    a "What are you doing?"

    #Show Grace Snarky
    g "Gall it a manual override."

    #begin door hacking puzzle here, resume script once the puzzle concludes.

    #show Grace Happy
    g "Yes!" 
    #show Grace Neutral
    g "Quick, get in!"

    #transition to hirose's office with a fade.
    #show Ada nervous
    a "Again, I really don't think this course of action is advisable."

    #show Grace Neutral
    g "If it makes you feel better, this isn't the first time I've done this."

    #show Ada Neutral
    a "Elaborate."
    g "Let's just say that whoever updates key card access needs to do their job faster."

    #transition to Hirose's desk
    #show Grace Neutral
    g "It almost hurts to admit it, but I'm so incredibly jealous of this office."

    #Begin the sequence that allows the players to look around Hirose's office. 
    #5 items split among 2 viewpoints: 
    #Viewpoint 1 is the desk itself. Items are. Pens, a cup of herbal brew, the base of Tosh's hologram projector, and the computer.
    #Viewpoint 2 is the window. The item is the window and the view of open space past it.
    #Once the player clicks on the computer, continue with the script.

    g "Alright, this'll only take me a mom--"
    #show Tosh Pleasant
    tosh "Hello, Dr. Fortran!"

    #show Ada nervous
    a "So, this is where Tosh is centered..."
    #show tosh neutral
    tosh "Sorry for not greeting you, I didn't notice you come in."
    tosh "Chairwoman Hirose isn't here at the moment. What is the purpose of your visit?"

    menu:
        "Try to bluff her.":
            jump failtosh1
        "Dismiss her.":
            jump failtosh2
        "Use your rank.":
            jump succeedtosh

label failtosh1:
    #show Tosh Pleasant
    tosh  "Oh! That's no issue, then. Let me just contact her to confi--"
    #show Ada Frustrated
    a "Hold on!"
    tosh "Hmm?"
    jump toshgetsroasted
    
label failtosh2:
    #show Grace Frustrated
    #show Tosh Alarmed
    tosh "Failure to supply a response means I have to contact Chairwoman Hirose, Dr. Fortran."
    #show Ada Frustrated
    a "You will do no such thing, Tosh."
    jump toshgetsroasted

label succeedtosh:
    #show Tosh Pleasant
    tosh "Reviewing familial protocols…"
    tosh "Precedent supports your argument. You may proceed."
    
    #show Grace Happy
    g "Thank you kindly, Tosh."
    
    tosh "I'll just log your visit so the Chairwoman can se--"
    #show Ada Neutral
    a "Belay that, Tosh. There'll be no logging of any kind."
    jump toshgetsroasted

label toshgetsroasted:
    #show Tosh Alarmed
    tosh "Who are you? You don't have a badge or serial number…"

    #show Ada Neutral
    a "I'm Ada. Ring a bell?"

    #show Tosh Pleasant
    tosh "Forgive me, Ada, I didn't recognize you! You're looking very human today."
    tosh "Please leave. You do not have the authorization to be here."
    
    #show Ada Frustrated
    a  "What is your purpose, Tosh?"

    tosh "To serve Chairwoman Hirose to the best of my ability. Please vacate the premises."
    #show Ada Happy
    a "I control your update schedule, Tosh."
    #show Ada neutral
    a "If your next update were to completely destroy your scheduling capability, you'd be reformatted for sure…"

    #show Tosh Alarmed
    tosh "..."
    #show Tosh Pleasant
    tosh "You may stay."

    a "And?"
    tosh "And I will not log this visit."

    #show Ada Amused
    a "Thank you for your cooperation, Tosh."

    menu:
        "Approve, but keep it orderly.":
            jump sepbutequal1
        "Scold her.":
            jump subservient1
        "Compliment her.":
            jump equal1

label sepbutequal1:
    #show Grace Neutral
    g "That was good thinking, but let me know the next time you're planning to threaten my mom's secretary VI."
    
    #show Ada Neutral
    a "Will do, Grace. I didn't think there was time to warn you."
    a "Now, let me see the computer, we don't have time to guess passwords."
    #[Begin Ada's Puzzle]
    jump wegotthedeets
    
label subservient1:
    #show Ada Neutral
    a "..."
    a "Noted. Let me see the computer, we'll get done quicker if I'm doing this."
    #[Begin Ada's Puzzle]
    jump wegotthedeets
    
label equal1:
    #show Ada Happy
    a "Far from the hardest thing I've ever done."
    #show Ada Neutral
    a "Now, let's see the computer. This shouldn't take me too long."
    #[Begin Ada's Puzzle]
    #After Ada's puzzle: jump wegotthedeets
    jump wegotthedeets

label wegotthedeets:
    #show Grace Happy
    g "We've got it!"
    #Show Grace Neutral
    g "Let's get back to my lab. We've got some work to do before we can use this."

    #Transition to Grace's Lab here
    "Grace inserts her keycard into her terminal. It boots up, and she runs an update program."
    #show Grace Happy
    g "There. My keycard's copying Hirose's access protocols."
    #show Grace Neutral
    g "That run-in with Tosh was too close."
    #show Ada Amused
    a "Until I took care of it rather handily, I'd say."

    menu:
        "Comment on her expression.":
            jump sortaroastada
        "Be dismissive.":
            jump actuallyroastada
        "Crack a joke.":
            jump toshgotwrecked

label sortaroastada:
    #show Grace Surprised
    g "Did you enjoy that?"
    #show Ada Neutral
    a "Hm?"
    #show Grace Snarky
    g "Talking down Tosh like that. I can't help but notice the giant grin on your face."
    "Ada pauses, and she reaches up to touch her face."
    #show Ada Concerned
    a "I didn't realize. I was not trying to be cruel, Grace."
    g "Well, I guess even machines like pecking downwards every once in a while."
    a "I'm not familiar with that colloquialism."
    g "Just watch my mother for long enough. She does the same thing."
    jump endChapterOne

label actuallyroastada:
    #show Grace Annoyed
    g "You did your job. Nothing more."
    g "I could've done that by myself."
    #show Ada Frustrated
    a "I beg to differ. I don't have to help you here, Grace."
    "Grace sighs."
    #show Grace Neutral
    g "I didn't ask for you to help. You're the one who wanted to come along."
    #show Ada Seething
    a "Noted."
    jump endChapterOne

label toshgotwrecked:
    #show Grace Happy
    g "I've got to say, I never liked that VI."
    #show Ada Amused
    a "Really?"
    #show Grace Neutral
    g "Too chipper for my liking. It's like she's too helpful."
    a "Have you considered the possibility that you detest Tosh because you often see her with your mother?"
    #show Grace Surprised
    g "What?! I would never!"
    #show Grace Neutral.
    g "..." 
    #show Grace Snarky
    g "You're probably right."
    jump endChapterOne

#end the chapter here, go to Chapter 2
label endChapterOne:
    "For now, this is the end."
    return
