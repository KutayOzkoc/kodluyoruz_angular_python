"""
İkinci Problem seti A sorusu

İki oyunculu bir Taş-Kağıt-Makas oyunu yapalım.

İpucu:

Oyuncudan oyunlarını isteyip (input() kullanarak), karşılaştıralım, kazananı tebrik eden bir mesaj 
yazdıralım ve oyuncuların yeni bir oyuna başlamak isteyip istemediğini soralım)

"""
while True:
    player_1 = input("Player 1 Oyununuzu uygulayın :(Kücük harf ile giriniz)")
    player_2 = input("Player 2 Oyununuzu uygulayın :(Kücük harf giriniz)")

    if(player_1 == "tas" and player_2 == "kagit"):
        print("Player 2 Kazandı !!")
    elif (player_1 == "tas" and player_2 == "makas"):
        print("Player 1 Kazandı !!")
    elif (player_1 == "tas" and player_2 == "tas"):
        print("!! Berabere !!")


    elif (player_1 == "makas" and player_2 == "kagit"):
        print("Player 2 Kazandı !!")
    elif (player_1 == "makas" and player_2 == "makas"):
        print("!! Berabere !!")
    elif(player_1 == "makas" and player_2 == "tas"):
        print("Player 1 Kazandı")

    elif (player_1 == "kagit" and player_2 == "kagit"):
        print("!! Berabere !!")
    elif (player_1 == "kagit" and player_2 == "makas"):
        print("!! Player2 Kazandı !!")
    elif(player_1 == "kagit" and player_2 == "tas"):
        print("Player 1 Kazandı")
    
    else:
        print("Hatalı Bir kareket yapildi lütfen açıklamayı okuyup ona göre input giriniz.")

    devam = input("Devam etmek istemiyorsanız (h/H) giriniz? Devam Etmek için Enter'a basınız ")
    if(devam == "H" or devam == "h"):
        break

print("Oyun Bitti")