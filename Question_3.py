# Questão 3 - Faturamento
# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
# que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def faturamento():
    with open("faturamento.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima = sum(1 for v in valores if v > media)

    print(f"Menor valor: {menor:.2f}")
    print(f"Maior valor: {maior:.2f}")
    print(f"Dias acima da média: {dias_acima}")


if __name__ == "__main__":
    faturamento()
