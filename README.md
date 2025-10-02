
# 📊 Proyecto Final – Análisis Económico con Python

**Segundo corte – Curso de programación**  
**Autor:** Edgar Felipe Plata Jaimes  
**Fecha de entrega:** 3 de octubre de 2025  
**Archivo único:** `proyecto.py`  
**Indicador analizado:** PIB per cápita (NY.GDP.PCAP.CD)  
**Países incluidos:** Colombia, México y Brasil  
**Fuente de datos:** API del Banco Mundial

---

## 🎯 Objetivo

Desarrollar un programa en Python que permita descargar, procesar y analizar datos económicos reales, aplicando los conceptos vistos en clase. El análisis se enfoca en la evolución del PIB per cápita entre 2010 y 2022.

---

## 🧱 Estructura del archivo

El archivo `proyecto.py` incluye:

- Parámetros configurables (indicador, países, años)
- Validaciones de entrada
- Descarga de datos desde la API del Banco Mundial
- Cálculo de estadísticas por país (media, mediana, desviación estándar)
- Visualización gráfica con `matplotlib`
- Menú interactivo para guiar al usuario

---

## 🛠️ Requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes librerías:

```bash
pip install pandas requests matplotlib
```

---

## 🚀 Ejecución

### En terminal (Windows, Mac o Linux):

```bash
python proyecto_final.py
```

### En Google Colab:

1. Sube el archivo `proyecto.py`
2. Ejecuta en una celda:

```python
!python proyecto_final.py
```

---

## ✅ Criterios cumplidos según la rúbrica

### Interfaz de Usuario

- **IU1:** Comentarios explicativos y formato claro
- **IU2:** Menú interactivo con instrucciones visibles
- **IU3:** Validación robusta de entradas

### Funcionalidad

- **F1:** Descarga y análisis de datos reales
- **F2:** Código modular, sin errores y con manejo de excepciones

### Entrega Final

- **EF1:** Planificación clara dentro del archivo único
- **EF2:** Presentación profesional y completa
- **EF3:** Código explicable en el quiz, con lógica sencilla y trazabilidad

---

## 📚 Referencias

- [World Bank API Documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- Documentación oficial de `pandas` y `matplotlib`
```

---


