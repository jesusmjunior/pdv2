# relatorios.py
import streamlit as st
import pandas as pd
from datetime import datetime

URL_VENDA = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0r3XE4DpzlYJjZwjc2c_pW_K3euooN9caPedtSq-nH_aEPnvx1jrcd9t0Yhg8fqXfR3j5jM2OyUQQ/pub?gid=1817416820&single=true&output=csv"


def render_relatorios():
    st.title("📊 Relatório de Vendas")

    try:
        venda_df = pd.read_csv(URL_VENDA)
        venda_df["DATA"] = pd.to_datetime(venda_df["DATA"], errors="coerce")
    except Exception as e:
        st.error(f"Erro ao carregar dados para relatório: {e}")
        return

    col1, col2 = st.columns(2)
    with col1:
        data_ini = st.date_input("Data Inicial", datetime.today())
    with col2:
        data_fim = st.date_input("Data Final", datetime.today())

    formas = venda_df["ID_FORMA_PGTO"].dropna().unique()
    forma_selecionada = st.selectbox("Filtrar por Forma de Pagamento (opcional)", ["Todas"] + list(formas))

    if st.button("Gerar Relatório"):
        try:
            filtro = (venda_df['DATA'].dt.date >= data_ini) & (venda_df['DATA'].dt.date <= data_fim)
            if forma_selecionada != "Todas":
                filtro &= (venda_df['ID_FORMA_PGTO'] == forma_selecionada)

            relatorio = venda_df[filtro].copy()

            if not relatorio.empty:
                st.success(f"Foram encontradas {len(relatorio)} vendas no período.")
                st.dataframe(relatorio)
                total = relatorio['TOTAL'].sum()
                st.markdown(f"### 💰 Total de Vendas no Período: R$ {total:.2f}")

                csv = relatorio.to_csv(index=False).encode()
                st.download_button("📥 Baixar CSV", csv, "relatorio_vendas.csv", "text/csv")
            else:
                st.warning("Nenhuma venda encontrada para os filtros aplicados.")

        except Exception as err:
            st.error(f"Erro no processamento do relatório: {err}")
