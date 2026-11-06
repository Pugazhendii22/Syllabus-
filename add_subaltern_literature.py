"""Add sourced teaching drafts for the five Subaltern Literature syllabus units."""
import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f: data=json.load(f)
def n(id,title,body,lesson,questions,source,preliminary=False):
 x={'id':id,'title':title,'source':source,'text':f'# {title}\nSubaltern Literature · Semester 6\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: check the assigned text, translation and edition before teaching; verify quotations directly.'}
 if preliminary:x['status']='preliminary'
 return x
data['course-36:0']=[
n('betik','Bailey Betik · Understanding Subaltern Studies', '''## Starting point
“Subaltern” describes a position of subordination in relation to power, not an identity shared in the same way by every disadvantaged person. Class, caste, gender, colonial rule, race and other relationships can intersect. Ask: subordinated by whom, in which place and at what time?

## Betik’s overview
Betik explains the influence of Antonio Gramsci and the South Asian Subaltern Studies collective associated with Ranajit Guha. From the early 1980s its historians challenged accounts that centred colonial rulers and nationalist elites while treating peasants and workers as followers. They studied popular politics, consciousness and agency in their own right.

## Reading evidence
Official records often preserve the perspectives of authorities. Reading an archive “against the grain” asks what its categories, silences and descriptions reveal unintentionally. A police report about a protest may tell us about official fear as well as protest; it does not transparently reproduce protesters’ own words. Compare with oral history, local writing and other evidence when available.

## Debate
A strict elite/subaltern divide can hide differences and changing positions within communities. Spivak’s question of representation also asks whether institutions can hear or translate a marginalised person’s account without reshaping it. Do not assume marginalised people have no agency or that a scholar simply “gives” them a voice.''','0–10: define power as a relationship. 10–20: locate the collective. 20–30: read a hypothetical police report critically. 30–40: examine the elite/subaltern binary. 40–50: write two questions for an archive.','How is subalternity relational? What can and cannot be inferred from an official record?','https://scholarblogs.emory.edu/postcolonialstudies/2020/02/17/subaltern-studies/'),
n('ludden','David Ludden · Introduction to Reading Subaltern Studies', '''## Identifying the reading
The syllabus prints “David Ludde”; the editor is David Ludden. His introduction, “A Brief History of Subalternity,” appears in Reading Subaltern Studies: Critical History, Contested Meaning and the Globalization of South Asia (2002). The title already signals a field with disagreements rather than one single settled meaning.

## Intellectual history
Ludden traces changing uses of subalternity, the collective’s South Asian historiographical intervention and the international movement of its ideas. Ask how a concept develops when historians, literary scholars and readers in different regions use it for different purposes. Global influence can increase visibility while also changing a term’s meaning.

## A major criticism
Ludden reports concerns that a rigid division between elite and subaltern can flatten social mobility, class differences and relationships among subordinated groups. A useful historical account must investigate those differences, not assume all elites or all subalterns act identically.

## Method
Distinguish the historian’s own argument from positions the historian summarises or criticises. The introduction is not evidence that every member of the collective held precisely the same theory. Compare Ludden’s account with Guha’s preface and Chakrabarty’s retrospective.''','0–10: identify book and editor. 10–20: outline the project’s movement. 20–30: explain the binary criticism. 30–40: compare Guha and Ludden. 40–50: write a nuanced definition.','Why does global circulation change a concept? How can a binary obscure mobility and internal differences?','https://nyuscholars.nyu.edu/en/publications/introduction-a-brief-history-of-subalternity'),
n('freire','Paulo Freire · Introduction to Pedagogy of the Oppressed', '''## Edition note
The syllabus says “Introduction.” English editions may include a translator’s introduction, a foreword and Freire’s own preface. Confirm the exact assigned pages. The discussion below identifies Freire’s preface and gives clearly labelled connections to later chapters rather than pretending all concepts appear in the assigned introduction.

## Preface: freedom and critical awareness
Writing in relation to educational work in Brazil and experiences of political exile, Freire discusses concerns that critical consciousness might create disorder. He examines fear of freedom and argues for reflection on social reality. Education is connected to ethical and political questions, not simply the transmission of information.

## Connections beyond the preface
In Chapter 1 he develops humanisation and oppression, arguing for a pedagogy made with oppressed people rather than imposed on them. Praxis joins reflection and action. In Chapter 2 his “banking” model criticises treating learners as passive containers; problem-posing education instead encourages dialogue and shared inquiry. These are useful links but should not be cited as if they were all from the preface.

## Classroom application
Use a local example students can safely discuss: who decides classroom rules and whose knowledge counts? Invite critique without demanding that students disclose personal experiences of oppression. Dialogue does not mean the teacher has no responsibility to prepare or assess.''','0–10: identify which introduction is assigned. 10–20: explain critical consciousness. 20–30: distinguish preface and later chapters. 30–40: redesign one classroom activity. 40–50: reflect on dialogue.','What is praxis? Why must the assigned introduction be distinguished from later chapters?','https://www.historyisaweapon.com/defcon2/pedagogy/',True),
n('senghor','Léopold Sédar Senghor · Négritude', '''## Context and selection
Négritude emerged among Francophone Black intellectuals including Aimé Césaire and Senghor in response to colonial racism and cultural denigration. The syllabus names “On Negritude” without a full edition. This is an introductory framework, not a verified close reading of a specific assigned essay; confirm its title and text.

## Key ideas
Senghor argues for affirming Black and African cultural values against colonial claims of inferiority. In his vision, an affirmation of cultural particularity can contribute to a wider human community rather than require cultural isolation. The movement was varied; Césaire’s and Senghor’s emphases should not be treated as identical.

## Debate and limitations
Senghor’s contrasts between African and European ways of feeling and reasoning can be criticised as essentialist: they risk attributing a single timeless nature to diverse peoples and repeating racial stereotypes. Explain this as a critical objection to his historical formulation, not as a biological truth about race. Négritude should be situated in the politics of colonial rule, intellectual exchange and anticolonial assertion.

## Comparison
Compare the assertion of cultural dignity with Subaltern Studies’ attention to historical agency. Neither movement is identical to the other: their locations, histories, methods and political vocabularies differ.''','0–10: define colonial assimilation. 10–20: locate Négritude. 20–30: examine affirmation and universality. 30–40: debate essentialism. 40–50: compare historical contexts.','Why was cultural affirmation politically important? What can be lost when diverse cultures are described as one essence?','https://www.ascleiden.nl/content/webdossiers/leopold-sedar-senghor',True),
n('ambedkar','B. R. Ambedkar · Castes in India', '''## Publication and problem
Ambedkar presented “Castes in India: Their Mechanism, Genesis and Development” in 1916; it appeared in 1917. He questions existing definitions and asks how caste maintains closed social boundaries.

## Endogamy and exogamy
Endogamy means marriage within a group; exogamy requires marriage outside a specified kin or clan group. Ambedkar argues that caste arises through imposing caste endogamy upon a society that also observes clan exogamy. Membership by birth and restrictions on intermarriage are closely connected in his argument.

## Caste and gender
He analyses how rules surrounding widows and widowers could maintain endogamy, discussing sati, enforced widowhood and the marriage of girls. His language of “surplus” women and men belongs to his analytical reconstruction; it must not be adopted as a judgment on people’s worth or treated as a universal account of every community. His argument makes control of women’s lives central to the reproduction of caste.

## Genesis and critique
Ambedkar proposes that priestly groups enclosed themselves and that imitation and enforced exclusion helped produce further closed groups. This is a historical argument open to evidence and debate, not proof that one individual invented caste. Distinguish this early paper from his later work Annihilation of Caste.''','0–10: define endogamy and exogamy. 10–20: reconstruct the argument. 20–30: discuss gendered rules sensitively. 30–40: compare imitation and exclusion. 40–50: write the central thesis.','How can endogamy and clan exogamy coexist? What role does control of marriage play in Ambedkar’s explanation?','https://dravidapozhil.pmu.edu/Castes-In-India.aspx')]
data['course-36:1']=[
n('gramsci','Antonio Gramsci · Methodological criteria', '''## Position and power
In the Prison Notebooks, Gramsci considers subordinate social groups in relation to dominant groups and the state. Their history is often recorded in fragments, because institutions are more likely to preserve the actions of rulers than the independent activities of subordinated people. Fragmentary evidence does not mean such groups lack thought or action.

## A programme of research
The “methodological criteria” ask historians to investigate how subaltern groups form, how they relate to dominant political formations, and how their own organisations and claims for autonomy develop. He also asks how ruling groups respond to and try to control them. Reconstructing these changing relationships requires specific historical evidence.

## Hegemony
Hegemony refers to leadership sustained through a combination of consent, institutions and cultural influence, not simply a synonym for any act of violence. Coercion and consent may interact. Ask how schools, associations, parties and the state shape what appears normal or possible.

## A distinction
Guha adapts the term for colonial South Asia rather than merely repeating Gramsci. Explain what changes across contexts and avoid implying that a subordinate group has only one homogeneous experience.''','0–10: introduce context of notebooks. 10–20: explain fragmented records. 20–30: trace the research programme. 30–40: apply hegemony to an example. 40–50: compare with Guha.','Why might records of subaltern groups be fragmentary? How is hegemony more than coercion alone?','https://lh.journals.yorku.ca/index.php/lh/article/download/15042/14089'),
n('guha','Ranajit Guha · Preface to Subaltern Studies', '''## The project
In the first volume’s preface, Guha presents subalternity as a general condition of subordination that may involve class, caste, age, gender, office and other relationships. The collective seeks to correct elitist emphases in research on South Asian history and society.

## People as historical actors
In the associated essay on colonial Indian historiography, Guha challenges histories that explain nationalism mainly through colonial officials or Indian elites. He asks historians to attend to popular political activity and consciousness. Identify the preface and associated essay separately: not every argument in the latter is a direct statement from the former.

## Autonomy and evidence
Guha’s account of a domain of subaltern politics contests the assumption that peasants merely follow elite leaders. Autonomy is an analytical claim to examine, not proof that subordinate and elite politics never influence each other. Consider petitions, memories and hostile administrative records as situated sources.

## Limits and debate
How do caste, gender and class differentiate a supposedly unified “people”? Later critics question binary categories and historians’ ability to recover consciousness. Read this as a productive debate about evidence and representation.''','0–10: define the project. 10–20: distinguish preface and essay. 20–30: explain elite-centred history. 30–40: test autonomy using a hypothetical protest. 40–50: write one criticism.','What does Guha mean by subordination? Why should the preface and later essay not be conflated?','https://ebooks.inflibnet.ac.in/engp16/chapter/minority-subaltern-studies/'),
n('chakrabarty','Dipesh Chakrabarty · Subaltern Studies and Postcolonial Historiography', '''## Guiding question
In this 2000 essay Chakrabarty asks how the original programme of Subaltern Studies can be understood as a postcolonial project rather than simply another version of radical or Marxist history. He traces its development from an intervention in Indian historiography to wider debates across disciplines.

## Colonial difference
A history that places Europe on a single universal timeline of progress can portray colonised societies as not yet modern. Chakrabarty asks readers to examine the assumptions built into such categories. This is not a request to ignore Europe or reject all concepts originating there; it is a challenge to treating one historical experience as the universal standard.

## Agency and consciousness
Subaltern actions need not fit elite expectations of rational modern politics to be historically meaningful. The task is to study people’s practices and the categories through which records make those practices legible, while recognising resistance, accommodation and internal difference.

## Comparison with Thompson
Both projects attend to ordinary people, but Chakrabarty argues that the colonial relationship and questions of historical difference make the South Asian intervention more than a simple transfer of British history from below. Treat this as his argument to evaluate, not a claim that British historians had no theoretical sophistication.''','0–10: state the essay’s question. 10–20: map the project’s reach. 20–30: discuss universal timelines. 30–40: compare with Thompson. 40–50: write a careful distinction.','Why does Chakrabarty connect Subaltern Studies with postcolonial history? What is problematic about a single universal timeline?','https://ebooks.inflibnet.ac.in/engp10/chapter/subaltern-theories-ranajit-guha-gayatri-chakravorty-spivak-dipesh-chakravarty/'),
n('thompson','E. P. Thompson · History from Below', '''## The approach
Thompson’s “History from Below” appeared in The Times Literary Supplement in 1966. The approach studies historical change through experiences and activities often neglected in accounts of rulers, famous leaders and formal institutions. It has a history before Thompson as well; do not credit one person with inventing every version of social history.

## Related work
In The Making of the English Working Class (1963), Thompson treats class as a historical relationship formed through experience and collective action rather than as a timeless label. Workers, artisans and political organisers are historical actors. Their ideas and aspirations deserve attention even when their movements did not succeed.

## Evidence and method
A historian can compare petitions, pamphlets, court records, union material and testimony, asking who produced each source and why. A labourer’s words recorded by a hostile official may be mediated; evidence should not be mistaken for direct access to a complete past.

## Comparison
History from below and Subaltern Studies share an interest in marginalised agency, but their contexts and theoretical questions differ. Chakrabarty places colonial difference and the politics of historical categories at the centre of his comparison.''','0–10: define history from below. 10–20: discuss class as a relationship. 20–30: compare two kinds of sources. 30–40: contrast Thompson and Chakrabarty. 40–50: formulate a research question.','What changes when history starts with workers rather than rulers? Why is a court record not a neutral transcript?','https://laviedesidees.fr/E-P-Thompson-A-Life-of-Struggle')]
data['course-36:2']=[
n('draupadi','Mahasweta Devi · Draupadi', '''## Content note
This story depicts state violence, torture and sexual assault. Offer a content warning and an alternative way to participate; do not ask students to describe or perform the assault.

## Story in sequence
Dopdi Mejhen, a Santhal woman, and her husband Dulna are associated with an insurgent struggle in a region shaped by land and water inequality. The authorities pursue them; Dulna is killed. An operation under the officer Senanayak hunts Dopdi. The narrative moves between official documents, the officer’s thinking and Dopdi’s memories, exposing the language through which power identifies its enemies.

Dopdi is captured and refuses to betray her comrades. On Senanayak’s orders, soldiers sexually assault her. The next morning she refuses the clothing offered to her, approaches Senanayak and confronts him with the evidence of the violence inflicted on her. The story ends with his fear in the face of an unarmed woman; it does not establish that state violence has ended or that she is safe afterward.

## Form and interpretation
Her name evokes the Mahabharata’s Draupadi, but Devi rewrites the familiar disrobing episode without presenting a simple repetition. Dopdi’s refusal to accept imposed shame is a defiant act, not evidence that violence leaves no lasting harm. Consider how gender, Adivasi identity, class and state power intersect. Gayatri Chakravorty Spivak translated the story into English; read translation and framing critically.''','0–10: give a content warning and context. 10–20: trace pursuit and capture without graphic detail. 20–30: compare official and Dopdi-centred perspectives. 30–40: discuss the epic allusion. 40–50: write about agency without claiming complete safety.','How does the story’s changing perspective expose power? Why should resistance not be confused with freedom from harm?','https://bookreviewsgalore.wordpress.com/2020/08/09/mahasweta-devis-draupadi-is-a-story-of-female-subversion-and-power/'),
n('militancy','Meena Kandasamy · Ms Militancy: poems and retelling', '''## Selection and title
The syllabus prints “Miss Militancy”; the collection is commonly titled Ms Militancy (2010). It does not list individual poems. This is an introduction plus a summary of one verifiable poem, not coverage of every poem; confirm the assigned edition and selection.

## Collection
Kandasamy uses anger, irony, sexual language, mythic retelling and striking shifts of voice to challenge caste hierarchy and patriarchy. The title links an ordinary form of address for a woman with active resistance. Anger is a political and aesthetic choice; it should not be dismissed as proof that the poems lack craft.

## “Princess-in-Exile”: summary
A rewritten Sita is separated from her husband and eventually confronted with his desire to reclaim her. Rather than treating her as a passive figure whose worth depends on his judgment, the poem imagines her acquiring the ability to leave and disappear. The retelling questions expectations of female obedience and chastity. Check the text for its exact compressed sequence and wording.

## Reading closely
Compare this Sita with the roles imposed on women in familiar versions of the epic. Who is allowed desire, speech and departure? The collection’s anti-caste politics and its attention to gender interact, but not every woman represented in the poems has an identical social position. Some poems contain explicit language and violence: prepare students accordingly.''','0–10: clarify edition and selection. 10–20: introduce mythic retelling. 20–30: summarise “Princess-in-Exile.” 30–40: analyse voice and departure. 40–50: compare another assigned poem directly.','What does changing Sita’s capacity to leave do to the familiar story? How does the title connect gender and resistance?','https://feminisminindia.com/2017/07/24/meena-kandasamy-ms-militancy/',True),
n('shoorpanakha','Poile Sengupta · Thus Spake Shoorpanakha, So Said Shakuni', '''## Setting and opening
A Woman and a Man wait for a delayed flight in an airport lounge. Their contemporary talk, irritation and humour gradually open into stories associated with Shoorpanakha of the Ramayana and Shakuni of the Mahabharata. The airport brings figures from different epics and times into one theatrical space.

## Counter-narratives
The Woman questions the ridicule and mutilation that follow Shoorpanakha’s expression of desire. The Man revisits Shakuni’s reputation and the injuries and politics behind revenge. Both question versions of events that have made them simply villains. Their accounts are perspectives to analyse, not automatically complete or final versions of either epic.

## Contemporary violence
The stories move into present-day loss: the Man speaks of violence against his family and reveals a bomb. The Woman challenges the cycle of hate and urges another possibility. The relation between mythic identity and contemporary persons is deliberately theatrical. Check the ending in the assigned script and staging rather than assuming that every production resolves the threat identically.

## Dramatic methods
Two performers, everyday objects, dialogue and sudden shifts of time let the audience reconsider storytelling itself. Compare the retelling with Kandasamy’s poetic strategies. Discussion of family violence should be non-graphic and sensitive.''','0–10: introduce setting. 10–20: map the two epic associations. 20–30: compare their complaints. 30–40: discuss revenge and the present-day threat. 40–50: analyse the staging.','What does the airport setting make possible? How do the characters challenge the label of villain?','https://www.the-criterion.com/V2/n1/Padmarani.pdf')]
data['course-36:3']=[
n('home-harlem','Claude McKay · Home to Harlem', '''## Part 1: return and search
Published in 1928 during the Harlem Renaissance, the novel follows Jake Brown, a Black American soldier who deserts after discriminatory military treatment, spends time abroad and returns to Harlem. He meets a woman, later identified as Felice, but loses track of her. He joins the world of clubs, work and friendships, including his old acquaintance Zeddy, and lives for a time with Rose. His relationship with Rose is strained and includes violence; analyse the treatment of women rather than romanticising it.

## Part 2: the railroad and Ray
Jake leaves Harlem for work on the Pennsylvania Railroad, where he meets Ray, an educated Haitian immigrant who wants to write. Their friendship brings the Haitian Revolution, US power in Haiti, race, education and migration into the novel. Their different interests and experiences complicate any single definition of Black identity. Ray later leaves for work at sea.

## Part 3: Felice and departure
Back in Harlem Jake finds Felice again. At a club Zeddy, who has also been involved with her, tries to take her away; a violent confrontation follows and Jake’s desertion is exposed. Zeddy later apologises. Fearing possible consequences, Jake and Felice decide to leave for Chicago together. Before departure Felice retrieves a necklace important to her.

## Critical lens
The novel celebrates vernacular speech, music and working-class life while showing racism, economic pressure and conflict within communities. Compare its views of Harlem and home without treating any one character as representative of all Black experience.''','0–10: locate Harlem Renaissance. 10–20: follow Jake’s return and Rose. 20–30: discuss Ray and Haiti. 30–40: trace Felice and Zeddy. 40–50: analyse the meaning of home.','Why does Jake leave Harlem again? How does Ray widen the novel’s geographical and political scope?','https://www.coursehero.com/lit/Home-to-Harlem/plot-summary/'),
n('and-then','Poomani · And Then (Piragu)', '''## What is verified
Poomani’s Tamil novel Piragu was translated as And Then by T. Marx. It focuses on life in a southern Tamil Nadu karisal region and the Chakkiliyar/Arunthathiyar community, including work associated with leather and caste exclusion. A review identifies Alagiri as a central narrative voice and describes village life, folk songs and changing social conditions.

## Reading approach
Look closely at labour, interdependence, speech, humour, family relationships and caste power. The novel’s people have complex lives and relationships; they should not be reduced to examples of suffering. Its regional language and rhythms matter. Translation must decide how to convey terms with no neat English equivalent; retaining a Tamil word can preserve a cultural distinction, but also requires readers to attend to context.

## Important limit
A reliable chapter-by-chapter account and the full ending have not yet been verified from the assigned translation. Do not substitute the plot of Poomani’s different novel Vekkai / Heat or the film Asuran. Use the book itself to make a sequence of events and identify speakers before teaching; this entry remains preliminary until that is done.

## Questions for a reading journal
What changes in the village over time? Which forms of labour are represented, and who benefits? How are folk songs and local speech translated? Cite specific pages from the edition used.''','0–10: identify original and translator. 10–20: map the community and region. 20–30: read an assigned passage. 30–40: compare local words and translation. 40–50: build an evidence-based event timeline.','Why is Piragu not the same novel as Vekkai? What can be gained or lost when regional speech is translated?','https://www.thehindu.com/books/books-authors/and-then-true-to-the-land-and-its-tongue/article30185616.ece',True),
n('stepchild','Joseph Macwan · The Stepchild: Angaliyat', '''## Setting and translation
Joseph Macwan’s Gujarati novel Angaliyat, translated into English by Rita Kothari as The Stepchild, follows members of a Vankar community in rural Gujarat across the period around Independence. The title evokes a stepchild’s insecure place within a family and invites reflection on exclusion from the nation’s promises. Verify names and chronology against the assigned translation.

## Story movement
Friends Teeha and Valji confront powerful caste men after harassment of Methi. Resistance exposes their families to retaliation and to pressure from within their own community. Methi’s relationship with Teeha is obstructed; her marriage to Chunthia is unhappy and violent. Valji is killed in an attempt connected with rescuing Methi. Kanku, Valji’s wife, mourns and continues to face difficult social choices.

As political power changes hands, independence does not remove caste domination. Teeha later faces a confrontation with powerful men and police; he is beaten and dies. Methi also dies later. The community’s grief, relationships and efforts to remember him continue beyond an individual act of resistance.

## Analysis
The novel contrasts national freedom with the persistence of local inequalities. Attend to Methi and Kanku’s choices rather than framing them merely as motivations for male bravery. The translation’s treatment of Vankar speech and idiom shapes how readers encounter the community. This is a narrative overview, not full chapter coverage.''','0–10: define the title and setting. 10–20: map Teeha, Valji, Methi and Kanku. 20–30: trace the conflicts. 30–40: compare national and social freedom. 40–50: discuss language and translation.','Why might the stepchild be a metaphor for exclusion? How does the novel complicate an easy celebration of independence?','https://www.the-criterion.com/V8/n2/IN37.pdf'),
n('jai-bhim','T. J. Gnanavel · Jai Bhim', '''## Content note and context
This 2021 Tamil legal drama contains sustained custodial torture and caste discrimination. Tell students before screening and permit alternatives to graphic scenes. The film is inspired by a 1993 case but is a dramatization: character names, events and courtroom scenes should not automatically be treated as historical records.

## Story in sequence
Sengeni and Rajakannu, an Irular couple, work for landowners and hope for a secure home. After Rajakannu catches a snake at a wealthy household, jewellery goes missing and police suspect him. Officers detain and torture members of his family; Rajakannu is also taken into custody. Sengeni is told that he and two other men escaped.

Teacher Mythra helps Sengeni approach lawyer Chandru, who files a habeas corpus petition seeking the missing men. The investigation tests police claims using witnesses, phone records and evidence concerning a body found on a road. Rajakannu died in custody, and the supposed escape and accident are exposed as a cover story. The surviving men testify. The court orders action against the officers and compensation; the film closes with Sengeni moving toward a new home.

## Discussion
Habeas corpus is a legal procedure used to challenge unlawful detention or require a person to be brought before a court; legal applications vary by jurisdiction and case. Notice Sengeni’s persistence and community solidarity as well as the lawyer’s work. Ask whether a film centred partly on a prominent advocate risks making collective struggles appear dependent on a single saviour.''','0–10: content warning and historical context. 10–20: map accusation and custody. 20–30: explain the petition and evidence. 30–40: analyse Sengeni’s role. 40–50: compare film and historical research.','What did the habeas corpus petition seek? Why must the film be distinguished from the real case?','https://indianculturalforum.in/2021/12/04/jai-bhim-a-flim-on-caste-and-police-brutality/')]
data['course-36:4']=[
n('mirror','Liana Badr · The Eye of the Mirror', '''## Context and translation
Liana Badr’s Arabic novel, translated into English by Samira Kawar, centres on a Palestinian refugee family and especially Aisha in the Tal al-Zaatar camp during the Lebanese civil war. The 1975–76 siege and massacre form the historical context. Sources use different spellings of the camp and Aisha’s name.

## Established narrative outline
Aisha works as a maid at a convent school and returns to her parents’ home in the camp as the war disrupts daily life. Bombardment, siege and the destruction of the camp affect family relationships and community survival. Her love, marriage and the question of having a family occur amid violence and displacement. The novel draws on multiple accounts and perspectives, foregrounding women’s experience rather than presenting war only through leaders and battles.

## Form and ethics
Consider the “mirror” as a prompt to discuss viewpoint and memory, but ground any interpretation in a passage. The novel is fiction informed by historical research; do not treat every episode as a direct documentary transcript. Palestinian refugees are not a homogeneous group, nor is civilian suffering a justification for attacks on any community.

## Coverage limit
This is a researched opening and context guide, not a verified complete plot or chapter-by-chapter account. Consult the assigned translation before naming the fate of every character or teaching the ending.''','0–10: locate the camp and translation. 10–20: outline Aisha’s situation. 20–30: discuss the siege sensitively. 30–40: examine a passage’s perspective. 40–50: record questions for the full novel.','How does attention to Aisha alter a leader-centred history of war? What is the difference between researched fiction and a documentary record?','http://www.banipal.co.uk/news/index.cfm?newsid=314',True),
n('cheran','R. Cheran · A Second Sunrise', '''## What is assigned?
A Second Sunrise can refer to the title poem and to a later English collection of Cheran’s poems, edited and translated by Lakshmi Holmström and Sascha Ebeling. The syllabus does not name individual poems. Confirm the assigned selection. This note summarises the title poem and introduces the collection; it does not cover every poem.

## Title poem: summary
The speaker walks in an eerily still landscape where even the sea seems motionless. An apparent second sunrise in the south turns out to be fire. The poem names a town burned, people made faceless and a land marked by an alien power. Questions addressed to a community shift the poem from shock and loss towards a call to rise and move forward. The image of sunrise is unsettling: light comes from destruction rather than ordinary renewal.

## Historical frame and form
The poem is associated with the 1981 burning of the Jaffna Public Library, not simply the separate anti-Tamil pogroms of July 1983. Silence, questions and the changing force of the fire image create the movement from witnessing to address. Historical context helps interpretation, but read the poem rather than assuming every image is a literal description of a single building.

## Beyond the title poem
Cheran’s collection includes love, sea, home, exile and war; the poetry should not be reduced to one event. Translation shapes rhythm and imagery. Avoid attributing violence to an entire ethnic group.''','0–10: establish poem versus collection. 10–20: trace stillness and fire. 20–30: discuss the 1981 context. 30–40: analyse the address to the community. 40–50: compare a second assigned poem.','Why is the second sunrise an unsettling image? Why must the 1981 library burning be distinguished from Black July 1983?','https://nationalcentreforwriting.org.uk/writing-hub/erasing-histories/',True),
n('burcaw','Shane Burcaw · Strangers Assume My Girlfriend Is My Nurse', '''## Genre and situation
This 2019 book is a collection of autobiographical essays, not a novel. Burcaw writes about life with spinal muscular atrophy, using a wheelchair, family, relationships and the assumptions strangers make about him and his girlfriend Hannah. The title identifies a recurring mistake: outsiders assume a disabled man and a nondisabled woman cannot be romantic partners.

## Themes
Humour and candid storytelling expose awkward public encounters, low expectations and barriers to access. Assistance with daily needs and independence are not opposites: a person can make decisions and maintain relationships while relying on other people or technology. Burcaw’s individual experiences do not represent all disabled people.

## Reading critically
Distinguish impairment, access barriers and social prejudice without denying bodily realities or medical needs. Ask how the narrator controls tone: humour can challenge pity, but readers should not demand that disabled people be cheerful, inspirational or willing to educate strangers. Recognise Hannah as a person and partner, not merely a symbol.

## Coverage limit
The syllabus names the book but no essay titles. This is a collection-level overview, not a summary of each essay. Identify the teacher’s assigned essays and read them directly before making episode-specific claims.''','0–10: establish genre and title. 10–20: examine the assumption in the title. 20–30: discuss support and autonomy. 30–40: analyse humour in an assigned essay. 40–50: revise an ableist assumption.','What assumption does the title challenge? Why can receiving assistance coexist with autonomy?','https://us.macmillan.com/books/9781250233165/strangersassumemygirlfriendismynurse/',True)]
with open(P,'w',encoding='utf-8') as f:
 json.dump(data,f,ensure_ascii=False,indent=2); f.write('\n')
print('Added',sum(len(v) for k,v in data.items() if k.startswith('course-36:')),'selections across five units')
