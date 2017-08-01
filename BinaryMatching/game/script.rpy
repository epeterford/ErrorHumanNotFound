# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image bg binary = "tileBackground.png"
# The game starts here.

label start:
    $ binaryScreen = Position(xpos=0.45, xanchor =0.0, ypos =0.4, yanchor = 0.0)
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg binary
    "Let's start the game."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
label doAgain:
    "Here we go again."
    menu:
        "Binary match easy.":
            call binaryMatchEasy#memoria_game
        "Binary match medium.":
            call binaryMatchMedium
        "Binary match hard.":
            call binaryMatchHard
        "End the game":
            jump endGame
    "Before the jump."
    jump doAgain
#    jump binaryMatchEasy
    # This ends the game.
    
label endGame:
    "The end."
    return
