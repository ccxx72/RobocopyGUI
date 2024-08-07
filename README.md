RobocopyGUI è un'interfaccia grafica utente (GUI) per il comando Robocopy di Windows. Robocopy (Robust File Copy) è un potente strumento da riga di comando per operazioni avanzate di copia e sincronizzazione dei file. Questa GUI semplifica l'utilizzo di Robocopy, offrendo un'interfaccia intuitiva e user-friendly.

Caratteristiche principali
1.	Interfaccia multilingua: Supporto per inglese e italiano, facilmente espandibile ad altre lingue.
2.	Selezione semplificata di sorgente e destinazione: Interfaccia grafica per la selezione delle cartelle.
3.	Opzioni Robocopy organizzate: Le numerose opzioni di Robocopy sono organizzate in categorie per una facile navigazione.
4.	Anteprima del comando: Visualizzazione in tempo reale del comando Robocopy che verrà eseguito.
5.	Esecuzione diretta: Possibilità di eseguire il comando Robocopy direttamente dall'interfaccia.
6.	Feedback visivo: Barra di stato per informazioni sull'esecuzione del comando.
7.	Design moderno: Utilizzo di temi moderni per un'esperienza utente migliorata.
8.	Tooltips: Suggerimenti contestuali per una migliore comprensione delle funzionalità.

Funzionalità tecniche

•	Tkinter e ttk: Utilizzo di Tkinter per la GUI di base e ttk per widget di stile moderno.

•	ttkthemes: Implementazione di temi moderni per migliorare l'aspetto dell'applicazione.

•	Localizzazione: Sistema di localizzazione basato su dizionari per supporto multilingua.

•	Subprocess: Utilizzo del modulo subprocess per l'esecuzione sicura dei comandi Robocopy.

•	Gestione degli errori: Cattura e visualizzazione degli errori durante l'esecuzione di Robocopy.

•	Layout dinamico: Interfaccia ridisegnabile per adattarsi ai cambiamenti di lingua.

•	Selezione multipla: Utilizzo di Listbox per la selezione multipla delle opzioni Robocopy.



Istruzioni per l'installazione e l'esecuzione
1.	Requisiti di sistema: 
o	Windows 10 o superiore (Robocopy è incluso in Windows)
o	Python 3.6 o superiore
2.	Installazione di Python: 
o	Scarica e installa Python da python.org
o	Durante l'installazione, assicurati di selezionare l'opzione "Add Python to PATH"
3.	Installazione delle dipendenze: 
o	Apri il prompt dei comandi o PowerShell
o	Esegui il seguente comando: 
		pip install ttkthemes
4.	Preparazione dei file: 
o	Crea una cartella per il progetto, ad esempio "RobocopyGUI"
o	Salva i file rcgui.py e localization.py nella cartella del progetto
5.	Esecuzione del programma: 
o	Apri il prompt dei comandi o PowerShell
o	Naviga alla cartella del progetto: 
		cd percorso\alla\cartella\RobocopyGUI
o	Esegui il programma con il comando: 
		python rcgui.py
6.	Utilizzo: 
o	Seleziona la lingua desiderata dal menu a tendina
o	Usa i pulsanti "Browse" per selezionare le cartelle sorgente e destinazione
o	Seleziona le opzioni Robocopy desiderate dalle varie schede
o	Controlla l'anteprima del comando nella parte inferiore della finestra
o	Clicca su "Run Robocopy" per eseguire il comando
7.	Risoluzione dei problemi: 
o	Se ricevi un errore relativo a moduli mancanti, assicurati di aver installato correttamente ttkthemes
o	In caso di problemi con l'esecuzione di Robocopy, verifica di avere i permessi necessari per le cartelle selezionate
