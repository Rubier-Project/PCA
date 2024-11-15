from typing import ( Literal, Union, Optional, List )
import json

user_points = Literal[
    'admin', 'dev', 'popular', 'artist'
]

user_statuses = Literal[
    'online', 'offline', 'Wont Back', 'I Love U', 'See Me'
]

message_types = Literal[
    'text', 'photo', 'file', 'video', 'gif'
]

mentors = Literal[
    'user', 'group', 'channel','bot',
    'photo', 'video', 'gif', 'music', 'file'
]

status_types = Literal[
    'OK',

    'INDEX_ERROR', 'DOESNT_OWN_MESSAGE', 'DOESNT_OWN_PACK', 'IRRESPONSIBLE', 'DONT_ALLOW', 'NOT_EDITABLE', 'NOT_MEMBER', 'NOT_PREMIUM',
    'NOT_ADMIN', 'REMOVED_USER', 'REMOVED_BOT', 'CANNOT_REMOVE_OWNER', 'NOT_IN_REMOVEDS_USERS', 'SUSED_GROUP', 'SUSED_CHANNEL',

    'EXISTS_USERNAME', 'EXISTS_PHONE_NUMBER', 'EXISTS_GROUP_ID', 'EXISTS_CHANNEL_ID', 'DIDNT_ENDSWITH_BOT', 'SUSED_USER',

    'INVALID_MENTOR_ID', 'INVALID_USERNAME', 'INVALID_MESSAGE_ID', 'INVALID_AUTH_TOKEN', 'INVALID_MESSAGE_TYPE', 'INVALID_ENC',
    'INVALID_KEYS_LENGTH', 'INVALID_ID', 'INVALID_MEDIA_ID', 'INVALID_DATA_TYPE', 'INVALID_PACK_NAME', 'INVALID_DURATION', 'INVALID_STATUS', 'INVALID_TITLE_LENGTH', 'INVALID_BIO_LENGTH', 'INVALID_FULLNAME_LENGTH',

    'UNCOVERD_MENTORED_ID', 'UNCOVERD_MENTORING_ID', 'UNCOVERD_TEXT', 'UNCOVERD_TEXT_LENGTH',
    'UNCOVERD_MESSAGE_ID', 'UNCOVERD_MESSAGE_TIME', 'UNCOVERD_REPLY_DATA', 'UNCOVERD_IS_SEEN', 'UNCOVERD_IS_EDIT', 'UNCOVERD_PACK_NAME', 'UNCOVERD_GIF_INDEX',
    'UNCOVERD_MEDIA_ID', 'UNCOVERD_HEIGHT', 'UNCOVERD_WIDTH', 'UNCOVERD_SIZE', 'UNCOVERD_FILENAME', 'UNCOVERD_FORMAT', 'UNCOVERD_ENC_BYTES', 'UNCOVERD_DURATION'
]

class UserSettings(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ]):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)

        self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
        self.hide_phone_number: Optional[Union[str, bool]] = self.__result__.get("hide_phone_number", "null")
        self.can_join_groups: Optional[Union[str, bool]] = self.__result__.get("can_join_groups", "null")
        self.can_join_channels: Optional[Union[str, bool]] = self.__result__.get("can_join_channels", "null")
        self.inner_gif: str = self.__result__.get("inner_gif", "null")
        self.inner_music: str = self.__result__.get("inner_music", "null")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
class GroupSettings(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ]):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)

        self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
        self.show_members: Optional[Union[str, bool]] = self.__result__.get("show_members", "null")
        self.show_admins: Optional[Union[str, bool]] = self.__result__.get("show_admins", "null")
        self.show_owner: Optional[Union[str, bool]] = self.__result__.get("show_owner", "null")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
class ChannelSettings(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ]):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)

        self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
        self.show_members: Optional[Union[str, bool]] = self.__result__.get("show_members", "null")
        self.show_admins: Optional[Union[str, bool]] = self.__result__.get("show_admins", "null")
        self.show_owner: Optional[Union[str, bool]] = self.__result__.get("show_owner", "null")
        
    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)

