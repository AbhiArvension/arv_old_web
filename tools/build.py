"""Static site generator. Run from the repo root:  python3 tools/build.py"""
import html
import json
import pathlib
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from art import art, icon, sprite  # noqa: E402
from data import CATEGORIES, HOME_FAQ, PRODUCTS, SERVICES, SITE  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = "2026-10-26"
E = html.escape
BASE = SITE["url"]
BRAND = "#c8102e"


def wa_link(text):
    return f"https://wa.me/{SITE['wa']}?text={quote(text)}"


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'


ORG = {
    "@context": "https://schema.org",
    "@type": ["Organization", "ProfessionalService"],
    "@id": f"{BASE}/#org",
    "name": SITE["name"],
    "alternateName": "Arvension",
    "url": BASE + "/",
    "logo": f"{BASE}/img/logo.png",
    "image": f"{BASE}/img/og-image.png",
    "telephone": SITE["tel"],
    "description": "ERP software, AI websites, chat apps, web apps and mobile apps company in Technopark, Thiruvananthapuram, Kerala.",
    "address": {"@type": "PostalAddress", "streetAddress": "4th Floor, Module 6, Gayathri Building, Technopark",
                "addressLocality": "Thiruvananthapuram", "addressRegion": "Kerala", "postalCode": "695581", "addressCountry": "IN"},
    "areaServed": "IN",
    "openingHours": "Mo-Sa 09:30-17:30",
    "sameAs": [s[2] for s in SITE["social"]],
}


def head(p, title, desc, path, og_image="img/og-image.png", extra=""):
    canon = f"{BASE}/{path}" if path else f"{BASE}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0b1220">
<link rel="canonical" href="{canon}">
<link rel="icon" type="image/png" href="{p}img/favicon.png">
<link rel="apple-touch-icon" href="{p}img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/{og_image}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{BASE}/{og_image}">
<link rel="stylesheet" href="{p}css/site.css?v=2">
{extra}</head>
"""


def header(p, current):
    links = [("erp.html", "ERP Solutions", "erp"), ("services.html", "Services", "services"),
             ("about.html", "About", "about"), ("contact.html", "Contact", "contact")]
    items = "".join(
        f'<a class="nl" href="{p}{h}"{" aria-current=page" if current == k else ""}>{t}</a>' for h, t, k in links)
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
{sprite()}
<header class="site-header">
<div class="container nav">
<a class="brand" href="{p}index.html" aria-label="{SITE['name']} home"><img src="{p}img/logo.webp" width="40" height="40" alt=""><span class="brand-name">Arvension<small>Technologies LLP</small></span></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="Menu">{icon('menu', 'ic i-menu')}{icon('close', 'ic i-close')}</button>
<nav class="nav-menu" id="nav-menu" aria-label="Main">{items}<a class="btn btn-primary" href="{wa_link('Hello Arvension, I would like a free ERP demo.')}" target="_blank" rel="noopener">Free demo</a></nav>
</div>
</header>
<main id="main">
"""


def footer(p):
    prods = "".join(f'<li><a href="{p}erp/{x["slug"]}.html">{E(x["name"])}</a></li>' for x in PRODUCTS)
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{icon(k)}</a>' for k, n, u in SITE["social"])
    svc = "".join(f'<li><a href="{p}services.html#{s["slug"]}">{E(s["name"])}</a></li>' for s in SERVICES)
    return f"""</main>
<footer class="site-footer">
<div class="container">
<div class="foot-grid">
<div class="foot-brand"><a class="brand" href="{p}index.html"><img src="{p}img/logo.webp" width="40" height="40" alt=""><span class="brand-name">Arvension<small>Technologies LLP</small></span></a>
<p>AI-powered ERP, websites, web apps and mobile apps, designed and built in Technopark, Thiruvananthapuram.</p>
<div class="social">{soc}</div></div>
<div><h3>ERP Solutions</h3><ul>{prods}</ul></div>
<div><h3>Services</h3><ul>{svc}</ul><h3 style="margin-top:22px">Company</h3><ul><li><a href="{p}about.html">About us</a></li><li><a href="{p}contact.html">Contact</a></li><li><a href="{p}privacy.html">Privacy policy</a></li><li><a href="{p}terms.html">Terms of use</a></li></ul></div>
<div><h3>Contact</h3><ul>
<li>{icon('pin')} {E(SITE['address'])}</li>
<li>{icon('phone-call')} <a href="tel:{SITE['tel']}">{SITE['phone']}</a></li>
<li>{icon('clock')} {SITE['hours']}</li></ul></div>
</div>
<div class="copy"><span>&copy; 2026 {SITE['name']}. All rights reserved.</span><span>Made in Kerala, India</span></div>
</div>
</footer>
<a class="wa-float" href="{wa_link('Hello Arvension, I would like to know more about your ERP solutions.')}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{icon('whatsapp')}</a>
<script src="{p}js/site.js?v=1" defer></script>
</body>
</html>
"""


