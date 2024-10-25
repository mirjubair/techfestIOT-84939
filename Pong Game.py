import tkinter as tk

# Game window
root = tk.Tk()
root.title("Pong Game")
canvas = tk.Canvas(root, width=400, height=300, bg='black')
canvas.pack()

# Paddle and ball settings
paddle = canvas.create_rectangle(10, 150, 30, 210, fill='white')
ball = canvas.create_oval(190, 140, 210, 160, fill='white')

# Ball velocity
ball_dx, ball_dy = 3, 3

# Paddle movement
def move_paddle(event):
    if event.keysym == 'Up' and canvas.coords(paddle)[1] > 0:
        canvas.move(paddle, 0, -20)
    elif event.keysym == 'Down' and canvas.coords(paddle)[3] < 300:
        canvas.move(paddle, 0, 20)

root.bind("<Up>", move_paddle)
root.bind("<Down>", move_paddle)

# Ball movement and collision detection
def move_ball():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)

    # Bounce off walls
    if ball_pos[1] <= 0 or ball_pos[3] >= 300:
        ball_dy = -ball_dy
    if ball_pos[0] <= 0 or ball_pos[2] >= 400:
        ball_dx = -ball_dx

    # Paddle collision
    if ball_pos[0] <= canvas.coords(paddle)[2] and \
       ball_pos[1] >= canvas.coords(paddle)[1] and \
       ball_pos[3] <= canvas.coords(paddle)[3]:
        ball_dx = -ball_dx

    root.after(50, move_ball)

move_ball()
root.mainloop()
