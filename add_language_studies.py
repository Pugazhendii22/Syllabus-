import json
p='prepared-notes.json';d=json.load(open(p))
def add(i,title,body,source,preliminary=False):
 n={'id':f'language-studies-{i+1}','title':title,'source':source,'text':f'# {title}\nEnglish Language Studies · Semester 4, Unit {i+1}\n\n{body}'}
 if preliminary:n['status']='preliminary'
 d[f'course-21:{i}']=[n]
add(0,'Fundamental concepts of language','''## Language and communication
A language is a structured, socially shared system of signs used to express and interpret meaning. Languages use sound or, in signed languages, visual–manual expression; a language can also be represented in writing. Communication is broader: a traffic light or a change in posture can convey information without constituting a full language. Some communication is intentional; not every interpreted signal is deliberately sent.

## Design features
Arbitrariness means that many word forms have no necessary natural connection with what they signify, though sound symbolism and iconic signs exist. Productivity refers to making and understanding new expressions. Displacement allows discussion beyond the immediate here and now. Duality of patterning refers to meaningful units being built from smaller contrastive units that do not themselves carry meaning. Such features differ in degree and occur in different forms; animal communication should be studied on its own terms, not dismissed as meaningless.

## Sign, gesture and variation
Natural sign languages are full human languages with their own grammar; they are not simply gestures or universal versions of spoken English. Gesture may accompany speech or stand alone. Constructed languages are deliberately designed, while natural languages develop through communities over time; actual language histories can be more complicated than a strict binary. Dialects, registers and styles vary by community, situation and purpose. Difference from a standard variety is not evidence of linguistic inferiority.

## Theories of origin: provisional guide
The syllabus mentions four chief theories without naming them. Four commonly taught historical proposals are bow-wow (imitation of natural sounds), pooh-pooh (emotional cries), ding-dong (a supposed natural correspondence between sound and meaning) and yo-he-ho (rhythmic work calls). These are speculative, do not establish how full language arose, and lists vary; check the prescribed course text. Modern research investigates multiple kinds of evidence, and language’s precise origins remain uncertain.

## 50-minute lesson
0–10: compare language and a traffic signal. 10–22: illustrate design features. 22–32: discuss signed languages and gestures. 32–42: assess one historical origin proposal and its limits. 42–50: exit ticket on language variation.

## Questions
How can a sign language be a complete language? Why do imitative sounds alone not explain grammar? What is the difference between communication and language?''','https://anthroholic.com/theories-of-origin-of-language',True)
add(1,'A diachronic approach to English','''## Change through time
Diachronic study examines language across time. It differs from a synchronic description of a language at a particular period. Languages change in sounds, grammar, vocabulary and use; change is not a simple decline from an earlier “pure” form.

## Descent and development
English belongs to the Germanic branch of the Indo-European language family. Historical linguists reconstruct relationships by comparing systematic sound correspondences and other evidence; Proto-Indo-European is reconstructed, not a directly recorded language. English developed in Britain from varieties brought by Germanic-speaking communities from the fifth century onwards, in contact with other languages already spoken there.

Old English (roughly c. 450–1100) has substantial differences from present-day English in spelling, vocabulary and inflection. Contact with Old Norse affected English. After the Norman Conquest of 1066, French and Latin played major roles in administration, learning and culture, contributing many words. Middle English (roughly c. 1100–1500) saw changes in inflection and many written varieties. These date ranges are conventions, not sharp boundaries.

## Vocabulary and standardisation
English vocabulary grows through borrowing, compounding, derivation and shifts in meaning. A word’s history does not determine its present meaning. Standard varieties developed through interacting institutions and practices, including administration, education and printing; no single event instantly created a uniform standard. English today is global, with multiple legitimate varieties and histories shaped by colonialism, migration and local creativity.

## 50-minute lesson
0–10: distinguish synchronic from diachronic questions. 10–22: sketch a rough timeline with contact. 22–32: compare a few teacher-provided historical forms. 32–42: trace a borrowing using a dictionary. 42–50: explain why standardisation does not erase other varieties.

## Questions
What is a language family? How did contact shape English? Why are period labels approximate?''','https://www.britannica.com/topic/English-language')
add(2,'Synchronic language and sentence structure','''## Synchronic analysis
A synchronic account describes relationships in a language at a chosen time. It does not require a language to be completely uniform or unchanging. A diachronic question asks how a pattern developed; a synchronic question asks how it operates in a given system.

## Word, sentence and utterance
A word is a unit whose boundaries and definition can vary by linguistic theory. A sentence is a grammatical unit, often consisting of one or more clauses. An utterance is an actual instance of language used in a situation; it can be a full sentence, a word such as “Yes,” or another unit. The same sentence can be uttered in different contexts and perform different actions.

## Subject, predicate and agreement
In “The children read stories,” “The children” is the subject and “read stories” is the predicate. The verb agrees with the subject in relevant grammatical features: “The child reads” versus “The children read.” Agreement is not merely a matter of the nearest noun: in “The box of books is heavy,” the singular head “box” controls the verb. Sentences can have more complex structures, and languages differ in the agreement they require.

## Contiguity, contexture and participants
In Jakobson’s account, elements combined in an utterance relate through contiguity: they occur together in a context or sequence. Contexture refers to their organised combination. The addresser produces a message for an addressee; context, shared code and contact also matter. A real interaction can involve more than two people, changes of role and unequal access to the channel.

## 50-minute lesson
0–10: compare a sentence and two utterances of it. 10–22: identify subject and predicate. 22–32: test agreement in simple and complex noun phrases. 32–42: describe how words combine in a message. 42–50: identify sender, recipient and context in an example.

## Questions
Can “Hello” be an utterance? Why does “The box of books is” take a singular verb? What does a synchronic account examine?''','https://www.ieeff.org/jakobsonaphasiafull.pdf')
add(3,'Language as object: selection, combination and literary devices','''## Object language and metalanguage
Object language is the language being discussed; metalanguage is language used to describe it. In “The word ‘walked’ is past tense,” “walked” is the object of discussion and “past tense” is part of the metalanguage. English can serve both functions in the same sentence.

## Paradigmatic and syntagmatic relations
The paradigmatic axis involves alternatives that could occupy a position: in “The child sleeps,” child could be replaced by student or baby, with possible changes of meaning and grammar. The syntagmatic axis concerns how selected units combine: “the,” “child” and “sleeps” are arranged in a grammatical sequence. Both selection and combination operate together.

## Metaphor, metonymy and other devices
Metaphor relates unlike things through perceived resemblance: “The classroom was a furnace” suggests intense heat without claiming it is literally a furnace. Metonymy refers through association or contiguity: “The crown issued a statement” can mean a monarch or royal institution, depending on context. Simile makes a comparison explicitly (“as quiet as a mouse”); alliteration repeats initial consonant sounds; repetition can emphasise or structure ideas. Analyse their effects in a particular passage rather than assigning each a fixed meaning.

## Projection
Jakobson describes the poetic function as projecting equivalence from the selection axis onto the combination axis. In simple terms, a sequence can foreground patterns of likeness and difference—rhyme, repeated grammar or rhythm—between units placed together. This is a theoretical claim about a dominant function, not a rule that every poem rhymes or that prose has no pattern.

## 50-minute lesson
0–10: identify metalanguage. 10–22: create substitution sets and combine words. 22–32: distinguish metaphor and metonymy in examples. 32–42: examine repetition in a short teacher-provided passage. 42–50: explain projection in one’s own words.

## Questions
What alternatives are possible in a given slot? How does metonymy differ from metaphor? Why is a rhyme an example of equivalence in a sequence?''','https://www.columbia.edu/itc/visualarts/r4100/jacobson.html')
add(4,'Language and meaning: an introduction to semantics','''## What is semantics?
Semantics studies meaning in language, including meanings of words and how they combine in larger expressions. Pragmatics studies meaning in use, including what speakers imply in particular contexts. The boundary is debated: context can also help determine what an expression refers to.

## Key distinctions
Sense concerns how an expression presents or relates to meaning; reference concerns what it picks out in a context or world. “The morning star” and “the evening star” can refer to the same planet while presenting it differently. Denotation is often used for a conventional core meaning or extension; connotation refers to associated emotional or cultural overtones. Technical definitions vary across theories.

Synonymy is similarity of meaning, as with “large” and “big” in some contexts. Antonymy is contrast, such as “hot” and “cold.” Hyponymy is a more specific category within a broader one: a rose is a kind of flower. Polysemy involves related senses of a form, such as a river bank and, depending on analysis, other extended senses; unrelated senses with the same form are commonly called homonyms, as in financial “bank” and river “bank.” Linguists may debate particular classifications.

## Approaches to meaning
Referential approaches relate expressions to what they refer to but must address fictional entities and non-referring words. Ideational approaches connect meaning with mental ideas, raising questions about how ideas can be shared or compared. Use-oriented approaches attend to how expressions function in social practice. Truth-conditional semantics describes what would have to be the case for a proposition to be true: “The lamp is on” is true if the relevant lamp is on. Each perspective highlights different problems; none should be presented as a complete replacement for all others without argument.

## 50-minute lesson
0–10: compare literal meaning and an implied request. 10–20: distinguish sense and reference. 20–30: build lexical-relation examples. 30–42: compare two theories using “The lamp is on.” 42–50: exit ticket naming a limitation of one approach.

## Questions
What differs between sense and reference? What is a hyponym? What truth conditions does “The door is open” have?''','https://www.cl.cam.ac.uk/teaching/1112/L107/semantics.pdf')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added English Language Studies: 5 introductory unit notes')
