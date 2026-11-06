import json,copy
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,pre=False):
 r={'id':id,'title':title,'source':source,'text':f'# {title}\nIndian Writing in English II · Semester 5\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Questions\n{questions}\n\nTeaching draft: compare the prescribed text and edition before class.'}
 if pre:r['status']='preliminary'
 return r
def reuse(unit,id,newunit):
 x=copy.deepcopy(next(x for x in d[f'course-23:{unit}'] if x['id']==id))
 x['text']=x['text'].replace('Indian Writing in English I · Semester 4, Unit I',f'Indian Writing in English II · Semester 5, Unit {newunit}').replace('Indian Writing in English I · Semester 4',f'Indian Writing in English II · Semester 5, Unit {newunit}').replace('Unit coverage is incomplete: these selections do not yet cover all the prescribed texts. Check your assigned edition.\n\n','')
 return x
d['course-29:0']=[
n('iyengar-history','K. R. Srinivasa Iyengar · Indian Writing in English — introduction', '''## Scope
The syllabus lists the history without specifying chapters. This is a preliminary orientation, not a chapter-by-chapter account of the book. Confirm the assigned portions and edition.

Iyengar’s Indian Writing in English helped establish a field of literary study through a broad survey of writers and works. A literary history does more than provide dates: it selects authors, groups them into periods and genres, and proposes relationships among language, nation and literary value. Ask whose writings become visible through those decisions and whose do not.

## Historical frame
The English language spread through unequal colonial institutions, but Indian writers used and transformed it for a range of purposes, including reform, anti-colonial thought, poetry and fiction. Literature in English interacts with Indian-language traditions, self-translation and multilingual experience; it must not stand for all Indian literature. Later writers extend and question earlier canons.

Compare Iyengar’s choices with Naik’s history and the course readings. When quoting or describing his individual judgments, consult the actual book.''','0–10: ask what a literary history selects. 10–22: outline colonial and postcolonial contexts. 22–32: compare language and genre. 32–42: examine a contents page. 42–50: write one question about inclusion.','What choices shape a literary canon? Why is Indian literature larger than writing in English?','https://www.msuniv.ac.in/images/distance%20education/learning%20materials/ug%20pg%202023/pg%202021/MA%20english%202021/DEHM13%20-%20I%20Semester%20-%20Indian%20English%20Literature%20-%20I.pdf',True),
n('naik-history','M. K. Naik · A History of Indian English Literature — introduction', '''## Scope
The syllabus names Naik’s book but does not specify chapters. This orientation is preliminary: check the assigned edition and readings before treating it as a summary of his full argument.

Naik surveys Indian English literature historically and discusses terminology, periods and genres. Terms such as “Indo-Anglian” and “Indian writing in English” have been used in different ways. Distinguish original writing in English, self-translation and translations by others, and do not assume every historian draws the boundaries identically.

## Questions for study
A chronology helps readers locate early colonial-era texts, nationalist-era writing and post-Independence developments. But no period is uniform: caste, gender, region, class, religion and access to education shape who can write, publish and be read. The familiar story of linear progress can overlook multilingual, Adivasi and marginalised traditions.

Compare Naik and Iyengar through a chosen chapter: what do they include, what labels do they use, and how do they support their judgments? Cite the edition and page rather than attributing an unverified quotation.''','0–10: identify two literary histories. 10–20: map broad periods. 20–30: compare terms for the field. 30–40: discuss canon and exclusion. 40–50: formulate a question for the assigned chapter.','What makes a literary history selective? How do multilingualism and translation complicate the field?','https://dokumen.pub/a-history-of-indian-english-literature-1nbsped-9788126018727-8126018720.html',True)]
d['course-29:1']=[reuse(0,'harp-india','II'),reuse(0,'palanquin','II'),
n('gitanjali-13','Rabindranath Tagore · Gitanjali 13', '''## Edition and summary
The numbering here follows the English Song Offerings edition; verify that your assigned edition uses the same numbering. The speaker says the song they came to sing remains unsung. They have spent their days repeatedly preparing the instrument; the words are not ready and longing remains. A flower has not opened, and the wind sighs. The speaker has not seen or heard the beloved directly, though they have heard footsteps outside. A seat has been prepared, but the lamp remains unlit and the meeting has not yet happened.

## Reading
Preparations replace the desired act of song and encounter. The addressee may be read devotionally, but the poem presents longing rather than an explicit successful meeting. The instrument, flower, road, seat and lamp turn an inner state into a sequence of physical images.''','0–10: read silently and aloud. 10–20: list what has not yet happened. 20–30: trace images of preparation. 30–40: discuss longing and delay. 40–50: write an explanation of the unsung song.','Why does preparation not become fulfilment? How does the poem convey hope and frustration together?','https://www.gutenberg.org/cache/epub/7164/pg7164-images.html'),
n('gitanjali-14','Rabindranath Tagore · Gitanjali 14', '''## Edition and summary
This follows numbering in the English Song Offerings; check your assigned edition. The speaker addresses a divine “thou,” thanking the addressee for gifts given without request: sky, light, body, life and mind. The speaker understands delays and refusals as a discipline that protects against excessive or uncertain desire. Sometimes the speaker lingers; at other moments they awaken and hurry towards a goal, but the divine presence remains hidden. The repeated daily process is understood as a making-ready for fuller acceptance.

## Reading
The poem transforms apparent denial into spiritual education. Its contrast between unasked gifts and deferred fulfilment creates tension: gratitude coexists with longing. Discuss the speaker’s interpretation rather than claiming that every experience of deprivation is beneficial.''','0–10: list the unasked gifts. 10–22: paraphrase delay and desire. 22–32: compare lingering with seeking. 32–42: debate the speaker’s interpretation. 42–50: write about the poem’s devotional voice.','What gifts does the speaker recognise? How can refusal be interpreted as preparation in this poem?','https://www.gutenberg.org/cache/epub/7164/pg7164-images.html'),
n('old-playhouse','Kamala Das · The Old Playhouse', '''## Content note
The poem describes coercive control and distress within a marriage; discussion need not require personal disclosures.

## Summary
Addressing a controlling “you,” the speaker imagines herself as a swallow whose urge to fly is to be subdued. She had hoped to understand herself and grow, but finds that her husband’s lessons centre on him. Physical intimacy and routine domestic service do not supply the reciprocity she seeks. His overpowering ego makes her feel diminished; closed windows, artificial light and stale flowers suggest an airless room. Her mind becomes an old playhouse with its lights extinguished, where song and dance have stopped. The final image of Narcissus and the breaking of mirrors expresses a desire to escape a destructive, self-absorbed version of love.

## Reading
Trace the movement from flight to enclosure to the imagined breaking of reflections. The speaker is a crafted poetic voice; do not treat every image as a documented biographical fact. Sexualised language, power and the contrast between body and emotional recognition matter.''','0–10: set discussion boundaries. 10–20: identify the swallow and room. 20–30: paraphrase the speaker’s complaint. 30–40: interpret the playhouse and mirrors. 40–50: write about freedom and control.','Why does the speaker describe herself as diminished? What might breaking mirrors represent?','https://www.poemhunter.com/poem/the-old-playhouse/'),
reuse(0,'mahapatra-twilight','II'),
n('background-casually','Nissim Ezekiel · Background, Casually', '''## Summary
The speaker presents a self-portrait of a frightened, awkward child, growing up as a Jewish boy at a Roman Catholic school where he experiences hostility and prejudice. He recalls Friday prayers, curiosity about different religious traditions and a search that does not settle easily. At twenty-two he goes abroad; in London he describes poverty, isolation, philosophy and poetry. Returning to India by ship, he asks how to feel at home. He recalls family attitudes, employment and marriage, and describes his ancestors among Indian caste communities.

The later speaker reflects on writing, observation and the discrepancy between outsiders’ praise and his own sense of complexity. He declares a commitment to stay where he is, though he calls that place “backward”: the word can be read critically as part of his ironic, troubled self-positioning, not an objective verdict on India.

## Reading
The title’s casual manner contrasts with difficult questions about exclusion and belonging. The poem is autobiographical in orientation but shaped by irony and selection; avoid repeating its characters’ religious stereotypes as facts.''','0–10: identify the speaker’s changing locations. 10–22: discuss school and prejudice. 22–32: trace London and return. 32–42: analyse the final commitment. 42–50: explain the title’s irony.','Why is belonging a question rather than a certainty? How does irony complicate the final claim?','https://kavitaezekielpoetry.com/nissim-ezekiel-2/'),
n('floating-island','Mamang Dai · Floating Island', '''## Summary
The speaker imagines a mountain reaching into water and addresses a “dear one,” asking them to stay and rest. A sleeping woman and birds nesting within her create an intimate landscape of shelter and dreaming. The current spins unpredictably; the speaker says farewell to the mountain while clinging to the life of water. A burnt hill, marked imaginatively by the faces of the speaker’s people, brings collective memory into the scene. Moonrise reveals change and dreams. The difficult hillside offers little rest, and feelings left unspoken become sadness.

## Reading
Landscape here is relational rather than merely decorative: mountain, river, body and community memory intersect. The shifting “I” and “you” invite more than one reading; do not turn the poem into a fixed plot or assume each image has only one meaning. Contrast tenderness with uncertainty, loss and change.''','0–10: map mountain and water. 10–22: paraphrase the address and sleeping woman. 22–32: consider the burnt hill and people. 32–42: discuss change and silence. 42–50: support one interpretation of the floating image.','How does landscape carry memory? Why might the current and the farewell complicate the idea of a safe home?','https://www.festivaldepoesiademedellin.org/en/Festival/31/MamangDai/')]
d['course-29:2']=[
n('clarinda','A. Madhaviah · Clarinda — preliminary story guide', '''## Scope and warning
The full novel and its chapter divisions have not yet been checked; this is a preliminary narrative outline, not a chapter-by-chapter guide. It includes forced sati and deception in marriage. The novel reimagines a historical figure and should not be treated as a transparent biography.

## Main story
Clavirunda, later called Clarinda, grows up in the region of Tanjore and receives an education from her grandfather. After his death she is married to an elderly Dewan who treats her badly. When he dies she faces pressure to undergo sati. An English officer, Lyttelton, rescues her and gives her shelter. Their relationship develops; she receives Christian instruction and converts.

A scholarly account describes Lyttelton as concealing an existing marriage in England and conducting a sham wedding with Clarinda. This complicates a simple romance of rescue and freedom. The novel also associates Clarinda with charitable action and women’s education. Verify the sequence and ending in the full assigned novel rather than assuming that its fictional events accurately describe the historical Clarinda.

## Interpretation
Compare education, widowhood and women’s choices with the unequal power of colonial encounter. Madhaviah’s fictional Christian–Hindu dialogue can be examined without treating either tradition as internally uniform.''','0–10: distinguish history and historical fiction. 10–20: map education and marriage. 20–30: discuss rescue and power. 30–40: examine conversion and reform. 40–50: list chapters and details to verify in the edition.','How does education shape Clarinda’s possibilities? Why is a rescue narrative not automatically a story of equal power?','https://artefacts-discovery.researcher.life/full_text/DA-2/d9/d9c408da9743383bb81b8a6da908a5da/full_text/a8b50ce8007d378ca83442d1013c7cb1.pdf',True),
n('coolie','Mulk Raj Anand · Coolie — journey and major episodes', '''## Content note
The novel contains child labour, physical abuse, communal violence and sexual exploitation. “Coolie” is a historical labour term that can be derogatory; discuss who uses it and why.

## Bilaspur and Sham Nagar
Munoo is an orphan of about fourteen from a hill village, living with his uncle and aunt. Poverty sends him to Sham Nagar to work as a domestic servant in Babu Nathoo Ram’s household. The promise of town life meets unequal power, exhausting work and Bibiji’s abuse. A frightening incident involving the family’s child contributes to Munoo’s flight. The episode exposes how class determines whose mistakes are forgiven.

## Daulatpur
On a train Munoo encounters Prabha Dayal, who takes him into the pickle business. Prabha and his wife offer kindness, but Prabha’s partner Ganpat treats the boy harshly. Financial treachery ruins the enterprise. Munoo tries to survive as a porter, competing against stronger workers, and experiences the insecurity of casual labour. A sympathetic elephant driver eventually helps him travel to Bombay.

## Bombay
The vast city initially excites Munoo, then exposes him to hunger and crowded, precarious life. He meets Hari and Lakshmi and works in a cotton mill. Friendship and political discussion appear alongside exploitation and conflict over wages. Labour organisation is undermined amid violence and communal division. These events show how employers and social divisions affect workers collectively as well as individually.

## Simla and the ending
After a motor accident involving Mrs Mainwaring, Munoo enters her employment and goes to Simla. He works as a servant and pulls a rickshaw; interpretations of their unequal relationship also address sexual exploitation. Hard labour and illness overwhelm him, and he dies of tuberculosis while still young. Returning to the hills does not restore the lost safety of childhood.

## Interpretation
The episodic journey links domestic service, small enterprise, industrial work and colonial leisure. Munoo encounters kindness, but individual kindness cannot remove structural poverty. Use this sequence as a guide and check chapter divisions and detailed events in the edition.''','0–10: draw Munoo’s route. 10–20: compare Sham Nagar and Daulatpur. 20–30: map workers and conflict in Bombay. 30–40: discuss Simla and illness. 40–50: write about individual kindness and systemic injustice.','Why does each new location fail to secure Munoo’s future? How does the novel connect class and child labour?','https://english.shabd.in/coolie-mulk-ray-anand/book/10286542'),
n('god-small-things','Arundhati Roy · The God of Small Things — story and narrative time', '''## Content note and narrative structure
The novel contains child sexual abuse, caste violence, police brutality, drowning and incest. Its chapters move back and forth between 1969 and the adult twins’ reunion in 1993. The sequence below is chronological for clarity, not the order of narration.

## Family and children
Ammu leaves an abusive marriage and returns with twins Estha and Rahel to her family’s home in Ayemenem, Kerala. Her brother Chacko has a daughter, Sophie Mol, with his former wife Margaret. Velutha, a skilled Paravan worker at the family pickle factory, is close to the children. Caste hierarchy shapes how the family and community treat him.

## A visit and hidden wounds
After Margaret’s later husband dies, she and Sophie visit. Family attention to the English visitors makes the twins feel their own uncertain place. At a cinema a man selling drinks sexually assaults Estha. The child’s fear helps motivate a plan to find a place of escape across the river. The adult narrative returns repeatedly to fragments of these events instead of presenting trauma as a simple linear confession.

## Ammu and Velutha
Ammu and Velutha begin a secret relationship across caste boundaries. When it is discovered, the family locks Ammu in her room and turns against Velutha. Angry and distressed, Ammu tells the twins they are a burden; they decide to run away. Sophie joins them. Their boat overturns and Sophie drowns; the twins reach the other side and sleep near the History House, unaware Velutha is also there.

## False accusation and its aftermath
Baby Kochamma tells police a false story accusing Velutha of assault and abduction. Police find him and beat him brutally in front of the children. When the truth threatens to expose the false report, Baby Kochamma pressures the twins by saying their mother and they could be imprisoned. Estha is made to identify Velutha as the abductor. Velutha dies in custody. Ammu tries to tell the truth, but the police humiliate her. Chacko expels Ammu and the twins are separated: Estha is sent to his father; Ammu later dies alone.

## The adult reunion and final scene
Rahel returns to Ayemenem after years away and reunites with Estha, who has stopped speaking. Their adult sexual encounter is presented in the shadow of shared grief and damaged boundaries, not as a cure for trauma. The novel closes by moving back to Ammu and Velutha’s first night together, with their fragile promise of tomorrow. This ending preserves tenderness while the reader already knows the violence to come.

## Interpretation
The so-called “Love Laws” describe social rules about who may love whom and how much. Child perspectives, repetition, unusual capitalisation and shifts in time expose how family, caste, gender and institutions enforce those rules. This guide covers major events, not every chapter.''','0–10: make two timelines, 1969 and 1993. 10–20: map family and caste relationships. 20–30: trace the false accusation. 30–40: explain why the final scene returns to the past. 40–50: support a claim about narrative time.','Why is Velutha falsely accused? What does the chronological summary miss about Roy’s narrative order?','https://www.litcharts.com/lit/the-god-of-small-things/summary'),
reuse(2,'laburnum','III'),
n('adivasi-dance','Hansda Sowvendra Shekhar · The Adivasi Will Not Dance', '''## Story sequence
Mangal Murmu is an ageing Santhal musician and troupe leader. He recounts the importance of music and dance to community life alongside the growing pressure of mining, industry and displacement in Jharkhand. Land and livelihoods are taken for projects presented as development; he contrasts official promises with the losses experienced by local people.

Officials invite Mangal’s troupe to perform at a function associated with a thermal power project and a visit by the President of India. The proposed celebration becomes intolerable when he learns that families from villages have been displaced for the project; his daughter and her children are among those affected. The event expects Adivasi culture to entertain dignitaries while the people who sustain that culture bear the costs of the project.

At the microphone Mangal refuses the expected performance and speaks about land, homes and injustice. He and members of the troupe are beaten down. His refusal is not a rejection of dance itself: it is a refusal to make culture serve as decoration for dispossession.

## Interpretation
Read Mangal as a particular narrator, not a spokesperson who makes all Adivasi experiences identical. Discuss voice, development, cultural representation and the difference between a fictional story and the historical conditions it evokes.''','0–10: identify narrator and setting. 10–20: map land, project and family. 20–30: explain the invitation to perform. 30–40: discuss refusal and cultural appropriation. 40–50: write whose version of development is challenged.','Why does Mangal refuse to dance at this event? How is culture separated from the rights of the people who create it?','https://speakingtigerbooks.com/product/the-adivasi-will-not-dance/')]
d['course-29:3']=[
n('taledanda','Girish Karnad · Taledanda — story and conflict', '''## Setting and warning
The play imagines twelfth-century Kalyana and the Sharana movement associated with Basavanna. It includes caste violence and political murder. It is a dramatic reworking of history, not a substitute for historical evidence.

## Reform and power
Basavanna serves King Bijjala and gathers devotees, or sharanas, committed to spiritual fellowship and opposition to caste hierarchy. Their community includes people from different occupations and birth groups. Bijjala’s support is valuable but politically fragile. His son Sovideva and conservative advisers resent Basavanna’s influence; a challenge involving the royal treasury fails when its accounts are found intact.

## The marriage
The proposal that Kalavati, daughter of the Brahmin Madhuvarasa, marry Sheelavanta, son of the cobbler Haralayya, tests whether declared equality can be practised. Both families support the marriage, while Basavanna fears the violence that may follow. Bijjala is anxious about public order but provides protection, and the wedding takes place. Its opponents see the alliance as a threat to caste hierarchy.

## Retaliation and collapse
Political intrigue strips Bijjala of power as Sovideva takes control. Violence against sharanas and the families associated with the marriage escalates. Jagadeva and others turn to revenge; Jagadeva kills Bijjala despite Basavanna’s commitment to nonviolence. Basavanna’s departure and reported death are associated with the movement’s devastating crisis. Consult the assigned script for the precise staging and order of final reports.

## Interpretation
The issue is not that equality itself causes injustice: entrenched caste power and political calculation produce opposition and violence. The play also examines disagreements over tactics within a reform movement. Compare public principles with what people do when their own families and power are involved.''','0–10: introduce Kalyana and sharanas. 10–20: map Bijjala, Basavanna and Sovideva. 20–30: discuss the marriage. 30–40: trace retaliation. 40–50: explain the tension between equality and nonviolence.','Why does the marriage test the movement’s ideals? How do caste power and political rivalry intersect?','https://puneresearch.com/media/data/issues/5ccff7f7e553f.pdf'),
n('final-solutions','Mahesh Dattani · Final Solutions — story and dramatic form', '''## Content note
The play depicts communal prejudice and violence. The beliefs of individual characters or mobs must not be treated as truths about whole religious communities.

## Past and present
Young Daksha records her experience in a diary in the years after Partition; as an older woman she is called Hardika. She remembers loss and her friendship with Zarine, a Muslim girl with whom she shares an interest in music. Family pressures and communal conflict damage their friendship. The play moves between Daksha’s memories and her family’s present, while a masked chorus adopts different communal identities.

## Shelter during a riot
Hardika lives with her son Ramnik, his wife Aruna and their daughter Smita. Communal tension intensifies outside. Two young Muslim men, Javed and Bobby, also called Babban, flee a mob and seek shelter. Ramnik admits them despite family objections. Smita knows them through her friend Tasneem, Javed’s sister and Bobby’s intended partner. Their presence exposes disagreements within the household rather than a single Hindu or Muslim viewpoint.

## Stories and confrontations
Javed’s anger is linked to experiences of discrimination, and he has worked as a hired participant in communal violence. Bobby challenges him while trying to keep them safe. Ramnik’s generous gesture is complicated by guilt, while Aruna’s concerns about ritual purity and Smita’s frustrations reveal tensions around gender and belief. The chorus gives theatrical form to the pressure and interchangeability of mob voices.

## Ending
Bobby enters the prayer area and holds an image of Krishna, challenging the idea that his touch contaminates it. The gesture offers a possibility of understanding, not proof that prejudice has disappeared. Ramnik reveals that his father and grandfather burned Zarine’s family shop and acquired it cheaply, exposing a concealed history behind Hardika’s memories. The ending asks whether acknowledgment and change are possible; it does not supply a neat final solution.

## Technique
Compare the diary, shifting time and masks: each shows how present conflicts inherit selected stories of the past.''','0–10: set respectful discussion rules. 10–20: map Daksha and Hardika. 20–30: sequence the guests’ arrival and confrontations. 30–40: interpret chorus and final revelations. 40–50: explain why the title is ironic.','What does the truth about Zarine’s shop change? Why does Bobby’s gesture not automatically end communal violence?','https://www.drishtithesight.com/volume-ix/resonance-of-communal-dis-harmony-in-mahesh-dattanis-final-solutions/'),
n('lights-out','Manjula Padmanabhan · Lights Out — story and staging', '''## Content note
This play centres on sexual violence, victim-blaming and bystander inaction. Offer a non-graphic alternative activity and do not ask students to recount personal experiences. A person’s occupation or clothing never makes sexual assault acceptable.

## Story
In their apartment Leela is disturbed by recurring cries from a neighbouring construction site and asks her husband Bhasker to contact the police. He minimises the events and hesitates to become involved. Their friend Mohan arrives, interested in witnessing what is happening. Leela’s friend Naina also hears and sees enough to identify an assault.

Rather than acting promptly, the group debates what they are witnessing. Bhasker and Mohan offer explanations, including a religious ritual, and suggest that the victim’s presumed identity might make the assault less serious. The play exposes these claims as evasions and victim-blaming. Surinder later proposes force; his aggressive treatment of Naina complicates his apparent desire to intervene. Proposed actions, including photographing the crime, become another form of delay and spectacle.

The sounds cease before effective help is given. The ending does not establish a rescue. The play’s closing note relates the drama to an eyewitness account while identifying its characters as fictional.

## Performance and ethics
The apartment and window put spectators in the position of observing observers. Sound, pauses and offstage action make inaction dramatically visible without requiring a graphic re-enactment. Analyse the responsibility of bystanders without assuming that physical confrontation is always a safe response in real emergencies.''','0–10: explain content and offer an alternative. 10–20: track Leela’s request for help. 20–30: identify excuses and victim-blaming. 30–40: analyse window and sound. 40–50: write about the difference between watching and acting.','How do explanations delay action? What does the audience learn through sounds and reactions rather than seeing the crime?','https://www.the-criterion.com/V8/n4/IN36.pdf')]
d['course-29:4']=[reuse(0,'macaulay-minute','V'),reuse(0,'aurobindo-renaissance','V'),
n('ambedkar-castes','B. R. Ambedkar · Castes in India: Their Mechanism, Genesis and Development', '''## Context and argument
Ambedkar presented this paper in 1916 and it was published in 1917. He examines caste as a social mechanism rather than accepting inherited explanations as self-evident. His central claim is that endogamy—marriage within a bounded group—is crucial to maintaining caste. He distinguishes it from exogamy, such as rules requiring marriage outside a clan, and argues that caste arises through imposing endogamy on an existing pattern of exogamy.

## How the mechanism is maintained
Ambedkar asks how a group sustains endogamy when a spouse dies. In his analysis, the group treats widows and widowers unequally. He identifies sati, enforced widowhood and the marriage of girls to older widowers as mechanisms that can preserve the marriage boundary. These are his critical explanations of oppressive practices, not recommendations or neutral descriptions of women as surplus. His terminology reflects the paper’s historical argument and should be discussed critically.

## Genesis and questions
He proposes that Brahmins enclosed themselves through endogamy and that other groups came to form closed castes through processes including imitation and social constraint. This historical account should be evaluated with later research, not asserted as the only possible explanation. The paper connects control over marriage, gender and social hierarchy; compare it with later anti-caste thought without assuming every argument is identical.''','0–10: define endogamy and exogamy. 10–20: explain their combination. 20–30: trace gendered mechanisms. 30–40: discuss historical explanation and evidence. 40–50: write how marriage and caste are linked.','Why is endogamy central to Ambedkar’s argument? How does his analysis connect caste with control of women?','https://anotherworldarchives.org/br-ambedkar/castes'),
n('nehru-religion','Jawaharlal Nehru · Religion, Philosophy and Science', '''## Context
This section of The Discovery of India reflects Nehru’s search for a way to think about truth, values and public life. He wrote the book during imprisonment in the 1940s. Treat the essay as a situated argument, not a definitive account of all religion or all science.

## Argument
Nehru criticises dogma and superstition as he has encountered them in organised religion, while recognising the human search for meaning and ethical values. He values science for its disciplined inquiry, willingness to test ideas and ability to expand knowledge and material possibilities. Yet he is troubled by a purely factual science detached from questions of purpose and human values.

He seeks an approach in which scientific temper is allied with philosophical reflection and openness to what remains unknown. This does not mean that religious claims are automatically scientific, or that science alone answers every moral question. Ask how his argument distinguishes scientific methods from their social uses.

## Reading critically
Identify where he is describing his own responses and where he makes general claims. Compare his vision with Aurobindo’s account of cultural renewal and ask how the two writers balance inherited traditions and modernity.''','0–10: define dogma and inquiry. 10–22: trace his critique of religion. 22–32: list science’s achievements and limits. 32–42: discuss philosophy and values. 42–50: write a balanced account of his position.','Why does Nehru value scientific temper? Why does he think factual knowledge alone is insufficient?','https://library.bjp.org/jspui/bitstream/123456789/277/1/The-Discovery-Of-India-Jawaharlal-Nehru.pdf'),
n('sen-justice','Amartya Sen · An Approach to Justice', '''## Context and central distinction
“An Approach to Justice” is the introduction to The Idea of Justice. Sen distinguishes seeking a perfectly just set of arrangements from comparing feasible alternatives to reduce injustice. He argues that assessment must consider actual lives and outcomes, not only institutions and rules as ideally designed. Institutions matter; his criticism is not that they can be ignored.

## Three children and a flute
Anne can play the flute; Bob is poor and has no toys; Carla made the flute. Each offers a different reason for receiving it: effective use or pleasure, need and equality, or entitlement through labour. Sen uses the case to show that serious and potentially impartial reasons can conflict; he does not present a single obvious winner that resolves every theory of justice. Public reasoning must engage with competing grounds.

## Niti and nyaya
Sen uses a distinction from Sanskrit thought: niti concerns organisational propriety and correct conduct, while nyaya points to justice as realised in the lives and world people actually experience. For him, evaluating an apparently proper rule also requires asking what happens under it, including behaviour and social conditions.

## Apply
Compare two practical policies for access to education: who can actually attend, participate and benefit? Explain evidence and competing values rather than assuming that a formally equal rule produces equal opportunity.''','0–10: pose the flute case. 10–22: identify three reasons. 22–32: distinguish ideal arrangements from realised outcomes. 32–42: compare two education policies. 42–50: defend a judgment while recognising a competing reason.','Why do Anne, Bob and Carla each have a claim? How do arrangements and realised justice differ?','https://books.google.com/books/about/The_Idea_of_Justice.html?id=enqMd_ze6RMC')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
