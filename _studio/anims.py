"""Signature animations for Storefront Studio sites (v2).

One signature animation per business ("anim" in sites.py). The same animation is used on the
concept and on the client's final site, so the owner gets exactly what they said yes to.
Every animation respects prefers-reduced-motion and ends in a clean, readable final state.
"""
import html
E = lambda s: html.escape(str(s), quote=True)

DEFAULT_ANIM = {"salute": "stamp", "clock": "countdown", "razor": "razor", "board": "splitflap", "kids": "pulse",
                "new": "badge", "locations": "pins", "botanical": "grow", "shine": "shine", "directions": "route",
                "steps": "progress"}


def anim_of(s):
    return s.get("anim") or DEFAULT_ANIM.get(s["signature"]["type"], "stamp")


def _chars(line, start):
    out, i = [], start
    for c in line:
        out.append('<span class="ch" style="--i:%d">%s</span>' % (i, "&nbsp;" if c == " " else E(c)))
        i += 1
    return "".join(out), i


def headline_html(s, a):
    lines = s["headline"].split("\n")
    if a in ("stamp", "badge"):
        parts, i = [], 0
        for l in lines:
            h, i = _chars(l, i)
            parts.append(f'<span class="ln" aria-hidden="true">{h}</span>')
        return f'<span class="sr">{E(s["headline"])}</span>' + "".join(parts)
    if a == "razor":
        return f'<span class="hl">{E(s["headline"])}<span class="blade" aria-hidden="true"><i></i></span></span>'
    return E(s["headline"])


def hero_extra(s, a):
    if a == "pulse":
        d = "M0 30 H110 L122 30 L132 6 L146 54 L158 16 L168 30 H250 L258 30 L266 22 L274 30 H420"
        return (f'<svg class="ecg" viewBox="0 0 420 60" aria-hidden="true"><path class="base" d="{d}"/><path class="trace" d="{d}"/>'
                '<g class="heart"><path d="M405 24 a6 6 0 0 1 10 -4 a6 6 0 0 1 10 4 c0 7 -10 14 -10 14 c0 0 -10 -7 -10 -14z" transform="translate(-10 4)"/></g></svg>')
    if a == "badge":
        return ('<div class="stampbadge" aria-hidden="true"><span class="burst"></span><svg viewBox="0 0 150 150"><circle class="ring" cx="75" cy="75" r="74"/>'
                '<defs><path id="c" d="M75 75 m-56 0 a56 56 0 1 1 112 0 a56 56 0 1 1 -112 0"/></defs>'
                '<text><textPath href="#c">NEW ON 17TH AVE N · FIVE STARS SO FAR · </textPath></text></svg><div class="core">5.0</div></div>')
    if a == "grow":
        return ('<svg class="stem" viewBox="0 0 200 360" aria-hidden="true"><g class="sway">'
                '<path class="st" d="M100 360 C100 280 96 200 108 120 C116 70 110 40 104 6"/>'
                '<path class="lf l1" d="M104 250 C70 236 46 210 40 176 C76 182 98 206 104 250Z"/>'
                '<path class="lf l2" d="M106 180 C140 168 160 140 166 108 C132 114 110 140 106 180Z"/>'
                '<path class="lf l3" d="M108 110 C84 96 72 74 72 50 C96 58 108 82 108 110Z"/>'
                '<circle class="bud" cx="104" cy="8" r="6"/></g></svg>')
    if a == "ripple":
        return ('<svg class="ripple" viewBox="0 0 240 240" aria-hidden="true">'
                '<circle class="rp r1" cx="120" cy="150" r="30"/><circle class="rp r2" cx="120" cy="150" r="30"/><circle class="rp r3" cx="120" cy="150" r="30"/>'
                '<path class="drop" d="M120 40 C120 40 92 78 92 98 a28 28 0 0 0 56 0 C148 78 120 40 120 40Z"/></svg>')
    if a == "shine":
        return ('<svg class="strands" viewBox="0 0 600 400" preserveAspectRatio="none" aria-hidden="true">'
                '<path d="M-20 300 C120 220 220 360 360 260 S560 160 640 220"/><path d="M-20 330 C140 250 240 380 380 290 S560 200 640 250"/>'
                '<path d="M-20 270 C110 200 210 330 350 230 S560 130 640 190"/></svg>')
    return ""


