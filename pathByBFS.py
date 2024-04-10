import pygame
import numpy as np
from collections import deque
import time

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

# Define directions for movement (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to perform BFS
def bfs(matrix, start, end):
    queue = deque([start])
    visited = set([start])
    prev = {}
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            # Reconstruct the path
            path = []
            while current != start:
                path.append(current)
                current = prev[current]
            path.append(start)
            return path[::-1]
        
        for direction in directions:
            next_row = current[0] + direction[0]
            next_col = current[1] + direction[1]
            next_pos = (next_row, next_col)
            
            if 0 <= next_row < matrix.shape[0] and 0 <= next_col < matrix.shape[1] and matrix[next_row][next_col] == 0 and next_pos not in visited:
                queue.append(next_pos)
                visited.add(next_pos)
                prev[next_pos] = current
    
    return None

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Perform BFS to find the path
    path = bfs(matrix, tuple(image_pos), (matrix.shape[0] - 1, matrix.shape[1] - 1))
    
    if path:
        # Move the image along the path
        for next_pos in path[1:]:
            # Check if the next position is not visited
            if matrix[next_pos[0]][next_pos[1]] == 0:
                # Change color of visited tile
                matrix[image_pos[0]][image_pos[1]] = 2
                # Move the image
                image_pos = list(next_pos)
                # Clear the screen
                screen.fill(WHITE)
                # Draw the matrix
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        if matrix[i][j] == 0:
                            color = LIGHT_GREEN
                        elif matrix[i][j] == 1:
                            color = DARK_GREEN
                        else:
                            color = WHITE
                        pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                # Draw the image at its current position
                screen.blit(image, (image_pos[1] * TILE_SIZE, image_pos[0] * TILE_SIZE))
                # Update the display
                pygame.display.flip()
                # Pause for .2 seconds
                time.sleep(0.2)
            else:
                print("Can't move on visited tile")
                break
    else:
        print("Can't reach the bottom right block")
        break

    # Check if image reaches the destination
    if tuple(image_pos) == (matrix.shape[0] - 1, matrix.shape[1] - 1):
        print("Reached the bottom right block")
        running = False

# Quit Pygame
pygame.quit()
