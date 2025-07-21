# Assign constants: Wi-Fi SSID & password, MQTT broker details, 
# notification API tokens, and motion sensor pin.

# Initialize motion sensor (Pin 1 as input)



# Function: connect_wifi
    # Enable station mode, disconnect if already connected
    # Try to connect to Wi-Fi
    # Keep retrying until connected (print dots as progress)



# Function: send_mqtt_signal
    # Try to connect to MQTT broker on port 1883
    # Publish "motion" message to the topic
    # Disconnect client after sending
    # If error occurs, print the error



# Function: send_phone_notification
    # Prepare POST request to Pushover API with tokens & message
    # Send request with try-catch
    # If response is 200, print success; else print error status & text
    # Close response object



# Main loop (runs forever):
    # If motion sensor detects movement:
        # Print "Motion Detected"
        # Connect to Wi-Fi
        # Send MQTT signal
        # Send phone notification
        # Wait 2 seconds to avoid spamming
