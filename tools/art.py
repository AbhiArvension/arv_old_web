"""Generates modern, bespoke, high-resolution SVG illustrations and icon sprites for Arvension."""

import html

E = html.escape

BRAND = "#c8102e"
DARK_NAVY = "#060b14"
SLATE_CARD = "#0d1527"
SLATE_BORDER = "#1e293b"
TEXT_MUTED = "#94a3b8"
TEXT_LIGHT = "#f1f5f9"

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
    "cpu": "M4 4h16v16H4zM9 9h6v6H9zM9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 15h3M1 9h3M1 15h3",
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
    "search": "M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.35-4.35",
    "bell": "M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 0 1-3.46 0",
    "trend": "M23 6l-9.5 9.5-5-5L1 18M17 6h6v6",
    "qr": "M3 3h6v6H3zM15 3h6v6h-6zM3 15h6v6H3zM15 15h2v2h-2zM19 15h2v2h-2zM15 19h2v2h-2zM19 19h2v2h-2z",
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


def _path_icon(name, x, y, scale=1.0, color="#fff", sw=1.8):
    d = ICONS.get(name, ICONS["check"])
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></g>'


def _chip(x, y, text, color, icon_name="check"):
    w = max(180, len(text) * 9 + 64)
    return f"""
    <g transform="translate({x} {y})">
      <rect width="{w}" height="44" rx="22" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-chip)"/>
      <circle cx="22" cy="22" r="13" fill="{color}" opacity="0.15"/>
      <circle cx="22" cy="22" r="6" fill="{color}"/>
      <text x="42" y="27" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700" fill="#0f172a">{E(text)}</text>
    </g>"""


def _canvas_bg(accent, secondary="#2563eb"):
    return f"""
    <defs>
      <filter id="shadow-win" x="-10%" y="-10%" width="125%" height="125%">
        <feDropShadow dx="0" dy="24" stdDeviation="28" flood-color="#000000" flood-opacity="0.6"/>
      </filter>
      <filter id="shadow-phone" x="-15%" y="-10%" width="130%" height="125%">
        <feDropShadow dx="0" dy="28" stdDeviation="30" flood-color="#000000" flood-opacity="0.75"/>
      </filter>
      <filter id="shadow-chip" x="-10%" y="-20%" width="120%" height="150%">
        <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.25"/>
      </filter>
    </defs>
    <!-- Background Canvas -->
    <rect width="1000" height="780" rx="36" fill="#080e1a"/>
    
    <!-- Subtle architectural guidelines -->
    <g stroke="#ffffff" stroke-opacity="0.04" stroke-width="1">
      <line x1="0" y1="130" x2="1000" y2="130"/>
      <line x1="0" y1="260" x2="1000" y2="260"/>
      <line x1="0" y1="390" x2="1000" y2="390"/>
      <line x1="0" y1="520" x2="1000" y2="520"/>
      <line x1="0" y1="650" x2="1000" y2="650"/>
      <line x1="200" y1="0" x2="200" y2="780"/>
      <line x1="400" y1="0" x2="400" y2="780"/>
      <line x1="600" y1="0" x2="600" y2="780"/>
      <line x1="800" y1="0" x2="800" y2="780"/>
    </g>
    """


def _desktop_chrome(x, y, w, h, title, status_text="99.98% Synced", accent=BRAND):
    return f"""
    <!-- Desktop Window Base -->
    <g transform="translate({x} {y})" filter="url(#shadow-win)">
      <rect width="{w}" height="{h}" rx="20" fill="#0b1324" stroke="#1e293b" stroke-width="1.5"/>
      <!-- Window Title Bar -->
      <path d="M0 20C0 8.95 8.95 0 20 0h{w-40}c11.05 0 20 8.95 20 20v28H0V20z" fill="#111c33"/>
      <line x1="0" y1="48" x2="{w}" y2="48" stroke="#1e293b" stroke-width="1"/>
      <!-- Mac Window Buttons -->
      <circle cx="24" cy="24" r="6" fill="#ef4444"/>
      <circle cx="44" cy="24" r="6" fill="#f59e0b"/>
      <circle cx="64" cy="24" r="6" fill="#10b981"/>
      <!-- URL / Title Pill -->
      <g transform="translate(90 12)">
        <rect width="260" height="24" rx="12" fill="#070c17" stroke="#1e2a42" stroke-width="1"/>
        <text x="28" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="600" fill="#94a3b8">{E(title)}</text>
        {_path_icon("shield", 10, 5, 0.55, "#38bdf8", 2.0)}
      </g>
      <!-- Live Sync Pill -->
      <g transform="translate({w-150} 12)">
        <rect width="134" height="24" rx="12" fill="#070c17" stroke="{accent}" stroke-opacity="0.3" stroke-width="1"/>
        <circle cx="14" cy="12" r="4" fill="#22c55e"/>
        <text x="26" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#22c55e">{E(status_text)}</text>
      </g>
    """


def _desktop_sidebar(nav_items, active_idx=0, accent=BRAND):
    out = [f"""
    <!-- Sidebar -->
    <rect x="0" y="48" width="136" height="442" fill="#070c17" stroke-right="#1e293b" opacity="0.95"/>
    <line x1="136" y1="48" x2="136" y2="490" stroke="#1e293b" stroke-width="1"/>
    <!-- Brand mark -->
    <g transform="translate(18 64)">
      <rect width="28" height="28" rx="8" fill="{accent}"/>
      <text x="8" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">A</text>
      <text x="36" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="800" fill="#f8fafc">ARV</text>
    </g>
    """]
    y = 112
    for i, (ic, label) in enumerate(nav_items):
        is_active = (i == active_idx)
        if is_active:
            out.append(f"""
            <g transform="translate(10 {y})">
              <rect width="116" height="32" rx="8" fill="{accent}" fill-opacity="0.2" stroke="{accent}" stroke-opacity="0.5" stroke-width="1"/>
              {_path_icon(ic, 10, 7, 0.75, "#ffffff", 2.0)}
              <text x="32" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#ffffff">{E(label)}</text>
            </g>
            """)
        else:
            out.append(f"""
            <g transform="translate(10 {y})">
              {_path_icon(ic, 10, 7, 0.75, "#64748b", 1.8)}
              <text x="32" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="500" fill="#64748b">{E(label)}</text>
            </g>
            """)
        y += 42
    out.append("""
    <!-- User bottom avatar -->
    <g transform="translate(14 445)">
      <circle cx="14" cy="14" r="13" fill="#1e293b"/>
      <text x="9" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#94a3b8">HQ</text>
      <text x="34" y="13" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#cbd5e1">Technopark</text>
      <text x="34" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="500" fill="#64748b">Kerala, India</text>
    </g>
    """)
    return "".join(out)


def _kpi_boxes(boxes, start_x=152, start_y=64, w=144, h=66):
    out = []
    for i, (title, val, badge, color) in enumerate(boxes):
        x = start_x + i * (w + 12)
        out.append(f"""
        <g transform="translate({x} {start_y})">
          <rect width="{w}" height="{h}" rx="12" fill="#0e172c" stroke="#1e2d4a" stroke-width="1"/>
          <text x="12" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="600" fill="#94a3b8">{E(title)}</text>
          <text x="12" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="16" font-weight="800" fill="#f8fafc">{E(val)}</text>
          <g transform="translate(12 50)">
            <rect width="68" height="12" rx="6" fill="{color}" fill-opacity="0.18"/>
            <text x="6" y="9.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="{color}">{E(badge)}</text>
          </g>
        </g>
        """)
    return "".join(out)


def _phone_mockup(x, y, app_title, screen_content, accent=BRAND):
    return f"""
    <!-- Modern Smartphone Mockup -->
    <g transform="translate({x} {y})" filter="url(#shadow-phone)">
      <!-- Outer Metal Body -->
      <rect width="310" height="570" rx="46" fill="#020617" stroke="#334155" stroke-width="2.5"/>
      <!-- Inner Bezel -->
      <rect x="8" y="8" width="294" height="554" rx="40" fill="#090f1d"/>
      <!-- Screen Header with Dynamic Island -->
      <path d="M8 48C8 25.9 25.9 8 48 8h214c22.1 0 40 17.9 40 40v30H8V48z" fill="#050a14"/>
      <!-- Dynamic Island pill -->
      <rect x="105" y="18" width="100" height="24" rx="12" fill="#000000"/>
      <circle cx="188" cy="30" r="5" fill="#111827"/>
      <!-- Phone Status Bar -->
      <text x="36" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">9:41</text>
      <!-- Battery / Wifi icons -->
      <g transform="translate(242 24)">
        <rect width="20" height="11" rx="3.5" fill="none" stroke="#f8fafc" stroke-width="1.5"/>
        <rect x="2" y="2" width="13" height="7" rx="2" fill="#22c55e"/>
        <path d="M21 4v3" stroke="#f8fafc" stroke-width="1.5" stroke-linecap="round"/>
      </g>
      <!-- App Header Bar -->
      <g transform="translate(18 52)">
        <rect width="274" height="42" rx="10" fill="#0d1629"/>
        <circle cx="22" cy="21" r="12" fill="{accent}"/>
        <text x="17" y="25" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#fff">A</text>
        <text x="42" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="12.5" font-weight="700" fill="#ffffff">{E(app_title)}</text>
        <circle cx="250" cy="21" r="4" fill="#22c55e"/>
      </g>
      
      <!-- Custom Mobile Screen Content -->
      <g transform="translate(18 102)">
        {screen_content}
      </g>
      
      <!-- Mobile Bottom Tab Bar -->
      <g transform="translate(18 506)">
        <rect width="274" height="46" rx="14" fill="#070d18" stroke="#1e293b" stroke-width="1"/>
        <g transform="translate(32 14)">{_path_icon("chart", 0, 0, 0.8, accent, 2.0)}</g>
        <g transform="translate(100 14)">{_path_icon("pin", 0, 0, 0.8, "#64748b", 1.8)}</g>
        <g transform="translate(168 14)">{_path_icon("clock", 0, 0, 0.8, "#64748b", 1.8)}</g>
        <g transform="translate(236 14)">{_path_icon("user", 0, 0, 0.8, "#64748b", 1.8)}</g>
      </g>
      <!-- Home indicator bar -->
      <rect x="95" y="552" width="120" height="4" rx="2" fill="#475569"/>
    </g>
    """


