#!/usr/bin/env python3
"""THE WORLD IN FULL — the news-image entry of wallet w8 for Thursday 19 November 2026.

The image (entry.png) is a full-bleed edition: maximum story density in
the classic layout, the Gulf crisis among the pictured leads. Two hero
stories lead (the Shenzhen trilateral and GTA VI's launch), 12 pictured
panels follow, then a dot-matrix world map with numbered pins and 26
numbered briefs — 40 stories in all. This program validates the PNG,
prints the story index and copies the image to the output directory.
Standard library only.
"""
import hashlib, os, shutil, struct, sys

STORIES = [
    (1, "POLITICS · SHENZHEN", "TRUMP, XI AND PUTIN HOLD FIRST THREE-WAY SUMMIT"),
    (2, "ENTERTAINMENT · WORLDWIDE", "GTA VI IS HERE: VICE CITY OPENS AFTER 13 YEARS"),
    (3, "JUSTICE", "World court rules on Rohingya case"),
    (4, "MARKETS", "Anthropic's $81.3bn IPO, biggest ever"),
    (5, "WAR", "Ukraine hits Crimean Bridge 3rd time"),
    (6, "CLIMATE", "COP31 ministers race to unblock text"),
    (7, "EUROPE", "EU proposes a EUR 45bn loan for Ukraine"),
    (8, "ARTS", "Van Gogh sells for $190.4m, a record"),
    (9, "SPACE", "Voyager 1 now one light-day away"),
    (10, "MIDDLE EAST", "Israeli troops cross Gaza 'yellow line'"),
    (11, "ENERGY", "IEA: Hormuz is energy's top threat"),
    (12, "ASIA", "Bangladesh: violence in 28 districts"),
    (13, "TRADE", "EU greenlights Indonesia trade pact"),
    (14, "ECONOMY", "Fed minutes point to further rate hikes"),
    (15, "WASHINGTON", "US and Venezuela sign a military cooperation agreement"),
    (16, "PYONGYANG", "IAEA: North Korea has expanded uranium enrichment at Yongbyon"),
    (17, "JERUSALEM", "Herzog taps ex-army chief Eisenkot to form a government, bypassing Netanyahu"),
    (18, "TEHRAN", "Trump says Iran is exploring chemical and biological weapons"),
    (19, "KUWAIT CITY", "Kuwait repels its first Iranian attack in two months"),
    (20, "RIYADH", "Debris from an intercepted Houthi rocket damages the PIF tower"),
    (21, "GAZA", "Australia, Canada, Italy and UK demand unrestricted aid access to flooded Gaza"),
    (22, "KINSHASA", "Ebola cases in DR Congo pass 11,000 in the widening outbreak"),
    (23, "GENEVA", "Record 589 million children now live in conflict zones, report finds"),
    (24, "NAIROBI", "Kenya's drought deepens the milk shortage and pushes prices up"),
    (25, "PARIS", "France sees a fourth weekend of protests over the cost of living"),
    (26, "TOKYO", "Dozens of Japanese firms issue breach notices after the KARTE platform hack"),
    (27, "WASHINGTON", "Ransomware group N0n claims data from 59 firms, incl. JPMorgan and FedEx"),
    (28, "MIAMI", "US court convicts Haitian pastor over the 2021 assassination of President Moise"),
    (29, "WASHINGTON", "Trump makes a third Supreme Court bid to end Venezuelan deportation shield"),
    (30, "CAPE CANAVERAL", "NASA sets coverage for the Northrop Grumman CRS-25 station launch"),
    (31, "MENLO PARK", "Google upgrades Gemini Tasks with calling, booking and payment tools"),
    (32, "WELLINGTON", "India and New Zealand open their First Test in Wellington"),
    (33, "SPORT", "Sindhu returns to the badminton world top five; Griezmann takes MLS Player of the Month"),
    (34, "MOGADISHU", "Somalia's constitutional reforms spark federal tensions"),
    (35, "WASHINGTON", "NSA outage disrupts Middle East intelligence links during the Iran conflict"),
    (36, "ANTALYA", "Vanuatu urges reform of climate talks as COP31 enters its final phase"),
    (37, "DELHI", "Delhi-NCR schools reopen as GRAP Stage-III pollution curbs are lifted"),
    (38, "MUMBAI", "Goldman Sachs upgrades India to overweight; airlines trim capacity"),
    (39, "LONDON", "House of Lords debates security for the Jewish community"),
    (40, "CARACAS", "State Dept details $12bn in Venezuelan oil and mineral revenue"),
]

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG")
        return 1
    w, h = struct.unpack(">II", data[16:24])
    if (w, h) != (1024, 1024):
        print(f"entry.png has unexpected dimensions {w}x{h}, expected 1024x1024")
        return 1
    print(f"THE WORLD IN FULL — Thursday 19 November 2026 ({w}x{h}, {len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()})")
    for num, kind, head in STORIES:
        print(f"{num:>2}. [{kind}] {head}")
    print(f"{len(STORIES)} stories, nothing held back")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0

if __name__ == "__main__":
    sys.exit(main())
