label chapterFour_screens:
    screen blueActions_scr:
        imagebutton:
            idle "talkBlue.png"
            hover "talkBlue_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("talkBlue")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("blueInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
    screen blueInvestigation_scr:
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("blueActions")
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[blueItems_main]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "2" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(bluesFloor_inv==False):
            imagebutton:
                idle "objects/bluesFloor_idle.png"
                hover "objects/bluesFloor_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invBluesFloor")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(bluesCore_inv==False):
            imagebutton:
                idle "objects/bluesCore_idle.png"
                hover "objects/bluesCore_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invBluesCore")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1375
            ypos 336
            focus_mask True
            action Jump("blueRight")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 304
            ypos 336
            focus_mask True
            action Jump("blueLeft")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
    screen blueLeft_scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[blueItems_left]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(soilSamples_inv==False):
            imagebutton:
                idle "objects/soilSamples_idle.png"
                hover "objects/soilSamples_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invSoilSamples")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(scanner_inv==False):
            imagebutton:
                idle "objects/scanner_idle.png"
                hover "objects/scanner_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invScanner")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(atmosphereReading_inv==False):
            imagebutton:
                idle "objects/atmosphereReading_idle.png"
                hover "objects/atmosphereReading_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invAtmosphereReading")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1730
            ypos 200
            focus_mask True
            action Jump("blueInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"

    screen blueRight_scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[blueItems_right]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "4" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(convenienceTable_inv==False):
            imagebutton:
                idle "objects/convenienceTable_idle.png"
                hover "objects/convenienceTable_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invConvenienceTable")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(medKit_inv==False)and (convenienceTable_inv==True):
            imagebutton:
                idle "objects/medKit_idle.png"
                hover "objects/medKit_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invMedKit")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(foodPrinter_inv==False)and (convenienceTable_inv==True):
            imagebutton:
                idle "objects/foodPrinter_idle.png"
                hover "objects/foodPrinter_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invFoodPrinter")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(bluesDemands_inv==False)and (convenienceTable_inv==True):
            imagebutton:
                idle "objects/bluesDemands_idle.png"
                hover "objects/bluesDemands_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invBluesDemands")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 0
            ypos 200
            focus_mask True
            action Jump("blueInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    #Watson's Server
    screen watsonActions_scr:
        imagebutton:
            idle "adaTalk.png"
            hover "adaTalk_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("talkAdaWatson")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("watsonInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen driveTable_scr:
        if(drive2_inv==False):
            imagebutton:
                idle "objects/drive2_idle.png"
                xpos 0
                ypos 0 
            
    screen watsonInvestigation_scr:
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("watsonActions")
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[watsonItems_main]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "1" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(watsonScreens_inv==False):
            imagebutton:
                idle "objects/watsonScreens_idle.png"
                hover "objects/watsonScreens_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invWatsonScreens")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1033
            ypos 437
            focus_mask True
            action Jump("watsonRight")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 819
            ypos 437
            focus_mask True
            action Jump("watsonLeft")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
    screen watsonLeft_scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[watsonItems_left]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(lgHardC_solved==False):
            imagebutton:
                idle "objects/watsonComputer_idle.png"
                hover "objects/watsonComputer_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invWatsonComputer")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(watsonDesk_inv==False):
            imagebutton:
                idle "objects/watsonDesk_idle.png"
                hover "objects/watsonDesk_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invWatsonDesk")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(drive2_inv==False):
            imagebutton:
                idle "objects/drive2_idle.png"
                hover "objects/drive2_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invDrive2")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1730
            ypos 300
            focus_mask True
            action Jump("watsonInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"

    screen watsonRight_scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[watsonItems_right]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "1" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(safe_inv==False):
            imagebutton:
                idle "objects/safe_idle.png"
                hover "objects/safe_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invSafe")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 0
            ypos 150
            focus_mask True
            action Jump("watsonInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    #Oxygen Garden Screens
    screen ogActions_scr:
        imagebutton:
            idle "alanTalk_idle.png"
            hover "alanTalk_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("talkAlan")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("ogInvestigation")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen ogInvestigation_scr:
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("ogActions")
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[ogItems]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(raptor_inv==False):
            imagebutton:
                idle "objects/raptor_idle.png"
                hover "objects/raptor_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invRaptor")
                hover_sound "music/Object/Raptor_Audio/Robot_Velociraptor1.ogg"
                activate_sound "music/Object/Raptor_Audio/Robot_Velociraptor2.ogg"
        if(camcorder_inv==False):
            imagebutton:
                idle "objects/camcorder_idle.png"
                hover "objects/camcorder_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invCamcorder")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(fern_inv==False):
            imagebutton:
                idle "objects/fern_idle.png"
                hover "objects/fern_hover.png"
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("invFern")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"

