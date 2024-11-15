from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from rich.console import Console
from rich.traceback import install
import websockets
import asyncio
import httpx
import requests
import random
import base64

from typing import (
    Optional,
    Union
)

import websockets.sync
import websockets.sync.client

from objext import (
    User,
    Group,
    Channel,
    Bot,
    Message,
    Media,
    UserSettings,
    GroupSettings,
    ChannelSettings,
    json,

    user_points,
    user_statuses
)

console = Console()
asynchttp = httpx.AsyncClient()
install()

class Encryption(object):
    def __init__(self):
        self.iv = bytes.fromhex("0"*32)
    
    def encrypt(self, text: str, key: str) -> dict:
        try:
            cipher = AES.new(key.encode(), AES.MODE_CBC, self.iv)
            data_pad = pad(text.encode(), AES.block_size)
            return {"enc": base64.b64encode(cipher.encrypt(data_pad)).decode(), "error": False}
        except Exception as er:
            return {"enc": str(er), "error": True}

    def decrypt(self, encoded_text: str, key: str) -> dict:
        try:
            decipher = AES.new(key.encode(), AES.MODE_CBC, self.iv)
            decoded_data = base64.b64decode(encoded_text)
            data_unpad = unpad(decipher.decrypt(decoded_data), AES.block_size)
            return {"dec": data_unpad.decode(), "error": False}
        except Exception as er:
            return {"dec": str(er), "error": True}
        
    def mediaEncrypt(self, data: Optional[Union[bytes, str]]) -> str:
        if isinstance(data, bytes):
            data = data.decode()

        return base64.b64encode(data.encode()).decode()
    
    def mediaDecrypt(self, data: Optional[Union[bytes, str]]) -> str:
        if isinstance(data, bytes):
            data = data.decode()

        return base64.b64decode(data.encode()).decode()

class AsyncEncryption(object):
    def __init__(self):
        self.iv = bytes.fromhex("0"*32)
    
    async def encrypt(self, text: str, key: str) -> dict:
        try:
            cipher = AES.new(key.encode(), AES.MODE_CBC, self.iv)
            data_pad = pad(text.encode(), AES.block_size)
            return {"enc": base64.b64encode(cipher.encrypt(data_pad)).decode(), "error": False}
        except Exception as er:
            return {"enc": str(er), "error": True}

    async def decrypt(self, encoded_text: str, key: str) -> dict:
        try:
            decipher = AES.new(key.encode(), AES.MODE_CBC, self.iv)
            decoded_data = base64.b64decode(encoded_text)
            data_unpad = unpad(decipher.decrypt(decoded_data), AES.block_size)
            return {"dec": data_unpad.decode(), "error": False}
        except Exception as er:
            return {"dec": str(er), "error": True}
        
    async def mediaEncrypt(self, data: Optional[Union[bytes, str]]) -> str:
        if isinstance(data, bytes):
            data = data.decode()

        return base64.b64encode(data.encode()).decode()
    
    async def mediaDecrypt(self, data: Optional[Union[bytes, str]]) -> str:
        if isinstance(data, bytes):
            data = data.decode()

        return base64.b64decode(data.encode()).decode()

class Random(object):
    def __init__(self):pass

    def select(self, options: Optional[Union[list, set]]):
        if isinstance(options, set):options = list(options)

        return random.choice(options)

class AsyncRandom(object):
    def __init__(self):pass

    async def select(self, options: Optional[Union[list, set]]) -> str:
        if isinstance(options, set):options = list(options)

        return random.choice(options)

class WebSocket(object):
    def __init__(self, AuthToken: str, randomSelect: bool = True):
        self.auth_token: str = AuthToken
        self.socket_servers = set(  )
        self.rnd = Random()
        self.random_select = randomSelect

    def review(self):
        if len(self.socket_servers) == 0:
            raise ValueError("Socket Servers Must not be empty - Select servers with `setServer` Method")

    def setServer(self, server: str) -> None:
        if server.endswith("/"):self.socket_servers.add(server)
        else:self.socket_servers.add(server+"/")

    def getServers(self) -> set:
        return self.socket_servers
    
    def disconnecttx(self) -> dict:
        self.review()

        js_data = { "auth_token": self.auth_token }
        js_data = json.dumps(js_data, ensure_ascii=False)

        if self.random_select:
            server: str = self.rnd.select(self.getServers())

            with websockets.sync.client.connect(server+"disconnecttx") as wss:
                wss.send(js_data)
                msg = wss.recv()
                return json.loads(msg)
            
        else:
            server = list(self.getServers())[0]

            with websockets.sync.client.connect(server+"disconnecttx") as wss:
                wss.send(js_data)
                msg = wss.recv()
                return json.loads(msg)
            
    def connecttx(self) -> dict:
        self.review()

        js_data = { "auth_token": self.auth_token }
        js_data = json.dumps(js_data, ensure_ascii=False)

        if self.random_select:
            server: str = self.rnd.select(self.getServers())

            with websockets.sync.client.connect(server+"connecttx") as wss:
                wss.send(js_data)
                msg = wss.recv()
                return json.loads(msg)
            
        else:
            server = list(self.getServers())[0]

            with websockets.sync.client.connect(server+"connecttx") as wss:
                wss.send(js_data)
                msg = wss.recv()
                return json.loads(msg)
            
    def setCustomStatus(self, status: user_statuses) -> dict:
        self.review()

        js_data = { "auth_token": self.auth_token, "status": status }
        js_data = json.dumps(js_data, ensure_ascii=False)

        if self.random_select:
            server: str = self.rnd.select(self.getServers())

            with websockets.sync.client.connect(server+"setCustomStatus") as wss:
                wss.send(js_data)
                msg = wss.recv()
                return json.loads(msg)
            
        else:
            server = list(self.getServers())[0]

            with websockets.sync.client.connect(server+"setCustomStatus") as wss:
                wss.send(js_data)
                msg = wss.recv()
                return json.loads(msg)
            
