# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#Cargamos datos  (igual que en analise)
datos = pd.read_csv("ventas.csv")

#titulo de pa paguina web
st.title("Analisis de ventas")

#un texto debajo del titulo 
st.write("Estos son los datos de venta crudos")

#METRICAS principales (KPIs)
total_vendido = datos["total"].sum()
num_ventas  = len(datos)
ticket_promedio= datos["total"].mean()

col1,col2, col3 = st.columns(3)

col1.metric("💰 Total vendido" , f"S/.{total_vendido:,.0f}")
col2.metric("🧾 Nro ventas " ,num_ventas)
col3.metric("🎯 Ticket Promedio" , f"S/.{ticket_promedio:,.0f}")



#Motram,os la tabla completa
st.dataframe(datos)

#====Grafico :dinero por vendedor== 

st.subheader("Dinero vendido por vendedor")

ventas_por_vendedor  = datos.groupby("vendedor")["total"].sum().sort_values(ascending=False)

#Usamos matplotlib para crear un grafico de barras

fig , ax = plt.subplots()

ventas_por_vendedor.plot(kind="bar", ax=ax)

#ax.set_title("Dinero vendido por vendedor")
ax.set_xlabel("Vendedor")
ax.set_ylabel("Total (S/.)")

st.pyplot(fig)

#====Grafico de ventas por producto==
st.subheader("Dinero vendido por producto")

ventas_por_producto = datos.groupby("producto")["total"].sum().sort_values(ascending=False)

fig, ax = plt.subplots()

ventas_por_producto.plot(kind="bar", ax=ax)

#Etiquetas y titulo
ax.set_xlabel("Productos")
ax.set_ylabel("Total (S/.)")

#guardamos el grafico
st.pyplot(fig)
