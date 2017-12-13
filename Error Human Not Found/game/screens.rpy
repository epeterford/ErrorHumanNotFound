################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action:
                activate_sound "music/UI/Dialogue_Select/EHNF_UI_DialogueSelect_Click.ogg"
                hover_sound "music/UI/Dialogue_Select/EHNF_UI_DialogueSelect_Highlight.ogg"


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        imagebutton: #Journal
            idle "journal_idle.png"
            hover "journal_hover.png"
            xpos 646
            ypos 989
            focus_mask True
            action ShowMenu("journal")
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg"
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        imagebutton: #Preferences
            idle "prefs_idle.png"
            hover "prefs_hover.png"
            xpos 1278 #1490
            ypos 989
            focus_mask True
            action ShowMenu('preferences')
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg"
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        imagebutton: #History
            idle "history_idle.png"
            hover "history_hover.png"
            xpos 1068
            ypos 989
            focus_mask True
            action ShowMenu('history')
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg"
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        imagebutton: #Save
            idle "save_idle.png"
            hover "save_hover.png"
            xpos 1489 #1279
            ypos 989
            focus_mask True
            action ShowMenu('save')
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg"
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        imagebutton: #Skip
            idle "skip_idle.png"
            selected "skip_hover.png"
            hover "skip_hover.png"
            xpos 857
            ypos 989
            focus_mask True
            action Skip() alternate Skip(fast=True, confirm=True)
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg"
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    import math
    config.overlay_screens.append("quick_menu")
    #config.overlay_screens.append("game_menu")

#default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation_mm():
    imagemap:
        ground "navigation_mm_idle.png"
        idle "navigation_mm_idle.png"
        hover "navigation_mm_hover.png"
        selected_idle "navigation_mm_selected.png"
        selected_hover "navigation_mm_selected.png"
            
        hotspot (12, 52, 315, 95) action Start() activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (12, 155, 315, 95) action ShowMenu("load") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (12, 283, 315, 95) action ShowMenu("preferences") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (12, 407, 315, 95) action ShowMenu("help") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (12, 538, 315, 95):
            if(databasePage ==1):
                action ShowMenu("database1")
            if(databasePage==2):
                action ShowMenu("database2")
            if(databasePage==3):
                action ShowMenu("database3")
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        hotspot (12, 669, 315, 95) action ShowMenu("about") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (12, 797, 315, 95) action ShowMenu ("mmCredits_start") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>" 
        hotspot (12, 896, 315, 95) action Quit(confirm=True) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (27, 976, 290, 85) action Return() activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#Return

screen navigation():
    #Implement hotspot imagemap here
    imagemap:
        ground "gui/overlay/side_menu.png"
        idle "gui/overlay/side_menu.png"
        hover "gui/overlay/side_menu_hover.png"
        selected_idle "gui/overlay/side_menu_selected.png"
        selected_hover "gui/overlay/side_menu_selected.png" 
        hotspot (27, 180, 290, 72) action ShowMenu ("journal") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (27, 243, 290, 85) action ShowMenu("history") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#History
        hotspot (27, 330, 290, 83) action ShowMenu("save") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#Save
        hotspot (27, 413, 290, 85) action ShowMenu("load") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#Load
        hotspot (27, 498, 290, 85) action ShowMenu("preferences") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#Settings
        hotspot (27, 583, 290, 85) action MainMenu() activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#Main Menu
        hotspot (27, 674, 290, 85) action ShowMenu("about") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#About
        hotspot (27, 761, 290, 85) action ShowMenu("help") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"#Help
        hotspot (27, 846, 290, 85) action Quit(confirm=not main_menu):
            if(not main_menu):
                activate_sound"music/UI/ENHF_UI_Button_v2.ogg" 
            if(main_menu):
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg"
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"#Quit
        hotspot (27, 976, 290, 85) action Return() activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"#Return



#        if _in_replay:

#            textbutton _("End Replay") action EndReplay(confirm=True)

#        elif not main_menu:

#            textbutton _("Main Menu") action MainMenu()

#        textbutton _("About") action ShowMenu("about")

#        if renpy.variant("pc"):

#            ## Help isn't necessary or relevant to mobile devices.
#            textbutton _("Help") action ShowMenu("help")

#            ## The quit button is banned on iOS and unnecessary on Android.
#            textbutton _("Quit") action Quit(confirm=not main_menu)


#style navigation_button is gui_button
#style navigation_button_text is gui_button_text

