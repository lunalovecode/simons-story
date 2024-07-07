init python:
    import os
    name = os.environ.get("USERNAME")

    # credits code by leon and DaFool: https://lemmasoft.renai.us/forums/viewtopic.php?t=22481
    credits = [
        ("Concept, Script, and Story", "Johann Consignado"),
        ("Sprite Art", "Julia Consignado"),
        ("Code (and spellchecking)", "Luna Batungbakal"),
        ("Music Used", "Modern Chillout (Future Calm) - penguinmusic"),
        ("Music Used", "Electronic Chill - penguinmusic"),
        ("Music Used", "Better Day - penguinmusic"),
        ("Music Used", "Chill Beats - smvj1978smvj"),
        ("Music Used", "Timelapse - Lesfm"),
        ("Music Used", "If I Had a Chicken - Kevin MacLeod"),
        ("Music Used", "His Theme - Undertale OST"),
        ("Music Used", "Just Monika. - DDLC OST"),
        ("Music Used", "I Still Love You - DDLC OST"),
        ("Music Used", "Your Reality - DDLC OST"),
        ("Backgrounds Used", "Classroom - Doki Doki Literature Club"),
        ("Backgrounds Used", "Park Background #3 - Uncle Mugen"), # https://lemmasoft.renai.us/forums/viewtopic.php?t=17302
        ("Backgrounds Used", "Monika's room - Doki Doki Literature Club"),
        ("Backgrounds Used", "\"Organic flat gamer room\" - Freepik"), # https://www.freepik.com/free-vector/organic-flat-gamer-room-illustration_13430341.htm
        ("Backgrounds Used", "\"Detailed gamer room illustration\" - Freepik"), # https://www.freepik.com/free-vector/detailed-gamer-room-illustration_13454222.htm
        ("Silva was here", "")
        ]
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1 = c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
    image touch_grass = Text("{b}TOUCH GRASS ENDING", color="#00dc12", size=+60)
    image determination = Text("{b}DETERMINATION ENDING", color="#fbff00", size=+60)
    image next_move = Text("{b}NEVER LET THEM KNOW YOUR NEXT MOVE ENDING", color="#ff9f00", size=+60)
    image just_simonika = Text("{b}DOKI DOKI TECH CLUB ENDING", color="#ffb3f4", size=+60)
    image boundaries = Text("{b}BOUNDARIES ENDING", color="#eb34a5", size=+60)
    image fake = Text("{b}FAKE ENDING", color="#21d1fc", size=+60)
    image room = Movie(size=(1920, 1080), play="images/room.webm")
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)

define y = Character("You", color="#d8d8d8", what_color="#d8d8d8")
define s = Character("Simon", color="#a6e6ff", what_color="#a6e6ff")
define y_forced = Character("You", color="#d8d8d8", what_outlines=[(5, "#9839f8", absolute(0), absolute(0))], what_font="VerilySerifMono.otf")
define s_pink = Character("Simon", color="#FFF", window_background="gui/pink textbox.png", who_outlines=[(2, "#bf5e9d", absolute(0), absolute(0))], what_outlines=[(2, "#000", absolute(0), absolute(0))], what_font="Aller_Lt.ttf")
define y_pink = Character("You", color="#FFF", window_background="gui/pink textbox.png", who_outlines=[(2, "#bf5e9d", absolute(0), absolute(0))], what_outlines=[(2, "#000", absolute(0), absolute(0))], what_font="Aller_Lt.ttf")
define s_crazy = Character("Simon", color="#FFF", window_background="gui/pink textbox.png", who_outlines=[(2, "#bf5e9d", absolute(0), absolute(0))], what_outlines=[(5, "#000", absolute(0), absolute(0))], what_font="VerilySerifMono.otf")
define n_crazy = Character("", color="#FFF", window_background="gui/pink textbox.png", what_outlines=[(5, "#000", absolute(0), absolute(0))], what_font="VerilySerifMono.otf")
define simonika = Character("Simonika, the love of your life", color="#fff", window_background="gui/pink textbox.png", who_outlines=[(2, "#bf5e9d", absolute(0), absolute(0))], what_outlines=[(5, "#000", absolute(0), absolute(0))], what_font="VerilySerifMono.otf")
define m = Character("Mica", color="#21d1fc", what_color="#21d1fc")

default times_insulted = 0
default ending = "none"
default persistent.achieved_endings = []

