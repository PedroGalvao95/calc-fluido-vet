import streamlit as st

st.title("Calculadora de Fluidoterapia Veterinária")

st.markdown("Ajuste os valores abaixo para calcular as taxas de fluidoterapia:")

# Inputs
species = st.selectbox("Espécie", ["Cão", "Gato"])
weight = st.number_input("Peso do animal (kg)", min_value=0.1, step=0.1)
dehydration = st.slider("Percentual de desidratação (%)", 0, 20, 0)
correction_time = st.number_input("Tempo para correção (horas)", min_value=1, step=1)
surgery = st.checkbox("Paciente em transoperatório?")

# Cálculos
if surgery:
    maintenance_rate = 5.0 if species == "Cão" else 3.0
    st.info(f"Modo Cirúrgico: Taxa ajustada para {maintenance_rate} mL/kg/h")
else:
    maintenance_rate = 2.5 if species == "Cão" else 1.9
    st.info(f"Modo Manutenção: Taxa ajustada para {maintenance_rate} mL/kg/h")

maintenance_daily = maintenance_rate * weight * 24  # mL/day
dehydration_deficit = weight * (dehydration / 100) * 1000  # mL
correction_rate = dehydration_deficit / correction_time if correction_time > 0 else 0  # mL/hr
total_rate = maintenance_rate * weight + correction_rate  # mL/hr


# Outputs
st.subheader("Resultados")
st.write(f"Taxa de manutenção: {maintenance_rate} mL/kg/hr")
st.write(f"Fluido de manutenção diário: {maintenance_daily:.1f} mL/dia")
st.write(f"Déficit de desidratação: {dehydration_deficit:.1f} mL")
st.write(f"Taxa de correção: {correction_rate:.1f} mL/hr")
st.write(f"Taxa total de fluidos: {total_rate:.1f} mL/hr")

