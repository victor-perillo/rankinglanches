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

    div.stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
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
    
    .stColumn div.stButton > button {
        height: 45px !important;
        font-size: 16px !important;
        margin-top: 0px !important;
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

# 3. Banco de Dados (CORRIGIDO)
ranking_db = [
    {'posicao': 1, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 2, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 3, 'nome': 'ELIOENAI CACERES PEREIRA', 'cpf': '***.496.738-**'},
    {'posicao': 4, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 5, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 6, 'nome': 'WILTON ROGÉRIO DA COSTA PEREIRA', 'cpf': '***.922.138-**'},
    {'posicao': 7, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 8, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 9, 'nome': 'VINICIUS GAMA DE FRANCA', 'cpf': '***.358.148-**'},
    {'posicao': 10, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 11, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 12, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 13, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 14, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 15, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 16, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 17, 'nome': 'TIAGO ALVES SIMOES', 'cpf': '***.528.818-**'},
    {'posicao': 18, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 19, 'nome': 'CRISTIANE ANTUNES DE OLIVEIRA DA SILVA', 'cpf': '***.916.068-**'},
    {'posicao': 20, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 21, 'nome': 'FREDERICO HASEGAWA COPELI VENA', 'cpf': '***.878.578-**'},
    {'posicao': 22, 'nome': 'MATEUS F ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 23, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 24, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 25, 'nome': 'ADEILTON ALVES BOSCARDIN', 'cpf': '***.449.378-**'},
    {'posicao': 26, 'nome': 'RICARDO HERNAN SARAVIA SIQUEIRA', 'cpf': '***.988.378-**'},
    {'posicao': 27, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 28, 'nome': 'BIANCA DIEBE', 'cpf': '***.838.758-**'},
    {'posicao': 29, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 30, 'nome': 'FELIPE HASHIMOTO FENGLER', 'cpf': '***.139.658-**'},
    {'posicao': 31, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 32, 'nome': 'HENRICO AUGUSTO LIMA LOPES', 'cpf': '***.973.248-**'},
    {'posicao': 33, 'nome': 'ANTONIO GABRIEL LIMA DE JESUS', 'cpf': '***.804.718-**'},
    {'posicao': 34, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 35, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 36, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 37, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 38, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 39, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 40, 'nome': 'CICERA MARIA C DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 41, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 42, 'nome': 'HELLEN VITORIA SANTOS OLIVEIRA', 'cpf': '***.395.998-**'},
    {'posicao': 43, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 44, 'nome': 'MURILO COELHO DOS SANTOS', 'cpf': '***.585.008-**'},
    {'posicao': 45, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 46, 'nome': 'DANILO DE OLIVERIA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 47, 'nome': 'BRUNO EDUARDO DAMASCO SABRIANO DA SILVA', 'cpf': '***.447.818-**'},
    {'posicao': 48, 'nome': 'JULIA GRANADO CORREA', 'cpf': '***.461.368-**'},
    {'posicao': 49, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 50, 'nome': 'CLAYTON FIGUEIREDO MAIA', 'cpf': '***.848.728-**'},
    {'posicao': 51, 'nome': 'MICHAEL MARQUES VIEIRA DE SOUZA', 'cpf': '***.340.948-**'},
    {'posicao': 52, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 53, 'nome': 'HERIVELTON HENRIQUE GONÇALVES', 'cpf': '***.607.418-**'},
    {'posicao': 54, 'nome': 'LUCAS SILVA PERES', 'cpf': '***.249.118-**'},
    {'posicao': 55, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 56, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 57, 'nome': 'ALESSANDRO RODRIGUES MELO FO', 'cpf': '***.118.258-**'},
    {'posicao': 58, 'nome': 'DAVY OLIVEIRA RIBEIRO', 'cpf': '***.517.878-**'},
    {'posicao': 59, 'nome': 'PEDRO VALADARES JUNIOR', 'cpf': '***.076.153-**'},
    {'posicao': 60, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 61, 'nome': 'LAURA DE ALMEIDA FOGAÇA', 'cpf': '***.329.568-**'},
    {'posicao': 62, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 63, 'nome': 'MARCOS UNO', 'cpf': '***.673.268-**'},
    {'posicao': 64, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 65, 'nome': 'FABIANO DA SILVA LINS DE ARAUJO', 'cpf': '***.651.038-**'},
    {'posicao': 66, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 67, 'nome': 'JOÃO VICTOR LOPEZ DE ARRUDA', 'cpf': '***.329.808-**'},
    {'posicao': 68, 'nome': 'LEON PEREIRA PINTO FAGUNDES', 'cpf': '***.469.018-**'},
    {'posicao': 69, 'nome': 'FLÁVIA ALVARENGA SARTORI', 'cpf': '***.695.758-**'},
    {'posicao': 70, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 71, 'nome': 'DANIELI FERREIRA DE JESUS', 'cpf': '***.932.848-**'},
    {'posicao': 72, 'nome': 'CÉSAR HENRIQUE CAMARGO DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 73, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 74, 'nome': 'PATRICIA CARDELI', 'cpf': '***.366.018-**'},
    {'posicao': 75, 'nome': 'THIAGO CICONELLO GIOVANETTI', 'cpf': '***.705.048-**'},
    {'posicao': 76, 'nome': 'NICOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 77, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 78, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 79, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 80, 'nome': 'GABRIEL RODRIGUES POZZA', 'cpf': '***.372.898-**'},
    {'posicao': 81, 'nome': 'LORENA CRISTINA CASSIANO', 'cpf': '***.493.518-**'},
    {'posicao': 82, 'nome': 'ALEX JULIO OLIVEIRA DA SILVA', 'cpf': '***.850.838-**'},
    {'posicao': 83, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 84, 'nome': 'POLYANNA PIRES PASCHOAL', 'cpf': '***.942.958-**'},
    {'posicao': 85, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 86, 'nome': 'GABRIEL TIAGO SANTOS LEME', 'cpf': '***.620.588-**'},
    {'posicao': 87, 'nome': 'AMADOR BUENO DE OLIVEIRA NETO', 'cpf': '***.548.238-**'},
    {'posicao': 88, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 89, 'nome': 'GABRIELLA FERNANDA PIERAMI', 'cpf': '***.935.418-**'},
    {'posicao': 90, 'nome': 'LUCAS VINICIOS CONSANI', 'cpf': '***.809.228-**'},
    {'posicao': 91, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 92, 'nome': 'MAYARA SOUZA BARROS', 'cpf': '***.545.948-**'},
    {'posicao': 93, 'nome': 'PAULO HENRIQUE VERRI RUFINO', 'cpf': '***.859.068-**'},
    {'posicao': 94, 'nome': 'KELVIN CORRÊA', 'cpf': '***.649.488-**'},
    {'posicao': 95, 'nome': 'DOUGLAS RAFAEL ASSIS MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 96, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 97, 'nome': 'VICTOR FAVRETTO', 'cpf': '***.827.468-**'},
    {'posicao': 98, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 99, 'nome': 'PAULO CESAR LOPES SILVA', 'cpf': '***.109.188-**'},
    {'posicao': 100, 'nome': 'MARCOS ELIAS FERREIRA SANTOS', 'cpf': '***.924.937-**'},
    {'posicao': 101, 'nome': 'MARIA EDUARDA MORENO LOPES', 'cpf': '***.335.888-**'},
    {'posicao': 102, 'nome': 'ALISON FERNANDES SANTOS', 'cpf': '***.715.938-**'},
    {'posicao': 103, 'nome': 'MATEUS FERNANDO XAVIER MARIANO', 'cpf': '***.903.418-**'},
    {'posicao': 104, 'nome': 'JONATAS SILVEIRA DA VARGEM', 'cpf': '***.451.678-**'},
    {'posicao': 105, 'nome': 'CLELIA DE JESUS QUEIROZ MOTTA', 'cpf': '***.071.678-**'},
    {'posicao': 106, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 107, 'nome': 'TIAGO MARTINS DOMINGUES', 'cpf': '***.241.908-**'},
    {'posicao': 108, 'nome': 'PEDRO ALBERTTE DO CARMO NETO', 'cpf': '***.598.478-**'},
    {'posicao': 109, 'nome': 'NICOLE FAVA PIRES', 'cpf': '***.051.518-**'},
    {'posicao': 110, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 111, 'nome': 'FABRICIO REIS ANTUNES', 'cpf': '***.785.958-**'},
    {'posicao': 112, 'nome': 'GUSTAVO HENRIQUE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 113, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 114, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 115, 'nome': 'ANGÉLICA DA SILVA CORDEIRO', 'cpf': '***.472.048-**'},
    {'posicao': 116, 'nome': 'DANIEL RODRIGUES LOPES ADEJARBAS', 'cpf': '***.276.508-**'},
    {'posicao': 117, 'nome': 'JOÃO VITOR DE CAMARGO BARROS', 'cpf': '***.513.388-**'},
    {'posicao': 118, 'nome': 'MARCUS VINICIUS CARDOSO DE FREITAS', 'cpf': '***.378.768-**'},
    {'posicao': 119, 'nome': 'THAFARO WESLLEY NOGUEIRA PAES', 'cpf': '***.955.418-**'},
    {'posicao': 120, 'nome': 'SAMUEL WILLIAM PAES', 'cpf': '***.233.758-**'},
    {'posicao': 121, 'nome': 'RODRIGO HENRIQUE DUARTE', 'cpf': '***.331.688-**'},
    {'posicao': 122, 'nome': 'RAFAEL FRANCISCO LARA DE OLIVEIRA', 'cpf': '***.543.308-**'},
    {'posicao': 123, 'nome': 'NÍCOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 124, 'nome': 'NICOLE JANINE BOLZANI OLIVEIRA', 'cpf': '***.303.578-**'},
    {'posicao': 125, 'nome': 'GUSTAVO H O LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 126, 'nome': 'JACKSON ROGÉRIO DA CRUZ', 'cpf': '***.069.868-**'},
    {'posicao': 127, 'nome': 'LEANDRO TEODORO POLERA', 'cpf': '***.565.548-**'},
    {'posicao': 128, 'nome': 'JULIA MARIA JUBAT ALVES DOS SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 129, 'nome': 'MIRELLA XAVIER GALINDO', 'cpf': '***.482.048-**'},
    {'posicao': 130, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 131, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 132, 'nome': 'BIANCA PICHIRILO VERGUEIRO BENATTI', 'cpf': '***.498.018-**'},
    {'posicao': 133, 'nome': 'EBER TEIXEIRA CALADO', 'cpf': '***.976.838-**'},
    {'posicao': 134, 'nome': 'GISLAINE OLIVEIRA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 135, 'nome': 'PEDRO ARTHUR DE OLIVEIRA', 'cpf': '***.415.258-**'},
    {'posicao': 136, 'nome': 'NATALIA SILVEIRA TOLEDO', 'cpf': '***.003.228-**'},
    {'posicao': 137, 'nome': 'THIAGO HENRIQUE MUNIZ NEVES', 'cpf': '***.276.608-**'},
    {'posicao': 138, 'nome': 'JEFFERSON PADILHA LUZ', 'cpf': '***.267.028-**'},
    {'posicao': 139, 'nome': 'CAIO COUTO FICHEL', 'cpf': '***.501.478-**'},
    {'posicao': 140, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 141, 'nome': 'MARINA PANNUNZIO RIBEIRO', 'cpf': '***.349.668-**'},
    {'posicao': 142, 'nome': 'ANA BEATRIZ CONCEICAO APARECIDA CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 143, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 144, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 145, 'nome': 'SABRINA SANT ANA DA SILVA ALVES', 'cpf': '***.844.038-**'},
    {'posicao': 146, 'nome': 'WENDELL CONTE JOSEFIK', 'cpf': '***.732.498-**'},
    {'posicao': 147, 'nome': 'VITOR MEIRA ALVES', 'cpf': '***.126.668-**'},
    {'posicao': 148, 'nome': 'LUCAS CAMELO', 'cpf': '***.754.708-**'},
    {'posicao': 149, 'nome': 'BRUNA LAIS LEME', 'cpf': '***.337.788-**'},
    {'posicao': 150, 'nome': 'VICTOR LOPES MARINS', 'cpf': '***.953.868-**'},
    {'posicao': 151, 'nome': 'EDSON VITOR PALDINI', 'cpf': '***.907.508-**'},
    {'posicao': 152, 'nome': 'ALLAN WANDREY QUEIROZ', 'cpf': '***.395.008-**'},
    {'posicao': 153, 'nome': 'CAUE POLIZELI CAMARGO', 'cpf': '***.808.628-**'},
    {'posicao': 154, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 155, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 156, 'nome': 'FABIO LUIZ DE FRANÇA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 157, 'nome': 'ISABELA MIWA DA SILVA', 'cpf': '***.050.578-**'},
    {'posicao': 158, 'nome': 'GISLAINE OLIVIERA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 159, 'nome': 'LEON P PINTO FAGUNDES', 'cpf': '***.469.018-**'},
    {'posicao': 160, 'nome': 'MARCEL MONTEIRO BALDUINO', 'cpf': '***.801.468-**'},
    {'posicao': 161, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 162, 'nome': 'SABRINA CARNEIRO RODRIGUES', 'cpf': '***.167.588-**'},
    {'posicao': 163, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 164, 'nome': 'FELIPE VINICIUS GONCALVES DOS REIS', 'cpf': '***.616.758-**'},
    {'posicao': 165, 'nome': 'RENATA MARTINS', 'cpf': '***.600.208-**'},
    {'posicao': 166, 'nome': 'MARCO TULIO DUENAS', 'cpf': '***.415.798-**'},
    {'posicao': 167, 'nome': 'GABRIEL FERREIRA DOS SANTOS', 'cpf': '***.779.118-**'},
    {'posicao': 168, 'nome': 'PAULO VITOR LEMES', 'cpf': '***.781.688-**'},
    {'posicao': 169, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 170, 'nome': 'GUSTAVO DE CAMPOS ANTUNES', 'cpf': '***.326.288-**'},
    {'posicao': 171, 'nome': 'LISANDRA FERNANDA DE GODOI', 'cpf': '***.048.668-**'},
    {'posicao': 172, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 173, 'nome': 'PAULO CESAR PONTES DE OLIVEIRA', 'cpf': '***.360.198-**'},
    {'posicao': 174, 'nome': 'MATEUS SILVA DALMARCO', 'cpf': '***.839.838-**'},
    {'posicao': 176, 'nome': 'MERILLYN APARECIDA DA CUNHA', 'cpf': '***.754.848-**'},
    {'posicao': 177, 'nome': 'ENIO APARECIDO DA SILVA', 'cpf': '***.696.198-**'},
    {'posicao': 178, 'nome': 'GUSTAVO HENRIQUE DOS REIS', 'cpf': '***.655.028-**'},
    {'posicao': 179, 'nome': 'NICOLAS KATSUJI NAGANO', 'cpf': '***.156.448-**'},
    {'posicao': 180, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 181, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 182, 'nome': 'ÍTALO BRENDO DE ARAÚJO VISNÓVESKI', 'cpf': '***.317.558-**'},
    {'posicao': 183, 'nome': 'PEDRO SILVA MARTINS', 'cpf': '***.245.268-**'},
    {'posicao': 184, 'nome': 'PRISCILA NORONHA MENDES', 'cpf': '***.687.188-**'},
    {'posicao': 185, 'nome': 'RAPHAEL CARDOZO CASTILHO', 'cpf': '***.652.058-**'},
    {'posicao': 186, 'nome': 'RICARDO DOS SANTOS ALENCAR', 'cpf': '***.969.878-**'},
    {'posicao': 187, 'nome': 'PRISCILA S K CORREA', 'cpf': '***.553.718-**'},
    {'posicao': 188, 'nome': 'LUIZ ANTONIO PANTOJO JUNIOR', 'cpf': '***.393.588-**'}
]

# 4. Interface principal
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center;'>🍔 Lanches</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #333;'>Consulta de Ranking</h2>", unsafe_allow_html=True)

# Input de busca
nome_busca = st.text_input("", placeholder="Insira seu nome completo...")

# Botão Buscar
c_btn1, c_btn2, c_btn3 = st.columns([0.1, 2.8, 0.1])
with c_btn2:
    botao_busca = st.button("Buscar")

# Lógica da Busca
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

st.markdown("<br>", unsafe_allow_html=True)

# --- BOTÕES SECUNDÁRIOS ---
col_res, col_sort = st.columns(2)

with col_res:
    if st.button("Resultado"):
        st.markdown("<h3 style='text-align: center;'>🏆 Top 2</h3>", unsafe_allow_html=True)
        top_2 = [u for u in ranking_db if u['posicao'] in [1, 2]]
        for p in top_2:
            st.markdown(f"""
                <div class="resultado-card" style="text-align: center;">
                    <p style="margin: 0;"><strong>{p['posicao']}º - {p['nome']}</strong></p>
                </div>
            """, unsafe_allow_html=True)

with col_sort:
    if st.button("Sorteio"):
        video_url = "https://raw.githubusercontent.com/victor-perillo/rankinglanches/main/sorteio.mp4"
        st.markdown("<p style='text-align: center; font-weight: bold;'>🎥 Vídeo do Sorteio</p>", unsafe_allow_html=True)
        st.video(video_url)

# 5. Rodapé
st.markdown("""
    <div class="footer-text">
        Atualizado em 04/05/2026<br>
        <strong>Promoção válida até 30/05/2026</strong>
    </div>
""", unsafe_allow_html=True)
