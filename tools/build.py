# -*- coding: utf-8 -*-
"""Builds ../index.html from src/index.base.html (original 15 systemic topics) + content.py (GP and HM topics)."""
import re, json, html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import content
content.TOPICS = []  # systemic-only edition: General Pathology / Haematology removed
s = open(os.path.join(HERE, 'src/index.base.html'), encoding='utf8').read()

PARTS = [('C', 'Systemic Pathology', 'sys', ['%02d' % i for i in range(1, 16)])]
PART_OF = {t: p[2] for p in PARTS for t in p[3]}
e = lambda t: html.escape(t, quote=False)

old_grid = re.search(r'<h2 id="topics">.*?(?=</main></div><div class="view" id="v-01")', s, re.S).group()
old_cards = {m.group(1): m.group(0) for m in re.finditer(r'<a class="topic" href="#/(\d\d)">.*?</a>', old_grid, re.S)}
names = {k: re.search(r'<h3>(.*?)</h3>', v).group(1) for k, v in old_cards.items()}
short = dict(re.findall(r'<option value="(\d\d)"[^>]*>\d\d  (.*?)</option>', re.search(r'<select class="jump".*?</select>', s, re.S).group()))

n = len(re.findall(r'id="q\d+"', s)); base_n = n
new_data, new_views = [], {}
for tid, tname, part, qs in content.TOPICS:
    names[tid] = e(tname); short[tid] = e(tname)
    arts = []
    for code, q, ans in qs:
        n += 1
        new_data.append([code, q, tid, 'q%d' % n, tname])
        arts.append('<article class="card" id="q%d"><header tabindex="0"><span class="code">%s</span><h4>%s</h4></header><div class="ans">%s</div></article>' % (n, code, e(q), ans))
    new_views[tid] = (qs, ''.join(arts))
total = n
order = sorted(names)

def jump(cur):
    return '<select class="jump" aria-label="Jump to topic">' + ''.join('<option value="%s"%s>%s  %s</option>' % (t, ' selected' if t == cur else '', t, short[t]) for t in order) + '</select>'

v01 = re.search(r'<div class="view" id="v-01".*?(?=<div class="view" id="v-02")', s, re.S).group()
head = v01[:v01.index('<main>')]
def pager(tid):
    i = order.index(tid)
    prev = '<a href="#/%s"><small>Previous</small>%s</a>' % (order[i-1], names[order[i-1]]) if i else '<span></span>'
    nxt = '<a class="nx" href="#/%s"><small>Next</small>%s</a>' % (order[i+1], names[order[i+1]]) if i < len(order)-1 else '<a class="nx" href="#/"><small>Finished</small>Back to all topics</a>'
    return '<div class="pager">%s%s</div>' % (prev, nxt)

views = ''
for tid in order[15:]:
    qs, arts = new_views[tid]
    pl = [p for p in PARTS if tid in p[3]][0]
    h = head.replace('id="v-01"', 'id="v-%s"' % tid).replace('Blood Vessels | Systemic Pathology Viva', '%s | Pathology Viva' % names[tid])
    h = h.replace('All topics</a> / 01', 'All topics</a> / %s' % tid).replace('<h1>Blood Vessels</h1>', '<h1>%s</h1>' % names[tid])
    h = h.replace('6 questions, in the same order as the NMC viva list.', '%d questions · Part %s, %s.' % (len(qs), pl[0], pl[1]))
    views += h + '<main>' + arts + '<p class="none">No question matches your search.</p>' + pager(tid) + '</main></div>'
s = re.sub(r'(id="v-15".*?)<div class="pager">.*?</div>', lambda m: m.group(1) + pager('15'), s, count=1, flags=re.S)
s = s.replace('<div class="view" id="v-bookmarks"', views + '<div class="view" id="v-bookmarks"', 1)
s = re.sub(r'<select class="jump".*?</select>', lambda m: jump(re.search(r'<option value="(\d\d)" selected', m.group()).group(1)), s, flags=re.S)
s = s.replace('"Histopathology Practical"]];', '"Histopathology Practical"]' + ''.join(', ' + json.dumps(d, ensure_ascii=False) for d in new_data) + '];', 1)

