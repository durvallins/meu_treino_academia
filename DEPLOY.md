# 🚀 Deploy no Streamlit Community Cloud

## Passo a Passo para Publicar

### 1. Acesse o Streamlit Cloud
- Vá para: https://share.streamlit.io/
- Faça login com sua conta GitHub

### 2. Crie um Novo App
- Clique em **"New app"**
- Selecione:
  - **Repository:** `durvallins/meu_treino_academia`
  - **Branch:** `main`
  - **Main file path:** `app.py`

### 3. Deploy
- Clique em **"Deploy!"**
- Aguarde alguns minutos enquanto o Streamlit prepara seu app
- Seu app ficará disponível em: `https://durvallins-meu-treino-academia.streamlit.app`

### 4. Configurações Opcionais
- **Domínio customizado**: Pode configurar nas settings
- **Secrets**: Se precisar de variáveis de ambiente no futuro
- **Resources**: O plano gratuito oferece recursos suficientes para este app

## 📝 Notas Importantes

✅ **O que está no repositório:**
- Código da aplicação (`app.py`)
- Dependências (`requirements.txt`)
- Arquivos de treino (`.txt` na pasta `treinos/`)
- Template de dados (`data/workouts_template.csv`)

❌ **O que NÃO está (e não deve estar):**
- Histórico pessoal de treinos (`historico.csv`)
- Ambiente virtual (`venv/`)
- Cache do Python (`__pycache__/`)

## 🔄 Atualizações Futuras

Para atualizar o app após mudanças:

```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
```

O Streamlit Cloud detecta as mudanças automaticamente e redeployer o app!

## 🆘 Problemas Comuns

**Erro de dependências:**
- Verifique se todas as bibliotecas estão no `requirements.txt`
- Teste localmente antes: `pip install -r requirements.txt`

**App não inicia:**
- Verifique os logs no Streamlit Cloud
- Confirme que `app.py` está na raiz do repositório

## 📱 Teste seu App

Após o deploy, teste:
- ✅ Seleção de treinos
- ✅ Visualização de exercícios
- ✅ Cronômetro de descanso
- ✅ Salvamento de histórico (será criado automaticamente)
- ✅ Responsividade no celular

---

**Link do Repositório:** https://github.com/durvallins/meu_treino_academia
**Seu App:** https://durvallins-meu-treino-academia.streamlit.app (após deploy)
