import random
import os

pontos_defesa_max_1 = 50
pontos_defesa_atual_1 = pontos_defesa_max_1

pontos_defesa_max_2 = 50
pontos_defesa_atual_2 = pontos_defesa_max_2

pontos_vida_max_1 = 100
pontos_vida_atual_1 = pontos_vida_max_1

pontos_vida_max_2 = 100
pontos_vida_atual_2 = pontos_vida_max_2

pontos_ataque_1 = 20
pontos_ataque_2 = 20

defesa_1 = False
defesa_2 = False

def atacar(vitima:str, dano_dado:int):

    global pontos_vida_atual_1
    global pontos_vida_atual_2
    global defesa_1
    global defesa_2

    jogador_defendendo_1 = defesa_1 and pontos_defesa_atual_1 > 0
    jogador_defendendo_2 = defesa_2 and pontos_defesa_atual_2 > 0

    if jogador_defendendo_1 or jogador_defendendo_2:
        defender(vitima, dano_dado)

    else:
        dar_dano(vitima, dano_dado)

def sortear_evento(chances_porcentagem)->bool:
    numero = random.randint(1,100)

    return numero <= chances_porcentagem

def defender(vitima, dano_dado):
    
    global pontos_vida_atual_1
    global pontos_vida_atual_2
    global pontos_defesa_atual_1
    global pontos_defesa_atual_2
    global defesa_1
    global defesa_2

    defesa_bem_sucedida = sortear_evento(25)
    
    if(defesa_bem_sucedida):
        dano_devolvido = int(dano_dado * 0.3)
        dano_recebido  = int(dano_dado * 0.4)

        if(vitima == "Jogador 1"):
            print("Jogador 1 defendeu [", (dano_dado - dano_recebido), "] pontos de ataque")

            dar_dano("Jogador 1", dano_recebido)
            dar_dano("Jogador 2", dano_devolvido)

        else:
            print("Jogador 2 defendeu [", (dano_dado - dano_recebido), "] pontos de ataque")

            dar_dano("Jogador 2", dano_recebido)
            dar_dano("Jogador 1", dano_devolvido)

    else:
        dar_dano(vitima, dano_dado)

def dar_dano(vitima, dano_recebido):
        
    global pontos_vida_atual_1
    global pontos_vida_atual_2
    global pontos_defesa_atual_1
    global pontos_defesa_atual_2
    global defesa_1
    global defesa_2

    if vitima == "Jogador 1":
        print("Jogador 1 levou [", dano_recebido, "] pontos de dano")    

        if defesa_1:
            defesa_1 = False
            pontos_defendidos = pontos_defesa_atual_1 - dano_recebido

            if pontos_defendidos > 0:
                pontos_defesa_atual_1 = pontos_defendidos

            else:
                pontos_vida_atual_1 += pontos_defendidos
                pontos_defesa_atual_1 = 0

        else:
           pontos_vida_atual_1 -= dano_recebido

    else:
        print("Jogador 2 levou [", dano_recebido, "] de dano")

        if defesa_2:
            defesa_2 = False
            pontos_defendidos = pontos_defesa_atual_2 - dano_recebido

            if pontos_defendidos > 0:
                pontos_defesa_atual_2 = pontos_defendidos

            else:
                pontos_vida_atual_2 += pontos_defendidos
                pontos_defesa_atual_2 = 0

        else:
            pontos_vida_atual_2 -= dano_recebido

def exibir_status_jogadores():

    global pontos_vida_atual_1
    global pontos_vida_atual_2
    global pontos_defesa_atual_1
    global pontos_defesa_atual_2
    global pontos_vida_max_1
    global pontos_vida_max_2
    global pontos_defesa_max_1
    global pontos_defesa_max_2
    global defesa_1
    global defesa_2

    print(  f"""
          
        ======== JOGADOR 1 ========
        HP: {pontos_vida_atual_1}/{pontos_vida_max_1}  
        PD: {pontos_defesa_atual_1}/{pontos_defesa_max_1}  
        Está defendendo: {defesa_1}

        ======== JOGADOR 2 ========
        HP: {pontos_vida_atual_2}/{pontos_vida_max_2}
        PD: {pontos_defesa_atual_2}/{pontos_defesa_max_2}
        Está defendendo: {defesa_2}

    """)
    
while pontos_vida_atual_1 > 0 and pontos_vida_atual_2 > 0:

    exibir_status_jogadores()

    opcao_jogador_1 = input("""
                        
        Jogador 1, escolha sua ação:
                    
        1. Atacar
        2. Defender
        3. Pular o Turno                    
                                
    """)

    os.system("cls")
    
    if opcao_jogador_1 == "1":
        defesa_1 = False
        atacar("Jogador 2", pontos_ataque_1)

    elif(opcao_jogador_1 == "2"):
        defesa_1 = True

    else:
        defesa_1 = False
        print("O Jogador 1 pulou o turno.")

    exibir_status_jogadores()

    opcao_jogador_2 = input("""

        Jogador 2, escolha sua ação:

        1. Atacar
        2. Defender
        3. Pular o Turno

    """)

    os.system("cls")
    
    if opcao_jogador_2 == "1":
        defesa_2 = False
        atacar("Jogador 1", pontos_ataque_2)

    elif(opcao_jogador_2 == "2"):
        defesa_2 = True

    else:
        defesa_2 = False
        print("O Jogador 2 pulou o turno.")

if pontos_vida_atual_1 > pontos_vida_atual_2:
    print("Parabéns Jogador 1, você venceu!")

else:
    print("Parabéns Jogador 2, você venceu!")

