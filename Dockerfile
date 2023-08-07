# Use the official HiveMQ Docker image as the base image
FROM hivemq/hivemq4

# Copy custom configuration files into the container
COPY config.xml /opt/hivemq/conf/config.xml

# Expose MQTT, Websocket, and clustering ports
EXPOSE 1883 8000 7800