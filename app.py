import streamlit as st
import os
import glob

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
    {'posicao': 1, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 2, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 3, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 4, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 5, 'nome': 'MATEUS CARDOSO PIRES', 'cpf': '***.179.968-**'},
    {'posicao': 6, 'nome': 'LUCCAS MATHEUS BARBOSA CRUZ', 'cpf': '***.836.468-**'},
    {'posicao': 7, 'nome': 'GABRIELA FREITAS RIBEIRO', 'cpf': '***.904.968-**'},
    {'posicao': 8, 'nome': 'VICTOR PERILLO RODRIGUES SAMPAIO', 'cpf': '***.334.318-**'},
    {'posicao': 9, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 10, 'nome': 'IGOR WENDEL AMARAL', 'cpf': '***.109.578-**'},
    {'posicao': 11, 'nome': 'BRUNO BERTIN VITORINO', 'cpf': '***.804.368-**'},
    {'posicao': 12, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 13, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 14, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 15, 'nome': 'NICOLAS CONSTANÇA MENTONE', 'cpf': '***.154.108-**'},
    {'posicao': 16, 'nome': 'VAGNER RODRIGUES SAMPAIO', 'cpf': '***.943.698-**'},
    {'posicao': 17, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 18, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 19, 'nome': 'RODOLFO ANTUNES DE ALMEIDA', 'cpf': '***.685.268-**'},
    {'posicao': 20, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 21, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 22, 'nome': 'GIOVANNA RAGA', 'cpf': '55.068.780/0001-01'},
    {'posicao': 23, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 24, 'nome': 'LAURA DA SILVA SEGANTIN', 'cpf': '***.300.358-**'},
    {'posicao': 25, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 26, 'nome': 'ANTHONNY COCUZZA', 'cpf': '***.196.318-**'},
    {'posicao': 27, 'nome': 'BRASILIO DEMETRIO MARCOS', 'cpf': '***.590.648-**'},
    {'posicao': 28, 'nome': 'MARIA EDUARDA FERNANDES RIBEIRO', 'cpf': '***.654.718-**'},
    {'posicao': 29, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 30, 'nome': 'DANIEL DE FREITAS ESTEVES DA COSTA', 'cpf': '***.311.778-**'},
    {'posicao': 31, 'nome': 'ADEILTON ALVES BOSCARDIN', 'cpf': '***.449.378-**'},
    {'posicao': 32, 'nome': 'LEONARDO VINÍCIUS RUIZ RONDELIS', 'cpf': '***.079.718-**'},
    {'posicao': 33, 'nome': 'THAFARO WESLLEY NOGUEIRA PAES', 'cpf': '***.955.418-**'},
    {'posicao': 34, 'nome': 'MURILO COELHO DOS SANTOS', 'cpf': '***.585.008-**'},
    {'posicao': 35, 'nome': 'MATEUS FERNANDO XAVIER MARIANO', 'cpf': '***.903.418-**'},
    {'posicao': 36, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 37, 'nome': 'VICTOR HUGO DIAS MODESTO', 'cpf': '***.282.068-**'},
    {'posicao': 38, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 39, 'nome': 'VINÍCIUS GAMA DE FRANÇA', 'cpf': '***.358.148-**'},
    {'posicao': 40, 'nome': 'VICTOR AUGUSTO DE SOUZA', 'cpf': '***.913.138-**'},
    {'posicao': 41, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 42, 'nome': 'LISANDRA FERNANDA DE GODOI', 'cpf': '***.048.668-**'},
    {'posicao': 43, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 44, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 45, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 46, 'nome': 'SOPHIA CASTILHO MORENO', 'cpf': '***.497.218-**'},
    {'posicao': 47, 'nome': 'ADMILSON DE GODOI', 'cpf': '***.777.758-**'},
    {'posicao': 48, 'nome': 'GIOVANNI DE SOUZA SANTOS', 'cpf': '***.126.928-**'},
    {'posicao': 49, 'nome': 'ABNER MARTINS DE CAMARGO', 'cpf': '***.241.638-**'},
    {'posicao': 50, 'nome': 'LUCAS SILVA PERES', 'cpf': '***.249.118-**'},
    {'posicao': 51, 'nome': 'THIAGO SCHIMIDT MACHADO', 'cpf': '***.898.288-**'},
    {'posicao': 52, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 53, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 54, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 55, 'nome': 'PRISCILA S K CORREA', 'cpf': '***.553.718-**'},
    {'posicao': 56, 'nome': 'NICOLAS SILVA PREVIATO', 'cpf': '***.392.738-**'},
    {'posicao': 57, 'nome': 'CÉSAR HENRIQUE CAMARGO DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 58, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 59, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 60, 'nome': 'TIAGO MARTINS DOMINGUES', 'cpf': '***.241.908-**'},
    {'posicao': 61, 'nome': 'RICARDO HERNAN SARAVIA SIQUEIRA', 'cpf': '***.988.378-**'},
    {'posicao': 62, 'nome': 'RODRIGO OLIVEIRA DA ROCHA', 'cpf': '***.086.868-**'},
    {'posicao': 63, 'nome': 'FÁBIO BLAS MASUELA', 'cpf': '***.731.318-**'},
    {'posicao': 64, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 65, 'nome': 'CAIO GUILHERME PEREIRA DOS SANTOS KITAGAKI', 'cpf': '***.590.628-**'},
    {'posicao': 66, 'nome': 'EVELIN DAYANE CAVALCANTE', 'cpf': '***.351.418-**'},
    {'posicao': 67, 'nome': 'BRYAN FRANCA SOARES', 'cpf': '***.447.638-**'},
    {'posicao': 68, 'nome': 'LETICIA PEREIRA', 'cpf': '***.745.188-**'},
    {'posicao': 69, 'nome': 'ANA CAROLINA MAGALHAES LOPES', 'cpf': '***.524.501-**'},
    {'posicao': 70, 'nome': 'ANA BEATRIZ CONCEICAO APARECIDA CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 71, 'nome': 'GISLAINE OLIVIERA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 72, 'nome': 'PEDRO PAZETTI DE OLIVEIRA', 'cpf': '***.199.158-**'},
    {'posicao': 73, 'nome': 'IRENE DE CAMPOS PERILLO', 'cpf': '***.970.888-**'},
    {'posicao': 74, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 75, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 76, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 77, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 78, 'nome': 'GUSTAVO DE CAMPOS ANTUNES', 'cpf': '***.326.288-**'},
    {'posicao': 79, 'nome': 'LUIZA DOS ANJOS OLIVEIRA', 'cpf': '***.469.738-**'},
    {'posicao': 80, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 81, 'nome': 'TIAGO DE SOUZA SANTOS', 'cpf': '***.259.568-**'},
    {'posicao': 82, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 83, 'nome': 'MATEUS FERNANDES ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 84, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 85, 'nome': 'HELLEN NUNES DOS SANTOS SOUZA', 'cpf': '***.123.355-**'},
    {'posicao': 86, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 87, 'nome': 'POLYANNA PIRES PASCHOAL', 'cpf': '***.942.958-**'},
    {'posicao': 88, 'nome': 'RAPHAELLA CAMILLY LUCAS RODRIGUES', 'cpf': '***.706.918-**'},
    {'posicao': 89, 'nome': 'LUIZ CARLOS DA SILVA BUENO', 'cpf': '***.273.528-**'},
    {'posicao': 90, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 91, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 92, 'nome': 'THALIA FERREIRA TIJOLLI DE FREITAS', 'cpf': '***.489.168-**'},
    {'posicao': 93, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 94, 'nome': 'JONATHAN ANDREW ALVES GARCIA', 'cpf': '***.133.298-**'},
    {'posicao': 95, 'nome': 'MATHEUS APARECIDO FERREIRA DO PRADO', 'cpf': '***.389.478-**'},
    {'posicao': 96, 'nome': 'ALISON CARRIEL ROCHA', 'cpf': '***.626.128-**'},
    {'posicao': 97, 'nome': 'TAMARA DE ASSIS BARBOSA', 'cpf': '***.376.378-**'},
    {'posicao': 98, 'nome': 'SERGIO DOMINGOS RODRIGUES SAMPAIO', 'cpf': '***.710.718-**'},
    {'posicao': 99, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 100, 'nome': 'GABRIEL PEDROSO DE GOES VIEIRA', 'cpf': '***.869.898-**'},
    {'posicao': 101, 'nome': 'CAIO COUTO FICHEL', 'cpf': '***.501.478-**'},
    {'posicao': 102, 'nome': 'MARIA LUIZA SCHNEIDER', 'cpf': '***.331.068-**'},
    {'posicao': 103, 'nome': 'FELIPE MENDES BALOTIM', 'cpf': '***.576.988-**'},
    {'posicao': 104, 'nome': 'RYAN PIETRO CONSOLARI', 'cpf': '***.356.588-**'},
    {'posicao': 105, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 106, 'nome': 'MIGUEL COELHO EVANGELISTA DOS SANTOS', 'cpf': '***.691.478-**'},
    {'posicao': 107, 'nome': 'PAULO HENRIQUE VERRI RUFINO', 'cpf': '***.859.068-**'},
    {'posicao': 108, 'nome': 'MATEUS SILVA DALMARCO', 'cpf': '***.839.838-**'},
    {'posicao': 109, 'nome': 'FABRICIO REIS ANTUNES', 'cpf': '***.785.958-**'},
    {'posicao': 110, 'nome': 'RAFAEL FRANCISCO LARA DE OLIVEIRA', 'cpf': '***.543.308-**'},
    {'posicao': 111, 'nome': 'GABRIEL FERREIRA DOS SANTOS', 'cpf': '***.779.118-**'},
    {'posicao': 112, 'nome': 'DOUGLAS RAFAEL ASSIS MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 113, 'nome': 'PAULO VITOR LEMES', 'cpf': '***.781.688-**'},
    {'posicao': 114, 'nome': 'CAIO HENRIQUE LEME SANTOS', 'cpf': '***.290.728-**'},
    {'posicao': 115, 'nome': 'LUCAS CAMELO', 'cpf': '***.754.708-**'},
    {'posicao': 116, 'nome': 'MATHEUS FRANCISCO ALVES', 'cpf': '***.682.298-**'},
    {'posicao': 117, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 118, 'nome': 'GABRIEL RODRIGUES SCHEREIBER POZZA', 'cpf': '***.372.898-**'},
    {'posicao': 119, 'nome': 'EDUARDO VIEIRA RIBEIRO DA SILVA', 'cpf': '***.475.388-**'},
    {'posicao': 120, 'nome': 'RENATA MARTINS', 'cpf': '***.600.208-**'},
    {'posicao': 121, 'nome': 'LUIZ ANTONIO PANTOJO JUNIOR', 'cpf': '***.393.588-**'},
    {'posicao': 122, 'nome': 'JUSSARA XAVIER DA SILVA MARIANO', 'cpf': '***.002.598-**'},
    {'posicao': 123, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 124, 'nome': 'ARTHUR ROGÉRIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 125, 'nome': 'JAQUELINE CLARA GUTIERREZ BRESIO', 'cpf': '***.333.108-**'},
    {'posicao': 126, 'nome': 'MARIA EDUARDA MORAIS OIKAWA', 'cpf': '***.300.368-**'},
    {'posicao': 127, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 128, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 129, 'nome': 'CICERA MARIA COELHO DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 130, 'nome': 'MARIA E PEREIRA NUNES', 'cpf': '***.951.288-**'},
    {'posicao': 131, 'nome': 'TALITA RAMOS LAURIANO AKYAMA', 'cpf': '***.427.478-**'},
    {'posicao': 132, 'nome': 'PEDRO VALADARES JUNIOR', 'cpf': '***.076.153-**'},
    {'posicao': 133, 'nome': 'THIAGO CICONELLO GIOVANETTI', 'cpf': '***.705.048-**'},
    {'posicao': 134, 'nome': 'MATEUS AURELIANO DA SILVA', 'cpf': '***.257.239-**'},
    {'posicao': 135, 'nome': 'SIMAM CARLOS BATISTA FERREIRA', 'cpf': '***.011.252-**'},
    {'posicao': 136, 'nome': 'HENRICO AUGUSTO LIMA LOPES', 'cpf': '***.973.248-**'},
    {'posicao': 137, 'nome': 'LAYARA BEATRIZ DOS SANTOS', 'cpf': '***.958.598-**'},
    {'posicao': 138, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 139, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 140, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 141, 'nome': 'GUSTAVO HENRIQUE BAUCH', 'cpf': '***.060.348-**'},
    {'posicao': 142, 'nome': 'VARDBELL RODRIGUES DOS SANTOS', 'cpf': '***.390.188-**'},
    {'posicao': 143, 'nome': 'GUSTAVO SCHIMIDT SANTOS', 'cpf': '***.053.488-**'},
    {'posicao': 144, 'nome': 'FERNANDO TERUMASA IKEDA SON', 'cpf': '***.875.388-**'},
    {'posicao': 145, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 146, 'nome': 'JOSYANE V', 'cpf': '***.489.872-**'},
    {'posicao': 147, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 148, 'nome': 'ISABELLY OGURI JORGE', 'cpf': '***.095.808-**'},
    {'posicao': 149, 'nome': 'ANDRE FERREIRA AGUIAR ALAMINO', 'cpf': '***.156.138-**'},
    {'posicao': 150, 'nome': 'FELIPE MARKS DA SILVA FERENSÓVICZ', 'cpf': '***.415.728-**'},
    {'posicao': 151, 'nome': 'ROSANA APARECIDA DOS SANTOS MATERA VERAS', 'cpf': '***.688.808-**'},
    {'posicao': 152, 'nome': 'DANILO DONIZETE LEANDRO', 'cpf': '***.578.048-**'},
    {'posicao': 153, 'nome': 'JONATAS DIEGO MARQUES', 'cpf': '***.388.618-**'},
    {'posicao': 154, 'nome': 'GUILHERME DUARTE MACHADO', 'cpf': '***.678.338-**'},
    {'posicao': 155, 'nome': 'GUILHERME REBOUCAS AMORIM', 'cpf': '***.925.158-**'},
    {'posicao': 156, 'nome': 'MIGUEL FIDENCIO AYRES', 'cpf': '***.438.038-**'},
    {'posicao': 157, 'nome': 'VITOR FERRAZ BLUMEN', 'cpf': '***.271.388-**'},
    {'posicao': 158, 'nome': 'VICTOR LOPES MARINS', 'cpf': '***.953.868-**'},
    {'posicao': 159, 'nome': 'JHENNIFER LARISSA ROSA PAINI', 'cpf': '***.093.158-**'},
    {'posicao': 160, 'nome': 'SANDY OLIVEIRA MESSIAS', 'cpf': '***.832.678-**'},
    {'posicao': 161, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 162, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 163, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 164, 'nome': 'ALEXANDRE SANCHES BONA', 'cpf': '***.605.808-**'},
    {'posicao': 165, 'nome': 'MARCEL MONTEIRO BALDUINO', 'cpf': '***.801.468-**'},
    {'posicao': 166, 'nome': 'NICOLE JANINE BOLZANI OLIVEIRA', 'cpf': '***.303.578-**'},
    {'posicao': 167, 'nome': 'VITOR MEIRA ALVES', 'cpf': '***.126.668-**'},
    {'posicao': 168, 'nome': 'PEDRO ALBERTTE DO CARMO NETO', 'cpf': '***.598.478-**'},
    {'posicao': 169, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 170, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 171, 'nome': 'LUCAS PIRES DE ALMEIDA', 'cpf': '***.223.318-**'},
    {'posicao': 172, 'nome': 'LEILA APARECIDA DE LIMA', 'cpf': '***.664.258-**'},
    {'posicao': 173, 'nome': 'MIRELLA XAVIER GALINDO', 'cpf': '***.482.048-**'},
    {'posicao': 174, 'nome': 'NELSON TADEU NUNES DE OLIVEIRA DO NASCIM', 'cpf': '***.714.138-**'},
    {'posicao': 175, 'nome': 'N & D CONTRUTORES', 'cpf': '49.551.066/0001-69'},
    {'posicao': 176, 'nome': 'TAYNARA MARTINS DUARTE', 'cpf': '***.785.838-**'},
    {'posicao': 177, 'nome': 'MATHEUS MORAIS KAWAMURA', 'cpf': '***.607.968-**'},
    {'posicao': 178, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 179, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 180, 'nome': 'CHRISTIAN DA SILVA PEREIRA', 'cpf': '***.675.888-**'},
    {'posicao': 181, 'nome': 'DANILO DE OLIVERIA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 182, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 183, 'nome': 'LUIZ GUSTAVO MACHADO', 'cpf': '***.195.518-**'},
    {'posicao': 184, 'nome': 'JOAO VITOR DE CAMARGO BARROS', 'cpf': '***.513.388-**'},
    {'posicao': 185, 'nome': 'GABRIEL CASTILHO MEDEIROS DE SOUZA', 'cpf': '***.364.088-**'},
    {'posicao': 186, 'nome': 'EDUARDO ALBERTO VIEIRA', 'cpf': '***.724.998-**'},
    {'posicao': 187, 'nome': 'FELIPE VINICIUS GONCALVES DOS REIS', 'cpf': '***.616.758-**'},
    {'posicao': 188, 'nome': 'MARLON BIANC VIEIRA FIGUEIREDO', 'cpf': '***.521.068-**'},
    {'posicao': 189, 'nome': 'PAULO ALVES MOREIRA JUNIOR', 'cpf': '***.778.968-**'},
    {'posicao': 190, 'nome': 'CAMILO OLIVEIRA DE FREITAS', 'cpf': '***.585.578-**'},
    {'posicao': 191, 'nome': 'EDSON VITOR PALDINI', 'cpf': '***.907.508-**'},
    {'posicao': 192, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 193, 'nome': 'PAULO RENATO DE JESUS BARBOSA', 'cpf': '***.271.907-**'},
    {'posicao': 194, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 195, 'nome': 'GABRIELLA FERNANDA PIERAMI', 'cpf': '***.935.418-**'},
    {'posicao': 196, 'nome': 'JOSÉ MARÍA MARTINS JUNIOR', 'cpf': '***.655.428-**'},
    {'posicao': 197, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 198, 'nome': 'JACKSON ROGÉRIO DA CRUZ', 'cpf': '***.069.868-**'},
    {'posicao': 199, 'nome': 'AMADOR BUENO DE OLIVEIRA NETO', 'cpf': '***.548.238-**'},
    {'posicao': 200, 'nome': 'BRENDA BIRAL BATISTA', 'cpf': '***.430.818-**'},
    {'posicao': 201, 'nome': 'NICOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 202, 'nome': 'JOAO VICTOR QUARESMA DE ARRUDA', 'cpf': '***.320.128-**'},
    {'posicao': 203, 'nome': 'GUILHERME ANTONIO DE ANDRADE', 'cpf': '***.820.208-**'},
    {'posicao': 204, 'nome': 'JACKSON HEBERT SANTOS', 'cpf': '***.868.628-**'},
    {'posicao': 205, 'nome': 'ALMENIA MARIA CRISTINA DE SOUZA MENCACCI', 'cpf': '***.476.868-**'},
    {'posicao': 206, 'nome': 'KAUAN DIAS GARCIA BARBOSA', 'cpf': '***.503.868-**'},
    {'posicao': 207, 'nome': 'DEBORA FRAGOSO TEOFILO DOS SANTOS', 'cpf': '***.694.388-**'},
    {'posicao': 208, 'nome': 'JULIA M J ALVES SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 209, 'nome': 'CAUA G BEZERRA SILVA', 'cpf': '***.369.208-**'},
    {'posicao': 210, 'nome': 'HENRIQUE VIDOTTO VINICO NETO', 'cpf': '***.292.128-**'},
    {'posicao': 211, 'nome': 'CAIO CESAR MARTINS DE LIMA', 'cpf': '***.943.768-**'},
    {'posicao': 212, 'nome': 'BRUNO FELIPE SOUZA ARAUJO', 'cpf': '***.240.388-**'},
    {'posicao': 213, 'nome': 'MIGUEL FELIPE DOS SANTOS GOUVEA', 'cpf': '***.993.238-**'},
    {'posicao': 214, 'nome': 'JESSICA CAROLINE LATANCE', 'cpf': '***.440.858-**'},
    {'posicao': 215, 'nome': 'MARCO TULIO DUENAS', 'cpf': '***.415.798-**'},
    {'posicao': 216, 'nome': 'FELIPE PAES DA SILVA', 'cpf': '***.762.688-**'},
    {'posicao': 217, 'nome': 'SIMONE CRISTINA DIAS', 'cpf': '***.796.618-**'},
    {'posicao': 218, 'nome': 'PETERSON ALVES PEREIRA', 'cpf': '***.310.166-**'},
    {'posicao': 219, 'nome': 'LEONARDO CARDOSO FRAIOLLI', 'cpf': '***.658.398-**'},
    {'posicao': 220, 'nome': 'MARIA EDUARDA MORENO LOPES', 'cpf': '***.335.888-**'},
    {'posicao': 221, 'nome': 'MATHEUS COSTA CAETANO PINTO', 'cpf': '***.393.090-**'},
    {'posicao': 222, 'nome': 'ROSELAINE SOUZA MESASHI', 'cpf': '***.697.538-**'},
    {'posicao': 223, 'nome': 'PEDRO H CARDOSO', 'cpf': '***.019.588-**'},
    {'posicao': 224, 'nome': 'MICHELE RIBEIRO DA CRUZ', 'cpf': '***.033.839-**'},
    {'posicao': 225, 'nome': 'DAVI COSTA DELAVIA', 'cpf': '***.829.368-**'},
    {'posicao': 226, 'nome': 'MATHEUS STROMBECK MORAES', 'cpf': '***.128.878-**'},
    {'posicao': 227, 'nome': 'DIANA SIQUEIRA LIBERATTI', 'cpf': '***.616.269-**'},
    {'posicao': 228, 'nome': 'GABRIELA PEREIRA DO PRADO', 'cpf': '***.352.918-**'},
    {'posicao': 229, 'nome': 'NILSON DE SOUZA COSTA', 'cpf': '***.363.206-**'},
    {'posicao': 230, 'nome': 'MARCOS MARTINS MENEGHETTI', 'cpf': '***.876.468-**'},
    {'posicao': 231, 'nome': 'JOVANA ARCINE DOMINGUES', 'cpf': '***.631.198-**'},
    {'posicao': 232, 'nome': 'LETÍCIA VITÓRIA DOS SANTOS SILVA', 'cpf': '***.057.198-**'},
    {'posicao': 233, 'nome': 'ALINE GABRIELE VALIM', 'cpf': '***.123.268-**'},
    {'posicao': 234, 'nome': 'PATRICK FERNANDES', 'cpf': '***.207.448-**'},
    {'posicao': 235, 'nome': 'BIANCA PICHIRILO VERGUEIRO BENATTI', 'cpf': '***.498.018-**'},
    {'posicao': 236, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 237, 'nome': 'GUILHERME VINICIUS BAEZA DE OLIVEIRA', 'cpf': '***.952.258-**'},
    {'posicao': 238, 'nome': 'GUILHERME ANTONIO RODRIGUES DA COSTA', 'cpf': '***.144.268-**'},
    {'posicao': 239, 'nome': 'GABRIEL ALCANTARA DIAS PRESTES', 'cpf': '***.224.798-**'},
    {'posicao': 240, 'nome': 'GUILHERME PAZETTI DE OLIVEIRA', 'cpf': '***.198.588-**'},
    {'posicao': 241, 'nome': 'JOAO GABRIEL MILONE VILELA DE CAMARGO', 'cpf': '***.245.718-**'},
    {'posicao': 242, 'nome': 'WENDEL MAXIMO VIEIRA', 'cpf': '***.826.178-**'},
    {'posicao': 243, 'nome': 'GUILHERME AUGUSTO GOMES ARRIBAMAR', 'cpf': '***.264.638-**'},
    {'posicao': 244, 'nome': 'MARCUS VINICIUS CARDOSO DE FREITAS', 'cpf': '***.378.768-**'},
    {'posicao': 245, 'nome': 'ALLAN WANDREY QUEIROZ', 'cpf': '***.395.008-**'},
    {'posicao': 246, 'nome': 'CAMILA MARTINS QUEIROZ', 'cpf': '***.530.648-**'},
    {'posicao': 247, 'nome': 'PATRICIA DE FIGUEIREDO RIBEIRO', 'cpf': '***.038.728-**'},
    {'posicao': 248, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 249, 'nome': 'FABIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 250, 'nome': 'PEDRO SILVA MARTINS', 'cpf': '***.245.268-**'},
    {'posicao': 251, 'nome': 'LEONARDO VIEIRA DA COSTA', 'cpf': '***.794.518-**'},
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

# Centraliza o botão de busca na mesma coluna do 2º lugar
c_btn1, c_btn2, c_btn3 = st.columns([1,1,1])
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

# 6. Botões de destaque: 1º Lugar, 2º Lugar e Sorteio (vídeo)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #333;'>Destaques</h3>", unsafe_allow_html=True)

btn_col1, btn_col2, btn_col3 = st.columns([1,1,1])

with btn_col1:
    if st.button("1º Lugar"):
        primeiro = next((u for u in ranking_db if u['posicao'] == 1), None)
        if primeiro:
            st.markdown(f"""
                <div class="vencedor-card">
                    <div style='font-size:22px; color:#8A05BE; font-weight:700;'>🏆 1º Lugar</div>
                    <div style='margin-top:8px; font-size:18px; color:#333;'><strong>{primeiro['nome']}</strong></div>
                    <div style='margin-top:6px; font-size:14px; color:#666;'>CPF: <strong>{primeiro['cpf']}</strong></div>
                    <div style='margin-top:6px; font-size:14px; color:#666;'>Posição: <span class="destaque">{primeiro['posicao']}º lugar</span></div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Ainda não há 1º lugar definido.")

with btn_col2:
    if st.button("2º Lugar"):
        segundo = next((u for u in ranking_db if u['posicao'] == 2), None)
        if segundo:
            st.markdown(f"""
                <div class="vencedor-card" style='background-color:#E3F2FD; border-color:#64B5F6;'>
                    <div style='font-size:20px; color:#0277BD; font-weight:700;'>🥈 2º Lugar</div>
                    <div style='margin-top:8px; font-size:16px; color:#333;'><strong>{segundo['nome']}</strong></div>
                    <div style='margin-top:6px; font-size:14px; color:#666;'>CPF: <strong>{segundo['cpf']}</strong></div>
                    <div style='margin-top:6px; font-size:14px; color:#666;'>Posição: <span class="destaque">{segundo['posicao']}º lugar</span></div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Ainda não há 2º lugar definido.")

with btn_col3:
    if st.button("Sorteio"):
        # Procura por arquivos .mp4 na pasta do app e reproduz o primeiro encontrado
        mp4_files = glob.glob("*.mp4")
        preferred = "sorteio.mp4"
        video_to_play = None
        if preferred in mp4_files:
            video_to_play = preferred
        elif mp4_files:
            # ordena para estabilidade e escolhe o primeiro
            mp4_files.sort()
            video_to_play = mp4_files[0]

        if video_to_play:
            try:
                st.video(video_to_play)
            except Exception:
                st.error(f"Erro ao reproduzir o vídeo '{video_to_play}'.")
        else:
            st.info("Nenhum arquivo MP4 encontrado no diretório do app. Faça upload de 'sorteio.mp4' ou adicione um .mp4.")

        # Card do ganhador do sorteio (exibe sempre ao clicar em Sorteio)
        st.markdown(f"""
            <div class="vencedor-card" style='background: linear-gradient(90deg,#fff3e0,#fff9c4); border-color:#FFB300;'>
                <div style='font-size:20px; font-weight:700;'>🎉 Ganhador do Sorteio</div>
                <div style='margin-top:8px; font-size:18px; color:#333;'><strong>VINÍCIUS GAMA DE FRANÇA</strong></div>
                <div style='margin-top:6px; font-size:14px; color:#666;'>CPF: <strong>•••.358.148-••</strong></div>
            </div>
        """, unsafe_allow_html=True)

# 5. Rodapé
st.markdown("""
    <div class="footer-text">
        Atualizado em 04/10/2026<br>
        <strong>Promoção Finalizada </strong>
    </div>
""", unsafe_allow_html=True)
