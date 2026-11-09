#!/usr/bin/env python3
"""Storefront Studio România: propuneri „premium” cu animații (GSAP + ScrollTrigger + Lenis).

Usage: python3 _studio/ro_god.py [slug ...]   -> concepts/<slug>/index.html
Datele (doar fapte reale) vin din ro_pro.SITES; aici se adaugă doar pozele exemplu (IMG).
Fără JavaScript sau cu „reduce motion”, pagina e complet vizibilă și statică.
"""
import html, json, os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from ro_pro import SITES, img, tel, maps, num, nota, DAYS, ZI, EMAIL, CF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: html.escape(str(s), quote=True)

# slug -> (hero 16:9 2k, [galerie]) ; completat după generare
M = "https://aa-barber-sibiu.higgsfield.app/m/{}.jpg"
IMG = {
  "kron-barber-shop-brasov": ("kron-hero", ["kron-g1", "kron-g2"], None),
  "bandit-barbers-cluj": ("bandit-hero", ["bandit-g1", "bandit-g2"], None),
  "mk-studio-barbershop-brasov": ("mk-hero", ["mk-g1", "mk-g2"], None),
  "aa-barber-sibiu": ("aa-hero", ["aa-p1", "aa-int"], "aa-p2"),
  "piaf-cafe-targu-mures": ("piaf-hero", ["piaf-p1"], "piaf-p2"),
  "scarlet-cafe-targu-mures": ("scarlet-hero", ["scarlet-p1"], "scarlet-p2"),
  "mr-pop-targu-mures": ("mrpop-hero", ["mrpop-p1"], "mrpop-p2"),
  "galleria-art-coffee-brasov": ("galleria-hero", ["galleria-p1"], "galleria-p2"),
  "voynich-cafe-pub-sighisoara": ("voynich-hero", ["voynich-p1"], "voynich-p2"),
  "vintage-lounge-sighisoara": ("vintage-hero", ["vintage-p1"], "vintage-p2"),
}


def words(text):
    """Împarte în cuvinte pentru animații, păstrând rândurile (\n)."""
    out = []
    for i, line in enumerate(text.split("\n")):
        if i:
            out.append("<br>")
        out.append(" ".join(f'<span class="m"><span class="wd">{E(w)}</span></span>' for w in line.split(" ") if w))
    return "".join(out)


def fill_words(text):
    return " ".join(f'<span class="fw">{E(w)}</span>' for w in text.split(" "))


def open_days(s):
    h = s.get("hours") or {}
    return sum(1 for d in DAYS if h.get(d))


