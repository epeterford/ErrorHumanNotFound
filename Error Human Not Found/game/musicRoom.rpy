init -100 python:
    mr = MusicRoom(fadeout=1.0)
    stoppedMR = False
    mr.add("music/Music_Gallery/EHNF_Main_Theme.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/Grace_Lab.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/EHNF_BAL_BGM.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/Ivan_Lab.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/EHNF_AC_BGM.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/Blue_BGM.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/EHNF_Oxygen_Garden_BGM.ogg", always_unlocked = True)
    mr.add("music/Music_Gallery/EHNF_CH5.mp3", always_unlocked = True)
    mr.add("music/Music_Gallery/Puzzle_BGM.ogg", always_unlocked = True)
    mr.loop = True
    
screen music_room:
    tag menu
    imagemap:
        ground "mr_ground.png"
    imagebutton:
        idle "track1_idle.png"
        hover "track1_hover.png"
        selected_idle "track1_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/EHNF_Main_Theme.ogg")
    imagebutton:
        idle "track2_idle.png"
        hover "track2_hover.png"
        selected_idle "track2_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/Grace_Lab.ogg")
    imagebutton:
        idle "track3_idle.png"
        hover "track3_hover.png"
        selected_idle "track3_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/EHNF_BAL_BGM.ogg")
    imagebutton:
        idle "track4_idle.png"
        hover "track4_hover.png"
        selected_idle "track4_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/Ivan_Lab.ogg")
    imagebutton:
        idle "track5_idle.png"
        hover "track5_hover.png"
        selected_idle "track5_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/EHNF_AC_BGM.ogg")
    imagebutton:
        idle "track6_idle.png"
        hover "track6_hover.png"
        selected_idle "track6_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/Blue_BGM.ogg")
    imagebutton:
        idle "track7_idle.png"
        hover "track7_hover.png"
        selected_idle "track7_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/EHNF_Oxygen_Garden_BGM.ogg")
    imagebutton:
        idle "track8_idle.png"
        hover "track8_hover.png"
        selected_idle "track8_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/EHNF_CH5.mp3")
    imagebutton:
        idle "track9_idle.png"
        hover "track9_hover.png"
        selected_idle "track9_selected.png"
        focus_mask True
        action mr.Play("music/Music_Gallery/Puzzle_BGM.ogg")
    imagebutton:
        idle "next_idle.png"
        hover "next2_hover.png"
        focus_mask True
        action mr.Next()
    imagebutton:
        idle "previous_idle.png"
        hover "previous_hover.png"
        focus_mask True
        action mr.Previous()
    imagebutton:
        idle "loop1_idle.png"
        hover "loop1_hover.png"
        selected_idle "loop1_selected.png"
        focus_mask True
        if mr.loop:
            action (mr.ToggleSingleTrack())
        else:
            action (mr.ToggleSingleTrack(), mr.ToggleLoop())
    if stoppedMR:
        imagebutton:
            idle "play_idle.png"
            hover "play_hover.png"
            focus_mask True
            action (SetVariable("stoppedMR", False), mr.Play())
    if not(stoppedMR):
        imagebutton:
            idle "stop_idle.png"
            hover "stop_hover.png"
            focus_mask True
            action (SetVariable("stoppedMR", True), mr.Stop())
    imagebutton:
        idle "shuffle_idle.png"
        hover "shuffle_hover.png"
        selected_idle "shuffle_selected.png"
        focus_mask True
        action mr.ToggleShuffle()
            
    on "replace" action mr.Play
    on "replaced" action Play("music", "music/Music_Gallery/EHNF_Main_Theme.ogg")
    use navigation_mm