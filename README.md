# PromptImage

Aplicação em Python com Streamlit para criar imagens a partir de descrições e editar a imagem gerada com novas instruções. A interface funciona no navegador e utiliza a API da OpenAI para processar os pedidos.

## Funcionalidades

- Criação de imagens a partir de uma descrição em texto.
- Edição da imagem original a partir de uma instrução.
- Exibição da imagem original e da nova versão na página.
- Manutenção dos resultados durante as interações usando `st.session_state`.
- Validação de campos vazios, indicadores de carregamento e mensagens de erro.
- Interface com pequenos ajustes de HTML e CSS para cores e alinhamento.

## Arquivos do projeto

| Arquivo | Função |
| --- | --- |
| `app.py` | Interface Streamlit e chamadas às funções de geração e edição. |
| `gerar_imagem.py` | Define `gerar_imagem(contexto)`, salva `otter.png` e retorna os bytes da imagem. |
| `editar_imagem.py` | Define `editar_imagem(orientacao)`, lê `otter.png`, salva `variacao.png` e retorna os bytes da edição. |
| `requirements.txt` | Dependências Python com suas versões. |
| `.env` | Configuração local da chave da API; deve ser criado por quem executar o projeto. |

## Instalação

É necessário ter Python instalado e uma chave da API com acesso ao modelo configurado no código.

No terminal, dentro da pasta do projeto, crie e ative um ambiente virtual. No Windows com PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com a sua chave:

```dotenv
OPENAI_API_KEY=sua_chave_aqui
```

Não publique o arquivo `.env` nem a chave da API no repositório.

Os dois scripts atualmente usam o identificador `gpt-image-2.5-sunburst`. Esse é o valor presente no projeto; a execução depende de ele estar disponível para a sua conta. Se necessário, ajuste o parâmetro `model` nos dois arquivos para um modelo compatível com as operações utilizadas.

## Executar a aplicação

Na pasta do projeto, execute:

```powershell
python -m streamlit run app.py
```

Abra o endereço exibido no terminal, normalmente `http://localhost:8501`. A página abre no navegador, mas o servidor roda no seu computador: mantenha o terminal aberto enquanto usa a aplicação. Para encerrar, pressione `Ctrl+C`.

## Como usar

1. Em **Criar imagem**, descreva a imagem desejada e clique em **Criar imagem**.
2. Aguarde a imagem aparecer na página.
3. Em **Editar imagem**, descreva a alteração desejada.
4. Clique em **Gerar nova versão** e aguarde o resultado.

O botão de edição só fica disponível depois que uma imagem é gerada na sessão. Ao gerar outra imagem, a edição anterior deixa de ser exibida.

## Executar pelo terminal

Os scripts também podem ser executados individualmente, sem a interface:

```powershell
python gerar_imagem.py
python editar_imagem.py
```

Cada script solicita a descrição no terminal. Para editar, é necessário que `otter.png` já exista na pasta de execução.

## Como as imagens são armazenadas

As funções decodificam a resposta em Base64, salvam a imagem em disco e retornam seus bytes para o Streamlit exibir com `st.image()`.

- `otter.png`: imagem original; sobrescrita a cada geração.
- `variacao.png`: resultado da edição; sobrescrito a cada edição.

Cada edição parte de `otter.png`, não da última variação. Os arquivos são salvos na pasta em que o comando é executado. A aplicação não mantém um histórico de imagens.

Os nomes dos arquivos são compartilhados entre execuções. A versão atual é adequada ao uso local individual; para múltiplos usuários, é necessário separar os arquivos por sessão para evitar sobrescritas.

Os arquivos `streamlit.stdout.log` e `streamlit.stderr.log`, quando presentes, registram mensagens da execução. Eles não são obrigatórios para o funcionamento da aplicação.

## Tecnologias

- **Python**: lógica da aplicação.
- **Streamlit**: interface no navegador.
- **OpenAI SDK**: chamadas de geração e edição de imagens.
- **python-dotenv**: carregamento da configuração do arquivo `.env`.
- **base64**: conversão das respostas em bytes de imagem.
