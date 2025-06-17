# MIT License
# Copyright (c) 2025 Manuel Ricci
# See LICENSE file in the root of this repository for full license information.

# Percorso al file log dei codici TOTP
$totpLogPath = "C:\Users\Proprietario\Desktop\codici_totp_log.txt"

# Verifica che il file esista
if (-Not (Test-Path $totpLogPath)) {
    Write-Host "File dei codici TOTP non trovato."
    exit 1
}

# Leggi l'ultima riga (ultimo codice)
$lastCode = Get-Content $totpLogPath | Select-Object -Last 1

# Richiedi il codice all'utente
$inputCode = Read-Host "Inserisci il codice TOTP"

# Verifica il codice
if ($inputCode -eq $lastCode) {
    Write-Host "Codice corretto. Accesso autorizzato."
    
    # Avvia una nuova shell PowerShell interattiva per mantenere la sessione SSH aperta
    powershell.exe
} else {
    Write-Host "Codice errato. Accesso negato."
    exit 1
}