# ============================================================================
# MASTER HERO ILLUSTRATION
# ============================================================================
def render_hero():
    accent = BRAND
    sec = "#2563eb"
    chips = ["Live Agent GPS Tracking", "Unlimited Branches & Staff", "AI Defaulter Risk Engine"]

    # Desktop Center Content: Analytics Chart + Live Operations Table
    desktop_inner = f"""
    <!-- KPI Row -->
    {_kpi_boxes([
        ("TOTAL TURNOVER", "₹2.84 Cr", "+18.4% MoM", "#22c55e"),
        ("ACTIVE BRANCHES", "48 Active", "100% Synced", "#38bdf8"),
        ("FIELD AGENTS", "142 Live", "GPS Online", "#a855f7"),
    ])}
    
    <!-- Central Area Performance Chart -->
    <g transform="translate(152 140)">
      <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Collection Performance (All Branches)</text>
      <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Real-time head office consolidation</text>
      
      <!-- Chart Area with Solid Accent Opacity -->
      <!-- Grid lines -->
      <line x1="20" y1="70" x2="300" y2="70" stroke="#1e293b" stroke-dasharray="3 3"/>
      <line x1="20" y1="105" x2="300" y2="105" stroke="#1e293b" stroke-dasharray="3 3"/>
      <line x1="20" y1="140" x2="300" y2="140" stroke="#1e293b" stroke-width="1"/>
      
      <!-- Area Fill -->
      <polygon points="20,140 20,118 65,108 110,116 155,92 200,98 245,68 290,52 290,140" fill="{accent}" fill-opacity="0.12"/>
      <!-- Curve Line -->
      <polyline points="20,118 65,108 110,116 155,92 200,98 245,68 290,52" fill="none" stroke="{accent}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
      
      <!-- Data Points & Tooltip -->
      <circle cx="200" cy="98" r="3.5" fill="#ffffff" stroke="{accent}" stroke-width="2"/>
      <circle cx="290" cy="52" r="4.5" fill="#ffffff" stroke="{accent}" stroke-width="2.5"/>
      <!-- Tooltip Tag -->
      <g transform="translate(225 24)">
        <rect width="68" height="20" rx="6" fill="#1e293b" stroke="{accent}" stroke-width="1"/>
        <text x="7" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#22c55e">₹42.8L (+24%)</text>
      </g>
      <!-- Month Axis -->
      <text x="20" y="156" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" fill="#64748b">MAY</text>
      <text x="75" y="156" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" fill="#64748b">JUN</text>
      <text x="135" y="156" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" fill="#64748b">JUL</text>
      <text x="195" y="156" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" fill="#64748b">AUG</text>
      <text x="250" y="156" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" fill="#38bdf8" font-weight="700">TODAY</text>
    </g>
    
    <!-- Real-time Live Operations Feed Table -->
    <g transform="translate(152 325)">
      <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Live Field Operations & Branch Ledger</text>
      <text x="360" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● AUTO-SYNC</text>
      
      <!-- Table Header -->
      <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
      <text x="18" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#64748b">BRANCH / CENTRE</text>
      <text x="160" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#64748b">MODULE</text>
      <text x="260" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#64748b">AMOUNT</text>
      <text x="360" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#64748b">STATUS</text>
      
      <!-- Row 1 -->
      <g transform="translate(16 56)">
        <rect width="438" height="26" rx="6" fill="#070c17" fill-opacity="0.6"/>
        <text x="8" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="600" fill="#f8fafc">Trivandrum City (Group 4)</text>
        <text x="144" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="500" fill="#94a3b8">Microfinance</text>
        <text x="244" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#f8fafc">₹45,000</text>
        <rect x="344" y="5" width="70" height="16" rx="8" fill="#10b981" fill-opacity="0.2"/>
        <text x="352" y="16.5" font-family="system-ui,-apple-system,sans-serif" font-size="8" font-weight="700" fill="#10b981">COLLECTED</text>
      </g>
      
      <!-- Row 2 -->
      <g transform="translate(16 86)">
        <rect width="438" height="26" rx="6" fill="#070c17" fill-opacity="0.6"/>
        <text x="8" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="600" fill="#f8fafc">Kochi Branch #12</text>
        <text x="144" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="500" fill="#94a3b8">Gold Loan Appraisal</text>
        <text x="244" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#f8fafc">₹1,85,000</text>
        <rect x="344" y="5" width="70" height="16" rx="8" fill="#38bdf8" fill-opacity="0.2"/>
        <text x="354" y="16.5" font-family="system-ui,-apple-system,sans-serif" font-size="8" font-weight="700" fill="#38bdf8">DISBURSED</text>
      </g>
      
      <!-- Row 3 -->
      <g transform="translate(16 116)">
        <rect width="438" height="26" rx="6" fill="#070c17" fill-opacity="0.6"/>
        <text x="8" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="600" fill="#f8fafc">St. Xavier's Transport</text>
        <text x="144" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="500" fill="#94a3b8">School Bus Route #4</text>
        <text x="244" y="17" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#f8fafc">32 Students</text>
        <rect x="344" y="5" width="70" height="16" rx="8" fill="#a855f7" fill-opacity="0.2"/>
        <text x="356" y="16.5" font-family="system-ui,-apple-system,sans-serif" font-size="8" font-weight="700" fill="#a855f7">LIVE GPS</text>
      </g>
    </g>
    """

    # Mobile Screen Content: Field Agent GPS Collection App
    mobile_content = f"""
    <!-- Agent Profile Card -->
    <rect width="274" height="64" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
    <circle cx="34" cy="32" r="18" fill="#1e293b"/>
    <text x="26" y="37" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="700" fill="#38bdf8">RM</text>
    <text x="62" y="27" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Rahul M. (Field Agent)</text>
    <text x="62" y="42" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Technopark Sector 4 • Route #8</text>
    <circle cx="248" cy="32" r="5" fill="#22c55e"/>

    <!-- Daily Collection Target Progress -->
    <g transform="translate(0 74)">
      <rect width="274" height="88" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
      <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="600" fill="#94a3b8">TODAY'S COLLECTIONS</text>
      <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="19" font-weight="800" fill="#f8fafc">₹38,500 <tspan font-size="11" font-weight="500" fill="#64748b">/ ₹45,000</tspan></text>
      <rect x="14" y="60" width="246" height="8" rx="4" fill="#1e293b"/>
      <rect x="14" y="60" width="210" height="8" rx="4" fill="{accent}"/>
      <text x="210" y="80" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="{accent}">85% COMPLETED</text>
    </g>

    <!-- Mini Live GPS Route Map Preview -->
    <g transform="translate(0 172)">
      <rect width="274" height="120" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
      <!-- Stylized vector roads -->
      <path d="M20 90 Q 70 30, 140 60 T 250 40" fill="none" stroke="#1e293b" stroke-width="12" stroke-linecap="round"/>
      <path d="M20 90 Q 70 30, 140 60 T 250 40" fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="6 4"/>
      <!-- Checkpoints -->
      <circle cx="20" cy="90" r="5" fill="#22c55e"/>
      <circle cx="100" cy="46" r="5" fill="#22c55e"/>
      <!-- Active GPS Pin with Pulse -->
      <circle cx="170" cy="58" r="14" fill="{accent}" fill-opacity="0.25"/>
      <circle cx="170" cy="58" r="6" fill="{accent}"/>
      <g transform="translate(14 16)">
        <rect width="116" height="20" rx="6" fill="#0b1324" stroke="#334155" stroke-width="1"/>
        <text x="8" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#38bdf8">📍 LIVE AGENT GPS</text>
      </g>
    </g>

    <!-- Next Customer Collection Card -->
    <g transform="translate(0 302)">
      <rect width="274" height="88" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
      <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#a855f7">NEXT COLLECTION (120m away)</text>
      <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Lakshmi Amma • SHG Unit 4</text>
      <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">Due: ₹1,500 <tspan font-size="9" font-weight="500" fill="#94a3b8">(Instalment #8)</tspan></text>
      <!-- Action button -->
      <g transform="translate(14 62)">
        <rect width="246" height="20" rx="6" fill="{accent}"/>
        <text x="74" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#ffffff">COLLECT &amp; ISSUE RECEIPT</text>
      </g>
    </g>
    """

    desktop_frame = _desktop_chrome(50, 110, 640, 500, "arvension.in/erp/head-office-hub", "48 Branches Online", accent)
    sidebar = _desktop_sidebar([
        ("chart", "Dashboard"),
        ("layers", "Branches"),
        ("db", "Ledger"),
        ("pin", "Agent GPS"),
        ("cpu", "AI Copilot"),
    ], active_idx=0, accent=accent)

    phone = _phone_mockup(646, 140, "Arvension Agent", mobile_content, accent)

    # 3 Floating Badges
    b1 = _chip(40, 660, chips[0], "#22c55e", "pin")
    b2 = _chip(610, 70, chips[1], "#38bdf8", "layers")
    b3 = _chip(480, 680, chips[2], accent, "cpu")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="Arvension AI ERP and Mobile Apps Ecosystem">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_inner}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


