#----------TO DO LIST----------#
#
# - Add Boss Bar
# - Reorder achievements
# - Speed up Taco Bell
#

# POST TESTING:
# - Buff John Cena
# - Buff Tel Aviv Dude
# - Gerardo health to 150
# - Chengus health to 250
#------------------------------#



#Packets
import time
import replit
from random import *
import sys
import json

#Conversation
from conversation.response import *

#Eat With Him
from eatwithhim.tacobell import *
from eatwithhim.popeyes import *
from eatwithhim.wendys import *

#Go to Israel
from israel.jerusalem import *
from israel.telaviv import *
from israel.lod import *

#Bosses
from bosses.cheng import *
from bosses.gerardo import *

#Times:
times = 0
times1 = 0
times2 = 1
times3 = 0
last = ""

#Achievements:
achievements = 11
achieve = 0
ecuador = 0
johncena = 0
popeyes = 0
eaten = 0
psycho = 0
horse = 0
lod = 0
deport = 0
boss1 = 0
boss2 = 0
boss3 = 0
boss5 = 0
boss6 = 0

#Inventory
im = 0 #Israeli Merch (1)
ja = 0 #Joaquin Body Armor (2)
bb = 0 #Big Belly Armor (3)
rm = 0 #Robber's Mask (4)
ca = 0 #Chengus Armor (7)

ba = 0 #Basic (0)
qs = 0 #Quesadilla Sword (1)
pb = 0 #Papa Baton (2)
ww = 0 #Wendy's Whip (3)
jc = 0 #John Cena's Biceps (5)
cs = 0 #Chengus Slayer (7)

#Boss Fights
strength = 0
low = 1
high = 5
armor = 0
health = 50

armor1 = "Basic Armor"
armor2 = "Empty"
weapon1 = "Basic Weapon"
weapon2 = "Empty"


#-------------REGISTRATION-------------#


#-------Log in/Register-------#
while 0 == 0:
  answer = input("What do you want to do: \n(1) - Log in\n(2) - Register\n\nType the number of what you want to do: ")\

  if answer == "2" or answer == "1":
    break
  else:
    replit.clear()


#-------Log in-------#
if answer == "1":
  loadName = input('\nWhat is your username? ')
  info = json.load(open( loadName+".json" ) )
  username = info['name']
  password = info['password']
  while 0 == 0:
    encrypt = input('What is your password? ')
    if encrypt == password:
      #---Load Achievements---#
      playerachieve = info['achieve']
      achieve = playerachieve[0]
      ecuador = playerachieve[1]
      johncena = playerachieve[2]
      popeyes = playerachieve[3]
      eaten = playerachieve[4]
      psycho = playerachieve[5]
      horse = playerachieve[6]
      lod = playerachieve[7]
      deport = playerachieve[8]
      boss1 = playerachieve[9]
      boss2 = playerachieve[10]
      boss3 = playerachieve[11]
      boss5 = playerachieve[12]
      boss6 = playerachieve[13]

      #---Load Inventory---#
      playerarmor = info['armor']
      armor1 = playerarmor[0]
      armor = playerarmor[1]
      im = playerarmor[2] #Israeli Merch (1)
      ja = playerarmor[3] #Joaquin Body Armor (2)
      bb = playerarmor[4] #Big Belly Armor (3)
      rm = playerarmor[5] #Robber's Mask (4)
      ca = playerarmor[6] #Chengus Armor (7)
      

      playerweapon = info['weapon']
      weapon1 = playerweapon[0]
      strength = playerweapon[1]
      ba = playerweapon[2] #Basic (0)
      qs = playerweapon[3] #Quesadilla Sword (1)
      pb = playerweapon[4] #Papa Baton (2)
      ww = playerweapon[5] #Wendy's Whip (3)
      jc = playerweapon[6] #John Cena's Biceps (5)
      cs = playerweapon[7] #Chengus Slayer (7)

      
      correct = 1
      break
    else:
      print("WRONG PASSWORD")

#-------Register-------#
elif answer == "2":
  username = input("Type your username (REMEMBER IT): ")
  password = input("Type your password (REMEMBER IT): ")

  achievestat = [achieve,ecuador,johncena,popeyes,eaten,psycho,horse,lod,deport,boss1,boss2,boss3,boss5,boss6]

  armorstat = [armor1,armor,im,ja,bb,rm,ca]
  weaponstat = [weapon1,strength,ba,qs,pb,ww,jc,cs]
  
  info = {'name':username,
          'password':password,
          'achieve':achievestat,
          'armor':armorstat
          'weapon':weaponstat}
  
  json.dump( info, open( info['name']+".json", 'w' ) )











