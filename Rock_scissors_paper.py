from random import*

valikud = ["kivi", "paber", "käärid"]

mängija = 0
bot_võitis = 0
Viigimäng = 0
mängija2 = 0


try:
    mänguvalik=input("Kas mängid sõbraga või bot-ga? sõber või bot: ")
    if mänguvalik.lower() == "bot":
        while True:
            print("[1] kivi\n[2] paber\n[3] käärid\n[4] Lõpeta\n")
            mängijavalik = int(input("Mida soovid valida: "))
    
            if mängijavalik == 4:
                break
    
            bot_valik = choice(valikud)
    
            if mängijavalik == 1:
                mängijavalik = "kivi"
            elif mängijavalik == 2:
                mängijavalik = "paber"
            elif mängijavalik == 3:
                mängijavalik = "käärid"
        
    
            print("Sinu valik {}".format(mängijavalik))
            print("Bot valik {}".format(bot_valik))
    
            if mängijavalik == bot_valik:
                print("Viigimäng")
                Viigimäng += 1
            elif mängijavalik.lower() == "kivi" and bot_valik == "käärid":
                print("Oled võitnud!")
                mängija += 1
            elif mängijavalik.lower() == "paber" and bot_valik == "kivi":
                print("Oled võitnud!")
                mängija += 1
            elif mängijavalik.lower() == "käärid" and bot_valik == "paper":
                print("Oled võitnud!")
                mängija += 1
            else:
                print("Bot võitis!")
                bot_võitis += 1   
        print("\n")
    elif mänguvalik.lower() == "sõber":
        while True:
            mängijavalik=int(input("1) Mängime või 2) Lõpetame: "))
            if mängijavalik == 2:
                break
            elif mängijavalik == 1:
                mängijavalik = choice(valikud)
                mängijavalik2 = choice(valikud)

            print("Sinu valik {}".format(mängijavalik))
            print("Sõbra valik {}".format(mängijavalik2))
    
            if mängijavalik == mängijavalik2:
                print("Viigimäng")
                Viigimäng += 1
            elif mängijavalik.lower() == "kivi" and mängijavalik2 == "käärid":
                print("Oled võitnud!")
                mängija += 1
            elif mängijavalik.lower() == "paber" and mängijavalik2 == "kivi":
                print("Oled võitnud!")
                mängija += 1
            elif mängijavalik.lower() == "käärid" and mängijavalik2 == "paper":
                print("Oled võitnud!")
                mängija += 1
            else:
                print("Sõber võitis!")
                mängija2 += 1
except:
    print("Vale andmetüüp")
try:
    if mänguvalik.lower() == "bot":
        print("Tulemused:")
        print("Mängija võitis: {}".format(mängija))
        print("Bot võitis: {}".format(bot_võitis))
        print("Viigimängu: {}".format(Viigimäng))
except:
    print("vale andmetüüp")
try:
    if mänguvalik.lower() == "sõber":
        print("Tulemused:")
        print("Mängija võitis: {}".format(mängija))
        print("Sõber võitis: {}".format(mängija2))
        print("Viigimängu: {}".format(Viigimäng))
except:
    print("vale andmetüüp")
