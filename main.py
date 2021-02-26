def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
basic.forever(on_forever)
