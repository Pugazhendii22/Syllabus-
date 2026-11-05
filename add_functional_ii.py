import json
p='prepared-notes.json';d=json.load(open(p))
def n(id,title,body,source,status=None):
 v={'id':id,'title':title,'text':'# '+title+'\nFunctional English II · Semester 3\n\n'+body+'\n\nRead the assigned text and verify its wording and selection against the course anthology.','source':source}
 if status:v['status']=status
 return v
def grammar(r): return n('grammar-'+r,'Grammar units '+r+' · not yet complete','''## Important limitation
The syllabus assigns units '''+r+''' of Raymond Murphy’s Essential English Grammar. Detailed notes for those textbook units have not yet been prepared. Unit numbers and content can vary by edition, so check the assigned 2012 edition’s table of contents rather than assuming the topics.

## What to do while the notes are incomplete
Identify the grammar point named in each assigned unit; read its explanation and try its exercises. For each mistake, write the original sentence, the corrected version and a brief explanation of the pattern. Bring uncertain answers to class. This is an interim study method, not a summary of those grammar units.

## Short classroom plan
0–10 minutes: identify the assigned grammar point. 10–20: teacher models a use and its context. 20–35: students try exercises individually and compare. 35–45: discuss why corrections work. 45–50: write one original example and an explanation.''','https://www.pondiuni.edu.in/wp-content/uploads/2024/03/SyllabusNEP-B.A.HonorsEnglish2023-24.pdf','preliminary')
d['course-19:0']=[
n('o-henry-twenty','O. Henry · After Twenty Years','''## Story overview
A police officer patrols a quiet New York street at night. A man waits in the doorway of a shop and explains that twenty years earlier, he and his friend Jimmy Wells agreed to meet at this spot at ten o’clock. The restaurant where they parted is gone, but the man has travelled from the West to keep the appointment. When he lights his cigar, the match briefly illuminates his face and a scar. He tells the officer about his friendship and apparent success. The officer leaves.

A little later another man approaches and calls him Bob. Bob believes he is Jimmy. They walk together, but in the brighter light of a shop window Bob notices that his companion’s nose is different and realises that he is not his friend. The stranger is a plainclothes officer, who arrests Bob as a man wanted in Chicago. He hands Bob a note from Jimmy.

The note reveals that the first officer was Jimmy: he had recognised Bob’s wanted face when the match was struck. Jimmy could not bring himself to make the arrest personally, so he obtained another officer to do it. Bob’s hand begins steady as he reads but trembles by the end. The story does not show a long reunion or tell us the outcome of the case.

## Analysis
The surprise ending depends on limited information and the reader’s assumptions about the first officer. The promise reveals loyalty even as the arrest creates a conflict between friendship and duty. The match and shop light enable two different recognitions. Bob’s material success should not be taken at face value as proof of honest achievement.

## 50-minute lesson
0–10: predict what an appointment after twenty years might reveal. 10–25: sequence the meeting, recognition and arrest. 25–35: identify clues before the ending. 35–45: discuss Jimmy’s choice. 45–50: exit ticket on the role of light.

## Questions
Who first recognises whom? Why does Jimmy ask another officer to act? How does the note change our understanding of the earlier conversation?''','https://www.commonlit.org/texts/after-twenty-years'),
n('assadi-ring','Mina Assadi · A Ring to Me is Bondage','''## Poem summary
The speaker repeatedly gives unexpected meanings to familiar things. Rather than focusing on a prayer mat, she imagines many roads through gardens and describes prayer in relation to happiness, movement and birdsong. She questions conventional assumptions about place and attachment, naming solitude happiness, a desert home and what makes her sad love.

She imagines a person who plucks a flower as unable to see its value, and a net separating fish from water as destructive. Looking at the sea, she imagines a relation between smallness and vastness that changes when the sea joins the ocean. Later she describes memory, a cage and an unused thought through surprising equivalences. The ring becomes an image of bondage, and the poem returns to the opening roads and gardens.

## Interpretation and form
The ring can suggest restrictive possession or a conventional relationship, but the poem does not require every ring or every relationship to have one meaning. Its repeated “to me” phrasing foregrounds a particular speaker’s perspective. Paradox and unconventional definitions invite readers to question customary associations; the return to the roads gives the poem a circular shape. Nature, freedom and confinement are productive themes, not a reason to treat the speaker as opposed to all religion or community.

## 50-minute lesson
0–10: students suggest associations for “ring” and “road.” 10–25: follow the speaker’s changed definitions. 25–35: discuss the net and cage images. 35–45: compare opening and ending. 45–50: write a supported interpretation of one paradox.

## Questions
Why does the poem use personal definitions? How do the roads and the ring contrast? Can the poem value freedom while also expressing sadness?''','http://www.artarena.force9.co.uk/mina.htm'),
n('kincaid-girl','Jamaica Kincaid · Girl','''## Form and overview
“Girl” is a very short work built largely as a sequence of instructions, commonly read as a mother speaking to a daughter. Its domestic and linguistic details evoke a Caribbean setting. The narrative is not organised like a conventional plot with several scenes; the pressure of repeated commands is itself central to its effect.

## What happens
The dominant speaker tells the girl how and when to wash clothes, how to cook, sew, garden, behave in public and manage relationships. Practical knowledge is interwoven with warnings about reputation and sexuality. She tells the girl not to sing benna in Sunday school; the girl briefly protests that she does not do so. The main voice continues, often assuming that the girl is at risk of becoming sexually disreputable.

Near the end the speaker advises the girl to test bread for freshness. The girl asks what to do if the baker refuses to let her touch it. The speaker responds by questioning whether the girl will become the sort of woman the baker would not trust near the bread. The work ends there; it does not tell us what the girl later chooses or becomes.

## Themes and method
The speaker transmits useful knowledge while enforcing restrictive expectations. The rapid, semicolon-linked instructions can feel both protective and overwhelming. The daughter’s two brief responses make unequal speaking power audible. Avoid reducing the mother to a villain or assuming that care cancels the harm of shaming; both can operate together. The story’s particular Caribbean details matter alongside broader questions about gender and social respectability.

## 50-minute lesson
0–10: discuss the difference between advice and command. 10–22: classify practical instructions and warnings. 22–35: analyse the two interruptions. 35–45: discuss care and control together. 45–50: exit ticket on the ending’s effect.

## Questions
How does punctuation shape pace? What does the daughter’s limited opportunity to speak reveal? Why does the bread question become a judgement about reputation?''','https://www.litcharts.com/lit/girl/summary'),grammar('64–74')]
d['course-19:1']=[
n('raja-cow','Raja Rao · The Cow of the Barricades','''## Story overview
A mysterious cow, Gauri, visits the Master regularly on Tuesdays. She accepts the grain he offers and then disappears. People search for her without finding a clear owner or ordinary explanation. Her unusual behaviour and her connection with the Master encourage villagers to treat her with reverence. The story also refers to her contact with Mahatma Gandhi; the Master and Gandhi should not simply be assumed to be the same character.

As political tensions increase, barricades divide the town, with armed authorities on one side and people resisting on the other. Gauri walks through the gathering. The crowd honours her and helps her onto the barricade. The chief of the opposing soldiers shoots her, and she dies. The narrative presents the absence of visible blood and the crowd’s reactions in a legendary, devotional register.

Afterwards a patron erects a statue of Gauri. Children play around it and toy Gauris circulate. The Master imagines her waiting to be reborn when India again suffers before freedom. The ending connects remembrance, popular legend and the freedom struggle, without describing Gauri as a literal historical participant in a documented event.

## Interpretation
The cow can represent compassion, nonviolence or collective hopes, but the story’s religious and political symbols invite debate rather than one compulsory equation. The narrative mixes colloquial storytelling, mythic imagery and political conflict. Ask how the community makes meaning from her death and whether the ending is wholly consoling.

## 50-minute lesson
0–10: identify narrator and setting. 10–22: trace Gauri’s visits. 22–35: reconstruct the barricade scene. 35–45: discuss statue, myth and political memory. 45–50: exit ticket on a detail that supports an interpretation.

## Questions
How does the story establish Gauri’s mystery? What changes when she reaches the barricades? How does the ending join play, remembrance and hope?''','https://xpressenglish.com/our-stories/barricades/'),
n('huxley-beauty','Aldous Huxley · The Beauty Industry','''## Argument overview
Huxley’s satirical essay considers the growth of the beauty industry and the money and attention devoted to appearance. He discusses changing social conditions and the increased availability and use of beauty products, then questions whether external treatment alone can produce the kind of beauty he values. He contrasts physical presentation with qualities of mind, feeling or character. His statistics and comparisons belong to the historical context of the essay and should be checked in the assigned text rather than repeated as current figures.

## Method and interpretation
The essay uses irony, exaggeration and contrasts to criticise consumer culture and narrow ideas of appearance. At the same time, a critical reader can question Huxley’s assumptions: his discussion often singles out women, risks judging people’s inner lives from their looks and treats some beauty practices as superficial without considering autonomy, work, pleasure or social pressure. Explain his argument fairly before evaluating its limits. Appearance does not reliably reveal moral character.

## Teaching plan: 50 minutes
0–10: distinguish an author’s claim from agreement with it. 10–22: map Huxley’s evidence and central contrast. 22–35: identify a satirical technique. 35–45: evaluate gender assumptions and present-day relevance. 45–50: write a claim with one support and one limitation.

## Questions
How does satire shape the reader’s response? What social conditions does Huxley connect with beauty products? Which assumptions in the essay can be challenged, and why?''','https://educationallodge.com/2022/05/the-beauty-industry-summary-author-intro-questions.html'),grammar('75–83')]
d['course-19:2']=[
n('heaney-digging','Seamus Heaney · Digging','''## Poem summary
At a desk the speaker holds a pen. He hears a spade outside and looks down at his father digging. The sight carries him back to his father’s earlier work digging potatoes, remembered through skilled movements and the cool feel of the crop. He also remembers his grandfather cutting turf in a bog and recalls bringing him milk before the older man returned to work.

The smell of earth and sound of cutting make these memories vivid. The speaker recognises that he does not follow the earlier generations with a spade. Returning to the pen in his hand, he decides to dig with it: writing will be his own form of careful work and exploration.

## Form and interpretation
The poem moves from present observation to memories and back to the pen. The opening compares the pen to a gun; the ending emphasises a different tool and action. Do not insist that the gun image has only one political or personal meaning. Sound patterns, tactile detail and the repeated action of digging honour manual skill while allowing a different vocation. The poem negotiates continuity and difference rather than simply rejecting family work.

## 50-minute lesson
0–10: sketch the three generations. 10–22: follow the shifts in time. 22–35: identify sound and sensory details. 35–45: compare pen and spade. 45–50: explain one effect using a precise detail.

## Questions
What triggers memory? How are the father’s and grandfather’s work represented? Why is the final act of digging figurative?''','https://interestingliterature.com/2016/10/a-short-analysis-of-seamus-heaneys-digging/'),
n('ghosh-sea','Amitav Ghosh · The Town by the Sea','''## Context and limitation
The assigned essay relates to the 26 December 2004 Indian Ocean tsunami and its consequences in the Andaman and Nicobar Islands. Anthologies may abridge the longer account. This note provides a broad, source-based outline; check the prescribed extract for exact names, sequence and detail. The subject involves bereavement and disaster and should be discussed sensitively.

## Outline
Ghosh’s account considers a town on Car Nicobar after the tsunami and the experience of a researcher whose family and home were caught in the disaster. The man is away when the earthquake and waves strike. His son survives, while his wife and daughter are lost. The narrator’s conversations and the damaged landscape connect a large-scale catastrophe with a particular family’s grief.

The account’s attention to surviving structures, everyday belongings and memories shows how material places can carry personal meaning. It also raises difficult questions about how people speak, remember and continue after loss. A reader should not judge a person’s grief from one gesture or conclude that valuing work or possessions proves a lack of love.

## Reading critically
Distinguish the narrator’s observations, another person’s recollections and your own inferences. The tsunami was a physical disaster with social consequences; describing nature’s power should not erase differences in vulnerability, aid or human responsibility. Use respectful language and avoid presenting tragedy as a simple moral lesson.

## 50-minute lesson
0–10: context and content note. 10–22: identify narrator, place and event. 22–35: trace one remembered object or place in the extract. 35–45: discuss the limits of inferring emotion. 45–50: write a question for the text rather than a judgement of the survivor.

## Questions
How does a specific family story affect our understanding of a disaster? What can objects reveal, and what can they not prove?''','https://journals.iium.edu.my/asiatic/index.php/ajell/article/download/3963/1270/5999','preliminary'),
n('bhatt-history','Sujata Bhatt · A Different History','''## Poem summary
The opening imagines the Greek god Pan migrating to India. Gods appear in forms associated with the natural world, and trees and books are treated with reverence. The speaker lists ways of handling a book carelessly and asks that pages be turned gently, respecting Sarasvati, associated with knowledge, and the tree from which the paper came.

The poem then turns to questions about language and oppression. Images of violent conquest complicate the earlier reverence for books and learning. The speaker asks how later generations can come to love a language connected with an oppressor’s history. The ending is a question and a paradox, not a declaration that the violence has been forgotten or that the language has only one meaning.

## Form and interpretation
Allusions to Pan and Sarasvati bring different traditions into relation. The shift from respectful instruction to questioning and violent imagery creates tension between language as knowledge and language implicated in power. A language is not literally a person who decides to kill: examine how the rhetorical questions make readers consider its historical uses. Readers can debate the emotional force of the final “love” without claiming that pain is necessarily absent.

## 50-minute lesson
0–10: identify the two movements. 10–22: discuss books, trees and deities. 22–35: examine the shift to questions about language. 35–45: discuss inheritance and colonial history. 45–50: exit response explaining one contrast.

## Questions
Why connect a book to a tree? How does the tone change? What makes the later generation’s relationship to language complex?''','https://english-studies.net/a-different-history-by-sujata-bhatt-a-critical-analysis/'),grammar('84–95')]
d['course-19:3']=[
n('narayan-engine','R. K. Narayan · Engine Trouble','''## Story from beginning to end
The narrator wins a road engine in a lottery at a travelling fair called Gaiety Land. What initially looks like a valuable prize immediately becomes a problem: it is large, heavy and difficult to move or sell. The fair’s management allows it to remain temporarily, but after the fair leaves the municipality demands that the narrator remove it or pay rent for the space.

Unable to find a buyer, he pays rent and spends increasing amounts trying to deal with the machine. When the ground is needed for another event, he arranges to move it to a friend’s property. He hires a temple elephant, labourers and Joseph, a former bus driver, to help direct the engine. Their efforts are not coordinated. The machine damages a compound wall, the elephant becomes agitated, and the owner and authorities hold the narrator responsible. What was supposed to be a windfall has become a source of debt, public embarrassment and domestic tension.

A visiting swami announces a performance involving a road engine driven over his body. The narrator hopes that allowing his engine to be used will finally solve his transport problem. The dangerous demonstration is stopped by the authorities, so this plan fails too. He considers leaving town.

An earthquake then shifts the engine into a disused well. The narrator fears another liability, but the well’s owner had been ordered to close it and welcomes the machine because it effectively fills the opening. The owner agrees to settle the problem and cover expenses in return for leaving the engine there. An accident finally resolves what careful efforts could not. The narrator is relieved.

## Technique and themes
First-person narration, escalating complications and reversals make the story comic. The prize’s supposed value depends on the owner’s ability to store, move or use it. Coincidence and absurdity shape the resolution; the story does not require readers to believe that disasters are generally fortunate. Consider the narrator’s perspective and the other people affected by his schemes.

## 50-minute lesson
0–10: discuss whether every prize is useful. 10–25: make a cause-and-effect chain from lottery to failed moves. 25–35: analyse the swami episode and earthquake. 35–45: discuss irony and practical value. 45–50: exit ticket explaining the final reversal.

## Questions
Why is the engine a burden? How does each attempted solution create another problem? Why does the well owner welcome it?''','http://sittingbee.com/engine-trouble-r-k-narayan/'),
n('fromm-love','Erich Fromm · Is Love an Art?','''## Context and central question
“Is Love an Art?” is associated with the opening of Fromm’s The Art of Loving (1956). The exact course extract should be checked. Fromm asks whether love is a skill requiring knowledge and effort or a pleasant feeling that happens by chance. He argues for the former.

## Main line of argument
Fromm suggests that many people focus on being loved—becoming attractive, successful or desirable—rather than developing their own capacity to love. A second assumption treats love mainly as a problem of finding the right object, rather than practising an ability. A third confuses the initial experience of falling in love with the continuing work of loving. These are Fromm’s diagnoses of cultural attitudes, not universal facts about every relationship.

If love is an art, he argues, a person must give it serious attention, learn both theory and practice, and recognise that improvement takes effort. In the broader book he links mature love with care, responsibility, respect and knowledge; check whether those later discussions occur within the assigned extract before attributing them to the opening alone.

## Evaluate the argument
Fromm’s framework invites reflection on attention, reciprocity and whether consumer habits shape relationships. Ask whether the analogy with an art has limits: relationships also depend on other people’s agency, social conditions, consent and circumstances beyond one person’s control. Effort does not obligate anyone to remain in an unsafe or unwanted relationship.

## 50-minute lesson
0–10: distinguish falling in love from sustaining care. 10–22: map the three assumptions Fromm questions. 22–35: assess his art analogy. 35–45: offer an example and a counterexample. 45–50: write one reasoned agreement or disagreement.

## Questions
What does it mean to treat love as a capacity? Why does Fromm distinguish being loved from loving? What are the limits of the skill analogy?''','https://www.supersummary.com/the-art-of-loving/summary/'),grammar('96–106')]
d['course-19:4']=[
n('functional-communication','Communication, greetings, requests and telephone skills','''## Understanding communication
Communication involves producing, receiving and interpreting messages in a context. A sender’s intention is not automatically the same as the listener’s understanding. Feedback—questions, paraphrases and responses—helps identify misunderstandings. Noise can include poor audio, ambiguous wording, interruptions or different assumptions.

## Greetings and introductions
Choose an appropriate greeting for the relationship and situation. In a formal introduction, give your name and relevant role: “Good morning. I’m Meena, a student in the English department.” In an informal setting, a shorter greeting may be appropriate. Pronounce and use another person’s name respectfully; do not assume a person’s preferred title.

## Making requests
A useful request states the action, context and, when appropriate, a realistic deadline. “Could you please share the meeting notes by Friday?” is more specific than “Send it soon.” Choose a tone suited to the situation, and allow the other person to ask questions or decline. Politeness is not the same as excessive length.

## Telephone communication
Before calling, identify your purpose and necessary information. Greet the person, introduce yourself and check whether it is a convenient time. Explain the reason for calling, listen, confirm important names or dates and summarise any agreed next steps. If the line is unclear, ask for repetition rather than pretending to understand. Avoid sharing private information without confirming identity and authorisation.

## Model call
“Good morning. This is Meena from the English department. May I speak to the library coordinator?” If the person is unavailable: “Could you please ask them to call me back? My number is …” Repeat the number slowly and thank the recipient. This is a model, not a real contact.

## 50-minute lesson
0–10: identify the parts of a communication exchange. 10–20: practise formal and informal greetings. 20–30: rewrite vague requests. 30–42: pairs role-play a call and take a message. 42–50: confirm details and reflect on one listening skill.

## Questions
How can you politely check whether someone is available? What information belongs in a telephone message? Why is feedback important?''','https://pressbooks.bccampus.ca/uvicpeopleteamsandorganizations/chapter/chapter-4-communication-and-perception/'),grammar('107–114')]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added Functional English II: 5 units,',sum(len(d[f'course-19:{i}']) for i in range(5)),'selections')
