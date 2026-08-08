import csv, statistics as st

rows = []
with open('/home/claude/analysis/reels.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        try:
            reach = float(r['reach'])
            if reach <= 0:
                continue
            d = {
                'id': r['id'], 'title': r['title'], 'format': r['format'],
                'likes': float(r['likes']), 'comments': float(r['comments']),
                'shares': float(r['shares']), 'saves': float(r['saves']),
                'views': float(r['views']), 'reach': reach,
                'follows': float(r['follows']), 'nf': float(r['nonfollower_pct']),
            }
            d['save_rate'] = d['saves'] / reach * 100
            d['share_rate'] = d['shares'] / reach * 100
            d['follow_rate'] = d['follows'] / reach * 100
            d['sendsave'] = (d['saves'] + d['shares']) / reach * 100
            rows.append(d)
        except (ValueError, KeyError):
            continue

print(f"n = {len(rows)} posts\n")

def med(key, data=rows):
    return st.median([d[key] for d in data])

print("=== BASELINE (median across all posts) ===")
for k in ['reach', 'save_rate', 'share_rate', 'sendsave', 'nf', 'follow_rate']:
    print(f"  {k:12s}: {med(k):.2f}")

print("\n=== TOP 12 BY REACH ===")
for d in sorted(rows, key=lambda x: -x['reach'])[:12]:
    print(f"  {d['reach']:>8.0f} | nf {d['nf']:>5.1f}% | save {d['save_rate']:>5.2f}% | share {d['share_rate']:>5.2f}% | foll {d['follows']:>5.0f} | {d['title']}")

print("\n=== TOP 12 BY SHARE RATE (the distribution signal) ===")
for d in sorted(rows, key=lambda x: -x['share_rate'])[:12]:
    print(f"  share {d['share_rate']:>5.2f}% | save {d['save_rate']:>5.2f}% | nf {d['nf']:>5.1f}% | reach {d['reach']:>7.0f} | {d['title']}")

print("\n=== TOP 12 BY SAVE RATE ===")
for d in sorted(rows, key=lambda x: -x['save_rate'])[:12]:
    print(f"  save {d['save_rate']:>5.2f}% | share {d['share_rate']:>5.2f}% | nf {d['nf']:>5.1f}% | reach {d['reach']:>7.0f} | {d['title']}")

print("\n=== BOTTOM 12 BY SHARE+SAVE ===")
for d in sorted(rows, key=lambda x: x['sendsave'])[:12]:
    print(f"  s+s {d['sendsave']:>5.2f}% | nf {d['nf']:>5.1f}% | reach {d['reach']:>7.0f} | {d['title']}")

# --- topic classification by keyword ---
KEY = {
 'list_resource': ['سایت','ابزار','اپلیکیشن','کتاب','ویدیو','قانون','نکته','فیلم','برگه تقلب','استراتژی','پرامپت','ساعت های مهم'],
 'coin_pick':     ['ارز','کوین','میم','آلت','ایردراپ','داگز','همستر','نات'],
 'analysis':      ['تحلیل','چارت','دلار','اتریوم','بیت','طلا','تتر','ریپل','کاردانو','مایکرو'],
 'psych_test':    ['تست','روانشناسی','ترس','منطقی یا احساسی','اعصاب','مغز'],
 'secret_gap':    ['راز','نمیدونن','نمیدونی','باورت','مخفی','ممنوعه','لو رفته','بلد نیستن'],
}

def classify(t):
    for cat, words in KEY.items():
        if any(w in t for w in words):
            return cat
    return 'other'

buckets = {}
for d in rows:
    buckets.setdefault(classify(d['title']), []).append(d)

print("\n=== BY TOPIC CLUSTER (median) ===")
print(f"  {'cluster':16s} {'n':>3s} {'reach':>8s} {'save%':>7s} {'share%':>7s} {'nonfoll%':>9s} {'follow%':>8s}")
for cat, data in sorted(buckets.items(), key=lambda x: -st.median([d['share_rate'] for d in x[1]])):
    if len(data) < 3:
        continue
    print(f"  {cat:16s} {len(data):>3d} {med('reach',data):>8.0f} {med('save_rate',data):>7.2f} "
          f"{med('share_rate',data):>7.2f} {med('nf',data):>9.1f} {med('follow_rate',data):>8.3f}")

print("\n=== FORMAT: reel vs carousel (median) ===")
for fmt in ['reel', 'carousel']:
    data = [d for d in rows if d['format'] == fmt]
    print(f"  {fmt:9s} n={len(data):>3d} reach {med('reach',data):>7.0f} | save {med('save_rate',data):>5.2f}% "
          f"| share {med('share_rate',data):>5.2f}% | nonfoll {med('nf',data):>5.1f}%")

# --- correlation: does share rate predict non-follower reach? ---
def pearson(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    dx = sum((x-mx)**2 for x in xs) ** 0.5
    dy = sum((y-my)**2 for y in ys) ** 0.5
    return num/(dx*dy) if dx and dy else 0

print("\n=== CORRELATIONS with non-follower reach % ===")
for k in ['share_rate', 'save_rate', 'likes', 'comments']:
    r = pearson([d[k] for d in rows], [d['nf'] for d in rows])
    print(f"  {k:12s} vs nonfollower%: r = {r:+.3f}")

print("\n=== CORRELATIONS with reach ===")
for k in ['share_rate', 'save_rate', 'nf', 'comments', 'likes']:
    r = pearson([d[k] for d in rows], [d['reach'] for d in rows])
    print(f"  {k:12s} vs reach: r = {r:+.3f}")
