import os
import time
from datetime import datetime

import pandas as pd
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Treino de Academia - Progressão",
    page_icon="🏋️‍♂️",
    layout="centered"
)

# --- Caminhos de Arquivos ---
TREINOS_DIR = "treinos"
DATA_DIR = "data"
HISTORICO_FILE = os.path.join(DATA_DIR, "historico.csv")

if not os.path.exists(TREINOS_DIR):
    os.makedirs(TREINOS_DIR)
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --- Funções de Dados ---

def formatar_nome_treino(nome_arquivo):
    """Remove extensão, substitui underscores e formata o nome do treino."""
    return nome_arquivo.replace(".txt", "").replace("_", " ")

def load_workout_data(file_name):
    """Carrega os dados de um arquivo de treino."""
    exercises = []
    summary = ""
    file_path = os.path.join(TREINOS_DIR, file_name)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                if stripped_line.startswith("#"):
                    summary += stripped_line.replace("#", "").strip() + " "
                elif "|" in stripped_line:
                    parts = stripped_line.split("|")
                    if len(parts) == 2:
                        name, series = parts
                        exercises.append({"Exercício": name.strip(), "Séries": series.strip()})
                    else:
                        st.warning(f"Linha mal formatada ignorada: {stripped_line}")
                else:
                    exercises.append({"Exercício": stripped_line, "Séries": "3x12"})
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")
        return pd.DataFrame(), ""
    except Exception as e:
        st.error(f"Erro ao ler arquivo {file_name}: {str(e)}")
        return pd.DataFrame(), ""
    
    return pd.DataFrame(exercises), summary.strip()

def salvar_historico(treino_nome):
    """Salva o treino concluído no histórico."""
    try:
        hoje = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        novo_registro = pd.DataFrame({"Data": [hoje], "Treino": [treino_nome]})
        
        if os.path.exists(HISTORICO_FILE):
            historico = pd.read_csv(HISTORICO_FILE)
            historico = pd.concat([historico, novo_registro], ignore_index=True)
        else:
            historico = novo_registro
        
        historico.to_csv(HISTORICO_FILE, index=False)
        return True
    except Exception as e:
        st.error(f"Erro ao salvar histórico: {str(e)}")
        return False

# CSS para Card Fixo do Cronômetro
st.markdown("""
<style>
    .cronometro-fixo {
        position: sticky;
        top: 60px;
        z-index: 999;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        text-align: center;
    }
    .tempo-grande {
        font-size: 3em;
        font-weight: bold;
        color: white;
        margin: 10px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .cronometro-titulo {
        color: white;
        font-size: 1.2em;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'tempo_restante' not in st.session_state:
    st.session_state.tempo_restante = 0

# --- Interface ---

st.title("🏋️‍♂️ Meu Treino de Academia")

# Sidebar para Histórico
with st.sidebar:
    st.header("📅 Histórico")
    if os.path.exists(HISTORICO_FILE):
        df_hist = pd.read_csv(HISTORICO_FILE)
        st.dataframe(df_hist.tail(10).iloc[::-1], hide_index=True)
    else:
        st.write("Nenhum treino registrado ainda.")

# Seleção de Treino
arquivos_treino = sorted([f for f in os.listdir(TREINOS_DIR) if f.endswith('.txt')])

if not arquivos_treino:
    st.warning(f"Crie arquivos .txt na pasta '{TREINOS_DIR}'.")
    st.stop()

treino_selecionado = st.selectbox(
    "Escolha o Treino de Hoje:",
    arquivos_treino,
    format_func=formatar_nome_treino
)

df_treino, resumo_treino = load_workout_data(treino_selecionado)

if df_treino.empty:
    st.error("Não foi possível carregar o treino. Verifique o arquivo.")
    st.stop()

if resumo_treino:
    st.markdown(f"**🎯 Objetivo:** *{resumo_treino}*")

st.divider()

# Card Fixo do Cronômetro
card_cronometro = st.container()
with card_cronometro:
    st.markdown('<div class="cronometro-fixo">', unsafe_allow_html=True)
    st.markdown('<p class="cronometro-titulo">⏱️ Cronômetro</p>', unsafe_allow_html=True)
    
    # Display do tempo
    tempo_display = st.empty()
    if st.session_state.timer_running and st.session_state.tempo_restante > 0:
        tempo_display.markdown(f'<div class="tempo-grande">⏰ {st.session_state.tempo_restante}s</div>', unsafe_allow_html=True)
    else:
        tempo_display.markdown('<div class="tempo-grande">--</div>', unsafe_allow_html=True)
    
    # Controles do cronômetro
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        tempo_descanso = st.number_input("Tempo (seg):", min_value=5, max_value=300, value=60, step=5, key="tempo")
    
    with col2:
        if st.button("▶️ Iniciar", use_container_width=True, type="primary"):
            st.session_state.timer_running = True
            st.session_state.tempo_restante = tempo_descanso
    
    with col3:
        if st.button("⏹️ Parar", use_container_width=True):
            st.session_state.timer_running = False
            st.session_state.tempo_restante = 0
    
    # Barra de progresso
    if st.session_state.timer_running and st.session_state.tempo_restante > 0:
        progresso = (tempo_descanso - st.session_state.tempo_restante) / tempo_descanso
        st.progress(progresso)
    else:
        st.progress(0)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Lógica do cronômetro
if st.session_state.timer_running and st.session_state.tempo_restante > 0:
    time.sleep(1)
    st.session_state.tempo_restante -= 1
    if st.session_state.tempo_restante == 0:
        st.session_state.timer_running = False
        st.balloons()
        st.success("🔥 Próxima Série!")
    st.rerun()

st.divider()

# Listagem de Exercícios
st.subheader(f"Lista de Exercícios - {formatar_nome_treino(treino_selecionado)}")

for index, row in df_treino.iterrows():
    cols = st.columns([3, 1, 1])
    with cols[0]:
        st.write(f"**{row['Exercício']}**")
    with cols[1]:
        st.caption(f"{row['Séries']}")
    with cols[2]:
        st.checkbox("OK", key=f"check_{treino_selecionado}_{index}")

st.divider()

if st.button("✅ Finalizar e Salvar Treino", use_container_width=True):
    if salvar_historico(formatar_nome_treino(treino_selecionado)):
        st.balloons()
        st.success("Treino registrado no histórico!")
        time.sleep(1)
        st.rerun()
    else:
        st.error("Erro ao salvar o treino. Tente novamente.")

st.info("💡 Edite seus treinos na pasta `treinos/`.")
