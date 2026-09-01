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
    {'posicao': 1, 'nome': 'IGOR WENDEL AMARAL', 'cpf': '***.109.578-**'},
    {'posicao': 2, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 3, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 4, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 5, 'nome': 'BRUNO BERTIN VITORIN', 'cpf': '***.804.368-**'},
    {'posicao': 6, 'nome': 'MATEUS CARDOSO PIRES', 'cpf': '***.179.968-**'},
    {'posicao': 7, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 8, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 9, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 10, 'nome': 'LUCAS CAMELO', 'cpf': '***.754.708-**'},
    {'posicao': 11, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 12, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 13, 'nome': 'ANA BEATRIZ MATOS VIANA', 'cpf': '***.863.088-**'},
    {'posicao': 14, 'nome': 'GIOVANNI DE SOUZA SANTOS', 'cpf': '***.126.928-**'},
    {'posicao': 15, 'nome': 'LUIZA DOS ANJOS OLIVEIRA', 'cpf': '***.469.738-**'},
    {'posicao': 16, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 17, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 18, 'nome': 'MURILO COELHO DOS SANTOS', 'cpf': '***.585.008-**'},
    {'posicao': 19, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 20, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 21, 'nome': 'TAMARA DE ASSIS', 'cpf': '***.376.378-**'},
    {'posicao': 22, 'nome': 'LETICIA PEREIRA', 'cpf': '***.745.188-**'},
    {'posicao': 23, 'nome': 'PRISCILA S K CORREA', 'cpf': '***.553.718-**'},
    {'posicao': 24, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 25, 'nome': 'RYAN PIETRO CONSOLARI', 'cpf': '***.356.588-**'},
    {'posicao': 26, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 27, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 28, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 29, 'nome': 'DOUGLAS RAFAEL ASSIS MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 30, 'nome': 'RODOLFO ANTUNES DE ALMEIDA', 'cpf': '***.685.268-**'},
    {'posicao': 31, 'nome': 'MIGUEL COELHO EVANGELISTA DOS SANTOS', 'cpf': '***.691.478-**'},
    {'posicao': 32, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 33, 'nome': 'MATHEUS MORAIS KAWAMURA', 'cpf': '***.607.968-**'},
    {'posicao': 34, 'nome': 'VICTOR AUGUSTO DE SOUZA', 'cpf': '***.913.138-**'},
    {'posicao': 35, 'nome': 'KENNEDY MAKOTO YOSHIDA DOS SANTOS', 'cpf': '***.056.259-**'},
    {'posicao': 36, 'nome': 'MATEUS FERNANDES ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 37, 'nome': 'FELIPE MENDES BALOTIM', 'cpf': '***.576.988-**'},
    {'posicao': 38, 'nome': 'BRYAN FRANCA SOARES', 'cpf': '***.447.638-**'},
    {'posicao': 39, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 40, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 41, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 42, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 43, 'nome': 'EVELIN DAYANE CAVALCANTE', 'cpf': '***.351.418-**'},
    {'posicao': 44, 'nome': 'DANILO DE OLIVERIA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 45, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 46, 'nome': 'RAFAEL FRANCISCO LARA DE OLIVEIRA', 'cpf': '***.543.308-**'},
    {'posicao': 47, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 48, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 49, 'nome': 'GABRIELA FREITAS RIBEIRO', 'cpf': '***.904.968-**'},
    {'posicao': 50, 'nome': 'THAFARO WESLLEY NOGUEIRA PAES', 'cpf': '***.955.418-**'},
    {'posicao': 51, 'nome': 'JAQUELINE CLARA GUTIERREZ BRESIO', 'cpf': '***.333.108-**'},
    {'posicao': 52, 'nome': 'RODRIGO OLIVEIRA DA ROCHA', 'cpf': '***.086.868-**'},
    {'posicao': 53, 'nome': 'FELIPE MARKS DA SILVA FERENSÓVICZ', 'cpf': '***.415.728-**'},
    {'posicao': 54, 'nome': 'EMELSON OLIVEIRA MELO FROES', 'cpf': '***.515.478-**'},
    {'posicao': 55, 'nome': 'CAIO GUILHERME PEREIRA DOS SANTOS KITAGAKI', 'cpf': '***.590.628-**'},
    {'posicao': 56, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 57, 'nome': 'LAURA DE ALMEIDA FOGACA', 'cpf': '***.329.568-**'},
    {'posicao': 58, 'nome': 'ADEILTON ALVES BOSCARDIN', 'cpf': '***.449.378-**'},
    {'posicao': 59, 'nome': 'DOUGLAS HENRIQUE DOS SANTOS', 'cpf': '***.296.668-**'},
    {'posicao': 60, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 61, 'nome': 'CLEBER OLIVEIRA DA SILVA', 'cpf': '***.719.038-**'},
    {'posicao': 62, 'nome': 'MARIA EDUARDA FERNANDES RIBEIRO', 'cpf': '***.654.718-**'},
    {'posicao': 63, 'nome': 'MARIA EDUARDA MORAIS OIKAWA', 'cpf': '***.300.368-**'},
    {'posicao': 64, 'nome': 'DOUGLAS RAFAEL DE SOUSA MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 65, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 66, 'nome': 'LUCAS SILVA PERES', 'cpf': '***.249.118-**'},
    {'posicao': 67, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 68, 'nome': 'LISANDRA FERNANDA DE GODOI', 'cpf': '***.048.668-**'},
    {'posicao': 69, 'nome': 'THIAGO SCHIMIDT MACHADO', 'cpf': '***.898.288-**'},
    {'posicao': 70, 'nome': 'HENRICO AUGUSTO LIMA LOPES', 'cpf': '***.973.248-**'},
    {'posicao': 71, 'nome': 'PAULO HENRIQUE VERRI RUFINO', 'cpf': '***.859.068-**'},
    {'posicao': 72, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 73, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 74, 'nome': 'ANA BEATRIZ CONCEICAO A CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 75, 'nome': 'VITOR FERRAZ BLUMEN', 'cpf': '***.271.388-**'},
    {'posicao': 76, 'nome': 'PAULO ALVES MOREIRA JUNIOR', 'cpf': '***.778.968-**'},
    {'posicao': 77, 'nome': 'LUIZ GUSTAVO GOMES', 'cpf': '***.130.118-**'},
    {'posicao': 78, 'nome': 'POLYANNA PIRES PASCHOAL', 'cpf': '***.942.958-**'},
    {'posicao': 79, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 80, 'nome': 'NICOLAS SILVA PREVIATO', 'cpf': '***.392.738-**'},
    {'posicao': 81, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 82, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 83, 'nome': 'CAIO HENRIQUE LEME SANTOS', 'cpf': '***.290.728-**'},
    {'posicao': 84, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 85, 'nome': 'JOSÉ MARÍA MARTINS JUNIOR', 'cpf': '***.655.428-**'},
    {'posicao': 86, 'nome': 'SERGIO DOMINGOS RODRIGUES SAMPAIO', 'cpf': '***.710.718-**'},
    {'posicao': 87, 'nome': 'LUCCAS MATHEUS BARBOSA CRUZ', 'cpf': '***.836.468-**'},
    {'posicao': 88, 'nome': 'LAURA DE ALMEIDA FOGAÇA', 'cpf': '***.329.568-**'},
    {'posicao': 89, 'nome': 'ABNER MARTINS DE CAMARGO', 'cpf': '***.241.638-**'},
    {'posicao': 90, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 91, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 92, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 93, 'nome': 'CICERA MARIA COELHO DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 94, 'nome': 'WENDELL CONTE JOSEFIK', 'cpf': '***.732.498-**'},
    {'posicao': 95, 'nome': 'LEONARDO VINÍCIUS RUIZ RONDELIS', 'cpf': '***.079.718-**'},
    {'posicao': 96, 'nome': 'GUSTAVO SCHIMIDT SANTOS', 'cpf': '***.053.488-**'},
    {'posicao': 97, 'nome': 'JORGE PEDROSO DE MORAIS NETO', 'cpf': '***.540.928-**'},
    {'posicao': 98, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 99, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 100, 'nome': 'WESLEY DE OLIVEIRA SANTOS', 'cpf': '***.977.388-**'},
    {'posicao': 101, 'nome': 'GABRIELLA FERNANDA PIERAMI', 'cpf': '***.935.418-**'},
    {'posicao': 102, 'nome': 'EDUARDO VIEIRA RIBEIRO DA SILVA', 'cpf': '***.475.388-**'},
    {'posicao': 103, 'nome': 'FABRICIO DA ROSA SOICA', 'cpf': '***.362.448-**'},
    {'posicao': 104, 'nome': 'EDUARDO APARECIDO BLUMEN', 'cpf': '***.093.858-**'},
    {'posicao': 105, 'nome': 'ARTHUR ROGÉRIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 106, 'nome': 'ALISON CARRIEL ROCHA', 'cpf': '***.626.128-**'},
    {'posicao': 107, 'nome': 'SANDY OLIVEIRA MESSIAS', 'cpf': '***.832.678-**'},
    {'posicao': 108, 'nome': 'MARCO ANTONIO ALVES', 'cpf': '***.706.658-**'},
    {'posicao': 109, 'nome': 'GABRIEL PEDROSO DE GOES VIEIRA', 'cpf': '***.869.898-**'},
    {'posicao': 110, 'nome': 'FÁBIO BLAS MASUELA', 'cpf': '***.731.318-**'},
    {'posicao': 111, 'nome': 'LUIZ CARLOS DA SILVA BUENO', 'cpf': '***.273.528-**'},
    {'posicao': 112, 'nome': 'VICTOR HUGO DIAS MODESTO', 'cpf': '***.282.068-**'},
    {'posicao': 113, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 114, 'nome': 'MARCO TULIO DUENAS', 'cpf': '***.415.798-**'},
    {'posicao': 115, 'nome': 'FELIPE VINICIUS GONCALVES DOS REIS', 'cpf': '***.616.758-**'},
    {'posicao': 116, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 117, 'nome': 'JOSYANE V', 'cpf': '***.489.872-**'},
    {'posicao': 118, 'nome': 'LEANDRO TEODORO POLERA', 'cpf': '***.565.548-**'},
    {'posicao': 119, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 120, 'nome': 'VINÍCIUS GAMA DE FRANÇA', 'cpf': '***.358.148-**'},
    {'posicao': 121, 'nome': 'JOVANA ARCINE DOMINGUES', 'cpf': '***.631.198-**'},
    {'posicao': 122, 'nome': 'GABRIEL ALCANTARA DIAS PRESTES', 'cpf': '***.224.798-**'},
    {'posicao': 123, 'nome': 'SOPHIA CASTILHO MORENO', 'cpf': '***.497.218-**'},
    {'posicao': 124, 'nome': 'JOAO VITOR DE CAMARGO BARROS', 'cpf': '***.513.388-**'},
    {'posicao': 125, 'nome': 'JULIA M J ALVES SANTOS', 'cpf': '***.363.038-**'},
    {'posicao': 126, 'nome': 'FELIPE HASHIMOTO FENGLER', 'cpf': '***.139.658-**'},
    {'posicao': 127, 'nome': 'GUILHERME VINICIUS BAEZA DE OLIVEIRA', 'cpf': '***.952.258-**'},
    {'posicao': 128, 'nome': 'BRASILIO DEMETRIO MARCOS', 'cpf': '***.590.648-**'},
    {'posicao': 129, 'nome': 'SIMAM CARLOS BATISTA FERREIRA', 'cpf': '***.011.252-**'},
    {'posicao': 130, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 131, 'nome': 'HELLEN NUNES', 'cpf': '***.123.355-**'},
    {'posicao': 132, 'nome': 'ALLAN WANDREY QUEIROZ', 'cpf': '***.395.008-**'},
    {'posicao': 133, 'nome': 'CAMILA ALESSANDRA B MAURO', 'cpf': '***.359.488-**'},
    {'posicao': 134, 'nome': 'MIGUEL FIDENCIO AYRES', 'cpf': '***.438.038-**'},
    {'posicao': 135, 'nome': 'DANIEL DE FREITAS ESTEVES DA COSTA', 'cpf': '***.311.778-**'},
    {'posicao': 136, 'nome': 'VICTOR LOPES MARINS', 'cpf': '***.953.868-**'},
    {'posicao': 137, 'nome': 'MARCEL MONTEIRO BALDUINO', 'cpf': '***.801.468-**'},
    {'posicao': 138, 'nome': 'JOSIMAR LAURENTINO DOS SANTOS JUNIOR', 'cpf': '***.101.528-**'},
    {'posicao': 139, 'nome': 'MIRELLA XAVIER GALINDO', 'cpf': '***.482.048-**'},
    {'posicao': 140, 'nome': 'MIGUEL FELIPE DOS SANTOS GOUVEA', 'cpf': '***.993.238-**'},
    {'posicao': 141, 'nome': 'TIAGO MARTINS DOMINGUES', 'cpf': '***.241.908-**'},
    {'posicao': 142, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 143, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 144, 'nome': 'KENNEDY MAKOTO YOSHIDA SANTOS', 'cpf': '***.056.259-**'},
    {'posicao': 145, 'nome': 'NICOLE FAVA PIRES', 'cpf': '***.051.518-**'},
    {'posicao': 146, 'nome': 'HENRY CAMILLO BERNEGOZZI', 'cpf': '***.002.618-**'},
    {'posicao': 147, 'nome': 'BRUNO RAFAEL DE CARVALHO CAVALCANTE', 'cpf': '***.161.708-**'},
    {'posicao': 148, 'nome': 'BRUNO B VITORINO', 'cpf': '***.804.368-**'},
    {'posicao': 149, 'nome': 'WENDEL MAXIMO VIEIRA', 'cpf': '***.826.178-**'},
    {'posicao': 150, 'nome': 'ANDRÉ FERREIRA AGUIAR ALAMINO', 'cpf': '***.156.138-**'},
    {'posicao': 151, 'nome': 'REGINA MARIA DE CASTILHO TRINDADE', 'cpf': '***.345.278-**'},
    {'posicao': 152, 'nome': 'RICARDO HERNAN SARAVIA SIQUEIRA', 'cpf': '***.988.378-**'},
    {'posicao': 153, 'nome': 'ISABELLY OGURI JORGE', 'cpf': '***.095.808-**'},
    {'posicao': 154, 'nome': 'ROSANA APARECIDA DOS SANTOS MATERA VERAS', 'cpf': '***.688.808-**'},
    {'posicao': 155, 'nome': 'PEDRO VALADARES JUNIOR', 'cpf': '***.076.153-**'},
    {'posicao': 156, 'nome': 'JULIANA MACHADO RIBEIRO', 'cpf': '***.945.278-**'},
    {'posicao': 157, 'nome': 'JULIETE SANTOS DE LIMA', 'cpf': '***.387.358-**'},
    {'posicao': 158, 'nome': 'ALEXANDRE SANCHES BONA', 'cpf': '***.605.808-**'},
    {'posicao': 159, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 160, 'nome': 'CLAYTON FIGUEIREDO MAIA', 'cpf': '***.848.728-**'},
    {'posicao': 161, 'nome': 'LETÍCIA VITÓRIA DOS SANTOS SILVA', 'cpf': '***.057.198-**'},
    {'posicao': 162, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 163, 'nome': 'GUSTAVO HENRIQUE BAUCH', 'cpf': '***.060.348-**'},
    {'posicao': 164, 'nome': 'FERNANDO TERUMASA IKEDA SON', 'cpf': '***.875.388-**'},
    {'posicao': 165, 'nome': 'DANILO ALBERTO DA SILVA FERNANDES', 'cpf': '***.555.889-**'},
    {'posicao': 166, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 167, 'nome': 'CESAR HENRIQUE C DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 168, 'nome': 'HERIVELTON HENRIQUE GONÇALVES', 'cpf': '***.607.418-**'},
    {'posicao': 169, 'nome': 'EDSON VITOR PALDINI', 'cpf': '***.907.508-**'},
    {'posicao': 170, 'nome': 'LAURA DA SILVA SEGANTIN', 'cpf': '***.300.358-**'},
    {'posicao': 171, 'nome': 'TIAGO DE SOUZA SANTOS', 'cpf': '***.259.568-**'},
    {'posicao': 172, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 173, 'nome': 'MARIANA BORGES CURVÊLO DA SILVA DE PAULA LIMA', 'cpf': '***.084.428-**'},
    {'posicao': 174, 'nome': 'ALEX VITOR FRUCTOS', 'cpf': '***.306.028-**'},
    {'posicao': 175, 'nome': 'SABRINA CRISTINA P VITORINO', 'cpf': '***.299.258-**'},
    {'posicao': 176, 'nome': 'MARIA LUIZA SCHNEIDER', 'cpf': '***.331.068-**'},
    {'posicao': 177, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 178, 'nome': 'OSIEL JOSE DE PROENCA', 'cpf': '***.203.338-**'},
    {'posicao': 179, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 180, 'nome': 'CARLOS EDUARDO MILAN FERREIRA', 'cpf': '***.249.918-**'},
    {'posicao': 181, 'nome': 'MATEUS SILVA DALMARCO', 'cpf': '***.839.838-**'},
    {'posicao': 182, 'nome': 'BIANCA DIEBE', 'cpf': '***.838.758-**'},
    {'posicao': 183, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'},
    {'posicao': 184, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 185, 'nome': 'DANILO INÁCIO DE ARAÚJO VISNÓVESKI', 'cpf': '***.318.148-**'},
    {'posicao': 186, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 187, 'nome': 'BRUNO CORREA DA SILVA', 'cpf': '***.342.418-**'},
    {'posicao': 188, 'nome': 'BARBARA CAROLINE TRINDADE', 'cpf': '***.401.418-**'},
    {'posicao': 189, 'nome': 'DAIANE KELLY DE ALMEIDA CAMARGO', 'cpf': '***.582.228-**'},
    {'posicao': 190, 'nome': 'NICOLAS CONSTANÇA MENTONE', 'cpf': '***.154.108-**'},
    {'posicao': 191, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 192, 'nome': 'GABRIEL CASTILHO MEDEIROS DE SOUZA', 'cpf': '***.364.088-**'},
    {'posicao': 193, 'nome': 'DANIEL APARECIDO DE OLIVEIRA SANTOS', 'cpf': '***.556.668-**'},
    {'posicao': 194, 'nome': 'CRISTIAN RIBEIRO DE CAMARGO', 'cpf': '***.330.638-**'},
    {'posicao': 195, 'nome': 'CAUA G BEZERRA SILVA', 'cpf': '***.369.208-**'},
    {'posicao': 196, 'nome': 'LUCAS PIRES DE ALMEIDA', 'cpf': '***.223.318-**'},
    {'posicao': 197, 'nome': 'MATEUS AURELIANO DA SILVA', 'cpf': '***.257.239-**'},
    {'posicao': 198, 'nome': 'CICERA MARIA C DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 199, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 200, 'nome': 'CRISTIANO VALERIO TAVERA CORDEIRO', 'cpf': '***.052.251-**'},
    {'posicao': 201, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 202, 'nome': 'LEONARDO CARDOSO FRAIOLLI', 'cpf': '***.658.398-**'},
    {'posicao': 203, 'nome': 'RAFAEL DA COSTA CASTRO', 'cpf': '***.429.148-**'},
    {'posicao': 204, 'nome': 'SANDRO APARECIDO NOGUEIRA', 'cpf': '***.866.808-**'},
    {'posicao': 205, 'nome': 'PRISCILA NORONHA MENDES', 'cpf': '***.687.188-**'},
    {'posicao': 206, 'nome': 'GUSTAVO DE CAMPOS ANTUNES', 'cpf': '***.326.288-**'},
    {'posicao': 207, 'nome': 'ALEXANDRE DIAS GOMES', 'cpf': '***.552.908-**'},
    {'posicao': 208, 'nome': 'CAUÃ GABRIEL BEZERRA DA SILVA', 'cpf': '***.369.208-**'},
    {'posicao': 209, 'nome': 'CAMILO OLIVEIRA DE FREITAS', 'cpf': '***.585.578-**'},
    {'posicao': 210, 'nome': 'MARIA EDUARDA MORENO LOPES', 'cpf': '***.335.888-**'},
    {'posicao': 211, 'nome': 'JUAN LUCAS DA SILVA', 'cpf': '***.632.726-**'},
    {'posicao': 212, 'nome': 'ROBERTA THAIS FERNANDES RIBEIRO', 'cpf': '***.584.468-**'},
    {'posicao': 213, 'nome': 'TIAGO ALVES SIMOES', 'cpf': '***.528.818-**'},
    {'posicao': 214, 'nome': 'GUILHERME AUGUSTO GOMES ARRIBAMAR', 'cpf': '***.264.638-**'},
    {'posicao': 215, 'nome': 'CRISTIANO NEVES DE BRITO', 'cpf': '***.965.945-**'},
    {'posicao': 216, 'nome': 'NATALIA SILVEIRA TOLEDO', 'cpf': '***.003.228-**'},
    {'posicao': 217, 'nome': 'MATHEUS COSTA CAETANO PINTO', 'cpf': '***.393.090-**'},
    {'posicao': 218, 'nome': 'CÉSAR HENRIQUE CAMARGO DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 219, 'nome': 'ADMILSON DE GODOI', 'cpf': '***.777.758-**'},
    {'posicao': 220, 'nome': 'ALMENIA MARIA CRISTINA DE SOUZA MENCACCI', 'cpf': '***.476.868-**'},
    {'posicao': 221, 'nome': 'ADEMAR SOARES C BRANCO', 'cpf': '***.420.347-**'},
    {'posicao': 222, 'nome': 'KEILLA FRANCINE CARDOSO DA SILVA', 'cpf': '***.374.618-**'},
    {'posicao': 223, 'nome': 'GABRIELA MARIA RODRIGUES DE MORAIS', 'cpf': '***.115.838-**'},
    {'posicao': 224, 'nome': 'GABRIEL YUJI SHIMODA VIEIRA', 'cpf': '***.802.918-**'},
    {'posicao': 225, 'nome': 'ABEL PEDRO DA SILVA JUNIOR', 'cpf': '***.712.338-**'},
    {'posicao': 226, 'nome': 'GABRIEL HENRIQUE SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 227, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 228, 'nome': 'NILSON DE SOUZA COSTA', 'cpf': '***.363.206-**'},
    {'posicao': 229, 'nome': 'PETERSON ALVES PEREIRA', 'cpf': '***.310.166-**'},
    {'posicao': 230, 'nome': 'GUILHERME ANTÓNIO RIBAS NOBREGA', 'cpf': '***.706.988-**'},
    {'posicao': 231, 'nome': 'ESTEFANI MARQUES ROSA', 'cpf': '***.156.118-**'},
    {'posicao': 232, 'nome': 'ALANIS APARECIDA LAUREANO DOMINGUES', 'cpf': '***.141.748-**'},
    {'posicao': 233, 'nome': 'ALISON FERNANDES SANTOS', 'cpf': '***.715.938-**'},
    {'posicao': 234, 'nome': 'ANA BEATRIZ CONCEICAO APARECIDA CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 235, 'nome': 'DANIEL JOSE BERNARDES FILHO', 'cpf': '***.229.748-**'},
    {'posicao': 236, 'nome': 'SERGIO PINHEIRO XAVIER', 'cpf': '***.423.355-**'},
    {'posicao': 237, 'nome': 'MARCOS MARTINS MENEGHETTI', 'cpf': '***.876.468-**'},
    {'posicao': 238, 'nome': 'NICOLLAS MENCACCI PEREIRA', 'cpf': '***.757.358-**'},
    {'posicao': 239, 'nome': 'RAPHAEL CARDOZO CASTILHO', 'cpf': '***.652.058-**'},
    {'posicao': 240, 'nome': 'TALITA RAMOS LAURIANO AKYAMA', 'cpf': '***.427.478-**'},
    {'posicao': 241, 'nome': 'GUILHERME DUARTE MACHADO', 'cpf': '***.678.338-**'},
    {'posicao': 242, 'nome': 'CAIKE MIGUEL MURAMOTO', 'cpf': '***.265.538-**'},
    {'posicao': 243, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 244, 'nome': 'GISLAINE OLIVIERA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 245, 'nome': 'GABRIELI PEDROSO GONCALVES', 'cpf': '***.340.888-**'},
    {'posicao': 246, 'nome': 'FABIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 247, 'nome': 'LUIZ GUSTAVO MACHADO', 'cpf': '***.195.518-**'},
    {'posicao': 248, 'nome': 'FELIPE MATHEUS DO NASCIMENTO ANTUNES', 'cpf': '***.638.018-**'},
    {'posicao': 249, 'nome': 'CRISTIANE CANDIDO CORREA', 'cpf': '***.451.358-**'},
    {'posicao': 250, 'nome': 'RAPHAELLA CAMILLY L RODRIGUES', 'cpf': '***.706.918-**'},
    {'posicao': 251, 'nome': 'RAPHAELLA CAMILLY LUCAS RODRIGUES', 'cpf': '***.706.918-**'},
    {'posicao': 252, 'nome': 'ROSANA MORAIS ROQUE SAKAI', 'cpf': '***.036.248-**'},
    {'posicao': 253, 'nome': 'TIAGO FERNANDO DE ALMEIDA SANTOS', 'cpf': '***.995.688-**'}
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
                <div style='margin-top:8px; font-size:18px; color:#333;'><strong>FABIO LUIZ DE FRANCA FILHO</strong></div>
                <div style='margin-top:6px; font-size:14px; color:#666;'>CPF: <strong>•••.724.428-••</strong></div>
            </div>
        """, unsafe_allow_html=True)

# 5. Rodapé
st.markdown("""
    <div class="footer-text">
        Atualizado em 01/09/2026<br>
        <strong>Promoção Finalizada </strong>
    </div>
""", unsafe_allow_html=True)
