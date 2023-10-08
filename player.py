import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.slime_idle = pygame.transform.rotozoom(pygame.image.load('Assets/slime1.png').convert_alpha(), 0, 2.5)
        self.slime_eat = pygame.transform.rotozoom(pygame.image.load('Assets/slime2.png').convert_alpha(), 0, 2.5)
        self.image = self.slime_idle
        self.rect = self.image.get_rect(topleft=(45, 400))
        self.collision_rect = pygame.Rect(105, 500, 200, 110)
        self.screen = pygame.display.get_surface()

        # status of player
        self.alive = True
        self.eating = False
        self.lives = 3
        self.points = 0

        # hit cooldown
        self.hit_cooldown = False
        self.hit_timer = 0

    def get_input(self):
        # taking input from the user
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_SPACE]:
            self.image = self.slime_eat
            self.eating = True
        else:
            self.image = self.slime_idle
            self.eating = False

    def player_hit_cooldown(self):
        if self.hit_cooldown == True:
            # Deduct one life at the start of the cooldown since the player has been hit
            if self.hit_timer == 0:
                self.lives -= 1

                # If player has 0 lives, discombobulate them
                if self.lives <= 0:
                    self.alive = False

            self.hit_timer += 1
            if self.hit_timer == 5:
                self.hit_cooldown = False
                self.hit_timer = 0

    def draw(self):
        self.screen.blit(self.image, (45, 400))

    def update(self):
        self.get_input()
        self.player_hit_cooldown()
        self.draw()

