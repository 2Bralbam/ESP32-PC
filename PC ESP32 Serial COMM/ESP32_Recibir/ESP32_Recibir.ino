#define LED_PIN             2

char c; 
char str[3];
uint8_t idx = 0;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
    c = Serial.read();
    if(c != '\n'){
      str[idx++] = c;
    }
    else{
      str[idx] = '\0';
      if (strcmp(str, "On") == 0) {
        Serial.println("Led Encendido");
        digitalWrite(LED_PIN, HIGH);
      } else if (strcmp(str, "Off") == 0) {
        Serial.println("Led Apagado");
        digitalWrite(LED_PIN, LOW);
      } else {
        Serial.println("Comando desconocido");
      }
      idx = 0;
    }
  }
}
