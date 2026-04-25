define mc = Character("[pcname]")
define g1 = Character("Girl(?)")
define g2 = Character("Tin(?)")
define m1 = Character("(Boss)")
define g3 = Character("???")

define eyeopen = ImageDissolve("fx/eyeopen.png", 1.5, 100)
define eyeclose = ImageDissolve("fx/eyeopen.png", 1.5, 100, reverse=True)
define flash = Fade(.25, 0, .75, color="#fff")
define redflash = Fade(.25, 0, .75, color="#ff0000")

default pcname = "Unit_01"


default p_they = "they"
default p_them = "them"
default p_their = "their"
default p_are = "are"
default gender = "neutral"

init python:
    def player_sprite_func(st, at):
        if gender == "male":
            return "images/mc_male.png", None
        elif gender == "female":
            return "images/mc_female.png", None
        return "images/mc_male.png", None

image player_sprite = DynamicDisplayable(player_sprite_func)

transform hud_overlay:
    matrixcolor TintMatrix("#00e5ff") * SaturationMatrix(0.5)

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform sprite_jump:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

$ renpy.pause(delay, hard=True)

image station_bg = im.Scale("images/station.jpg", 1920, 1080)

label start:
    scene black

    menu:
        "How do you prefer to be addressed?"

        "Male Lead":
            $ gender = "male"
            $ p_they, p_them, p_their, p_are = "he", "him", "his", "is"

        "Female Lead":
            $ gender = "female"
            $ p_they, p_them, p_their, p_are = "she", "her", "her", "is"

    show player_sprite at center with fade

    "I told [p_them] that [p_they] [p_are] a great friend!"

    menu:
        "Are you sure about this?\nNote: You cannot change this later."

        "Yes":
            jump prologue

        "No":
            jump start


label prologue:

    scene inside_train

    "Wednesday - 11:34 PM"
    "Weather: Cloudy/Rainy"

    "Train Conductor" "Last stop: Saitama. Please make sure to depart when we arrive."

    "I did it... huh..."
    "(I finally finished college...)"
    "(Why can't I at least be happy about this?)"

    "Sigh..."

    scene station_bg
    show player_sprite

    "{i}Mumbles{/i}"

    "Right..."
    "I am...."

    $ pcname = renpy.input("Enter your name:")
    $ pcname = pcname.strip()

    if pcname == "":
        $ pcname = "Unit_01"

    mc "I'm indebted to my school because I can't pay the fee."
    mc "I can't find a job as well."

    "[pcname]'s stomach growls out of hunger."

    "[p_they] notice that [p_they] [p_are] in front of a 11-7 store."
    "[p_they] reached out to [p_their] pocket but to no avail."

    mc "{i}Tsk...{/i}"
    mc "I have no money either..."

    "[pcname] walked away."

    hide player_sprite

    show player_sprite:
            xzoom -1.0
            xalign 0.5
            yalign 1.0
            linear 2.5 xalign 1.5

    mc "{i}sigh...{/i}"

    scene bridge_night with dissolve

    hide player_sprite

    show player_sprite

    mc "I can't wait to get home and drink some water..."

    "When [pcname] tries to pass the bridge, [p_they] notices something closing in."

    mc "An apparition? A ghost? What is this?"

    "[p_they] slowly approaches the source of this mysterious light."

    "A sudden bolt of lightning strikes nearby."

    show player_sprite

    show bridge_night with flash

    "The entity reveals itself as a lightning wisp."

    "It rushes toward [pcname] at incredible speed."

    "A powerful force sends [p_them] flying off the bridge."

    show player_sprite:
        xzoom -1.0
        yalign 1.0
        xalign 0.5
        linear 1.0 xalign -1.5

    show bridge_night with redflash

    "Severely injured, [pcname] sees [p_their] life flash before [p_their] eyes."

    scene black with dissolve

    mc "{i}So this is it... huh...{/i}"
    mc "{i}I worked so hard, just to meet my end like this?{/i}"
    mc "{i}Well... no one's waiting for me anyway...{/i}"

    "[pcname] falls into the river."

    scene black with dissolve

    "{i}Maybe dying like this is better...{/i}"
    "[p_they] finally succumbed to [p_their] demise."

    "Or..."

    " "
    "-y"
    "Oy"

    g1 "Oyyyyyyyyyyy"
    g1 "...wake the hell up..."

    mc "(H-how am I still alive?)"
    mc "(Something's poking my face...)"
    mc "(I can't open my eyes...)"

    g1 "Gud, u alive..."

    mc "Wai- whaaaaaaaaa???"
    mc "H-hey! Where are you dragging me?!"

    "[pcname] opens [p_their] eyes."

    scene forest with dissolve

    g1 "Human meat, dinner solved. Ahahahaha"

    "[pcname] struggles to stand."

    g1 "Uwahhhhhhh!!!"

    mc "Uhmmmmm..."

    "They stare at each other."

    g1 "Are you okay?"

    show player_sprite

    mc "I guess? Yeah..."

    "[p_they] checks [p_their] body—everything seems fine."

    mc "{i}(How did I end up in a forest?){/i}"

    g1 "Thank goodness you're okay..."

    mc "Can I ask something?"

    mc "Where are we?"

    g1 "In the forest."

    g1 "{b}Hahahahaha{/b}"

    mc "What prefecture is this?"

    g1 "I dunno... This is the Dark Forest."

    mc "{i}(This isn't Japan...){/i}"

    "[pcname] explains everything."

    mc "After that... I got hit by lightning."

    g1 "Uh-huh..."

    mc "Are you even listening?"

    g1 "Y-yeah..."

    mc "Why is the ground shaking?"

    g1 "Bad... we go now."

    mc "W-where?!"

    g1 "No time! Follow me!"

    "A giant wolf appears. Lightning crashes around it."

    show forest with flash

    mc "WHAT WAS THAT?!"

    g1 "RUN! I EXPLAIN LATER!"

    scene black

    mc "{i}This is not Japan...{/i}"
    mc "{i}My life on Earth... is over.{/i}"

    scene forest

    mc "AGHHHHHHHH!!!"

    "[pcname] realizes..."

    "[p_they] has been reincarnated into another world."

    jump side_story

    return

    #init python:
        #def mc_callback(event, interact=True, **kwargs):
            #if event == "show":
                #if not renpy.showing("player_sprite"):
                    #renpy.show("player_sprite", zorder=100)
                #elif event == "end":
                    #if renpy.showing("player_sprite"):
                        #renpy.hide("player_sprite")

