from azure.iot.device import IoTHubDeviceClient
import time
import json
import random

# Replace this with the connection string of the IoT device you registered
CONNECTION_STRING = "HostName=MasonSquareIoTHub.azure-devices.net;DeviceId=spoof0001;SharedAccessKey=Xj1HrHB8dUE5ajQpjfRRFKTffX/JRoFqAm9wa/WmsEM="

# Create an IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_data():
    try:
        room_numbers = [
            *range(1000, 1010),  # Floor 1, rooms 1000-1009
            *range(2000, 2010),  # Floor 2, rooms 2000-2009
            *range(3000, 3010),  # Floor 3, rooms 3000-3009
            *range(4000, 4010),  # Floor 4, rooms 4000-4009
            *range(5000, 5010)   # Floor 5, rooms 5000-5009
        ]

        for room_id in room_numbers:
            # Simulating the data to send with more realistic variations
            temperature = round(random.uniform(21.5, 24.0), 2)  # Typical office temperature range
            humidity = round(random.uniform(40, 60), 2)  # Moderate humidity level in an office
            oxygen = round(random.uniform(95, 99), 2)  # Oxygen level is usually stable
            co = round(random.uniform(0, 5), 2)  # Low carbon monoxide levels
            co2 = round(random.uniform(400, 800), 2)  # Typical indoor CO2 concentration
            energy_usage = round(random.uniform(150, 250), 2)  # Energy usage per room, moderate variation
            water_usage = round(random.uniform(5, 15), 2)  # Lower water usage for office spaces
            occupancy = random.randint(0, 40)  # Generate a whole number for occupancy
            
            # Creating the JSON message for each room
            message = {
                "deviceId": f"room_{room_id}",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "temperature": temperature,
                "humidity": humidity,
                "oxygen": oxygen,
                "carbon_monoxide": co,
                "carbon_dioxide": co2,
                "energy_usage": energy_usage,
                "water_usage": water_usage,
                "occupancy": occupancy,  # Occupancy as a whole number
            }
            
            # Convert message to JSON
            message_json = json.dumps(message)
            
            # Send message to IoT Hub
            print(f"Sending message for room {room_id}: {message_json}")
            client.send_message(message_json)
            
            # Sleep for a short time between room messages to avoid overwhelming the device
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("IoT Hub client stopped.")

if __name__ == "__main__":
    while True:
        send_data()
        print("Waiting for 5 minutes before sending the next batch...")
        time.sleep(300)  # Wait for 5 minutes
