# proyecto_final.py

import requests
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ CONFIGURACIÓN ------------------
INDICADOR = "NY.GDP.PCAP.CD"
PAISES = ["CO", "MX", "BR"]
ANIO_INICIO = 2010
ANIO_FIN = 2022

# ------------------ UTILIDADES ------------------
def validar_opcion(opcion, opciones_validas):
    try:
        return int(opcion) in opciones_validas
    except ValueError:
        return False

def mostrar_mensaje(tipo, texto):
    iconos = {
        "info": "ℹ️INFO:",
        "exito": "✅ÉXITO:",
        "error": "❌ERROR:"
    }
    print(f"{iconos.get(tipo, '')} {texto}")

# ------------------ DESCARGA DE DATOS ------------------
def descargar_datos():
    mostrar_mensaje("info", f"Descargando datos de {INDICADOR} para países: {', '.join(PAISES)}")
    registros = []

    for pais in PAISES:
        url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{INDICADOR}?date={ANIO_INICIO}:{ANIO_FIN}&format=json&per_page=100"
        try:
            respuesta = requests.get(url)
            datos = respuesta.json()[1]
            for entrada in datos:
                registros.append({
                    "país": entrada["country"]["value"],
                    "año": entrada["date"],
                    "valor": entrada["value"]
                })
        except Exception as e:
            mostrar_mensaje("error", f"No se pudo obtener datos para {pais}: {e}")

    df = pd.DataFrame(registros)
    mostrar_mensaje("exito", f"Datos descargados correctamente: {len(df)} registros")
    return df

# ------------------ ANÁLISIS DE DATOS ------------------
def analizar_datos(df):
    if df is None or df.empty:
        mostrar_mensaje("error", "No se proporcionaron datos para analizar.")
        return

    resumen = df.groupby("país")["valor"].agg(["mean", "median", "std"]).reset_index()
    print("\n📈 Estadísticas por país:")
    print(resumen)

    # Gráfico
    plt.figure(figsize=(10, 6))
    for pais in df["país"].unique():
        datos_pais = df[df["país"] == pais]
        plt.plot(datos_pais["año"], datos_pais["valor"], label=pais)

    plt.title("PIB per cápita (USD)")
    plt.xlabel("Año")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ------------------ MENÚ PRINCIPAL ------------------
def mostrar_menu():
    print("\n📊 Bienvenido al Analizador Económico")
    print("1. Descargar datos")
    print("2. Analizar datos")
    print("3. Salir")

def main():
    datos = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if not validar_opcion(opcion, [1, 2, 3]):
            mostrar_mensaje("error", "Opción inválida. Intente de nuevo.")
            continue

        opcion = int(opcion)
        if opcion == 1:
            datos = descargar_datos()
        elif opcion == 2:
            analizar_datos(datos)
        elif opcion == 3:
            print("👋 Gracias por usar el programa. Hasta pronto.")
            break

if __name__ == "__main__":
    main()