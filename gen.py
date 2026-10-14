#!/usr/bin/env python3
"""Generate METHODS.md (flat table) + docs/bas-ip-api.md (full RU reference)
for CURRENT versions only."""
import json, glob, os, re

ROOT = "/root/workdir/bas-ip-api-current"
OUT = os.path.join(ROOT, "docs", "bas-ip-api.md")

def dev_of(fn):
    return os.path.basename(fn).replace("__current.json", "")

def esc(s):
    if s is None: return ""
    return str(s).replace("|", "\\|").replace("\n", " ")

def type_str(s):
    if not isinstance(s, dict): return ""
    t = s.get("type") or ("object" if "properties" in s else "")
    if s.get("enum"): t += " enum(" + ", ".join(map(str, s["enum"])) + ")"
    if t == "array" and isinstance(s.get("items"), dict):
        it = s["items"].get("type") or ("object" if "properties" in s["items"] else "")
        t = f"array<{it}>"
    return t

def flatten_schema(schema, prefix="", out=None, depth=0):
    if out is None: out = []
    if depth > 6 or not isinstance(schema, dict): return out
    for comb in ("allOf", "oneOf", "anyOf"):
        if comb in schema:
            for sub in schema[comb]:
                flatten_schema(sub, prefix, out, depth+1)
            return out
    props = schema.get("properties")
    if isinstance(props, dict):
        req = set(schema.get("required") or [])
        for name, ps in props.items():
            if not isinstance(ps, dict): continue
            field = f"{prefix}.{name}" if prefix else name
            out.append((field, type_str(ps), "да" if name in req else "нет",
                        esc(ps.get("description")), esc(ps.get("example"))))
            if ps.get("type") == "array" and isinstance(ps.get("items"), dict):
                flatten_schema(ps["items"], field + "[]", out, depth+1)
            elif ps.get("type") == "object" or "properties" in ps:
                flatten_schema(ps, field, out, depth+1)
    return out

def schema_block(title, schema):
    rows = flatten_schema(schema)
    if not rows:
        return ""
    L = [f"<details><summary>{title}</summary>", "",
         "| Поле | Тип | Обяз. | Описание | Пример |", "|---|---|---|---|---|"]
    for f, t, r, d, e in rows:
        L.append(f"| `{esc(f)}` | {esc(t)} | {r} | {d} | {e} |")
    L += ["", "</details>", ""]
    return "\n".join(L)

def example_of(content):
    try:
        for mt, mo in (content or {}).items():
            ex = mo.get("example")
            if ex is None and isinstance(mo.get("schema"), dict):
                ex = mo["schema"].get("example")
            if ex is not None:
                return json.dumps(ex, ensure_ascii=False, indent=2)
    except Exception:
        pass
    return None

specs = []
for f in sorted(glob.glob(os.path.join(ROOT, "openapi", "*.json"))):
    specs.append((dev_of(f), json.load(open(f))))

# ---------- METHODS.md ----------
mlines = ["# BAS-IP API — все методы (актуальные версии)", ""]
total = 0
for dev, d in specs:
    ops = [(p, m, o) for p, ms in d["paths"].items() for m, o in ms.items()]
    total += len(ops)
    mlines += [f"## {dev} — current ({len(ops)} операций)", "",
               "| Метод | Путь | Название | Теги |", "|---|---|---|---|"]
    for p, m, o in sorted(ops, key=lambda x: (x[0], x[1])):
        title = o.get("summary") or (o.get("description") or "")[:70]
        tags = ",".join(o.get("tags") or [])
        mlines.append(f"| {m.upper()} | `{p}` | {esc(title)} | {tags} |")
    mlines.append("")
open(os.path.join(ROOT, "METHODS.md"), "w").write("\n".join(mlines))

# ---------- docs/bas-ip-api.md ----------
L = ["# BAS-IP — справочник по API (актуальные версии)", "",
     "Документ описывает **текущие** (current) версии HTTP API оборудования BAS-IP.",
     f"Всего семейств: **{len(specs)}**, операций: **{total}**.", "",
     "Источник: спецификации OpenAPI, опубликованные на `developers.bas-ip.com`.", "",
     "## Содержание", ""]
for dev, d in specs:
    n = sum(len(ms) for ms in d["paths"].values())
    L.append(f"- [{dev}](#{dev}) — {n} операций")
L += ["", "> Условные обозначения: вложенные поля через `.`, элементы массива через `[]`.",
      "> Авторизация — HTTP Bearer (`Authorization: Bearer <token>`), если не указано иное.", ""]

