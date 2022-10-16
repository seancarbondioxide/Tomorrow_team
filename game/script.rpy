# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p1 = Character("???")
define p2 = Character("Professor")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    e "Huh? It's so dark, someone find a light switch"

    scene bg hallway

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy




    e "What is this weird place, I can see a shadow over there but can't see a face"

    show professor shadow
    hide eileen

    p1 "Welcome to my little game"
    p1 "You must answer some riddles to move to the next room"
    p1 "Answer wrong you may be turned away...."


    scene bg professor
    p1 "Or you may not survive.."





    #////////////////////////////////////////////////////////////////////////
    #SEAN
    #Call scene
    #call character
    #Dialogue


    #////////////////////////////////////////////////////////////////////////
    #BEN
    #Call scene
    #call character
    #Dialogue


    #////////////////////////////////////////////////////////////////////////
    #SHELLY
    #Call scene
    #call character
    #Dialogue

    #////////////////////////////////////////////////////////////////////////
    #ZEN
    #Call scene
    #call character
    #Dialogue

    #////////////////////////////////////////////////////////////////////////

    #CONNOR
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

    return
