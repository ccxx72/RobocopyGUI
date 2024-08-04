# localization.py

translations = {
    'en': {
        'title': "Robocopy GUI",
        'source': "Source:",
        'destination': "Destination:",
        'browse': "Browse",
        'command_preview': "Command Preview:",
        'run_robocopy': "Run Robocopy",
        'error_title': "Error",
        'error_message': "Please select both source and destination directories.",
        'option_categories': [
            "Copy Options",
            "File Selection Options",
            "Retry Options",
            "Logging Options",
            "Performance Options",
            "Backup Options",
            "Control Options"
        ],
        'language': "Language:",
    },
    'it': {
        'title': "Interfaccia Grafica Robocopy",
        'source': "Sorgente:",
        'destination': "Destinazione:",
        'browse': "Sfoglia",
        'command_preview': "Anteprima Comando:",
        'run_robocopy': "Esegui Robocopy",
        'error_title': "Errore",
        'error_message': "Seleziona sia la directory sorgente che quella di destinazione.",
        'option_categories': [
            "Opzioni di Copia",
            "Opzioni di Selezione File",
            "Opzioni di Ripetizione",
            "Opzioni di Registrazione",
            "Opzioni di Prestazioni",
            "Opzioni di Backup",
            "Opzioni di Controllo"
        ],
        'language': "Lingua:",
    }
}

copy_options = [
    "/S - Copy subdirectories",
    "/E - Copy subdirectories, including empty ones",
    "/Z - Copy files in restartable mode",
    "/B - Copy files in Backup mode",
    "/ZB - Use restartable mode; if access denied, use Backup mode",
    "/COPY:copyflags - Specify the file properties to copy",
    "/DCOPY:T - Copy Directory Timestamps",
    "/SEC - Copy files with security",
    "/COPYALL - Copy all file info",
    "/NOCOPY - Copy no file info",
    "/SECFIX - Fix file security on all files",
    "/TIMFIX - Fix file times on all files",
    "/PURGE - Delete dest files/directories that no longer exist in source",
    "/MIR - Mirror a directory tree",
    "/MOV - Move files",
    "/MOVE - Move files and directories",
    "/A+:[RASHCNET] - Add the given attributes to copied files",
    "/A-:[RASHCNET] - Remove the given attributes from copied files"
]

file_selection_options = [
    "/A - Copy only files with the Archive attribute set",
    "/M - Copy only files with the Archive attribute set and reset it",
    "/IA:[RASHCNETO] - Include only files with any of the given Attributes set",
    "/XA:[RASHCNETO] - Exclude files with any of the given Attributes set",
    "/XF file [file]... - Exclude files matching given names/paths/wildcards",
    "/XD dirs [dirs]... - Exclude directories matching given names/paths",
    "/XC - Exclude changed files",
    "/XN - Exclude newer files",
    "/XO - Exclude older files",
    "/XX - Exclude extra files and directories",
    "/XL - Exclude 'lonely' files and directories",
    "/IS - Include Same files",
    "/IT - Include Tweaked files",
    "/MAX:n - Maximum file size",
    "/MIN:n - Minimum file size",
    "/MAXAGE:n - Maximum file age",
    "/MINAGE:n - Minimum file age",
    "/MAXLAD:n - Maximum last access date",
    "/MINLAD:n - Minimum last access date",
    "/XJ - Exclude junction points"
]

retry_options = [
    "/R:n - Number of retries on failed copies",
    "/W:n - Wait time between retries",
    "/REG - Save /R:n and /W:n in the Registry as default settings",
    "/TBD - Wait for sharenames To Be Defined"
]

