import random
def main():
    vida_av=100
    att_av=random.randint(10,20)
    deff_av=random.randint(1,5)

    vida_mons=random.randint(60,80)
    att_mons=random.randint(20,30)

    rodada=1

    while vida_av >0 and vida_mons > 0:
        print("Aventureiro: vida:",vida_av ,"Ataque:",att_av, "Defesa:",deff_av)
        print("Monstro: Vida:" , vida_mons, "Ataque", att_mons)
        print("rodada", rodada)
        vida_mons= vida_mons - random.randint(1,att_av)
        vida_av= vida_av-random.randint(1,att_mons)
        if vida_mons<=0:
            print("o Monstro Morreu!")
            break
        if vida_av<=0:
            print("Você Morreu!")
            break
      
        rodada+=1

main()

