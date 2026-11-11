"""Leaduri România: saloane de unghii, Târgu Mureș (găsite 2026-11-11). Doar fapte reale din MERO / Google (via ghidestet.com)."""
U = "https://d8j0ntlcm91z4.cloudfront.net/user_3IB0uJbZVPl5lDVYEgoQrDqMOSq/hf_20261111_{}.png"
I_HERO = U.format("060343_a733606a-b3bd-48b6-b6a6-8e1afe0d8905")
I_WORK = U.format("060344_86599e0b-2eb4-4898-ba36-49b64f8eaeae")
I_PEDI = U.format("060343_724d1502-876e-46a7-bbf2-00b74d0926e2")
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def H(mf, sa, su):
    d = {k: mf for k in DAYS[:5]}
    d["Sat"], d["Sun"] = sa, su
    return d


def T(bg, ink, muted, accent, panel, on, display, fonts):
    return dict(bg=bg, ink=ink, muted=muted, accent=accent, panel=panel, on=on, display=display,
                fonts=fonts + "&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")


FR = "Fraunces:opsz,wght@9..144,500;9..144,700"
OU = "Outfit:wght@500;700;800"
BR = "Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800"

SITES = [
  dict(slug="nailsbycristina-targu-mures", name="NailsbyCristina", kind="barber", city="Târgu Mureș",
       address="Strada Regele Ferdinand 10B (Octavia Studio)", zip="Târgu Mureș", phone="0757 262 451",
       rating=4.98, reviews=472, src="MERO", rating2="4,9 pe Google",
       hours={"Mon": "8:45-21:00", "Tue": "8:30-21:00", "Wed": "8:30-21:00", "Thu": "8:30-21:00", "Fri": "8:30-21:00", "Sat": "8:30-14:00", "Sun": None},
       book="https://mero.ro/p/nailsbycristina", cta="Programează-te",
       headline="Unghii impecabile,\nîn Octavia Studio.", lede="Ojă semipermanentă, construcție și întreținere cu gel, pedichiură. Pe Regele Ferdinand, în Târgu Mureș.",
       services=[("Oja semi cu apex", "1 oră 15 min", "96 lei"), ("Pedichiură semi", "1 oră 10 min", "110 lei"),
                 ("Construcție cu gel scurt", "2 ore", "190 lei"), ("Întreținere gel scurt", "1 oră 40 min", "132 lei"),
                 ("Construcție cu gel lung", "2 ore 10 min", "168 lei"), ("Întreținere gel lung", "2 ore", "152 lei")],
       sig=("Nu doar unghiile.", "Clientele revin și pentru atmosferă: servicii rapide, curate, într-un studio cu program lung, de luni până sâmbătă."),
       quotes=[("Servicii impecabile si rapide! De fiecare data o placere sa revin , nu doar pentru unghii ci si pentru atmosfera placuta❤️", "Sara R., MERO"),
               ("Servicii de calitate, atmosfera relaxanta si profesionalism! O adevărată specialistă ❤️", "Emilia C., MERO"),
               ("Recomand cu încredere salonul. Întotdeauna au dat dovada de profesionalism și eficiență.", "Dragos Toma, Google")],
       now="un profil MERO și o pagină de Facebook", photo=I_WORK, photo2=I_PEDI,
       theme=T("#F6F0EC", "#2A1E1C", "#7A6863", "#B5546B", "#EFE5DF", "#FFFFFF", "Fraunces", FR)),
  dict(slug="nirvana-nail-studio-targu-mures", name="NIRVANA Nail Studio", kind="barber", city="Târgu Mureș",
       address="Strada Secerei 22", zip="540498 Târgu Mureș", phone="0751 995 564",
       rating=5.0, reviews=94, src="Google", rating2=None,
       hours=H("7:00-21:00", "7:00-21:00", None),
       book=None, cta="Sună pentru programare",
       headline="Nota 5,0.\nDe la fiecare clientă.", lede="Manichiură, pedichiură și design de unghii pe Strada Secerei, în Târgu Mureș. Deschis de luni până sâmbătă, 7-21.",
       services=[("Manichiură", "Clasică sau semipermanentă", None), ("Pedichiură", "Îngrijire completă", None), ("Design de unghii", "Modele la alegere", None), ("Cursuri", "Pentru viitoare nail artiste", None)],
       sig=("Ieși mai bine decât ai intrat.", "Clientele scriu despre o atmosferă elegantă și relaxantă și despre fete profesioniste, atente la detalii."),
       quotes=[("Recomand din tot sufletul acest salon! Atmosfera este foarte plăcută, iar rezultatele sunt peste așteptări de fiecare dată.", "Andreea Câmpean, Google"),
               ("Deja ma duc la ea de mult timp si de fiecare data cand ies de la manichiura ma simt mai bine.", "Ilinca Loredana, Google"),
               ("Atmosfera este elegantă și relaxantă, iar fetele sunt extrem de profesioniste și atente la detalii.", "Simina Pirlea, Google")],
       now="niciun site", photo=I_WORK, photo2=I_PEDI,
       theme=T("#14121A", "#F2EEF6", "#A79FB3", "#C9A7E8", "#1C1925", "#14121A", "Fraunces", FR)),
  dict(slug="anna-szasz-academy-targu-mures", name="Anna Szasz Academy", kind="barber", city="Târgu Mureș",
       address="Piața Republicii 48", zip="540110 Târgu Mureș", phone="0759 022 388",
       rating=4.9, reviews=74, src="Google", rating2=None, hours=None,
       book=None, cta="Sună pentru detalii",
       headline="Manichiură\nși cursuri, cu Anna.", lede="Manichiură, pedichiură și cursuri de manichiură clasică, gel și întreținere, în Piața Republicii, Târgu Mureș.",
       services=[("Curs de manichiură clasică", "Pentru începătoare", None), ("Curs de gel", "Construcție pas cu pas", None), ("Curs de întreținere", "Tehnica corectă", None), ("Manichiură și pedichiură", "Pentru cliente", None)],
       sig=("Calmă și atentă la detalii.", "Cursantele o descriu pe Anna ca pe un om calm, finuț, gata să ajute în fiecare moment."),
       quotes=[("Anna este o femeie calmă, finuță, atentă la detalii și este gata să vă ajute în fiecare moment", "Cocoară Maria Mădălina, Google"),
               ("mereu acolo sa ma sustina si sa ma indrume spre a da tot ce e mai bun", "Larisa Duma, Google")],
       now="cartonașul de pe Google", photo=I_WORK, photo2=I_HERO,
       theme=T("#F3EFE8", "#1D1B18", "#6B655C", "#A0703A", "#E9E2D6", "#FFFFFF", "Bricolage Grotesque", BR)),
  dict(slug="pedichiura-suzi-targu-mures", name="Taslitchi Zsuzsanna", kind="barber", city="Târgu Mureș",
       address="Strada Călărașilor 51 (în salonul Glowartist)", zip="540044 Târgu Mureș", phone="0770 683 513",
       rating=5.0, reviews=18, src="Google", rating2=None,
       hours=H("8:00-20:00", "8:00-13:00", None),
       book=None, cta="Sună pentru programare",
       headline="Pedichiură complexă,\nfăcută cu grijă.", lede="Pedichiură complexă pe Strada Călărașilor 51, în Târgu Mureș. Programări de luni până sâmbătă.",
       services=[("Pedichiură complexă", "Îngrijire atentă", None), ("Pedichiură", "Clasică", None), ("Consultație", "Spuneți-ne ce vă supără", None)],
       sig=("Atenție la detalii.", "Clientele scriu despre profesionalism, experiență în domeniu și o lucrare făcută foarte fain."),
       quotes=[("Recomand servicile lui Suzi, a lucrat foarte fain si cu siguranta as mai reveni 🥰", "Maria Dragomir, Google"),
               ("Recomand cu încredere! Atenție la detalii, profesionalism și exprență în domeniu 👍🏻♥️", "Raluca Neagu, Google")],
       now="un link de Facebook", photo=I_PEDI, photo2=I_WORK,
       theme=T("#EEF3F1", "#14211D", "#5A6B65", "#2F7A68", "#E1EAE6", "#FFFFFF", "Outfit", OU)),
  dict(slug="salonul-corinne-targu-mures", name="Salonul Corinne", kind="barber", city="Târgu Mureș",
       address="Piața Trandafirilor 53", zip="Târgu Mureș", phone="0740 886 169",
       rating=4.1, reviews=24, src="Google", rating2=None,
       hours=H("8:00-21:00", "8:00-17:00", None),
       book=None, cta="Sună pentru programare",
       headline="Chiar în\nPiața Trandafirilor.", lede="Salon de manichiură și pedichiură în centrul Târgu Mureșului. Deschis de luni până sâmbătă.",
       services=[("Manichiură", "", None), ("Pedichiură", "", None), ("Ojă semipermanentă", "", None)],
       sig=("În centru, cu program lung.", "De luni până vineri 8-21 și sâmbăta 8-17, în Piața Trandafirilor 53."),
       quotes=[("Experiente plăcute, recomand!!", "Angela Gedo, Google")],
       now="un link spre o pagină Google Sites care nu mai funcționează", photo=I_WORK, photo2=I_PEDI,
       theme=T("#FBF4F2", "#2B1A1C", "#7D6466", "#C2405A", "#F3E6E3", "#FFFFFF", "Fraunces", FR)),
  dict(slug="glamorous-center-targu-mures", name="Glamorous Center", kind="barber", city="Târgu Mureș",
       address="Strada Sinaia 3", zip="540527 Târgu Mureș", phone="0728 032 739",
       rating=4.8, reviews=10, src="Google", rating2=None,
       hours=H("9:00-20:00", "9:00-15:00", "9:00-15:00"),
       book=None, cta="Sună pentru programare",
       headline="Unghii, gene\nși machiaj.", lede="Unghii cu gel, extensii de gene, machiaj și remodelare corporală pe Strada Sinaia 3, Târgu Mureș. Deschis 7 zile din 7.",
       services=[("Unghii cu gel", "", None), ("Extensii gene", "", None), ("Machiaj", "", None), ("Remodelare corporală", "", None)],
       sig=("Totul într-un singur loc.", "O locație elegantă, cu personal amabil și profesionist, după cum scriu clientele."),
       quotes=[("Locație elegantă și personal amabil și profesionist", "Carmen vlaicu, Google")],
       now="niciun site", photo=I_WORK, photo2=I_PEDI,
       theme=T("#121212", "#F4EFE6", "#A8A096", "#D4AF6A", "#1B1B1B", "#121212", "Fraunces", FR)),
]

IMG = {s["slug"]: (I_HERO, [I_WORK, I_PEDI], None) for s in SITES}
