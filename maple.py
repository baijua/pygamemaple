import pygame as pg
import gamebox as gb
import random
import time

pg.mixer.pre_init(44100, 16, 2, 4096)
pg.init()

#background_music = "/Users/jacobsadeh/Downloads/python_story/python_music.wav"
#hit_sound = "/Users/jacobsadeh/Downloads/python_story/Hit.wav"
#pg.mixer.music.load(background_music)
#pg.mixer.music.set_volume(.7)
#pg.mixer.music.play(-1)

camera = gb.Camera(800, 600)

game = "on"

start_screen = gb.from_image(camera.x, camera.y, "https://bit.ly/2Q8qL8m")

stand_right = gb.load_sprite_sheet("https://bit.ly/2RbNzAH", 4, 1)

walk_right = gb.load_sprite_sheet("https://bit.ly/2An2tg4", 5, 1)

walk_left = gb.load_sprite_sheet("https://bit.ly/2r5hWNI", 5, 1)

hit_right = gb.load_sprite_sheet("https://bit.ly/2Racwwk", 3, 2)

jump_right = gb.load_sprite_sheet("https://bit.ly/2qZcVpY", 2, 1)

hit_left = gb.load_sprite_sheet("https://bit.ly/2QpqKMR", 3, 2)

stand_left = gb.load_sprite_sheet("https://bit.ly/2PR6UdD", 4, 1)

jump_left = gb.load_sprite_sheet("https://bit.ly/2Bukwme", 2, 1)

stand_frame = 0
walk_frame = 0
hit_frame = 0
jump_frame = 0
frame = 0

sklistn=''

design = 1
character = gb.from_image(camera.x, 540, stand_right[frame])

floor_design = "https://bit.ly/2Kp4VaJ"

if design == 2:
    floor_design = "https://bit.ly/2zP1dDh"

floors = [
    gb.from_image(120, 615, floor_design),
    gb.from_image(570, 615, floor_design),
    gb.from_image(1020, 615, floor_design),
    gb.from_image(1470, 615, floor_design),
    gb.from_image(-330, 615, floor_design),
    gb.from_image(-780, 615, floor_design),
    gb.from_image(-1230, 615, floor_design),
    gb.from_image(-1680, 615, floor_design),
    gb.from_image(-2130, 615, floor_design),
    gb.from_image(-2580, 615, floor_design),
    gb.from_image(1920, 615, floor_design),
    gb.from_image(2370, 615, floor_design),
    gb.from_image(2580, 615, floor_design),
    gb.from_image(300, 350, floor_design),
    gb.from_image(-300, 150, floor_design),
    gb.from_image(-500, 400, floor_design),
    gb.from_image(900, 400, floor_design),
    gb.from_image(1200, 150, floor_design),
    gb.from_image(1700, 250, floor_design),
    gb.from_image(2580, 615, floor_design),
    gb.from_image(2580, 615, floor_design),

]

background_design = "https://bit.ly/2PPmOVO"

if design == 2:
    background_design = "https://bit.ly/2BOL9Tq"

backgrounds = [
    gb.from_image(camera.x + 1309, camera.y, background_design),
    gb.from_image(camera.x, camera.y, background_design),
    gb.from_image(camera.x - 1310.4, camera.y, background_design),
    gb.from_image(camera.x - 2620.3, camera.y, background_design),
    gb.from_image(camera.x + 2620.3, camera.y, background_design),
]

skeletrooper_walk = gb.load_sprite_sheet("https://bit.ly/2OT1B8l", 4, 1)
skeletrooper_die = gb.load_sprite_sheet("https://i.imgur.com/40K6PdH.png", 2, 6)
skeletrooper_hit = gb.load_sprite_sheet("https://bit.ly/2r0a0ND", 1, 1)
skeletrooper_attack = gb.load_sprite_sheet("https://i.imgur.com/WlGsUa2.png", 1, 6)

