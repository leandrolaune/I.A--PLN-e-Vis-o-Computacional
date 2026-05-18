import sys
import subprocess
import os  # Adicionado para gerenciamento de diretórios e caminhos de log
import logging  # Adicionado para o motor de logs de operação

# Garantia de instalação segura e carregamento síncrono do modelo em português
try:
    import rich
    import spacy
    nlp = spacy.load('pt_core_news_sm')
except (ImportError, IOError):
    # Inclusão da flag --user para evitar [WinError 5] Acesso Negado em ambiente local
    subprocess.run([sys.executable, "-m", "pip",
                    "install", "-q", "--user", "rich", "spacy"])
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--user",
                    "https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-3.7.0/pt_core_news_sm-3.7.0.tar.gz"])
    import spacy
    nlp = spacy.load('pt_core_news_sm')

import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt

console = Console()

CORES_ENTIDADES = {
    "ORG": "bold blue",
    "PESSOA": "bold green",
    "LOC": "bold magenta",
    "DATA": "bold dark_goldenrod",
    "VALOR": "bold green",
    "PRODUTO": "bold deep_sky_blue1"
}


def exibir_plataforma_ner(texto_para_processar):
    doc = nlp(texto_para_processar)
    texto_estilizado = Text()
    cursor = 0

    for ent in sorted(doc.ents, key=lambda e: e.start_char):
        texto_estilizado.append(texto_para_processar[cursor:ent.start_char])
        cor = CORES_ENTIDADES.get(ent.label_, "bold black")

        texto_estilizado.append(f" {ent.text} ", style=f"{cor} on #E2E8F0")
        texto_estilizado.append(f"({ent.label_})", style=f"dim {cor}")
        cursor = ent.end_char

    texto_estilizado.append(texto_para_processar[cursor:])

    console.print(
        Panel(
            texto_estilizado,
            title="[bold blue] INTERFACE GRÁFICA DE ENTIDADES [/bold blue]",
            border_style="blue",
            padding=(1, 2)
        )
    )

    if doc.ents:
        tabela = Table(title="\n BANCO DE DADOS ESTRUTURADOS",
                       title_style="bold white", border_style="dim")
        tabela.add_column("Índice", justify="center", style="dim", width=6)
        tabela.add_column("Texto da Entidade", style="bold white", width=30)
        tabela.add_column("Categoria", justify="center")
        tabela.add_column("Descrição do Rótulo", style="italic gray70")

        for idx, ent in enumerate(doc.ents, start=1):
            cor = CORES_ENTIDADES.get(ent.label_, "white")
            tabela.add_row(
                str(idx),
                ent.text,
                f"[{cor}]{ent.label_}[/{cor}]",
                spacy.explain(ent.label_)
            )
        console.print(tabela)
    else:
        console.print(
            "[yellow] Nenhuma entidade detectada no bloco de texto.[/yellow]")


