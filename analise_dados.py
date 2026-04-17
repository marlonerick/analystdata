# ======================
# 📊 CARREGAMENTO
# ======================

import pandas as pd

# Carregar os dados
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# ======================
# 📈 ANÁLISE GERAL
# ======================

# Mostrar primeiras linhas
print("\n📌 Primeiras linhas:")
print(df.head())

# Faturamento total (gorjetas)
faturamento_total = df["total_bill"].sum()
print(f"\n💰 Faturamento total: R${faturamento_total:.2f}")

#Maior valor gasto
maior_valor = df["total_bill"].max()
print("\n📈 Maior valor gasto. R$", maior_valor)

# Média de gastos
media = df["total_bill"].mean()
print(f"\n📊 Média de gasto: {media:.2f}")

#Menor valor gasto
menor_valor = df["total_bill"].min()
print("\n📉 Menor valor gasto. R$", menor_valor)

# Dia com maior faturamento
faturamento_por_dia = df.groupby("day")["total_bill"].sum()
print("\n📅 Faturamento por dia:")
print(faturamento_por_dia.sort_values(ascending=False).to_frame())

# Melhor dia
melhor_dia = faturamento_por_dia.idxmax()
print(f"\n🏆 Dia com mais faturamento: {melhor_dia}")

# Tipo de cliente que mais gasta
por_genero = df.groupby("sex")["total_bill"].mean()
print("\n", por_genero.to_frame(name="👥 Média por gênero:"))

# ========================
# 🔍 ANÁLISES ESPECÍFICAS
# ========================

filtro =  df[df["total_bill"] > 20 ]
print("\n💳 Contas acima de 20:")
print(filtro[["total_bill", "tip", "day"]].head())

avg_bill_by_smoker = df.groupby('smoker')["total_bill"].mean()
print(f"\n",avg_bill_by_smoker.to_frame(name="🚬 Fumantes").round(2))

media_por_horario = df.groupby("time")["total_bill"].mean()
print(f"\n{media_por_horario.to_frame(name='🕓 Media por horario').round(2)}")

top3 = df.nlargest(3, "total_bill")
print("\n🔝 Maiores contas:")
print(top3[["total_bill", "tip", "day", "time"]])

print("\n💰 Gorjeta percentual")
df["tip_percent"] = df["tip"] / df["total_bill"]
print("\n",df["tip_percent"].head().to_frame())
print("\n",df["tip_percent"].describe().to_frame())

media_gorjeta = df.groupby("time")["tip_percent"].mean()
print("\n💸 Média de gorjeta (%):")
print(media_gorjeta.to_frame(name="Média(%)"))

# ======================
# 📊 VISUALIZAÇÃO
# ======================

import matplotlib.pyplot as plt

ax = faturamento_por_dia.plot(kind="bar", color=["#FF9999", "#66B2FF"])
plt.title("Faturamento por Dia", fontsize=14, fontweight='bold')
plt.xlabel("Dia da semana")
plt.ylabel("Total")
# adiciona valores as barras do grafico.
plt.bar_label(ax.containers[0], padding=3, fmt="R$ %.2f")
# aumenta um pouco o limite do eixo Y para o número não bater no topo
plt.ylim(0, faturamento_por_dia.max() * 1.1)
plt.tight_layout()
plt.show()

ax = avg_bill_by_smoker.plot(kind="bar", color=["#FF9999", "#66B2FF"])
plt.title("Fumantes vs Não fumantes", fontsize=14, fontweight='bold')
plt.xticks([0,1], ["Não fumantes", "Fumantes"], rotation=0)
plt.xlabel("Categorias")
plt.ylabel("Valores")
# adiciona valores as barras do grafico.
plt.bar_label(ax.containers[0], padding=3, fmt="R$ %.2f")
# aumenta um pouco o limite do eixo Y para o número não bater no topo
plt.ylim(0, avg_bill_by_smoker.max() * 1.1)
plt.tight_layout()
plt.show()


print("\n📊 INSIGHTS:")

print("- O jantar apresenta maior faturamento médio que o almoço")
print("- Fumantes possuem ticket médio ligeiramente maior")
print("- Os maiores valores estão concentrados em dias específicos")