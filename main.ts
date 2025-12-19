namespace SpriteKind {
    export const Gas = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    darts = [assets.image`Dart1`, assets.image`Dart2`, assets.image`Dart1`]
    projectile = sprites.createProjectileFromSprite(darts._pickRandom(), mySprite, 0, -140)
    projectile.startEffect(effects.warmRadial, 100)
    music.play(music.createSoundEffect(WaveShape.Square, 1600, 1, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy(effects.confetti, 200)
    otherSprite.destroy(effects.confetti, 200)
    info.changeScoreBy(1)
    if (info.score() == 1) {
        info.changeScoreBy(5)
        mySprite.sayText("easy?, now INTENSIVE", 3000, false)
        music.play(music.stringPlayable("C E G C G E G C ", 273), music.PlaybackMode.UntilDone)
        enemySpeed += 100
    }
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 600, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    info.changeLifeBy(-1)
    otherSprite3.destroy(effects.confetti, 400)
    scene.cameraShake(4, 500)
    music.play(music.createSoundEffect(WaveShape.Square, 5000, 2845, 255, 0, 500, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Gas, function (sprite2, otherSprite2) {
    statusbar.value = 100
    otherSprite2.destroy()
    music.play(music.createSoundEffect(WaveShape.Sine, 2889, 200, 255, 0, 200, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
info.onLifeZero(function () {
    game.over(false)
    music.play(music.stringPlayable("E D C A G E D C ", 273), music.PlaybackMode.UntilDone)
})
statusbars.onZero(StatusBarKind.Energy, function (status) {
    game.over(false)
    music.play(music.stringPlayable("E D C A G E D C ", 273), music.PlaybackMode.UntilDone)
})
let my_enemy: Sprite = null
let myFuel: Sprite = null
let projectile: Sprite = null
let darts: Image[] = []
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
let enemySpeed = 0
enemySpeed += 50
scene.setBackgroundImage(assets.image`Galaxy`)
scroller.scrollBackgroundWithSpeed(0, 10)
mySprite = sprites.create(assets.image`Rocket`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
animation.runImageAnimation(
mySprite,
assets.animation`Flying Rocket`,
100,
true
)
statusbar = statusbars.create(20, 4, StatusBarKind.Energy)
statusbar.attachToSprite(mySprite, -25, 0)
music.play(music.stringPlayable("C G F E D C D C ", 246), music.PlaybackMode.UntilDone)
game.onUpdateInterval(5000, function () {
    myFuel = sprites.createProjectileFromSide(assets.image`Fuel`, 0, 40)
    myFuel.x = randint(5, 155)
    myFuel.setKind(SpriteKind.Gas)
})
game.onUpdateInterval(500, function () {
    my_enemy = sprites.createProjectileFromSide(assets.image`Spider`, 0, enemySpeed)
    my_enemy.x = randint(5, 150)
    my_enemy.setKind(SpriteKind.Enemy)
    animation.runImageAnimation(
    my_enemy,
    assets.animation`Flying Spider`,
    100,
    true
    )
})
game.onUpdateInterval(300, function () {
    statusbar.value += -1
})
game.onUpdateInterval(1200, function () {
    my_enemy = sprites.createProjectileFromSide(assets.image`Spider`, 0, enemySpeed)
    my_enemy.x = randint(5, 150)
    my_enemy.setKind(SpriteKind.Enemy)
    animation.runImageAnimation(
    my_enemy,
    assets.animation`Flying Spider`,
    100,
    true
    )
})