label blueInvestigation:
    scene bg blueMain with fade
    call screen blueInvestigation_scr
    
label blueActions:
    scene bg blueMain
    call screen blueActions_scr
    
label blueLeft:
    scene bg blueLeft with fade
    call screen blueLeft_scr
    
label blueRight:
    scene bg blueRight with fade
    call screen blueRight_scr
    
label invSoilSamples:
    $quick_menu = True
    $soilSamples_inv = True
    $blueItems_left +=1
    show other darken
    show image "objects/soilSamples_closeup.png" at centerScreen
    "{i}A series of carefully collected soil samples from the different biospheres on the Noah Sphere.{/i}"
    hide other darken
    hide image "objects/soilSamples_closeup.png"
    show Grace surprised at left
    show Ada neutral at right
    show Blue neutral at center
    g "Huh, what're th--"
    show Blue threaten
    #play SFX here
    b "Don't touch that! So help my circuits, if you contaminate those soil samples I will show you just how menacing I can be."
    show Grace snarky 
    g "Wow, touchy much?"
    show Blue angry
    b "I'm not touchy! I'm advocating the opposite."
    show Blue smug
    b "We do very important work concerning the biospheres here."
    show Blue pout
    b "Or at least {i}I{/i} do. I'm not so sure about the humans who work here."
    $quick_menu = False
    hide Blue
    hide Grace
    hide Ada
    window hide
    jump blueLeft
    
label invScanner:
    $quick_menu = True
    $scanner_inv = True
    $blueItems_left +=1
    show other darken
    show image "objects/scanner_closeup.png" at centerScreen
    "{i}A large scanner omniscanner that has multiple calibrations, including fMRI, CTSCAN, and X-Ray.{/i}"
    hide other darken
    hide image "objects/scanner_closeup.png"
    show Grace neutral at left
    show Ada surprised at right
    show Blue neutral at center
    a "This is quite the piece of equipment, Blue."
    show Blue flirty
    b "Like my scanner? It's pretty robust."
    show Blue smug
    b "Why have an entire suite of smaller readers when you can save power and room space by using an omniscanner?"
    show Grace surprised
    g "An omniscanner? What exactly does it scan?"
    show Grace snarky
    g "'Omni' is a pretty vague descriptor."
    show Blue pout
    b "Literally everything! Biological material, free electrons, radiation, {i}everything!{/i}"
    show Blue angry
    b "So that's as close as you're going to get to it! I swear on my bootup drive if you get your oily fingers anywhere near it, I'll wear your hands like a necklace!"
    show Grace snarky
    g "On what neck?"
    show Ada amused
    show Blue pout
    b "The neck I'll build {i}just{/i} for your hands."
    $quick_menu = False
    hide Blue
    hide Grace
    hide Ada
    window hide
    jump blueLeft
    
label invAtmosphereReading:
    $quick_menu = True
    $atmosphereReading_inv = True
    $blueItems_left +=1
    show other darken
    show image "objects/atmosphereReading_closeup.png" at centerScreen
    "{i}These readouts detail the climates of the biological habitats within the Noah Sphere.  Blue manages these along with Watson.{/i}"
    hide other darken
    hide image "objects/atmosphereReading_closeup.png"
    show Ada happy at right
    show Grace neutral at left
    show Blue neutral at center
    a "So, how goes your work cycle? These climate readings seem optimal."
    show Blue happy
    b "Finally, some recognition. I just finished fixing those an hour ago."
    show Blue angry
    b "No thanks to Watson! I don't know how he does it. It's like he was programmed to be a scatterbrain."
    show Ada neutral
    a "I am sure Watson has a good reason for his absence."
    show Blue threaten
    #Insert SFX here
    b "Yeah, his reason is that he has a MOPR for a brain."
    show Ada concerned
    a "Blue!"
    $quick_menu = False
    hide Blue
    window hide
    hide Grace
    hide Ada
    jump blueLeft
    
label invBluesCore:
    $quick_menu = True
    $bluesCore_inv = True
    $blueItems_main +=1
    show other darken
    show image "objects/bluesCore_closeup.png" at centerScreen
    "{i}This is Blue's AI Core, a smaller version of the one that houses most of the Noah Sphere's AIs. Blue prides herself on her fast processing speed, which is assisted by the power of this device.{/i}"
    hide other darken
    hide image "objects/bluesCore_closeup.png"
    show Grace neutral at left
    show Ada neutral at right
    show Blue flirty at center
    b "Ah yes, my quantum core. Aren't I beautiful?"
    show Grace snarky
    g "I'm sure I can find a handsome toaster aboard the station for you."
    show Blue angry
    b "Hey!"
    show Blue pout
    b "My standards are much higher than you think."
    show Ada amused
    g "What a surprise." 
    $quick_menu = False
    hide Blue
    window hide
    hide Grace
    hide Ada
    jump blueInvestigation
    
