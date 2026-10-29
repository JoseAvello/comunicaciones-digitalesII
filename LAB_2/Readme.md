# Laboratorio 2: Interferencia Intersímbolo (ISI)

**Asignatura:** CIT2111 Comunicaciones Digitales  
**Institución:** Universidad Diego Portales — Escuela de Informática y Telecomunicaciones  
**Semestre:** II - 2026  
**Grupo:** 02  

### Integrantes
* **José Avello** — [jose.avello1@mail.udp.cl](mailto:jose.avello1@mail.udp.cl)
* **Jean Jorquera** — [jean.jorquera@mail.udp.cl](mailto:jean.jorquera@mail.udp.cl)
* **Álvaro Valdebenito** — [alvaro.valdebenito@mail.udp.cl](mailto:alvaro.valdebenito@mail.udp.cl)

---

## 1. Descripción del Proyecto

Este laboratorio estudia el fenómeno de la **Interferencia Intersímbolo (ISI)** en una transmisión digital de banda base implementada en **GNU Radio**. 

A través del análisis con **diagramas de ojo**, se evalúa cómo la limitación de ancho de banda del canal y la adición de ruido gaussiano degradan la señal transmitida. Se comparan dos esquemas de transmisión:
1. **Pulsos Rectangulares:** Sensibles a la ISI cuando el canal restringe el ancho de banda.
2. **Pulsos Coseno Alzado (Root Raised Cosine - RRC):** Diseñados para cumplir el criterio de Nyquist y eliminar la ISI en los instantes de muestreo.

---

## 2. Parámetros del Sistema

Los parámetros configurados en los diagramas de flujo de GNU Radio son:

* **Frecuencia de Muestreo ($f_s$):** $100\text{ kHz}$
* **Período de Símbolo ($T_s$):** $5\text{ ms}$
* **Tasa de Símbolos ($R_s$):** $200\text{ símbolos/s}$ ($R_s = \frac{1}{T_s}$)
* **Muestras por Símbolo ($N_s$):** $500\text{ muestras}$ ($N_s = f_s \cdot T_s = 100\,000 \cdot 0.005$)
* **Mapeo Bipolar:** $0 \mapsto -1$ y $1 \mapsto +1$

---

## 3. Bloques de GNU Radio Utilizados

| Bloque | Función y Justificación |
| :--- | :--- |
| **Random Uniform Source** | Genera una secuencia binaria aleatoria (valores $0$ y $1$) como señal de prueba. |
| **Chunks to Symbols** | Sustituye cada bit de entrada por su nivel bipolar correspondiente ($-1$ y $+1$). |
| **Repeat** | Repite cada muestra $500$ veces a $100\text{ kHz}$ para formar un pulso rectangular de $5\text{ ms}$. |
| **Low Pass Filter** | Modela un canal de comunicaciones limitado en banda con frecuencia de corte ($f_c$) ajustable. |
| **Noise Source** | Agrega ruido gaussiano blanco para simular las perturbaciones del canal. |
| **Root Raised Cosine Filter** | Filtro de conformación de pulso utilizado para mitigar la ISI cumpliendo el criterio de Nyquist. |
| **QT GUI Eye Sink** | Muestra el diagrama de ojo superponiendo segmentos de señal sincronizados con el período de símbolo. |
| **QT GUI Range** | Control interactivo para variar parámetros en tiempo real ($f_c$, amplitud de ruido $\sigma$, roll-off $\alpha$). |

---

## 4. Experimentos y Resultados

### 4.1. Pulso Rectangular
* **Frecuencia de Corte del Canal ($f_c$):**
  * **$f_c = 100\text{ Hz}$ (Corte bajo):** Atenúa fuertemente las componentes de alta frecuencia. Los flancos se suavizan y los pulsos se expanden en el tiempo, provocando el cierre del diagrama de ojo debido a la ISI.
  * **$f_c = 1000\text{ Hz}$ (Corte alto):** Preserva mejor el espectro de la señal, reduciendo la ISI y manteniendo una clara apertura horizontal y vertical.
* **Ruido Gaussiano:**
  * Al aumentar la amplitud del ruido ($\sigma = 0.05 \rightarrow 0.25$), se incrementa la dispersión vertical de las trazas (grosor de las bandas lógicas), reduciendo el margen de decisión e incrementando la probabilidad de error.

### 4.2. Pulso Coseno Alzado (RRC)
* **Criterio de Nyquist:**
  * **$f_c = 1500\text{ Hz}$:** El ancho de banda del canal abarca el espectro completo del pulso RRC, eliminando la ISI en los instantes de muestreo y logrando máxima apertura.
  * **$f_c = 150\text{ Hz}$:** El canal corta parte del espectro requerido, rompiendo la condición de Nyquist y reapareciendo la ISI.
* **Factor de Roll-off ($\alpha$):**
  * **$\alpha = 0.10$ (Bajo):** Optimiza el uso del espectro, pero la respuesta al impulso decae lentamente ($\text{sinc}$), generando alta sensibilidad al *jitter* de fase y una menor apertura horizontal.
  * **$\alpha = 0.80$ (Alto):** Acelera el decaimiento temporal del pulso, aumentando la tolerancia a errores de sincronización (ojo más abierto horizontalmente) a costa de un mayor ancho de banda.
* **Resolución Temporal ($N_s$):**
  * Al reducir el muestreo a $N_s = 50$ muestras por símbolo, el diagrama de ojo pierde definición gráfica, mostrando trazos poligonales en lugar de curvas suaves.

---

## 5. Estructura del Repositorio

```text
.
├── flowgraphs/
│   ├── lab2_pulso_rectangular.grc   # Diagrama de flujo para pulso rectangular
│   └── lab2_coseno_alzado.grc      # Diagrama de flujo con filtros RRC
├── doc/
│   └── informe_laboratorio_2.pdf    # Informe completo del laboratorio
└── README.md                        # Documentación del proyecto
```

---

## 6. Referencias
1. H. Nyquist, *"Certain topics in telegraph transmission theory,"* Transactions of the American Institute of Electrical Engineers, vol. 47, no. 2, pp. 617-644, 1928.
2. GNU Radio, *"QT GUI Eye Sink,"* Documentación Oficial de GNU Radio.
3. GNU Radio, *"Root Raised Cosine Filter,"* Documentación Oficial de GNU Radio.
4. A. Arslan, *"Raised Cosine Pulse,"* EE445S Real-Time Digital Signal Processing Laboratory, UT Austin.
5. R. Muñoz Lara, *"Laboratorio 2: Interferencia intersímbolo (ISI),"* CIT2111 Comunicaciones Digitales, Universidad Diego Portales, semestre II, 2026.
