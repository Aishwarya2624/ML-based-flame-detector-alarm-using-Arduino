// === ML Model Parameters (from your Python training) ===
float weight = 0.053855f;   // example; replace with your value
float bias   = -27.539853f; // example; replace with your value

// === Pin Definitions ===
const int flameSensorPin = A0;  // analog input
const int ledPin         = 13;  // status LED
const int buzzerPin      = 12;  // buzzer output

// === Sigmoid Function ===
float sigmoid(float x) {
  return 1.0 / (1.0 + exp(-x));
}

void setup() {
  pinMode(flameSensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("🔥 ML Flame Detector with Buzzer");
}

void loop() {
  int rawVal = analogRead(flameSensorPin);     // 0–1023
  float logit = weight * rawVal + bias;
  float prob  = sigmoid(logit);

  Serial.print("Raw = ");
  Serial.print(rawVal);
  Serial.print(" | Prob = ");
  Serial.println(prob, 4);

  if (prob > 0.5) {
    Serial.println("✅ No Flame");
    digitalWrite(ledPin, HIGH);
    // Sound buzzer: 2 kHz tone for 200 ms
    noTone(buzzerPin);
  } else {
    Serial.println("🔥 FLAME DETECTED");
    digitalWrite(ledPin, LOW);
    tone(buzzerPin, 2000, 200);
  }

  delay(1000);
}
