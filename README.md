# Asynchronous/Synchronous Module
+ [Github Link](https://github.com/Rubier-Project/PCA)
+ [Telegram Channel](https://t.me/PikaApplication)

# WebSocket

### Asynchronous
```python
async def runner():
    ws = AsyncWebSocket("1f643dead3a310bb18aa64a7438ba72b")
    await ws.setServer("ws://127.0.0.1:3000/") # Seted localhost for Test
    data = await ws.connecttx()
    console.print(data)

asyncio.run(runner())
```

### Synchronous
```python
ws = WebSocket("1f643dead3a310bb18aa64a7438ba72b")
ws.setServer("ws://127.0.0.1:3000/") # Seted localhost for Test
data = ws.connecttx()
console.print(data)
```

# HTTP(s)

### Asynchronous
```python
async def runner():
    http = AsyncHttp("1f643dead3a310bb18aa64a7438ba72b")
    await http.setServer("http://127.0.0.1:3000/") # Seted localhost for Test
    data = await http.getUserByMentorID("UMfb6f1ff72611d76f4cc0db7ced1b7f")
    console.print(data)

asyncio.run(runner())
```

### Synchronous
```python
http = Http("1f643dead3a310bb18aa64a7438ba72b")
http.setServer("http://127.0.0.1:3000/") # Seted localhost for Test
data = http.getMe()
console.print(data)
```
