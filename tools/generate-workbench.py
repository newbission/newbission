from pathlib import Path
import random
from html import escape
O=Path(__file__).resolve().parents[1]
A=O/'assets'
M='font-family="ui-monospace,SFMono-Regular,Consolas,monospace"'
S='font-family="Arial,Helvetica,Apple SD Gothic Neo,sans-serif"'
for theme in ['dark','light']:
 d=theme=='dark'
 bg='#171A19' if d else '#F2EFE7';ink='#EFEDE4' if d else '#222620';muted='#949D90' if d else '#697262';line='#343B32' if d else '#D4D8C9';lime='#D1EF80' if d else '#48681F';panel='#20261F' if d else '#E7E9DF'
 # SVG original artwork, no remote images or scripts
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="520" viewBox="0 0 1200 520" role="img" aria-label="newbission — a work in progress. 신인의 자세로, 열정과 패기 있게.">
<defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="{muted}" opacity=".15"/></pattern><linearGradient id="screen" x2="1" y2="1"><stop stop-color="#292F30"/><stop offset="1" stop-color="#121B1D"/></linearGradient><linearGradient id="key" x2="1" y2="1"><stop stop-color="#D9D9C9"/><stop offset="1" stop-color="#969E8B"/></linearGradient></defs>
<style>.cursor{{animation:blink 1.2s step-end infinite}}.float{{animation:float 6s ease-in-out infinite}}.squiggle{{stroke-dasharray:7 8;animation:move 8s linear infinite}}@keyframes blink{{50%{{opacity:0}}}}@keyframes float{{50%{{transform:translateY(-8px)}}}}@keyframes move{{to{{stroke-dashoffset:-150}}}}@media(prefers-reduced-motion:reduce){{.cursor,.float,.squiggle{{animation:none}}}}</style>
<rect width="1200" height="520" rx="16" fill="{bg}"/><rect width="1200" height="520" rx="16" fill="url(#dots)"/>
<path d="M32 74H1168M32 460H1168" stroke="{line}"/>
<g {M} font-size="11" letter-spacing="1.5" fill="{muted}"><text x="36" y="46">N / PERSONAL WORKBENCH</text><text x="1164" y="46" text-anchor="end">OPEN ENDED. ALWAYS CURIOUS.</text></g>
<rect x="37" y="108" width="147" height="26" rx="13" fill="{lime}"/><text x="110" y="125" {M} font-size="10" letter-spacing="1" text-anchor="middle" fill="{bg}">A WORK IN PROGRESS</text>
<text x="29" y="232" {S} font-size="106" font-weight="800" letter-spacing="-7" fill="{ink}">newbission<tspan fill="{lime}">.</tspan></text>
<text x="39" y="270" {M} font-size="13" letter-spacing="1.7" fill="{muted}">NEWBIE + AMBITION + PASSION</text>
<text x="38" y="337" {S} font-size="25" font-weight="500" fill="{ink}">신인의 자세로,</text><text x="38" y="373" {S} font-size="25" font-weight="500" fill="{ink}">열정과 패기 있게.</text>
<path d="M281 367q60 -50 107 -10t88 -28" stroke="{lime}" stroke-width="2" fill="none"/><path d="M463 328l14 -2 -5 14" fill="none" stroke="{lime}" stroke-width="2"/>
<g transform="translate(674 90)">
<!-- paper terminal / isometric desk -->
<path d="M-15 292L252 356 485 249 221 186Z" fill="{panel}" stroke="{line}"/>
<g class="float">
<path d="M77 25L331 81 331 258 77 202Z" fill="#8E9B83" stroke="#BAC4B1" stroke-width="1.5"/>
<path d="M77 25L86 19 341 75 331 81Z" fill="#C9D0BC"/>
<path d="M331 81L341 75 341 252 331 258Z" fill="#697661"/>
<path d="M91 42L316 91 316 237 91 188Z" fill="url(#screen)"/>
<path d="M112 69L176 83M112 86L227 111M127 106L199 122M127 124L260 154M112 138L167 151" stroke="#D1EF80" stroke-width="4" opacity=".85"/>
<path d="M180 154l50 11M112 156l39 9" stroke="#B8A9D9" stroke-width="4"/>
<path class="cursor" d="M243 168l7 2 0 9 -7 -2Z" fill="#D1EF80"/>
<path d="M77 202L331 258 258 294 5 237Z" fill="url(#key)" stroke="#C3CCBA"/>
<path d="M5 237L258 294 258 302 5 245Z" fill="#748267"/>
<path d="M258 294L331 258 331 266 258 302Z" fill="#59694F"/>
<g stroke="#687461" stroke-width="4" opacity=".7"><path d="M67 217l206 46M47 227l206 46M88 219l-35 17M114 225l-35 17M140 231l-35 17M166 237l-35 17M192 243l-35 17M218 249l-35 17M244 255l-35 17"/></g>
</g>
<!-- tiny helper robot -->
<g transform="translate(371 181) rotate(11)"><rect x="-2" y="0" width="75" height="58" rx="15" fill="#B9ABD4"/><rect x="7" y="11" width="57" height="33" rx="8" fill="#30343B"/><rect x="17" y="22" width="7" height="9" rx="2" fill="#D1EF80"/><rect x="46" y="22" width="7" height="9" rx="2" fill="#D1EF80"/><path d="M35 0V-14" stroke="#B9ABD4" stroke-width="3"/><circle class="cursor" cx="35" cy="-17" r="4" fill="#D1EF80"/><path d="M9 58v11M61 58v11" stroke="#B9ABD4" stroke-width="8"/></g>
<!-- sticker -->
<g transform="translate(323 9) rotate(13)"><rect width="116" height="49" rx="4" fill="#D1EF80"/><text x="58" y="20" {M} font-size="11" text-anchor="middle" fill="#26321D">MAKE IT.</text><text x="58" y="36" {M} font-size="11" text-anchor="middle" fill="#26321D">MAKE IT BETTER.</text></g>
<path class="squiggle" d="M12 142C-54 67 -46 10 34 8" fill="none" stroke="{muted}" stroke-width="1.5"/><text x="-6" y="185" {M} font-size="12" fill="{muted}" transform="rotate(-12)">&lt; / &gt;</text>
</g>
<text x="37" y="491" {M} font-size="11" letter-spacing="2" fill="{muted}">THINK. BUILD. BREAK. LEARN. REPEAT.</text><g transform="translate(1073 482)" fill="{lime}"><rect width="9" height="9" opacity=".25"/><rect x="19" width="9" height="9" opacity=".5"/><rect x="38" width="9" height="9" opacity=".75"/><rect class="cursor" x="57" width="9" height="9"/></g></svg>'''
 (A/f'workbench-{theme}.svg').write_text(svg)
 # local one-piece branded nav buttons implementable as linked README images
 for name,label,caption,num in [('portfolio','WORK / PORTFOLIO','프로젝트 구경하기','01'),('resume','ABOUT / RESUME','이력서 보기','02')]:
  s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="550" height="92" viewBox="0 0 550 92"><rect x="1" y="1" width="548" height="90" rx="8" fill="{panel}" stroke="{line}"/><text x="21" y="27" {M} font-size="10" fill="{muted}">{num} / {escape(label)}</text><text x="21" y="62" {S} font-size="19" font-weight="600" fill="{ink}">{caption}</text><path d="M494 30h20v20m0 -20l-28 28" stroke="{lime}" stroke-width="2" fill="none"/></svg>'''
  (A/f'wb-{name}-{theme}.svg').write_text(s)
 for name,label,sub in [('toolbox','TOOLS ON THE DESK','not a ranking, just my toolkit'),('log','THE COMMIT TRAIL','little by little, commit by commit')]:
  s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="58" viewBox="0 0 1100 58"><path d="M0 15H1100" stroke="{line}"/><rect x="0" y="30" width="7" height="7" fill="{lime}"/><text x="20" y="39" {M} font-size="12" letter-spacing="2" fill="{ink}">{label}</text><text x="1100" y="39" text-anchor="end" {M} font-size="10" fill="{muted}">{sub}</text></svg>'''
  (A/f'wb-{name}-{theme}.svg').write_text(s)
 # Original cards with bundled Skill Icons artwork; no decoration arrows.
 import re
 for filename,label,desc,source,num in [
     ('backend','CODE & SERVICES','데이터를 다루고, API를 만들고, 기능을 서비스로 연결.','backend','01'),
     ('infra','SHIP & OPERATE','배포하고, 운영하며, 반복 작업을 줄이는 도구들.','infra','02')]:
     raw=(A/f'{source}-{theme}.svg').read_text()
     # Isolate IDs inside the nested icon SVG from the card and other icons.
     ids=re.findall(r'\bid="([^"]+)"',raw)
     for item in sorted(set(ids),key=len,reverse=True):
         raw=raw.replace(f'id="{item}"',f'id="wb-{source}-{item}"').replace(f'url(#{item})',f'url(#wb-{source}-{item})').replace(f'href="#{item}"',f'href="#wb-{source}-{item}"')
     w=216.75 if source=='backend' else 273
     raw=re.sub(r'<svg\b',f'<svg x="24" y="62"',raw,count=1)
     raw=re.sub(r'width="[^"]+"',f'width="{w}"',raw,count=1)
     card=f'''<svg xmlns="http://www.w3.org/2000/svg" width="550" height="172" viewBox="0 0 550 172"><rect x="1" y="1" width="548" height="170" rx="8" fill="{panel}" stroke="{line}"/><text x="24" y="34" {M} font-size="11" letter-spacing="2" fill="{muted}">{num} / {escape(label)}</text>{raw}<text x="24" y="145" {S} font-size="12" fill="{muted}">{desc}</text></svg>'''
     (A/f'wb-{filename}-{theme}.svg').write_text(card)
 note=f'''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="250" viewBox="0 0 500 250"><rect x="1" y="1" width="498" height="248" rx="8" fill="{panel}" stroke="{line}"/><text x="28" y="36" {M} font-size="11" letter-spacing="2" fill="{muted}">A NOTE TO SELF</text><text x="28" y="97" {S} font-size="28" fill="{ink}">처음 해보는 일도,</text><text x="28" y="138" {S} font-size="28" fill="{ink}"><tspan fill="{lime}">끝까지</tspan> 해보는 쪽으로.</text><text x="28" y="186" {S} font-size="14" fill="{muted}">신인의 자세는 잃지 않고,</text><text x="28" y="210" {S} font-size="14" fill="{muted}">만드는 사람으로 계속 나아가기.</text></svg>'''
 (A/f'wb-note-{theme}.svg').write_text(note)
 footer=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="52" viewBox="0 0 1100 52"><path d="M0 1H1100" stroke="{line}"/><text x="0" y="32" {M} font-size="11" letter-spacing="1.5" fill="{muted}">NEWBIE MINDSET. <tspan fill="{lime}">ENDLESS AMBITION.</tspan></text><text x="1100" y="32" text-anchor="end" {M} font-size="10" fill="{muted}">SEE YOU AT THE NEXT COMMIT ▪</text></svg>'''
 (A/f'wb-footer-{theme}.svg').write_text(footer)

# Full-width closing note; keep it as the last content block.
for theme in ['dark', 'light']:
    dark = theme == 'dark'
    bg, ink, soft, line, accent = ('#20261F','#EFEDE4','#949D90','#343B32','#D1EF80') if dark else ('#E7E9DF','#222620','#697262','#D4D8C9','#48681F')
    note = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="190" viewBox="0 0 1100 190"><rect x="1" y="1" width="1098" height="188" rx="8" fill="{bg}" stroke="{line}"/><text x="32" y="39" {M} font-size="11" letter-spacing="2" fill="{soft}">A NOTE TO SELF</text><text x="32" y="92" {S} font-size="29" fill="{ink}">처음 해보는 일도, <tspan fill="{accent}">끝까지</tspan> 해보는 쪽으로.</text><text x="32" y="139" {S} font-size="15" fill="{soft}">신인의 자세는 잃지 않고, 만드는 사람으로 계속 나아가기.</text></svg>'''
    (A / f'wb-note-wide-{theme}.svg').write_text(note)
