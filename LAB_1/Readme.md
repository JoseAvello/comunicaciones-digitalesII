# Laboratorio 1: Digitalización de una Señal Analógica

Este repositorio contiene el desarrollo, diagramas de flujo en **GNU Radio** y análisis experimental para el estudio de la conversión analógico-digital (muestreo y cuantización uniforme)[cite: 1]. Incluye pruebas en tiempo real con hardware SDR (**USRP B200 mini**) y caracterización del ruido de cuantización y aliasing espectral[cite: 1].

## 👥 Integrantes
* **José Avello** — `jose.avello1@mail.udp.cl`[cite: 1]
* **Jean Jorquera** — `jean.jorquera@mail.udp.cl`[cite: 1]
* **Álvaro Valdebenito** — `alvaro.valdebenito@mail.udp.cl`[cite: 1]

**Institución:** Universidad Diego Portales — Escuela de Informática y Telecomunicaciones (Grupo 02, Semestre II - 2026)[cite: 1]

---

## 🚀 Descripción del Proyecto

El proyecto aborda las etapas fundamentales del proceso de digitalización y modulación por código de pulsos (PCM)[cite: 1, 4]:
1. **Muestreo PAM (Natural e Instantánea):** Generación de modulación por amplitud de pulsos a partir de una señal sinusoidal ($f_m = 1\text{ kHz}$) y cuadrada ($f_s = 20\text{ kHz}$)[cite: 1]. Transmisión RF en una frecuencia central de $50\text{ MHz}$[cite: 1].
2. **Evaluación de Aliasing:** Verificación empírica del Teorema de Nyquist al reducir la frecuencia de muestreo hasta el límite crítico $f_s = 2f_m = 2\text{ kHz}$[cite: 2, 4].
3. **Cuantización y Medición de SNR:** Implementación de un retenedor (*Sample & Hold*) y cuantizador uniforme[cite: 1, 4]. Medición experimental de las potencias de señal ($P_s$), ruido ($P_n$) y validación de la **regla teórica de 6 dB por bit**[cite: 3, 4].

---

## 🛠️ Requisitos e Instalación

* **GNU Radio** (v3.8+)[cite: 1]
* **Python 3.x** con `numpy`[cite: 4]
* **UHD / USRP Hardware:** USRP B200 mini (opcional para pruebas en RF)[cite: 1]
* **Instrumentación:** Analizador de espectros (para mediciones de RF)[cite: 1]

---

## 📊 Resultados Destacados

* **Diferencia Espectral PAM:** La modulación PAM instantánea exhibe la envolvente de atenación $H_0(f) = \tau \operatorname{sinc}(f\tau) e^{-j\pi f\tau}$ asociada al retenedor de orden cero, a diferencia de la PAM natural cuya envolvente se rige únicamente por el ciclo de trabajo de los pulsos[cite: 1, 2].
* **Límite de Aliasing:** El solapamiento espectral se confirmó visualmente en simulación y en hardware al cruzar el umbral de $f_s = 2\text{ kHz}$[cite: 2, 4].
* **Escalamiento SNR:** El barrido experimental de $N=3$ a $N=8$ bits entregó un ajuste de regresión lineal de **$6.92\text{ dB/bit}$**, validando la regla empírica cercana a $6.02\text{ dB/bit}$[cite: 3, 4].

---

## 💻 Código de Bloques Personalizados (Python)

El proyecto utiliza bloques sincrónicos embebidos en GNU Radio para el muestreo y la cuantización uniforme[cite: 1]:

### 1. Bloque Sampler (Retenidor)
```python
# Núcleo de retención de muestras
for i in range(len(out)):
    if in_ctrl[i] > 0 and not self.prev_ctrl:
        self.held = in_data[i]
    out[i] = self.held
    self.prev_ctrl = in_ctrl[i] > 0
```[cite: 4]

### 2. Bloque Quantizer (Cuantizador Uniforme)
```python
# Cálculo de niveles y cuantización uniforme
L = 2**self.N
delta = 2.0 * self.Mp / L
x = np.clip(input_items[0], -self.Mp, self.Mp - np.finfo(np.float32).eps)
idx = np.floor((x + self.Mp) / delta)
output_items[0][:] = -self.Mp + (idx + 0.5) * delta
```[cite: 4]

---

## 📚 Referencias
* Documentación oficial de GNU Radio[cite: 4].
* Oppenheim, A. V., & Schafer, R. W. *Discrete-Time Signal Processing*. 3rd ed., Pearson, 2010[cite: 4].
