"""Leaduri România: restaurante, Sibiu (găsite 2026-11-13). Doar fapte reale (date Google prin Wanderlog, In Your Pocket, travelpal)."""
H = "https://d2ol7oe51mr4n9.cloudfront.net/user_3IB0uJbZVPl5lDVYEgoQrDqMOSq/{}.jpg"
P = "https://d8j0ntlcm91z4.cloudfront.net/user_3IB0uJbZVPl5lDVYEgoQrDqMOSq/hf_20261109_{}.png"
# poze exemplu refolosite (deja găzduite), marcate „Poză exemplu” în pagină
VOY = (H.format("c429634a-0bff-4f8d-ba85-9a9a83018c80"), [P.format("100542_ca789888-a0ef-41e9-8497-c95a33d42364")], P.format("100541_eb848b90-a300-46b0-866b-23114648bb5f"))
VIN = (H.format("53c8acc7-1003-4db1-9c84-2d28499328b2"), [P.format("100650_d7bd79a0-02f4-4610-b58e-c3f26e012346")], P.format("100647_432922dd-b13e-4403-b14b-450737322089"))
POP = (H.format("2f0d9247-ec7d-4536-bfd0-67cd57d883d8"), [P.format("100648_53a9641c-41ca-4402-ab27-830e7a68ed46")], P.format("100647_8fa378ff-bf31-49df-b723-0d68b8bfcc4f"))
GAL = (H.format("847cb5fb-17ed-4e20-99c1-4613a5e82f11"), [P.format("100542_ef36bf1e-fb12-4155-85f6-a50191946991")], P.format("100543_fffc6820-bb07-436d-b794-56a215fe0ff1"))
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def T(bg, ink, muted, accent, panel, on, display, fonts):
    return dict(bg=bg, ink=ink, muted=muted, accent=accent, panel=panel, on=on, display=display,
                fonts=fonts + "&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")


FR = "Fraunces:opsz,wght@9..144,500;9..144,700"
OU = "Outfit:wght@500;700;800"
BR = "Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800"
ALL = lambda h: {d: h for d in DAYS}

SITES = [
  dict(slug="la-cuptor-sibiu", name="La Cuptor", kind="cafe", city="Sibiu",
       address="Strada 9 Mai 7", zip="Sibiu", phone="0743 897 964",
       rating=4.6, reviews=4799, src="Google", rating2=None,
       hours={"Mon": "14:00-23:00", "Tue": "14:00-23:00", "Wed": "14:00-23:00", "Thu": "14:00-23:00", "Fri": "13:00-23:45", "Sat": "13:00-23:45", "Sun": "13:00-23:00"},
       book=None, cta="Rezervă o masă",
       headline="Din cuptor,\npe Strada 9 Mai.", lede="Restaurant La Cuptor, Strada 9 Mai 7, Sibiu. Cocoș de munte la cuptor, pulpe de rață crocante, pâine cu maia.",
       services=[("Cocoș de munte la cuptor", "Cu înghețată de usturoi negru", None), ("Pulpe de rață crocante", None, None), ("Măduvă la cuptor", None, None), ("Pâine cu maia", None, None), ("Limonade artizanale", None, None)],
       sig=("Aproape 4.800 de recenzii.", "Oaspeții din Sibiu și turiștii v-au dat nota 4,6 pe Google."),
       quotes=[], now="o pagină de Facebook", photo=VOY[0], photo2=VOY[2],
       theme=T("#F6EFE6", "#2A1A12", "#7A6656", "#B5502A", "#EEE3D4", "#FFFFFF", "Fraunces", FR)),
  dict(slug="la-arhive-sibiu", name="La Arhive", kind="cafe", city="Sibiu",
       address="Strada Arhivelor 1", zip="Sibiu", phone="0771 539 530",
       rating=4.4, reviews=1735, src="Google", rating2=None, hours=ALL("11:00-23:00"),
       book=None, cta="Rezervă o masă",
       headline="Bucătărie românească,\nla Arhive.", lede="Restaurant La Arhive, Strada Arhivelor 1, Sibiu. Deschis zilnic 11:00-23:00.",
       services=[("Ciorbă rădăuțeană", None, None), ("Ciulama de ciuperci", None, None), ("Mici", None, None), ("Varză acră", None, None), ("Pizza", None, None)],
       sig=("Peste 1.700 de recenzii.", "Clienții v-au dat nota 4,4 pe Google pentru mâncarea românească de la Arhive."),
       quotes=[], now="niciun site", photo=POP[0], photo2=POP[2],
       theme=T("#F3F1EA", "#1E2A22", "#66705F", "#7A8F3A", "#E7E4D6", "#FFFFFF", "Bricolage Grotesque", BR)),
  dict(slug="crama-sibiana-sibiu", name="Crama Sibiană", kind="cafe", city="Sibiu",
       address="Piața Mică 31", zip="Sibiu", phone="0729 614 260",
       rating=4.0, reviews=2475, src="Google", rating2=None, hours=ALL("12:00-23:55"),
       book=None, cta="Rezervă o masă",
       headline="Cramă românească\nîn Piața Mică.", lede="Crama Sibiană, Piața Mică 31, Sibiu. Sărmăluțe, mititei, ciorbă în pâine și papanași. Deschis zilnic de la 12:00.",
       services=[("Sărmăluțe cu mămăligă", None, None), ("Ciorbă în pâine", None, None), ("Mititei", None, None), ("Mămăligă cu brânză și smântână", None, None), ("Papanași", None, None), ("Afinată", None, None)],
       sig=("În inima Sibiului.", "O cramă în Piața Mică, cu peste 2.400 de recenzii pe Google."),
       quotes=[], now="o pagină de Facebook", photo=VIN[0], photo2=VIN[2],
       theme=T("#1A1210", "#F3E9DF", "#B3A091", "#C8873A", "#241915", "#1A1210", "Fraunces", FR)),
  dict(slug="tango-restaurant-sibiu", name="Tango Restaurant & Pub", kind="cafe", city="Sibiu",
       address="Piața Mică 23", zip="Sibiu", phone="0754 709 373",
       rating=4.3, reviews=1496, src="Google", rating2=None, hours=ALL("11:00-23:00"),
       book=None, cta="Rezervă o masă",
       headline="Pizza mare\nîn Piața Mică.", lede="Tango Restaurant & Pub, Piața Mică 23, Sibiu. Bucătărie italiană, pizza și burgeri, muzică live joia.",
       services=[("Pizza", "Pizza mare, lăudată de clienți", None), ("Paste și preparate italiene", None, None), ("Burgeri", None, None), ("Muzică live", "Joia seara", None)],
       sig=("Aproape 1.500 de recenzii.", "Clienții v-au dat nota 4,3 pe Google pentru Tango din Piața Mică."),
       quotes=[], now="o pagină de Facebook", photo=GAL[0], photo2=GAL[2],
       theme=T("#101418", "#EEF1F4", "#9AA4AE", "#E0453A", "#182027", "#FFFFFF", "Outfit", OU)),
]

IMG = {"la-cuptor-sibiu": VOY, "la-arhive-sibiu": POP, "crama-sibiana-sibiu": VIN, "tango-restaurant-sibiu": GAL}
