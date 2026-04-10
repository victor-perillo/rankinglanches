import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Consulta de Ranking", 
    page_icon="🍔", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# 2. Estilização Customizada (CSS)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 450px;
    }

    /* Centraliza o contêiner do botão */
    div.stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    /* Estilização do Botão de Buscar - GRANDE E DISTRIBUÍDO */
    div.stButton > button {
        background-color: #8A05BE !important;
        color: white !important;
        border-radius: 12px !important;
        width: 100% !important;
        height: 60px !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border: none !important;
        transition: 0.3s ease !important;
        margin-top: 10px !important;
    }

    div.stButton > button:hover {
        background-color: #700499 !important;
        color: white !important;
    }
    
    .resultado-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        margin-bottom: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        color: #333;
    }
    
    .destaque {
        color: #8A05BE;
        font-weight: bold;
        font-size: 18px;
    }

    .footer-text {
        text-align: center;
        font-size: 13px;
        color: #888;
        margin-top: 40px;
        border-top: 1px solid #eee;
        padding-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Banco de Dados
ranking_db = [
    {'posicao': 1, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 2, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 3, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 4, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 5, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 6, 'nome': 'HELLEN VITORIA SANTOS OLIVEIRA', 'cpf': '***.395.998-**'},
    {'posicao': 7, 'nome': 'MATEUS F ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 8, 'nome': 'DAVY OLIVEIRA RIBEIRO', 'cpf': '***.517.878-**'},
    {'posicao': 9, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 10, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 11, 'nome': 'JOÃO VICTOR LOPEZ DE ARRUDA', 'cpf': '***.329.808-**'},
    {'posicao': 12, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 13, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 14, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 15, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 16, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 17, 'nome': 'HENRICO AUGUSTO LIMA LOPES', 'cpf': '***.973.248-**'},
    {'posicao': 18, 'nome': 'BIANCA DIEBE', 'cpf': '***.838.758-**'},
    {'posicao': 19, 'nome': 'CRISTIANE ANTUNES DE OLIVEIRA DA SILVA', 'cpf': '***.916.068-**'},
    {'posicao': 20, 'nome': 'LORENA CRISTINA CASSIANO', 'cpf': '***.493.518-**'},
    {'posicao': 21, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 22, 'nome': 'THIAGO CICONELLO GIOVANETTI', 'cpf': '***.705.048-**'},
    {'posicao': 23, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 24, 'nome': 'ANTONIO GABRIEL LIMA DE JESUS', 'cpf': '***.804.718-**'},
    {'posicao': 25, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 26, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 27, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 28, 'nome': 'LEON PEREIRA PINTO FAGUNDES', 'cpf': '***.469.018-**'},
    {'posicao': 29, 'nome': 'TIAGO ALVES SIMOES', 'cpf': '***.528.818-**'},
    {'posicao': 30, 'nome': 'ELIOENAI CACERES PEREIRA', 'cpf': '***.496.738-**'},
    {'posicao': 31, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 32, 'nome': 'MURILO COELHO DOS SANTOS', 'cpf': '***.585.008-**'},
    {'posicao': 33, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 34, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 35, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 36, 'nome': 'ALESSANDRO RODRIGUES MELO FO', 'cpf': '***.118.258-**'},
    {'posicao': 37, 'nome': 'MARCOS ELIAS FERREIRA SANTOS', 'cpf': '***.924.937-**'},
    {'posicao': 38, 'nome': 'TIAGO MARTINS DOMINGUES', 'cpf': '***.241.908-**'},
    {'posicao': 39, 'nome': 'ADEILTON ALVES BOSCARDIN', 'cpf': '***.449.378-**'},
    {'posicao': 40, 'nome': 'FREDERICO HASEGAWA COPELI VENA', 'cpf': '***.878.578-**'},
    {'posicao': 41, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 42, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 43, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 44, 'nome': 'RICARDO HERNAN SARAVIA SIQUEIRA', 'cpf': '***.988.378-**'},
    {'posicao': 45, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 46, 'nome': 'CLAYTON FIGUEIREDO MAIA', 'cpf': '***.848.728-**'},
    {'posicao': 47, 'nome': 'POLYANNA PIRES PASCHOAL', 'cpf': '***.942.958-**'},
    {'posicao': 48, 'nome': 'DANIEL RODRIGUES LOPES ADEJARBAS', 'cpf': '***.276.508-**'},
    {'posicao': 49, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 50, 'nome': 'BRUNO EDUARDO DAMASCO SABRIANO DA SILVA', 'cpf': '***.447.818-**'},
    {'posicao': 116, 'nome': 'PRISCILA S K CORREA', 'cpf': '***.553.718-**'}
]

# 4. Interface
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center;'>🍔 Lanches</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #333;'>Consulta de Ranking</h2>", unsafe_allow_html=True)

# Input de busca
nome_busca = st.text_input("", placeholder="Insira seu nome completo...")

# Botão centralizado e distribuído conforme o novo CSS
c_btn1, c_btn2, c_btn3 = st.columns([0.2, 2.6, 0.2])
with c_btn2:
    botao_busca = st.button("Buscar")

# --- LÓGICA 1: BUSCA ---
if botao_busca:
    if not nome_busca:
        st.warning("Por favor, digite um nome.")
    else:
        resultados = [u for u in ranking_db if nome_busca.lower() in u['nome'].lower()]
        if resultados:
            for p in resultados:
                st.markdown(f"""
                    <div class="resultado-card">
                        <p style="margin: 0;">Nome: <strong style="color: #333;">{p['nome']}</strong></p>
                        <p style="margin: 5px 0;">CPF: <strong>{p['cpf']}</strong></p>
                        <p style="margin: 10px 0 0 0;">Posição: <span class="destaque">{p['posicao']}º lugar</span></p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Nome não encontrado.")

# 5. Rodapé
st.markdown("""
    <div class="footer-text">
        Atualizado em 10/04/2026<br>
        <strong>Promoção válida até 30/04/2026</strong>
    </div>
""", unsafe_allow_html=True)
