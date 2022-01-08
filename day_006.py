# 100daysOfCode Day 6 - Escaping the Maze
# website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

count = 0
while not at_goal():
    if right_is_clear():
        if count > 20:
            turn_left()
            turn_left()
            count = 0
        else:
            turn_right()
            move()
            count += 1
    elif wall_on_right() and not front_is_clear():
        turn_left()
    else:
        move()