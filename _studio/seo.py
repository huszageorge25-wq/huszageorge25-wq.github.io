"""Builds the SEO layer of the Storefront Studio site.

  python3 _studio/seo.py

Writes: websites-for/ (hub + one page per industry), guides/ (hub + articles),
start/ (how to buy + deposit), 404.html, robots.txt, sitemap.xml, llms.txt,
og.png is made separately (see make_og in README). Also patches the <head> and
footer of the root index.html between SEO markers (safe to run again).
Content lives in _studio/seo_data.py. Never invent reviews, ratings or clients.
"""
import html, json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from seo_data import INDUSTRIES, GUIDES
from extras import OFFER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://huszageorge25-wq.github.io"
TODAY = datetime.date.today().isoformat()
# Google Analytics 4 measurement ID (free). Empty = no tracking loads. George pastes his G-XXXXXXX here.
GA_ID = ""
PAY = "https://link.payoneer.com/Token?t=A2ABF332A9F441559223002E50F51EEF&src=pl"
TEL, TEL_TXT, MAIL = OFFER["assistant_tel"], OFFER["assistant"], OFFER["email"]
E = lambda s: html.escape(str(s), quote=True)

ORG = {
  "@type": "ProfessionalService", "@id": BASE + "/#business", "name": "Storefront Studio",
  "url": BASE + "/", "logo": BASE + "/favicon.svg", "image": BASE + "/og.png",
  "description": "Fixed-price websites for US local businesses, live the same day. Free homepage concept before you pay.",
  "telephone": "+1-614-967-9783", "email": MAIL, "areaServed": {"@type": "Country", "name": "United States"},
  "priceRange": "$960-$2,000", "knowsLanguage": ["en"],
  "address": {"@type": "PostalAddress", "streetAddress": "Strada Podei 28 A", "postalCode": "545400", "addressLocality": "Sighisoara", "addressCountry": "RO"},
  "makesOffer": [
    {"@type": "Offer", "name": "Starter website", "price": "1200", "priceCurrency": "USD", "description": "1 to 3 pages, live the same day"},
    {"@type": "Offer", "name": "Standard website", "price": "2000", "priceCurrency": "USD", "description": "Up to 5 pages with booking, ordering or quote form"},
    {"@type": "Offer", "name": "Care plan", "price": "79", "priceCurrency": "USD", "description": "Hosting and same-day changes, monthly"}],
}

CSS = """
:root{--porcelain:#F4F4F1;--paper:#fff;--ink:#17181C;--graphite:#5F6268;--hair:#E2E2DD;--cobalt:#2448E8;--night:#0B0C0E;--gutter:clamp(16px,4vw,40px)}
@media (prefers-color-scheme:dark){:root{--porcelain:#0E0F12;--paper:#17181C;--ink:#F2F2F0;--graphite:#A3A6AD;--hair:#2A2C31;--cobalt:#5B78FF;--night:#000}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--porcelain);color:var(--ink);font:400 17px/1.6 Geist,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}h1,h2,h3,p{margin:0}
.wrap{max-width:1100px;margin:0 auto;padding:0 var(--gutter)}
.nav{position:sticky;top:0;z-index:9;background:color-mix(in srgb,var(--porcelain) 85%,transparent);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid var(--hair)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:60px;gap:12px}
.brand{display:flex;gap:10px;align-items:center;font-weight:600;text-decoration:none;letter-spacing:-.02em}
.brand img{width:26px;height:26px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border-radius:999px;font-weight:500;text-decoration:none;border:1px solid transparent;font-size:16px}
.btn.primary{background:var(--cobalt);color:#fff}.btn.quiet{border-color:color-mix(in srgb,var(--ink) 25%,transparent)}
.nav .btn{min-height:38px;padding:0 16px;font-size:14.5px;white-space:nowrap}.brand{white-space:nowrap}
@media (max-width:520px){.nav .btn.quiet{display:none}}
.crumbs{font-size:14px;color:var(--graphite);padding-top:22px}.crumbs a{text-decoration:none}
header.hero{padding-top:clamp(40px,7vw,88px);padding-bottom:clamp(32px,5vw,56px)}
h1{font-weight:600;letter-spacing:-.04em;line-height:1.02;font-size:clamp(40px,6.6vw,76px);max-width:16ch}
.lede{font-size:clamp(18px,1.7vw,21px);color:var(--graphite);max-width:60ch;margin-top:22px}
.ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.note{font-size:14px;color:var(--graphite);margin-top:14px}
section{padding:clamp(40px,6vw,72px) 0;border-top:1px solid var(--hair)}
h2{font-weight:600;letter-spacing:-.03em;line-height:1.1;font-size:clamp(28px,3.6vw,42px);max-width:22ch;margin-bottom:22px}
h3{font-size:19px;font-weight:600;margin-bottom:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
.card{background:var(--paper);border:1px solid var(--hair);border-radius:20px;padding:22px}
.card p,.prose p,li{color:var(--graphite)}
ul.ticks{list-style:none;padding:0;margin:0;display:grid;gap:10px}
ul.ticks li{padding-left:28px;position:relative}
ul.ticks li:before{content:"";position:absolute;left:4px;top:.55em;width:12px;height:7px;border-left:2px solid var(--cobalt);border-bottom:2px solid var(--cobalt);transform:rotate(-45deg)}
.price{font-size:34px;font-weight:600;letter-spacing:-.03em;color:var(--ink)}
.price s{font-size:20px;color:var(--graphite);margin-right:8px}
details{background:var(--paper);border:1px solid var(--hair);border-radius:16px;padding:16px 20px;margin-bottom:10px}
summary{font-weight:600;cursor:pointer}details p{margin-top:10px;color:var(--graphite)}
.prose{max-width:70ch}.prose h2{margin-top:36px;margin-bottom:12px;font-size:clamp(24px,3vw,32px)}.prose p{margin-bottom:14px}
.cta-band{background:var(--night);color:#F5F5F7;border-radius:28px;padding:clamp(28px,5vw,56px);margin:clamp(40px,6vw,72px) 0}
.cta-band h2{color:#fff}.cta-band p{color:#B4B6BC;max-width:56ch}
.cta-band .btn.quiet{border-color:#55575d;color:#fff}
.links{columns:3 220px;gap:24px;padding:0;list-style:none;margin:0}.links li{margin-bottom:8px}
footer{border-top:1px solid var(--hair);padding:36px 0 110px;font-size:14px;color:var(--graphite)}
footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px;margin-bottom:22px}
footer h3{font-size:14px;color:var(--ink)}footer ul{list-style:none;padding:0;margin:8px 0 0}footer li{margin-bottom:6px}footer a{text-decoration:none}
.dock{position:fixed;left:0;right:0;bottom:0;z-index:10;display:flex;gap:8px;padding:10px var(--gutter) calc(10px + env(safe-area-inset-bottom));background:color-mix(in srgb,var(--porcelain) 92%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-top:1px solid var(--hair)}
.dock .btn{flex:1;min-height:46px}
@media (min-width:821px){.dock{display:none}footer{padding-bottom:36px}}
"""

