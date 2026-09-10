#!/usr/bin/env python3
"""
Agregar links al PDF sinsaldoflyer.pdf con coordenadas proporcionales.
"""

import pikepdf

PDF_ORIGINAL = "/home/jl/Documentos/Working/CLIENTES/Sin Saldo/Proyecto Final/sinsaldoflyer.pdf"
PDF_SALIDA = "/home/jl/Documentos/Working/CLIENTES/Sin Saldo/Proyecto Final/sinsaldoflyer-links.pdf"

# PDF original que funciona: 559.92 x 960
# PDF nuevo: 347.2 x 434
# Factores: X=0.62, Y=0.452

# Links
LINKS = {
    "spotify": "https://open.spotify.com/track/57H3eQZx3qgBa7sG1pL4lj",
    "instagram": "https://instagram.com/sin_saldo_folklore",
    "youtube": "https://youtube.com/@sinsaldofolklore6547",
    "whatsapp": "https://wa.me/5492664636411",
    "quienes_somos": "https://j0t4web.github.io/sinsaldo/"
}

# Abrir PDF
pdf = pikepdf.open(PDF_ORIGINAL)
page = pdf.pages[0]

print(f"Tamaño: {float(page.MediaBox[2])} x {float(page.MediaBox[3])}")

# Coordenadas proporcionales (factores: X=0.62, Y=0.452)
# PDF original: Spotify/Instagram en y=71.25-123.75, YouTube/WhatsApp en y=15-67.5
# PDF nuevo: multiplicar por 0.452

anotaciones = []

# Spotify (izquierda, fila superior de iconos)
annot = pikepdf.Dictionary(
    Type=pikepdf.Name.Annot,
    Subtype=pikepdf.Name.Link,
    Rect=[13.95, 32.2, 172.05, 55.9],
    Border=[0, 0, 0],
    A=pikepdf.Dictionary(
        Type=pikepdf.Name.Action,
        S=pikepdf.Name.URI,
        URI=LINKS["spotify"]
    )
)
anotaciones.append(annot)
print(f"✅ Spotify: (13.95, 32.2) a (172.05, 55.9)")

# Instagram (derecha, fila superior de iconos)
annot = pikepdf.Dictionary(
    Type=pikepdf.Name.Annot,
    Subtype=pikepdf.Name.Link,
    Rect=[176.7, 32.2, 334.8, 55.9],
    Border=[0, 0, 0],
    A=pikepdf.Dictionary(
        Type=pikepdf.Name.Action,
        S=pikepdf.Name.URI,
        URI=LINKS["instagram"]
    )
)
anotaciones.append(annot)
print(f"✅ Instagram: (176.7, 32.2) a (334.8, 55.9)")

# YouTube (izquierda, fila inferior de iconos)
annot = pikepdf.Dictionary(
    Type=pikepdf.Name.Annot,
    Subtype=pikepdf.Name.Link,
    Rect=[13.95, 6.78, 172.05, 30.5],
    Border=[0, 0, 0],
    A=pikepdf.Dictionary(
        Type=pikepdf.Name.Action,
        S=pikepdf.Name.URI,
        URI=LINKS["youtube"]
    )
)
anotaciones.append(annot)
print(f"✅ YouTube: (13.95, 6.78) a (172.05, 30.5)")

# WhatsApp (derecha, fila inferior de iconos)
annot = pikepdf.Dictionary(
    Type=pikepdf.Name.Annot,
    Subtype=pikepdf.Name.Link,
    Rect=[176.7, 6.78, 334.8, 30.5],
    Border=[0, 0, 0],
    A=pikepdf.Dictionary(
        Type=pikepdf.Name.Action,
        S=pikepdf.Name.URI,
        URI=LINKS["whatsapp"]
    )
)
anotaciones.append(annot)
print(f"✅ WhatsApp: (176.7, 6.78) a (334.8, 30.5)")

# ¿Quiénes somos? (botón central, arriba de los iconos)
# En el PDF original estaría aproximadamente en y=200-250
# Proporcional: y=90-113
annot = pikepdf.Dictionary(
    Type=pikepdf.Name.Annot,
    Subtype=pikepdf.Name.Link,
    Rect=[60, 90, 287, 113],
    Border=[0, 0, 0],
    A=pikepdf.Dictionary(
        Type=pikepdf.Name.Action,
        S=pikepdf.Name.URI,
        URI=LINKS["quienes_somos"]
    )
)
anotaciones.append(annot)
print(f"✅ ¿Quiénes somos?: (60, 90) a (287, 113)")

# Agregar todas las anotaciones
page.Annots = pikepdf.Array(anotaciones)

print(f"\n🔗 Total links: {len(anotaciones)}")

# Guardar
pdf.save(PDF_SALIDA)
pdf.close()

print(f"💾 PDF guardado: {PDF_SALIDA}")
