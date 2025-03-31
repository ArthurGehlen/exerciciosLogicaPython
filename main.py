import pwinput
from getpass import getpass

class Exercicios:
    def __init__(self):
        self.result_string = ""
        self.result_number = 0
        self.secondary_result_number = 0
    
    # Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas.
    def ex_1(self, nota_1: int, nota_2: int, nota_3):
        result = (nota_1 + nota_2 + nota_3) / 3
        self.result_number = round(result, 2) # Arredondando
        return self.result_number
    
    # Faça um programa para converter um certo valor em dólar para reais (ver cotação do dia).
    def ex_2(self, quant_dolar): # Cotação atual: R$ 5,76
        result = quant_dolar * 5.76
        self.result_number = round(result, 2)
        return self.result_number

    # Faça um programa para converter um certo valor em reais para dólares (ver cotação do dia).
    def ex_3(self, quant_reais):
        self.result_number = quant_reais * 0.17
        self.result_number = round(self.result_number, 2)
        return self.result_number

    # Faça um programa que leia um saldo e imprimir o saldo com reajuste de 1%.
    def ex_4(self, value):
        self.result_number = value + (value * 0.01)
        return self.result_number

    # Faça um programa que leia o valor de um produto e imprimir o valor corrigido com o reajuste de 33.33%.
    def ex_5(self, value):
        self.result_number = value + (value * 0.33)
        return self.result_number
    
    # Faça programa que leia uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius e Kelvin.
    def ex_6(self, fahrenheit):
        self.result_number = 5 / 9 + (fahrenheit - 32) # Para CELCIUS
        self.result_number = round(self.result_number, 2)

        self.secondary_result_number = ((fahrenheit - 32) / 1.8) + 273.15 # Para KELVIN
        self.secondary_result_number = round(self.secondary_result_number, 2)

        return self.result_number, self.secondary_result_number

    # Faça programa que leia uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit e Kelvin.
    def ex_7(self, celcius):
        self.result_number = celcius * 1.8 + 32 # Para FAHRENHEIT
        self.result_number = round(self.result_number, 2)

        self.secondary_result_number = celcius + 273.15 # Para KELVIN
        self.secondary_result_number = round(self.secondary_result_number, 2)

        return self.result_number, self.secondary_result_number

    # Faça programa que leia uma temperatura em graus Kelvin, calcular e escrever o valor correspondente em graus Fahrenheit e Celsius.
    def ex_8(self, kelvin):
        self.result_number = kelvin - 273.15 # Para CELCIUS
        self.result_number = round(self.result_number, 2)

        self.secondary_result_number = (kelvin - 273.15) * 1.8 + 32 # Para FAHRENHEIT
        self.secondary_result_number = round(self.secondary_result_number, 2)

        return self.result_number, self.secondary_result_number

    # Faça um programa que leia o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
    def ex_9(self, salario, perc_aumento):
        perc_aumento /= 100
        self.result_number = salario + (salario * perc_aumento)
        return salario * perc_aumento, self.result_number

    # Faça um programa que leia um número, verifique se este número é positivo ou negativo. Se for negativo mostre a mensagem "Você digitou um numero negativo", Senão mostre:" Você digitou um número positivo.
    def ex_10(self, value):
        return 'Você digitou um numero negativo' if value < 0 else 'Você digitou um número positivo'

    # Faça um programa que leia um número, verifique se este número é positivo, negative ou Zero. Se for negativo mostre a mensagem "Você digitou um numero negativo",
    #  Se for positivo mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou zero”.
    def ex_11(self, value):
        if value == 0:
            return 'Você digitou zero'
        elif value > 1:
            return 'Você digitou um número positivo'
        else: 
            return 'Você digitou um numero negativo'

    # Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas, se a media aritmética for:
    # ♦ Media maior ou igual a 7 – ALUNO APROVADO
    # ♦ Media maior ou igual a 5 e menor que 7 – ALUNO EM RECUPERAÇÃO
    # ♦ Media menor que 5 – ALUNO REPROVADO
    def ex_12(self, nota_1: int, nota_2: int, nota_3):
        result = (nota_1 + nota_2 + nota_3) / 3
        self.result_number = round(result, 2) # Arredondando

        if self.result_number >= 7:
            self.result_string = 'APROVADO'
        elif self.result_number >= 5 and self.result_number < 7:
            self.result_string = 'ALUNO EM RECUPERAÇÃO'
        else:
            self.result_string = 'ALUNO REPROVADO'

        return self.result_number, self.result_string

    # Faça um programa que leia um número e verifique se este número é par ou ímpar.
    def ex_13(self, value):
        return value % 2 == 0

    # Faça um programa que leia 3 números e “diga” qual é o maior deles.
    def ex_14(self, num_1, num_2, num_3):
        arr = [] # Array criada para armazenar, ordenar por ordem crescente e retornar o último (maior) número
        arr.append(num_1) ; arr.append(num_2) ; arr.append(num_3) 
        arr.sort()
        self.result_number = arr[2]
        if num_1 == num_2 == num_3:
            return 'Números iguais'
   
        return self.result_number   

    # Faça um programa que leia a idade de um nadador e classifique-o numa das seguintes categorias abaixo:
    # • Idoso (idade >= 65);
    # • Adulto (idade >= 21);
    # • Juvenil (idade >= 14);
    # • Infantil (idade >=9);
    # • Mirim (Idade < 9).
    def ex_15(self, age: int):
        if age >= 65:
            return 'Idoso'
        elif age >= 21 and age < 65:
            return 'Adulto'
        elif age >= 14 and age < 21:
            return 'Infantil'
        
        return 'Mirim'

    # Faça um programa que leia dois números e efetua a adição. Se o valor somado for maior que 20,
    # este deverá ser apresentado somando-se a ele 8; se o valor somado for menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
    def ex_16(self, num_1, num_2):
        self.result_number = num_1 + num_2

        if self.result_number > 20:
            return self.result_number + 8
        
        return self.result_number - 5

    # Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o valor da compra for menor que 20,00;
    # caso contrário, o lucro será de 30%. Ler o valor do produto e imprimir o valor da venda, conforme as taxas do enunciado.
    def ex_17(self, value):
        if value < 20:
            return value + value * 0.45 
        
        return value + value * 0.3

    # Bônus
    # Faça um programa que converta a temperatura. Deve ser selecionada a temperatura que será inserida assim como a que será exibida.
    # As temperaturas utilizadas devem ser Celsius, Fahrenheit e Kelvin.
    def ex_18(self, input_temperature_name: str, output_temperature_name: str, input_temperature):
        if input_temperature_name == 'Celsius':
            if output_temperature_name == 'Fahrenheit':
                self.result_number = input_temperature * 1.8 + 32 
                self.result_number = round(self.result_number, 2)

                return self.result_number
            
            if output_temperature_name == 'Kelvin':
                self.result_number = input_temperature + 273.15 
                self.result_number = round(self.result_number, 2)

                return self.result_number
        
        if input_temperature_name == 'Fahrenheit':
            if output_temperature_name == 'Celsius':
                self.result_number = 5 / 9 * (input_temperature - 32)
                self.result_number = round(self.result_number, 2)

                return self.result_number
            
            if output_temperature_name == 'Kelvin':
                self.result_number = ((input_temperature - 32) / 1.8) + 273.15 
                self.result_number = round(self.result_number, 2)

                return self.result_number

        if input_temperature_name == 'Kelvin':
            if output_temperature_name == 'Celsius':
                self.result_number = input_temperature - 273.15 
                self.result_number = round(self.result_number, 2)

                return self.result_number

            if output_temperature_name == 'Fahrenheit':
                self.result_number = (input_temperature - 273.15) * 1.8 + 32
                self.result_number = round(self.result_number, 2)

                return self.result_number

    # Função para verificar ganhador no pedra, papel e tesoura
    def check_winner(self, user_1_answer: str, user_2_answer: str):
        user_1_answer.upper()
        user_2_answer.upper()

        if user_1_answer == user_2_answer:
            self.result_string = "Empate"
            return self.result_string
        elif (user_1_answer == "PEDRA" and user_2_answer == "TESOURA") or (user_1_answer == "TESOURA" and user_2_answer == "PAPEL") or (user_1_answer == "PAPEL" and user_2_answer == "PEDRA"):
            self.result_string = "Player 1 Ganhou!!!"
            return self.result_string
        else:
            self.result_string = "Player 2 Ganhou!!!"
            return self.result_string

    # Faça o jogo de Jokenpô
    def ex_19(self):
        # self.user_input_1 = pwinput.pwinput(prompt='1° Jogador -> ')
        self.user_input_1 = getpass("1° Jogador ->")
        if len(self.user_input_1) > 5:
            self.user_input_1 = pwinput.pwinput(prompt='1° Jogador -> ')

        while self.user_input_1 != "Pedra" and self.user_input_1 != "Papel" and self.user_input_1 != "Tesoura":
            print("Digite uma resposta vailda")
            self.user_input_1 = pwinput.pwinput(prompt='1° Jogador -> ')

        self.user_input_2 = pwinput.pwinput(prompt='2° Jogador ->')

        while self.user_input_2 != "Pedra" and self.user_input_2 != "Papel" and self.user_input_2 != "Tesoura":
            print("Digite uma resposta vailda")
            self.user_input_2 = pwinput.pwinput(prompt='2° Jogador ->')

        self.check_winner(self.user_input_1, self.user_input_2)
        return self.result_string
        
exercicio = Exercicios()
print(exercicio.ex_19())