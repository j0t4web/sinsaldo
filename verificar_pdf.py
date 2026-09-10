#!/usr/bin/env python3
import fitz

pdf_path = "/home/jl/Documentos/Working/CLIENTES/Sin Saldo/Proyecto Final/sinsaldoflyer.pdf"
doc = fitz.open(pdf_path)
page = doc[0]

print(f"Tamaño de página: {page.rect}")
print(f"Ancho: {page.rect.width}, Alto: {page.rect.height}")

# Verificar si ya hay links
links = page.get_links()
print(f"\nLinks existentes: {len(links)}")
for link in links:
    print(f"  - {link}")

doc.close()
