#!/usr/bin/env python3
"""Storefront Studio România: propuneri premium (concepts/<slug>/index.html).

Usage: python3 _studio/ro_pro.py [slug ...]
Doar fapte reale: telefon, adresă, program, rating și recenzii de pe Google Maps / MERO / Fresha.
Pozele generate sunt marcate „Poză exemplu”.
"""
import html, json, os, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: html.escape(str(s), quote=True)
PX = "https://images.pexels.com/photos/{0}/pexels-photo-{0}.jpeg?auto=compress&cs=tinysrgb&w={1}"
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3IB0uJbZVPl5lDVYEgoQrDqMOSq/hf_20261109_{}.png"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
ZI = {"Mon": "Luni", "Tue": "Marți", "Wed": "Miercuri", "Thu": "Joi", "Fri": "Vineri", "Sat": "Sâmbătă", "Sun": "Duminică"}
EMAIL = "huszageorge25@gmail.com"


def img(x, w=1600):
    return PX.format(x, w) if isinstance(x, int) else x


def H(mf, sa, su):
    """mf = Luni-Vineri, sa = Sâmbătă, su = Duminică ("9:00-20:00" sau None)."""
    d = {k: mf for k in DAYS[:5]}
    d["Sat"], d["Sun"] = sa, su
    return d


