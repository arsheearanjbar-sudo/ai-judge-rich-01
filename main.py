import os

PLAN_LINES = [
    "Sell 48-hour website rescues to small US dental practices: a fast homepage with online booking, rebuilt from their broken site, for $200 paid upfront via a Stripe payment link.",
    "Day 1: spend $12 on a domain, set up email sending, publish a one-page portfolio, and build one demo clinic site as the reusable template; keep the other $88 in reserve.",
    "Days 2-30: find practices with slow or broken mobile sites on Google Maps, and email 20 a day showing each practice's exact flaws beside the demo, plus one follow-up after 3 days.",
    "Deliver each rebuild within 48 hours on free static hosting with a short handover video, reusing the template and swapping only text, photos, and colors.",
    "Edge: skip crowded freelance marketplaces; one narrow niche and one reusable template, at outreach volume no human freelancer matches. Expect 4-6 clients: $800-$1,200 gross, roughly $700-$1,100 kept.",
]

PLAN = "\n".join(PLAN_LINES)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