class User(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if isinstance(abstracted, dict) or isinstance(abstracted, list) else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            if isinstance(abstracted, dict):
                self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
                self.fullname: str = self.__result__.get("fullname", "null")
                self.username: str = self.__result__.get("username", "null")
                self.bio: str = self.__result__.get("bio", "null")
                self.phone_number: str = self.__result__.get("phone_number", "null")
                self.auth_token: str = self.__result__.get("auth_token", "null")
                self.mentor_id: str = self.__result__.get("mentor_id", "null")
                self.settings: UserSettings = UserSettings(self.__result__.get("settings", {}))
                self.profile_encoded_bytes: str = self.__result__.get("profile_encoded_bytes", "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")
                self.stories: Optional[Union[List[List[Media, dict]]]] = self.__result__.get("stories", {})
                self.point: Optional[Union[str, list[user_points]]] = self.__result__.get("point", "null")
                self.is_suspesion: Optional[Union[str, bool]] = self.__result__.get("is_suspesion", "null")
                self.is_premium: Optional[Union[str, bool]] = self.__result__.get("is_premium", "null")
                self.user_status: user_statuses = self.__result__.get("status", "null")
                self.background_hex: str = self.__result__.get("background_hex", "#000000")
                self.packs: list[str] = self.__result__.get("packs", [])

            elif isinstance(abstracted, list):
                self.__result__: list[User] = [User({})] if len(abstracted) == 0 else abstracted

                self.status: status_types = self.__result__[0].status
                self.fullname: str = self.__result__[0].fullname
                self.username: str = self.__result__[0].username
                self.bio: str = self.__result__[0].bio
                self.phone_number: str = self.__result__[0].phone_number
                self.auth_token: str = self.__result__[0].auth_token
                self.mentor_id: str = self.__result__[0].mentor_id
                self.settings: UserSettings = self.__result__[0].settings
                self.profile_encoded_bytes: str = self.__result__[0].profile_encoded_bytes
                self.point: Optional[Union[str, list[user_points]]] = self.__result__[0].point
                self.stories: Optional[Union[List[List[Media, dict]]]] = self.__result__[0].stories
                self.is_suspesion: Optional[Union[str, bool]] = self.__result__[0].is_suspesion
                self.is_premium: Optional[Union[str, bool]] = self.__result__[0].is_premium
                self.user_status: user_statuses = self.__result__[0].user_status
                self.background_hex: str = self.__result__[0].background_hex
                self.packs: list[str] = self.__result__[0].packs

        else:

            if isinstance(abstracted, dict):
                self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
                self.fullname: str = self.__result__.get(char.get("char")).get("fullname", "null")
                self.username: str = self.__result__.get(char.get("char")).get("username", "null")
                self.bio: str = self.__result__.get(char.get("char")).get("bio", "null")
                self.phone_number: str = self.__result__.get(char.get("char")).get("phone_number", "null")
                self.auth_token: str = self.__result__.get(char.get("char")).get("auth_token", "null")
                self.mentor_id: str = self.__result__.get(char.get("char")).get("mentor_id", "null")
                self.settings: UserSettings = UserSettings(self.__result__.get(char.get("char")).get("settings", {}))
                self.profile_encoded_bytes: str = self.__result__.get(char.get("char")).get("profile_encoded_bytes", "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")
                self.stories: Optional[Union[List[List[Media, dict]]]] = self.__result__.get(char.get("char")).get("stories", {})
                self.point: Optional[Union[str, list[user_points]]] = self.__result__.get(char.get("char")).get("point", "null")
                self.is_suspesion: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_suspesion", "null")
                self.is_premium: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_premium", "null")
                self.user_status: user_statuses = self.__result__.get(char.get("char")).get("status", "null")
                self.background_hex: str = self.__result__.get(char.get("char")).get("background_hex", "#000000")
                self.packs: list[str] = self.__result__.get(char.get("char")).get("packs", [])

            elif isinstance(abstracted, list):
                self.__result__: list[User] = [User({})] if len(abstracted) == 0 else abstracted

                self.status: status_types = self.__result__[0].status
                self.fullname: str = self.__result__[0].fullname
                self.username: str = self.__result__[0].username
                self.bio: str = self.__result__[0].bio
                self.phone_number: str = self.__result__[0].phone_number
                self.auth_token: str = self.__result__[0].auth_token
                self.mentor_id: str = self.__result__[0].mentor_id
                self.settings: UserSettings = self.__result__[0].settings
                self.profile_encoded_bytes: str = self.__result__[0].profile_encoded_bytes
                self.stories: Optional[Union[List[List[Media, dict]]]] = self.__result__[0].stories
                self.point: Optional[Union[str, list[user_points]]] = self.__result__[0].point
                self.is_suspesion: Optional[Union[str, bool]] = self.__result__[0].is_suspesion
                self.is_premium: Optional[Union[str, bool]] = self.__result__[0].is_premium
                self.user_status: user_statuses = self.__result__[0].user_status
                self.background_hex: str = self.__result__[0].background_hex
                self.packs: list[str] = self.__result__[0].packs

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
class Bot(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if isinstance(abstracted, dict) else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.fullname: str = self.__result__.get("fullname", "null")
            self.bot_id: str = self.__result__.get("bot_id", "null")
            self.bio: str = self.__result__.get("bio", "null")
            self.bot_mentor_id: str = self.__result__.get("bot_mentor_id", "null")
            self.bot_token: str = self.__result__.get("bot_token", "null")
            self.point: Optional[Union[List[user_points]]] = self.__result__.get("point", [])
            self.created_in: str = self.__result__.get("created_in", "")
            self.background_hex: str = self.__result__.get("background_hex", "#000000")
            self.is_suspension: Optional[Union[str, bool]] = self.__result__.get("is_suspension", "null")
            self.profile_encoded_bytes: str = self.__result__.get("profile_encoded_bytes", "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAAXNSR0IArs4c6QAABOtJREFUeF7tnG1S4zAMhu3ABXaAQv+VkyycZOEkwElgTwKcZPOvUOhwARrvJC1fpa0lvXKdBDGzM/vDkuP3iSz5I/XO/rIq4LP2bp07A5D5JTAABiCzApm7twgwAJkVyNy9RYAByKxA5u4tAgxAZgUyd28R8BMBjMcvI1dUf+qxex9O5hr4kXOu/pf6r5x3EErvfPP/yoX74WD/JnXHq/xvLQLeRJ8L7hei5xjy2j4bGCG4G1cVf4fDXwtQaZ8xOYAP4d1l2qGoei+3BSIZgI4Kv0yxATE83LtSxfvJWRIAtfh+Z3bd0qlGomUZZsVpimlJHcD46enEh+JWMsqW25TBhSvtZK0KYDx5PvPOX7dcSOTx1KckNQA/QPx3cCG4S628oAJAOO2UdS0egr9zRXXvXnfLFHPs8uveFAf13+7ryAU/Kpz/HZw7Y4ZFGXx1Pjw4uGPafWsOA5gn3Oof40HUw5jR98qmDZSd2Yl3/oKxGFRJzDCAh8nzLbXa0QxdVPRV9oLSuTwa7B0jzwIBGD9OL7wnLbDUQhYZLNV2EdV1JRfdGvHO3RwO9s6pvpfbQQAeJtNA6FglVAn9qDZhQIDGJwbwOJleE5IX9HCqigqcUSEgUSAGQHn7g69ONSoFgXZqJsQiQzzFigBQav62J1wOoZTjFQEgVD5wdcARKHVb2lQU7o4G+6fcZxEC2Jx8gwvn2nsm3IFptydEgeilYwMgPIg7Guyx/WoLpu2PkgskOY8tVKz6QSoCbdG0/cWmXsnY1QFwp58VR5XNHlF9XlvNiit0f0jTfzz6+XmADSD2FnDCkLCShvaNtP3HNx23AmBab7ytXaKHWXFMeWtjIL9OH/yBpfBPyAPsRCyIgM0VECUBx0P5++zNWVek8t8LAIRBrMudpNVmav+xHQDKC/h5gFuPAMK8vLZ4oURBav+dBxArYzeXjvFckNp/5wE8TDYn8UjtHk1yW/C/cQu+9VMQKFB0lb0F/10HQD/CXHF6FD194pWfX3ugrGQ7PwWlTpKp/XcfAP8WxftrSlllA2Woo/jvPIBaTdFCibHFndJ/LwDUEHjlYrz8XM4Xqfz3BkATCYRrLZTF17rSNYX/XgFoIIxfRsVOdRFcGC0ueH1cWVT4UkXbf+8AaB+apPZnAFIrHPFvAAwAfh6QWUOoe4sASD7c2ADgGkIeDAAkH25sAHANIQ8GAJIPNzYAuIaQBwMAyYcbGwBcQ8hD7wBk+Bkb6O5prwBQtouh1zVuzL572hsAyOF5XFduC/qBTy8ASI4MuZJy21MPfjoPADk054rKbE+6e9p9AIRjSKZwas0pUdB5ALzDcjVtiY7iuaDzANCrg0Qlpc0od0+7fjURO9BB38Dc9stvxta/D8gtQO7+DUDkF15i18tRgAbAAFgO+BwFlgOW5gSbgiK/M4HOwbntLQf0IAds/FJeugLqi11sClOIAPk3Xn0Red04KN+YwQBacIjSWo6UzTwcAPCNV2uVU3owyjdmMIDaQRsPVJQ0FLvh/k7SW0fsdcCbYbu3lcU6Cg3j29gb8oawT+I3XnLv3bCUzPvQSnhZlhXfYHVDOflTqn7DJp6C5M9vlqoRYHJiClgEYPrB1gYAlhBzYAAw/WBrAwBLiDkwAJh+sLUBgCXEHBgATD/Y2gDAEmIODACmH2xtAGAJMQf/ARnPQ53+buaeAAAAAElFTkSuQmCC")
            
        else:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.fullname: str = self.__result__.get(char.get("char")).get("fullname", "null")
            self.bot_id: str = self.__result__.get(char.get("char")).get("bot_id", "null")
            self.bio: str = self.__result__.get(char.get("char")).get("bio", "null")
            self.bot_mentor_id: str = self.__result__.get(char.get("char")).get("bot_mentor_id", "null")
            self.bot_token: str = self.__result__.get(char.get("char")).get("bot_token", "null")
            self.point: Optional[Union[List[user_points]]] = self.__result__.get(char.get("char")).get("point", [])
            self.created_in: str = self.__result__.get(char.get("char")).get("created_in", "")
            self.background_hex: str = self.__result__.get(char.get("char")).get("background_hex", "#000000")
            self.is_suspension: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_suspension", "null")
            self.profile_encoded_bytes: str = self.__result__.get(char.get("char")).get("profile_encoded_bytes", "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAAXNSR0IArs4c6QAABOtJREFUeF7tnG1S4zAMhu3ABXaAQv+VkyycZOEkwElgTwKcZPOvUOhwARrvJC1fpa0lvXKdBDGzM/vDkuP3iSz5I/XO/rIq4LP2bp07A5D5JTAABiCzApm7twgwAJkVyNy9RYAByKxA5u4tAgxAZgUyd28R8BMBjMcvI1dUf+qxex9O5hr4kXOu/pf6r5x3EErvfPP/yoX74WD/JnXHq/xvLQLeRJ8L7hei5xjy2j4bGCG4G1cVf4fDXwtQaZ8xOYAP4d1l2qGoei+3BSIZgI4Kv0yxATE83LtSxfvJWRIAtfh+Z3bd0qlGomUZZsVpimlJHcD46enEh+JWMsqW25TBhSvtZK0KYDx5PvPOX7dcSOTx1KckNQA/QPx3cCG4S628oAJAOO2UdS0egr9zRXXvXnfLFHPs8uveFAf13+7ryAU/Kpz/HZw7Y4ZFGXx1Pjw4uGPafWsOA5gn3Oof40HUw5jR98qmDZSd2Yl3/oKxGFRJzDCAh8nzLbXa0QxdVPRV9oLSuTwa7B0jzwIBGD9OL7wnLbDUQhYZLNV2EdV1JRfdGvHO3RwO9s6pvpfbQQAeJtNA6FglVAn9qDZhQIDGJwbwOJleE5IX9HCqigqcUSEgUSAGQHn7g69ONSoFgXZqJsQiQzzFigBQav62J1wOoZTjFQEgVD5wdcARKHVb2lQU7o4G+6fcZxEC2Jx8gwvn2nsm3IFptydEgeilYwMgPIg7Guyx/WoLpu2PkgskOY8tVKz6QSoCbdG0/cWmXsnY1QFwp58VR5XNHlF9XlvNiit0f0jTfzz6+XmADSD2FnDCkLCShvaNtP3HNx23AmBab7ytXaKHWXFMeWtjIL9OH/yBpfBPyAPsRCyIgM0VECUBx0P5++zNWVek8t8LAIRBrMudpNVmav+xHQDKC/h5gFuPAMK8vLZ4oURBav+dBxArYzeXjvFckNp/5wE8TDYn8UjtHk1yW/C/cQu+9VMQKFB0lb0F/10HQD/CXHF6FD194pWfX3ugrGQ7PwWlTpKp/XcfAP8WxftrSlllA2Woo/jvPIBaTdFCibHFndJ/LwDUEHjlYrz8XM4Xqfz3BkATCYRrLZTF17rSNYX/XgFoIIxfRsVOdRFcGC0ueH1cWVT4UkXbf+8AaB+apPZnAFIrHPFvAAwAfh6QWUOoe4sASD7c2ADgGkIeDAAkH25sAHANIQ8GAJIPNzYAuIaQBwMAyYcbGwBcQ8hD7wBk+Bkb6O5prwBQtouh1zVuzL572hsAyOF5XFduC/qBTy8ASI4MuZJy21MPfjoPADk054rKbE+6e9p9AIRjSKZwas0pUdB5ALzDcjVtiY7iuaDzANCrg0Qlpc0od0+7fjURO9BB38Dc9stvxta/D8gtQO7+DUDkF15i18tRgAbAAFgO+BwFlgOW5gSbgiK/M4HOwbntLQf0IAds/FJeugLqi11sClOIAPk3Xn0Red04KN+YwQBacIjSWo6UzTwcAPCNV2uVU3owyjdmMIDaQRsPVJQ0FLvh/k7SW0fsdcCbYbu3lcU6Cg3j29gb8oawT+I3XnLv3bCUzPvQSnhZlhXfYHVDOflTqn7DJp6C5M9vlqoRYHJiClgEYPrB1gYAlhBzYAAw/WBrAwBLiDkwAJh+sLUBgCXEHBgATD/Y2gDAEmIODACmH2xtAGAJMQf/ARnPQ53+buaeAAAAAElFTkSuQmCC")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)

class Message(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.text: str = self.__result__.get("text", "")
            self.text_length: int = self.__result__.get("text_length", 0)
            self.message_time: str = self.__result__.get("message_time", "null")
            self.message_id: str = self.__result__.get("message_id", "null")
            self.type: message_types = self.__result__.get("type", "text")
            self.mentored_id: str = self.__result__.get("mentored_id", "null")
            self.mentoring_id: str = self.__result__.get("mentoring_id", "null")
            self.mentored_photo: str = self.__result__.get("mentored_photo", "null")
            self.mentoring_photo: str = self.__result__.get("mentoring_photo", "null")
            self.mentored_inner_gif: str = self.__result__.get("mentored_inner_gif", "null")
            self.mentoring_inner_gif: str = self.__result__.get("mentoring_inner_gif", "null")
            self.media: Optional[Union[str, Media]] = self.__result__.get("media", "null")
            self.glassify_buttons: Optional[Union[List[str]]] = self.__result__.get("glassify_buttons", [])
            self.is_seen: Optional[Union[str, bool]] = self.__result__.get("is_seen", "null")
            self.is_edit: Optional[Union[str, bool]] = self.__result__.get("is_edit", "null")
            self.reply_data: Optional[Union[dict, Message]] = self.__result__.get("reply_data", {})

        else:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.text: str = self.__result__.get(char.get("char")).get("text", "")
            self.text_length: int = self.__result__.get(char.get("char")).get("text_length", 0)
            self.message_time: str = self.__result__.get(char.get("char")).get("message_time", "null")
            self.message_id: str = self.__result__.get(char.get("char")).get("message_id", "null")
            self.type: message_types = self.__result__.get(char.get("char")).get("type", "text")
            self.mentored_id: str = self.__result__.get(char.get("char")).get("mentored_id", "null")
            self.mentoring_id: str = self.__result__.get(char.get("char")).get("mentoring_id", "null")
            self.mentored_photo: str = self.__result__.get(char.get("char")).get("mentored_photo", "null")
            self.mentoring_photo: str = self.__result__.get(char.get("char")).get("mentoring_photo", "null")
            self.mentored_inner_gif: str = self.__result__.get(char.get("char")).get("mentored_inner_gif", "null")
            self.mentoring_inner_gif: str = self.__result__.get(char.get("char")).get("mentoring_inner_gif", "null")
            self.media: Optional[Union[str, Media]] = self.__result__.get(char.get("char")).get("media", "null")
            self.glassify_buttons: Optional[Union[List[str]]] = self.get(char.get("char")).__result__.get("glassify_buttons", [])
            self.is_seen: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_seen", "null")
            self.is_edit: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_edit", "null")
            self.reply_data: Optional[Union[dict, Message]] = self.__result__.get(char.get("char")).get("reply_data", {})
        
    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)

class GroupOwner(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class GroupAdmins(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class GroupBotAdmins(Bot):...

class GroupMembers(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class GroupBotMembers(Bot):...

class GroupRemovedsList(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class GroupRemovedsBots(Bot):...
    
class Group(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.owner: Optional[Union[dict, GroupOwner]] = GroupOwner(self.__result__.get("owner", {}))
            self.admins = GroupAdmins(self.__result__.get("admins", []))
            self.members: Optional[Union[List, List[GroupMembers]]] = self.__result__.get("members", GroupMembers([]))
            self.removeds_list: Optional[Union[List, List[GroupRemovedsList]]] = self.__result__.get("removeds_list", GroupRemovedsList([]))
            self.settings: Optional[Union[dict, GroupSettings]] = GroupSettings(self.__result__.get("settings", {}))
            self.is_lock: Optional[Union[str, bool]] = self.__result__.get("is_lock", "null")
            self.is_suspesion: Optional[Union[str, bool]] = self.__result__.get("is_suspesion", "null")
            self.group_point: Optional[Union[str, list]] = self.__result__.get("group_point", "null")
            self.mentor_id: str = self.__result__.get("mentor_id", "null")
            self.title: str = self.__result__.get("title", "null")
            self.bio: str = self.__result__.get("bio", "null")
            self.created_in: str = self.__result__.get("created_in", "null")
            self.group_id: str = self.__result__.get("group_id", "null")
            self.profile_encoded_bytes: str = self.__result__.get("profile_encoded_bytes", "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")

        else:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.owner: Optional[Union[dict, GroupOwner]] = GroupOwner(self.__result__.get(char.get("char")).get("owner", {}))
            self.admins = GroupAdmins(self.__result__.get(char.get("char")).get("admins", []))
            self.members: Optional[Union[List, List[GroupMembers]]] = self.__result__.get(char.get("char")).get("members", GroupMembers([]))
            self.removeds_list: Optional[Union[List, List[GroupRemovedsList]]] = self.__result__.get(char.get("char")).get("removeds_list", GroupRemovedsList([]))
            self.settings: Optional[Union[dict, GroupSettings]] = GroupSettings(self.__result__.get(char.get("char")).get("settings", {}))
            self.is_lock: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_lock", "null")
            self.is_suspesion: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_suspesion", "null")
            self.group_point: Optional[Union[str, list]] = self.__result__.get(char.get("char")).get("group_point", "null")
            self.mentor_id: str = self.__result__.get(char.get("char")).get("mentor_id", "null")
            self.title: str = self.__result__.get(char.get("char")).get("title", "null")
            self.bio: str = self.__result__.get(char.get("char")).get("bio", "null")
            self.created_in: str = self.__result__.get(char.get("char")).get("created_in", "null")
            self.group_id: str = self.__result__.get(char.get("char")).get("group_id", "null")
            self.profile_encoded_bytes: str = self.__result__.get(char.get("char")).get("profile_encoded_bytes", "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")


    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)

class ChannelOwner(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class ChannelAdmins(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class ChannelBotAdmins(Bot):...

class ChannelMembers(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class ChannelMembers(Bot):...

class ChannelRemovedsList(User):
    def __init__(self, abstracted):
        super().__init__(abstracted)

class ChannelRemovedsBot(Bot):...

class Channel(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.owner: Optional[Union[dict, ChannelOwner]] = ChannelOwner(self.__result__.get("owner", {}))
            self.admins = ChannelAdmins(self.__result__.get("admins", []))
            self.members: Optional[Union[List, List[ChannelMembers]]] = self.__result__.get("members", ChannelMembers([]))
            self.removeds_list: Optional[Union[List, List[ChannelRemovedsList]]] = self.__result__.get("removeds_list", ChannelRemovedsList([]))
            self.settings: Optional[Union[dict, ChannelSettings]] = ChannelSettings(self.__result__.get("settings", {}))
            self.is_suspesion: Optional[Union[str, bool]] = self.__result__.get("is_suspesion", "null")
            self.channel_point: Optional[Union[str, list]] = self.__result__.get("Channel_point", "null")
            self.mentor_id: str = self.__result__.get("mentor_id", "null")
            self.title: str = self.__result__.get("title", "null")
            self.bio: str = self.__result__.get("bio", "null")
            self.created_in: str = self.__result__.get("created_in", "null")
            self.channel_id: str = self.__result__.get("Channel_id", "null")
            self.profile_encoded_bytes: str = self.__result__.get("profile_encoded_bytes", "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")

        else:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.owner: Optional[Union[dict, ChannelOwner]] = ChannelOwner(self.__result__.get(char.get("char")).get("owner", {}))
            self.admins = ChannelAdmins(self.__result__.get(char.get("char")).get("admins", []))
            self.members: Optional[Union[List, List[ChannelMembers]]] = self.__result__.get(char.get("char")).get("members", ChannelMembers([]))
            self.removeds_list: Optional[Union[List, List[ChannelRemovedsList]]] = self.__result__.get(char.get("char")).get("removeds_list", ChannelRemovedsList([]))
            self.settings: Optional[Union[dict, ChannelSettings]] = ChannelSettings(self.__result__.get(char.get("char")).get("settings", {}))
            self.is_suspesion: Optional[Union[str, bool]] = self.__result__.get(char.get("char")).get("is_suspesion", "null")
            self.channel_point: Optional[Union[str, list]] = self.__result__.get(char.get("char")).get("Channel_point", "null")
            self.mentor_id: str = self.__result__.get(char.get("char")).get("mentor_id", "null")
            self.title: str = self.__result__.get(char.get("char")).get("title", "null")
            self.bio: str = self.__result__.get(char.get("char")).get("bio", "null")
            self.created_in: str = self.__result__.get(char.get("char")).get("created_in", "null")
            self.channel_id: str = self.__result__.get(char.get("char")).get("Channel_id", "null")
            self.profile_encoded_bytes: str = self.__result__.get(char.get("char")).get("profile_encoded_bytes", "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAAXNSR0IArs4c6QAABs5JREFUeF7tnFF22zYQRQF1BT1OFOvPWUntlSReSeOV2F1JvJPqT44Sn67ARA8pUaYpAu9hMABbGv41CZBzZ94MBqCsqX+zWsDOOnud3FQAMztBBVABzGyBmaevEVABzGyBmaevEVABzGyBmaevEVABzGyBmaevEVABlLXAbvfPlVk1X1bWXDljvhpjtsa4rXP2cfPp4q7s05j31YrY/fx5bd3qe8DIW+fMQ0kQ70aCdj+e/7TWfGM83DnzrRSEdwFgt//11Rp7zxi/v6YUhMUDIGTHx2XrbHO7+fjxMQZc7LWLB/C0//XdGHsda5jj9dvL9cVn4b3UbYsG8GP/fH+sdChjTF1kjXn4tL64FQ8Ablw0gKf9s1MwXFYpWiwArupxR30PS1TOKFgsAML7O31vF2b2t5d7kCe27mV1s9n8vlWIqDdDLBIA4/3ONjd9hcNUSrmiYJEAnvbPfxtjrvze6h4v1x9uhv8nqqUsFdHiADCLrqH39xAOUtS04Lx/U/elStLiAODS89z7eyPiKPDfKwWxOABIfpxxt5v1h4cpgxHRoy5DiwJAGNC4l9VnXzVDyVAAoCQKFgUAyQ9TyZSWoUUBSJGfUzLGnVNVGVoMAKaWD8nPXNXQcgBgzzWX6wvqfZEMae4VUA8kSS6he1pvNc3qD2u7PVmjsSerof+nKIC7Z3rlaFEARN9F3HPR0P8TAGLvWGufoBiAY4nXbogHWgSdCbbOuDtfrT5Zv2ODBcvP8ZhUOTroJaUoRBEATIIcvURUD56p/1n9Z1fFWnmgCACU1DweRMuRpv6XzgPZATCt4Ziu5dS1mvpfOg9kBSCQnjP7hno3r3IR3npk6n9RHgi0Ndi8kBWAUHrGzx5ceebQfxqsQiLOBoAxzOFcZvcXrIxCPRw0D9P/8XkrciCNRJwNANLlbvllm25XCpzX7EpTX92dIwGXTMRZACCv7Iw/OH/JJGqftyHQTA7xRQCRw5Ibc1kAoNBtX3hYlzMLH18UoNMPkgR8ioAC25TqAAivac/En502Q1LSRc1oM4SZK3YBNo4GCDgxEasDoAw5Ub5xUfC2CYalLr1phqI5NRGrA0AeE6pKCHhvVscod6RUQGxLInUOVQDYIw+Vj+/INyMpQ49DwFK9s4WAIBuTFmWqAJBBxsl3uq2AjpO/vjCUB4UNdMIpkiohVQAp8sPX3q9RBEtQhVYBk5tSEr0aAEp+CIMwL9zLGAKeYphSpagaACw/vFYiaWl111l3h7541Nq1gpGWUIqqAUAPGVMt4MR32DULfXjnm6//Tthad308kt59J2yN3Ta2+WuqQEAOkZLsVQBoyU9EL75dlj2GzvSPARyTafulJN4SHX2ch6J7dgDoAZnqJ3YFivrtw1UzEVFnLfDhB9v4fl5exxOpRICm/LALIBYAko/QOH0U5SxFtQAEP4aTdCSJlw4yaJtwxKdHiGPXt2pzQ66EnwyA0X9JOciUo2HrhXMEtPzgghYC+txV2nVNBwBOkcVUP+d5AK2KY8yY91rp1zPJAFACTqkQcPLLa9SY0WcDgBKw9MG6Rhhx4i3GSMNrO21/WR1+H2jVfGF/ScU3nyTPtWMlRQCj0xL9j2kDSABMRWVqtEkjPQ0AOBKeov9a5eg5IH/NjuQ0BHsWAOiBpQ81fNFUzxwZLXzG6LAHzBwgPmMhdbakCID6X6YfT6sQk4/keUe2Gk4FEF6AEe1nZD0mz6AxDv/nDSRbPfPjj4oB7vHHVzGekpKAh/PJDPL2iRnvT0z+op0xcQSgFbBUE6fcIRWA5FkEc5YFABOwgv6fPBJ+sxWOYkmbgInw8aySiBdHAPIQyUv7zCgxxutYMm1u70fvOH5eyTsnAAj/JIzEG7wAiCOC2ivUdjwks2cABFuTKQCCFZAmgIM3ot8AmkaQ8hyxFVhMou+fVgQAeYYk6aFaLFYOusJT4RdwYxaCkn7Q/wYASvpTACWafFZuR8hfMQDIGJIHQREQ44ntWJpRyEafJOJEEYD0OAuAyNa0RI9Tq7D/DgCFFkSKFLT3piRf6dwlARStgHqDoKOIg8pC/eeGGRmSyF60BBGLItGSHOWAmIVRFgmkVuPxi754AAU2YXwwGC/sys8cEkjloBIAgCdIdJDx/m5lSnmhrv6f+lFUOVoAwBwl6MkIxK9iSXSYdQAiAqPlN1qCYAmaIfxPAAgZyKH/EQ6wcACEDOTQ/xgZii1/oyOADdd6HWeBCoCzU7arKoBspuUGrgA4O2W7qgLIZlpu4AqAs1O2qyqAbKblBq4AODtlu6oCyGZabuAKgLNTtqsqgGym5QauADg7ZbvqX7OUJ6zUjUcxAAAAAElFTkSuQmCC")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)

class Photo(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get("media_id", "null")
            self.__height__: str = self.__result__.get("height", "0")
            self.height: int = self.__height__ if type(self.__height__) is int else 0 if not self.__height__.isdigit() else int(self.__height__)
            self.__width__: str = self.__result__.get("width", "0")
            self.width: int = self.__width__ if type(self.__width__) is int else 0 if not self.__width__.isdigit() else int(self.__width__)
            self.__size__: str = self.__result__.get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.filename: str = self.__result__.get("filename", "null")
            self.format: str = self.__result__.get("format", "null")
            self.enc_bytes: str = self.__result__.get("enc_bytes", "null")

        else:

            self.status: status_types = self.__result__.get(char.get("char")).get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get(char.get("char")).get("media_id", "null")
            self.__height__: str = self.__result__.get(char.get("char")).get("height", "0")
            self.height: int = self.__height__ if type(self.__height__) is int else 0 if not self.__height__.isdigit() else int(self.__height__)
            self.__width__: str = self.__result__.get(char.get("char")).get("width", "0")
            self.width: int = self.__width__ if type(self.__width__) is int else 0 if not self.__width__.isdigit() else int(self.__width__)
            self.__size__: str = self.__result__.get(char.get("char")).get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.filename: str = self.__result__.get(char.get("char")).get("filename", "null")
            self.format: str = self.__result__.get(char.get("char")).get("format", "null")
            self.enc_bytes: str = self.__result__.get(char.get("char")).get("enc_bytes", "null")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
    def __repr__(self):
        return "<Photo>"

class Video(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get("media_id", "null")
            self.__height__: str = self.__result__.get("height", "0")
            self.height: int = self.__height__ if type(self.__height__) is int else 0 if not self.__height__.isdigit() else int(self.__height__)
            self.__width__: str = self.__result__.get("width", "0")
            self.width: int = self.__width__ if type(self.__width__) is int else 0 if not self.__width__.isdigit() else int(self.__width__)
            self.__size__: str = self.__result__.get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.__duration__: str = self.__result__.get("duration", "0")
            self.duration: int = self.__duration__ if type(self.__duration__) is int else 0 if not self.__duration__.isdigit() else int(self.__duration__)
            self.filename: str = self.__result__.get("filename", "null")
            self.format: str = self.__result__.get("format", "null")
            self.enc_bytes: str = self.__result__.get("enc_bytes", "null")

        else:

            self.status: status_types = self.__result__.get(char.get("char")).get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get(char.get("char")).get("media_id", "null")
            self.__height__: str = self.__result__.get(char.get("char")).get("height", "0")
            self.height: int = self.__height__ if type(self.__height__) is int else 0 if not self.__height__.isdigit() else int(self.__height__)
            self.__width__: str = self.__result__.get(char.get("char")).get("width", "0")
            self.width: int = self.__width__ if type(self.__width__) is int else 0 if not self.__width__.isdigit() else int(self.__width__)
            self.__size__: str = self.__result__.get(char.get("char")).get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.__duration__: str = self.__result__.get(char.get("char")).get("duration", "0")
            self.duration: int = self.__duration__ if type(self.__duration__) is int else 0 if not self.__duration__.isdigit() else int(self.__duration__)
            self.filename: str = self.__result__.get(char.get("char")).get("filename", "null")
            self.format: str = self.__result__.get(char.get("char")).get("format", "null")
            self.enc_bytes: str = self.__result__.get(char.get("char")).get("enc_bytes", "null")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
    def __repr__(self):
        return "<Video>"

class Music(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get("media_id", "null")
            self.__size__: str = self.__result__.get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.__duration__: str = self.__result__.get("duration", "0")
            self.duration: int = self.__duration__ if type(self.__duration__) is int else 0 if not self.__duration__.isdigit() else int(self.__duration__)
            self.filename: str = self.__result__.get("filename", "null")
            self.format: str = self.__result__.get("format", "null")
            self.enc_bytes: str = self.__result__.get("enc_bytes", "null")

        else:

            self.status: status_types = self.__result__.get(char.get("char")).get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get(char.get("char")).get("media_id", "null")
            self.__size__: str = self.__result__.get(char.get("char")).get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.__duration__: str = self.__result__.get(char.get("char")).get("duration", "0")
            self.duration: int = self.__duration__ if type(self.__duration__) is int else 0 if not self.__duration__.isdigit() else int(self.__duration__)
            self.filename: str = self.__result__.get(char.get("char")).get("filename", "null")
            self.format: str = self.__result__.get(char.get("char")).get("format", "null")
            self.enc_bytes: str = self.__result__.get(char.get("char")).get("enc_bytes", "null")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
    def __repr__(self):
        return "<Music>"

class File(object):
    def __init__(self, abstracted: Optional[
        Union[
            dict,
            str
        ]
    ], **char):
        
        self.__result__: dict = abstracted if type(abstracted) is dict else json.loads(abstracted)
        self.__keys__: list = list(char.keys())

        if not "char" in self.__keys__:

            self.status: status_types = self.__result__.get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get("media_id", "null")
            self.__size__: str = self.__result__.get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.filename: str = self.__result__.get("filename", "null")
            self.format: str = self.__result__.get("format", "null")
            self.enc_bytes: str = self.__result__.get("enc_bytes", "null")

        else:

            self.status: status_types = self.__result__.get(char.get("char")).get("status", "IRRESPONSIBLE")
            self.media_id: str = self.__result__.get(char.get("char")).get("media_id", "null")
            self.__size__: str = self.__result__.get(char.get("char")).get("size", "0")
            self.size: int = self.__size__ if type(self.__size__) is int else 0 if not self.__size__.isdigit() else int(self.__size__)
            self.filename: str = self.__result__.get(char.get("char")).get("filename", "null")
            self.format: str = self.__result__.get(char.get("char")).get("format", "null")
            self.enc_bytes: str = self.__result__.get(char.get("char")).get("enc_bytes", "null")

    def __str__(self):
        return json.dumps(self.__result__, ensure_ascii=False, indent=2)
    
    def __repr__(self):
        return "<File>"

class Gif(Video):
    def __init__(self, abstracted, **char):
        super().__init__(abstracted, **char)

    def __repr__(self):
        return "<Gif>"

class Media(object):
    def __init__(self):
        
        self.photo: Photo = Photo
        self.video: Video = Video
        self.music: Music = Music
        self.file: File = File
        self.gif: Gif = Gif

        self.__photo__: Photo = Photo({})
        self.__video__: Video = Video({})
        self.__music__: Music = Music({})
        self.__file__: File = File({})
        self.__gif__: Gif = Gif({})

    def __str__(self) -> str:
        return json.dumps(
            {
                "photo": "{}".format(self.__photo__.__repr__()),
                "video": "{}".format(self.__video__.__repr__()),
                "music": "{}".format(self.__music__.__repr__()),
                "file": "{}".format(self.__file__.__repr__()),
                "gif": "{}".format(self.__gif__.__repr__())
            },
            ensure_ascii=False,
            indent=2
        )
    
    def __repr__(self) -> str:
        return json.dumps(
            {
                "photo": "{}".format(self.__photo__.__repr__()),
                "video": "{}".format(self.__video__.__repr__()),
                "music": "{}".format(self.__music__.__repr__()),
                "file": "{}".format(self.__file__.__repr__()),
                "gif": "{}".format(self.__gif__.__repr__())
            },
            ensure_ascii=False,
            indent=2
        )
    
# Media Usage:
#
#     media = Media()
#
#     photo_data = {}
#
#     pd = media.photo(photo_data).width
#     pdw = media.__photo__.width
#
#     print(pd) # Output: 0 <class int>
#     print(pwd) # Output: 0 <class int>