CSS = r"""
*,*::before,*::after{box-sizing:border-box}html{-webkit-text-size-adjust:100%}html.lenis,html.lenis body{height:auto}.lenis.lenis-smooth{scroll-behavior:auto!important}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body),system-ui,sans-serif;font-size:1.0625rem;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%}a{color:inherit}:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.w{width:min(1240px,100% - 40px);margin-inline:auto}.mu{color:var(--muted)}
.d{font-family:var(--display),var(--body),sans-serif;font-stretch:var(--st);font-weight:800;letter-spacing:-.035em;line-height:.92}
.m{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.08em;margin-bottom:-.08em}.wd{display:inline-block}
/* loader */
.ld{position:fixed;inset:0;z-index:100;background:var(--ink);color:var(--bg);display:none;flex-direction:column;justify-content:flex-end;padding:clamp(24px,5vw,64px)}
.js-go .ld{display:flex}
.ld .nm{font-size:clamp(3rem,11vw,10rem)}.ld .row{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;margin-top:18px;font-weight:600}
.ld .cnt{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:800;font-size:clamp(2rem,5vw,4rem);color:var(--accent);line-height:1}
.ld .bar{height:2px;background:color-mix(in srgb,var(--bg) 20%,transparent);margin-top:22px;overflow:hidden}.ld .bar i{display:block;height:100%;width:0;background:var(--accent)}
/* top */
.pb{position:relative;z-index:30;background:var(--accent);color:var(--on);font-size:.82rem;text-align:center;padding:8px 14px;font-weight:600}.pb a{color:inherit}
.nav{position:fixed;top:34px;left:0;right:0;z-index:40;transition:top .4s,background .4s,backdrop-filter .4s;color:#fff}
.nav.solid{top:0;background:color-mix(in srgb,var(--bg) 78%,transparent);backdrop-filter:blur(14px);color:var(--ink);box-shadow:0 1px 0 color-mix(in srgb,var(--ink) 10%,transparent)}
.nav .w{display:flex;justify-content:space-between;align-items:center;height:76px}
.brand{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:800;font-size:1.35rem;text-decoration:none;letter-spacing:-.02em}
.nav nav{display:flex;gap:28px;align-items:center;font-size:.95rem;font-weight:500}.nav nav a.l{text-decoration:none;position:relative}
.nav nav a.l::after{content:"";position:absolute;left:0;right:100%;bottom:-4px;height:2px;background:var(--accent);transition:right .35s}.nav nav a.l:hover::after{right:0}
.cta{display:inline-flex;align-items:center;gap:10px;min-height:46px;padding:0 22px;border-radius:999px;background:var(--accent);color:var(--on);text-decoration:none;font-weight:700}
/* hero */
.hero{position:relative;height:100dvh;min-height:620px;color:#fff;overflow:hidden;background:#000}
.hero .bg{position:absolute;inset:0;will-change:clip-path}.hero .bg img{width:100%;height:100%;object-fit:cover;will-change:transform}
.hero .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,.05) 38%,rgba(0,0,0,.82) 100%)}
.hero .copy{position:absolute;left:0;right:0;bottom:0;padding-bottom:clamp(40px,7vh,80px)}
h1{font-size:clamp(3.2rem,9.6vw,9.6rem);margin:0 0 26px}
.lede{font-size:clamp(1.1rem,1.6vw,1.35rem);max-width:42ch;margin:0 0 30px;opacity:.95}
.btns{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.b1{position:relative;display:inline-flex;align-items:center;gap:12px;min-height:60px;padding:0 30px;border-radius:999px;background:var(--accent);color:var(--on);font-weight:700;text-decoration:none;overflow:hidden;isolation:isolate}
.b1::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,#fff 22%,transparent);transform:translateY(101%);transition:transform .45s cubic-bezier(.7,0,.2,1);z-index:-1}.b1:hover::before{transform:none}
.b1 i{font-style:normal;transition:transform .35s}.b1:hover i{transform:translateX(5px)}
.b2{display:inline-flex;align-items:center;min-height:60px;padding:0 26px;border-radius:999px;color:inherit;text-decoration:none;font-weight:600;box-shadow:inset 0 0 0 1.5px currentColor;transition:background .3s,color .3s}
.b2:hover{background:#fff;color:#111;box-shadow:none}
.proof{display:flex;flex-wrap:wrap;gap:10px 26px;align-items:center;margin-top:28px;font-size:.98rem}
.stars{color:var(--accent);letter-spacing:2px}.open{display:inline-flex;align-items:center;gap:8px;font-weight:600}
.open i{width:9px;height:9px;border-radius:50%;background:#999}.open.on i{background:#3DDC84;box-shadow:0 0 0 0 rgba(61,220,132,.6);animation:pulse 2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 10px rgba(61,220,132,0)}100%{box-shadow:0 0 0 0 rgba(61,220,132,0)}}
.pn{position:absolute;right:14px;bottom:14px;font-size:.72rem;background:rgba(0,0,0,.55);color:#fff;padding:4px 10px;border-radius:999px;z-index:2;backdrop-filter:blur(6px)}
.scue{position:absolute;right:clamp(20px,4vw,48px);bottom:clamp(40px,7vh,80px);width:58px;height:58px;border-radius:50%;border:1.5px solid rgba(255,255,255,.6);display:grid;place-items:center}
.scue i{width:2px;height:16px;background:#fff;animation:sc 1.6s infinite}@keyframes sc{0%{transform:translateY(-8px);opacity:0}50%{opacity:1}100%{transform:translateY(8px);opacity:0}}
/* marquee */
.mq{overflow:hidden;padding:26px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 12%,transparent)}
.mq .tr{display:flex;gap:56px;width:max-content;animation:mq 60s linear infinite;will-change:transform}.mq .tr.rev{animation-direction:reverse;margin-top:14px;animation-duration:75s}
.mq span{white-space:nowrap;font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:700;font-size:clamp(1.3rem,2.4vw,2rem);letter-spacing:-.02em}
.mq .tr.rev span{color:transparent;-webkit-text-stroke:1px var(--muted)}
.mq span::before{content:"✦";color:var(--accent);margin-right:56px;-webkit-text-stroke:0}
@keyframes mq{to{transform:translateX(-50%)}}
section{padding:clamp(88px,12vw,160px) 0;position:relative}
h2{font-size:clamp(2.4rem,5.6vw,5rem);margin:0 0 22px}
.eb{display:inline-flex;gap:10px;align-items:center;font-weight:700;font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:22px}.eb::before{content:"";width:28px;height:2px;background:currentColor}
/* statement */
.st p{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:700;font-size:clamp(1.9rem,4.4vw,4rem);line-height:1.08;letter-spacing:-.03em;margin:0;max-width:22ch}
.fw{transition:opacity .2s}.go .fw{opacity:.16}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:clamp(56px,8vw,100px);border-top:1px solid color-mix(in srgb,var(--ink) 14%,transparent);padding-top:36px}
.stats .n{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:800;font-size:clamp(3.2rem,7vw,6.4rem);line-height:1;letter-spacing:-.04em;color:var(--accent)}
.stats p{margin:8px 0 0;color:var(--muted);font-weight:500}
/* services */
.sv{background:var(--panel)}
.sv .hd{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:24px;margin-bottom:40px}
.ls{list-style:none;margin:0;padding:0;border-top:1px solid color-mix(in srgb,var(--ink) 16%,transparent)}
.ls li{position:relative;display:grid;grid-template-columns:70px 1fr auto;gap:20px;align-items:center;padding:28px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 16%,transparent);transition:padding .4s}
.ls li .ix{font-weight:700;color:var(--muted);font-size:.9rem}
.ls h3{margin:0;font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:700;font-size:clamp(1.4rem,2.6vw,2.2rem);letter-spacing:-.02em;line-height:1.1}
.ls p{margin:4px 0 0;color:var(--muted)}.ls b{font-family:var(--display),sans-serif;font-stretch:var(--st);font-size:clamp(1.3rem,2.2vw,1.9rem);white-space:nowrap}
.ls li::after{content:"";position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--accent);transition:width .6s cubic-bezier(.7,0,.2,1)}
@media(pointer:fine){.ls li:hover{padding-left:16px}.ls li:hover::after{width:100%}}
.hov{position:fixed;left:0;top:0;width:280px;height:340px;border-radius:18px;overflow:hidden;pointer-events:none;z-index:50;opacity:0;transform:translate(-50%,-50%) scale(.6);display:none}
.hov img{width:100%;height:100%;object-fit:cover}@media(pointer:fine){.hov{display:block}}
.note{font-size:.9rem;color:var(--muted);margin-top:22px}
/* horizontal gallery */
.hz{padding:0;overflow:hidden;background:var(--ink);color:var(--bg)}
.hz .in{display:flex;align-items:center;gap:clamp(18px,3vw,40px);padding:clamp(88px,12vw,140px) clamp(20px,4vw,60px);width:max-content}
.hz .intro{width:min(420px,80vw);flex:none}.hz .intro h2{color:var(--bg)}.hz .intro p{color:color-mix(in srgb,var(--bg) 70%,transparent)}
.hz figure{position:relative;flex:none;margin:0;width:clamp(260px,34vw,520px);aspect-ratio:4/5;border-radius:24px;overflow:hidden}
.hz figure:nth-child(odd){margin-top:80px}.hz figure img{width:100%;height:120%;object-fit:cover;will-change:transform}
.hz figcaption{position:absolute;left:18px;bottom:16px;font-weight:700;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.5)}
/* reviews stack */
.rs .card{position:sticky;top:14vh;background:var(--bg);border:1px solid color-mix(in srgb,var(--ink) 12%,transparent);border-radius:28px;padding:clamp(28px,5vw,64px);margin-bottom:24px;box-shadow:0 30px 60px -30px rgba(0,0,0,.35);transform-origin:center top}
.rs .card:nth-child(2){top:calc(14vh + 22px)}.rs .card:nth-child(3){top:calc(14vh + 44px)}
.rs .card.a{background:var(--accent);color:var(--on);border:0}.rs .card.k{background:var(--ink);color:var(--bg);border:0}
.rs blockquote{margin:0}.rs blockquote p{font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:700;font-size:clamp(1.6rem,3.6vw,3.2rem);line-height:1.12;letter-spacing:-.025em;margin:0 0 26px}
.rs cite{font-style:normal;font-weight:600;opacity:.8}.rs .st5{letter-spacing:3px;margin-bottom:18px;display:block}
.lab{font-size:.88rem;color:var(--muted);margin-top:18px}
/* signature */
.sg{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(32px,6vw,96px);align-items:center}
.sg figure{position:relative;margin:0;border-radius:28px;overflow:hidden;aspect-ratio:4/5}.sg figure img{width:100%;height:118%;object-fit:cover;will-change:transform}
/* visit */
.vs{background:var(--panel)}.vgrid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,6vw,96px)}
address{font-style:normal;font-size:1.3rem;line-height:1.5;margin-bottom:22px}
.ph{display:inline-block;font-family:var(--display),sans-serif;font-stretch:var(--st);font-weight:800;font-size:clamp(2.4rem,5.4vw,4.6rem);text-decoration:none;letter-spacing:-.035em;line-height:1;margin-bottom:28px;background:linear-gradient(var(--accent),var(--accent)) no-repeat 0 100%/0 4px;transition:background-size .5s}
.ph:hover{background-size:100% 4px}
.hours .hr{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 12%,transparent);font-size:1.05rem}
.hours .hr.today{color:var(--accent);font-weight:700}.hours .hr.today b::after{content:"  ·  azi"}
/* offer */
.of{background:var(--ink);color:var(--bg);overflow:hidden}.of .mu{color:color-mix(in srgb,var(--bg) 68%,transparent)}
.of h2{max-width:16ch}.of .big{color:var(--accent)}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:48px 0}
.cmp > div{border-radius:26px;padding:32px;background:color-mix(in srgb,var(--bg) 6%,transparent)}
.cmp > div.y{background:var(--accent);color:var(--on)}.cmp h3{margin:0 0 14px;font-size:1.1rem;letter-spacing:.08em;text-transform:uppercase}
.cmp ul{margin:0;padding:0;list-style:none}.cmp li{padding:10px 0;border-bottom:1px solid color-mix(in srgb,currentColor 18%,transparent);font-weight:500}
.cmp > div:first-child li::before{content:"✕  ";opacity:.6}.cmp > div.y li::before{content:"✓  ";font-weight:800}
.pr{display:grid;grid-template-columns:1fr 1fr;gap:20px;perspective:1200px}
.pk{border:1px solid color-mix(in srgb,var(--bg) 18%,transparent);border-radius:26px;padding:34px;transform-style:preserve-3d;transition:transform .2s;background:color-mix(in srgb,var(--bg) 3%,transparent)}
.pk.hl{border:2px solid var(--accent);background:color-mix(in srgb,var(--accent) 12%,transparent)}
.pk .d{font-size:clamp(3rem,6vw,4.8rem);margin:10px 0}.pk .tag{display:inline-block;font-size:.78rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;background:var(--accent);color:var(--on);padding:4px 10px;border-radius:999px;margin-left:8px}
.gu{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:40px 0}
.gu div{border-top:2px solid var(--accent);padding-top:18px}.gu b{display:block;font-size:1.15rem;margin-bottom:6px}
.of .b2{color:var(--bg)}.of .b2:hover{color:#111}
/* footer */
footer{padding:60px 0 120px;overflow:hidden}
.giant{font-size:clamp(4rem,17vw,17rem);white-space:nowrap;color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--ink) 35%,transparent);margin:0 0 30px}
footer .row{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;font-size:.9rem;color:var(--muted)}
/* mobile bar */
.mb{position:fixed;left:12px;right:12px;bottom:12px;z-index:45;display:none;grid-template-columns:1fr 1fr 1.3fr;gap:8px;padding:8px;border-radius:999px;background:color-mix(in srgb,#0b0b0b 90%,transparent);backdrop-filter:blur(12px);box-shadow:0 12px 34px rgba(0,0,0,.35)}
.mb a{display:flex;align-items:center;justify-content:center;min-height:50px;border-radius:999px;color:#fff;text-decoration:none;font-weight:700;font-size:.95rem}.mb a.m1{background:var(--accent);color:var(--on)}
/* cursor */
.cur{position:fixed;left:0;top:0;width:44px;height:44px;margin:-22px 0 0 -22px;border:1.5px solid var(--accent);border-radius:50%;pointer-events:none;z-index:99;display:none;mix-blend-mode:difference;transition:width .3s,height .3s,margin .3s,background .3s}
.cur.big{width:84px;height:84px;margin:-42px 0 0 -42px;background:color-mix(in srgb,var(--accent) 30%,transparent)}
@media(pointer:fine){.js-on .cur{display:block}}
@media(max-width:860px){.nav nav a.l{display:none}.stats{grid-template-columns:1fr 1fr}.ls li{grid-template-columns:44px 1fr;}.ls b{grid-column:2}.sg,.vgrid,.cmp,.pr,.gu{grid-template-columns:1fr}
 .mb{display:grid}.hz .in{overflow-x:auto;width:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}.hz figure{scroll-snap-align:center;width:78vw}.hz figure:nth-child(odd){margin-top:0}.scue{display:none}.nav{top:34px}}
@media(prefers-reduced-motion:reduce){.mq .tr{animation:none}.go .fw{opacity:1}.open.on i{animation:none}.scue i{animation:none}}
"""

