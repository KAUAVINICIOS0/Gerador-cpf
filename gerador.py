# Importa random que pelo nome já diz é aleatoria
import random

# Solicita a quantidade de cpf que deseja gerar
pedido = input('Quantos cpf vc quer gerar? ')

# Verificando o que foi digitado
try:
    pedido_int = int(pedido)
    # For que basicamente gera os primeiros 9 digitos 
    for _ in range(pedido_int):
        # Gerando 9 digitos do cpf
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        # Declaração de variáveis
        contador = 1
        segundo_contador = 0
        multiplicador_regressivo = 10
        soma_digitos = 0
        soma_2_digitos = 0
        multiplicador_regressivo_2 = 11

        # Concatenando cada número e multiplicando com a contagem regressiva
        for numero_atual in nove_digitos:
            numero_atual = int(numero_atual)
            soma_digitos = soma_digitos + (numero_atual * multiplicador_regressivo)
            multiplicador_regressivo -= 1
        
        # Calculo para "criar"
        resto_da_divisao = (soma_digitos * 10) % 11

        # verificando se o primeiro digito do cpf é 9
        # se o resultado for maior que 9, ele vira 0
        primeiro_digito = 0 if resto_da_divisao > 9 else resto_da_divisao

        # Inicio da validação do segundo digito
        cpf_com_primeiro_digito = nove_digitos + str(primeiro_digito)
        
        
        # Concatenando cada número e multiplicando com a contagem regressiva
        for numero_at in cpf_com_primeiro_digito:
            numero_at = int(numero_at)
            soma_2_digitos = soma_2_digitos + (numero_at * multiplicador_regressivo_2)
            multiplicador_regressivo_2 -= 1
        
        # Calculo para "criar" o segundo digito
        resto_da_divisao_seg_dig = (soma_2_digitos * 10) % 11

        # verificando se o primeiro digito do cpf é 9
        # se o resultado for maior que 9, ele vira 0 
        segundo_digito = 0 if resto_da_divisao_seg_dig > 9 else resto_da_divisao_seg_dig

        # Aqui basicamente ta o cpf gerado
        cpf_gerado_pelo_calculo = f'{nove_digitos}-{primeiro_digito}{segundo_digito}'

        # Resultado final
        print('-----------------------------')
        print(f"cpf: {cpf_gerado_pelo_calculo}")
        print('-----------------------------')
        
except:
    print('-----------------------------')
    print('Valor digitado não é inteiro')
    print('Por Favor tente novamente')
    print('-----------------------------')