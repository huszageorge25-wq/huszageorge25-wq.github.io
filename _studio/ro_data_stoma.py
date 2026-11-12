"""Leaduri România: cabinete stomatologice, Mediaș (găsite 2026-11-12). Doar fapte reale (Google Maps via dentalmap.ro)."""
U = "https://d8j0ntlcm91z4.cloudfront.net/user_3IB0uJbZVPl5lDVYEgoQrDqMOSq/hf_20261112_054814_a185cb55-d059-45cf-a317-eabf11e7419c.png"
PX = "https://images.pexels.com/photos/3845810/pexels-photo-3845810.jpeg?auto=compress&cs=tinysrgb&w=2000"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def T(bg, ink, muted, accent, panel, on, display, fonts):
    return dict(bg=bg, ink=ink, muted=muted, accent=accent, panel=panel, on=on, display=display,
                fonts=fonts + "&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")


FR = "Fraunces:opsz,wght@9..144,500;9..144,700"
OU = "Outfit:wght@500;700;800"
BR = "Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800"

SITES = [
  dict(slug="smile-studio-medias", name="Smile Studio Mediaș", kind="barber", city="Mediaș",
       address="Piața George Enescu 9", zip="Mediaș", phone="0754 910 056",
       rating=4.9, reviews=30, src="Google", rating2=None, hours=None,
       book=None, cta="Sună pentru programare",
       headline="Estetică dentară\nîn centrul Mediașului.", lede="Cabinet de stomatologie și estetică dentară în Piața George Enescu 9, Mediaș. Programări la telefon.",
       services=[("Consultație", "Primul pas: discutăm ce vă doriți", None), ("Estetică dentară", "Pentru un zâmbet de care să fiți mândri", None), ("Stomatologie generală", "Tratamente pentru toată familia", None)],
       sig=("Nota 4,9 de la pacienți.", "Pacienții din Mediaș v-au dat nota 4,9 pe Google."),
       quotes=[], now="niciun site", photo=PX, photo2=U,
       theme=T("#F2F6F7", "#10232A", "#5B6E74", "#1F8A9B", "#E3ECEE", "#FFFFFF", "Fraunces", FR)),
  dict(slug="clinica-dr-micu-medias", name="Clinica Stomatologică Dr. Micu", kind="barber", city="Mediaș",
       address="Strada Mărășești 37", zip="551058 Mediaș", phone="0734 952 118",
       rating=4.5, reviews=20, src="Google", rating2=None, hours=None,
       book=None, cta="Sună pentru programare",
       headline="Stomatologie,\npe Strada Mărășești.", lede="Clinica Stomatologică Dr. Micu, Strada Mărășești 37, Mediaș. Programări la telefon.",
       services=[("Consultație", "Discutăm ce vă supără", None), ("Stomatologie generală", "Tratamente pentru toată familia", None), ("Programare la telefon", "Un click și sunați", None)],
       sig=("Aproape de casă.", "Un cabinet din Mediaș, pe Strada Mărășești 37, unde pacienții vă găsesc ușor."),
       quotes=[], now="o pagină de Facebook", photo=PX, photo2=U,
       theme=T("#F5F3EE", "#1B2430", "#636B75", "#2E6FB0", "#ECE8DF", "#FFFFFF", "Bricolage Grotesque", BR)),
  dict(slug="digixdent-medias", name="DigiXDent", kind="barber", city="Mediaș",
       address="Strada Cloșca 2", zip="551030 Mediaș", phone="0742 042 217",
       rating=5.0, reviews=42, src="Google", rating2=None,
       hours={"Mon": "12:00-18:00", "Tue": "9:00-15:00", "Wed": "9:00-15:00", "Thu": "9:00-15:00", "Fri": "9:00-15:00", "Sat": None, "Sun": None},
       book=None, cta="Sună pentru programare",
       headline="Radiologie dentară\nîn Mediaș.", lede="Radiologie dentară pe Strada Cloșca 2, Mediaș. Luni 12-18, marți-vineri 9-15.",
       services=[("Radiologie dentară", "Radiografii pentru medicul dumneavoastră stomatolog", None), ("Programare la telefon", "Sunați și vă spunem când puteți veni", None)],
       sig=("Nota 5,0 de la pacienți.", "42 de pacienți v-au dat nota 5,0 pe Google."),
       quotes=[], now="niciun site", photo=U, photo2=PX,
       theme=T("#0F1720", "#EEF3F7", "#9AA8B5", "#4FC3D9", "#16212C", "#0F1720", "Outfit", OU)),
]

IMG = {s["slug"]: (s["photo"], [s["photo2"]], None) for s in SITES}