#style navigation_button:
#    size_group "navigation"
#    properties gui.button_properties("navigation_button")

#style navigation_button_text:
#    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:
    tag menu
    imagemap:
        ground "mm_idle.png"
        idle "mm_idle.png"
        hover "mm_hover.png"
            
        hotspot (12, 52, 315, 95) action Start() activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (12, 155, 315, 95) action ShowMenu("load") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (12, 283, 315, 95) action ShowMenu("preferences") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (12, 407, 315, 95) action Help() activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (12, 538, 315, 95):
            if(databasePage ==1):
                action ShowMenu("database1")
            if(databasePage==2):
                action ShowMenu("database2")
            if(databasePage==3):
                action ShowMenu("database3")
            activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        hotspot (12, 669, 315, 95) action ShowMenu("about") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
        hotspot (12, 797, 315, 95) action ShowMenu("mmCredits_start") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
        hotspot (12, 896, 315, 95) action Quit(confirm=False) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
    if persistent.beatGame:
        imagebutton:
            idle "puzzleGallery_idle.png" 
            hover "puzzleGallery_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action (SetVariable("puzzleGallery", True), Start()) #("pg_mainMenu")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "musicRoom_idle.png" 
            hover "musicRoom_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action ShowMenu("music_room")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):
#    imagemap:
#        ground "gui/overlay/game_menu.png"
#        idle "gui/overlay/game_menu.png"
#        hover "gui/overlay/game_menu_hover.png"
                
#        hotspot (12, 83, 315, 95) action Start()
#        hotspot (12, 186, 315, 95) action ShowMenu("load")
#        hotspot (12, 314, 315, 95) action ShowMenu("preferences")
#        hotspot (12, 438, 315, 95) action ShowMenu("about")
#        hotspot (12, 569, 315, 95) action Help()

#    style_prefix "game_menu"

#    if main_menu:
#        add gui.main_menu_background
    
    if _history:
        add gui.history_menu_background
    if (title=="About"):
        add gui.about_menu_background
#    else:
#        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

#    use navigation

#    if main_menu:
#        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
    


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            
            label "[config.name!t]\n" xpos 500
           # text _("Version [config.version!t]\n") xpos 650

            ## gui.about is usually set in options.rpy.
            if gui.about and persistent.beatGame:
                text "[gui.about!t]\n" xpos 100
            elif gui.about:
                text "[gui.about2!t]\n" xpos 100
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} 6.99.\n\n[renpy.license!t]") xpos 100

    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text:
    xmaximum gui.about_text_xmaximum
#    is gui_textR
style about_xmaximum is about_text_xmaximum
style about_label_text:
    size gui.label_text_size
 


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load
init python:
    config.thumbnail_width = 385#428
    config.thumbnail_height = 217#240
screen save():

    tag menu

    imagemap:   
        ground "gui/overlay/save_ground3.png"
        idle "gui/overlay/save_idle3.png"
        hover "gui/overlay/save_hover3.png"
        selected_idle "gui/overlay/save_selected3.png"
        selected_hover "gui/overlay/save_selected_hover3.png"
        cache False
        
        hotspot (1812, 24, 84, 133) clicked FilePage(1) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 157, 84, 128) clicked FilePage(2) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 285, 84, 128) clicked FilePage(3) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 413, 84, 128) clicked FilePage(4) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 541, 84, 125) clicked FilePage(5) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 666, 84, 128) clicked FilePage(6) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 794, 84, 131) clicked FilePage(7) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 925, 84, 132) clicked FilePage(8) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

        hotspot (623, 83, 535, 280) clicked FileSave(1):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(1)  
            add FileScreenshot(1) xalign 0.7 yalign 0.47
