import streamlit as st
import pandas as pd
import numpy as np

def conn_mysql():
    conn = st.connection('mysql', type='sql')

st.header('Cadastro', divider='rainbow')
st.title('Nesta Página')
st.markdown('''Você vai cadastrar o aluno na Universidade Estadual de Tangamandápio (UFTM)''')
conexao = conn_mysql()
cpf = st.text_input('Digite seu CPF')
nome = st.text_input('Digite seu Nome')
curso = st.text_input('Digite o curso em que está matriculado')
ctt = st.text_input('Digite seu telefone de contato')
email = st.text_input('Digite seu Email')
if conexao:
    joja = st.button('Cadastrar')
    if joja:
        st.success("Aluno matriculado com sucesso")
        conexao.execute('INSERT INTO alunos (CPF, Nome, Curso, telCtt, Email) values (%s,%s,%s,%s,%s)', (cpf,nome,curso,ctt,email))
        conexao.commit()