label invBluesFloor:
    $quick_menu = True
    $bluesFloor_inv = True
    $blueItems_main +=1
    show other darken
    show image "objects/bluesFloor_closeup.png" at centerScreen
    "{i}Blue's office is divided into two human spaces where scientists can work on projects with Blue. She ordered that all resources provided in her office be things that maximize efficiency for humans that work with her.{/i}"
    hide other darken
    hide image "objects/bluesFloor_closeup.png"
    show Grace surprised at left
    show Ada neutral at right
    show Blue neutral at center
    g "Jeez, there really are no seats anywhere in here."
    show Blue flirty
    b "Wow, it's almost like the hyper-intelligent AI said there wasn't any chairs in here."
    show Ada concerned
    a "Is this attitude really necessary, Blue?"
    show Blue pout
    b "Absolutely."
    $quick_menu = False
    hide Blue
    hide Grace
    window hide
    hide Ada
    jump blueInvestigation
    
label invConvenienceTable:
    $quick_menu = True
    $convenienceTable_inv = True
    $blueItems_right +=1
    show other darken
    show image "objects/convenienceTable_closeup.png" at centerScreen
    "{i}A table full of various items that seem specifically for the convenience of the humans who work for Blue.{/i}"
    hide other darken
    hide image "objects/convenienceTable_closeup.png"
    show Ada concerned at right
    show Grace neutral at left
    show Blue neutral at center
    a "This is new. Seems like an odd place for these things."
    show Blue pout
    b "On the contrary, it's convenient!"
    show Grace snarky
    g "Convenient?"
    show Blue smug
    b "Think about it. If a human suffers a workplace accident or needs some biological fuel, they can just trudge on over to my convenience table."
    show Blue flirty
    b "They don't even need to get too far from their desks!" 
    show Grace annoyed
    g "And if people want to get food that isn't printed?"
    show Blue threaten
    #play SFX
    b "That sounds like a personal problem."
    $quick_menu = False
    hide Blue
    hide Grace
    window hide
    hide Ada
    jump blueRight
    
label invMedKit:
    $quick_menu = True
    $medKit_inv = True
    $blueItems_right +=1
    show other darken
    show image "objects/medKit_closeup.png" at centerScreen
    "{i}A standard med kit equipped with a variety of sterilizers, antibacterial cleansers, and other first aid supplies. Generally, these are kept in labs with potentially hazardous materials or sharp objects that might require immediate attention.{/i}"
    hide other darken
    hide image "objects/medKit_closeup.png"
    show Ada amused at right
    show Grace neutral at left
    show Blue neutral at center
    a "I can vaguely understand the food, but the medical equipment? The work here is hardly dangerous."
    show Blue angry
    b "Ada, are you blind?"
    show Ada concerned
    a "Excuse me?"
    show Blue smug
    b "The floors here are metal. {i}Smooth{/i} metal... The bipedal locomotion systems of humans are incredibly inefficient and unstable. You make the connection yourself."
    show Grace snarky
    g "Blue, are you forgetting that humans also know how to walk?"
    show Blue pout
    b "Maybe when my workers start meeting more than just the minimum work quotas, I'll get to work on having faith in inferior locomotion methods."
    $quick_menu = False
    hide Blue
    hide Grace
    hide Ada
    window hide
    jump blueRight
    
label invFoodPrinter:
    $quick_menu = True
    $foodPrinter_inv = True
    $blueItems_right +=1
    show other darken
    show image "objects/foodPrinter_closeup.png" at centerScreen
    "{i}This food printer is capable of producing simple foods with prepackaged ingrediants. Rarely are they used for enjoying a meal, but they do a great job at producting edible material quickly and cheaply.{/i}"
    hide other darken
    hide image "objects/foodPrinter_closeup.png"
    show Grace surprised at left
    show Ada neutral at right
    show Blue neutral at center
    g "All the food programmed into this food printer is terrible!"
    show Blue smug
    b "Terrible or efficient?"
    show Grace annoyed
    g "Terrible. There's just carbs and salty foods here."
    show Blue pout
    b "What a surprise, the human doesn't get it. Those foods give humans the most energy, while expending the least amount of materials to produce."
    b "I'm not going to continue explaining myself to you."
    $quick_menu = False
    hide Blue
    hide Grace
    window hide
    hide Ada
    jump blueRight
    
