import pygame


class Engine():
	def __init__(self, size, title="Game", fc=(0,0,0)):
		self.size = size
		self.fc = fc
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption(title)

	def update(self):
		pass

	def run(self, fps):
		run = True
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			self.screen.fill(self.fc)
			self.update()
			pygame.display.update()
			pygame.time.Clock().tick(fps)