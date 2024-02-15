###############
##  ATENÇÃO  ##
###############
## Este app  ##
## foi feito ##
## para ser  ##
## aberto em ##
## Dark Mode ##
###############  

#Caso não tenha instalado, deve instalar
#pip install mysql.connector-python
#pip install streamlit
#pip install streamlit-option-menu

##### Importando bibliotecas #####

import streamlit as st
import numpy as np
import pandas as pd
#from streamlit_option_menu import option_menu

##### Configurando a aba da página #####

st.set_page_config(page_title='UFTM', page_icon='🎓')

##### Conexão ao Banco MySQL #####



def conn_mysql():
    conn = st.connection('mysql', type='sql')
        
    ##### Definindo as páginas #####
     
    #### Pagina 1 - Mostra o início do site junto com a logo e sua funcionalidade ####
st.image('https://i.imgur.com/TBvRRfw.jpg', width=720)
st.divider()
st.title('Bem-Vindo(a) à Universidade Federal de Tangamandápio (UFTM)')
st.write('Neste site, você (professor) poderá cadastrar seu aluno (em Cadastro) e ver a listagem de quantos alunos há na UFTM (em Listagem)')
    
    
    #### Pagina 2 - Serve para cadastras os demais alunos no banco de dados ###

    #### Pagina 3 - Serve para dar uma beleza para quando for chamar a página 'pagina_exibicao' ####
    
    def pagina_bonita():
        st.header('Listagem dos Alunos', divider='rainbow')
        st.title('Nesta Página')
        st.markdown('''Você poderá ver quais alunos estão matriculados na **Universidade Federal de Tangamandápio**
        \nClique no botão :red["Mostrar alunos matriculados"] para ver nossa lista de alunos matriculados''')
    
    #### Pagina 3.2 - Serve para exibir os alunos que foram cadastrados no banco de dados ####
    
    def pagina_exibicao():
        st.title('Listagem de alunos matriculados')
        conexao = conn_mysql()
        if conexao:        
            cursor.query('SELECT * FROM Alunos')
            resultados = cursor.fetchall()
            st.write("Resultados da consulta ao banco de dados MySQL: ")
            for resultado in resultados:
                st.write(f'CPF: {resultado[0]}, Nome: {resultado[1]}, Curso: {resultado[2]}, Telefone de contato: {resultado[3]}, Email: {resultado[4]}')

    #### Pagina 4 - Serve para dar os créditos à autora ####

    def pagina_creditos():
        st.title('Créditos')
        st.text('Feito por Hanna Patrocinio Benevides da Silveira.')
        st.divider()
        st.image('https://www.ibipora.pr.gov.br/imagens/logoRodape.png')
        st.divider()
        st.text('Todos os direitos reservados. UFTM © 2024')
        
    ##### Definindo a função para chamar as páginas #####

    with st.sidebar:
        st.image('https://i.imgur.com/TBvRRfw.jpg',use_column_width=True)
        pagina_atual = option_menu("Selecione a página", ["Início", "Cadastro","Listagem","Créditos"], 
        icons=["", "", ""], 
        menu_icon="column", default_index=1,
        styles={
            "container": {"padding": "0!important", "background-color": "#262730"},
            "icon": {"color": "#FAFAFA", "font-size": "30px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"}, 
            "nav-link-selected": {"background-color": "#0E1117"},
        }
    )

    ##### Chamando as páginas #####

    if pagina_atual == 'Cadastro':
        pagina_cadastro()
    elif pagina_atual == 'Início':
        pagina_inicio()
    elif pagina_atual == 'Listagem':
        pagina_bonita()
        if st.button ('Mostrar alunos matriculados'):
            st.divider()
            pagina_exibicao()    
    elif pagina_atual == 'Créditos':
        pagina_creditos()

##### No fim do código chamamos a função imensa que é o nosso código todo #####

mae()
