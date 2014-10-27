class Interface(object):
    """
    Permet d'interagir avec une machine à caoua
    """

    def __init__(self):
        self.machine = None

    def run(self):
        if self.machine and self.machine.maintenance:
            state = 'Maintenance'
        else:
            state = 'Conso'
        action = input(state+">> ")
