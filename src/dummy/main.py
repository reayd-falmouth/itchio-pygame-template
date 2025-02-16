import asyncio
import pygame

# Initialize Pygame
pygame.init()

# Load the image
image_path = "cover.png"
image = pygame.image.load(image_path)

# Set display mode to match image size
screen = pygame.display.set_mode(image.get_size())

clock = pygame.time.Clock()


async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the image
        screen.blit(image, (0, 0))
        pygame.display.update()

        await asyncio.sleep(0)  # Required for asyncio compatibility
        clock.tick(60)

    pygame.quit()


asyncio.run(main())
