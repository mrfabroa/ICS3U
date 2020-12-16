
# Import necessary libraries
import arcade
import os

# Define a window space
arcade.open_window(600, 600, "My First Arcade Program")

# Set background colour
arcade.set_background_color(arcade.color.WHITE)

# Drawing occurs after this line
arcade.start_render()

# Examples of drawing commands
arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)

# Drawing occurs before this line
arcade.finish_render()

arcade.run()
