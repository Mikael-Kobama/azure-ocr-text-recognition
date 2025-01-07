import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from msrest.authentication import CognitiveServicesCredentials

# Defina sua chave e ponto de extremidade
subscription_key = "<your_subscription_key>"
endpoint = "<your_endpoint>"

# Criar um cliente
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Caminho para a imagem
image_path = "inputs/image1.jpg"

# Abrir a imagem
with open(image_path, "rb") as image_stream:
    result = client.recognize_printed_text_in_stream(image_stream, TextRecognitionMode.PRINTED)

# Salvar os resultados em um arquivo de texto
with open("output/result1.txt", "w") as result_file:
    for region in result.regions:
        for line in region.lines:
            for word in line.words:
                result_file.write(word.text + " ")

