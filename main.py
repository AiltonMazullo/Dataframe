import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Massa de Dados (Alunos)
dados = [
    {"Matricula": 1, "Nome": "Aluno 1", "Nota1": 8.5, "Nota2": 7.0, "Media": 7.75, "Quantidade de faltas": 3, "Situacao": "Aprovado"},
    {"Matricula": 2, "Nome": "Aluno 2", "Nota1": 7.5, "Nota2": 8.0, "Media": 7.75, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 3, "Nome": "Aluno 3", "Nota1": 6.0, "Nota2": 6.5, "Media": 6.25, "Quantidade de faltas": 1, "Situacao": "Final"},
    {"Matricula": 4, "Nome": "Aluno 4", "Nota1": 8.0, "Nota2": 8.5, "Media": 8.25, "Quantidade de faltas": 0, "Situacao": "Aprovado"},
    {"Matricula": 5, "Nome": "Aluno 5", "Nota1": 9.0, "Nota2": 9.5, "Media": 9.25, "Quantidade de faltas": 1, "Situacao": "Aprovado"},
    {"Matricula": 6, "Nome": "Aluno 6", "Nota1": 5.0, "Nota2": 5.5, "Media": 5.25, "Quantidade de faltas": 6, "Situacao": "Final"},
    {"Matricula": 7, "Nome": "Aluno 7", "Nota1": 7.0, "Nota2": 6.0, "Media": 6.5, "Quantidade de faltas": 2, "Situacao": "Final"},
    {"Matricula": 8, "Nome": "Aluno 8", "Nota1": 8.0, "Nota2": 7.5, "Media": 7.75, "Quantidade de faltas": 4, "Situacao": "Aprovado"},
    {"Matricula": 9, "Nome": "Aluno 9", "Nota1": 7.5, "Nota2": 7.0, "Media": 7.25, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 10, "Nome": "Aluno 10", "Nota1": 4.0, "Nota2": 3.0, "Media": 3.5, "Quantidade de faltas": 5, "Situacao": "Reprovado"},
    {"Matricula": 11, "Nome": "Aluno 11", "Nota1": 6.5, "Nota2": 5.5, "Media": 6.0, "Quantidade de faltas": 7, "Situacao": "Final"},
    {"Matricula": 12, "Nome": "Aluno 12", "Nota1": 8.5, "Nota2": 8.0, "Media": 8.25, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 13, "Nome": "Aluno 13", "Nota1": 7.5, "Nota2": 7.0, "Media": 7.25, "Quantidade de faltas": 3, "Situacao": "Aprovado"},
    {"Matricula": 14, "Nome": "Aluno 14", "Nota1": 5.0, "Nota2": 4.5, "Media": 4.75, "Quantidade de faltas": 8, "Situacao": "Final"},
    {"Matricula": 15, "Nome": "Aluno 15", "Nota1": 2.5, "Nota2": 3.0, "Media": 2.75, "Quantidade de faltas": 4, "Situacao": "Reprovado"},
    {"Matricula": 16, "Nome": "Aluno 16", "Nota1": 7.0, "Nota2": 8.0, "Media": 7.5, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 17, "Nome": "Aluno 17", "Nota1": 3.5, "Nota2": 3.0, "Media": 3.25, "Quantidade de faltas": 9, "Situacao": "Reprovado"},
    {"Matricula": 18, "Nome": "Aluno 18", "Nota1": 8.0, "Nota2": 7.0, "Media": 7.5, "Quantidade de faltas": 6, "Situacao": "Aprovado"},
    {"Matricula": 19, "Nome": "Aluno 19", "Nota1": 9.0, "Nota2": 8.5, "Media": 8.75, "Quantidade de faltas": 0, "Situacao": "Aprovado"},
    {"Matricula": 20, "Nome": "Aluno 20", "Nota1": 4.0, "Nota2": 5.0, "Media": 4.5, "Quantidade de faltas": 8, "Situacao": "Final"},
    {"Matricula": 21, "Nome": "Aluno 21", "Nota1": 2.0, "Nota2": 1.5, "Media": 1.75, "Quantidade de faltas": 3, "Situacao": "Reprovado"},
    {"Matricula": 22, "Nome": "Aluno 22", "Nota1": 8.0, "Nota2": 7.5, "Media": 7.75, "Quantidade de faltas": 1, "Situacao": "Aprovado"},
    {"Matricula": 23, "Nome": "Aluno 23", "Nota1": 5.5, "Nota2": 6.0, "Media": 5.75, "Quantidade de faltas": 4, "Situacao": "Final"},
    {"Matricula": 24, "Nome": "Aluno 24", "Nota1": 9.0, "Nota2": 8.5, "Media": 8.75, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 25, "Nome": "Aluno 25", "Nota1": 3.0, "Nota2": 2.5, "Media": 2.75, "Quantidade de faltas": 10, "Situacao": "Reprovado"},
    {"Matricula": 26, "Nome": "Aluno 26", "Nota1": 6.0, "Nota2": 5.5, "Media": 5.75, "Quantidade de faltas": 3, "Situacao": "Final"},
    {"Matricula": 27, "Nome": "Aluno 27", "Nota1": 8.0, "Nota2": 7.0, "Media": 7.5, "Quantidade de faltas": 4, "Situacao": "Aprovado"},
    {"Matricula": 28, "Nome": "Aluno 28", "Nota1": 6.5, "Nota2": 6.0, "Media": 6.25, "Quantidade de faltas": 2, "Situacao": "Final"},
    {"Matricula": 29, "Nome": "Aluno 29", "Nota1": 7.5, "Nota2": 8.0, "Media": 7.75, "Quantidade de faltas": 1, "Situacao": "Aprovado"},
    {"Matricula": 30, "Nome": "Aluno 30", "Nota1": 3.0, "Nota2": 4.0, "Media": 3.5, "Quantidade de faltas": 7, "Situacao": "Reprovado"},
    {"Matricula": 31, "Nome": "Aluno 31", "Nota1": 7.5, "Nota2": 8.0, "Media": 7.75, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 32, "Nome": "Aluno 32", "Nota1": 5.0, "Nota2": 4.5, "Media": 4.75, "Quantidade de faltas": 5, "Situacao": "Final"},
    {"Matricula": 33, "Nome": "Aluno 33", "Nota1": 2.5, "Nota2": 3.0, "Media": 2.75, "Quantidade de faltas": 10, "Situacao": "Reprovado"},
    {"Matricula": 34, "Nome": "Aluno 34", "Nota1": 6.5, "Nota2": 7.0, "Media": 6.75, "Quantidade de faltas": 4, "Situacao": "Final"},
    {"Matricula": 35, "Nome": "Aluno 35", "Nota1": 9.0, "Nota2": 8.5, "Media": 8.75, "Quantidade de faltas": 1, "Situacao": "Aprovado"},
    {"Matricula": 36, "Nome": "Aluno 36", "Nota1": 4.0, "Nota2": 4.5, "Media": 4.25, "Quantidade de faltas": 8, "Situacao": "Final"},
    {"Matricula": 37, "Nome": "Aluno 37", "Nota1": 3.5, "Nota2": 3.0, "Media": 3.25, "Quantidade de faltas": 9, "Situacao": "Reprovado"},
    {"Matricula": 38, "Nome": "Aluno 38", "Nota1": 7.0, "Nota2": 6.5, "Media": 6.75, "Quantidade de faltas": 2, "Situacao": "Final"},
    {"Matricula": 39, "Nome": "Aluno 39", "Nota1": 8.5, "Nota2": 9.0, "Media": 8.75, "Quantidade de faltas": 0, "Situacao": "Aprovado"},
    {"Matricula": 40, "Nome": "Aluno 40", "Nota1": 4.5, "Nota2": 4.0, "Media": 4.25, "Quantidade de faltas": 8, "Situacao": "Final"},
    {"Matricula": 41, "Nome": "Aluno 41", "Nota1": 3.0, "Nota2": 2.5, "Media": 2.75, "Quantidade de faltas": 9, "Situacao": "Reprovado"},
    {"Matricula": 42, "Nome": "Aluno 42", "Nota1": 7.5, "Nota2": 8.0, "Media": 7.75, "Quantidade de faltas": 1, "Situacao": "Aprovado"},
    {"Matricula": 43, "Nome": "Aluno 43", "Nota1": 5.5, "Nota2": 6.0, "Media": 5.75, "Quantidade de faltas": 3, "Situacao": "Final"},
    {"Matricula": 44, "Nome": "Aluno 44", "Nota1": 4.0, "Nota2": 4.5, "Media": 4.25, "Quantidade de faltas": 7, "Situacao": "Final"},
    {"Matricula": 45, "Nome": "Aluno 45", "Nota1": 2.0, "Nota2": 1.5, "Media": 1.75, "Quantidade de faltas": 10, "Situacao": "Reprovado"},
    {"Matricula": 46, "Nome": "Aluno 46", "Nota1": 8.0, "Nota2": 8.5, "Media": 8.25, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
    {"Matricula": 47, "Nome": "Aluno 47", "Nota1": 7.0, "Nota2": 6.5, "Media": 6.75, "Quantidade de faltas": 3, "Situacao": "Final"},
    {"Matricula": 48, "Nome": "Aluno 48", "Nota1": 6.0, "Nota2": 5.5, "Media": 5.75, "Quantidade de faltas": 6, "Situacao": "Final"},
    {"Matricula": 49, "Nome": "Aluno 49", "Nota1": 3.5, "Nota2": 3.0, "Media": 3.25, "Quantidade de faltas": 9, "Situacao": "Reprovado"},
    {"Matricula": 50, "Nome": "Aluno 50", "Nota1": 7.5, "Nota2": 8.0, "Media": 7.75, "Quantidade de faltas": 2, "Situacao": "Aprovado"},
]

# Criando DataFrame
df = pd.DataFrame(dados)

# Análise Estatística
media = df['Media'].mean()
mediana = df['Media'].median()
moda = df['Media'].mode()[0]
desvio_padrao = df['Media'].std()

print('===================')
print('Análise Estatística')
print('===================\n')

print(f"-> Média: {media}")
print(f"-> Mediana: {mediana}")
print(f"-> Moda: {moda}")
print(f"-> Desvio Padrão: {desvio_padrao}\n")

print('===============')
print('Análise Gráfica')
print('===============\n')

# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['Media'], bins=10, kde=True)
plt.axvline(media, color='r', linestyle='--', label=f'Média: {media:.2f}')
plt.axvline(mediana, color='g', linestyle='-', label=f'Mediana: {mediana:.2f}')
plt.axvline(moda, color='b', linestyle='-', label=f'Moda: {moda}')
plt.title('Histograma das Médias')
plt.xlabel('Médias')
plt.ylabel('Frequência')
plt.legend()
plt.show()

print()

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Media'])
plt.title('Boxplot das Médias')
plt.ylabel('Médias')
plt.show()

print()

# Gráfico de Dispersão
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Media'], marker='o', linestyle='-', color='b')
plt.title('Gráfico de Dispersão das Médias')
plt.xlabel('Índice')
plt.ylabel('Médias')
plt.show()

print()

# Análise de Distribuição
plt.figure(figsize=(10, 6))
sns.violinplot(y=df['Media'])
plt.title('Análise de Distribuição das Médias')
plt.ylabel('Médias')
plt.show()