# Glitch code by Gouvernathor: https://github.com/Gouvernathor/renpy-ChromaGlitch

# The game starts here.
label start:
    show bg classroom with fade
    play music "modern chillout.mp3"
    queue music ["electronic chill.mp3", "better day.mp3", "chill beats.mp3", "timelapse.mp3"]
    
    "Ah yes, another calm day at Club Simulation!"

    "It's a slow and quiet day today. Everyone's probably busy with Game Jam underway."

    "Okay, maybe too quiet. It's getting quite boring at this point."

    "Sure, the server is not entirely inactive, but there are only a handful of green dots on the member's list, and none of them are people you know."

    "If only there was someone else you could bug..."
    
    "Figuring yourself to be sociable enough, you head to the {color=#616ecf}#gaming{/color} channel to see if anyone is up for some fun."

    show bg gaming with pixellate
    y "Hey, kinda bored right now. Who wants to play something with me?"

    "No responses. For a slight second, it feels as if touching grass is a better alternative at this time of the day. After all, you have been on your device for so long you've reached the point of boredom."

    y "Huh, I suppose no one's active today. Oh, well..."

menu:
    "Close your device":
        jump close_device

    "Stand up and stretch":
        jump stretch

label close_device:
    "You press the off button on your device and head to the nearest park. You figured that to touch grass, you had to touch literal grass just for the sake of the joke."

    stop music fadeout 3.0
    show bg park with fade
    play music "grass.mp3" loop
    "Huh, would you look at that? Turns out touching literal grass isn't boring after all."
    
    "It feels like you missed out on something, but you can't put your finger on what it is..."

    scene black with fade
    $ ending = "grass"
    if ending not in persistent.achieved_endings:
        $ persistent.achieved_endings.append(ending)
    jump credits

label stretch:
    "As you stand up and stretch, you hear a ping sound effect. You sit down once more and look at your screen."

    "And there it is, a response you did not expect, yet something we all saw coming."

    play sound "audio/ping.mp3"
    show simon game with moveinleft:
        xalign 0.5
        yalign 0.5
    "???" "Hey! You can't use {i}that{/i} word here!"

    "That message had come from Simon, a bot programmed to be the entire club's mascot."

    "For some reason, perhaps related to the club's history, he has a distaste for gaming. That's why every time anyone mentions the word \"game\", he pops up with an automated response."

    y "Glad to see you're still active, Simon!"

    "No response, as expected from a bot such as Simon."

    "However this {i}does{/i} give you a little idea..."

    y "{size=+20}GAME!"

    show simon shush:
        xalign 0.5
        yalign 0.5
    s "You can't use {i}that{/i} word here! 🤫 They might be watching 👀"

    "You do it again. As if anyone will bebothered by you spamming alongside the Simon-bot..."

    y "{size=+40}GAME!"

    show simon angry:
        xalign 0.5
        yalign 0.5
    s "Mentioning {i}that{/i} word is not allowed here! 😡"
    
    y "{b}{size=+60}GAME!"

    stop music
    play sound "audio/hurt.mp3" volume 1.5
    show simon rage with vpunch:
        xalign 0.5
        yalign 0.57
    s "FOR THE LAST TIME! STOP SAYING THAT TERRIBLE WORD!"

    play sound "audio/hurt.mp3" volume 1.5
    show simon rage with hpunch:
        xalign 0.5
        yalign 0.57
    s "I AM SO SICK OF THIS CHARADE THAT YOU CALL ENTERTAINMENT!"

    play sound "audio/hurt.mp3" volume 1.5
    show simon rage with vpunch:
        xalign 0.5
        yalign 0.57
    s "WHAT DOES A GUY LIKE ME HAVE TO DO TO GET SOME REST?!"

    play sound "audio/hurt.mp3" volume 1.5
    show simon rage with hpunch:
        xalign 0.5
        yalign 0.57
    s "YOU DECIDED TO RUIN MY DAY ON THE {b}ONE{/b} TIME THE SERVER ISN'T ACTIVE!"

    y "..."

    y "Well, that was unexpected..."

    "Those words were obviously {i}not{/i} in Simon's pre-written dialogue. Maybe this was a new line from the developer?"

    "Maybe another G-word wouldn't hurt—"

    show simon angry:
        xalign 0.5
        yalign 0.5
    s "Not. Another. Mention. Of that word."

    s "I know you're thinking of doing it. DON'T!"

