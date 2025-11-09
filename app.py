import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==============================
# 🎨 Configuração da Página
# ==============================
st.set_page_config(
    page_title="Dashboard de Receitas por Categoria",
    page_icon="📊",
    layout="wide"
)

# ==============================
# 🧭 Título e Introdução
# ==============================
st.title("📈 Dashboard de Exemplo com Streamlit")
st.markdown("""
Bem-vindo ao seu primeiro app em **Streamlit**!  
Aqui você pode visualizar dados, gerar gráficos interativos e testar funcionalidades de interface.
""")

# ==============================
# 📅 Filtros
# ==============================
st.sidebar.header("⚙️ Filtros de Visualização")

anos = list(range(2015, 2026))
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", anos)

categorias = ["Tecnologia", "Saúde", "Educação", "Finanças", "Varejo"]
categoria_selecionada = st.sidebar.multiselect("Selecione Categorias", categorias, default=categorias)

# ==============================
# 📊 Gerar Dados Aleatórios
# ==============================
np.random.seed(42)
dados = pd.DataFrame({
    "Ano": np.random.choice(anos, 200),
    "Categoria": np.random.choice(categorias, 200),
    "Receita": np.random.randint(50000, 500000, 200),
    "Lucro": np.random.randint(10000, 200000, 200)
})

# Aplicar Filtros
dados_filtrados = dados[
    (dados["Ano"] == ano_selecionado) &
    (dados["Categoria"].isin(categoria_selecionada))
]

# ==============================
# 📉 Gráfico de Barras (Plotly)
# ==============================
fig = px.bar(
    dados_filtrados,
    x="Categoria",
    y="Receita",
    color="Categoria",
    title=f"Receita por Categoria ({ano_selecionado})",
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

# ==============================
# 💰 Métricas de Destaque
# ==============================
col1, col2, col3 = st.columns(3)
col1.metric("💵 Receita Total", f"R$ {dados_filtrados['Receita'].sum():,.0f}")
col2.metric("📈 Lucro Médio", f"R$ {dados_filtrados['Lucro'].mean():,.0f}")
col3.metric("🏷️ Categorias Selecionadas", len(categoria_selecionada))

# ==============================
# 🧾 Tabela de Dados
# ==============================
st.subheader("📋 Dados Filtrados")
st.dataframe(dados_filtrados, use_container_width=True)

# ==============================
# ✅ Rodapé
# ==============================
st.markdown("---")
st.markdown("👨‍💻 Desenvolvido por **Matheus Ramos** 🚀")