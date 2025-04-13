# painel.py
import streamlit as st
import pandas as pd
from datetime import datetime

URL_VENDA = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=1817416820&single=true&output=csv"


def render_painel():
    st.title("📈 Painel Financeiro")

    try:
        venda_df = pd.read_csv(URL_VENDA)
        venda_df["DATA"] = pd.to_datetime(venda_df["DATA"], errors="coerce")
    except Exception as e:
        st.error(f"Erro ao carregar dados para o painel: {e}")
        return

    try:
        import plotly.express as px

        st.subheader("Total por Forma de Pagamento")
        pgto_group = venda_df.groupby("ID_FORMA_PGTO")["TOTAL"].sum().reset_index()
        fig_pgto = px.bar(pgto_group, x="ID_FORMA_PGTO", y="TOTAL")
        st.plotly_chart(fig_pgto)

        st.subheader("Evolução Diária de Vendas")
        diario = venda_df.groupby(venda_df["DATA"].dt.date)["TOTAL"].sum().reset_index()
        fig_dia = px.line(diario, x="DATA", y="TOTAL")
        st.plotly_chart(fig_dia)

        st.metric("Total Geral de Vendas", f"R$ {venda_df['TOTAL'].sum():,.2f}")

    except ModuleNotFoundError:
        st.warning("A biblioteca plotly não está instalada. Execute: pip install plotly")
    except Exception as e:
        st.error(f"Erro ao gerar gráficos: {e}")
