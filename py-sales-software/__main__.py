import streamlit as st
import pandas as pd
import plotly.express as px

tabelaVendas = pd.read_csv("csv-vendas.csv")

st.write("# Sistema de Vendas")
st.write("###### Projeto acadêmico desenvolvido por Nichollas Braz.")

# seção de cadastro de vendas

st.sidebar.write("## Cadastrar Vendas")

vendedores = ["Thalys", "Pedro", "Nogueira"]
produtos = ["Celular", "Notebook", "Fone"]

data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", vendedores)
produto = st.sidebar.selectbox("Produto", produtos)
quantidade = st.sidebar.number_input("Quantidade",step=1)
valor = st.sidebar.number_input("Valor")
cadastroKey = st.sidebar.button("Cadastrar Venda")

if cadastroKey:
    if valor == 0 or quantidade == 0 or vendedor == "":
        st.warning("Verifique as informações e tente novamente.")
    novaVenda = [str(data), vendedor, produto, quantidade, valor]
    ultimaLinha = len(tabelaVendas)
    tabelaVendas.loc[ultimaLinha] = novaVenda
    tabelaVendas.to_csv("csv-vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso.")

# seção de visualização de vendas

st.write("## Vendas Cadastradas")

st.dataframe(tabelaVendas)

# seção de dashboard

st.write("## Dashboard")

faturamento = tabelaVendas["valor"].sum()
st.metric("Faturamento Total:", f"R${faturamento:.2f}")

# gráfico de barra

graph_1 = px.bar(tabelaVendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(graph_1)

# gráfico de pizza

graph_2 = px.pie(tabelaVendas, names="produto", values="valor", color="produto", hole=0.5)
st.plotly_chart(graph_2)
