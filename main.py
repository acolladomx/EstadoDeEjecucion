import time
from checkpoint_manager import CheckpointHandler

class ProcesadorDeDatos:
    def __init__(self):
        self.progreso = 0
        self.resultados = []

    def ejecutar(self):
        handler = CheckpointHandler()
        
        # Intentar restaurar estado previo
        estado_previo = handler.load()
        if estado_previo:
            self.progreso = estado_previo.progreso
            self.resultados = estado_previo.resultados

        print(f"Iniciando/Reanudando desde el paso: {self.progreso}")

        try:
            for i in range(self.progreso, 10):
                # Simulamos trabajo pesado
                print(f"Trabajando en bloque {i}...")
                time.sleep(2) 
                
                self.progreso = i + 1
                self.resultados.append(f"Resultado_{i}")

                # Guardar checkpoint después de cada paso importante
                handler.save(self)
            
            print("¡Tarea completada con éxito!")
            handler.delete_checkpoint()

        except KeyboardInterrupt:
            print("\n[Error] Ejecución interrumpida por el usuario. El estado se ha guardado.")
