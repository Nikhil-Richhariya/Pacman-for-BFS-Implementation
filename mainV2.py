import pygame
import numpy as np

# Define colors
LIGHT_GREEN = (152, 251, 152)  # Light green
DARK_GREEN = (34, 139, 34)      # Dark green
WHITE = (255, 255, 255)         # White

# Initialize Pygame
pygame.init()

# Set dimensions for the window and tiles
WINDOW_SIZE = (500, 500)
TILE_SIZE = 10

# Create Pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Matrix Display")

# Load the image
image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

# Create matrix
matrix = np.zeros((50, 50), dtype=int)

# Total number of elements in the matrix
total_elements = matrix.size

# Calculate the number of 1's needed (approximately 30%)
num_ones = int(0.3 * total_elements)

# Generate random indices for the 1's
indices = np.random.choice(total_elements, num_ones, replace=False)

# Convert indices to row and column indices
row_indices, col_indices = np.unravel_index(indices, matrix.shape)

# Assign 1's to the random positions
matrix[row_indices, col_indices] = 1

matrix[0][0] = 0
matrix[1][1] = 0

# Initial position of the image
image_pos = [0, 0]

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the image based on arrow keys
            if event.key == pygame.K_UP and image_pos[0] > 0 and matrix[image_pos[0] - 1][image_pos[1]] == 0:
                image_pos[0] -= 1
            elif event.key == pygame.K_DOWN and image_pos[0] < matrix.shape[0] - 1 and matrix[image_pos[0] + 1][image_pos[1]] == 0:
                image_pos[0] += 1
            elif event.key == pygame.K_LEFT and image_pos[1] > 0 and matrix[image_pos[0]][image_pos[1] - 1] == 0:
                image_pos[1] -= 1
            elif event.key == pygame.K_RIGHT and image_pos[1] < matrix.shape[1] - 1 and matrix[image_pos[0]][image_pos[1] + 1] == 0:
                image_pos[1] += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            color = DARK_GREEN if matrix[i][j] == 1 else LIGHT_GREEN
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw the image at its current position
    screen.blit(image, (image_pos[1] * TILE_SIZE, image_pos[0] * TILE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
