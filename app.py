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

# 3. Banco de Dados Completo (Ranking Consolidado: 01/03 a 19/03)
# Atualizado com base no extrato CSV processado.
# 3. Banco de Dados Completo (Ranking Consolidado: 01/03 a 23/03)
# Removidos: Familiares conforme solicitado.
# Total de registros: 97
ranking_db = ranking_db = ranking_db = [
    {'posicao': 1, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 2, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 3, 'nome': 'FLÁVIA CAMARGO CAMPOS', 'cpf': '***.900.098-**'},
    {'posicao': 4, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 5, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 6, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 7, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 8, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 9, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 10, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 11, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 12, 'nome': 'MATEUS F ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 13, 'nome': 'ANDERSON MARTINS MARQUES', 'cpf': '***.887.218-**'},
    {'posicao': 14, 'nome': 'THIAGO HENRIQUE MUNIZ NEVES', 'cpf': '***.276.608-**'},
    {'posicao': 15, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 16, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 17, 'nome': 'JOAO VICTOR ALCANTARA AZEVEDO', 'cpf': '***.739.108-**'},
    {'posicao': 18, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 19, 'nome': 'DANIEL RODRIGUES LOPES ADEJARBAS', 'cpf': '***.276.508-**'},
    {'posicao': 20, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 21, 'nome': 'EMANUEL MEDEIROS ROSA', 'cpf': '***.521.808-**'},
    {'posicao': 22, 'nome': 'MARCOS UNO', 'cpf': '***.673.268-**'},
    {'posicao': 23, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 24, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 25, 'nome': 'MATHEUS AUGUSTO SANTOS GUEFF', 'cpf': '***.498.128-**'},
    {'posicao': 26, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 27, 'nome': 'FÁBIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 28, 'nome': 'ALESSANDRO RODRIGUES MELO FO', 'cpf': '***.118.258-**'},
    {'posicao': 29, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 30, 'nome': 'VINICIUS GAMA DE FRANCA', 'cpf': '***.358.148-**'},
    {'posicao': 31, 'nome': 'BRENDA BIRAL BATISTA', 'cpf': '***.430.818-**'},
    {'posicao': 32, 'nome': 'TIAGO ALVES SIMOES', 'cpf': '***.528.818-**'},
    {'posicao': 33, 'nome': 'SAMIRA TAMER', 'cpf': '***.086.048-**'},
    {'posicao': 34, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 35, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 36, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 37, 'nome': 'LAURA DA SILVA SEGANTIN', 'cpf': '***.300.358-**'},
    {'posicao': 38, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 39, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 40, 'nome': 'CICERA MARIA C DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 41, 'nome': 'JULIANA ALVES DORIGAO', 'cpf': '***.755.028-**'},
    {'posicao': 42, 'nome': 'PAULO VITOR LEMES', 'cpf': '***.781.688-**'},
    {'posicao': 43, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 44, 'nome': 'PRISCILA NORONHA MENDES', 'cpf': '***.687.188-**'},
    {'posicao': 45, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 46, 'nome': 'HERIVELTON HENRIQUE GONÇALVES', 'cpf': '***.607.418-**'},
    {'posicao': 47, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 48, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 49, 'nome': 'LEANDRO TEODORO POLERA', 'cpf': '***.565.548-**'},
    {'posicao': 50, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 51, 'nome': 'ROBSON MENDES VIANA', 'cpf': '***.020.348-**'},
    {'posicao': 52, 'nome': 'SOPHIA CASTILHO MORENO', 'cpf': '***.497.218-**'},
    {'posicao': 53, 'nome': 'RICARDO HERNAN SARAVIA SIQUEIRA', 'cpf': '***.988.378-**'},
    {'posicao': 54, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 55, 'nome': 'GILBERTO DE OLIVEIRA SANTOS', 'cpf': '***.649.528-**'},
    {'posicao': 56, 'nome': 'MILENA MOURA DE SOUZA', 'cpf': '***.470.138-**'},
    {'posicao': 57, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 58, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 59, 'nome': 'ENZO LIAN PINHEIRO MENDES', 'cpf': '***.139.548-**'},
    {'posicao': 60, 'nome': 'LORENA CRISTINA CASSIANO', 'cpf': '***.493.518-**'},
    {'posicao': 61, 'nome': 'EDUARDO APARECIDO DE CARVALHO', 'cpf': '***.821.918-**'},
    {'posicao': 62, 'nome': 'DILZE DUARTE ARAUJO', 'cpf': '***.929.438-**'},
    {'posicao': 63, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 64, 'nome': 'KAWAN FERNANDES DE ARAUJO', 'cpf': '***.099.108-**'},
    {'posicao': 65, 'nome': 'GISLAINE OLIVIERA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 66, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 67, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 68, 'nome': 'MICHAEL MARQUES VIEIRA DE SOUZA', 'cpf': '***.340.948-**'},
    {'posicao': 69, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 70, 'nome': 'DANIELI FERREIRA DE JESUS', 'cpf': '***.932.848-**'},
    {'posicao': 71, 'nome': 'JOAO PEDRO DRUZIAN FERREIRA', 'cpf': '***.484.748-**'},
    {'posicao': 72, 'nome': 'MARINA SILVEIRA TOLEDO', 'cpf': '***.003.218-**'},
    {'posicao': 73, 'nome': 'GUSTAVO DE CAMPOS ANTUNES', 'cpf': '***.326.288-**'},
    {'posicao': 74, 'nome': 'DANILO DE OLIVERIA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 75, 'nome': 'BRENO JOSE DA SILVA', 'cpf': '***.182.118-**'},
    {'posicao': 76, 'nome': 'FABRICIO REIS ANTUNES', 'cpf': '***.785.958-**'},
    {'posicao': 77, 'nome': 'NICOLE JANINE BOLZANI OLIVEIRA', 'cpf': '***.303.578-**'},
    {'posicao': 78, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 79, 'nome': 'LUCAS PIRES DE ALMEIDA', 'cpf': '***.223.318-**'},
    {'posicao': 80, 'nome': 'ELIOENAI CACERES PEREIRA', 'cpf': '***.496.738-**'},
    {'posicao': 81, 'nome': 'TIAGO AUGUSTO PEDROSO DE CARVALHO', 'cpf': '***.333.798-**'},
    {'posicao': 82, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 83, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 84, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 85, 'nome': 'FABIO AUGUSTO DE CASTRO MORAES', 'cpf': '***.121.458-**'},
    {'posicao': 86, 'nome': 'DANILO ALBERTO DA SILVA FERNANDES', 'cpf': '***.555.889-**'},
    {'posicao': 87, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 88, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 89, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 90, 'nome': 'AMADOR BUENO DE OLIVEIRA NETO', 'cpf': '***.548.238-**'},
    {'posicao': 91, 'nome': 'ALISON FERNANDES SANTOS', 'cpf': '***.715.938-**'},
    {'posicao': 92, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 93, 'nome': 'CESAR HENRIQUE CAMARGO DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 94, 'nome': 'CAMILA MARTINS QUEIROZ', 'cpf': '***.530.648-**'},
    {'posicao': 95, 'nome': 'CLAYTON FIGUEIREDO MAIA', 'cpf': '***.848.728-**'},
    {'posicao': 96, 'nome': 'ALISON CARRIEL ROCHA', 'cpf': '***.626.128-**'},
    {'posicao': 97, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 98, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 99, 'nome': 'FERNANDA TERESA CORREA DA SILV', 'cpf': '***.570.758-**'},
    {'posicao': 100, 'nome': 'GABRIEL CASTILHO MEDEIROS DE SOUZA', 'cpf': '***.364.088-**'},
    {'posicao': 101, 'nome': 'DOUGLAS RAFAEL DE SOUSA MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 102, 'nome': 'ENIO APARECIDO DA SILVA', 'cpf': '***.696.198-**'},
    {'posicao': 103, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 104, 'nome': 'PAULO CESAR LOPES SILVA', 'cpf': '***.109.188-**'},
    {'posicao': 105, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 106, 'nome': 'MAICON RODRIGUES DOS SANTOS', 'cpf': '***.396.118-**'},
    {'posicao': 107, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 108, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 109, 'nome': 'NÍCOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 110, 'nome': 'KELVIN CORRÊA', 'cpf': '***.649.488-**'},
    {'posicao': 111, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 112, 'nome': 'SABRINA CARNEIRO RODRIGUES', 'cpf': '***.167.588-**'},
    {'posicao': 113, 'nome': 'GABRIEL CANDIDO CORREA', 'cpf': '***.160.028-**'},
    {'posicao': 114, 'nome': 'JONATHAN ANDREW ALVES GARCIA', 'cpf': '***.133.298-**'},
    {'posicao': 115, 'nome': 'GUILHERME TOBIAS PIVA', 'cpf': '***.719.958-**'},
    {'posicao': 116, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 117, 'nome': 'IAGO YURI ROSSAN', 'cpf': '***.414.088-**'},
    {'posicao': 118, 'nome': 'JULIANA MACHADO RIBEIRO ANANIAS', 'cpf': '***.945.278-**'},
    {'posicao': 119, 'nome': 'KARLOS INACIO DA SILVA', 'cpf': '***.430.194-**'},
    {'posicao': 120, 'nome': 'FELIPE HASHIMOTO FENGLER', 'cpf': '***.139.658-**'},
    {'posicao': 121, 'nome': 'KARINA BRUNO DE OLIVEIRA', 'cpf': '***.900.288-**'},
    {'posicao': 122, 'nome': 'FLÁVIA ALVARENGA SARTORI', 'cpf': '***.695.758-**'},
    {'posicao': 123, 'nome': 'MATEUS CARDOSO PIRES', 'cpf': '***.179.968-**'},
    {'posicao': 124, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 125, 'nome': 'LUCAS VINICIOS CONSANI', 'cpf': '***.809.228-**'},
    {'posicao': 126, 'nome': 'JULIA MARIA JUBAT ALVES DOS SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 127, 'nome': 'BEATRIZ CORTEZ SIQUEIRA', 'cpf': '***.175.134-**'},
    {'posicao': 128, 'nome': 'NICOLAS KATSUJI NAGANO', 'cpf': '***.156.448-**'},
    {'posicao': 129, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 130, 'nome': 'JEFFERSON PADILHA LUZ', 'cpf': '***.267.028-**'},
    {'posicao': 131, 'nome': 'MATEUS FERNANDO XAVIER MARIANO', 'cpf': '***.903.418-**'},
    {'posicao': 132, 'nome': 'FREDERICO HASEGAWA COPELI VENA', 'cpf': '***.878.578-**'},
    {'posicao': 133, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 134, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 135, 'nome': 'GABRIEL PEDROSO DE GOES VIEIRA', 'cpf': '***.869.898-**'},
    {'posicao': 136, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 137, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 138, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 139, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 140, 'nome': 'GABRIEL RIBEIRO CORREA', 'cpf': '***.092.198-**'},
    {'posicao': 141, 'nome': 'CAUA FLORENTINO RUFINO', 'cpf': '***.837.778-**'},
    {'posicao': 142, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 143, 'nome': 'LUIZ GUSTAVO OBARA DA SILVA', 'cpf': '***.687.008-**'},
    {'posicao': 144, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 145, 'nome': 'RENATA MARTINS', 'cpf': '***.600.208-**'},
    {'posicao': 146, 'nome': 'PEDRO ALBERTTE CARMO NT', 'cpf': '***.598.478-**'},
    {'posicao': 147, 'nome': 'ANTONIO GABRIEL LIMA DE JESUS', 'cpf': '***.804.718-**'},
    {'posicao': 148, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 149, 'nome': 'WENDEL AUGUSTO LOPES VASCO', 'cpf': '***.598.038-**'},
    {'posicao': 150, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 151, 'nome': 'BRUNO HENRIQUE RODRIGUES DA SILVA', 'cpf': '***.832.928-**'},
    {'posicao': 152, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 153, 'nome': 'DANIEL JOSE BERNARDES FILHO', 'cpf': '***.229.748-**'},
    {'posicao': 154, 'nome': 'EDUARDO ALBERTO VIEIRA', 'cpf': '***.724.998-**'},
    {'posicao': 155, 'nome': 'JOAO MARCELO AZEVEDO FERRAZ ROSA', 'cpf': '***.906.836-**'},
    {'posicao': 156, 'nome': 'FABIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 157, 'nome': 'EDUARDO ALVES TAVEIRA', 'cpf': '***.396.148-**'},
    {'posicao': 158, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 159, 'nome': 'PEDRO SILVA MARTINS', 'cpf': '***.245.268-**'},
    {'posicao': 160, 'nome': 'SANDRA MARIA DE SOUSA SALINAS', 'cpf': '***.148.401-**'}
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
        Atualizado em 26/03/2026<br>
        <strong>Final da promoção: 31/03/2026</strong>
    </div>
""", unsafe_allow_html=True)
