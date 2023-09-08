import paho.mqtt.client as mqtt
import time, ssl

# Callback when a connection has been established with the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to a topic
    client.subscribe("test/topic")

# Callback when a message is received from the broker
def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())

# Create a MQTT client instance
client = mqtt.Client(
    client_id="python-test",
    transport="websockets",
)

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Set username and password if required
# client.username_pw_set("username", "password")

# Connect to the HiveMQ broker (replace with actual broker address)
broker_address = "<PROJECT_NAME>.up.railway.app"
client.ws_set_options(path="/mqtt")
client.tls_set(cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLS)
client.connect(broker_address, 443, 60)

# Start the network loop
client.loop_start()

time.sleep(2)

# Publish a message to a topic
client.publish("test/topic", "Hello from Python!")

# Wait for a moment to receive the published message
time.sleep(2)

# Disconnect from the broker
client.disconnect()
client.loop_stop()