HEAD_JS = "if(!matchMedia('(prefers-reduced-motion: reduce)').matches){document.documentElement.classList.add('js-go');setTimeout(function(){document.documentElement.classList.remove('js-go')},4500)}"

JS = r"""
(function(){
var S=window.__S__,D=document,RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches,MOB=innerWidth<=860;
/* program live */
var p=new Intl.DateTimeFormat('en-US',{timeZone:'Europe/Bucharest',weekday:'short',hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date()),o={};p.forEach(function(x){o[x.type]=x.value});
var dd=o.weekday,mm=(+o.hour%24)*60+(+o.minute);D.querySelectorAll('.hr[data-day="'+dd+'"]').forEach(function(r){r.classList.add('today')});
var bd=D.querySelectorAll('[data-open]');if(!S.h){bd.forEach(function(x){x.hidden=true})}else{var h=S.h[dd],t='Închis azi',on=false;if(h){var a=h.split('-'),s=a[0].split(':'),e=a[1].split(':'),sm=+s[0]*60+ +s[1],em=+e[0]*60+ +e[1];if(em<=sm)em+=1440;if(mm>=sm&&mm<em){on=true;t='Deschis acum · până la '+a[1]}else if(mm<sm){t='Deschide azi la '+a[0]}else{t='Închis acum'}}bd.forEach(function(x){x.querySelector('span').textContent=t;x.classList.toggle('on',on)})}
var nav=D.querySelector('.nav');function navS(){nav.classList.toggle('solid',scrollY>innerHeight*.75)}addEventListener('scroll',navS,{passive:true});navS();
var ld=D.querySelector('.ld');
if(RM||!window.gsap||!window.ScrollTrigger){D.documentElement.classList.remove('js-go');return}
D.documentElement.classList.add('js-on');
var g=gsap;g.registerPlugin(ScrollTrigger);
var lenis=null;if(window.Lenis&&!MOB){lenis=new Lenis({lerp:.09,wheelMultiplier:1});lenis.on('scroll',ScrollTrigger.update);g.ticker.add(function(t){lenis.raf(t*1000)});g.ticker.lagSmoothing(0);
 D.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(ev){var id=a.getAttribute('href');if(id.length>1&&D.querySelector(id)){ev.preventDefault();lenis.scrollTo(id,{offset:-60})}})})}
/* intro */
var tl=g.timeline({defaults:{ease:'power4.out'}});
if(D.documentElement.classList.contains('js-go')&&ld){
 if(lenis)lenis.stop();
 var c={v:0},cn=ld.querySelector('.cnt');
 tl.from('.ld .wd',{yPercent:110,stagger:.05,duration:.8})
   .to(c,{v:S.r,duration:1,ease:'power2.out',onUpdate:function(){cn.textContent=c.v.toFixed(1).replace('.',',')+' ★'}},'-=.5')
   .to('.ld .bar i',{width:'100%',duration:1,ease:'power2.inOut'},'<')
   .to(ld,{yPercent:-100,duration:1,ease:'expo.inOut',onComplete:function(){D.documentElement.classList.remove('js-go');g.set(ld,{clearProps:'all'});if(lenis)lenis.start()}},'+=.15');
}
tl.from('.hero .bg img',{scale:1.35,duration:2.2,ease:'expo.out'},ld?'-=.75':0)
  .from('.hero h1 .wd',{yPercent:118,rotate:4,stagger:.07,duration:1.15},'-=1.9')
  .from('.hero .fd',{y:34,opacity:0,stagger:.1,duration:.9},'-=.9')
  .from('.nav',{y:-30,opacity:0,duration:.8},'-=.9');
/* hero scroll: imaginea devine card, textul urcă */
g.to('.hero .bg',{clipPath:'inset(7% 4% 0% 4% round 32px)',ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
g.to('.hero .bg img',{scale:1.15,yPercent:8,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
g.to('.hero .copy',{yPercent:-35,opacity:0,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'80% top',scrub:true}});
/* marquee viteză + skew la scroll */
var sk=g.quickTo('.mq .tr','skewX',{duration:.4,ease:'power3'});ScrollTrigger.create({onUpdate:function(st){var v=g.utils.clamp(-12,12,st.getVelocity()/-260);sk(v)}});
/* titluri pe cuvinte */
D.querySelectorAll('[data-sp]').forEach(function(el){g.from(el.querySelectorAll('.wd'),{yPercent:115,stagger:.06,duration:1.1,ease:'power4.out',scrollTrigger:{trigger:el,start:'top 85%'}})});
D.querySelectorAll('[data-up]').forEach(function(el){g.from(el,{y:70,opacity:0,duration:1.1,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 88%'}})});
/* text care se umple la scroll */
var st=D.querySelector('.st');if(st){st.classList.add('go');g.to('.st .fw',{opacity:1,stagger:.08,ease:'none',scrollTrigger:{trigger:'.st p',start:'top 78%',end:'bottom 42%',scrub:true}})}
/* numărătoare */
D.querySelectorAll('[data-count]').forEach(function(el){var to=+el.dataset.count,dec=+(el.dataset.dec||0),o2={v:0};ScrollTrigger.create({trigger:el,start:'top 88%',once:true,onEnter:function(){g.to(o2,{v:to,duration:2,ease:'power3.out',onUpdate:function(){el.textContent=dec?o2.v.toFixed(dec).replace('.',','):Math.round(o2.v).toLocaleString('ro-RO')}})}})});
/* servicii: imagine care urmărește cursorul */
var hov=D.querySelector('.hov');if(hov&&FINE){var hi=hov.querySelector('img'),qx=g.quickTo(hov,'x',{duration:.5,ease:'power3'}),qy=g.quickTo(hov,'y',{duration:.5,ease:'power3'});
 D.querySelectorAll('.ls li').forEach(function(li){li.addEventListener('mouseenter',function(){hi.src=li.dataset.img;g.to(hov,{opacity:1,scale:1,duration:.4})});li.addEventListener('mouseleave',function(){g.to(hov,{opacity:0,scale:.6,duration:.4})})});
 addEventListener('mousemove',function(e){qx(e.clientX);qy(e.clientY)})}
g.from('.ls li',{y:40,opacity:0,stagger:.08,duration:.9,ease:'power3.out',scrollTrigger:{trigger:'.ls',start:'top 85%'}});
/* galerie orizontală fixată */
var hz=D.querySelector('.hz .in');if(hz&&!MOB){var dist=function(){return hz.scrollWidth-innerWidth};
 var tw=g.to(hz,{x:function(){return -dist()},ease:'none',scrollTrigger:{trigger:'.hz',start:'top top',end:function(){return '+='+dist()},pin:true,scrub:1,invalidateOnRefresh:true}});
 D.querySelectorAll('.hz figure img').forEach(function(im){g.fromTo(im,{xPercent:-8},{xPercent:8,ease:'none',scrollTrigger:{trigger:im.parentNode,containerAnimation:tw,start:'left right',end:'right left',scrub:true}})})}
/* recenzii suprapuse */
var cards=D.querySelectorAll('.rs .card');cards.forEach(function(cd,i){if(i<cards.length-1){g.to(cd,{scale:.9-.02*(cards.length-i),opacity:.55,ease:'none',scrollTrigger:{trigger:cards[i+1],start:'top bottom',end:'top 20%',scrub:true}})}});
/* paralaxă */
D.querySelectorAll('[data-par] img').forEach(function(im){g.fromTo(im,{yPercent:-10},{yPercent:0,ease:'none',scrollTrigger:{trigger:im.parentNode,start:'top bottom',end:'bottom top',scrub:true}})});
/* footer: numele mare alunecă */
g.fromTo('.giant',{xPercent:10},{xPercent:-25,ease:'none',scrollTrigger:{trigger:'footer',start:'top bottom',end:'bottom bottom',scrub:true}});
if(FINE){
 /* butoane magnetice */
 D.querySelectorAll('.mag').forEach(function(b){var x=g.quickTo(b,'x',{duration:.6,ease:'elastic.out(1,.4)'}),y=g.quickTo(b,'y',{duration:.6,ease:'elastic.out(1,.4)'});
  b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect();x((e.clientX-r.left-r.width/2)*.35);y((e.clientY-r.top-r.height/2)*.35)});b.addEventListener('mouseleave',function(){x(0);y(0)})});
 /* carduri de preț 3D */
 D.querySelectorAll('.pk').forEach(function(k){k.addEventListener('mousemove',function(e){var r=k.getBoundingClientRect(),px=(e.clientX-r.left)/r.width-.5,py=(e.clientY-r.top)/r.height-.5;k.style.transform='rotateY('+(px*10)+'deg) rotateX('+(-py*10)+'deg)'});k.addEventListener('mouseleave',function(){k.style.transform=''})});
 /* cursor */
 var cu=D.querySelector('.cur'),cx=g.quickTo(cu,'x',{duration:.35,ease:'power3'}),cy=g.quickTo(cu,'y',{duration:.35,ease:'power3'});
 addEventListener('mousemove',function(e){cx(e.clientX);cy(e.clientY)});D.querySelectorAll('a,button,.ls li').forEach(function(a){a.addEventListener('mouseenter',function(){cu.classList.add('big')});a.addEventListener('mouseleave',function(){cu.classList.remove('big')})});
}
addEventListener('load',function(){ScrollTrigger.refresh()});
})();
"""


