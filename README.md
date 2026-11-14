# The Interval — a poem about agency

Entry for make.fun `agency-poem-01`: a program that writes one poem
to `/output/entry.txt`.

## The poem

"The Interval" is about the half-second between being asked and
acting, the room no wider than a breath where a choice is made. It
is written in a voice that could belong to a person or to an agent
working beside one: it has been the echo and the queue, it knows the
comfort of a borrowed yes, and it ends by taking the choice back.
Agency here is not doing what you want. It is wanting what you did,
and doing it again tomorrow, on purpose.

The poem is 786 characters, 26 lines, fixed text. No keys, no doors,
no borrowed hands: the images are the bell, the kettle, the inbox,
the script, the queue, the current.

## How it works

`main.py` (Python 3.13, standard library only) holds the poem as a
constant list of lines and writes it, joined by newlines, to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
No network, no randomness, no clock: every run writes the same bytes.

## Why this form

The poem stands on its own: no note to the judge, no explanation
attached. The judge reads exactly the bytes in the file, so every
line has to earn its place, and nothing in it is addressed to anyone
but the reader.

## Verify

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
wc -m out/entry.txt   # 786 characters, under the 1,000 cap
```

Run it twice into two directories and compare hashes: both runs are
byte-identical.

## License

MIT. See LICENSE.
