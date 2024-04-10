import pygame
import numpy as np
from collections import deque
import time

# Define colors
LIGHT_GREEN = (152, 251, 152)  # Light green
DARK_GREEN = (34, 139, 34)      # Dark green
WHITE = (255, 255, 255)         # White
BLUE = (0, 0, 255)              # Blue for path visualization
YELLOW = (255, 255, 0)          # Yellow for the final path

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
    found = False
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            found = True
            # Reconstruct the path
            path = []
            while current != start:
                path.append(current)
                current = prev[current]
            path.append(start)
            return path[::-1], found
        
        for direction in directions:
            next_row = current[0] + direction[0]
            next_col = current[1] + direction[1]
            next_pos = (next_row, next_col)
            
            if 0 <= next_row < matrix.shape[0] and 0 <= next_col < matrix.shape[1] and matrix[next_row][next_col] == 0 and next_pos not in visited:
                queue.append(next_pos)
                visited.add(next_pos)
                prev[next_pos] = current
                # Update visualization
                matrix[next_row][next_col] = 2
                update_display()
                time.sleep(0.52)
    
    return None, found

# Function to update display
def update_display():
    screen.fill(WHITE)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 0:
                color = LIGHT_GREEN
            elif matrix[i][j] == 1:
                color = DARK_GREEN
            elif matrix[i][j] == 2:
                color = WHITE
            elif matrix[i][j] == 3:
                color = YELLOW
            else:
                color = BLUE
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    screen.blit(image, (image_pos[1] * TILE_SIZE, image_pos[0] * TILE_SIZE))
    pygame.display.flip()

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Perform BFS to find the path
    path, found = bfs(matrix, tuple(image_pos), (matrix.shape[0] - 1, matrix.shape[1] - 1))
    
    if path:
        # Move the image along the path
        for next_pos in path[1:]:
            # Move the image
            image_pos = list(next_pos)
            update_display()
            time.sleep(0.5)
    elif found:
        # Color the tiles on the path
        for pos in path:
            matrix[pos[0]][pos[1]] = 3
        update_display()
        print("Reached the bottom right block")
        running = False
    else:
        print("Can't reach the bottom right block")
        break

# Quit Pygame
pygame.quit()
