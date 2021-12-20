from kps_tehdas import KPSTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        
        pelit = {
            'a': KPSTehdas.luo_kps_pelaaja_vs_pelaaja(),
            'b': KPSTehdas.luo_kps_tekoaly(),
            'c': KPSTehdas.luo_kps_parempi_tekoaly(10)
        }

        if vastaus in ['a', 'b', 'c']:
            tulosta_ohje()

            peli = pelit[vastaus]
            peli.pelaa()
            
        else:
            break


def tulosta_ohje():
    print("Peli loppuu kun pelaaja antaa virheellisen \
        siirron eli jonkun muun kuin k, p tai s")

if __name__ == "__main__":
    main()
