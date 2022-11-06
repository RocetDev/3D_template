from math import sin, cos, tan
import numpy as np


def rotate_x(angle):
	rotate_x = np.array([
			[1, 0 ,0, 0],
			[0, cos(angle), -sin(angle), 0],
			[0, sin(angle), cos(angle), 0],
			[0, 0, 0, 1],
		])
	return rotate_x


def rotate_y(angle):
	rotate_y = np.array([
			[cos(angle), 0, sin(angle), 0],
			[0, 1, 0, 0],
			[-sin(angle), 0, cos(angle), 0],
			[0, 0, 0, 1],
		])
	return rotate_y


def rotate_y(angle):
	rotate_z = np.array([
			[cos(angle), -sin(angle), 0, 0],
			[sin(angle), cos(angle), 0, 0],
			[0, 0, 1, 0],
			[0, 0, 0, 1],
		])
	return rotate_z


def transform(scale, move):
	a, b, c = scale
	i, j, k = move
	transform_matrix = np.array([
			[a, 0, 0, i],
			[0, b, 0, j],
			[0, 0, c, k],
			[0, 0, 0, 1],
		])
	return transform_matrix


def transform_scale(a, b, c):
	trans_scale = np.array([
			[a, 0, 0, 0],
			[0, b, 0, 0],
			[0, 0, c, 0],
			[0, 0, 0, 1],
		])
	return trans_scale


def transform_move(a, b, c):
	move = np.array([
			[1, 0, 0, a],
			[0, 1, 0, b],
			[0, 0, 1, c],
			[0, 0, 0, 1],
		])
	return move