"""Signature animations and the owner offer for Storefront Studio pages.

Every site gets ONE signature animation (set "anim" in sites.py, or a default by signature type)
and an owner-facing offer section built only from approved terms in OFFER plus the site's real facts.
"""
import html, re
E = lambda s: html.escape(str(s), quote=True)

# Approved terms only. The engine updates founding_left when a founding client pays.
OFFER = dict(regular=1200, founding=960, standard=2000, standard_founding=1600, founding_left=10, founding_total=10,
             care=79, assistant="+1 (614) 967-9783", assistant_tel="+16149679783",
             email="huszageorge25@gmail.com")

def offer_html(s):
    o = OFFER
    fixes = s.get("fixes") or []
    fx = "".join(f"<li>{E(f)}</li>" for f in fixes)
    fixes_block = f'<div class="fixes"><h3>What this fixes on your current site</h3><ul>{fx}</ul></div>' if fixes else ""
    unit = {"barber": "cuts", "salon": "appointments", "dental": "visits", "roofer": "jobs"}[s["kind"]]
    payback = ""
    if s.get("avg_price"):
        n = -(-o["founding"] // s["avg_price"])
        payback = f'<p class="payback">At ${s["avg_price"]} a {unit[:-1]}, the whole site costs about {n} {unit}. One extra a day pays it back in a few weeks.</p>'
    owner = s.get("owner") or "the owner"
    subj = f"Yes - {s['name']} website"
    return f"""<section id="offer" class="offer"><div class="wrap">
<p class="for">For {E(owner)} of {E(s['name'])}</p>
<h2>Make this your real website. Live today.</h2>
<div class="offer-grid">
<div class="deal">
<div class="price"><span class="was">${o['regular']:,}</span><span class="now">${o['founding']:,}</span></div>
<p class="terms">Founding client price, for our first {o['founding_total']} clients. {o['founding_left']} of {o['founding_total']} spots left.</p>
<ul class="inc">
<li>This design, finished with your own photos, logo, services and prices</li>
<li>Built for phones first: tap to call, directions and booking</li>
<li>Live the same day when your details arrive by 12 pm Eastern on a weekday</li>
<li>Two rounds of changes included</li>
<li>Half to start (${o['founding']//2}), half only when you love it</li>
</ul>
<p class="guarantee"><strong>Don't love the first design? Your deposit comes back.</strong> You risk nothing.</p>
{payback}
</div>
<div class="act">
{fixes_block}
<a class="btn big" href="tel:{o['assistant_tel']}">Call my assistant · {o['assistant']}</a>
<a class="btn ghost big" href="mailto:{o['email']}?subject={E(subj.replace(' ','%20'))}">Email George: “yes”</a>
<p class="small">The assistant is an AI that answers 24/7 and can set everything up. Or just reply “yes” to my email. Need more pages or online booking? Ask about Standard: ${o['standard_founding']:,} for founding clients (regular ${o['standard']:,}). Optional care plan ${o['care']}/month.</p>
</div></div></div></section>"""


OFFER_CSS = """
.offer{--oa:color-mix(in srgb,var(--accent) 62%,var(--bg));background:var(--ink);color:var(--bg);padding:clamp(72px,10vw,120px) 0}
.offer .for{margin:0 0 12px;font-weight:600;color:var(--oa)}
.offer h2{max-width:16ch}
.offer-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5vw,72px);margin-top:28px}
.price{display:flex;align-items:baseline;gap:18px}
.price .was{font-size:1.6rem;text-decoration:line-through;opacity:.55}
.price .now{font-family:var(--display);font-weight:var(--dw);font-stretch:var(--ds);letter-spacing:var(--tr);font-size:clamp(4rem,10vw,7rem);line-height:1;color:var(--oa)}
.terms{margin:6px 0 22px;opacity:.85}
.inc{list-style:none;padding:0;margin:0 0 22px}
.inc li{padding:10px 0 10px 30px;position:relative;border-bottom:1px solid color-mix(in srgb,var(--bg) 14%,transparent)}
.inc li::before{content:"";position:absolute;left:4px;top:18px;width:12px;height:7px;border-left:2.5px solid var(--oa);border-bottom:2.5px solid var(--oa);transform:rotate(-45deg)}
.guarantee{font-size:1.1rem}
.payback{opacity:.85}
.fixes{background:color-mix(in srgb,var(--bg) 8%,transparent);border-radius:var(--r);padding:24px;margin-bottom:22px}
.fixes h3{margin:0 0 10px;font-size:1.05rem}
.fixes ul{margin:0;padding-left:18px;opacity:.9}
.fixes li{margin:6px 0}
.act .btn{width:100%;margin-bottom:12px}
.btn.big{min-height:60px;font-size:1.05rem}
.offer .btn.ghost{color:var(--bg)}
.small{font-size:.9rem;opacity:.75}
.hero-type .strip{position:relative}
.photo-note{position:absolute;right:12px;bottom:12px;z-index:2;font-size:.75rem;background:rgba(0,0,0,.55);color:#fff;padding:4px 10px;border-radius:999px}
@media(max-width:860px){.offer-grid{grid-template-columns:1fr}}
"""
