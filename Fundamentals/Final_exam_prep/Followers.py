facebook = {}

while True:

    command = input().split(':')

    if command[0] == 'Log out':
        print(f"{len(facebook.keys())} followers")
        for follower in facebook:
            print(f"{follower}: {facebook[follower]['likes'] + facebook[follower]['comments']}")
        break

    username = command[1]

    if command[0] == 'New follower':
        if username not in facebook:
            facebook[username] = {'likes': 0 ,'comments': 0}

    if command[0] == 'Like':
        count = int(command[2])
        if username not in facebook:
            facebook[username] = {'likes': count ,'comments': 0}
        else:
            facebook[username]['likes'] += count
    if command[0] == 'Comment':
        if username not in facebook:
            facebook[username] = {'likes': 0 ,'comments': 1}
        else:
            facebook[username]['comments'] += 1
    if command[0] == 'Blocked':
        if username in facebook:
            facebook.pop(username)
        else:
            print(f"{username} doesn't exist.")