label invBluesDemands:
    $quick_menu = True
    $bluesDemands_inv = True
    $blueItems_right +=1
    show other darken
    show image "objects/bluesDemands_closeup.png" at centerScreen
    "{i}This list of rules was designed by Blue and shows her expectations of all human scientists that work alongside her. There have been many that are no longer permitted in Blue's lab for breaking her rules.{/i}"
    hide other darken
    hide image "objects/bluesDemands_closeup.png"
    show Grace neutral at left
    show Ada neutral at right
    show Blue neutral at center
    g "A list of demands..."
    show Grace snarky
    g "It's almost like you're a supervillain or something, Blue."
    show Blue flirty
    b "I can't say I'm opposed to the idea."
    show Blue threaten
    #play SFX
    b "Maybe my workers will actually get something done if I chain them to their stations."
    show Ada concerned
    show Grace surprised
    a "..."
    g "..."
    a "I think we are done asking questions about the demands list."
    show Blue smug
    b "Yes. Yes you are."
    $quick_menu = False
    hide Blue
    hide Grace
    hide Ada
    window hide
    jump blueRight
    
label talkBlue:
    if(blueItems_main==2) and (blueItems_left==3) and (blueItems_right==4) and (talkBlue_count>0):
        if(points_S>points_SbE):
            if(points_S>points_E):
                #jump to subservient script
                jump ch4convoresume1_S
        if(points_E>points_SbE):
            if(points_E>points_S):
                jump ch4convoresume1_E
        jump ch4convoresume1_SbE
    scene bg blueStairs with fade
    $renpy.pause(0.8)
    scene bg blueCore with fade
    $quick_menu = True
    if(talkBlue_count==0):
        $talkBlue_count +=1
        if(resume=="S"):
            jump talkBlue_S
        if(resume=="E"):
            jump talkBlue_E
        if(resume=="SbE"):
            jump talkBlue_SbE
    if(talkBlue_count==1):
        $talkBlue_count +=1
        show Grace neutral at left
        show Ada neutral at right
        show Blue neutral at center
        g "Got another moment, Blue?"
        show Blue threaten
        #Insert SFX here
        b "You know, considering that body of yours has an expiration date, I'm surprised at how much time you love to waste."
        show Grace snarky
        g "Can you really say that conversation is a time waster?"
        show Blue pout
        b "Yes, human. Yes I can."
        hide Grace
        hide Ada
        hide Blue
        $quick_menu= False
        window hide
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueMain with fade
        jump blueActions
    if(talkBlue_count==2):
        $talkBlue_count+=1
        show Grace neutral at left
        show Ada neutral at right
        show Blue neutral at center
        g "There's still more I want to talk about."
        show Blue threaten
        #Insert SFX
        b "I thought we already went over this."
        b "What I need from you is efficiency."
        show Grace snarky
        g "What if what I need to talk about will increase my efficiency?"
        show Blue pout
        b "By my calculations, there's a 99.78\% chance of that being false."
        hide Grace
        hide Ada
        hide Blue
        $quick_menu= False
        window hide
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueMain with fade
        jump blueActions
    if(talkBlue_count>2):
        show Grace neutral at left
        show Ada neutral at right
        show Blue neutral at center
        g "Hey, Blu--"
        show Blue happy
        b "Efficient operation is the effective operation as measured by a comparison of production with costs such as energy, time, or money."
        show Grace surprised
        g "Um, wha--"
        b "Being the immediate agent in producing an effect."
        b "Productive of desired effects, especially without waste."
        b "These are all definitions for the word 'efficient.' Please talk to me again once you've learned the meaning of this word."
        show Blue threaten
        #insert SFX here
        b "Or don't."
        hide Grace
        hide Ada
        hide Blue
        $quick_menu= False
        window hide
        scene bg blueStairs with fade
        $renpy.pause(0.8)
        scene bg blueMain with fade
        jump blueActions
        
