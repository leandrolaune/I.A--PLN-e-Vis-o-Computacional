Se você quer fazer tudo pelo terminal, além de parecer muito mais profissional, o processo é bem mais rápido. Como o seu professor é exigente, fazer pelo terminal garante que nenhum arquivo temporário seja enviado de forma errada e deixa o histórico de commits impecável.

Substitua todo o processo visual do VS Code por estes comandos direto no terminal (abra o terminal com `Ctrl + '`):

---

## 🛠️ O Passo a Passo pelo Terminal

### Passo 1: Autenticação (Caso ainda não tenha feito)

Se você nunca usou o Git nesse computador, configure seu nome e e-mail (use o mesmo e-mail da sua conta do GitHub):

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email@github.com"

```

### Passo 2: Inicializar o Repositório Local

Garante que você está na pasta raiz do seu projeto (onde estão os arquivos `codigo_PLN.py` e `codigo_visão_computacional.py`) e digite:

```bash
git init

```

*(Esse comando cria uma pasta oculta `.git` e transforma seu diretório local em um repositório).*

### Passo 3: Estagiar os Arquivos (Adicionar ao Git)

Para preparar os arquivos para o salvamento, use o comando de adição. O ponto `.` significa "adicionar tudo o que está nesta pasta":

```bash
git add .

```

> 💡 **Por que isso é seguro?** Como criamos o arquivo `.gitignore` anteriormente, o Git vai ler as regras dele e ignorar automaticamente as pastas inúteis como `__pycache__` e `.vscode`, adicionando apenas o que importa.

### Passo 4: Criar o Primeiro Commit

Agora, salve o estado atual dos seus arquivos localmente com uma mensagem clara e formal para o seu professor ver:

```bash
git commit -m "feat: estrutura inicial do sistema hibrido e documentacao"

```

### Passo 5: Configurar a Branch Principal

Por padrão, o Git local antigo pode criar uma branch chamada `master`, mas o GitHub hoje usa o padrão `main`. Mude o nome dela para evitar conflitos:

```bash
git branch -M main

```

---

## 🌐 Conectando com o GitHub

Agora você precisa ir até o site do GitHub no seu navegador rapidinho para criar o "balde" onde o seu código vai cair:

1. Acesse **github.com** e faça login.
2. No canto superior direito, clique no botão de **`+` (Mais)** e selecione **New repository** (Novo repositório).
3. No campo **Repository name**, coloque o nome do projeto (ex: `ia-pln-e-visao-computacional`).
4. **⚠️ Atenção Crítica:** Marque a opção **Public** (Público) para o seu professor conseguir acessar.
5. **NÃO** marque nenhuma caixinha de "Add a README", "Add .gitignore" ou "Choose a license". Deixe tudo em branco, pois nós já criamos esses arquivos no seu computador.
6. Clique no botão verde **Create repository**.

Na página seguinte, o GitHub vai te dar uma tela cheia de comandos. Nós só precisamos de **dois** comandos que estão na seção *"or push an existing repository from the command line"*.

---

### Passo 6: Vincular o Terminal ao GitHub e Subir o Código

Copie e cole estes dois últimos comandos no seu terminal do VS Code (ajustando com o link do seu repositório que o site gerou):

```bash
# 1. Diz ao seu computador para onde enviar o código (substitua pelo SEU link)
git remote add origin https://github.com/seu-usuario/ia-pln-e-visao-computacional.git

# 2. Envia os arquivos definitivamente para a nuvem
git push -u origin main

```

> 🛸 **Nota:** Se for a primeira vez que você faz isso pelo terminal, ele vai abrir uma janelinha do navegador pedindo para você clicar em **"Sign in with your browser"** (Fazer login pelo navegador) para autorizar o terminal a mexer na sua conta do GitHub. É só clicar e autorizar.

Pronto! Quando o terminal terminar de carregar os objetos (chegar a 100%), atualize a página do GitHub no seu navegador. Seu projeto estará lindamente publicado e pronto para o link ser enviado ao professor.
