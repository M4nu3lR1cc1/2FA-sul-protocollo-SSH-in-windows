# 2FA-sul-protocollo-SSH-in-windows
# 🔐 Autenticazione a Due Fattori (2FA) su SSH in Windows (senza software di terze parti)

Questo progetto dimostra come implementare un sistema di autenticazione a due fattori (2FA) per connessioni SSH su **Windows**, senza utilizzare applicazioni di terze parti come Google Authenticator.  
La soluzione è completamente **self-hosted**, ed è basata su uno **script Python** per generare codici TOTP e uno **script PowerShell** per la verifica OTP, la gestione dei log e l'invio delle notifiche via email.

## 📌 Funzionalità

- Generazione TOTP conforme a RFC 6238 con Python
- Verifica dell'OTP tramite PowerShell
- Logging di accessi e tentativi falliti
- Invio automatico di email in caso di accesso (riuscito o fallito)
- Nessuna dipendenza da app esterne


## ⚙️ Requisiti

- Windows 10/11 con PowerShell abilitato
- Python 3.x installato
- OpenSSH abilitato su Windows
- Accesso amministrativo
- Un client SSH per connettersi (es. PuTTY, OpenSSH, ecc.)


🔐 Utilizzo
L'utente tenta l'accesso via SSH.

Viene richiesto di inserire un codice OTP.

PowerShell verifica il codice tramite script.

Se corretto:

Accesso consentito

Log salvato 

Email inviata

Se errato:

Accesso negato

Log ed email inviati

⚠️ Avvertenze
Questo sistema non utilizza PAM o servizi esterni: l'affidabilità è legata alla robustezza degli script.

Non è pensato per ambienti enterprise senza ulteriori misure di sicurezza.

Proteggi bene la chiave segreta (config.json) e limita l'accesso in lettura.

🧑‍💻 Autore: ManuelRicci

YouTube: https://www.youtube.com/channel/UCbfJzXsKc9lhrpH5-sa7zcg

LinkedIn: https://www.linkedin.com/in/manuel-ricci-767167370/