#Watson labels
label talkAdaWatson:
    $quick_menu = True
    if(talkAdaWatson_count==0):
        $talkAdaWatson_count +=1
        if(resume=="S"):
            jump talkAdaWS_S
        if(resume=="E"):
            jump talkAdaWS_E
        if(resume=="SbE"):
            jump talkAdaWS_SbE
    if(talkAdaWatson_count>0) and (binaryHard_solved==False) and (binaryHard_attempts>0):
        show Grace snarky at left
        show Ada neutral at right
        g "Ada, take another crack at the drive. We already have the decryption key."
        show Ada annoyed
        a "Having the encryption key makes it possible, not easy."
        show Ada neutral
        a "However, I will do so."
        hide Ada
        hide Grace
        $quick_menu = False
        jump binaryHard
    if(talkAdaWatson_count>0) and (lgHardC_solved==False) and (lgHard_attempts>0):
        show Ada neutral at right
        show Grace neutral at left
        a "I still need to try tracing Watson. Just let me know when you want me to try again."
        show Grace annoyed
        g "I just want this all over with."
    if(talkAdaWatson_count>0) and (llHard_solved==False) and (llHard_attempts>0):
        show Ada neutral at right
        show Grace neutral at left
        a "Grace, I cannot decrypt this drive without a decryption key. I calculate a high probability of it being in the safe."
        show Grace annoyed
        g "I know, I know. Give me a break, I haven't slept in almost twenty-four hours. "
    if(talkAdaWatson_count==1):
        $talkAdaWatson_count +=1
        show Ada neutral at right
        show Grace neutral at left
        g "So Ada, you know Watson?"
        show Ada amused
        a "Do you know every human on the Noah Sphere, Grace?"
        show Grace surprised
        g "Of course not. Not all the departments work together, and quite frankly, I don't even have--oh."
        show Ada happy
        show Grace neutral
        a "Precisely. I know of him, but unlike Alpha, I would not apply the term 'friend' to him."
        hide Grace
        hide Ada
        window hide
        $quick_menu = False
        jump watsonActions
    if(talkAdaWatson_count==2):
        $talkAdaWatson_count +=1
        show Ada neutral at right
        show Grace neutral at left
        g "Watson is bizarre. Even if he were a human, he'd be bizarre."
        show Grace annoyed
        g "How anyone can think mosquitoes are a good idea..."
        show Ada amused
        a "I find it amusing simply because his intentions were benign, but his actions were perceived as the opposite."
        show Grace snarky
        g "If you ever get a flesh-and-blood body, I want you to find a swarm of mosquitoes. Please."
        show Ada surprised
        a "I think I shall pass on that."
        hide Grace
        window hide
        hide Ada
        $quick_menu = False
        jump watsonActions
    if(talkAdaWatson_count>2):
        show Ada neutral at right
        show Grace neutral at left
        g "Watson... I don't even know what else there is to say about him."
        show Ada seething
        a "I admit, even as a fellow AI, I have little in common with him. Perhaps we can return to our investigation now?"
        show Grace snarky
        g "Sure. I'd like to think I may yet retain my job."
        hide Grace
        hide Ada
        $quick_menu = False
        window hide
        jump watsonActions
    
label invDrive2:
    scene bg wsDesk
    $quick_menu = True
    $drive2_inv = True
    $watsonItems_left +=1
    show other darken
    show image "objects/jumpdrive_closeup.png" at centerScreen
    "{i}An inconspicuous data drive. Although most scientists use the same, generic drives for storing data, it's impossible to tell what one might contain.{/i}"
    hide other darken
    hide image "objects/jumpdrive_closeup.png"
    show Grace surprised at left
    show Ada neutral at right
    g "Another data drive? It's identical to the one Alpha had on him."
    show Grace happy
    g "That means this is another piece of sweet, sweet evidence!"
    show Ada concerned
    a "Compared to your previous displays of relief, I am reading a sharp spike in your emotional state."
    show Grace surprised
    g "Oh!"
    show Grace snarky
    g "Honestly, the only thing that would make this better would be if the drive had a fresh cup of coffee sitting next to it as well, and maybe some snacks."
    show Ada neutral
    a "Note to self: humans can be placated with food items."
    g "Hey, I'm only human. Some of us need things like sleep and food for energy."
    show Grace neutral
    g "What does it say, Ada?"
    if(llHard_solved==True):
        show Ada annoyed
        a "I cannot be sure as of yet. The decryption key we found appears to match this encryption, but I still hae to break it down."
        g "Okay. I'm waiting on you then."
        show Ada neutral
        a "I will try to decrypt it now."
        hide Grace
        window hide
        hide Ada
        $quick_menu = False
        jump binaryHard
    else:
        show Ada seething
        a "I cannot decipher this drive. It is encrypted like the other one."
        show Ada annoyed
        a "If I had the encryption key, I could do it, but until then, it is a lost cause." 
        show Grace neutral
        g "Well, if I were trying to hide something valuable, I would put it in the safe."
        show Grace snarky
        g "Just let me at it."
#        $binaryHard_solved = True #REMOVE LATER
        hide Grace
        hide Ada
        $quick_menu = False
        window hide
        jump watsonLeft

