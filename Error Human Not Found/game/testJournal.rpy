##############################################################################
## Variables and Functions
##
## This block of code contains all of the variables and functions required to
## get the screens to work.

init -2 python:
    #### The date in the game
    ## Made an empty string at the beginning because you
    ## haven't yet started the game, and so you're not anywhere.
    date_ref = ""
    #### The time reference in the game
    ## For this, I usually use 3-hour chunks, unless I need
    ## something a bit more specific for a certain part.
    time_ref = ""
    #### Your current location in the game
    loc_ref = ""
    #### The curent page of the journal
    current_journal_page = 0
    #### The number of journal pages which can be accessed
    ## You'll want to increment this variable as you go, every time
    ## you hit a point where the player should have access to the next
    ## journal entry, which are pre-defined below.  As this is set to 3,
    ## you can access all the pages I have put into the list below.
    ######## WARNING! ########
    ## If you make this higher than the number of journal pages defined
    ## in the list below, it'll spit you out an error when you try to
    ## access a part of the list which doesn't exist.  If it's giving you
    ## a problem of it being outside the bounds of the array, that's what
    ## you did wrong.
    unlocked_journal_pages = 3
    #### The contents of the journal pages
    ## This is a list of the contents of the journal pages.  The first
    ## item in the list, in this case "X", is in position 0, so your
    ## current journal page, which is set to zero, points to this location.
    ## For the sake of easy programming, define all of your journal pages
    ## before-hand.  Otherwise, you have to deal with inserting them and
    ## nonesense like that, which is sort of painful until you get the
    ## hang of doing it.
    journal_entries = list([
        "It was supposed to be a pinnacle of human and AI relations.\n\n"
         "Instead, we have a dead AI, and I have fingers pointing at me when I {i}know{/i} I did "
         "nothing wrong. But I make an easy scapegoat. I'm the youngest person working on the Markov "
         "Project, one of the youngest researchers on Noah Sphere at all. Not to mention that anyone "
         "who dislikes my mother would love to see me taken down just to get at her. Too bad they don't "
         "know that I dislike her just as much as they do.\n\n",
         
        "I wish my father was here, but work has him away. Maybe my 'partner,' Ada, will be able to help "
         "me clear my name before I get railroaded by the official investigation team. "
         "I don't think Ada was aware of \"Director\" Hirose being my mother. Lucky her. I wish it "
         "was something I could be unaware of.\n\n",
         
        "At least Ada's useful in one respect. I may be banned from investigating, but with her " 
         "credentials, I'll clear my name. Someone has to. "
         "Ada isn't human. She's a walking, talking robot. But sometimes, I think I'm more of a robot "
         "than she is. I've been approaching this whole thing as if it were an insult to me... I should "
         "have considered the fact that a sentient being is dead. I promise, I will find out why."
        ])
    
    #### The increment function
    ## This is what you put after your "action" keyword
    class incrementJournal():
        ## This defines what happens when the class is called
        ## (as in, when you click the button)
        def __call__(self):
            ## Gotta use the "global" keyword to use any variable
            ## outside your function, as it's a quirk of Python 
            global current_journal_page
            ## Increment the counter variable which keeps track of
            ## which journal page is currently active
            current_journal_page += 1
            ## Restart the interaction to refresh your screen
            renpy.restart_interaction()
        
    #### The decrement function
    ## Exactly the same as above, only you decrement the
    ## counter variable, instead of incrementing it.
    class decrementJournal():
        def __call__(self):
            global current_journal_page
            current_journal_page -= 1
            renpy.restart_interaction()
        
    #### The void function
    ## A void function that I like to use to block out buttons
    def void():
        ## Do something that won't affect the rest of the game
        DummyVariable = 0
        
##############################################################################
# Stats and Info
#
# Displays current statistics and vital information, like the date and time.
    
screen journal:
    ## Replace any other menu that's currently open.
    tag menu
    ## Use the navigation menu (the one you see when you open
    ## the preferences window and such).
    use navigation
    ## This is more or less code I adapted from the preferences
    ## menu, so I'm not 100% certain why it works, I just know that it does.
    #hbox:
     #   xmaximum 1920
      #  vbox:
            ## Creates a box with the label "Vitals", to indicate
            ## that this is the section which shows Sofie's vitals,
            ## which were defined above.
       #     frame:
        #        style_group "pref"
         #       has vbox
          #      label _("Vitals")
           # frame:
            #    style_group "pref"
             #   has vbox
              #  label _("Health")
                ## "bar" creates a bar, "value" sets it current value,
                ## and "range" sets the maximum value, resulting in a
                ## bar which is the ratio between the value and the range.
               # bar value sofie_health range 100
            #frame:
             #   style_group "pref"
              #  has vbox
               # label _("Sanity")
                #bar value sofie_sanity range 100
    hbox:
        xpos 0
        xmaximum 1920
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Grace's Notes")
            ## This is where we use the date, time, and location informatin
            ## we specified earlier (and which we change later on to reflect)
            ## the goings-on of the game.
            frame:
                style_group "pref"
                has vbox
                label _("Date: [date_ref]")
                label _("Reference time: [time_ref]")
                label _("Location: [loc_ref]")
            ## This is the button that brings us to our journal page.
            frame:
                style_group "pref"
                has vbox
                textbutton _("Journal") action ShowMenu("notes_screen")

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Notes
#
# Displays the log of notes.
    
screen notes_screen:
    tag menu
    use navigation
    vbox:
        xminimum 1920
        xmaximum 1920
        frame:
            yminimum 1080
            ymaximum 1080
            style_group "pref"
            has vbox
            ## This is where we display the currently-selected page of
            ## the journal, prefaced by the label "Notes:".
            label _("Notes:")
            label (journal_entries[current_journal_page])
    vbox:
        xpos 1400
        xmaximum 300
        frame:
            style_group "pref"
            has vbox
            ## This is the control of the journal page.
            label _("Page Nav")
            ## If the currently-selected page is less than the total number
            ## of pages (minus one, as the first item in the list is at
            ## location 0, instead of location 1), make the button increment
            ## the journal page when pressed.
            if current_journal_page < (unlocked_journal_pages - 1):
                textbutton _("Next") action incrementJournal()
            ## Otherwise, disable the button.
            else:
                textbutton _("Next") action void()
            ## Like above, only as long as we're not on the first page
            ## (location 0 in the list), allow the player to move back a page.
            if current_journal_page >= 1:
                textbutton _("Previous") action decrementJournal()
            else:
                textbutton _("Previous") action void()

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0