#-------------INTRODUCTION-------------#

while 0==0:
  replit.clear()
  times = times + 1
  if times == 1:
    
    line1 = "\033[0;37;40m|-------"
    line2 = "\033[0;32;40m TALK TO JOAQUIN "
    line3 = "\033[0;37;40m-------|\n"
    
    for x in line1:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(.1)
      
    for x in line2:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    
    for x in line3:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.1)
  else:
    print("\033[0;37;40m|------- \033[0;32;40m TALK TO JOAQUIN \033[0;37;40m-------|\n")
    
    


  #-------------What do you want to do?-------------#
  
  print("\033[0;37;40mYou have unlocked\033[1;31;40m",achieve,
        "\033[0;37;40machievements out of\033[1;32;40m",achievements)
  
  print("\033[0;37;40m\nWhat do you want to do with Joaquin?")

  print("\nIMPORTANT:")

  print("\033[0;35;40m(s) - \033[0;35;40mType 's' to save your stats")    
  
  print("\033[0;34;40m(1) - \033[0;37;40mEquip your Items (Inventory)")    
  
  print("\033[0;34;40m(2) - \033[0;37;40mView Your Achievements")

  print("\nActions: ")
  
  print("\033[0;34;40m(3) - \033[0;37;40mGo to Israel with Him")
  
  print("\033[0;34;40m(4) - \033[0;37;40mEat With Him")
  
  print("\033[0;34;40m(5) - \033[0;37;40mEat Him")
  
  print("\033[0;34;40m(6) - \033[0;37;40mHave a Conversation")

  if johncena != 0:
    print("\033[0;31;40m\nUltimate Bosses: \n\033[0;34;40m(7) - \033[0;37;40mGerardo")

    if boss5 != 0:
      print("\033[0;34;40m(8) - \033[0;37;40m???")
      if achieve == 11:
        print("\033[0;34;40m(8) - \033[0;37;40mDat Boi Chengus")
  
  answer1 = input("\033[0;37;40m\n\nWhich one do you want to do?\033[0;34;40m ")






  
  #-------------SAVE YOUR DATA-------------#

  if answer1 == "s":

    print("Beginning data save...")

    achievestat = [achieve,ecuador,johncena,popeyes,eaten,psycho,horse,lod,deport,boss1,boss2,boss3,boss5,boss6]
  
    armorstat = [armor1,armor,im,ja,bb,rm,ca]
    weaponstat = [weapon1,strength,ba,qs,pb,ww,jc,cs]
    
    info = {'name':username,
            'password':password,
            'achieve':achievestat,
            'armor':armorstat
            'weapon':weaponstat}

    
  
    json.dump( info, open( info['name']+".json", 'w' ) )

    print("Save complete!")

    input("\033[0;37;40m\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")
    



  
  
  #-------------HAVE A CONVERSATION-------------#
  if answer1 == "6":


    #-------Introduction-------#
    replit.clear()
    print("Say the word 'leave' if you want to exit\n")
    intro()
      
    #-------Main Conversation-------#
    while 0==0:
      times1 = times1 + 1

      action = 0
      answer = input("\033[0;34;40m\nSpeak: ")
      answer = answer.lower() #Makes answer lowercase to clarify the logic
      
      psycho = psycho + 1
      if psycho == 1:
        achieve = achieve + 1
        time.sleep(.5)
        print("\n\033[0;33;40mACHIEVEMENT UNLOCK: Pspeaking to a Psycho\n")
        time.sleep(1)

      #-------Actual Behavior-------#

        
      #-----Curly-----#
      if "curl" in answer or "curly" in answer or "hair" in answer or "straight" in answer:
        times2 = 1
        last = "curly"
        action = 1
        curly()
         
      #-----Hello-----#
      elif "hello" in answer:
        hello()

      #-----Taco-----#
      elif "taco" in answer or "tacos" in answer:
        times2 = 1
        last = "taco"
        action = 1
        taco()

      #-----Ecuador-----#
      elif "ecuador" in answer or "ecuadorian" in answer:
        ecuador1()
        ecuador = ecuador + 1
        if ecuador == 1:
          achieve = achieve + 1
          time.sleep(.5)
          print("\033[0;33;40m\nBONUS ACHIEVEMENT UNLOCK: Ecuador on Top")
          time.sleep(1)

      #-----How are you-----#
      elif "wsp" in answer or "life" in answer or "how" in answer:
        times2 = 1
        last = "wsp"
        action = 1
        wsp()
        

      #-----Israel-----#
      elif "jew" in answer or "israel" in answer or "jewish" in answer or "jews" in answer or "israeli" in answer:
        times2 = 1
        last = "israel"
        action = 1
        israel()
            

      #-----Ok-----#
      elif "ok" in answer or "okay" in answer or "okee" in answer or "oke" in answer:
        times2 = 1
        last = "ok"
        action = 1
        ok()
         

      #-----Drug-----#
      elif "drug" in answer or "drugs" in answer or "druggy" in answer or "junky" in answer:
        times2 = 1
        last = "drug"
        action = 1
        drug()
          

      #-----Mom-----#
      elif "mom" in answer or "mommy" in answer or "mum" in answer or "mother" in answer or "mother" in answer:
        times2 = 1
        last = "mom"
        action = 1
        mom()

        
      #-----Yes-----#
      elif "ye" in answer or "yes" in answer or "yas" in answer:
        times2 = 1
        last = "yes"
        action = 1
        yes()
        
      #-----Shut-----#
      elif "shutup" in answer or "shut" in answer or "up" in answer or "mouth" in answer:
        times2 = 1
        last = "yes"
        action = 1
        shut()
        
      #-----Phone-----#
      elif "phone" in answer or "smartphone" in answer or "iphone" in answer or "cellphone" in answer or "android" in answer or "samsung" in answer:
        times2 = 1
        last = "phone"
        action = 1
        phone()

      #-----Men-----#
      elif "male" in answer or "men" in answer or "man" in answer or "boy" in answer or "boys" in answer or "boi" in answer or "bois" in answer:
        times2 = 1
        last = "men"
        action = 1
        men()

      

      #-----Leave-----#
      elif "leave" in answer:
        print("\033[0;32;40mJoaquin: Goodbye!")
        time.sleep(1)
        break
        
        
      else:
        if times1 == 1:
          ran()
        elif times2 == 2:
          ran()
        elif last == "curly":
          times2 = 2
          curly()
        elif last == "taco":
          times2 = 2
          taco()
        elif last == "wsp":
          times2 = 2
          wsp()
        elif last == "israel":
          times2 = 2
          israel()
        elif last == "ok":
          times2 = 2
          ok()
        elif last == "drug":
          times2 = 2
          drug()
        elif last == "mom":
          times2 = 2
          mom()
        elif last == "yes":
          times2 = 2
          yes()
        elif last == "shut":
          times2 = 2
          shut()
        elif last == "phone":
          times2 = 2
          phone()
        elif last == "men":
          times2 = 2
          men()
        else:
          ran()
          
  
  
  #-------------EAT WITH HIM-------------#
  if answer1 == "4":
    while 0 == 0:
      replit.clear()
      answer = input("\033[0;37;40mWhere do you want to eat? \n\n\033[0;34;40m(1) - \033[0;37;40mTacobell \n\033[0;34;40m(2) - \033[0;37;40mPopeyes \n\033[0;34;40m(3) - \033[0;37;40mWendys \n\nWhat do you want to do?\033[0;34;40m ")
      if answer == "1":
        say = 1
        break
      if answer == "2":
        say = 2
        break
      if answer == "3":
        say = 3
        break
    replit.clear()

    #-------TACO BELL-------#
    if say == 1:
      horse1 = taco(horse,achieve,bb,qs)
      horse = horse1[0];
      achieve = horse1[1];
      bb = horse1[2];
      qs = horse1[3];
      time.sleep(2)

    #-------POPEYES-------#
    if say == 2:
      pop1 = popeye(strength,armor,johncena,popeyes,achieve,health,jc)
      popeyes = pop1[0]
      johncena = pop1[1]
      achieve = pop1[2]
      jc = pop1[3]
      time.sleep(2)
    
          
    #-------Wendys-------#
    if say == 3:
      wen1 = wendys(strength,armor,boss3,achieve,health,ww)
      boss3 = wen1[0]
      achieve = wen1[1]
      ww = wen1[2]


  


      
  #-------------EAT HIM-------------#
  if answer1 == "5":
    replit.clear()
    while 0==0:
      answer = input("\033[0;37;40mAre you sure you want to eat Joaquin?\033[0;34;40m ")
      answer = answer.lower()

      if answer == "no" or answer == "not":
        print("\033[0;37;40mYou didn't eat Joaquin...")
        time.sleep(1)
        print("\033[0;37;40mSo Joaquin ate you LLLLL") 
        eaten = eaten + 1
        if eaten == 1:
          achieve = achieve + 1
          print("\033[0;33;40mACHIEVEMENT UNLOCK: Get Eaten By Joaquin")
        break
        time.sleep(2)
              
      else:
        print("\033[0;37;40mYou ate Joaquin. He was Yummy!")
        time.sleep(1)
        print("\033[0;33;40m\nGood thing Joaquin didn't eat you...")
        break

    input("\033[0;37;40m\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")
    



  
  
  #-------------Go to Israel-------------#
  if answer1 == "3":
    replit.clear()
    print("\033[0;37;40mWhich city in Israel do you want to go to? \n\n\033[0;34;40m(1) - \033[0;37;40mJerusalem \n\033[0;34;40m(2) - \033[0;37;40mTel Aviv \n\033[0;34;40m(3) - \033[0;37;40mLod")
    while 0 == 0:
      answer = input("\nWhere do you want to go?\033[0;34;40m ")
      
      if answer == "1" or answer == "2" or answer == "3":
        replit.clear()
        break   
    
    if answer == "1":
      jeru1 = jerusalem(strength,armor,boss1,achieve,health,im,pb,deport)
      boss1 = jeru1[0];
      achieve = jeru1[1];
      im = jeru1[2];
      pb = jeru1[3];
      deport = jeru1[4]
      
    if answer == "2":
      tel1 = telaviv(strength,armor,boss2,achieve,health,rm)
      boss2 = tel1[0]
      achieve = tel1[1]
      rm = tel1[2]

    if answer == "3":
      lod1 = lodv(lod,achieve)
      lod = lod1[0]
      achieve = lod1[1]



  
  
  #-------------Inventory-------------#
  if answer1 == "1":
    replit.clear()
    print("\033[0;37;40mSlots:")
    print("\033[0;33;40mPrimary armor:\033[0;35;40m",armor1,"|",armor,"Armor |")
    print("\033[0;33;40mPrimary weapon:\033[0;35;40m",weapon1,"|",strength,"Strength |")
    
   
