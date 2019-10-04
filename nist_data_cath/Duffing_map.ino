double x1 = 0.4;
double x2 = -0.2;
double x1n;
double x2n;
byte *ptr;
byte x1array[8];
byte x2array[8];
bool terabit;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:
  x1n = x2;
  x2n = -0.2 * x1 + 2.75 * x2 - x2 * x2 * x2;
  x1 = x1n;
  x2 = x2n;

  ptr = (byte *)&x1; //把um存到指標裡 方便傳送
  for (int i = 0; i < 8; i++)
  {
    x1array[i] = *ptr, HEX;
    *ptr++;
  }
  ptr = (byte *)&x2; //把um存到指標裡 方便傳送
  for (int i = 0; i < 8; i++)
  {
    x2array[i] = *ptr, HEX;
    *ptr++;
  }

  for (int i = 0; i < 8; i++) {
    terabit = x2array[0] & 0x80;
    Serial.print(terabit);
    x2array[0] = x2array[0] << 1;
  }

}
