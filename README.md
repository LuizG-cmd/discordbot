-----

# 🤖 Aldeia Promo Bot

Um simples bot do Discord escrito em Python que utiliza `discord.py` e **Selenium** para buscar rapidamente o preço de **Placas de Vídeo** no site da **KaBuM\!**.

-----

## ✨ Funcionalidades

  * **Busca de Preços Rápida:** Encontra o primeiro preço e link disponível para um modelo de placa de vídeo específico na KaBuM\!.
  * **Integração com Discord:** Responde diretamente no canal com o nome do produto, preço e um link.

-----

## 🛠️ Instalação e Configuração

Siga os passos abaixo para colocar o bot em funcionamento.

### Pré-requisitos

Você precisará ter o **Python** (versão 3.8+) instalado, além do **ChromeDriver** (compatível com sua versão do Google Chrome) ou qualquer outro driver de navegador para o Selenium.

### 1\. Clonar o Repositório

Como o código está inline, salve o código Python em um arquivo chamado `bot.py`.

### 2\. Instalar Dependências

Abra o terminal no diretório onde salvou o arquivo e instale as bibliotecas necessárias:

```bash
pip install discord.py selenium
```

### 3\. Configurar o Token do Bot

Você precisa obter um **Token de Bot** do seu aplicativo no [Portal do Desenvolvedor do Discord](https://www.google.com/search?q=https://discord.com/developers/applications).

Edite a linha `TOKEN = ""` no arquivo `bot.py` e insira seu token:

```python
TOKEN = "SEU_TOKEN_AQUI"
```

> ⚠️ **Aviso de Intenções:** Certifique-se de que a intenção `Message Content Intent` está ativada nas configurações do seu bot no Portal do Desenvolvedor, pois o bot precisa ler o conteúdo das mensagens.

### 4\. Executar o Bot

Execute o arquivo Python para iniciar o bot:

```bash
python bot.py
```

Você verá a mensagem de confirmação no console:

```
✅ Bot conectado como <Nome_do_Seu_Bot>
```

-----

## 🚀 Como Usar no Discord

O bot usa o prefixo de comando padrão `!`

### Comando: `!preco`

Use este comando seguido pelo nome ou modelo da placa de vídeo que deseja buscar.

| Comando | Descrição |
| :--- | :--- |
| `!preco <modelo>` | Busca o preço do primeiro produto relevante encontrado na KaBuM\!. |

**Exemplo:**

```
!preco RTX 4070 ti
```

**Resposta do Bot (Exemplo):**

```
🔍 Buscando preço para: **RTX 4070 ti**...
**Placa De Vídeo Gigabyte Geforce Rtx 4070 Ti Gaming Oc 12g, Dlss 3, Gddr6x**
💰 Preço: R$ 5.999,99
🔗 [Ver no Kabum](<link_para_o_produto>)
```

-----

## ⚙️ Tecnologias Utilizadas

  * **Python**
  * **discord.py** (Para a interface com o Discord)
  * **Selenium** (Para o *web scraping* dos preços)

-----

## 📝 Observações

O *web scraping* pode quebrar se a KaBuM\! alterar a estrutura HTML do seu site (os nomes das classes `productCard`, `nameCard`, `priceCard` e o *tag* `a`). Caso isso ocorra, o código na função `buscar_kabum` precisará ser atualizado.

-----

Posso te ajudar a criar um comando de ajuda (`!help`) para este bot ou talvez integrar outra loja na busca?
