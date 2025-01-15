# introduction
This program is a visualization of how a satellite moves in Earth's orbit with preset values of altitude, speed, and initial position. In my work, I have used the following Python libraries, such as numpu, matplotlib, and scipy. 

Let's talk in more detail about the output results. The first graph shows the change in speed and altitude of the satellite over time. 
![image](https://github.com/user-attachments/assets/f654bd5f-5b78-4591-826b-17b43d5c7762)
The graph shows that the speed increases with decreasing altitude. This is because the satellite is closer to the center of the Earth.

The initial position of a satellite is defined as the sum of the Earth's radius and the altitude at which it is located. You can "play around" with this and see how, with increasing speed, the satellite leaves the earth's gravity zone and flies into space.
It shows that the height becomes negative at some point in time. This can be explained by the fact that from the point of view of the mathematical function, the task is performed correctly, but from the side of physics, of course, this is impossible. 

The second graph shows the trajectory of the satellite, but not only in orbit, but also at an altitude less than the radius of the Earth.
![image](https://github.com/user-attachments/assets/2ccac1dd-8966-4954-ba17-8a3a85e8dea9)
This graph shows the trajectory of the satellite itself and how much the number and frequency of orbits increases.
# conclusion
In conclusion, I would like to conclude that such a situation is impossible, since when the satellite reaches zero altitude (falling to the Ground), its further movement is impossible. This program shows its behavior under the condition that the density of the Earth and air would be the same. 
This can be used to consider the situation with other planets, you just need to set their gravitational constant G, mass M, radius of the planets, and more.


