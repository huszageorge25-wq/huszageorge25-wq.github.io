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

DEFAULT_ANIM = {"salute": "stamp", "clock": "countdown", "razor": "razor", "board": "splitflap", "kids": "pulse",
                "new": "badge", "locations": "pins", "botanical": "grow", "shine": "shine", "directions": "route",
                "steps": "progress"}

ANIM_CSS = {
"stamp": """
.anim-stamp h1 .ln{display:block;transform:translateY(-40px) scale(1.15);opacity:0}
.ready .anim-stamp h1 .ln{transform:none;opacity:1;transition:transform .55s cubic-bezier(.3,1.6,.5,1),opacity .2s}
.ready .anim-stamp h1 .ln:nth-child(2){transition-delay:.18s}
.anim-stamp h1::after{content:"";display:block;height:6px;width:0;background:var(--accent);margin-top:14px}
.ready .anim-stamp h1::after{width:min(320px,60%);transition:width .8s .55s cubic-bezier(.2,.7,.2,1)}
""",
"countdown": """
.anim-countdown .bignum{animation:neon 1.6s steps(1) 1 both}
@keyframes neon{0%{opacity:.15}8%{opacity:1}12%{opacity:.3}18%{opacity:1}30%{opacity:.5}34%,100%{opacity:1}}
.left{display:block;font-family:var(--display);font-weight:var(--dw);font-size:clamp(1.4rem,2.6vw,2rem);margin-top:6px;color:var(--ink);font-variant-numeric:tabular-nums}
""",
"razor": """
.anim-razor h1{position:relative;clip-path:inset(0 100% 0 0)}
.ready .anim-razor h1{clip-path:inset(0 0 0 0);transition:clip-path 1.1s cubic-bezier(.7,0,.2,1)}
.anim-razor .blade{position:absolute;top:0;bottom:0;width:3px;background:var(--accent);left:0;opacity:0}
.ready .anim-razor .blade{animation:blade 1.1s cubic-bezier(.7,0,.2,1) both}
@keyframes blade{0%{left:0;opacity:1}90%{opacity:1}100%{left:100%;opacity:0}}
.anim-razor .hl{position:relative;display:inline-block}
""",
"splitflap": """
.anim-splitflap .board tr{transform:rotateX(90deg);transform-origin:top;opacity:0}
.anim-splitflap .board.on tr{transform:none;opacity:1;transition:transform .45s cubic-bezier(.3,1.4,.5,1),opacity .2s}
""",
"pulse": """
.ecg{display:block;width:min(420px,80%);height:56px;margin:4px 0 18px}
.ecg path{fill:none;stroke:var(--accent);stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:900;stroke-dashoffset:900}
.ready .ecg path{stroke-dashoffset:0;transition:stroke-dashoffset 1.8s .3s cubic-bezier(.4,0,.2,1)}
.ecg .dot{fill:var(--accent);transform-box:fill-box;transform-origin:center;opacity:0}
.ready .ecg .dot{animation:beat 1.2s 2s 3 both}
@keyframes beat{0%{opacity:1;transform:scale(1)}15%{transform:scale(1.6)}30%{transform:scale(1)}45%{transform:scale(1.35)}60%,100%{opacity:1;transform:scale(1)}}
""",
"badge": """
.stampbadge{position:absolute;right:clamp(16px,4vw,48px);top:clamp(90px,14vh,140px);width:150px;height:150px;z-index:3;opacity:0;transform:rotate(-140deg) scale(.4)}
.ready .stampbadge{opacity:1;transform:rotate(-12deg) scale(1);transition:transform 1s .6s cubic-bezier(.3,1.5,.5,1),opacity .3s .6s}
.stampbadge svg{width:100%;height:100%;animation:spin 30s linear infinite}
.stampbadge text{font-family:var(--display);font-weight:var(--dw);font-size:15px;letter-spacing:2px;fill:var(--on)}
.stampbadge .core{position:absolute;inset:34px;border-radius:50%;background:var(--accent);color:var(--on);display:grid;place-items:center;font-family:var(--display);font-weight:var(--dw);font-size:1.7rem;line-height:1}
.stampbadge circle.ring{fill:var(--accent)}
@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:860px){.stampbadge{width:112px;height:112px;top:auto;bottom:16px;right:16px}.stampbadge .core{inset:26px;font-size:1.25rem}}
""",
"pins": """
.pinmap{position:relative;height:140px;margin:0 0 28px;border-radius:var(--r);background:var(--panel);overflow:hidden}
.pinmap .road{position:absolute;left:6%;right:6%;top:58%;height:4px;background:color-mix(in srgb,var(--ink) 18%,transparent);border-radius:4px}
.pinmap .pin{position:absolute;top:58%;width:22px;height:22px;margin:-30px 0 0 -11px;border-radius:50% 50% 50% 0;background:var(--accent);transform:translateY(-120px) rotate(-45deg);opacity:0}
.pinmap .pin::after{content:"";position:absolute;inset:7px;border-radius:50%;background:var(--bg)}
.pinmap.on .pin{transform:translateY(0) rotate(-45deg);opacity:1;transition:transform .7s cubic-bezier(.3,1.6,.5,1),opacity .2s}
.pinmap.on .pin.b{transition-delay:.35s}
.pinmap .lab{position:absolute;top:66%;transform:translateX(-50%);font-weight:600;font-size:.9rem;opacity:0}
.pinmap.on .lab{opacity:1;transition:opacity .4s .9s}
""",
"grow": """
.stem{position:absolute;right:clamp(8px,3vw,40px);bottom:0;width:min(230px,30vw);height:auto;z-index:2;pointer-events:none}
.stem path{fill:none;stroke:var(--accent);stroke-width:2.2;stroke-linecap:round;stroke-dasharray:600;stroke-dashoffset:600}
.ready .stem path{stroke-dashoffset:0;transition:stroke-dashoffset 2.4s .4s cubic-bezier(.4,0,.2,1)}
.ready .stem path.l2{transition-delay:1s}.ready .stem path.l3{transition-delay:1.4s}.ready .stem path.l4{transition-delay:1.8s}
.hero-split .copy{position:relative}
@media(max-width:860px){.stem{width:120px;opacity:.6}}
""",
"shine": """
.anim-shine h1{background:linear-gradient(110deg,currentColor 40%,var(--accent) 50%,currentColor 60%) 120% 0/250% 100% no-repeat;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#fff}
.ready .anim-shine h1{animation:sheen 2.4s .5s cubic-bezier(.4,0,.2,1) 1 forwards}
@keyframes sheen{to{background-position:-20% 0}}
""",
"route": """
.route{width:100%;max-width:640px;height:auto;margin:0 0 28px}
.route .path{fill:none;stroke:var(--accent);stroke-width:4;stroke-linecap:round;stroke-dasharray:8 10}
.route .draw{fill:none;stroke:var(--bg);stroke-width:7;stroke-dasharray:700;stroke-dashoffset:0}
.route.on .draw{stroke-dashoffset:-700;transition:stroke-dashoffset 2.6s cubic-bezier(.4,0,.2,1)}
.route .bld{fill:var(--panel);stroke:color-mix(in srgb,var(--ink) 25%,transparent)}
.route text{font-family:var(--body);font-size:13px;fill:var(--muted)}
.route .goal{fill:var(--accent)}
""",
"progress": """
.steps{position:relative}
.steps::before{content:"";position:absolute;left:0;right:0;top:24px;height:3px;background:color-mix(in srgb,var(--ink) 12%,transparent)}
.steps::after{content:"";position:absolute;left:0;top:24px;height:3px;width:0;background:var(--accent)}
.steps.on::after{width:100%;transition:width 1.8s cubic-bezier(.4,0,.2,1)}
.steps .n{position:relative;z-index:1;background:var(--bg);width:max-content;padding-right:12px}
@media(max-width:860px){.steps::before,.steps::after{display:none}}
""",
}

