import csv
import random

def gerar_resposta_simulada():
    """Gera uma resposta simulada para cada campo."""

    anos = [6, 7, 8, 9]
    ano = random.choice(anos)

    problema = "Thiago é um pequeno comerciante. Ele trabalha de segunda a sexta-feira vendendo água e doces. Na semana passada, ele arrecadou R$ 12,00 por dia de trabalho. Desse valor, ele usou R$ 15,00 para comprar água e doces para vender na semana seguinte e o que sobrou ele deu para seus três irmãos. Quanto cada irmão de Thiago recebeu?"

    # Simulação da interpretação (variando em nível de detalhe e clareza)
    interpretacoes = [
        "Thiago vende água e doces, ganha 12 reais por dia, gasta 15 e divide o resto.",
        "Thiago trabalha 5 dias, ganha 12 por dia, tira 15 e divide o que sobra por 3.",
        "Thiago tem um gasto de 15 reais e ganha 12 reais por dia, e tem 3 irmãos.",
        "Thiago ganha 12 reais por dia de segunda a sexta e gasta 15 reais para comprar água e doces e divide o que sobra entre seus 3 irmãos.",
        "Thiago trabalha 5 dias na semana e ganha 12 reais por dia, gasta 15 reais para comprar água e doces e divide o que sobra entre seus 3 irmãos.",
    ]
    interpretacao = random.choice(interpretacoes)

    # Simulação das estratégias (variando em precisão e detalhe)
    estrategias = [
        "Somar tudo, tirar 15 e dividir por 3.",
        "Ver quanto ele ganha, tirar o gasto e dividir.",
        "Multiplicar 12 por 5, subtrair 15 e dividir por 3.",
        "Calcular o total ganho na semana, subtrair o gasto com compras e dividir o valor restante por 3.",
        "Calcular o total ganho na semana, subtrair o gasto com compras e dividir o valor restante por 3.",
    ]
    estrategia = random.choice(estrategias)

    # Simulação dos cálculos/técnicas (incluindo erros comuns)
    calculos_tecnicas = [
        "12 x 5 = 60; 60 - 15 = 45; 45 / 3 = 15",
        "12 + 5 = 17; 17 - 15 = 2; 2 / 3 = 0,66",
        "12 - 15 = -3; -3 / 3 = -1",
        "12 x 5 = 60; 60 - 15 = 45; 45 / 3 = 15",
        "12 x 5 = 60; 60 - 15 = 45; 45 / 3 = 15",
    ]
    calculo_tecnica = random.choice(calculos_tecnicas)

    # Simulação das respostas (incluindo respostas incorretas e sem sentido)
    respostas = [
        "Cada irmão recebeu R$15,00.",
        "Cada irmão recebeu R$0,66.",
        "Cada irmão recebeu -R$1,00.",
        "Cada irmão recebeu R$15,00.",
        "Cada irmão recebeu R$15,00.",
    ]
    resposta = random.choice(respostas)

    return ano, problema, interpretacao, estrategia, calculo_tecnica, resposta

# Gerar 100 respostas simuladas
respostas_simuladas = []
for i in range(1, 101):
    ano, problema, interpretacao, estrategia, calculo_tecnica, resposta = gerar_resposta_simulada()
    respostas_simuladas.append([f"Estudante {i}", ano, problema, interpretacao, estrategia, calculo_tecnica, resposta])

# Salvar as respostas em um arquivo CSV
with open("respostas_estudantes.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(["Nome", "Ano", "Problema", "Interpretação", "Estratégia", "Cálculo/Técnica", "Resposta"])  # Cabeçalho
    escritor_csv.writerows(respostas_simuladas)

print("Arquivo CSV 'respostas_estudantes.csv' gerado com sucesso!")