def cta(title="Get a free live demo of your ERP", text="Tell us about your business. We will show you a working demo and a clear quote, with no obligation."):
    return f"""<section class="section"><div class="container"><div class="cta reveal">
<h2>{E(title)}</h2><p>{E(text)}</p>
<div class="btn-row"><a class="btn btn-primary" href="{wa_link('Hello Arvension, I would like a free ERP demo.')}" target="_blank" rel="noopener">{icon('whatsapp')} Chat on WhatsApp</a>
<a class="btn btn-ghost" href="tel:{SITE['tel']}">{icon('phone-call')} Call {SITE['phone']}</a></div></div></div></section>"""


def faq_block(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in items) + "</div>"


def faq_ld(items):
    return ld({"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})


def product_card(p, x):
    apps = "".join(f'<span class="tag">{E(a[0].replace(" Mobile App", " App"))}</span>' for a in x["apps"][:3])
    return f"""<a class="card reveal" href="{p}erp/{x['slug']}.html" style="--c:{x['color']}">
<span class="ibox">{icon(x['icon'])}</span><h3>{E(x['name'])}</h3><p>{E(x['short'])}</p>
<div class="tags">{apps}</div><span class="more">Explore {icon('arrow')}</span></a>"""


def product_groups(p):
    out = []
    for key, title, sub in CATEGORIES:
        cards = "".join(product_card(p, x) for x in PRODUCTS if x["cat"] == key)
        out.append(f'<div class="cat-title"><h3>{E(title)}</h3><p>{E(sub)}</p></div><div class="grid">{cards}</div>')
    return "".join(out)


def checks(items):
    return '<ul class="checks">' + "".join(f'<li>{icon("check")}<span>{E(i)}</span></li>' for i in items) + "</ul>"


# ----------------------------------------------------------------- pages
def page_index():
    p = ""
    title = "Arvension Technologies | AI ERP Software, Websites & Mobile Apps in Kerala"
    desc = "AI-based ERP for schools, colleges, microfinance, chit fund, gold loan, Nidhi and co-operative societies, plus AI websites, chat apps and mobile apps. Technopark, Trivandrum."
    schema = ld(ORG) + ld({"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"], "url": BASE + "/"}) + faq_ld(HOME_FAQ)
    apps = [
        ("user", "Customer & Member App", "Accounts, schedules, receipts and online payment for customers of finance ERPs."),
        ("pin", "Field Agent App", "Collections and visits with live GPS tracking for the head office."),
        ("clock", "Staff Attendance Punch-in", "GPS and selfie-verified attendance for branch and site staff."),
        ("school", "Parent App", "Attendance, fees, homework, results and live bus location for parents."),
        ("bus", "School Bus Driver App", "Trip start, stop-wise punch-in and live tracking for school transport."),
        ("shield", "Director App", "Approvals, dashboards and alerts built for Nidhi and co-operative boards."),
    ]
    app_cards = "".join(f'<div class="card reveal"><span class="ibox" style="--c:#2563eb">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in apps)
    ai = ["Risk scoring that flags likely defaulters before they miss a payment",
          "A plain-language assistant: ask “which branch is overdue this week?” and get an answer",
          "Anomaly detection on cash, collections, stock and attendance",
          "Smart WhatsApp and SMS reminders sent at the right time",
          "Automatic summaries and insights for owners and directors"]
    svc = "".join(f'<a class="card reveal" href="services.html#{s["slug"]}"><span class="ibox" style="--c:{BRAND}">{icon(s["icon"])}</span><h3>{E(s["name"])}</h3><p>{E(s["short"])}</p><span class="more">Learn more {icon("arrow")}</span></a>' for s in SERVICES)
    steps = [("Free demo", "See a live ERP demo for your industry and tell us how you work."),
             ("Customise", "We configure workflows, forms, reports and branding for your business."),
             ("Launch & train", "We migrate your data, set up the apps and train your team."),
             ("Support & grow", "Ongoing support, updates and new features as you expand.")]
    st = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in steps)
    body = f"""<section class="hero"><div class="container grid-2">
<div><span class="eyebrow">{icon('sparkle')} AI-powered software company in Kerala</span>
<h1>ERP, mobile apps and AI software that <em>run your business</em></h1>
<p class="lead">From schools and colleges to microfinance, chit fund, gold loan, Nidhi and co-operative societies. One system for every branch, with mobile apps for your customers, agents and staff.</p>
<div class="btn-row"><a class="btn btn-primary" href="{wa_link('Hello Arvension, I would like a free ERP demo.')}" target="_blank" rel="noopener">{icon('whatsapp')} Book a free demo</a><a class="btn btn-ghost" href="erp.html">Explore ERP solutions</a></div>
<ul class="trust"><li>{icon('check')} Unlimited branches &amp; staff</li><li>{icon('check')} Android &amp; iOS apps</li><li>{icon('check')} AI built in</li><li>{icon('check')} Local support</li></ul></div>
<div class="hero-art"><img src="img/hero.svg" width="1000" height="780" alt="Arvension ERP dashboard and mobile app preview" fetchpriority="high"></div>
</div></section>
<section class="strip"><ul class="container">
<li><strong>12</strong><span>Ready ERP solutions</span></li><li><strong>Unlimited</strong><span>Branches &amp; staff</span></li>
<li><strong>6+</strong><span>Mobile app types</span></li><li><strong>AI</strong><span>Inside every ERP</span></li></ul></section>
<section class="section" id="erp"><div class="container">
<div class="section-head"><span class="eyebrow">ERP Solutions</span><h2>The right ERP for your industry</h2><p>Ready-to-customise systems, already proven in how institutions and finance companies actually work. Pick yours and we tailor it.</p></div>
{product_groups(p)}</div></section>
<section class="section soft"><div class="container">
<div class="section-head"><span class="eyebrow">Mobile apps</span><h2>Apps your customers, agents and staff will actually use</h2><p>Every ERP comes with the mobile apps that make it work in the real world, not just in the office.</p></div>
<div class="grid">{app_cards}</div></div></section>
<section class="section dark"><div class="container split">
<div><span class="eyebrow">{icon('sparkle')} Artificial intelligence</span><h2>AI that does real work, not just a buzzword</h2>
<p>Our ERPs use AI where it saves money and time: predicting problems, automating follow-ups and answering questions about your own data.</p>{checks(ai)}
<a class="btn btn-primary" href="services.html#ai-websites-chat-apps">AI websites &amp; chat apps</a></div>
<div class="split-media reveal"><img src="img/ai-chat.svg" width="1000" height="780" alt="AI chat assistant answering business questions" loading="lazy"></div></div></section>
<section class="section"><div class="container">
<div class="section-head"><span class="eyebrow">Services</span><h2>Websites, web apps, mobile apps and AI</h2><p>Not just ERP. We design and build the digital products your business needs to be found, trusted and chosen.</p></div>
<div class="grid">{svc}</div></div></section>
<section class="section soft"><div class="container">
<div class="section-head"><span class="eyebrow">How we work</span><h2>From first call to live system</h2></div>
<ol class="steps">{st}</ol></div></section>
<section class="section"><div class="container split">
<div class="split-media reveal"><img src="img/about.svg" width="1000" height="780" alt="Arvension team building software" loading="lazy"></div>
<div><span class="eyebrow">Why Arvension</span><h2>Built by a Kerala software team that stays with you</h2>
{checks(["One platform for head office, branches, field teams and customers", "No limits on branches, staff or customers for our finance ERPs", "Customised to your workflow, not forced into a template", "Direct support from the team that built it", "Based in Technopark, Thiruvananthapuram, serving clients across India"])}
<a class="btn btn-outline" href="about.html">About us</a></div></div></section>
<section class="section soft"><div class="container"><div class="section-head"><span class="eyebrow">FAQ</span><h2>Questions we hear often</h2></div>{faq_block(HOME_FAQ)}</div></section>
{cta()}"""
    return head(p, title, desc, "", extra=schema) + header(p, "home") + body + footer(p)


def page_erp():
    p = ""
    title = "ERP Software Solutions for Schools, Finance & Construction | Arvension"
    desc = "Explore 12 AI-based ERP solutions: school, college, hostel, library, mess, store, construction, microfinance, chit fund, gold loan, Nidhi and co-operative society."
    schema = ld({"@context": "https://schema.org", "@type": "ItemList", "name": "Arvension ERP solutions",
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/erp/{x['slug']}.html", "name": x["full"]} for i, x in enumerate(PRODUCTS)]})
    body = f"""<section class="hero page-hero"><div class="container">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>ERP Solutions</span></nav>
<h1>AI-based ERP solutions for every industry we serve</h1>
<p class="lead">Twelve proven ERP systems with web dashboards and mobile apps, fully customised for your business.</p>
<div class="btn-row"><a class="btn btn-primary" href="{wa_link('Hello Arvension, I would like a free ERP demo.')}" target="_blank" rel="noopener">{icon('whatsapp')} Get a free demo</a></div></div></section>
<section class="section"><div class="container">{product_groups(p)}</div></section>
<section class="section soft"><div class="container section-head"><h2>Do not see your industry?</h2><p>We also build custom ERPs and apps from scratch. Tell us how your business runs and we will design the system around it.</p><a class="btn btn-primary" href="services.html#erp-development">Custom ERP development</a></div></section>
{cta()}"""
    return head(p, title, desc, "erp.html", extra=schema) + header(p, "erp") + body + footer(p)


def page_product(x):
    p = "../"
    path = f"erp/{x['slug']}.html"
    sw = ld({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": x["full"], "applicationCategory": "BusinessApplication",
             "operatingSystem": "Web, Android, iOS", "description": x["desc"], "url": f"{BASE}/{path}",
             "image": f"{BASE}/img/products/{x['slug']}.svg", "provider": {"@id": f"{BASE}/#org"}})
    crumbs = ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "ERP Solutions", "item": BASE + "/erp.html"},
        {"@type": "ListItem", "position": 3, "name": x["full"], "item": f"{BASE}/{path}"}]})
    mods = "".join(f'<li>{icon("check")}<span>{E(m)}</span></li>' for m in x["modules"])
    apps = "".join(f'<div class="card reveal"><span class="ibox" style="--c:{x["color"]}">{icon("phone")}</span><h3>{E(a)}</h3><p>{E(d)}</p></div>' for a, d in x["apps"])
    same = [y for y in PRODUCTS if y["cat"] == x["cat"] and y is not x]
    rest = [y for y in PRODUCTS if y["cat"] != x["cat"]]
    related = "".join(product_card(p, y) for y in (same + rest)[:3])
    msg = f"Hello Arvension, I would like a demo of the {x['full']}."
    body = f"""<section class="hero page-hero" style="--c:{x['color']}"><div class="container grid-2">
<div><nav class="crumbs" aria-label="Breadcrumb"><a href="{p}index.html">Home</a><span aria-hidden="true">/</span><a href="{p}erp.html">ERP Solutions</a><span aria-hidden="true">/</span><span>{E(x['name'])}</span></nav>
<h1>{E(x['h1'])}</h1><p class="lead">{E(x['sub'])}</p>
<div class="btn-row"><a class="btn btn-primary" href="{wa_link(msg)}" target="_blank" rel="noopener">{icon('whatsapp')} Get a free demo</a><a class="btn btn-ghost" href="tel:{SITE['tel']}">{icon('phone-call')} Call now</a></div></div>
<div class="hero-art"><img src="{p}img/products/{x['slug']}.svg" width="1000" height="780" alt="{E(x['full'])} dashboard and mobile app" fetchpriority="high"></div></div></section>
<section class="section"><div class="container prose" style="max-width:860px"><h2 style="margin-top:0">Overview</h2><p style="font-size:1.1rem">{E(x['intro'])}</p>
<p><strong>Built for:</strong> {E(x['who'])}</p></div></section>
<section class="section soft"><div class="container"><div class="section-head"><span class="eyebrow">Features</span><h2>What is inside the {E(x['name'])}</h2></div>
<ul class="modules" style="--c:{x['color']}">{mods}</ul></div></section>
<section class="section"><div class="container"><div class="section-head"><span class="eyebrow">Mobile apps</span><h2>Mobile apps included</h2></div><div class="grid">{apps}</div></div></section>
<section class="section dark"><div class="container split">
<div><span class="eyebrow">{icon('sparkle')} AI features</span><h2>Smarter with built-in AI</h2>{checks(x['ai'])}</div>
<div><h2 style="font-size:1.5rem">Why choose this system</h2>{checks(x['benefits'])}<a class="btn btn-primary" href="{wa_link(msg)}" target="_blank" rel="noopener">Request a demo</a></div></div></section>
<section class="section"><div class="container"><div class="section-head"><span class="eyebrow">FAQ</span><h2>{E(x['name'])}: common questions</h2></div>{faq_block(x['faq'])}</div></section>
<section class="section soft"><div class="container"><div class="section-head"><h2>Related solutions</h2></div><div class="grid">{related}</div></div></section>
{cta('Ready to see it working for your business?')}"""
    return head(p, x["title"], x["desc"], path, extra=sw + crumbs + faq_ld(x["faq"])) + header(p, "erp") + body + footer(p)


