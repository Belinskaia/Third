def connect_user(auth_data):
    with open(auth_data, 'w', encoding='UTF-8') as folder:
        coroutine = write_to_file(folder)
        yield from coroutine

def write_to_file(f_obj):
    text = yield
    while True:
        f_obj.write(text)
        text = yield

def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"

def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

def main():
    users = []
    user_work = []
    for i in connection():
        information = i.split()
        if 'disconnect' in i:
            user_work[users.index(information[1])].close()
            user_work.pop(users.index(information[1]))
            users.remove(information[1])
        if 'auth' in i:
            users.append(information[1])
            user_work.append(connect_user(information[1]))
            next(user_work[users.index(information[1])])
        else:
            if information[0] in users:
                user_work[users.index(information[0])].send(information[1])

if __name__ == '__main__':
    main()
    
'''
for i in connection(): 
    print(i)
    '''
