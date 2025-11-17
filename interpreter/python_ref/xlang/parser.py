# Minimal parser returning list of (verb, args) tuples
import re

STMT_RE = re.compile(r'^U\s+(?P<verb>\w+)\s*(?P<args>.*)$', re.IGNORECASE)

def parse_program(source: str):
    lines = [l.strip() for l in source.splitlines() if l.strip() and not l.strip().startswith('#')]
    out = []
    for ln in lines:
        m = STMT_RE.match(ln)
        if not m:
            raise SyntaxError(f"Invalid statement: {ln}")
        verb = m.group('verb').lower()
        args = m.group('args').strip()
        out.append((verb, args))
    return out
