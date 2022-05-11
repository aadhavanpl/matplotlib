import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        self.x_value = [0]
        self.y_value = [0]
    
    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3 ,4, 5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_value, rw.y_value, s=3)

    option = input("[y/n]: ")
    if option=='y':
        plt.show()
    else:
        break 