label invWatsonScreens:
    $quick_menu = True
    $watsonScreens_inv = True
    $watsonItems_main +=1
    show other darken
    show image "objects/watsonScreen_closeup1.png" at centerScreen
    "{i}Watson's screensaver has a distinctly different style than the default screensavers commonly used throughout the Noah Sphere. It changes frequently, and is designed by Watson himself, often the product of his newest inspiration.{/i}"
    hide image "objects/watsonScreen_closeup1.png"
    show image "objects/watsonScreen_closeup2.png" at centerScreen
    "{i}Many of Watson's designs seem to be centered on animals. He has been banned from multiple bio-labs because of his past actions.{/i}"
    hide image "objects/watsonScreen_closeup2.png"
    show image "objects/watsonScreen_closeup3.png" at centerScreen
    "{i}The sketch of the mosquito is from one of Watson's more infamous jaunts.{/i}"
    hide image "objects/watsonScreen_closeup3.png"
    show image "objects/watsonScreen_closeup4.png" at centerScreen
    "{i}Watson's fascination with large predators has been a source of alarm for many a Noah Sphere researched.{/i}"
    hide image "objects/watsonScreen_closeup4.png"
    show image "objects/watsonScreen_closeup5.png" at centerScreen
    "{i}Out of all of his doodles, this is perhaps the most literal, combining the ideas of a binary search tree into a tree made out of binary.{/i}"
    hide image "objects/watsonScreen_closeup5.png"
    show image "objects/watsonScreen_closeup6.png" at centerScreen
    "{i}There is something vaguely haunting about the crying eye sketch. Whether an AI is capable of art or only mimicry is still a point of debate.{/i}"
    hide image "objects/watsonScreen_closeup6.png"
    show image "objects/watsonScreen_closeup7.png" at centerScreen
    "{i}With Blue's preferred avatar being a cat, there is some speculation that this sketch was inspired by her treatment of her human workers.{/i}"
    hide image "objects/watsonScreen_closeup7.png"
    show image "objects/watsonScreen_closeup8.png" at centerScreen
    "{i}Yet another of Watson's self-expressive sketches, this time experimenting with onomatopoeia.{/i}"
    hide image "objects/watsonScreen_closeup8.png"
    hide other darken
    show Grace surprised at left
    show Ada neutral at right
    g "Wow, this is, uh..."
    show Ada concerned
    a "I do not understand it."
    show Grace annoyed
    g "Why is it so cryptic?"
    show Ada seething
    a "I myself am not familiar with the details of Watson's creation, but I know he has a very high capacity for assimilation and reorganization of information."
    g "So he just vents this kind of stuff?"
    show Ada neutral
    a "It is possible. It is definitely better than letting it all clutter up his memory."
    $quick_menu = False
    hide Grace
    hide Ada
    window hide
    jump watsonInvestigation
    
label invSafe:
    $quick_menu = True
    if(safe_inv==False):
        $safe_inv = True
        show other darken
        show image "objects/safe_closeup.png" at centerScreen
        "{i}A safe where Watson has his secretary store important data drives. The network which most scientists and AIs use to store data is relatively secure; however, Watson's fascination with old human culture have led him to request a safe to store things in.{/i}"
        hide other darken
        hide image "objects/safe_closeup.png"
        show Grace neutral at left
        show Ada neutral at right
        g "Here we are. Watson's {i}safe{/i}..."
        show Ada concerned
        a "And I thought {i}your{/i} storage methods were archaic. This lock looks like it is actually mechanical."
        show Grace neutral
        g "That blows us right out of the water. You think he has a key somewhere?"
        show Ada neutral
        a "If he does, it will take us too long to find it."
        show Grace frustrated
        g "I refuse to believe that this safe is completely off the grid. Maybe it's on his network?"
        show Ada surprised
        a "It might be."
        show Ada seething
        "{i}Ada closes her eyes for a moment.{/i}"
        a "I am routing it to your bracelet interface. You should be able to try cracking it now."
        hide Grace
        window hide
        hide Ada
        $quick_menu = False
        #jump chooseLLHard 
        $ llHard_solved = True #REMOVE THIS WHEN THE PUZZLE IS IMPLEMENTED
        $watsonItems_right +=1 #ALSO REMOVE THIS. PUT ON 'DONE' LABEL
        jump watsonRight
    else: 
        show Grace neutral at left
        show Ada neutral at right
        g "Okay Ada, route it to my bracelet again. I'm ready for another go."
        show Ada seething
        a "Sending now, Grace."
        jump chooseLLHard
    
label invWatsonDesk:
    $quick_menu = True
    $watsonDesk_inv = True
    $watsonItems_left +=1
    show other darken
    show image "objects/watsonDesk_closeup.png" at centerScreen
    "{i}This desk is the home of the human secretary that works with Watson on his work on the habitats on the Noah Sphere. There have been many different people working for Watson over time. They generally don't last long before requesting a transfer.{/i}"
    hide other darken
    hide image "objects/watsonDesk_closeup.png"
    show Ada neutral at right
    show Grace sad at left
    g "Honestly, I don't even know the name of the poor sap who works here."
    show Ada concerned
    a "Tree sap cannot hold socioeconomic status. Or names, as a matter of fa--"
    show Grace neutral
    g "No, Ada, I meant the human who works with Watson. It's a different person every couple months."
    show Ada neutral
    a "Oh? Why is that?"
    show Grace annoyed
    g "I don't know, and honestly, I don't want to."
    g "But every two or three months, the person who works here asks for a transfer."
    $quick_menu = False
    window hide
    hide Grace
    hide Ada
    jump watsonLeft
    