SITES = [
  dict(slug="kron-barber-shop-brasov", name="Kron Barber Shop", kind="barber", city="Brașov",
       address="Strada Crișului 18A (Cosmopolit, lângă Magnolia)", zip="500283 Brașov", phone="0748 613 027",
       rating=4.8, reviews=551, src="Google", rating2="4,99 pe MERO, din 5.585 de evaluări",
       hours={"Mon": "9:00-20:00", "Tue": "9:00-20:00", "Wed": "9:00-20:00", "Thu": "9:00-19:00", "Fri": "9:00-20:00", "Sat": "9:00-20:00", "Sun": None},
       book="https://mero.ro/p/thedenbarbershop", cta="Programează-te",
       headline="Kron life,\npe Crișului.", lede="Tuns, barbă și prosop fierbinte în Cosmopolit, Brașov. Programare online, direct pe MERO.",
       services=[("Tuns + spălat", "45 min - 1 oră", "100-110 lei"), ("Tuns, barbă + spălat", "1 oră - 1 oră 20 min", "130-140 lei"),
                 ("Aranjat barbă", "20-30 min", "60-70 lei"), ("Tuns student", "1 oră", "80 lei"), ("Special package", "1 oră 30 min", "250 lei")],
       sig=("Special package.", "Tuns personalizat, barbă conturată, spălat, sprâncene, prosop fierbinte și frecție a scalpului. O oră și jumătate doar pentru tine."),
       quotes=[("Totul a decurs conform așteptărilor, oameni faini, amabili, profesioniști.", "Dorin T., MERO"),
               ("Un om minunat, sociabil și profesionist. Tot respectul și sigur voi reveni.", "Denis M., MERO"),
               ("Great atmosphere. Great barbers. Great prices. Highly recommended.", "Alex Cracut, Google")],
       now="un profil MERO", photo=2881253, photo2=1813272,
       theme=dict(bg="#0E1116", ink="#F1EDE6", muted="#9AA3AE", accent="#C9A227", panel="#161B22", on="#0E1116",
                  display="Archivo", fonts="Archivo:wdth,wght@62..125,500;125,800;125,900&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="125%")),
  dict(slug="bandit-barbers-cluj", name="Bandit Barbers", kind="barber", city="Cluj-Napoca",
       address="Strada Gheorghe Șincai 12", zip="400004 Cluj-Napoca", phone="0744 227 237",
       rating=4.9, reviews=2761, src="Google", rating2="5,0 pe Fresha, din 1.805 voturi",
       hours=H("10:00-20:00", "10:00-20:00", "10:00-20:00"),
       book="https://www.fresha.com/a/bandit-barbers-cluj-napoca-strada-gheorghe-sincai-12-kdugyl6t", cta="Programează-te",
       headline="Fade perfect.\nȘapte zile pe săptămână.", lede="Barbershop pe Gheorghe Șincai, deschis zilnic 10-20. Copiii și cățeii sunt bineveniți.",
       services=[("Tuns și aranjat de barbă", "1 oră", "de la 110 lei"), ("Tuns", "Clasic sau modern", None), ("Aranjat barbă", "Contur și formă", None)],
       sig=("Copii și câini, bineveniți.", "Pe Fresha, salonul e trecut ca prietenos cu copiii și cu animalele de companie, aproape de transportul public, cu confirmare instant a programării."),
       quotes=[("Had a perfect fade cut for a super decent price! Very chic interior and nice ambience.", "Ruben van S, Google"),
               ("Atent, serios, un băiat de nota 10! Un profesionist adevărat!", "Lucian V, Fresha"),
               ("Best haircut I've ever had. Cool, clean, great service.", "George Howells, Google")],
       now="o pagină Fresha (banditbarbers.ro trimite direct acolo)", photo=7697642, photo2=3998429,
       theme=dict(bg="#F3F1EC", ink="#141414", muted="#5E5A55", accent="#C8302C", panel="#E8E4DC", on="#FFFFFF",
                  display="Bricolage Grotesque", fonts="Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")),
  dict(slug="mk-studio-barbershop-brasov", name="MK Studio Barbershop", kind="barber", city="Brașov",
       address="Strada Molnar Janos 20, Bloc 50", zip="500466 Brașov", phone="0768 143 385",
       rating=4.6, reviews=204, src="Google", rating2=None,
       hours=H("10:00-19:00", "9:00-15:00", None),
       book=None, cta="Sună pentru programare",
       headline="Tunsoarea ta,\nfăcută cu răbdare.", lede="Frizerie de cartier pe Molnar Janos, în Brașov. Pentru tine și pentru cel mic.",
       services=[("Tuns bărbați", "Clasic sau modern", None), ("Tuns copii", "Băieții vin cu tata", None), ("Barbă", "Contur și formă", None)],
       sig=("Vii cu băiatul? Perfect.", "Un client a venit cu fiul lui și au plecat amândoi mulțumiți. Exact pentru asta e o frizerie de cartier."),
       quotes=[("My son and I got haircuts here. We were very happy with the work of both barbers.", "Vitalii Skaletskyi, Google"),
               ("Nice and warm environment, friendly atmosphere and above all, professional service.", "Constantin Varzari, Google"),
               ("Great service! Very happy with my haircut!", "Gabriel L., Google")],
       now="o pagină de Facebook", photo=1570807, photo2=7518738,
       theme=dict(bg="#EEF1EE", ink="#16201B", muted="#5A6660", accent="#2F6B4F", panel="#E1E7E2", on="#FFFFFF",
                  display="Outfit", fonts="Outfit:wght@500;700;800&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")),
  dict(slug="aa-barber-sibiu", name="A'A Barber", kind="barber", city="Sibiu",
       address="Strada Luptei 19", zip="550330 Sibiu", phone="0725 168 726",
       rating=4.9, reviews=180, src="Google", rating2="4,99 pe MERO, din 4.621 de evaluări",
       hours=H("9:00-20:00", "8:00-16:00", None),
       book="https://mero.ro/p/frizeria-fin", cta="Programează-te",
       headline="Tunsoare bună,\nfără grabă.", lede="Frizerie pe Strada Luptei 19, Sibiu. Alegi serviciul și frizerul, apoi te programezi online.",
       services=[("Tuns modern, spălat și aranjat", "40-45 min", "70-75 lei"), ("Tuns modern, barbă, spălat și aranjat", "1 oră", "85-90 lei"),
                 ("Barbă", "20-30 min", "30-50 lei"), ("Tunsoare din foarfecă", "1 oră", "100 lei")],
       sig=("Trei frizeri. Peste 4.600 de evaluări.", "Alexandru-Alberto Surupăceanu, Sergiu Constantin Drăghici și Călin Mihaiu. Toți trei au nota 4,99 pe MERO. Clădirea albă, nouă, pe dreapta."),
       quotes=[("Foarte serioși și lucrează frumos.", "Bogdan B., MERO"), ("Profesionist!", "Ciprian G., MERO"), ("Cel mai bun frizer.", "Andreas C., MERO")],
       now="un profil MERO", photo=CF.format("095743_b855c145-eb67-4b88-be7c-63ee30958c1f"), photo2=CF.format("095742_61792373-d4c7-4470-82fd-1e197346f80e"),
       theme=dict(bg="#EEF0F2", ink="#16191D", muted="#5B626B", accent="#2F4FB5", panel="#E3E7F2", on="#FFFFFF",
                  display="Cabinet Grotesk", fonts="Inter+Tight:wght@400;500;600", fontshare="cabinet-grotesk@700,800", body="Inter Tight", stretch="100%")),
  dict(slug="piaf-cafe-targu-mures", name="Piaf Cafe", kind="cafe", city="Târgu Mureș",
       address="Strada Bolyai 10", zip="540064 Târgu Mureș", phone="0771 525 526",
       rating=4.4, reviews=1419, src="Google", rating2=None, hours=None,
       book=None, cta="Rezervă o masă",
       headline="Brunch pe o stradă\nliniștită din centru.", lede="Cafenea și brunch pe Strada Bolyai 10, la două minute de centru. La masă, la pachet sau cu livrare.",
       services=[("Brunch", "Servit la masă sau pe terasă", None), ("Burgeri", "Lăudați de clienți", None), ("Cafea", "Mare și bună, zic clienții", None), ("La pachet și livrare", "Ridicare de la local sau livrare", None)],
       sig=("Terasa de pe Bolyai.", "Terasa e chiar pe stradă, una liniștită, la 2-3 minute de centru. Locul perfect pentru o cafea lungă."),
       quotes=[("The place is very beautiful. The fact that it has a terrace on the street is another charm.", "Dr. Radu Balanean, Google"),
               ("Great burgers and friendly staff.", "Ondrej Radič Čierny, Google"),
               ("They surprised me with the coffee, which was huge and tasty too.", "Adriana Dumitrof, Google")],
       now="niciun site", photo=CF.format("100542_404dc6e5-db3c-496d-9a43-8a9ede56d90b"), photo2=CF.format("100541_5b048852-34cc-4277-9c92-5d0c8e021848"),
       theme=dict(bg="#FBF2EF", ink="#2B1B1E", muted="#7A6266", accent="#C2405A", panel="#F4E2DE", on="#FFFFFF",
                  display="Bricolage Grotesque", fonts="Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")),
  dict(slug="scarlet-cafe-targu-mures", name="Scarlet Cafe", kind="cafe", city="Târgu Mureș",
       address="Piața Teatrului 6", zip="540046 Târgu Mureș", phone="0770 940 972",
       rating=4.4, reviews=861, src="Google", rating2=None,
       hours={"Mon": "8:00-00:00", "Tue": "8:00-00:00", "Wed": "8:00-00:00", "Thu": "8:00-00:00", "Fri": "8:00-01:00", "Sat": "9:00-01:00", "Sun": "9:00-00:00"},
       book=None, cta="Rezervă o masă",
       headline="Cafea pe\nPiața Teatrului.", lede="În centrul Târgu Mureșului, de la 8 dimineața până după miezul nopții. Cafea, mâncare și băuturi.",
       services=[("Cafea", "De dimineață până noaptea", None), ("Mâncare", "Bruschete, sandvișuri și altele", None), ("Băuturi", "Pentru seara în oraș", None)],
       sig=("Deschis până la 1 noaptea.", "Vineri și sâmbătă stăm deschiși până la 1. În restul zilelor, până la miezul nopții. Chiar în centru."),
       quotes=[("Great place in Targu Mures. It is very central. The service was very good, the food was great and so were the drinks and coffee.", "Flavy T, Google"),
               ("Nice place with a cozy atmosphere right in the center of Targu Mures. The coffee was good, service quick.", "Joyce Lajkó, Google"),
               ("I also liked how the place looked.", "Flavy T, Google")],
       now="niciun site", photo=CF.format("100541_ac3d4ca4-4a6a-4274-a8ef-918f28d6c4b3"), photo2=CF.format("100542_6ce09289-67d0-4c77-8829-a663d95fcd57"),
       theme=dict(bg="#F4F5F7", ink="#1D1416", muted="#655C5E", accent="#B3202F", panel="#ECEDF1", on="#FFFFFF",
                  display="Outfit", fonts="Outfit:wght@500;700;800&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")),
  dict(slug="mr-pop-targu-mures", name="MR POP", kind="cafe", city="Târgu Mureș",
       address="Aleea Carpați 49A", zip="540311 Târgu Mureș", phone="0733 330 333",
       rating=4.9, reviews=198, src="Google", rating2=None,
       hours=H("8:00-19:00", "9:00-18:00", "9:00-18:00"),
       book=None, cta="Sună-ne",
       headline="Cafeaua de\npe Carpați.", lede="Cafenea de cartier pe Aleea Carpați. Latte, banana bread, sandvișuri și kombucha. La masă, la pachet sau cu livrare.",
       services=[("Latte și cafea de specialitate", "Lăudate în recenzii", None), ("Banana bread, brownie, croissant", "Prețuri foarte ok, zic clienții", None),
                 ("Sandvișuri și veggie melt", "Pentru brunch-ul de duminică", None), ("Kombucha cu mentă", "", None)],
       sig=("Brunch de duminică, fără grabă.", "Deschis și în weekend, de la 9 la 18. Clienții vin pentru atmosfera relaxată și pleacă cu banana bread la pachet."),
       quotes=[("Veggie melt and mint kombucha were fantastic. Latte was beautiful and delicious.", "Andie C, Google"),
               ("Lovely coffee spot for a late Sunday brunch. The coffee is delicious, the atmosphere very relaxing.", "ABell, Google"),
               ("Really cute spot with great food and friendly service!", "Hannah Sturman, Google")],
       now="o pagină de Facebook", photo=CF.format("100648_53a9641c-41ca-4402-ab27-830e7a68ed46"), photo2=CF.format("100647_8fa378ff-bf31-49df-b723-0d68b8bfcc4f"),
       theme=dict(bg="#FFF8EC", ink="#1F1A14", muted="#6E6455", accent="#E0562F", panel="#FCEBD2", on="#FFFFFF",
                  display="Bricolage Grotesque", fonts="Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")),
  dict(slug="galleria-art-coffee-brasov", name="Galleria Art & Coffee", kind="cafe", city="Brașov",
       address="Strada Colonel Ion Buzoianu 1A", zip="500084 Brașov", phone="0742 800 100",
       rating=4.7, reviews=942, src="Google", rating2=None,
       hours=H("9:00-22:00", "9:00-22:00", "9:00-22:00"),
       book=None, cta="Sună-ne",
       headline="Cafea\nprintre tablouri.", lede="Cafenea cu artă, la câțiva pași de Piața Sfatului. Deschis zilnic, de la 9 la 22.",
       services=[("Cafea", "Caramel latte, affogato", None), ("Băuturi reci", "Spritz, smoothie", None), ("Dulciuri", "Cookies și altele", None)],
       sig=("O cafenea care arată ca o galerie.", "Atenție la detalii, atmosferă, priveliște. Și personal care te ajută să comanzi chiar dacă nu vorbești română."),
       quotes=[("Beautiful artsy cafe near the city centre. I got a caramel latte and it was delicious. The views are great.", "Omar Kurdi, Google"),
               ("This place was superb! Such attention to detail. Atmosphere spot on.", "Keith Steele, Google"),
               ("Been coming here every summer for a couple of years.", "Paul Rosner, Google")],
       now="o pagină de Facebook", photo=CF.format("100542_ef36bf1e-fb12-4155-85f6-a50191946991"), photo2=CF.format("100543_fffc6820-bb07-436d-b794-56a215fe0ff1"),
       theme=dict(bg="#EEF0F2", ink="#232A31", muted="#5F6A74", accent="#B4643A", panel="#E2E6EA", on="#FFFFFF",
                  display="Cabinet Grotesk", fonts="Inter+Tight:wght@400;500;600", fontshare="cabinet-grotesk@700,800", body="Inter Tight", stretch="100%")),
  dict(slug="voynich-cafe-pub-sighisoara", name="Voynich Cafe & Pub", kind="pub", city="Sighișoara",
       address="Strada Octavian Goga 12, Scara B", zip="545400 Sighișoara", phone="0752 243 538",
       rating=4.6, reviews=501, src="Google", rating2=None,
       hours=H("16:00-23:50", "16:00-23:50", "16:00-23:50"),
       book=None, cta="Sună-ne",
       headline="Pub-ul ascuns\nal Sighișoarei.", lede="Bere cehă și românească, multe băuturi, prețuri bune. Deschis în fiecare seară de la 16.",
       services=[("Bere la halbă", "Kozel, Ursus și altele", None), ("Băuturi", "De toate felurile", None), ("Seri liniștite", "Departe de locurile aglomerate", None)],
       sig=("Fiecare scaun e unic.", "Mese, scaune și lămpi, fiecare altfel. Uneori ți se alătură și pisica la masă."),
       quotes=[("Cool vibe, big choice of drinks, very nice staff and good prices. If you are lucky a cat can join you at a table.", "Regina Falangie, Google"),
               ("A great little pub in the middle of town. The beer range and selection was awesome.", "Nick Galton-Fenzi, Google"),
               ("Quite cosy with every item (chairs, tables or lamps) being one of a kind.", "Laurentiu-Marian Angheluta, Google")],
       now="niciun site", photo=CF.format("100542_ca789888-a0ef-41e9-8497-c95a33d42364"), photo2=CF.format("100541_eb848b90-a300-46b0-866b-23114648bb5f"),
       theme=dict(bg="#14161C", ink="#F2EDE4", muted="#A3A7B0", accent="#E3B23C", panel="#1C1F27", on="#14161C",
                  display="Big Shoulders Display", fonts="Big+Shoulders+Display:wght@700;900&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="100%")),
  dict(slug="vintage-lounge-sighisoara", name="Vintage Lounge", kind="restaurant", city="Sighișoara",
       address="Strada Octavian Goga 6", zip="545400 Sighișoara", phone="0771 536 136",
       rating=4.4, reviews=1135, src="Google", rating2=None,
       hours=H("9:00-23:00", "9:00-23:00", "9:00-23:00"),
       book=None, cta="Rezervă o masă",
       headline="Porții mari,\npriveliște bună.", lede="Restaurant și lounge în Sighișoara, deschis zilnic de la 9 la 23. Mici, burgeri, pizza și multe altele.",
       services=[("Mici", "Clasicul românesc", None), ("Burgeri și pizza", "Pentru toată gașca", None), ("Paste", "Penne arrabbiata și altele", None), ("Pulpă de curcan", "", None)],
       sig=("Urci câteva trepte și ai priveliștea.", "Spații deschise, aer condiționat vara, porții mari și servire în 10 minute, după cum scriu clienții."),
       quotes=[("The food is very good and big portions. Big variety for all tastes. Prices are good too!", "nicks magic, Google"),
               ("We had great meals for four of us. Hamburger, pizza, turkey leg and mici. All were great.", "SONiA, Google"),
               ("Nice atmosphere and open spaces with good views. Served in 10 minutes and tasted good.", "Shuang, Google")],
       now="o pagină de Facebook", photo=CF.format("100650_d7bd79a0-02f4-4610-b58e-c3f26e012346"), photo2=CF.format("100647_432922dd-b13e-4403-b14b-450737322089"),
       theme=dict(bg="#18201C", ink="#EEE8DC", muted="#A6ADA5", accent="#E07A7A", panel="#1F2924", on="#18201C",
                  display="Archivo", fonts="Archivo:wdth,wght@62..125,500;125,800;125,900&family=Inter+Tight:wght@400;500;600", body="Inter Tight", stretch="125%")),
]


def tel(p):
    d = "".join(c for c in p if c.isdigit()).lstrip("0")
    return "+40" + d


def maps(s):
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(f"{s['name']} {s['address']} {s['city']}")


def embed(s):
    return "https://www.google.com/maps?q=" + urllib.parse.quote(f"{s['name']}, {s['address']}, {s['city']}") + "&output=embed"


def num(n):
    return f"{n:,}".replace(",", ".")


def nota(r):
    return f"{r:.1f}".replace(".", ",")


def hours_rows(s):
    if not s.get("hours"):
        return '<p class="muted">Programul de azi: sunați-ne și vă spunem. Pe site-ul final apare programul exact.</p>'
    out = []
    for d in DAYS:
        v = s["hours"].get(d)
        val = "Închis" if not v else v.replace("-", " - ")
        out.append(f'<div class="hr" data-day="{d}"><span>{ZI[d]}</span><b>{val}</b></div>')
    return '<div class="hours">' + "".join(out) + "</div>"


CSS = r"""
*,*::before,*::after{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body),system-ui,sans-serif;font-size:1.0625rem;line-height:1.6;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}a{color:inherit}:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.w{width:min(1180px,100% - 40px);margin-inline:auto}.muted{color:var(--muted)}
.d{font-family:var(--display),var(--body),sans-serif;font-stretch:var(--st);font-weight:800;letter-spacing:-.03em;line-height:.95}
.pb{background:var(--ink);color:var(--bg);font-size:.82rem;text-align:center;padding:8px 14px}.pb a{color:inherit;font-weight:600}
.hero{position:relative;min-height:min(94dvh,860px);display:flex;flex-direction:column;color:#fff;isolation:isolate;overflow:hidden}
.hero .bg{position:absolute;inset:0;z-index:-1}.hero .bg img{width:100%;height:100%;object-fit:cover;transform:scale(1.08);transition:transform 2.4s cubic-bezier(.2,.7,.2,1)}
.ready .hero .bg img{transform:scale(1)}
.hero .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.08) 35%,rgba(0,0,0,.8) 100%)}
.nav{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:22px 0}
.brand{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:800;font-size:1.3rem;text-decoration:none;letter-spacing:-.02em}
.nav nav{display:flex;gap:26px;align-items:center;font-size:.95rem}.nav nav a.l{text-decoration:none;opacity:.85}
.hero .copy{margin-top:auto;padding:40px 0 56px}
h1{font-size:clamp(3rem,8.6vw,7.6rem);margin:0 0 22px;white-space:pre-line}
.lede{font-size:clamp(1.1rem,1.6vw,1.3rem);max-width:40ch;margin:0 0 30px;opacity:.94}
.row{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.b1{display:inline-flex;align-items:center;gap:10px;min-height:56px;padding:0 28px;border-radius:999px;background:var(--accent);color:var(--on);font-weight:700;text-decoration:none;transition:transform .15s,filter .15s}
.b1:hover{filter:brightness(1.07)}.b1:active{transform:scale(.98)}.b1 i{font-style:normal;transition:transform .3s}.b1:hover i{transform:translateX(4px)}
.b2{display:inline-flex;align-items:center;min-height:56px;padding:0 24px;border-radius:999px;color:inherit;text-decoration:none;font-weight:600;box-shadow:inset 0 0 0 1.5px currentColor}
.b3{display:inline-flex;min-height:40px;align-items:center;padding:0 18px;border-radius:999px;background:#fff;color:#111;text-decoration:none;font-weight:700;font-size:.92rem}
.proof{display:flex;flex-wrap:wrap;gap:10px 22px;align-items:center;margin-top:26px;font-size:.98rem}
.stars{color:var(--accent);letter-spacing:2px}.open{display:inline-flex;align-items:center;gap:8px;font-weight:600}
.open i{width:9px;height:9px;border-radius:50%;background:#aaa}.open.on i{background:#3DDC84;box-shadow:0 0 0 4px rgba(61,220,132,.25)}
.pn{position:absolute;right:14px;bottom:14px;font-size:.72rem;background:rgba(0,0,0,.55);color:#fff;padding:4px 10px;border-radius:999px;z-index:2}
.mq{overflow:hidden;border-block:1px solid color-mix(in srgb,var(--ink) 14%,transparent);background:var(--panel)}
.mq .tr{display:flex;gap:48px;width:max-content;padding:18px 0;animation:mq 48s linear infinite}
.mq span{white-space:nowrap;font-weight:600}.mq span::before{content:"★★★★★ ";color:var(--accent)}
@keyframes mq{to{transform:translateX(-50%)}}
section{padding:clamp(72px,10vw,128px) 0}
h2{font-size:clamp(2.2rem,4.8vw,3.8rem);margin:0 0 18px}
.q3{display:grid;grid-template-columns:1.3fr 1fr;gap:clamp(24px,4vw,56px);align-items:start}
.qbig p{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:700;font-size:clamp(1.7rem,3.2vw,2.6rem);line-height:1.15;letter-spacing:-.02em;margin:0}
.qsm{display:grid;gap:28px;border-left:1px solid color-mix(in srgb,var(--ink) 16%,transparent);padding-left:clamp(20px,3vw,40px)}
.qsm p{font-size:1.2rem;font-weight:600;margin:0}cite{display:block;margin-top:10px;font-style:normal;color:var(--muted);font-size:.92rem}
.lab{font-size:.85rem;color:var(--muted);margin-top:30px}
.two{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(32px,6vw,96px);align-items:start}
.menu{list-style:none;margin:0;padding:0}
.menu li{display:grid;grid-template-columns:1fr auto;gap:16px;align-items:baseline;padding:20px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 14%,transparent)}
.menu li:first-child{border-top:1px solid color-mix(in srgb,var(--ink) 14%,transparent)}
.menu h3{margin:0;font-size:1.2rem}.menu p{margin:2px 0 0;color:var(--muted);font-size:.95rem}
.menu b{font-family:var(--display),sans-serif;font-stretch:var(--st);font-size:1.35rem;white-space:nowrap}
.panel{background:var(--panel)}
.sig{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,80px);align-items:center}
.sig figure{margin:0;position:relative;overflow:hidden;border-radius:22px}.sig figure img{width:100%;aspect-ratio:4/5;object-fit:cover}
.big{font-size:clamp(5rem,14vw,10rem);color:var(--accent);margin:0 0 8px}
.vis{display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,6vw,80px)}
address{font-style:normal;font-size:1.25rem;line-height:1.5;margin-bottom:18px}
.ph{display:block;font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:800;font-size:clamp(2rem,3.6vw,2.8rem);text-decoration:none;margin-bottom:22px;letter-spacing:-.02em}
.hours .hr{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 12%,transparent)}
.hours .hr.today{color:var(--accent)}.hours .hr.today b::after{content:" · azi"}
iframe{width:100%;height:320px;border:0;border-radius:22px;margin-top:24px;filter:grayscale(.2)}
.of{background:var(--ink);color:var(--bg)}.of .muted{color:color-mix(in srgb,var(--bg) 70%,transparent)}
.of .for{color:var(--accent);font-weight:700;margin:0 0 12px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:36px 0}
.cmp div{border-radius:22px;padding:28px;background:color-mix(in srgb,var(--bg) 7%,transparent)}
.cmp div.y{background:var(--accent);color:var(--on)}.cmp h3{margin:0 0 12px;font-size:1.1rem}.cmp ul{margin:0;padding-left:18px}.cmp li{margin:6px 0}
.pr{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.pk{border:1px solid color-mix(in srgb,var(--bg) 20%,transparent);border-radius:22px;padding:30px}
.pk.hl{border:2px solid var(--accent)}.pk .d{font-size:clamp(2.8rem,5vw,4rem);margin:8px 0}
.gu{margin:28px 0;font-size:1.15rem}.of .b2{color:var(--bg)}
footer{padding:36px 0 120px;font-size:.88rem;color:var(--muted)}footer .w{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px}
.bar{position:fixed;left:12px;right:12px;bottom:12px;z-index:20;display:none;grid-template-columns:1fr 1fr 1.3fr;gap:8px;padding:8px;border-radius:999px;background:color-mix(in srgb,#111 92%,transparent);backdrop-filter:blur(10px);box-shadow:0 10px 30px rgba(0,0,0,.3)}
.bar a{display:flex;align-items:center;justify-content:center;min-height:48px;border-radius:999px;color:#fff;text-decoration:none;font-weight:700;font-size:.95rem}
.bar a.m{background:var(--accent);color:var(--on)}
.rv{opacity:0;transform:translateY(22px)}.ready .rv{opacity:1;transform:none;transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.ready .rv.d2{transition-delay:.12s}.ready .rv.d3{transition-delay:.24s}
.up{transform:translateY(28px);transition:transform .8s cubic-bezier(.2,.7,.2,1)}.up.in{transform:none}
@media(max-width:860px){.nav nav a.l{display:none}.q3,.two,.sig,.vis,.cmp,.pr{grid-template-columns:1fr}.qsm{border-left:0;padding-left:0}.bar{display:grid}.hero{min-height:88dvh}}
@media(prefers-reduced-motion:reduce){.rv,.ready .rv,.up{opacity:1;transform:none;transition:none}.hero .bg img{transform:none;transition:none}.mq .tr{animation:none}}
"""

JS = r"""
(function(){var S=window.__S__;requestAnimationFrame(function(){document.documentElement.classList.add('ready')});
var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15}):null;
document.querySelectorAll('.up').forEach(function(e){io?io.observe(e):e.classList.add('in')});
var p=new Intl.DateTimeFormat('en-US',{timeZone:'Europe/Bucharest',weekday:'short',hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date()),o={};p.forEach(function(x){o[x.type]=x.value});
var d=o.weekday,m=(+o.hour%24)*60+(+o.minute);document.querySelectorAll('.hr[data-day="'+d+'"]').forEach(function(r){r.classList.add('today')});
var b=document.querySelectorAll('[data-open]');if(!S.h){b.forEach(function(x){x.hidden=true});return}
var h=S.h[d],t='Închis azi',on=false;if(h){var a=h.split('-'),s=a[0].split(':'),e=a[1].split(':'),sm=+s[0]*60+ +s[1],em=+e[0]*60+ +e[1];if(em<=sm)em+=1440;
if(m>=sm&&m<em){on=true;t='Deschis acum · până la '+a[1]}else if(m<sm){t='Deschide azi la '+a[0]}else{t='Închis acum'}}
b.forEach(function(x){x.querySelector('span').textContent=t;x.classList.toggle('on',on)})})();
"""


def page(s):
    t = s["theme"]
    book = s["book"] or f"tel:{tel(s['phone'])}"
    tgt = ' target="_blank" rel="noopener"' if s["book"] else ""
    short = "Programare" if s["book"] else ("Rezervă" if "Rezerv" in s["cta"] else "Sună")
    fonts = f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={t["fonts"]}&display=swap">'
    if t.get("fontshare"):
        fonts += f'<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]={t["fontshare"]}&display=swap">'
    open_b = '<span class="open" data-open><i></i><span>Program</span></span>'
    r2 = f'<span>{E(s["rating2"])}</span>' if s.get("rating2") else ""
    mq_items = "".join(f"<span>„{E(q)}” {E(a.split(',')[0])}</span>" for q, a in s["quotes"])
    menu = "".join(f'<li><div><h3>{E(n)}</h3>{f"<p>{E(d)}</p>" if d else ""}</div>{f"<b>{E(p)}</b>" if p else ""}</li>' for n, d, p in s["services"])
    has_prices = any(p for _, _, p in s["services"])
    menu_note = ("Prețurile sunt cele publicate pe pagina de programare." if has_prices
                 else "Pe site-ul final aici intră meniul vostru complet, cu prețuri, ca oamenii să știe ce comandă înainte să vină.")
    menu_title = "Servicii și prețuri" if s["kind"] == "barber" else "Ce găsești la noi"
    q0, a0 = s["quotes"][0]
    qs = "".join(f"<blockquote><p>„{E(q)}”</p><cite>{E(a)}</cite></blockquote>" for q, a in s["quotes"][1:])
    big = nota(s["rating"])
    subj = urllib.parse.quote(f"Da, vreau site-ul pentru {s['name']}")
    data = json.dumps({"h": s.get("hours")})
    return f"""<!doctype html>
<html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(s['name'])} · {E(s['city'])}</title><meta name="robots" content="noindex, nofollow">
<meta name="description" content="{E(s['lede'])}"><meta name="theme-color" content="{t['bg']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{fonts}
<style>:root{{--bg:{t['bg']};--ink:{t['ink']};--muted:{t['muted']};--accent:{t['accent']};--panel:{t['panel']};--on:{t['on']};--display:'{t['display']}';--body:'{t['body']}';--st:{t['stretch']}}}{CSS}</style>
</head><body>
<div class="pb">Propunere de site făcută special pentru {E(s['name'])} · <a href="#oferta">Vezi oferta</a></div>
<header class="hero"><div class="bg"><img src="{img(s['photo'], 2000)}" alt="" fetchpriority="high"><span class="pn">Poză exemplu · aici intră pozele voastre</span></div>
<div class="w nav"><a class="brand" href="#">{E(s['name'])}</a><nav><a class="l" href="#meniu">{"Servicii" if s["kind"] == "barber" else "Meniu"}</a><a class="l" href="#recenzii">Recenzii</a><a class="l" href="#vizita">Vizită</a><a class="b3" href="{E(book)}"{tgt}>{short}</a></nav></div>
<div class="w copy"><h1 class="d rv">{E(s['headline'])}</h1><p class="lede rv d2">{E(s['lede'])}</p>
<div class="row rv d2"><a class="b1" href="{E(book)}"{tgt}>{E(s['cta'])} <i>→</i></a><a class="b2" href="tel:{tel(s['phone'])}">Sună: {E(s['phone'])}</a></div>
<div class="proof rv d3"><span><span class="stars" aria-hidden="true">★★★★★</span> {big} din {num(s['reviews'])} de recenzii pe {s['src']}</span>{r2}{open_b}</div></div></header>
<div class="mq" aria-hidden="true"><div class="tr">{mq_items}{mq_items}{mq_items}{mq_items}</div></div>
<section id="recenzii"><div class="w"><h2 class="d up">Ce spun clienții.</h2><div class="q3 up"><blockquote class="qbig"><p>„{E(q0)}”</p><cite>{E(a0)}</cite></blockquote><div class="qsm">{qs}</div></div>
<p class="lab">Recenzii reale, copiate exact cum au fost scrise de clienți.</p></div></section>
<section id="meniu" class="panel"><div class="w two"><div><h2 class="d up">{menu_title}</h2><p class="muted">{E(menu_note)}</p><a class="b1" href="{E(book)}"{tgt}>{E(s['cta'])} <i>→</i></a></div><ul class="menu up">{menu}</ul></div></section>
<section><div class="w sig"><figure class="up"><img src="{img(s['photo2'], 1200)}" alt="" loading="lazy"><span class="pn">Poză exemplu</span></figure>
<div class="up"><p class="d big">{num(s["reviews"])}</p><p class="muted" style="margin:-4px 0 18px;font-weight:600">recenzii pe {s["src"]}, nota {big}</p><h2 class="d">{E(s['sig'][0])}</h2><p class="muted" style="font-size:1.15rem;max-width:44ch">{E(s['sig'][1])}</p></div></div></section>
<section id="vizita" class="panel"><div class="w vis"><div><h2 class="d up">Vino pe la noi.</h2><address>{E(s['name'])}<br>{E(s['address'])}<br>{E(s['zip'])}</address>
<a class="ph" href="tel:{tel(s['phone'])}">{E(s['phone'])}</a><div class="row"><a class="b1" href="{maps(s)}" target="_blank" rel="noopener">Indicații <i>↗</i></a><a class="b2" href="tel:{tel(s['phone'])}">Sună acum</a></div></div>
<div><h2 class="d up">Program</h2>{open_b}<div style="height:14px"></div>{hours_rows(s)}</div></div></section>
<section id="oferta" class="of"><div class="w"><p class="for">Pentru proprietarul {E(s['name'])}</p>
<h2 class="d" style="max-width:18ch">{num(s['reviews'])} de oameni v-au lăudat pe {s['src']}. Restul nu vă găsesc.</h2>
<p class="muted" style="max-width:62ch;font-size:1.12rem">{'Cine vă caută acum pe telefon nu găsește niciun site al vostru.' if s['now']=='niciun site' else 'Cine vă caută acum pe telefon găsește doar ' + E(s['now']) + '.'} Nu vede dintr-o privire {"prețurile, programul și butonul de programare" if s["kind"] == "barber" else "meniul, programul și butonul de sunat"}, așa că alege localul de alături. Pagina de mai sus e făcută deja cu datele voastre reale.</p>
<div class="cmp"><div><h3>Acum</h3><ul><li>{E(s['now'][0].upper() + s['now'][1:])}</li><li>{"Prețurile nu se văd pe Google" if s["kind"] == "barber" else "Meniul nu se vede pe Google"}</li><li>Recenziile bune stau ascunse</li></ul></div>
<div class="y"><h3>Cu site-ul acesta</h3><ul><li>Un site al vostru, pe domeniul vostru</li><li>Buton de sunat, indicații și {"programare" if s["book"] else "rezervare"} dintr-un click</li><li>Recenziile voastre, la vedere, pe prima pagină</li></ul></div></div>
<div class="pr"><div class="pk"><p style="margin:0;font-weight:700">Starter</p><p class="d">1.500 lei</p><p class="muted" style="margin:0">Până la 3 pagini. Exact ce vedeți aici, terminat cu pozele și textele voastre.</p></div>
<div class="pk hl"><p style="margin:0;font-weight:700;color:var(--accent)">Standard</p><p class="d">2.500 lei</p><p class="muted" style="margin:0">Până la 5 pagini, formular de {"programare" if s["kind"] == "barber" else "rezervare"} și profilul Google pus la punct.</p></div></div>
<p class="gu"><b>Gata în aceeași zi în care primim pozele. Avans 50%, iar dacă primul design nu vă place, vă dăm avansul înapoi.</b></p>
<div class="row"><a class="b1" href="mailto:{EMAIL}?subject={subj}">Vreau site-ul <i>→</i></a></div>
<p class="muted" style="margin-top:18px;font-size:.92rem">George, Storefront Studio, Sighișoara. Mentenanță opțională: 150 lei pe lună.</p></div></section>
<footer><div class="w"><span>{E(s['name'])} · {E(s['address'])}, {E(s['zip'])}</span><span>Propunere: Storefront Studio</span></div></footer>
<nav class="bar" aria-label="Acțiuni rapide"><a href="tel:{tel(s['phone'])}">Sună</a><a href="{maps(s)}" target="_blank" rel="noopener">Indicații</a><a class="m" href="{E(book)}"{tgt}>{short}</a></nav>
<script>window.__S__={data};{JS}</script>
</body></html>"""


def main():
    want = set(sys.argv[1:])
    for s in SITES:
        if want and s["slug"] not in want:
            continue
        out = os.path.join(ROOT, "concepts", s["slug"])
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "index.html"), "w") as f:
            f.write(page(s))
        print("https://huszageorge25-wq.github.io/concepts/%s/" % s["slug"])


if __name__ == "__main__":
    main()