def qn(c): return int(re.search(r'(\d+) questions', c).group(1))
def card(tid):
    if tid in old_cards: c = old_cards[tid]
    else:
        qs = new_views[tid][0]
        c = '<a class="topic" href="#/%s"><span class="no">%s</span><h3>%s</h3><p>%s</p><span class="cnt">%d questions</span></a>' % (tid, tid, names[tid], e('; '.join(q[1][:50] + ('…' if len(q[1]) > 50 else '') for q in qs[:2])), len(qs))
    return c.replace('<a class="topic"', '<a class="topic" data-n="%d"' % qn(c), 1)
secs = ''
for letter, pname, key, tids in PARTS:
    cs = [card(t) for t in tids]
    secs += '<section class="part" data-part="%s"><div class="part-h"><h3>%s</h3><span class="mu">%d topics · %d questions</span><span class="ring pp" data-pp="%s"></span></div><div class="grid">%s</div></section>' % (key, pname, len(tids), sum(qn(c) for c in cs), key, ''.join(cs))
chips = '<div class="chips" id="pchips" role="group" aria-label="Filter by part"><button aria-pressed="true" data-f="all">All parts</button>' + ''.join('<button aria-pressed="false" data-f="%s">%s</button>' % (p[2], p[1]) for p in PARTS) + '<span class="sp"></span><button aria-pressed="false" data-sort="n">Sort: most questions</button></div>'
s = s.replace(old_grid, '<h2 id="topics">Topics<small>%d questions</small></h2>%s' % (total, secs), 1)

s = s.replace('<small>Browse</small>15 topics', '<small>Browse</small>%d topics' % len(order))

s = s.replace("sort((a,b)=>a.slice(1)-b.slice(1))", "sort((a,b)=>(a.slice(1)-b.slice(1))||a.localeCompare(b))", 1)
s = s.replace("new Blob([JSON.stringify(S,null,1)]", "new Blob([JSON.stringify(Object.assign({},S,{ink:(typeof Ink!=='undefined'?Ink.dump():{})}),null,1)]", 1)
s = s.replace("function imp(f){if(!f)return;f.text().then(t=>{try{const o=JSON.parse(t);if(!o||!Array.isArray(o.bm))throw 0;Object.assign(S,o);save();location.reload()}catch(e){alert('That file is not a valid backup.')}})}",
 "function imp(f){if(!f)return;f.text().then(async t=>{let o;try{o=JSON.parse(t);if(!o||!Array.isArray(o.bm))throw 0}catch(e){alert('That file is not a valid backup.');return}const ink=o.ink;delete o.ink;Object.assign(S,o);save();if(ink&&typeof Ink!=='undefined')await Ink.load(ink);location.reload()})}", 1)
assert 'Ink.load' in s and 'Ink.dump' in s and 'localeCompare(b))' in s

PART_JS = "const PART_OF=%s;\n" % json.dumps(PART_OF) + r"""(function(){const p=prog;prog=function(){p();const L=new Set(S.learned),T={},N={};DATA.forEach(d=>{const k=PART_OF[d[2]];N[k]=(N[k]||0)+1;if(L.has(d[3]))T[k]=(T[k]||0)+1});document.querySelectorAll('[data-pp]').forEach(r=>{const k=r.dataset.pp,c=Math.round(100*(T[k]||0)/N[k]);r.style.setProperty('--p',c);r.textContent=c+'%'})};prog();
const ch=document.getElementById('pchips');if(!ch)return;const secs=[...document.querySelectorAll('section.part')],orig=secs.map(x=>[...x.querySelectorAll('.topic')]);let f='all',srt=false;
function apply(){secs.forEach((x,i)=>{x.hidden=f!=='all'&&x.dataset.part!==f;const g=x.querySelector('.grid'),a=orig[i].slice();if(srt)a.sort((u,v)=>v.dataset.n-u.dataset.n||u.getAttribute('href').localeCompare(v.getAttribute('href')));a.forEach(t=>g.append(t))});ch.querySelectorAll('[data-f]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.f===f));ch.querySelector('[data-sort]').setAttribute('aria-pressed',srt)}
ch.onclick=e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.f)f=b.dataset.f;else srt=!srt;apply()}})();
"""
i = s.index('const DATA='); j = s.index('</script>', i)
s = s[:j] + '\n' + PART_JS + s[j:]
open(os.path.join(HERE, '_stage.html'), 'w', encoding='utf8').write(s)
print('questions', base_n, '->', total, 'topics', len(order))

