import os
import glob
import pandas as pd
import numpy as np

def load_real_data():
    """
    Tenta carregar dados reais do diretório /data.
    Suporta CSV automaticamente.
    """

    files = glob.glob("data/*.csv")

    if len(files) == 0:
        print("⚠️ Nenhum dado real encontrado em /data. Usando fallback simulado.")
        z = np.linspace(0.01, 1.5, 50)
        y = np.random.normal(70, 5, size=len(z))
        yerr = np.ones_like(y)
        return z, y, yerr

    # usa o primeiro dataset real disponível
    df = pd.read_csv(files[0])

    # tentativa de mapeamento padrão cosmológico
    z = df.iloc[:, 0].values
    y = df.iloc[:, 1].values if df.shape[1] > 1 else np.zeros_like(z)
    yerr = df.iloc[:, 2].values if df.shape[1] > 2 else np.ones_like(z)

    print(f"📦 Dados reais carregados: {files[0]} | N={len(z)}")

    return z, y, yerr


if __name__ == "__main__":
    z, y, yerr = load_real_data()
    print("OK load:", len(z))
