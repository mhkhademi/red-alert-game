import pgzrun                             
import random

'''********************   Constant Variable   *****************'''

FONT_COLOR = (255, 255, 255)               # Display_message font color
WIDTH = 800                                # Display_width
HEIGHT = 600                               # Display_height
CENTER_X = WIDTH / 2                       # Display_center_x
CENTER_Y = HEIGHT / 2                      # Display_center_y
CENTER = (CENTER_X, CENTER_Y)              # Display_center_list
FINAL_LEVEL = 10                           # Number_of_levels
START_SPEED = 20                           # Initial_speed
COLORS = ["green", "blue"]                 # Not click on the this colors

'''********************   Variable   *****************'''

game_over = False                          # Determine_the_player_game_over
game_complete = False                      # Determine_the_end_of_the_game
current_level = 1                          # Current_level
stars = []                                 # Actors_list
animations = []                            # Actors_Animations_list

'''********************   Founctions   *****************'''

def draw ():
    global stars, current_level, game_over, game_complete
    screen.clear()                         #Clear_the_screen
    screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER!", "Try again.")          #Print_message_game_over_on_display
    elif game_complete:
        display_message("YOU WON!", "Well done.")            #Print_message_end_game_on_display
    else:
        for star in stars:
            star.draw()                    #Draw_star

def update ():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

def make_stars (number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create (number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars (colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars (stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout) :
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars ( stars_to_animate ):
    for star in stars_to_animate :
        duration = START_SPEED - current_level
        star.anchor = ("center" , "bottom")
        animation = animate(star , duration=duration , on_finished=handle_game_over , y = HEIGHT)
        animations.append(animation)

def handle_game_over ():
    global game_over
    game_over = True

def on_mouse_down (pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos) :
            if "red" in star.image :
                red_star_click()
            else :
                handle_game_over()

def red_star_click():
    global current_level , stars , animations , game_complete
    stop_animations ( animations )
    if current_level == FINAL_LEVEL :
        game_complete = True
    else :
        current_level = current_level + 1
        stars = []
        animations = []

def stop_animations ( animations_to_stop ):
    for animation in animations_to_stop :
        if animation.running :
            animation.stop()

def display_message ( heading_text , sub_heading_text ):
    screen.draw.text( heading_text , fontsize = 60 , center = CENTER , color = FONT_COLOR )
    screen.draw.text( sub_heading_text , fontsize = 30 , center = ( CENTER_X , CENTER_Y + 30 ) , color = FONT_COLOR )

pgzrun.go()