def analytics():
    if not GA_ID:
        return ""
    return f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var h=a.getAttribute('href')||'',ev=null;
if(h.indexOf('tel:')===0)ev='call_click';else if(a.id==='go')ev='website_check_send';else if(h.indexOf('mailto:')===0)ev=/Referral/.test(h)?'referral_click':'concept_request';
else if(h.indexOf('payoneer')>-1)ev='deposit_click';else if(h.indexOf('/website-check/')>-1)ev='check_open';
if(ev)gtag('event',ev,{{link_kind:h.split('?')[0].split(':')[0],page_path:location.pathname}});}});
document.addEventListener('submit',function(e){{if(e.target&&e.target.id==='concept')gtag('event','concept_request',{{form:'homepage'}});}});
document.addEventListener('change',function(e){{if(e.target&&e.target.closest&&e.target.closest('.q')&&!window.__chk){{window.__chk=1;gtag('event','check_started');}}}});</script>"""

def head(title, desc, path, ld, noindex=False):
    url = BASE + path
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Storefront Studio">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/og.png"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{BASE}/og.png">
<meta name="theme-color" content="#F4F4F1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap">
<style>{CSS}</style>
{analytics()}
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False)}</script>
</head>
<body>
<nav class="nav"><div class="wrap"><a class="brand" href="/"><img src="/favicon.svg" alt="" width="26" height="26">Storefront Studio</a>
<span style="display:flex;gap:8px"><a class="btn quiet" href="/website-check/">Check my site</a><a class="btn primary" href="/#contact">Free concept</a></span></div></nav>
"""

def crumbs(items):
    ld = {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + p} for i, (n, p) in enumerate(items)]}
    html_ = " / ".join(f'<a href="{p}">{E(n)}</a>' if i < len(items) - 1 else E(n) for i, (n, p) in enumerate(items))
    return f'<div class="wrap crumbs">{html_}</div>', ld

def faq_ld(pairs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}

def faq_html(pairs):
    return "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in pairs)

GENERAL_FAQ = [
  ("How can my website be live the same day?", "Send your logo, photos, services and hours by 12 pm Eastern on a weekday and your site goes live that evening. Connecting a domain you already own can take a few extra hours."),
  ("Do I pay before I see anything?", "No. We design a free concept of your homepage first. If you want it, you pay a 50% deposit. If you don't like the first design, the full deposit comes back."),
  ("Where are you based?", "Storefront Studio is run by George from Romania and works remotely with US businesses by email, phone and video. That's how prices stay well below local agencies."),
  ("Can I talk to someone now?", f"Yes. Call {TEL_TXT}. It's an AI assistant that answers 24/7, explains the packages and books a call with George if you want one."),
]

