import pygame
from food import Burger
from food import Chips
from food import Rotten
from player import Player
import random
from pygame import mixer

pygame.init()

screen_width = 1500
screen_height = 1000

display_surface = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


class MainGame:
    def __init__(self):
        # loading bg and sprites
        self.bg_diner = pygame.transform.rotozoom(pygame.image.load('Assets/bg_diner.png').convert_alpha(), 0, 0.44)
        self.burger = pygame.transform.rotozoom(pygame.image.load('Assets/burger.png').convert_alpha(), 0, 1.7)
        self.reciept = pygame.transform.rotozoom(pygame.image.load('Assets/reciept.png').convert_alpha(), 0, 2.25)

        # printing text to screen
        self.text_font = pygame.font.Font("pixel.ttf", 45)
        self.text_font1 = pygame.font.Font("pixel.ttf", 150)

        self.slime = Player()
        self.food_group = pygame.sprite.Group()

        self.paused = False

        self.foods = ['chips', 'borgar', 'rotten']

        food_amount = 8
        for amount in range(0, food_amount):
            self.create_new_food()

        # sounds
        pygame.mixer.pre_init(44100, -16, 2, 512)  # configurations for sounds
        mixer.init()
        # IDK if I can use this music but credits to Nintendo for the soundtrack
        self.game_fx = pygame.mixer.Sound('kirby butter building.mp3')
        self.game_fx.set_volume(0.3)
        self.game_fx.play()

        self.run_game()

    # function created with help from Coding With Russ on YouTube
    def draw_text(self,text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        display_surface.blit(img, (x, y))

    def create_new_food(self):
        # printing food off-screen at random x positions so the food don't spawn uniformly
        x_pos = random.randint(1500, 2000)
        food_being_used = self.foods[random.randint(0, 2)]
        if food_being_used == 'borgar':
            food_obj = Burger(x_pos, 450)
        elif food_being_used == 'chips':
            food_obj = Chips(x_pos, 450)
        elif food_being_used == 'rotten':
            food_obj = Rotten(x_pos, 450)

        self.food_group.add(food_obj)

    def run_game(self):
        running = True
        while running:

            display_surface.blit(self.bg_diner, (0, 0))
            self.draw_text(f"Lives: {self.slime.lives}", self.text_font, (0, 0, 0), 300, 70)
            self.draw_text(f"Points: {self.slime.points}", self.text_font, (0, 0, 0), 300, 150)
            display_surface.blit(self.reciept, (0, 10))

            # Updating
            self.slime.update()

            # burger collisions and functionality
            for sprite in self.food_group:
                sprite.update(self.slime.collision_rect, self.slime.eating)
                if sprite.colliding == True:
                    if sprite.deduct_life == True:
                        self.slime.hit_cooldown = True
                    else:
                        self.slime.points += 1

                    sprite.kill()
                    self.create_new_food()

            if self.slime.alive == False:
                self.draw_text("Game Over", self.text_font1, (0, 0, 0), 540, 430)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            time_delta = clock.tick(60)

            pygame.display.update()


game = MainGame()