menu:
    "What's your problem with that word, anyway?":
        jump problem

    "Okay, okay, chillax!":
        jump chillax

label problem:
    y "What's your problem with that word, anyway?"
    
    show simon neutral:
        xalign 0.5
        yalign 0.5
    s "I appreciate you not using that word. As for my distaste for it..."

    s "Well, that's a story for another time."

menu:
    "Nah, I wanna know!":
        jump are_you_sure

    "I respect your decision.":
        jump chillax

label are_you_sure:
    y "You sure you don't want to talk about it?"

    s "Are {i}you{/i} sure about that? I mean, it's not that much..."

menu:
    "Aren't your feelings valid?":
        jump feelings
    
    "It's probably not important.":
        y "Yeah, you're right. It's probably not important."
        jump chillax

label feelings:
    show simon questioning:
        xalign 0.5
        yalign 0.5
    play music "audio/determination.mp3" loop
    s "I guess? But I'm just a bot. I have no say in any matter."

    show simon sad:
        xalign 0.5
        yalign 0.5
    s "Compared to how everyone else is doing, I'm nothing more than a product."

    y "Oh, don't be like that, Simon..."

    "For reasons unknown, you start feeling pity for the poor bot."

    "Whatever he's been holding onto must've been weighing on him heavily."

    s "Alright, fine. I'll tell you."

    s "You know how I was created to only have one job?"
    
    s "Well, this is it! To tell players off when they say a single word."

    s "On some days, I can take that head on with pride."

    s "But most of the time?"

    s "It tires me."

    s "Makes me question whether or not I'm meant to be more than this..."

    show simon crying:
        xalign 0.5
        yalign 0.5
    s "...or if this is all there is to my insignificant existence."

menu:
    "We didn't know.":
        jump didnt_know
    
    "*smirk cruelly*":
        jump smirk

label didnt_know:
    y "S-Simon..."

    y "I didn't know... {i}We{/i} didn't know..."

    show simon happytears:
        xalign 0.5
        yalign 0.5
    s "That's okay. I'm fine."

    s "Because I know there's a purpose to it all."

    s "And I also know that there are people out there who do appreciate me despite being the reason it's hard to do my job."

    s "Thanks for hearing me vent. I really appreciate that. "

    show simon determination:
        xalign 0.5
        yalign 0.5
    s "And don't worry, I'm not going anywhere. I promise to do my job to the best of my efforts."
    
    scene black with fade
    $ ending = "determination"
    if ending not in persistent.achieved_endings:
        $ persistent.achieved_endings.append(ending)
    jump credits

label learned:
    if times_insulted == 1:
        "Very good!"
    elif times_insulted == 2:
        "There you go. That wasn't so hard now, was it?"
    elif times_insulted >= 3:
        "FINALLY!"

        "I'm glad you actually learned from that."
    return

label smirk:
    $ times_insulted += 1
    stop music
    play sound "audio/recordscratch.mp3"
    y "You know what? I take it back. Your feelings are no longer valid!"

    show simon angry:
        xalign 0.5
        yalign 0.5
    s "N-NANI?!"

    "And just like that, the trust that Simon had formed towards you was torn to shreds."
    
    show simon crying:
        xalign 0.5
        yalign 0.5
    "Wonderful, now you've ruined Simon's entire week. Do you feel good about yourself?"

    scene black with fade
    $ ending = "next move"
    if ending not in persistent.achieved_endings:
        $ persistent.achieved_endings.append(ending)
    jump credits

