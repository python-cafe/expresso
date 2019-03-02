import requests
import os


def baixar_arquivo(url, endereco=None):
    if endereco is None:
        endereco = os.path.basename(url.split("?")[0])
    resposta = requests.get(url, stream=True)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            for parte in resposta.iter_content(chunk_size=256):
                novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == "__main__":
    # testando a função
    test_url = "https://www.visgraf.impa.br/Data/RefBib/PS_PDF/wtd2018/adaptive-reconstruction-implicit-finalv1.pdf"
    baixar_arquivo(test_url)