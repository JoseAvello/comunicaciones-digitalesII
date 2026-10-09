# Laboratorio 1: Digitalización de una Señal Analógica

Este repositorio contiene el desarrollo, diagramas de flujo en **GNU Radio** y análisis experimental para el estudio de la conversión analógico-digital (muestreo y cuantización uniforme)[cite: 1]. Incluye pruebas en tiempo real con hardware SDR (**USRP B200 mini**) y caracterización del ruido de cuantización y aliasing espectral[cite: 1].

## 👥 Integrantes
* **José Avello** — `jose.avello1@mail.udp.cl`
* **Jean Jorquera** — `jean.jorquera@mail.udp.cl`
* **Álvaro Valdebenito** — `alvaro.valdebenito@mail.udp.cl`

**Institución:** Universidad Diego Portales — Escuela de Informática y Telecomunicaciones (Grupo 02, Semestre II - 2026)[cite: 1]

---

## 🚀 Descripción del Proyecto

El proyecto aborda las etapas fundamentales del proceso de digitalización y modulación por código de pulsos (PCM)[cite: 1, 4]:
1. **Muestreo PAM (Natural e Instantánea):** Generación de modulación por amplitud de pulsos a partir de una señal sinusoidal ($f_m = 1\text{ kHz}$) y cuadrada ($f_s = 20\text{ kHz}$)[cite: 1]. Transmisión RF en una frecuencia central de $50\text{ MHz}$[cite: 1].
2. **Evaluación de Aliasing:** Verificación empírica del Teorema de Nyquist al reducir la frecuencia de muestreo hasta el límite crítico $f_s = 2f_m = 2\text{ kHz}$[cite: 2, 4].
3. **Cuantización y Medición de SNR:** Implementación de un retenedor (*Sample & Hold*) y cuantizador uniforme[cite: 1, 4]. Medición experimental de las potencias de señal ($P_s$), ruido ($P_n$) y validación de la **regla teórica de 6 dB por bit**[cite: 3, 4].

---

## 🛠️ Requisitos e Instalación

* **GNU Radio** (v3.8+)
* **Python 3.x** con `numpy`
* **UHD / USRP Hardware:** USRP B200 mini (opcional para pruebas en RF)
* **Instrumentación:** Analizador de espectros (para mediciones de RF)

---
