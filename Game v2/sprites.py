    # Sprite classes

# Imports
import pygame as pg
from settings import *

vec = pg.math.Vector2

# Classes

class Player2(pg.sprite.Sprite):

	def __init__(self, game, w, h):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.image.load("head2.png")
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.height /2)
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = vec(600, HEIGHT / 2)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def jump(self):
		self.rect.y += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.y -= 1
		if hits:
			self.vel.y = -PLAYER_JUMP

	def update(self):
		self.acc = vec(0, GRAVITY)

		keys = pg.key.get_pressed()

		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC

		self.acc.x += self.vel.x * PLAYER_FRICTION
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		if self.pos.x < 0:
			self.pos.x = 0

		if self.pos.x > WIDTH:
			self.pos.x = WIDTH

		self.rect.midbottom = self.pos
class Player(pg.sprite.Sprite):

	def __init__(self, game, w, h):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.image.load("head1.png")
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.height /2)
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = vec(200, HEIGHT / 2)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def jump(self):
		self.rect.y += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.y -= 1
		if hits:
			self.vel.y = -PLAYER_JUMP

	def update(self):
		self.acc = vec(0, GRAVITY)

		keys = pg.key.get_pressed()

		if keys[pg.K_d]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_a]:
			self.acc.x = -PLAYER_ACC

		self.acc.x += self.vel.x * PLAYER_FRICTION
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		if self.pos.x < 0:
			self.pos.x = 0

		if self.pos.x > WIDTH:
			self.pos.x = WIDTH

		self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):

	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w, h))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Goal1(pg.sprite.Sprite):
  
  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
    pg.sprite.Sprite.__init__(self)
    self.vx = vel_x
    self.vy = vel_y
    self.image = pg.image.load(arquivo_imagem)
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y

class Background(pg.sprite.Sprite):
  
  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
    pg.sprite.Sprite.__init__(self)
    self.vx = vel_x
    self.vy = vel_y
    self.image = pg.image.load(arquivo_imagem)
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y
class Scoreboard(pg.sprite.Sprite):
  
  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
    pg.sprite.Sprite.__init__(self)
    self.vx = vel_x
    self.vy = vel_y
    self.image = pg.image.load(arquivo_imagem)
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y    

class Square(pg.sprite.Sprite): 

	def __init__(self, game, w, h):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.image.load("ball.png")
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.height /2)
		self.pos = vec(400, (HEIGHT-40))
		self.vel = vec(SQUARE_INICIAL, 0)
        
	def update(self):
#
		self.acc = vec(0, GRAVITY)		
		if self.pos.x < 0:
			self.vel.x = -self.vel.x + 0.1

		if self.pos.x > WIDTH:
			self.vel.x = -self.vel.x - 0.1
		self.acc.x += self.vel.x * PLAYER_FRICTION
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc
		self.pos.x += self.vel.x

		self.rect.midbottom = self.pos
	
	def jump(self):
		self.rect.y += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.y -= 1
		if hits:
			self.vel.y = -SQUARE_JUMP

class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()

class Menu(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        
class Pause(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
                
