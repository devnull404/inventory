# Sistema de Punto de Venta (ABARROTES DON RAFA)
En este repositorio se encuentra alojado el sistema de punto de venta de Abarrotes Don Rafa, con ubicación en el poblado de Hobomo, Campeche, y podrás encontrar todo lo necesario para mantener y agregar funcionalidades a nuestro sistema si eres parte de este establecimiento como becario. El código principal se encuentra en el archivo **main.py**.

## Arquitectura del POS propuesto
El sistema de Punto de Venta propuesto consta de 5 partes, estas son:

- Raspberry Pi 4B.
- Router.
- Impresora.
- Lector de código de barras.
- Cajón de efectivo.

En la siguiente imagen, podemos apreciar cómo están interconectados cada uno:



Para inicializar el sistema de venta en mostrador, es necesario importar la librería a la consola Python, y llamar al método **SellProducts** de la siguiente manera

```python
import main
main.SellProducts()
```