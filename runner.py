import pygame
import sys
import os
import random
from character import Character
from physics import Physics
import background
from pipes import TubePair
from pygame.sprite import LayeredUpdates

def main():
    #sets up the game and audio mixer
    pygame.init()
    pygame.mixer.init()
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
    )
    pygame.display.set_caption("Flappy Bird Game")
    clock = pygame.time.Clock()
    running = True

    #saves the audio to variables
    jump_sound = pygame.mixer.Sound('assets/jump.wav')
    jump_sound.set_volume(0.5)
    fail_sound = pygame.mixer.Sound('assets/fail.wav')
    fail_sound.set_volume(0.5)
    victory_sound = pygame.mixer.Sound('assets/win.wav')
    victory_sound.set_volume(0.5)
    add_score_sound = pygame.mixer.Sound('assets/coin.wav')
    victory_sound.set_volume(0.5)

    physics = Physics(gravity=2000)
    mc = Character(500, SCREEN_HEIGHT // 2, physics, jump_sound)

    all_sprites = LayeredUpdates()
    pipes_group = pygame.sprite.Group()
    tube_pairs = []
    #adds sprites to background
    background_elements = background.load_background(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites.add(background_elements['sky_sprite'])
    all_sprites.add(background_elements['ground_sprite'])
    all_sprites.add(background_elements['sun_sprite'])
    all_sprites.add(background_elements['cloud_sprites'])

    mc._layer = 2
    all_sprites.add(mc)

    TUBE_WIDTH = 100
    TUBE_GAP = 400
    TUBE_VELOCITY = 300
    TUBE_FREQUENCY = 1500
    last_tube_spawn_time = pygame.time.get_ticks()

    pause_start_time = 0
    total_pause_duration = 0
    #checks to see if high_score file exists if not high_score = 0
    high_score_file = 'high_score.txt'
    if os.path.exists(high_score_file):
        with open(high_score_file, 'r') as file:
            try:
                high_score = int(file.read())
            except ValueError:
                high_score = 0
    else:
        high_score = 0

    current_score = 0

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 36)

    victory = False
    paused = False
    #code to run code
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if mc.alive:
                        mc.jump()
                elif event.key == pygame.K_ESCAPE:
                    if mc.alive:
                        paused = True
                        pause_start_time = pygame.time.get_ticks()
                    else:
                        running = False
        #pauses
        if paused:
            show_pause_screen(screen, font)
            paused = False
            pause_end_time = pygame.time.get_ticks()
            pause_duration = pause_end_time - pause_start_time
            total_pause_duration += pause_duration
            last_tube_spawn_time += pause_duration
            clock.tick()
            continue

        delta_time = clock.tick(60) / 1000.0

        current_time = pygame.time.get_ticks() - total_pause_duration
        if current_time - last_tube_spawn_time >= TUBE_FREQUENCY:
            last_tube_spawn_time = current_time
            new_tube_pair = TubePair(
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                TUBE_WIDTH,
                TUBE_GAP,
                TUBE_VELOCITY,
                layer=1
            )
            new_tube_pair.add_to_group(pipes_group, all_sprites)
            tube_pairs.append(new_tube_pair)

        all_sprites.update(delta_time)

        if pygame.sprite.spritecollide(mc, pipes_group, False):
            mc.alive = False

        for tube_pair in tube_pairs[:]:
            if not tube_pair.passed and tube_pair.top_tube.rect.right < mc.rect.left:
                tube_pair.passed = True
                current_score += 1
                add_score_sound.play()
                if current_score >= 10:
                    victory = True
                    running = False
                    victory_sound.play()
                    break
            if not tube_pair.top_tube.alive() and not tube_pair.bottom_tube.alive():
                tube_pairs.remove(tube_pair)

        all_sprites.draw(screen)

        score_text = font.render(f"Score: {current_score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_text, (10, 50))

        pygame.display.flip()

        if not mc.alive:
            running = False
            fail_sound.play()
    #creates the high_score file to save high score
    if int(current_score) > high_score:
        high_score = int(current_score)
        with open(high_score_file, 'w') as file:
            file.write(str(high_score))

    if victory:
        show_victory_screen(screen, font, current_score, high_score)
    else:
        show_game_over_screen(screen, font, current_score, high_score)

    pygame.quit()
    sys.exit(0)

def show_pause_screen(screen, font):
    paused = True
    clock = pygame.time.Clock()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_q:
                    paused = False
                    pygame.quit()
                    sys.exit(0)

        screen.fill((0, 0, 0))

        pause_text = font.render("Game Paused", True, (255, 255, 0))
        screen.blit(pause_text, (screen.get_width() // 2 - pause_text.get_width() // 2,
                                 screen.get_height() // 2 - 50))

        resume_text = font.render("Press 'Esc' to Resume or 'Q' to Quit", True, (255, 255, 255))
        screen.blit(resume_text, (screen.get_width() // 2 - resume_text.get_width() // 2,
                                  screen.get_height() // 2 + 10))

        pygame.display.flip()
        clock.tick(60)

def show_victory_screen(screen, font, current_score, high_score):
    victory = True
    clock = pygame.time.Clock()
    while victory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                victory = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    victory = False
                elif event.key == pygame.K_r:
                    victory = False
                    main()
                    return

        screen.fill((0, 0, 0))

        victory_text = font.render("Victory!", True, (0, 255, 0))
        screen.blit(victory_text, (screen.get_width() // 2 - victory_text.get_width() // 2,
                                   screen.get_height() // 2 - 100))

        final_score_text = font.render(f"Final Score: {int(current_score)}", True, (255, 255, 255))
        screen.blit(final_score_text, (screen.get_width() // 2 - final_score_text.get_width() // 2,
                                       screen.get_height() // 2))

        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_text, (screen.get_width() // 2 - high_score_text.get_width() // 2,
                                      screen.get_height() // 2 + 50))

        instructions_text = font.render("Press 'R' to Play Again or 'Esc' to Quit", True, (255, 255, 255))
        screen.blit(instructions_text, (screen.get_width() // 2 - instructions_text.get_width() // 2,
                                        screen.get_height() // 2 + 150))

        pygame.display.flip()
        clock.tick(60)

def show_game_over_screen(screen, font, current_score, high_score):
    game_over = True
    clock = pygame.time.Clock()
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = False
                elif event.key == pygame.K_r:
                    game_over = False
                    main()
                    return

        screen.fill((0, 0, 0))

        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2,
                                     screen.get_height() // 2 - 100))

        final_score_text = font.render(f"Final Score: {int(current_score)}", True, (255, 255, 255))
        screen.blit(final_score_text, (screen.get_width() // 2 - final_score_text.get_width() // 2,
                                       screen.get_height() // 2))

        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_text, (screen.get_width() // 2 - high_score_text.get_width() // 2,
                                      screen.get_height() // 2 + 50))

        instructions_text = font.render("Press 'R' to Retry or 'Esc' to Quit", True, (255, 255, 255))
        screen.blit(instructions_text, (screen.get_width() // 2 - instructions_text.get_width() // 2,
                                        screen.get_height() // 2 + 150))

        pygame.display.flip()
        clock.tick(60)