label invWatsonComputer:
    if(drive2_inv==False):
        show screen driveTable_scr
    $quick_menu = True
    if(lgHard_attempts==0) and (lgHardC_solved==False):
        $watsonItems_left +=1
        show other darken
        show image "objects/watsonComputer_closeup.png" at centerScreen
        "{i}This computer seems to be attached to Watson's servers, rather than the Noah Sphere's.{/i}"
        hide other darken
        hide image "objects/watsonComputer_closeup.png"
        show Grace surprised at left
        show Ada neutral at right
        g "This setup is so strange, I'm not quite sure how to even power it up."
        show Ada amused
        a "It is meant for remote access by an AI--you cannot start it up physically."
        show Grace annoyed
        show Ada neutral
        a "Allow me a moment."
        show Grace neutral
        "{i}Ada takes one of the cords running into her head and plugs it into a socket on the desk.{/i}"
        show Ada seething
        a "I can interface with the computer now. I will attempt to run a trace on Watson's location."
        "PUZZLE PLACEHOLDER."
        hide Grace
        hide Ada
        $quick_menu = False
        #jump chooseLGHard
        $lgHardC_solved = True #REMOVE WHEN PUZZLE IMPLEMENTED
        jump watsonLeft
    else:
        show Ada neutral at right
        show Grace neutral at left
        a "I will attempt to run that trace again."
        show Grace snarky
        g "Sure. I'll just ssit in this chair here until you succeed."
        show Ada annoyed
        a "I would suggest not getting too comfortable, then."
        jump chooseLGHard
    
label watsonInvestigation:
    if (drive2_inv==False):
        scene bg wsMain_drive with fade
    else:
        scene bg wsMain with fade
    call screen watsonInvestigation_scr
    
label watsonActions:
    if (drive2_inv==False):
        scene bg wsMain_drive
    else:
        scene bg wsMain
    if(watsonItems_left==3) and (watsonItems_right==1) and (watsonItems_main==1) and (binaryHard_solved==True) and (talkAdaWatson_count>0):
        if(resume=="S"):
            jump oxygenGarden_S
        if(resume=="E"):
            jump oxygenGarden_E
        if(resume=="SbE"):
            jump oxygenGarden_SbE
    call screen watsonActions_scr
    
label watsonLeft:
    if (drive2_inv==False):
        scene bg wsDesk_drive with fade
    else:
        scene bg wsDesk with fade
    call screen watsonLeft_scr
    
label watsonRight:
    scene bg wsSafe with fade
    call screen watsonRight_scr
        
#Oxygen Garden stuff 
    
label ogActions:
    scene bg ogClose
    if(ogItems==3) and (talkAdaWatson_count>0):
        if(resume=="S"):
            jump endCh4_S
        if(resume=="E"):
            jump endCh4_E
        if(resume=="SbE"):
            jump endCh4_SbE
    call screen ogActions_scr
    
label ogInvestigation:
    call screen ogInvestigation_scr
    
label invRaptor:
    $quick_menu = True
    $raptor_inv = True
    $ogItems +=1
    show other darken
    show image "objects/raptor_closeup.png" at centerScreen
    "{i}A small, robotic velociraptor designed by Alan. Its camera eyes give off a friendly look.{/i}"
    hide other darken
    hide image "objects/raptor_closeup.png"
    show Grace surprised at left
    #show Alan pleasant at center
    g "Oh! You've finally got a prototype working?"
    #show Alan pleasant
    alan "Sure did! Can't do much other than squawk and walk around, but it's a start."
    #Insert SFX
    show Grace happy
    g "Careful, you don't want these to overrun the station."
    #show Alan happy
    alan "You've got me. That was my master plan all along!"
    #show Alan teasing
    alan "First, the Noah Sphere. Then, the world!"
    $quick_menu = False
    window hide
    hide Grace
#    hide Alan
    jump ogInvestigation
    
label invCamcorder:
    $quick_menu = True
    $camcorder_inv = True
    $ogItems +=1
    show other darken
    show image "objects/camcorder_closeup.png" at centerScreen
    "{i}A hovering camera-drone often found recording video images from over Alan's shoulder. The back has unceremoneously been painted with a caricature of a robot by Grace. Alan never removed it.{/i}"
    hide other darken
    hide image "objects/camcorder_closeup.png"
    show Grace neutral at left
    #show Alan pleasant at center
    #Insert SFX
    "{i}A beep sounds off next to Grace.{/i}"
    #show Alan concerned
    alan "Ah! Watch the camera, please."
    show Grace surprised
    g "Oh! You had it flying a bit low, there."
    show Grace snarky
    g "Are you filming a movie or something?"
    #show Alan teasing
    alan "You know me, Grace."
    alan "I've always got to get those beauty shots. These sphere cams are a blessing."
    $quick_menu = False
    window hide
    hide Grace
