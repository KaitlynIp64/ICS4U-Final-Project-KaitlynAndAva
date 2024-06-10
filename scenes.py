#!/usr/bin/env python3

# Created by: Kaitlyn I and Ava V
# Created on: June 2024
# This constants file is for Space Alien game

import time
import random
import stage
import supervisor
import ugame
import constants

from code import SpaceAliensGame

class SplashScene:
    def __init__(self, game):
        self.game = game

    def run(self):
        coin_sound = open("coin.wav", 'rb')
        self.game.sound.mute(False)
        self.game.sound.play(coin_sound)

        image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

        background = stage.Grid(
            image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
        )

        game = stage.Stage(ugame.display, constants.FPS)
        game.layers = [background]
        game.render_block()

        while True:
            time.sleep(1.0)
            self.game.menu_scene()

class MenuScene:
    def __init__(self, game):
        self.game = game

    def run(self):
        image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

        text = []
        text1 = stage.Text(
            width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
        )
        text1.move(20, 10)
        text1.text("MT Game Studios")
        text.append(text1)

        text2 = stage.Text(
            width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
        )
        text2.move(40, 110)
        text2.text("PRESS START")
        text.append(text2)

        background = stage.Grid(
            image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
        )

        background.tile(2, 2, 0)
        background.tile(3, 2, 1)
        background.tile(4, 2, 2)
        background.tile(5, 2, 3)
        background.tile(6, 2, 4)
        background.tile(7, 2, 0)
        background.tile(2, 3, 0)
        background.tile(3, 3, 5)
        background.tile(4, 3, 6)
        background.tile(5, 3, 7)
        background.tile(6, 3, 8)
        background.tile(7, 3, 0)
        background.tile(2, 4, 0)
        background.tile(3, 4, 9)
        background.tile(4, 4, 10)
        background.tile(5, 4, 11)
        background.tile(6, 4, 12)
        background.tile(7, 4, 0)
        background.tile(2, 5, 0)
        background.tile(3, 5, 0)
        background.tile(4, 5, 13)
        background.tile(5, 5, 14)
        background.tile(6, 5, 0)
        background.tile(7, 5, 0)

        game = stage.Stage(ugame.display, constants.FPS)
        game.layers = text + [background]
        game.render_block()

        while True:
            keys = ugame.buttons.get_pressed()

            if keys & ugame.K_START != 0:
                self.game.game_scene()

            game.tick()

