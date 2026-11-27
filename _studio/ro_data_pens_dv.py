"""Leaduri România: pensiuni, Deva (găsite 2026-11-27). Doar fapte reale de pe profilul Google Business al afacerii."""
PX = "https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w={1}"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def T(bg, ink, muted, accent, panel, on, display, fonts):
    return dict(bg=bg, ink=ink, muted=muted, accent=accent, panel=panel, on=on, display=display,
                fonts=fonts + "&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")


FR = "Fraunces:opsz,wght@9..144,500;9..144,700"

SITES = [
  dict(slug="villa-brussels-deva", name="Villa Brussels", kind="barber", city="Deva",
       address="Strada Mihai Eminescu nr. 56", zip="330172 Deva, Hunedoara", phone="0721 661 572",
       rating=4.8, reviews=652, src="Google", rating2=None,
       hours={d: "0:00-23:59" for d in DAYS},
       book=None, cta="Rezervă direct, la telefon",
       headline="Pensiune în centrul Devei.\nRezervați direct.", lede="Villa Brussels, Strada Mihai Eminescu 56, Deva. 14 camere, unele cu balcon, mic dejun și parcare privată incluse în preț. Recepție deschisă non-stop.",
       menu_title="Camere și facilități",
       need="Nu vede dintr-o privire camerele, prețul direct și un buton de rezervare, așa că rezervă prin platforme, unde plătiți comision, sau la altă pensiune.",
       menu_note="Pe site-ul final aici intră camerele cu poze, prețurile directe și formularul de rezervare, ca oaspeții să rezerve direct la voi, nu prin platforme.",
       services=[("14 camere", "Aerisite, unele cu balcon", None), ("Mic dejun inclus", "Inclus în prețul cazării", None),
                 ("Parcare privată", "Inclusă în prețul cazării", None), ("Cafenea și terasă", "La pensiune", None),
                 ("Vorbim limbile", "Română, engleză, franceză, italiană", None), ("Recepție non-stop", "Deschis 24 de ore", None)],
       sig=("Nota 4,8 de la oaspeți.", "Oaspeții scriu despre camere curate, liniștite și primitoare, în centrul Devei, cu statuia Manneken Pis în curte."),
       quotes=[("O locatie foarte frumoasa, curata si primitoare", "Vassilion Daniel, Google"),
               ("Totul a fost la superlativ", "Janet AnaMaria Pitulice, Google"),
               ("Camera a fost curată, confortabilă și liniștită", "Daria Brinda, Google")],
       now="cartonașul de pe Google și platformele de rezervări", photo=PX.format(271624, 2000), photo2=PX.format(164595, 1400),
       theme=T("#F4F0E8", "#1E1B16", "#6A6358", "#8A5A2B", "#EAE3D6", "#FFFFFF", "Fraunces", FR)),
]
