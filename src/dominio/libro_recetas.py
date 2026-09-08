from src.dominio.receta import Receta

class LibroDeRecetas:
    def __init__(self):
        self.recetas = []
        self._cargar_catalogo_inicial()

    def _cargar_catalogo_inicial(self):
        """Catálogo inicial con recetas cargadas directamente en código (hardcodeadas)."""
        r1 = Receta(
            titulo="Milanesas con Papas Fritas",
            categoria="Plato Principal",
            tiempo_preparacion=45,
            ingredientes=["carne para milanesa", "huevos", "pan rallado", "papas", "aceite", "sal"],
            pasos=[
                "Pasar la carne por huevo batido con condimentos.",
                "Empanar con el pan rallado y presionar bien.",
                "Cortar las papas en bastones.",
                "Freír las papas y las milanesas en aceite caliente hasta dorar."
            ]
        )

        r2 = Receta(
            titulo="Empanadas de Carne",
            categoria="Entrada",
            tiempo_preparacion=60,
            ingredientes=["tapas de empanada", "carne picada", "cebolla", "huevo duro", "aceitunas", "comino"],
            pasos=[
                "Saltear la cebolla e incorporar la carne picada con especias.",
                "Dejar enfriar el relleno y agregar huevo duro y aceitunas.",
                "Rellenar las tapas y realizar el repulgue.",
                "Hornear a fuego fuerte a 200°C durante 15-20 minutos."
            ]
        )

        r3 = Receta(
            titulo="Flan Casero",
            categoria="Postre",
            tiempo_preparacion=50,
            ingredientes=["leche", "huevos", "azúcar", "esencia de vainilla"],
            pasos=[
                "Hacer un caramelo con azúcar en una flanera.",
                "Batir los huevos con la leche, el azúcar y la vainilla.",
                "Colocar la mezcla en la flanera y cocinar a baño María al horno.",
                "Dejar enfriar bien antes de desmoldar."
            ]
        )

        self.recetas.extend([r1, r2, r3])

    def obtener_todas(self):
        return self.recetas
    