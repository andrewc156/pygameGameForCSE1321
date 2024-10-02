class Physics:
    def __init__(self, item):
        self.gravity = 10

    def update(self, time, item):
        item.V_y -= self.gravity
        item.positiony += item.V_y