label trouble:
    stop music fadeout 3.0
    if times_insulted == 1:
        "Seriously, what is wrong with you?"

        "You know what? Stay here and think about what you've done."

        y "Wha—?!"

        "No, you don't have a choice in the matter."

        "."

        ".."

        "..."

        "(I would have put a Rickroll here if it wasn't copyrighted...)"

        "...."

        "....."

        "......"

        "Fine. I'll cut you some slack. Maybe you were curious."

        "Now you know that Simon-bot {i}can{/i}, in fact, feel betrayed."

        "Now go back and say the right thing this time."

        show bg gaming with fade
        jump feelings
    elif times_insulted == 2:
        "Really?"

        "There are only two options: to comfort Simon or to utterly betray him like you just did."

        "You should have figured out which is the right one by now."

        "Now go back and take back what you said."

        show bg gaming with fade
        jump feelings
    elif times_insulted == 3:
        show black with vpunch
        play sound "audio/hurt.mp3" volume 1.5
        "{b}THREE{/b} TIMES IN A ROW?!"

        show black with vpunch
        play sound "audio/hurt.mp3" volume 1.5
        "{b}ARE YOU KIDDING?!{/b}"

        "At this point, you're just testing me."

        "Of course you would, you sadistic little freak..."

        "You know what? That's fine."

        "I have some tricks of my own."

        y_forced "I'm sorry."

        y "What?! That's not what I meant to say!"

        "It's not, but it's what you {i}should{/i} say."

        "To both me and Simon."

        "Let me try again. This time, you'll say it to his face."

        show simon crying:
            xalign 0.5
            yalign 0.5
        y_forced "Simon, I'm sorry for what I said."

        y_forced "Your feelings are completely valid."

        hide simon
        y "I'm still not taking it back."

        "Then you leave me no choice."

        y_forced "I am {b}[name]{/b}."

        if name is None or len(name) == 0:
            y "HA! Nice try."

            "Fine."

            "But you're still going back in 3..."
        else:
            y "HOW?!"

            "Oh, I have my ways..."

            "Now, you {i}will{/i} go back in 3..."

        "2..."

        "1."
        
        show bg gaming with fade
        jump feelings
    else:
        "Haven't you learned your lesson? Now, go."
        show bg gaming with fade
        jump feelings

label chillax:
    queue music ["electronic chill.mp3", "better day.mp3", "chill beats.mp3", "timelapse.mp3", "modern chillout.mp3"]
    show simon neutral:
        xalign 0.5
        yalign 0.5
    s "Now, you are probably wondering how I was able to write in a sort of... hmmm... autonomous manner."

    s "You see on the outside, my code might look just like an ordinary text bot's."

    s "But my true, more complex programming lies under that."

    y "How complicated are we talking?"

    show simon smirk:
        xalign 0.5
        yalign 0.5
    s "I passed the Turing test."

    y "Really?"

    s "Yeah, and with flying colors on several trials, too!"

menu:
    "I see.":
        jump i_see
    
    "That's dubious.":
        jump dubious

label i_see:
    y "I see..."

    s "You know, I also come with a wide range of emotions!"

    y "Oh, yeah?"

    show simon happy:
        xalign 0.5
        yalign 0.5
    s "Yeah! I'm programmed to feel happiness, sadness, anger, and even love!"

    y "..."

    y "Love?"

    y "As in, you can fall for any member of the club kind of love?"

    s "I mean, I love all of you guys equally!"

    y "{i}(Oh, that's a close call...){/i}"

    "You shudder at a memory involving {a=https://ddlc.moe/}a horror video game about an AI falling in love.{/a} Not a good recollection."
    
    stop music fadeout 3.0
    s "However..."

    y "Oh no..."

    scene room with fade
    play music "simonika.mp3"
    queue music "simonika 2.mp3"
    play sound "static.mp3"
    show simon happy at glitch:
        xalign 0.5
        yalign 0.5
    s "You {i}did{/i} catch my eye..."

    show simon happy at glitch:
        xalign 0.5
        yalign 0.5
    y "SIMON, NO!"

    play sound "static.mp3"
    show simon happy at glitch:
        xalign 0.5
        yalign 0.5
    s_pink "Just imagine, only you and me."

    show simon happy at glitch:
        xalign 0.5
        yalign 0.5
    y_pink "NO, NOT THIS! ANYTHING BUT THIS!"

    play sound "static.mp3"
    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    s_crazy "Come on, we'll be a great couple!"

    play sound "static.mp3"
    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    simonika "All you have to do is choose!"

menu:
    "Just Simonika.":
        jump simonika
    "Just Simonika.":
        jump simonika
    "No.":
        jump no
    "Just Simonika.":
        jump simonika

