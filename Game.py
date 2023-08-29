from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font, Button
import time

canvas_width = 800
canvas_height = 400
root = Tk()
c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue')  # creates the sky
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)  # creates the grass
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)  # creates the sun in the corner
c.pack()

color_cycle = cycle(['light coral','lemon chiffon', 'CadetBlue1'])  # the colors of the balls
ball_width = 45
ball_height = 45
ball_score = 10
ball_speed = 500
ball_interval = 4000
difficulty_factor = 0.95
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y,
                       catcher_start_x2, catcher_start_y2, start=200, extent=140,
                       style='arc', outline=catcher_color, width=3)

game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)
score = 0
score_text = c.create_text(10, 10, anchor='nw', font=game_font, fill='darkblue', text='Score: ' + str(score))

# def paused():
#    time.sleep(10000)


# pause = Button(width=10, height=3, text='Pause', command=paused)
# pause.pack()

lives_remaining = 3
lives_text = c.create_text(canvas_width - 10, 10, anchor='ne', font=game_font, fill='darkblue',
                           text='Lives: ' + str(lives_remaining))
balls = []


def create_ball():
    x = randrange(10, 740)
    y = 40
    new_ball = c.create_oval(x, y, x + ball_width, y + ball_height, fill=next(color_cycle), width=0)
    balls.append(new_ball)
    root.after(ball_interval, create_ball)


def move_balls():
    for ball in balls:
        (ball_x, ball_y, ball_x2, ball_y2) = c.coords(ball)
        c.move(ball, 0, 10)
        if ball_y2 > canvas_height:
            ball_dropped(ball)
    root.after(ball_speed, move_balls)


def ball_dropped(ball):
    balls.remove(ball)
    c.delete(ball)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('Game Over!', 'Final Score: ' + str(score))
        root.destroy()


def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining))


def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for ball in balls:
        (ball_x, ball_y, ball_x2, ball_y2) = c.coords(ball)
        if catcher_x < ball_x and ball_x2 < catcher_x2 and catcher_y2 - ball_y2 < 40:
            balls.remove(ball)
            c.delete(ball)
            increase_score(ball_score)
    root.after(100, check_catch)


def increase_score(points):
    global score, ball_speed, ball_interval
    score += points
    ball_speed = int(ball_speed * difficulty_factor)
    ball_interval = int(ball_interval * difficulty_factor)
    c.itemconfigure(score_text, text='Score: ' + str(score))


def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)


def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()

root.after(1000, create_ball)
root.after(1000, move_balls)
root.after(1000, check_catch)
root.mainloop()
