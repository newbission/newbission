"""Generate the original, theme-aware SVG assets used by the profile README."""
from pathlib import Path
import random
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets'
random.seed(24)
stars = [(random.randint(25,975),random.randint(20,285),random.choice([.8,1,1.5]),random.random()) for _ in range(56)]
for theme in ['dark','light']:
    dark = theme == 'dark'
    bg, panel, ink, soft, border = ('#070D1C','#0D172B','#ECF5FF','#8CA6CD','#233957') if dark else ('#F4F8FF','#FFFFFF','#10274E','#526F99','#CDDBEF')
    blue = '#4D88FF' if dark else '#2455E6'
    star = '#A8CDFF' if dark else '#6895CC'
    header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="380" viewBox="0 0 1000 380" role="img" aria-label="newbission. Newbie mindset. Ambition to build. Passion to keep going.">
<defs>
<radialGradient id="halo"><stop stop-color="#3672FF" stop-opacity="{'.32' if dark else '.12'}"/><stop offset="1" stop-color="#3672FF" stop-opacity="0"/></radialGradient>
<radialGradient id="planet" cx="32%" cy="25%"><stop stop-color="#9BEAFF"/><stop offset=".35" stop-color="#4387FF"/><stop offset=".72" stop-color="#1848AE"/><stop offset="1" stop-color="#0B1743"/></radialGradient>
<linearGradient id="ring"><stop stop-color="#3779FF" stop-opacity=".1"/><stop offset=".5" stop-color="#8DE3FF"/><stop offset="1" stop-color="#3779FF" stop-opacity=".1"/></linearGradient>
<linearGradient id="type"><stop stop-color="{ink}"/><stop offset="1" stop-color="{blue}"/></linearGradient>
<clipPath id="clip"><rect width="1000" height="380" rx="18"/></clipPath>
</defs>
<style>
.star{{animation:twinkle 5s ease-in-out infinite alternate}}.orbital{{transform-origin:796px 170px;animation:orbit 24s linear infinite}}.cursor{{animation:blink 1.2s step-end infinite}}.beacon{{animation:beacon 4s ease-in-out infinite}}@keyframes twinkle{{to{{opacity:.18}}}}@keyframes orbit{{to{{transform:rotate(360deg)}}}}@keyframes blink{{50%{{opacity:0}}}}@keyframes beacon{{50%{{opacity:.4}}}}@media(prefers-reduced-motion:reduce){{.star,.orbital,.cursor,.beacon{{animation:none}}}}
</style>
<g clip-path="url(#clip)"><rect width="1000" height="380" fill="{bg}"/><ellipse cx="805" cy="155" rx="300" ry="265" fill="url(#halo)"/>
'''
    for i,(x,y,r,opacity) in enumerate(stars):
        header += f'<circle class="star" cx="{x}" cy="{y}" r="{r}" fill="{star}" opacity="{.2+opacity*.5:.2f}" style="animation-delay:-{i%5}s"/>'
    header += f'''
<g fill="none" stroke="{border}" stroke-width="1"><path d="M25 46V25H46M954 25H975V46M25 334V355H46M954 355H975V334"/><path d="M594 30V273" stroke-dasharray="2 8"/></g>
<text x="51" y="55" fill="{soft}" font-family="monospace" font-size="11" letter-spacing="2">PERSONAL SPACE / 001</text>
<circle class="beacon" cx="902" cy="51" r="3" fill="{blue}"/><text x="913" y="55" fill="{soft}" font-family="monospace" font-size="10">BUILDING</text>
<g fill="none"><ellipse cx="796" cy="170" rx="144" ry="102" stroke="{blue}" opacity=".18"/><circle cx="796" cy="170" r="120" stroke="{blue}" stroke-dasharray="2 10" opacity=".28"/><circle cx="796" cy="170" r="149" stroke="{blue}" opacity=".09"/></g>
<g class="orbital"><circle cx="916" cy="170" r="4" fill="#6ED6FF"/><circle cx="676" cy="170" r="2.5" fill="{blue}"/></g>
<ellipse cx="796" cy="170" rx="150" ry="33" transform="rotate(-24 796 170)" fill="none" stroke="url(#ring)" stroke-width="3" opacity=".5"/>
<circle cx="796" cy="170" r="65" fill="url(#planet)"/><path d="M662 218 Q800 212 929 112" fill="none" stroke="url(#ring)" stroke-width="3"/>
<text x="50" y="151" fill="url(#type)" font-family="Arial,Helvetica,sans-serif" font-size="78" font-weight="700" letter-spacing="-4">newbission<tspan fill="{blue}">.</tspan></text>
<text x="54" y="189" fill="{soft}" font-family="monospace" font-size="12" letter-spacing="2">NEWBIE + AMBITION + PASSION</text>
<text x="53" y="238" fill="{ink}" font-family="Arial,Apple SD Gothic Neo,sans-serif" font-size="21">신인의 자세로, 열정과 패기 있게.</text>
<rect x="42" y="288" width="916" height="54" rx="8" fill="{panel}" stroke="{border}"/>
<circle cx="62" cy="315" r="3" fill="{blue}"/>
<text x="78" y="320" fill="{soft}" font-family="monospace" font-size="13"><tspan fill="{blue}">~/newbission</tspan><tspan> $ keep learning &amp;&amp; keep building</tspan><tspan class="cursor" fill="{blue}"> ▌</tspan></text>
</g></svg>'''
    (OUT / f'orbital-{theme}.svg').write_text(header)
    for file,label,sub in [('tools','TOOLBOX','what I work with'),('activity','ACTIVITY','small steps, real progress')]:
        (OUT/f'{file}-{theme}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="54" viewBox="0 0 850 54"><path d="M0 30H228M622 30H850" stroke="{border}"/><circle cx="242" cy="30" r="3" fill="{blue}"/><text x="425" y="25" text-anchor="middle" font-family="monospace" font-size="13" letter-spacing="4" fill="{ink}">{label}</text><text x="425" y="45" text-anchor="middle" font-family="monospace" font-size="10" fill="{soft}">{sub}</text><circle cx="608" cy="30" r="3" fill="{blue}"/></svg>''')
    (OUT/f'footer-{theme}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="65" viewBox="0 0 850 65"><path d="M0 5H850" stroke="{border}"/><text x="0" y="38" font-family="monospace" font-size="10" letter-spacing="2" fill="{soft}">STILL A NEWBIE. ALWAYS A BUILDER.</text><g fill="{blue}"><rect x="793" y="26" width="8" height="8" opacity=".3"/><rect x="811" y="26" width="8" height="8" opacity=".6"/><rect x="829" y="26" width="8" height="8"/></g></svg>''')