def sig_extra(s, a):
    if a == "countdown":
        return '<span class="left" data-left aria-live="off"></span>'
    if a == "pins":
        return ('<div class="pinmap" data-on aria-hidden="true"><svg viewBox="0 0 600 140" preserveAspectRatio="none"><path class="rd" d="M40 96 C180 40 420 140 560 84"/>'
                '<path class="trip" d="M144 72 C240 70 360 104 456 92"/></svg>'
                '<div class="pin" style="left:24%;top:52%"><i></i></div><div class="lab" style="left:24%">Broad Ripple</div>'
                '<div class="pin b" style="left:76%;top:66%"><i></i></div><div class="lab b" style="left:76%">Fletcher Place</div>'
                '<span class="car"></span></div>')
    if a == "route":
        p = "M30 175 H560 V60 H486"
        return ('<svg class="route" data-on viewBox="0 0 640 220" role="img" aria-label="Map: from N. Florida Ave, around to the fenced lot behind the building, through the back gate">'
                '<rect class="bld" x="250" y="40" width="220" height="110" rx="8"/><text x="292" y="100">Salon Cypress</text>'
                '<rect class="lot" x="500" y="80" width="120" height="80" rx="6"/><text x="512" y="125">Fenced lot</text>'
                '<text x="20" y="206">N. Florida Ave</text><text x="440" y="30">Back gate</text>'
                f'<path class="path" d="{p}"/><path class="draw" pathLength="100" d="{p}"/>'
                '<g class="gate"><line x1="478" y1="48" x2="478" y2="72"/></g>'
                f'<circle class="walker" r="8"><animateMotion begin="indefinite" dur="2.8s" fill="freeze" path="{p}" calcMode="spline" keyTimes="0;1" keySplines=".4 0 .2 1"/></circle>'
                '</svg>')
    return ""


