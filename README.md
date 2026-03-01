# APP_TREINO 🏋️‍♂️

Aplicativo para acompanhamento de progressão de treinos na academia desenvolvido com Streamlit.

## Como Executar Localmente

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o app:
   ```bash
   streamlit run app.py
   ```

## Funcionalidades
- Seleção de treino do dia (A, B, C, D).
- Registro de cargas e repetições.
- Checkbox de conclusão de exercício.
- Integração planejada com Google Sheets para persistência online.

## Estrutura do Projeto
Consulte o arquivo `claude.md` para mais detalhes sobre a arquitetura e decisões de design.
