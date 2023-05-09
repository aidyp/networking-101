# Level 0


## Task
Level 0 involves writing no code, but we have to learn a little about TCP first. There is a lot more to TCP, but put simply, it lets you send arbitrary data to a server that is all contained in one logical connection

## Make a hot cup of TCP
There is a nice tool called `netcat`. You can install it with

```
brew install netcat
```

Then start a TCP server in one terminal window with
```
nc -l 50000
```

Connect to it in another terminal window 
```
nc 127.0.0.1 50000
```

And then send some data through the connection!