class GameScene:
    def __init__(self, game):
        self.game = game

    def run(self):
        score = 0

        score_text = stage.Text(width=29, height=12)
        score_text.clear()
        score_text.cursor(0, 0)
        score_text.move(1, 1)
        score_text.text("Score: {0}".format(score))

        def show_alien():
            for alien_number in range(len(aliens)):
                if aliens[alien_number].x < 0:
                    aliens[alien_number].move(
                        random.randint(
                            0 + constants.SPRITE_SIZE,
                            constants.SCREEN_X - constants.SPRITE_SIZE,
                        ),
                        constants.OFF_TOP_SCREEN,
                    )
                    break

        image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
        image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

        a_button = constants.button_state["button_up"]

        pew_sound = open("pew.wav", "rb")
        boom_sound = open("boom.wav", "rb")
        crash_sound = open("crash.wav", "rb")
        self.game.sound.stop()
        self.game.sound.mute(False)

        background = stage.Grid(
            image_bank_background,
            constants.SCREEN_GRID_X,
            constants.SCREEN_GRID_Y,
        )
        for x_location in range(constants.SCREEN_GRID_X):
            for y_location in range(constants.SCREEN_GRID_Y):
                tile_picked = random.randint(1, 3)
                background.tile(x_location, y_location, tile_picked)

        ship = stage.Sprite(
            image_bank_sprites,
            5,
            75,
            constants.SCREEN_Y - (2 * constants.SPRITE_SIZE),
        )

        aliens = []
        for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
            a_single_alien = stage.Sprite(
                image_bank_sprites,
                9,
                constants.OFF_SCREEN_X,
                constants.OFF_SCREEN_Y,
            )
            aliens.append(a_single_alien)
        show_alien()

        lasers = []
        for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
            a_single_laser = stage.Sprite(
                image_bank_sprites,
                10,
                constants.OFF_SCREEN_X,
                constants.OFF_SCREEN_Y,
            )
            lasers.append(a_single_laser)

        game = stage.Stage(ugame.display, constants.FPS)
        game.layers = [score_text] + aliens + lasers + [ship] + [background]
        game.render_block()

        while True:
            keys = ugame.buttons.get_pressed()

            if keys & ugame.K_X:
                pass
            if keys & ugame.K_O != 0:
                if a_button == constants.button_state["button_up"]:
                    a_button = constants.button_state["button_just_pressed"]
                elif a_button == constants.button_state["button_just_pressed"]:
                    a_button = constants.button_state["button_still_pressed"]
            else:
                if a_button == constants.button_state["button_still_pressed"]:
                    a_button = constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]
            if keys & ugame.K_START != 0:
                pass
            if keys & ugame.K_SELECT != 0:
                pass
            if keys & ugame.K_RIGHT != 0:
                if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                    ship.move(ship.x + 1, ship.y)
                else:
                    ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            if keys & ugame.K_LEFT != 0:
                if ship.x >= 0:
                    ship.move(ship.x - 1, ship.y)
                else:
                    ship.move(0, ship.y)
            if keys & ugame.K_UP != 0:
                pass
            if keys & ugame.K_DOWN != 0:
                pass

            if a_button == constants.button_state["button_just_pressed"]:
                for laser_number in range(len(lasers)):
                    if lasers[laser_number].x < 0:
                        lasers[laser_number].move(ship.x, ship.y)
                        self.game.sound.play(pew_sound)
                        break

            for laser_number in range(len(lasers)):
                if lasers[laser_number].x > 0:
                    lasers[laser_number].move(
                        lasers[laser_number].x,
                        lasers[laser_number].y - constants.LASER_SPEED,
                    )
                    if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                        lasers[laser_number].move(
                            constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y,
                        )

            for alien_number in range(len(aliens)):
                if aliens[alien_number].x > 0:
                    aliens[alien_number].move(
                        aliens[alien_number].x,
                        aliens[alien_number].y + constants.ALIEN_SPEED,
                    )
                    if aliens[alien_number].y > constants.SCREEN_Y:
                        aliens[alien_number].move(
                            constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y,
                        )
                        show_alien()
                        score -= 1
                        if score < 0:
                            score = 0
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text("Score: {0}".format(score))

            for laser_number in range(len(lasers)):
                if lasers[laser_number].x > 0:
                    for alien_number in range(len(aliens)):
                        if aliens[alien_number].x > 0:
                            if stage.collide(
                                lasers[laser_number].x + 6,
                                lasers[laser_number].y + 2,
                                lasers[laser_number].x + 11,
                                lasers[laser_number].y + 12,
                                aliens[alien_number].x + 1,
                                aliens[alien_number].y,
                                aliens[alien_number].x + 15,
                                aliens[alien_number].y + 15,
                            ):
                                aliens[alien_number].move(
                                    constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y,
                                )
                                lasers[laser_number].move(
                                    constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y,
                                )
                                self.game.sound.stop()
                                self.game.sound.play(boom_sound)
                                show_alien()
                                show_alien()
                                score += 1
                                score_text.clear()
                                score_text.cursor(0, 0)
                                score_text.move(1, 1)
                                score_text.text("Score: {0}".format(score))

            for alien_number in range(len(aliens)):
                if aliens[alien_number].x > 0:
                    if stage.collide(
                        aliens[alien_number].x + 1,
                        aliens[alien_number].y,
                        aliens[alien_number].x + 15,
                        aliens[alien_number].y + 15,
                        ship.x,
                        ship.y,
                        ship.x + 15,
                        ship.y + 15,
                    ):
                        self.game.sound.stop()
                        self.game.sound.play(crash_sound)
                        self.game.game_over_scene(score)

            game.render_sprites(aliens + lasers + [ship])
            game.tick()

class GameOverScene:
    def __init__(self, game, score):
        self.game = game
        self.score = score

    def run(self):
        self.game.sound.stop()

        image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

        background = stage.Grid(
            image_bank_2,
            constants.SCREEN_GRID_X,
            constants.SCREEN_GRID_Y,
        )

        text = []
        text1 = stage.Text(
            width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
        )
        text1.move(22, 20)
        text1.text("Final Score: {:0>2d}".format(self.score))
        text.append(text1)

        text2 = stage.Text(
            width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
        )
        text2.move(43, 60)
        text2.text("GAME OVER")
        text.append(text2)

        text3 = stage.Text(
            width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
        )
        text3.move(32, 110)
        text3.text("PRESS SELECT")
        text.append(text3)

        game = stage.Stage(ugame.display, constants.FPS)
        game.layers = text + [background]
        game.render_block()

        while True:
            keys = ugame.buttons.get_pressed()
        
            if keys & ugame.K_SELECT != 0:
                supervisor.reload()
            game.tick()
