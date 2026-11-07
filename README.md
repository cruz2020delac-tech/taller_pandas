# Taller- Pandas
**Autor:** [sergio campo]

---

### Respuestas al Desafío Final

1. **¿Qué categoría genera más ingresos?**
   La categoría que genera más ingresos es la de Tecnología.
   Se agrupó la información por la columna `"categoria"`, se sumaron los valores de la columna `"total"` y se ordenaron de mayor a menor.

2. **¿Qué canal vende más?**
    El canal que vende más es Online, registrando un mayor volumen tanto en número de transacciones como en ingresos totales.
   Se agrupó por la columna `"canal"`, aplicando un conteo de ventas y una suma de los ingresos totales para comparar su rendimiento.

3. **¿Los clientes VIP compran más que los Regulares?**
   Sí, al analizar los promedios por cliente, los clientes del segmento VIP realizan más compras individuales y generan un gasto promedio superior por usuario en comparación con los clientes Regulares.
   Se calculó el número único de clientes por segmento y se dividieron las compras y el gasto total entre dichos usuarios para obtener promedios reales y equitativos.

4. **¿Qué método de pago es el más usado?**
   El método de pago más utilizado por los clientes es Tarjeta de Crédito.
   Se aplicó un conteo de frecuencias (`value_counts`) sobre la columna `"metodo_pago"` para identificar cuál opción registra la mayor cantidad de transacciones.

5. **¿Cuáles son los cinco clientes con más compras?**
   Los cinco clientes con mayor volumen de compras y mejor desempeño de gasto son aquellos con mayor número de transacciones registradas en el tope de la tabla agrupada.
   Se agrupó por identificador y nombre del cliente, contando las compras y sumando el gasto total, ordenando descendentemente por ambas métricas y filtrando los primeros 5 registros con `.head(5)`.
