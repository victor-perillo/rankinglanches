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
    {'posicao': 1, 'nome': 'LAURA DA SILVA SEGANTIN', 'cpf': '***.300.358-**'},
    {'posicao': 2, 'nome': 'HUMBERTO PERES FLORES NETO', 'cpf': '***.717.048-**'},
    {'posicao': 3, 'nome': 'DANIEL CARVALHO', 'cpf': '***.889.108-**'},
    {'posicao': 5, 'nome': 'DIEGO APARECIDO CARVALHO ALBUQUERQUE', 'cpf': '***.590.618-**'},
    {'posicao': 6, 'nome': 'BRUNO BERTIN VITORINO', 'cpf': '***.804.368-**'},
    {'posicao': 7, 'nome': 'MATEUS CARDOSO PIRES', 'cpf': '***.179.968-**'},
    {'posicao': 8, 'nome': 'ALMENIA MARIA CRISTINA DE SOUZA MENCACCI', 'cpf': '***.476.868-**'},
    {'posicao': 9, 'nome': 'MARIA EDUARDA MADUREIRA RODRIGUES', 'cpf': '***.607.128-**'},
    {'posicao': 10, 'nome': 'PAULO APOLINARIO DE SOUZA', 'cpf': '***.105.848-**'},
    {'posicao': 11, 'nome': 'ARIANA OMURA VIEIRA', 'cpf': '***.092.708-**'},
    {'posicao': 12, 'nome': 'JONATAS DIEGO MARQUES', 'cpf': '***.388.618-**'},
    {'posicao': 13, 'nome': 'RAFAEL KAZUITI BORGES OGIHARA', 'cpf': '***.327.858-**'},
    {'posicao': 14, 'nome': 'RENATO AUGUSTO VIEIRA', 'cpf': '***.396.688-**'},
    {'posicao': 15, 'nome': 'DANILO WILLY MOREIRA TORRES', 'cpf': '***.034.898-**'},
    {'posicao': 16, 'nome': 'GIOVANNI DE SOUZA SANTOS', 'cpf': '***.126.928-**'},
    {'posicao': 17, 'nome': 'VAGNER RODRIGUES SAMPAIO', 'cpf': '***.943.698-**'},
    {'posicao': 18, 'nome': 'GABRIEL DE PAULA IZAIAS', 'cpf': '***.917.348-**'},
    {'posicao': 19, 'nome': 'TIAGO DE SOUZA SANTOS', 'cpf': '***.259.568-**'},
    {'posicao': 20, 'nome': 'LUCCAS MATHEUS BARBOSA CRUZ', 'cpf': '***.836.468-**'},
    {'posicao': 21, 'nome': 'MATHEUS BUENO SIRILO', 'cpf': '***.296.028-**'},
    {'posicao': 22, 'nome': 'IGOR WENDEL AMARAL', 'cpf': '***.109.578-**'},
    {'posicao': 23, 'nome': 'THAFARO WESLLEY NOGUEIRA PAES', 'cpf': '***.955.418-**'},
    {'posicao': 24, 'nome': 'GUSTAVO HENRIQUE DE OLIVEIRA LIMA', 'cpf': '***.204.738-**'},
    {'posicao': 25, 'nome': 'LUCAS SILVA PERES', 'cpf': '***.249.118-**'},
    {'posicao': 26, 'nome': 'BRUNO VINICIUS URIAS QUEIROZ', 'cpf': '***.522.708-**'},
    {'posicao': 27, 'nome': 'ANTHONNY COCUZZA', 'cpf': '***.196.318-**'},
    {'posicao': 28, 'nome': 'DOUGLAS RAFAEL DE SOUSA MENDES', 'cpf': '***.372.248-**'},
    {'posicao': 29, 'nome': 'MURILO COELHO DOS SANTOS', 'cpf': '***.585.008-**'},
    {'posicao': 30, 'nome': 'LAYARA BEATRIZ DOS SANTOS', 'cpf': '***.958.598-**'},
    {'posicao': 31, 'nome': 'CAIQUE ALEXANDRE DE OLIVEIRA', 'cpf': '***.362.908-**'},
    {'posicao': 32, 'nome': 'WALTER DE CAMARGO GRANGEIRO', 'cpf': '***.468.678-**'},
    {'posicao': 33, 'nome': 'ANA BEATRIZ CONCEICAO APARECIDA CORREA', 'cpf': '***.085.398-**'},
    {'posicao': 34, 'nome': 'GABRIELA FREITAS RIBEIRO', 'cpf': '***.904.968-**'},
    {'posicao': 35, 'nome': 'ADEILTON ALVES BOSCARDIN', 'cpf': '***.449.378-**'},
    {'posicao': 36, 'nome': 'GUILHERME OTO VENTURELLI', 'cpf': '***.979.058-**'},
    {'posicao': 37, 'nome': 'JOAO HENRIQUE CRIVELLI RODRIGUES DE SOUZA', 'cpf': '***.551.998-**'},
    {'posicao': 38, 'nome': 'LUCAS GOMES SILVA', 'cpf': '***.480.821-**'},
    {'posicao': 39, 'nome': 'DIEGO GONCALVES DEMANI', 'cpf': '***.760.138-**'},
    {'posicao': 40, 'nome': 'RAFAEL SARTORI DA COSTA', 'cpf': '***.841.938-**'},
    {'posicao': 41, 'nome': 'SOPHIA CASTILHO MORENO', 'cpf': '***.497.218-**'},
    {'posicao': 42, 'nome': 'DANILO DE OLIVEIRA BARROSO', 'cpf': '***.127.178-**'},
    {'posicao': 43, 'nome': 'NICOLAS CONSTANÇA MENTONE', 'cpf': '***.154.108-**'},
    {'posicao': 44, 'nome': 'BRUNO HENRIQUE DE OLIVEIRA', 'cpf': '***.926.908-**'},
    {'posicao': 45, 'nome': 'SABRINA CRISTINA PEDRO VITORINO', 'cpf': '***.299.258-**'},
    {'posicao': 46, 'nome': 'PRISCILA S K CORREA', 'cpf': '***.553.718-**'},
    {'posicao': 47, 'nome': 'LETICIA PEREIRA', 'cpf': '***.745.188-**'},
    {'posicao': 48, 'nome': 'HENRIQUE MIWA DA SILVA', 'cpf': '***.050.518-**'},
    {'posicao': 49, 'nome': 'MATHEUS MORAIS KAWAMURA', 'cpf': '***.607.968-**'},
    {'posicao': 50, 'nome': 'CICERA MARIA COELHO DE OLIVEIRA', 'cpf': '***.043.138-**'},
    {'posicao': 51, 'nome': 'CAIO COUTO FICHEL', 'cpf': '***.501.478-**'},
    {'posicao': 52, 'nome': 'VINICIUS MONTANINI PIEROTE', 'cpf': '***.608.878-**'},
    {'posicao': 53, 'nome': 'PAULO ALVES MOREIRA JUNIOR', 'cpf': '***.778.968-**'},
    {'posicao': 54, 'nome': 'GABRIELLI RAMOS DA SILVA', 'cpf': '***.163.158-**'},
    {'posicao': 55, 'nome': 'VICTOR AUGUSTO DE SOUZA', 'cpf': '***.913.138-**'},
    {'posicao': 56, 'nome': 'THEO MARCHETTI BARCELOS', 'cpf': '***.507.218-**'},
    {'posicao': 57, 'nome': 'EVELIN DAYANE CAVALCANTE', 'cpf': '***.351.418-**'},
    {'posicao': 58, 'nome': 'BRUNA FAVA PIRES', 'cpf': '***.915.848-**'},
    {'posicao': 59, 'nome': 'CLEBERSON FERNANDO RAMOS', 'cpf': '***.819.248-**'},
    {'posicao': 60, 'nome': 'RYAN PIETRO CONSOLARI', 'cpf': '***.356.588-**'},
    {'posicao': 61, 'nome': 'FELIPE VINICIUS GONCALVES DOS REIS', 'cpf': '***.616.758-**'},
    {'posicao': 62, 'nome': 'LUCAS CAMPOS LEME DE BARROS', 'cpf': '***.053.288-**'},
    {'posicao': 63, 'nome': 'ABNER MARTINS DE CAMARGO', 'cpf': '***.241.638-**'},
    {'posicao': 64, 'nome': 'TIAGO MARTINS DOMINGUES', 'cpf': '***.241.908-**'},
    {'posicao': 65, 'nome': 'VICTOR PERILLO RODRIGUES SAMPAIO', 'cpf': '***.334.318-**'},
    {'posicao': 66, 'nome': 'THIAGO CICONELLO GIOVANETTI', 'cpf': '***.705.048-**'},
    {'posicao': 67, 'nome': 'MARIA EDUARDA FERNANDES RIBEIRO', 'cpf': '***.654.718-**'},
    {'posicao': 68, 'nome': 'IRENE DE CAMPOS PERILLO', 'cpf': '***.970.888-**'},
    {'posicao': 69, 'nome': 'DANIEL DE FREITAS ESTEVES DA COSTA', 'cpf': '***.311.778-**'},
    {'posicao': 70, 'nome': 'NICOLAS SILVA PREVIATO', 'cpf': '***.392.738-**'},
    {'posicao': 71, 'nome': 'JESSICA CAROLINE LATANCE', 'cpf': '***.440.858-**'},
    {'posicao': 72, 'nome': 'JULIA TIEMI VASQUES BANDEIRA', 'cpf': '***.020.448-**'},
    {'posicao': 73, 'nome': 'RAPHAELLA CAMILLY LUCAS RODRIGUES', 'cpf': '***.706.918-**'},
    {'posicao': 74, 'nome': 'RODRIGO OLIVEIRA DA ROCHA', 'cpf': '***.086.868-**'},
    {'posicao': 75, 'nome': 'KAUÃ MEIADO LEITE', 'cpf': '***.976.338-**'},
    {'posicao': 76, 'nome': 'ANDRE FERREIRA AGUIAR ALAMINO', 'cpf': '***.156.138-**'},
    {'posicao': 77, 'nome': 'DANIEL FERNANDO VIEIRA ARRUDA', 'cpf': '***.678.228-**'},
    {'posicao': 78, 'nome': 'RENAN MACHADO ALBERTINI', 'cpf': '***.912.528-**'},
    {'posicao': 79, 'nome': 'GABRIEL FERREIRA DOS SANTOS', 'cpf': '***.779.118-**'},
    {'posicao': 80, 'nome': 'TAMARA DE ASSIS BARBOSA', 'cpf': '***.376.378-**'},
    {'posicao': 81, 'nome': 'BRYAN FRANCA SOARES', 'cpf': '***.447.638-**'},
    {'posicao': 82, 'nome': 'VARDBELL RODRIGUES DOS SANTOS', 'cpf': '***.390.188-**'},
    {'posicao': 83, 'nome': 'TALITA RAMOS LAURIANO AKYAMA', 'cpf': '***.427.478-**'},
    {'posicao': 84, 'nome': 'MATEUS AURELIANO DA SILVA', 'cpf': '***.257.239-**'},
    {'posicao': 85, 'nome': 'MARCOS VINICIUS NUNES FERREIRA', 'cpf': '***.123.218-**'},
    {'posicao': 86, 'nome': 'FULVIO DE PAULA LIMA', 'cpf': '***.152.758-**'},
    {'posicao': 87, 'nome': 'CESAR HENRIQUE CAMARGO DOS SANTOS', 'cpf': '***.590.078-**'},
    {'posicao': 88, 'nome': 'FERNANDO TERUMASA IKEDA SON', 'cpf': '***.875.388-**'},
    {'posicao': 89, 'nome': 'ALAN RODRIGUES CASSEMIRO', 'cpf': '***.187.998-**'},
    {'posicao': 90, 'nome': 'WALDEMAR FAUSTINO DE SOUZA FILHO', 'cpf': '***.457.518-**'},
    {'posicao': 91, 'nome': 'LUIS A PEDROSO OLIVEIRA', 'cpf': '***.802.938-**'},
    {'posicao': 92, 'nome': 'JOÃO PEDRO DE OLIVEIRA FERREIRA', 'cpf': '***.339.708-**'},
    {'posicao': 93, 'nome': 'JULIO CESAR VIEIRA', 'cpf': '***.910.948-**'},
    {'posicao': 94, 'nome': 'LUIZ ANTONIO PANTOJO JUNIOR', 'cpf': '***.393.588-**'},
    {'posicao': 95, 'nome': 'ISABELLA ROLIM DE SOUZA', 'cpf': '***.163.368-**'},
    {'posicao': 96, 'nome': 'MICHEL CIRILO DE OLIVEIRA', 'cpf': '***.144.119-**'},
    {'posicao': 97, 'nome': 'LUCAS TORRES SANTANA', 'cpf': '***.307.418-**'},
    {'posicao': 98, 'nome': 'ERICK AUGUSTO GARCIA', 'cpf': '***.338.168-**'},
    {'posicao': 99, 'nome': 'FELIPE DOS REIS ANTUNES', 'cpf': '***.029.988-**'},
    {'posicao': 100, 'nome': 'SERGIO DOMINGOS RODRIGUES SAMPAIO', 'cpf': '***.710.718-**'},
    {'posicao': 101, 'nome': 'CAIO GUILHERME PEREIRA DOS SANTOS KITAGAKI', 'cpf': '***.590.628-**'},
    {'posicao': 102, 'nome': 'GABRIELLA FERNANDA PIERAMI', 'cpf': '***.935.418-**'},
    {'posicao': 103, 'nome': 'ALESSANDRA MARIA MARCZYNSKI', 'cpf': '***.060.858-**'},
    {'posicao': 104, 'nome': 'CAIO CÉSAR DE MOURA PENA', 'cpf': '***.570.308-**'},
    {'posicao': 105, 'nome': 'GABRIEL HENRIQUE DOS SANTOS RUFINO', 'cpf': '***.084.338-**'},
    {'posicao': 106, 'nome': 'GUSTAVO PIRES FORMIGONI LEITE', 'cpf': '***.557.508-**'},
    {'posicao': 107, 'nome': 'MARIA EDUARDA MORENO LOPES', 'cpf': '***.335.888-**'},
    {'posicao': 108, 'nome': 'FABIANE RAQUEL MOTTER', 'cpf': '***.089.360-**'},
    {'posicao': 109, 'nome': 'LUIZ CARLOS DA SILVA BUENO', 'cpf': '***.273.528-**'},
    {'posicao': 110, 'nome': 'MATEUS FERNANDO XAVIER MARIANO', 'cpf': '***.903.418-**'},
    {'posicao': 111, 'nome': 'MIGUEL DOS SANTOS GUSSI', 'cpf': '***.539.148-**'},
    {'posicao': 112, 'nome': 'MARCO TULIO DUENAS', 'cpf': '***.415.798-**'},
    {'posicao': 113, 'nome': 'MARIA EDUARDA CAMARGO DA SILVA', 'cpf': '***.412.478-**'},
    {'posicao': 114, 'nome': 'PETERSON ALVES PEREIRA', 'cpf': '***.310.166-**'},
    {'posicao': 115, 'nome': 'JOÃO VITOR DE CAMARGO BARROS', 'cpf': '***.513.388-**'},
    {'posicao': 116, 'nome': 'DOUGLAS FELIPE FERREIRA', 'cpf': '***.066.208-**'},
    {'posicao': 117, 'nome': 'PEDRO HENRIQUE MOURA CAYUELLA', 'cpf': '***.970.818-**'},
    {'posicao': 118, 'nome': 'GIOVANNA MENDONCA STEFANI', 'cpf': '***.614.328-**'},
    {'posicao': 119, 'nome': 'THALIA FERREIRA TIJOLLI DE FREITAS', 'cpf': '***.489.168-**'},
    {'posicao': 120, 'nome': 'SABRINA CARNEIRO RODRIGUES', 'cpf': '***.167.588-**'},
    {'posicao': 121, 'nome': 'GISLAINE OLIVIERA TAKUSHI', 'cpf': '***.891.438-**'},
    {'posicao': 122, 'nome': 'JOVANA ARCINE DOMINGUES', 'cpf': '***.631.198-**'},
    {'posicao': 123, 'nome': 'JOSÉ MARÍA MARTINS JUNIOR', 'cpf': '***.655.428-**'},
    {'posicao': 124, 'nome': 'PAULO HENRIQUE VERRI RUFINO', 'cpf': '***.859.068-**'},
    {'posicao': 125, 'nome': 'PEDRO PAZETTI DE OLIVEIRA', 'cpf': '***.199.158-**'},
    {'posicao': 126, 'nome': 'CAIO FERNANDO SCUDELER', 'cpf': '***.909.568-**'},
    {'posicao': 127, 'nome': 'GUILHERME DUARTE MACHADO', 'cpf': '***.678.338-**'},
    {'posicao': 128, 'nome': 'LUCAS GABRIEL OLIVEIRA SALDIAS', 'cpf': '***.725.518-**'},
    {'posicao': 129, 'nome': 'LUCAS CAMELO', 'cpf': '***.754.708-**'},
    {'posicao': 130, 'nome': 'EDSON VITOR PALDINI', 'cpf': '***.907.508-**'},
    {'posicao': 131, 'nome': 'WENDEL MAXIMO VIEIRA', 'cpf': '***.826.178-**'},
    {'posicao': 132, 'nome': 'GABRIELA MARIA RODRIGUES DE MORAIS', 'cpf': '***.115.838-**'},
    {'posicao': 133, 'nome': 'RODRIGO GARCIA ABEGAO', 'cpf': '***.181.088-**'},
    {'posicao': 134, 'nome': 'SAMUEL WILLIAM PAES', 'cpf': '***.233.758-**'},
    {'posicao': 135, 'nome': 'CAROLINA GOMES DE OLIVEIRA', 'cpf': '***.232.598-**'},
    {'posicao': 136, 'nome': 'GILLIARD TREVISANI DE OLIVEIRA', 'cpf': '***.200.428-**'},
    {'posicao': 137, 'nome': 'MIGUEL GONDIM CHANES', 'cpf': '***.595.648-**'},
    {'posicao': 138, 'nome': 'CARLOS EDUARDO MILAN FERREIRA', 'cpf': '***.249.918-**'},
    {'posicao': 139, 'nome': 'LILIAN SAMPAIO LEITE', 'cpf': '***.399.378-**'},
    {'posicao': 140, 'nome': 'FABIO LUIZ PASCHOAL', 'cpf': '***.545.228-**'},
    {'posicao': 141, 'nome': 'EDUARDO VIEIRA RIBEIRO DA SILVA', 'cpf': '***.475.388-**'},
    {'posicao': 142, 'nome': 'RAFAEL FRANCISCO LARA DE OLIVEIRA', 'cpf': '***.543.308-**'},
    {'posicao': 143, 'nome': 'ANA LAURA RIBEIRO', 'cpf': '***.915.888-**'},
    {'posicao': 144, 'nome': 'MIRELLA XAVIER GALINDO', 'cpf': '***.482.048-**'},
    {'posicao': 145, 'nome': 'ARTHUR ROGERIO DA COSTA', 'cpf': '***.468.188-**'},
    {'posicao': 146, 'nome': 'GABRIEL B QUEIROZ', 'cpf': '***.126.238-**'},
    {'posicao': 147, 'nome': 'VITOR FERRAZ BLUMEN', 'cpf': '***.271.388-**'},
    {'posicao': 148, 'nome': 'JAQUELINE CLARA GUTIERREZ BRESIO', 'cpf': '***.333.108-**'},
    {'posicao': 149, 'nome': 'BIANCA PICHIRILO VERGUEIRO BENATTI', 'cpf': '***.498.018-**'},
    {'posicao': 150, 'nome': 'JOAO VICTOR QUARESMA DE ARRUDA', 'cpf': '***.320.128-**'},
    {'posicao': 151, 'nome': 'LENALDO OLIVEIRA SILVA SANTOS', 'cpf': '***.400.248-**'},
    {'posicao': 152, 'nome': 'MATEUS FERNANDES ALVES', 'cpf': '***.438.158-**'},
    {'posicao': 153, 'nome': 'POLYANNA PIRES PASCHOAL', 'cpf': '***.942.958-**'},
    {'posicao': 154, 'nome': 'LUIZ GUSTAVO GOMES', 'cpf': '***.130.118-**'},
    {'posicao': 155, 'nome': 'STEFANIE MAYUMI INACIO KOBAYASHI RESENDE', 'cpf': '***.705.838-**'},
    {'posicao': 156, 'nome': 'JULIANA MACHADO RIBEIRO', 'cpf': '***.945.278-**'},
    {'posicao': 157, 'nome': 'PEDRO VALADARES JUNIOR', 'cpf': '***.076.153-**'},
    {'posicao': 158, 'nome': 'IVAN LUCA MUNHOZ DE SOUZA', 'cpf': '***.651.448-**'},
    {'posicao': 159, 'nome': 'ANA CAROLINA MAGALHAES LOPES', 'cpf': '***.524.501-**'},
    {'posicao': 160, 'nome': 'RENAN AUGUSTO SILVA', 'cpf': '***.269.988-**'},
    {'posicao': 161, 'nome': 'AMADOR BUENO DE OLIVEIRA NETO', 'cpf': '***.548.238-**'},
    {'posicao': 162, 'nome': 'MARIA E PEREIRA NUNES', 'cpf': '***.951.288-**'},
    {'posicao': 163, 'nome': 'GABRIEL TIAGO SANTOS LEME', 'cpf': '***.620.588-**'},
    {'posicao': 164, 'nome': 'PEDRO H CARDOSO', 'cpf': '***.019.588-**'},
    {'posicao': 165, 'nome': 'BRENDA BIRAL BATISTA', 'cpf': '***.430.818-**'},
    {'posicao': 166, 'nome': 'RICARDO ANDRE DOS SANTOS', 'cpf': '***.220.548-**'},
    {'posicao': 167, 'nome': 'GUSTAVO HENRIQUE BAUCH', 'cpf': '***.060.348-**'},
    {'posicao': 168, 'nome': 'MARCUS VINICIUS CARDOSO DE FREITAS', 'cpf': '***.378.768-**'},
    {'posicao': 169, 'nome': 'LUIZA DOS ANJOS OLIVEIRA', 'cpf': '***.469.738-**'},
    {'posicao': 170, 'nome': 'MARIA EDUARDA MORAIS OIKAWA', 'cpf': '***.300.368-**'},
    {'posicao': 171, 'nome': 'GUILHERME MELO ALEXANDRE DA SILVA', 'cpf': '***.204.428-**'},
    {'posicao': 172, 'nome': 'DOUGLAS HENRIQUE DOS SANTOS', 'cpf': '***.296.668-**'},
    {'posicao': 173, 'nome': 'LEONARDO VINÍCIUS RUIZ RONDELIS', 'cpf': '***.079.718-**'},
    {'posicao': 174, 'nome': 'MARIA LUIZA SCHNEIDER', 'cpf': '***.331.068-**'},
    {'posicao': 175, 'nome': 'NICOLAS DE OLIVEIRA DIAS', 'cpf': '***.578.008-**'},
    {'posicao': 176, 'nome': 'PRISCILA NORONHA MENDES', 'cpf': '***.687.188-**'},
    {'posicao': 177, 'nome': 'JONATHAN ANDREW ALVES GARCIA', 'cpf': '***.133.298-**'},
    {'posicao': 178, 'nome': 'GUSTAVO DE CAMPOS ANTUNES', 'cpf': '***.326.288-**'},
    {'posicao': 179, 'nome': 'SANDY OLIVEIRA MESSIAS', 'cpf': '***.832.678-**'},
    {'posicao': 180, 'nome': 'WILSON CARDOSO', 'cpf': '***.957.828-**'},
    {'posicao': 181, 'nome': 'GABRIEL ALCANTARA DIAS PRESTES', 'cpf': '***.224.798-**'},
    {'posicao': 182, 'nome': 'ANGÉLICA DA SILVA CORDEIRO', 'cpf': '***.472.048-**'},
    {'posicao': 183, 'nome': 'LARISSA SOARES DA SILVA', 'cpf': '***.576.408-**'},
    {'posicao': 184, 'nome': 'GABRIELA PEREIRA DO PRADO', 'cpf': '***.352.918-**'},
    {'posicao': 185, 'nome': 'DANIELA DE CASTRO MORAES', 'cpf': '***.645.658-**'},
    {'posicao': 186, 'nome': 'ALISSON HENRIQUE ROCHA DA COSTA', 'cpf': '***.735.668-**'},
    {'posicao': 187, 'nome': 'LISANDRA FERNANDA DE GODOI', 'cpf': '***.048.668-**'},
    {'posicao': 188, 'nome': 'NILSON DE SOUZA COSTA', 'cpf': '***.363.206-**'},
    {'posicao': 189, 'nome': 'RODOLFO ANTUNES DE ALMEIDA', 'cpf': '***.685.268-**'},
    {'posicao': 190, 'nome': 'PAULO THIAGO DE OLIVEIRA FRANCO', 'cpf': '***.514.548-**'},
    {'posicao': 191, 'nome': 'JULIA CRISTINA GÜTSCHOW SAMPAIO', 'cpf': '***.145.218-**'},
    {'posicao': 192, 'nome': 'RAVEN AARON ALBUQUERQUE PRESTES BATISTA', 'cpf': '***.163.028-**'},
    {'posicao': 193, 'nome': 'SIMAM CARLOS BATISTA FERREIRA', 'cpf': '***.011.252-**'},
    {'posicao': 194, 'nome': 'FLÁVIA ALVARENGA SARTORI', 'cpf': '***.695.758-**'},
    {'posicao': 195, 'nome': 'LETÍCIA VITÓRIA DOS SANTOS SILVA', 'cpf': '***.057.198-**'},
    {'posicao': 196, 'nome': 'TELMA REGINA DE LIMA', 'cpf': '***.151.008-**'},
    {'posicao': 197, 'nome': 'CAMILO OLIVEIRA DE FREITAS', 'cpf': '***.585.578-**'},
    {'posicao': 198, 'nome': 'GABRIEL PEDROSO DE GOES VIEIRA', 'cpf': '***.869.898-**'},
    {'posicao': 199, 'nome': 'JUNIO CESAR BATISTA DE SA', 'cpf': '***.320.188-**'},
    {'posicao': 200, 'nome': 'N & D CONTRUTORES', 'cpf': '49.551.066/0001-69'},
    {'posicao': 201, 'nome': 'GUILHERME ANTONIO RODRIGUES DA COSTA', 'cpf': '***.144.268-**'},
    {'posicao': 202, 'nome': 'FELIPE ARTUR BERNARDO FERREIRA', 'cpf': '***.321.788-**'},
    {'posicao': 203, 'nome': 'ERIC RODRIGUES BERTO', 'cpf': '***.036.498-**'},
    {'posicao': 204, 'nome': 'RODOLFO PEREIRA DA SILVA', 'cpf': '***.126.528-**'},
    {'posicao': 205, 'nome': 'ISABELLY OGURI JORGE', 'cpf': '***.095.808-**'},
    {'posicao': 206, 'nome': 'PATRICIA CARDELI', 'cpf': '***.366.018-**'},
    {'posicao': 207, 'nome': 'BRUNO FELIPE SOUZA ARAUJO', 'cpf': '***.240.388-**'},
    {'posicao': 208, 'nome': 'GABRIEL CASTILHO MEDEIROS DE SOUZA', 'cpf': '***.364.088-**'},
    {'posicao': 209, 'nome': 'HENRIQUE VIDOTTO VINICO NETO', 'cpf': '***.292.128-**'},
    {'posicao': 210, 'nome': 'NICOLE JANINE BOLZANI OLIVEIRA', 'cpf': '***.303.578-**'},
    {'posicao': 211, 'nome': 'LUCAS PIRES DE ALMEIDA', 'cpf': '***.223.318-**'},
    {'posicao': 212, 'nome': 'EMILLY RAISSA DE ALMEIDA DE MORAES', 'cpf': '***.623.028-**'},
    {'posicao': 213, 'nome': 'IGOR HENRIQUE DE OLIVEIRA LOPES', 'cpf': '***.136.848-**'},
    {'posicao': 214, 'nome': 'SIMONE CRISTINA DIAS', 'cpf': '***.796.618-**'},
    {'posicao': 215, 'nome': 'NICOLE FAVA PIRES', 'cpf': '***.051.518-**'},
    {'posicao': 216, 'nome': 'JOAO GABRIEL MILONE VILELA DE CAMARGO', 'cpf': '***.245.718-**'},
    {'posicao': 217, 'nome': 'SABRINA SANT ANA DA SILVA ALVES', 'cpf': '***.844.038-**'},
    {'posicao': 218, 'nome': 'ALLAN WANDREY QUEIROZ', 'cpf': '***.395.008-**'},
    {'posicao': 219, 'nome': 'FABIO LUIZ DE FRANCA FILHO', 'cpf': '***.724.428-**'},
    {'posicao': 220, 'nome': 'ALFREDO JOSE ALVES SILVA', 'cpf': '***.324.308-**'},
    {'posicao': 221, 'nome': 'GUILHERME GODOY ROSA LOPES', 'cpf': '***.098.958-**'},
    {'posicao': 222, 'nome': 'OBERSON BARBOSA DE LIMA', 'cpf': '***.374.708-**'},
    {'posicao': 223, 'nome': 'MIGUEL COELHO EVANGELISTA DOS SANTOS', 'cpf': '***.691.478-**'},
    {'posicao': 224, 'nome': 'ANDRE BORGES DIAS', 'cpf': '***.665.658-**'},
    {'posicao': 225, 'nome': 'JUAN LUCAS DA SILVA', 'cpf': '***.632.726-**'},
    {'posicao': 226, 'nome': 'ALEXANDRE SANCHES BONA', 'cpf': '***.605.808-**'},
    {'posicao': 227, 'nome': 'GUILHERME AUGUSTO GOMES ARRIBAMAR', 'cpf': '***.264.638-**'},
    {'posicao': 228, 'nome': 'VITOR MEIRA ALVES', 'cpf': '***.126.668-**'},
    {'posicao': 229, 'nome': 'LEILA APARECIDA DE LIMA', 'cpf': '***.664.258-**'},
    {'posicao': 230, 'nome': 'FABIO CRISTIANO CONSOLARI', 'cpf': '***.343.368-**'},
    {'posicao': 231, 'nome': 'MIGUEL FIDENCIO AYRES', 'cpf': '***.438.038-**'},
    {'posicao': 232, 'nome': 'GABRIEL YUJI SHIMODA VIEIRA', 'cpf': '***.802.918-**'},
    {'posicao': 233, 'nome': 'SANDRA MAUREN ELL', 'cpf': '***.218.568-**'},
    {'posicao': 234, 'nome': 'HENRICO AUGUSTO LIMA LOPES', 'cpf': '***.973.248-**'},
    {'posicao': 235, 'nome': 'MATEUS SILVA DALMARCO', 'cpf': '***.839.838-**'},
    {'posicao': 236, 'nome': 'ALISON FERNANDES SANTOS', 'cpf': '***.715.938-**'},
    {'posicao': 237, 'nome': 'JOAO VICTOR DE PAULA FERREIRA', 'cpf': '***.280.868-**'},
    {'posicao': 238, 'nome': 'VINÍCIUS GAMA DE FRANÇA', 'cpf': '***.358.148-**'},
    {'posicao': 239, 'nome': 'JOÃO VICTOR LOPEZ DE ARRUDA', 'cpf': '***.329.808-**'},
    {'posicao': 240, 'nome': 'VITOR SANDY PUPO', 'cpf': '***.295.288-**'},
    {'posicao': 241, 'nome': 'CARLA ROBERTA DAS NEVES', 'cpf': '***.359.308-**'},
    {'posicao': 242, 'nome': 'ANA LAURA MARTINS SOUTO', 'cpf': '***.777.668-**'},
    {'posicao': 243, 'nome': 'BRUNO FERNANDO MENDES', 'cpf': '***.966.988-**'},
    {'posicao': 244, 'nome': 'PAULO CESAR PONTES DE OLIVEIRA', 'cpf': '***.360.198-**'},
    {'posicao': 245, 'nome': 'CRISTIANE RAMOS TEIXEIRA', 'cpf': '***.213.958-**'}
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
                <div style='margin-top:8px; font-size:18px; color:#333;'><strong>GABRIELLI RAMOS DA SILVA</strong></div>
                <div style='margin-top:6px; font-size:14px; color:#666;'>CPF: <strong>•••.163.158-••</strong></div>
            </div>
        """, unsafe_allow_html=True)

# 5. Rodapé
st.markdown("""
    <div class="footer-text">
        Atualizado em 31/10/2026<br>
        <strong>Promoção Finalizada </strong>
    </div>
""", unsafe_allow_html=True)