ANIM_JS = """
(function(){
 if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){document.querySelectorAll('[data-on]').forEach(function(e){e.classList.add('on')});return}
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.35});
 document.querySelectorAll('[data-on]').forEach(function(e){io.observe(e)});
 document.querySelectorAll('.anim-splitflap .board tr').forEach(function(r,i){r.style.transitionDelay=(i*.09)+'s'});
 var left=document.querySelector('[data-left]');
 if(left&&window.__SITE__.hours){var S=window.__SITE__;
  function tick(){var p=new Intl.DateTimeFormat('en-US',{timeZone:S.tz,weekday:'short',hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date()),o={};p.forEach(function(x){o[x.type]=x.value});
   var m=(+o.hour%24)*60+(+o.minute),h=S.hours[o.weekday];
   if(!h){left.textContent='Closed today. Back tomorrow.';return}
   var a=h.split('-'),s=a[0].split(':'),e=a[1].split(':'),sm=+s[0]*60+ +s[1],em=+e[0]*60+ +e[1];
   if(m>=sm&&m<em){var d=em-m;left.textContent='Open for another '+Math.floor(d/60)+'h '+(d%60<10?'0':'')+(d%60)+'m today'}
   else if(m<sm){left.textContent='Opening soon today'}else{left.textContent='Closed now. Back tomorrow.'}}
  tick();setInterval(tick,30000)}
})();
"""
REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.anim-razor h1{clip-path:none!important}.anim-stamp h1 .ln,.anim-splitflap .board tr,.stampbadge,.pinmap .pin,.pinmap .lab{opacity:1!important;transform:none!important}.stampbadge{transform:rotate(-12deg)!important}.ecg path,.stem path{stroke-dashoffset:0!important}.ecg .dot{opacity:1}}"


