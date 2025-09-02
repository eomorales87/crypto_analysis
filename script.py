import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, parse_dates=["date"])

def plot_price_analysis(df: pd.DataFrame, crypto_name: str, save_path: str):
    plt.figure(figsize=(12,6))
    plt.plot(df["date"], df["price"], label="Precio", alpha=0.7)
    plt.plot(df["date"], df["MA7"], label="MA7")
    plt.plot(df["date"], df["MA30"], label="MA30")
    plt.plot(df["date"], df["MA90"], label="MA90")
    plt.title(f"Precio Histórico y Medias Móviles - {crypto_name}")
    plt.xlabel("Fecha")
    plt.ylabel("USD")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()

def main():
    for crypto in ["bitcoin", "ethereum"]:
        df = load_data(f"data/{crypto}_data.csv")
        plot_price_analysis(df, crypto.capitalize(), f"results/plots/{crypto}_plot.png")
        print(f"Gráfico de {crypto} guardado en results/plots/{crypto}_plot.png")

if __name__ == "__main__":
    main()
