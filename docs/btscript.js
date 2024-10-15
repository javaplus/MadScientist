const controlButton = document.getElementById("controlButton");
const deviceNameInput = document.getElementById("deviceNameInput");
const connectionStatus = document.getElementById("connectionStatus");

// Button elements for each command
const forwardButton = document.getElementById("forwardButton");
const backwardButton = document.getElementById("backwardButton");
const leftButton = document.getElementById("leftButton");
const rightButton = document.getElementById("rightButton");
const stopButton = document.getElementById("stopButton");

controlButton.addEventListener("click", BLEManager);

deviceNameInput.value = "Peripheral";

// Store connected device and service
let connectedDevice;
let envService;

async function BLEManager() {
    connectionStatus.textContent = "SEARCHING";
    try {
        const device = await navigator.bluetooth.requestDevice(
            {filters: [{
                name: deviceNameInput.value,
                services: ['environmental_sensing']
                }]
            });    

        connectedDevice = await device.gatt.connect();
        connectionStatus.textContent = "CONNECTED";

    } catch (error) {
        if (typeof device !== 'undefined'){
            connectionStatus.textContent = "Connection Failed";
        }else{
            connectionStatus.textContent = "CANCELLED";
        }
        
    }
    try {
        envService = await connectedDevice.getPrimaryService("environmental_sensing");
        console.log("Services Obtained");

         // Enable button interactions after connection
         enableControlButtons();
            
    } catch (error) {
        console.log("ERROR getting service");
        console.log(error);
        connectionStatus.textContent = "No Services";
        
    }

}
    

    // Function to enable control buttons
function enableControlButtons() {
    forwardButton.addEventListener("click", () => sendCommand("forward"));
    backwardButton.addEventListener("click", () => sendCommand("backward"));
    leftButton.addEventListener("click", () => sendCommand("left"));
    rightButton.addEventListener("click", () => sendCommand("right"));
    stopButton.addEventListener("click", () => sendCommand("stop"));
}

// Function to send command to the peripheral
async function sendCommand(direction) {
    try {
        const temperatureCharacteristic = await envService.getCharacteristic("temperature");
        const encoder = new TextEncoder('utf-8');
        const value = encoder.encode(direction);
        console.log("Sending message: " + direction);
        await temperatureCharacteristic.writeValueWithResponse(value);
        console.log("Command sent: " + direction);
    } catch (error) {
        console.log("Error sending command.");
        console.log(error);
        connectionStatus.textContent = "Error sending command";
    }
}
    
 