logging_options = [
    "/L - List only - don't copy, timestamp or delete any files",
    "/X - Report all eXtra files",
    "/V - Produce verbose output",
    "/TS - Include source file Time Stamps",
    "/FP - Include Full Pathname of files",
    "/BYTES - Print sizes as bytes",
    "/NS - No Size - don't log file sizes",
    "/NC - No Class - don't log file classes",
    "/NFL - No File List - don't log file names",
    "/NDL - No Directory List - don't log directory names",
    "/NP - No Progress - don't display percentage copied",
    "/ETA - Show Estimated Time of Arrival",
    "/LOG:file - Output status to LOG file",
    "/LOG+:file - Output status to LOG file (append)",
    "/UNILOG:file - Output status to LOG file as UNICODE",
    "/UNILOG+:file - Output status to LOG file as UNICODE (append)",
    "/TEE - Output to console window, as well as the log file",
    "/NJH - No Job Header",
    "/NJS - No Job Summary",
    "/JOB:jobname - Take parameters from the named JOB file",
    "/SAVE:jobname - SAVE parameters to the named job file",
    "/QUIT - QUIT after processing command line",
    "/NOSD - No Source Directory is specified",
    "/NODD - No Destination Directory is specified",
    "/IF - Include the following Files"
]

performance_options = [
    "/MT[:n] - Do multi-threaded copies with n threads",
    "/RH:hhmm-hhmm - Run Hours",
    "/PF - Check run hours on a Per File basis"
]

backup_options = [
    "/B - Copy files in Backup mode",
    "/ZB - Use restartable mode; if access denied, use Backup mode",
    "/EFSRAW - Copy all encrypted files in EFS RAW mode"
]

control_options = [
    "/SECFIX - Fix file security on all files",
    "/TIMFIX - Fix file times on all files",
    "/CREATE - Create directory tree and zero-length files only",
    "/DST - Compensate for one-hour DST time differences",
    "/PURGE - Delete dest files/directories that no longer exist in source",
    "/MIR - Mirror a directory tree",
    "/MOV - Move files",
    "/MOVE - Move files and directories",
    "/A+:[RASHCNET] - Add the given attributes to copied files",
    "/A-:[RASHCNET] - Remove the given attributes from copied files"
]

# Italian translations for the options
copy_options_it = [
    "/S - Copia sottodirectory",
    "/E - Copia sottodirectory, incluse quelle vuote",
    "/Z - Copia file in modalità riavviabile",
    "/B - Copia file in modalità Backup",
    "/ZB - Usa modalità riavviabile; se accesso negato, usa modalità Backup",
    "/COPY:copyflags - Specifica le proprietà dei file da copiare",
    "/DCOPY:T - Copia i timestamp delle directory",
    "/SEC - Copia i file con sicurezza",
    "/COPYALL - Copia tutte le informazioni dei file",
    "/NOCOPY - Non copiare le informazioni dei file",
    "/SECFIX - Correggi la sicurezza dei file su tutti i file",
    "/TIMFIX - Correggi i tempi dei file su tutti i file",
    "/PURGE - Elimina i file/directory di destinazione non più esistenti nella sorgente",
    "/MIR - Specchia una struttura di directory",
    "/MOV - Sposta i file",
    "/MOVE - Sposta file e directory",
    "/A+:[RASHCNET] - Aggiungi gli attributi dati ai file copiati",
    "/A-:[RASHCNET] - Rimuovi gli attributi dati dai file copiati"
]

file_selection_options_it = [
    "/A - Copia solo i file con l'attributo Archivio impostato",
    "/M - Copia solo i file con l'attributo Archivio impostato e lo reimposta",
    "/IA:[RASHCNETO] - Includi solo i file con uno degli attributi dati impostati",
    "/XA:[RASHCNETO] - Escludi i file con uno degli attributi dati impostati",
    "/XF file [file]... - Escludi i file corrispondenti ai nomi/percorsi/caratteri jolly dati",
    "/XD dirs [dirs]... - Escludi le directory corrispondenti ai nomi/percorsi dati",
    "/XC - Escludi i file modificati",
    "/XN - Escludi i file più recenti",
    "/XO - Escludi i file più vecchi",
    "/XX - Escludi file e directory extra",
    "/XL - Escludi file e directory 'solitari'",
    "/IS - Includi i file uguali",
    "/IT - Includi i file modificati",
    "/MAX:n - Dimensione massima del file",
    "/MIN:n - Dimensione minima del file",
    "/MAXAGE:n - Età massima del file",
    "/MINAGE:n - Età minima del file",
    "/MAXLAD:n - Data massima di ultimo accesso",
    "/MINLAD:n - Data minima di ultimo accesso",
    "/XJ - Escludi i punti di giunzione"
]

