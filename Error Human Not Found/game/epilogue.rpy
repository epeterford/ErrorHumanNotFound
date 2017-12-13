label credits:
    window hide
    $quick_menu = False
    scene bg openCrawlBG at basicfade
    show image "credits.png":
        xpos 0.0 ypos 0.0 xanchor 0.0 yanchor 0.0
        linear 100 xpos 0.0 ypos -8.0
    $renpy.pause(100)
    
label Epilogue:
    scene bg black
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    $quick_menu = True
    "{i}Somewhere deep inside one of the Noah Sphere's servers...{/i}"
    unknown "..."
    unknown "-lo-"
    unknown "-rd-"
    w "Hello, world."
    w "I'm ba-ack."
    if persistent.unlockWatson ==None:
        $persistent.unlockWatson= True
        "{i}{b}Database Entry Unlocked: Watson.{/b}{/i}"
    $persistent.beatGame = True
    "{i}{b}THE END.{/b}{/i}"
    $achievement.Sync()
    $achievement.sync()
    $achievement.grant("ACH_WHODUNIT")
    $achievement.Sync()
    $achievement.sync()
    return
    
