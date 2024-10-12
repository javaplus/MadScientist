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
        console.log("Characteristics discovered");
        console.log('> Characteristic UUID:  ' + temperatureCharacteristic.uuid);
        console.log('> Broadcast:            ' + temperatureCharacteristic.properties.broadcast);
        console.log('> Broadcast:            ' + temperatureCharacteristic.properties.broadcast);
        console.log('> Broadcast:            ' + temperatureCharacteristic.properties.broadcast);
        console.log('> Read:                 ' + temperatureCharacteristic.properties.read);
        console.log('> Broadcast:            ' + temperatureCharacteristic.properties.broadcast);
        console.log('> Write w/o response:   ' +
            temperatureCharacteristic.properties.writeWithoutResponse);
        console.log('> Write:                ' + temperatureCharacteristic.properties.write);
        console.log('> Notify:               ' + temperatureCharacteristic.properties.notify);
        console.log('> Indicate:             ' + temperatureCharacteristic.properties.indicate);
        console.log('> Signed Write:         ' +
            temperatureCharacteristic.properties.authenticatedSignedWrites);
        console.log('> Queued Write:         ' + temperatureCharacteristic.properties.reliableWrite);
        console.log('> Writable Auxiliaries: ' +
            temperatureCharacteristic.properties.writableAuxiliaries);

        await new Promise(r => setTimeout(r, 2000));
        let encoder = new TextEncoder('utf-8');
        let value = encoder.encode("hello");
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