def pricing_block():
    o = OFFER
    return f"""<section><div class="wrap"><h2>One fixed price. Agreed before we start.</h2>
<div class="grid">
<div class="card"><h3>Starter</h3><p class="price"><s>${o['regular']:,}</s>${o['founding']:,}</p><p>Founding price for our first {o['founding_total']} clients. 1 to 3 pages, your services, hours and map, tap to call, live the same day.</p></div>
<div class="card"><h3>Standard</h3><p class="price"><s>${o['standard']:,}</s>${o['standard_founding']:,}</p><p>Up to 5 pages with online booking, ordering or a quote form, photo gallery and Google Business Profile setup help.</p></div>
<div class="card"><h3>Care plan</h3><p class="price">${o['care']}<span style="font-size:17px;font-weight:400">/month</span></p><p>Fast, secure hosting and changes done the same day. Cancel with 30 days' notice.</p></div>
</div><p class="note">50% to start, 50% when you approve the finished site. Prices in US dollars. You own your domain and content.</p></div></section>"""

def cta_band(h="See your new website today.", p="Tell us your business name and city. We'll design a free concept of your homepage and send it the same day. No obligation."):
    return f"""<div class="wrap"><div class="cta-band"><h2>{E(h)}</h2><p>{E(p)}</p>
<div class="ctas"><a class="btn primary" href="/#contact">Get my free concept</a><a class="btn quiet" href="tel:{TEL}">Call {TEL_TXT}</a></div>
<p class="note" style="color:#8E9096">The phone line is an AI assistant, available 24/7. Or email <a href="mailto:{MAIL}">{MAIL}</a>.</p></div></div>"""

def footer():
    ind = "".join(f'<li><a href="/websites-for/{i["slug"]}/">Websites for {E(i["name"].lower())}</a></li>' for i in INDUSTRIES[:8])
    ind2 = "".join(f'<li><a href="/websites-for/{i["slug"]}/">Websites for {E(i["name"].lower())}</a></li>' for i in INDUSTRIES[8:15]) + f'<li><a href="/websites-for/"><b>All {len(INDUSTRIES)} industries</b></a></li><li><a href="/serving-all-50-states/">Serving all 50 states</a></li>'
    gd = "".join(f'<li><a href="/guides/{g["slug"]}/">{E(g["title"])}</a></li>' for g in GUIDES)
    return f"""<footer><div class="wrap"><div class="cols">
<div><h3>Industries</h3><ul>{ind}</ul></div><div><h3>&nbsp;</h3><ul>{ind2}</ul></div>
<div><h3>Guides</h3><ul>{gd}<li><a href="/start/">How to get started</a></li><li><a href="/website-check/">Free website check</a></li><li><a href="/referrals/">Referral program</a></li></ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:{TEL}">{TEL_TXT} (AI assistant, 24/7)</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>Serving local businesses in all 50 states</li></ul></div>
</div>© {datetime.date.today().year} Storefront Studio. Websites for US local businesses.</div></footer>
<div class="dock"><a class="btn quiet" href="tel:{TEL}">Call now</a><a class="btn primary" href="/#contact">Free concept</a></div>
</body></html>"""

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

