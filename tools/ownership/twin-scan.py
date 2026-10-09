#!/usr/bin/env python3
"""Ownership inventory scan: every file in mauro-os skills/, tools/, .claude/ and Mauro's
global ~/.claude/skills, matched by basename against /Users/mauro/growthub-os.
For each file: twin path(s), lines that differ, growthub-os mentions, first commit in mauro-os.
Run: python3 tools/ownership/twin-scan.py > tools/ownership/twin-scan.csv
"""
import csv, difflib, os, re, subprocess, sys
from pathlib import Path

MO = Path('/Users/mauro/mauro-os'); GH = Path('/Users/mauro/growthub-os'); GS = Path('/Users/mauro/.claude/skills')
SKIP_DIRS = {'node_modules', '.git', '__pycache__', '.venv', 'venv'}
TEXT = {'.md', '.py', '.json', '.html', '.css', '.csv', '.txt', '.yaml', '.sh'}
AGENCY = re.compile(r'growthub|lorenzo|bogdan|growtHub|/growthub-os|pravata|bogzabs', re.I)

gh_index = {}
for root, dirs, files in os.walk(GH):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        gh_index.setdefault(f, []).append(Path(root) / f)

def lines(p):
    try: return p.read_text(errors='ignore').splitlines()
    except Exception: return []

def first_commit(p):
    try:
        out = subprocess.run(['git', '-C', str(MO), 'log', '--follow', '--format=%ad|%an|%s', '--date=short', '--', str(p.relative_to(MO))],
                             capture_output=True, text=True).stdout.strip().splitlines()
        return out[-1] if out else ''
    except Exception: return ''

def gh_first(p):
    out = subprocess.run(['git', '-C', str(GH), 'log', '--follow', '--format=%ad|%an', '--date=short', '--', str(p.relative_to(GH))],
                         capture_output=True, text=True).stdout.strip().splitlines()
    return out[-1] if out else ''

targets = []
for sub in ['skills', 'tools', '.claude']:
    for root, dirs, files in os.walk(MO / sub):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f in ('.DS_Store', 'settings.local.json'): continue
            targets.append(Path(root) / f)
for root, dirs, files in os.walk(GS):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
    for f in files:
        if not f.startswith('.'): targets.append(Path(root) / f)

w = csv.writer(sys.stdout)
w.writerow(['file', 'lines', 'agency_mentions', 'twin_in_growthub_os', 'lines_differ', 'gh_twin_first_commit', 'mauro_os_first_commit'])
for p in sorted(targets):
    L = lines(p) if p.suffix in TEXT else []
    mentions = sum(1 for l in L if AGENCY.search(l))
    twins = [t for t in gh_index.get(p.name, []) if p.name not in ('README.md', 'SKILL.md', 'main.md', '_master.md', 'build.py', 'settings.json', 'manifest.json', 'openai.yaml')]
    best, bestdiff = '', ''
    if twins and p.suffix in TEXT:
        scored = []
        for t in twins:
            d = sum(1 for x in difflib.unified_diff(L, lines(t), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---'))
            scored.append((d, t))
        bestdiff, best = min(scored)
    elif twins:
        best = twins[0]
    rel = str(p).replace('/Users/mauro/', '~/')
    w.writerow([rel, len(L), mentions, str(best).replace('/Users/mauro/', '~/') if best else '', bestdiff,
                gh_first(best) if best else '', first_commit(p) if str(p).startswith(str(MO)) else ''])
