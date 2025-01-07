# Projeto de Reconhecimento de Texto com Azure

Este projeto demonstra como usar o **Azure Cognitive Services** para realizar o reconhecimento de texto em imagens usando o serviço de **OCR** (Reconhecimento Óptico de Caracteres).

## Estrutura do Projeto

- **inputs/**: Contém as imagens utilizadas no processo de OCR.
- **output/**: Contém os resultados do reconhecimento de texto extraído das imagens.
- **requirements.txt**: Arquivo com as dependências necessárias (simulando que estamos utilizando a Azure SDK).

## Passo a Passo

1. **Criação do Repositório**
   - Criamos um repositório no GitHub para armazenar o código e os resultados do nosso projeto.

2. **Uso do Azure OCR**
   - Usamos a API de OCR do Azure para detectar e extrair texto de imagens.
   - As imagens foram carregadas para o serviço, e o serviço retornou os textos extraídos.

3. **Resultado**
   - Os resultados do OCR foram armazenados na pasta `output/`, com cada arquivo contendo o texto extraído de uma imagem específica.

4. **Como rodar o projeto (Simulação)**

   Para rodar este projeto, siga as etapas abaixo (simulando o uso do Azure):

   - Crie uma conta no Azure.
   - Crie um serviço de **Cognitive Services** e obtenha sua chave de API e ponto de extremidade.
   - Instale as bibliotecas necessárias, incluindo o SDK do Azure.
   
   ```bash
   pip install azure-cognitiveservices-vision-computervision