def industry_page(i):
    path = f"/websites-for/{i['slug']}/"
    title = f"Websites for {i['name']}, Live the Same Day | Storefront Studio"
    desc = f"Professional {i['one']} websites for US {i['owner']}: tap to call, booking, hours and Google-ready. Free homepage concept first. From ${OFFER['founding']:,}."
    cr, crld = crumbs([("Home", "/"), ("Industries", "/websites-for/"), (f"Websites for {i['name'].lower()}", path)])
    faqs = i["faq"] + GENERAL_FAQ
    service = {"@type": "Service", "name": f"Website design for {i['name'].lower()}", "serviceType": "Website design", "provider": {"@id": BASE + "/#business"},
               "areaServed": {"@type": "Country", "name": "United States"}, "audience": {"@type": "BusinessAudience", "name": i["owner"]},
               "offers": {"@type": "Offer", "price": str(OFFER["founding"]), "priceCurrency": "USD"}, "url": BASE + path}
    feats = "".join(f"<li>{E(f)}</li>" for f in i["features"])
    probs = "".join(f'<div class="card"><p>{E(p)}</p></div>' for p in i["problems"])
    searches = ", ".join(f"“{s}”" for s in i["search"])
    kw = [f"{i['one']} website", f"{i['one']} website design", f"web design for {i['name'].lower()}", f"website for {i['owner']}", f"small business website for {i['name'].lower()}", f"{i['one']} website cost", f"mobile website for {i['name'].lower()}", f"local SEO for {i['name'].lower()}"]
    kwl = "".join(f"<li>{E(k)}</li>" for k in kw)
    others = "".join(f'<li><a href="/websites-for/{o["slug"]}/">{E(o["name"])}</a></li>' for o in INDUSTRIES if o is not i)
    body = f"""{cr}
<main><header class="hero wrap"><h1>Websites for {E(i['name'].lower())} that bring in customers.</h1>
<p class="lede">{E(i['intro'])}</p>
<div class="ctas"><a class="btn primary" href="/#contact">Get a free concept for my {E(i['one'])}</a><a class="btn quiet" href="tel:{TEL}">Call {TEL_TXT}</a></div>
<p class="note">See your new homepage before you pay anything. Live the same day once you say yes.</p></header>
<section><div class="wrap"><h2>What every {E(i['one'])} website we build includes</h2><ul class="ticks">{feats}</ul></div></section>
<section><div class="wrap"><h2>Problems we fix most often</h2><div class="grid">{probs}</div></div></section>
<section><div class="wrap prose"><h2>Built to show up when people search</h2>
<p>Customers looking for a {E(i['one'])} type things like {E(searches)} into Google. We build every page so search engines can read your name, address, phone, hours and services clearly, load it fast on phones, and add the structured data Google uses for local results.</p>
<p>Owners usually find us by searching for things like:</p><ul class="ticks" style="margin-bottom:16px">{kwl}</ul>
<p>On the Standard plan we also walk you through your Google Business Profile, the listing that shows on Google Maps, so your website and your profile tell the same story.</p></div></section>
{pricing_block()}
<section><div class="wrap"><h2>Questions {E(i['owner'])} ask</h2>{faq_html(faqs)}</div></section>
{cta_band()}
<section><div class="wrap"><h2>Other industries we build for</h2><ul class="links">{others}</ul></div></section>
</main>"""
    page = {"@type": "WebPage", "@id": BASE + path, "url": BASE + path, "name": title, "keywords": ", ".join(kw + i["search"]), "about": {"@id": BASE + "/#business"}, "inLanguage": "en-US"}
    write(path, head(title, desc, path, [ORG, page, service, crld, faq_ld(faqs)]) + body + footer())
    return path

