import random 
import math
import time


def type_print(text1, delay=0.05):
    for char in text1:
     print(char, end='', flush=True)
     time.sleep(delay)
print()

text1=(
    """
???     : Hello Adventurer How do you do? Welcome to Avegard, A World filled with Monsters, Dragon, Magic and More 
          Firstly, Would you mind Telling me your name?
    """
)

type_print(text1)


name = str(input("""
Please enter your name:"""))

# wait i can just directly add the lines to type_print

type_print(f"""
Bob:      Ahhh, {name} thats a fine name, Like a true Warrior, Anyways We can have continue on the pleasantries later
          The Village is right now in danger, The monsters of the Northern Dragon King's Army is trying to capture 
          the village and keep its villagers as hostages and blackmail the Great Empire
          How do I know this? You dont need to know that, Just go ahead and swing you sword and defeat the Army like a 
          true stick swinger you are 
          Yes you, alone against a hoard of armed monsters
          Reinforcements? Never heard of that word, Anyway off you go Adventurer 
Narrator: So off you went trying to struggle against a hoarde of monster alone, eventhough you are just a low level 
          adventurer that just started this game 2 mins ago and as the Bob said, a stickswinger without even a sword
Narrator: As you get closer to the hoard of monster you relise they dont seem that tough, Its just 3 goblins or so you thought
          You charge forward with all the courage in you (and later realise that was a stupid decision) towards the hoarde trying
          not to shit your pants with a stick in your hand and hit a goblin and knock it out(dont ask how even idk)
          then you think to yourself "this wasnt that hard, 2 more to go" and so you turn around look st the other two goblins
          and i kid you not there was like 20 goblins which spawned out of thin air, to make matters worse there was a big buff 
          goblin warlord which also appeared out of thin air
          You think to yourself "Yep im dead, So much for my adventurer life which lasted 5mins, So much for the Harem plan I made
          But suddenly a bright light appears from above blinding you and suddenly you arent at the village anymore
          You think yourself "Am already in heaven?" (if your life was that easy i wouldnt have made this game)
???:      You are not dead, yet
Narrator: You look up to see a awfully conviniently placed angle which came a awfully convinient enough time, was this your luck? or
          was it plot armour? who knows.   
Angel:    Ill cut to the chase, I want you to help the village right now and then go on an adventure and defeat the Northern Dragon 
          King
Narrator: You think"Arent angels supposed to be more kind? and me defeating the dragon king? imm just a stick swinger"
Angel:    Ik you are just a stick swinger(Yes she can read your mind) But if you use my conviniently placed armour and wepons here you 
          can defeat them
          Do you accept?
Narrator: Then you ask her "Cant you just beat him yourself, I mean you are literally an ANGEL!!"
Angel:    Well 1) I dont want to its too troublesome for me to go down and beat that punk
               2) I'd rather watch you suffer and try to beat him than wipe him out with a single move
               3) I'm too busy farming materials and husbandos in my gacha game so bug off 
               So do you accept or not ?
Narrator: You realising the angel is not an angle but just a shut-in gacha addict thinks about her offer
""")

offer = str(input("Do you accept the angels offer? (y/n):"))

if offer == "y":
   type_print("""
Angel:     Oh good i finally have someone to do my job, Useless sure but the armour is too OP, you literally cant die
Narrator:  +1 Heavenly OP armour set, +1 Heavenly OP sword 
Narrator:  You feel the power surge in you as you get the loot
Angel:     Alr off you go hopefully i dont have to see you
Narrator:  Suddenly you wake up in the same place in the same situation like nothing happened at but now you got you sword 
           and armour and so you decided to battle the goblin horde ( even tho your till sccared af)

           BATTLE BEGINS 
""")
   attack = str(input("""Choose what move to use: 
1)Sticker swinger special   2)Excalibuhhhhhh
3)Basic attack 1            4)Touch them with your sword 

(choose the number):"""))

   if attack in {"1" , "2", "3", "4"}:
      type_print("""
Narrator: Becuase of your OP sword the moment the sword comes near the goblins they just disintergrate, and the goblin warlord
          has already staterd running away
          First time in your life you actually feel like you are useful, the villager thanks you and everyone was saved, though
          you never saw bob again 
Narrator: And so after the events happpened at the village ypu truly set out on your journey 
          Now, Because Im way too lazy to type out rest of the story here's what happens 
          You travel to many countries and gather companions to travel together with, since the OP armour cannot change a person
          you were irresponsible enough to get a girl pregnant without meaning to, but from your travels you have dtarted to change 
          and actually cared for your now wife (good job on not trying to go buy milk), eventually you reached the Northern Dragon Kings
          lair to defeat him. You reach his lair and see a a big dragon with scales as thick as ERA armour of a soviet tank, but regardless
          you and your trusty sword and stick swinger abilities defeat him
          You are crowned a hero and you live happily ever after ( mostly because im lazy to write a dramatic ending, wondring where Bob went)


                                                                 THE END   
""")


elif offer == "n":
   type_print(
"""
Angel:    Oh, you wont acccept my offer you mere mortal, you should've really known you place, Too bad
Narrator: Too bad kid, you very unfortunately made the wrong choice it seems, you suddenly wake up where you were earlier, surrounded by goblins
          if anything, you know you've messed up big time and should've taken the angels offer
          the goblins pounce on you one by one hitting the shi out of you with their sticks annd getting thrown around, to finish the job the warlord
          comes and tears you limb to limb making you have a very painful death indeed

                                                                    YOU DIED.
                                                                     THE END
"""
   )