def page_services():
    p = ""
    title = "Web Design, Web Apps, Mobile Apps & AI Chat Apps | Arvension Trivandrum"
    desc = "Website design company in Thiruvananthapuram: AI websites, chatbots, custom web apps, Android and iOS mobile apps and ERP development for businesses across India."
    imgs = {"ai-websites-chat-apps": "ai-chat", "web-design": "web", "web-apps": "dash", "mobile-apps": "mobile", "erp-development": "hero"}
    rows = []
    for i, s in enumerate(SERVICES):
        rows.append(f"""<div class="svc split{' rev' if i % 2 else ''}" id="{s['slug']}"><div class="split-media reveal"><img src="img/{imgs[s['slug']]}.svg" width="1000" height="780" alt="{E(s['name'])}" loading="lazy"></div>
<div><span class="ibox" style="--c:{BRAND}">{icon(s['icon'])}</span><h2 style="margin-top:16px">{E(s['name'])}</h2><p>{E(s['short'])}</p>{checks(s['points'])}
<a class="btn btn-primary" href="{wa_link('Hello Arvension, I am interested in ' + s['name'] + '.')}" target="_blank" rel="noopener">Discuss your project</a></div></div>""")
    schema = ld({"@context": "https://schema.org", "@type": "ItemList", "name": "Arvension services",
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f"{BASE}/services.html#{s['slug']}"} for i, s in enumerate(SERVICES)]})
    body = f"""<section class="hero page-hero"><div class="container">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Services</span></nav>
<h1>Websites, web apps, mobile apps and AI, built to grow your business</h1>
<p class="lead">A full-stack software team in Technopark, Trivandrum. We design, build, launch and support.</p></div></section>
<section class="section"><div class="container">{''.join(rows)}</div></section>{cta('Have a project in mind?', 'Share your idea and we will come back with a plan, timeline and quote.')}"""
    return head(p, title, desc, "services.html", extra=schema) + header(p, "services") + body + footer(p)


