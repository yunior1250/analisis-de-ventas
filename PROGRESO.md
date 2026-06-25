# 📒 Bitácora del proyecto: Análisis de Ventas

Proyecto para el portafolio. Aprendiendo análisis de datos paso a paso.
Stack del usuario: Laravel, Flutter, Android, Python.

---

## 🗺️ El mapa completo (5 etapas)

```
1. Tener los datos        →  un archivo .csv
2. Cargarlos y limpiarlos →  con Pandas
3. Explorar y graficar    →  en un Jupyter Notebook  (esto es "el análisis")
4. Mostrar resultados     →  una app web (Streamlit)
5. Subirlo a la nube      →  GitHub + Streamlit Cloud (el demo del portafolio)
```

---

## ✅ Lo que YA hicimos

- [x] **Paso 1: Carpeta + entorno virtual**
  - Carpeta del proyecto: `~/Analista/analisis-ventas`
  - Creado el entorno virtual `venv`
  - (Tuvimos que instalar `python3.12-venv` con `sudo apt install python3.12-venv`)
- [x] **Paso 2: Librerías instaladas** dentro del venv:
  - pandas, numpy, matplotlib, seaborn, jupyter
- [x] **Paso 3: Conseguir los datos**
  - Creado `ventas.csv` a mano en VS Code (10 ventas de prueba)
  - Aprendido qué es un CSV y por qué se usa (vs Excel)
  - Columnas: fecha, producto, categoria, cantidad, precio_unitario, total, ciudad, vendedor
- [x] **Paso 4: Cargar los datos con Pandas**
  - Creado `analisis.py` con `pd.read_csv("ventas.csv")`
  - Ejecutado con `python analisis.py` (¡tabla cargada! = un DataFrame)
  - Aprendido: SIEMPRE activar `venv` antes de ejecutar (`source venv/bin/activate`)

---

## ▶️ Cómo RETOMAR mañana (importante)

Cada vez que vuelvas a trabajar, abre la terminal y haz esto:

```bash
cd ~/Analista/analisis-ventas
source venv/bin/activate
```

Debes ver `(venv)` al inicio de la línea. Si no, repite el `source`.

---

## ⏭️ Lo que SIGUE (próxima sesión)

- [x] **Paso 5: Explorar** los datos con Pandas
      - [x] Totales y promedios: `.sum()`, `.mean()`, `len()`
      - [x] Agrupar por producto/ciudad/vendedor: `datos.groupby("col")["total"].sum()`
      - [x] Ordenar con `.sort_values(ascending=False)` (mayor a menor)
      - Insights: Laptop = top producto; Arequipa = top ciudad; Luis = top vendedor
- [x] **Paso 6: Graficar** con matplotlib (LISTO ✅)
      - [x] Gráfico de barras dinero por vendedor → `grafico-ventas-vendedor.png`
      - [x] Gráfico de barras dinero por producto → `grafico-ventas-producto.png`
      - [x] Gráfico de barras dinero por ciudad → `grafico-ventas-ciudad.png`
      - Aprendido: `plt.figure()` antes de cada gráfico = "hoja nueva" para no dibujar encima
      - Aprendido: patrón = agrupar (`groupby`) → ordenar → `.plot(kind="bar")` → títulos → `savefig`
      - NOTA: VS Code subraya `import matplotlib` con "Cannot find module" porque
        el editor mira el Python del sistema, NO el venv. El código corre igual en la
        terminal. Para quitar el aviso: Ctrl+Shift+P > "Python: Select Interpreter" > elegir el de ./venv/
- [x] **Paso 7: App web** con Streamlit (LISTO ✅)
      - [x] Instalado streamlit (`pip install streamlit`)
      - [x] Creado `app.py` (separado de `analisis.py`)
      - [x] `st.title`, `st.write`, `st.dataframe(datos)` → tabla interactiva
      - [x] KPIs con `st.columns(3)` + `st.metric` → Total vendido / N° ventas / Ticket promedio
      - [x] Los 3 gráficos en la web con `fig, ax = plt.subplots()` + `st.pyplot(fig)`
      - Aprendido: se ejecuta con `streamlit run app.py` (NO `python app.py`)
      - Aprendido: f-strings `f"S/. {x:,.0f}"` para coma de miles sin decimales
- [x] **Paso 8: Subir a GitHub + Streamlit Cloud** (LISTO ✅ — ¡PROYECTO TERMINADO!)
      - [x] `requirements.txt` con `pip freeze > requirements.txt`
      - [x] `.gitignore` (ignora `venv/`, `__pycache__/`, `*.pyc`)
      - [x] `git init` + `git add .` + `git commit` + `git push`
      - [x] Repo en GitHub: https://github.com/yunior1250/analisis-de-ventas
      - [x] Desplegado en Streamlit Community Cloud (share.streamlit.io) → app pública
      - [ ] PENDIENTE: anotar aquí el LINK PÚBLICO final de la app (copiarlo de Streamlit Cloud)
      - Aprendido GIT desde cero: commit = punto de guardado; remote = GitHub; push = subir
      - PROBLEMA RESUELTO: el editor (Antigravity) secuestraba la contraseña con
        `GIT_ASKPASS=...`. Solución: `GIT_ASKPASS= GIT_TERMINAL_PROMPT=1 git push ...`
        + token (PAT) classic con scope `repo` como contraseña.

---

## 💡 Recordatorios útiles

- Para **salir** del entorno virtual: escribe `deactivate`
- Para **abrir Jupyter** (más adelante): `jupyter notebook`
- Las librerías están instaladas SOLO dentro de `venv` (la "burbuja" del proyecto).

---

_Última sesión: 2026-06-23 — 🎉 PROYECTO TERMINADO (Pasos 1 al 8 completos).
App Streamlit con KPIs + tabla + 3 gráficos, subida a GitHub y DESPLEGADA en
Streamlit Community Cloud (link público funcionando).
RETOMAR EN (próxima sesión, opcional/pulido):
  1. Copiar el LINK PÚBLICO de la app y pegarlo arriba en Paso 8 y en el README.
  2. Crear un README.md bonito para el repo (descripción + captura + link) → es lo
     primero que ve un reclutador en GitHub.
  3. Pulido opcional de la app: gráficos lado a lado con st.columns, colores, o
     un st.selectbox para filtrar por ciudad/vendedor (interactividad = más impacto).
  4. (Más adelante) Pasar el análisis a un Jupyter Notebook para mostrar el razonamiento._
