# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Grace", color ="#006d0d")
define a = Character("Ada", color="#3a416c")
define secretary = Character("Virtual Secretary", color ="#383838") 
define h = Character("Director Hirose", color="8b00bf")
define knuth = Character("Director Knuth", color="#5a0167")
define neva = Character("Director Nevalinna", color="#5a0167")
define cray = Character("Director Cray", color="#5a0167")
define godel = Character("Director Gödel", color="#5a0167")
define b = Character("Blue", color="#0016bb")
define c = Character("Colossus", color="#765e00")
define e = Character("Eastern Goddess", color="#e6e03d")
define w = Character("Watson", color="#000000")
define ivan = Character("Ivan", color="#556b1f")
define lynn = Character("Lynn", color="#ce00a0")
define alan = Character("Alan", color="#005aaf")
define tosh = Character("Tosh", color="#383838")
define mopr = Character("M.O.P.R", color="#ad0000")

image bg bed = "bg bed layout.png"
image bg computer = "bg computer terminal.png"
image bg view = "bg window and lamp.png"
image bg conclaveWaitingRoom = "2_theconclave_A_1.png"
image bg conclaveDoor = "2_theconclave_A1_1.png"
image bg conclave = "2_theconclave_B_2.png"
define dissolve = Dissolve (1.0)

image Tosh neutral = "Tosh_Happy1.png"

define audio.creep = "music/Creep_Wav.ogg"
define audio.digi = "music/Digi_Sprites.ogg"
define audio.robot = "music/robotScanner.ogg"
define audio.sraf = "music/srafTexture.ogg"
define audio.stab = "music/stabTapeEcho.ogg"

init python:
    renpy.music.register_channel("channel00", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel01", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel02", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel03", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel04", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
#Creep_Wav.ogg, #Digi_Sprites.ogg, robotScanner.ogg, sraftexture.ogg, stabTapeEcho.ogg

# The game starts here.

label start:

    play channel00 creep
    play channel01 digi
    play channel02 robot
    play channel03 sraf
    play channel04 stab

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg computer
    with fade
    # This ends the game.

    jump prologue
