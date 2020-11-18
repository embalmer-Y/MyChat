class UserLink(object):
    def __init__(self, name, user_id, msg, key='Emb'):
        self.name = name
        self.user_id = user_id
        self.msg = msg
        self.key = key
        self.__sock = None

    def __str__(self):
        return f'name:{self.name}, id:{self.user_id}'


class ChatParty(object):
    def __init__(self):
        self.party_queue = {}
        self.online_user = []
        self.msg_queue = {}

    def distribution_msg(self, user_obj):
        if user_obj.msg[0] in self.party_queue:
            for name in self.party_queue[user_obj.msg[0]]:
                self.msg_queue[name].append([user_obj.name, user_obj.msg, 0, user_obj.key])
        else:
            self.party_queue[user_obj.msg[0]] = []
            self.party_queue[user_obj.msg[0]].append(user_obj.name)

    def send_msg(self, name):
        for msg_list in self.msg_queue[name].items:
            if msg_list[2] != 0:
                msg_list[2] = 1
                yield msg_list[0], msg_list[1], msg_list[3]
            else:
                continue

    def user_msg_init(self, msg):
        user = UserLink(name=msg['name'], user_id=msg['id'], msg=msg['msg'], key=msg['key'])
        if user.name in self.online_user:
            self.distribution_msg(user)
        else:
            self.online_user.append(user.name)
            self.msg_queue[user.name] = []