def industries_hub():
    path = "/websites-for/"
    title = "Websites for Local Businesses by Industry | Storefront Studio"
    desc = "Fixed-price websites for US barbershops, salons, restaurants, dentists, roofers, plumbers, HVAC, gyms and more. Free concept first, live the same day."
    cr, crld = crumbs([("Home", "/"), ("Industries", path)])
    cards = "".join(f'<a class="card" style="text-decoration:none" href="/websites-for/{i["slug"]}/"><h3>{E(i["name"])}</h3><p>{E(i["intro"][:120].rsplit(" ",1)[0])}…</p></a>' for i in INDUSTRIES)
    body = f"""{cr}<main><header class="hero wrap"><h1>Websites for every kind of local business.</h1>
<p class="lede">Pick your trade to see what we build for businesses like yours, what it costs and how it goes live the same day.</p></header>
<section><div class="wrap"><div class="grid">{cards}</div></div></section>{cta_band()}</main>"""
    lst = {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": n + 1, "url": f"{BASE}/websites-for/{i['slug']}/", "name": i["name"]} for n, i in enumerate(INDUSTRIES)]}
    write(path, head(title, desc, path, [ORG, crld, lst]) + body + footer())
    return path

def guide_page(g):
    path = f"/guides/{g['slug']}/"
    cr, crld = crumbs([("Home", "/"), ("Guides", "/guides/"), (g["title"], path)])
    art = {"@type": "Article", "headline": g["title"], "description": g["desc"], "datePublished": "2026-10-29", "dateModified": TODAY,
           "author": {"@type": "Person", "name": "George", "worksFor": {"@id": BASE + "/#business"}}, "publisher": {"@id": BASE + "/#business"},
           "mainEntityOfPage": BASE + path, "image": BASE + "/og.png", "inLanguage": "en-US"}
    secs = "".join(f"<h2>{E(h)}</h2><p>{E(p)}</p>" for h, p in g["body"])
    more = "".join(f'<li><a href="/guides/{o["slug"]}/">{E(o["title"])}</a></li>' for o in GUIDES if o is not g)
    body = f"""{cr}<main><header class="hero wrap"><h1>{E(g['title'])}</h1><p class="lede">{E(g['desc'])}</p>
<p class="note">By George, founder of Storefront Studio. Updated {datetime.date.today().strftime('%B %Y')}.</p></header>
<section><div class="wrap prose">{secs}</div></section>{cta_band()}
<section><div class="wrap"><h2>More guides</h2><ul class="links">{more}<li><a href="/websites-for/">Websites by industry</a></li></ul></div></section></main>"""
    write(path, head(f"{g['title']} | Storefront Studio", g["desc"], path, [ORG, art, crld]) + body + footer())
    return path

def guides_hub():
    path = "/guides/"
    cr, crld = crumbs([("Home", "/"), ("Guides", path)])
    cards = "".join(f'<a class="card" style="text-decoration:none" href="/guides/{g["slug"]}/"><h3>{E(g["title"])}</h3><p>{E(g["desc"])}</p></a>' for g in GUIDES)
    body = f"""{cr}<main><header class="hero wrap"><h1>Free guides for local business owners.</h1>
<p class="lede">Plain-English advice on websites, Google and getting more calls. No jargon.</p></header>
<section><div class="wrap"><div class="grid">{cards}</div></div></section>{cta_band()}</main>"""
    write(path, head("Website and Local Search Guides for Small Businesses | Storefront Studio", "Free, plain-English guides for US small business owners: website costs, Google Business Profile and a website checklist.", path, [ORG, crld]) + body + footer())
    return path

def start_page():
    path = "/start/"
    o = OFFER
    cr, crld = crumbs([("Home", "/"), ("Get started", path)])
    steps = [("1. Get your free concept", "Send your business name and city with the form on the homepage, by email, or call the assistant. We design your homepage and send it the same day."),
             ("2. Say yes and pay the deposit", f"Like it? Pay 50% through our secure payment link (card or US bank transfer). Founding prices: Starter deposit ${o['founding']//2:,}, Standard deposit ${o['standard_founding']//2:,}. Regular prices: ${o['regular']//2:,} and ${o['standard']//2:,}. You type the amount on the payment page."),
             ("3. Send your details", "Logo, 5 to 15 photos, services or menu with prices, hours and a few words about you. Never send passwords."),
             ("4. Go live", "Your site is online the same day if everything arrives by 12 pm Eastern on a weekday. Two rounds of changes included. Pay the other 50% when you approve it.")]
    st = "".join(f'<div class="card"><h3>{E(h)}</h3><p>{E(p)}</p></div>' for h, p in steps)
    howto = {"@type": "HowTo", "name": "How to get a website from Storefront Studio", "step": [{"@type": "HowToStep", "name": h, "text": p} for h, p in steps]}
    body = f"""{cr}<main><header class="hero wrap"><h1>From hello to live website in one day.</h1>
<p class="lede">Four simple steps. You spend about ten minutes; we do the rest.</p>
<div class="ctas"><a class="btn primary" href="/#contact">Get my free concept</a><a class="btn quiet" href="tel:{TEL}">Call {TEL_TXT}</a></div></header>
<section><div class="wrap"><div class="grid">{st}</div></div></section>
<section><div class="wrap"><h2>Already approved your concept?</h2>
<p class="lede" style="margin-top:0">Pay your deposit with the secure payment link. Enter the exact amount from your confirmation email. If your first design isn't right for you, the full deposit comes back.</p>
<div class="ctas"><a class="btn primary" href="{PAY}" rel="nofollow noopener" target="_blank">Pay my deposit securely</a><a class="btn quiet" href="mailto:{MAIL}?subject=Question%20about%20my%20website">Ask a question first</a></div>
<p class="note">Payments are processed by Payoneer. We never ask for card details by email or phone.</p></div></section>
{pricing_block()}<section><div class="wrap"><h2>Questions</h2>{faq_html(GENERAL_FAQ)}</div></section></main>"""
    write(path, head("Get Started: Free Concept, Deposit and Same-Day Launch | Storefront Studio", "How to get your website from Storefront Studio: free concept, 50% deposit by secure link, send your details, live the same day.", path, [ORG, crld, howto, faq_ld(GENERAL_FAQ)]) + body + footer())
    return path


CHECKS = [
  ("first", "Your business name and what you do are clear on the first screen of a phone", "Put your name and one line about what you do at the very top."),
  ("first", "Your phone number is one tap away", "Add a tap-to-call button that stays on screen on phones."),
  ("first", "Your hours are visible without searching", "Show your hours on the first screen, ideally with a live open-now badge."),
  ("first", "There is a button for directions", "Add a directions button that opens Google or Apple Maps."),
  ("trust", "There are real photos of your place, team or work", "Replace stock or missing photos with real ones of your business."),
  ("trust", "Your reviews, or a link to them, are on the site", "Show your Google rating and link to your reviews."),
  ("trust", "The copyright year is current and no template text is left", "Remove leftover template text and update the footer year."),
  ("trust", "Licenses, insurance or credentials are shown if your trade needs them", "List your license and insurance details where customers can see them."),
  ("action", "There is a clear Book, Order or Get a quote button", "Add one main action button that leads straight to booking, ordering or a quote."),
  ("action", "Your prices, or starting prices, are listed", "List your services with prices or starting prices."),
  ("action", "Your contact form works and goes to an inbox you read", "Test your form today; if it fails, customers are being lost silently."),
  ("speed", "The site loads in a couple of seconds on mobile data", "Compress your photos and drop heavy plugins so the site loads fast."),
]

def check_page():
    path = "/website-check/"
    cr, crld = crumbs([("Home", "/"), ("Free website check", path)])
    qs = "".join(f'<label class="card q" style="display:flex;gap:14px;align-items:flex-start;cursor:pointer"><input type="checkbox" data-fix="{E(fix)}" style="width:22px;height:22px;margin-top:3px;accent-color:var(--cobalt)"><span>{E(q)}</span></label>' for _, q, fix in CHECKS)
    app = {"@type": "WebApplication", "name": "Free local business website check", "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "provider": {"@id": BASE + "/#business"}, "url": BASE + path}
    js = """<script>(()=>{const boxes=[...document.querySelectorAll('.q input')],sc=document.getElementById('score'),bar=document.getElementById('bar'),fx=document.getElementById('fixes'),msg=document.getElementById('msg'),go=document.getElementById('go');
const upd=()=>{const yes=boxes.filter(b=>b.checked).length,n=boxes.length,pct=Math.round(yes/n*100);sc.textContent=yes+' / '+n;bar.style.width=pct+'%';
const miss=boxes.filter(b=>!b.checked).map(b=>b.dataset.fix);fx.innerHTML=miss.slice(0,5).map(t=>'<li>'+t.replace(/</g,'&lt;')+'</li>').join('');
msg.textContent=yes===n?'Great site. Most local businesses miss at least three of these.':yes>=9?'Close. A few fixes would turn more visitors into calls.':yes>=5?'Your site is losing customers on the points below.':'Your website is probably costing you customers every day.';
const biz=document.getElementById('biz').value||'my business';go.href='mailto:__MAIL__?subject='+encodeURIComponent('Free concept: '+biz+' (website check '+yes+'/'+n+')')+'&body='+encodeURIComponent('Business: '+biz+'\\nCity: '+(document.getElementById('city').value||'')+'\\nWebsite check score: '+yes+'/'+n+'\\nTo fix:\\n- '+miss.join('\\n- '));};
boxes.forEach(b=>b.addEventListener('change',upd));document.querySelectorAll('#biz,#city').forEach(i=>i.addEventListener('input',upd));upd();})();</script>""".replace("__MAIL__", MAIL)
    body = f"""{cr}<main><header class="hero wrap"><h1>Is your website costing you customers?</h1>
<p class="lede">Take this free 12-point check on your phone. Tick what your website already does. You'll get a score and the fixes that matter most, in about two minutes.</p></header>
<section><div class="wrap"><div class="grid" style="grid-template-columns:1fr">{qs}</div></div></section>
<section><div class="wrap"><div class="card" style="padding:28px"><p class="note" style="margin:0">Your score</p><p class="price" id="score">0 / 12</p>
<div style="height:10px;border-radius:9px;background:var(--hair);margin:12px 0 18px;overflow:hidden"><div id="bar" style="height:100%;width:0;background:var(--cobalt);transition:width .3s"></div></div>
<h3 id="msg"></h3><ul class="ticks" id="fixes" style="margin-top:14px"></ul>
<h3 style="margin-top:26px">Get these fixed in one day</h3><p>We'll design a free concept of your new homepage that fixes everything above, and send it the same day.</p>
<div class="grid" style="margin-top:14px"><label>Business name<br><input id="biz" style="width:100%;min-height:46px;border-radius:12px;border:1px solid var(--hair);padding:0 12px;font:inherit;background:var(--porcelain);color:var(--ink)"></label><label>City and state<br><input id="city" style="width:100%;min-height:46px;border-radius:12px;border:1px solid var(--hair);padding:0 12px;font:inherit;background:var(--porcelain);color:var(--ink)"></label></div>
<div class="ctas"><a class="btn primary" id="go" href="mailto:{MAIL}">Send me my free concept</a><a class="btn quiet" href="tel:{TEL}">Call {TEL_TXT}</a></div>
<p class="note">Sending opens your email app with your score filled in. The phone line is an AI assistant, available 24/7.</p></div></div></section>
<section><div class="wrap prose"><h2>Why these 12 points</h2><p>Most people find a local business on their phone, decide in seconds, and call or book the first one that answers their question. Each point on this list removes one reason to leave. See the full explanation in our <a href="/guides/local-business-website-checklist/">website checklist guide</a>.</p></div></section></main>{js}"""
    write(path, head("Free Website Check for Local Businesses (12 Points, 2 Minutes) | Storefront Studio", "Free 12-point website check for US small businesses. Get a score and the fixes that bring in more calls and bookings, then a free homepage concept.", path, [ORG, crld, app]) + body + footer())
    return path

def referral_page():
    path = "/referrals/"
    cr, crld = crumbs([("Home", "/"), ("Referrals", path)])
    body = f"""{cr}<main><header class="hero wrap"><h1>Know an owner who needs a better website?</h1>
<p class="lede">Introduce them. When they become a client, you get a free month of the care plan for each one. No limit, nothing to sign.</p>
<div class="ctas"><a class="btn primary" href="mailto:{MAIL}?subject=Referral&body=Business%20I'm%20referring%3A%0ACity%3A%0ATheir%20email%20or%20phone%20(with%20their%20OK)%3A%0AMy%20business%3A">Send a referral</a><a class="btn quiet" href="tel:{TEL}">Call {TEL_TXT}</a></div></header>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>1. Tell us who</h3><p>Email us their business name and city. Only share their contact details if they said it's OK.</p></div>
<div class="card"><h3>2. We do the rest</h3><p>We design a free concept of their homepage and send it to them, mentioning you sent them.</p></div>
<div class="card"><h3>3. You get a free month</h3><p>When they pay their deposit, your next month of the care plan is free. Not on the care plan yet? It starts your first month free.</p></div>
</div></div></section>{cta_band("Not a client yet?", "Start with your own free concept. Our first ten clients also get 20% off.")}</main>"""
    write(path, head("Referral Program: A Free Month for Every Owner You Introduce | Storefront Studio", "Refer a local business owner to Storefront Studio. When they become a client, you get a free month of the website care plan.", path, [ORG, crld]) + body + footer())
    return path

STATES = "Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada New_Hampshire New_Jersey New_Mexico New_York North_Carolina North_Dakota Ohio Oklahoma Oregon Pennsylvania Rhode_Island South_Carolina South_Dakota Tennessee Texas Utah Vermont Virginia Washington West_Virginia Wisconsin Wyoming".replace("_", " ").split()
def states_page():
    path = "/serving-all-50-states/"
    cr, crld = crumbs([("Home", "/"), ("Serving all 50 states", path)])
    tz = [("Eastern (New York, Florida, Ohio, Georgia)", "12 pm", "same evening"), ("Central (Texas, Illinois, Tennessee, Missouri)", "11 am", "same evening"), ("Mountain (Colorado, Utah, New Mexico; Arizona 9 am in summer)", "10 am", "same evening"), ("Pacific (California, Washington, Oregon)", "9 am", "same evening"), ("Alaska and Hawaii", "8 am Alaska, 7 am Hawaii (6 am in summer)", "same day, your time")]
    rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in tz)
    st = "".join(f"<li>Websites for small businesses in {E(x)}</li>" for x in STATES)
    inds = "".join(f'<li><a href="/websites-for/{i["slug"]}/">{E(i["name"])}</a></li>' for i in INDUSTRIES)
    body = f"""{cr}<main><header class="hero wrap"><h1>Websites for local businesses in all 50 states.</h1>
<p class="lede">We work remotely with owners anywhere in the US, by email, phone and video. Same fixed prices everywhere, a free concept first, and launch the same day in your time zone.</p>
<div class="ctas"><a class="btn primary" href="/#contact">Get my free concept</a><a class="btn quiet" href="tel:{TEL}">Call {TEL_TXT}</a></div></header>
<section><div class="wrap"><h2>Same-day launch in your time zone</h2>
<table style="width:100%;border-collapse:collapse;background:var(--paper);border:1px solid var(--hair);border-radius:16px;overflow:hidden;font-size:15px"><thead><tr style="text-align:left"><th style="padding:12px">Time zone</th><th style="padding:12px">Send your details by</th><th style="padding:12px">Live</th></tr></thead><tbody>{rows}</tbody></table>
<p class="note">Weekdays. Connecting a domain you already own can take a few extra hours.</p></div></section>
<section><div class="wrap"><h2>States we serve</h2><ul class="links">{st}</ul></div></section>
<section><div class="wrap"><h2>Industries we build for</h2><ul class="links">{inds}</ul></div></section>{cta_band()}</main>"""
    css = "<style>td,th{padding:12px;border-top:1px solid var(--hair)}</style>"
    write(path, head("Small Business Websites in All 50 States, Live the Same Day | Storefront Studio", "Fixed-price websites for local businesses across the United States, from New York to California. Free concept first, live the same day in your time zone.", path, [ORG, crld]).replace("</head>", css + "</head>") + body + footer())
    return path

def not_found():
    body = f"""<main><header class="hero wrap"><h1>This page isn't here.</h1><p class="lede">It may have moved. Try the homepage, or find websites for your industry.</p>
<div class="ctas"><a class="btn primary" href="/">Go to homepage</a><a class="btn quiet" href="/websites-for/">Websites by industry</a></div></header></main>"""
    open(os.path.join(ROOT, "404.html"), "w").write(head("Page not found | Storefront Studio", "Page not found.", "/404.html", [ORG], noindex=True) + body + footer())

def robots_sitemap_llms(paths):
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /concepts/\nDisallow: /_studio/\n\nSitemap: {BASE}/sitemap.xml\n")
    urls = ["/"] + paths
    pri = lambda p: "1.0" if p == "/" else ("0.8" if p.startswith("/websites-for/") or p == "/start/" else "0.7")
    xml = "".join(f"<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pri(p)}</priority></url>" for p in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{xml}</urlset>\n')
    lines = [f"# Storefront Studio", "", "> Fixed-price websites for US local businesses (barbers, salons, restaurants, dentists, contractors and more), live the same day. Free homepage concept before payment. Starter $1,200 (founding $960), Standard $2,000 (founding $1,600), care plan $79/month. 50% deposit, refundable if the first design isn't liked.", "",
             f"Contact: {TEL_TXT} (AI assistant, 24/7), {MAIL}", "", "## Pages", f"- [Home]({BASE}/)", f"- [Get started]({BASE}/start/)", f"- [Websites by industry]({BASE}/websites-for/)"]
    lines += [f"- [Websites for {i['name'].lower()}]({BASE}/websites-for/{i['slug']}/)" for i in INDUSTRIES]
    lines += ["", "## Guides"] + [f"- [{g['title']}]({BASE}/guides/{g['slug']}/): {g['desc']}" for g in GUIDES]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(lines) + "\n")

def patch_home():
    p = os.path.join(ROOT, "index.html")
    h = open(p).read()
    h = re.sub(r"\n?<!-- SEO:start -->.*?<!-- SEO:end -->", "", h, flags=re.S)
    h = re.sub(r"\n?<!-- SEOFOOT:start -->.*?<!-- SEOFOOT:end -->", "", h, flags=re.S)
    h = re.sub(r"<title>.*?</title>", "<title>Websites for US Small Businesses, Live the Same Day | Storefront Studio</title>", h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Fixed-price websites for US local businesses: barbers, salons, restaurants, dentists, roofers and more. See a free concept first, go live the same day. From $960.">', h, count=1)
    h = h.replace('<html lang="en">', '<html lang="en-US">', 1)
    faq = [(re.sub(r"<[^>]+>", "", q).strip(), re.sub(r"<[^>]+>", "", a).strip()) for q, a in re.findall(r"<summary[^>]*>(.*?)</summary>\s*<p>(.*?)</p>", h, flags=re.S)]
    site = {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "Storefront Studio", "publisher": {"@id": BASE + "/#business"}, "inLanguage": "en-US"}
    graph = [ORG, site] + ([faq_ld(faq)] if faq else [])
    seo = f"""
<!-- SEO:start -->
{analytics()}
<link rel="canonical" href="{BASE}/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:url" content="{BASE}/"><meta property="og:image" content="{BASE}/og.png"><meta property="og:site_name" content="Storefront Studio"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{BASE}/og.png">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>
<!-- SEO:end -->"""
    h = h.replace("</head>", seo + "\n</head>", 1)
    links = " · ".join(f'<a href="/websites-for/{i["slug"]}/">{E(i["name"])}</a>' for i in INDUSTRIES)
    gl = " · ".join(f'<a href="/guides/{g["slug"]}/">{E(g["title"])}</a>' for g in GUIDES)
    foot = f"""
<!-- SEOFOOT:start -->
<div class="wrap" style="font-size:13.5px;line-height:1.9;color:var(--graphite);padding-top:18px;padding-bottom:28px"><p><b style="color:var(--ink)">Websites for:</b> {links}</p><p style="margin-top:8px"><b style="color:var(--ink)">Free guides:</b> {gl} · <a href="/start/">How to get started</a> · <a href="/website-check/"><b>Free website check</b></a> · <a href="/serving-all-50-states/">Serving all 50 states</a> · <a href="/referrals/">Referrals</a></p></div>
<!-- SEOFOOT:end -->"""
    h = h.replace("</footer>", foot + "\n</footer>", 1)
    if 'href="/website-check/">Free check' not in h:
        h = h.replace('<li><a href="#faq">Questions</a></li>', '<li><a href="#faq">Questions</a></li><li><a href="/website-check/">Free check</a></li>', 1)
    open(p, "w").write(h)

if __name__ == "__main__":
    paths = [industries_hub()] + [industry_page(i) for i in INDUSTRIES] + [guides_hub()] + [guide_page(g) for g in GUIDES] + [start_page(), check_page(), referral_page(), states_page()]
    not_found(); robots_sitemap_llms(paths); patch_home()
    print(f"built {len(paths)} pages + 404, robots.txt, sitemap.xml, llms.txt; homepage patched")
