# cadastro_produto.py
import streamlit as st
import pandas as pd

# URLs dos dados externos (devem ser centralizadas depois)
URL_GRUPO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=528868130&single=true&output=csv"
URL_MARCAS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=832596780&single=true&output=csv"

def render_cadastro_produto():
    st.title("📦 Cadastro de Produto")

    try:
        grupo_df = pd.read_csv(URL_GRUPO)
        marcas_df = pd.read_csv(URL_MARCAS)
    except Exception as e:
        st.error(f"Erro ao carregar dados de grupo/marcas: {e}")
        return

    with st.form("form_cad_produto"):
        nome = st.text_input("Nome do Produto")
        grupo = st.selectbox("Grupo", grupo_df["DESCRICAO"].dropna())
        marca = st.selectbox("Marca", marcas_df["DESCRICAO"].dropna())
        preco = st.number_input("Preço", min_value=0.0)
        estoque = st.number_input("Estoque", min_value=0)
        enviar = st.form_submit_button("Salvar")

        if enviar:
            st.success("Produto cadastrado com sucesso!")
            st.json({
                "nome": nome,
                "grupo": grupo,
                "marca": marca,
                "preco": preco,
                "estoque": estoque
            })
