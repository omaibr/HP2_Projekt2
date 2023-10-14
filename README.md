# HP2_Projekt2

# Temperaturmätning med Raspberry Pi Pico och DS18B20

För att använda koden behöver du:

- Raspberry Pi Pico
- DS18B20-temperatursensor

I detta projekt är målet att utveckla ett program som kan avläsa data från en temperatursensor av typen (ds18x20) och sedan presentera resultaten i terminalen i formatet <unit id> <sensor id> <measurement>. Ett exempel på utskriften är: e6614103e71d8d2e 28d6445c090000da 23.75. Programmet ska kunna se hur många temp-sensorer som är anslutna. Det ska finnas en config.json-fil som anger vilken pin vi ska använda och hur långt intervallet mellan varje utskrift ska vara.


## Installation

För att köra koden på din Raspberry Pi Pico, följ dessa steg:

1. **Ladda ner MicroPython till Raspberry Pi Pico**
   - Håll in BOOTSEL-knappen på Picon samtidigt som du ansluter den till datorn.
   - Ladda ner MicroPython och överför den till Picon.

2. **Kör koden med Thonny**
   - Öppna koden i en lämplig IDE, t.ex. VS Code.
   - Anslut din Pico till datorn via USB.
   - Använd Thonny eller liknande för att köra koden på din Pico.

---