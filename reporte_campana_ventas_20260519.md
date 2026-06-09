# Reporte de Campaña — Campaña de Ventas
**Cuenta:** RABID 2026 CP (`act_26624228317198141`)
**Período analizado:** 17–18 de mayo de 2026 (últimos 7 días)
**ROAS objetivo:** 3x
**Fecha del reporte:** 19 de mayo de 2026

---

## Resumen ejecutivo

La campaña tiene **2 días activa**. No se registraron compras en el período, lo que arroja un ROAS de 0x frente al objetivo de 3x. Sin embargo, el píxel sí registra actividad hasta el nivel de checkout (2 pagos iniciados con ticket estimado de ~$47.000 ARS c/u), lo que indica que el problema no es la llegada de tráfico sino la conversión final. Los rankings de calidad aún no están disponibles por el poco tiempo activa.

**Diagnóstico principal:** El embudo se corta en dos puntos críticos — la página de producto no convierte (2% de carritos sobre vistas) y no se registran compras post-checkout (posible falla en el píxel de confirmación de compra).

---

## Métricas del período

| Métrica | Valor | Benchmark | Estado |
|---------|-------|-----------|--------|
| Entrega | ACTIVA | — | 🟢 |
| Presupuesto diario | $10.000 ARS/día | — | — |
| Importe gastado | $15.878,73 ARS | — | — |
| Valor de conversión de compras | $0 | — | — |
| **ROAS** | **0x** | **Objetivo: 3x** | 🔴 |
| Compras | 0 | — | — |
| Costo por compra | — | — | — |
| % Compras / Visitas p.d. | 0% | — | 🔴 |
| Valor de conversión promedio | — | — | — |
| % Compras / Pagos iniciados | 0% (0/2) | 🔴 <10% / 🟡 10–30% / 🟢 >30% | 🔴 |
| Pagos iniciados | 2 | — | — |
| Costo por pago iniciado | $7.939 ARS | — | — |
| % Checkout / Carritos | 100% (2/2) | 🔴 <30% / 🟡 30–50% / 🟢 >50% | 🟢 |
| Artículos al carrito | 2 | — | — |
| Costo por carrito | $7.939 ARS | — | — |
| % Carritos / Ver contenido | 2,0% (2/98) | 🔴 <10% / 🟡 10–20% / 🟢 >20% | 🔴 |
| Visualizaciones de contenido | 98 | — | — |
| Costo por visualización | $162 ARS | — | — |
| % Ver contenido / Visitas p.d. | 132% (98/74) | 🔴 <60% / 🟡 60–100% / 🟢 >100% | 🟢 |
| Visitas a página de destino | 74 | — | — |
| Costo por visita | $214 ARS | — | — |
| % Visitas / Clics salientes | 119% (74/62) | 🔴 <50% / 🟡 50–70% / 🟢 >70% | 🟢 |
| Clics salientes | 62 | — | — |
| CTR saliente | 1,17% | 🔴 <1% / 🟡 1–2% / 🟢 >2% | 🟡 |
| Costo por clic saliente | $256 ARS | — | — |
| % Reproducciones 3s / Impresiones | 14,2% (752/5.285) | 🔴 <20% / 🟡 20–30% / 🟢 >30% | 🔴 |
| Tiempo promedio de reproducción | 3s | 🔴 <3s / 🟡 3–6s / 🟢 >6s | 🟡 |
| Frecuencia | 1,95 | <3 ideal / >5 saturado | 🟢 |
| Alcance | 2.710 personas | — | — |
| Costo por mil alcanzadas | $5.860 ARS | — | — |
| Impresiones | 5.285 | — | — |
| CPM | $3.004 ARS | — | — |
| Fecha de creación | 17/05/2026 | — | — |
| Métricas de calidad | No disponible aún | ABOVE_AVERAGE ideal | — |

---

## 1️⃣ ¿Qué pasó?

Se invirtieron **$15.878 ARS** en los primeros 2 días de campaña. No se registró ninguna compra, lo que resulta en un **ROAS de 0x frente al objetivo de 3x** — 100% por debajo del objetivo. 🔴

El píxel sí captura actividad hasta el nivel de checkout: 2 personas iniciaron el proceso de pago con un ticket estimado de **~$47.000 ARS por unidad**. Esto indica que hay demanda real, pero la conversión final no está ocurriendo (o no se está registrando).