def page_about():
    p = ""
    title = "About Arvension Technologies LLP | Software Company in Technopark, Trivandrum"
    desc = "Arvension Technologies LLP is a Kerala software company building AI-based ERP, websites, web apps and mobile apps from Technopark, Thiruvananthapuram."
    vals = [("Practical first", "We build what your team will actually use every day, not features that look good in a brochure."),
            ("Straight talk", "Clear scope, clear pricing and honest timelines from the first conversation."),
            ("Long-term partner", "We stay after launch with support, updates and new features as your business grows.")]
    v = "".join(f'<div class="card reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in vals)
    body = f"""<section class="hero page-hero"><div class="container">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>About</span></nav>
<h1>A Kerala software team that builds the systems businesses run on</h1>
<p class="lead">Arvension Technologies LLP started as a student start-up from College of Engineering Attingal (IHRD) and is today based in Technopark, Thiruvananthapuram.</p></div></section>
<section class="section"><div class="container split">
<div><span class="eyebrow">Our story</span><h2>From campus start-up to ERP specialists</h2>
<p>We began by building software for small businesses and training students. Over time we saw the same problems everywhere: schools, finance companies and contractors running critical work on registers and spreadsheets.</p>
<p>So we built ERP systems for them, and wrapped each in the mobile apps real teams need: attendance, field collection with live tracking, parent and customer apps. Today we also build AI websites and chat apps, web apps and mobile apps for clients across India.</p></div>
<div class="split-media reveal"><img src="img/about.svg" width="1000" height="780" alt="Arvension team at work" loading="lazy"></div></div></section>
<section class="section soft"><div class="container"><div class="section-head"><span class="eyebrow">What we value</span><h2>How we work</h2></div><div class="grid">{v}</div></div></section>
<section class="section"><div class="container prose"><h2 style="margin-top:0">Visit us</h2><p>{E(SITE['address'])}<br>{SITE['hours']}</p>
<p><a class="btn btn-outline" href="contact.html">Contact us</a></p></div></section>{cta()}"""
    return head(p, title, desc, "about.html", extra=ld(ORG)) + header(p, "about") + body + footer(p)


def page_contact():
    p = ""
    title = "Contact Arvension Technologies | Get a Free ERP Demo, Trivandrum"
    desc = "Contact Arvension Technologies LLP in Technopark, Thiruvananthapuram. Call +91 91421 25724 or message us on WhatsApp for a free ERP demo and quote."
    opts = "".join(f"<option>{E(x['name'])}</option>" for x in PRODUCTS) + "<option>AI website / chat app</option><option>Website design</option><option>Web app</option><option>Mobile app</option><option>Custom software</option>"
    body = f"""<section class="hero page-hero"><div class="container">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Contact</span></nav>
<h1>Let us talk about your project</h1><p class="lead">Request a free demo. Fill in the form and it opens a WhatsApp message to our team, or call us directly.</p></div></section>
<section class="section"><div class="container contact-grid">
<div><ul class="info-list">
<li><span class="ibox" style="--c:{BRAND}">{icon('pin')}</span><div><strong>Address</strong>{E(SITE['address'])}</div></li>
<li><span class="ibox" style="--c:#16a34a">{icon('phone-call')}</span><div><strong>Phone / WhatsApp</strong><a href="tel:{SITE['tel']}">{SITE['phone']}</a></div></li>
<li><span class="ibox" style="--c:#2563eb">{icon('clock')}</span><div><strong>Working hours</strong>{SITE['hours']}</div></li></ul>
<iframe class="map" title="Arvension Technologies location in Technopark, Trivandrum" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Technopark+Trivandrum&amp;output=embed"></iframe></div>
<form class="lead-form" id="lead-form" data-wa="{SITE['wa']}">
<label>Your name<input name="name" required autocomplete="name"></label>
<label>Phone number<input name="phone" type="tel" required autocomplete="tel" inputmode="tel"></label>
<label>I am interested in<select name="interest">{opts}</select></label>
<label>Message (optional)<textarea name="message"></textarea></label>
<button class="btn btn-wa" type="submit">{icon('whatsapp')} Send on WhatsApp</button>
<p class="form-note">This opens WhatsApp with your details prefilled. We reply during working hours.</p></form></div></section>"""
    schema = ld({"@context": "https://schema.org", "@type": "ContactPage", "url": f"{BASE}/contact.html", "name": "Contact Arvension Technologies"}) + ld(ORG)
    return head(p, title, desc, "contact.html", extra=schema) + header(p, "contact") + body + footer(p)


def legal(name, title, desc, sections):
    p = ""
    secs = "".join(f"<h2>{E(h)}</h2>{b}" for h, b in sections)
    body = f"""<section class="hero page-hero"><div class="container"><h1>{E(name)}</h1><p class="lead">Last updated: 26 October 2026</p></div></section>
<section class="section"><div class="container prose">{secs}</div></section>"""
    path = name.lower().split()[0] + ".html"
    return head(p, title, desc, path, extra='<meta name="robots" content="index,follow">\n') + header(p, "") + body + footer(p)


def page_privacy():
    s = [("Who we are", f"<p>{SITE['name']} (&ldquo;Arvension&rdquo;, &ldquo;we&rdquo;) operates arvension.in. This policy explains what information we collect through this website and how we use it.</p>"),
         ("Information we collect", "<ul><li>Details you share with us, such as name, phone number and message, when you contact us or request a demo.</li><li>Basic technical data your browser sends to any website, such as device type and pages visited, in server logs kept by our hosting provider.</li></ul><p>This website does not run advertising trackers. When you use the contact form it opens WhatsApp on your device; the message is then handled by WhatsApp under its own privacy policy.</p>"),
         ("How we use it", "<ul><li>To reply to your enquiry and provide demos and quotes.</li><li>To improve our website and services.</li></ul><p>We do not sell your personal information.</p>"),
         ("Sharing", "<p>We share information only with service providers who help us operate our business, or when the law requires it.</p>"),
         ("Your choices", f"<p>You can ask us to access, correct or delete the information you have given us by calling {SITE['phone']} or writing to us on WhatsApp.</p>"),
         ("Client software", "<p>Data stored in ERP systems and apps we build for clients is governed by the agreement with each client.</p>"),
         ("Contact", f"<p>{E(SITE['name'])}, {E(SITE['address'])}. Phone: {SITE['phone']}.</p>")]
    return legal("Privacy Policy", "Privacy Policy | Arvension Technologies LLP", "How Arvension Technologies LLP collects, uses and protects information shared through arvension.in.", s)


def page_terms():
    s = [("Use of this website", "<p>The content on arvension.in is provided for general information about our services. By using this website you agree to these terms.</p>"),
         ("Services and quotes", "<p>Descriptions of our ERP systems, apps and features are indicative. The final scope, price and timeline for any project are set out in a written proposal or agreement.</p>"),
         ("Intellectual property", f"<p>The website content, design and logo belong to {E(SITE['name'])}. Please do not copy them without written permission.</p>"),
         ("Third-party links", "<p>This site links to third-party services such as WhatsApp, Google Maps and social networks. We are not responsible for their content or practices.</p>"),
         ("Limitation of liability", "<p>We take care to keep this website accurate and available but provide it as is, without warranties, to the extent permitted by law.</p>"),
         ("Governing law", "<p>These terms are governed by the laws of India. Courts at Thiruvananthapuram, Kerala have jurisdiction.</p>"),
         ("Contact", f"<p>Questions about these terms: {SITE['phone']}, {E(SITE['address'])}.</p>")]
    return legal("Terms of Use", "Terms of Use | Arvension Technologies LLP", "Terms for using the Arvension Technologies LLP website and our service proposals.", s)


def page_404():
    p = "/"
    body = f"""<section class="hero page-hero"><div class="container"><h1>Page not found</h1><p class="lead">The page you are looking for does not exist or has moved.</p>
<div class="btn-row"><a class="btn btn-primary" href="/index.html">Go to home</a><a class="btn btn-ghost" href="/erp.html">View ERP solutions</a></div></div></section>"""
    return head(p, "Page not found | Arvension Technologies", "Page not found.", "404.html", extra='<meta name="robots" content="noindex">\n') + header(p, "") + body + footer(p)


def build():
    for old in (ROOT / "erp").glob("*.html"):
        old.unlink()
    write("index.html", page_index())
    write("erp.html", page_erp())
    write("services.html", page_services())
    write("about.html", page_about())
    write("contact.html", page_contact())
    write("privacy.html", page_privacy())
    write("terms.html", page_terms())
    write("404.html", page_404())
    for x in PRODUCTS:
        write(f"erp/{x['slug']}.html", page_product(x))
        write(f"img/products/{x['slug']}.svg", art(x["color"], x["icon"], x["chips"]))
    write("img/hero.svg", art(BRAND, "sparkle", ["AI insights", "Live agent tracking", "Unlimited branches"]))
    write("img/ai-chat.svg", art("#7c3aed", "chat", ["AI assistant", "24/7 replies", "Lead capture"], "chat"))
    write("img/web.svg", art("#0891b2", "globe", ["SEO-ready", "Mobile-first", "Fast"], "site"))
    write("img/dash.svg", art("#2563eb", "chart", ["Dashboards", "Secure login", "API ready"]))
    write("img/mobile.svg", art("#16a34a", "phone", ["Android", "iOS", "Live GPS"], "phones"))
    write("img/about.svg", art("#d97706", "code", ["Made in Kerala", "Technopark", "Built to last"]))
    urls = ["", "erp.html", "services.html", "about.html", "contact.html", "privacy.html", "terms.html"] + [f"erp/{x['slug']}.html" for x in PRODUCTS]
    smap = "".join(f"<url><loc>{BASE}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{'1.0' if not u else '0.8'}</priority></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{smap}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("built", len(urls) + 1, "pages")


if __name__ == "__main__":
    build()
