from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

def editar_imagem(orientacao):
    orientacao = orientacao.strip()

    if not orientacao:
        raise ValueError("Descreva a alteração que deseja fazer.")

    client = OpenAI()
    with open("otter.png", "rb") as imagem:
        result = client.images.edit(
            model="gpt-image-2.5-sunburst",
            image=imagem,
            prompt=orientacao,
        )

    image_bytes = base64.b64decode(result.data[0].b64_json)

    with open("variacao.png", "wb") as arquivo:
        arquivo.write(image_bytes)

    return image_bytes


if __name__ == "__main__":
    orientacao = input("O que você deseja alterar? ")
    editar_imagem(orientacao)
    print("Imagem editada salva em variacao.png!")
