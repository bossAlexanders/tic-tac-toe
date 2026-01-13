from tkinter import *
from tkinter import messagebox

def init_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    canvas.delete('all')
    draw_grid()

def draw_grid():
    for i in range(1,3):
        canvas.create_line(i * cell_size, 0, i * cell_size, canvas_size, width=2 )
        canvas.create_line(0, i * cell_size, canvas_size, i * cell_size, width=2 )

def on_click(event):
    global current_player, x_wins, o_wins, wins_all, draw, procent_X, procent_O, wins_needed
    
    col = event.x // cell_size
    row = event.y // cell_size
    index = row * 3 + col

    if board[index] == "":
        board[index] = current_player
        draw_symbol(row, col, current_player)

        if check_winner():
            messagebox.showinfo('Победа!',f"Победила команда {current_player}")
            wins_all += 1
            if current_player == "X":
                x_wins += 1
                x_score_label.config(text=f"X побед: {x_wins}")
            else:
                o_wins += 1
                o_score_label.config(text=f"O побед: {o_wins}")
            wins_all_label.config(text=f"Сыграно игр всего: {wins_all}")

            if wins_all > 0:
                procent_X = round((x_wins / wins_all) * 100, 1)
                procent_O = round((o_wins / wins_all) * 100, 1)
                procent_X_label.config(text=f"Побед X: {procent_X}%")
                procent_O_label.config(text=f"Побед O: {procent_O}%")
            
            if x_wins == wins_needed or o_wins == wins_needed:
                messagebox.showinfo('Супер!', f"Супер победитель {current_player}!")
                x_score_label.config(text=f"X побед: {x_wins}")
                o_score_label.config(text=f"O побед: {o_wins}")
                wins_needed_label.config(text=f"Нужно побед: {mega_wins}")
            if x_wins == mega_wins or o_wins == mega_wins:
                messagebox.showinfo("ЧТОО?!", f'МЕГА победитель {current_player}')
            init_game()
            
        elif "" not in board:
            wins_all += 1
            draw += 1
            procent_X = round((x_wins / wins_all) * 100, 1)
            procent_O = round((o_wins / wins_all) * 100, 1)
            procent_X_label.config(text=f"Побед X: {procent_X}%")
            procent_O_label.config(text=f"Побед O: {procent_O}%")
            wins_all_label.config(text=f"Сыграно игр всего: {wins_all}")
            draw_label.config(text=f"Колл-во ничьей: {draw}")
            messagebox.showinfo('Ничья!', "Никто не победил")
            init_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            current_player_label.config(text=f"Текущий игрок: {current_player}")

def draw_symbol(row,col, symbol):
    x = col * cell_size + cell_size // 2
    y = row * cell_size + cell_size // 2
    w = cell_size * 0.36

    if symbol == "X":
        canvas.create_line(x-w,y-w,x+w,y+w,width=3,fill='blue')
        canvas.create_line(x+w,y-w,x-w,y+w,width=3,fill='blue')
    if symbol == "O":
        canvas.create_oval(x-w,y-w,x+w,y+w,width=3,outline='red')

def check_winner():
    win_post = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6),
    ]
    for pos in win_post:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != '':
            return True
    return False

root = Tk()
root.title('Крестики нолики')
score_frame = Frame(root,bg='#CFCFCF')
score_frame.pack()

board, current_player = None, None
canvas_size = 500
x_wins, o_wins = 0, 0
wins_needed = 3
mega_wins = 7
wins_all = 0
procent_X = 0
procent_O = 0
draw = 0
cell_size = canvas_size // 3
canvas = Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack(pady= 20)

current_player_label = Label(score_frame, text="Текущий игрок: X", width=20, bg='#CFCFCF')
x_score_label =  Label(score_frame, text="X побед: 0", width=15, bg='#CFCFCF')
o_score_label = Label(score_frame, text="O побед: 0", width=15, bg='#CFCFCF')
wins_needed_label = Label(score_frame, text=f"Нужно побед: {wins_needed}", width=15, bg='#CFCFCF')
wins_all_label = Label(score_frame, text=f"Сыграно игр всего: {wins_all}", width=20, bg='#CFCFCF')
procent_O_label = Label(score_frame, text=f"Процент Побед O: {procent_O}", width=15, bg='#CFCFCF')
procent_X_label = Label(score_frame, text=f"Процент Побед X: {procent_X}", width=15, bg='#CFCFCF')
draw_label = Label(score_frame, text=f"Колл-во ничьей: {draw}", width=15, bg='#CFCFCF')

current_player_label.grid(row=0, column=0, padx=5)
x_score_label.grid(row=0, column=1, padx=5)
o_score_label.grid(row=0, column=2, padx=5)
wins_needed_label.grid(row=0, column=3, padx=5)
procent_X_label.grid(row=1, column=0, padx=15)
procent_O_label.grid(row=1, column=1, padx=15)
wins_all_label.grid(row=1, column=2, padx=15)
draw_label.grid(row=1, column=3, padx=20)

canvas.bind("<Button-1>", on_click)

init_game()

root.mainloop()