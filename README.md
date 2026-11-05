# Ammu’s teaching studio

A mobile-oriented study space for the Pondicherry University B.A. (Honours) English syllabus (2023–24 onward). Run with Python 3; the app itself requires no third-party packages:

```sh
cd teaching-studio
python server.py
```

Open http://localhost:8000 on the same machine. Choose a semester, subject and unit, then tap one of the visible buttons under **Choose notes to read**. Reading size, saved notes and bookmarks are stored in the current browser on that device; they do not sync.

## Current content and limitations

As of this update, `prepared-notes.json` contains **150 note selections across 86 of 195 extracted unit pages**, including **15 explicitly preliminary selections**. This is an availability count, not a measure of complete coverage. Many topics and later semesters remain unfinished. Nine courses have no unit details extracted and must be checked against the source PDF.

Notes and lesson sequences are available for the extracted units of four Semester 1 courses, five Semester 2 courses and six Semester 3 courses, plus English Language Studies and all five units of American Literature I in Semester 4. American Literature I has context, five poetry selections, two essays, three novels and five short stories. The Scarlet Letter has a concise chapter-by-chapter guide; the other two novels have plot overviews. Indian Writing in English I has four initial poetry notes in Unit I only; that unit and all its other units remain incomplete. Semester 3 additions include Literature and Visual Media, Content Writing, Functional English II, and Functional Communicative Writing. Several items are introductory or preliminary: in particular, detailed coverage of the assigned Functional English grammar textbook units has not been prepared. The course-17 Baudrillard, Baskaran, Neale and Ray/Pandian/Prasad outlines need verification against the precise assigned extracts. Course-21's list of origin theories is provisional because the syllabus does not name the four theories.

Literary notes vary in depth; novel and drama coverage is generally an overview rather than the full chapter-by-chapter or scene-by-scene explanation requested. The Amis “Heavy Water” outline is incomplete. The included notes are assistant-authored study drafts, not independently peer-reviewed: compare them with the actual assigned texts and editions and verify historical claims, interpretations and references before teaching. Do not assume that any unit with a note has all its prescribed readings fully covered.

The syllabus navigator is automatically extracted from the original 202-page PDF, `syllabus.pdf`. The extraction is heuristic and may miss lines or unit boundaries. The original PDF and assigned editions are authoritative. `courses.json` contains the extracted syllabus at runtime; `extract.py` can regenerate it from `syllabus.txt`.

## Optional AI

The authored notes work without AI or a key. The optional AI tools require a real OpenAI-compatible provider and server-side configuration:

```sh
AI_API_KEY='your-key' AI_MODEL='your-model' AI_BASE_URL='https://your-provider.example/v1' python server.py
```

The server appends `/chat/completions` to the HTTPS base URL. Provider availability, free quotas and prices vary. Restart after changing configuration; do not share or commit keys. The simple server is for trusted local/private use, not public deployment without authentication, rate limiting and further security. AI output must be checked.

## Developer notes

The existing `prepared-notes.json` is the canonical accumulated dataset. **Do not run `create_notes.py` by itself:** it overwrites the file and erases later additions. Subsequent `add_*.py` and `expand_visual_media.py` scripts add or replace specific unit entries; rerunning them can overwrite manual changes to those units. Newest additions are `add_functional_ii.py`, `add_functional_writing.py` `add_language_studies.py`, `add_american_literature.py`, `add_american_fiction.py` and `add_indian_poetry_start.py`.

Automated checks have included JavaScript syntax, JSON parsing, fake-DOM interaction tests and HTTP responses. Testing in a real mobile browser and assistive-technology accessibility testing have not yet been performed.
