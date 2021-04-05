#include <Adafruit_GPS.h> //Install Adafruit GPS library before
#include <SoftwareSerial.h>

#define LoRaserial Serial1
SoftwareSerial GPSserial(10, 9); //Rx=10; Tx=9 Pin

Adafruit_GPS GPS(&GPSserial);

#define PMTK_SET_NMEA_UPDATE_1HZ  "$PMTK220,1000*1F"
#define PMTK_SET_NMEA_UPDATE_5HZ  "$PMTK220,200*2C"
#define PMTK_SET_NMEA_UPDATE_10HZ "$PMTK220,100*2F"

// turn on only the second sentence (GPRMC)
#define PMTK_SET_NMEA_OUTPUT_RMCONLY "$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29"

//String ID;
#define ID "2"

void setup() {
  // put your setup code here, to run once:

  //randomSeed(analogRead(A0));
  //ID = random(99999999);
  
  GPS.begin(9600);
  LoRaserial.begin(9600);
  delay(2000);

  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);

  delay(1000);
}

void loop() {
  GPS.read();
  if (GPS.newNMEAreceived()) {
    if (!GPS.parse(GPS.lastNMEA()))
      return;
  }
  if (LoRaserial.available()) {
    delay(500);
    String command = "";
    while (LoRaserial.available()) {
      char c = LoRaserial.read();
      command += c;
    }
    Serial.println(command);
    if (command.indexOf("ID") >= 0 && command.indexOf(ID) < 0) {
      LoRaserial.println(ID);
    }
    if (command.equals("RD " + String(ID))) {
      if (GPS.fix) {
        LoRaserial.print(GPS.latitude, 4); LoRaserial.print(GPS.lat);
        LoRaserial.print(", ");
        LoRaserial.print(GPS.longitude, 4); LoRaserial.println(GPS.lon);
      } else {
        LoRaserial.println("No GPS fix, No GPS fix");
        Serial.println("No fix");
      }
    }
  }
}
