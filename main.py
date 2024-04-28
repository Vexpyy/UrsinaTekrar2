from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

Entity.default_shader = bls

class CustomSky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = "earthlike_planet.hdr",
            double_sided = True,
            scale = 300,
            rotation_y = 200
        )

class Uydular(Button):
    def __init__(self, position=Vec3(0)):
        super().__init__(
            parent = scene,
            model = "uydu2.glb",
            collider = "box",
            position = position,
            color=color.white,
            scale = 33,
            rotation_y = randint(0,360)
        )

    def update(self):
        if round(distance(player, self)) < 100:
            self.on_click = Func(player.animate_position, self.position + Vec3(0, 5, 0), duration = 1, curve = curve.in_circ)
 
    def on_mouse_enter(self):
        print_on_screen(round(distance(player, self)), scale = 2)

app = Ursina(borderless=False)
sky = CustomSky()

ground = Entity(parent=scene, model ="plane",scale=300,y=-20,texture = "zemin",
                texture_scale=(50,50), collider="box",color = color.rgb(82,44,22))


Astronaut1 = Entity(model="Astronaut.glb",y=-20,z=40,x=-10,scale = 2)
Astronaut2 = Entity(model="Astronaut_main.glb",y=-6.5,z=70,x=0,scale = 45)
Astronaut3 = Entity(model="Astronaut.glb",y=-20,z=40,x=15,scale = 3)
Astronaut1.rotation_y = 345
Astronaut2.rotation_y = 354
Astronaut3.rotation_y = 20

Yapı1 = Entity(model="yapı.glb",y=-9,z=-50,x=-20,scale = 45)
Yapı1.rotation_y = 140


robot1 = Entity(model="robot1.glb",y=-17,z=-20,x=-10,scale = 10)
robot1.rotation_y =200

robot2 = Entity(model="robot1.glb",y=-17,z=-20,x=-1,scale = 10)
robot2.rotation_y =190

robot3 = Entity(model="robot1.glb",y=-17,z=-20,x=-5.5,scale = 10)
robot3.rotation_y =195

u1 = Uydular(position = (-10,20,-20))
u2 = Uydular(position = (-30,25,50))
u3 = Uydular(position = (50,35,10))
u4 = Uydular(position = (50,35,70))
u5 = Uydular(position = (-10,20,-100))
u6 = Uydular(position = (0,80,70))

player = FirstPersonController()

app.run()
