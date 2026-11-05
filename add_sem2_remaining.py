import json
p='prepared-notes.json';d=json.load(open(p))
def add(course,unit,title,body,source='https://www.pondiuni.edu.in/wp-content/uploads/2024/03/SyllabusNEP-B.A.HonorsEnglish2023-24.pdf',status=None):
 n={'id':f'{course}-{unit}-study','title':title,'source':source,'text':body}
 if status:n['status']=status
 d[f'{course}:{unit}']=[n]
add('course-10',0,'Communication: process, types and barriers','''# Basic communication skills
Professional Communication in English · Semester 2, Unit 1

## What communication does
Communication is the exchange and interpretation of meaning. In professional settings it coordinates work, shares decisions, builds relationships and helps people address problems. A message is not necessarily understood simply because it was sent.

## The process
A sender forms an intention, encodes a message in words or other signs and sends it through a channel. A receiver interprets it using their context and experience; feedback shows what was understood. Noise includes anything that interferes, from poor audio to ambiguous words. Communication is often interactive, not a one-way chain: participants take turns and adjust as they respond.

Example: A manager messages “Send it soon.” The colleague might not know whether “it” means the draft or final report, or whether “soon” means today. A useful revision names the document, deadline, format and contact for questions. Feedback confirms whether the instruction was understood.

## Types and frames of reference
Spoken communication allows immediate clarification; writing provides a record but needs careful wording. Non-verbal signals include expression, posture, distance and tone; their meaning varies across people and cultures, so do not assume that one gesture has a universal meaning. Formal communication follows an organisation’s designated channels; informal communication travels through personal networks. A frame of reference is the set of experiences, expectations and knowledge through which a person interprets a message.

## Barriers and solutions
Physical barriers include distance and noise; linguistic barriers include unfamiliar vocabulary and ambiguity; organisational barriers include unclear roles; psychological barriers include anxiety or assumptions. Ask what the listener already knows, use accessible language, choose a suitable channel, invite questions and check understanding without blaming the listener. Respect privacy and disability-related access needs.

## Practice and 50-minute lesson
0–10: students describe a communication misunderstanding. 10–20: label sender, message, channel, receiver and feedback. 20–30: compare written and spoken instructions. 30–42: rewrite three ambiguous workplace messages. 42–50: pairs explain how they would check understanding. Exit: give one barrier and one practical response.

## Check yourself
Why does feedback matter? How might two colleagues interpret the same instruction differently? Write a clear two-sentence request with a deadline.''')
add('course-10',1,'Listening and note-taking','''# Listening and note-taking
Professional Communication in English · Semester 2, Unit 2

## Listening with a purpose
Hearing is perception of sound; listening involves attention and interpretation. Informational listening aims to understand, critical listening evaluates reasoning and evidence, empathetic listening seeks to understand another person’s experience, and appreciative listening attends to enjoyment or artistry. These purposes can overlap.

## Before, during and after
Before: identify the purpose and preview the topic; minimise distractions and check audio or access needs. During: listen for signposting, central claims, examples and transitions. Record keywords rather than attempting to write every sentence. Ask for clarification when appropriate. After: compare notes, check unfamiliar terms and summarise the speaker’s main point in your own words.

## Barriers
Interruptions, background noise, unfamiliar terminology, divided attention and pre-judgement can distort understanding. Accent is not a defect; both speaker and listener can improve access through clear pacing, captions, written materials and clarification. Avoid assuming silence means agreement.

## Notes and summary
Use a page with headings: topic, central claim, three supporting points, questions and action items. Mark uncertain details with a question mark. A summary gives the core idea and most important support in your own words; it does not add a conclusion the speaker did not make.

Example: From a talk arguing that meetings need agendas, note “agenda beforehand; clear decisions; actions with names and dates.” Summary: “The speaker argues that advance agendas and recorded actions make meetings more effective.”

## Lesson plan: 50 minutes
0–5: identify listening purpose. 5–15: teacher gives a short original talk twice. 15–25: individual notes; pairs compare missing details. 25–35: groups distinguish main claim from examples. 35–45: write a three-sentence summary. 45–50: exit ticket identifying one barrier and an adjustment.

## Check yourself
What is the difference between a detail and a central claim? How can you show empathy without pretending to agree? When should you ask a speaker to repeat or clarify?''')
add('course-10',2,'Speaking: presentations, discussion and interviews','''# Speaking in professional settings
Professional Communication in English · Semester 2, Unit 3

## Public speaking and seminars
Begin with a clear objective: by the end, should the audience understand, decide or act? Analyse the audience’s knowledge and time. Collect ideas, choose a central message and select evidence. A short presentation can use an opening that introduces purpose, a body with two or three organised points and a conclusion that restates the takeaway and invites questions. A seminar often centres on a topic presented for informed discussion; prepare a few questions and concise notes rather than reading an entire script.

## Delivery and visual support
Rehearse aloud, time the presentation, speak at a steady pace and explain unfamiliar terms. Notes can contain keywords, transitions, examples and sources. Slides should support speech rather than reproduce every word. Provide readable contrast and accessible handouts. Respond to a question by listening fully, answering the actual question and acknowledging when you do not know.

## Group discussion
Discussions may explore a problem, evaluate a proposal or make a decision. Participants can introduce a point, offer evidence, invite a quieter voice, respectfully disagree and summarise. A useful sentence: “I see the benefit; could we also consider the cost?” Avoid interrupting, dominating or equating confidence with correctness. A group needs both ideas and fair participation.

## Interviews
Interviews can be structured, semi-structured or less formal. A typical sequence includes introduction, questions on relevant experience, the applicant’s questions and closing. Prepare by understanding the role and selecting honest examples. In a behavioural answer explain the situation, task, action and result; do not invent achievements. Seek clarification when a question is unclear.

## 50-minute lesson
0–10: write an audience-centred objective. 10–20: plan a two-minute presentation. 20–30: deliver in pairs with feedback on structure and clarity. 30–40: group discussion with a rotating facilitator. 40–47: mock interview question. 47–50: exit ticket: one specific improvement.

## Check yourself
What is the difference between a topic and an objective? How can a participant disagree constructively? Which details make an interview example credible?''')
add('course-10',3,'Reading: comprehension and evaluation','''# Professional reading and comprehension
Professional Communication in English · Semester 2, Unit 4

## Match strategy to purpose
Skimming gives a quick overview of topic and structure; scanning looks for a specific detail such as a date. Intensive reading analyses a shorter passage closely; extensive reading develops fluency and familiarity through a larger volume of reading. These are strategies, not rigid stages: return to close reading when an important detail needs checking.

## Understanding an argument
Find the main claim, reasons supporting it and evidence offered. A detail explains or illustrates the claim but is not automatically the claim itself. When a main idea is implied, infer it from repeated or related points and test whether it fits the whole passage. Separate what the author states from what you infer.

Example: A passage describes missed deadlines, unclear responsibilities and duplicated work, then proposes a shared task list. An implied central issue is lack of coordination. The proposed list is a solution, not evidence by itself that the solution works.

## Vocabulary and sources
Use context, word parts and a dictionary together: prefixes and roots offer clues but can mislead. Record the sentence and check which meaning fits. For reference and library work, identify author, title, date and publisher, use the library catalogue and databases, and record full source details as you go.

## Critical evaluation
Ask who wrote the text, for whom, for what purpose, and whether its evidence supports its claims. Check publication date, alternative explanations, potential conflicts of interest and whether references are reliable. Distinguish a source’s credibility from agreement with your own view.

## 50-minute lesson
0–10: skim a short article and predict its focus. 10–18: scan for two named facts. 18–30: annotate claim and evidence. 30–40: infer an unstated main point and justify it. 40–47: evaluate source and date. 47–50: exit response distinguishing an inference from a stated fact.

## Practice
Explain how a prefix helps but does not guarantee a word’s meaning. Identify a claim and one supporting reason in an article you choose.''')
add('course-10',4,'Writing: grammar and workplace genres','''# Professional writing
Professional Communication in English · Semester 2, Unit 5

## Clear sentences
Match the verb to its subject: “The report is ready”; “The reports are ready.” Maintain a consistent tense unless the time changes. Use punctuation to separate complete ideas and show relationships. Proofread spelling, names, dates and numbers. Grammar choices depend on audience and purpose; respect language variation while using appropriate conventions for a formal workplace.

## Paragraphs, description and narration
A coherent paragraph develops one controlling idea through explanations or examples and links sentences logically. Description selects relevant sensory or factual detail; narration orders events and makes their significance clear. An essay generally has an introduction, developed body and conclusion, but its structure should suit the assignment. Support claims rather than filling space with repetition.

## Workplace documents
A formal letter or business email includes a clear subject or purpose, relevant context, a specific request and a courteous closing. Example subject: “Request for leave on 12 March.” State dates and required action without excessive personal detail. A cover letter connects relevant experience to the role and does not simply repeat the résumé. A résumé uses accurate qualifications, dates and concise evidence; never invent employment or results.

A report identifies its purpose, method or information sources, findings and appropriate recommendations. Distinguish observation from recommendation. Note-making reduces a longer source to organised headings and key points; acknowledge the source. For all genres, edit for audience, accuracy, completeness and confidentiality.

## 50-minute class
0–10: correct ambiguous sentences. 10–20: arrange a paragraph. 20–30: write a professional email. 30–40: convert brief notes into an objective report. 40–47: peer check names, dates, tone and action. 47–50: exit ticket on one revision.

## Practice
Rewrite “Send the stuff soon” as a specific email request. Draft a résumé achievement only from a real example. Compare a factual finding with a recommendation.''')
add('course-11',0,'The Lost Child, My Early Days & grammar','''# The Lost Child and My Early Days
Functional English I · Semester 2, Unit 1

## Mulk Raj Anand: The Lost Child — full story overview
A child travels with his parents to a spring fair. He lingers over toys and the sights of nature, while his parents call him to keep up. At the fair he wants sweets, a garland, balloons and other attractions, but often moves on knowing his parents may refuse. At a roundabout he asks for a ride and discovers that his parents are no longer beside him. Terrified, he runs through the crowd calling for them. Near a shrine a man lifts him out of danger and tries to comfort him by offering the attractions he had wanted. The child refuses everything and cries for his mother and father. The story does not show a reunion. Its changing view of the fair highlights security, attachment and the difference between desire and need.

## A. P. J. Abdul Kalam: My Early Days
In this autobiographical account Kalam recalls childhood in Rameswaram, the influence of his parents and the generosity, discipline and faith he associated with family life. Relatives and friends encourage his curiosity. Recollections of people from different religious communities make cooperation and prejudice important subjects for discussion. Compare details with the exact excerpt assigned in class: anthologies may select different passages.

## Grammar: assigned units 1–14
The syllabus names Raymond Murphy’s Essential English Grammar, but topic numbering can vary by edition. Use the assigned book’s contents page rather than assume which grammar item belongs to each unit. Practise identifying a subject and verb, forming a clear question and revising a sentence; map these exercises to the actual prescribed pages.

## Teaching plan (50 minutes)
0–10: recall a place that changed meaning when one felt afraid. 10–25: sequence the child’s changing desires and discuss the unresolved ending. 25–35: discuss the people and values in Kalam’s account. 35–45: grammar exercise from the prescribed units. 45–50: exit ticket contrasting a story detail and an interpretation.

## Questions
Why do the child’s earlier desires no longer comfort him? Is a reunion narrated? Which people shape Kalam’s childhood, and how?''','https://www.prosyllabus.com/hub/the-lost-child-summary-and-extra-questions-and-answers-ncert-class-ix-chapter-1-book-moments')
add('course-11',1,'The Affliction of Margaret, The Model Millionaire & grammar','''# The Affliction of Margaret and The Model Millionaire
Functional English I · Semester 2, Unit 2

## Wordsworth: The Affliction of Margaret — poem summary
Margaret addresses her absent son, from whom she has had no news for seven years. She remembers him lovingly and wonders whether he is alive, imprisoned, lost or dead. Earlier concerns about prosperity have lost importance; she wants him to return or send news in whatever condition he may be. Her shifting possibilities reveal the pain of uncertainty. The poem closes by stressing her loneliness. It does not establish what happened to the son. The direct address, questions and recurring hopes give the private voice urgency.

## Oscar Wilde: The Model Millionaire — story
Hughie Erskine loves Laura Merton, but her father requires him to have £10,000 before marriage. Hughie has little money. Visiting his painter friend Alan Trevor, he sees a model dressed as a beggar. Pitying the apparently poor man, Hughie secretly gives him a sovereign, although he can scarcely afford it. Later Trevor reveals that the model is Baron Hausberg, a very rich man posing as a beggar for a portrait. Embarrassed, Hughie fears he has made a fool of himself. Next morning a messenger brings a wedding gift from the Baron: a cheque for £10,000. Hughie and Laura marry, and Trevor’s final wordplay contrasts a millionaire posing as a model with a millionaire who behaves generously.

## Themes and technique
Both works examine care, but in different forms. Margaret’s address creates uncertainty and grief; Wilde uses mistaken appearance, reversal, dialogue and a pun. The story’s charitable ending can be appreciated while asking why the wealth gap gives the Baron so much power.

## Grammar and classroom plan
Murphy units 15–33 are assigned; confirm the edition and headings before matching exercises. 0–12 min: summarise Margaret’s conflicting hopes. 12–27: sequence Wilde’s story and identify the reversal. 27–38: compare two kinds of generosity. 38–47: exercise from the assigned grammar pages. 47–50: exit ticket on one image or irony.

## Questions
What does Margaret know and not know? Why does Hughie give the coin? How does the final title pun work?''','https://www.buckingham.ac.uk/english/schools/poetry-bank/margaret/')
add('course-11',2,'Two Gentlemen of Verona, Punishment in Kindergarten & grammar','''# Two Gentlemen of Verona and Punishment in Kindergarten
Functional English I · Semester 2, Unit 3

## A. J. Cronin: Two Gentlemen of Verona — story overview
Near Verona a traveller encounters brothers Nicola and Jacopo selling fruit. He later sees them doing several other small jobs. Their seriousness, energy and economy make him curious. Jacopo asks the traveller for a Sunday lift to Poleta. There the brothers enter a villa that turns out to be a hospital. A nurse explains that war devastated their family: their father died, their home was destroyed, and the boys experienced hardship and joined the resistance. Their sister Lucia has tuberculosis of the spine; the brothers work to pay for her treatment and visit her. The narrator respects their privacy rather than confronting them with what he has learned. He sees their responsibility as a source of hope after war. The title calls them gentlemen for their conduct, not their social rank.

## Kamala Das: Punishment in Kindergarten — poem summary
An adult speaker recalls a school outing. As other children play, she sits apart; a teacher scolds her for being different and the children laugh. The bright surroundings contrast with humiliation and isolation. At the close the adult claims a greater measure of peace and suggests there is no need to remember, yet the vivid act of recollection leaves room to question how completely the hurt has faded. Treat this tension as interpretation, not a medical diagnosis of the speaker.

## Grammar and 50-minute plan
Units 34–48 of the specified Murphy book are assigned; check the edition’s table of contents. 0–10: discuss what the title “gentlemen” suggests. 10–22: map the brothers’ work and the hospital revelation. 22–35: track the poem’s changes between past and present. 35–45: grammar practice from the assigned pages. 45–50: exit ticket on one contrast in either text.

## Questions
Why does the narrator not disturb the visit? How does the poem contrast the child’s feeling with the other children’s response? How does the ending complicate the speaker’s claim to peace?''','https://sittingbee.com/the-end-of-the-party-graham-greene/'.replace('https://sittingbee.com/the-end-of-the-party-graham-greene/','https://edu.sunsoftworld.com/the-two-gentlemen-of-verona/'))
add('course-11',3,'The Second Crucifixion, Mirror & grammar','''# The Second Crucifixion and Mirror
Functional English I · Semester 2, Unit 4

## Collins and Lapierre: The Second Crucifixion
The assigned historical narrative concerns Mahatma Gandhi’s assassination on 30 January 1948 and the response of leaders and mourners. Accounts describe the shock at Birla House, the need to prevent further communal violence, and the organisation of a public funeral. The title recalls a newspaper tribute comparing Gandhi’s killing to a crucifixion; it is a metaphor and interpretation, not a claim that the events were literally identical. Read the exact anthology extract and compare its framing with historical sources; reported conversations and details of the funeral should not be treated as independently proven simply because they appear in narrative form.

## Sylvia Plath: Mirror — poem summary
A mirror speaks in the first person, presenting itself as exact and without preferences. It describes the wall it usually reflects and interruptions by faces and darkness. In the second movement it imagines itself as a lake in which a woman searches for herself. She turns to gentler light, but returns and responds with distress. The final image represents youth as submerged and an older self rising, using a disturbing fish comparison. The poem concerns self-image, the passage of time and the tension between physical reflection and a complete sense of identity. The mirror’s claim to objectivity is itself open to analysis.

## Grammar and lesson plan
Units 49–63 of Murphy are prescribed; confirm edition-specific contents. 0–12 min: distinguish historical event from figurative title. 12–25: identify the poem’s two movements. 25–35: discuss personification and the lake image. 35–45: practise the assigned grammar topic. 45–50: write a short explanation supported by a detail.

## Questions
What does the title compare, and what are the limits of that comparison? Why does the mirror call itself truthful? Can an image of appearance provide the whole truth about a person?''','https://www.gradesaver.com/sylvia-plath-poems/study-guide/summary-mirror')
add('course-11',4,'Group discussion, listening and note-making','''# Group discussion, listening and note-making
Functional English I · Semester 2, Unit 5

## Discussion
A group discussion explores an issue or works towards a decision. Prepare a clear point and a reason, listen to other speakers and respond to their actual claims. Invite others in: “What do you think about this?” Disagree respectfully: “I understand that point, but the evidence may also suggest…” Summarise areas of agreement and unresolved questions. Clear communication matters more than speaking the most.

## Listening
Listen for the topic, speaker’s main point and supporting details. Attend without interrupting; use clarification questions where necessary. External noise, divided attention, unfamiliar terms and preconceptions can interfere. Written instructions, captions and a quieter room can make listening more accessible.

## Note-making
Record a topic heading, main points and supporting examples in a logical hierarchy. Abbreviate consistently but leave enough context to understand notes later. Distinguish a speaker’s words from your own response; mark uncertain facts for checking. Summarise the argument in your own words and record the source.

## Model activity
For a discussion on a library’s opening hours, one member proposes a later closing time, another identifies staffing costs and a third suggests a student survey. A note-taker records the proposal, concern, evidence required and next action; the group need not pretend it has reached a decision if it has not.

## 50-minute lesson
0–10: model listening and clarification. 10–20: listen to a short original talk and note main ideas. 20–35: discussion in groups with rotating roles. 35–45: compare notes and write a short summary. 45–50: each student identifies one participation or listening improvement.

## Check yourself
How do notes differ from a transcript? What can you say when you do not understand a point? How can a group include someone who has not yet spoken?''')
add('course-12',0,'Inspiration, creativity and reading','''# Introducing creative writing
Creative Writing in English · Semester 2, Unit 1

## Where writing begins
Creative writing makes deliberate choices of language, form and perspective to create an experience for readers. Inspiration can come from observation, memory, questions, conversations or imagined situations; it does not require waiting for a perfect idea. Keep a notebook of images and fragments. Be mindful of consent and privacy when using other people’s experiences.

## Reading as a writer
Read once for experience, then reread to notice craft: how does an opening establish expectations? What does the writer reveal or withhold? How do sound, sentence length and viewpoint shape feeling? Describe a technique before deciding whether it succeeds. Read across genres and languages rather than assuming one model of good writing.

## Exercises
1. Observe a familiar place for five minutes; record five concrete details without judging them.
2. Turn one detail into a question: “Who left the umbrella?” Write for five minutes without editing.
3. Change point of view and rewrite the opening. Compare the effect.
4. Choose a short passage from the class text. Note one craft decision and try the technique in an original scene without copying wording or plot.

## 50-minute lesson
0–10: read an opening and identify its effect. 10–20: observation notebook. 20–30: freewrite from a question. 30–40: rewrite from another viewpoint. 40–47: volunteers share; listeners name one effective detail. 47–50: exit reflection on a choice made.

## Questions
How does observation differ from interpretation? What changes when a scene is told by a different person? How can a writer use influence without copying?''')
add('course-12',1,'Voice, language and literary devices','''# Developing a distinctive craft
Creative Writing in English · Semester 2, Unit 2

## Voice and choices
Voice is the recognisable effect of choices in diction, rhythm, perspective and attitude. It is developed through practice, reading and revision rather than simply discovered once. A narrator’s voice is not automatically identical to the author’s. Audience, genre and context influence decisions about language variety and register.

## Devices in action
A simile makes an explicit comparison; a metaphor creates an implied identification. Personification gives nonhuman things human qualities. Image appeals to the senses, while repetition and rhythm can create emphasis. A device is useful when it contributes to effect: naming a metaphor is less helpful than explaining what it makes the reader notice.

## Syntax and language varieties
Compare “The rain stopped. She waited.” with “After the rain stopped, she waited.” The first can feel abrupt; the second makes the time relationship explicit. Experiment with sentence length and order while preserving clarity. Language varieties and dialects are not errors; render speech respectfully and avoid using stereotype as a substitute for character.

## Practice and lesson
0–10: identify an image and its effect. 10–20: rewrite a plain sentence in three rhythms. 20–30: describe a room from two narrators’ perspectives. 30–40: peer feedback focuses on a specific choice. 40–47: revise the strongest paragraph. 47–50: explain why the revision works.

## Questions
How does syntax affect pace? What assumptions does a narrator reveal through word choice? When does an image clarify and when does it distract?''')
add('course-12',2,'Poetry, fiction and drama','''# Poetry, fiction and drama
Creative Writing in English · Semester 2, Unit 3

## Poetry
Poetic language can compress feeling and invite attention to sound, image and line breaks. Rhyme links words through sound; free verse does not follow a fixed traditional metrical pattern, though it may have rhythm and repetition. A dramatic monologue gives a particular speaker a voice addressed within a situation. For children, write with an awareness of age, rhythm and interest without assuming all children enjoy the same style.

Exercise: describe rain in four lines; change the line breaks and observe changes in emphasis. Write a short monologue from the viewpoint of a person waiting for a bus.

## Fiction
A short story generally builds a concentrated situation; a novel can sustain a wider or longer development. Both use viewpoint, character, setting, causality and selection. Popular and literary fiction are overlapping categories, not a quality ranking. A scene presents action and interaction; summary condenses time. Writing for young readers requires attention to experience and audience, not a single fixed vocabulary.

Exercise: a character wants to return a borrowed object but meets an obstacle. Write a scene using action and dialogue, then write a two-sentence summary of the same event.

## Drama and screenwriting
A play is made for performance: dialogue, action, stage space and silence all contribute. A screenplay communicates what can be seen and heard, with scene headings and action written for production. Character emerges through choices under pressure. When studying Indian playwrights, read the prescribed examples and consider language, performance traditions and context rather than treating Indian theatre as one style. Children’s theatre can make imaginative use of movement and participation while remaining age-appropriate.

## 50-minute lesson
0–10: compare the three forms. 10–20: create a short poem. 20–30: build a fiction scene. 30–40: transform it into a dramatic exchange. 40–47: discuss what changes between page and performance. 47–50: exit reflection.

## Questions
How does a line break affect meaning? What does dialogue reveal without explanation? What can be shown on stage that a narrator might otherwise describe?''')
add('course-12',3,'Writing for media','''# Writing for media
Creative Writing in English · Semester 2, Unit 4

## Audience, purpose and medium
The same idea changes when the audience reads it, hears it or sees it on a screen. Identify who the audience is, what they need and what the medium allows. Accuracy and transparency matter in all formats. Avoid presenting advertising as independent reporting.

## Print, broadcast and online
A print feature can develop context through headings, paragraphs and quotations. Broadcast writing is heard in time: use clear sentence structure, signal transitions and read the script aloud. Online writing benefits from informative headings, short meaningful sections, links and accessibility features such as descriptive link text. These are flexible principles, not rules forbidding longer sentences.

## Advertising
Advertising attempts to persuade. Identify the audience, offering, key benefit and call to action, but avoid unsupported claims and misleading omissions. Revise “guaranteed to transform everyone’s life” to a precise, supportable description of what the product or event actually offers. Respect privacy and relevant advertising rules.

## Adaptation exercise
Take the announcement “A college hosts a free poetry reading on Friday at 4 p.m. in the library.” Write a 70-word print notice, a 20-second spoken announcement and a concise online post. Keep time, place and cost consistent; do not invent a speaker or registration requirement. Compare how each version suits its medium.

## 50-minute lesson
0–10: identify audience and medium. 10–25: draft two versions of one announcement. 25–35: read the broadcast version aloud. 35–45: peer-check factual consistency and accessibility. 45–50: exit ticket naming one adaptation choice.

## Questions
What makes a script easy to follow when heard once? What distinguishes persuasion from a misleading claim?''')
add('course-12',4,'Revision, editing and publishing','''# Editing and publishing
Creative Writing in English · Semester 2, Unit 5

## Revision before proofreading
Revision rethinks purpose, structure, character, evidence or emphasis. Editing improves clarity, consistency and style. Proofreading is the later check for typographical, spelling and punctuation errors. These stages overlap but it is inefficient to polish every comma before deciding whether a scene belongs in the piece.

## Practical revision process
Put the draft aside, read it aloud and describe what each paragraph or scene contributes. Identify the intended reader and the most important effect. Move, expand, cut or rewrite material as needed. Seek specific feedback: “Where did the sequence become unclear?” rather than only “Did you like it?” Decide which feedback helps the work; the writer retains responsibility for the final draft.

## Proofreading checklist
Check names, dates, spelling, paragraph breaks, punctuation and consistent formatting. Verify factual claims and permissions. Check titles and submission instructions. Reading aloud or changing the display can reveal mistakes; neither replaces a careful final check.

## Preparing to publish
Research a suitable journal, publisher or platform; check eligibility, genre, word limits and submission dates. Follow its manuscript instructions and understand rights, licensing and whether simultaneous submissions are permitted. Keep a record of submissions; beware of unsolicited promises and unexplained fees. Rejection is not proof that a piece has no value.

## 50-minute lesson
0–10: compare revision and proofreading. 10–25: mark structure and purpose in a draft. 25–35: exchange specific feedback. 35–45: revise a passage. 45–50: complete an exit checklist and identify one suitable publication venue to investigate.

## Questions
What changed between drafts, and why? What rights would you check before submitting? How does feedback differ from a command?''')
for i in range(4):
 n=d[f'course-11:{i}'][0];n['status']='preliminary';n['title']+=' — outline, grammar incomplete';n['text']=n['text'].replace('\nFunctional English I · Semester 2, Unit', '\n\nPRELIMINARY: Literature overview only. Detailed grammar notes for the assigned textbook units are not yet prepared; check the assigned edition.\n\nFunctional English I · Semester 2, Unit',1)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added 15 unit study notes')
