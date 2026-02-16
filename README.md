# Python Checkpoint Manager (PyCheckPoint)

Implementación de una solución de Application Checkpointing diseñada para proporcionar tolerancia a fallos en procesos de ejecución prolongada.

## Descripción del Proyecto

En entornos de computación de alto rendimiento (HPC) o procesamiento de datos masivos, las interrupciones (errores de red, cierres manuales o fallos de hardware) pueden causar la pérdida de horas de trabajo acumulado. 

Este proyecto utiliza la serialización binaria de la librería 'pickle' de Python para capturar el estado completo de un objeto en ejecución. Esto permite que el programa se reanude exactamente desde el último punto de control guardado en el disco.

## Características Técnicas

* Persistencia de Estado: Serialización de instancias de clases y estructuras de datos complejas.
* Recuperación Automática: Detección de archivos de checkpoint existentes al inicio para restaurar el contexto.
* Manejo de Interrupciones: Control de excepciones para 'KeyboardInterrupt', asegurando la integridad del estado antes del cierre.
* Gestión de Archivos: Eliminación automática del archivo temporal tras la finalización exitosa del proceso.

## Tecnologías Utilizadas

* Lenguaje: Python 3.x
* Librerías:
    * pickle: Para la serialización y deserialización de objetos.
    * os: Para la gestión de archivos y rutas del sistema.
    * time: Para la simulación de carga de trabajo y latencia.

## Guía de Uso
