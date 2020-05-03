import os
import chess

turn_id = 1

print('''\nWelcome to terminal chess!\n
Enter your moves using a type of algebraic notation
(piece you would like to move, it's location and where you would like to move it).
Example: Pe2-e4 moves the pawn on e2 to e4 or Ng1-f3 moves the knight on g1 to f3''')
while True:
    player = 'White' if turn_id % 2 != 0 else 'Black'
    try:
        print(chess.chess_board(player))
        player_move = input(f'\n{player}: ').lower()
        if player_move == 'help':
            print('''\nMove notation:
"Ex: Ke2-e4" moves king on e2 to e4\n
(P) for pawn, (R) for Rook, (N) for Knight, (B) for bishop, (Q) for Queen and (K) for king
"O-O" for king-side castling
"O-O-O" for queen-side castling
"=" to offer draw
"RESIGN" to resign from game''')
        elif player_move == 'resign':
            print(f'{player} resigned. {"Black" if player == "White" else "White"} is victorious.')
            break
        elif player_move == '=':
            while True:
                try:
                    draw_response = input(f'\n{player} offers you a draw. Do you accept? (Y)es or (N)o\n{"Black: " if player == "White" else "White: "}').lower()
                    assert draw_response == 'y' or draw_response == 'n'
                    break
                except: print('\nInvalid response. (Y) for yes you would like to accept the draw offer of (N) for no you would like to continue playing.')
            if draw_response == 'y':
                print("\nGame ends in a draw.")
                break
        elif player_move == 'o-o':
            assert chess.short_castle(player) == True
            chess.add_last_move(player, player_move)
            turn_id += 1
        elif player_move == 'o-o-o':
            assert chess.long_castle(player) == True
            chess.add_last_move(player, player_move)
            turn_id += 1
        else:
            # Maybe move this to chess module or remove entirely
            assert ((player_move[0] == 'r' or player_move[0] == 'n' or player_move[0] == 'b' or player_move[0] == 'q' or player_move[0] == 'k' or player_move[0] == 'p')
            and (player_move[1] == 'a' or player_move[1] == 'b' or player_move[1] == 'c' or player_move[1] == 'd' or player_move[1] == 'e' or player_move[1] == 'f' or player_move[1] == 'g' or player_move[1] == 'h')
            and int(player_move[2]) in range(1, 9)
            and player_move[3] == '-'
            and (player_move[4] == 'a' or player_move[4] == 'b' or player_move[4] == 'c' or player_move[4] == 'd' or player_move[4] == 'e' or player_move[4] == 'f' or player_move[4] == 'g' or player_move[4] == 'h')
            and int(player_move[5]) in range(1, 9)
            and chess.legal_move(player,player_move) == True)
            # os.system('cls' if os.name == 'nt' else 'clear')
            chess.add_last_move(player, player_move)
            turn_id += 1
    except: print('\nNot a legal move. Enter "HELP" for all types of moves')