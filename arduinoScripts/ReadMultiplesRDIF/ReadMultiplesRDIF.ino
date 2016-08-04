/*
  Código para saber que identificador NFC hay en cada posicion de forma continua
 */

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

#define SS_PIN2 8
#define RST_PIN2 7
 
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class
MFRC522 rfid2(SS_PIN2, RST_PIN2); // Instance of the class

MFRC522::MIFARE_Key key; 
MFRC522::PICC_Type piccType;

// Init array that will store new NUID 
byte nuidPICC[3];

byte piano[4] = {131, 43, 239, 117};
byte sample[4] = {229, 211, 125, 99};

int currentId;
int currentId2;

int lastId;
int lastId2;

void setup() { 
  Serial.begin(9600);
  SPI.begin(); // Init SPI bus

  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
}
 
void loop() {
  currentId = readModule(rfid);
  if(currentId != lastId){
    Serial.println("0" + String(currentId));
  }
  
  currentId2 = readModule(rfid2);
  if(currentId2 != lastId2){
    Serial.println("1" + String(currentId2));
  }

  lastId = currentId;
  lastId2 = currentId2;
}

int readModule(MFRC522 module){
  module.PCD_Init(); // Init MFRC522
 
  // Look for new cards
  if (!module.PICC_IsNewCardPresent()){
    // Halt PICC
    module.PICC_HaltA();

    // Stop encryption on PCD
    module.PCD_StopCrypto1();
    return 0;
  }

   // Verify if the NUID has been readed
  if (!module.PICC_ReadCardSerial()){
    // Halt PICC
    module.PICC_HaltA();

    // Stop encryption on PCD
    module.PCD_StopCrypto1();
    return 0;
  }
    
  piccType = module.PICC_GetType(rfid.uid.sak);
   
  if(piano[0] == module.uid.uidByte[0] &&
    piano[1] == module.uid.uidByte[1] &&
    piano[2] == module.uid.uidByte[2] &&
    piano[3] == module.uid.uidByte[3]){
    // Halt PICC
    module.PICC_HaltA();

    // Stop encryption on PCD
    module.PCD_StopCrypto1();

    return 1;
  }

  if(sample[0] == module.uid.uidByte[0] &&
    sample[1] == module.uid.uidByte[1] &&
    sample[2] == module.uid.uidByte[2] &&
    sample[3] == module.uid.uidByte[3]){

    // Halt PICC
    module.PICC_HaltA();

    // Stop encryption on PCD
    module.PCD_StopCrypto1();

    return 2;
    
  }

    
  // Halt PICC
  module.PICC_HaltA();

  // Stop encryption on PCD
  module.PCD_StopCrypto1();
}
