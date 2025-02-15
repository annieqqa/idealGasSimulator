# idealGasSimulator
 Simulate, visualize and prove the ideal gas equations
 
## Particle system attributes (parSys)
1. N: number of particles in the container
2. T: average KE
3. dt: time step
4. dx, dy, dz: space step

## Particle attributes (particle)
1. xCoord, yCoord, zCoord: x-,y-,z-coordinates; randomly assigned during initialization
2. v: initial speed, magnitude of the direction vector in space when combined with the normalised unit vector based on i, j, k
3. r: radius of each particle during visualisation
4. i, j, k: i-, j-, k- components of the direction vector of the particles, randomly assigned based on v

## Particle methods
1. propagate: update the position vector based on the speed
2. collide: corresponding i-/j-/k-component changes sign

## Container Attributes (container)
Rectangular prism is used, but the container could also be any other shape e.g. cylindrical (TODO)
1. h: height of the prism (direction: upwards)
2. w: width of the prism (direction: out of screen)
3. l: length of the prism (direction: right)

## Visualization attributes (camera)
1. xCoord, yCoord, zCoord
2. i, j, k: i-,j-,k-components of the direction vector of the camera, corresponding to the x-,y-,z-directions
3. frameW: width of the window
4. frameH: height of the window

## Visualisation methods
1. zoom in/out (TODO)
2. rendContainer: render coordinates of container, which stays constant for now
3. rendParticles: render coordinates of particle, which is changing

## Experimental details (dataProcess)
1. plot graph