#            add AlphaMask((FileScreenshot(1)), "gui/overlay/alphaMask2.png") xalign 0.5 yalign 0.45
            text FileTime(1, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(1):
                style "slot_name_text"
            key "save_delete" action FileDelete(1)#clicked FileSave(1):
            #use load_save_slot(number=1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (1205, 83, 535, 280) clicked FileSave(2):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(2) 
#            add AlphaMask((FileScreenshot(2)), "gui/overlay/alphaMask3.png") xalign 0.7 yalign 0.45
            add FileScreenshot(2) xalign 0.7 yalign 0.47
            text FileTime(2, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(2):
                style "slot_name_text"
            key "save_delete" action FileDelete(2) 
#            use load_save_slot(number=2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (623, 395, 535, 280) clicked FileSave(3):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(3) 
            add FileScreenshot(3) xalign 0.7 yalign 0.47
            text FileTime(3, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(3):
                style "slot_name_text"
            key "save_delete" action FileDelete(3) 
#            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (1205, 395, 535, 280) clicked FileSave(4):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(4) 
            add FileScreenshot(4) xalign 0.7 yalign 0.47
            text FileTime(4, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(4):
                style "slot_name_text"
            key "save_delete" action FileDelete(4) 
#            use load_save_slot(number=4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (623, 713, 535, 280) clicked FileSave(5):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(5) 
            add FileScreenshot(5) xalign 0.7 yalign 0.47
            text FileTime(5, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(5):
                style "slot_name_text"
            key "save_delete" action FileDelete(5) 
#            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (1205, 713, 535, 280) clicked FileSave(6):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(6) 
            add FileScreenshot(6) xalign 0.7 yalign 0.47
            text FileTime(6, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(6):
                style "slot_name_text"
            key "save_delete" action FileDelete(6) 
            
    if (not main_menu):
        use navigation
    if (main_menu):
        use navigation_mm
        
screen load():

    tag menu

    imagemap:   
        ground "gui/overlay/load_ground.png"
        idle "gui/overlay/load_idle.png"
        hover "gui/overlay/load_hover.png"
        selected_idle "gui/overlay/load_selected.png"
        selected_hover "gui/overlay/load_selected_hover.png"
        cache False
        
        hotspot (1812, 24, 84, 133) clicked FilePage(1) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 157, 84, 128) clicked FilePage(2) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 285, 84, 128) clicked FilePage(3) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 413, 84, 128) clicked FilePage(4) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 541, 84, 125) clicked FilePage(5) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 666, 84, 128) clicked FilePage(6) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 794, 84, 131) clicked FilePage(7) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1812, 925, 84, 132) clicked FilePage(8) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

        hotspot (623, 83, 535, 280) clicked FileLoad(1):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(1)  
            add FileScreenshot(1) xalign 0.7 yalign 0.47
            text FileTime(1, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(1):
                style "slot_name_text"
            key "save_delete" action FileDelete(1)#clicked FileSave(1):
            #use load_save_slot(number=1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
            
        hotspot (1205, 83, 535, 280) clicked FileLoad(2):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(2) 
#            add AlphaMask((FileScreenshot(2)), "gui/overlay/alphaMask3.png") xalign 0.7 yalign 0.45
            add FileScreenshot(2) xalign 0.7 yalign 0.47
            text FileTime(2, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(2):
                style "slot_name_text"
            key "save_delete" action FileDelete(2) 
#            use load_save_slot(number=2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (623, 395, 535, 280) clicked FileLoad(3):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(3) 
            add FileScreenshot(3) xalign 0.7 yalign 0.47
            text FileTime(3, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(3):
                style "slot_name_text"
            key "save_delete" action FileDelete(3) 
#            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (1205, 395, 535, 280) clicked FileLoad(4):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(4) 
            add FileScreenshot(4) xalign 0.7 yalign 0.47
            text FileTime(4, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(4):
                style "slot_name_text"
            key "save_delete" action FileDelete(4) 
#            use load_save_slot(number=4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (623, 713, 535, 280) clicked FileLoad(5):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(5) 
            add FileScreenshot(5) xalign 0.7 yalign 0.47
            text FileTime(5, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(5):
                style "slot_name_text"
            key "save_delete" action FileDelete(5) 
#            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (1205, 713, 535, 280) clicked FileLoad(6):
            activate_sound"music/UI/ENHF_UI_Menu_Enter.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            action FileAction(6) 
            add FileScreenshot(6) xalign 0.7 yalign 0.47
            text FileTime(6, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("")):
                style "slot_time_text"
                yalign 1.1
                xpos 19
                size 28
            text FileSaveName(6):
                style "slot_name_text"
            key "save_delete" action FileDelete(6) 

    if (not main_menu):
        use navigation
    if (main_menu):
        use navigation_mm

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is sl_button_text
style slot_time_text is sl_button_text
style slot_name_text is sl_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
init -1:
    define gui.sl_button_width = 350
    define gui.sl_button_height = 309
    define gui.sl_button_text_idle_color = "#ffffff"
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
screen window_display:
    add "gui/overlay/window_true.png"
    
screen fullscreen_display:
    add "gui/overlay/fullscreen_true.png"
    
screen music_options:
    add "gui/overlay/music_hints.png"

screen sfx_options:
    add "gui/overlay/sfx_hints.png"

screen mute_options:
    add "gui/overlay/mute_hints.png"

screen textSpeed_options:
    add "gui/overlay/textSpeed_hints.png"
    
screen autoForward_options:
    add "gui/overlay/autoForward_hints.png"
    
screen skip_options:
    add "gui/overlay/skip_hints.png"

screen unseenText_options:
    add "gui/overlay/unseenText_hints.png"

screen afterChoice_options:
    add "gui/overlay/afterChoice_hints.png"
    
screen transitions_options:
    add "gui/overlay/transitions_hints.png"
    
screen display_options:
    add "gui/overlay/display_hints.png"
    
screen blue_leftFace: #Done
    add "gui/overlay/blue_face_left.png"

screen blue_rightFace: #Done
    add "gui/overlay/blue_face_right.png"
    
screen blue_afterChoice:
    add "gui/overlay/blue_afterChoices.png"
    
screen blue_autoHigh: #Done
    add "gui/overlay/blue_auto_high.png"
    
screen blue_autoMed: #Done
    add "gui/overlay/blue_auto_medium.png"
    
screen blue_autoLow: #Done
    add "gui/overlay/blue_auto_off.png"
    
screen blue_fullscreen: #Done
    add "gui/overlay/blue_fullscreen.png"
    
screen blue_musicHigh: #Done
    add "gui/overlay/blue_music_high.png"
    
screen blue_musicMed: #Done
    add "gui/overlay/blue_music_medium.png"
    
screen blue_musicLow: #Done
    add "gui/overlay/blue_music_low.png"
    
screen blue_mute: 
    add "gui/overlay/blue_mute.png"
    
screen blue_soundHigh: #Done
    add "gui/overlay/blue_sound_high.png"
    
screen blue_soundLow: #Done
    add "gui/overlay/blue_sound_low.png"
    
screen blue_soundMed(): #Done
    add "gui/overlay/blue_sound_medium.png"
    
screen blue_textSpeedHigh(): #Done
    add "gui/overlay/blue_textspeed_high.png"
    
screen blue_textSpeedLow(): #Done
    add "gui/overlay/blue_textspeed_low.png"
    
screen blue_textSpeedMed(): #Done
    add "gui/overlay/blue_textspeed_medium.png"
    
screen blue_title(): #Done
    add "gui/overlay/blue_title.png"
    
screen blue_transitions():
    add "gui/overlay/blue_transitions.png"
    
screen blue_unseen():
    add "gui/overlay/blue_unseen.png"
    
screen blue_window(): #Done
    add "gui/overlay/blue_window.png"

screen remote_comments0(): #Done
    add "gui/overlay/blue_remote0.png"

screen remote_comments1(): #Done
    add "gui/overlay/blue_remote1.png"
    
screen remote_comments2(): #Done
    add "gui/overlay/blue_remote2.png"
        
screen remote_comments3(): #Done
    add "gui/overlay/blue_remote3.png"
        
screen remote_comments4(): #Done
    add "gui/overlay/blue_remote4.png"
    
screen blue_neutral():
    add "gui/overlay/blue_neutral.png"

screen preferences():
#    $ blue_remoteClicks +=1
    $ chairResponse = renpy.random.randint(0,8)
    if(blueLastChair == chairResponse):
        if(chairResponse>0):
            $chairResponse -=1
        else:
            $chairResponse = 8
    $blueLastChair = chairResponse
    $ musicVolumeVal = _preferences.get_volume('music')
    $ soundVolumeVal = _preferences.get_volume('sfx')
    $ textSpeedVal = _preferences.text_cps
    $ autoForwardVal = _preferences.afm_time
    if (musicVolumeVal<0):
        $musicVolumeVal=0.0
    if (musicVolumeVal>1.0):
        $musicVolumeVal=1.0
    if (soundVolumeVal<0):
        $soundVolumeVal = 0.0
    if (soundVolumeVal>1.0):
        $soundVolumeVal = 1.0
    if not(textSpeedVal==None):
        $textSpeedVal = math.trunc(textSpeedVal)
        if (textSpeedVal<0) or (textSpeedVal==0):
            $textSpeedVal = 1
        if (textSpeedVal >200):
            $textSpeedVal = 200
    if not(autoForwardVal==None):
        $autoForwardVal = math.trunc(autoForwardVal)
        if (autoForwardVal >30):
            $autoForwardVal = 30
        if (autoForwardVal < 0):
            $autoForwardVal = 0
    tag menu
    
    mousearea: #Music volume
        area (589, 131, 1200,73)
        hovered Show("music_options") #, transition = dissolve)
        unhovered Hide("music_options") #, transition = dissolve)
    
    mousearea: #SFX
        area (554, 204, 1235, 73) #transitions
        hovered Show("sfx_options")#, transition=dissolve)
        unhovered Hide("sfx_options")#, transition=dissolve)
    
    mousearea: #Mute All words
        area (790, 279, 410, 73) #skip
        hovered Show("mute_options")#, transition=dissolve)
        unhovered Hide("mute_options")#, transition=dissolve)
        
    mousearea: #Mute All box
        area (1460, 274, 128, 90) #skip
        hovered Show("mute_options")#, transition=dissolve)
        unhovered Hide("mute_options")#, transition=dissolve)

    mousearea: #Text speed
        area (636, 410, 1153, 73)
        hovered Show("textSpeed_options")#, transition=dissolve)
        unhovered Hide("textSpeed_options")#, transition=dissolve)
        
    mousearea: #Auto Forward
        area (551, 483, 1238, 73) 
        hovered Show("autoForward_options")#, transition=dissolve)
        unhovered Hide("autoForward_options")#, transition=dissolve)
        
    mousearea: #Skip
        area (984, 562, 220, 73) 
        hovered Show("skip_options")#, transition=dissolve)
        unhovered Hide("skip_options")#, transition=dissolve)
        
    mousearea: #Unseen Text
        area (1217, 648, 188, 60) 
        hovered Show("unseenText_options")#, transition=dissolve)
        unhovered Hide("unseenText_options")#, transition=dissolve)
        
    mousearea: #Unseen Text box
        area (1249, 562, 117, 76) 
        hovered Show("unseenText_options")#, transition=dissolve)
        unhovered Hide("unseenText_options")#, transition=dissolve)
        
    mousearea: #After choices
        area (1449, 648, 169, 64) 
        hovered Show("afterChoice_options")#, transition=dissolve)
        unhovered Hide("afterChoice_options")#, transition=dissolve)
        
    mousearea: #After choices box
        area (1467, 562, 130, 76) 
        hovered Show("afterChoice_options")#, transition=dissolve)
        unhovered Hide("afterChoice_options")#, transition=dissolve)
        
    mousearea: #Transitions
        area (1624, 648, 263, 32) 
        hovered Show("transitions_options")#, transition=dissolve)
        unhovered Hide("transitions_options")#, transition=dissolve)
        
    mousearea: #Transitions box
        area (1688, 562, 114, 76) 
        hovered Show("transitions_options")#, transition=dissolve)
        unhovered Hide("transitions_options")#, transition=dissolve)
        
    mousearea: #Display
        area (834, 679, 955, 149) 
        hovered Show("display_options")#, transition=dissolve)
        unhovered Hide("display_options")#, transition=dissolve)
        
#    mousearea: #Blue
#        area ((581, 823, 29, 84), (581, 1006, 95, 74))
#        hovered Show("blue_chair")
#        unhovered Hide("blue_chair")

    mousearea: #Blue left face
        area(834, 791, 312, 288)
        hovered Show("blue_leftFace")
        unhovered Hide("blue_leftFace")
        
    mousearea: #Error tag
        area(1146, 791, 329, 289)
        hovered Show("blue_title")
        unhovered Hide("blue_title")
        
    mousearea: #Blue right face
        area(1475, 791, 301, 289)
        hovered Show("blue_rightFace")
        unhovered Hide("blue_rightFace")
        
    mousearea: #Blue main
        area(371, 823, 210, 257)
        if (chairResponse==0):
            if(musicVolumeVal <= 0.10):
                hovered Show("blue_musicLow")
            if(musicVolumeVal > 0.1) and (musicVolumeVal<0.9):
                hovered Show("blue_musicMed")
            if(musicVolumeVal >=0.9):
                hovered Show("blue_musicHigh")
        if (chairResponse==1):
            if(soundVolumeVal <= 0.1):
                hovered Show("blue_soundLow")
            if(soundVolumeVal > 0.1) and (soundVolumeVal<0.9):
                hovered Show("blue_soundMed")
            if(soundVolumeVal >=0.9):
                hovered Show("blue_soundHigh")
        if (chairResponse==2):
            if(textSpeedVal <=20):
                hovered Show("blue_textSpeedLow")
            if(textSpeedVal > 20) and (textSpeedVal<180):
                hovered Show("blue_textSpeedMed")
            if(textSpeedVal >=180):
                hovered Show("blue_textSpeedHigh")
        if (chairResponse==3):
            if(autoForwardVal <=3):
                hovered Show("blue_autoLow")
            if(autoForwardVal >3) and (autoForwardVal<27):
                hovered Show("blue_autoMed")
            if(autoForwardVal >=27):
                hovered Show("blue_autoHigh")
        if(chairResponse==4):
            if (_preferences.fullscreen==False):
                hovered Show("blue_window")
            if (_preferences.fullscreen==True):
                hovered Show("blue_fullscreen")
        if(chairResponse==5):
            if(_preferences.get_volume('sfx')==0) and (_preferences.get_volume('music')==0): #(_preferences.muteAll = True):
                hovered Show("blue_mute")
            else:
                hovered Show("blue_neutral")
        if(chairResponse==6):
            if(_preferences.skip_unseen==True):
                hovered Show("blue_unseen")
            else:
                hovered Show("blue_neutral")
        if(chairResponse==7):
            if(_preferences.skip_after_choices == True):
                hovered Show("blue_afterChoice")
            else:
                hovered Show("blue_neutral")
        if(chairResponse==8):
            if(_preferences.transitions==0):
                hovered Show("blue_transitions")
            else:
                hovered Show("blue_neutral")
        unhovered (Hide("blue_soundHigh"), Hide("blue_soundLow"), Hide("blue_soundMed"), 
            Hide("blue_musicLow"), Hide("blue_musicMed"), Hide("blue_musicHigh"), Hide("blue_textSpeedLow"),
            Hide("blue_textSpeedHigh"), Hide("blue_textSpeedMed"), Hide("blue_autoLow"), Hide("blue_autoMed"),
            Hide("blue_autoHigh"), Hide("blue_fullscreen"), Hide("blue_window"), Hide("blue_mute"), 
            Hide("blue_unseen"), Hide("blue_transitions"), Hide("blue_afterChoice"), Hide("blue_neutral"))
        
    mousearea: #Blue's remote
        area (581, 907, 81, 100)
        if (blue_remoteClicks==0):
            hovered Show("remote_comments0")
        if (blue_remoteClicks==1):
            hovered Show("remote_comments1")
        if (blue_remoteClicks==2):
            hovered Show("remote_comments2")
        if (blue_remoteClicks==3):
            hovered Show("remote_comments3")
        if (blue_remoteClicks>3):
            hovered Show("remote_comments4")
        unhovered (Hide("remote_comments0"), Hide("remote_comments1"), Hide("remote_comments2"), Hide("remote_comments3"), Hide("remote_comments4"))
   
    imagemap:   
        ground "gui/overlay/options_ground.png"
        idle "gui/overlay/options_idle.png"
        hover "gui/overlay/options_hover.png"
        selected_idle "gui/overlay/options_selected.png"
        selected_hover "gui/overlay/options_selected_hover.png"
        
        #Display 
        hotspot (1269, 696, 77, 109) action Preference("display", "toggle") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1692, 693, 77, 112)action Preference("display", "toggle") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        
        #Volume
        #Music arrows
        hotspot (1276, 131, 71, 69) action Preference("music volume", musicVolumeVal-0.1) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1704, 131, 61, 69) action Preference("music volume", musicVolumeVal+0.1) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        
        hotspot (1276, 200, 71, 83) action (Preference("sound volume", soundVolumeVal-0.1), Play("sound", config.sample_sound)) hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1704, 200, 71, 83) action (Preference("sound volume", soundVolumeVal+0.1), Play("sound", config.sample_sound)) hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

        bar pos (1350, 131) value Preference("music volume") style "pref_slider"  
        bar pos (1350, 210) value Preference("sound volume") style "pref_slider" #action Play("sound", config.sample_sound)
        hotspot (1460, 274, 128, 90) action Preference("all mute", "toggle") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

        #Skip Options
        hotspot (1249, 562, 117, 76) action Preference("skip", "toggle") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"  
        hotspot (1688, 562, 114, 76) action InvertSelected(Preference("transitions", "toggle")) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1467, 562, 130, 76) action Preference("after choices", "toggle") activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        
#        hotspot (1276, 363, 71, 83) action Preference("text speed", 1) #Set to minimum on click
#        hotspot (1704, 363, 71, 83) action Preference("text speed", 200) #Set to maximum on click
        if((textSpeedVal-20)==0):
            hotspot (1276, 400, 71, 83) action Preference("text speed", 1) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        else:
            hotspot (1276, 400, 71, 83) action Preference("text speed", textSpeedVal-20) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1704, 400, 71, 83) action Preference("text speed", textSpeedVal+20) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        
        if not(autoForwardVal==None):
