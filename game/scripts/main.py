import pygame
import sys

class Game():
    def __init__(self) -> None:
        pygame.init()
        
        self.window_width = 800
        self.window_height = 800
        self.caption = "Chess by Sam Chandler"
        self.display_surface = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.caption)
        self.fps_clock = pygame.time.Clock()
        self.FPS = 60
        
        self.board_image = pygame.image.load("python-chess\\game\\assets\\boards\\board.png")
        board_size_needed = (self.window_width, self.window_height)
        self.board_image = pygame.transform.scale(self.board_image, board_size_needed)
        
        # self.letters_image = pygame.image.load("python-chess\\game\\assets\\text\\letters.png")
        # letters_size_needed = (483, 30)
        # self.letters_image = pygame.transform.scale(self.letters_image, letters_size_needed)
        
        # self.numbers_image = pygame.image.load("python-chess\\game\\assets\\text\\numbers.png")
        # numbers_size_needed = (30, 483)
        # self.numbers_image = pygame.transform.scale(self.numbers_image, numbers_size_needed)
        
        self.square_size = self.window_width / 8
        self.board = []
        for _ in range(8):
            self.board.append(["" for _ in range(8)])
        print(self.board)
        
        self.running = True
        
        self.execute()
        
    def execute(self) -> None:
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            
            self.render()
            self.fps_clock.tick(self.FPS)
        
        
    def render(self) -> None:
        self.display_surface.blit(self.board_image, (0, 0))
        # self.display_surface.blit(self.letters_image, (120, 750))
        # self.display_surface.blit(self.numbers_image, (0, 0))
        
        pygame.display.update()
        
        
    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.quit()
        
    def quit(self) -> None:
        pygame.quit()
        sys.exit(0)
        
class Piece(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        
class King(Piece):
    def __init__(self, colour) -> None:
        if self.colour == "w":
            
        
        
if __name__ == "__main__":
    game = Game()