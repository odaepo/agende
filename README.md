## Introduzione
Questo programma consente di generare un'agenda mensile in formato PDF. Ogni giorno del mese viene rappresentato su una pagina basata su un modello SVG personalizzabile. Il programma permette di specificare il mese e l'anno desiderati, generando un PDF finale contenente tutte le pagine dei giorni del mese selezionato.

## Requisiti
Per eseguire il programma, è necessario avere installati i seguenti pacchetti Python:

- cairosvg (per convertire file SVG in PDF)
- PyPDF2 (per unire i PDF generati)

Per installarli, eseguire il comando:

bash
pip install cairosvg PyPDF2


## Utilizzo

1. Eseguire lo script
   Avviare il programma eseguendo il comando:
   bash
   python script.py
   

2. Inserire i dati richiesti
   Il programma richiede di inserire:
   - Il numero del mese (da 1 a 12)
   - L'anno di riferimento (es. 2025)

3. Generazione dei PDF
   - Per ogni giorno del mese, il programma crea una pagina basata su un file SVG.
   - Il nome del giorno e la data vengono inseriti nel file SVG.
   - Se esiste un file SVG specifico per un giorno della settimana (ad esempio, lunedi.svg per i lunedì), verrà utilizzato quel file; altrimenti, verrà usato un file di default (a.svg).
   - I file PDF temporanei vengono generati e uniti in un unico PDF finale.

4. Risultato finale
   Il file generato avrà il nome agenda_Mese_Anno.pdf (ad esempio, agenda_Febbraio_2025.pdf) e conterrà tutte le pagine dei giorni del mese selezionato.

## Personalizzazione

### Modifica dei Template SVG
Per personalizzare l'aspetto delle pagine dell'agenda, è possibile modificare o aggiungere file SVG:

- Se si desidera un layout specifico per un giorno della settimana, creare un file SVG con il nome corrispondente in minuscolo, ad esempio:
  - lunedi.svg
  - martedi.svg
  - mercoledi.svg

- All'interno del file SVG, il programma sostituirà la stringa "Lunedi' 30 Febbraio 2025" con la data effettiva generata.

- Se un file specifico non è disponibile, il programma utilizzerà il file a.svg come modello di default.

## Risoluzione Problemi

- Errore "Il file X.svg non è stato trovato!"
  - Assicurarsi che il file SVG specifico per il giorno esista nella directory del programma.
  - Se non si vuole usare file specifici per ogni giorno, creare e utilizzare solo a.svg.

- Errore "Valore non valido!" all'inserimento del mese o anno
  - Verificare di aver inserito un numero valido per il mese (1-12) e un anno in formato corretto.

- Il PDF finale non viene creato
  - Controllare se tutti i file SVG richiesti sono presenti e validi.
  - Verificare che cairosvg e PyPDF2 siano installati correttamente.

## Conclusione
Il programma permette di generare agende mensili personalizzate partendo da modelli SVG. Grazie alla possibilità di usare file SVG distinti per ogni giorno della settimana, è possibile ottenere un layout altamente personalizzato per ogni giorno del mese.

