import os
import json
import requests
import uuid
from datetime import datetime
from telegram import Bot

# Determine the directory of the script and construct the path to config.conf
script_directory = os.path.dirname(__file__)
config_file_path = os.path.join(script_directory, 'config.conf')

# Load config values from the config.conf file
with open(config_file_path) as config_file:
    config = json.load(config_file)

# Get your Telegram bot token and chat ID
telegram_bot_token = config.get('TELEGRAM_BOT_TOKEN', 'default_value_if_not_found')
telegram_chat_id = config.get('TELEGRAM_CHAT_ID', 'default_value_if_not_found')

# Initialize the Telegram bot
bot = Bot(token=telegram_bot_token)

# Send a message to a Telegram channel or group
def send_telegram_message(text):
    bot.send_message(chat_id=telegram_chat_id, text=text)

# Continue with the rest of your script using the config values
data = {
    "client_id": config['CLIENT_ID'],
    "client_secret": config['CLIENT_SECRET'],
    "username": config['API_USER'],
    "password": config['API_PASSWORD'],
    "grant_type": "password"
}
token_url = 'https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token'
response = requests.post(token_url, data=data)
response_data = response.json()
access_token = response_data.get('access_token')

# Set trace id
trace_id = str(uuid.uuid4())

# Get instances
uuid_val = str(uuid.uuid4())
instances_url = 'https://api.contabo.com/v1/compute/instances?size=1000'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
    'x-request-id': uuid_val,
    'x-trace-id': trace_id
}
response = requests.get(instances_url, headers=headers)
instances_json_response = response.json()
print("\ninstances_json_response\n")
print(json.dumps(instances_json_response, indent=2))
print("\n=============\n")

instances = [instance['instanceId'] for instance in instances_json_response['data']]

# For each instance, delete the oldest snapshot and create a new snapshot named with the timestamp
timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
for instance_id in instances:
    print(f"\n ==== instanceId: {instance_id} ====\n")
    
    uuid_val = str(uuid.uuid4())
    snapshots_url = f'https://api.contabo.com/v1/compute/instances/{instance_id}/snapshots'
    response = requests.get(snapshots_url, headers=headers)
    snapshots_data = response.json()['data']
    
    if snapshots_data:
        oldest_snapshot = snapshots_data[0]['snapshotId']
        
        uuid_val = str(uuid.uuid4())
        delete_snapshot_url = f'https://api.contabo.com/v1/compute/instances/{instance_id}/snapshots/{oldest_snapshot}'
        response = requests.delete(delete_snapshot_url, headers=headers, json={})

        # Send a message to Telegram channel/group on success or failure
        if response.status_code == 204:
            send_telegram_message(f"[Contabo_Snapshot] ❌ Deleted snapshot for instance {instance_id} successfully.")
        else:
            error_message = response.json().get('message', 'Unknown error')
            send_telegram_message(f"[Contabo_Snapshot] 💥 Failed to delete snapshot for instance {instance_id}. Error: {error_message}")
            
    uuid_val = str(uuid.uuid4())
    create_snapshot_url = f'https://api.contabo.com/v1/compute/instances/{instance_id}/snapshots'
    snapshot_data = {
        "name": timestamp,
        "description": "Snapshot-Description"
    }
    response = requests.post(create_snapshot_url, headers=headers, json=snapshot_data)
    
    # Send a message to Telegram channel/group on success or failure
    if response.status_code == 201:
        send_telegram_message(f"[Contabo_Snapshot] ✅ Created snapshot for instance {instance_id} successfully.")
    else:
        send_telegram_message(f"[Contabo_Snapshot] 💥 Failed to create snapshot for instance {instance_id}.")

exit(0)