ANIM_CSS = {
"stamp": """
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.anim-stamp h1{white-space:normal;perspective:600px}
.anim-stamp h1 .ln{display:block}
.anim-stamp h1 .ch{display:inline-block;transform:translateY(-.55em) rotateX(80deg) scale(1.2);opacity:0;transform-origin:50% 100%}
.ready .anim-stamp h1 .ch{transform:none;opacity:1;transition:transform .6s cubic-bezier(.2,1.5,.4,1) calc(var(--i)*26ms),opacity .25s calc(var(--i)*26ms)}
.anim-stamp h1::after{content:"";display:block;height:6px;width:0;margin-top:16px;background:linear-gradient(100deg,var(--accent) 0 40%,#fff6d6 50%,var(--accent) 60% 100%) 120% 0/250% 100%}
.ready .anim-stamp h1::after{width:min(340px,62%);background-position:-30% 0;transition:width .9s .9s cubic-bezier(.2,.7,.2,1),background-position 1.4s 1.6s ease}
@property --sweep{syntax:'<angle>';inherits:false;initial-value:0deg}
.medal{position:relative;display:inline-block;padding:.08em .18em}
.medal::before{content:"";position:absolute;inset:-.06em -.04em;border-radius:50%;border:4px solid var(--accent);-webkit-mask:conic-gradient(#000 var(--sweep),transparent 0);mask:conic-gradient(#000 var(--sweep),transparent 0);opacity:.85}
.medal.on::before{--sweep:360deg;transition:--sweep 1.6s cubic-bezier(.4,0,.2,1)}
""",
"badge": """
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.anim-badge h1{white-space:normal}
.anim-badge h1 .ln{display:block}
.anim-badge h1 .ch{display:inline-block;opacity:0;transform:translateY(.4em)}
.ready .anim-badge h1 .ch{opacity:1;transform:none;transition:opacity .35s calc(var(--i)*20ms),transform .5s cubic-bezier(.2,.8,.2,1) calc(var(--i)*20ms)}
.stampbadge{position:absolute;right:clamp(16px,4vw,56px);top:clamp(96px,14vh,150px);width:156px;height:156px;z-index:3;opacity:0;transform:scale(2.6) rotate(-30deg);filter:blur(6px)}
.ready .stampbadge{animation:slam .55s 1.1s cubic-bezier(.5,0,.75,0) forwards}
@keyframes slam{to{opacity:1;transform:scale(1) rotate(-12deg);filter:none}}
.stampbadge .burst{position:absolute;inset:0;border-radius:50%;border:3px solid var(--accent);opacity:0}
.ready .stampbadge .burst{animation:burst .8s 1.62s ease-out}
@keyframes burst{0%{opacity:.9;transform:scale(1)}100%{opacity:0;transform:scale(1.9)}}
.ready .hero .copy{animation:thud .35s 1.62s}
@keyframes thud{25%{transform:translate(2px,3px)}50%{transform:translate(-2px,-1px)}75%{transform:translate(1px,1px)}}
.stampbadge svg{width:100%;height:100%;animation:spin 32s linear 2.4s infinite}
.stampbadge text{font-family:var(--display);font-weight:var(--dw);font-size:15px;letter-spacing:2px;fill:var(--on)}
.stampbadge .core{position:absolute;inset:34px;border-radius:50%;background:var(--ink);color:var(--accent);display:grid;place-items:center;font-family:var(--display);font-weight:var(--dw);font-size:1.8rem;line-height:1}
.stampbadge circle.ring{fill:var(--accent)}
@keyframes spin{to{transform:rotate(360deg)}}
.hero-split .copy{position:relative}
@media(max-width:860px){.stampbadge{width:110px;height:110px;top:-56px;right:16px}.stampbadge .core{inset:25px;font-size:1.25rem}}
""",
"countdown": """
.anim-countdown .bignum{text-shadow:0 0 18px color-mix(in srgb,var(--accent) 70%,transparent),0 0 60px color-mix(in srgb,var(--accent) 45%,transparent)}
.anim-countdown .bignum.on{animation:neon 1.5s steps(1) 1 both,breathe 4s 1.6s ease-in-out infinite}
@keyframes neon{0%{opacity:.12}7%{opacity:1}11%{opacity:.25}17%{opacity:1}28%{opacity:.45}33%,100%{opacity:1}}
@keyframes breathe{50%{text-shadow:0 0 26px color-mix(in srgb,var(--accent) 85%,transparent),0 0 90px color-mix(in srgb,var(--accent) 55%,transparent)}}
.left{display:block;font-family:var(--display);font-weight:var(--dw);font-size:clamp(1.3rem,2.4vw,1.9rem);margin-top:10px;font-variant-numeric:tabular-nums}
.left b{color:var(--accent);font-weight:inherit}
""",
"razor": """
.anim-razor .hl{position:relative;display:inline-block;clip-path:inset(-10% 100% -10% 0)}
.ready .anim-razor .hl{clip-path:inset(-10% 0 -10% 0);transition:clip-path 1.25s .2s cubic-bezier(.75,0,.2,1)}
.anim-razor .blade{position:absolute;top:-6%;bottom:-6%;left:0;width:2px;background:var(--accent);opacity:0}
.anim-razor .blade i{position:absolute;top:-14px;left:-9px;width:20px;height:14px;background:linear-gradient(90deg,#c9c9c9,#fff 45%,#9a9a9a);clip-path:polygon(0 0,100% 0,60% 100%,40% 100%)}
.ready .anim-razor .blade{animation:blade 1.25s .2s cubic-bezier(.75,0,.2,1) both}
@keyframes blade{0%{left:0;opacity:1}92%{opacity:1}100%{left:100%;opacity:0}}
.anim-razor h1::after{content:"";display:block;height:2px;margin-top:18px;background:var(--accent);transform:scaleX(0);transform-origin:left}
.ready .anim-razor h1::after{transform:scaleX(1);transition:transform .9s 1.3s cubic-bezier(.2,.7,.2,1)}
.sig-photo{position:relative}
.sig-photo::before{content:"";position:absolute;left:0;top:-36px;height:1px;width:calc(var(--p,0)*100%);background:var(--accent)}
""",
"splitflap": """
.anim-splitflap .board{perspective:800px}
.anim-splitflap .board tr{transform:rotateX(-90deg);transform-origin:50% 0;opacity:0}
.anim-splitflap .board.on tr{transform:none;opacity:1;transition:transform .5s cubic-bezier(.3,1.5,.5,1),opacity .15s}
.anim-splitflap .board td,.anim-splitflap .board th{font-variant-numeric:tabular-nums;font-family:var(--display);letter-spacing:.02em}
.anim-splitflap .board .hours-note{font-family:var(--display);font-size:1.4rem;line-height:1.3}
.flap{display:inline-block;min-width:.62em;text-align:center}
""",
"pulse": """
.ecg{display:block;width:min(440px,82%);height:60px;margin:2px 0 20px;overflow:visible}
.ecg path{fill:none;stroke-linecap:round;stroke-linejoin:round}
.ecg .base{stroke:color-mix(in srgb,currentColor 22%,transparent);stroke-width:2}
.ecg .trace{stroke:var(--accent);stroke-width:3.2;stroke-dasharray:90 620;stroke-dashoffset:90;filter:drop-shadow(0 0 6px var(--accent));opacity:0}
.ready .ecg .trace{opacity:1;animation:trace 2.4s .4s linear infinite}
@keyframes trace{to{stroke-dashoffset:-620}}
.ecg .heart path{fill:var(--accent)}
.ecg .heart{transform-box:fill-box;transform-origin:center}
.ready .ecg .heart{animation:beat 2.4s 1.6s ease-in-out infinite}
@keyframes beat{0%,100%{transform:scale(1)}8%{transform:scale(1.45)}16%{transform:scale(1)}24%{transform:scale(1.25)}32%{transform:scale(1)}}
""",
"pins": """
.pinmap{position:relative;height:170px;margin:0 0 28px;border-radius:var(--r);background:var(--panel);overflow:hidden}
.pinmap svg{position:absolute;inset:0;width:100%;height:100%}
.pinmap .rd{fill:none;stroke:color-mix(in srgb,var(--ink) 16%,transparent);stroke-width:10;stroke-linecap:round}
.pinmap .trip{fill:none;stroke:var(--accent);stroke-width:3;stroke-dasharray:6 8;stroke-dashoffset:400;opacity:0}
.pinmap.on .trip{opacity:1;stroke-dashoffset:0;transition:stroke-dashoffset 1.6s 1s ease,opacity .2s 1s}
.pinmap .pin{position:absolute;width:26px;height:26px;margin:-34px 0 0 -13px;transform:translateY(-140px);opacity:0}
.pinmap .pin i{position:absolute;inset:0;border-radius:50% 50% 50% 0;background:var(--accent);transform:rotate(-45deg)}
.pinmap .pin i::after{content:"";position:absolute;inset:8px;border-radius:50%;background:var(--panel)}
.pinmap .pin::after{content:"";position:absolute;left:3px;right:3px;bottom:-12px;height:6px;border-radius:50%;background:rgba(0,0,0,.18);transform:scale(.3);opacity:0}
.pinmap.on .pin{transform:none;opacity:1;transition:transform .75s cubic-bezier(.3,1.7,.5,1),opacity .15s}
.pinmap.on .pin::after{transform:none;opacity:1;transition:all .5s .4s}
.pinmap.on .pin.b{transition-delay:.3s}
.pinmap .lab{position:absolute;bottom:14px;transform:translate(-50%,10px);font-weight:700;font-size:.92rem;opacity:0}
.pinmap.on .lab{opacity:1;transform:translate(-50%,0);transition:all .5s .9s}
.pinmap.on .lab.b{transition-delay:1.1s}
""",
"grow": """
.stem{position:absolute;right:clamp(4px,3vw,40px);bottom:0;width:min(240px,30vw);height:auto;z-index:2;pointer-events:none;overflow:visible}
.stem .st{fill:none;stroke:var(--accent);stroke-width:2.4;stroke-linecap:round;stroke-dasharray:420;stroke-dashoffset:420}
.ready .stem .st{stroke-dashoffset:0;transition:stroke-dashoffset 2.2s .3s cubic-bezier(.4,0,.2,1)}
.stem .lf{fill:color-mix(in srgb,var(--accent) 30%,transparent);stroke:var(--accent);stroke-width:1.6;transform-box:fill-box;transform:scale(0)}
.stem .l1{transform-origin:100% 100%}.stem .l2{transform-origin:0 100%}.stem .l3{transform-origin:100% 100%}
.ready .stem .lf{transform:scale(1);transition:transform 1s cubic-bezier(.3,1.4,.5,1)}
.ready .stem .l1{transition-delay:1.1s}.ready .stem .l2{transition-delay:1.5s}.ready .stem .l3{transition-delay:1.9s}
.stem .bud{fill:var(--accent);transform-box:fill-box;transform-origin:center;transform:scale(0)}
.ready .stem .bud{transform:scale(1);transition:transform .6s 2.4s cubic-bezier(.3,1.8,.5,1)}
.stem .sway{transform-origin:100px 360px}
.ready .stem .sway{animation:sway 7s 3s ease-in-out infinite}
@keyframes sway{50%{transform:rotate(1.8deg)}}
.hero-split .copy{position:relative}
@media(max-width:860px){.stem{width:110px;opacity:.65}}
""",
"shine": """
.anim-shine h1{background:linear-gradient(105deg,#fff 0 42%,#fff3e8 46%,var(--accent) 50%,#fff3e8 54%,#fff 58% 100%) 130% 0/260% 100% no-repeat;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.ready .anim-shine h1{animation:sheen 2.6s .6s cubic-bezier(.4,0,.2,1) forwards,sheen2 2.6s 9s cubic-bezier(.4,0,.2,1) infinite}
@keyframes sheen{to{background-position:-30% 0}}
@keyframes sheen2{0%{background-position:130% 0}40%,100%{background-position:-30% 0}}
.strands{position:absolute;inset:auto 0 0 0;height:60%;width:100%;z-index:-1;pointer-events:none;opacity:.7}
.strands path{fill:none;stroke:var(--accent);stroke-width:1.4;stroke-dasharray:900;stroke-dashoffset:900}
.ready .strands path{stroke-dashoffset:0;transition:stroke-dashoffset 3.2s cubic-bezier(.4,0,.2,1)}
.ready .strands path:nth-child(2){transition-delay:.3s}.ready .strands path:nth-child(3){transition-delay:.6s}
.ready .strands{animation:flow 9s 3.4s ease-in-out infinite}
@keyframes flow{50%{transform:translateY(-10px) scaleY(1.04)}}
""",
"ripple": """
.ripple{position:absolute;right:clamp(12px,6vw,90px);bottom:clamp(70px,14vh,150px);width:clamp(120px,16vw,210px);height:auto;pointer-events:none;overflow:visible;z-index:2}
.ripple .drop{fill:var(--accent);opacity:0;transform:translateY(-40px);transform-box:fill-box}
.ripple .rp{fill:none;stroke:var(--accent);stroke-width:2.5;opacity:0;transform-box:fill-box;transform-origin:center}
.ready .ripple .drop{animation:dropfall 3.6s .5s cubic-bezier(.5,0,.8,.6) infinite}
.ready .ripple .r1{animation:ring 3.6s 1.25s ease-out infinite}
.ready .ripple .r2{animation:ring 3.6s 1.55s ease-out infinite}
.ready .ripple .r3{animation:ring 3.6s 1.85s ease-out infinite}
@keyframes dropfall{0%{opacity:0;transform:translateY(-60px)}12%{opacity:1}22%{opacity:1;transform:translateY(40px) scaleY(1.1)}26%,100%{opacity:0;transform:translateY(52px) scale(.4)}}
@keyframes ring{0%{opacity:.9;transform:scale(.2,.08)}70%,100%{opacity:0;transform:scale(2.4,.9)}}
@media(max-width:860px){.ripple{width:96px;bottom:auto;top:84px;right:14px;opacity:.85}}
""",
"route": """
.route{width:100%;max-width:680px;height:auto;margin:0 0 28px;overflow:visible}
.route .path{fill:none;stroke:color-mix(in srgb,var(--ink) 18%,transparent);stroke-width:4;stroke-linecap:round;stroke-dasharray:2 10}
.route .draw{fill:none;stroke:var(--accent);stroke-width:4;stroke-linecap:round;stroke-dasharray:100;stroke-dashoffset:100}
.route.on .draw{stroke-dashoffset:0;transition:stroke-dashoffset 2.8s cubic-bezier(.4,0,.2,1)}
.route .bld{fill:var(--panel);stroke:color-mix(in srgb,var(--ink) 22%,transparent)}
.route .lot{fill:none;stroke:color-mix(in srgb,var(--ink) 30%,transparent);stroke-dasharray:4 4}
.route text{font-family:var(--body);font-size:13px;fill:var(--muted)}
.route .walker{fill:var(--accent);stroke:var(--bg);stroke-width:3}
.route .gate line{stroke:var(--ink);stroke-width:4;stroke-linecap:round}
.route .gate{transform-box:fill-box;transform-origin:50% 0}
.route.on .gate{transform:rotate(-70deg);transition:transform .6s 2.7s cubic-bezier(.3,1.5,.5,1)}
""",
"progress": """
.steps{position:relative}
.steps::before{content:"";position:absolute;left:0;right:0;top:24px;height:3px;background:color-mix(in srgb,var(--ink) 12%,transparent)}
.steps::after{content:"";position:absolute;left:0;top:24px;height:3px;width:calc(var(--p,0)*100%);background:var(--accent)}
.steps .n{position:relative;z-index:1;background:var(--bg);width:max-content;padding-right:14px;transition:transform .4s cubic-bezier(.3,1.8,.5,1),color .3s;color:color-mix(in srgb,var(--ink) 35%,transparent)}
.steps li.hit .n{color:var(--accent);transform:scale(1.15)}
.steps li h3::after{content:"";display:inline-block;width:12px;height:7px;margin-left:10px;border-left:2.5px solid var(--accent);border-bottom:2.5px solid var(--accent);transform:rotate(-45deg) scale(0);vertical-align:3px}
.steps li.hit h3::after{transform:rotate(-45deg) scale(1);transition:transform .35s .15s cubic-bezier(.3,1.8,.5,1)}
@media(max-width:860px){.steps::before,.steps::after{display:none}.steps .n{color:var(--accent)}}
""",
}