# ============================================================================
# BESPOKE PRODUCT GENERATOR
# ============================================================================
def render_product_svg(slug, color, icon_name, chips):
    accent = color
    sec = _mix(accent, "#2563eb", 0.5)

    # Industry-specific layouts
    if slug == "school-management-system":
        title = "School ERP & Transport Manager"
        status = "2,480 Students Online"
        nav = [("school", "School"), ("bus", "Transport"), ("clock", "Timetable"), ("user", "Parents"), ("shield", "Admin")]
        kpis = [
            ("TOTAL STUDENTS", "2,480", "98.2% Present", "#22c55e"),
            ("FEE COLLECTION", "94.8%", "Term 2 Synced", "#38bdf8"),
            ("BUS FLEET", "14 Active", "Live GPS", "#a855f7"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- Timetable & Class Attendance Matrix -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Daily Attendance &amp; Class Timetable</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Smart RFID &amp; App Punch-in</text>
          
          <g transform="translate(16 48)">
            <!-- Period 1 -->
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Grade 8-A</text>
            <text x="80" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Mathematics (Tr. Sarah)</text>
            <rect x="220" y="6" width="60" height="16" rx="8" fill="#22c55e" fill-opacity="0.2"/>
            <text x="228" y="17.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">42/42 HERE</text>
          </g>
          <g transform="translate(16 82)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#a855f7">Grade 9-B</text>
            <text x="80" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Physics Lab (Tr. Manoj)</text>
            <rect x="220" y="6" width="60" height="16" rx="8" fill="#22c55e" fill-opacity="0.2"/>
            <text x="228" y="17.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">38/40 HERE</text>
          </g>
          <g transform="translate(16 116)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#f59e0b">Grade 10-C</text>
            <text x="80" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">English Literature</text>
            <rect x="220" y="6" width="60" height="16" rx="8" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="232" y="17.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">IN CLASS</text>
          </g>
        </g>
        
        <!-- Live School Bus Transport Status -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Live School Transport Fleet GPS</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● 14 BUSES LIVE</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <circle cx="20" cy="18" r="10" fill="#f59e0b"/>
            <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="800" fill="#000">04</text>
            <text x="38" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Bus Route #4 (East Campus)</text>
            <text x="38" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Driver: Sasi K. • Speed: 32 km/h • Stop: Kowdiar Jct</text>
            <rect x="350" y="8" width="76" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="360" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">ON SCHEDULE</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <circle cx="20" cy="18" r="10" fill="#f59e0b"/>
            <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="800" fill="#000">07</text>
            <text x="38" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Bus Route #7 (Technopark Hub)</text>
            <text x="38" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Driver: Anil R. • Speed: 28 km/h • Stop: Kazhakuttom</text>
            <rect x="350" y="8" width="76" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="362" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">BOARDING</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <!-- Parent App Screen -->
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="#2563eb"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">AS</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Aarav Sharma</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Grade 8-A • Roll No. 14</text>
        
        <!-- Live School Bus Tracking on Map -->
        <g transform="translate(0 76)">
          <rect width="274" height="150" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <!-- Vector road -->
          <path d="M20 120 Q 80 40, 160 80 T 250 50" fill="none" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>
          <path d="M20 120 Q 80 40, 160 80 T 250 50" fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="6 4"/>
          <circle cx="160" cy="80" r="14" fill="#f59e0b" fill-opacity="0.3"/>
          <circle cx="160" cy="80" r="7" fill="#f59e0b"/>
          <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">🚌 LIVE SCHOOL BUS #4</text>
          <text x="14" y="36" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">2 Stops Away • ETA 4 mins</text>
          <!-- Punch in badge -->
          <g transform="translate(14 114)">
            <rect width="180" height="22" rx="6" fill="#0b1324" stroke="#22c55e" stroke-width="1"/>
            <text x="8" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#22c55e">✓ Boarded at 8:12 AM</text>
          </g>
        </g>
        
        <!-- Term Fee Card -->
        <g transform="translate(0 236)">
          <rect width="274" height="64" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#94a3b8">TERM 2 ACADEMIC FEES</text>
          <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="15" font-weight="800" fill="#22c55e">Paid ₹18,500 ✓</text>
          <text x="190" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">RECEIPT</text>
        </g>
        """
        app_name = "Arvension Parent"

    elif slug == "college-management-system":
        title = "College Academic & Examination ERP"
        status = "3,820 Students Online"
        nav = [("college", "Academics"), ("chart", "Exams"), ("user", "Faculty"), ("award", "Placement"), ("shield", "Admin")]
        kpis = [
            ("DEPARTMENTS", "8 Active", "Accredited", "#a855f7"),
            ("EXAM PUBLISHED", "Sem 1-8", "100% Results", "#22c55e"),
            ("PLACEMENTS", "91.4%", "412 Offers", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- Academic Semesters & CGPA Matrix -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Semester Internal Assessment &amp; Credits</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">University Evaluation Rules Configured</text>
          
          <!-- Bar comparison -->
          <g transform="translate(16 54)">
            <text x="0" y="12" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Computer Science (CSE)</text>
            <rect x="0" y="18" width="220" height="8" rx="4" fill="{accent}"/>
            <text x="230" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">8.84 CGPA</text>
          </g>
          <g transform="translate(16 90)">
            <text x="0" y="12" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Electronics (ECE)</text>
            <rect x="0" y="18" width="190" height="8" rx="4" fill="#38bdf8"/>
            <text x="230" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">8.42 CGPA</text>
          </g>
          <g transform="translate(16 126)">
            <text x="0" y="12" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Mechanical Engineering</text>
            <rect x="0" y="18" width="170" height="8" rx="4" fill="#f59e0b"/>
            <text x="230" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">8.15 CGPA</text>
          </g>
        </g>
        
        <!-- Faculty Workload & Hall Ticket Release -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Faculty Schedule &amp; Hall Allocation</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#a855f7">● SEMESTER EXAMS</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Dr. K. Narayanan • Cloud Architecture Exam</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Hall 302 • 120 Candidates Registered • Invigilator Ready</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">VERIFIED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Prof. Priya George • Data Structures Internal</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Lab 4 • 64 Candidates • Marks Auto-Synced to University Portal</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">SUBMITTED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">AK</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Aditi K. (B.Tech CS)</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Sem 6 • Roll #48 • CGPA: 9.12</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="{accent}">INTERNAL ASSESSMENT</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="20" font-weight="800" fill="#22c55e">48 / 50 <tspan font-size="11" font-weight="500" fill="#94a3b8">(Distinction)</tspan></text>
          <text x="14" y="70" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#f8fafc">Attendance: 93.4% (Eligible for Exams)</text>
          <g transform="translate(14 80)">
            <rect width="246" height="20" rx="6" fill="#1e293b"/>
            <text x="60" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#38bdf8">VIEW DIGITAL HALL TICKET</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">UPCOMING CAMPUS DRIVE</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Infosys Systems Engineer • ₹6.5 LPA</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Shortlisted for Technical Round ✓</text>
        </g>
        """
        app_name = "Arvension College"

    elif slug == "microfinance-erp":
        title = "Microfinance MFI Group Lending ERP"
        status = "184 Centres Live"
        nav = [("microfinance", "Centres"), ("chart", "Collections"), ("pin", "Field GPS"), ("db", "Disbursement"), ("shield", "Admin")]
        kpis = [
            ("DISBURSED MTD", "₹1.62 Cr", "Zero Defaults", "#22c55e"),
            ("PAR > 30 DAYS", "0.38%", "Low Risk", "#38bdf8"),
            ("ACTIVE CENTRES", "184 Centres", "100% Synced", "#16a34a"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- JLG / SHG Collection Sheet Console -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">JLG / SHG Centre Demand Sheet</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Real-time live field collections</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#22c55e">Centre #12 (Kowdiar)</text>
            <text x="140" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">₹32,000 / ₹32,000</text>
            <circle cx="270" cy="14" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 82)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Centre #14 (Pattom)</text>
            <text x="140" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">₹28,500 / ₹28,500</text>
            <circle cx="270" cy="14" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 116)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#f59e0b">Centre #18 (Kazhakuttom)</text>
            <text x="140" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">₹24,000 In Progress</text>
            <circle cx="270" cy="14" r="5" fill="#f59e0b"/>
          </g>
        </g>
        
        <!-- Live Field Agent Routing & PAR Monitor -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Field Collections &amp; Instant Receipt Ledger</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● REAL-TIME GPS</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Sunitha P. • SHG Unit 2</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Agent: Deepu V. • Loan #MF-4091 • Biometric Authenticated</text>
            <text x="280" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">₹1,200 PAID</text>
            <rect x="370" y="8" width="56" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="378" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">SYNCED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Kusumam R. • SHG Unit 5</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Agent: Deepu V. • Loan #MF-3820 • WhatsApp Receipt Triggered</text>
            <text x="280" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">₹1,500 PAID</text>
            <rect x="370" y="8" width="56" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="378" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">SYNCED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="64" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="32" r="18" fill="{accent}"/>
        <text x="26" y="37" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="700" fill="#fff">DV</text>
        <text x="62" y="27" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Deepu V. (Field Agent)</text>
        <text x="62" y="42" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Centre #14 • 18 / 20 Collected</text>
        
        <g transform="translate(0 74)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">📍 LIVE AGENT GPS ROUTE</text>
          <path d="M20 80 Q 80 30, 150 60 T 240 40" fill="none" stroke="#1e293b" stroke-width="10" stroke-linecap="round"/>
          <path d="M20 80 Q 80 30, 150 60 T 240 40" fill="none" stroke="#22c55e" stroke-width="3"/>
          <circle cx="150" cy="60" r="12" fill="#22c55e" fill-opacity="0.3"/>
          <circle cx="150" cy="60" r="6" fill="#22c55e"/>
          <text x="14" y="100" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#38bdf8">Next Stop: Centre #15 (200m away)</text>
        </g>
        
        <g transform="translate(0 194)">
          <rect width="274" height="84" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#94a3b8">RECORD COLLECTION</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Radha S. (Kudumbashree #4)</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="800" fill="#22c55e">Collect ₹1,200</text>
          <g transform="translate(14 60)">
            <rect width="246" height="18" rx="6" fill="{accent}"/>
            <text x="80" y="13" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#fff">PRINT RECEIPT</text>
          </g>
        </g>
        """
        app_name = "Arvension Field Agent"

    elif slug == "gold-loan-erp":
        title = "Gold Loan Appraisal & Vault ERP"
        status = "Vault Audit: Verified"
        nav = [("gold", "Appraisal"), ("shield", "Vault"), ("chart", "Interest"), ("user", "Customers"), ("db", "Ledger")]
        kpis = [
            ("GOLD IN VAULT", "48.6 kg", "100% Verified", "#eab308"),
            ("LOAN PORTFOLIO", "₹5.20 Cr", "Daily Accrual", "#22c55e"),
            ("22K GOLD RATE", "₹6,920/g", "+₹40 Today", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- Digital Gold Appraisal Sheet -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Digital Gold Appraisal &amp; Purity Sheet</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Automated LTV Calculation &amp; Packet Seal</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#eab308">Bangles (4 pcs)</text>
            <text x="110" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#f8fafc">Gross: 48.2g • Net: 45.8g</text>
            <text x="240" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">916 KDM</text>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#eab308">Chain &amp; Locket</text>
            <text x="110" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#f8fafc">Gross: 24.5g • Net: 23.2g</text>
            <text x="240" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">916 KDM</text>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Max LTV Sanction (75%):</text>
            <text x="140" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="800" fill="#f8fafc">₹2,35,000</text>
            <rect x="230" y="2" width="58" height="16" rx="8" fill="#eab308" fill-opacity="0.2"/>
            <text x="238" y="13" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#eab308">APPROVED</text>
          </g>
        </g>
        
        <!-- Vault Locker & Packet Audit Console -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Vault Locker Tracking &amp; Packet Audit</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#eab308">● BIOMETRIC LOCK</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Packet #GL-9021 • Suresh Babu</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Locker B-4 • Barcode Verified • Net Weight: 45.80g</text>
            <text x="280" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">₹2,35,000</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">IN VAULT</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Packet #GL-9024 • Mini Thomas</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Locker B-6 • Appraisal Complete • Net Weight: 32.10g</text>
            <text x="280" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">₹1,65,000</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="370" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">SEALED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">GL</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Suresh Babu</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Loan #GL-9021 • Locker B-4</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">ACTIVE GOLD LOAN</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="19" font-weight="800" fill="#f8fafc">₹2,35,000</text>
          <text x="14" y="68" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#94a3b8">Daily Interest: ₹63.50 • Due: ₹2,150</text>
          <g transform="translate(14 78)">
            <rect width="246" height="20" rx="6" fill="{accent}"/>
            <text x="60" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#fff">PAY INTEREST / RENEW ONLINE</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">GOLD PACKET AUDIT</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">48.2g (4 Bangles) Hallmarked 916</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Safe in Technopark Main Vault ✓</text>
        </g>
        """
        app_name = "Arvension Gold Loan"

    elif slug == "chit-fund-erp":
        title = "Chit Fund Auction & Subscriber ERP"
        status = "36 Active Groups"
        nav = [("chit", "Chit Groups"), ("chart", "Auctions"), ("db", "Dividends"), ("user", "Subscribers"), ("shield", "Admin")]
        kpis = [
            ("RUNNING GROUPS", "36 Groups", "100% Filled", "#db2777"),
            ("MONTHLY VOLUME", "₹94.5L", "+12.2% Growth", "#22c55e"),
            ("SUBSCRIBERS", "1,820", "Active Ledger", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- Live Chit Auction Console -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Live Digital Auction Console</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Group #CF-25L (25 Months • 25 Members)</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#db2777">Chit Value</text>
            <text x="120" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#f8fafc">₹25,00,000</text>
            <rect x="220" y="6" width="60" height="18" rx="6" fill="#22c55e" fill-opacity="0.2"/>
            <text x="228" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">MONTH 8</text>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#f59e0b">Lowest Bid (25%)</text>
            <text x="120" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#f59e0b">₹6,25,000</text>
            <text x="210" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Prize: ₹18.75L</text>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Dividend Per Member:</text>
            <text x="140" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="800" fill="#22c55e">₹12,500 Credited</text>
          </g>
        </g>
        
        <!-- Subscriber Instalment Ledger -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Subscriber Payment &amp; Dividend Ledger</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#db2777">● AUTO-DIVIDEND</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Mohan Kumar • Ticket #14 (CF-25L)</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Due: ₹87,500 (Gross ₹1,00,000 - Dividend ₹12,500) • Paid Online</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">CLEARED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Anil Rajan • Ticket #19 (CF-10L)</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Due: ₹40,000 (Dividend ₹10,000 Deducted) • Agent Collected</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">CLEARED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">MK</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Mohan Kumar</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Ticket #14 • Group CF-25L</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">MONTH 8 INSTALMENT</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="19" font-weight="800" fill="#f8fafc">₹87,500 <tspan font-size="10" font-weight="500" fill="#22c55e">(-₹12,500 Dividend)</tspan></text>
          <g transform="translate(14 74)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="80" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">PAY VIA UPI / NETBANKING</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">NEXT LIVE AUCTION</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Tomorrow at 4:30 PM IST</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Online Bidding Enabled on Mobile App ✓</text>
        </g>
        """
        app_name = "Arvension Chit Fund"

    elif slug == "nidhi-company-erp":
        title = "Nidhi Company Banking & Deposit ERP"
        status = "NDH-1 & NDH-3 Compliant"
        nav = [("nidhi", "Members"), ("db", "Deposits"), ("chart", "Loans"), ("shield", "Compliance"), ("user", "Directors")]
        kpis = [
            ("TOTAL MEMBERS", "6,420", "+120 This Month", "#0d9488"),
            ("DEPOSIT BASE", "₹12.4 Cr", "FD & RD Synced", "#22c55e"),
            ("LOAN ASSETS", "₹9.8 Cr", "Gold & Property", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- Member Deposit Schemes Console -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Deposit Schemes &amp; Interest Accrual</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Automated Monthly Compounding &amp; TDS</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#0d9488">Fixed Deposit (FD)</text>
            <text x="120" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">11.5% p.a. • ₹7.8 Cr Active</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Recurring (RD)</text>
            <text x="120" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">10.5% p.a. • Daily / Monthly</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">NOF Ratio:</text>
            <text x="65" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">1:16.4 (Compliant &lt; 1:20)</text>
            <rect x="220" y="2" width="68" height="16" rx="8" fill="#22c55e" fill-opacity="0.2"/>
            <text x="226" y="13" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">NDH PASS</text>
          </g>
        </g>
        
        <!-- Loan Approvals & Cash Console -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Branch Cash Balancing &amp; Loan Approvals</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#0d9488">● DIRECTOR QUEUE</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Loan #ND-402 • Member: Rajendran Nair</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Loan against Property Security • Valued at ₹18.5L • Sanction ₹6.5L</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#f59e0b" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#f59e0b">APPROVAL</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">10% Unencumbered Deposits</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Scheduled Commercial Bank Safe Custody • ₹1.24 Cr Deposited</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">VERIFIED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">DIR</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Board Director</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Executive Mobile Console</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">TOTAL BRANCH CASH</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="19" font-weight="800" fill="#f8fafc">₹34.2 Lakhs</text>
          <text x="14" y="68" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">All 8 Branch Day-End Safes Balanced ✓</text>
          <g transform="translate(14 76)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="68" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">1-TAP LOAN APPROVALS (2)</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">REGULATORY RATIOS</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">NDH-1 &amp; NDH-3 Auto-Calculated</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Ready for Ministry of Corporate Affairs ✓</text>
        </g>
        """
        app_name = "Arvension Director"

    elif slug == "multi-state-cooperative-society-erp":
        title = "Multi-State Co-Operative Society ERP"
        status = "Multi-State Consolidation Active"
        nav = [("coop", "Societies"), ("layers", "States"), ("db", "Ledger"), ("chart", "Pigmy"), ("shield", "Board")]
        kpis = [
            ("ACTIVE STATES", "Kerala & TN", "32 Branches", "#be123c"),
            ("SHARE CAPITAL", "₹14.8 Cr", "Audit Certified", "#22c55e"),
            ("TOTAL MEMBERS", "22,400", "Tier 1 Capital", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">State-Wise Branch Consolidation</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Multi-State Society Hierarchy</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#be123c">Kerala Region</text>
            <text x="110" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">18 Branches • ₹8.4 Cr Turnover</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Tamil Nadu Region</text>
            <text x="110" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">14 Branches • ₹6.4 Cr Turnover</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Annual Member Dividend:</text>
            <text x="135" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">12% Approved at AGM</text>
          </g>
        </g>
        
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Daily Pigmy Collection &amp; Member Shares</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#be123c">● LIVE LEDGER</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">K. Vasudevan • Member #MSCS-8812</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Pigmy Daily Deposit ₹300 • Agent #12 Collected • Sync 10:14 AM</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">POSTED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Co-operative Thrift Loan Disbursement</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Branch: Coimbatore Main • 24 Loan Accounts Processed</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">COMPLETE</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">KV</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">K. Vasudevan</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Member ID: #MSCS-8812</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">SAVINGS &amp; SHARE CAPITAL</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="19" font-weight="800" fill="#f8fafc">₹2,10,400</text>
          <text x="14" y="68" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Daily Pigmy: ₹300 Collected Today ✓</text>
          <g transform="translate(14 76)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="64" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">VIEW PASSBOOK ENTRIES</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">ANNUAL DIVIDEND</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">12% Dividend Credited to Savings</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Society Audit Passed ✓</text>
        </g>
        """
        app_name = "Arvension Member App"

    elif slug == "construction-management-system":
        title = "Construction ERP & BOQ Cost Control"
        status = "8 Active Sites Online"
        nav = [("construction", "Projects"), ("chart", "BOQ Cost"), ("clock", "Attendance"), ("db", "Materials"), ("shield", "Billing")]
        kpis = [
            ("ACTIVE SITES", "8 Projects", "₹48 Cr Underway", "#d97706"),
            ("BOQ VARIANCE", "-2.1% On Track", "Zero Cost Overrun", "#22c55e"),
            ("SITE LABOUR", "320 Present", "GPS Verified", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Project BOQ &amp; Cost Estimation</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Skyline Towers • Foundation &amp; Structure</text>
          
          <g transform="translate(16 54)">
            <text x="0" y="12" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">TMT Steel (Fe 550D) - 48 MT</text>
            <rect x="0" y="18" width="220" height="8" rx="4" fill="{accent}"/>
            <text x="230" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">92% Utilized</text>
          </g>
          <g transform="translate(16 90)">
            <text x="0" y="12" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Ready Mix Concrete (M30) - 420 m³</text>
            <rect x="0" y="18" width="180" height="8" rx="4" fill="#38bdf8"/>
            <text x="230" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">85% Poured</text>
          </g>
          <g transform="translate(16 126)">
            <text x="0" y="12" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Masonry &amp; AAC Blocks</text>
            <rect x="0" y="18" width="140" height="8" rx="4" fill="#22c55e"/>
            <text x="230" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">60% Complete</text>
          </g>
        </g>
        
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Site Biometric Labour &amp; Vendor RA Bills</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#d97706">● GEO-FENCED</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Technopark Phase 4 Site • Labour Strength: 84</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Supervisor: Jijo Paul • GPS Geo-Fence Verified • Selfie Attendance ✓</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">VERIFIED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">RA Bill #4 • Steel Fabrication Subcontractor</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Certified ₹4,80,000 • 5% Retention Deducted • Ready for Payment</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">CERTIFIED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">SE</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Site Engineer App</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Technopark Phase 4 Project</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">SITE LABOUR ATTENDANCE</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="19" font-weight="800" fill="#22c55e">48 Present <tspan font-size="10" font-weight="500" fill="#94a3b8">/ 50 Registered</tspan></text>
          <text x="14" y="68" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Geo-fenced within 100m perimeter ✓</text>
          <g transform="translate(14 76)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="74" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">SUBMIT DAILY DPR</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">MATERIAL GRN RECEIPT</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">200 Bags UltraTech Cement Inwarded</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">PO #PO-9912 Verified by Store ✓</text>
        </g>
        """
        app_name = "Arvension Site App"

    elif slug == "store-management-system":
        title = "Store & Inventory Multi-Warehouse ERP"
        status = "14,200 SKUs Managed"
        nav = [("store", "Inventory"), ("qr", "Barcode"), ("db", "Stock Ledger"), ("chart", "Reorders"), ("shield", "Audits")]
        kpis = [
            ("TOTAL SKUs", "14,200", "Multi-Store", "#4f46e5"),
            ("REORDER ALERTS", "8 Critical", "Auto-Indent", "#f59e0b"),
            ("INVENTORY VAL", "₹1.82 Cr", "FIFO Costing", "#22c55e"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Multi-Warehouse Inventory Stock</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Real-time Central and Site Depots</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#4f46e5">Central Warehouse</text>
            <text x="130" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">9,840 Items • ₹1.24 Cr</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Campus Depot A</text>
            <text x="130" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">2,420 Items • ₹34.5L</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Barcode Scanner:</text>
            <text x="100" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">QR &amp; Code128 Ready</text>
          </g>
        </g>
        
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Goods Receipt Note (GRN) &amp; Issue Ledger</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#4f46e5">● LIVE SCAN</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">GRN #GRN-4420 • Industrial Copper Cable 2.5mm</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Vendor: Havells India • 50 Coils • Batch #HC-88 • Barcode Printed</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">RECEIVED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Inter-Store Transfer #TR-102</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Central Warehouse → Site Store B • 12 Items In Transit</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="366" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">IN TRANSIT</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">SK</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Storekeeper Terminal</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Handheld Barcode Reader</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">BARCODE SCANNED</text>
          <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="15" font-weight="800" fill="#f8fafc">Copper Cable 2.5mm</text>
          <text x="14" y="64" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#22c55e">Stock: 42 Coils • Bin: Rack B-12</text>
          <g transform="translate(14 74)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="74" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">ISSUE TO DEPARTMENT</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#f59e0b">AUTO REORDER ALERT</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">TMT Rebar 12mm below min buffer</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#38bdf8">Purchase Indent Auto-Created ✓</text>
        </g>
        """
        app_name = "Arvension Store"

    elif slug == "hostel-management-system":
        title = "Hostel Resident & Room Allocation ERP"
        status = "650 Beds • 94.2% Occupied"
        nav = [("hostel", "Rooms"), ("user", "Residents"), ("clock", "Outpass"), ("chart", "Dues"), ("shield", "Warden")]
        kpis = [
            ("TOTAL CAPACITY", "650 Beds", "94.2% Occupancy", "#0891b2"),
            ("OUTPASS TODAY", "14 Approved", "Parent Notified", "#22c55e"),
            ("FEE COLLECTION", "96.8%", "Mess Integrated", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Bed Matrix (Block B • Floor 2)</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Interactive Room &amp; Bed Occupancy</text>
          
          <g transform="translate(16 54)">
            <rect width="66" height="42" rx="6" fill="#070c17" stroke="#22c55e" stroke-width="1"/>
            <text x="8" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">Room 201</text>
            <text x="8" y="32" font-family="system-ui,-apple-system,sans-serif" font-size="8" fill="#22c55e">2/2 Full</text>
          </g>
          <g transform="translate(90 54)">
            <rect width="66" height="42" rx="6" fill="#070c17" stroke="#22c55e" stroke-width="1"/>
            <text x="8" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">Room 202</text>
            <text x="8" y="32" font-family="system-ui,-apple-system,sans-serif" font-size="8" fill="#22c55e">2/2 Full</text>
          </g>
          <g transform="translate(164 54)">
            <rect width="66" height="42" rx="6" fill="#070c17" stroke="#38bdf8" stroke-width="1"/>
            <text x="8" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">Room 203</text>
            <text x="8" y="32" font-family="system-ui,-apple-system,sans-serif" font-size="8" fill="#38bdf8">1 Bed Free</text>
          </g>
          <g transform="translate(238 54)">
            <rect width="66" height="42" rx="6" fill="#070c17" stroke="#f59e0b" stroke-width="1"/>
            <text x="8" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#f8fafc">Room 204</text>
            <text x="8" y="32" font-family="system-ui,-apple-system,sans-serif" font-size="8" fill="#f59e0b">Leave (1)</text>
          </g>
          
          <g transform="translate(16 114)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Warden Night Rollcall:</text>
            <text x="125" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">100% Accounted For ✓</text>
          </g>
        </g>
        
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Digital Leave &amp; Outpass Approval Queue</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#0891b2">● QR GATE PASS</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Ananya M. • Room 204-B (Block B)</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Weekend Home Visit • Parent Consent Received on WhatsApp • Gate Pass QR Ready</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">APPROVED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Gokul R. • Room 108-A (Block A)</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Library Late Study Pass • Valid till 10:30 PM • Warden Approved</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">ACTIVE</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">AM</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Ananya M.</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Room 204-B • Block B</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">DIGITAL OUTPASS PASS</text>
          <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="15" font-weight="800" fill="#22c55e">Weekend Leave Approved ✓</text>
          <text x="14" y="64" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#f8fafc">Valid till Sunday 8:00 PM</text>
          <g transform="translate(14 74)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="74" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">SHOW GATE PASS QR</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">HOSTEL &amp; MESS DUES</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Monthly Rent &amp; Mess: Paid ✓</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Zero Dues • Digital Receipt Generated</text>
        </g>
        """
        app_name = "Arvension Resident"

    elif slug == "library-management-system":
        title = "Library Automation & Circulation ERP"
        status = "38,500 Books Catalogued"
        nav = [("library", "Catalogue"), ("qr", "Circulation"), ("user", "Members"), ("clock", "Overdue"), ("shield", "Stock Audit")]
        kpis = [
            ("TOTAL TITLES", "38,500 Books", "Dewey Decimal", "#059669"),
            ("CIRCULATION", "1,840 Issued", "Barcode Fast Scan", "#22c55e"),
            ("OVERDUE ALERTS", "WhatsApp Sent", "Auto-Fine Ready", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Rapid Circulation &amp; Check-out Desk</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Barcode Scanner &amp; Student ID Matching</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#059669">Artificial Intelligence</text>
            <text x="120" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Russell • Due: 18 Nov</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Database Systems</text>
            <text x="120" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Silberschatz • Due: 22 Nov</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Automated Overdue Fine:</text>
            <text x="140" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">WhatsApp Notice Triggered</text>
          </g>
        </g>
        
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Digital Accession Register &amp; Stock Verification</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#059669">● BARCODE VERIFIED</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Accession #ACC-28941 • Clean Architecture (Martin)</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Shelf B-4 • Borrowed by Rahul S. (Roll #402) • Returned in Mint Condition</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">CHECK-IN</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Online Reservation Queue</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Deep Learning (Goodfellow) • 2 Members Waiting • Notification Sent</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="366" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">RESERVED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">RS</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Rahul S.</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Library Member ID: #LIB-402</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">ACTIVE BORROWED BOOK</text>
          <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#f8fafc">AI Modern Approach</text>
          <text x="14" y="64" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#22c55e">Due: 18 Nov 2026 (7 Days Left)</text>
          <g transform="translate(14 74)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="74" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">1-CLICK BOOK RENEWAL</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">DIGITAL CATALOGUE SEARCH</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">38,500 Volumes Accessible on Phone</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Instant Reserve &amp; e-Book Portal ✓</text>
        </g>
        """
        app_name = "Arvension Library"

    elif slug == "mess-management-system":
        title = "Mess & Canteen Meal Token ERP"
        status = "1,280 Meals Served Today"
        nav = [("mess", "Meal Planner"), ("qr", "Tokens"), ("db", "Kitchen Stock"), ("chart", "Rebates"), ("shield", "Billing")]
        kpis = [
            ("MEALS TODAY", "1,280 Served", "RFID/QR Counted", "#ea580c"),
            ("COST PER MEAL", "₹48.50", "Per-Head Exact", "#22c55e"),
            ("KITCHEN BUFFER", "4 Days Stock", "Zero Food Waste", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Weekly Meal Menu &amp; Calorie Costing</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Breakfast • Lunch • Evening Tea • Dinner</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#ea580c">Today's Lunch</text>
            <text x="110" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Kerala Sadhya • 420 Count</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 84)">
            <rect width="288" height="30" rx="6" fill="#070c17"/>
            <text x="10" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Dinner Plan</text>
            <text x="110" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Chapati &amp; Paneer • 390 Count</text>
            <circle cx="270" cy="15" r="5" fill="#22c55e"/>
          </g>
          
          <g transform="translate(16 122)">
            <text x="0" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Automated Leave Rebates:</text>
            <text x="140" y="14" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#22c55e">42 Students Credited ✓</text>
          </g>
        </g>
        
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Live Counter QR Token Scanning &amp; Kitchen Stock</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#ea580c">● RFID SCANNER</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Counter #1 RFID Scan • Student Roll #104</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Meal Token Issued: Special Fish Curry Lunch • Scanned at 1:12 PM</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">ISSUED</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Kitchen Grocery Purchase &amp; Wastage Audit</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Rice, Vegetables &amp; Dairy Recorded • Zero Discrepancy with Supplier GRN</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="368" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">AUDITED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        <text x="28" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#fff">MS</text>
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Hostel Mess App</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">College Canteen Token</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">TODAY'S LUNCH SPECIAL</text>
          <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="15" font-weight="800" fill="#f8fafc">Kerala Sadhya Meals</text>
          <text x="14" y="64" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#22c55e">QR Token Punched at 1:15 PM ✓</text>
          <g transform="translate(14 74)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="74" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">APPLY FOR LEAVE REBATE</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">MESS BILL REBATES</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Approved Outpass Auto-Credited</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Fair Billing based on Actual Meals ✓</text>
        </g>
        """
        app_name = "Arvension Mess"

    else:
        # Fallback
        title = f"{slug.replace('-', ' ').title()} Portal"
        status = "100% Cloud Synced"
        nav = [(icon_name, "Overview"), ("chart", "Analytics"), ("db", "Records"), ("clock", "Attendance"), ("shield", "Admin")]
        kpis = [
            ("TOTAL RECORDS", "14,850", "Live Cloud", accent),
            ("EFFICIENCY", "99.4%", "+22% Improved", "#22c55e"),
            ("SYSTEM STATUS", "Active", "Zero Downtime", "#38bdf8"),
        ]
        desktop_center = f"""
        {_kpi_boxes(kpis)}
        <!-- Real-time Enterprise Workspace -->
        <g transform="translate(152 140)">
          <rect width="320" height="175" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Operational Dashboard &amp; Workflows</text>
          <text x="16" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="500" fill="#94a3b8">Multi-branch and mobile app integration</text>
          
          <g transform="translate(16 48)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="{accent}">Workflow Step 1</text>
            <text x="110" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Inward &amp; Verification</text>
            <circle cx="270" cy="14" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 82)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">Workflow Step 2</text>
            <text x="110" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Ledger Posting</text>
            <circle cx="270" cy="14" r="5" fill="#22c55e"/>
          </g>
          <g transform="translate(16 116)">
            <rect width="288" height="28" rx="6" fill="#070c17"/>
            <text x="10" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#f59e0b">Workflow Step 3</text>
            <text x="110" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">Audit Trail Certified</text>
            <circle cx="270" cy="14" r="5" fill="#22c55e"/>
          </g>
        </g>
        
        <!-- Live Operations Feed -->
        <g transform="translate(152 325)">
          <rect width="470" height="152" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
          <text x="16" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="11.5" font-weight="700" fill="#f8fafc">Live Transactions &amp; Mobile Activity Log</text>
          <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="{accent}">● AUTO-AUDIT</text>
          <line x1="16" y1="36" x2="454" y2="36" stroke="#1e293b" stroke-width="1"/>
          
          <g transform="translate(16 52)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Technopark Branch • Active Session #104</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Mobile Punch-in Verified • Geo-Location Confirmed</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">ACTIVE</text>
          </g>
          <g transform="translate(16 98)">
            <rect width="438" height="36" rx="8" fill="#070c17"/>
            <text x="12" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Automated Daily Reconciliation</text>
            <text x="12" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Zero Discrepancy • Ready for Director Review</text>
            <rect x="360" y="8" width="66" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
            <text x="372" y="21.5" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">PASSED</text>
          </g>
        </g>
        """
        mobile_inner = f"""
        <rect width="274" height="66" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
        <circle cx="34" cy="33" r="18" fill="{accent}"/>
        {_path_icon(icon_name, 24, 23, 0.8, '#fff', 2.0)}
        <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Mobile Workspace</text>
        <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="500" fill="#94a3b8">Real-time Cloud Sync</text>
        
        <g transform="translate(0 76)">
          <rect width="274" height="110" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
          <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="{accent}">QUICK ACTION</text>
          <text x="14" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="16" font-weight="800" fill="#f8fafc">Instant Mobile Record</text>
          <text x="14" y="68" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Selfie &amp; GPS Punch-in Verified ✓</text>
          <g transform="translate(14 76)">
            <rect width="246" height="22" rx="6" fill="{accent}"/>
            <text x="80" y="15" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#fff">OPEN DETAILS</text>
          </g>
        </g>
        
        <g transform="translate(0 196)">
          <rect width="274" height="80" rx="14" fill="#0e172a" stroke="#1e293b" stroke-width="1"/>
          <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#38bdf8">SYSTEM AUDIT</text>
          <text x="14" y="38" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Unlimited Branches &amp; Staff</text>
          <text x="14" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Data Synced to Head Office ✓</text>
        </g>
        """
        app_name = f"Arvension {slug.split('-')[0].capitalize()}"

    desktop_frame = _desktop_chrome(50, 110, 640, 500, f"arvension.in/erp/{slug}", status, accent)
    sidebar = _desktop_sidebar(nav, active_idx=0, accent=accent)
    phone = _phone_mockup(646, 140, app_name, mobile_inner, accent)

    b1 = _chip(40, 660, chips[0], accent, "check")
    b2 = _chip(610, 70, chips[1], "#38bdf8", "layers")
    b3 = _chip(480, 680, chips[2], "#22c55e", "check")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="{E(slug)} illustration">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_center}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


# ============================================================================
# SERVICE ILLUSTRATIONS
# ============================================================================
def render_ai_chat():
    accent = "#7c3aed"
    sec = "#db2777"
    chips = ["24/7 AI Lead Assistant", "Instant WhatsApp Bot", "Multilingual Support"]

    desktop_inner = f"""
    {_kpi_boxes([
        ("CONVERSATIONS", "18,420", "24/7 Active", "#22c55e"),
        ("LEADS CAPTURED", "1,240", "WhatsApp Synced", "#a855f7"),
        ("RESPONSE TIME", "0.4s", "Instant AI", "#38bdf8"),
    ])}
    
    <!-- AI Conversation Console -->
    <g transform="translate(152 140)">
      <rect width="470" height="338" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="18" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Arvension AI Copilot • Customer Live Stream</text>
      <text x="360" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● COPILOT ACTIVE</text>
      <line x1="18" y1="36" x2="452" y2="36" stroke="#1e293b" stroke-width="1"/>
      
      <!-- User message 1 -->
      <g transform="translate(18 52)">
        <rect width="320" height="48" rx="12" fill="#1e293b"/>
        <text x="14" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="600" fill="#f8fafc">Hello! What are the documents required</text>
        <text x="14" y="36" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="600" fill="#f8fafc">for a microfinance group loan?</text>
      </g>
      
      <!-- AI Copilot Response -->
      <g transform="translate(68 114)">
        <rect width="380" height="96" rx="12" fill="#7c3aed" fill-opacity="0.25" stroke="#7c3aed" stroke-width="1.5"/>
        <circle cx="22" cy="22" r="10" fill="#7c3aed"/>
        <text x="16" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="800" fill="#fff">AI</text>
        <text x="42" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Arvension AI Assistant</text>
        <text x="42" y="42" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#e2e8f0">1. Aadhaar KYC of all group members</text>
        <text x="42" y="58" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#e2e8f0">2. Group formation resolution letter</text>
        <text x="42" y="74" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#e2e8f0">3. Bank passbook copy for disbursement</text>
      </g>
      
      <!-- Action buttons -->
      <g transform="translate(68 222)">
        <rect width="160" height="28" rx="8" fill="#16a34a"/>
        <text x="18" y="18" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#fff">📲 Book Demo on WhatsApp</text>
      </g>
      
      <!-- Input bar -->
      <g transform="translate(18 280)">
        <rect width="434" height="42" rx="10" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
        <text x="14" y="25" font-family="system-ui,-apple-system,sans-serif" font-size="11" fill="#64748b">Type your business query in Malayalam, English, or Hindi...</text>
        <circle cx="410" cy="21" r="14" fill="#7c3aed"/>
        <text x="404" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#fff">→</text>
      </g>
    </g>
    """

    mobile_inner = f"""
    <!-- WhatsApp Mobile View -->
    <rect width="274" height="66" rx="14" fill="#075e54"/>
    <circle cx="34" cy="33" r="18" fill="#128c7e"/>
    {_path_icon("whatsapp", 24, 23, 0.8, '#fff', 2.0)}
    <text x="62" y="28" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#ffffff">Arvension AI WhatsApp</text>
    <text x="62" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#a7f3d0">Verified Business • Online</text>

    <g transform="translate(0 76)">
      <rect width="274" height="180" rx="14" fill="#070f1e" stroke="#1e2d4a" stroke-width="1"/>
      <g transform="translate(10 14)">
        <rect width="180" height="36" rx="8" fill="#1e293b"/>
        <text x="10" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#f8fafc">I need an ERP demo in Kochi</text>
      </g>
      <g transform="translate(30 60)">
        <rect width="230" height="72" rx="8" fill="#056162"/>
        <text x="10" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#ffffff">Hello! We would love to show you a</text>
        <text x="10" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#ffffff">live demo. Our Kerala team is available</text>
        <text x="10" y="48" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#ffffff">this week. Would Wed 11 AM work?</text>
        <text x="180" y="64" font-family="system-ui,-apple-system,sans-serif" font-size="8" fill="#a7f3d0">11:02 AM ✓✓</text>
      </g>
      <g transform="translate(30 142)">
        <rect width="230" height="24" rx="6" fill="#25d366"/>
        <text x="60" y="16" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#000">Confirm 11 AM Demo</text>
      </g>
    </g>
    """

    desktop_frame = _desktop_chrome(50, 110, 640, 500, "arvension.in/ai-chat-engine", "AI Active", accent)
    sidebar = _desktop_sidebar([("chat", "Chat Engine"), ("cpu", "AI Models"), ("user", "Leads"), ("shield", "Security")], 0, accent)
    phone = _phone_mockup(646, 140, "WhatsApp AI", mobile_inner, accent)

    b1 = _chip(40, 660, chips[0], accent, "cpu")
    b2 = _chip(610, 70, chips[1], "#22c55e", "whatsapp")
    b3 = _chip(480, 680, chips[2], "#38bdf8", "globe")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="AI Websites and Chat Apps">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_inner}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


def render_web():
    accent = "#0891b2"
    sec = "#2563eb"
    chips = ["100/100 Lighthouse Speed", "Mobile-First Responsive", "On-Page SEO Engine"]

    desktop_inner = f"""
    {_kpi_boxes([
        ("LIGHTHOUSE SCORE", "100 / 100", "Top Performance", "#22c55e"),
        ("LOAD SPEED", "0.4s", "Instant FCP", "#0891b2"),
        ("SEO RANKING", "Page 1 Ready", "Schema Included", "#38bdf8"),
    ])}
    
    <!-- Multi-Viewport Responsive Showcase -->
    <g transform="translate(152 140)">
      <rect width="470" height="338" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="18" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Modern Responsive Website Architecture</text>
      <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● CWV PASSED</text>
      <line x1="18" y1="36" x2="452" y2="36" stroke="#1e293b" stroke-width="1"/>
      
      <!-- Website Hero Preview inside mockup -->
      <g transform="translate(18 52)">
        <rect width="434" height="150" rx="10" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
        <!-- Hero text -->
        <rect x="20" y="20" width="120" height="10" rx="5" fill="{accent}"/>
        <text x="20" y="54" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="800" fill="#f8fafc">Websites That Turn</text>
        <text x="20" y="76" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="800" fill="#38bdf8">Visitors Into Clients</text>
        <text x="20" y="98" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#94a3b8">Fast, accessible, mobile-first design built in Technopark.</text>
        <rect x="20" y="112" width="110" height="24" rx="12" fill="{accent}"/>
        <text x="36" y="128" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#fff">Get Started →</text>
      </g>
      
      <!-- Lighthouse 4 circle metrics -->
      <g transform="translate(18 218)">
        <g transform="translate(30 0)">
          <circle cx="30" cy="30" r="26" fill="none" stroke="#22c55e" stroke-width="5"/>
          <text x="18" y="35" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#22c55e">100</text>
          <text x="4" y="74" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#94a3b8">PERFORMANCE</text>
        </g>
        <g transform="translate(135 0)">
          <circle cx="30" cy="30" r="26" fill="none" stroke="#22c55e" stroke-width="5"/>
          <text x="18" y="35" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#22c55e">100</text>
          <text x="2" y="74" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#94a3b8">ACCESSIBILITY</text>
        </g>
        <g transform="translate(240 0)">
          <circle cx="30" cy="30" r="26" fill="none" stroke="#22c55e" stroke-width="5"/>
          <text x="18" y="35" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#22c55e">100</text>
          <text x="3" y="74" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#94a3b8">BEST PRACTICE</text>
        </g>
        <g transform="translate(345 0)">
          <circle cx="30" cy="30" r="26" fill="none" stroke="#22c55e" stroke-width="5"/>
          <text x="18" y="35" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#22c55e">100</text>
          <text x="22" y="74" font-family="system-ui,-apple-system,sans-serif" font-size="9" font-weight="700" fill="#94a3b8">SEO</text>
        </g>
      </g>
    </g>
    """

    mobile_inner = f"""
    <!-- Mobile view of website -->
    <rect width="274" height="260" rx="14" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
    <rect x="14" y="16" width="90" height="8" rx="4" fill="{accent}"/>
    <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#f8fafc">Mobile-First</text>
    <text x="14" y="62" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#38bdf8">Ultra Fast UX</text>
    <text x="14" y="80" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">100% Responsive on iOS &amp; Android</text>
    <rect x="14" y="94" width="246" height="60" rx="8" fill="#0e172a"/>
    <text x="26" y="118" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#22c55e">✓ Zero Cumulative Layout Shift</text>
    <text x="26" y="136" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#38bdf8">✓ 0.4s First Contentful Paint</text>
    """

    desktop_frame = _desktop_chrome(50, 110, 640, 500, "arvension.in/web-design", "100% Speed", accent)
    sidebar = _desktop_sidebar([("globe", "Web Design"), ("palette", "UI/UX"), ("chart", "SEO"), ("shield", "Hosting")], 0, accent)
    phone = _phone_mockup(646, 140, "Mobile Web", mobile_inner, accent)

    b1 = _chip(40, 660, chips[0], "#22c55e", "check")
    b2 = _chip(610, 70, chips[1], accent, "phone")
    b3 = _chip(480, 680, chips[2], "#38bdf8", "search")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="Website Design and Development">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_inner}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


def render_dash():
    accent = "#2563eb"
    sec = "#7c3aed"
    chips = ["Role-Based Access Control", "Enterprise Cloud SaaS", "REST & GraphQL APIs"]

    desktop_inner = f"""
    {_kpi_boxes([
        ("USERS MANAGED", "42,800", "Role-Based", "#22c55e"),
        ("API UPTIME", "99.99%", "High Availability", "#2563eb"),
        ("QUERY LATENCY", "12ms", "Optimized DB", "#38bdf8"),
    ])}
    
    <!-- Cloud Web Application Console -->
    <g transform="translate(152 140)">
      <rect width="470" height="338" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="18" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Enterprise SaaS Application &amp; Role Matrix</text>
      <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● SECURE SSL</text>
      <line x1="18" y1="36" x2="452" y2="36" stroke="#1e293b" stroke-width="1"/>
      
      <!-- Role hierarchy -->
      <g transform="translate(18 50)">
        <rect width="434" height="32" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Super Administrator</text>
        <text x="160" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Full Org Control • Audit Logs • API Keys</text>
        <rect x="360" y="6" width="60" height="20" rx="10" fill="#22c55e" fill-opacity="0.2"/>
        <text x="372" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#22c55e">ACTIVE</text>
      </g>
      <g transform="translate(18 90)">
        <rect width="434" height="32" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Branch Manager</text>
        <text x="160" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Regional Approvals • Staff Attendance • Reports</text>
        <rect x="360" y="6" width="60" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
        <text x="370" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">LIMITED</text>
      </g>
      <g transform="translate(18 130)">
        <rect width="434" height="32" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#f8fafc">Field Executive</text>
        <text x="160" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Mobile App Collections • GPS Verified Access</text>
        <rect x="360" y="6" width="60" height="20" rx="10" fill="#a855f7" fill-opacity="0.2"/>
        <text x="370" y="19" font-family="system-ui,-apple-system,sans-serif" font-size="8.5" font-weight="700" fill="#a855f7">FIELD APP</text>
      </g>
      
      <!-- API health monitor -->
      <g transform="translate(18 175)">
        <rect width="434" height="80" rx="10" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
        <text x="14" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10.5" font-weight="700" fill="#38bdf8">REST &amp; GraphQL Webhook Stream</text>
        <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">POST /api/v2/collection/sync • 200 OK • 18ms</text>
        <text x="14" y="62" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#f8fafc">GET  /api/v2/branch/48/metrics • 200 OK • 12ms</text>
      </g>
    </g>
    """

    mobile_inner = f"""
    <rect width="274" height="260" rx="14" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
    <text x="14" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#f8fafc">Admin Dashboard</text>
    <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Executive Cloud Mobile Monitor</text>
    <g transform="translate(14 60)">
      <rect width="246" height="50" rx="8" fill="#0e172a"/>
      <text x="12" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#94a3b8">Active Sessions Today</text>
      <text x="12" y="40" font-family="system-ui,-apple-system,sans-serif" font-size="16" font-weight="800" fill="#22c55e">1,480 Users</text>
    </g>
    <g transform="translate(14 120)">
      <rect width="246" height="50" rx="8" fill="#0e172a"/>
      <text x="12" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#94a3b8">Daily Database Backups</text>
      <text x="12" y="40" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700" fill="#38bdf8">Encrypted &amp; Stored ✓</text>
    </g>
    """

    desktop_frame = _desktop_chrome(50, 110, 640, 500, "arvension.in/web-apps", "99.99% Uptime", accent)
    sidebar = _desktop_sidebar([("chart", "Dashboards"), ("shield", "Roles"), ("code", "APIs"), ("db", "Database")], 0, accent)
    phone = _phone_mockup(646, 140, "Admin Mobile", mobile_inner, accent)

    b1 = _chip(40, 660, chips[0], accent, "shield")
    b2 = _chip(610, 70, chips[1], "#22c55e", "layers")
    b3 = _chip(480, 680, chips[2], "#38bdf8", "code")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="Web Application Development">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_inner}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


def render_mobile():
    accent = "#16a34a"
    sec = "#2563eb"
    chips = ["Native Android & iOS Apps", "Live GPS Geofencing", "Offline Sync Engine"]

    desktop_inner = f"""
    {_kpi_boxes([
        ("MOBILE USERS", "64,200", "iOS & Android", "#22c55e"),
        ("GPS ACCURACY", "±2 Metres", "Geo-Fenced", "#16a34a"),
        ("OFFLINE SYNC", "100% Reliable", "Local SQLite", "#38bdf8"),
    ])}
    
    <!-- Mobile App Architecture Console -->
    <g transform="translate(152 140)">
      <rect width="470" height="338" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="18" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Cross-Platform Native Engineering</text>
      <text x="340" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● APP STORE READY</text>
      <line x1="18" y1="36" x2="452" y2="36" stroke="#1e293b" stroke-width="1"/>
      
      <g transform="translate(18 52)">
        <rect width="434" height="42" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#22c55e">Field Agent Live GPS Tracking</text>
        <text x="12" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Background location service during working hours with zero battery drain</text>
      </g>
      <g transform="translate(18 104)">
        <rect width="434" height="42" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Staff Attendance Selfie &amp; Geo-Punch</text>
        <text x="12" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Face verification + branch perimeter validation prevents proxy attendance</text>
      </g>
      <g transform="translate(18 156)">
        <rect width="434" height="42" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#a855f7">Customer &amp; Member Self-Service</text>
        <text x="12" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Passbook, loan schedules, online UPI payments, and push notifications</text>
      </g>
    </g>
    """

    mobile_inner = f"""
    <rect width="274" height="260" rx="14" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
    <text x="14" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#f8fafc">Attendance Punch-in</text>
    <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Technopark Branch • In Office</text>
    
    <g transform="translate(14 60)">
      <rect width="246" height="80" rx="10" fill="#0e172a" stroke="#22c55e" stroke-width="1.5"/>
      <circle cx="40" cy="40" r="22" fill="#1e293b"/>
      <text x="32" y="46" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700" fill="#22c55e">✓</text>
      <text x="74" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Geo-Location Validated</text>
      <text x="74" y="50" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#22c55e">Punched in at 9:28 AM</text>
    </g>
    
    <g transform="translate(14 154)">
      <rect width="246" height="42" rx="8" fill="#16a34a"/>
      <text x="56" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="10" font-weight="700" fill="#fff">OFFLINE SYNC: 100% OK</text>
    </g>
    """

    desktop_frame = _desktop_chrome(50, 110, 640, 500, "arvension.in/mobile-apps", "Native Apps", accent)
    sidebar = _desktop_sidebar([("phone", "Mobile Apps"), ("pin", "GPS Engine"), ("clock", "Attendance"), ("shield", "Auth")], 0, accent)
    phone = _phone_mockup(646, 140, "Mobile Punch-in", mobile_inner, accent)

    b1 = _chip(40, 660, chips[0], accent, "phone")
    b2 = _chip(610, 70, chips[1], "#38bdf8", "pin")
    b3 = _chip(480, 680, chips[2], "#22c55e", "clock")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="Mobile App Development">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_inner}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


def render_about():
    accent = "#d97706"
    sec = BRAND
    chips = ["Technopark Trivandrum HQ", "Enterprise Software Engineering", "Dedicated Kerala Team"]

    desktop_inner = f"""
    {_kpi_boxes([
        ("ENGINEERING HQ", "Technopark", "Trivandrum, Kerala", "#f59e0b"),
        ("ENTERPRISE ERPs", "12 Solutions", "Production Proven", "#22c55e"),
        ("CODE QUALITY", "Enterprise", "Zero Legacy Tech", "#38bdf8"),
    ])}
    
    <!-- Software Engineering & Architecture Console -->
    <g transform="translate(152 140)">
      <rect width="470" height="338" rx="14" fill="#0d162a" stroke="#1e2d4a" stroke-width="1"/>
      <text x="18" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700" fill="#f8fafc">Arvension Technologies LLP • Engineering Console</text>
      <text x="350" y="24" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" font-weight="700" fill="#22c55e">● CI/CD GREEN</text>
      <line x1="18" y1="36" x2="452" y2="36" stroke="#1e293b" stroke-width="1"/>
      
      <g transform="translate(18 52)">
        <rect width="434" height="42" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#f59e0b">From Campus Start-up to Enterprise Specialists</text>
        <text x="12" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Started at College of Engineering Attingal (IHRD), now based in Technopark</text>
      </g>
      <g transform="translate(18 104)">
        <rect width="434" height="42" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#22c55e">Gayathri Building, Module 6, Technopark</text>
        <text x="12" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Direct software support by the senior engineering team who built your system</text>
      </g>
      <g transform="translate(18 156)">
        <rect width="434" height="42" rx="8" fill="#070c17"/>
        <text x="12" y="20" font-family="system-ui,-apple-system,sans-serif" font-size="11" font-weight="700" fill="#38bdf8">High-Scale Architecture &amp; Data Security</text>
        <text x="12" y="34" font-family="system-ui,-apple-system,sans-serif" font-size="9" fill="#94a3b8">Encrypted database backups, role-based controls, and automated failover</text>
      </g>
    </g>
    """

    mobile_inner = f"""
    <rect width="274" height="260" rx="14" fill="#070c17" stroke="#1e293b" stroke-width="1"/>
    <text x="14" y="26" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="800" fill="#f8fafc">Arvension HQ</text>
    <text x="14" y="44" font-family="system-ui,-apple-system,sans-serif" font-size="9.5" fill="#94a3b8">Technopark, Thiruvananthapuram</text>
    <g transform="translate(14 60)">
      <rect width="246" height="50" rx="8" fill="#0e172a"/>
      <text x="12" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#94a3b8">Serving Clients Across</text>
      <text x="12" y="40" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="800" fill="#f59e0b">India &amp; Middle East</text>
    </g>
    <g transform="translate(14 120)">
      <rect width="246" height="50" rx="8" fill="#0e172a"/>
      <text x="12" y="22" font-family="system-ui,-apple-system,sans-serif" font-size="10" fill="#94a3b8">Local Support</text>
      <text x="12" y="40" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700" fill="#22c55e">Dedicated Engineers ✓</text>
    </g>
    """

    desktop_frame = _desktop_chrome(50, 110, 640, 500, "arvension.in/about", "Technopark HQ", accent)
    sidebar = _desktop_sidebar([("code", "Engineering"), ("pin", "Technopark"), ("shield", "Values"), ("user", "Team")], 0, accent)
    phone = _phone_mockup(646, 140, "Arvension Team", mobile_inner, accent)

    b1 = _chip(40, 660, chips[0], accent, "pin")
    b2 = _chip(610, 70, chips[1], "#22c55e", "code")
    b3 = _chip(480, 680, chips[2], "#38bdf8", "shield")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 780" role="img" aria-label="About Arvension Technologies">
      {_canvas_bg(accent, sec)}
      {desktop_frame}
      {sidebar}
      {desktop_inner}
      </g>
      {phone}
      {b1}
      {b2}
      {b3}
    </svg>"""


# ============================================================================
# DISPATCHER
# ============================================================================
def art(accent, icon_name, chips, mode="dash", slug=None):
    if slug:
        return render_product_svg(slug, accent, icon_name, chips)
    if mode == "hero":
        return render_hero()
    if mode == "chat":
        return render_ai_chat()
    if mode == "site":
        return render_web()
    if mode == "dash_service":
        return render_dash()
    if mode == "phones":
        return render_mobile()
    if mode == "about":
        return render_about()

    # Fallback to master hero
    return render_hero()
