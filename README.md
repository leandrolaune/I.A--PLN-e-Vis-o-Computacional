
# Sistemas de Inteligência Artificial: Processamento de Linguagem Natural (PLN) & Visão Computacional

Este repositório compreende o desenvolvimento de uma infraestrutura analítica híbrida dividida em dois motores de execução independentes e modulares: **Processamento de Linguagem Natural (PLN)** focado em Reconhecimento de Entidades Nomeadas (NER) e **Visão Computacional** direcionado para o Processamento Digital de Sinais (PDS), segmentação estrutural e agrupamento estatístico.

O projeto foi estruturado de forma organizada em módulos de domínio específicos para facilitar a legibilidade, auditoria de resultados e testes do sistema.

---

## 📂 Estrutura de Diretórios do Projeto

A organização dos artefatos no repositório segue a topologia mapeada abaixo:

```text
I.A--PLN-e-Vis-o-Computacional/
│
├── PLN/
│   ├── codigo_PLN                      <-- Código-fonte do motor de extração linguística
│   ├── Evidência_log_terminal_de_execução <-- Log persistente gerado em ambiente de execução
│   ├── Terminal_de_Execução_código_PLN_parte1.jpeg <-- Evidência visual do console
│   ├── Terminal_de_Execução_código_PLN_parte2.jpeg <-- Evidência visual do console
│   └── Terminal_de_Execução_código_PLN_parte3.jpeg <-- Evidência visual do console
│
├── Visão Computacional/
│   ├── Código_Visão_Computacional.py    <-- Código-fonte do pipeline de lote (batch processing)
│   ├── Evidência_Log_de_execução_do_terminal.txt <-- Histórico operacional do processamento
│   └── Evidência_Terminal_de_Execução_código_Visão_Computacional.jpeg <-- Gráficos e dashboards
│
├── .gitignore                          <-- Regras de exclusão de arquivos temporários
└── README.md                           <-- Documentação técnica orientada à auditoria

```

---

## 🛠️ Descrição Técnica dos Componentes

### 1. Motor de Visão Computacional (`Código_Visão_Computacional.py`)

Componente analítico focado no processamento de matrizes multidimensionais e reconhecimento de padrões visuais em lote:

* **Aumento de Dados (Data Augmentation):** Multiplicação geométrica a partir de amostras estáveis, utilizando inversões axiais e manipulação de brilho local para expandir o ecossistema para 102 matrizes operacionais independentes.
* **Filtragem Espacial e PDS:** Mitigação de ruídos de alta frequência via desfoque Gaussiano acoplada à equalização adaptativa de histograma limitada por contraste (CLAHE).
* **Segmentação Estrutural:** Limiarização adaptativa utilizando o Algoritmo de Otsu para isolamento de binarização da imagem.
* **Clustering Não-Supervisionado:** Agrupamento estatístico espacial por espectro de cor via algoritmo *K-Means Clustering* ($K=4$).
* **Reconhecimento de Padrões:** Detecção de estruturas faciais baseado em classificadores em cascata (*Haar Cascade Classifier*).

### 2. Motor de Processamento de Linguagem Natural (`codigo_PLN`)

Console interativo corporativo focado em análise morfológica e extração semântica:

* **Análise Léxica e NER (Named Entity Recognition):** Varredura e classificação automatizada de entidades gramaticais complexas nativas do idioma Português (rotulando dados de `ORG` - Organizações, `PESSOA` - Indivíduos, `LOC` - Localizações, `VALOR` - Dados Monetários e `DATA`).
* **Interface de Terminal Rica (Rich UI):** Emprego da biblioteca *Rich* para renderizar os outputs do modelo estatístico `pt_core_news_sm` (*SpaCy*) em painéis estilizados e tabelas de bancos de dados estruturadas em console.

---

## ⚙️ Instalação de Dependências e Configuração do Ambiente

Para que o ambiente local consiga compilar e executar os módulos corretamente, **é necessária a instalação prévia das dependências de prateleira e do modelo estatístico**. Sem este passo, o interpretador Python acusará falhas de módulo não encontrado (`ModuleNotFoundError`).

### 1. Comando para Instalação das Bibliotecas

Abra o terminal do seu sistema operacional ou o terminal integrado do VS Code e execute o comando abaixo para instalar todos os pacotes necessários via `pip`:

```bash
pip install opencv-python numpy scikit-image matplotlib rich spacy

```

### 2. Instalação Obrigatória do Modelo de Idioma (PLN)

O pipeline de Processamento de Linguagem Natural utiliza o modelo treinado em português do *SpaCy*. Ele deve ser baixado explicitamente através do comando:

```bash
python -m spacy download pt_core_news_sm

```

### 🧠 Diagnósticos de Importação (Pylance / VS Code)

Caso o ambiente de desenvolvimento (como a extensão *Pylance* do VS Code) aponte avisos visuais como `Import "cv2" could not be resolved` ou `Import "rich" could not be resolved`, certifique-se de que realizou a instalação dos comandos acima e que o VS Code está apontando para o interpretador correto do Python onde os pacotes foram instalados. Uma vez alinhadas as dependências no ambiente local, os códigos executam de forma totalmente estável, íntegra e sem interrupções.

---

## 📊 Governança, Logs e Auditoria (Provas de Execução)

Para fins de validação técnica e acadêmica, o repositório traz em suas respectivas pastas as evidências irrefutáveis de funcionamento do ecossistema:

1. **Arquivos de Logs Físicos:** Arquivos `.txt` gerados pelo próprio histórico do terminal durante a compilação, mapeando horários e status operacionais (`INFO`/`WARNING`).
2. **Depósito de Imagens:** Capturas de tela (`.jpeg`) expondo as tabelas estruturadas de PLN obtidas a partir de strings complexas e o dashboard analítico em quatro quadrantes gerado pela infraestrutura de visão computacional.

---
