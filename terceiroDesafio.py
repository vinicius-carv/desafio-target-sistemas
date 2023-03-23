'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

'''
import json
f = open('resources/dados.json')
data=json.load(f)
dias=[]
valor=[]
# Separando os dados do json para análise
for i in range(len(data)):
    dias.append(data[i]["dia"])
    valor.append(data[i]["valor"])
# Menor valor de faturamento no mês
print("O menor valor no faturamento do mês foi de: R$ "+str(min(valor))+" no dia nº "+str(dias[valor.index((min(valor)))]))
# Maior valor de faturamento no mês
print("O maior valor no faturamento do mês foi de: R$ "+str(round(max(valor),2))+" no dia nº "+str(dias[valor.index((max(valor)))]))
# Média de faturamento mensal
total=0
for j in range(len(valor)):
    if(valor[j]!=0):
        total+=valor[j]
print("Faturamento mensal: R$ "+str(round(total,2)))
f.close()