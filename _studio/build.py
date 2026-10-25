#!/usr/bin/env python3
"""Storefront Studio site builder.

Usage:  python3 _studio/build.py            (builds every site in sites.py into concepts/<slug>/)
        python3 _studio/build.py legends-barber-shop

Each business gets its own identity (palette, type, hero layout, signature section)
from its entry in sites.py. Only real facts go into sites.py.
"""
import html, json, os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from sites import SITES, PX

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: html.escape(str(s), quote=True)
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAYN = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}


def tel(p):
    d = "".join(c for c in p if c.isdigit())
    return "+1" + d[-10:]


def fmt_t(t):
    h, m = map(int, t.split(":"))
    ap = "am" if h < 12 else "pm"
    h12 = h % 12 or 12
    return f"{h12}{'' if m == 0 else ':%02d' % m}{ap}"


def maps(s):
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(f"{s['name']} {s['address']} {s['city']}")


def stars(r):
    full = int(round(r))
    return "★" * full + "☆" * (5 - full)


def rating_line(s):
    rv = f" from {s['reviews']} reviews" if s.get("reviews") else " on Google"
    return f"{s['rating']:.1f}{rv}"


def hours_block(s):
    if not s.get("hours"):
        return f'<p class="hours-note">{E(s.get("hours_note", "Call for today’s hours."))}</p>'
    rows = []
    for d in DAYS:
        v = s["hours"].get(d)
        val = "Closed" if not v else f"{fmt_t(v.split('-')[0])} – {fmt_t(v.split('-')[1])}"
        rows.append(f'<tr data-day="{d}"><th scope="row">{DAYN[d]}</th><td>{val}</td></tr>')
    return '<table class="hours">' + "".join(rows) + "</table>"


def services_block(s):
    unit = "salon" if s["kind"] == "salon" else ("office" if s["kind"] == "dental" else "shop")
    items = []
    for name, note, price in s["services"]:
        tail = f'<span class="dots" aria-hidden="true"></span><strong>{E(price)}</strong>' if price else ""
        items.append(f'<li class="{"" if price else "np"}"><div><h3>{E(name)}</h3><p>{E(note)}</p></div>{tail}</li>')
    foot = {"barber": "Ask the shop for current prices.", "salon": "Prices depend on hair length and the look you want. Ask the salon.",
            "dental": "Ask about your insurance when you call."}[s["kind"]]
    if s.get("cash_only"):
        foot += " Cash only."
    return f'<ul class="menu">{"".join(items)}</ul><p class="fine">{E(foot)}</p>'


def signature_block(s):
    g = s["signature"]; t = g["type"]
    if t in ("steps", "directions"):
        lis = "".join(f'<li><span class="n">{i}</span><div><h3>{E(a)}</h3><p>{E(b)}</p></div></li>' for i, (a, b) in enumerate(g["steps"], 1))
        extra = f'<a class="btn ghost" href="{maps(s)}" target="_blank" rel="noopener">Open in Google Maps</a>' if t == "directions" else ""
        intro = f'<p class="sig-body">{E(g.get("body",""))}</p>' if g.get("body") else ""
        return f'<div class="sig sig-steps"><h2>{E(g["title"])}</h2>{intro}<ol class="steps">{lis}</ol>{extra}</div>'
    if t == "locations":
        a = f'<div class="loc"><h3>Broad Ripple</h3><p>{E(s["address"].replace(" (Broad Ripple)",""))}</p><a href="tel:{tel(s["phone"])}">{E(s["phone"])}</a></div>'
        n, ph, ad = s["phone2"]
        b = f'<div class="loc"><h3>{E(n)}</h3><p>{E(ad)}</p><a href="tel:{tel(ph)}">{E(ph)}</a></div>'
        return f'<div class="sig sig-locs"><h2>{E(g["title"])}</h2><p class="sig-body">{E(g["body"])}</p><div class="locs">{a}{b}</div></div>'
    if t == "salute":
        return f'<div class="sig sig-big"><div class="bignum">$25</div><div><h2>{E(g["title"])}</h2><p class="sig-body">{E(g["body"])}</p></div></div>'
    if t == "clock":
        return f'<div class="sig sig-big"><div class="bignum" data-clock>9pm</div><div><h2>{E(g["title"])}</h2><p class="sig-body">{E(g["body"])}</p></div></div>'
    if t == "board":
        return f'<div class="sig sig-board"><h2>{E(g["title"])}</h2><p class="sig-body">{E(g["body"])}</p><div class="board">{hours_block(s)}</div></div>'
    photo = PX.format(s["theme"]["photo2"], 1200)
    return f'<div class="sig sig-photo"><img src="{photo}" alt="" loading="lazy"><div><h2>{E(g["title"])}</h2><p class="sig-body">{E(g["body"])}</p></div></div>'


CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
.menu li.np{grid-template-columns:1fr}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body),system-ui,sans-serif;font-size:1.0625rem;line-height:1.6;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
a{color:inherit}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:4px}
.wrap{width:min(1180px,100% - 40px);margin-inline:auto}
.banner{background:var(--ink);color:var(--bg);font-size:.8125rem;text-align:center;padding:8px 16px}
.banner a{color:inherit}
header.top{position:absolute;inset:auto 0 auto 0;z-index:5}
.nav{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:22px 0}
.brand{font-family:var(--display);font-weight:var(--dw);font-stretch:var(--ds);font-size:1.25rem;letter-spacing:var(--tr);text-decoration:none;line-height:1}
.nav .links{display:flex;gap:28px;align-items:center;font-size:.95rem}
.nav .links a{text-decoration:none;opacity:.85}
.nav .links a:hover{opacity:1}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:0 26px;border-radius:999px;background:var(--accent);color:var(--on);font-weight:600;text-decoration:none;border:0;font:inherit;font-weight:600;cursor:pointer;transition:transform .15s ease,filter .15s ease}
.btn:hover{filter:brightness(1.06)}
.btn:active{transform:scale(.98)}
.btn.ghost{background:transparent;color:inherit;box-shadow:inset 0 0 0 1.5px currentColor}
.btn.small{min-height:42px;padding:0 18px;font-size:.95rem}
.open{display:inline-flex;align-items:center;gap:8px;font-size:.9rem;font-weight:600}
.open i{width:9px;height:9px;border-radius:50%;background:var(--muted)}
.open.is-open i{background:#3DDC84;box-shadow:0 0 0 4px rgba(61,220,132,.22)}
.stars{color:var(--accent);letter-spacing:2px}
/* hero: full */
.hero{position:relative}
.hero-full{min-height:min(92vh,820px);display:flex;align-items:flex-end;color:#fff;isolation:isolate}
.hero-full .bg{position:absolute;inset:0;z-index:-1}
.hero-full .bg img{width:100%;height:100%;object-fit:cover}
.hero-full .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,.05) 30%,rgba(0,0,0,.72) 100%)}
.hero-full .copy{padding:140px 0 64px}
/* hero: split */
.hero-split{display:grid;grid-template-columns:1.05fr .95fr;min-height:min(92vh,820px)}
.hero-split .copy{display:flex;flex-direction:column;justify-content:flex-end;padding:140px clamp(20px,5vw,72px) 64px max(20px,calc((100vw - 1180px)/2))}
.hero-split .pic{position:relative;overflow:hidden}
.hero-split .pic img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
/* hero: type */
.hero-type .copy{padding:150px 0 40px}
.hero-type .strip{height:clamp(240px,42vw,520px);overflow:hidden}
.hero-type .strip img{width:100%;height:100%;object-fit:cover}
h1{font-family:var(--display);font-weight:var(--dw);font-stretch:var(--ds);letter-spacing:var(--tr);line-height:.95;font-size:clamp(3rem,8.4vw,7.4rem);margin:0 0 22px;white-space:pre-line}
.hero-type h1{font-size:clamp(3.2rem,11vw,10rem)}
.lede{font-size:clamp(1.1rem,1.6vw,1.3rem);max-width:34ch;margin:0 0 30px;opacity:.92}
.actions{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.proof{display:flex;flex-wrap:wrap;gap:10px 22px;align-items:center;margin-top:28px;font-size:.95rem}
section{padding:clamp(72px,10vw,128px) 0}
h2{font-family:var(--display);font-weight:var(--dw);font-stretch:var(--ds);letter-spacing:var(--tr);font-size:clamp(2.1rem,4.6vw,3.6rem);line-height:1;margin:0 0 18px}
.sig-body{font-size:1.15rem;max-width:46ch;color:var(--muted);margin:0 0 28px}
.panel{background:var(--panel)}
.two{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(32px,6vw,96px);align-items:start}
.menu{list-style:none;margin:0;padding:0}
.menu li{display:grid;grid-template-columns:auto 1fr auto;align-items:baseline;gap:16px;padding:20px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 14%,transparent)}
.menu li:first-child{border-top:1px solid color-mix(in srgb,var(--ink) 14%,transparent)}
.menu h3{font-size:1.2rem;margin:0;font-weight:600}
.menu p{margin:2px 0 0;color:var(--muted);font-size:.95rem}
.menu .dots{border-bottom:1.5px dotted color-mix(in srgb,var(--ink) 30%,transparent);transform:translateY(-6px)}
.menu strong{font-family:var(--display);font-weight:var(--dw);font-size:1.3rem;white-space:nowrap}
.fine{font-size:.875rem;color:var(--muted);margin-top:18px}
.sig-big{display:grid;grid-template-columns:auto 1fr;gap:clamp(24px,5vw,80px);align-items:center}
.bignum{font-family:var(--display);font-weight:var(--dw);font-stretch:var(--ds);letter-spacing:var(--tr);font-size:clamp(6rem,20vw,15rem);line-height:.8;color:var(--accent)}
.sig-photo{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,80px);align-items:center}
.sig-photo img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:var(--r)}
.steps{list-style:none;margin:0 0 28px;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.steps li{display:flex;flex-direction:column;gap:14px}
.steps .n{font-family:var(--display);font-weight:var(--dw);font-size:3rem;line-height:1;color:var(--accent)}
.steps h3{margin:0 0 6px;font-size:1.15rem}
.steps p{margin:0;color:var(--muted)}
.locs{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.loc{background:var(--panel);border-radius:var(--r);padding:28px}
.loc h3{font-family:var(--display);font-weight:var(--dw);font-size:1.8rem;margin:0 0 6px;letter-spacing:var(--tr)}
.loc p{margin:0 0 14px;color:var(--muted)}
.loc a{font-weight:600;text-decoration:none;border-bottom:2px solid var(--accent)}
.board{background:var(--ink);color:var(--bg);border-radius:var(--r);padding:clamp(20px,4vw,40px);max-width:560px}
.hours{width:100%;border-collapse:collapse}
.hours th,.hours td{padding:10px 0;text-align:left;border-bottom:1px solid color-mix(in srgb,currentColor 14%,transparent);font-weight:400}
.hours td{text-align:right}
.hours tr.today th,.hours tr.today td{font-weight:700;color:var(--accent)}
.hours-note{margin:0;color:var(--muted)}
.board .hours-note{color:inherit;opacity:.85}
.visit{display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,6vw,96px)}
.visit address{font-style:normal;font-size:1.3rem;line-height:1.45;margin-bottom:22px}
.visit .phone{display:block;font-family:var(--display);font-weight:var(--dw);font-size:clamp(1.8rem,3.4vw,2.6rem);letter-spacing:var(--tr);text-decoration:none;margin-bottom:24px}
footer{padding:40px 0 120px;font-size:.875rem;color:var(--muted);border-top:1px solid color-mix(in srgb,var(--ink) 12%,transparent)}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px}
.bar{position:fixed;left:12px;right:12px;bottom:12px;z-index:20;display:none;grid-template-columns:1fr 1fr 1.3fr;gap:8px;padding:8px;border-radius:999px;background:color-mix(in srgb,var(--ink) 92%,transparent);backdrop-filter:blur(10px);box-shadow:0 10px 30px rgba(0,0,0,.25)}
.bar a{display:flex;align-items:center;justify-content:center;min-height:48px;border-radius:999px;color:var(--bg);text-decoration:none;font-weight:600;font-size:.95rem}
.bar a.main{background:var(--accent);color:var(--on)}
.reveal{opacity:0;transform:translateY(18px)}
.ready .reveal{opacity:1;transform:none;transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.ready .reveal.d2{transition-delay:.12s}.ready .reveal.d3{transition-delay:.24s}
.hero img.kb{transform:scale(1.08)}
.ready .hero img.kb{transform:scale(1);transition:transform 2.2s cubic-bezier(.2,.7,.2,1)}
@media (max-width:860px){
 .nav .links a.hide-m{display:none}
 .hero-split{grid-template-columns:1fr}
 .hero-split .pic{order:-1;height:56vh;min-height:320px}
 .hero-split .copy{padding:36px 20px 48px}
 header.top{position:absolute}
 .hero-split header.top{color:#fff}
 .two,.visit,.sig-photo,.sig-big,.locs{grid-template-columns:1fr}
 .steps{grid-template-columns:1fr}
 .bar{display:grid}
 .menu li{grid-template-columns:1fr auto}
 .menu .dots{display:none}
}
@media (prefers-reduced-motion:reduce){.reveal,.ready .reveal,.hero img.kb,.ready .hero img.kb{opacity:1;transform:none;transition:none}}
"""

JS = r"""
(function(){
 var S=window.__SITE__;
 requestAnimationFrame(function(){document.documentElement.classList.add('ready')});
 function nowIn(tz){var p=new Intl.DateTimeFormat('en-US',{timeZone:tz,weekday:'short',hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date());var o={};p.forEach(function(x){o[x.type]=x.value});return {d:o.weekday,m:(+o.hour%24)*60+(+o.minute)}}
 var n=nowIn(S.tz), badge=document.querySelectorAll('[data-open]');
 document.querySelectorAll('tr[data-day="'+n.d+'"]').forEach(function(r){r.classList.add('today')});
 if(!S.hours){badge.forEach(function(b){b.hidden=true});return}
 var h=S.hours[n.d], open=false, txt='Closed today';
 if(h){var a=h.split('-'),s=a[0].split(':'),e=a[1].split(':'),sm=+s[0]*60+ +s[1],em=+e[0]*60+ +e[1];
  if(n.m>=sm&&n.m<em){open=true;txt='Open now · until '+fmt(a[1])}else if(n.m<sm){txt='Opens today at '+fmt(a[0])}else{txt='Closed now'}}
 badge.forEach(function(b){b.querySelector('span').textContent=txt;b.classList.toggle('is-open',open)});
 function fmt(t){var q=t.split(':'),H=+q[0],M=+q[1];return (H%12||12)+(M?':'+(M<10?'0':'')+M:'')+(H<12?'am':'pm')}
})();
"""


def page(s):
    t = s["theme"]
    dark = t["bg"].lstrip("#")
    lum = sum(int(dark[i:i + 2], 16) for i in (0, 2, 4)) / 3
    on = "#111111" if lum < 128 and t["accent"] in ("#D4A72C", "#FF8A3D", "#F0B53C", "#E8A27C") else ("#FFFFFF" if lum >= 128 or t["accent"] in ("#D7263D",) else "#111111")
    if t["accent"] in ("#D7263D", "#8E1B1B", "#A4472F", "#5E7A5A", "#2F5D46", "#0F7A72", "#B4643A"):
        on = "#FFFFFF"
    hero_img = PX.format(t["photo"], 2000)
    book_href = s["book_url"] or f"tel:{tel(s['phone'])}"
    book_attr = ' target="_blank" rel="noopener"' if s["book_url"] else ""
    call = f'<a class="btn ghost" href="tel:{tel(s["phone"])}">Call {E(s["phone"])}</a>'
    main = f'<a class="btn" href="{E(book_href)}"{book_attr}>{E(s["cta"])}</a>'
    badge = '<span class="open" data-open><i></i><span>Hours</span></span>'
    proof = f'<div class="proof reveal d3"><span><span class="stars" aria-hidden="true">{stars(s["rating"])}</span> {E(rating_line(s))}</span>{badge}</div>'
    copy = f'<h1 class="reveal">{E(s["headline"])}</h1><p class="lede reveal d2">{E(s["lede"])}</p><div class="actions reveal d2">{main}{call}</div>{proof}'
    nav = f'<header class="top"><div class="wrap nav"><a class="brand" href="#">{E(s["name"])}</a><nav class="links" aria-label="Main"><a class="hide-m" href="#menu">Services</a><a class="hide-m" href="#visit">Visit</a><a class="btn small" href="{E(book_href)}"{book_attr}>{E(s["cta"])}</a></nav></div></header>'
    if t["hero"] == "full":
        hero = f'<div class="hero hero-full">{nav}<div class="bg"><img class="kb" src="{hero_img}" alt="" fetchpriority="high"></div><div class="wrap copy">{copy}</div></div>'
    elif t["hero"] == "split":
        hero = f'<div class="hero hero-split">{nav}<div class="copy">{copy}</div><div class="pic"><img class="kb" src="{hero_img}" alt="" fetchpriority="high"></div></div>'
    else:
        hero = f'<div class="hero hero-type">{nav}<div class="wrap copy">{copy}</div><div class="strip"><img class="kb" src="{hero_img}" alt="" fetchpriority="high"></div></div>'
    menu_title = {"barber": "Cuts and shaves", "salon": "Services", "dental": "Care for every age"}[s["kind"]]
    menu_intro = s.get("menu_intro") or {"barber": "Walk out sharp. Every cut is finished with care, whatever the style.",
                                         "salon": "Every visit starts with a conversation about the look you want.",
                                         "dental": "From first checkups to same-week help when something hurts."}[s["kind"]]
    second = ""
    if s.get("phone2"):
        n, ph, ad = s["phone2"]
        second = f'<p><strong>{E(n)}</strong><br>{E(ad)} · <a href="tel:{tel(ph)}">{E(ph)}</a></p>'
    data = json.dumps({"tz": s["tz"], "hours": s.get("hours")})
    fonts = f'https://fonts.googleapis.com/css2?family={t["fonts"]}&display=swap'
    hero_color_fix = ".hero-split header.top{color:var(--ink)}@media(max-width:860px){.hero-split header.top{color:#fff}}" if t["hero"] == "split" else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(s['name'])} · concept homepage</title>
<meta name="robots" content="noindex"><meta name="description" content="{E(s['lede'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<style>:root{{--bg:{t['bg']};--ink:{t['ink']};--muted:{t['muted']};--accent:{t['accent']};--panel:{t['panel']};--on:{on};--display:{t['display']};--body:{t['body']};--dw:{t.get('dweight',700)};--ds:{t.get('dstretch','100%')};--tr:{t.get('tracking','0')};--r:{t.get('radius','18px')}}}{CSS}{hero_color_fix}</style>
</head><body>
<div class="banner">Concept preview made for {E(s['name'])} by <a href="https://huszageorge25-wq.github.io/">Storefront Studio</a></div>
<main>
{hero}
<section class="sig-wrap"><div class="wrap">{signature_block(s)}</div></section>
<section id="menu" class="panel"><div class="wrap two"><div><h2>{menu_title}</h2><p class="sig-body">{E(menu_intro)}</p>{main}</div><div>{services_block(s)}</div></div></section>
<section id="visit"><div class="wrap visit"><div><h2>Visit</h2><address>{E(s['name'])}<br>{E(s['address'])}<br>{E(s['city'])}</address><a class="phone" href="tel:{tel(s['phone'])}">{E(s['phone'])}</a>{second}<div class="actions"><a class="btn" href="{maps(s)}" target="_blank" rel="noopener">Get directions</a>{call}</div></div><div><h2>Hours</h2>{badge}<div style="height:16px"></div>{hours_block(s)}</div></div></section>
</main>
<footer><div class="wrap"><span>{E(s['name'])} · {E(s['address'])}, {E(s['city'])}</span><span>Concept by <a href="https://huszageorge25-wq.github.io/">Storefront Studio</a></span></div></footer>
<nav class="bar" aria-label="Quick actions"><a href="tel:{tel(s['phone'])}">Call</a><a href="{maps(s)}" target="_blank" rel="noopener">Directions</a><a class="main" href="{E(book_href)}"{book_attr}>{"Book" if len(s['cta'])>13 else E(s['cta'])}</a></nav>
<script>window.__SITE__={data};{JS}</script>
</body></html>"""


def main():
    want = set(sys.argv[1:])
    for s in SITES:
        if want and s["slug"] not in want:
            continue
        out = os.path.join(ROOT, os.environ.get("OUT", "concepts"), s["slug"])
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "index.html"), "w") as f:
            f.write(page(s))
        print("built", s["slug"])


if __name__ == "__main__":
    main()
