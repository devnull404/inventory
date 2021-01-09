# Sistema de Punto de Venta (ABARROTES DON RAFA)
En este repositorio se encuentra alojado el sistema de punto de venta de Abarrotes Don Rafa, con ubicación en el poblado de Hobomo, Campeche, y podrás encontrar todo lo necesario para mantener y agregar funcionalidades a nuestro sistema si eres parte de este establecimiento como becario. El código principal se encuentra en el archivo **main.py**.

# ¿Dónde puedes encontrarnos?
En el poblado de Hobomó, Campeche, en un horario de 7:00 AM - 11:00 PM, y en la siguiente imagen podrás encontrar un mapa con nuestra ubicación: 

![alt text](https://github.com/devnull404/inventory/blob/main/assets/map.png)

## Arquitectura del POS propuesto
El sistema de Punto de Venta propuesto consta de 5 partes, estas son:

- Raspberry Pi 4B.
- Router.
- Impresora.
- Lector de código de barras.
- Cajón de efectivo.

En la siguiente imagen, podemos apreciar cómo están interconectados cada uno:

![alt text](https://github.com/devnull404/inventory/blob/main/assets/setup.png)


## Inizialización del POS
Para inicializar el sistema de venta en mostrador, es necesario importar la librería a la consola Python, y llamar al método **SellProducts** de la siguiente manera

```python
import main
main.SellProducts()
```

Para más información sobre cómo utilizarlo en modo inventario, mantenerlo y añadir más funcionalidades, serás capacitado in situ a la hora de trabajar con el sistema, donde aprenderás todo lo necesario para diseñar e implementar un POS.

## Algunas imágenes del sistema interconectado
Nuestro equipo trabaja desde SSH para programar el sistema directamente desde un equipo portatil para facilitar el desarrollo y mantenimiento del sistema. 

![alt text](https://github.com/devnull404/inventory/blob/main/assets/System.jpeg)
**Conexión básica: Laptop -> Raspberry Pi vía SSH:Ethernet.**

![alt text](https://github.com/devnull404/inventory/blob/main/assets/rp.jpeg)
**Raspberry Pi 4B: último modelo, con UBUNTU 20.04.**

![alt text](https://github.com/devnull404/inventory/blob/main/assets/gun.jpeg)
**Lector de Barras digital.**