for index in range(100):
    pins.digital_write_pin(DigitalPin.P1, 1)
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.pause(0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(1000)