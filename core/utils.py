
import io
import PyPDF2

def extrair_texto_pdf(file_stream):
    try:
        reader = PyPDF2.PdfReader(file_stream)
        texto = "".join(page.extract_text() for page in reader.pages)
        return texto
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return None