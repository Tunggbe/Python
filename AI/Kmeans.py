import pygame
import math
from random import randint
from sklearn.cluster import KMeans

def draw_point(x,y,color):
	pygame.draw.circle(screen, BLACK, (x,y), 6)
	pygame.draw.circle(screen, color, (x,y), 4)

def random_cluster(k):
	for i in range(k):
		random_point = [randint(50,700),randint(50,495)]
		clusters.append(random_point)

def draw_cluster(x,y,i):
	pygame.draw.circle(screen, colors[i], (x,y), 8)

def distance(point, cluster):
	return ((cluster[0]-point[0])**2+(cluster[1]-point[1])**2)**1/2

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("Kmeans visualization")

running = True

clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (255, 165, 0), (0, 191, 255), (255, 255, 0), (128, 0, 128), (75, 0, 130)]
font = pygame.font.SysFont('sans', 40)
small_font = pygame.font.SysFont('sans', 15)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render('run', True, WHITE)
text_random = font.render('Random', True, WHITE)
text_algorithm = font.render('Algorithm', True, WHITE)
text_reset = font.render('Reset', True, WHITE)

k = 0
error = 0
points = []
clusters = []
labels = []

while running:
	clock.tick(60)
	screen.fill(BACKGROUND)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# Draw interface

	# Draw panel
	pygame.draw.rect(screen, BLACK, (50,50,700,500))
	pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))

	# Draw K button +
	pygame.draw.rect(screen, BLACK, (850,50,50,50))
	screen.blit(text_plus,(865,50))

	# Draw K button -
	pygame.draw.rect(screen, BLACK, (950,50,50,50))
	screen.blit(text_minus,(970,50))
	
	# Draw "K=" button
	text_k = font.render('K = ' + str(k), True, BLACK)
	screen.blit(text_k,(1050,50))
	
	# Draw "Run" Button
	pygame.draw.rect(screen,BLACK, (850,150,150,50))
	screen.blit(text_run,(900,150))

	# Draw "Random" Button
	pygame.draw.rect(screen,BLACK, (850,250,150,50))
	screen.blit(text_random,(860,250))

	
	
	# Draw "Algorithm" button
	pygame.draw.rect(screen,BLACK, (850,450,150,50))
	screen.blit(text_algorithm,(855,450))

	# Draw "reset" button
	pygame.draw.rect(screen,BLACK, (850,550,150,50))
	screen.blit(text_reset,(870,550))

	# End draw interface
	
	if 50 < mouse_x < 750 and 50 < mouse_y < 550:
		text_mouse = small_font.render("(" + str(mouse_x-55) + "," + str(mouse_y-55) + ")", True, BLACK)
		screen.blit(text_mouse,(mouse_x+10,mouse_y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			if 850 < mouse_x < 900 and 50 < mouse_y < 100:#+
				if k < len(colors):
					k += 1

			
			if 950 < mouse_x < 1000 and 50 < mouse_y < 100:#-
				if k > 0:
					k -= 1
			
			if 850 < mouse_x < 1000 and 150 < mouse_y < 200:#run
				error = []
				labels = []
				new_clusters = []
				for i in range(len(points)):
					distance_to_cluster = []
					for j in range(len(clusters)):
						dis = distance(points[i], clusters[j])
						distance_to_cluster.append(dis)
					min_distance = min(distance_to_cluster)
					label = distance_to_cluster.index(min_distance)
					labels.append(label)
				for i in range(k):
					sum_cluster_x = 0
					sum_cluster_y = 0
					denominator = 0
					for j in range(len(points)):
						if labels[j] == i:
							sum_cluster_x += points[j][0]
							sum_cluster_y += points[j][1]
							denominator += 1
					if denominator != 0:
						average_cluster_x = sum_cluster_x/denominator
						average_cluster_y = sum_cluster_y/denominator
						new_cluster = (int(average_cluster_x),int(average_cluster_y))
						clusters[i] = new_cluster
			
			if 850 < mouse_x < 1000 and 250 < mouse_y < 300:#random
				clusters = []
				labels = []
				random_cluster(k)
			
			if 850 < mouse_x < 1000 and 450 < mouse_y < 500:#algorithm
				kmeans = KMeans(n_clusters = k).fit(points)
				clusters = kmeans.cluster_centers_
				labels = kmeans.labels_
		
			
			if 850 < mouse_x < 1000 and 550 < mouse_y < 600:#reset
				k = 0
				points = []
				clusters = []
				labels = []

			if 55 < mouse_x < 745 and 55 < mouse_y < 545:
				labels = []
				point = (mouse_x-50, mouse_y-50)
				points.append(point)
			
	

	error = 0
	if clusters != [] and labels != []:
		for i in range(len(points)):
			error += distance(points[i],clusters[labels[i]])
	
	# Draw point
	for i in range(len(points)):
		if labels == []:
			draw_point(points[i][0]+50,points[i][1]+50,WHITE)
		else:
			draw_point(points[i][0]+50,points[i][1]+50,colors[labels[i]])
			
	# Draw cluster
	for i in range(len(clusters)):
		draw_cluster(clusters[i][0]+50,clusters[i][1]+50,i)

	# Draw "Error" Text
	text_error = font.render('Error = ' + str(int(error)), True, BLACK)
	screen.blit(text_error,(850, 350))
	
	pygame.display.flip()

pygame.quit()