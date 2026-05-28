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

    .vencedor-card {
        background-color: #FFF9C4;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #FFD700;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255,215,0,0.2);
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
    {'posicao': 1, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 2, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 3, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 4, 'nome': 'PAULO VITOR LEMES', 'cpf': '***.781.688-**'},
    {'posicao': 5, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 6, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 7, 'nome': 'WILTON ROGÉRIO DA COSTA PEREIRA', 'cpf': '***.922.138-**'},
    {'posicao': 8, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 9, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 10, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 11, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 12, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 13, 'nome': 'DOUGLAS RAFAEL ASSIS MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 14, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 15, 'nome': 'RODOLFO ANTUNES DE ALMEIDA', 'cpf': '***.685.268-**'},
    {'posicao': 16, 'nome': 'ELIOENAI CACERES PEREIRA', 'cpf': '***.496.738-**'},
    {'posicao': 17, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 18, 'nome': 'MURILO COELHO DOS SANTOS', 'cpf': '***.585.008-**'},
    {'posicao': 19, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 20, 'nome': 'PRISCILA NORONHA MENDES', 'cpf': '***.687.188-**'},
    {'posicao': 21, 'nome': 'LUCAS CAMELO', 'cpf': '***.754.708-**'},
    {'posicao': 22, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 23, 'nome': 'LISANDRA FERNANDA DE GODOI', 'cpf': '***.048.668-**'},
    {'posicao': 24, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 25, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 26, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 27, 'nome': 'PEDRO ALBERTTE DO CARMO NETO', 'cpf': '***.598.478-**'},
    {'posicao': 28, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 29, 'nome': 'CAIO GUILHERME PEREIRA DOS SANTOS KITAGAKI', 'cpf': '***.590.628-**'},
    {'posicao': 30, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 31, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 32, 'nome': 'HELLEN VITORIA SANTOS OLIVEIRA', 'cpf': '***.395.998-**'},
    {'posicao': 33, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 34, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 35, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 36, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 37, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 38, 'nome': 'MATEUS CARDOSO PIRES', 'cpf': '***.179.968-**'},
    {'posicao': 39, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 40, 'nome': 'ADEILTON ALVES BOSCARDIN', 'cpf': '***.449.378-**'},
    {'posicao': 41, 'nome': 'VICTOR LOPES MARINS', 'cpf': '***.953.868-**'},
    {'posicao': 42, 'nome': 'ALISON CARRIEL ROCHA', 'cpf': '***.626.128-**'},
    {'posicao': 43, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 44, 'nome': 'BRUNO EDUARDO DAMASCO SABRIANO DA SILVA', 'cpf': '***.447.818-**'},
    {'posicao': 45, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 46, 'nome': 'NICOLE FAVA PIRES', 'cpf': '***.051.518-**'},
    {'posicao': 47, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 48, 'nome': 'CAIO HENRIQUE LEME SANTOS', 'cpf': '***.290.728-**'},
    {'posicao': 49, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 50, 'nome': 'IAGO YURI ROSSAN', 'cpf': '***.414.088-**'},
    {'posicao': 51, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 52, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 53, 'nome': 'TIAGO ALVES SIMOES', 'cpf': '***.528.818-**'},
    {'posicao': 54, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 55, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 56, 'nome': 'FELIPE HASHIMOTO FENGLER', 'cpf': '***.139.658-**'},
    {'posicao': 57, 'nome': 'THAFARO WESLLEY NOGUEIRA PAES', 'cpf': '***.955.418-**'},
    {'posicao': 58, 'nome': 'RAPHAEL CARDOZO CASTILHO', 'cpf': '***.652.058-**'},
    {'posicao': 59, 'nome': 'CESAR HENRIQUE C DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 60, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 61, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 62, 'nome': 'DANIELA DE CASTRO MORAES', 'cpf': '***.645.658-**'},
    {'posicao': 63, 'nome': 'DANILO DE OLIVERIA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 64, 'nome': 'SAMUEL WILLIAM PAES', 'cpf': '***.233.758-**'},
    {'posicao': 65, 'nome': 'PEDRO VALADARES JUNIOR', 'cpf': '***.076.153-**'},
    {'posicao': 66, 'nome': 'ARIANA VIEIRA OMURA', 'cpf': '***.092.708-**'},
    {'posicao': 67, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 68, 'nome': 'ALMENIA MARIA CRISTINA DE SOUZA MENCACCI', 'cpf': '***.476.868-**'},
    {'posicao': 69, 'nome': 'RAFAEL FRANCISCO LARA DE OLIVEIRA', 'cpf': '***.543.308-**'},
    {'posicao': 70, 'nome': 'MARCOS UNO', 'cpf': '***.673.268-**'},
    {'posicao': 71, 'nome': 'ANDERSON DE SOUZA PAULINO', 'cpf': '***.424.278-**'},
    {'posicao': 72, 'nome': 'TIAGO MARTINS DOMINGUES', 'cpf': '***.241.908-**'},
    {'posicao': 73, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 74, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 75, 'nome': 'VITOR MEIRA ALVES', 'cpf': '***.126.668-**'},
    {'posicao': 76, 'nome': 'CHRISTIAN DA SILVA PEREIRA', 'cpf': '***.675.888-**'},
    {'posicao': 77, 'nome': 'MIGUEL FELIPE DOS SANTOS GOUVEA', 'cpf': '***.993.238-**'},
    {'posicao': 78, 'nome': 'GISLAINE OLIVEIRA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 79, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 80, 'nome': 'TICIANE RAFAELA OTO', 'cpf': '***.852.938-**'},
    {'posicao': 81, 'nome': 'ALESSANDRO RODRIGUES MELO FO', 'cpf': '***.118.258-**'},
    {'posicao': 82, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 83, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 84, 'nome': 'VINÍCIUS GAMA DE FRANÇA', 'cpf': '***.358.148-**'},
    {'posicao': 85, 'nome': 'BIANCA DIEBE', 'cpf': '***.838.758-**'},
    {'posicao': 86, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 87, 'nome': 'HERIVELTON HENRIQUE GONÇALVES', 'cpf': '***.607.418-**'},
    {'posicao': 88, 'nome': 'THIAGO CICONELLO GIOVANETTI', 'cpf': '***.705.048-**'},
    {'posicao': 89, 'nome': 'GIOVANNI DE SOUZA SANTOS', 'cpf': '***.126.928-**'},
    {'posicao': 90, 'nome': 'GUSTAVO FERRARI MESQUITA AMORIM', 'cpf': '***.048.128-**'},
    {'posicao': 91, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 92, 'nome': 'JACKSON HEBERT SANTOS', 'cpf': '***.868.628-**'},
    {'posicao': 93, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 94, 'nome': 'PAULO HENRIQUE VERRI RUFINO', 'cpf': '***.859.068-**'},
    {'posicao': 95, 'nome': 'VICTOR HUGO DIAS MODESTO', 'cpf': '***.282.068-**'},
    {'posicao': 96, 'nome': 'DANIELI FERREIRA DE JESUS', 'cpf': '***.932.848-**'},
    {'posicao': 97, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 98, 'nome': 'GABRIEL HENRIQUE GARCIA ARANTES', 'cpf': '***.958.128-**'},
    {'posicao': 99, 'nome': 'MIGUEL FIDENCIO AYRES', 'cpf': '***.438.038-**'},
    {'posicao': 100, 'nome': 'JOÃO VICTOR LOPEZ DE ARRUDA', 'cpf': '***.329.808-**'},
    {'posicao': 101, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 102, 'nome': 'ANA BEATRIZ CONCEICAO APARECIDA CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 103, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 104, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 105, 'nome': 'JULIA MARIA JUBAT ALVES DOS SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 106, 'nome': 'FELIPE VINICIUS GONCALVES DOS REIS', 'cpf': '***.616.758-**'},
    {'posicao': 107, 'nome': 'RYAN PIETRO CONSOLARI', 'cpf': '***.356.588-**'},
    {'posicao': 108, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 109, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 110, 'nome': 'CLAYTON FIGUEIREDO MAIA', 'cpf': '***.848.728-**'},
    {'posicao': 111, 'nome': 'GUILHERME VINICIUS BAEZA DE OLIVEIRA', 'cpf': '***.952.258-**'},
    {'posicao': 112, 'nome': 'FELIPE GOMES FELIX', 'cpf': '***.257.488-**'},
    {'posicao': 113, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 114, 'nome': 'JONATAS SILVEIRA DA VARGEM', 'cpf': '***.451.678-**'},
    {'posicao': 115, 'nome': 'HENRICO AUGUSTO LIMA LOPES', 'cpf': '***.973.248-**'},
    {'posicao': 116, 'nome': 'MARAISA OLIVEIRA HUGGLER', 'cpf': '***.261.768-**'},
    {'posicao': 117, 'nome': 'MARCO TULIO DUENAS', 'cpf': '***.415.798-**'},
    {'posicao': 118, 'nome': 'GABRIELA PEREIRA DO PRADO', 'cpf': '***.352.918-**'},
    {'posicao': 119, 'nome': 'CICERA MARIA COELHO DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 120, 'nome': 'MAYARA SOUZA BARROS', 'cpf': '***.545.948-**'},
    {'posicao': 121, 'nome': 'MATEUS SILVA DALMARCO', 'cpf': '***.839.838-**'},
    {'posicao': 122, 'nome': 'LUCAS LINS MARTINS', 'cpf': '***.534.458-**'},
    {'posicao': 123, 'nome': 'LORENA CRISTINA CASSIANO', 'cpf': '***.493.518-**'},
    {'posicao': 124, 'nome': 'KARLOS INACIO DA SILVA', 'cpf': '***.430.194-**'},
    {'posicao': 125, 'nome': 'VICTOR FAVRETTO', 'cpf': '***.827.468-**'},
    {'posicao': 126, 'nome': 'GABRIEL RODRIGUES SCHEREIBER POZZA', 'cpf': '***.372.898-**'},
    {'posicao': 127, 'nome': 'KELVIN CORRÊA', 'cpf': '***.649.488-**'},
    {'posicao': 128, 'nome': 'GUSTAVO H O LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 129, 'nome': 'SAMUEL LOPES VIEIRA DA ROCHA', 'cpf': '***.300.138-**'},
    {'posicao': 130, 'nome': 'FREDERICO HASEGAWA COPELI VENA', 'cpf': '***.878.578-**'},
    {'posicao': 131, 'nome': 'ENIO APARECIDO DA SILVA', 'cpf': '***.696.198-**'},
    {'posicao': 132, 'nome': 'ANTONIO GABRIEL LIMA DE JESUS', 'cpf': '***.804.718-**'},
    {'posicao': 133, 'nome': 'CAIO C CORRA BELLO', 'cpf': '***.393.148-**'},
    {'posicao': 134, 'nome': 'FERNANDO RIBEIRO DOS SANTOS', 'cpf': '***.650.658-**'},
    {'posicao': 135, 'nome': 'GUILHERME TOBIAS PIVA', 'cpf': '***.719.958-**'},
    {'posicao': 136, 'nome': 'POLYANNA PIRES PASCHOAL', 'cpf': '***.942.958-**'},
    {'posicao': 137, 'nome': 'ROBSON NICOLAS CARDOSO', 'cpf': '***.620.988-**'},
    {'posicao': 138, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 139, 'nome': 'CAIO HENRIQUE RODRIGUES', 'cpf': '***.533.748-**'},
    {'posicao': 140, 'nome': 'NICOLLAS MENCACCI PEREIRA', 'cpf': '***.757.358-**'},
    {'posicao': 141, 'nome': 'GABRIELLA FERNANDA PIERAMI', 'cpf': '***.935.418-**'},
    {'posicao': 142, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 143, 'nome': 'PATRICIA CARDELI', 'cpf': '***.366.018-**'},
    {'posicao': 144, 'nome': 'BRUNO GALDINO DE ARRUDA', 'cpf': '***.710.318-**'},
    {'posicao': 145, 'nome': 'SABRINA CRISTINA PEDRO VITORINO', 'cpf': '***.299.258-**'},
    {'posicao': 146, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 147, 'nome': 'JOSE CARLOS LOPES PEREIRA', 'cpf': '***.424.808-**'},
    {'posicao': 148, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 149, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 150, 'nome': 'BIANCA PICHIRILO VERGUEIRO BENATTI', 'cpf': '***.498.018-**'},
    {'posicao': 151, 'nome': 'DOUGLAS FELIPE FERREIRA', 'cpf': '***.066.208-**'},
    {'posicao': 152, 'nome': 'GABRIEL TIAGO SANTOS LEME', 'cpf': '***.620.588-**'},
    {'posicao': 153, 'nome': 'TIAGO AUGUSTO PEDROSO DE CARVALHO', 'cpf': '***.333.798-**'},
    {'posicao': 154, 'nome': 'LAYARA BEATRIZ DOS SANTOS', 'cpf': '***.958.598-**'},
    {'posicao': 155, 'nome': 'CLAUDIO ROBERTO CORREDATO', 'cpf': '***.556.928-**'},
    {'posicao': 156, 'nome': 'DOUGLAS VICTOR WENZEL NUNES', 'cpf': '***.636.418-**'},
    {'posicao': 157, 'nome': 'GUILHERME ANTONIO RODRIGUES DA COSTA', 'cpf': '***.144.268-**'},
    {'posicao': 158, 'nome': 'KARINA BRUNO DE OLIVEIRA', 'cpf': '***.900.288-**'},
    {'posicao': 159, 'nome': 'LEANDRO TEODORO POLERA', 'cpf': '***.565.548-**'},
    {'posicao': 160, 'nome': 'VITOR FERRAZ BLUMEN', 'cpf': '***.271.388-**'},
    {'posicao': 161, 'nome': 'GUILHERME ANDRADE ALVES DA SILVA', 'cpf': '***.149.078-**'},
    {'posicao': 162, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 163, 'nome': 'DAVI DE LIMA', 'cpf': '***.714.688-**'},
    {'posicao': 164, 'nome': 'GILLIARD TREVISANI DE OLIVEIRA', 'cpf': '***.200.428-**'},
    {'posicao': 165, 'nome': 'LAURA DE PAULA FERREIRA', 'cpf': '***.280.868-**'},
    {'posicao': 166, 'nome': 'GUSTAVO SCHIMIDT SANTOS', 'cpf': '***.053.488-**'},
    {'posicao': 167, 'nome': 'CICERA MARIA C DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 168, 'nome': 'CAUA DE OLIVEIRA CUNHA', 'cpf': '***.175.288-**'},
    {'posicao': 169, 'nome': 'ALISON FERNANDES SANTOS', 'cpf': '***.715.938-**'},
    {'posicao': 170, 'nome': 'FABIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 171, 'nome': 'BRENDA BIRAL BATISTA', 'cpf': '***.430.818-**'},
    {'posicao': 172, 'nome': 'FÁBIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 173, 'nome': 'ANA BEATRIZ CONCEICAO A CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 174, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 175, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 176, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 177, 'nome': 'GABRIEL RIBEIRO CORREA', 'cpf': '***.092.198-**'},
    {'posicao': 178, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 179, 'nome': 'SABRINA CARNEIRO RODRIGUES', 'cpf': '***.167.588-**'},
    {'posicao': 180, 'nome': 'SILVIO GABRIEL DE JEZUS', 'cpf': '***.028.008-**'},
    {'posicao': 181, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 182, 'nome': 'MICHAEL MARQUES VIEIRA DE SOUZA', 'cpf': '***.340.948-**'},
    {'posicao': 183, 'nome': 'JOSE MARIA NOGUEIRA FOGACA JUNIOR', 'cpf': '***.802.708-**'},
    {'posicao': 184, 'nome': 'MATEUS FERNANDES ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 185, 'nome': 'FABIANO DA SILVA LINS DE ARAUJO', 'cpf': '***.651.038-**'},
    {'posicao': 186, 'nome': 'GUILHERME ANTÓNIO RIBAS NOBREGA', 'cpf': '***.706.988-**'},
    {'posicao': 187, 'nome': 'TAÍSE MIGUEL RODRIGUES', 'cpf': '***.105.998-**'},
    {'posicao': 188, 'nome': 'ANA ISABELLY SONCIM VENANCIO', 'cpf': '***.766.618-**'},
    {'posicao': 189, 'nome': 'LILIAN SAMPAIO LEITE', 'cpf': '***.399.378-**'},
    {'posicao': 190, 'nome': 'MARIA LUIZA SCHNEIDER', 'cpf': '***.331.068-**'},
    {'posicao': 191, 'nome': 'BIANCA DOMINGUES VAZ', 'cpf': '***.337.068-**'},
    {'posicao': 192, 'nome': 'CLELIA DE JESUS QUEIROZ MOTTA', 'cpf': '***.071.678-**'},
    {'posicao': 193, 'nome': 'RAFAELA MOCCI BORTOLAJA PRETTE', 'cpf': '***.064.888-**'},
    {'posicao': 194, 'nome': 'GABRIEL ALCANTARA DIAS PRESTES', 'cpf': '***.224.798-**'},
    {'posicao': 195, 'nome': 'GUSTAVO HENRIQUE BAUCH', 'cpf': '***.060.348-**'},
    {'posicao': 196, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 197, 'nome': 'PEDRO SILVA MARTINS', 'cpf': '***.245.268-**'},
    {'posicao': 198, 'nome': 'MARIA EDUARDA MORENO LOPES', 'cpf': '***.335.888-**'},
    {'posicao': 199, 'nome': 'SABRINA SANT ANA DA SILVA ALVES', 'cpf': '***.844.038-**'},
    {'posicao': 200, 'nome': 'MARCOS VINICIUS NUNES FERREIRA', 'cpf': '***.123.218-**'}
]
# 4. Interface principal
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    try:
        st.image("logo.jpg", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center;'>🍔 Lanches</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #333;'>Consulta de Ranking</h2>", unsafe_allow_html=True)

nome_busca = st.text_input("", placeholder="Insira seu nome completo...")

c_btn1, c_btn2, c_btn3 = st.columns([0.1, 2.8, 0.1])
with c_btn2:
    botao_busca = st.button("Buscar")

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
        Atualizado em 28/05/2026<br>
        <strong>Promoção válida até 29/05/26 </strong>
    </div>
""", unsafe_allow_html=True)
