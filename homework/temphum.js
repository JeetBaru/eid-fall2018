/*
* File: temphum.js
* 
* Function: This application logs temperature and humidity from
* 			 DHT22 sensor on RPi3. It also logs, max, min and average values
* 			 of temperature and humidity
* 
* References: https://github.com/momenso/node-dht-sensor/blob/master/test/sync-implicit.js
* 			  http://www.airspayce.com/mikem/bcm2835/
* 
* Install Note: You need to have node-dht-sensor node module installed on the system
* 				Make sure to give correct path inside require(...)
* 
* Author: Jeet Baru 
*/

// implicit sensor read test
var sensor = require('/home/pi/node_modules/node-dht-sensor');

var usage = 'USAGE: node temphum.js [sensorType] [gpioPin] <repeats>\n' +
    '    sensorType:\n' +
    '         11: For DHT11 sensor.\n' +
    '         22: For DHT22 or AM2302 sensors.\n\n' +
    '    gpipPin:\n' +
    '         Pin number where the sensor is physically connected to.\n\n' +
    '    repeats:\n' +
    '         How many times the read operation will be performed, default: 10\n';

var sensorType = parseInt(process.argv[2] || '22', 10);
var gpioPin = parseInt(process.argv[3] || '4', 10);
var repeats = parseInt(process.argv[4] || '10', 10);
var count = 0;
var maxtemp = 0;
var mintemp = 99;
var maxhum = 0;
var minhum = 99;
var totaltemp = 0;
var totalhum = 0;

// initialize sensor
if (!sensor.initialize(sensorType, gpioPin)) {
  console.warn('Failed to initialize sensor');
  return;
}

var iid = setInterval(function() {
  if (++count >= repeats) {
    clearInterval(iid);
  }
  var start = new Date().getTime();
  var readout = sensor.read();
  var end = new Date().getTime();
  console.log(`temperature: ${readout.temperature.toFixed(1)}°C, ` +
              `humidity: ${readout.humidity.toFixed(1)}%, ` +
              `valid: ${readout.isValid}, ` +
              `errors: ${readout.errors}, ` +
              `time: ${end - start}ms`);
              
  //depending on values read populate counters for max and min temp and hum
  if (readout.temperature.toFixed(1) > maxtemp){
	  maxtemp = readout.temperature.toFixed(1);
  }
  if (readout.temperature.toFixed(1) < mintemp){
	  mintemp = readout.temperature.toFixed(1);
  }
  if (readout.humidity.toFixed(1) > maxhum){
	  maxhum = readout.humidity.toFixed(1);
  }
  if (readout.humidity.toFixed(1) < minhum){
	  minhum = readout.humidity.toFixed(1);
  }
  totaltemp = Number(totaltemp) + Number(readout.temperature.toFixed(1));
  totalhum = Number(totalhum) + Number(readout.humidity.toFixed(1));
  
  //if final values read display log
  if (count >= repeats){
	console.log(`Maximum Temeperature: ${maxtemp}`)
	console.log(`Minimum Temeperature: ${mintemp}`)
	console.log(`Maximum Humidity: ${maxhum}`)
	console.log(`Minimum Humidity: ${minhum}`)
	//calculate and print average values
	console.log(`Average Temeperature: ${(totaltemp/repeats).toFixed(1)}`)
	console.log(`Average Humidity: ${(totalhum/repeats).toFixed(1)}`)
  }	
}, 1000);

