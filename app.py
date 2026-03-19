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
ranking_db = [
    {"posicao": 1, "nome": "Flávia Camargo Campos", "cpf": "***.900.098-**"},
    {"posicao": 2, "nome": "VINICIUS MONTANINI PIEROTE", "cpf": "***.608.878-**"},
    {"posicao": 3, "nome": "Ariana Omura Vieira", "cpf": "***.092.708-**"},
    {"posicao": 4, "nome": "VITOR SANDY PUPO", "cpf": "***.295.288-**"},
    {"posicao": 5, "nome": "THEO MARCHETTI BARCELOS", "cpf": "***.507.218-**"},
    {"posicao": 6, "nome": "Matheus Augusto Santos Gueff", "cpf": "***.498.128-**"},
    {"posicao": 7, "nome": "GUSTAVO PIRES FORMIGONI LEITE", "cpf": "***.557.508-**"},
    {"posicao": 8, "nome": "Maria Eduarda Madureira Rodrigues", "cpf": "***.607.128-**"},
    {"posicao": 9, "nome": "WALDEMAR FAUSTINO DE SOUZA FILHO", "cpf": "***.457.518-**"},
    {"posicao": 10, "nome": "GABRIEL DE PAULA IZAIAS", "cpf": "***.917.348-**"},
    {"posicao": 11, "nome": "SAMIRA TAMER", "cpf": "***.086.048-**"},
    {"posicao": 12, "nome": "EMANUEL MEDEIROS ROSA", "cpf": "***.521.808-**"},
    {"posicao": 13, "nome": "Ivan Luca Munhoz de Souza", "cpf": "***.651.448-**"},
    {"posicao": 14, "nome": "MARCOS UNO", "cpf": "***.673.268-**"},
    {"posicao": 15, "nome": "LAURA DA SILVA SEGANTIN", "cpf": "***.300.358-**"},
    {"posicao": 16, "nome": "LUCAS CAMPOS LEME DE BARROS", "cpf": "***.053.288-**"},
    {"posicao": 17, "nome": "Bruno Vinicius Urias Queiroz", "cpf": "***.522.708-**"},
    {"posicao": 18, "nome": "MATEUS F ALVES", "cpf": "***.438.158-**"},
    {"posicao": 19, "nome": "Danilo Willy Moreira Torres", "cpf": "***.034.898-**"},
    {"posicao": 20, "nome": "ANA BEATRIZ MATOS VIANA", "cpf": "***.863.088-**"},
    {"posicao": 21, "nome": "GABRIEL B QUEIROZ", "cpf": "***.126.238-**"},
    {"posicao": 22, "nome": "Humberto Peres Flores Neto", "cpf": "***.717.048-**"},
    {"posicao": 23, "nome": "JULIANA ALVES DORIGAO", "cpf": "***.755.028-**"},
    {"posicao": 24, "nome": "PAULO VITOR LEMES", "cpf": "***.781.688-**"},
    {"posicao": 25, "nome": "TIAGO ALVES SIMOES", "cpf": "***.528.818-**"},
    {"posicao": 26, "nome": "MICHAEL MARQUES VIEIRA DE SOUZA", "cpf": "***.340.948-**"},
    {"posicao": 27, "nome": "Leandro Teodoro Polera", "cpf": "***.565.548-**"},
    {"posicao": 28, "nome": "Sophia Castilho Moreno", "cpf": "***.497.218-**"},
    {"posicao": 29, "nome": "RAVEN AARON ALBUQUERQUE PRESTES BATISTA", "cpf": "***.163.028-**"},
    {"posicao": 30, "nome": "Thiago Henrique Muniz Neves", "cpf": "***.276.608-**"},
    {"posicao": 31, "nome": "Gustavo Henrique de Oliveira Lima", "cpf": "***.204.738-**"},
    {"posicao": 32, "nome": "KAWAN FERNANDES DE ARAUJO", "cpf": "***.099.108-**"},
    {"posicao": 33, "nome": "Rafael Sartori da Costa", "cpf": "***.841.938-**"},
    {"posicao": 34, "nome": "FREDERICO HASEGAWA COPELI VENA", "cpf": "***.878.578-**"},
    {"posicao": 35, "nome": "LUCAS GABRIEL OLIVEIRA SALDIAS", "cpf": "***.725.518-**"},
    {"posicao": 36, "nome": "JOAO PEDRO DRUZIAN FERREIRA", "cpf": "***.484.748-**"},
    {"posicao": 37, "nome": "ELAINE PERILLO RODRIGUES SAMPAIO", "cpf": "***.880.148-**"},
    {"posicao": 38, "nome": "Nicolas de Oliveira Dias", "cpf": "***.578.008-**"},
    {"posicao": 39, "nome": "LUCAS TORRES SANTANA", "cpf": "***.307.418-**"},
    {"posicao": 40, "nome": "Kelvin Corrêa", "cpf": "***.649.488-**"},
    {"posicao": 41, "nome": "Gustavo de Campos Antunes", "cpf": "***.326.288-**"},
    {"posicao": 42, "nome": "Breno Jose da Silva", "cpf": "***.182.118-**"},
    {"posicao": 43, "nome": "DANIEL CARVALHO", "cpf": "***.889.108-**"},
    {"posicao": 44, "nome": "ELIOENAJ CACERES PEREIRA", "cpf": "***.496.738-**"},
    {"posicao": 45, "nome": "TIAGO AUGUSTO PEDROSO DE CARVALHO", "cpf": "***.333.798-**"},
    {"posicao": 46, "nome": "PAULO APOLINARIO DE SOUZA", "cpf": "***.105.848-**"},
    {"posicao": 47, "nome": "FABIO LUIZ DE FRANCA FILHO", "cpf": "***.724.428-**"},
    {"posicao": 48, "nome": "ANDERSON MARTINS MARQUES", "cpf": "***.887.218-**"},
    {"posicao": 49, "nome": "Nicole Janine Bolzani Oliveira", "cpf": "***.303.578-**"},
    {"posicao": 50, "nome": "Emilly Raissa de Almeida de Moraes", "cpf": "***.623.028-**"},
    {"posicao": 51, "nome": "GABRIELLI RAMOS DA SILVA", "cpf": "***.163.158-**"},
    {"posicao": 52, "nome": "Felipe dos Reis Antunes", "cpf": "***.029.988-**"},
    {"posicao": 53, "nome": "João Pedro de Oliveira Ferreira", "cpf": "***.339.708-**"},
    {"posicao": 54, "nome": "PEDRO HENRIQUE MOURA CAYUELLA", "cpf": "***.970.818-**"},
    {"posicao": 55, "nome": "Marina Silveira Toledo", "cpf": "***.003.218-**"},
    {"posicao": 56, "nome": "CESAR HENRIQUE CAMARGO DOS SANTOS", "cpf": "***.590.078-**"},
    {"posicao": 57, "nome": "CAIQUE ALEXANDRE DE OLIVEIRA", "cpf": "***.362.908-**"},
    {"posicao": 58, "nome": "PRISCILA NORONHA MENDES", "cpf": "***.687.188-**"},
    {"posicao": 59, "nome": "JULIO CESAR VIEIRA", "cpf": "***.910.948-**"},
    {"posicao": 60, "nome": "IRENE DE CAMPOS PERILLO", "cpf": "***.970.888-**"},
    {"posicao": 61, "nome": "FERNANDA TERESA CORREA DA SILV", "cpf": "***.570.758-**"},
    {"posicao": 62, "nome": "MATHEUS BUENO SIRILO", "cpf": "***.296.028-**"},
    {"posicao": 63, "nome": "BRUNA FAVA PIRES", "cpf": "***.915.848-**"},
    {"posicao": 64, "nome": "Enzo Lian Pinheiro Mendes", "cpf": "***.139.548-**"},
    {"posicao": 65, "nome": "Douglas Rafael de Sousa Mendes", "cpf": "***.372.248-**"},
    {"posicao": 66, "nome": "Herivelton Henrique Gonçalves", "cpf": "***.607.418-**"},
    {"posicao": 67, "nome": "FULVIO DE PAULA LIMA", "cpf": "***.152.758-**"},
    {"posicao": 68, "nome": "ALESSANDRO RODRIGUES MELO FO", "cpf": "***.118.258-**"},
    {"posicao": 69, "nome": "Camila Martins Queiroz", "cpf": "***.530.648-**"},
    {"posicao": 70, "nome": "Guilherme Oto Venturelli", "cpf": "***.979.058-**"},
    {"posicao": 71, "nome": "Flávia Alvarenga Sartori", "cpf": "***.695.758-**"},
    {"posicao": 72, "nome": "Gislaine Oliviera Takushi", "cpf": "***.891.438-**"},
    {"posicao": 73, "nome": "Julia Tiemi Vasques Bandeira", "cpf": "***.020.448-**"},
    {"posicao": 74, "nome": "JULIA MARIA JUBAT ALVES DOS SANTOS", "cpf": "***.363.038-**"},
    {"posicao": 75, "nome": "Carolina Gomes de Oliveira", "cpf": "***.232.598-**"},
    {"posicao": 76, "nome": "CAIO FERNANDO SCUDELER", "cpf": "***.909.568-**"},
    {"posicao": 77, "nome": "MIGUEL DOS SANTOS GUSSI", "cpf": "***.539.148-**"},
    {"posicao": 78, "nome": "Renata Martins", "cpf": "***.600.208-**"},
    {"posicao": 79, "nome": "DANILO DE OLIVERIA BARROSO", "cpf": "***.127.178-**"},
    {"posicao": 80, "nome": "DANIEL JOSE BERNARDES FILHO", "cpf": "***.229.748-**"},
    {"posicao": 81, "nome": "CICERA MARIA C DE OLIVEIRA", "cpf": "***.043.138-**"},
    {"posicao": 82, "nome": "Eric Rodrigues Berto", "cpf": "***.036.498-**"},
    {"posicao": 83, "nome": "Eduardo Alves Taveira", "cpf": "***.396.148-**"}
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
