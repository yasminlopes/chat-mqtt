#importando o MQTT
import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1234

user = input("[INFO] Digite o seu nome: ")
client = mqtt.Client(user, False)
def c_conex(client, userdata, flags, rc):
    # print('[INFO] Conectado!')
    pass

def c_desc(client, userdata, rc=0):
    pass

def c_on(client, userdata, mid, granted_qos):
    pass

def c_post(client, userdata, mid):
    pass
  
def c_msg(client, userdata, message):
    topics = (message.topic).split('/')
    if topics[1] != user:
        print(f'{topics[1]}: {str(message.payload.decode("utf-8"))}')
        
client.c_conex = c_conex
client.c_desc = c_desc
client.c_post = c_post
client.c_on = c_on
client.c_msg = c_msg

client.c_conex(BROKER, PORT)
client.loop_start()
client.on('chat/#')

while True:
    client.post(f'chat/{user}', input())