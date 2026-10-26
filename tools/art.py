"""Generates the SVG illustrations and icon sprite used by the site."""

ICONS = {
    "construction": "M3 21h18M5 21V8l7-4 7 4v13M9 21v-6h6v6",
    "school": "M2 9l10-5 10 5-10 5-10-5zM6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5",
    "college": "M3 10l9-6 9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 20h18",
    "hostel": "M3 18V6M3 14h18v4M21 14v-3a3 3 0 0 0-3-3h-7v6M7 11.5h.01",
    "library": "M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5zM19 19v2H6",
    "mess": "M6 3v8M4 3v5a2 2 0 0 0 4 0V3M6 11v10M17 3c-2 2-2.5 5-2.5 8H17v10",
    "store": "M21 8l-9-5-9 5v8l9 5 9-5V8zM3 8l9 5 9-5M12 13v9",
    "microfinance": "M12 3C7.6 3 4 4.3 4 6s3.6 3 8 3 8-1.3 8-3-3.6-3-8-3zM4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6",
    "chit": "M21 12a9 9 0 0 1-15.5 6.2M3 12A9 9 0 0 1 18.5 5.8M18 2v4h-4M6 22v-4h4",
    "gold": "M6 3h12l4 6-10 12L2 9l4-6zM2 9h20M12 21L8 9l4-6 4 6-4 12",
    "nidhi": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3zM9 12l2 2 4-4",
    "coop": "M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 10a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM22 20v-2a4 4 0 0 0-3-3.9M16 3.1a3.5 3.5 0 0 1 0 6.8",
    "phone": "M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zM11 18h2",
    "globe": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18",
    "chat": "M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-5.4A8 8 0 1 1 21 12zM8.5 12h.01M12 12h.01M15.5 12h.01",
    "sparkle": "M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3zM19 16l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7.7-2z",
    "code": "M16 18l6-6-6-6M8 6l-6 6 6 6",
    "pin": "M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11zM12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z",
    "clock": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2",
    "check": "M5 12l5 5L20 7",
    "chart": "M4 20V10M10 20V4M16 20v-7M22 20H2",
    "bus": "M4 16V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10M4 16h16M4 16v2h3v-2M17 16v2h3v-2M4 11h16M8 13h.01M16 13h.01",
    "mail": "M3 6h18v12H3zM3 7l9 6 9-6",
    "arrow": "M5 12h14M13 6l6 6-6 6",
    "menu": "M4 7h16M4 12h16M4 17h16",
    "close": "M6 6l12 12M18 6L6 18",
    "layers": "M12 3l9 5-9 5-9-5 9-5zM3 13l9 5 9-5M3 17.5l9 5 9-5",
    "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z",
    "user": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1",
    "palette": "M12 3a9 9 0 1 0 0 18c1.2 0 2-.8 2-1.8 0-.5-.2-.9-.5-1.2-.3-.4-.5-.8-.5-1.3 0-1 .8-1.7 1.8-1.7H17a4 4 0 0 0 4-4c0-4.4-4-8-9-8zM7.5 11h.01M10 7.5h.01M14 7.5h.01",
    "phone-call": "M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z",
    "facebook": "M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v7h4v-7h3l1-4h-4V8z",
    "linkedin": "M4 9h4v11H4zM6 4a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v1.5c.8-1.2 2-1.8 3.5-1.8 3 0 3.5 2 3.5 4.5V20h-4v-6c0-1.3-.3-2-1.5-2S14 12.7 14 14v6h-4V9z",
    "x": "M4 4l16 16M20 4L4 20",
    "db": "M12 3C7.6 3 4 4.3 4 6s3.6 3 8 3 8-1.3 8-3-3.6-3-8-3zM4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3",
    "whatsapp": "M3 21l1.6-4.7A9 9 0 1 1 8 19.6L3 21zM9 8.5c0 3.5 3 6.5 6.5 6.5l1.2-1.6-2.2-1.2-1 .8a5 5 0 0 1-2.3-2.3l.8-1-1.2-2.2L9 8.5z",
}


