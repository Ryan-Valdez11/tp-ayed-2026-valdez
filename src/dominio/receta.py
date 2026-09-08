class Receta:
    def __init__(self, titulo: str, categoria: str, tiempo_preparacion: int, ingredientes: list, pasos: list):
        self.titulo = titulo
        self.categoria = categoria
        self.tiempo_preparacion = tiempo_preparacion  # Tiempo en minutos
        self.ingredientes = ingredientes
        self.pasos = pasos

    def __repr__(self):
        return f"Receta('{self.titulo}', '{self.categoria}', {self.tiempo_preparacion} min)"