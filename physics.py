class Physics:
    def __init__(self, gravity=10):
        self.gravity = gravity

    def apply_gravity(self, time, item):
        item.V_y += self.gravity * time
        item.positiony += item.V_y * time


        ground_level = item.window_height - 100 - item.rect.height
        if item.positiony >= ground_level:
            item.positiony = ground_level
            item.V_y = 0
            item.is_jumping = False
            item.alive = False


        elif item.positiony < 0:
            item.positiony = 0
            item.V_y = 0
