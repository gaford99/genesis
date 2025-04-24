import threading

import numpy as np

import genesis as gs

def run_sim(scene):
    for _ in range(200):
        scene.step(refresh_visualizer=False)


def main():
    ########################## init ##########################
    gs.init(backend=gs.cpu)

    ########################## create a scene ##########################

    scene = gs.Scene(
        sim_options=gs.options.SimOptions(),
        show_viewer=True,
        viewer_options=gs.options.ViewerOptions(
            camera_pos=(3.5, 0.0, 2.5),
            camera_lookat=(0.0, 0.0, 0.5),
            camera_fov=40,
        ),
        vis_options = gs.options.VisOptions(
            show_world_frame = True, # visualize the coordinate frame of `world` at its origin
            world_frame_size = 1.0, # length of the world frame in meter
            show_link_frame  = False, # do not visualize coordinate frames of entity links
            show_cameras     = False, # do not visualize mesh and frustum of the cameras added
            plane_reflection = True, # turn on plane reflection
            ambient_light    = (0.1, 0.1, 0.1), # ambient light setting
    ),
        show_FPS=True,
        rigid_options=gs.options.RigidOptions(
            dt=0.01,
            gravity=(0.0, 0.0, -10.0),
        ),
        renderer = gs.renderers.RayTracer(), # using rasterizer for camera rendering
    )
    

    ########################## entities ##########################
    plane = scene.add_entity(gs.morphs.Plane())
    r0 = scene.add_entity(
        gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml"),
    )

    ########################## build ##########################
    scene.build()

    threading.Thread(target=run_sim, args=(scene)).start()
    scene.viewer.run()


if __name__ == "__main__":
    main()