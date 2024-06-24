# hotel_reservation_system.py

class Habitacion:
    """
    Clase que representa una habitación de hotel.

    Atributos:
    numero (int): Número de la habitación.
    tipo (str): Tipo de habitación (por ejemplo, 'Simple', 'Doble').
    precio (float): Precio por noche de la habitación.
    ocupada (bool): Indica si la habitación está ocupada o no.
    """

    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        """
        Reserva la habitación si está libre.

        Returns:
        str: Mensaje indicando si la habitación fue reservada o ya estaba ocupada.
        """
        if not self.ocupada:
            self.ocupada = True
            return f"Habitación {self.numero} ha sido reservada."
        else:
            return f"Habitación {self.numero} ya está ocupada."

    def liberar(self):
        """
        Libera la habitación si está ocupada.

        Returns:
        str: Mensaje indicando si la habitación fue liberada o ya estaba libre.
        """
        if self.ocupada:
            self.ocupada = False
            return f"Habitación {self.numero} ha sido liberada."
        else:
            return f"Habitación {self.numero} ya está libre."


class Hotel:
    """
    Clase que representa un hotel.

    Atributos:
    nombre (str): Nombre del hotel.
    habitaciones (list): Lista de habitaciones del hotel.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación a la lista de habitaciones del hotel.

        Args:
        habitacion (Habitacion): La habitación a agregar.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """
        Muestra las habitaciones disponibles del hotel.

        Returns:
        str: Mensaje con los números de las habitaciones disponibles.
        """
        disponibles = [hab for hab in self.habitaciones if not hab.ocupada]
        if disponibles:
            return f"Habitaciones disponibles: {[hab.numero for hab in disponibles]}"
        else:
            return "No hay habitaciones disponibles."

    def reservar_habitacion(self, numero):
        """
        Reserva una habitación específica si está disponible.

        Args:
        numero (int): El número de la habitación a reservar.

        Returns:
        str: Mensaje indicando si la habitación fue reservada o no encontrada.
        """
        for hab in self.habitaciones:
            if hab.numero == numero:
                return hab.reservar()
        return f"Habitación {numero} no encontrada."

    def liberar_habitacion(self, numero):
        """
        Libera una habitación específica si está ocupada.

        Args:
        numero (int): El número de la habitación a liberar.

        Returns:
        str: Mensaje indicando si la habitación fue liberada o no encontrada.
        """
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