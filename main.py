import pygame

pygame.init()
screen = pygame.display.set_mode(
    (1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
)
clock = pygame.time.Clock()
running = True
playing = True
settings = False
entitycounter = 0

# tiles
level = Level(level_map, screen)

# main character
main_character = level.get_player()
# font
headingGameFont = pygame.font.Font("./assets/Kaph-Regular.otf", 20)
slime1 = Slime(entitycounter, 500, 1080 - 69.3333, 0, 0, 0)
health_img = pygame.image.load("assets/gui/health.png")
health_img = pygame.transform.scale(health_img, (301, 53.6))
health_img_rect = health_img.get_rect()
health_img_rect.center = (160.5, 37)
green = (58, 153, 68)
speed = 5
while running:
    if playing:
        # character movement
        delta_time = clock.tick(60) / 10.0
        main_character.move(delta_time)
        main_character.update_health(delta_time)
        screen.fill((255, 255, 255))
        slime1.activate(screen, main_character, delta_time)
        level.run()

        if main_character.health >= 97:
            pygame.draw.rect(
                screen, green, (40, 26.5, 266.1 * main_character.health / 100, 7)
            )
            pygame.draw.rect(
                screen, green, (40, 33.5, 266.1 * main_character.health / 100, 7)
            )
            pygame.draw.rect(
                screen, green, (40, 40.5, 266.1 * main_character.health / 100, 7)
            )
            pygame.draw.rect(
                screen, green, (40, 47.5, 266.1 * main_character.health / 100, 7)
            )
        else:
            pygame.draw.rect(
                screen, green, (40, 26.5, 266 * main_character.health / 100 + 10, 7)
            )
            pygame.draw.rect(
                screen, green, (40, 33.5, 266 * main_character.health / 100 + 5, 7)
            )
            pygame.draw.rect(
                screen, green, (40, 40.5, 266 * main_character.health / 100, 7)
            )
            pygame.draw.rect(
                screen, green, (40, 47.5, 266 * main_character.health / 100 - 5, 7)
            )

        # fps counter
        fpsText = Text()
        fpsText = fpsText.get_paragraph_text(
            f"FPS: {str(int(clock.get_fps()))}", "black", 1850, 30
        )
        screen.blit(fpsText[1], fpsText[0])

        # health display
        screen.blit(health_img, health_img_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    main_character.jump()
                # if event.key == pygame.K_s:
                #     #crouch
                if event.key == pygame.K_LCTRL:
                    main_character.sprinting = True
                if event.key == pygame.K_j:
                    main_character.change_health(-60, gradual=True)
                if event.key == pygame.K_a:
                    main_character.update_x_velocity(-speed)
                if event.key == pygame.K_d:
                    main_character.update_x_velocity(speed)
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    settings = True
            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_s:
                #     #uncrouch
                if event.key == pygame.K_j:
                    main_character.change_health(60, gradual=True)
                if event.key == pygame.K_a:
                    main_character.update_x_velocity(0)
                if event.key == pygame.K_d:
                    main_character.update_x_velocity(0)
                if event.key == pygame.K_LCTRL:
                    main_character.sprinting = False

    if settings:
        quit_button_hover = False
        mouse = pygame.mouse.get_pos()
        settings_rect = pygame.draw.rect(
            screen, "black", (560, 340, 800, 400), border_radius=20
        )
        # paused header
        headingText = Text()
        headingText = headingText.get_heading_one(
            "Paused", "white", settings_rect.centerx, 400
        )
        screen.blit(headingText[1], headingText[0])

        # quit button
        if 960 + 200 >= mouse[0] >= 960 - 200 and 625 + 50 >= mouse[1] >= 625 - 50:
            quit_button_hover = True
        if quit_button_hover:
            quit_button = pygame.draw.rect(
                screen,
                "grey",
                (settings_rect.centerx - 200, 600, 400, 50),
                border_radius=30,
            )
        else:
            quit_button = pygame.draw.rect(
                screen,
                "white",
                (settings_rect.centerx - 200, 600, 400, 50),
                border_radius=30,
            )
        quit_text = Text()
        quit_text = quit_text.get_heading_two(
            "Quit", "black", settings_rect.centerx, 625
        )
        screen.blit(quit_text[1], quit_text[0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings = False
                    playing = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (
                    960 + 200 >= mouse[0] >= 960 - 200
                    and 625 + 50 >= mouse[1] >= 625 - 50
                ):
                    running = False

    pygame.display.flip()
    clock.tick(120)