class AsyncWebSocket(object):
    def __init__(self, AuthToken: str, randomSelect: bool = True):
        self.auth_token: str = AuthToken
        self.socket_servers = set(  )
        self.rnd = AsyncRandom()
        self.random_select = randomSelect

    def review(self):
        if len(self.socket_servers) == 0:
            raise ValueError("Socket Servers Must not be empty - Select servers with `setServer` Method")

    async def setServer(self, server: str) -> None:
        if server.endswith("/"):self.socket_servers.add(server)
        else:self.socket_servers.add(server+"/")

    async def getServers(self) -> set:
        return self.socket_servers
    
    async def disconnecttx(self) -> dict:
        self.review()

        js_data = { "auth_token": self.auth_token }
        js_data = json.dumps(js_data, ensure_ascii=False)
        servers = await self.getServers()

        if self.random_select:
            server: str = await self.rnd.select(servers)

            async with websockets.connect(server+"disconnecttx") as ws:
                await ws.send(js_data)
                msg = await ws.recv()
                return json.loads(msg)
            
        else:
            server = list(servers)[0]

            async with websockets.connect(server+"disconnecttx") as ws:
                await ws.send(js_data)
                msg = await ws.recv()
                return json.loads(msg)
            
    async def connecttx(self) -> dict:
        self.review()

        js_data = { "auth_token": self.auth_token }
        js_data = json.dumps(js_data, ensure_ascii=False)
        servers = await self.getServers()

        if self.random_select:
            server: str = await self.rnd.select(servers)

            async with websockets.connect(server+"connecttx") as ws:
                await ws.send(js_data)
                msg = await ws.recv()
                return json.loads(msg)
            
        else:
            server = list(servers)[0]

            async with websockets.connect(server+"connecttx") as ws:
                await ws.send(js_data)
                msg = await ws.recv()
                return json.loads(msg)
            
    async def setCustomStatus(self, status: user_statuses) -> dict:
        self.review()

        js_data = { "auth_token": self.auth_token, "status": status }
        js_data = json.dumps(js_data, ensure_ascii=False)
        servers = await self.getServers()

        if self.random_select:
            server: str = await self.rnd.select(servers)

            async with websockets.connect(server+"setCustomStatus") as ws:
                await ws.send(js_data)
                msg = await ws.recv()
                return json.loads(msg)
            
        else:
            server = list(servers)[0]

            async with websockets.connect(server+"setCustomStatus") as ws:
                await ws.send(js_data)
                msg = await ws.recv()
                return json.loads(msg)
            
class Http(object):
    def __init__(self, AuthToken: str, random_select: bool = True):
        self.auth_token: str = AuthToken
        self.servers = set(  )
        self.rnd = Random()
        self.enc = Encryption()
        self.random_select = random_select

    def review(self):
        if len(self.servers) == 0:
            raise ValueError("Servers Must not be empty - Select servers with `setServer` Method")

    def setServer(self, server: str) -> None:
        if server.endswith("/"):self.servers.add(server)
        else:self.servers.add(server+"/")

    def getServers(self) -> set:
        return self.servers
    
    def getMe(self) -> User:
        self.review()

        js_data = { "auth_token": self.auth_token }
        js_data = self.enc.encrypt(json.dumps(js_data, ensure_ascii=False), self.auth_token)

        if js_data['error'] == True:
            raise ValueError(js_data['enc'])
        
        js_data = { "enc_data": js_data['enc'], "powkey": self.auth_token }

        if self.random_select:
            server = self.rnd.select(self.getServers())
            try:
                __data__ = requests.post(server+"getMe", json=js_data).json()
                __u__ = self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(__u__)
            except requests.ConnectionError: raise requests.ConnectionError("Please Check your Internet and Try again ...")

        else:
            server = list(self.getServers())[0]
            try:
                __data__ = User(requests.post(server+"getMe", json=js_data).json())
                __u__ = self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(__u__)
            except requests.ConnectionError: raise requests.ConnectionError("Please Check your Internet and Try again ...")

    def getUserByMentorID(self, mentor_id: str) -> User:
        self.review()

        js_data = { "auth_token": self.auth_token, "mentor_id": mentor_id }
        js_data = self.enc.encrypt(json.dumps(js_data, ensure_ascii=False), self.auth_token)

        if js_data['error'] == True:
            raise ValueError(js_data['enc'])
        
        js_data = { "enc_data": js_data['enc'], "powkey": self.auth_token }

        if self.random_select:
            server = self.rnd.select(self.getServers())
            try:
                __data__ = requests.post(server+"getUserByMentorID", json=js_data).json()
                __u__ = self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(__u__)
            except requests.ConnectionError: raise requests.ConnectionError("Please Check your Internet and Try again ...")

        else:
            server = list(self.getServers())[0]
            try:
                __data__ = requests.post(server+"getUserByMentorID", json=js_data).json()
                __u__ = self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(__u__)
            except requests.ConnectionError: raise requests.ConnectionError("Please Check your Internet and Try again ...")

