# Main Game

# Imports
import pygame as pg
import random
from settings import *
from sprites import *
from os import path

# Class Jogo
class Game:

	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH+int(PLAYER_WIDTH/2), HEIGHT))
		self.screen = pg.image.load("fundo2.png").convert
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.font_name = pg.font.match_font(FONT_NAME)
		self.running = True
		#self.score = 0
        
		#self.load_data()

	#def load_data(self):
	#	#load highscore
	#	self.dir = path.dirname(__file__)
	#	if path.isfile(path.join(self.dir, HS_FILE)):
	#		self.file_exist = "r+"
	#	else:
	#		self.file_exist = "w"

	#	with open(path.join(self.dir, HS_FILE), self.file_exist) as hs:
	#		try:
	#			self.highscore = int(hs.read())
	#		except:
	#			self.highscore = 0

	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		self.squares = pg.sprite.Group()
		floor = Platform(0, HEIGHT - 40, WIDTH+int(PLAYER_WIDTH/2), 40)
		self.all_sprites.add(floor)
		self.platforms.add(floor)
		self.square = Square(self, SQUARE_WIDTH, SQUARE_HEIGHT)
		self.squares.add(self.square)
		self.all_sprites.add(self.square)
		self.player = Player(self, PLAYER_WIDTH, PLAYER_HEIGHT)
		self.player2 = Player2(self, PLAYER_WIDTH, PLAYER_HEIGHT)  
		self.all_sprites.add(self.player)
		self.all_sprites.add(self.player2)  
		self.run()

	def run(self):
		self.playing = True

		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		self.all_sprites.update()
		if self.square.vel.y>0:
			hits4 = pg.sprite.spritecollide(self.square,self.platforms, False)
			if hits4:
				self.square.pos.y = hits4[0].rect.top + 1
				self.square.vel.y = 0
		if self.player.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player, self.platforms, False)
			if hits:
				self.player.pos.y = hits[0].rect.top + 1
				self.player.vel.y = 0
		hits = pg.sprite.spritecollide(self.player, self.squares, False)
		if self.player2.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player2, self.platforms, False)  
			if hits:
				self.player2.pos.y = hits[0].rect.top + 1
				self.player2.vel.y = 0
		hits2  = pg.sprite.spritecollide(self.player, self.squares, False)
		hits3  = pg.sprite.spritecollide(self.player2, self.squares, False)
		if self.player.pos.x == 40 or self.player.pos.x ==750: 
			self.square.vel.x = 0
		if hits3:        
			self.square.vel.x = -self.square.vel.x
			self.square.vel.x = -self.square.vel.x
		if hits2:
				if self.square.vel.x!=0:
				    self.square.vel.x = -self.square.vel.x
				else:
				    self.square.vel.x= self.player.vel.x
		if self.square.pos.x == 800 or self.square.pos.x ==0:
			self.square.vel.x = -self.square.vel.x
            #if self.score > self.highscore:
		#	self.highscore = self.score
		#	with open(path.join(self.dir, HS_FILE), "r+") as hs:
		#		hs.write(str(self.highscore))

	def events(self):
		for event in pg.event.get():

			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_UP:
					self.player.jump()
				if event.key == pg.K_w:
					self.player2.jump()
				if  pg.sprite.spritecollide(self.player, self.squares, False):
					self.square.jump()
					self.square.vel.x = 30
				if  pg.sprite.spritecollide(self.player2, self.squares, False):
					self.square.jump()
					self.square.vel.x = -30    
				if self.square.pos.x <100 and self.square.pos.y >400:
					self.ResetBall()
				if self.square.pos.x >500 and self.square.pos.y > 400:
					self.ResetBall()                    
             
	def draw(self):
		self.fundo = pg.image.load("fundo2.png").convert
		self.screen = self.fundo
		self.all_sprites.draw(self.screen) #mudei de screen p fundo
		#self.draw_text("Score: " + str(self.score), 24, BLACK, WIDTH / 2, HEIGHT / 4)
		#if self.score >= self.highscore and self.highscore != 0:
		#	self.draw_text("NEW HIGH SCORE! " + str(self.highscore), 24, BLACK, WIDTH / 2, (HEIGHT / 4) - 30)
		#else:
		#	self.draw_text("High Score: " + str(self.highscore), 24, BLACK, WIDTH / 2, (HEIGHT / 4) - 30)
	
		pg.display.flip()

	def show_start_screen(self):
		self.screen.fill(BGCOLOR)
		self.draw_text(TITLE, 48, RED, WIDTH / 2, HEIGHT / 4)
		self.draw_text("Press the arrows to move", 24, BLACK, WIDTH / 2, HEIGHT / 2)
		self.draw_text("Press a key to play", 24, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
		#self.draw_text("High Score: " + str(self.highscore), 24, BLACK, WIDTH / 2, 15)
		pg.display.flip()
		self.wait_for_key()

	def ResetBall(self):

		self.square.pos= vec(400, (HEIGHT-40))
		self.draw_text("GOAL!", 48, RED, WIDTH / 2, HEIGHT / 4)        
	def show_go_screen(self):
		if not self.running:
			return
		self.screen.fill(BGCOLOR)
		self.draw_text("GAME OVER", 48, RED, WIDTH / 2, HEIGHT / 4)
	#	self.draw_text("Score: " + str(self.score), 36, BLACK, WIDTH / 2, (HEIGHT / 2) + 30)
		self.draw_text("Press a key to play again", 24, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
	#	if self.score >= self.highscore and self.highscore != 0:
	#		self.draw_text("NEW HIGH SCORE! " + str(self.highscore), 24, BLACK, WIDTH / 2, (HEIGHT / 4) - 30)
	#	else:
	#		self.draw_text("High Score: " + str(self.highscore), 36, BLACK, WIDTH / 2, (HEIGHT / 2) - 30)
		pg.display.flip()
		self.wait_for_key()


	def wait_for_key(self):
		waiting = True
		while waiting:
			self.clock.tick(FPS)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					waiting = False
					self.running = False
				if event.type == pg.KEYUP:
					self.score = 0
					waiting = False

	def draw_text(self, text, size, color, x, y):
		font = pg.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		self.screen.blit(text_surface, text_rect)


# Jogo
g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pg.quit()






