Claro! Criar um arquivo `README.md` detalhado para acompanhar seu projeto é uma prática excelente para garantir que outros desenvolvedores possam entender e usar seu código corretamente. Aqui está um exemplo de como você poderia estruturar o `README.md` para o aplicativo que discutimos, incluindo a descrição do programa, instruções de instalação e uso, e explicações detalhadas das funções e variáveis:

```markdown
# PDF Assistant

## Descrição
O PDF Assistant é uma aplicação de interface gráfica (GUI) desenvolvida em Python que permite aos usuários carregar arquivos PDF, extrair seu texto e fazer perguntas baseadas no texto extraído. O programa utiliza o modelo GPT-Neo da EleutherAI para gerar respostas às perguntas feitas, proporcionando uma ferramenta interativa para análise e consulta de documentos.

## Funcionalidades
- Carregar múltiplos arquivos PDF.
- Exibir o caminho dos arquivos carregados.
- Permitir ao usuário digitar perguntas.
- Gerar respostas com base no texto extraído dos PDFs usando o modelo GPT-Neo.

## Dependências
Este projeto depende das seguintes bibliotecas:
- `pdfplumber` para extração de texto de arquivos PDF.
- `transformers` e `torch` para carregar e utilizar o modelo GPT-Neo.
- `tkinter` para a interface gráfica.

## Instalação

### Clonar o Repositório
Primeiro, clone o repositório para sua máquina local usando:
```bash
git clone https://github.com/seuusuario/pdf-assistant.git
cd pdf-assistant
```

### Instalar as Dependências
Você pode instalar todas as dependências necessárias executando:
```bash
pip install pdfplumber transformers torch
```

## Uso
Para executar o aplicativo, navegue até o diretório do projeto e execute:
```bash
python app.py
```

## Estrutura do Código

### `app.py`

#### Importações
- `tkinter` é usado para criar a interface gráfica.
- `pdfplumber` é utilizado para extrair texto dos PDFs carregados.
- `transformers` e `torch` são usados para carregar o modelo GPT-Neo e realizar a geração de texto.

#### Funções

##### `extract_text_from_pdf(pdf_path)`
Extrai todo o texto de um arquivo PDF especificado pelo caminho `pdf_path`.
- **Parâmetros**:
  - `pdf_path`: Caminho para o arquivo PDF.
- **Retorno**:
  - `full_text`: Texto extraído do PDF.

##### `generate_response(question, context)`
Gera uma resposta baseada em uma pergunta e um contexto dado, utilizando o modelo GPT-Neo.
- **Parâmetros**:
  - `question`: Texto da pergunta feita pelo usuário.
  - `context`: Texto extraído dos PDFs como contexto para a pergunta.
- **Retorno**:
  - Resposta gerada pelo modelo.

##### GUI Widgets
- `open_file_btn`: Botão para abrir o diálogo de seleção de arquivo.
- `clear_btn`: Botão para limpar a lista de arquivos PDF carregados.
- `pdf_text`: Área de texto onde os caminhos dos arquivos carregados são exibidos.
- `question_entry`: Campo de entrada para o usuário digitar perguntas.
- `submit_btn`: Botão para enviar a pergunta e gerar uma resposta.
- `answer_text`: Área de texto onde a resposta é exibida.

#### Variáveis
- `pdf_files`: Lista que armazena os caminhos dos arquivos PDF carregados.

## Suporte
Para suporte, abra uma issue no repositório GitHub do projeto ou envie um e-mail para marcelocarvalho.p@gmail.com.

## Autores
- Marcelo de Carvalho Pereira

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE.md` para detalhes.
```

