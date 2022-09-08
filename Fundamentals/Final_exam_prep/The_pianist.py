pieces = int(input())
playlist = {}
for each in range(pieces):
    info = input().split('|')

    current_piece = info[0]
    current_composer = info[1]
    current_key = info[2]
    playlist[current_piece] = current_composer,current_key
while True:
    command = input().split('|')

    if command[0] == 'Stop':
        for x,y in playlist.items():
            print(f"{x} -> Composer: {y[0]}, Key: {y[1]}")

    if command[0] == 'Add':
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in playlist.keys():
            playlist[piece] = composer,key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    if command[0] == 'Remove':
        piece_out = command[1]
        if piece_out in playlist.keys():
            playlist.pop(piece_out)
            print(f'Successfully removed {piece_out}!')
        else:
            print(f'Invalid operation! {piece_out} does not exist in the collection.')
    if command[0] == 'ChangeKey':
        old_piece = command[1]
        new_key = command[2]
        if old_piece in playlist:
            playlist[old_piece] = playlist[old_piece][0],new_key
            print(f'Changed the key of {old_piece} to {new_key}!')
        else:
            print(f'Invalid operation! {old_piece} does not exist in the collection.')
