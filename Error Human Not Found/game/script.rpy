# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Grace", color ="#0abab5")
define a = Character("Ada", color="#a1c9ee")
define secretary = Character("Virtual Secretary", color ="#ffffff") 
define h = Character("Director Hirose", color="8b1dff")
define knuth = Character("Director Knuth", color="#c088fb")
define neva = Character("Director Nevalinna", color="#c088fb")
define cray = Character("Director Cray", color="#c088fb")
define godel = Character("Director Gödel", color="#c088fb")
define b = Character("Blue", color="#00f9ff")
define c = Character("Colossus", color="#b9b5bd")
define e = Character("Eastern Goddess", color="#4cff61")
define w = Character("Watson", color="#ff7400")
define ivan = Character("Ivan", color="#acc391")
define lynn = Character("Lynn", color="#ffa8e1")
define alan = Character("Alan", color="#ff0000")
define tosh = Character("Tosh", color="#deffe0")
define mopr = Character("M.O.P.R", color="#7990ff")

define merlin = ("Merlin")
image bg bed = "bg bed layout.png"
image bg computer = "bg computer terminal.png"
image bg view = "bg window and lamp.png"
image merlin neutral= "Merlin_neutral.png"
image merlin frustrated = "Merlin_frustrated.png"
image testSprite female = "spriteSizeTest.png"
image testSprite small = "sizeTestSmall.png"
image testSprite med = "sizeTestMedium.png"
image testSprite large = "sizeTestLarge.png"
image testSprite xl = "sizeTestXL.png"
define dissolve = Dissolve (1.0)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg computer
    with dissolve 
    
    show testSprite female
    "Let's do a quick sprite size check."
    
    show testSprite large
    "This is large."
    
    show testSprite med
    "This is medium."
    
    show testSprite small
    "And this is small." 
    
    show testSprite xl
    "And here's extra large."
    
    "This is a test for all the characters and their colors."
    
    g "I'm not just {i}a{/i} character, I'm {i}the{/i} character."
    
    a "Oh please. Everyone knows I do {b}all{/b} the heavy lifting."
    
    secretary "I only appear to tell Grace to wait for her appointment. She ignores me."
    
    h "She doesn't listen to me either."
    
    knuth "Well, we're all generic too."
    
    neva "At least I get a nickname of sorts."
    
    cray "What kind of name is Cray even?"
    hide testSprite female
    with dissolve
    
    godel "I get a special character in my name."
    
    b "Weeeeee! Awww, I don't have my images yet. ಠ_ಠ "
    c "Blue, behave."
    e "Oh, don't mind my other (worse) half."
    w "And I'm dead. Joy."
    ivan "Well don't look at me. That was all your own fault, Watson."
    
    lynn "Aww, the kids do enjoy their squabbles. Did you know--"
    
    alan "I'm sure they probably do, Lynn. Hello everyone!"
    
    tosh "Everyone? I need to log all these visitors."
    
    mopr "BEEEPPP! Beeep-boop."
    
    "Next is a sprite size test. Merlin doesn't have a full body, so he's floating. Oh well."
    
    show merlin neutral at right
    
    merlin "What was that about?"
    
    scene bg bed
    with dissolve
    
    show merlin neutral at center 
    
    merlin "And why am I in space?"
    
    show merlin frustrated
    
    merlin "I have a feeling Morgana is to blame..."
    
    scene bg view
    with fade
    
    show merlin neutral at left
    
    merlin "This is someone's room. I should leave."
    
    hide merlin neutral

    # This ends the game.

    jump prologue
