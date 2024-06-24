# hotel_reservation_system.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return f"Habitación {self.numero} ha sido reservada."
        else:
            return f"Habitación {self.numero} ya está ocupada."

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            return f"Habitación {self.numero} ha sido liberada."
        else:
            return f"Habitación {self.numero} ya está libre."

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        disponibles = [hab for hab in self.habitaciones if not hab.ocupada]
        if disponibles:
            return f"Habitaciones disponibles: {[hab.numero for hab in disponibles]}"
        else:
            return "No hay habitaciones disponibles."

    def reservar_habitacion(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero:
                return hab.reservar()
        return f"Habitación {numero} no encontrada."

    def liberar_habitacion(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero:
                return hab.liberar()
        return f"Habitación {numero} no encontrada."

# Ejemplo de uso
hotel = Hotel("Hotel POO")
habitacion1 = Habitacion(101, "Simple", 100)
habitacion2 = Habitacion(102, "Doble", 150)

hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

print(hotel.mostrar_habitaciones_disponibles())
print(hotel.reservar_habitacion(101))
print(hotel.mostrar_habitaciones_disponibles())
print(hotel.liberar_habitacion(101))
print(hotel.mostrar_habitaciones_disponibles())