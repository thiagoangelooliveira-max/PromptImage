from openai import OpenAI
import base64
from dotenv import load_dotenv

load_dotenv()

def gerar_imagem(contexto):
    contexto = contexto.strip()

    if not contexto:
        raise ValueError("Descreva a imagem que deseja gerar.")

    client = OpenAI()
    result = client.images.generate(
        model="gpt-image-2.5-sunburst",
        prompt=contexto,
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open("otter.png", "wb") as arquivo:
        arquivo.write(image_bytes)

    return image_bytes


if __name__ == "__main__":
    descricao = input("Descreva a imagem que deseja gerar: ")
    gerar_imagem(descricao)
    print("Imagem salva em otter.png!")
