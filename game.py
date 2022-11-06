import pygame
import numpy as np
from math import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
# colours

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# cube informatino

scale = 100
angle = 0

circle_pos = [WIDTH/2, HEIGHT/2]

points = []

points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_matrix = np.matrix([
	[1, 0, 0],
	[0, 1, 0],
])

projected_points = [
	[n, n] for n in range(len(points))
]

def connect_points(i, j, points):
	pygame.draw.line(screen, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))



clock = pygame.time.Clock()

runWin = True
while runWin:
	pygame.display.set_caption(str(clock.get_fps()))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runWin = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				scale += 5
			elif event.key == pygame.K_RIGHT:
				if scale > 50:
					scale -= 5

	rotation_z = np.matrix([
		 		[cos(angle), -sin(angle), 0],
		 		[sin(angle), cos(angle), 0],
		 		[0, 0, 1],
		 	])

	rotation_y = np.matrix([
		 		[cos(angle), 0, sin(angle)],
		 		[0, 1, 0],
		 		[-sin(angle), 0, cos(angle)],
		 	])

	rotation_x = np.matrix([
		 		[1, 0, 0],
		 		[0, cos(angle), -sin(angle)],
		 		[0, sin(angle), cos(angle)],
		 	])

	angle += 0.01

	screen.fill((0, 0, 0))

	# draw area

	i = 0
	for point in points:
		rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
		rotated2d = np.dot(rotation_y, rotated2d)

		projected2d = np.dot(projection_matrix, rotated2d)

		x = int(projected2d[0][0] * scale) + circle_pos[0]
		y = int(projected2d[1][0] * scale) + circle_pos[1]

		projected_points[i] = [x, y]
		pygame.draw.circle(screen, BLUE, (x, y), 5)
		i += 1

	for p in range(4):
		connect_points(p, (p+1) % 4, projected_points)
		connect_points(p+4, ((p+1) % 4)+4, projected_points)
		connect_points(p, (p+4), projected_points)

	pygame.display.flip()
	clock.tick(60)
	