# Level 1

## Task
Level 1 involves writing some code. I've written some boilerplate so that we can have some logic on the server.

Key bits are here,

```python
while True:
    client_conn, client_addr = server_socket.accept()
    data = client_conn.recv(1024).decode()
    print(data)
    response = 'Beep Boop!\n I am a server!\n'
    client_conn.sendall(response.encode())
    client_conn.close()
```

This is where we do stuff with the data. 

## How to get setup
Verify that you can make your server work by running it the code with `python main.py` and then connect using `nc` in the normal way.

## What are we going to do
HTTP is 'just text'. More specifically, it is a protocol about what the structure of messages should be over TCP. HTTP sets what the response to a request should be. We're going to start by returning a hello world HTTP request -- status code 200 with some messages
```
HTTP/1.0 200 OK
Hello World
```


