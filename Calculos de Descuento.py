def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    Args:
    - monto_total: El monto total de la compra.
    - porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10%).

    Returns:
    - El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Función para mostrar resultados
def mostrar_resultados(monto_total_compra, descuento, monto_final):
    print("Monto total de la compra:", monto_total_compra)
    print("Descuento aplicado:", descuento)
    print("Monto final a pagar después del descuento:", monto_final)

# Llamada a la función proporcionando solo el monto total de la compra
monto_total_compra_1 = 1000
descuento_calculado_1 = calcular_descuento(monto_total_compra_1)
monto_final_1 = monto_total_compra_1 - descuento_calculado_1
print("Resultados de la primera llamada:")
mostrar_resultados(monto_total_compra_1, descuento_calculado_1, monto_final_1)
print()

# Llamada a la función proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_total_compra_2 = 2000
porcentaje_descuento_2 = 15
descuento_calculado_2 = calcular_descuento(monto_total_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_total_compra_2 - descuento_calculado_2
print("Resultados de la segunda llamada:")
mostrar_resultados(monto_total_compra_2, descuento_calculado_2, monto_final_2)


