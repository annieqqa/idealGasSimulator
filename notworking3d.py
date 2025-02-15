import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
class parSys():
    def __init__(self, N=1, T=298, dt=0.01, l=2, w=2, h=2):
        self.N = N # number of particles
        self.T = T # temperature
        self.dt = dt # time step
        self.l = l # length of the box
        self.w = w # width of the box
        self.h = h # height of the box
        self.particles = []
    def initialize_particles(self):
        # initialize particles randomly
        for i in range(self.N):
            p = particle()
            p.x = random.uniform(0, self.l)
            p.y = random.uniform(0, self.w)
            p.z = random.uniform(0, self.h)
            p.i = random.uniform(0,1)
            p.j = random.uniform(0,1)
            p.k = random.uniform(0,1)
            self.particles.append(p)
    def update_particles(self):
        # update particles
        for i in range(self.N):
            p = self.particles[i]
            p.x = p.x + p.i*self.dt
            p.y = p.y + p.j*self.dt
            p.z = p.z + p.k*self.dt
            if p.x > self.l or p.x < 0:
                p.i = -p.i
            if p.y > self.w or p.y < 0:
                p.j = -p.j
            if p.z > self.h or p.z < 0:
                p.k = -p.k
    def get_particles(self):
        x = np.empty(self.N)
        y = np.empty(self.N)
        z = np.empty(self.N)
        for i in range(self.N):
            p = self.particles[i]
            np.append(x, p.x)
            np.append(y, p.y)
            np.append(z, p.z)
        return x, y, z
        

class particle():
    def __init__(self, x=0, y=0, z=0, i=0, j=0, k=0):
        self.x = x
        self.y = y
        self.z = z
        self.i = i
        self.j = j
        self.k = k

def run(data):
    ax.clear()              # 清空圖表
    ax.set(xlim3d=(0, 2), xlabel='X')
    ax.set(ylim3d=(0, 2), ylabel='Y')
    ax.set(zlim3d=(0, 2), zlabel='Z')
    ps.update_particles()
    x, y, z = ps.get_particles()
    # print (x, y, z)
    ax.scatter(x, y, z)


if __name__ == '__main__':
    ps = parSys()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set(xlim3d=(0, 2), xlabel='X')
    ax.set(ylim3d=(0, 2), ylabel='Y')
    ax.set(zlim3d=(0, 2), zlabel='Z')

    ps.initialize_particles()
    num_step = 100
    ani = animation.FuncAnimation(fig, run, num_step, interval=10)
    plt.show()
    ani.save('animation.gif', fps=2)