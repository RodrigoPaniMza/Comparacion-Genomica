# Comparacion-Genomica
Trabajo Verano de la ciencia de la región centro 2025

Este repositorio contiene todos los archivos utilizados y generados durante el análisis de ortogrupos y alineamientos locales entre proteínas humanas y de la babosa Deroceras laeve. El objetivo del estudio fue identificar ortología entre especies, explorar métricas comparativas y generar visualizaciones para respaldar las conclusiones del trabajo de investigación.
# Contenido del repositorio
├── README.md
├── analisis_ortogrupos.ipynb       # Notebook principal con el análisis de ortogrupos y estadísticas
├── resultados_investigacion.pdf    # Documento final con los resultados del proyecto
├── scripts/
│   └── alineamientos.py            # Script ejecutado en el clúster (alineamientos locales con Biopython)
├── data/
│   ├── ortogrupos.tsv              # Tabla con ortogrupos compartidos y específicos por especie
│   ├── genes_humanos.tsv           # Anotaciones y secuencias de proteínas humanas
│   ├── genes_deroceras.tsv         # Anotaciones y secuencias de proteínas de *Deroceras laeve*
│   └── *.csv / *.tsv               # Otros archivos tabulares de entrada usados en el análisis
├── resultados/
│   ├── treemap_ortogrupos.png      # Visualización jerárquica de distribución de genes
│   └──comparacion_estadistica.png # Gráficas comparativas entre especies