#            if (autoForwardVal ==0) or (autoForwardVal<0):
#                hotspot (1276, 446, 71, 83) action Preference("auto-forward time", 0)R
#            if (autoForwardVal>0) and (autoForwardVal<40):
            hotspot (1276, 483, 71, 83) action Preference("auto-forward time", autoForwardVal-3) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            hotspot (1704, 483, 71, 83) action Preference("auto-forward time", autoForwardVal+3) activate_sound"music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
#            if (autoForwardVal==40) or (autoForwardVal>40):
#                hotspot (1704, 446, 71, 83) action Preference("auto-forward time", 40)
            
        bar pos (1350, 416) value Preference("text speed") style "pref_slider"
        
        bar pos (1350, 492) value Preference("auto-forward time") style "pref_slider"
#        hotspot (1276, 446, 71, 83) action Preference("auto-forward time", 0)
#        hotspot (1704, 446, 71, 83) action Preference("auto-forward time", 40)#autoForwardVal+10)

    imagebutton:
        idle "gui/overlay/remote_idle.png"
        hover "gui/overlay/remote_hover.png"
        xpos 0
        ypos 0
        focus_mask True
        hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        activate_sound "music/UI/ENHF_UI_Button_v2.ogg"
        if (blue_remoteClicks<4):
            action SetVariable("blue_remoteClicks", blue_remoteClicks + 1)
        else:
            action SetVariable("blue_remoteClicks", 0)
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
        
    if (_preferences.fullscreen==False):
        imagebutton:
            idle "gui/overlay/window_true.png" 
            xpos 0
            ypos 0
    if (_preferences.fullscreen==True):
        imagebutton:
            idle "gui/overlay/fullscreen_true.png"
            xpos 0
            ypos 0
  