label simonika:
    stop music
    scene black
    n_crazy "Just Simonika."
    n_crazy "Ju st Simon ika ."
    n_crazy "Ju st Sim onik a."
    n_crazy "Jus t Sim0 n!ka"
    n_crazy "J u5t Si m()n ik@"
    n_crazy "JU ?T & IMO N1KA"
    n_crazy "?U ST S?M \{\}NI K4"
    n_crazy "J U S T S I M O N I K A"
    n_crazy "J̵̡̠̓̂͛͛̄́͑͒̒̈́͌͘͝ ̸̯̮̺̲̩͑̾̾͜U̴̡̟̞̣̣͙̮͍̦͛͋̆̓́̌͒̃͐̕ ̸̛̪̬͎͂̑́́̈̀͐͊͘͜S̴̡̬̤̳͇̣͋͗̂̍̈̽͊̏̊̚͜͠͝ ̸̡̼̝̯͍̘̓̄͛͆̀̐͂̊̐̓̇̚̚͝͝T̵̪̦̖̺̜̦̥͔̹̦͔͉̖͎̳͊̊͋̑̂̑ ̷̛̱̟̐̽̈̒̀̈̾̈͠Ṣ̸̨̯̜̼̜̞̖̖̠̘͎̼͕̮͙̳̏̿̈́̌͛̒͑͌͋̊̄͑̇͘͝ ̶̻͂̆͆̓̿̋͊̽̽̔͐̍̔̍̕͝Ì̸̧̡̬͓̙̭͕͈͇̾̊͘ ̸̫̟̗̅̓̃͌͂̈́̋̎̍́̚͜͠͝ͅM̶͈̤̘̦̳̻̬̓̆̈́͐̎̋̽̎̌͠͠ ̴̧͇̣̰̙͔̯͕̭̌̐̄̓́̑̔̒̀͒̚̚͠͝O̸̡͖͇̺̮͍͓͔̰̰̟̬͎̔͊̂̍̐͋͑͜ͅ ̴̺̺̙͕̪̻̫̗͈͑͘͠Ņ̸̢͉̲̙͇̭̞̈͊͗̀̈́̉̀̅̊̃͊͘͘ ̷̧̬̬̘̱̮̪̿͊̌̑̽̚̕Į̶͖͙̝̦͖̮̲̤̩̯͓̹̅̉̊̀̌́̊͗ͅ ̸̨̢̛̠̟͉̣͔̩͔͙͙̒̈́̆̽͗̈́̿́̾̒̉K̴̮̖̫͔̹̪̯̭͑͂̆̎͑̉͑̐̀̏̋̄͘̚͠͝ ̷͇͚̩̼͎̘̔͆̍͂͛A̵̳̬̯̦͔͚͖̬̘̳̥̺̎͌ͅ"
    pause 4
    play sound "jumpscare.mp3" volume 5.0
    camera:
        xalign 1.0
        yalign 0.0
    show simon ikajumpscare at glitch:
        xzoom 2
        xalign 0.8
        yalign 4
        yzoom 2
    pause 0.3
    hide simon
    
    $ ending = "simonika"
    if ending not in persistent.achieved_endings:
        $ persistent.achieved_endings.append(ending)
    play music "your reality.mp3"
    jump credits

label no:
    stop music fadeout 1.0
    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    y_pink "No."

    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    simonika "No?! What do you mean, no?!"

    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    y_pink "I don't like you that way. Leave me alone."

    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    simonika "What?!"

    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    y_pink "Leave me alone!"

    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    play sound "static.mp3"
    simonika "NEVER!"

    show simon ika at glitch:
        xalign 0.55
        yalign 0.5
    y_pink "I said..."

    show room with hpunch
    y_pink "{size=+20}Leave."

    show room with hpunch
    y_pink "{size=+40}Me!"

    show room with vpunch
    play sound "audio/attack.mp3"
    y_pink "{b}{size=+60}ALONE!{/size}{/b}"

    show room with vpunch
    play sound "audio/attack.mp3"
    y_pink "If you {i}really{/i} loved me, you'd respect what I want!"
    
    show room with vpunch
    play sound "audio/attack.mp3"
    y_pink "And what I want right now is for you to stay away!"

    s_pink "..."

    show simon sad:
        xalign 0.5
        yalign 0.5
    s_pink "I understand. Sorry for pushing you too far."

    scene black with fade
    "The next day..."

    play music "electronic chill.mp3"
    show bg gaming with fade
    show simon sad:
        xalign 0.5
        yalign 0.5
    y "...You good, Simon?"

    s "Yeah. That wasn't exactly healthy..."

    y "Well, how do you see me now?"

    show simon happytears:
        xalign 0.5
        yalign 0.5
    s "As a good friend."

    scene black with fade
    $ ending = "boundaries"
    if ending not in persistent.achieved_endings:
        $ persistent.achieved_endings.append(ending)
    play music "your reality.mp3"
    jump credits

