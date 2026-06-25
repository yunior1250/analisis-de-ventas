import pandas  as pd 
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt




datos = pd.read_csv("ventas.csv")

#print("\nDinero vendido por productos")
#print(datos.groupby("producto")["total"].sum())

#print("\nDinero vendido por ciudad")
#print(datos.groupby("ciudad")["total"].sum())
#print("\nDinero vendido  por vendedor "   )
#print(datos.groupby("vendedor")["total"].sum().sort_values(ascending=False))  


#GRAFICOS
#Calculamos : dinero por vendedor ,  de mayor a menor 
ventas_por_vendedor  = datos.groupby("vendedor")["total"].sum().sort_values(ascending=False)
print(ventas_por_vendedor)
#Lo convertimos en grafico 
ventas_por_vendedor.plot(kind="bar")

# Le ponemos titulo  y etiquetas
plt.title("Dinero vendido por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Total (S/.)")

#guardamos el grafico como imgaen
plt.tight_layout()
plt.savefig("grafico-ventas-vendedor.png")
print("Grafico guardado como grafico-ventas-vendedor.png")
#Grafico 2
plt.figure()
ventas_por_producto = datos.groupby("producto")["total"].sum().sort_values(ascending = False)
print (ventas_por_producto)

ventas_por_producto.plot(kind = "bar")

plt.title("Dinero vendido por producto")
plt.xlabel("Productos")
plt.ylabel("Total (S/.)")

plt.tight_layout()
plt.savefig("grafico-ventas-producto.png")
print("Grafico guardado como grafico-ventas-producto.png")

#Grafico 3 
plt.figure()
ventas_por_ciudad = datos.groupby("ciudad")["total"].sum().sort_values(ascending=False)
print(ventas_por_ciudad)

ventas_por_ciudad.plot(kind = "bar")

plt.title("Dinero vendido por ciudad")
plt.xlabel("Ciudades")
plt.ylabel("Total (S/.)")


plt.tight_layout()
plt.savefig("grafico-ventas-ciudad.png")
print("Grafico guardado como grafico-ventas-ciudad.png")


