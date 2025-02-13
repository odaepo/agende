import calendar
import datetime
import os
from cairosvg import svg2pdf
from PyPDF2 import PdfMerger  # Per versioni precedenti di PyPDF2: PdfFileMerger
# pip install cairosvg PyPDF2


def main():
    # Lettura da tastiera di mese e anno
    try:
        mese_input = int(input("Inserisci il numero del mese (1-12): "))
        anno_input = int(input("Inserisci l'anno (es. 2025): "))
    except ValueError:
        print("Valore non valido!")
        return

    # Dizionario dei giorni della settimana in italiano (con la prima lettera maiuscola)
    giorni_settimana = {
        0: "Lunedi'",
        1: "Martedi'",
        2: "Mercoledi'",
        3: "Giovedi'",
        4: "Venerdi'",
        5: "Sabato",
        6: "Domenica"
    }

    # Dizionario dei nomi dei mesi in italiano
    mesi = {
        1: "Gennaio",
        2: "Febbraio",
        3: "Marzo",
        4: "Aprile",
        5: "Maggio",
        6: "Giugno",
        7: "Luglio",
        8: "Agosto",
        9: "Settembre",
        10: "Ottobre",
        11: "Novembre",
        12: "Dicembre"
    }

    # Controlla se il numero del mese è corretto
    if mese_input < 1 or mese_input > 12:
        print("Il numero del mese deve essere compreso tra 1 e 12!")
        return

    # Determina il numero di giorni nel mese
    _, num_days = calendar.monthrange(anno_input, mese_input)

    # Lista per salvare i nomi dei PDF temporanei creati per ogni giorno
    pdf_temp_files = []

    # Elaborazione per ogni giorno del mese
    for giorno in range(1, num_days + 1):
        # Crea l'oggetto data
        data_corrente = datetime.date(anno_input, mese_input, giorno)
        # Ottieni il nome del giorno della settimana
        giorno_sett = giorni_settimana[data_corrente.weekday()]
        # Crea la stringa sostitutiva nel formato richiesto
        nuova_stringa = f"{giorno_sett} {giorno} {mesi[mese_input]} {anno_input}"

        # Leggi il contenuto del file a.svg
        try:
            with open("a.svg", "r", encoding="utf-8") as file_svg:
                contenuto_svg = file_svg.read()
        except FileNotFoundError:
            print("Il file a.svg non è stato trovato!")
            return

        # Sostituisci la stringa segnaposto "Lunedi' 30 Febbraio 2025" con la stringa calcolata
        svg_modificato = contenuto_svg.replace("Lunedi' 30 Febbraio 2025", nuova_stringa)

        # Nome del PDF temporaneo per il giorno corrente
        pdf_temp = f"temp_{giorno:02d}.pdf"

        # Converte l'SVG modificato in PDF
        svg2pdf(bytestring=svg_modificato.encode("utf-8"), write_to=pdf_temp)
        pdf_temp_files.append(pdf_temp)
        print(f"Creato PDF per il giorno {giorno}: {pdf_temp}")

    # Unisce tutti i PDF temporanei in un unico file PDF
    merger = PdfMerger()
    for pdf in pdf_temp_files:
        merger.append(pdf)
    output_pdf = f"agenda_{mesi[mese_input]}_{anno_input}.pdf"
    merger.write(output_pdf)
    merger.close()
    print(f"PDF finale creato: {output_pdf}")

    # Rimuove i file PDF temporanei
    for pdf in pdf_temp_files:
        os.remove(pdf)

if __name__ == "__main__":
    main()
