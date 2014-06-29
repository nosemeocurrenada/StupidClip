class Message():
    """
    Clase base para mensajes
    Atributos
        timestamp    Hora y fecha a la que se produjo
        message      Mensaje en si
        sender       Remitente (Usuario, pc)
    """
    def __init__(self, message, sender):
        from datetime import datetime
        self.timestamp = datetime.now ()
        self.message = message
        self.sender = sender