# --- Escopo de Execução e Orquestração da Infraestrutura de PLN ---
if __name__ == "__main__":
    # Configuração e inicialização dinâmica do arquivo físico de log
    os.makedirs("docs", exist_ok=True)
    caminho_log = os.path.join("docs", "log_execucao.txt")

    # Configurado em modo 'a' (append) para adicionar logs sem apagar o que o módulo de visão escreveu
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [PLN] - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(caminho_log, encoding='utf-8', mode='a')
        ]
    )

    logging.info("====================================================")
    logging.info("INICIANDO CONSOLE DE PROCESSAMENTO DE LINGUAGEM NATURAL")
    logging.info("====================================================")

    cabecalho_texto = Text(
        "ENTERPRISE NATURAL LANGUAGE PROCESSING ENGINE\nComponent: Named Entity Recognition (NER) v3.2",
        justify="center"
    )

    console.print("\n" + "="*80, style="dim blue")
    console.print(
        Panel(
            cabecalho_texto,
            title="[bold cyan] CONSOLE DE PROCESSAMENTO LOCAL (PT-BR) [/bold cyan]",
            border_style="bold cyan",
            padding=(1, 1)
        )
    )

    # --- Dataset Macro e Corporativo de Grande Escopo ---
    texto_exemplo = (
        "O cenário de fusões e aquisições no setor energético brasileiro registrou uma movimentação recorde "
        "neste primeiro trimestre. A Eletrobras, maior companhia de geração de energia da América Latina, "
        "firmou um acordo vinculante para a venda de seu complexo eólico localizado em Osório, no Rio Grande do Sul. "
        "A compradora é o fundo de investimentos canadense Brookfield Asset Management, que desembolsará a quantia "
        "de R$ 4,7 bilhões pelo ativo. O anúncio oficial foi conduzido pelo diretor financeiro da estatal, Eduardo Haiama, "
        "durante uma teleconferência transmitida diretamente de Genebra para analistas financeiros globais. "
        "Esse movimento faz parte do plano de desinvestimento da empresa, que busca focar suas operações em linhas de "
        "transmissão de alta tensão. Em contrapartida, o mercado de infraestrutura aguarda o desfecho da nova rodada de "
        "licitações coordenada pela Aneel em Brasília, prevista para ocorrer no dia 22 de junho de 2026. "
        "Fontes ligadas ao Ministério da Fazenda indicam que o governo federal projeta arrecadar mais de R$ 12 bilhões "
        "em bônus de outorga com esses novos contratos. Paralelamente, a Petrobras informou que iniciou negociações com a "
        "Shell para o desenvolvimento conjunto de tecnologias de captura de carbono na Bacia de Santos, um projeto piloto "
        "avaliado inicialmente em R$ 850 milhões. A execução operacional dessa parceria tecnológica ficará sob a supervisão "
        "da engenheira Clarice Coppetti e deve mobilizar centers de pesquisa no Rio de Janeiro e em Londres ao longo dos "
        "próximos três anos. Especialistas do Goldman Sachs destacam que o fluxo de capital estrangeiro direcionado para a "
        "infraestrutura verde no Brasil cresceu cerca de 35% na comparação com o mesmo período do ano passado, consolidando "
        "o país como o principal destino de investimentos sustentáveis entre os mercados emergentes. O fechamento definitivo "
        "de todas essas transações de grande porte ainda depende do escrutínio técnico e da aprovação final do Cade para evitar "
        "concentração de mercado."
    )

    console.print(
        "\n[bold orange3] PROCESSANDO DATASET DE LARGO ESCOPO (ANÁLISE AVANÇADA):[/bold orange3]")

    logging.info(
        "Iniciando extração de Entidades Nomeadas (NER) no dataset corporativo padrão...")
    exibir_plataforma_ner(texto_exemplo)
    logging.info("Dataset padrão processado. Entidades extraídas com sucesso.")

    console.print("\n" + "="*80, style="dim blue")
    console.print(
        "\n[bold green] INPUT SYSTEM | EXECUÇÃO PERSONALIZADA[/bold green]")

    texto_customizado = Prompt.ask(
        "[bold white]Insira o texto em português para análise[/bold white]\n"
        "[dim](Pressione ENTER para processar)[/dim]\n"
    )

    if texto_customizado.strip():
        console.print(
            "\n[bold orange3] PROCESSANDO DATASET DO USUÁRIO:[/bold orange3]")
        logging.info("Texto customizado detectado no prompt de usuário.")
        logging.info("Iniciando varredura NER no texto customizado...")
        exibir_plataforma_ner(texto_customizado)
        logging.info(
            "Processamento do texto customizado concluído com sucesso.")

        # Mantém a janela aberta no terminal local até o usuário pressionar Enter
        Prompt.ask("\n[dim]Pressione ENTER para encerrar o programa[/dim]")
    else:
        console.print(
            "\n[yellow] Nenhuma entrada fornecida. Encerrando o programa.[/yellow]")
        logging.warning(
            "Execução personalizada finalizada sem entrada de texto do usuário.")

    console.print("\n" + "="*80, style="dim blue")
    logging.info("SISTEMA DE PLN FINALIZADO COM SUCESSO.")
    logging.info("====================================================\n")