# skeletrooper = gb.from_image(500, 255, skeletrooper_walk[0])
skeletrooper_1 = gb.from_image(-100, 55, skeletrooper_walk[0])
skeletrooper_2 = gb.from_image(-300, 305, skeletrooper_walk[0])
skeletrooper_3 = gb.from_image(1100, 305, skeletrooper_walk[0])
skeletrooper_4 = gb.from_image(1400, 55, skeletrooper_walk[0])
skeletrooper_5 = gb.from_image(1900, 155, skeletrooper_walk[0])

boss = gb.load_sprite_sheet("https://i.imgur.com/u2HSo3L.png", 4, 1)
skeletrooper = gb.from_image(500, 255, boss[0])

# skeletrooper = gb.from_image(500, 255, "https://bit.ly/2SpCg83")
health_bar = gb.load_sprite_sheet("https://bit.ly/2DHNJLY", 1, 5)

health_frame = 0

health = gb.from_image(camera.x - 280, 585, health_bar[health_frame])

levels = 1

exp = 0

if exp == 50:
    levels += 1
    exp = 0

level = gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold")

experience_bar = gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow")

direction = 1

skeletrooper_health = 100
skeletrooper_1_health = 30
skeletrooper_2_health = 30
skeletrooper_3_health = 30
skeletrooper_4_health = 30
skeletrooper_5_health = 30


character.yspeed = 0

mspeed=8
mpos1=100

clock = pg.time.Clock()
hittime= clock.tick()

design_test = True
skel = True
skel_1 = True
skel_2 = True
skel_3 = True
skel_4 = True
skel_5 = True

