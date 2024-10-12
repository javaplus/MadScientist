const controlButton = document.getElementById("controlButton");
const deviceNameInput = document.getElementById("deviceNameInput");
const connectionStatus = document.getElementById("connectionStatus");


controlButton.addEventListener("click", BLEManager);

deviceNameInput.value = "Peripheral";

async function BLEManager() {
    connectionStatus.textContent = "SEARCHING";
    connectedDevice = undefined;
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
    envService = undefined;
    try {
        envService = await connectedDevice.getPrimaryService("environmental_sensing");
        console.log("Services Obtained");
            
    } catch (error) {
        console.log("ERROR getting service");
        console.log(error);
        connectionStatus.textContent = "No Services";
        
    }

    try {
        const temperatureCharacteristic = await envService.getCharacteristic("temperature");    
 

        // await new Promise(r => setTimeout(r, 2000));
        let encoder = new TextEncoder('utf-8');
        let value = encoder.encode("forward");
        //let value = Uint8Array.of(0x01)
        console.log("Sending message:" + value);

        for (let index = 0; index < 20; index++) {
            //await temperatureCharacteristic.writeValueWithoutResponse(value);
            response = await temperatureCharacteristic.writeValueWithResponse(value);
            console.log("wrote data:" + response);    
            // sleep for 2 sec
            await new Promise(r => setTimeout(r, 2000));
        }
        

    } catch (error) {
        console.log("Error getting characteristic.");
        console.log(error);
        connectionStatus.textContent = "No Characteristics to use";
    }
    
    
 
}