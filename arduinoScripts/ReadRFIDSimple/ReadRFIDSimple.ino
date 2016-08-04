/*
  Código para saber que identificador NFC hay en cada posicion de forma continua
 */

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
 
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class

MFRC522::MIFARE_Key key; 

// Init array that will store new NUID 
byte nuidPICC[3];

byte guitar[4] = {53, 07, 04, 109};
byte piano[4] = {131, 43, 239, 117};
byte sample[4] = {229, 211, 125, 99};
byte keyboard[4] = {69, 42, 174, 107};

int currentId;

void setup() { 
  Serial.begin(9600);
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522 

  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
}
 
void loop() {
  // Look for new cards
  if ( ! rfid.PICC_IsNewCardPresent()){
    if(currentId != 3){
      currentId = 3;
      Serial.println(3);
    }
    return;
  }
    
  // Verify if the NUID has been readed
  if ( ! rfid.PICC_ReadCardSerial())
    return;
    
  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
   
  if(guitar[0] == rfid.uid.uidByte[0] &&
    guitar[1] == rfid.uid.uidByte[1] &&
    guitar[2] == rfid.uid.uidByte[2] &&
    guitar[3] == rfid.uid.uidByte[3] &&
    currentId != 0){

    currentId = 0;
    
    Serial.println(0);
      
  }

  if(piano[0] == rfid.uid.uidByte[0] &&
    piano[1] == rfid.uid.uidByte[1] &&
    piano[2] == rfid.uid.uidByte[2] &&
    piano[3] == rfid.uid.uidByte[3] &&
    currentId != 1){

    currentId = 1;
    
    Serial.println(1);
  }

  if(sample[0] == rfid.uid.uidByte[0] &&
    sample[1] == rfid.uid.uidByte[1] &&
    sample[2] == rfid.uid.uidByte[2] &&
    sample[3] == rfid.uid.uidByte[3] &&
    currentId != 2){

    currentId = 2;
    
    Serial.println(2);
  }

  if(keyboard[0] == rfid.uid.uidByte[0] &&
    keyboard[1] == rfid.uid.uidByte[1] &&
    keyboard[2] == rfid.uid.uidByte[2] &&
    keyboard[3] == rfid.uid.uidByte[3] &&
    currentId != 4){

    currentId = 4;
    
    Serial.println(4);
  }
    
  // Halt PICC
  rfid.PICC_HaltA();

  // Stop encryption on PCD
  rfid.PCD_StopCrypto1();

  
  rfid.PCD_Init(); // Init MFRC522 

  delay(100);
}


/**
 * Helper routine to dump a byte array as hex values to Serial. 
 */
void printHex(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
}

/**
 * Helper routine to dump a byte array as dec values to Serial.
 */
void printDec(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], DEC);
  }
}
