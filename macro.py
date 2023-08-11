import mrcfile
import matplotlib.pyplot as plt

def visualize_mrc(file_path):
    try:
        # Abre o arquivo MRC para leitura
        with mrcfile.open(file_path, mode='r') as mrc:
            data = mrc.data

        # Exibe a imagem
        plt.imshow(data[0], cmap='gray')
        plt.title("Imagem MRC")
        plt.colorbar()
        plt.show()
    except Exception as e:
        print("Erro ao visualizar o arquivo MRC:", e)

# Substitua 'caminho/do/seu/arquivo.mrc' pelo caminho completo para o seu arquivo MRC
mrc_file_path = 'C:/Users/Zero/Desktop/tft tela 2.mcr'

# Chama a função para visualizar o arquivo MRC
visualize_mrc(mrc_file_path)
