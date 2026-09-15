"""Stats behind the @shannholmberg profile analysis.

LIMIT: 52 rows transcribed from the 2026-09-15 raw extraction. The median is the capture's
own figure (9,553), carried over rather than recomputed, because impressions on the capture
are timeline figures read at one moment and they keep climbing after. Topic labels are my
assignment, not the author's, so the topic table is the softest thing here.
"""
import statistics as st

# (date, type, impressions, likes, replies, reposts, bookmarks, media, topic)
D = [
 ("08-11","post",1807,14,8,1,None,"image","personal"),
 ("08-11","qt",22876,186,19,20,295,"image","marketing-engineer"),
 ("08-12","post",1831,16,None,1,20,"link","cta"),
 ("08-12","qt",39382,203,14,14,365,"image","ai-writing"),
 ("08-12","post",106743,587,26,40,889,"image","tool-reaction"),
 ("08-13","qt",20270,212,24,18,336,"carousel","ai-writing"),
 ("08-14","qt",27360,259,16,8,407,"image","agents"),
 ("08-15","qt",16823,185,7,11,205,"carousel","tool-reaction"),
 ("08-16","qt",69152,709,26,37,1009,"carousel","tool-reaction"),
 ("08-17","qt",30769,354,17,26,490,"image","second-brain"),
 ("08-19","qt",140457,1073,51,124,1865,"carousel","tool-reaction"),
 ("08-20","qt",3209,24,3,2,14,"video","agents"),
 ("08-20","qt",20936,294,14,30,442,"carousel","agents"),
 ("08-22","qt",3327,19,8,None,21,"carousel","tool-reaction"),
 ("08-23","post",566,3,None,None,None,"link","cta"),
 ("08-23","post",3503,52,6,4,62,"image","agency-work"),
 ("08-24","qt",3613,24,8,1,16,"carousel","other"),
 ("08-24","qt",14000,180,17,9,231,"carousel","second-brain"),
 ("08-25","post",554,5,None,None,1,"none","personal"),
 ("08-25","qt",3140,51,17,7,9,"video","agency-work"),
 ("08-25","qt",151596,832,28,58,1542,"carousel","skills-library"),
 ("08-26","qt",31057,315,22,23,531,"carousel","skills-library"),
 ("08-27","post",805,6,1,None,1,"link","cta"),
 ("08-27","post",7463,156,30,13,184,"image","agents"),
 ("08-28","post",2759,40,17,1,23,"image","other"),
 ("08-30","post",5253,43,10,2,93,"image","marketing-engineer"),
 ("08-31","post",798,None,None,None,None,"link","cta"),
 ("08-31","post",2647,18,4,None,10,"image","agents"),
 ("08-31","post",12666,206,26,13,190,"none","stack"),
 ("08-31","post",23880,308,49,16,429,"image","agents"),
 ("08-31","qt",546619,2473,143,68,1658,"carousel","stack"),
 ("09-01","qt",10416,89,10,4,118,"image","marketing-engineer"),
 ("09-01","qt",200950,1748,83,104,2626,"carousel","stack"),
 ("09-02","qt",6461,89,18,5,98,"image","other"),
 ("09-03","qt",3465,33,19,None,20,"carousel","marketing-engineer"),
 ("09-04","qt",180446,1235,59,94,2218,"carousel","tool-reaction"),
 ("09-07","qt",25486,172,36,10,200,"image","stack"),
 ("09-08","qt",5060,63,17,1,66,"carousel","agency-work"),
 ("09-08","qt",6295,35,13,None,12,"video","other"),
 ("09-08","qt",7118,82,17,4,48,"none","tool-reaction"),
 ("09-10","qt",14368,93,14,1,148,"none","tool-reaction"),
 ("09-10","qt",16546,101,16,6,174,"none","marketing-engineer"),
 ("09-10","article",257640,844,23,93,1998,"image","marketing-engineer"),
 ("09-11","post",448,4,2,None,None,"link","cta"),
 ("09-11","qt",3126,38,11,3,11,"video","agency-work"),
 ("09-11","qt",8690,91,14,8,83,"none","marketing-engineer"),
 ("09-12","qt",189705,1555,50,222,2630,"image","second-brain"),
 ("09-13","qt",25040,309,29,35,386,"carousel","stack"),
 ("09-13","qt",32012,418,44,43,465,"carousel","second-brain"),
 ("09-14","post",232,None,None,None,1,"link","cta"),
 ("09-14","qt",2319,35,14,2,26,"video","other"),
 ("09-14","qt",6536,109,20,8,120,"carousel","second-brain"),
]

MEDIAN = 9553          # from the capture
THRESH = 3 * MEDIAN    # 28,659

imp = lambda r: r[2]
n = len(D)
out = [r for r in D if imp(r) >= THRESH]

def group(idx, label):
    keys = sorted({r[idx] for r in D})
    print(f"\n{label:<16} {'n':>3} {'share':>6} {'median':>9} {'outliers':>9} {'reach share':>12}")
    total_imp = sum(imp(r) for r in D)
    for k in keys:
        rows = [r for r in D if r[idx] == k]
        o = [r for r in rows if imp(r) >= THRESH]
        share = sum(imp(r) for r in rows) / total_imp
        print(f"{k:<16} {len(rows):>3} {len(rows)/n:>5.0%} {st.median([imp(r) for r in rows]):>9,.0f} "
              f"{len(o):>9} {share:>11.0%}")

print(f"items {n} · median {MEDIAN:,} · outlier threshold {THRESH:,} · outliers {len(out)}")
print(f"total impressions {sum(imp(r) for r in D):,}")
top = sorted(D, key=imp, reverse=True)
print(f"top 10 carry {sum(imp(r) for r in top[:10])/sum(imp(r) for r in D):.0%} of all impressions")
print(f"top 5  carry {sum(imp(r) for r in top[:5])/sum(imp(r) for r in D):.0%}")

group(1, "TYPE")
group(7, "MEDIA")
group(8, "TOPIC")

print("\nbookmark-to-like ratio, the 8 biggest:")
for r in top[:8]:
    bm, lk = r[6], r[3]
    print(f"  {imp(r):>9,}  {r[8]:<20} bm/lk {bm/lk if bm and lk else float('nan'):.2f}")

cta = [r for r in D if r[8] == "cta"]
print(f"\ncta posts: n={len(cta)} median {st.median([imp(r) for r in cta]):,.0f} "
      f"max {max(imp(r) for r in cta):,} · all are link cards, all below median")
