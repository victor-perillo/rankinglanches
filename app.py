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
    
    .stButton>button {
        background-color: #8A05BE;
        color: white;
        border-radius: 12px;
        width: 100%;
        padding: 10px;
        font-weight: bold;
        border: none;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #700499;
        color: white;
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

# 3. Banco de Dados (Ranking Consolidado)
ranking_db = [
    {'posicao': 1, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 2, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 3, 'nome': 'FLÁVIA CAMARGO CAMPOS', 'cpf': '***.900.098-**'},
    {'posicao': 4, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 5, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 6, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 7, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 8, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 9, 'nome': 'ANDERSON MARTINS MARQUES', 'cpf': '***.887.218-**'},
    {'posicao': 10, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 11, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 12, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 13, 'nome': 'LEANDRO MARTINES SILVA', 'cpf': '***.187.558-**'},
    {'posicao': 14, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 15, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 16, 'nome': 'MATEUS F ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 17, 'nome': 'THIAGO HENRIQUE MUNIZ NEVES', 'cpf': '***.276.608-**'},
    {'posicao': 18, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 19, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 20, 'nome': 'JOAO VICTOR ALCANTARA AZEVEDO', 'cpf': '***.739.108-**'},
    {'posicao': 21, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 22, 'nome': 'DANIEL RODRIGUES LOPES ADEJARBAS', 'cpf': '***.276.508-**'},
    {'posicao': 23, 'nome': 'EMANUEL MEDEIROS ROSA', 'cpf': '***.521.808-**'},
    {'posicao': 24, 'nome': 'MARCOS UNO', 'cpf': '***.673.268-**'},
    {'posicao': 25, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 26, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 27, 'nome': 'MATHEUS AUGUSTO SANTOS GUEFF', 'cpf': '***.498.128-**'},
    {'posicao': 28, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 29, 'nome': 'FÁBIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 30, 'nome': 'ALESSANDRO RODRIGUES MELO FO', 'cpf': '***.118.258-**'},
    {'posicao': 31, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 32, 'nome': 'TIAGO ALVES SIMOES', 'cpf': '***.528.818-**'},
    {'posicao': 33, 'nome': 'VINICIUS GAMA DE FRANCA', 'cpf': '***.358.148-**'},
    {'posicao': 34, 'nome': 'SAMIRA TAMER', 'cpf': '***.086.048-**'},
    {'posicao': 35, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 36, 'nome': 'BRENDA BIRAL BATISTA', 'cpf': '***.430.818-**'},
    {'posicao': 37, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 38, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 39, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 40, 'nome': 'LAURA DA SILVA SEGANTIN', 'cpf': '***.300.358-**'},
    {'posicao': 41, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 42, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 43, 'nome': 'CICERA MARIA C DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 44, 'nome': 'JULIANA ALVES DORIGAO', 'cpf': '***.755.028-**'},
    {'posicao': 45, 'nome': 'PAULO VITOR LEMES', 'cpf': '***.781.688-**'},
    {'posicao': 46, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 47, 'nome': 'FABRICIO REIS ANTUNES', 'cpf': '***.785.958-**'},
    {'posicao': 48, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 49, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 50, 'nome': 'PRISCILA NORONHA MENDES', 'cpf': '***.687.188-**'},
    {'posicao': 51, 'nome': 'NICOLE JANINE BOLZANI OLIVEIRA', 'cpf': '***.303.578-**'},
    {'posicao': 52, 'nome': 'RICARDO HERNAN SARAVIA SIQUEIRA', 'cpf': '***.988.378-**'},
    {'posicao': 53, 'nome': 'SOPHIA CASTILHO MORENO', 'cpf': '***.497.218-**'},
    {'posicao': 54, 'nome': 'MILENA MOURA DE SOUZA', 'cpf': '***.470.138-**'},
    {'posicao': 55, 'nome': 'ROBSON MENDES VIANA', 'cpf': '***.020.348-**'},
    {'posicao': 56, 'nome': 'ENZO LIAN PINHEIRO MENDES', 'cpf': '***.139.548-**'},
    {'posicao': 57, 'nome': 'GILBERTO DE OLIVEIRA SANTOS', 'cpf': '***.649.528-**'},
    {'posicao': 58, 'nome': 'LEANDRO TEODORO POLERA', 'cpf': '***.565.548-**'},
    {'posicao': 59, 'nome': 'HERIVELTON HENRIQUE GONÇALVES', 'cpf': '***.607.418-**'},
    {'posicao': 60, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 61, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 62, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 63, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 64, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 65, 'nome': 'PRISCILA S K CORREA', 'cpf': '***.553.718-**'},
    {'posicao': 66, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 67, 'nome': 'LORENA CRISTINA CASSIANO', 'cpf': '***.493.518-**'},
    {'posicao': 68, 'nome': 'EDUARDO APARECIDO DE CARVALHO', 'cpf': '***.821.918-**'},
    {'posicao': 69, 'nome': 'DILZE DUARTE ARAUJO', 'cpf': '***.929.438-**'},
    {'posicao': 70, 'nome': 'GISLAINE OLIVIERA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 71, 'nome': 'TATIANY BITENER MARTINES', 'cpf': '***.747.158-**'},
    {'posicao': 72, 'nome': 'PEDRO ARTHUR DE OLIVEIRA', 'cpf': '***.415.258-**'},
    {'posicao': 73, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 74, 'nome': 'KAWAN FERNANDES DE ARAUJO', 'cpf': '***.099.108-**'},
    {'posicao': 75, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 76, 'nome': 'DANILO DE OLIVERIA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 77, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 78, 'nome': 'MICHAEL MARQUES VIEIRA DE SOUZA', 'cpf': '***.340.948-**'},
    {'posicao': 79, 'nome': 'GUSTAVO DE CAMPOS ANTUNES', 'cpf': '***.326.288-**'},
    {'posicao': 80, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 81, 'nome': 'DANIELI FERREIRA DE JESUS', 'cpf': '***.932.848-**'},
    {'posicao': 82, 'nome': 'MARINA SILVEIRA TOLEDO', 'cpf': '***.003.218-**'},
    {'posicao': 83, 'nome': 'JOAO PEDRO DRUZIAN FERREIRA', 'cpf': '***.484.748-**'},
    {'posicao': 84, 'nome': 'BRENO JOSE DA SILVA', 'cpf': '***.182.118-**'},
    {'posicao': 85, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 86, 'nome': 'LUCAS PIRES DE ALMEIDA', 'cpf': '***.223.318-**'},
    {'posicao': 87, 'nome': 'TIAGO AUGUSTO PEDROSO DE CARVALHO', 'cpf': '***.333.798-**'},
    {'posicao': 88, 'nome': 'ELIOENAI CACERES PEREIRA', 'cpf': '***.496.738-**'},
    {'posicao': 89, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 90, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 91, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 92, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 93, 'nome': 'FABIO AUGUSTO DE CASTRO MORAES', 'cpf': '***.121.458-**'},
    {'posicao': 94, 'nome': 'DANILO ALBERTO DA SILVA FERNANDES', 'cpf': '***.555.889-**'},
    {'posicao': 95, 'nome': 'AMADOR BUENO DE OLIVEIRA NETO', 'cpf': '***.548.238-**'},
    {'posicao': 96, 'nome': 'ALISON CARRIEL ROCHA', 'cpf': '***.626.128-**'},
    {'posicao': 97, 'nome': 'ALISON FERNANDES SANTOS', 'cpf': '***.715.938-**'},
    {'posicao': 98, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 99, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 100, 'nome': 'CLAYTON FIGUEIREDO MAIA', 'cpf': '***.848.728-**'},
    {'posicao': 101, 'nome': 'CAMILA MARTINS QUEIROZ', 'cpf': '***.530.648-**'},
    {'posicao': 102, 'nome': 'DOUGLAS RAFAEL DE SOUSA MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 103, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 104, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 105, 'nome': 'CESAR HENRIQUE CAMARGO DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 106, 'nome': 'SABRINA CARNEIRO RODRIGUES', 'cpf': '***.167.588-**'},
    {'posicao': 107, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 108, 'nome': 'GABRIEL CANDIDO CORREA', 'cpf': '***.160.028-**'},
    {'posicao': 109, 'nome': 'GABRIEL CASTILHO MEDEIROS DE SOUZA', 'cpf': '***.364.088-**'},
    {'posicao': 110, 'nome': 'FELIPE HASHIMOTO FENGLER', 'cpf': '***.139.658-**'},
    {'posicao': 111, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 112, 'nome': 'FERNANDA TERESA CORREA DA SILV', 'cpf': '***.570.758-**'},
    {'posicao': 113, 'nome': 'KARINA BRUNO DE OLIVEIRA', 'cpf': '***.900.288-**'},
    {'posicao': 114, 'nome': 'JULIANA MACHADO RIBEIRO ANANIAS', 'cpf': '***.945.278-**'},
    {'posicao': 115, 'nome': 'KARLOS INACIO DA SILVA', 'cpf': '***.430.194-**'},
    {'posicao': 116, 'nome': 'MAICON RODRIGUES DOS SANTOS', 'cpf': '***.396.118-**'},
    {'posicao': 117, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 118, 'nome': 'PATRICIA CARDELI', 'cpf': '***.366.018-**'},
    {'posicao': 119, 'nome': 'NÍCOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 120, 'nome': 'PAULO CESAR LOPES SILVA', 'cpf': '***.109.188-**'},
    {'posicao': 121, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 122, 'nome': 'ENIO APARECIDO DA SILVA', 'cpf': '***.696.198-**'},
    {'posicao': 123, 'nome': 'KELVIN CORRÊA', 'cpf': '***.649.488-**'},
    {'posicao': 124, 'nome': 'IAGO YURI ROSSAN', 'cpf': '***.414.088-**'},
    {'posicao': 125, 'nome': 'GUILHERME TOBIAS PIVA', 'cpf': '***.719.958-**'},
    {'posicao': 126, 'nome': 'JONATHAN ANDREW ALVES GARCIA', 'cpf': '***.133.298-**'},
    {'posicao': 127, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 128, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 129, 'nome': 'LUCAS VINICIOS CONSANI', 'cpf': '***.809.228-**'},
    {'posicao': 130, 'nome': 'FLÁVIA ALVARENGA SARTORI', 'cpf': '***.695.758-**'},
    {'posicao': 131, 'nome': 'BEATRIZ CORTEZ SIQUEIRA', 'cpf': '***.175.134-**'},
    {'posicao': 132, 'nome': 'MATEUS CARDOSO PIRES', 'cpf': '***.179.968-**'},
    {'posicao': 133, 'nome': 'NICOLAS KATSUJI NAGANO', 'cpf': '***.156.448-**'},
    {'posicao': 134, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 135, 'nome': 'JULIA MARIA JUBAT ALVES DOS SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 136, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 137, 'nome': 'PEDRO ALBERTTE DO CARMO NETO', 'cpf': '***.598.478-**'},
    {'posicao': 138, 'nome': 'JEFFERSON PADILHA LUZ', 'cpf': '***.267.028-**'},
    {'posicao': 139, 'nome': 'MATHEUS FRANCISCO ALVES', 'cpf': '***.682.298-**'},
    {'posicao': 140, 'nome': 'MATEUS FERNANDO XAVIER MARIANO', 'cpf': '***.903.418-**'},
    {'posicao': 141, 'nome': 'FREDERICO HASEGAWA COPELI VENA', 'cpf': '***.878.578-**'},
    {'posicao': 142, 'nome': 'GABRIEL PEDROSO DE GOES VIEIRA', 'cpf': '***.869.898-**'},
    {'posicao': 143, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 144, 'nome': 'MARIA EDUARDA MORENO LOPES', 'cpf': '***.335.888-**'},
    {'posicao': 145, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 146, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 147, 'nome': 'GABRIEL RIBEIRO CORREA', 'cpf': '***.092.198-**'},
    {'posicao': 148, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 149, 'nome': 'CAUA FLORENTINO RUFINO', 'cpf': '***.837.778-**'},
    {'posicao': 150, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 151, 'nome': 'LUIZ GUSTAVO OBARA DA SILVA', 'cpf': '***.687.008-**'},
    {'posicao': 152, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 153, 'nome': 'ANTONIO GABRIEL LIMA DE JESUS', 'cpf': '***.804.718-**'},
    {'posicao': 154, 'nome': 'WENDEL AUGUSTO LOPES VASCO', 'cpf': '***.598.038-**'},
    {'posicao': 155, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 156, 'nome': 'PEDRO ALBERTTE CARMO NT', 'cpf': '***.598.478-**'},
    {'posicao': 157, 'nome': 'RENATA MARTINS', 'cpf': '***.600.208-**'},
    {'posicao': 158, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 159, 'nome': 'BRUNO HENRIQUE RODRIGUES DA SILVA', 'cpf': '***.832.928-**'},
    {'posicao': 160, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 161, 'nome': 'DANIEL JOSE BERNARDES FILHO', 'cpf': '***.229.748-**'},
    {'posicao': 162, 'nome': 'JOAO MARCELO AZEVEDO FERRAZ ROSA', 'cpf': '***.906.836-**'},
    {'posicao': 163, 'nome': 'EDUARDO ALBERTO VIEIRA', 'cpf': '***.724.998-**'},
    {'posicao': 164, 'nome': 'EDUARDO ALVES TAVEIRA', 'cpf': '***.396.148-**'},
    {'posicao': 165, 'nome': 'FABIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 166, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 167, 'nome': 'PEDRO SILVA MARTINS', 'cpf': '***.245.268-**'},
    {'posicao': 168, 'nome': 'SABRINA SANT ANA DA SILVA ALVES', 'cpf': '***.844.038-**'},
    {'posicao': 169, 'nome': 'SANDRA MARIA DE SOUSA SALINAS', 'cpf': '***.148.401-**'}
]

# 4. Construção da Interface
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    try:
        # Se você tiver a logo.jpg, ele exibe. Se não, exibe o texto abaixo.
        st.image("logo.jpg", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center;'>🍔 Promoção</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #333; margin-bottom: 25px;'>Consulta de Ranking</h2>", unsafe_allow_html=True)

# Campo de texto
nome_busca = st.text_input("", placeholder="Insira seu nome completo...")

# Botões de Ação
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    col_btn_a, col_btn_b = st.columns(2)
    with col_btn_a:
        botao_busca = st.button("Buscar")
    with col_btn_b:
        botao_resultados = st.button("Ganhadores")

# --- LÓGICA 1: BOTÃO GANHADORES (1º e 2º) ---
if botao_resultados:
    st.markdown("### 🏆 Top 2 Liderança")
    vencedores = [u for u in ranking_db if u['posicao'] in [1, 2]]
    for v in vencedores:
        cor = "#FFD700" if v['posicao'] == 1 else "#C0C0C0"
        medalha = "🥇" if v['posicao'] == 1 else "🥈"
        st.markdown(f"""
            <div class="resultado-card" style="border-left: 8px solid {cor};">
                <div class="podio-label" style="color: {cor};">{medalha} {v['posicao']}º LUGAR</div>
                <p style="margin: 0; font-size: 18px;"><strong>{v['nome']}</strong></p>
                <p style="margin: 0; color: #666; font-size: 14px;">CPF: {v['cpf']}</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("---")

# --- LÓGICA 2: BUSCA INDIVIDUAL ---
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
                        <p style="margin: 10px 0 0 0;">Sua Posição: <span class="destaque">{p['posicao']}º lugar</span></p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Nome não encontrado no ranking.")

# 5. Rodapé Informativo
st.markdown("""
    <div class="footer-text">
        Atualizado em 30/03/2026<br>
        <strong>Final da promoção: 31/03/2026</strong>
    </div>
""", unsafe_allow_html=True)