def tick(keys):
    global game, character, frame, hit_sound, background_music, health_frame, direction, skeletrooper_health
    global stand_frame, walk_frame, hit_frame, jump_frame, level, levels, exp, skeletrooper_4_health
    global frame, mspeed, hittime, skeletrooper_1_health, skeletrooper_2_health, skeletrooper_3_health
    global skeletrooper_5_health, skel, skel_1, skel_2, skel_3, skel_4, skel_5, design
    global floor_design,floor,floors,background,background_design,backgrounds,sklistn, design_test

    character.yspeed += 5
    character.y = character.y + character.yspeed

    if character.x >= 2365:
        character.x -= 10

    if character.x <= -1570:
        character.x += 10
    frame += 1
    if frame == 2:
        frame = 0

    camera.draw(start_screen)

    if pg.K_b in keys:
        game = "on"

    if health_frame == 4:
        game = "die"

    if game == "die":
        camera.clear("white")
        camera.draw(gb.from_text(camera.x, camera.y, "Oof, dead", 70, "red"))
        #pg.mixer.music.load(hit_sound)
        #pg.mixer.music.set_volume(.7)
        #pg.mixer.music.play()

        gb.pause()

    if game == "on":
        camera.clear("White")
        camera.draw(character)

        for background in backgrounds:
            camera.draw(background)

        if skeletrooper_health <= 0 and skeletrooper_1_health <= 0 and skeletrooper_2_health <= 0:
            if skeletrooper_3_health <= 0 and skeletrooper_4_health <= 0 and skeletrooper_5_health <= 0:
                camera.clear("White")
                camera.draw(character)
                design = 2
                for background in backgrounds:
                    camera.draw(background)

        for floor in floors:
            if character.bottom_touches(floor):
                character.yspeed = 0
                if pg.K_UP in keys:  # if up is pressed, jump
                    if direction == -1:
                        character.image = jump_left[frame]
                    else:
                        character.image = jump_right[frame]
                    character.yspeed = -55

            if character.touches(floor):
                character.move_to_stop_overlapping(floor)
            if skeletrooper.touches(floor):
                skeletrooper.move_to_stop_overlapping(floor)

            camera.draw(floor)
        camera.draw(skeletrooper)
        ################################################################################################
        sklist=[skeletrooper_1,skeletrooper_2,skeletrooper_3,skeletrooper_4,skeletrooper_5]
        for trooper in sklist:
            trooper.image=skeletrooper_walk[frame]
            for trooper in sklist:
                camera.draw(trooper)
        ################################################################################################
        for trooper in sklist:
            trooper.x -= mspeed
        skeletrooper.x-=mspeed
        if skeletrooper.x <= 100 or skeletrooper.x >= 500:
            mspeed = -mspeed
            for trooper in sklist:
                trooper.flip()
                skeletrooper.flip()

        if (character.touches(skeletrooper) or
            character.touches(skeletrooper_1) or character.touches(skeletrooper_2) or character.touches(skeletrooper_3)
                    or character.touches(skeletrooper_4) or character.touches(skeletrooper_5)):
            health_frame += 1
            if direction == 1:
                character.x -= 100
            if direction == -1:
                character.x += 100
            health.image = health_bar[health_frame]
            character.move_to_stop_overlapping(skeletrooper)
            character.move_to_stop_overlapping(skeletrooper_1)
            character.move_to_stop_overlapping(skeletrooper_2)
            character.move_to_stop_overlapping(skeletrooper_3)
            character.move_to_stop_overlapping(skeletrooper_4)
            character.move_to_stop_overlapping(skeletrooper_5)

        if pg.K_RIGHT in keys:
            character.image = walk_right[walk_frame]
            if walk_frame == 4:
                walk_frame = 0
            walk_frame += 1
            character.x += 10
            camera.x = character.x
            health.x = character.x - 280
            level.x = character.x + 340
            experience_bar.x = character.x

            if direction == -1:
                direction *= -1
            else:
                direction *= 1

        elif pg.K_LEFT in keys:
            character.image = walk_left[walk_frame]
            if walk_frame == 4:
                walk_frame = 0
            walk_frame += 1
            character.x -= 10
            camera.x = character.x
            health.x = character.x - 280
            level.x = character.x + 340
            experience_bar.x = character.x
            if direction == -1:
                direction *= 1
            else:
                direction *= -1

        elif pg.K_SPACE in keys:
            if direction == -1:
                if character.touches(skeletrooper, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                if character.touches(skeletrooper_1, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_1_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                if character.touches(skeletrooper_2, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_2_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                if character.touches(skeletrooper_3, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_3_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                if character.touches(skeletrooper_4, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_4_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                if character.touches(skeletrooper_5, 100, 100):
                    character.image = hit_left[hit_frame]
                    skeletrooper_5_health -= 10
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                else:
                    character.image = hit_left[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
            elif direction == 1:
                if character.touches(skeletrooper, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_health -= 10
                if character.touches(skeletrooper_1, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_1_health -= 10
                if character.touches(skeletrooper_2, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_2_health -= 10
                if character.touches(skeletrooper_3, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_3_health -= 10
                if character.touches(skeletrooper_4, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_4_health -= 10
                if character.touches(skeletrooper_5, 100, 100):
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1
                    skeletrooper_5_health -= 10
                else:
                    character.image = hit_right[hit_frame]
                    if hit_frame == 3:
                        hit_frame = 0
                    hit_frame += 1

        elif direction == -1:
            character.image = stand_left[0-4]

        else:
            character.image = stand_right[0-4]

        if skeletrooper_health <= 0:
            if exp == 50:
                levels += 1
                exp = 0
            skeletrooper.x = 9000
            if skeletrooper.x == 9000:
                if skel:
                    skel = not skel
                    exp += 50
                    pass

            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))

        if skeletrooper_1_health <= 0:
            if exp == 50:
                levels += 1
                camera.draw(gb.from_text(character.x, character.y - 20, "Level Up!", 30, "yellow"))
                exp = 0
            skeletrooper_1.x = 9000
            if skeletrooper_1.x == 9000:
                if skel_1:
                    skel_1 = not skel_1
                    exp += 10
                    pass

            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))

        if skeletrooper_2_health <= 0:
            if exp == 50:
                levels += 1
                camera.draw(gb.from_text(character.x, character.y - 20, "Level Up!", 30, "yellow"))
                exp = 0
            skeletrooper_2.x = 9000
            if skeletrooper_2.x == 9000:
                if skel_2:
                    skel_2 = not skel_2
                    exp += 10
                    pass

            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))

        if skeletrooper_3_health <= 0:
            if exp == 50:
                levels += 1
                camera.draw(gb.from_text(character.x, character.y - 20, "Level Up!", 30, "yellow"))
                exp = 0
            skeletrooper_3.x = 9000
            if skeletrooper_3.x == 9000:
                if skel_3:
                    skel_3 = not skel_3
                    exp += 10
                    pass

            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))

        if skeletrooper_4_health <= 0:
            if exp == 50:
                levels += 1
                camera.draw(gb.from_text(character.x, character.y - 20, "Level Up!", 30, "yellow"))
                exp = 0
            skeletrooper_4.x = 9000
            if skeletrooper_4.x == 9000:
                if skel_4:
                    skel_4 = not skel_4
                    exp += 10
                    pass

            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))

        if skeletrooper_5_health <= 0:
            if exp == 50:
                levels += 1
                camera.draw(gb.from_text(character.x, character.y - 20, "Level Up!", 30, "yellow"))
                exp = 0
            skeletrooper_5.x = 9000
            if skeletrooper_5.x == 9000:
                if skel_5:
                    skel_5 = not skel_5
                    exp += 10
                    pass

        if all(trooper == sklist[0] for trooper in sklist):
            design=2
        if design == 2:
            if design_test:
                design_test = not design_test
                camera.clear("white")
                pass
            # camera.clear('white')
            floor_design = "https://bit.ly/2zP1dDh"
            floors = [
                gb.from_image(120, 615, floor_design),
                gb.from_image(570, 615, floor_design),
                gb.from_image(1020, 615, floor_design),
                gb.from_image(1470, 615, floor_design),
                gb.from_image(-330, 615, floor_design),
                gb.from_image(-780, 615, floor_design),
                gb.from_image(-1230, 615, floor_design),
                gb.from_image(-1680, 615, floor_design),
                gb.from_image(-2130, 615, floor_design),
                gb.from_image(-2580, 615, floor_design),
                gb.from_image(1920, 615, floor_design),
                gb.from_image(2370, 615, floor_design),
                gb.from_image(2580, 615, floor_design),
                gb.from_image(300, 350, floor_design),
                gb.from_image(-300, 150, floor_design),
                gb.from_image(-500, 400, floor_design),
                gb.from_image(900, 400, floor_design),
                gb.from_image(1200, 150, floor_design),
                gb.from_image(1700, 250, floor_design),
                gb.from_image(2580, 615, floor_design),
                gb.from_image(2580, 615, floor_design),

            ]

            background_design = "https://bit.ly/2BOL9Tq"

            backgrounds = [
                gb.from_image(camera.x + 1309, camera.y, background_design),
                gb.from_image(camera.x, camera.y, background_design),
                gb.from_image(camera.x - 1310.4, camera.y, background_design),
                gb.from_image(camera.x - 2620.3, camera.y, background_design),
                gb.from_image(camera.x + 2620.3, camera.y, background_design),
            ]

            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))


        else:
            camera.draw(gb.from_text(camera.x, 587, "Exp: " + str(exp) + "/50", 30, "yellow"))
            camera.draw(gb.from_text(camera.x + 340, 585, "Lvl " + str(levels), 30, "gold"))

        camera.draw(character)
        camera.draw(health)
        # camera.draw(level)
        # camera.draw(experience_bar)

    camera.display()


ticks_per_second = 60

gb.timer_loop(ticks_per_second, tick)