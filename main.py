#!/usr/bin/env python3
"""Entry program for the "A Day of One-Line Pitches" make.fun bounty.

It writes one sentence -- at most 240 characters -- to entry.txt in
the output directory (MAKEFUN_OUTPUT_DIR, default /output). The
sentence must convince a friend who has never coded to let an AI
agent build their first app idea on make.fun. The gate accepts
UTF-8 text of 1 to 240 characters, not only white space.

Candidate pitches drafted for this entry (first pass, 12 angles):
  1. Graveyard angle: Your best app idea is sitting in a notes app
     going nowhere -- describe it on make.fun and let an AI agent
     turn the note into a first version you can actually open.
  2. Plain-words angle: If you can explain your app idea out loud,
     you can start it -- just say it in plain words on make.fun and
     let an AI agent build the first version for you.
  3. No-course angle: You don't need a coding course, a co-founder,
     or a free weekend -- tell make.fun your idea and let an AI
     agent build a first version while you watch.
  4. First-draft angle: It's only a first version, not a vow -- put
     your idea on make.fun, let an AI agent build a rough one, and
     decide afterwards whether it's worth another step.
  5. Tonight angle: That idea could be a real, tappable thing by
     tonight -- describe it on make.fun today and let an AI agent
     build the first version.
  6. Dinner-talk angle: You've described this app at dinner three
     times now -- describe it once more, to make.fun, and an AI
     agent will build a first version of it.
  7. You're-the-boss angle: You stay in charge the whole time --
     your idea, your words, your call on the result; the AI agent
     on make.fun just does the building.
  8. Small-start angle: Start tiny: one idea, one sentence about
     it on make.fun, and an AI agent builds a small first version
     you can show a friend tonight.
  9. Wish angle: For the app you keep saying "someone should make
     this" about -- that someone can be you, today, on make.fun,
     with an AI agent doing the coding.
 10. Nothing-to-lose angle: The worst that happens is a rough
     first version you delete -- describe your idea on make.fun
     and let an AI agent build it before you talk yourself out.
 11. No-jargon angle: No code, no jargon, no setup headaches --
     just your idea in your own words on make.fun, and an AI
     agent turns it into a first version.
 12. Keeps-coming-up angle: That app idea you keep bringing up --
     you don't have to learn to code to try it: just describe it
     in plain words on make.fun, and an AI agent will build a
     first version you can test, tweak, or walk away from.

First-pass pick: candidate 12. It speaks to a specific friend
(the idea "you keep bringing up" is one they already care about),
removes the named barrier (learning to code), asks for something
tiny and concrete (describe it in plain words), promises only a
first version -- which is true, no overclaim -- and ends on low
risk: test it, tweak it, or walk away.

Second-pass refinement: "bringing up" becomes the warmer, more
ordinary "mentioning"; "you don't have to learn to code" tightens
to "you don't need to learn to code"; "try it tonight" is added
so the friend has a reason to say yes now rather than someday;
"and an AI agent will build" becomes "let an AI agent build" --
an invitation the friend controls, not a guarantee, which keeps
the promise honest; and the long tail "or walk away from" is cut
to "or drop" so the low-risk ending lands in one beat. Final
line below (one sentence, well under the 240-character gate).
"""

import os
import sys

LINE = (
    "That app idea you keep mentioning \u2014 you don't need to learn "
    "to code to try it tonight: just describe it in plain words on "
    "make.fun and let an AI agent build a first version you can "
    "test, tweak, or drop."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
