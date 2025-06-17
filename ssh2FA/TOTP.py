# MIT License
# Copyright (c) 2025 Manuel Ricci
# See LICENSE file in the root of this repository for full license information.

import pyotp
import qrcode
import time
import os
from pathlib import Path

# === CONFIGURAZIONE ===
account_name = "utente@example.com"
issuer_name = "MioServizio"
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

# === URI per Google Authenticator ===
uri = totp.provisioning_uri(name=account_name, issuer_name=issuer_name)
print(f"Chiave segreta: {secret}")
print(f"URI per Authenticator: {uri}")

# === Genera QR code ===
qr = qrcode.make(uri)
qr_file = "qrcode_totp.png"
qr.save(qr_file)
try:
    qr.show()
except:
    pass

# === PERCORSO DEL FILE SUL DESKTOP ===
desktop_path = Path(r"C:\Users\Proprietario\Desktop")
log_file_path = desktop_path / "codici_totp_log.txt"

print(f"📄 I codici verranno salvati in: {log_file_path}")

# === FUNZIONE PER PULIRE LO SCHERMO ===
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# === LOOP CONTINUO PER GENERARE E LOGGARE I CODICI ===
print("\nPremi CTRL+C per fermare.\n")
last_code = None

try:
    while True:
        current_code = totp.now()
        time_remaining = totp.interval - (time.time() % totp.interval)

        if current_code != last_code:
            # Scrive solo il codice OTP, una riga per ciascuno
            with open(log_file_path, "a") as f:
                f.write(f"{current_code}\n")

            clear_console()
            print("=== Generatore TOTP ===\n")
            print(f"🔐 Codice attuale: {current_code}")
            print(f"⏳ Tempo rimanente: {int(time_remaining)} secondi")
            print(f"\n📄 Log salvato in: {log_file_path}")
            last_code = current_code

        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Uscita dal generatore TOTP.")
