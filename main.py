# main.py
import streamlit as st
from .auth import autenticar_usuario
from .cadastro_produto import render_cadastro_produto
from .cadastro_cliente import render_cadastro_cliente
from .registro_venda import render_registro_venda
from .relatorios import render_relatorios
from .painel import render_painel

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    autenticar_usuario()
    st.stop()

st.sidebar.title("🔹 Menu PDV")
if st.sidebar.button("Sair"):
    st.session_state["autenticado"] = False
    st.experimental_rerun()

menu = st.sidebar.radio("Escolha a opção:", [
    "Cadastro Produto", "Cadastro Cliente", "Registrar Venda", "Relatórios", "Painel"])

if menu == "Cadastro Produto":
    render_cadastro_produto()
elif menu == "Cadastro Cliente":
    render_cadastro_cliente()
elif menu == "Registrar Venda":
    render_registro_venda()
elif menu == "Relatórios":
    render_relatorios()
elif menu == "Painel":
    render_painel()
