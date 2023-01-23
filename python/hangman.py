import pygame, sys
import random
sys.path.append("/Users/akashkesani/Desktop/projects/V8_game_engine")

from engine.play.entity import gamelooper,frameviewer
from engine.play.action import display,terminate,loop
from engine.actor.entity import circle
from engine.actor.action import draw_circle,put_position
from engine.physics.entity import particles, spring_force, gravity_force, rectangle_collider
from engine.physics.action import (position_solve, velocity_solve, euler_solve,
                                   pick_position, spring_force_action, gravity_force_action,
                                   inside_rectangle_collision, outside_rectangle_collision)

GM = gamelooper.GameLooper()
FV = frameviewer.FrameViewer((1280,720))


def create_elements ( number_of_elements ):
    
    init_data = []
    
    for i in range(0,number_of_elements):
        position_x = random.random()*2311313 % 1280
        position_y = random.random()*2311313 % 720
        red = random.random()*4232442 %255
        blue = random.random()*4232442 %255
        green = random.random()*4232442 %255
        circle_ = circle.Circle([position_x,position_y],[red,blue,green],10)
        circle_.name = "circle" + str(i)
        draw = draw_circle.DrawCircle()
        circle_.add_action(draw)
        init_data.append(circle_)
    
    return init_data

def move_elements (init_data):
    particles_ = particles.Particles()

    for i in range(0,len(init_data)):
        position_ = init_data[i].position
        velocity_ = [ float(random.randrange(-100,100,1)) / 100,
                           float(random.randrange(-100,100,1)) / 100]
        mass = 1.0
        particles_.add_particle(position_, velocity_, mass)

 
    PositionSolve_ = position_solve.PositionSolve()
    VelocitySolve_ = velocity_solve.VelocitySolve()
    EulerSolve_ = euler_solve.EulerSolve()

    SpringForce = spring_force.SpringForce()
    SpringForceAction = spring_force_action.SpringForceAction()
    SpringForce.add_action(SpringForceAction)
    VelocitySolve_.children.append(SpringForceAction)

    GravityForce = gravity_force.GravityForce()
    GravityForceAction = gravity_force_action.GravityForceAction()
    GravityForce.add_action(GravityForceAction)
    VelocitySolve_.children.append(GravityForceAction)

    RectangleCollider = rectangle_collider.RectangleCollider([0,0],[1280,720])
    Collision1 = inside_rectangle_collision.InsideRectangleCollision()
    RectangleCollider.add_action(Collision1)
    VelocitySolve_.children.append(Collision1)
    
    DividerRect1 = rectangle_collider.RectangleCollider([1000,0],[1050,250])
    Collision2 = outside_rectangle_collision.OutsideRectangleCollision()
    DividerRect1.add_action(Collision2)
    VelocitySolve_.children.append(Collision2)

    DividerRect2 = rectangle_collider.RectangleCollider([1000,325],[1050,720])
    Collision3 = outside_rectangle_collision.OutsideRectangleCollision()
    DividerRect2.add_action(Collision3)
    VelocitySolve_.children.append(Collision3)
    
    particles_.add_action(PositionSolve_)
    particles_.add_action(VelocitySolve_)
    particles_.add_action(EulerSolve_)

    EulerSolve_.children.append(VelocitySolve_)
    EulerSolve_.children.append(PositionSolve_)

    for i in range(0,len(init_data)-1):
        PickData = pick_position.PickPosition(i)
        PutData = put_position.PutPosition()
        particles_.add_action(PickData)
        init_data[i].add_action(PutData)
        PickData.children.append(PutData)
        EulerSolve_.children.append(PickData)
    
    return particles_

        


    
display = display.Display()
terminate = terminate.Terminate()

items = create_elements(20)
paricles_ = move_elements(items)

for i in items:
    display.children.append(i.actions[0])

display.children.append(paricles_.actions[2])

loop = loop.Loop()


FV.insert_action(display)
FV.insert_action(terminate)
GM.insert_action(loop)

GM.loopActions.append(display)
GM.eventActions.append(terminate)

loop.act()



