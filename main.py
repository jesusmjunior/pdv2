# main.py
import streamlit as st
from .pdv20251.auth import autenticar_usuario
from .pdv20251.cadastro_produto import render_cadastro_produto
from .pdv20251.cadastro_cliente import render_cadastro_cliente
from .pdv20251.registro_venda import render_registro_venda
from .pdv20251.relatorios import render_relatorios
from .pdv20251.painel import render_painel

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