# common auth/servers
srv = []
seen = set()
for dev, d in specs:
    for s in (d.get("servers") or []):
        k = (s.get("description"), s.get("url"))
        if k not in seen:
            seen.add(k); srv.append(s)
L += ["## Серверы", "",
      "| Описание | URL |", "|---|---|"]
for s in srv:
    L.append(f"| {esc(s.get('description'))} | `{esc(s.get('url'))}` |")
L += ["", "Локальный сервер устройства — фактический IP панели в вашей сети + `/api/v1`.",
      "Mock-сервер SwaggerHub — для тестов без железа.", ""]

for dev, d in specs:
    ops = [(p, m, o) for p, ms in d["paths"].items() for m, o in ms.items()]
    L += [f"## {dev}", "", f"Операций: **{len(ops)}**.", ""]
    # group by first tag
    groups = {}
    for p, m, o in ops:
        tg = (o.get("tags") or ["other"])[0]
        groups.setdefault(tg, []).append((p, m, o))
    for tg in sorted(groups):
        L += [f"### {dev} / {tg}", ""]
        for p, m, o in sorted(groups[tg], key=lambda x: (x[0], x[1])):
            title = o.get("summary") or ""
            desc = o.get("description") or ""
            L.append(f"#### `{m.upper()}` `{p}`")
            L.append("")
            if title: L.append(f"**{esc(title)}**"); L.append("")
            if desc:
                # strip leading markdown bullets that duplicate; keep as-is
                L.append(desc.strip()); L.append("")
            tags = ", ".join(o.get("tags") or [])
            sec = o.get("security")
            secs = ", ".join(sorted({k for s in (sec or []) for k in s})) if sec else "—"
            L.append(f"*Теги: `{tags}` · Авторизация: {secs}*")
            L.append("")
            # parameters
            params = o.get("parameters") or []
            if params:
                L += ["**Параметры**", "", "| Имя | Где | Обяз. | Тип | Описание |", "|---|---|---|---|---|"]
                for pr in params:
                    sch = pr.get("schema") or {}
                    L.append(f"| `{esc(pr.get('name'))}` | {esc(pr.get('in'))} | "
                             f"{'да' if pr.get('required') else 'нет'} | {esc(type_str(sch))} | "
                             f"{esc(pr.get('description'))} |")
                L.append("")
            # request body
            rb = o.get("requestBody")
            if isinstance(rb, dict):
                L += [f"**Тело запроса** ({'обязательно' if rb.get('required') else 'опционально'})", ""]
                for mt, mo in (rb.get("content") or {}).items():
                    L.append(f"Тип: `{mt}`")
                    L.append("")
                    sch = mo.get("schema") or {}
                    if sch.get("description"):
                        L.append(f"> {esc(sch['description'])}"); L.append("")
                    blk = schema_block(f"Схема тела запроса · {mt}", sch)
                    if blk: L.append(blk)
                    ex = example_of({mt: mo})
                    if ex:
                        L += ["<details><summary>Пример тела запроса</summary>", "",
                              "```json", ex, "```", "", "</details>", ""]
            # responses
            resp = o.get("responses") or {}
            if resp:
                L += ["**Ответы**", "", "| Код | Описание | Тип тела |", "|---|---|---|"]
                for code in sorted(resp, key=lambda c: (str(c).isdigit() and int(c) or 0, str(c))):
                    ro = resp[code] or {}
                    cts = ", ".join((ro.get("content") or {}).keys()) or "—"
                    L.append(f"| `{esc(code)}` | {esc(ro.get('description'))} | {esc(cts)} |")
                L.append("")
                for code in sorted(resp, key=lambda c: (str(c).isdigit() and int(c) or 0, str(c))):
                    ro = resp[code] or {}
                    for mt, mo in (ro.get("content") or {}).items():
                        sch = mo.get("schema") or {}
                        blk = schema_block(f"Схема ответа {code} · {mt} — {esc(ro.get('description'))}", sch)
                        if blk: L.append(blk)
                        ex = example_of({mt: mo})
                        if ex:
                            L += [f"<details><summary>Пример ответа {code} · {mt}</summary>", "",
                                  "```json", ex, "```", "", "</details>", ""]
            L.append("---")
            L.append("")

open(OUT, "w").write("\n".join(L))
print(f"specs: {len(specs)}, operations: {total}")
print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")
print(f"wrote {ROOT}/METHODS.md")