#-------Equipping Armor-------#
    
    print("\033[0;37;40m\n\nWhich armor do you want to equip (type ID)?")
    #---Basic---#
    print("\n\033[0;34;40m(ID: ba) - \033[0;37;40mBasic |+0 armor|")

    #---Israeli Merch---#
    if im != 0:
      print("\033[0;34;40m(ID: im) - \033[0;37;40mIsraeli Merch |+1 armor|")

    #---Joaquin Body Armor---#
    if ja != 0:
      print("\033[0;34;40m(ID: ja) - \033[0;37;40mJoaquin Body Armor |+2 armor|")

    #---Big Belly Armor---#
    if bb != 0:
      print("\033[0;34;40m(ID: bb) - \033[0;37;40mBig Belly Armor |+3 armor|")

    #---Robber's Mask---#
    if rm != 0:
      print("\033[0;34;40m(ID: rm) - \033[0;37;40mRobber's Mask |+4 armor|")

    #---CHENGUS ARMOR---#
    if ca != 0:
      print("\033[0;34;40m(ID: ca) - \033[0;37;40mCHENGUS ARMOR |+7 armor|")

    #---Do Nothing---#
    print("\033[0;34;40m(Press [ENTER]) - \033[0;37;40mChange Nothing")

    answer = input("\nType the ID of the armor you want:\033[0;34;40m ")

    if answer == "ba":
      armor1 = "Basic Armor"
      armor = 0
      print("\033[0;37;40m\nBasic Armor Equipped! |\033[0;32;40m+0 Armor\033[0;37;40m|")
    
    if answer == "im":
      armor1 = "Israeli Merch"
      armor = 1
      print("\033[0;37;40m\nIsraeli Merch Equipped! |\033[0;32;40m+1 Armor\033[0;37;40m|")
    
    if answer == "ja":
      armor1 = "Joaquin Body Armor"
      armor = 2
      print("\033[0;37;40m\nJoaquin Body Armor Equipped! |\033[0;32;40m+2 Armor\033[0;37;40m|")

    if answer == "bb":
      armor1 = "Big Belly Armor"
      armor = 3
      print("\033[0;37;40m\nBig Belly Armor Equipped! |\033[0;32;40m+3 Armor\033[0;37;40m|")

    if answer == "rm":
      armor1 = "Robber's Mask"
      armor = 4
      print("\033[0;37;40m\nRobber's Mask Equipped! |\033[0;32;40m+4 Armor\033[0;37;40m|")

    if answer == "ca":
      armor1 = "CHENGUS ARMOR"
      armor = 7
      print("\033[0;37;40m\nCHENGUS ARMOR Equipped! |\033[0;32;40m+7 Armor\033[0;37;40m|")
      
      
    input("\033[0;37;40m\n\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")
      

