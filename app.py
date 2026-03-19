import streamlit as st

# 1. Configuração da página para Mobile e Desktop
st.set_page_config(
    page_title="Consulta de Ranking", 
    page_icon="🍔", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# 2. Estilização Customizada (CSS) - Design Moderno e Responsivo
st.markdown("""
    <style>
    /* Esconde elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Container principal ajustado para telas de celular */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 450px;
    }
    
    /* Estilo do Botão Roxo (Estilo Nu) */
    .stButton>button {
        background-color: #8A05BE;
        color: white;
        border-radius: 12px;
        width: 100%;
        padding: 12px;
        font-weight: bold;
        border: none;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #700499;
        color: white;
        transform: translateY(-2px);
    }
    
    /* Estilo dos cards de resultado */
    .resultado-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        color: #333;
    }
    
    .destaque {
        color: #8A05BE;
        font-weight: bold;
        font-size: 20px;
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

# 3. Banco de Dados Completo (Ranking Consolidado: 01/03 a 18/03)
# Baseado no valor total acumulado do maior para o menor.
ranking_db = [
    {"posicao": 1, "nome": "FLÁVIA CAMARGO CAMPOS", "cpf": "***.900.098-**"},
    {"posicao": 2, "nome": "VINICIUS MONTANINI PIEROTE", "cpf": "***.608.878-**"},
    {"posicao": 3, "nome": "ARIANA OMURA VIEIRA", "cpf": "***.092.708-**"},
    {"posicao": 4, "nome": "THEO MARCHETTI BARCELOS", "cpf": "***.507.218-**"},
    {"posicao": 5, "nome": "VITOR SANDY PUPO", "cpf": "***.295.288-**"},
    {"posicao": 6, "nome": "MATHEUS AUGUSTO SANTOS GUEFF", "cpf": "***.498.128-**"},
    {"posicao": 7, "nome": "MARIA EDUARDA MADUREIRA RODRIGUES", "cpf": "***.607.128-**"},
    {"posicao": 8, "nome": "IVAN LUCA MUNHOZ DE SOUZA", "cpf": "***.651.448-**"},
    {"posicao": 9, "nome": "GUSTAVO PIRES FORMIGONI LEITE", "cpf": "***.557.508-**"},
    {"posicao": 10, "nome": "LUCAS CAMPOS LEME DE BARROS", "cpf": "***.053.288-**"},
    {"posicao": 11, "nome": "SAMIRA TAMER", "cpf": "***.086.048-**"},
    {"posicao": 12, "nome": "GABRIEL DE PAULA IZAIAS", "cpf": "***.917.348-**"},
    {"posicao": 13, "nome": "DANILO WILLY MOREIRA TORRES", "cpf": "***.034.898-**"},
    {"posicao": 14, "nome": "MATEUS FALVES", "cpf": "***.438.158-**"},
    {"posicao": 15, "nome": "WALDEMAR FAUSTINO DE SOUZA FILHO", "cpf": "***.457.518-**"},
    {"posicao": 16, "nome": "EMANUEL MEDEIROS ROSA", "cpf": "***.521.808-**"},
    {"posicao": 17, "nome": "MARCOS UNO", "cpf": "***.673.268-**"},
    {"posicao": 18, "nome": "HUMBERTO PERES FLORES NETO", "cpf": "***.717.048-**"},
    {"posicao": 19, "nome": "LAURA DA SILVA SEGANTIN", "cpf": "***.300.358-**"},
    {"posicao": 20, "nome": "GABRIEL B QUEIROZ", "cpf": "***.126.238-**"},
    {"posicao": 21, "nome": "LEANDRO TEODORO POLERA", "cpf": "***.565.548-**"},
    {"posicao": 22, "nome": "LUCAS GABRIEL OLIVEIRA SALDIAS", "cpf": "***.725.518-**"},
    {"posicao": 23, "nome": "JULIANA ALVES DORIGAO", "cpf": "***.755.028-**"},
    {"posicao": 24, "nome": "TIAGO ALVES SIMOES", "cpf": "***.528.818-**"},
    {"posicao": 25, "nome": "SOPHIA CASTILHO MORENO", "cpf": "***.497.218-**"},
    {"posicao": 26, "nome": "PAULO VITOR LEMES", "cpf": "***.781.688-**"},
    {"posicao": 27, "nome": "ANA BEATRIZ MATOS VIANA", "cpf": "***.863.088-**"},
    {"posicao": 28, "nome": "BRUNO VINICIUS URIAS QUEIROZ", "cpf": "***.522.708-**"},
    {"posicao": 29, "nome": "ANDERSON MARTINS MARQUES", "cpf": "***.887.218-**"},
    {"posicao": 30, "nome": "RAVEN AARON ALBUQUERQUE PRESTES BATISTA", "cpf": "***.163.028-**"},
    {"posicao": 31, "nome": "KAWAN FERNANDES DE ARAUJO", "cpf": "***.099.108-**"},
    {"posicao": 32, "nome": "GUSTAVO HENRIQUE DE OLIVEIRA LIMA", "cpf": "***.204.738-**"},
    {"posicao": 33, "nome": "THIAGO HENRIQUE MUNIZ NEVES", "cpf": "***.276.608-**"},
    {"posicao": 34, "nome": "ELAINE PERILLO RODRIGUES SAMPAIO", "cpf": "***.880.148-**"},
    {"posicao": 35, "nome": "RAFAEL SARTORI DA COSTA", "cpf": "***.841.938-**"},
    {"posicao": 36, "nome": "NICOLE JANINE BOLZANI OLIVEIRA", "cpf": "***.303.578-**"},
    {"posicao": 37, "nome": "TIAGO AUGUSTO PEDROSO DE CARVALHO", "cpf": "***.333.798-**"},
    {"posicao": 38, "nome": "ELIOENAJ CACERES PEREIRA", "cpf": "***.496.738-**"},
    {"posicao": 39, "nome": "MICHAEL MARQUES VIEIRA DE SOUZA", "cpf": "***.340.948-**"},
    {"posicao": 40, "nome": "JOAO PEDRO DRUZIAN FERREIRA", "cpf": "***.484.748-**"},
    {"posicao": 41, "nome": "KELVIN CORRÊA", "cpf": "***.649.488-**"},
    {"posicao": 42, "nome": "PAULO APOLINARIO DE SOUZA", "cpf": "***.105.848-**"},
    {"posicao": 43, "nome": "JULIO CESAR VIEIRA", "cpf": "***.910.948-**"},
    {"posicao": 44, "nome": "PRISCILA NORONHA MENDES", "cpf": "***.687.188-**"},
    {"posicao": 45, "nome": "PEDRO HENRIQUE MOURA CAYUELLA", "cpf": "***.970.818-**"},
    {"posicao": 46, "nome": "MARINA SILVEIRA TOLEDO", "cpf": "***.003.218-**"},
    {"posicao": 47, "nome": "MATHEUS BUENO SIRILO", "cpf": "***.296.028-**"},
    {"posicao": 48, "nome": "NICOLAS DE OLIVEIRA DIAS", "cpf": "***.578.008-**"},
    {"posicao": 49, "nome": "LUCAS TORRES SANTANA", "cpf": "***.307.418-**"},
    {"posicao": 50, "nome": "ALESSANDRO RODRIGUES MELO FO", "cpf": "***.118.258-**"},
    {"posicao": 51, "nome": "ENZO LIAN PINHEIRO MENDES", "cpf": "***.139.548-**"},
    {"posicao": 52, "nome": "FERNANDA TERESA CORREA DA SILV", "cpf": "***.570.758-**"},
    {"posicao": 53, "nome": "BRENO JOSE DA SILVA", "cpf": "***.182.118-**"},
    {"posicao": 54, "nome": "BRUNA FAVA PIRES", "cpf": "***.915.848-**"},
    {"posicao": 55, "nome": "CAIQUE ALEXANDRE DE OLIVEIRA", "cpf": "***.362.908-**"},
    {"posicao": 56, "nome": "CAMILA MARTINS QUEIROZ", "cpf": "***.530.648-**"},
    {"posicao": 57, "nome": "CESAR HENRIQUE CAMARGO DOS SANTOS", "cpf": "***.590.078-**"},
    {"posicao": 58, "nome": "DANIEL CARVALHO", "cpf": "***.889.108-**"},
    {"posicao": 59, "nome": "DOUGLAS RAFAEL DE SOUSA MENDES", "cpf": "***.372.248-**"},
    {"posicao": 60, "nome": "EMILLY RAISSA DE ALMEIDA DE MORAES", "cpf": "***.623.028-**"},
    {"posicao": 61, "nome": "FELIPE DOS REIS ANTUNES", "cpf": "***.029.988-**"},
    {"posicao": 62, "nome": "HERIVELTON HENRIQUE GONÇALVES", "cpf": "***.607.418-**"},
    {"posicao": 63, "nome": "GABRIELLI RAMOS DA SILVA", "cpf": "***.163.158-**"},
    {"posicao": 64, "nome": "JOÃO PEDRO DE OLIVEIRA FERREIRA", "cpf": "***.339.708-**"},
    {"posicao": 65, "nome": "AMADOR BUENO DE OLIVEIRA NETO", "cpf": "***.548.238-**"},
    {"posicao": 66, "nome": "GUSTAVO DE CAMPOS ANTUNES", "cpf": "***.326.288-**"},
    {"posicao": 67, "nome": "FULVIO DE PAULA LIMA", "cpf": "***.152.758-**"},
    {"posicao": 68, "nome": "FABIO LUIZ DE FRANCA FILHO", "cpf": "***.724.428-**"},
    {"posicao": 69, "nome": "GUILHERME OTO VENTURELLI", "cpf": "***.979.058-**"},
    {"posicao": 70, "nome": "GISLAINE OLIVIERA TAKUSHI", "cpf": "***.891.438-**"},
    {"posicao": 71, "nome": "FLÁVIA ALVARENGA SARTORI", "cpf": "***.695.758-**"},
    {"posicao": 72, "nome": "JULIA MARIA JUBAT ALVES DOS SANTOS", "cpf": "***.363.038-**"},
    {"posicao": 73, "nome": "JULIA TIEMI VASQUES BANDEIRA", "cpf": "***.020.448-**"},
    {"posicao": 74, "nome": "FREDERICO HASEGAWA COPELI VENA", "cpf": "***.878.578-**"},
    {"posicao": 75, "nome": "CAROLINA GOMES DE OLIVEIRA", "cpf": "***.232.598-**"},
    {"posicao": 76, "nome": "CAIO FERNANDO SCUDELER", "cpf": "***.909.568-**"},
    {"posicao": 77, "nome": "RENATA MARTINS", "cpf": "***.600.208-**"},
    {"posicao": 78, "nome": "MIGUEL DOS SANTOS GUSSI", "cpf": "***.539.148-**"},
    {"posicao": 79, "nome": "DANILO DE OLIVERIA BARROSO", "cpf": "***.127.178-**"},
    {"posicao": 80, "nome": "DANIEL JOSE BERNARDES FILHO", "cpf": "***.229.748-**"},
    {"posicao": 81, "nome": "CICERA MARIA C DE OLIVEIRA", "cpf": "***.043.138-**"},
    {"posicao": 82, "nome": "EDUARDO ALVES TAVEIRA", "cpf": "***.396.148-**"},
    {"posicao": 83, "nome": "ERIC RODRIGUES BERTO", "cpf": "***.036.498-**"}
]

# 4. Construção da Interface
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.error("Imagem 'logo.jpg' não encontrada na pasta.")

st.markdown("<h2 style='text-align: center; color: #333; margin-bottom: 25px;'>Confira sua posição</h2>", unsafe_allow_html=True)

# Campo de texto
nome_busca = st.text_input("", placeholder="Insira seu nome completo...")

# Centralização do Botão usando colunas
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    botao_clicado = st.button("Buscar no Ranking")

# Lógica de Busca e Exibição
if botao_clicado:
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
                        <p style="margin: 10px 0 0 0;">Sua Posição: <span class="destaque">{p['posicao']}º lugar</span></p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Nome não encontrado no ranking.")

# 5. Rodapé Informativo
st.markdown("""
    <div class="footer-text">
        Atualizado em 19/03/2026<br>
        <strong>Final da promoção: 31/03/2026</strong>
    </div>
""", unsafe_allow_html=True)
