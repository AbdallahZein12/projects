import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space War")

BG = pygame.transform.scale(pygame.image.load("Background.jpg"), (WIDTH,HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("timesnewroman", 30)

def draw(player,elapsed_time, stars):
    WIN.blit(BG,(0,0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))
    
    pygame.draw.rect(WIN,"blue", player)
    
    for star in stars:
        pygame.draw.rect(WIN, "red", star)
    
    pygame.display.update()

def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    
    paused = False
    
    
       
    
    while run:
        
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit: 
            paused = True
            
            lost_text = FONT.render("YOU LOST!", 1 , "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            lasted = FONT.render(f"You lasted: {round(elapsed_time)}s", 1, "white")
            WIN.blit(lasted, (WIDTH/2 - lasted.get_width()/2, HEIGHT/2 + lasted.get_height()))
            prompt = FONT.render("Press enter to try again!", 1, "blue")
            WIN.blit(prompt, (WIDTH/2 - prompt.get_width()/2, HEIGHT/2 + prompt.get_height()*3))
            pygame.display.update()
            keys = pygame.key.get_pressed()

            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            paused = False
                            main()
                        
               
                
            

        
        draw(player, elapsed_time, stars)
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
        