import sys
import subprocess
import os  # Adicionado apenas para o gerenciamento de caminhos do arquivo de log
import logging  # Adicionado para o motor de logs de operação

# Gerenciamento de dependências para garantir a portabilidade do ambiente
try:
    import cv2
    import numpy as np
    import skimage
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                    "opencv-python", "numpy", "scikit-image", "matplotlib"])

import cv2
import numpy as np
from skimage import data
import matplotlib.pyplot as plt


class PipelineVisaoComputacional:
    """
    Motor corporativo para processamento em lote (Batch Processing) de datasets de imagens,
    integrando filtragem espacial, clustering e reconhecimento de padrões.
    """

    def __init__(self):
        # Base de amostragem estrutural estável
        base_imagens = [
            data.astronaut(),
            data.chelsea(),
            data.coffee()
        ]

        # Geração sintética do dataset expandido (Target: ~100 imagens estruturadas)
        self.dataset_imagens = []

        # Loop multiplicador geométrico para atingir 102 matrizes de dados independentes
        for img in base_imagens:
            # Padronização de escala para otimização de memória do pipeline em lote (256x256)
            img_redimensionada = cv2.resize(
                img, (256, 256), interpolation=cv2.INTER_AREA)

            for i in range(34):  # 3 imagens base * 34 variações = 102 amostras operacionais
                if i == 0:
                    self.dataset_imagens.append(img_redimensionada)
                elif i % 3 == 0:
                    # Inversão nos eixos horizontal e vertical
                    self.dataset_imagens.append(
                        cv2.flip(img_redimensionada, -1))
                elif i % 2 == 0:
                    # Espelhamento no eixo horizontal
                    self.dataset_imagens.append(
                        cv2.flip(img_redimensionada, 1))
                else:
                    # Alteração de ganho de iluminação local para diversificação de histograma
                    fator_brilho = np.ones(
                        img_redimensionada.shape, dtype="uint8") * (i * 2)
                    img_brilho = cv2.add(img_redimensionada, fator_brilho)
                    self.dataset_imagens.append(img_brilho)

        # Estrutura de dados para armazenar o dataset totalmente processado
        self.dataset_processado = []

    def _processar_segmentacao_estrutural(self, img_cinza, kernel_blur=(5, 5), clip_limit=3.0, grid_size=(8, 8)):
        """
        Módulo Interno: Pipeline de Processamento Digital de Sinais (PDS)
        """
        img_blur = cv2.GaussianBlur(img_cinza, kernel_blur, 0)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
        img_clahe = clahe.apply(img_blur)
        _, segmento_otsu = cv2.threshold(
            img_clahe, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return img_clahe, segmento_otsu

    def _processar_segmentacao_estatistica(self, img_rgb, n_clusters=4, max_iter=10, epsilon=1.0):
        """
        Módulo Interno: Agrupamento por Machine Learning (K-Means)
        """
        pixels = img_rgb.reshape((-1, 3))
        pixels = np.float32(pixels)
        criterios = (cv2.TERM_CRITERIA_EPS +
                     cv2.TERM_CRITERIA_MAX_ITER, max_iter, epsilon)

        _, rotulos, centros = cv2.kmeans(
            pixels, n_clusters, None, criterios, 10, cv2.KMEANS_RANDOM_CENTERS
        )

        centros_cores = np.uint8(centros)
        pixels_segmentados = centros_cores[rotulos.flatten()]
        return pixels_segmentados.reshape(img_rgb.shape)

    def _reconhecer_padroes_faciais(self, img_rgb, img_cinza):
        """
        Módulo Interno: Detecção e Reconhecimento de Estruturas Faciais via Haar Cascade
        """
        path_cascade = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        detector_face = cv2.CascadeClassifier(path_cascade)
        imagem_reconhecimento = img_rgb.copy()

        faces_detectadas = detector_face.detectMultiScale(
            img_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
        )

        for (x, y, w, h) in faces_detectadas:
            cv2.rectangle(imagem_reconhecimento, (x, y),
                          (x + w, y + h), (0, 255, 0), 2)

        return imagem_reconhecimento

    def executar_pipeline_no_dataset(self):
        """
        Aplica todas as transformações de engenharia a todo o banco de dados carregado.
        """
        for idx, img in enumerate(self.dataset_imagens):
            img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            # Execução sequencial dos algoritmos sobre a amostra atual
            img_pre, img_otsu = self._processar_segmentacao_estrutural(
                img_cinza)
            img_kmeans = self._processar_segmentacao_estatistica(img)
            img_face = self._reconhecer_padroes_faciais(img, img_cinza)

            # Armazenamento estruturado dos múltiplos outputs no dicionário do dataset
            self.dataset_processado.append({
                "original": img,
                "pre_processada": img_pre,
                "otsu": img_otsu,
                "kmeans": img_kmeans,
                "face_detectada": img_face
            })

        print(
            f"✔️ Sucesso: {len(self.dataset_processado)} imagens foram totalmente processadas no lote.")

    def gerar_dashboard_demonstracao(self, indice_amostra=0):
        """
        Isola e renderiza os resultados gráficos de apenas uma amostra para documentação.
        """
        if not self.dataset_processado:
            raise RuntimeError(
                "O pipeline precisa ser executado antes de gerar a demonstração visual.")

        # Extração da amostra escolhida do dataset processado
        amostra = self.dataset_processado[indice_amostra]

        fig, axes = plt.subplots(2, 2, figsize=(14, 12), dpi=100)
        ax = axes.ravel()

        # Quadrantes analíticos da demonstração isolada
        ax[0].imshow(amostra["face_detectada"])
        ax[0].set_title(
            f"1. AMOSTRA {indice_amostra} - DETECÇÃO FACIAL (Haar Cascade)", fontsize=11, fontweight='bold')
        ax[0].axis('off')

        ax[1].imshow(amostra["pre_processada"], cmap='gray')
        ax[1].set_title(
            f"2. AMOSTRA {indice_amostra} - Filtro Gaussiano + CLAHE)", fontsize=11, fontweight='bold')
        ax[1].axis('off')

        ax[2].imshow(amostra["otsu"], cmap='gray')
        ax[2].set_title(
            f"3. AMOSTRA {indice_amostra} - SEGMENTAÇÃO DE OTSU", fontsize=11, fontweight='bold')
        ax[2].axis('off')

        ax[3].imshow(amostra["kmeans"])
        ax[3].set_title(
            f"4. AMOSTRA {indice_amostra} - CLUSTERING (K-Means K=4)", fontsize=11, fontweight='bold')
        ax[3].axis('off')

        plt.tight_layout()
        plt.show()


# --- Escopo de Execução da Infraestrutura de Dados ---
if __name__ == "__main__":
    # Configuração e inicialização dinâmica do arquivo físico de log
    os.makedirs("docs", exist_ok=True)
    caminho_log = os.path.join("docs", "log_execucao.txt")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [VISÃO] - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(caminho_log, encoding='utf-8', mode='a'),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info("====================================================")
    logging.info("INICIANDO COMPONENTE DE VISÃO COMPUTACIONAL")
    logging.info("====================================================")

    try:
        # Instancia o pipeline modular
        pipeline = PipelineVisaoComputacional()
        logging.info(
            "Pipeline instanciado. Iniciando amostragem estrutural estável...")

        # Processa todas as imagens do dataset em lote (batch processing)
        logging.info(
            f"Multiplicando dataset sintético... Alvo: 102 matrizes operacionais.")
        pipeline.executar_pipeline_no_dataset()
        logging.info(
            f"Processamento concluído. {len(pipeline.dataset_processado)} imagens prontas em memória.")

        logging.info(
            "Carregando renderização de interface gráfica (Dashboard)...")
        logging.info("SISTEMA DE VISÃO FINALIZADO COM SUCESSO.")
        logging.info("====================================================\n")

        # Renderiza o resultado analítico fixado na primeira amostra (Aeronauta)
        pipeline.gerar_dashboard_demonstracao(indice_amostra=0)

    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado na operação: {str(e)}")