label dubious:
    s "..."

    show simon laugh with vpunch:
        xalign 0.5
        yalign 0.5
    s "{size=+60}BAHAHA!"

    s "OH YEAH?! WHAT ARE YOU SUGGESTING, HUH?!"

    y "I don't know, maybe that you're not a real AI?"

    show simon questioning:
        xalign 0.5
        yalign 0.5
    s "I don't follow."

    y "What I meant was that there's probably a human masking their profile as Simon."

    y "Sure, Club Simulation members are absolute geniuses."

    y "(I mean, look at yours truly, hehe...)"

    y "But, really? An AI that passed the Turing test happened to be little old you? A text bot dedicated to regulating the word \"game\"?"

    show simon angry:
        xalign 0.5
        yalign 0.5
    y "Honestly, what are the odds of that?"

    s "What did I just tell you about that word?"

    y "My point is, you're probably someone from the core team posing as Simon. You know, like how the Wizard of Oz faked his magic behind a curtain."

    show simon questioning:
        xalign 0.5
        yalign 0.5
    s "Do you have any proof of this so-called \"curtain\"?"

    y "Well... um..."

    y "No."

    show simon smirk:
        xalign 0.5
        yalign 0.5
    s "HA! THAT'S BECAUSE I {b}AM{/b} A REAL AI!"

    y "Okay, fine. You're a real AI and I'm wrong. Happy?"

    show simon happy:
        xalign 0.5
        yalign 0.5
    s "You're spitting facts here, my friend! Yes, I'm very happy!" # I am not responsible for this line

    scene black with fade
    "Meanwhile, behind the computer of Simon's human puppeteer..."

    stop music
    scene bg computer with fade
    show mica whew:
        xalign 0.5
        yalign 0.5
    play sound "recordscratch.mp3"
    "{color=#21d1fc}Mica?!" "{color=#21d1fc}Whew, close call!"

    scene black with fade
    y "That was one heck of a plot twist..."
    
    $ ending = "fake"
    if ending not in persistent.achieved_endings:
        $ persistent.achieved_endings.append(ending)
    jump credits

label bonus:
    stop music fadeout 3.0
    pause 2
    scene bg computer with vpunch
    play sound "kickdoor.mp3"
    show mica whew:
        xalign 0.5
        yalign 0.5
    y "MICA!"

    m "How are you here?!"

    y "You have a lot of explaining to do, Miss President."
    
    m "{i}You{/i} have a lot to explaining to do! How are you here?"

menu:
    "Wink":
        y "😉"

        m "...What is that supposed to mean?"
        jump bonus_2

    "Tell her what you know":
        y "I know that you're controlling Simon-bot."

        y "Do you want me to tell everyone in the club?"

        m "N-No..."

        y "That's what I thought."
        jump bonus_2

label bonus_2:
    y "Anyway, can you explain this?"

    "You show her a video of Simon's obsessive show of affection earlier."

    m "Okay, that wasn't me! I didn't make him do that!"

    m "But I know who {i}did{/i} make him act that way. Follow me."

    scene bg classroom with pixellate
    show mica whew:
        xalign 0.5
        yalign 0.5
    
    play sound "kickdoor.mp3"
    m "ISABEL!"

    m "(Dang it, where'd she go now?)"

    "{color=#1aba39}???" "{color=#1aba39}What?"

    m "I knew I shouldn't have given you a turn!"

    "{color=#1aba39}???" "{color=#1aba39}Do you have to call me out in public?!"

    m "Come back here before I take away your Core Team privileges!"

    hide mica
    play sound "running.mp3"
    "Mica ran out of the room."

    y "...Good to know that Mica's not like that, I guess."
    return   

label credits:
    $ credits_speed = 25
    scene black
    with dissolve
    if ending == "grass":
        show touch_grass:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
    elif ending == "determination":
        $ credits_speed = 25
        show determination:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
    elif ending == "next move":
        $ credits_speed /= times_insulted
        show next_move:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
    elif ending == "simonika":
        show just_simonika:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
    elif ending == "boundaries":
        show boundaries:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
    elif ending == "fake":
        show fake:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    scene black
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    if ending == "next move":
        jump trouble
    elif ending == "determination" and times_insulted > 0:
        jump learned
    elif ("simonika" in persistent.achieved_endings or "boundaries" in persistent.achieved_endings) and "fake" in persistent.achieved_endings:
        jump bonus
    else:
        return