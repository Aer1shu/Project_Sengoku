define mc = Character("[pcname]")
define m1 = Character("???")
define g1 = Character("Girl(?)")



# The game starts here.

label start:

    $ gender = "Male"

    scene black
    show mc_female at right
    show mc_male at left 
    with fade
    
    menu gender_choice:

        "Would you like a Male Lead character?":
            $ gender = 'male'
            hide mc_female with dissolve
            show mc_male at center with move

        "Or a Female Lead character?":
            $ gender = 'female'
            hide mc_male with dissolve
            show mc_female at center with move

    menu confirm:

        "Are you sure about this?\nNote: You cannot change this later."

        "Yes":
            "Alrighty"
            jump prologue
            with fade

        "No":
            jump start

    label prologue:
        
        if gender == "female":
            image imageScale = im.Scale("images/station.png", 1920, 1080)

            scene inside_train

            "Wednesday - 11:34 PM"

            "Weather: Cloudy/Rainy"

            "Train Conductor" "Last stop: Saitama. please make sure to depart when we arrive."

            "I did it... huh..."

            "(I finally finished college...)"

            "(Why I cant be atleast happy about this?)"

            "Sigh..."

            scene imageScale

            show mc_female

            "{i}Mumbles{/i}" 
            
            "Right..."

            "I am...."
        
            $ pcname = renpy.input("Enter your name:")

            $ pcname = pcname.strip()

            if pcname == "":
                $ pcname = "Unit_01"

            mc "I'm in debt to my school because I can't pay the fee."

            mc "I can't find a job as well."

            "[pcname]'s stomach growls out of hunger."

            "She notice that she is in front of a 11-7 store."

            "She reached out to her pocket but to no avail."

            mc "{i}Tsk...{/i}"

            mc "I have no money either..."

            "[pcname] walked away."

            with dissolve

            scene bridge_night

            show mc_female

            mc "{i}sigh...{/i}"

            mc "I can't wait to get home and drink a glass of water..."

            hide mc_female

            "When [pcname] tries to pass the bridge, she notices something closing in"

            mc "An aparition? A ghost? What is this?"

            "She slowly approaches the source of this mysterious light source"

            "When she reached halfway through the bridge. A jolt of lightning suddenly struck"

            "The lightning reached for the nearest light post, effectively hitting it"

            "Soon after, she realized that the mysterious entity in front of her was a lightning wisp"

            "It approached her at the speed of light"

            "The moment it reached her, a strong force sent her flying away from the bridge"

            "Severely injured, [pcname] suddenly saw her life flashed before her eyes"

            mc "{i}So, is this it, huh...{/i}"

            mc "{i}I worked so hard, just to meet my end like this?{/i}"

            mc "{i}Well, I'm fine with this, I mean, no one's waiting for me \n back home anyways...{/i}"

            "[pcname] fell into the river, grinning"

            with dissolve

            scene black

            "{i}I guess dying like this is better than living in this one hell of a world.{/i}"

            "She finally succumbed to her demise"

            "Or..."

            " "

            "-y"

            "Oy"

            m1 "Oyyyyyyyyyyy"

            m1 "Wesk oy"

            mc "(H-how am I still alive?)"

            mc "(Something's poking at my face...)"

            mc "(I've lost all my strength to open my eyes)"

            m1 "Yol oka-?"

            mc "(I can't understand a word.)"

            m1 "Gud le alive..."

            mc "Wai- whaaaaaaaaa???"

            mc "H-hey! where are you dragging me?!"

            mc "Hey!"

            "She opens her eyes, only to see something unusual"

            with Fade (0, 0, 0.5)

            scene forest

            m1 "Human meat, dinner solved. Ahahahaha"

            "[pcname] took up all of her strength to stand up"

            m1 "Uwahhhhhhh!!!"

            mc "Uhmmmmm..."

            "The two stared at each other for a moment"

            "Any second now..."

            m1 "Are you okay?"

            show mc_female

            mc "I guess? Yeah..."

            "She checked her body for missing limbs, fractured or broken bones"

            "But everything seems normal and she feels fine"

            mc "{i}(How did I end up in the forest anyway?){/i}"

            m1 "Thank goodness you're okay..."

            mc "Anywho..."

            mc "..."

            mc "Can I ask you something?"

            mc "{i}(This girl looks cute){/i}"

            mc "{i}(Her hair is, no doubt, naturally white){/i}"

            mc "Where are we?"

            g1 "In the forest?"

            g1 "..."

            g1 "{b}Hahahahahaha{/b}"

            mc "What prefecture is this? How did I end up here?"

            g1 "Pre... Picture! Ahhhh!"

            g1 "I dunno..."

            g1 "We are in the dark forest."

            mc "Its prefec-, no! That's not the point!"

            mc "Dark forest?"

            g1 "Yes! Perfect Hunting ground!"

            mc "{i}(Where in Japan is this place?){/i}"

            g1 "You, not from here?"

            mc "I... the last thing I remembered was..."

            with fade

            scene black

            "[pcname] told the girl about what happened before she ended up in the forest"

            with Fade (0, 0, 0.5)

            scene forest

            show mc_female

            mc "After that, I got into an accident and fell to the river."

            mc "If I can recall it correctly, I stumbled upon a lightning wisp."

            mc "It exploded when it closed into me."

            mc "And the rest is history."

            g1 "Uh-huh..."

            mc "Hey..."

            mc "Are you even listening to me?"

            g1 "Y-yeah..."

            mc "You're clearly not-"

            mc "Why is the ground shaking?"

            g1 "This is bad..."

            g1 "{i}Sigh{/i}"

            g1 "Let's get out of here..."

            mc "Wh-where are we going?!"

            mc "HEYYYYYYYYYYYYYYYYYYYY!!!"

            g1 "No time to explain! Just follow me!"

            hide mc_female

            "A giant wolf appeared, as it howls, huge bolts of lightning struck"

            mc "WHAT WAS THAT!?!?!?!"

            g1 "RUN! I'LL EXPLAIN IT TO YOU LATER IN THE CITY!"

            g1 "{i}(I'm gonna tell the guild master about this{/i})"

            scene black

            mc "{i}(This is not Japan.){/i}"

            mc "{i}(I can safely say that my life on Earth has ended.{/i})"

            with Fade (0, 0, 0.5)

            scene forest

            mc "AGHHHHHHHHHHHHHHHHHHHHH!!!!"

            "[pcname] realized..."

            "She got reincarnated into a different world."




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        elif gender == "male":

            scene inside_train

            "Wednesday - 11:34 PM"

            "Weather: Cloudy/Rainy"

            "Train Conductor" "Last stop: Saitama. please make sure to depart when we arrive."

            "I did it... huh..."

            "(I finally finished college...)"

            "(Why I cant be atleast happy about this?)"

            "Sigh..."

            scene imageScale

            show mc_male

            "{i}Mumbles{/i}" 
            
            "Right..."

            "I am...."
        
            $ pcname = renpy.input("Enter your name:")

            $ pcname = pcname.strip()

            if pcname == "":
                $ pcname = "Unit_01"

            mc "I'm in debt to my school because I can't pay the fee."

            mc "I can't find a job as well."

            "[pcname]'s stomach growls out of hunger."

            "He notice that he is in front of a 11-7 store."

            "He reached out to his pocket but to no avail."

            mc "{i}Tsk...{/i}"

            mc "I have no money either..."

            "[pcname] walked away."

            with dissolve

            scene bridge_night

            show mc_male

            mc "{i}sigh...{/i}"

            mc "I can't wait to get home and drink a glass of water..."

            hide mc_male

            "When [pcname] tries to pass the bridge, he notices that something is closing in"

            mc "An aparition? A ghost? What is this?"

            "He slowly approaches the source of this mysterious light source"

            "When he reached halfway through the bridge. A jolt of lightning suddenly struck"

            "The lightning reached for the nearest light post, effectively hitting it"

            "Soon after, he realized that the mysterious entity in front of him was a lightning wisp"

            "It approached him at the speed of light"

            "The moment it reached him, a strong force sent him flying away from the bridge"

            "Severely injured, [pcname] suddenly saw his life flashed before his eyes"

            mc "{i}So, is this it, huh...{/i}"

            mc "{i}I worked so hard, just to meet my end like this?{/i}"

            mc "{i}Well, I'm fine with this, I mean, no one's waiting for me back home anyways...{/i}"

            "[pcname] fell into the river, grinning"

            with dissolve

            scene black

            "{i}I guess dying like this is better than living in this one hell of a world.{/i}"

            "He finally succumbed to his demise"


            " "

            "-y"

            "Oy"

            m1 "Oyyyyyyyyyyy"

            m1 "Wesk oy"

            mc "(How am I still alive?)"

            mc "(Something's poking at my face...)"

            mc "(I've lost all my strength to open my eyes)"

            m1 "Yol oka-?"

            mc "(I can't understand a word.)"

            m1 "Gud le alive..."

            mc "Wai- whaaaaaaaaa???"

            mc "Hey! where are you dragging me?!"

            mc "Hey!"

            "He opens his eyes, only to see something unusual"

            scene forest

            m1 "Human meat, dinner solved. Ahahahaha"

            "[pcname] took up all of his strength to stand up"

            m1 "Uwahhhhhhh!!!"

            mc "Hey..."

            "The two stared at each other for a moment"

            "Any second now..."

            m1 "Are you okay?"

            show mc_male

            mc "Yeah..."

            "He checked his body for missing limbs, fractured or broken bones"

            "But everything seems normal and he feels fine"

            mc "{i}(How did I end up in the forest anyway?){/i}"

            m1 "Thank goodness you're okay..."

            mc "So..."

            mc "Can I ask you something?"

            mc "{i}(This girl looks cute){/i}"

            mc "{i}(Her hair is, no doubt, naturally white){/i}"

            mc "Where are we?"

            g1 "In the forest?"

            g1 "..."

            g1 "{b}Hahahahahaha{/b}"

            mc "What prefecture is this? How did I end up here?"

            g1 "Pre... Picture! Ahhhh!"

            g1 "I dunno..."

            g1 "We are in the dark forest."

            mc "Huh?"

            mc "Dark forest?"

            g1 "Yes! Perfect Hunting ground!"

            mc "{i}(Where in Japan is this place?){/i}"

            g1 "You, not from here?"

            mc "The last thing I remembered was..."

            with fade

            scene black

            "[pcname] told the girl about what happened before he ended up in the forest"

            with Fade (0, 0, 0.5)

            scene forest

            show mc_male

            mc "After that, I got into an accident and fell to the river."

            mc "If I can recall it correctly, I stumbled upon a lightning wisp."

            mc "It exploded when it closed into me."

            mc "And the rest is history."

            g1 "Uh-huh..."

            mc "Hey..."

            mc "Are you even listening to me?"

            g1 "Y-yeah..."

            mc "I feel like you're not payin-"

            mc "Why is the ground shaking?"

            g1 "This is bad..."

            g1 "{i}Sigh{/i}"

            g1 "Let's get out of here..."

            mc "Where are we headed to?!"

            mc "HEYYYYYYYYYYYYYYYYYYYY!!!"

            g1 "No time to explain! Just follow me!"

            hide mc_male

            "A giant wolf appeared, as it howls, huge bolts of lightning struck"

            mc "WHAT WAS THAT!?!?!?!"

            g1 "RUN! I'LL EXPLAIN IT TO YOU LATER IN THE CITY!"

            g1 "{i}(I'm gonna tell the guild master about this{/i})"

            scene black

            mc "{i}(This is not Japan.){/i}"

            mc "{i}(I can safely say that my life on Earth has ended.{/i})"

            with Fade (0, 0, 0.5)

            scene forest

            mc "YEAHHHHHHHHHHHHHHHHHHHHHHHHH!!!"

            "[pcname] realized..."

            "He got reincarnated into a different world."








    return
