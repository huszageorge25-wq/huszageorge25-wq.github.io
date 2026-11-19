"""Leaduri România: spălătorii auto, Odorheiu Secuiesc (găsite 2026-11-19). Doar fapte reale (date Google Maps prin map24.ro)."""
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
SG = "Space+Grotesk:wght@500;700"

SITES = [
  dict(slug="iker-automoso-odorheiu", name="Iker Autómosó és Autókozmetika", kind="barber", city="Odorheiu Secuiesc",
       address="Strada II Rákóczi Ferenc 177", zip="535600 Odorheiu Secuiesc", phone="0742 161 934",
       rating=4.4, reviews=34, src="Google", rating2=None, hours=H("9:00-17:00", "9:00-15:00", None),
       book=None, cta="Sună pentru programare",
       headline="Mașina curată,\nfără drum degeaba.", lede="Spălătorie și cosmetică auto pe Strada II Rákóczi Ferenc 177, Odorheiu Secuiesc. Luni-vineri 9-17, sâmbătă 9-15. Sunați și vă spunem când puteți veni.",
       services=[("Spălătorie auto", "Sunați și aflați când aveți loc", None), ("Cosmetică auto", "Spuneți-ne ce vreți și vă spunem cât durează", None), ("Sâmbăta deschis", "9:00 - 15:00", None)],
       sig=("Deschis și sâmbăta.", "Clienții v-au dat nota 4,4 pe Google, iar sâmbăta sunteți deschiși până la 15."),
       quotes=[], now="niciun site", photo=PX.format(6873123, 2000), photo2=PX.format(6872146, 1400),
       theme=T("#0E1116", "#EEF2F6", "#97A1AD", "#3BB4F2", "#161B22", "#0E1116", "Outfit", OU)),
  dict(slug="szombatfalvi-automoso-odorheiu", name="Szombatfalvi Autómosó", kind="barber", city="Odorheiu Secuiesc",
       address="Strada Orbán Balázs", zip="535600 Odorheiu Secuiesc", phone="0745 220 742",
       rating=4.5, reviews=18, src="Google", rating2=None,
       hours={"Mon": "9:00-18:00", "Tue": "9:00-18:00", "Wed": "9:00-18:00", "Thu": "9:00-17:00", "Fri": "9:00-18:00", "Sat": "10:00-15:00", "Sun": None},
       book=None, cta="Sună pentru programare",
       headline="Spălătorie auto\npe Orbán Balázs.", lede="Szombatfalvi Autómosó, Strada Orbán Balázs, Odorheiu Secuiesc. Luni-vineri de la 9, sâmbătă 10-15. Sunați înainte și nu mai stați la coadă.",
       services=[("Spălătorie auto", "Sunați și aflați când aveți loc", None), ("Programare la telefon", "Un click și sunați direct", None), ("Sâmbăta deschis", "10:00 - 15:00", None)],
       sig=("Nota 4,5 de la clienți.", "Clienții din Odorheiu Secuiesc v-au dat nota 4,5 pe Google."),
       quotes=[], now="doar pagina de Facebook", photo=PX.format(3354648, 2000), photo2=PX.format(6872572, 1400),
       theme=T("#F2F6F9", "#0D1B2A", "#58697A", "#0A84C6", "#E2EBF2", "#FFFFFF", "Bricolage Grotesque", BR)),
  dict(slug="79-automoso-odorheiu", name="79 Autómosó", kind="barber", city="Odorheiu Secuiesc",
       address="Strada II Rákóczi Ferenc", zip="535600 Odorheiu Secuiesc", phone="0740 892 957",
       rating=4.6, reviews=12, src="Google", rating2=None, hours=H("9:00-18:00", "9:00-16:00", None),
       book=None, cta="Sună pentru programare",
       headline="Spumă, apă,\nși gata.", lede="79 Autómosó, Strada II Rákóczi Ferenc, Odorheiu Secuiesc. Luni-vineri 9-18, sâmbătă 9-16. Sunați și vă spunem când puteți veni.",
       services=[("Spălătorie auto", "Sunați și aflați când aveți loc", None), ("Programare la telefon", "Un click și sunați direct", None), ("Sâmbăta deschis", "9:00 - 16:00", None)],
       sig=("Nota 4,6 de la clienți.", "Clienții v-au dat nota 4,6 pe Google, iar sâmbăta sunteți deschiși până la 16."),
       quotes=[], now="niciun site", photo=PX.format(6872169, 2000), photo2=PX.format(6873088, 1400),
       theme=T("#101010", "#F4F4F2", "#A3A3A0", "#E8402F", "#1A1A1A", "#101010", "Archivo", AR)),
  dict(slug="budvar-automoso-odorheiu", name="Budvár Auto Mosó", kind="barber", city="Odorheiu Secuiesc",
       address="Strada Budvár 7-9", zip="535600 Odorheiu Secuiesc", phone="0742 515 368",
       rating=4.1, reviews=12, src="Google", rating2=None, hours=H("9:00-17:00", "9:00-14:00", None),
       book=None, cta="Sună pentru programare",
       headline="Spălătorie auto\npe Strada Budvár.", lede="Budvár Auto Mosó, Strada Budvár 7-9, Odorheiu Secuiesc. Luni-vineri 9-17, sâmbătă 9-14. Sunați înainte să veniți.",
       services=[("Spălătorie auto", "Sunați și aflați când aveți loc", None), ("Programare la telefon", "Un click și sunați direct", None), ("Sâmbăta deschis", "9:00 - 14:00", None)],
       sig=("Deschis și sâmbăta.", "Sâmbăta sunteți deschiși 9-14, dar cine vă caută pe telefon nu vede asta."),
       quotes=[], now="niciun site", photo=PX.format(6873076, 2000), photo2=PX.format(6872572, 1400),
       theme=T("#F5F3EE", "#1B1A17", "#64615A", "#1F8A5B", "#E9E6DE", "#FFFFFF", "Space Grotesk", SG)),
]

IMG = {s["slug"]: (s["photo"], [s["photo2"]], None) for s in SITES}
