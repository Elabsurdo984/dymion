Dymion Physics Course
=====================

Welcome to the official Dymion learning path. This course will teach you physics 
concepts by simulating them with code.

Lesson 1: The World of Vectors
------------------------------

In physics, most things aren't just numbers; they have a direction. These are **Vectors**.
A vector in Dymion has three components: :math:`x`, :math:`y`, and :math:`z`.

To create a position or a force in Dymion:

.. code-block:: python

   from dymion import Vector
   
   # A position 10 meters to the right and 5 meters up
   pos = Vector(10, 5, 0)
   
   # The magnitude is the "length" of the vector
   print(pos.magnitude) 

Lesson 2: Moving Objects (Kinematics)
-------------------------------------

Kinematics is the study of motion without considering its causes. 
The most important object is the **Particle**. It has position, velocity, and acceleration.

.. code-block:: python

   from dymion import Particle, Vector

   # A ball moving at 20 m/s upwards
   ball = Particle(velocity=Vector(0, 20, 0))
   
   # Update moves the particle based on its velocity
   ball.update(dt=1.0)
   print(f"New position: {ball.position}")

Lesson 3: Forces and Mass (Dynamics)
------------------------------------

Dynamics explains *why* things move. We use the **Body** class because it has **mass**.
According to Newton's Second Law:

.. math::

   \vec{F} = m \cdot \vec{a}

In Dymion, you apply forces to a body, and it calculates the acceleration automatically.

.. code-block:: python

   from dymion import Body, Vector
   from dymion.dynamics import gravity

   crate = Body(mass=50) # A 50kg crate
   crate.apply_force(gravity(crate)) # Earth's gravity
   
   crate.update(dt=0.1)
   print(f"Calculated Acceleration: {crate.acceleration}")

Next Lessons
------------

* **Energy:** Understanding Work, Power, and the conservation of energy.
* **Momentum:** What happens when two bodies collide?
* **Orbits:** How planets stay in the sky.
