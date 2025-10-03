# Analizador Económico: descarga, resume y grafica indicadores
# Fuente de datos: API del Banco Mundial (World Bank API v2)
# Indicador por defecto: NY.GDP.PCAP.CD (PIB per cápita, USD)
import requests
import pandas as pd
import matplotlib.pyplot as plt
#Definimos clases
class AnalizadorEconomico:

    #Clase que encapsula el flujo de trabajo:
    #1) Descargar datos desde la API del Banco Mundial para uno o varios países y un rango de años.
    #2) Guardar los datos en un DataFrame de pandas.

    def __init__(self, indicador, paises, anio_inicio, anio_fin):
        self.indicador = indicador
        self.paises = paises
        self.anio_inicio = anio_inicio
        self.anio_fin = anio_fin
        self.df = pd.DataFrame()

    def descargar_datos(self):
        print(f"ℹ️INFO: Descargando datos de {self.indicador} para países: {', '.join(self.paises)}")
        registros = []
  
  #Utilizamos Api para traer los datos 
  #Aquí recorremos todas las filas (país, año, valor)


        for pais in self.paises:
            url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{self.indicador}?date={self.anio_inicio}:{self.anio_fin}&format=json&per_page=100"
            try:
                respuesta = requests.get(url)
                datos = respuesta.json()[1]
                registros += [
                    {
                        "país": entrada["country"]["value"],
                        "año": entrada["date"],
                        "valor": entrada["value"]
                    }
                    for entrada in datos
                ]
            except Exception as e:
                print(f"❌ERROR: No se pudo obtener datos para {pais}: {e}")

        self.df = pd.DataFrame(registros)
        print(f"✅ÉXITO: Datos descargados correctamente: {len(self.df)} registros")

    def analizar_datos(self):
        if self.df.empty:
            print("❌ERROR: No hay datos para analizar.")
            return

        resumen = self.df.groupby("país")["valor"].agg(["mean", "median", "std"]).reset_index()
        print("\n📈 Estadísticas por país:")
        print(resumen)

        plt.figure(figsize=(10, 6))
        for pais in self.df["país"].unique():
            datos_pais = self.df[self.df["país"] == pais]
            plt.plot(datos_pais["año"], datos_pais["valor"], label=pais)

        plt.title("PIB per cápita (USD)")
        plt.xlabel("Año")
        plt.ylabel("Valor")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def mostrar_menu():
    print("\n📊 Bienvenido al Analizador Económico")
    print("1. Descargar datos")
    print("2. Analizar datos")
    print("3. Salir")

def main():
    analizador = AnalizadorEconomico(
        indicador="NY.GDP.PCAP.CD",
        paises=["CO", "MX", "BR"],
        anio_inicio=2010,
        anio_fin=2022
    )

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion not in ["1", "2", "3"]:
            print("❌ Opción inválida. Intente de nuevo.")
            continue

        if opcion == "1":
            analizador.descargar_datos()
        elif opcion == "2":
            analizador.analizar_datos()
        elif opcion == "3":
            print("👋 Gracias por usar el programa. Hasta pronto.")
            break

if __name__ == "__main__":
    main()
