import pygame

WHITE = (255, 255, 255)
BLUE = (45, 128, 255)

pygame.init()
screen = pygame.display.set_mode((300, 500))
running = True

music_playing = True
current = 0
music = ['imase - Night Dancer.mp3', 'NewJeans - OMG.mp3', 'Eve - Raison Detre.mp3']
pygame.mixer.music.load(music[current])
pygame.mixer.music.play()

def next_song() :
	global current
	if current == len(music) - 1 :
		current = 0
		pygame.mixer.music.load(music[current])
		pygame.mixer.music.play()
	elif current < len(music) :
		current += 1
		pygame.mixer.music.load(music[current])
		pygame.mixer.music.play()
	
def previous_song() :
	global current
	if current == 0 :
		current = len(music) - 1
		pygame.mixer.music.load(music[current])
		pygame.mixer.music.play()
	else :
		current -= 1
		pygame.mixer.music.load(music[current])
		pygame.mixer.music.play()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont("opensans", 30)
play_button = pygame.image.load('pause.jpeg')

def button(image, x, y) :
	rect = image.get_rect()
	rect.topleft = (95, 350)
	pos = pygame.mouse.get_pos()

	screen.blit(image, (95, 350))
	if rect.collidepoint(pos) :
		return True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if music_playing == True :
					pygame.mixer.music.pause()
					music_playing = False
					play_button = pygame.image.load('play.jpeg')
				else :
					pygame.mixer.music.unpause()
					music_playing = True
					play_button = pygame.image.load('pause.jpeg')

			if event.key == pygame.K_RIGHT :
				next_song()
			if event.key == pygame.K_LEFT :
				previous_song()
			if event.key == pygame.K_r :
				pygame.mixer.music.rewind()

		if event.type == SONG_END:
			next_song()
		
		if event.type == pygame.MOUSEBUTTONDOWN and play :
			if music_playing == True :
				pygame.mixer.music.pause()
				music_playing = False
				play_button = pygame.image.load('pause.jpeg')
			else :
				pygame.mixer.music.unpause()
				music_playing = True
				play_button = pygame.image.load('play.jpeg')
			
	

	

	image = pygame.image.load('bg1.jpeg')
	screen.blit(image, (0, 0))
	play = button(play_button, (screen.get_width() - play_button.get_width()) / 2, screen.get_height() - 65)
	song_name = music[current].capitalize()
	text = font.render(song_name, True, WHITE)
	screen.blit(text, ((screen.get_width() - text.get_width()) / 2, 50))

	pygame.display.flip()

	clock.tick(FPS)