init -100 python:
    config.default_afm_enable = True
    config.default_afm_time =40
    blue_remoteClicks = 0
    blueChairOptions = 0
    blueLastChair = -1
init -2 python:
    musicVolumeVal = _preferences.get_volume('music')
    soundVolumeVal = _preferences.get_volume('sfx')
    textSpeedVal = _preferences.text_cps
    autoForwardVal = _preferences.afm_time
    style.pref_slider.left_bar = "gui/overlay/slider_right.png" #full
    style.pref_slider.right_bar = "gui/overlay/slider_left.png" #empty
    style.pref_slider.hover_left_bar = "gui/overlay/slider_right_hover.png" #full
    style.pref_slider.hover_right_bar = "gui/overlay/slider_left_hover.png" #empty
    style.pref_slider.xalign = 0.0

    style.pref_slider.xmaximum = 352   # width of your left_bar image.
    style.pref_slider.xminimum = 352 
    style.pref_slider.yminimum = 64
    style.pref_slider.ymaximum = 64    # height of your left_bar image.  Probably will be the height of the red part of the bar plus the slider's height.

    style.pref_slider.thumb = None    

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html
screen history_menu(title, scroll=None):
    add gui.history_menu_background

    frame:
        style "history_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "history_menu_navigation_frame"

            frame:
                style "history_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

