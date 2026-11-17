"""Leaduri România: patiserii, Cluj-Napoca (găsite 2026-11-17). Doar fapte reale (date Google prin Wanderlog)."""
from ro_data_rest import VOY, VIN, POP, GAL, T, FR, OU, BR

SITES = [
  dict(slug="a-la-tarte-cluj", name="A la Tarte", kind="cafe", city="Cluj-Napoca",
       address="Strada Ion I. C. Brătianu 35", zip="400079 Cluj-Napoca", phone="0758 539 936",
       rating=4.6, reviews=890, src="Google", rating2=None, hours=None,
       book=None, cta="Sună-ne",
       headline="Tarte și quiche,\nca în Franța.", lede="A la Tarte, Strada Ion I. C. Brătianu 35, Cluj-Napoca. Bistro franțuzesc cu tarte, quiche și fursecuri.",
       services=[("Tarte", None, None), ("Quiche", None, None), ("Fursecuri", None, None)],
       sig=("Aproape 900 de recenzii.", "Clienții v-au dat nota 4,6 pe Google pentru A la Tarte."),
       quotes=[], now="niciun site", photo=GAL[0], photo2=GAL[2],
       theme=T("#F7F2EA", "#2A1E16", "#76685B", "#B4683A", "#EFE6D8", "#FFFFFF", "Fraunces", FR)),
  dict(slug="friandise-cluj", name="Friandise", kind="cafe", city="Cluj-Napoca",
       address="Bulevardul Eroilor 10", zip="400394 Cluj-Napoca", phone="0756 021 547",
       rating=4.7, reviews=457, src="Google", rating2=None, hours=None,
       book=None, cta="Sună-ne",
       headline="Deserturi și ciocolată\npe Bulevardul Eroilor.", lede="Friandise, Bulevardul Eroilor 10, Cluj-Napoca. Patiserie, ciocolată artizanală și înghețată cu arome ca lavandă sau rubarbă și soc.",
       services=[("Patiserie și deserturi", None, None), ("Ciocolată artizanală", None, None), ("Înghețată", "Lavandă, spirulină, rubarbă și soc", None)],
       sig=("Nota 4,7 pe Google.", "Peste 450 de clienți v-au lăsat o recenzie pe Google."),
       quotes=[], now="niciun site", photo=VIN[0], photo2=VIN[2],
       theme=T("#F6F0F2", "#2B1D24", "#73636B", "#A8456B", "#EEE3E8", "#FFFFFF", "Bricolage Grotesque", BR)),
]

IMG = {"a-la-tarte-cluj": GAL, "friandise-cluj": VIN}