COMMON_CSS = """
.hero img.kb{will-change:transform}
"""

ANIM_JS = r"""
(function(){
 var RM=window.matchMedia('(prefers-reduced-motion: reduce)').matches, S=window.__SITE__;
 var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');e.target.dispatchEvent(new Event('inview'));io.unobserve(e.target)}})},{threshold:.35}):null;
 document.querySelectorAll('[data-on],.medal,.bignum,.board').forEach(function(e){if(RM||!io){e.classList.add('on');e.dispatchEvent(new Event('inview'))}else io.observe(e)});
 /* count-up ($25 medal) */
 document.querySelectorAll('[data-count]').forEach(function(el){var to=+el.dataset.count,pre=el.dataset.prefix||'';
  el.addEventListener('inview',function(){if(RM){el.textContent=pre+to;return}var t0=null;function f(t){t0=t0||t;var k=Math.min(1,(t-t0)/1300),e=1-Math.pow(1-k,3);el.textContent=pre+Math.round(to*e);if(k<1)requestAnimationFrame(f)}requestAnimationFrame(f)})});
 /* split-flap */
 var CH='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:';
 document.querySelectorAll('.anim-splitflap .board').forEach(function(b){
  b.querySelectorAll('tr').forEach(function(r,i){r.style.transitionDelay=(i*.09)+'s'});
  b.addEventListener('inview',function(){if(RM)return;b.querySelectorAll('td,th,.hours-note').forEach(function(c,i){var fin=c.textContent,n=0,max=10+i;var iv=setInterval(function(){n++;if(n>=max){c.textContent=fin;clearInterval(iv);return}c.textContent=fin.replace(/[A-Za-z0-9]/g,function(x){return Math.random()<n/max?x:CH[Math.floor(Math.random()*CH.length)]})},45)})})});
 /* scroll-linked progress (steps, razor hairline) + gentle hero parallax */
 var steps=document.querySelector('.anim-progress .steps'), sp=document.querySelector('.anim-razor .sig-photo'), hero=document.querySelector('.hero img.kb');
 function onScroll(){var vh=innerHeight;
  if(steps){var r=steps.getBoundingClientRect(),p=Math.max(0,Math.min(1,(vh*.8-r.top)/(r.height+vh*.25)));steps.style.setProperty('--p',p);steps.querySelectorAll('li').forEach(function(li,i,a){li.classList.toggle('hit',p>=i/(a.length-1)-.02||innerWidth<860)})}
  if(sp){var q=sp.getBoundingClientRect();sp.style.setProperty('--p',Math.max(0,Math.min(1,(vh-q.top)/(vh*.9))))}
  if(hero&&!RM&&scrollY<vh*1.2)hero.style.translate='0 '+(scrollY*.12)+'px'}
 addEventListener('scroll',onScroll,{passive:true});onScroll();
 /* route walker */
 document.querySelectorAll('.route').forEach(function(r){r.addEventListener('inview',function(){var m=r.querySelector('animateMotion');if(m&&m.beginElement&&!RM)m.beginElement();else{var w=r.querySelector('.walker');w&&w.setAttribute('transform','translate(486 60)')}})});
 /* live countdown to closing */
 var left=document.querySelector('[data-left]');
 if(left&&S.hours){function tick(){var p=new Intl.DateTimeFormat('en-US',{timeZone:S.tz,weekday:'short',hour:'numeric',minute:'numeric',second:'numeric',hour12:false}).formatToParts(new Date()),o={};p.forEach(function(x){o[x.type]=x.value});
   var s=((+o.hour%24)*60+(+o.minute))*60+(+o.second),h=S.hours[o.weekday];
   if(!h){left.textContent='Closed today. Back tomorrow.';return}
   var a=h.split('-'),b=a[0].split(':'),c=a[1].split(':'),ss=(+b[0]*60+ +b[1])*60,es=(+c[0]*60+ +c[1])*60;
   if(s>=ss&&s<es){var d=es-s,H=Math.floor(d/3600),M=Math.floor(d%3600/60),X=d%60;left.innerHTML='Chairs open for <b>'+H+':'+(M<10?'0':'')+M+':'+(X<10?'0':'')+X+'</b> more today'}
   else if(s<ss){left.textContent='Opening later today'}else{left.textContent='Closed now. Back tomorrow.'}}
  tick();setInterval(tick,1000)}
})();
"""

REDUCED = ("@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}"
           ".anim-razor .hl{clip-path:none!important}.anim-stamp h1 .ch,.anim-badge h1 .ch,.anim-splitflap .board tr,.stampbadge,.pinmap .pin,.pinmap .lab,.pinmap .trip,.stem .lf,.stem .bud{opacity:1!important;transform:none!important;filter:none!important}"
           ".stampbadge{transform:rotate(-12deg)!important}.ecg .trace{display:none}.ripple .drop{opacity:1!important;transform:none!important}.stem .st,.strands path,.route .draw,.pinmap .trip{stroke-dashoffset:0!important}.medal::before{--sweep:360deg}"
           ".anim-shine h1{background:none;-webkit-text-fill-color:currentColor}.anim-razor h1::after,.anim-stamp h1::after{transform:none;width:min(340px,62%)}}")