# ---------------------------------------------------------------- CSS, ink script, CSP
CSS = r"""
.chips{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:4px 0 18px}.chips .sp{flex:1}
.chips button{background:var(--panel);border:1px solid var(--line);color:var(--text);font:600 13px var(--body);padding:8px 14px;border-radius:999px;cursor:pointer}
.chips button[aria-pressed=true]{border-color:var(--orange);color:var(--lbl)}
section.part{margin:0 0 30px}.part-h{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:8px 0 14px}.part-h h3{margin:0;font:800 20px var(--disp)}.part-h .mu{color:var(--muted);font-size:13px;flex:1}
.ring.pp{width:46px;height:46px;font-size:11px}
.card .ans{position:relative}canvas.ink{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:2}
#ink{position:fixed;left:50%;transform:translateX(-50%);bottom:70px;z-index:40;display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:4px;max-width:calc(100vw - 20px);background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:6px;box-shadow:0 8px 30px rgba(0,0,0,.35)}
#ink[hidden]{display:none}#ink button{background:none;border:0;color:var(--text);font:600 12px var(--body);padding:7px 10px;border-radius:999px;cursor:pointer}
#ink button:hover:not(:disabled){background:var(--chip)}#ink button:disabled{opacity:.35;cursor:default}#ink button[aria-pressed=true]{background:var(--chip);color:var(--lbl);box-shadow:inset 0 0 0 1px var(--lbl)}
#ink .done{color:var(--lbl)}#ink .sep{width:1px;height:22px;background:var(--line);margin:0 4px}
#ink .sw button{width:22px;height:22px;padding:0;border-radius:50%;background:var(--c);border:2px solid transparent;margin:0 2px}#ink .sw button[aria-pressed=true]{border-color:var(--text);box-shadow:none;background:var(--c)}
#ink .zs button{padding:7px 8px}
body.inking.ink-pen .card .ans,body.inking.ink-hl .card .ans,body.inking.ink-er .card .ans,body.inking.ink-lasso .card .ans{touch-action:none;-webkit-user-select:none;user-select:none;cursor:crosshair}
body.inking .card .ans{outline:1px dashed var(--line);outline-offset:-1px}
@media print{#ink{display:none}}
"""
s = re.sub(r'@font-face\{font-family:"(?:Plus Jakarta Sans|Source Sans 3)".*?\}\n?', '', s)
s = s.replace('</style>', CSS + open(os.path.join(HERE, 'theme.css'), encoding='utf8').read() + '</style>', 1)
H1 = '<h1>Viva Prep —<br>Read.<br>Recall. Answer.</h1>'
assert H1 in s
s = s.replace(H1, '<p class="eyebrow">NMC viva list · Robbins 11th</p><h1>Systemic Pathology<em>Read. Recall. Answer.</em></h1>', 1)
s = s.replace('<b>Systemic Pathology Viva Questions with Answers.</b> ', '', 1)
STATS = '<div class="stats"><div><b>%d</b><span>Viva questions</span></div><div><b>%d</b><span>Systemic topics</span></div><div><b>NMC</b><span>Question order</span></div><div><b>11th</b><span>Robbins edition</span></div></div>' % (total, len(order))
T = '<ul id="res"></ul></div></div></div></div><main'
assert T in s
s = s.replace(T, '<ul id="res"></ul></div></div></div>' + STATS + '</div><main', 1)
s = s.replace('content="#000000" media', 'content="#0c131f" media').replace('content="#f7f4f2" media', 'content="#f7f6f2" media')
CSP = "<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self'; connect-src 'self'; manifest-src 'self'; worker-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'\"><meta name=\"referrer\" content=\"no-referrer\">"
s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + CSP, 1)
s = s.replace("<script>\nif ('serviceWorker'", '<script src="ink.js"></script>\n<script>\nif (\'serviceWorker\'', 1)
assert 'src="ink.js"' in s and 'Content-Security-Policy' in s
open(os.path.join(HERE, '..', 'index.html'), 'w', encoding='utf8').write(s)
os.remove(os.path.join(HERE, '_stage.html'))
print('wrote index.html', len(s))
