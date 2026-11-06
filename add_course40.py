"""Syllabus page 162 calls this Translation, but its prescribed content is postcolonial."""
import json
P='prepared-notes.json'
with open(P,encoding='utf8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,preliminary=False):
 x={'id':id,'title':title,'source':source,'text':f'# {title}\nSemester 7 · Major Discipline 18\n\nSyllabus check: the printed course title is “Translation: Theory and Practice,” but its description and readings concern postcolonial literature. These notes follow the printed readings; confirm the course title and prescribed material with the college.\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: consult the assigned text and edition; check quotations, translations and interpretations before teaching.'}
 if preliminary:x['status']='preliminary'
 return x
d['course-40:0']=[
n('macaulay','Macaulay · Minute on Indian Education', '''## Argument and setting
In 1835, Thomas Babington Macaulay argued over the East India Company’s allocation of educational funds. He favoured English education and European learning over official support for Sanskrit and Arabic learning. His claims that European knowledge was inherently superior are colonial judgments, not objective facts.

## The intermediary class
He proposed educating a limited group of Indians to act as intermediaries between the rulers and the population, expecting knowledge to filter into Indian languages. His argument explicitly rejected attempting to educate the whole population with the funds he discussed. Read this alongside unequal access to education and the power to decide which languages counted as valuable.

## Critical reading
Distinguish the Minute’s proposal from the entire history of Indian education: policies changed, and Indian educators and communities had diverse responses. English later became a resource for anti-colonial debate as well as an instrument of colonial power. Ask who is permitted to define useful knowledge and how Macaulay represents Indian intellectual traditions.''','0–10: introduce Company rule and 1835. 10–20: map the funding argument. 20–30: discuss the proposed intermediary class. 30–40: identify unsupported hierarchies. 40–50: compare language and power today.','Who would receive priority in Macaulay’s plan? Why is a colonial assertion of cultural superiority not neutral evidence?','https://franpritchett.com/00generallinks/macaulay/txt_minute_education_1835.html'),
n('young-remains','Robert J. C. Young · Postcolonial Remains', '''## Central question
Young’s 2012 essay asks what remains of colonial structures and what postcolonial criticism must address in the present. “Remains” suggests both continuing legacies and the work that remains to be done; political independence does not automatically remove unequal relations.

## Issues and approach
The essay considers Indigenous struggles under settler colonialism, irregular migration and political Islam as issues not neatly captured by a single familiar model of anti-colonial nationalism. It asks how some people or struggles become difficult to see or read within dominant public frameworks. These different cases should not be treated as identical.

## Apply cautiously
Compare a government’s account of a disputed territory with the claims of its Indigenous communities. What is visible in each account? Who controls the categories used? This question is a teaching application, not a substitute for Young’s detailed argument. “Postcolonial” is a critical orientation as well as a term for historical aftermath; check the essay for its own examples and qualifications.''','0–10: discuss independence and continuing inequality. 10–20: explain “remains”. 20–30: identify the three examples. 30–40: consider visibility and representation. 40–50: formulate a question for close reading.','Why does independence not settle every colonial relation? Why should the examples not be merged into one story?','https://www.semanticscholar.org/paper/Postcolonial-Remains-Young/4dcf2226973f09e0614e7e014fad4b96b07c27fc'),
n('christian-theory','Barbara Christian · The Race for Theory', '''## Argument
In her 1987 essay Christian questions academic pressures that make a particular abstract, specialised form of theory the gatekeeper of literary value. She asks who controls publishing, teaching and professional recognition, and whose work is sidelined by those standards.

## Theory in many forms
Christian argues that people of colour have long theorised through narrative, proverbs, riddles and other forms of making meaning. She is not claiming that such communities cannot practise abstract thought, or that all members think alike. Her criticism challenges the hierarchy that recognises only some forms as theory.

## Reading practice
Pay attention to the literary work, its history and the critic’s social position rather than applying one method mechanically. For a class exercise, ask how a short story develops an idea about power without turning its characters into mere examples of a prefabricated theory.

## Debate
Does specialised terminology clarify a difficult problem, restrict access, or both? Christian’s essay itself is theoretical argument; it is not simply a rejection of thinking critically.''','0–10: list places where ideas are made. 10–20: identify institutional gatekeeping. 20–30: discuss narrative as theorising. 30–40: test an example. 40–50: debate clarity and specialised vocabulary.','How can a story theorise? What is Christian criticising when she questions the “race” for theory?','https://doi.org/10.2307/1354255')]
d['course-40:1']=[
n('walcott-ruins','Derek Walcott · Ruins of a Great House', '''## Poem movement
The speaker walks among the remains of a Caribbean colonial great house. Decayed masonry, trees and signs of former wealth provoke thought about the people who owned the estate and the labour and violence that sustained it. The ruin exposes the vulnerability of apparently permanent power.

## Literary inheritance
The poem invokes English writers and their words while condemning imperial cruelty. The speaker moves through anger toward a complicated sense of shared mortality associated with John Donne. Compassion does not require forgetting slavery or pretending all parties had equal power.

## Teaching point
The house is both a material site and a figure for colonial history. Ask why a Caribbean poet might draw on a literary inheritance connected to the empire while challenging the violence of that empire.''','0–10: picture the ruined estate. 10–20: connect wealth and coerced labour. 20–30: identify literary allusions. 30–40: trace the shift in feeling. 40–50: discuss memory and compassion.','How do ruin and quotation work together? Does compassion erase accountability?','https://poemanalysis.com/derek-walcott/ruins-of-a-great-house/'),
n('walcott-sea','Derek Walcott · The Sea is History', '''## Summary
A questioning voice asks where Caribbean monuments and historical memory are. The speaker answers that the sea holds them. Images of ships, crowded cries, drowned bodies and coral evoke the Middle Passage and the history of enslavement. An imagined underwater journey finds columns and cathedrals in marine formations rather than in European stone monuments.

The poem moves through emancipation, the emergence of nations and a satirical procession of creatures resembling officials, politicians and judges. Its final sound suggests history still beginning, rather than a past neatly completed.

## Form and meaning
Biblical names including Genesis, Exodus and Lamentations are repurposed to narrate a Caribbean history often excluded from dominant archives. The sea is a grave and a repository of memory, not proof that no written Caribbean history exists. Apparent denials that particular events are “History” invite debate about who has the power to define historical narrative.''','0–10: identify the opening question. 10–20: map sea and slavery images. 20–30: discuss biblical references. 30–40: consider emancipation and the final creatures. 40–50: interpret the ending.','Why call the sea an archive? How do biblical forms acquire new meanings here?','https://scholarblogs.emory.edu/complit203/2017/03/03/lotus/'),
n('bennett-reverse','Louise Bennett-Coverley · Colonization in Reverse', '''## Summary
A Jamaican speaker observes the movement of Jamaicans to Britain and humorously calls it colonisation in reverse. Relatives, neighbours and acquaintances travel to the imperial “mother country”; the speaker watches the movement with comic astonishment. The comic reversal makes familiar colonial relationships appear strange.

## Voice and context
Bennett writes in Jamaican Creole, a rule-governed language variety suitable for sophisticated literary and oral expression, not “broken English.” The poem’s rhythm, idiom, questions and conversational speaker draw energy from performance. Read migration in relation to postwar labour demand and the racism Caribbean migrants encountered in Britain.

## Interpretation
The title is ironic: migrants did not acquire the coercive power of the British Empire over Jamaica. Humour permits pride and anxiety to coexist, including expectations about work and opportunity.''','0–10: establish migration context. 10–20: paraphrase the speaker’s questions. 20–30: discuss Creole and performance respectfully. 30–40: unpack the ironic reversal. 40–50: compare humour and power.','Why is the title ironic rather than a literal equivalence? What does the language contribute to the speaker’s authority?','https://mmcclellan.omeka.net/exhibits/show/annotation/00--intro-to-web-annotation/period-5-bennett--colonization'),
n('soyinka-phone','Wole Soyinka · Telephone Conversation', '''## Summary
A prospective tenant telephones a landlady about a room. When the speaker discloses that he is African, the conversation changes: she asks how dark his skin is. He responds with increasingly elaborate descriptions and finally an absurd invitation to see for herself. The phone conversation ends in tension.

## Technique
The speaker’s witty, controlled language exposes the indignity and absurdity of racial classification. References to the red telephone booth and other ordinary details locate prejudice in an everyday encounter. The landlady’s questions turn a housing inquiry into a demand that the speaker account for his body.

## Interpretation
Humour gives the speaker agency without making discrimination harmless. Avoid inventing a final tenancy decision: the poem stages an interaction, not a complete housing outcome.''','0–10: reconstruct the call. 10–20: locate the turning point. 20–30: analyse colour vocabulary and tone. 30–40: discuss housing discrimination. 40–50: explain the comic ending.','How does the speaker resist the landlady’s categories? Why does the everyday setting matter?','https://www.litcharts.com/poetry/wole-soyinka/telephone-conversation'),
n('brathwaite-negus','Kamau Brathwaite · Negus', '''## Movement of the poem
The poem begins with broken repetition and insists that familiar signs of political freedom are not enough. The speaker seeks language adequate to anger, history, collective struggle and remaking the future. Images of banks, foreign corporations and state power connect the problem of speech with continuing material domination.

## Form
Repetition, interruption, punctuation and oral rhythm make readers hear a struggle to say what inherited forms may not easily contain. “Negus” is an Ethiopian title for a ruler and brings associations of Black sovereignty; avoid reducing the poem to a simple biography of a king.

## Critical reading
Brathwaite’s later discussions of nation language provide one useful context, but do not assume every nonstandard feature means a single thing. Independence and self-expression matter, yet the repeated “not enough” resists declaring liberation complete.''','0–10: listen to the poem’s rhythms if a recording is available. 10–20: trace repetition. 20–30: connect words and economic power. 30–40: discuss the title. 40–50: interpret “not enough”.','What does repetition refuse? How is language connected to structures beyond language?','https://jacket2.org/podcasts/find-me-rage-poemtalk-149'),
n('curnow-house','Allen Curnow · House and Land', '''## Summary
A visitor and a historian encounter Miss Wilson and Alice in an old settler household in Aotearoa New Zealand. The poem records inherited objects, remembered family and the historian’s account of a continuing spirit of exile. Miss Wilson’s own memories and responses do not always fit the historian’s sweeping explanation. A changing afternoon and rain lead to the bleak final image of a settler land without a soul at home.

## Interpretation
The house suggests inherited status and an attachment to Britain, while the land raises questions about belonging. The speaker’s generalisation describes settler alienation; it should not be accepted as a statement that Māori people had no home there. Māori histories and dispossession are important contexts that the poem’s settler perspective can leave marginal.

## Form
Shifts among observation, reported speech and reflection create distance between public history and particular experience. Read the final gloom as an interpretation rather than the only possible account of Aotearoa.''','0–10: map visitor, historian and household. 10–20: compare family memory with historical generalisation. 20–30: examine house and land. 30–40: question the settler perspective. 40–50: discuss the ending.','Whose belonging does the final statement describe? How does a historian’s account differ from Miss Wilson’s memory?','https://www.poetlaureate.org.nz/2015/10/house-and-land.html'),
n('faiz-trace','Faiz Ahmad Faiz · Nowhere No Trace Can I Discover', '''## Summary
The speaker searches for traces of blood but finds no obvious stain on hands, weapons, dust or walls. The poem then describes blood shed without the public recognition of a ceremonial sacrifice or a battlefield martyr. It calls this blood orphaned: no one listens, no witness comes forward, and the case closes as the blood of the oppressed sinks into dust.

## Meaning and form
The absence of visible evidence is not proof that no violence occurred. Repetition, negation and the image of a closed legal case expose the abandonment of victims. The blood seems to cry out even as the world refuses to hear it.

## Translation
Faiz wrote in Urdu; English wording and line breaks depend on the translator and anthology. Compare the assigned version before quoting, and do not attach the poem to a particular incident without evidence.''','0–10: describe the failed search. 10–20: identify repeated negations. 20–30: discuss the orphaned blood. 30–40: compare silence and legal judgment. 40–50: consider translation choices.','Why does the absence of stains not erase violence? What does the closed case suggest about justice?','https://srishtivarenya.blogspot.com/2020/02/no-where-no-trace-can-i-discover-faiz.html',True),
n('diop-africa','David Diop · Africa', '''## Summary
The speaker addresses Africa through memories of ancestral warriors and a grandmother’s songs. Though distant, the speaker feels a bodily connection to the continent. Images of blood, labour, humiliation and a whipped back confront the violence of slavery and domination. A responding voice identifies Africa with a young tree growing stubbornly, whose fruit acquires the bitter taste of liberty.

## Interpretation
The tree suggests persistence and the possibility of freedom, but “bitter” keeps suffering and the costs of struggle in view. Personification and direct address make the continent a partner in dialogue rather than a passive landscape. Africa contains many distinct peoples and histories: a poetic collective voice should not be mistaken for a claim that every African experience is the same.

## Translation
Diop wrote in French; translations may differ. Check the assigned version before quoting or discussing line breaks.''','0–10: locate ancestral memory. 10–20: trace images of labour and violence. 20–30: discuss the answering voice and tree. 30–40: explain bitter liberty. 40–50: consider the collective address.','Why is the fruit of liberty described as bitter? How do memory and resistance interact?','https://literaturepadi.com.ng/2023/06/09/content-analysis-of-david-diops-africa/')]
d['course-40:2']=[
n('achebe-image','Chinua Achebe · An Image of Africa', '''## Argument
Achebe’s lecture, later published as an essay, challenges Joseph Conrad’s Heart of Darkness for representing Africa as a backdrop against which European characters explore themselves. He objects to the dehumanisation and limited speech granted to African people and questions critical praise that overlooks such representation.

## Reading the controversy
Conrad’s narrator Marlow is a character, not automatically identical to Conrad; Achebe nevertheless argues that narrative distance does not exempt the work from criticism. Readers have debated the limits and strengths of this claim. Discuss the novel’s artistic qualities and its racial politics together rather than assuming either cancels the other.

## Classroom application
Compare a scene’s descriptions of African figures with the space given to European reflection. Whose speech receives complexity? The exercise concerns the assigned novel’s representation, not a general claim about Africans or about every reader of Conrad.''','0–10: establish Conrad and Achebe. 10–20: explain the idea of Africa as backdrop. 20–30: distinguish author and narrator. 30–40: analyse representation. 40–50: debate literary value and responsibility.','What is lost when a place becomes a backdrop? Does narrative distance settle the question of racism?','https://cjuneadams.com/2018/08/13/chinua-achebe-an-image-of-africa-racism-in-conrads-heart-of-darkness/'),
n('spivak-three','Gayatri Chakravorty Spivak · Three Women’s Texts and a Critique of Imperialism', '''## The three works
Spivak’s 1985 essay reads Charlotte Brontë’s Jane Eyre, Jean Rhys’s Wide Sargasso Sea and Mary Shelley’s Frankenstein. It asks how imperialism shapes the making of subjects and the boundaries of a feminism centred on the individual European woman.

## Jane and Antoinette
Jane’s development cannot be separated from the imperial world in which Bertha Mason is represented and confined. Rhys reimagines Bertha as Antoinette Cosway, showing a different history of naming, marriage and displacement. But Spivak also asks what Rhys’s novel cannot fully represent, including the position of Christophine. Antoinette, a white Creole, and Christophine, a Black Caribbean woman, do not occupy the same social position.

## Frankenstein and method
The essay also examines reproduction and the making of a human subject through Shelley’s novel. “Worlding” can describe processes through which an imperial perspective makes a colonised place legible on its own terms. Spivak’s argument does not say women writers are automatically anti-imperialist, or that every feminist reading must be discarded.''','0–10: identify the three novels. 10–20: discuss Jane and Bertha. 20–30: compare Rhys and Christophine. 30–40: introduce subject-making. 40–50: consider feminism and empire together.','Why do Antoinette and Christophine occupy different positions? How can a feminist narrative also depend on empire?','https://doi.org/10.1086/448328'),
n('ngugi-decolonising','Ngũgĩ wa Thiong’o · Decolonising the Mind', '''## Central argument
Ngũgĩ examines how colonial schooling and cultural institutions devalue African languages while privileging European ones. He treats language as both communication and a carrier of culture, memory and power. His account of punishment for speaking Gĩkũyũ at school shows language policy as a lived experience, not just a dictionary choice.

## Literature and theatre
He discusses writing, theatre and the publishing world, including the politics of audiences and access. His own commitment to writing in Gĩkũyũ is a response to the hierarchy he criticises. The book does not make all African-language communities identical or resolve every practical issue of translation, literacy and multilingual education.

## Scope
The syllabus names the book without a chapter or extract. This is an introductory guide to its main concerns, not a full chapter-by-chapter reading. Confirm the assigned selection and spelling in the edition used.''','0–10: discuss language and schooling. 10–20: explain communication and culture. 20–30: identify audience and publishing. 30–40: debate multilingual choices. 40–50: apply to a classroom example.','How can language policy distribute power? Why is choosing one language for literature a complex practical and political decision?','https://www.goodreads.com/en/book/show/152622.Decolonising_the_Mind',True)]
d['course-40:3']=[
n('hayavadana','Girish Karnad · Hayavadana: act-by-act', '''## Frame and Act I
The Bhagavata introduces a performance after an invocation to Ganesha. Hayavadana, a man with a horse’s head, wants to become a complete human being. In the main story the close friends Devadatta, a poet, and Kapila, associated with physical strength, meet Padmini. Devadatta marries her, but attraction and jealousy complicate their friendship.

While travelling, Devadatta cuts off his head at a temple. Kapila discovers him and does the same. Padmini finds both bodies; the goddess Kali offers to restore them if she replaces the heads. In her haste she exchanges the heads, producing two living men with mixed bodies. Both claim to be Padmini’s husband.

## Act II
A sage decides that the head determines identity, so the man with Devadatta’s head returns with Padmini. They have a son. Speaking dolls report changes in the household as Devadatta’s body loses strength and Padmini dreams of Kapila. Padmini visits Kapila in the forest; Devadatta finds them, and the two men kill one another. Padmini chooses to die on their funeral pyre, entrusting her son to the Bhagavata.

In the frame, Kali has made Hayavadana a complete horse rather than a complete man. The boy, previously unable to laugh, laughs with him; Hayavadana’s human voice becomes a neigh.

## Interpretation
Masks, dolls, songs and the framed story question whether mind, body or social recognition makes a whole person. Treat sati critically as a dramatic event, not an ideal or a recommendation.''','0–10: map frame and characters. 10–20: trace the swapped heads. 20–30: compare the sage’s ruling and Padmini’s desires. 30–40: follow the tragic ending and horse frame. 40–50: debate completeness.','What criterion does the sage use for identity? How does Hayavadana’s ending complicate the wish for completeness?','https://www.litcharts.com/lit/hayavadana/summary'),
n('rita-joe','George Ryga · The Ecstasy of Rita Joe: dramatic guide', '''## Content warning
The play depicts racism, sexual violence and murder. Discussion should avoid graphic re-enactment and victim-blaming.

## Courtroom and memory
Rita Joe, an Indigenous young woman who has left her reserve for a city, faces a magistrate and criminal charges. The courtroom is interwoven with memories of family, schooling, employment and encounters with officials. The non-linear structure resists presenting her life as a simple chronological case file.

## Institutions and relationships
Her father David Joe and Jaimie Paul are important figures in her remembered and present relationships. Teachers, officials and supposed helpers often presume authority to define Rita’s needs while failing to listen to her. Rita seeks opportunity and speaks back against injustice; do not describe her only as passive.

## Ending and interpretation
Rita is sexually assaulted and murdered. Songs, montage, lighting and shifts of time give the play an expressionistic form. Its critique of institutional racism and settler colonial violence can be discussed alongside the fact that its author is non-Indigenous and that Indigenous responses to its representation vary. Compare its portrayal with work by Indigenous playwrights rather than treating one play as an authoritative account of all First Nations experiences.''','0–10: content warning and context. 10–20: map court and memory. 20–30: examine listening and institutional power. 30–40: discuss theatrical form and ending sensitively. 40–50: consider representation.','How does the courtroom structure shape Rita’s story? What are the possibilities and limits of a non-Indigenous playwright’s representation?','https://www.canadiantheatre.com/dict.pl?term=The+Ecstasy+of+Rita+Joe'),
n('dream-mountain','Derek Walcott · Dream on Monkey Mountain: sequence', '''## Prison and vision
Makak, an elderly charcoal burner, is held in a colonial Caribbean jail with Tigre and Souris under Corporal Lestrade. He recounts a vision of a white woman who tells him of an African royal identity. The staging moves among jail, dream, memory and ritual; do not present every dream death as a literal event in the waking frame.

## Healing and escape
In the dream Makak and his friend Moustique encounter a sick man whom Makak appears to heal. Moustique impersonates Makak to gain money, is exposed and killed by a crowd. After further imprisonment, Makak and the prisoners escape; he wounds Lestrade, who later joins the journey. Tigre’s greed leads to conflict and his death in the dream.

## Dream kingdom and waking
Makak is imagined as king in Africa and judgments become increasingly violent. Pressed by Lestrade, Makak beheads the white apparition. The epilogue returns to the jail, where apparently dead figures are present again. Makak remembers his name, Felix Hobain, and is released; he plans to return home to Monkey Mountain.

## Reading
The dream can explore colonial racism, internalised ideals of whiteness and the difficulty of reclaiming identity, while also questioning revenge and fantasies of pure origins. Song, masks and transformations complicate the division between literal and symbolic events.''','0–10: map jail and dream. 10–20: discuss vision and healing. 20–30: trace escape and shifting loyalties. 30–40: compare dream kingdom and epilogue. 40–50: interpret the apparition.','Which deaths occur inside the dream? Why is the recovered name important?','https://ebooks.inflibnet.ac.in/engp06/chapter/derek-walcott-dream-on-monkey-mountain/'),
n('lion-jewel','Wole Soyinka · The Lion and the Jewel: Morning, Noon, Night', '''## Morning
In Ilujinle the schoolteacher Lakunle criticises Sidi’s carrying water and proposes marriage without the customary bride-price. Sidi wants the price paid, partly because otherwise neighbours may assume she is not a virgin. A visiting photographer’s magazine makes Sidi famous. Villagers re-enact the photographer’s visit through dance and mime; Baroka, the village Bale, notices Sidi’s images.

## Noon
Baroka’s senior wife Sadiku carries his proposal to Sidi, who refuses. Baroka then tells Sadiku that he has lost his sexual potency, presenting this as a secret. His story is a calculated deception. Lakunle describes Baroka’s obstruction of a railway, yet Baroka also shows interest in new technology: tradition and modernity are not sealed categories.

## Night
Sadiku tells Sidi the alleged secret. Sidi visits Baroka believing she can mock him safely. He flatters her and discusses a stamp bearing her image. Their encounter occurs offstage; Sidi later returns distressed and says she is no longer a virgin. Many readings understand the encounter as rape or coercion. Do not recast deception and distress as evidence of freely given consent. Lakunle offers marriage without bride-price; Sidi instead prepares to marry Baroka.

## Discussion
The comic staging and final wedding should be considered alongside gendered power and the limited choices available to Sidi. Avoid treating her beauty or confidence as a reason for violence.''','0–10: map the three times of day. 10–20: discuss the magazine and bride-price. 20–30: trace Baroka’s deception. 30–40: discuss consent and the ending carefully. 40–50: challenge a simple tradition/modernity binary.','Why does Sidi insist on bride-price? How does the offstage encounter complicate a purely comic reading?','https://www.litcharts.com/lit/the-lion-and-the-jewel/summary')]
d['course-40:4']=[
n('patient-1','The English Patient · chapters 1–3', '''## Chapter 1: The Villa
Near the end of the Second World War, a young Canadian nurse tends a badly burned man in an Italian villa once used as a hospital. Believed to be English, the patient cannot initially provide a reliable account of his identity. His memories move between the villa and the desert, where Bedouin rescuers cared for him after his plane burned. The nurse reads to him and gardens among damaged buildings.

## Chapter 2: In Near Ruins
The nurse is Hana. Caravaggio, a family friend and wartime thief whose thumbs have been mutilated, hears of her whereabouts and comes to the villa. Hana’s grief, exhaustion and attachment to the patient emerge gradually. A young Sikh sapper, Kirpal Singh, known as Kip, comes to clear explosives from the area.

## Chapter 3: Sometime a Fire
Kip’s dangerous work and memories of his British mentor Lord Suffolk reveal the skill and risk of bomb disposal. His fellow sapper Hardy is killed while dealing with a device. Hana and Kip grow close. Fragmented chronology means that a memory’s placement in the book is not necessarily its place in historical time.

## Teaching focus
The villa is a temporary refuge but remains threatened by hidden explosives. Care is personal and also shaped by war and empire.''','0–10: map the villa. 10–20: identify Hana, patient and Caravaggio. 20–30: explain Kip’s work. 30–40: sort present and memory. 40–50: discuss care amid danger.','Why does Hana stay? What is the effect of withholding a stable account of the patient’s identity?','https://www.coursehero.com/lit/The-English-Patient/summaries/'),
n('patient-2','The English Patient · chapters 4–6', '''## Chapters 4–5: desert and Katharine
The narrative turns to Western desert exploration in the years before and during war. The patient recalls expeditions, maps, the book of Herodotus he carries and the arrival of Geoffrey and Katharine Clifton. Katharine and the explorer begin an intense affair, which later ends. Their relationship is remembered in fragments, not as a simple continuous romance.

## Chapter 6: A Buried Plane
Caravaggio suspects the patient is the Hungarian explorer László Almásy, whose wartime activities involved the Germans. The story of a buried plane and the Cliftons’ crash begins to emerge. Geoffrey crashes his plane in an apparent attempt to kill the explorer; Geoffrey dies, and Katharine is seriously injured. Almásy leaves her in a cave and seeks help. Further details return later, particularly in chapter 9.

## Reading
Maps and exploration appear as intellectual fascination but also connect with military and imperial control. The novel’s damaged copy of Herodotus, filled with additions, resembles an archive repeatedly revised. The novel and the film adaptation do not have identical endings.''','0–10: trace the desert expedition. 10–20: locate the Cliftons. 20–30: discuss the crash and delayed revelations. 30–40: analyse maps and the Herodotus book. 40–50: compare memory and chronology.','Why are maps both useful and politically consequential? What remains uncertain at this stage?','https://www.coursehero.com/lit/The-English-Patient/summaries/'),
n('patient-3','The English Patient · chapters 7–10', '''## Chapters 7–8: Kip and the villa
Kip’s history as an Indian Sikh trained in Britain gives another perspective on wartime loyalty and empire. His mentor Lord Suffolk is killed while working on a bomb. At the villa, Kip and Hana’s intimacy grows within a landscape where explosives may be hidden in ordinary things. Their relationship offers connection without eliminating their different histories.

## Chapter 9: The Cave of Swimmers
The patient’s account expands. After Geoffrey’s crash, Almásy leaves the injured Katharine in the cave and seeks assistance; British authorities detain him. He later assists German agents crossing the desert. On returning to the cave, he finds Katharine dead. His attempt to fly away with her body ends when the aircraft catches fire, leading to his rescue and treatment. Caravaggio’s questions expose the limits of neat national loyalties.

## Chapter 10: August
News of the US atomic bombings of Hiroshima and Nagasaki transforms Kip’s view of the people and imperial order with whom he has worked. He threatens the patient with a rifle but does not shoot, then leaves the villa. The novel later imagines Kip as a doctor with a family in India, still remembering Hana. Hana writes to Clara about her father and her grief. The novel does not end with the film’s lethal morphine scene.

## Interpretation
Avoid reducing Kip’s anger to a private romantic disagreement: it responds to racialised global violence as well as to his relationships at the villa.''','0–10: discuss Kip’s training. 10–20: reconstruct the cave story. 20–30: explain the bombings’ impact. 30–40: compare the novel’s ending with adaptations. 40–50: analyse memory and empire.','Why does the bombing change Kip’s relationship to the villa? How does the later glimpse of Kip complicate the ending?','https://www.litcharts.com/lit/the-english-patient/summary'),
n('barbarians-early','Waiting for the Barbarians · chapters 1–3', '''## Content warning
The novel depicts torture, sexual power imbalances and state violence. Discuss without reproducing the violence graphically.

## Chapter 1
An unnamed magistrate administers a frontier settlement for an unnamed Empire. Colonel Joll arrives to investigate rumours of a threat from people the Empire calls “barbarians.” He interrogates prisoners using torture; a prisoner dies and a boy is injured. The magistrate is disturbed but initially remains an official who benefits from the system.

## Chapter 2
After Joll’s departure the magistrate encounters a young woman left disabled and partially blinded by torture. He gives her work and shelter and repeatedly washes her feet and body. His care is mixed with fascination and an unequal authority that he does not fully understand. She is not simply a symbol placed there to teach him a lesson.

## Chapter 3
The magistrate travels with soldiers to return her to her people through a difficult winter landscape. They become sexually intimate during the journey. At the meeting she chooses to remain with her people, although he asks her to accompany him back. When he returns, imperial officers arrest him on suspicion of aiding the enemy.

## Interpretation
“Barbarian” is the Empire’s label, not an objective description. First-person narration limits our access to the woman’s perspective.''','0–10: identify the frontier and content warning. 10–20: analyse Joll’s interrogation. 20–30: discuss care and unequal power. 30–40: follow the journey. 40–50: examine the narrator’s limits.','Why does torture fail as a reliable way of finding truth? What makes the magistrate’s care ethically complicated?','https://dougslangandlit.blog/2022/03/03/prose-study-waiting-for-the-barbarians-by-j-m-coetzee/'),
n('barbarians-late','Waiting for the Barbarians · chapters 4–6', '''## Chapter 4
The magistrate is confined and interrogated. When Joll returns with prisoners, he witnesses public brutality and intervenes, calling attention to the violence. The authorities humiliate and torture him. His suffering changes his position, but it does not erase his earlier role in the Empire or make his experience identical to that of those colonised.

## Chapter 5
The magistrate is released from confinement but lives in poverty and uncertainty, dependent on others. Rumours of invasion and military preparations unsettle the town. The Empire’s attempt to identify an enemy has helped produce fear and conflict.

## Chapter 6
The imperial expedition fails. Soldiers retreat and many die in the hostile landscape; officials and some residents abandon the settlement. The magistrate helps the remaining townspeople prepare for winter. He imagines writing a record of their settlement. Children build a snowman, recalling his earlier dream, while the future remains uncertain.

## Form and questions
The unnamed Empire and frontier make the story an allegory that can speak beyond one historical place, while its South African author’s context remains relevant. Ask how the narrator both challenges and reproduces imperial ways of seeing.''','0–10: revisit Joll’s prisoners. 10–20: trace the magistrate’s change in status. 20–30: explain military failure. 30–40: discuss the ending and snowman. 40–50: evaluate the narrator’s complicity.','Does the magistrate’s suffering cancel his past complicity? Why does the novel leave the town’s future unresolved?','https://www.supersummary.com/waiting-for-the-barbarians/summary/'),
n('once-upon','Nadine Gordimer · Once Upon a Time', '''## Frame
A writer-narrator has been asked for a children’s story but resists the expectation. At night a noise frightens her; she realises it may come from movement of the earth beneath the house. Unable to sleep, she invents a bedtime story.

## Story within the story
A wealthy family in a segregated South African setting lives behind increasing security: gates, alarms, higher walls and finally coils of razor wire. Fear of outsiders, shaped by racial inequality and actual reports of crime, drives each new measure. The family’s domestic workers and the grandmother figure also participate in the atmosphere of anxiety.

The mother reads their son a fairy tale about a prince making his way through thorns. Imitating the prince, the child tries to pass through the razor wire and is catastrophically injured. The final image shows adults carrying his bleeding body; the text’s wording leaves his precise survival status unconfirmed.

## Interpretation
Fairy-tale repetition and “happily ever after” become bitterly ironic. The security device harms someone it was installed to protect. Avoid reducing apartheid and racial hierarchy to a universal lesson that fear alone causes every form of violence.''','0–10: describe the frame. 10–20: list each security measure. 20–30: discuss racialised fear and privilege. 30–40: connect fairy tale and ending sensitively. 40–50: analyse irony.','Why include the writer’s framing story? How does the final accident challenge the family’s idea of safety?','https://www.enotes.com/topics/once-upon-time/questions/what-happens-to-the-little-boy-at-the-end-of-once-2560836'),
n('american-embassy','Chimamanda Ngozi Adichie · The American Embassy', '''## Content warning and structure
The story includes political persecution and the killing of a child. An unnamed woman waits for a US asylum interview in Lagos. Memories interrupt the queue and gradually reveal the events behind her application.

## Events
Her husband, a journalist critical of Nigeria’s military government, receives a threat and escapes with help. Men come to their home looking for him. Their four-year-old son Ugonna is shot; the woman escapes by jumping from a balcony and later buries him. In the queue, another applicant advises her on how to present her case.

## Interview and ending
Inside the embassy she struggles with being asked to provide evidence of danger and to turn her son’s death into an account for an official. She decides not to continue the interview and leaves, imagining planting flowers at Ugonna’s grave. The story does not establish that staying is safe, or that all asylum seekers should make the same choice.

## Analysis
Flashbacks register traumatic memory without needing a medical diagnosis. The narrator’s mixed feelings about her husband’s journalism complicate the public celebration of courage: political work also has consequences for families, without making the journalist responsible for the state’s violence.''','0–10: give content warning and establish the queue. 10–20: order the flashbacks. 20–30: discuss evidence and the interview. 30–40: consider grief and agency. 40–50: interpret the grave.','Why does the story move between queue and memory? What tension exists between a legal need for evidence and the narrator’s grief?','https://www.litcharts.com/lit/the-thing-around-your-neck/the-american-embassy')]
with open(P,'w',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Added',sum(len(d[f'course-40:{i}']) for i in range(5)),'selections')
