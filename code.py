import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Contador de Billetes", layout="centered")

st.title("💵 Contador de Billetes (MXN)")

st.write("Ingresa la cantidad de billetes por denominación:")

# Diccionario de denominaciones
denominaciones = {
    20: 0,
    50: 0,
    100: 0,
    200: 0,
    500: 0,
    1000: 0
}

# Inputs para cada denominación
conteo = {}

for denom in denominaciones:
    conteo[denom] = st.number_input(
        f"Billetes de ${denom}",
        min_value=0,
        step=1,
        value=0
    )

# Cálculo del total
total = sum(denom * cantidad for denom, cantidad in conteo.items())

# Mostrar desglose
st.subheader("Desglose")
for denom, cantidad in conteo.items():
    if cantidad > 0:
        st.write(f"${denom} x {cantidad} = ${denom * cantidad}")

# Mostrar total
st.subheader("Total")
st.success(f"💰 Total: ${total:,.2f} MXN")
