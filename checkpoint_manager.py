import pickle
import os

class CheckpointHandler:
    def __init__(self, filename="checkpoint.pkl"):
        self.filename = filename

    def save(self, data):
        """Guarda el estado actual en un archivo binario."""
        with open(self.filename, "wb") as f:
            pickle.dump(data, f)
        print(f"[Sistema] Checkpoint guardado en: {self.filename}")

    def load(self):
        """Carga el estado si el archivo existe."""
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
            print(f"[Sistema] Estado restaurado desde: {self.filename}")
            return data
        return None

    def delete_checkpoint(self):
        """Limpia el checkpoint al finalizar la tarea con éxito."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