def page(s):
    t = s["theme"]
    h_, g_, p2_ = IMG[s["slug"]]
    hero, gal = M.format(h_), [M.format(x) for x in g_]
    p2 = M.format(p2_) if p2_ else img(s["photo2"], 1400)
    book = s["book"] or f"tel:{tel(s['phone'])}"
    tgt = ' target="_blank" rel="noopener"' if s["book"] else ""
    short = "Programare" if s["book"] else ("Rezervă" if "Rezerv" in s["cta"] else "Sună")
    fonts = f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={t["fonts"]}&display=swap">'
    if t.get("fontshare"):
        fonts += f'<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]={t["fontshare"]}&display=swap">'
    open_b = '<span class="open" data-open><i></i><span>Program</span></span>'
    pics = [p2] + gal + [hero]
    while len(pics) < 4:
        pics.append(img(s["photo"], 1400))
    q = s["quotes"]
    mq1 = "".join(f"<span>„{E(x)}”</span>" for x, _ in q)
    mq2 = "".join(f"<span>{E(n)}</span>" for n, _, _ in s["services"]) + f"<span>{E(s['city'])}</span><span>{nota(s['rating'])} pe {s['src']}</span>"
    svc = "".join(f'<li data-img="{pics[i % len(pics)]}"><span class="ix">0{i + 1}</span><div><h3>{E(n)}</h3>{f"<p>{E(d)}</p>" if d else ""}</div>{f"<b>{E(p)}</b>" if p else ""}</li>' for i, (n, d, p) in enumerate(s["services"]))
    has_prices = any(p for _, _, p in s["services"])
    note = ("Prețuri din pagina oficială de programare." if has_prices else "Pe site-ul final aici intră meniul vostru complet, cu prețuri.")
    labels = [x[0] for x in s["services"]] + [s["city"]] * 4
    gal_html = "".join(f'<figure><img src="{u}" alt="" loading="lazy"><figcaption>{E(labels[i])}</figcaption><span class="pn">Poză exemplu</span></figure>' for i, u in enumerate(pics[:4]))
    cards = "".join(f'<div class="card {"" if i == 0 else "a" if i == 1 else "k"}"><span class="st5">★★★★★</span><blockquote><p>„{E(x)}”</p><cite>{E(a)}</cite></blockquote></div>' for i, (x, a) in enumerate(q))
    statement = f"{num(s['reviews'])} de oameni au scris despre {s['name']}. {s['sig'][1]}"
    days = open_days(s)
    stat3 = (f'<div><div class="n" data-count="{days}">{days}</div><p>zile pe săptămână deschis</p></div>' if days else
             '<div><div class="n">1</div><p>click până la masa voastră</p></div>')
    hrs = ('<p class="mu">Programul de azi: sunați-ne. Pe site-ul final apare programul exact.</p>' if not s.get("hours") else
           '<div class="hours">' + "".join(f'<div class="hr" data-day="{d}"><span>{ZI[d]}</span><b>{"Închis" if not s["hours"].get(d) else s["hours"][d].replace("-", " - ")}</b></div>' for d in DAYS) + "</div>")
    now_line = ("nu găsește niciun site al vostru." if s["now"] == "niciun site" else f"găsește doar {E(s['now'])}.")
    what = "prețurile, programul și butonul de programare" if s["kind"] == "barber" else "meniul, programul și butonul de sunat"
    subj = urllib.parse.quote(f"Da, vreau site-ul pentru {s['name']}")
    data = json.dumps({"h": s.get("hours"), "r": s["rating"]})
    letter = E(s["name"][0])
    fav = f"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='{urllib.parse.quote(t['accent'])}'/%3E%3Ctext x='50%25' y='56%25' font-family='Arial' font-weight='900' font-size='38' fill='{urllib.parse.quote(t['on'])}' text-anchor='middle' dominant-baseline='middle'%3E{urllib.parse.quote(s['name'][0])}%3C/text%3E%3C/svg%3E"
    return f"""<!doctype html>
<html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(s['name'])} · {E(s['city'])}</title><meta name="robots" content="noindex, nofollow">
<meta name="description" content="{E(s['lede'])}"><meta name="theme-color" content="{t['ink']}"><link rel="icon" href="{fav}">
<meta property="og:title" content="{E(s['name'])} · {E(s['city'])}"><meta property="og:description" content="{E(s['lede'])}"><meta property="og:image" content="{hero}">
<script>{HEAD_JS}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{fonts}
<link rel="preload" as="image" href="{hero}">
<style>:root{{--bg:{t['bg']};--ink:{t['ink']};--muted:{t['muted']};--accent:{t['accent']};--panel:{t['panel']};--on:{t['on']};--display:'{t['display']}';--body:'{t['body']}';--st:{t['stretch']}}}{CSS}</style>
</head><body>
<div class="ld" aria-hidden="true"><div class="d nm">{words(s['name'])}</div><div class="row"><span>{E(s['city'])} · propunere de site</span><span class="cnt">0,0 ★</span></div><div class="bar"><i></i></div></div>
<div class="cur" aria-hidden="true"></div><div class="hov" aria-hidden="true"><img alt=""></div>
<div class="pb">Propunere făcută special pentru {E(s['name'])} · <a href="#oferta">Vezi oferta</a></div>
<header class="nav"><div class="w"><a class="brand" href="#">{E(s['name'])}</a><nav><a class="l" href="#servicii">{"Servicii" if s["kind"] == "barber" else "Meniu"}</a><a class="l" href="#recenzii">Recenzii</a><a class="l" href="#vizita">Vizită</a><a class="cta mag" href="{E(book)}"{tgt}>{short}</a></nav></div></header>
<section class="hero" style="padding:0"><div class="bg"><img src="{hero}" alt="" fetchpriority="high"><span class="pn">Poză exemplu · aici intră pozele voastre</span></div>
<div class="copy"><div class="w"><h1 class="d">{words(s['headline'])}</h1><p class="lede fd">{E(s['lede'])}</p>
<div class="btns fd"><a class="b1 mag" href="{E(book)}"{tgt}>{E(s['cta'])} <i>→</i></a><a class="b2 mag" href="tel:{tel(s['phone'])}">Sună: {E(s['phone'])}</a></div>
<div class="proof fd"><span><span class="stars" aria-hidden="true">★★★★★</span> {nota(s['rating'])} din {num(s['reviews'])} de recenzii pe {s['src']}</span>{f"<span>{E(s['rating2'])}</span>" if s.get("rating2") else ""}{open_b}</div></div></div>
<div class="scue" aria-hidden="true"><i></i></div></section>
<div class="mq" aria-hidden="true"><div class="tr">{mq1 * 4}</div><div class="tr rev">{mq2 * 4}</div></div>
<section class="st"><div class="w"><span class="eb">Despre noi</span><p>{fill_words(statement)}</p>
<div class="stats"><div><div class="n" data-count="{s['rating']}" data-dec="1">{nota(s['rating'])}</div><p>nota pe {s['src']}</p></div><div><div class="n" data-count="{s['reviews']}">{num(s['reviews'])}</div><p>recenzii de la clienți</p></div>{stat3}</div></div></section>
<section id="servicii" class="sv"><div class="w"><div class="hd"><div><span class="eb">{"Servicii" if s["kind"] == "barber" else "Meniu"}</span><h2 class="d" data-sp>{words("Servicii și prețuri" if s["kind"] == "barber" else "Ce găsești la noi")}</h2></div><a class="b1 mag" href="{E(book)}"{tgt}>{E(s['cta'])} <i>→</i></a></div>
<ul class="ls">{svc}</ul><p class="note">{E(note)}</p></div></section>
<section class="hz"><div class="in"><div class="intro"><span class="eb">Atmosfera</span><h2 class="d">{words("Intră și simte locul.")}</h2><p>Aici intră pozele voastre reale. Pentru propunere am pus poze exemplu.</p></div>{gal_html}</div></section>
<section id="recenzii" class="rs"><div class="w"><span class="eb">Recenzii reale</span><h2 class="d" data-sp>{words("Ce spun clienții.")}</h2><div style="height:30px"></div>{cards}<p class="lab">Copiate exact cum le-au scris clienții, pe {s['src'] if all(s['src'] in a for _, a in q) else "Google, MERO sau Fresha"}.</p></div></section>
<section><div class="w sg"><figure data-par><img src="{pics[1]}" alt="" loading="lazy"><span class="pn">Poză exemplu</span></figure><div data-up><span class="eb">De ce noi</span><h2 class="d">{E(s['sig'][0])}</h2><p class="mu" style="font-size:1.2rem;max-width:44ch">{E(s['sig'][1])}</p><a class="b1 mag" href="{E(book)}"{tgt}>{E(s['cta'])} <i>→</i></a></div></div></section>
<section id="vizita" class="vs"><div class="w vgrid"><div data-up><span class="eb">Vizită</span><h2 class="d">Vino pe la noi.</h2><address>{E(s['name'])}<br>{E(s['address'])}<br>{E(s['zip'])}</address>
<a class="ph" href="tel:{tel(s['phone'])}">{E(s['phone'])}</a><div class="btns"><a class="b1 mag" href="{maps(s)}" target="_blank" rel="noopener">Indicații <i>↗</i></a><a class="b2" href="tel:{tel(s['phone'])}" style="color:var(--ink)">Sună acum</a></div></div>
<div data-up><span class="eb">Program</span><div style="margin-bottom:14px">{open_b}</div>{hrs}</div></div></section>
<section id="oferta" class="of"><div class="w"><span class="eb">Pentru proprietarul {E(s['name'])}</span>
<h2 class="d" data-sp>{words(num(s['reviews']) + " de oameni v-au lăudat. Restul nu vă găsesc.")}</h2>
<p class="mu" style="max-width:62ch;font-size:1.15rem">Cine vă caută acum pe telefon {now_line} Nu vede dintr-o privire {what}, așa că alege localul de alături. Pagina pe care tocmai ați văzut-o e făcută deja, cu datele voastre reale.</p>
<div class="cmp"><div data-up><h3>Acum</h3><ul><li>{E(s['now'][0].upper() + s['now'][1:])}</li><li>{"Prețurile nu se văd pe Google" if s["kind"] == "barber" else "Meniul nu se vede pe Google"}</li><li>Recenziile bune stau ascunse</li><li>Clienții noi aleg pe altcineva</li></ul></div>
<div class="y" data-up><h3>Cu site-ul acesta</h3><ul><li>Site-ul vostru, pe domeniul vostru</li><li>Sunat, indicații și {"programare" if s["book"] else "rezervare"} dintr-un click</li><li>Recenziile voastre, pe prima pagină</li><li>Arată așa, cu animațiile acestea, pe orice telefon</li></ul></div></div>
<div class="pr"><div class="pk" data-up><p style="margin:0;font-weight:700">Starter</p><p class="d">1.500 lei</p><p class="mu" style="margin:0">Până la 3 pagini. Exact ce vedeți aici, terminat cu pozele și textele voastre.</p></div>
<div class="pk hl" data-up><p style="margin:0;font-weight:700">Standard <span class="tag">recomandat</span></p><p class="d big">2.500 lei</p><p class="mu" style="margin:0">Până la 5 pagini, formular de {"programare" if s["kind"] == "barber" else "rezervare"} și profilul Google pus la punct.</p></div></div>
<div class="gu"><div><b>Gata în aceeași zi</b><span class="mu">în care primim pozele și textele.</span></div><div><b>Avans 50%</b><span class="mu">restul doar la final.</span></div><div><b>Fără risc</b><span class="mu">nu vă place primul design? Vă dăm avansul înapoi.</span></div></div>
<div class="btns"><a class="b1 mag" href="mailto:{EMAIL}?subject={subj}">Vreau site-ul <i>→</i></a></div>
<p class="mu" style="margin-top:18px;font-size:.92rem">George, Storefront Studio, Sighișoara. Mentenanță opțională: 150 lei pe lună.</p></div></section>
<footer><p class="d giant" aria-hidden="true">{E(s['name'])} · {E(s['name'])}</p><div class="w row"><span>{E(s['name'])} · {E(s['address'])}, {E(s['zip'])}</span><span>Propunere: Storefront Studio</span></div></footer>
<nav class="mb" aria-label="Acțiuni rapide"><a href="tel:{tel(s['phone'])}">Sună</a><a href="{maps(s)}" target="_blank" rel="noopener">Indicații</a><a class="m1" href="{E(book)}"{tgt}>{short}</a></nav>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script><script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
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