retry_options_it = [
    "/R:n - Numero di tentativi per le copie fallite",
    "/W:n - Tempo di attesa tra i tentativi",
    "/REG - Salva /R:n e /W:n nel Registro come impostazioni predefinite",
    "/TBD - Attendi che i nomi condivisi siano definiti"
]

logging_options_it = [
    "/L - Solo elenco - non copiare, timbrare o eliminare alcun file",
    "/X - Riporta tutti i file eXtra",
    "/V - Produci output dettagliato",
    "/TS - Includi i timestamp dei file sorgente",
    "/FP - Includi il percorso completo dei file",
    "/BYTES - Stampa le dimensioni in byte",
    "/NS - No Size - non registrare le dimensioni dei file",
    "/NC - No Class - non registrare le classi dei file",
    "/NFL - No File List - non registrare i nomi dei file",
    "/NDL - No Directory List - non registrare i nomi delle directory",
    "/NP - No Progress - non visualizzare la percentuale copiata",
    "/ETA - Mostra il tempo stimato di arrivo",
    "/LOG:file - Output dello stato su file LOG",
    "/LOG+:file - Output dello stato su file LOG (aggiungi)",
    "/UNILOG:file - Output dello stato su file LOG come UNICODE",
    "/UNILOG+:file - Output dello stato su file LOG come UNICODE (aggiungi)",
    "/TEE - Output sulla finestra della console, oltre che sul file di log",
    "/NJH - No Job Header",
    "/NJS - No Job Summary",
    "/JOB:jobname - Prendi i parametri dal file JOB nominato",
    "/SAVE:jobname - SALVA i parametri nel file job nominato",
    "/QUIT - ESCI dopo l'elaborazione della riga di comando",
    "/NOSD - Nessuna Directory Sorgente specificata",
    "/NODD - Nessuna Directory Destinazione specificata",
    "/IF - Includi i seguenti File"
]

performance_options_it = [
    "/MT[:n] - Esegui copie multi-thread con n thread",
    "/RH:hhmm-hhmm - Ore di esecuzione",
    "/PF - Controlla le ore di esecuzione su base Per File"
]

backup_options_it = [
    "/B - Copia i file in modalità Backup",
    "/ZB - Usa modalità riavviabile; se accesso negato, usa modalità Backup",
    "/EFSRAW - Copia tutti i file crittografati in modalità EFS RAW"
]

control_options_it = [
    "/SECFIX - Correggi la sicurezza dei file su tutti i file",
    "/TIMFIX - Correggi i tempi dei file su tutti i file",
    "/CREATE - Crea solo la struttura della directory e file di lunghezza zero",
    "/DST - Compensa le differenze di un'ora per l'ora legale",
    "/PURGE - Elimina i file/directory di destinazione non più esistenti nella sorgente",
    "/MIR - Specchia una struttura di directory",
    "/MOV - Sposta i file",
    "/MOVE - Sposta file e directory",
    "/A+:[RASHCNET] - Aggiungi gli attributi dati ai file copiati",
    "/A-:[RASHCNET] - Rimuovi gli attributi dati dai file copiati"
]

# Group all options for easier access
robocopy_options = {
    'en': [copy_options, file_selection_options, retry_options, logging_options, performance_options, backup_options, control_options],
    'it': [copy_options_it, file_selection_options_it, retry_options_it, logging_options_it, performance_options_it, backup_options_it, control_options_it]
}