#define mc = Character("[pcname]", callback=mc_callback)

label act1:

    scene forest

    show player_sprite

    mc "Wait! Someone's over there!"

    hide player_sprite

    "[pcname] pulls the mysterious girl's hood off"

    show player_sprite

    mc "I said wait!"

    hide player_sprite

    "The mysterious girl suddenly stopped"

    show player_sprite

    mc "Wait... What... Are you...?"

    hide player_sprite

    show yuna

    g1 "NO TIME! JUST RUN!"

    show yuna:
        xzoom -1.0
        linear 1.0 xalign 10.0

    show player_sprite

    mc "Someone's over there!"

    hide player_sprite
    
    hide yuna

    "The mysterious girl stares to where [pcname] is pointing"

    show arees

    g2 "The hell is going on?"

    g2 "Who are you two?"

    hide arees

    show forest at hud_overlay

    hud "Judging by how they look, the blonde one must have the same case as you."

    hud "While the other one... Might be a local. She does look like some sort of a human-animal hybrid."

    hide forest

    show forest

    show arees

    g2 "Yeah, no shit."

    hide arees

    "The mysterious girl suddenly drags [g2]."

    show yuna

    g1 "LET ME EXPLAIN ONCE WE GET TO SAFETY!"

    g2 "WHAT THE FU-"

    show yuna:
        xzoom -1.0
        linear 1.0 xalign 10.0
    
    show arees:
        yalign 1.0
        xzoom -1.0
        linear 1.0 xalign 10.0

    scene black with fade

    image town = im.Scale("town.jpg", 1920,1080)

    scene town  with dissolve

    show player_sprite

    mc "My arm hurts like hell..."

    hide player_sprite

    show yuna

    g1 "Welcome to the town of Biringan."

    hide yuna

    show player_sprite

    mc "Wait, I've heard of that tow-"

    hide player_sprite

    show arees

    g2 "Scrap that, this place is full of hybrids, blondie."

    g2 "Your friend here, she has bear ears."

    hide arees

    show player_sprite

    mc "Yeah, no shit man..."

    hide player_sprite

    show yuna

    g1 "I don't know it I should be offended or laugh at that..."

    g1 "Anyways... We're here. I'll be answering your questions."

    g1 "Feel free to ask anything."

    hide yuna

    "The two of them stared at each other for a moment"

    show player_sprite

    mc "Right... So... What's with that yee yee ass dog earlier?"

    hide player_sprite

    show yuna

    g1 "'Yee yee'? What does that mean?"

    hide yuna

    show player_sprite

    mc "As you can see... I'm not from here. I don't even know..."

    mc "How I could suddenly talk your language..."

    mc "This... Doesn't make sense..."

    hide player_sprite

    show arees

    g2 "I was just looking for something to eat. And then I got into that forest all of a sudden."

    hide arees

    show player_sprite

    mc "No one asked you."

    hide player_sprite

    g2 "I'm just saying, blondie."

    show yuna

    g1 "Right... So it's your first time being here?"

    hide yuna

    "Both of them nods at the mysterious girl"

    show yuna

    g1 "Right. Follow me. Boss knows about almost anything in this area."

    g1 "He might give answers to questions that I haven't answered."

    hide yuna

    show player_sprite

    mc "Right... So it's swords and magic in this world huh?"

    mc "What's next? Gonna make an excuse that you ran out of mana?"

    hide player_sprite

    show arees

    g2 "What the hell is a 'Mana'?"

    hide arees

    show player_sprite

    mc "No one's talking to you, scraps."

    hide player_sprite

    show arees

    g2 "I'm talking to my companion, blondie."

    hud "'Mana', It's basically this world's life force. Without it, you can't cast magic and transmute items."

    g2 "Ahh... I see."

    g2 "Wait... Transmute?"

    hud "Transmutation of items requires Mana and raw or refined materials depending on what you're going to make."

    g2 "Interesting..."

    hide arees

    show yuna

    g1 "Keep up. Boss doesn't want sluggish people around."

    hide yuna

    show player_sprite

    mc "Why are you talking to yourself again, scraps?"

    hide player_sprite

    show yuna
    
    g1 "Oh... Right..."

    hide yuna

    "The three of them went around town"

    "They have arrived in front of an imposing building"

    show player_sprite

    mc "Wow, this place looks like..."

    mc "Shit..."

    mc "Who the fuck designed this house?"

    hide player_sprite

    show arees

    g2 "Beats me. This one's more cheerful than the ruins in my world."

    hide arees

    show player_sprite

    mc "Where did you even come from, scraps?"

    hide player_sprite

    show arees

    g2 "I guess... I'm from the future? I don't really know."

    scene black

    g2 "Or a different world. But to give you an overview, the world where I came from"

    g2 "Was too focused on development. It worked too well..."

    g2 "It ended up ruining everything... Turning a once thriving planet..."

    g2 "Into a dystopian 'Paradise'"

    show town

    show player_sprite

    mc "Yeah, yeah. Spare me that shit, scraps."

    g2 "What...?"

    show yuna

    g1 "Anywayyyy... We're here."

    hide yuna

    "The building's doors slowly opens as the mysterious girl pushes through them"

    scene guildhouse with dissolve

    "Now what took you so long, Yuna?"

    "An imposing voice suddenly pierces through the silence"

    $ g1 = "Yuna"

    show yuna at sprite_jump, center

    g1 "Uhmmm... Boss, I can explain!"

    "She starts trembling"

    hide yuna

    m1 "And who are these people?"

    "The boss asks her coldly"
    
    m1 "You better not bring deadweights now Yuna."

    show yuna

    g1 "I was just helping them, boss."

    hide yuna

    "She's nervous at how her boss reacts."

    m1 "Hmmm..."

    m1 "You better not let me down this time, Yuna."

    "Her eyes lit up like Hiroshima"

    show yuna

    g1 "I won't let you down, boss!"

    hide yuna

    m1 "You better not."

    "The boss lets out a sigh"

    show player_sprite

    mc "So... Yuna, huh?"

    hide player_sprite

    show arees

    g2 "So, Yuna. Your boss doesn't like us that much"

    hide arees

    show player_sprite

    mc "Right... He looks like he's ready to swing his sword at us."

    mc "Not that I'm complaining though. If you catch my drift."

    hide player_sprite

    show arees

    g2 "Man... I want to strangle you so bad right now."

    hide arees

    show player_sprite

    mc "He looks burly as hell. I want to get choked by hi-"

    hide player_sprite

    show arees

    g2 "Stop"

    hide arees

    show player_sprite at sprite_jump, center

    mc "Right... Must have been the wind."

    mc "So... Yuna, huh?"

    hide player_sprite

    show yuna

    g1 "Yeah, that's me."

    hide yuna

    show player_sprite

    mc "He's not interested in us..."

    hide player_sprite

    show arees

    g2 "Sure do."

    g2 "He sounds like he wants to feed us to that big ass dog."

    hide arees

    show yuna at sprite_jump, center

    g1 "It's fine. That's just how he sounds like!"

    g1 "Mind telling me your names then?"

    hide yuna

    show player_sprite

    mc "Fine, Yuna~"

    mc "I'm [pcname], I'm not from this world so... I want to know more about this world."

    hide player_sprite

    "[pcname] stares at [g2]."

    show arees

    g2 "What do you want me to do?"

    hide arees

    show player_sprite

    mc "What do you mean 'What do you want me to do'?"

    hide player_sprite

    show arees

    g2 "Fine."

    hide arees

    "[g2] takes a deep breath"

    show arees
    
    g2 "I am... Wait... Who am I?"

    g2 "Help me out here."

    show guildhouse at hud_overlay

    hud "Say some generic name or something."

    hide guildhouse

    show guildhouse

    show arees

    g2 "I'm... Aeris?"

    $ g2 = "Aeris"

    hide arees

    show arees at sprite_jump, center

    g2 "Yeah, Aeris! That's me."

    hide arees

    show player_sprite

    mc "Right... You don't sound so sure about that buddy. But sure..."

    hide player_sprite

    show arees

    g2 "Stop, blondie."

    hide arees

    show player_sprite

    mc "Okay. So... What now?"

    hide player_sprite

    show yuna

    g1 "Well then. [pcname] and [g2]."

    g1 "I suppose that you want to know how this world works, yes?"

    hide yuna

    show player_sprite

    mc "Obviously, Yuna."

    mc "So... Can I start asking you questions now?"

    hide player_sprite

    show yuna

    g1 "Of course! But I'm not sure if I can answer all of them. But I'll try my best."

    hide yuna

    "She assures both of them. Smiling nervously."

    menu questions:
        g1 "So, what do you want to know?"

        "What are you?":

            jump about_yuna

            label about_yuna:

                show yuna

                g1 "As you can see, I'm a human-animal hybrid. I have bear ears and a tail."
                
                g1 "I was born in the woods. I don't know much about the city life, but I do know how to survive in the wild."

                g1 "I just came here because I owe boss that much. I don't have any other place to go."

                g1 "I'm a scout for boss. I go out and gather information about the world and report it to him."

                hide yuna

                jump questions

        "Why did you bring us here?":

            jump bring_info

            label bring_info:

                show yuna
                
                g1 "Well... I was just walking around the forest when I saw you. You were unconscious, so I decided to help you out."

                g1 "I thought you were dead at first, but then you woke up and I was relieved."

                g1 "As for you, [g2], I just saw you wandering around the forest and I thought you were lost. So I decided to bring you here as well."

                g1 "I didn't know that you two were from another world until you told me."

                hide yuna

                jump questions


        "What is this place?":
            jump place_info

            label place_info:

                show yuna

                g1 "This is the town of Biringan. It's a small town located in the middle of the forest."

                g1 "It's a safe haven for people like me and boss. We don't have to worry about being attacked by monsters or other dangers in the forest."

                g1 "Boss is the one who runs this town. He provides us with food, shelter, and protection from any threats that may come our way."

                g1 "He's a very powerful person."

                hide yuna

                jump questions

        "Are there other people like you?":

            jump people_info

            label people_info:

                show yuna

                g1 "There are other hybrids like me, but they're not as common as you might think. Most of them are either hunters or gatherers like me."

                g1 "Some of them are also warriors who protect the town from any threats that may come our way."

                g1 "They're all very loyal to boss and will do anything to protect him and the town."

                hide yuna

                jump questions

        "So, who is this boss guy?":

            jump boss_question
            
            label boss_question:

                show yuna

                g1 "He is of dragon blood. He's the one who saved me from dying in the forest and gave me a place to stay. I'm very grateful to him."

                g1 "He's also the one who gives us orders and tasks to do. He's very strict and doesn't tolerate any disobedience."

                g1 "He's also very mysterious. No one really knows much about him except that he's very powerful and has a lot of influence in this world."

                hide yuna

                jump questions

        "That's all for now.":

            jump end_questions

            label end_questions:

                show yuna

                g1 "Alright then. If you have any more questions, feel free to ask me anytime."

                g1 "I'll be happy to answer them for you."

                hide yuna

                jump act1_end

    label act1_end:

        show player_sprite

        mc "Thanks, Yuna. That was very helpful."

        mc "I feel like I have a better understanding of this world now."

        mc "One last thing..."

        mc "How do I use magic? I want to learn how to use magic."

        hide player_sprite

        show yuna

        g1 "I don't know. I can't use offensive and healing magic. But I do have these!"

        hide yuna

        "She shows them her weapons. A pair of daggers."

        show yuna

        g1 "I use these to defend myself and to hunt for food. They're very useful in the forest."

        g1 "Neat, right?"

        show yuna at sprite_jump, center

        "[g1] huffs and smiles proudly."

        hide yuna

        show player_sprite

        mc "Right... So, where can I get a pair of those?"

        hide player_sprite

        show yuna

        g1 "Right... I transmuted these myself. I can teach you how to transmute items if you want."

        hide yuna

        show arees

        g2 "Interesting."

        show guildhouse at hud_overlay

        hide arees

        hud "Are you sure about this, dumbass? You don't even know how to use magic yet."

        hide guildhouse

        show guildhouse

        show arees

        g2 "Then do tell me about it. Be useful for once."

        hide arees

        show yuna

        g1 "Why is she talking to herself?"

        hide yuna

        show player_sprite

        mc "Beats me. She said that she has a companion somewhere."

        hide player_sprite

        show arees

        g2 "Are you gonna help me or not?"

        hide arees

        show guildhouse at hud_overlay

        hud "You know, I don't have much knowledge about this world, right?"

        hud "Maybe try gathering more information about how magic works."

        hide guildhouse

        show guildhouse

        show arees

        g2 "Fine."

        hide arees

        show player_sprite

        mc "She's starting to weird me out [g1]."

        hide player_sprite

        show yuna

        g1 "I know..."

        g1 "Let's just focus on finding a way to get you some magic training, okay?"

        g1 "I actually know someone."

        g1 "But she's not here yet. She's been out for a week now."

        hide yuna

        show player_sprite

        mc "May I ask who she is?"

        hide player_sprite

        "The door opens, and a girl walks in."

        "Her appearance is striking, with short black hair and piercing orange eyes."

        "She looks different from [g1], composed and observant"

        "Like an owl, she seems to be taking in everything around her with a calm demeanor."

        show snow

        g3 "[g1], Who are these people?"

        hide snow

        show yuna at sprite_jump, center

        g1 "Ah! Speaking of the devil herself!"

        $ g3 = "Snow"

        g1 "[pcname], [g2], This is my friend, [g3]. She's a fellow scout just like me! I look up to her a lot." 
        
        g1 "She's very skilled and has a lot of knowledge about this world."

        hide yuna

        "[g3] walks up to them and looks them up and down."

        show snow

        g3 "Seriously, [g1]... You bring random people into our town without even asking me first?"

        hide snow

        show yuna

        g1 "Ehe... You've been out for a week, [g3]. I didn't expect you to come back early."

        g1 "You used to stay out to scout for months."

        hide yuna

        show snow

        g3 "Fair enough. Does boss know about this?"

        hide snow

        "[g3] stares at [g1] suspiciously."

        show yuna

        g1 "Of course! I told him just before you returned. I was just answering their questions."

        g1 "Say, [g3], can you teach them how to use magic? I think they want to learn."

        hide yuna

        show snow

        g3 "You know that I'm not that good at it, right? I'm just a scout like you."

        hide snow

        show player_sprite

        mc "Wait wait wait... You're a scout, right?"

        hide player_sprite

        show snow

        g3 "That would be correct."

        hide snow

        "[pcname] looks at [g3]. Noticing something unusual."

        show player_sprite

        mc "What's with that big axe?"

        mc "Isn't that counterintuitive? You're supposed to be agile and stealthy, right?"

        hide player_sprite

        show snow

        g3 "I got used to it."

        g3 "I can still be agile and stealthy with this axe. I just have to be more careful with my movements."

        g3 "And, I have some defensive magic when things go south."

        hide snow

        show yuna

        g1 "She's actually pretty good with that axe. She's one of the best scouts we have."

        hide yuna

        show snow

        g3 "Flattery won't get you anywhere, [g1]."

        hide snow

        show yuna

        g1 "Ehehehe..."

        hide yuna

        show snow

        g3 "And I'm sure as hell won't excuse you for this."

        hide snow

        show yuna

        g1 "I'm sorry, okay? I just wanted to help them out. I didn't mean to cause any trouble."

        hide yuna

        show snow

        g3 "Fine..."

        hide snow

        "[g3] sighs and looks at them both."

        show snow

        g3 "So, mind telling me your names?"

        hide snow

        show player_sprite

        mc "I'm [pcname], and this is [g2]. We're not from this world, so we're trying to learn as much as we can about it."

        g2 "Didn't even gave me a chance to do it myself, blondie."

        mc "You know a lot about this world, right?"

        hide player_sprite

        show snow

        g3 "Yeah, but don't expect much."

        hide snow

        show arees

        g2 "Do you perhaps have any information about magic?"

        hide arees

        show snow

        g3 "I do know about that. But I have very limited knowledge, just hearsays and rumors."

        hide snow

        show arees

        g2 "I understand."

        g2 "Record this [hud]."

        hide arees

        show guildhouse at hud_overlay

        hud "Fine..."

        g2 "Well, aren't you a ray of sunshine."

        hud "Recording information about magic. Please wait..."

        hud "Testing sound receptors, functional."

        hud "Testing visual receptors, functional."

        hud "Calibration complete."

        scene guildhouse

        show arees

        g2 "Alright, I'm ready to listen."

        hide arees

        show snow

        g3 "So, magic is a very complex and mysterious force in this world. It's not something that can be easily explained or understood."

        hide snow

        show arees

        g2 "Yeah, yeah. Skip to the good part."

        hide arees

        show snow

        g3 "Fine. Magic is basically the manipulation of the world's energy to create various effects. It can be used for combat, healing, crafting, and many other things."

        g3 "There are different types of magic, such as defensive, offensive, healing magic, and transmutation magic. Each type has its own unique properties and uses."

        hide snow

        show arees

        g2 "Get to the part about how to use it."

        hide arees

        show snow

        g3 "Well, to use magic, you need to have a certain amount of mana. Mana is the energy that fuels magic. You can replenish your mana by resting or using certain items."

        hide snow

        show arees

        g2 "So, it's like an enegry system or something?"

        hide arees

        show snow

        g3 "Guess so. Anyways, if you want to cast spells, you should see how it casts first."

        g3 "You might need a magic user for that, transmutation specifically."

        g3 "I mean, I can show you what I know. But, I'm tired from all that walking."

        g3 "And, I can only cast defensive spells."

        hide snow

        show arees

        g2 "Right..."

        hide arees

        show player_sprite

        mc "[g1], come here!"

        hide player_sprite

        "[g1] walks over to them."

        show yuna:
            xzoom -1.0
            yalign 1.0
            xalign 0.0
            linear 1.0 xalign 0.5

        g1 "You need something?"

        hide yuna

        show player_sprite

        mc "Do your transmutation thing. I want to see how it works."

        hide player_sprite

        show yuna

        g1 "Okay. Watch closely."

        hide yuna

        show player_sprite

        mc "What are you planning to make though?"

        hide player_sprite

        show yuna

        g1 "I was thinking of making a weapon. Maybe a dagger or something."

        g1 "I have some materials here. Watch closely."

        hide yuna

        "[g1] takes out some raw materials and starts transmuting them."

        show yuna at sprite_jump, center

        "[g1] mutters some incantations under her breath."

        show guildhouse with flash

        hide yuna

        show yuna at sprite_jump, center

        "[g1] focuses her mana on the materials, and they start to glow."

        show guildhouse with flash

        hide yuna

        show yuna at sprite_jump, center

        "[g1] continues to focus her mana, and the materials start to take shape."

        show guildhouse with flash

        hide yuna

        show yuna at sprite_jump, center

        "[g1] finishes the transmutation, and a dagger appears in her hand."

        hide yuna

        show player_sprite

        mc "How the fuck did that happen..."

        mc "Scraps, you better be recording that."

        hide player_sprite

        "[pcname] takes the dagger and examines it."

        show player_sprite

        mc "[g1], can I have this?"

        hide player_sprite

        show yuna

        g1 "Uhhhh... Sure? But it's subpar compared to what others can make."

        hide yuna

        show player_sprite

        mc "Don't worry. Something is definitely better than nothing, right?"

        hide player_sprite

        show yuna

        g1 "I guess..."

        show guildhouse at hud_overlay

        hide yuna

        hud "Recording complete"

        hide guildhouse

        show guildhouse

        show arees

        g2 "Let me try it."

        g2 "Hey, bird lady."

        g2 "Can you give me that thing inside your bag?"

        hide arees

        "[g3] stares at her coldly, her mood suddenly shifted to irritation"

        show snow at sprite_jump:
            xalign 1.0
            yalign 1.0

        g3 "Don't. Call. Me. That."

        hide snow

        "[g3] throws a bar of some kind of metal at [g2]"

        "The bar whirrs as it flies through the air. Almost hitting [g2] dead in the head"

        show arees at sprite_jump, center:
            xzoom -1.0

        g2 "Shit!"

        g2 "I'm sorry, I didn't mean to offend you."

        hide arees

        "[g3] sighs and looks away."

        show snow

        g3 "You should be more careful with your words."

        hide snow

        show arees

        g2 "I'll... Keep that in mind."

        hide area   

        "[g3] walks away, heading to the boss' quarters"

        show yuna

        g1 "Oh. You shouldn't call her that, [g2]."

        hide yuna

        show arees

        g2 "I'm used to giving people nicknames. I didn't expect her to react to that badly."

        hide arees

        show yuna

        g1 "Fair, you're not saying it with bad intent."

        hide yuna

        show arees

        g2 "Well, let me try transmuting this."

        g2 "So, how do you exactly know what comes off after this?"

        g2 "Do you just think about what you're going to make, or say specific incantations like you did earlier?"

        hide arees

        show yuna at sprite_jump, center

        g1 "Ehehe..."

        hide yuna

        show yuna at sprite_jump, center

        g1 "Those are actually gibberish..."

        hide yuna

        "[g1] scratches her head, nervously laughing."

        show yuna

        g1 "You have to think of what you're planning to make. Nothing more, really."

        g1 "As for the quality. It depends on your material and how much mana you put into it."

        hide yuna

        show arees

        g2 "I see. So, it's basically just a matter of how much mana you put into it and the quality of the materials you use."

        hide arees

        show player_sprite

        mc "Right, right. Get to it, scraps. I want to see you make something."

        hide player_sprite

        show arees

        g2 "Calm down! I'm trying to focus here, blondie!"

        hide arees

        "[g2] picks up the metal bar that [g3] threw at her and starts transmuting it."

        "[g2] focuses her mana on the bar, and it starts to glow."

        show arees at sprite_jump, center

        show guildhouse with flash

        "[g2] continues to focus her mana, and the bar starts to take shape."

        show arees at sprite_jump, center

        show guildhouse with flash

        hud "Mana at 10 percent, transmutation in progress..."

        show arees at sprite_jump, center

        show guildhouse with redflash

        hud "Mana at 5 percent, transmutation complete."

        hide arees

        show guildhouse with redflash

        show player_sprite

        mc "What did you end up making?"

        hide player_sprite

        "A shield appears in [g2]' hand."

        show guildhouse at hud_overlay

        hud "Inspecting transmuted item..."

        hud "Item name: Basic Shield. Item quality: Average."

        hud "Not bad. Considering how limited your mana pool is."

        hud "Using auxiliary power. Mana level critical."

        hide guildhouse

        show guildhouse

        scene guildhouse with redflash

        show arees

        g2 "I feel dizzy..."

        g2 "I think I overdid it..."

        hide arees

        show guildhouse at hud_overlay

        hud "Auxiliary power activated. Mana replenishing..."

        show guildhouse with redflash

        hud "Mana replenished. Auxiliary power deactivated."

        show guildhouse with flash

        hud "Mana level at 10 percent."

        hide guildhouse

        show guildhouse

        show arees

        g2 "Phew... That was close."

        hide arees

        show player_sprite

        mc "You're cheating, scraps."

        hide player_sprite

        show arees

        g2 "You know that I'm not human, right?"

        g2 "At least, I used to be."

        g2 "I don't know if you already know about it, but yeah, I am a humanoid cyborg."

        hide arees

        show player_sprite

        mc "Oh, no wonder why you talk to yourself somethimes."

        mc "You have an AI inside you, I assume?"

        hide player_sprite

        show arees

        g2 "How did you-"

        hide arees

        show player_sprite

        mc "You're not the only one who's not from this world, you know?"

        mc "I have an AI inside me as well. It's been talking to me since I woke up in this world."

        hide player_sprite

        "[pcname] tries not to laugh at [g2] who looks dumbfounded."

        show player_sprite at sprite_jump, center

        mc "I'm kidding!"

        mc "You gullible idiot. I don't have an AI inside me. I'm just messing with you."

        hide player_sprite

        "[pcname] laughs at [g2]'s reaction."

        "[g2] walks towards [pcname] and grabs [p_them] by the collar."

        "[g2] shakes her violently, her eyes filled with annoyance."

        show arees at bounce, center:
            xzoom -1.0
            xalign 0.0

        g2 "I fucking hate you so much!"

        show player_sprite:
            xalign 1.0
            yalign 1.0

        mc "Hey, calm down! I'm just joking around!"

        "[pcname] keeps laughing, not taking [g2]'s anger seriously."

        mc "Stop! You're gonna tear my shirt up!"

        g2 "I hate you so much!"

        hide arees

        hide player_sprite

        "Suddenly, the boss walks out of his quarters, noticing the commotion."

        "He walks alongside [g3] and looks at them both."

        "[g2] suddenly stops shaking [pcname]"

        m1 "What's going on here?"

        show yuna

        g1 "Ah, boss, [g3], they're just joking around."

        g1 "So... What did you and [g3] discuss about?"

        hide yuna

        show yuuto

        m1 "Nothing much. Just talking about her report."

        hide yuuto

        show yuna

        g1 "I see."

        hide yuna

        show yuuto

        m1 "Well, I hope you two are not causing any trouble here. I don't want to have to deal with any problems."

        hide yuuto

        show player_sprite

        mc "Hey, mind telling me your name?"

        hide player_sprite

        $ m1 = "Yuuto"

        show yuuto

        m1 "My name is Yuuto. I'm the boss of this town. I run everything here and make sure that everything is in order."

        m1 "People here appointed me as their leader."

        m1 "I assume [g1] and [g3] here have told you about this world, correct?"

        hide yuuto

        show player_sprite

        mc "[g1] told me about the basics."

        hide player_sprite

        show yuuto

        m1 "I see. Well, if you have any questions, feel free to ask me as well. I'll try my best to answer them."

        hide yuuto

        show player_sprite

        mc "[m1], huh..."

        show player_sprite at sprite_jump

        "[pcname] shakes the thoughts off [p_their] head."

        mc "Where was I? Oh, right. I have some questions for you, [m1]."

        "To be continued? Or not. (This Visual novel is still on the works. Expect some changes to the plot and visuals. Thanks for reading.)"

        "-Ayid the slayer and the Sengoku Guys. EYYYYYY"