class Physics:
    def __init__(self, gravity=10):
        self.gravity = gravity

    def apply_gravity(self, time, item):
        item.V_y += self.gravity * time
        item.positiony += item.V_y * time
        if item.positiony > item.window_height:
            item.positiony = item.window_height
            item.V_y = 0
            item.is_jumping = False
            item.alive = False

