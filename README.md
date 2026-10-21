# Análisis de ventas de Northwind

## Descripción del proyecto

Este proyecto tiene como objetivo analizar los datos de ventas de la base de datos Northwind utilizando SQL y Python. Se realizan consultas para identificar los productos con mayores ingresos y los empleados asociados a mayores ingresos por ventas.

## Herramientas utilizadas

- **SQLite:** consultas y extracción de datos.
- **Python:** procesamiento y análisis de datos.
- **Pandas:** organización de los resultados en tablas.
- **Matplotlib y Seaborn:** visualización de los datos mediante gráficos de barras.

## Análisis realizados

1. Identificación de los 10 productos con mayores ingresos.
2. Identificación de los 10 empleados asociados a mayores ingresos.
3. Creación de gráficos para facilitar la interpretación de los resultados.

## Estructura del proyecto

- `analisis_ventas.py`: código Python para realizar el análisis.
- `sql/consultas.sql`: consulta SQL para identificar los productos con mayores ingresos.
- `README.md`: documentación del proyecto.

## Cómo ejecutar el proyecto

1. Instalar Python.
2. Instalar las bibliotecas necesarias:

   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Colocar el archivo `Northwind.db` en el directorio desde el que se ejecutará el programa.
4. Ejecutar:

   ```bash
   python analisis_ventas.py
   ```

## Resultados

Los resultados incluyen tablas con los productos y empleados destacados, además de gráficos de barras para comparar los ingresos calculados.

**Nota:** los ingresos calculados no representan ganancias netas, ya que no se descuentan los costos ni otros gastos.
