# App de Progressão de Treinos - APP_TREINO

Este documento detalha o estado atual e as especificações do aplicativo de acompanhamento de treinos.

## 1. Objetivo do Aplicativo
O objetivo é fornecer uma interface simples e amigável para celulares (via navegador) onde o aluno possa:
- Selecionar o treino do dia (A, B, C ou D).
- Visualizar o objetivo específico de cada treino.
- Marcar a conclusão de cada exercício em tempo real.
- Utilizar um cronômetro de descanso entre as séries.
- Consultar o histórico dos últimos treinos realizados.

## 2. Método de Entrada de Dados (Data Source)

### **Arquivos de Texto (.txt) na pasta `treinos/`**
- **Padrão de Nomenclatura:** `Treino_A.txt`, `Treino_B.txt`, etc.
- **Formato Interno:**
    - Linhas iniciadas com `#`: Definem o **Objetivo** do treino (exibido em destaque no app).
    - Linhas com `|`: Separam o **Nome do Exercício** da **Série/Repetições** (ex: `Supino | 4x12`).
    - Linhas simples: Tratadas apenas como o nome do exercício com série padrão (3x12).

## 3. Arquitetura Atual do Sistema

```text
APP_TREINO/
├── app.py                # Interface Streamlit e lógica principal
├── requirements.txt      # Dependências (streamlit, pandas)
├── README.md             # Instruções de uso e deploy
├── .gitignore            # Proteção de arquivos sensíveis e temporários
├── treinos/              # Pasta com as definições dos treinos
│   ├── Treino_A.txt
│   ├── Treino_B.txt
│   ├── Treino_C.txt
│   └── Treino_D.txt
├── data/                 # Armazenamento de dados persistentes
│   └── historico.csv     # Registro das sessões concluídas
└── src/                  # (Opcional) Lógica modularizada futura
```

## 4. Funcionalidades Implementadas
- [x] **Carregamento Dinâmico**: Lê arquivos `.txt` e formata o dropdown automaticamente.
- [x] **Objetivos dos Treinos**: Extração de resumos via comentários `#`.
- [x] **Interface Mobile-Friendly**: Otimizada para uso em pé na academia.
- [x] **Cronômetro de Descanso**: Localizado na barra lateral para controle entre séries.
- [x] **Histórico de Progresso**: Salva data/hora e nome do treino concluído em arquivo local.
- [x] **Tratamento de Erros**: Validação robusta de arquivos e feedback de erros.
- [x] **Código Modularizado**: Funções separadas para cada responsabilidade.
- [x] **Formatação Consistente**: Função dedicada para formatação de nomes de treino.

## 5. Próximos Passos (Roadmap Sugerido)
1. **Registro de Cargas**: Permitir salvar o peso usado em cada exercício para ver a progressão real.
2. **Dashboard de Evolução**: Gráficos mostrando a frequência de treinos por semana/mês.
3. **Persistência Online**: Migrar o `historico.csv` para um banco de dados ou Google Sheets para evitar perda de dados no deploy.
4. **Notificações de Descanso**: Som ou vibração ao finalizar o cronômetro.
5. **Modo Escuro**: Tema escuro para uso noturno na academia.
6. **Estatísticas**: Total de cargas levantadas, treinos no mês, recordes pessoais.

## 6. Melhorias Recentes (Março 2026)
✅ **Corrigido erro ortográfico**: "Nomeclatura" → "Nomenclatura"
✅ **Tratamento robusto de erros**: Validação de arquivos e feedback apropriado
✅ **Função formatação reutilizável**: `formatar_nome_treino()` elimina duplicação de código
✅ **Validação de linhas malformadas**: Aviso quando formato está incorreto
✅ **Correção .gitignore**: Agora os arquivos `.txt` de treino são versionados corretamente
✅ **Feedback de salvamento**: Retorno de sucesso/erro ao salvar histórico
✅ **Validação de DataFrame vazio**: Tratamento quando arquivo não pode ser carregado
✅ **Cronômetro na área principal**: Movido da sidebar para melhor visibilidade mobile
✅ **Barra de progresso**: Feedback visual durante contagem regressiva
✅ **Layout otimizado**: Tudo visível na mesma tela (exercícios + cronômetro)

---
*Documento atualizado por Gemini CLI*
