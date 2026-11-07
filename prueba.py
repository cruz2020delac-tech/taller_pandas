import pandas as pd


# ventas_reducido = pd.read_csv("Data/raw/ventas.csv", usecols=["producto", "total"])
# print(ventas_reducido)

ventas = pd.read_csv("Data/raw/ventas.csv")
# cliente = pd.read_csv("Data/raw/cliente.csv")


# print(ventas.shape)
# ventas.info()
# print(ventas.describe())

# print(cliente.shape)
# cliente.info()
# print(cliente.describe())



print(ventas["total"])
ventas = ventas.set_index("id_venta")
print(ventas.head())