screen history():
    tag menu
    ## Avoid predicting this screen, as it can be very large.
    predict False

    use history_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"
    
        for h in _history_list:

            window:
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")

style history_menu_outer_frame is empty
style history_menu_navigation_frame is empty
style history_menu_content_frame is empty
style history_menu_viewport is gui_viewport
style history_menu_side is gui_side
style history_menu_scrollbar is gui_vscrollbar

style history_menu_label is gui_label
style history_menu_label_text is gui_label_text

style history_menu_outer_frame:
    bottom_padding 45
    top_padding 180

#    background "gui/overlay/game_menu.png"

style history_menu_navigation_frame:
    xsize 420
    yfill True

style history_menu_content_frame:
    left_margin 50
    right_margin 30
    top_margin 15

style history_menu_viewport:
    xsize 1420

style history_menu_vscrollbar:
    unscrollable gui.unscrollable

style history_menu_side:
    spacing 15

style history_menu_label:
    xpos 60
    ysize 180

style history_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width + 20
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu
    add gui.help_menu_background
    default device = "keyboard"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

#                if scroll == "viewport":

#                viewport:
#                    scrollbars "vertical"
#                    mousewheel True
#                    draggable True

#                    side_yfill True

#                    vbox:
#                        transclude

    if (not main_menu):
        use navigation
        
    if (main_menu):
        use navigation_mm

    style_prefix "help"

    vbox:
        spacing 23

        hbox:

            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") xpos 900 ypos 180 activate_sound "music/UI/ENHF_UI_Button_v2.ogg" selected_sound "" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            textbutton _("Mouse") action SetScreenVariable("device", "mouse") xpos 1000 ypos 180 activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") xpos 680 ypos 200 activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter") xpos 510 ypos 200 
        text _("Advances dialogue and activates the interface.") xpos 530 ypos 200

    hbox:
        label _("Space") xpos  510 ypos 200
        text _("Advances dialogue without selecting choices.") xpos 530 ypos 200

    hbox:
        label _("Arrow Keys") xpos 510 ypos 200
        text _("Navigate the interface.")xpos 530 ypos 200

    hbox:
        label _("Escape")xpos 510 ypos 200
        text _("Accesses the game menu.")xpos 530 ypos 200

    hbox:
        label _("Ctrl")xpos 510 ypos 200
        text _("Skips dialogue while held down.")xpos 530 ypos 200

    hbox:
        label _("Tab")xpos 510 ypos 200
        text _("Toggles dialogue skipping.")xpos 530 ypos 200

    hbox:
        label _("Page Up")xpos 510 ypos 200
        text _("Rolls back to earlier dialogue.")xpos 530 ypos 200

    hbox:
        label _("Page Down")xpos 510 ypos 200
        text _("Rolls forward to later dialogue.")xpos 530  ypos 200

    hbox:
        label "H"xpos 510 ypos 200
        text _("Hides the user interface when not in a puzzle.")xpos 530 ypos 200

    hbox:
        label "S"xpos 510 ypos 200
        text _("Takes a screenshot.")xpos 530 ypos 200

    hbox:
        label "V"xpos 510  ypos 200
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")xpos 530 ypos 200


