# Ammu’s teaching studio

A mobile-oriented study space for the Pondicherry University B.A. (Honours) English syllabus (2023–24 onward). Run with Python 3; the app itself requires no third-party packages:

```sh
cd teaching-studio
python server.py
```

Open http://localhost:8000 on the same machine. Choose a semester, subject and unit, then tap one of the visible buttons under **Choose notes to read**. Reading size, saved notes and bookmarks are stored in the current browser on that device; they do not sync.

## Install on a phone

On iPhone or iPad, open the deployed HTTPS site in Safari, tap **Share → Add to Home Screen → Add** (leave “Open as Web App” on if shown). On Android, use the app’s Add to home screen button or the browser menu. If an older shortcut shows the wrong icon, remove that shortcut and add it again after the updated site is deployed. Removing a shortcut can remove its separate browser storage: keep a copy of saved material first. Different browser and installed-app storage may not sync.

After a successful online visit and service-worker installation, the app shell and currently prepared notes can be used offline on supported browsers. External references and optional AI need the internet; browser storage may be cleared or evicted. Updates download when online and can require closing and reopening the app. Real iOS/Android install and offline behaviour has not been independently tested.

**Vercel:** This is a static deployment by default. `server.py` is not automatically run on Vercel, so `/api/status` and `/api/chat` are absent unless a separate server-side API is deployed and configured. Prepared notes do not need an API. Never put AI keys in client-side code or version control.

## Current content and limitations

As of this update, `prepared-notes.json` contains **316 note selections across 129 of 199 syllabus navigation sections**, including **31 explicitly preliminary selections**. This is an availability count, not a measure of complete coverage. Many topics and later semesters remain unfinished. Eight courses have no unit details extracted and must be checked against the source PDF.

Modern Poetry in Semester 6 now has introductory notes for all five units, including summaries of named poems and a five-part guide to The Waste Land. The syllabus attributes “An Expostulation” to C. D. Lewis, while a poem with that title is attributed to C. S. Lewis; the entry is preliminary until the assigned text is confirmed. Introduction to Linguistics in Semester 6 now has 17 introductory teaching selections across all five syllabus units, including examples and lesson sequences; these remain study drafts and should be checked before teaching. The Semester 5 internship now has four manually restored syllabus sections (A–D), with practical guidance. The printed 80 hours per credit and reference to Blackboard must be confirmed with the college. New Literatures in English has introductory notes for all five units, including poem summaries and story guides; Walcott’s syllabus title “Ruined House” requires confirmation against “Ruins of a Great House.” Full chapter- and scene-level coverage is still needed. Notes and lesson sequences are available for the extracted units of four Semester 1 courses, five Semester 2 courses and six Semester 3 courses, plus English Language Studies and all five units of American Literature I in Semester 4. American Literature I has context, five poetry selections, two essays, three novels and five short stories. The Scarlet Letter has a concise chapter-by-chapter guide; the other two novels have plot overviews. Indian Writing in English II now has notes for all five extracted units, including all named poems and the major fiction and drama. Iyengar, Naik and Clarinda are preliminary; the novels and plays still need full chapter- or scene-level coverage. Shakespeare has notes across all five extracted units, including act-by-act guides to the five plays. Its sonnet list and criticism chapters are unspecified in the syllabus: the four numbered sonnets are clearly marked practice examples, not a verified prescribed selection, and the criticism notes are preliminary introductions. Scene-by-scene coverage is still needed. Literary Criticism I now has introductory notes for all five extracted units in Semester 5; its Saussure / “Incest and Myth” attribution is explicitly preliminary because the intended text is unclear, and the Horace page or line range needs confirmation. Literature and Environment has introductory notes for all five extracted units, including ecocritical concepts, disaster narratives, the Anthropocene, four films and the named poems; the exact Animal Dreams and Slow Violence excerpts need confirmation. Indian Writing in English I has notes across all five extracted units: background and poetry in Unit I; three novel overviews in Unit II; stories in Unit III; novels and essays in Unit IV; and drama overviews in Unit V. The Captive Ladie and The Transplanted Wife have explicitly preliminary outlines; the latter is a story collection and the precise prescribed story has not been verified. The novels and plays still need full chapter- or scene-level coverage and deeper verification. Semester 3 additions include Literature and Visual Media, Content Writing, Functional English II, and Functional Communicative Writing. Several items are introductory or preliminary: in particular, detailed coverage of the assigned Functional English grammar textbook units has not been prepared. The course-17 Baudrillard, Baskaran, Neale and Ray/Pandian/Prasad outlines need verification against the precise assigned extracts. Course-21's list of origin theories is provisional because the syllabus does not name the four theories.

Literary notes vary in depth; novel and drama coverage is generally an overview rather than the full chapter-by-chapter or scene-by-scene explanation requested. The Amis “Heavy Water” outline is incomplete. The included notes are assistant-authored study drafts, not independently peer-reviewed: compare them with the actual assigned texts and editions and verify historical claims, interpretations and references before teaching. Do not assume that any unit with a note has all its prescribed readings fully covered.

The syllabus navigator was heuristically extracted from the original 202-page PDF, `syllabus.pdf`; course 30’s four content sections were later restored manually and are not labelled formal units in the source. The extraction may miss lines or boundaries. The original PDF and assigned editions are authoritative. `courses.json` contains the runtime data. Running `extract.py` may overwrite manual corrections; rerun `add_internship.py` after extraction to restore course 30 and its notes.

## Optional AI

The authored notes work without AI or a key. The optional AI tools require a real OpenAI-compatible provider and server-side configuration:

```sh
AI_API_KEY='your-key' AI_MODEL='your-model' AI_BASE_URL='https://your-provider.example/v1' python server.py
```

The server appends `/chat/completions` to the HTTPS base URL. Provider availability, free quotas and prices vary. Restart after changing configuration; do not share or commit keys. The simple server is for trusted local/private use, not public deployment without authentication, rate limiting and further security. AI output must be checked.

## Developer notes

The existing `prepared-notes.json` is the canonical accumulated dataset. **Do not run `create_notes.py` by itself:** it overwrites the file and erases later additions. Subsequent `add_*.py` and `expand_visual_media.py` scripts add or replace specific unit entries; rerunning them can overwrite manual changes to those units. Newest additions are `add_functional_ii.py`, `add_functional_writing.py` `add_language_studies.py`, `add_american_literature.py`, `add_american_fiction.py`, `add_indian_poetry_start.py`, `add_indian_unit1.py` `add_indian_novels.py`, `add_indian_remaining.py`, `add_environment.py`, `add_criticism_i.py`, `add_shakespeare.py`, `add_indian_ii.py`, `add_internship.py` `add_new_literatures.py` `add_linguistics.py` and `add_modern_poetry.py`.

Automated checks have included JavaScript syntax, JSON parsing, fake-DOM interaction tests, simulated PWA/service-worker tests and HTTP responses. Testing in a real mobile browser and assistive-technology accessibility testing have not yet been performed.