def sprite():
    out = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">']
    for k, d in ICONS.items():
        out.append(f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></symbol>')
    out.append("</svg>")
    return "".join(out)


def icon(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def _mix(hexc, other, f):
    h = hexc.lstrip("#")
    a = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    o = [int(other.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(x + (y - x) * f):02x}" for x, y in zip(a, o))


def _chip(x, y, text, color):
    w = len(text) * 12 + 64
    return (
        f'<g transform="translate({x} {y})"><rect width="{w}" height="54" rx="27" fill="#fff"/>'
        f'<circle cx="28" cy="27" r="9" fill="{color}"/>'
        f'<text x="48" y="35" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="21" font-weight="700" fill="#0f172a">{text}</text></g>'
    )


def _icon_g(name, x, y, scale, color="#fff", sw=1.8):
    return (
        f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[name]}"/></g>'
    )


def _window(accent, mode):
    s = [f'<rect x="60" y="100" width="720" height="500" rx="26" fill="#fff"/>',
         '<circle cx="96" cy="136" r="7" fill="#fca5a5"/><circle cx="120" cy="136" r="7" fill="#fcd34d"/><circle cx="144" cy="136" r="7" fill="#86efac"/>',
         '<rect x="60" y="160" width="720" height="2" fill="#eef0f5"/>']
    if mode == "chat":
        s.append(f'<rect x="90" y="190" width="400" height="64" rx="22" fill="#eef0f5"/><rect x="116" y="212" width="250" height="12" rx="6" fill="#c3c9d6"/>')
        s.append(f'<rect x="300" y="276" width="440" height="84" rx="22" fill="{accent}"/><rect x="326" y="302" width="320" height="12" rx="6" fill="#ffffff" opacity=".9"/><rect x="326" y="326" width="200" height="12" rx="6" fill="#ffffff" opacity=".6"/>')
        s.append('<rect x="90" y="382" width="360" height="64" rx="22" fill="#eef0f5"/><rect x="116" y="404" width="220" height="12" rx="6" fill="#c3c9d6"/>')
        s.append(f'<rect x="300" y="468" width="300" height="56" rx="22" fill="{accent}"/><rect x="326" y="490" width="190" height="12" rx="6" fill="#fff" opacity=".85"/>')
        s.append('<rect x="90" y="544" width="650" height="40" rx="20" fill="#f3f4f8"/>')
        return "".join(s)
    if mode == "site":
        s.append(f'<rect x="90" y="190" width="660" height="150" rx="18" fill="{_mix(accent, "#000000", .25)}"/>'
                 '<rect x="120" y="222" width="320" height="18" rx="9" fill="#fff"/><rect x="120" y="254" width="240" height="12" rx="6" fill="#fff" opacity=".6"/>'
                 '<rect x="120" y="286" width="110" height="34" rx="17" fill="#fff"/>')
        for i in range(3):
            x = 90 + i * 222
            s.append(f'<rect x="{x}" y="364" width="206" height="200" rx="18" fill="#f3f4f8"/><rect x="{x + 18}" y="382" width="60" height="60" rx="16" fill="{accent}" opacity="{1 - i * .2}"/>'
                     f'<rect x="{x + 18}" y="460" width="130" height="12" rx="6" fill="#c3c9d6"/><rect x="{x + 18}" y="486" width="165" height="10" rx="5" fill="#dde1ea"/><rect x="{x + 18}" y="506" width="120" height="10" rx="5" fill="#dde1ea"/>')
        return "".join(s)
    # dashboard
    s.append('<rect x="60" y="162" width="150" height="438" rx="0" fill="#f6f7fb"/>')
    for i in range(6):
        fill = accent if i == 0 else "#d5d9e3"
        s.append(f'<rect x="82" y="{188 + i * 48}" width="106" height="14" rx="7" fill="{fill}"/>')
    for i in range(3):
        x = 236 + i * 178
        s.append(f'<rect x="{x}" y="186" width="162" height="96" rx="16" fill="#f6f7fb"/><rect x="{x + 16}" y="204" width="60" height="9" rx="4.5" fill="#c3c9d6"/>'
                 f'<rect x="{x + 16}" y="228" width="{90 - i * 14}" height="22" rx="8" fill="{accent}" opacity="{1 - i * .22}"/>')
    s.append('<rect x="236" y="304" width="338" height="270" rx="16" fill="#f6f7fb"/>')
    for i, h in enumerate([70, 120, 90, 160, 130, 190, 150]):
        s.append(f'<rect x="{260 + i * 43}" y="{552 - h}" width="26" height="{h}" rx="8" fill="{accent}" opacity="{.35 + i * .09:.2f}"/>')
    s.append('<rect x="590" y="304" width="170" height="270" rx="16" fill="#f6f7fb"/>')
    s.append(f'<circle cx="675" cy="410" r="52" fill="none" stroke="#dde1ea" stroke-width="18"/><circle cx="675" cy="410" r="52" fill="none" stroke="{accent}" stroke-width="18" stroke-dasharray="210 330" stroke-linecap="round" transform="rotate(-90 675 410)"/>')
    s.append('<rect x="612" y="494" width="126" height="10" rx="5" fill="#c3c9d6"/><rect x="612" y="518" width="90" height="10" rx="5" fill="#dde1ea"/>')
    return "".join(s)


def _phone(accent, icon_name, x=690, y=230):
    dark = _mix(accent, "#000000", .3)
    s = [f'<g transform="translate({x} {y})">',
         '<rect width="270" height="520" rx="46" fill="#0b1220"/><rect x="10" y="10" width="250" height="500" rx="38" fill="#fff"/>',
         '<rect x="95" y="20" width="80" height="18" rx="9" fill="#0b1220"/>',
         f'<rect x="10" y="10" width="250" height="190" rx="38" fill="{accent}"/><rect x="10" y="120" width="250" height="80" fill="{accent}"/>',
         f'<circle cx="135" cy="104" r="42" fill="{dark}" opacity=".55"/>',
         _icon_g(icon_name, 105, 74, 2.5),
         '<rect x="80" y="160" width="110" height="12" rx="6" fill="#fff" opacity=".85"/>']
    for i in range(4):
        yy = 222 + i * 62
        s.append(f'<rect x="30" y="{yy}" width="210" height="50" rx="14" fill="#f3f4f8"/><circle cx="56" cy="{yy + 25}" r="12" fill="{accent}" opacity="{1 - i * .2}"/>'
                 f'<rect x="78" y="{yy + 14}" width="{110 - i * 8}" height="10" rx="5" fill="#c3c9d6"/><rect x="78" y="{yy + 31}" width="70" height="8" rx="4" fill="#dde1ea"/>')
    s.append("</g>")
    return "".join(s)


def art(accent, icon_name, chips, mode="dash"):
    c1 = _mix(accent, "#0b1220", .72)
    c2 = _mix(accent, "#0b1220", .35)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img">',
        f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>'
        f'<radialGradient id="gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{accent}" stop-opacity=".55"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>',
        '<rect width="1000" height="780" rx="40" fill="url(#bg)"/>',
        '<circle cx="880" cy="90" r="260" fill="url(#gl)"/><circle cx="60" cy="740" r="240" fill="url(#gl)"/>',
    ]
    for gx in range(0, 1000, 50):
        for gy in range(0, 780, 50):
            parts.append(f'<circle cx="{gx + 25}" cy="{gy + 25}" r="1.6" fill="#fff" opacity=".12"/>')
    parts.append(_window(accent, mode))
    if mode == "phones":
        parts = parts[:-1]
        parts.append(_phone(accent, icon_name, 70, 150))
        parts.append(_phone(_mix(accent, "#ffffff", .15), "pin", 360, 90))
        parts.append(_phone(_mix(accent, "#000000", .15), "clock", 650, 190))
    else:
        parts.append(_phone(accent, icon_name))
    pos = [(40, 650), (610, 70), (500, 668)]
    for (x, y), t in zip(pos, chips):
        parts.append(_chip(x, y, t, accent))
    parts.append("</svg>")
    return "".join(parts)