#-------Equipping Weapon-------#
    replit.clear()
    print("\033[0;37;40mSlots:")
    print("\033[0;33;40mPrimary armor:\033[0;35;40m",armor1,"|",armor,"Armor |")
    print("\033[0;33;40mPrimary weapon:\033[0;35;40m",weapon1,"|",strength,"Strength |")
    
    print("\033[0;37;40m\n\nWhich weapon do you want to equip (type ID)?")
    #---Basic---#
    print("\033[0;34;40m\n(ID: ba) - \033[0;37;40mBasic |+0 Strength|")

    #---Quesadilla Sword---#
    if qs != 0:
      print("\033[0;34;40m(ID: qs) - \033[0;37;40mQuesadilla Sword |+1 Strength|")

    #---Papa Baton---#
    if pb != 0:
      print("\033[0;34;40m(ID: pb) - \033[0;37;40mPapa Baton |+2 Strength|")

    #---Wendy's Whip---#
    if ww != 0:
      print("\033[0;34;40m(ID: ww) - \033[0;37;40mWendy's Whip |+3 Strength|")

    #---John Cena's Biceps---#
    if jc != 0:
      print("\033[0;34;40m(ID: jc) - \033[0;37;40mJohn Cena's Biceps |+5 Strength|")

    #---CHENGUS SLAYER ---#
    if cs != 0:
      print("\033[0;34;40m(ID: jc) - \033[0;37;40m |+5 Strength|")
      
    #---Do Nothing---#
    print("\033[0;34;40m(Press [ENTER]) - \033[0;37;40mChange Nothing")

    
    answer = input("\nType the ID of the weapon you want:\033[0;34;40m ")

    if answer == "ba":
      weapon1 = "Basic Weapon"
      armor = 0
      print("\033[0;37;40m\nBasic Armor Equipped! |\033[0;32;40m+0 Strength\033[0;37;40m|")
    
    if answer == "qs":
      weapon1 = "Quesadilla Sword"
      strength = 1
      print("\033[0;37;40m\nQuesadilla Sword Equipped! |\033[0;32;40m+1 Strength\033[0;37;40m|")
    
    if answer == "pb":
      weapon1 = "Papa Baton"
      strength = 2
      print("\033[0;37;40m\nPapa Baton's Equipped! |\033[0;32;40m+2 Strength\033[0;37;40m|")
    
    if answer == "ww":
      weapon1 = "Wendy's Whip"
      strength = 3
      print("\033[0;37;40m\nWendy's Whip Equipped! |\033[0;32;40m+3 Strength\033[0;37;40m|")

    if answer == "jc":
      weapon1 = "John Cena's Biceps"
      strength = 5
      print("\033[0;37;40m\nJohn Cena's Biceps Equipped! |\033[0;32;40m+5 Strength\033[0;37;40m|")

    if answer == "cs":
      weapon1 = "CHENGUS SLAYER"
      strength = 7
      print("\033[0;37;40m\nCHENGUS SLAYER Equipped! |\033[0;32;40m+7 Strength\033[0;37;40m|")
    
    
    input("\033[0;37;40m\n\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")


  
  
  #-------------Achievements-------------#
  if answer1 == "2":

    replit.clear()
    print("\033[0;37;40mYou have unlocked\033[1;31;40m",achieve,
        "\033[0;37;40machievements out of\033[1;32;40m",achievements)

    if popeyes > 0:
      print("\033[0;32;40m\nA Peaceful Visit to Popeyes: UNLOCKED")
    else:
      print("\033[0;31;40m\nA Peaceful Visit to Popeyes: LOCKED")

    if eaten > 0:
      print("\033[0;32;40m\nGet Eaten by Joaquin: UNLOCKED")
    else:
      print("\033[0;31;40m\nGet Eaten by Joaquin: LOCKED")

    if psycho > 0:
      print("\033[0;32;40m\nPspeaking with a Psycho: UNLOCKED")
    else:
      print("\033[0;31;40m\nPspeaking with a Psycho: LOCKED")

    if horse > 0:
      print("\033[0;32;40m\nSurving Tacobell: UNLOCKED")
    else:
      print("\033[0;31;40m\nSurviving Tacobell: LOCKED")

    if lod > 0:
      print("\033[0;32;40m\nVisit the Most Boring City on Earth: UNLOCKED")
    else:
      print("\033[0;31;40m\nVisit the Most Boring City on Earth: LOCKED")

    if deport > 0:
      print("\033[0;32;40m\nGet Deported: UNLOCKED")
    else:
      print("\033[0;31;40m\nGet Deported: LOCKED")

    if ecuador > 0:
      print("\033[0;32;40m\n(BONUS)Ecuador on Top: UNLOCKED")
    else:
      if achieve > 11:
        print("\033[0;31;40m\n???: LOCKED")

    
    input("\033[0;37;40m\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")

    replit.clear()
    print("\033[0;37;40mYou have unlocked\033[1;31;40m",achieve,
        "\033[0;37;40machievements out of\033[1;32;40m",achievements)

    if boss1 > 0:
      print("\033[0;32;40m\nBeat Boss #1: UNLOCKED")
    else:
      print("\033[0;31;40m\nBeat Boss #1: LOCKED")

    if boss2 > 0:
      print("\033[0;32;40m\nBeat Boss #2: UNLOCKED")
    else:
      print("\033[0;31;40m\nBeat Boss #2: LOCKED")

    if boss3 > 0:
      print("\033[0;32;40m\nBeat Boss #3: UNLOCKED")
    else:
      print("\033[0;31;40m\nBeat Boss #3: LOCKED")
    
    if johncena > 0:
      print("\033[0;32;40m\nBeat Boss #4: UNLOCKED")
    else:
      print("\033[0;31;40m\nBeat Boss #4: LOCKED")

    if boss5 > 0:
      print("\033[0;32;40m\nBeat Boss #5: UNLOCKED")
    else:
      print("\033[0;31;40m\nBeat Boss #5: LOCKED")

    if boss6 > 0:
      print("\033[0;32;40m\nBeat Dat Boi Chengus: UNLOCKED")
    else:
      if boss6 != 0:
        print("\033[0;31;40m\n???: LOCKED")

    input("\033[0;37;40m\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")


  
  
  #-------------GERARDO-------------#
  if answer1 == "7" and johncena != 0:

    if boss5 == 0:
      replit.clear()
      print("\033[0;37;40mYou tell Joaquin that Gerardo is smarter than him")
      time.sleep(2)
      print("\033[0;37;40m\nJoaquin challenges Gerardo to a duel...")
  
      input("\033[0;37;40m\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")
      fernando1 = gerardo(strength,armor,boss5,achieve,health,cs,ca)
  
      boss5 = fernando1[0]
      achieve = fernando1[1]
      cs = fernando1[2]
      ca = fernando1[3]
    else:
      print("That CHENGUS gear looks kinda weird...")
      
      time.sleep(1.5)
      
      print("What would happen if you got\n all of the achievements?")

      time.sleep(1.5)

      input("\033[0;37;40m\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")


  
  
  #-------------CHENGUS-------------#
  if answer1 == "8" and boss6 != 0:
    if achieve < 12:
      print("That CHENGUS gear looks kinda weird...")
      
      time.sleep(1.5)
      
      print("You wonder what happens if you get\n all of the achievements?")

      time.sleep(1.5)

      input("\033[0;37;40m\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")

    else:
      print("\033[0;31;40mA wild CHENGUS appeared")

      time.sleep(1.5)

      input("\033[0;37;40m\n\nPress \033[0;34;40m[ENTER]\033[0;37;40m to continue")
      cheng1 = cheng(strength,armor,boss6,achieve,health)
  
      boss6 = cheng1[0]
      achieve = cheng1[1]
