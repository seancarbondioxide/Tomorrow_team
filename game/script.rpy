# Declare characters used by this game. The color argument colorizes the
# name of the character.


define h = Character('Harry', color = "#008080")
define s = Character('Sofia', color = "#c8ffc8")
define c = Character('Chloe', color = "#c8c8ff")
define m = Character('Max', color = "#800080")


# The game starts here.

label start:

    scene bg car

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show hajime smile:
        xalign 1.0
        yalign 1.0


    h "What a great way to start our holiday!"

    hide hajime smile

    show sayaka happy:
        xalign 1.0
        yalign 1.0

    s "Yeah! Work has been busy as. I'm glad we can finally get together."

    hide sayaka happy

    show makoto solve:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "Hey Chloe, you alright? You've been driving for a while."

    hide makoto solve

    show chiaki yawn:
        xalign 1.0
        yalign 1.0

    c "Yeah I'm fine. There's still a bit of road to cover."

    hide chiaki yawn

    show chiaki wonder:
        xalign 1.0
        yalign 1.0

    c "Hey Harry, you must be tired from work eh?"

    hide chiaki wonder

    show hajime laugh:
        xalign 1.0
        yalign 1.0

    h "Haha yeah. But I'm glad I don't have to think about work."

    hide hajime laugh

    show sayaka unsure:
        xalign 1.0
        yalign 1.0

    s "Look at all that fog, I'm a little worried that we might get lost..."

    s "I haven't seen a car in a long time, to be honest I don't really want to leave the car and explore until we reach our destination"

    hide sayaka unsure

    show chiaki point:
        xalign 1.0
        yalign 1.0

    c "Don't worry Sam, As long as we've got the GPS we'll be fine!"

    hide chiaki point

    show makoto deny:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "Sorry to interupt, but I {b}really{b} need to go to the bathroom..."

    hide makoto deny

    show hajime sad:
        xalign 1.0
        yalign 1.0

    h "Seriously? Can't you wait a little longer? I'm sure we'll be there within the hour..."


    hide hajime sad

    show makoto insist:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "No... I don't think I can hold much longer. Can you pull over Daisy?"

    hide makoto insist

    show chiaki stern:
        xalign 1.0
        yalign 1.0

    c "Alright, let me find a place to pull over. Just give me a minute."

    hide chiaki stern

    scene bg barn #Scene to be drawn up? Used a Placeholder image for now.
    with dissolve

    show hajime determined:
        xalign 1.0
        yalign 1.0

    h "This looks like a nice place."

    hide hajime determined

    show makoto frustrated:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "Can't talk, I'm going inside. Surely they have a bathroom. Why don't you wait outside? I shouldn't be long."

    hide makoto frustrated

    show sayaka guard:
        xalign 1.0
        yalign 1.0

    s "Can you hurry up Max? I really don't want to stay in some unknown location, its getting quite dark and I want to get going!"

    hide sayaka guard

    show chiaki sigh:
        xalign 1.0
        yalign 1.0

    c "Don't worry about him Sam. Let's just focus on getting ready to leave when he comes back."

    hide chiaki sigh

    show sayaka hesitate:
        xalign 1.0
        yalign 1.0

    s "Thanks Chloe. It's just... the fog. Its getting thicker. I've never seen so much fog, something just isn't right..."

    hide sayaka hesitate

    show hajime laugh:
        xalign 1.0
        yalign 1.0

    h "Honestly, what are you worried about Sam? We're all together, we've got our phones, it's not like we're trapped in some asylum. Lighten up!"

    hide hajime laugh

    show sayaka cold:
        xalign 1.0
        yalign 1.0

    s "Don't do that Harry. I'm just trying to be careful. Its just us 4."

    hide sayaka cold

    show hajime laugh:
        xalign 1.0
        yalign 1.0

    h "Alright, alright... I'll stop! Haha."

    hide hajime laugh

    show hajime ponder:
        xalign 1.0
        yalign 1.0

    h "Not to stay on the same topic, but where is Max? Its been a little while and he hasn't returned yet."

    hide hajime ponder

    show hajime nervous:
        xalign 1.0
        yalign 1.0

    h "Surely, he wouldn't be trapped {b}inside{b}?"

    hide hajime nervous

    show sayaka scared:
        xalign 1.0
        yalign 1.0

    s "Harry {b}STOP{b} joking around. He could be in trouble."

    hide sayaka scared

    show chiaki a:
        xalign 1.0
        yalign 1.0

    c "What if he is inside? Shouldn't we go and investigate?"

    hide chiaki a

    show sayaka ghost:
        xalign 1.0
        yalign 1.0

    s "Explore some old barn? Hell no! I'm staying here."

    hide sayaka ghost

    show hajime point:
        xalign 1.0
        yalign 1.0

    h "C'mon, safety in numbers, we'll be fine. We'll go in together."

    hide hajime point

    show sayaka cold:
        xalign 1.0
        yalign 1.0

    s "Alright but I'm sticking close to you two."

    hide sayaka cold

    show chiaki wonder:
        xalign 1.0
        yalign 1.0

    c "We'll be fine. Let's find Max, get back to the car and leave."

    hide chiaki wonder

    show hajime point:
        xalign 1.0
        yalign 1.0

    h "I'll lead the way. Just follow closely."

    hide hajimed point

    scene black
    with dissolve


    show hajime clench:
        xalign 1.0
        yalign 1.0

    h "I can't see a thing in here... its pitch black. Can you two see anything?"

    hide hajime clench

    show sayaka nervous:
        xalign 1.0
        yalign 1.0

    s "Me Neither, this was a terrible idea! What about you Chloe?"

    hide sayaka nervous

    show chiaki search:
        xalign 1.0
        yalign 1.0

    c "Not really no, but let's keep walking... stay close to me."

    hide chiaki search

    show hajime blink:
        xalign 1.0
        yalign 1.0

    h "Let's just keep following this path until..."

    hide hajime blink

    scene black
    with vpunch

    show hajime shocked:
        xalign 1.0
        yalign 1.0

    h "GAHHH!"

    hide hajime shocked

    show bg foyer
    with fade

    show chiaki sick:
        xalign 1.0
        yalign 1.0

    c "Ow... My legs, we must have fallen through some sort of a trap door."

    hide chiaki sick

    show hajime what:
        xalign 1.0
        yalign 1.0

    h "Is everyone alright? That felt like quite a drop."

    hide hajime what

    show sayaka slightsmile:
        xalign 1.0
        yalign 1.0

    s "I'm fine Harry... but..."

    hide sayaka slightsmile

    show sayaka scared:
        xalign 1.0
        yalign 1.0

    s "Where are we??? This looks straight out of a horror movie I saw."

    hide sayaka scared

    show hajime scared:
        xalign 1.0
        yalign 1.0

    h "I don't know but this doesn't look anything like the barn that we saw from the outside... "

    hide hajime scared

    show hajime what:
        xalign 1.0
        yalign 1.0

    h "Wait, is that Max?"

    hide hajime what

    show chiaki a:
        xalign 1.0
        yalign 1.0

    c "Oh shoot, you're right! Max!"

    hide chiaki a

    show makoto whatever:
        xalign 1.0
        yalign 1.0
        zoom 1.4


    m "Ow... My head, where am I?"

    hide makoto whatever

    show hajime gasp:
        xalign 1.0
        yalign 1.0

    h "Max! Oh my god are you alright? We thought we lost you."

    hide hajime gasp

    show makoto vshocked:
        xalign 1.0
        yalign 1.0
        zoom 1.4


    m "I'm fine guys, thanks. I just walked into the barn and then fell through some trap door. It looked nothing like the outside"

    hide makoto vshocked

    show hajime shocked:
        xalign 1.0
        yalign 1.0

    h "What is happening?! Is our mind playing tricks on us?!"

    hide hajime shocked

    show chiaki holdbreath:
        xalign 1.0
        yalign 1.0

    c "Harry calm down... I'm just anxious as to find out where we are but right now we need to focus on getting out of here"

    hide chiaki holdbreath

    show hajime clench:
        xalign 1.0
        yalign 1.0

    h "I guess you're right Chloe. Maybe we should look around. At least we've got each other's company."

    hide hajime clench

    show makoto solve:
        xalign 1.0
        yalign 1.0
        zoom 1.4


    m "Wait, I have an idea, there are some doors behind us, why don't we try leaving from there?"

    hide makoto solve

    show hajime ponder:
        xalign 1.0
        yalign 1.0

    h "That's not a bad idea Max, at least it'll give us an idea where we are!"

    hide hajime ponder

    show hajime determined:
        xalign 1.0
        yalign 1.0

    h "Maybe we'll be able to head back to our car this way!"

    hide hajime determined

    show sayaka hesitate:
        xalign 1.0
        yalign 1.0

    s "I'm all for trying anything if we're together. Chloe?"

    hide sayaka hesitate

    show chiaki clutch:
        xalign 1.0
        yalign 1.0

    c "Yeah anything is better than staying in this horrid place. Let's have a look outside."


    scene bg exterior
    with dissolve

    show sayaka terrified:
        xalign 1.0
        yalign 1.0

    s "What is this supposed to be?!"

    hide sayaka terrified

    show chiaki a:
        xalign 1.0
        yalign 1.0

    c "This looks like some sort of an asylum or old hospital..."

    hide chiaki a

    show chiaki sick:
        xalign 1.0
        yalign 1.0

    c "It looks like the fog has gotten very thick as well. I can't see a thing out there."

    hide chiaki sick

    show hajime drool:
        xalign 1.0
        yalign 1.0

    h "Maybe we shouldn't go back inside... We could explore this area?"

    hide hajime drool

    show makoto determined:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "I'm not sure..."

    hide makoto determined

    show makoto blink:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "As much as I don't want to go inside, it's quite dark outside, and the fog just makes things worse."

    hide makoto blink

    show sayaka ghost:
        xalign 1.0
        yalign 1.0

    s "Can we at least try exploring the outside? I really don't want to go back in there."

    hide sayaka ghost

    show makoto idea:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "Alright... we'll have a look around."

    hide makoto idea

    scene black
    with dissolve

    scene bg exterior
    with dissolve

    show hajime laugh:
        xalign 1.0
        yalign 1.0

    h "Hey... didn't we just pass this building??"

    hide hajime laugh

    show makoto deny:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "It does look like the same one, yes..."

    hide makoto deny

    show sayaka scared:
        xalign 1.0
        yalign 1.0

    s "It can't be... let's try exploring one more time."

    hide sayaka scared

    scene black
    with dissolve

    show chiaki a:
        xalign 1.0
        yalign 1.0

    c "It's so foggy, I can't see a thing..."

    hide chiaki a

    show hajime determined:
        xalign 1.0
        yalign 1.0

    h "Hey look! I see a building!"

    hide hajime determined

    scene bg exterior
    with dissolve


    show hajime deny:
        xalign 1.0
        yalign 1.0

    h "That's the same building that we've been seeing, isn't it?"

    hide hajime deny

    show makoto solve:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "You know, I think we're stuck in some sort of loop."

    hide makoto solve

    show makoto deny:
        xalign 1.0
        yalign 1.0
        zoom 1.4

    m "As much as I hate to say this, I think we should go back in. We've exhausted our options and we're no closer to finding a way out."

    hide makoto deny

    show sayaka hesitate:
        xalign 1.0
        yalign 1.0

    s "As much as I don't want to go back in that horrid place, I don't think we have a choice."

    hide sayaka hesitate

    show chiaki stern:
        xalign 1.0
        yalign 1.0

    c "Fine. We'll go back inside, but we need to stick together. This is getting creepy enough as it is."

    hide chiaki stern

    show hajime scared:
        xalign 1.0
        yalign 1.0

    h "Sigh... Guess we don't have a choice. Let's go back in."

    scene black
    with dissolve

    show bg foyer
    with fade

    show makoto think:
        xalign 1.0
        yalign 1.0

    m "It looks like there's multiple ways we can go..."

    #////////////////////////////////////////////////////////////////////////
    #SHELLY
    #Call scene
    #call character
    #Dialogue


    #////////////////////////////////////////////////////////////////////////
    #SEAN
    #Call scene
    #call character
    #Dialogue


    #////////////////////////////////////////////////////////////////////////
    #CONNOR
    #Call scene
    #call character
    #Dialogue


    #////////////////////////////////////////////////////////////////////////
    #BEN
    #Call scene
    #call character
    #Dialogue

    #////////////////////////////////////////////////////////////////////////
    #NIKHIL
    #Call scene
    #call character
    #Dialogue

    #////////////////////////////////////////////////////////////////////////


    # This ends the game.