def anim_of(s):
    return s.get("anim") or DEFAULT_ANIM.get(s["signature"]["type"], "stamp")


def headline_html(s, a):
    lines = s["headline"].split("\n")
    if a == "stamp":
        return "".join(f'<span class="ln">{E(l)}</span>' for l in lines)
    if a == "razor":
        return f'<span class="hl">{E(s["headline"])}<span class="blade" aria-hidden="true"></span></span>'
    return E(s["headline"])


def hero_extra(s, a):
    if a == "pulse":
        return ('<svg class="ecg" viewBox="0 0 420 56" aria-hidden="true"><path d="M2 30 H120 L134 30 L144 8 L156 50 L168 18 L178 30 H262 L272 30 L280 20 L288 30 H392"/>'
                '<path class="dot" d="M398 30 m-10 -4 a6 6 0 0 1 10 -3 a6 6 0 0 1 10 3 c0 6 -10 12 -10 12 c0 0 -10 -6 -10 -12z"/></svg>')
    if a == "badge":
        return ('<div class="stampbadge" aria-hidden="true"><svg viewBox="0 0 150 150"><circle class="ring" cx="75" cy="75" r="74"/><defs><path id="c" d="M75 75 m-56 0 a56 56 0 1 1 112 0 a56 56 0 1 1 -112 0"/></defs>'
                '<text><textPath href="#c">NEW ON 17TH AVE N · FIVE STARS SO FAR · </textPath></text></svg><div class="core">5.0</div></div>')
    if a == "grow":
        return ('<svg class="stem" viewBox="0 0 200 360" aria-hidden="true"><path d="M100 360 C100 280 96 200 108 120 C116 70 110 40 104 6"/>'
                '<path class="l2" d="M104 250 C70 236 46 210 40 176 C76 182 98 206 104 250"/>'
                '<path class="l3" d="M106 180 C140 168 160 140 166 108 C132 114 110 140 106 180"/>'
                '<path class="l4" d="M108 110 C84 96 72 74 72 50 C96 58 108 82 108 110"/></svg>')
    return ""


def sig_extra(s, a):
    if a == "countdown":
        return '<span class="left" data-left aria-live="polite"></span>'
    if a == "pins":
        return ('<div class="pinmap" data-on aria-hidden="true"><div class="road"></div>'
                '<div class="pin" style="left:24%"></div><div class="lab" style="left:24%">Broad Ripple</div>'
                '<div class="pin b" style="left:76%"></div><div class="lab" style="left:76%">Fletcher Place</div></div>')
    if a == "route":
        return ('<svg class="route" data-on viewBox="0 0 640 220" role="img" aria-label="Map: from N. Florida Ave, around to the lot behind the building, through the back gate">'
                '<rect class="bld" x="250" y="40" width="220" height="110" rx="6"/><text x="300" y="100">Salon Cypress</text>'
                '<text x="20" y="200">N. Florida Ave</text><text x="490" y="200">Fenced lot</text><text x="486" y="30">Back gate</text>'
                '<path class="path" d="M30 175 H560 V60 H480"/><path class="draw" d="M30 175 H560 V60 H480"/><circle class="goal" cx="476" cy="60" r="9"/></svg>')
    return ""


def offer_html(s):
    o = OFFER
    fixes = s.get("fixes") or []
    fx = "".join(f"<li>{E(f)}</li>" for f in fixes)
    fixes_block = f'<div class="fixes"><h3>What this fixes on your current site</h3><ul>{fx}</ul></div>' if fixes else ""
    unit = {"barber": "cuts", "salon": "appointments", "dental": "visits"}[s["kind"]]
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
