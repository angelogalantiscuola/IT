## WSL <!-- omit in toc -->

- [WSL: Windows Subsystem for Linux](#wsl-windows-subsystem-for-linux)
- [Perché usare WSL invece di Windows quando si scrive codice](#perché-usare-wsl-invece-di-windows-quando-si-scrive-codice)
- [Come installare WSL in Windows](#come-installare-wsl-in-windows)

### WSL: Windows Subsystem for Linux

Il **Windows Subsystem for Linux (WSL)** è una funzionalità di Windows che permette di eseguire un ambiente GNU/Linux direttamente su Windows, senza la necessità di una macchina virtuale o di un dual-boot. WSL consente agli sviluppatori di utilizzare strumenti e applicazioni Linux nativamente su Windows, migliorando l'integrazione tra i due sistemi operativi.

### Perché usare WSL invece di Windows quando si scrive codice

Ci sono diversi motivi per cui uno sviluppatore potrebbe preferire utilizzare WSL invece di Windows per scrivere codice:

- **Compatibilità con strumenti Linux**: Molti strumenti di sviluppo, librerie e framework sono nativamente disponibili su Linux. Utilizzando WSL, è possibile accedere a questi strumenti senza dover lasciare l'ambiente Windows.
- **Ambiente di sviluppo coerente**: Se il codice deve essere eseguito su server Linux in produzione, sviluppare in un ambiente Linux locale può ridurre le discrepanze tra sviluppo e produzione.
- **Prestazioni**: WSL offre prestazioni migliori rispetto a una macchina virtuale tradizionale, poiché non richiede l'overhead di un hypervisor.
- **Integrazione con Windows**: WSL permette di utilizzare strumenti e applicazioni Windows insieme a quelli Linux, offrendo un ambiente di sviluppo ibrido e flessibile.

### Come installare WSL in Windows

L'installazione di WSL su Windows è un processo semplice che può essere completato in pochi passaggi:

1. **Abilitare la funzionalità WSL**:
   - Apri PowerShell come amministratore e esegui il seguente comando:
     ```powershell
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     ```

2. **Abilitare la funzionalità Virtual Machine Platform**:
   - Sempre in PowerShell come amministratore, esegui:
     ```powershell
     dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
     ```

3. **Installare una distribuzione Linux**:
   - Apri il Microsoft Store e cerca una distribuzione Linux (ad esempio, Ubuntu). Clicca su "Ottieni" per installarla.

4. **Impostare WSL 2 come versione predefinita**:
   - Dopo aver installato la distribuzione, apri PowerShell come amministratore e esegui:
     ```powershell
     wsl --set-default-version 2
     ```

5. **Avviare la distribuzione Linux**:
   - Una volta completata l'installazione, apri la distribuzione Linux dal menu Start. Segui le istruzioni per completare la configurazione iniziale.

6. **Verificare l'installazione**:
   - Puoi verificare che WSL sia correttamente installato eseguendo il comando `wsl -l -v` in PowerShell. Dovresti vedere la tua distribuzione Linux elencata con la versione WSL 2.

Con questi passaggi, avrai un ambiente Linux completamente funzionante all'interno di Windows, pronto per essere utilizzato per lo sviluppo software.