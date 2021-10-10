""" game_functions.py

The game_functions.py file contains a number of functions that carry out
the bulk of the work in the game. The check_events() function detects relevant
events, such as keypresses and releases, and processes each of these
types of events through the helper functions check_keydown_events() and
A Ship That Fires Bullets 257 check_keyup_events().
For now, these functions manage the movement of the ship. The game_functions
module also contains update_screen(), which redraws the screen on each pass
through the main loop.

Project: Alien Invasion
Name: Antonio Jimenez
Version: 1

"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events.

    the check_events() function checks for every activity involving the keyboard,
    mouse or screen. when an event is activated then the specific check_events are
    executed.

    Parameters
    ------------
    ai_settings: obj
        the ai_settings class is passed to a different function depending on the event.

    ship: obj
        the ship class is passed to a different function depending on the event.

    screen: obj
        the object created by pygame which specifies the space made and to be passed
        to another function.

    aliens: obj
        the aliens class is passed to a different function depending on the event.

    bullets: obj
        the bullets class is passed to a different funtion depending on the event.

    """
    # for every event in "pygame.event.get()" listen for any of the following
    # and if the .type matches, execute the following.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks play.

    the check_play_button function checks if the coordianates of the mouse click
    matches with the play button. If so, then the game_active flag will be True,
    starting the game.

    Parameters
    -------------
    stats: obj
        stats in this function will be used to

    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initalize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        #Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scorebord image.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_keydown_events (event, ai_settings, screen, ship, bullets):
    """respond to keydown presses

    the check_keydown_events() responds to the specific keypresses with the left
    and right buttons.The flag for the ship is then changed to true. when the
    spacebar is pressed the fire_bullet() is then executed with the parameters

    Parameters
    -----------
        event: obj
            the event object is from the check_events() function which takes
            specific events (like pressing down, up, ect) and passes them.

        ai_settings: obj
            the ai_settings class is passed to a different function depending on the event.

        screen: obj
            the object created by pygame which specifies the space made and to be passed
            to another function.

        ship: obj
            the ship object is utilized so that the movement flag of both left
            and right are changed. otherwise it is passed to the fire_bullet function.

        bullets: obj
            the bullets are passed onto the fire_bullets function.

    """
    # if the key down event is the right button then set the moving
    # flag to true.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    # if the Q button is pressed then the window closes.
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events (event, ship):
    """Respond to key releases

    check events when the button is released, after being pressed. In this function
    the only responses necessary are to change the flags of the ship movement, that
    being left and right.

    Parameters
    ------------
        event: obj
            the event object, in this function, is used to check if the event
            being passed matches the button pressed.

        ship: obj
            the ship object is utilized so that the movement flag of both left
            and right are changed.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire bullets if limit not reached yet

    this function takes the number of bullets stored and checks if the amount of
    bullets allowed, stored in the ai_settings, is greater than it. When True
    a new bullet object is created called new_bullet and is added to the bullets sprites.

    Parameters
    -----------
        ai_settings: obj
            ai_settings is used to grab the integer "bullets_allowed" to compare
            to the amount of bullets in the group.
    """
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of the bullets and get rid of the old bullets."""
    # Update bullet position.
    bullets.update()

    # get rid of the bullets that have dissapeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided
    # Check for any bullets that have hit the aliens.
    # if so, get rid of the bullet and the aliens.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # if collisions dictionary has been defined then for each value in the collision dictionary,
    # the score will add by the alien values multiplied by the length of the amount
    # of the aliens in the group.
    # (the point is made if the bullet width is 300, then the score should multiply)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            # execute prep_score function.
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create a new fleet.
        # if the entire fleet is destroyed start a new level as well.
        bullets.empty()
        ai_settings.increase_speed()

        # increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a fleet full of aliens.

    """
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_of_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_row):
        for alien_number in range(number_of_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aleins have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if the fleet is at an edge, and then update the positions of all the aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to the ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # update scoreboard.
        sb.prep_ship()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update image on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    # fill the screen with the fill function.
    screen.fill(ai_settings.bg_color)

    # draw the ship using blitme
    # be sure to have the ship after the fill, so that the ship is over the
    # background.
    ship.blitme()
    aliens.draw(screen)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
