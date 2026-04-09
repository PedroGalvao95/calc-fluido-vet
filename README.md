# calc-fluido-vet
Calculadora de fluidoterapia veterinária (cães e gatos)

Uma aplicação interativa desenvolvida para auxiliar médicos veterinários no cálculo preciso de taxas de fluidoterapia para cães e gatos. O projeto diferencia as necessidades metabólicas de manutenção das exigências críticas do transoperatório.

## 📖 Contexto e Justificativa

Na rotina de cirurgia de tecidos moles, a precisão na fluidoterapia é vital. Taxas excessivas podem levar ao edema pulmonar (especialmente em felinos), enquanto taxas insuficientes comprometem a perfusão renal sob anestesia.

Este projeto foi criado para codificar as diretrizes da **AAHA (American Animal Hospital Association)**, oferecendo uma interface rápida para o dia a dia hospitalar, eliminando erros de cálculo manual sob pressão.

## 🛠️ Funcionalidades

- **Diferenciação por Espécie:** Aplica taxas específicas para caninos e felinos.
- **Modo Transoperatório:** Ajuste automático para perdas evaporativas e vasodilatação anestésica (5 mL/kg/h para cães e 3 mL/kg/h para gatos).
- **Modo Manutenção:** Baseado em necessidades basais de repouso.
- **Cálculo de Volume Total:** Projeção para 24 horas de tratamento.

## 💻 Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Interface Web:** [Streamlit](https://streamlit.io/)
- **Lógica de Domínio:** Medicina Veterinária e Fisiologia Cirúrgica.

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:
   
   git clone [https://github.com/PedroGalvao95/calc-fluido-vet.git](https://github.com/PedroGalvao95/calc-fluido-vet.git)

2. Instale a dependência:

    pip install -r requirements.txt

3. Execute o app:

    streamlit run app.py

📈 Evolução do Projeto (Roadmap)
[ ] Implementar fórmulas alométricas;
[ ] Adicionar cálculo de Gotas/Minuto (Macro e Microequipo);
[ ] Incluir módulo de CRI (Constant Rate Infusion) para fármacos analgésicos.

Desenvolvido por Pedro Galvão - Médico Veterinário Analista e Estudante de Análise e Desenvolvimento de Sistemas.