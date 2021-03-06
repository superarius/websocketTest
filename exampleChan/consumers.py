import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http, channel_session


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'msg': 'login'
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'msg': 'logout'
        })
    })
    Group('users').discard(message.reply_channel)

@channel_session_user
def ws_receive(message):
    Group('users').send({
        'text': json.dumps({
            'msg': message['text']	
             
        })
    })


