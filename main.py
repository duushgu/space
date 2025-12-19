@namespace
class SpriteKind:
    Gas = SpriteKind.create()

def on_a_pressed():
    global darts, projectile
    darts = [assets.image("""
            Dart1
            """),
        assets.image("""
            Dart2
            """),
        assets.image("""
            Dart1
            """)]
    projectile = sprites.create_projectile_from_sprite(darts._pick_random(), mySprite, 0, -140)
    projectile.start_effect(effects.warm_radial, 100)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            1600,
            1,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global enemySpeed
    sprite.destroy(effects.confetti, 200)
    otherSprite.destroy(effects.confetti, 200)
    info.change_score_by(1)
    if info.score() == 1:
        info.change_score_by(5)
        mySprite.say_text("easy?, now INTENSIVE", 3000, False)
        music.play(music.string_playable("C E G C G E G C ", 273),
            music.PlaybackMode.UNTIL_DONE)
        enemySpeed = 99
    music.play(music.create_sound_effect(WaveShape.NOISE,
            5000,
            600,
            255,
            0,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite3):
    info.change_life_by(-1)
    otherSprite3.destroy(effects.confetti, 400)
    scene.camera_shake(4, 500)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            2845,
            255,
            0,
            500,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite2, otherSprite2):
    statusbar.value = 100
    otherSprite2.destroy()
    music.play(music.create_sound_effect(WaveShape.SINE,
            2889,
            200,
            255,
            0,
            200,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Gas, on_on_overlap3)

def on_life_zero():
    game.over(False)
    music.play(music.string_playable("E D C A G E D C ", 273),
        music.PlaybackMode.UNTIL_DONE)
info.on_life_zero(on_life_zero)

def on_on_zero(status):
    game.over(False)
    music.play(music.string_playable("E D C A G E D C ", 273),
        music.PlaybackMode.UNTIL_DONE)
statusbars.on_zero(StatusBarKind.energy, on_on_zero)

my_enemy: Sprite = None
myFuel: Sprite = None
projectile: Sprite = None
darts: List[Image] = []
statusbar: StatusBarSprite = None
mySprite: Sprite = None
enemySpeed = 0
enemySpeed = 50
scene.set_background_image(assets.image("""
    Galaxy
    """))
scroller.scroll_background_with_speed(0, 10)
mySprite = sprites.create(assets.image("""
    Rocket
    """), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
animation.run_image_animation(mySprite,
    assets.animation("""
        Flying Rocket
        """),
    100,
    True)
statusbar = statusbars.create(20, 4, StatusBarKind.energy)
statusbar.attach_to_sprite(mySprite, -25, 0)
music.play(music.string_playable("C G F E D C D C ", 246),
    music.PlaybackMode.UNTIL_DONE)

def on_update_interval():
    global myFuel
    myFuel = sprites.create_projectile_from_side(assets.image("""
        Fuel
        """), 0, 40)
    myFuel.x = randint(5, 155)
    myFuel.set_kind(SpriteKind.Gas)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global my_enemy
    my_enemy = sprites.create_projectile_from_side(assets.image("""
        Spider
        """), 0, 50)
    my_enemy.x = randint(5, 150)
    my_enemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(my_enemy,
        assets.animation("""
            Flying Spider
            """),
        100,
        True)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    statusbar.value += -1
game.on_update_interval(300, on_update_interval3)

def on_update_interval4():
    global my_enemy
    my_enemy = sprites.create_projectile_from_side(assets.image("""
        Spider
        """), 0, 50)
    my_enemy.x = randint(5, 150)
    my_enemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(my_enemy,
        assets.animation("""
            Flying Spider
            """),
        100,
        True)
game.on_update_interval(1200, on_update_interval4)
