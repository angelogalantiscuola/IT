## Shell  <!-- omit in toc -->

- [Linguaggi di Scripting](#linguaggi-di-scripting)
  - [Bash (Bourne Again Shell)](#bash-bourne-again-shell)
  - [CMD (Command Prompt)](#cmd-command-prompt)
  - [PowerShell](#powershell)


Una **shell** è un'interfaccia che permette agli utenti di interagire con il sistema operativo tramite comandi testuali. Le shell possono essere utilizzate per eseguire comandi singoli, script complessi e automazione di compiti ripetitivi. Il termine "shell" deriva dal fatto che essa agisce come un involucro (shell) attorno al kernel del sistema operativo, fornendo un'interfaccia per l'interazione con il sistema.

### Linguaggi di Scripting

#### Bash (Bourne Again Shell)
- **Sistema Operativo**: Principalmente Linux e Unix, ma disponibile anche su macOS e tramite Windows Subsystem for Linux (WSL).
- **Shell**: Bash
- **Linguaggio di Scripting**: Bash scripting
  - Utilizzato per scrivere script di shell (.sh) che possono automatizzare compiti, manipolare file, eseguire comandi di sistema e molto altro.
  - Esempio di script Bash:
    ```bash
    #!/bin/bash
    echo "Hello, World!"
    ```

#### CMD (Command Prompt)
- **Sistema Operativo**: Windows
- **Shell**: CMD
- **Linguaggio di Scripting**: Batch scripting
  - Utilizzato per scrivere script batch (.bat o .cmd) che possono eseguire comandi di sistema, gestire file e directory, e automatizzare compiti su Windows.
  - Esempio di script Batch:
    ```batch
    @echo off
    echo Hello, World!
    ```

#### PowerShell
- **Sistema Operativo**: Windows, ma disponibile anche su Linux e macOS tramite PowerShell Core.
- **Shell**: PowerShell
- **Linguaggio di Scripting**: PowerShell scripting
  - Utilizzato per scrivere script PowerShell (.ps1) che possono eseguire comandi di sistema, gestire file e directory, interagire con API di Windows e .NET, e molto altro.
  - Esempio di script PowerShell:
    ```powershell
    Write-Output "Hello, World!"
    ```
