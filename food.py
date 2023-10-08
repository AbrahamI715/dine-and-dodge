import pygame
import random
import math


class Food(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

        self.original_y = y

        self.speed = speed

        self.screen = pygame.display.get_surface()
        self.screen_width = self.screen.get_width()

        self.deduct_life = False
        self.colliding = False
        self.existence_timer = random.randint(1,20) * 0.1

    def collision(self, player_rect, is_eating):
        if self.rect.colliderect(player_rect):
            self.colliding = True
            if is_eating == False:
                self.deduct_life = True
            else:
                self.deduct_life = False

        else:
            self.colliding = False

    def move(self):
        self.existence_timer += 0.1
        self.rect.y += math.sin(self.existence_timer)
        self.rect.x -= self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, player_rect, is_eating):
        self.move()
        self.collision(player_rect, is_eating)
        self.draw()


class Burger(Food):
    def __init__(self, x, y):
        image = pygame.transform.rotozoom(pygame.image.load('Assets/burger.png').convert_alpha(), 0, 1.7)
        speed = random.randint(1, 5)
        super().__init__(image, x, y, speed)


class Chips(Food):
    def __init__(self, x, y):
        image = pygame.transform.rotozoom(pygame.image.load('Assets/chips.png').convert_alpha(), 0, 1.7)
        speed = random.randint(2, 5)
        super().__init__(image, x, y, speed)


class Rotten(Food):
    def __init__(self, x, y):
        image = pygame.transform.rotozoom(pygame.image.load('Assets/rotten_flesh.png').convert_alpha(), 0, 0.255)
        speed = random.randint(1, 4)
        super().__init__(image, x, y, speed)

    def collision(self, player_rect, is_eating):
        if self.rect.colliderect(player_rect):
            self.colliding = True
            if is_eating == False:
                self.deduct_life = False
            else:
                self.deduct_life = True

        else:
            self.colliding = False

