#Задание 5.3

def print_board(board):
    print('-'*14)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*14)

def choice(name):
    valid = False
    while not valid:
        cell = input('Выберите ячейку ' + name + ' --> ')
        try:
            cell =int(cell)
        except:
            print('Ошибочный ввод')
            continue
        if cell >= 1 and cell <= 9:
            if(str(board[cell-1]) not in 'XO'):
                board[cell-1] = name
                valid = True
            else:
                print('Занято')
        else:
            print('Попробуй снова')

def victory(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

board = list(range(1,10))
counter = 0
while counter < 9:
    print_board(board)
    if counter % 2 == 0:
        choice('X')
    else:
        choice('0')
    counter +=1
    if counter > 4:
        win = victory(board)
        if win:
            print(win,'Победа')
            counter = 10
            break
    if counter == 9:
        print('Ничия!')
    print_board(board)
