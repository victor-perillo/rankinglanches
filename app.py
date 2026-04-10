import streamlit as st

# 1. Configuração da página
st.set_page_config(
    page_title="Consulta de Ranking", 
    page_icon="🍔", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# 2. Estilização Customizada (CSS)
s/* No seu código, altere este bloco específico dentro da tag <style> */

#/* Caracteristicas do botão
.stButton {
    display: flex;
    justify-content: center;
    width: 100%;
}

.stButton>button {
    background-color: #8A05BE;
    color: white;
    border-radius: 12px;
    width: 60%;         /* DEFINE A LARGURA (ex: 60% da tela) */
    min-width: 200px;  /* Garante uma largura mínima */
    height: 55px;       /* Mantém uma boa altura */
    padding: 0px;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
    font-size: 18px;    /* Aumenta a fonte para combinar */
    margin: 20px auto;  /* Espaço em cima e centraliza */
}
    
    /* Padronização dos Botões */
    .stButton>button {
        background-color: #8A05BE;
        color: white;
        border-radius: 12px;
        width: 100%;
        height: 60px;
        padding: 0px;
        font-weight: bold;
        border: none;
        transition: 0.3s ease;
        font-size: 20px;
        margin-top: 5px;
    }
    .stButton>button:hover {
        background-color: #700499;
        color: white;
        border: none;
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

    .podio-label {
        font-size: 12px;
        text-transform: uppercase;
        font-weight: bold;
        margin-bottom: 2px;
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

# 3. Banco de Dados (Corrigido e Completo)
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
    {'posicao': 51, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 52, 'nome': 'GUSTAVO H O LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 53, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 54, 'nome': 'NÍCOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 55, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 56, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 57, 'nome': 'LUCAS VINICIOS CONSANI', 'cpf': '***.809.228-**'},
    {'posicao': 58, 'nome': 'JULIA MARIA JUBAT ALVES DOS SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 59, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 60, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 61, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 62, 'nome': 'NICOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 63, 'nome': 'NICOLE JANINE BOLZANI OLIVEIRA', 'cpf': '***.303.578-**'},
    {'posicao': 64, 'nome': 'MAYARA SOUZA BARROS', 'cpf': '***.545.948-**'},
    {'posicao': 65, 'nome': 'JOÃO VITOR DE CAMARGO BARROS', 'cpf': '***.513.388-**'},
    {'posicao': 66, 'nome': 'LAURA DE ALMEIDA FOGAÇA', 'cpf': '***.329.568-**'},
    {'posicao': 67, 'nome': 'THIAGO HENRIQUE MUNIZ NEVES', 'cpf': '***.276.608-**'},
    {'posicao': 68, 'nome': 'PEDRO VALADARES JUNIOR', 'cpf': '***.076.153-**'},
    {'posicao': 69, 'nome': 'PEDRO ARTHUR DE OLIVEIRA', 'cpf': '***.415.258-**'},
    {'posicao': 70, 'nome': 'LUCAS SILVA PERES', 'cpf': '***.249.118-**'},
    {'posicao': 71, 'nome': 'MARCOS UNO', 'cpf': '***.673.268-**'},
    {'posicao': 72, 'nome': 'EBER TEIXEIRA CALADO', 'cpf': '***.976.838-**'},
    {'posicao': 73, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 74, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 75, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 76, 'nome': 'BIANCA PICHIRILO VERGUEIRO BENATTI', 'cpf': '***.498.018-**'},
    {'posicao': 77, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 78, 'nome': 'HERIVELTON HENRIQUE GONÇALVES', 'cpf': '***.607.418-**'},
    {'posicao': 79, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 80, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 81, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 82, 'nome': 'MICHAEL MARQUES VIEIRA DE SOUZA', 'cpf': '***.340.948-**'},
    {'posicao': 83, 'nome': 'VINICIUS GAMA DE FRANCA', 'cpf': '***.358.148-**'},
    {'posicao': 84, 'nome': 'CAUE POLIZELI CAMARGO', 'cpf': '***.808.628-**'},
    {'posicao': 85, 'nome': 'FLÁVIA ALVARENGA SARTORI', 'cpf': '***.695.758-**'},
    {'posicao': 86, 'nome': 'KELVIN CORRÊA', 'cpf': '***.649.488-**'},
    {'posicao': 87, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 88, 'nome': 'MARCEL MONTEIRO BALDUINO', 'cpf': '***.801.468-**'},
    {'posicao': 89, 'nome': 'ALLAN WANDREY QUEIROZ', 'cpf': '***.395.008-**'},
    {'posicao': 90, 'nome': 'DANIELI FERREIRA DE JESUS', 'cpf': '***.932.848-**'},
    {'posicao': 91, 'nome': 'EDSON VITOR PALDINI', 'cpf': '***.907.508-**'},
    {'posicao': 92, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 93, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 94, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 95, 'nome': 'CICERA MARIA C DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 96, 'nome': 'GABRIEL FERREIRA DOS SANTOS', 'cpf': '***.779.118-**'},
    {'posicao': 97, 'nome': 'PAULO VITOR LEMES', 'cpf': '***.781.688-**'},
    {'posicao': 98, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 99, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 100, 'nome': 'SABRINA SANT ANA DA SILVA ALVES', 'cpf': '***.844.038-**'},
    {'posicao': 101, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 102, 'nome': 'PEDRO ALBERTTE DO CARMO NETO', 'cpf': '***.598.478-**'},
    {'posicao': 103, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 104, 'nome': 'PAULO CESAR LOPES SILVA', 'cpf': '***.109.188-**'},
    {'posicao': 105, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 106, 'nome': 'GUSTAVO HENRIQUE DOS REIS', 'cpf': '***.655.028-**'},
    {'posicao': 107, 'nome': 'MARCO TULIO DUENAS', 'cpf': '***.415.798-**'},
    {'posicao': 108, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 109, 'nome': 'CLELIA DE JESUS QUEIROZ MOTTA', 'cpf': '***.071.678-**'},
    {'posicao': 110, 'nome': 'NICOLE FAVA PIRES', 'cpf': '***.051.518-**'},
    {'posicao': 111, 'nome': 'FELIPE VINICIUS GONCALVES DOS REIS', 'cpf': '***.616.758-**'},
    {'posicao': 112, 'nome': 'ANA BEATRIZ CONCEICAO APARECIDA CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 113, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 114, 'nome': 'LISANDRA FERNANDA DE GODOI', 'cpf': '***.048.668-**'},
    {'posicao': 115, 'nome': 'JONATAS SILVEIRA DA VARGEM', 'cpf': '***.451.678-**'},
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

# Linha de botões padronizada
c_btn1, c_btn2, c_btn3 = st.columns([0.5, 2, 0.5])

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