class AsyncHttp(object):
    def __init__(self, AuthToken: str, random_select: bool = True):
        self.auth_token: str = AuthToken
        self.servers = set(  )
        self.rnd = AsyncRandom()
        self.enc = AsyncEncryption()
        self.random_select = random_select

    def review(self):
        if len(self.servers) == 0:
            raise ValueError("Servers Must not be empty - Select servers with `setServer` Method")

    async def setServer(self, server: str) -> None:
        if server.endswith("/"):self.servers.add(server)
        else:self.servers.add(server+"/")

    async def getServers(self) -> set:
        return self.servers
    
    async def getMe(self) -> User:
        self.review()

        js_data = { "auth_token": self.auth_token }
        js_data = await self.enc.encrypt(json.dumps(js_data, ensure_ascii=False), self.auth_token)

        if js_data['error'] == True:
            raise ValueError(js_data['enc'])
        
        js_data = { "enc_data": js_data['enc'], "powkey": self.auth_token }
        servers = await self.getServers()

        if self.random_select:
            server = await self.rnd.select(servers)
            try:
                __data__ = await asynchttp.post(server+"getMe", json=js_data)
                __data__ = __data__.json()
                __u__ = await self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(json.loads(__u__['dec']), char='user')
            except httpx.ConnectError: raise httpx.ConnectError("Please Check your Internet and Try again ...")

        else:
            server = list(servers)[0]
            try:
                __data__ = await asynchttp.post(server+"getMe", json=js_data)
                __data__ = __data__.json()
                __u__ = await self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(json.loads(__u__['dec']), char='user')
            except requests.ConnectionError: raise requests.ConnectionError("Please Check your Internet and Try again ...")

    async def getUserByMentorID(self, mentor_id: str) -> User:
        self.review()

        js_data = { "auth_token": self.auth_token, "mentor_id": mentor_id }
        js_data = await self.enc.encrypt(json.dumps(js_data, ensure_ascii=False), self.auth_token)

        if js_data['error'] == True:
            raise ValueError(js_data['enc'])
        
        js_data = { "enc_data": js_data['enc'], "powkey": self.auth_token }
        servers = await self.getServers()

        if self.random_select:
            server = await self.rnd.select(servers)
            try:
                __data__ = await asynchttp.post(server+"getUserByMentorID", json=js_data)
                __data__ = __data__.json()
                __u__ = await self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(json.loads(__u__['dec']), char='user')
            except httpx.ConnectError: raise httpx.ConnectError("Please Check your Internet and Try again ...")

        else:
            server = list(servers)[0]
            try:
                __data__ = await asynchttp.post(server+"getUserByMentorID", json=js_data)
                __data__ = __data__.json()
                __u__ = await self.enc.decrypt(__data__['enc_data'], __data__['powkey'])
                return User(json.loads(__u__['dec']), char='user')
            except httpx.ConnectError: raise httpx.ConnectError("Please Check your Internet and Try again ...")

# TEST

# async def runner():
#     http = AsyncHttp("1f643dead3a310bb18aa64a7438ba72b")
#     await http.setServer("http://127.0.0.1:3000/")
#     data = await http.getUserByMentorID("UMfb6f1ff72611d76f4cc0db7ced1b7f")
#     #console.print(data)
#     return data

# data = asyncio.run(runner())
# console.print(data.settings.hide_phone_number)

# async def runner():
#     ws = AsyncWebSocket("1f643dead3a310bb18aa64a7438ba72b")
#     await ws.setServer("ws://127.0.0.1:3000/")
#     data = await ws.connecttx()
#     console.print(data)
#     return data

# data = asyncio.run(runner())
# console.print(json.loads(Encryption().decrypt(data['enc_data'], data['powkey'])['dec']))