> ⚠️ Contexto importante: la campaña tiene solo 2 días activa. Los rankings de calidad aún aparecen como "no disponible" — esto es normal en las primeras 48–72 hs. Las conclusiones definitivas requieren al menos 7 días y un mínimo de 50 eventos de optimización.

---

## 2️⃣ ¿Por qué pasó?

### Embudo de conversión

```
Impresiones (5.285)
      ↓ CTR 1,17% 🟡
Clics salientes (62)
      ↓ 119% 🟢
Visitas a página de destino (74)
      ↓ 132% 🟢
Ver contenido (98)
      ↓ 2,0% 🔴  ← CUELLO DE BOTELLA PRINCIPAL
Agregar al carrito (2)
      ↓ 100% 🟢
Checkout iniciado (2)
      ↓ 0% 🔴  ← SEGUNDO CUELLO DE BOTELLA
Compras (0)
```

**Problema 1 — Página de producto no convierte (2,0% 🔴)**
De 98 personas que vieron el producto, solo 2 lo pusieron en el carrito. La landing page o la página de producto tiene algo que frena la decisión de compra: precio, imágenes, descripción, CTA o propuesta de valor.

**Problema 2 — 0 compras post-checkout (0% 🔴)**
Las 2 personas que llegaron al proceso de pago no completaron la compra. Dos posibles causas:
- Fricción en el proceso de pago (pasos, métodos, UX)
- El píxel de Meta no está disparando en la página de confirmación de compra

**Señal del creativo**
- % Reproducciones 3s: 14,2% 🔴 — el gancho del video no retiene en los primeros 3 segundos
- Tiempo promedio de reproducción: 3s 🟡 — en el límite aceptable

**Lo que funciona bien**
- La landing carga rápido: 119% visitas/clics 🟢
- La página de producto se consume bien una vez que el usuario llega: 132% ver contenido/visitas 🟢
- Frecuencia baja (1,95): sin saturación de audiencia 🟢

---

## 3️⃣ ¿Qué haremos?

### Prioridad 1 — Verificar el píxel de compra *(hoy)*
Confirmar que el evento `Purchase` del píxel de Meta dispara correctamente en la página de confirmación de compra. Usar el **Meta Pixel Helper** (extensión de Chrome) o el **Administrador de Eventos** en Business Manager para verificarlo. Si no está disparando, todas las optimizaciones automáticas de la campaña están trabajando sin el dato más importante.

### Prioridad 2 — Optimizar la página de producto *(esta semana)*
Con un 2% de conversión del producto al carrito, hay una fricción significativa. Revisar:
- ¿El precio es visible y claro?
- ¿Las imágenes del producto son de calidad y muestran detalle?
- ¿El botón de compra/agregar al carrito es prominente?
- ¿Hay prueba social? (reseñas, cantidad vendida, etc.)
- ¿La propuesta de valor está clara above the fold?

### Prioridad 3 — Mejorar el gancho del creativo *(próxima semana)*
El 14,2% de reproducción en los primeros 3 segundos está por debajo del benchmark. Testear una versión del video que abra con el beneficio principal o un elemento visual que detenga el scroll. Los primeros 3 segundos son los que deciden si alguien sigue mirando.

### Prioridad 4 — No modificar la campaña antes del 24/05 *(esperar)*
Con solo 2 días de datos, el algoritmo de Meta está en plena fase de aprendizaje. Cualquier cambio estructural (audiencia, presupuesto, creativos en el mismo conjunto) reinicia ese proceso. Dejar correr hasta el **24 de mayo** y evaluar con datos completos de 7 días.

---

## Próximos pasos recomendados

| Acción | Responsable | Fecha límite |
|--------|-------------|--------------|
| Verificar píxel de compra con Meta Pixel Helper | Marketing/Tech | 20/05/2026 |
| Auditar página de producto (precio, imágenes, CTA, prueba social) | Marketing | 21/05/2026 |
| Nuevo análisis con 7 días de datos | Marketing | 24/05/2026 |
| Testear nuevo creativo con gancho mejorado | Creativos | 26/05/2026 |

---

*Reporte generado el 19/05/2026 — Metodología 3 Q's (Felipe Vergara) · Datos: Meta Marketing API v21.0*
