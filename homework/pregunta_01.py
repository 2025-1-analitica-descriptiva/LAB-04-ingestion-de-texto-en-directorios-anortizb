# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import pandas as pd
import os

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # Crear la carpeta output si no existe
    os.makedirs('files/output', exist_ok = True)

    def create_dataset(root_dir):
        data = []

        for sentiment in ['positive', 'negative', 'neutral']:
            sentiment_path = os.path.join(root_dir, sentiment)

            if os.path.exists(sentiment_path):

                for filename in os.listdir(sentiment_path):

                    if filename.endswith('.txt'):
                        filepath = os.path.join(sentiment_path, filename)

                        with open(filepath, 'r', encoding = 'utf-8') as f:
                            phrase = f.read().strip()
                        data.append({'phrase': phrase, 'target': sentiment})
        return pd.DataFrame(data)

    # Generar train_dataset.csv
    train_df = create_dataset('files/input/train')
    train_df.to_csv('files/output/train_dataset.csv', index = False)

    # Generar test_dataset.csv
    test_df = create_dataset('files/input/test')
    test_df.to_csv('files/output/test_dataset.csv', index = False)

if __name__ == "__main__":
    pregunta_01()