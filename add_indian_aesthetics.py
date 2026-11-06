"""Add introductory teaching drafts for Semester 6 Indian Aesthetics."""
import json
P='prepared-notes.json'
with open(P,encoding='utf8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,preliminary=False):
 x={'id':id,'title':title,'source':source,'text':f'# {title}\nIndian Aesthetics · Semester 6\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: consult the prescribed edition, translation and course expectations; transliteration and interpretations vary.'}
 if preliminary:x['status']='preliminary'
 return x
d['course-37:0']=[
n('context','Indian aesthetics · Traditions and philosophical contexts', '''## What is aesthetics?
Aesthetics asks how art is made, experienced and evaluated. Indian traditions include theories of performance, poetry, music, visual art and religious practice developed over many centuries in Sanskrit and other languages. They do not form one unchanging doctrine or speak for every Indian artist.

## From Vedic contexts to later treatises
The syllabus asks for a survey from the Vedic period. Vedic hymns and ritual practices show interest in sound, recitation and imagery; later aesthetic treatises should not be treated as if all their concepts were already a single completed Vedic theory. Buddhist, Jain, Hindu, regional, courtly and other contexts contribute to the larger history.

## Useful terms
Rasa is aesthetic flavour or relish; bhava concerns a state or emotion represented or evoked. Dhvani concerns poetic suggestion. These belong to different debates and are not interchangeable. A philosophical claim about consciousness or perception may shape how a theorist explains art, but not every artistic work has the same religious purpose.

## Study method
For each theory ask: who proposes it, in what text and context, what problem does it answer, and where is the evidence? Compare a theatrical performance with a painting instead of assuming the same vocabulary works identically in every art form.''','0–10: ask what makes an experience aesthetic. 10–20: sketch a varied historical timeline. 20–30: define rasa and dhvani. 30–40: compare a poem and an image. 40–50: write one question about generalisation.','Why is “Indian aesthetics” a family of traditions rather than a single fixed doctrine? How do rasa and dhvani differ?','https://ebooks.inflibnet.ac.in/engp11/chapter/rasa/'),
n('citrasutra','Chitrasutra and the six limbs of painting', '''## Text and setting
The Chitrasutra (Citrasutra) is the painting section of the Vishnudharmottara Purana, traditionally located in chapters 35–43 of its third book. Dating and textual transmission are debated. Its discussion links visual practice with other arts and includes questions of form, colour and technique.

## Shadanga: six limbs
A widely taught list of the six limbs of painting is preserved in Yashodhara’s Jayamangala commentary on the Kamasutra; related principles are also discussed in the Chitrasutra. Do not assume the two texts present identical lists in identical wording.

1. Rupabheda: differentiation and recognition of forms.
2. Pramana: measure and proportion.
3. Bhava: expression of a state or feeling.
4. Lavanya-yojana: the effective arrangement of grace or charm.
5. Sadrishya: resemblance or correspondence to the subject.
6. Varnika-bhanga: handling or modulation of colour and pigment.

## Application
Choose an image and describe how form, proportion and colour work before judging whether it is “good.” Resemblance can mean more than photographic copying; the historical critic’s terms have contexts that need interpretation. Compare translations, especially where technical meanings differ.''','0–10: locate the painting treatise. 10–20: list six limbs. 20–30: use them to describe an image. 30–40: discuss resemblance and grace. 40–50: distinguish the textual sources of the list.','Name the six limbs and give an example of two. Why should the Jayamangala list not simply be attributed word-for-word to the Chitrasutra?','https://cec.nic.in/webpath/curriculum/Module/FART/Paper26/6/downloads/script.pdf')]
d['course-37:1']=[
n('natya','Bharata Muni · Natyashastra and performance', '''## Scope and attribution
The Natyashastra is a foundational Sanskrit treatise on dramaturgy and performance traditionally attributed to Bharata Muni. It is a layered historical text, so a precise single date and individual authorship should not be assumed. Versions and chapter numbering vary.

## Origin narrative and purpose
Its account of a “fifth Veda” explains theatre’s origins through a traditional narrative involving divine creation and performance. Present this as the text’s account, not independently verified historical fact. Theatre integrates speech, movement, music, setting and audience response, and can represent varied conditions of human life.

## Four modes of abhinaya
Angika: bodily gesture and movement. Vachika: speech and vocal expression. Aharya: costume, makeup and visual presentation. Sattvika: embodied expressions associated with inner states, such as tears or trembling. These modes interact in performance; avoid equating one gesture mechanically with one emotion across all traditions.

## The spectator
The treatise addresses dramatic construction, theatre space, music and performance as well as rasa. An audience interprets a coordinated artistic event, not simply a written plot. Later commentators differ over how that experience arises.''','0–10: define dramaturgy. 10–20: distinguish origin story and history. 20–30: demonstrate four modes without requiring personal disclosure. 30–40: analyse a performance. 40–50: recap.','What are the four modes of abhinaya? Why is the fifth-Veda narrative not the same kind of claim as a modern historical date?','https://ebooks.inflibnet.ac.in/engp11/chapter/natya-sastra/')]
d['course-37:2']=[
n('rasa-terms','Rasa theory · Formula, components and examples', '''## The central formulation
The rasa sutra associates the arising of rasa with the combination of vibhava, anubhava and vyabhichari bhava. Its precise terms for combination and arising were later interpreted differently. Rasa is aesthetic relish or flavour, not merely the character’s private emotion.

## Components
Vibhava: determinants, such as a person loved and a setting that stimulates longing. Anubhava: observable expressions, such as a glance, speech or gesture. Vyabhichari (sanchari) bhavas: passing states such as anxiety or hope. Sthayi bhava: a relatively enduring emotional disposition organised and developed in the work. These categories are analytical aids, not a psychological diagnosis.

## Eight and nine
A standard list of eight rasas is shringara (love), hasya (comic), karuna (pathos), raudra (fury), vira (heroic), bhayanaka (fear), bibhatsa (disgust) and adbhuta (wonder). Shanta (tranquillity) becomes important as a ninth in later traditions, with textual and scholarly debate about its status. Do not claim every edition has an identical list.

## Worked example
In a fictional farewell scene, separation and setting are determinants; pauses and tears are expressions; uncertainty and memory may be passing states. The scene may evoke pathos, but an audience’s response is not guaranteed and alternative readings remain possible.''','0–10: define aesthetic relish. 10–20: sort four components. 20–30: list the rasas. 30–40: analyse a farewell scene. 40–50: compare interpretations of the sutra.','How does a vibhava differ from an anubhava? Why is rasa not simply identical to a character’s emotion?','https://ebooks.inflibnet.ac.in/engp11/chapter/rasa/'),
n('three-commentators','Lollata, Shankuka and Bhatta Nayaka', '''## A shared question
How does the rasa sutra explain the relation between represented characters, performers and spectators? The syllabus spells the names Bhattlollatt, Shankuk and Bhattnayak; common forms are Bhatta Lollata, Shri Shankuka and Bhatta Nayaka. Much of their early commentary survives through later accounts, especially Abhinavagupta, so reconstructions differ.

## Lollata: production (utpatti-vada)
A common reconstruction places the developed emotion primarily in the represented character, secondarily attributed to the actor through performance. Determinants, expressions and passing states contribute to the development. Ask what it means to locate the process in the represented person rather than the spectator.

## Shankuka: inference (anumiti-vada)
Shankuka emphasises the spectator’s recognition through skilled representation and inference. A painted horse is a traditional analogy: the spectator recognises a represented horse without believing the painting is a living horse. Performance is neither ordinary reality nor simple ignorance of the difference.

## Bhatta Nayaka: enjoyment (bhukti-vada)
Nayaka rejects accounts that leave aesthetic experience merely in the actor or character. In a commonly presented interpretation, artistic representation generalises emotional material, enabling the spectator to relish it as rasa. This shifts attention to aesthetic enjoyment. His terminology and relationship to later universalisation theories require care.

## Comparison
Apply each model to the same scene. They are rival explanations, not three fixed steps every spectator must follow. Avoid claiming a lost author’s position with more certainty than surviving sources allow.''','0–10: set the shared question. 10–20: explain Lollata. 20–30: explore the painted-horse analogy. 30–40: explain Nayaka. 40–50: compare the models.','Which account emphasises inference? Why must reconstructions of early commentators be treated cautiously?','https://ebooks.inflibnet.ac.in/engp11/chapter/rasa/')]
d['course-37:3']=[
n('anandavardhana','Anandavardhana · Dhvani and poetic suggestion', '''## Text and central idea
Anandavardhana’s Dhvanyaloka argues for the importance of dhvani, often translated “suggestion” or “resonance,” in poetry. A poem can communicate more than its literal statement. The suggested meaning may be more important aesthetically than what is directly said.

## How suggestion works
Imagine a line describing an untouched cup beside an empty chair. Literally, it depicts objects; in context it may suggest absence or longing without naming either. This is a teaching example, not a quotation from the Dhvanyaloka. Interpretation must be supported by the work’s language and context; it is not permission to invent any meaning whatsoever.

## Varieties
Discussions commonly distinguish suggestion of an idea (vastu-dhvani), a figure (alankara-dhvani) and aesthetic mood (rasa-dhvani). Rasa-dhvani becomes especially important in later criticism. The reader or listener’s sensitivity and familiarity with language and conventions matter.

## Relation to rasa
Dhvani describes suggestion in language; rasa describes aesthetic relish. They are related but not synonyms. Abhinavagupta later wrote the Locana commentary on the Dhvanyaloka, linking these debates with his wider aesthetic theory.''','0–10: distinguish literal and suggested meanings. 10–20: introduce Dhvanyaloka. 20–30: discuss the example. 30–40: compare three kinds of suggestion. 40–50: explain dhvani versus rasa.','How can a poem suggest absence without stating it? Why are dhvani and rasa related but not identical?','https://philosophy.institute/aesthetics/dhvani-soul-indian-poetic-expression/'),
n('abhinava','Abhinavagupta · Manifestation and aesthetic relish', '''## Texts and context
The Kashmiri thinker Abhinavagupta commented on the Natyashastra in the Abhinavabharati and on Anandavardhana’s Dhvanyaloka in the Locana. He draws on earlier aesthetic debates and his own philosophical context; do not collapse all his ideas into those of his predecessors.

## Manifestation (abhivyakti)
His account is often described as abhivyakti-vada: performance makes an aesthetic experience manifest for a responsive spectator. The represented circumstances, actions and changing states help evoke an enduring disposition as rasa. This is not simply copying an actor’s personal feelings.

## Generalisation and sahridaya
Sadharanikarana, often rendered generalisation or universalisation, helps explain how dramatic particulars can be experienced beyond the spectator’s immediate private interests. A sahridaya is a responsive, attuned reader or spectator. “Universal” here is a theoretical claim about aesthetic experience; actual audiences may differ in knowledge, access and response.

## Shanta and comparison
Abhinavagupta influentially defends the rasa of tranquillity, shanta, in a debated tradition. Compare his manifestation account with Bhatta Nayaka’s enjoyment and Anandavardhana’s suggestion. Avoid claiming that tranquillity was simply invented by one writer or that every spectator must experience the same rasa.''','0–10: identify commentaries. 10–20: explain manifestation. 20–30: discuss generalisation. 30–40: compare three theorists. 40–50: evaluate the idea of a single ideal spectator.','What does sadharanikarana try to explain? How does manifestation differ from a claim that a spectator literally becomes the character?','https://ebooks.inflibnet.ac.in/engp11/chapter/rasa/')]
d['course-37:4']=[
n('coomaraswamy','Ananda K. Coomaraswamy · Art, craft and tradition', '''## Reading scope
The syllabus names A. K. Coomaraswamy without specifying an essay. This is an introduction to themes across his writings, not a summary of an identified prescribed passage; confirm the text and page range.

## Art and making
Coomaraswamy wrote on South Asian art history, craft and symbolism. He challenged a narrow separation of fine art from skilled making, and criticised modern industrial conditions that sever workmanship from meaningful use. His accounts often connect an object’s form, purpose and symbolic or philosophical context.

## Tradition and the artist
He valued traditional artistic knowledge and was critical of treating individual novelty as the sole measure of artistic worth. Ask how apprenticeship, technique, community, patronage and inherited forms contribute to making. At the same time, artists and craftspeople make choices; traditional work should not be assumed to be completely anonymous or unchanging.

## Critical perspective
His contrasts between a spiritual “East” and industrial modernity can be questioned when they generalise diverse histories or idealise the past. Read a specific work and its date before asserting a uniform position across his career. Compare his emphasis on tradition and craft with Tagore’s discussion of personality and expression.''','0–10: locate writer and reading. 10–20: compare art and craft. 20–30: examine a useful designed object. 30–40: test claims about tradition. 40–50: contrast with Tagore.','Why does craft matter to Coomaraswamy’s account? What is the risk of treating tradition as static?','https://arthistorians.info/coomaraswamya/',True),
n('tagore-aesthetics','Rabindranath Tagore · Art, personality and surplus', '''## Reading scope
The syllabus names Tagore without identifying a work. The discussion uses ideas associated with “What is Art?” in Personality: Lectures Delivered in America (1917); confirm whether this is the assigned essay. It is an introductory guide, not a substitute for the text.

## Art beyond immediate utility
Tagore argues that human beings possess emotional energy beyond what is required for self-preservation. This “surplus” seeks expression in art. He relates artistic creation to personality, feeling and the human relationship with the world rather than treating a work as mere factual information.

## Expression and form
Art does not simply report an object; through form it communicates a felt relationship with experience. Emotion alone is not a finished work: language, rhythm, image or another medium shapes expression. A reader can ask how an artwork brings an individual perspective into a relation with others.

## Questions and comparison
Compare Tagore’s emphasis on personality with Coomaraswamy’s critique of individualistic originality, without pretending that either thinker is reducible to a slogan. Scholars have also asked whether an individual-focused account adequately explains collective artistic creation. Examine Tagore’s historical language critically, including claims about gender in the essay.''','0–10: identify the essay and syllabus uncertainty. 10–20: define surplus. 20–30: discuss form and feeling. 30–40: compare collective and individual creativity. 40–50: compare Tagore with Coomaraswamy.','What does Tagore mean by surplus emotional energy? How might a theory of individual expression address collective art?','https://ebooks.inflibnet.ac.in/engp11/chapter/rabindranath-tagore-and-indian-aesthetics/',True)]
with open(P,'w',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Added',sum(len(v) for k,v in d.items() if k.startswith('course-37:')),'Indian Aesthetics selections across five units')