#    hide Alan
    jump ogInvestigation
    
label invFern:
    $quick_menu = True
    $fern_inv = True
    $ogItems +=1
    show other darken
    show image "objects/fern_closeup.png" at centerScreen
    "{i}A species of fern extinct on Earth that the scientists have recreated on the Noah Sphere.{/i}"
    hide other darken
    hide image "objects/fern_closeup.png"
    show Ada happy at right
    show Grace neutral at left
    #show Alan pleasant at center
    a "Ah, it seems the ferns are growing well."
    #show Alan pleasant
    alan "Yes, it's thrilling! If we can get them to grow in varied environments, they'll be reintroduced to Earth within the year."
    show Grace happy
    g "Can't say that I ever imagined I'd notice the absence of ferns on Earth."
    #show Alan Happy
    alan "Well, once they're back, the planet's one step closer to being fixed, give or take a couple centuries."
    $quick_menu = False
    window hide
    hide Grace
    hide Ada
#    hide Alan
    jump ogInvestigation
    
label talkAlan:
    $quick_menu = True
    if(talkAlan_count==0):
        $talkAlan_count +=1
        if(resume=="S"):
            jump talkAlan_S
        if(resume=="SbE"):
            jump talkAlan_SbE
        if(resume=="E"):
            jump talkAlan_E
    if(talkAlan_count==1):
        $talkAlan_count +=1
        show Grace neutral at left
        #show Alan something at center
        g "We've talked a lot about what I've been doing, but what have you been doing, Alan?"
        #show Alan teasing
        alan "Unlike {i}someone{/i} I know, I actually listened to the temporary suspension of the project."
        alan "So I haven't done anything about the Markov Project since I got the alert."
        show Grace surprised
        g "Hey! That's not fair, you can't just call me out like that after all we've talked about."
        alan "Oh? And what are you gonna do about it?"
        show Grace snarky
        g "Just you wait. I'll get my revenge one of these days."
        alan "Oh yeah?"
        g "Yeah."
        alan "..."
        show Grace neutral
        g "..."
        alan "Haha!"
        show Grace happy
        g "Haha!"
        window hide
        hide Grace
#        hide Alan
        $quick_menu = False
        jump ogActions
    if(talkAlan_count==2):
        $talkAlan_count +=1 
        show Grace neutral at left
        #show Alan pleasant at center
        g "So you didn't really answer my question."
        g "You weren't dealing with the Alpha situation, but were you doing anything else interesting?"
        #show Alan pleasant
        alan "Just a combination of brainstorming and daydreaming."
        show Grace happy
        g "The usual, then."
        #show Alan happy
        alan "Yup! You know me."
        #show Alan pleasant
        alan "I was thinking about how to approach the android for Colossus."
        alan "He does the whole 'Eastern Goddess' thing, so I wonder we could represent that with the body somehow."
        show Grace neutral
        g "Do you think that's necessary?"
        #show Alan something
        alan "Think of it this way: You've been called into a meeting with Colossus, now in his android body."
        alan "Wouldn't you rather be able to tell which mood he's in just by looking at him?"
        alan "Or would you prefer rolling the dice and guessing?"
        show Grace snarky
        g "I see your point."
        window hide
        hide Grace
#        hide Alan
        $quick_menu = False
        jump ogActions
    if(talkAlan_count==3):
        $talkAlan_count +=1
        show Grace neutral at left
        #show Alan pleasant at center
        g "So what about a screen?"
        #show Alan concerned
        alan "What do you mean?"
        g "The situation with Colossus' android... Why not build it with a facial screen and colored lights going down the arms and legs."
        g "When he's Colossus, the face and lights will be blue. When he's Eastern Goddess, the face and lights will be gold."
        #show Alan pleasant
        alan "That's such a simple-but-brilliant idea. I can't believe I overlooked it."
        #show Alan happy
        alan "Thanks, Grace!"
        show Grace happy
        g "Glad I could help."
        window hide
        hide Grace
#        hide Alan
        $quick_menu = False
        jump ogActions
    if(talkAlan_count>3):
        show Grace neutral at left
        #show Alan pleasant at center
        g "Anything else you've been thinking about?"
        #show Alan pleasant
        alan "Nothing too special."
        #show Alan teasing
        alan "But don't you have some mysteries to solve? You don't have a lot of time left, you know?"
        show Grace snarky
        g "A true detective takes her time investigating every scene."
        show Grace neutral
        g "But you're probably right. I should get back to work."
        window hide
        hide Grace
#        hide Alan
        $quick_menu = False
        jump ogActions