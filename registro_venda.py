# registro_venda.py
import streamlit as st
import pandas as pd
from datetime import datetime

URL_CLIENTE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=1645177762&single=true&output=csv"
URL_PRODUTO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=1506891785&single=true&output=csv"
URL_PGTO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=1061064660&single=true&output=csv"

def render_registro_venda():
    st.title("🧾 Registrar Venda")

    try:
        cliente_df = pd.read_csv(URL_CLIENTE)
        produto_df = pd.read_csv(URL_PRODUTO)
        forma_pgto_df = pd.read_csv(URL_PGTO)
    except Exception as e:
        st.error(f"Erro ao carregar dados de venda: {e}")
        return

    with st.form("form_venda"):
        cliente = st.selectbox("Cliente", cliente_df["NOME"].dropna())
        forma_pgto = st.selectbox("Forma de Pagamento", forma_pgto_df["DESCRICAO"].dropna())

        st.markdown("---")
        st.subheader("Produtos")

        itens = []
        for i in range(3):
            col1, col2 = st.columns(2)
            with col1:
                produto = st.selectbox(f"Produto {i+1}", produto_df["DESCRICAO"], key=f"produto_{i}")
            with col2:
                qtd = st.number_input(f"Quantidade {i+1}", min_value=0, step=1, key=f"qtd_{i}")

            if qtd > 0:
                preco = float(produto_df.loc[produto_df["DESCRICAO"] == produto, "PRECO"].values[0])
                total = qtd * preco
                itens.append({"produto": produto, "quantidade": qtd, "preco_unit": preco, "total": total})

        submitted = st.form_submit_button("Finalizar Venda")

    if submitted and itens:
        total_geral = sum(item["total"] for item in itens)
        venda = {
            "cliente": cliente,
            "forma_pgto": forma_pgto,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total": total_geral,
            "itens": itens
        }

        st.success("Venda registrada com sucesso!")
        st.json(venda)
