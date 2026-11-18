"""Leaduri România: service auto, Alba Iulia (găsite 2026-11-18). Doar fapte reale (date Google Maps prin map24.ro)."""
PX = "https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w={1}"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def T(bg, ink, muted, accent, panel, on, display, fonts):
    return dict(bg=bg, ink=ink, muted=muted, accent=accent, panel=panel, on=on, display=display,
                fonts=fonts + "&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")


def H(mf, sa, su):
    d = {k: mf for k in DAYS[:5]}
    d["Sat"], d["Sun"] = sa, su
    return d


OU = "Outfit:wght@500;700;800"
BR = "Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800"
AR = "Archivo:wght@500;800;900"

SITES = [
  dict(slug="redcom-service-alba-iulia", name="Redcom Service Auto", kind="barber", city="Alba Iulia",
       address="Strada Făgăraș 2", zip="510002 Alba Iulia", phone="0721 902 053",
       rating=4.4, reviews=56, src="Google", rating2=None, hours=H("9:00-18:00", "9:00-14:00", None),
       book=None, cta="Sună pentru programare",
       headline="Mașina ta,\npe mâini bune.", lede="Redcom, service auto pe Strada Făgăraș 2, Alba Iulia. Luni-vineri 9-18, sâmbătă 9-14. Sunați și vă spunem când puteți veni.",
       services=[("Service auto", "Spuneți-ne ce are mașina și vă spunem când puteți veni", None), ("Programare la telefon", "Un click și sunați direct", None), ("Sâmbăta deschis", "9:00 - 14:00", None)],
       sig=("Deschis și sâmbăta.", "Clienții v-au dat nota 4,4 pe Google, iar sâmbăta sunteți deschiși până la 14."),
       quotes=[], now="un site vechi care nu mai merge (redcom-srl.business.site dă eroare)", photo=PX.format(4489749, 2000), photo2=PX.format(13065690, 1400),
       theme=T("#F3F2EF", "#14171C", "#5E636B", "#D2382B", "#E7E5E0", "#FFFFFF", "Archivo", AR)),
  dict(slug="vali-carmen-tinichigerie-alba-iulia", name="Tinichigerie Vopsitorie Vali & Carmen", kind="barber", city="Alba Iulia",
       address="Strada Călugăreni 8", zip="510378 Alba Iulia", phone="0745 254 700",
       rating=4.6, reviews=29, src="Google", rating2=None, hours=H("8:00-17:00", None, None),
       book=None, cta="Sună pentru o ofertă",
       headline="Tinichigerie și vopsitorie\nîn Alba Iulia.", lede="Tinichigerie și vopsitorie auto pe Strada Călugăreni 8, Alba Iulia. Luni-vineri 8-17. Sunați pentru o ofertă.",
       services=[("Tinichigerie auto", "Spuneți-ne ce s-a întâmplat cu mașina", None), ("Vopsitorie auto", "Ofertă la telefon", None)],
       sig=("Nota 4,6 de la clienți.", "Clienții din Alba Iulia v-au dat nota 4,6 pe Google."),
       quotes=[], now="niciun site", photo=PX.format(4480505, 2000), photo2=PX.format(3807277, 1400),
       theme=T("#0F1318", "#EEF1F4", "#98A2AD", "#F2A93B", "#171D24", "#0F1318", "Outfit", OU)),
  dict(slug="electro-servis-alba-iulia", name="Electro Servis", kind="barber", city="Alba Iulia",
       address="Strada Regimentul V Vânători 3", zip="510158 Alba Iulia", phone="0258 813 474",
       rating=4.3, reviews=53, src="Google", rating2=None, hours=H("9:00-17:00", None, None),
       book=None, cta="Sună pentru programare",
       headline="Service auto,\npe Regimentul V Vânători.", lede="Electro Servis, Strada Regimentul V Vânători 3, Alba Iulia. Luni-vineri 9-17. Sunați și vă programăm.",
       services=[("Service auto", "Spuneți-ne ce are mașina", None), ("Programare la telefon", "Un click și sunați direct", None)],
       sig=("Peste 50 de recenzii.", "Clienții v-au dat nota 4,3 pe Google pentru Electro Servis."),
       quotes=[], now="doar o pagină într-un catalog de service-uri", photo=PX.format(4489732, 2000), photo2=PX.format(4116193, 1400),
       theme=T("#F2F5F8", "#0F1E2E", "#5A6878", "#1D6FD1", "#E3EAF1", "#FFFFFF", "Bricolage Grotesque", BR)),
]

IMG = {s["slug"]: (s["photo"], [s["photo2"]], None) for s in SITES}
