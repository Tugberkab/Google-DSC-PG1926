def mailCorrection(mailAdresi):
    kullaniciAdiList = ["a","b","c","d","e","f","g","h","i","j","k",
              "l","m","n","o","p","q","r","s","t","u","v",
              "w","x","y","z","A","B","C","D","E","F","G",
              "H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z","-","_",1,2,3,4,5,6,7,8,9,0]
    
    webSiteList = ["a","b","c","d","e","f","g","h","i","j","k",
              "l","m","n","o","p","q","r","s","t","u","v",
              "w","x","y","z","A","B","C","D","E","F","G",
              "H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,
              6,7,8,9]
    
    correction = False
    atLocation = mailAdresi.find("@")
    if atLocation == -1:
        print("\nMail adresiniz yanlıştır.")
    else:
        kullaniciAdi = mailAdresi[:atLocation]
        for i in range(0, len(kullaniciAdiList)):
            for k in range(0, len(kullaniciAdi)):
                holdList = kullaniciAdiList[i]
                holdKullaniciAdi = kullaniciAdi[k]
                if holdList != holdKullaniciAdi:
                    correction = True
                else:
                    correction
        
        dotLocation = mailAdresi.find(".")
        webSitesi = mailAdresi[atLocation:dotLocation]
        
        for i in range(0, len(webSiteList)):
            for k in range(0, len(webSitesi)):
                holdListWeb = webSiteList[i]
                holdWebSite = webSitesi[k]
                if holdListWeb != holdWebSite:
                    correction
                else:
                    correction = True
        
        if correction == False:
            print("\nMail adresiniz yanlıştır.")
        else:
            print("\nMail adresiniz doğrudur.")


uzanti = int(input("Uzantı uzunluğunu giriniz: "))
if uzanti > 3:
    print("Uzantı uzunluğu 3'ten büyük olamaz.")
else:
    mailAdresi = input("Mail adresinizi giriniz: ")
    mailCorrection(mailAdresi)



