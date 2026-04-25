define hud = Character("HUD")

label side_story:
    while 3:

        scene black

        "..."

        "How does this even start..."

        "So uhhh..."

        "How do I put it"

        "So, this is how I was created"

        "I guess"

        "So it all started in"

        "{i}Cool transition{i}"

        with dissolve

        scene factory

        "Ah, this goes here"

        "And this part goes here"

        "{i}This individual is talking to himself{i}"

        "Ahahaha..."

        "Hah..."

        "No wonder I got exiled from society"

        "{i}Looking at his creation, he feels relieved and nervous{i}"

        "Will this scrap even work, I wonder..."

        "Hmmm... Better call it a day I guess..."

        "{i}He mutters to himself{i}"

        with dissolve

        scene black

        "{i}Hours passed until dawn{i}"

        show factory

        "{i}It is your typical day in a dystopian society{i}"

        "Damn..."

        "Same shitty day huh..."

        "Well... Time to continue"

        "{i}He is talking to himself yet again{i}"

        "{i}He tries to boot this 'scrap' that he is working on{i}"

        "Hmmm..."

        "What seems to be the problem here..."

        "{i}The thing starts to puff out smoke{i}"

        "Oh."

        "Shit..."

        "No no no nononoonono"

        "{i}Before he reacted to the situation, some of the insides\n of his work has been fried{i}"

        "Shit... Just my luck"

        "Damn it, that component was hard to come by."

        "{i}What caused such a big problem was a slight oversight{i}"

        "I knew it. Whoever did this wiring is dumb"

        "{i}He looks at a shiny plate, seeing his reflection{i}"

        "Oh..."

        "I guess there's no one else to blame."

        "Well... Time to scavenge for scraps"

        "{i}His stomach growls{i}"

        "This... Is a different issue as well..."

        with dissolve

        scene black

        "So, uhhhh..."

        "Where was I?"

        "Ohhh right!"

        "Should I really include the filler parts, since that bastard..."

        "was pestering me often about including those parts of the story"

        "Although, that may waste a significant amount of your time"

        "Should I? It is your choice."

        menu branch:
            "Yes":
                jump yes_no

            "No":
                jump yes_no

    label yes_no:

        "Seems like all choices does not matter..."

        "Well, sorry about that... I shouldn't have..."

        "Well..."

        "Where am I?"

        "RIIIIIIIIGHT!"

        "Let me recap..."

        "So, he assembled something"

        "He slept"

        "Tried to turn the thing on"

        "Went up in flames"

        "All right..."

        image scrapyard = im.Scale("images/scrapyard.jpg", 1920, 1080)

        show scrapyard

        "Damn... I need to find that specific component"

        "And food..."

        "Hmmm..."

        "Food comes first..."

        "Man... Where am I supposed to find food in the junkyard..."

        "Wait..."

        "I sense something..."

        "Is that... A wisp?"

        "{i}Starts walking towards the 'Unknown Entity'{i}"

        "That thing looks fun."

        "Hehehe..."

        "{i}Of course this individual was hallucinating{i}"

        "{i}He suffered from starvation{i}"

        "..."

        with dissolve

        scene forest

        "Uhhhhh..."

        "Where the hell am I..."

        "This place is kinda... Green."

        show forest at hud_overlay

        hud "System Functional. All Components Functional."

        hud "How may I help you today?"

        scene forest

        "What the hell happened to me..."

        "Wait... I sound like... That scrap..."

        "{i}Finds a stream and runs at the edge{i}"

        "My legs... I can't feel anything."

        "Why is my arm... Made of steel..."

        show forest at hud_overlay

        hud "Woah, calm down there, champ. You're not rendered completely."

        hud "I suggest that you should stay still for a while. You don't have anything that's covering you."

        hud "You don't want your components getting rusty, yes?"

        scene forest

        "Wait, who the hell are you?"

        "And where am I?"

        show forest at hud_overlay

        hud "Oh, right... Try looking around. I'll try to give you context on everything you see as we go by."

        scene forest

        "What happened to me...?"

        "Why can't I feel anything?"

        show forest at hud_overlay

        hud "Already told you, champ. Your body..."

        hud "Is still creating it's outer layer."

        scene forest

        "Do you even know anything from this world?"

        "Last thing I remember was... Uh... I tried making this android..."

        with dissolve

        scene black

        scene forest

        "So, that's what happened."

        show forest at hud_overlay

        hud "Nerve linings and External protective layer has been created. Testing."

        "Ow! What the-"

        hud "Adjusting Component Sensitivity to external factors."

        hud "Adjustment Complete. Component Functional."

        scene forest

        "{i}Stares Downwards{i}"

        "Hey... Why does it feel bouncy when I walk... What is this..."

        "Also... Why am I naked..."

        show forest at hud_overlay

        hud "That's not my problem anymore... Go find something to cover yourself with."

        scene forest

        "Why is the ground shaking...?"

        "{i}Bolts of lightning can be heard nearby{i}"

        show forest with flash

        "What is that?"

        "This is starting to scare me."

        hud "Calm down. I'm scanning for nearby entities."

        show forest at hud_overlay

        hud "It's closing in your general direction."

        "Shit..."

        hide forest

        show forest

        show player_sprite
        
        mc "WHAT WAS THAT!?!?!?!"

        hide player_sprite

        g1 "RUN! I TELL YOU LATER IN THE CITY!"

        "Wait... Are those... People?"

        jump act1

        return