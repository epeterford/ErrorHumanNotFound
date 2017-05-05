# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define eric = Character("ThunderWolf")
define j = Character("MetalElephant")
define merlin = ("Merlin")
image bg bed = "bg bed layout.png"
image bg computer = "bg computer terminal.png"
image bg view = "bg window and lamp.png"
image merlin = "Merlin_neutral.png"
define dissolve = Dissolve (1.0)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    eric "This is a test print"
    
    eric "Is the coolet kid in town!"
    
    j "What a blowhard..."
    
    scene bg computer
    with dissolve 
    
    show merlin at right
    
    merlin "What was that about?"
    
    scene bg bed
    with dissolve
    
    show merlin at center 
    
    merlin "And why am I in space?"
    
    scene bg view
    with fade
    
    show merlin at left
    
    merlin "This is someone's room. I should leave."
    
    hide merlin

    # This ends the game.

    jump prologue