screen mouse_help():

    hbox:
        label _("Left Click")xpos 510 ypos 200
        text _("Advances dialogue and activates the interface.")xpos 530 ypos 200

    hbox:
        label _("Right Click")xpos 510 ypos 200
        text _("Accesses the game menu.")xpos 530 ypos 200

    hbox:
        label _("Mouse Wheel Up")xpos 510 ypos 200
        text _("Rolls back to earlier dialogue.")xpos 530 ypos 200

    hbox:
        label _("Mouse Wheel Down")xpos 510 ypos 200
        text _("Rolls forward to later dialogue.")xpos 530 ypos 200


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")xpos 510 ypos 200
        text _("Advances dialogue and activates the interface.")xpos 530 ypos 200

    hbox:
        label _("Left Trigger\nLeft Shoulder")xpos 510 ypos 200
        text _("Rolls back to earlier dialogue.")xpos 530 ypos 200

    hbox:
        label _("Right Shoulder")xpos 510 ypos 200
        text _("Rolls forward to later dialogue.")xpos 530 ypos 200

    hbox:
        label _("D-Pad, Sticks")xpos 510 ypos 200
        text _("Navigate the interface.")xpos 530 ypos 200

    hbox:
        label _("Start, Guide")xpos 510 ypos 200
        text _("Accesses the game menu.")xpos 530 ypos 200

    hbox:
        label _("Y/Top Button")xpos 510 ypos 200
        text _("Hides the user interface.")xpos 530 ypos 200

    textbutton _("Calibrate") action GamepadCalibrate()xpos 510 ypos 200


style help_button is gui_button:
    font gui.name_text_font
style help_button_text is gui_button_text:
    color "#005fd0"
    selected_color "#05c2f4"
    hover_color "#c5ebf1"
style help_label is gui_label:
    font gui.name_text_font
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
    font gui.name_text_font

style help_button_text:
    properties gui.button_text_properties("help_button")
    font gui.name_text_font

style help_label:
    xsize 375
    right_padding 30
    font gui.name_text_font

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
    font gui.name_text_font



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
                textbutton _("No") action no_action activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg"


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quickd or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900




