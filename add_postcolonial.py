"""Add introductory, source-linked Postcolonial Literature notes."""
import json
P='prepared-notes.json'
with open(P,encoding='utf8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,preliminary=False):
 x={'id':id,'title':title,'source':source,'text':f'# {title}\nPostcolonial Literature · Semester 7\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: consult the assigned text and edition, check quotations and historical claims, and consider alternative readings.'}
 if preliminary:x['status']='preliminary'
 return x
d['course-41:0']=[
n('postcolonial-terms','Postcolonial studies · concepts and key terms', '''## Scope
Postcolonial studies examines colonial power, resistance and its continuing effects on culture, institutions, land and knowledge. Independence does not end every colonial relationship; in settler colonial contexts Indigenous peoples continue to contest dispossession. African, Caribbean, South Asian, Aotearoa New Zealand, Australian and Canadian writing are varied traditions, not one voice.

## Power and representation
Colonialism is domination and settlement or administration of peoples and territories; diaspora describes communities dispersed across places and their continuing connections. Eurocentrism treats Europe as the default measure. Hegemony is leadership or dominance maintained partly through institutions and consent, not only force. A master narrative or metanarrative is a large explanatory story that may marginalise other histories.

## Identity and difference
Self and Other name a relation in which a group defines itself against those it represents as different. Races are socially constructed categories with real consequences through racism. A nation is a historically made political community, not a timeless or naturally uniform identity. Hybridity describes cultural mixtures and negotiations; it does not mean unequal power has vanished. Mimicry names partial imitation that may both serve and unsettle colonial authority.

## Subaltern and method
Subaltern refers to people excluded from dominant structures of political representation; it is not a synonym for every marginalised person. Ask who speaks, who is heard and who controls archives. Use the terms precisely in a specific text rather than attaching them as labels without evidence.''','0–10: locate regions and histories. 10–20: explain empire and its afterlives. 20–30: work in pairs on key terms. 30–40: apply othering to a fictional example. 40–50: reflect on limitations.','How does hegemony differ from force alone? Why is a diaspora not necessarily a uniform community?','https://scholarblogs.emory.edu/postcolonialstudies/2020/02/17/subaltern-studies/')]
d['course-41:1']=[
n('brathwaite-colombe','Kamau Brathwaite · Colombe', '''## Text and title
The syllabus prints “Columbe”; a poem commonly titled “Colombe” depicts Columbus’s approach to Caribbean land. Confirm the assigned anthology before assuming these are the same text.

## Summary
The poem repeatedly imagines Columbus looking from his ship toward shore. Birds, trees, rocks and waterfalls appear through a perspective that also speaks of “my” and “our” land. The speaker asks whether his vision included the coming violence of soldiers, weapons and forced subjection. The final approach to shore leaves the encounter suspended.

## Analysis
The broken word “dis-covery” challenges a story in which an inhabited place becomes historically meaningful only when a European sees it. Shifts between Columbus’s gaze and an inhabited landscape question who gets to name a “new world.” Images of beauty coexist with anticipatory violence; the poem does not require an invented account of a particular eyewitness.''','0–10: verify title. 10–20: map ship and shore. 20–30: identify changes in perspective. 30–40: examine the broken word. 40–50: discuss discovery and violence.','For whom is the land “new”? How does the speaker challenge Columbus’s perspective?','https://jacoblaneria.wordpress.com/2020/04/17/colombe-by-kamau-brathwaite/',True),
n('walcott-ruins-41','Derek Walcott · Ruins of a Great House', '''## Summary
The speaker encounters a ruined Caribbean colonial house and its grounds. Decay brings to mind plantation wealth and the historical violence that sustained it. The poem’s voice moves between anger at empire and complicated compassion prompted by shared mortality.

## Form and ideas
Allusions to English literature, including John Donne, are part of the speaker’s inheritance even as the poem questions the empire associated with it. The ruined house is a particular material site and a symbol of power’s vulnerability. Compassion does not make enslavers and enslaved people equally responsible for colonial violence.

## Teaching question
How can a writer both use and challenge the language and literature of an imperial tradition?''','0–10: imagine the ruins. 10–20: connect property and coerced labour. 20–30: discuss literary allusion. 30–40: trace anger and compassion. 40–50: defend an interpretation.','How does the house embody history? Does compassion require forgetting injustice?','https://poemanalysis.com/derek-walcott/ruins-of-a-great-house/'),
n('senghor-new-york','Léopold Sédar Senghor · New York', '''## Summary
The speaker addresses New York, first struck by its impressive skyscrapers and then disturbed by coldness and alienation. In Harlem, music, colour, movement and social life create a contrasting rhythm. The poem asks the city to admit Black life into its rigid structures and imagines a renewed unity.

## Form and critical reading
The French poem is subtitled for jazz orchestra and trumpet solo; repetition, address and musical imagery invite performance. Senghor’s Négritude celebrates Black cultural value against racism, but the suggestion that peoples possess fixed racial essences is open to criticism. The poem’s Harlem is an artistic vision, not a comprehensive account of every resident.

## Translation
Wording varies between English translations of “À New York”; use the prescribed version for quotations.''','0–10: trace the first response to the city. 10–20: compare steel and Harlem’s rhythms. 20–30: consider music. 30–40: discuss Négritude and essentialism. 40–50: interpret the appeal.','Why does the poem shift to Harlem? How can a celebration of identity risk stereotyping?','https://worldselsewhere.wordpress.com/2010/11/27/senghor-a-new-york-to-new-york/'),
n('okara-drum','Gabriel Okara · The Mystic Drum', '''## Summary
The speaker describes an inner drum whose rhythm makes fish, people and even the dead dance. A woman stands behind a tree and smiles rather than joining. The drum grows more powerful, but the woman gradually changes: roots and leaves appear, smoke issues from her nose and her smile becomes frightening. The speaker packs away the drum and resolves not to beat it so loudly again.

## Interpretation
The poem can be read as a love lyric, a drama of communication and estrangement, or an allegory of cultural encounter. None of these interpretations needs the woman to stand for all women or outsiders. The drum’s rhythm creates connection but cannot guarantee that another person shares the speaker’s experience.

## Form
Refrains, repetition and shifts in tempo imitate musical performance. Notice how the repeated image of the woman changes rather than assuming the ending was predictable from the start.''','0–10: track drum and dancers. 10–20: compare repetitions. 20–30: trace the woman’s transformation. 30–40: discuss different interpretations. 40–50: explain the final silence.','Why does the speaker put the drum away? Can the poem sustain both personal and cultural readings?','https://sde.uoc.ac.in/sites/default/files/sde_videos/eng2c08.pdf'),
n('lee-country','Lee Tzu Pheng · My Country and My People', '''## Summary
The Singaporean speaker describes feeling uncertain about country and belonging. Her childhood brings together Chinese cultural inheritance, neighbours of different backgrounds and diaries kept in English. The poem recalls rapid urban development, tourist-friendly national images and the loss of large trees. Its repeated admission of not understanding country and people refuses a simple patriotic formula.

## Interpretation
The speaker is not necessarily rejecting Singapore; she is questioning how to belong honestly in a changing, multilingual society. Contrast public images of a modern nation with intimate memory and environmental change. Descriptions of neighbours should be discussed critically rather than treated as definitive accounts of an ethnic community.

## Form
Repetition and shifts between personal memories and public landscape keep uncertainty alive. The image of people moving downstream suggests change that the speaker cannot simply control.''','0–10: map languages and memories. 10–20: examine the repeated statement. 20–30: discuss development and trees. 30–40: question public images of belonging. 40–50: write an interpretation.','Why is uncertainty different from indifference? How does urban development affect the poem’s sense of place?','https://sea-globe.com/singapore-poetry-lee-tzu-pheng-arthur-yap-southeast-asia-globe'),
n('naheed-grass','Kishwar Naheed · The Grass is Like Me', '''## Summary
The speaker compares herself and women to grass that grows beneath feet and is repeatedly cut when it rises. The lawnmower’s promise of smooth velvet becomes an image of social pressure to flatten women. Yet the desire to grow persists in both earth and women. The closing contrast between a footpath, straw and grass varies in English translation.

## Reading
Repeated comparison and direct address turn an ordinary lawn into an argument about gender, control and resilience. The speaker’s resistance is powerful, but the poem should not be used to blame women whose circumstances make resistance dangerous.

## Translation
Naheed wrote in Urdu. The syllabus does not specify translator; English versions differ, especially at the end. Verify the assigned translation before quotation or close line-by-line work.''','0–10: describe the grass image. 10–20: trace cutting and growth. 20–30: discuss the direct address. 30–40: compare available translations. 40–50: interpret resilience without victim-blaming.','Why does the lawnmower’s “velvet” image matter? What changes when different translations end differently?','https://farrukhi.substack.com/p/found-in-translation-kishwar-naheed-6d0',True)]
d['course-41:2']=[
n('midnight','Salman Rushdie · Midnight’s Children: narrative guide', '''## Birth and family history
Saleem Sinai tells his life story to Padma while working in a pickle factory. He begins before his birth, with the histories of his grandparents and parents. At the moment of Indian independence in 1947, he and another baby, Shiva, are born. Nurse Mary Pereira switches their name tags, so each grows up in the other family’s social circumstances. Saleem’s claim that his life is tied to the nation must be read as part of his imaginative, sometimes unreliable narration.

## Children of midnight
Saleem discovers he can hear other children born in the first hour of independence, each with an unusual ability. He creates a conference in his mind. Differences of class, language, religion and political outlook complicate the effort to act together; Shiva becomes his rival. Family discoveries and movement between India and Pakistan reshape Saleem’s life.

## War and Emergency
Bombing during the 1965 war kills several members of Saleem’s family and leaves him with memory loss. He later serves with the Pakistani army during the Bangladesh war and travels through the Sundarbans. Parvati helps him return to India. She becomes pregnant by Shiva and marries Saleem, who raises Aadam as his son. During the Emergency, the magicians’ settlement is destroyed, Parvati dies, and Saleem and other midnight’s children are detained and forcibly sterilised.

## Ending and form
After release Saleem finds Aadam and Mary in Bombay. He plans to marry Padma and predicts that his own body will disintegrate into countless fragments; this is a prophecy, not an event witnessed after it occurs. Pickling, digression, oral storytelling and magic complicate any single official account of national history.''','0–10: trace the baby switch. 10–20: explain the conference. 20–30: map war and displacement. 30–40: discuss the Emergency sensitively. 40–50: examine Saleem as narrator.','Why is the switch significant for class? How does Saleem’s prophecy differ from a narrated fact?','https://www.ebsco.com/research-starters/literature-and-writing/midnights-children-salman-rushdie/'),
n('ice-candy','Bapsi Sidhwa · Ice-Candy-Man: narrative guide', '''## Lahore before Partition
Lenny, a young Parsi girl with polio, grows up in a relatively privileged household in Lahore. Her Hindu ayah Shanta takes her into the city, where a lively circle of admirers includes the Masseur and the Ice-Candy-Man. Lenny’s observations mix childlike misunderstanding with insight; adult conversations introduce political conflict and impending Partition.

## Violence and betrayal
As British India is partitioned in 1947, communal violence and displacement transform everyday relationships. The Ice-Candy-Man is deeply affected by reports and sights of violence against Muslims, but his suffering does not excuse his participation in violence. The Masseur is killed. A crowd searches for Shanta; Lenny reveals where she is hiding, and men abduct her. Responsibility for the abduction lies with the abductors, not with the frightened child.

## Recovery and aftermath
Shanta is held and sexually exploited; Ice-Candy-Man is implicated in her confinement. Lenny’s Godmother intervenes and helps secure her release, and Shanta is sent toward her family in India. The ending cannot simply restore what has happened. Other stories, including Ranna’s account of village massacre, widen the novel beyond Lenny’s direct sight.

## Interpretation
Also published as Cracking India, the novel examines gendered violence and the unequal vulnerabilities of communities and classes. Do not confuse the novel’s plot with an adaptation. This is an overview, not a complete chapter-by-chapter guide.''','0–10: give content warning and map the household. 10–20: discuss the circle of friends. 20–30: trace Partition and abduction. 30–40: discuss intervention and aftermath. 40–50: analyse Lenny’s narration.','How does Lenny’s perspective both reveal and limit the account? Why must blame for the abduction remain with the perpetrators?','https://en.wikipedia.org/wiki/Cracking_India'),
n('yellow-sun','Chimamanda Ngozi Adichie · Half of a Yellow Sun: four-part guide', '''## Part I: early 1960s
Ugwu comes to Nsukka to work for university lecturer Odenigbo. Olanna, Odenigbo’s partner, joins the household. Her twin Kainene manages family business interests and becomes involved with the English writer Richard. Their lives show class differences and competing hopes for independent Nigeria.

## Part II: late 1960s
Coups and massacres of Igbo people precede Biafra’s declaration of independence and the Nigerian civil war. Olanna escapes violence in Kano with a child called Baby. Ugwu, Olanna and Odenigbo face repeated displacement, shortages and bombing. The novel moves forward before explaining all the family’s earlier relationships.

## Part III: return to the early 1960s
The story returns to Odenigbo’s encounter with Amala and Olanna’s relationship with Richard. Olanna and Odenigbo reconcile; they raise Amala’s daughter Chiamaka, called Baby. Kainene learns of Olanna and Richard’s encounter and the sisters’ relationship fractures. The backward shift asks readers to revise assumptions made in Part II.

## Part IV: late war and aftermath
Kainene runs a refugee camp; the sisters reconcile. Ugwu is forcibly conscripted, participates in the gang rape of a bar girl and is later wounded. Forced conscription does not excuse his participation in sexual violence. Kainene crosses lines to trade for supplies and disappears; her fate remains unknown. Biafra surrenders, and survivors return to damaged homes. Ugwu writes about the war, revealing an African witness to a history outsiders often claim authority to tell.

## Form
Alternating periods and perspectives connect intimate relationships with national history; the title recalls Biafra’s flag.''','0–10: give content warning and timeline. 10–20: map the principal characters. 20–30: explain the return to earlier years. 30–40: discuss war and Kainene’s disappearance. 40–50: ask who writes history.','Why reveal Baby’s parentage later? What ethical questions arise from Ugwu’s role as both participant and witness?','https://www.litcharts.com/lit/half-of-a-yellow-sun/summary')]
d['course-41:3']=[
n('anowa','Ama Ata Aidoo · Anowa: phases and chorus', '''## Warning and frame
The play includes enslavement and suicide. An Old Man and Old Woman comment on a story set on the Gold Coast in the nineteenth century; their disagreements make the community’s judgments visible.

## Phase I
Anowa refuses suitors approved by her mother Badua and chooses Kofi Ako. Her parents worry about the match. The couple leave their village, Yebi, despite Badua’s objections. Anowa’s independence creates conflict with expectations for daughters and wives, but tradition is not represented by only one voice.

## Phase II
Anowa and Kofi work hard as travelling traders. Their childlessness troubles them. Kofi wants to purchase enslaved people to increase their prosperity; Anowa objects. Their disagreement is moral and political as well as personal.

## Phase III and ending
Kofi becomes wealthy through an economy dependent on slavery. Their relationship deteriorates; Anowa cannot accept wealth built on human exploitation. In a final confrontation she publicly asserts that Kofi is impotent; he shoots himself and she drowns herself. The chorus figures debate responsibility. Neither infertility nor disability is a moral failing; the tragedy emerges through social pressures, slavery and conflict, not a medical diagnosis.

## Analysis
The play’s historical attention to African participation in slavery does not erase European imperial demand or wider systems of exploitation. Anowa’s resistance deserves attention alongside the limits of her situation.''','0–10: introduce the chorus and warning. 10–20: trace the marriage. 20–30: discuss slavery and work. 30–40: compare the chorus’s judgments. 40–50: assess responsibility.','Why do Anowa and Kofi disagree about wealth? What does the chorus contribute to the question of blame?','http://www.postcolonialweb.org/africa/ghana/aidoo/anowa5.html'),
n('unplugging','Yvette Nolan · The Unplugging: story guide', '''## Setting
After electricity stops working, communities struggle to survive. Bern and Elena, two older women, are exiled because their community considers them too old to bear children. They find shelter in the bush and draw on remembered knowledge of gathering, trapping, food and seasonal survival.

## A visitor
A young man, Seamus, comes from the community. Bern wants to teach and share; Elena distrusts him and fears for their safety. His arrival strains their friendship. He takes supplies and leaves, confirming some of Elena’s fears, but returns after learning from their knowledge and reflects on the possibility of changing the community that excluded them.

## Interpretation
The drama values older women’s knowledge without implying that every Indigenous community possesses identical traditions. The women must balance generosity with the right to protect themselves. The play is inspired by the Gwich’in story Two Old Women as told by Velma Wallis; discuss adaptation and cultural specificity rather than calling the play a universal Indigenous myth.

## Scope
This is a sequence overview; check the assigned script for exact scene divisions, staging and final wording.''','0–10: describe the loss of electricity. 10–20: explain exile and survival. 20–30: compare Bern’s and Elena’s responses. 30–40: discuss sharing and risk. 40–50: consider the source story.','Why does the community exile the women? What competing reasons shape their response to Seamus?','https://www.gwaandaktheatre.ca/performances/the-unplugging'),
n('stolen','Jane Harrison · Stolen: five interconnected lives', '''## Content warning and setting
The play concerns the forced removal of Aboriginal children from families in Australia, institutional abuse, sexual violence and suicide. Its fragmented scenes follow five characters across childhood and adulthood rather than presenting a single linear plot.

## Five stories
Shirley is separated from family and spends years seeking reunion; later she celebrates becoming a grandmother. Anne, raised by a non-Indigenous family, faces difficult questions when she reconnects with her Aboriginal family. Sandy’s repeated movement and search for home challenge the idea that identity can simply be erased.

Ruby is abused in domestic service and lives with severe psychological distress; her family eventually locates her. Jimmy is denied the truth about his mother’s efforts to contact him. She dies before they can reunite, and he dies by suicide. These outcomes differ: it is false to claim that all five achieve uncomplicated reunions.

## Form and context
Suitcases, beds, abrupt scene changes and collective voices connect individual experiences to the Stolen Generations while preserving differences among people. The policy of forced removal had long-lasting intergenerational effects. Do not ask Aboriginal students to disclose family experiences, and do not equate distress with a lack of resilience.''','0–10: context and content warning. 10–20: map the five characters. 20–30: discuss institutions and withheld letters. 30–40: compare different outcomes. 40–50: consider staging and memory.','Why does the play use fragmented scenes? How do the five outcomes resist a single story of removal?','https://www.worldlitonline.net/the-plight-of-stolen-generation-in-jane-harrisons-stolen.pdf')]
d['course-41:4']=[
n('said-orientalism','Edward Said · Introduction to Orientalism', '''## Three related senses
Said introduces Orientalism as an academic field studying the “Orient,” a style of thought that opposes “Orient” to “Occident,” and a historically organised discourse linked to institutional and imperial power. His focus is especially on British and French, and later US, representations of the Middle East and North Africa.

## Representation and power
Said asks how writing, scholarship and administration can produce recurring images of a supposedly timeless, exotic or irrational East. These representations help define a supposedly rational West and can support unequal power. He does not claim that actual Asian or Middle Eastern societies are imaginary, or that every individual scholar thinks identically.

## Method and debate
Discourse and power/knowledge are associated with Foucault; hegemony with Gramsci. Said also stresses historical context and the individual text. Critics have questioned his categories and attention to differences among writers and colonised communities. Read those debates alongside, not instead of, his argument.

## Apply
Analyse an advertisement or travel passage: who describes whom, what generalisations appear, and what institutions give the account authority? A single stereotype alone does not demonstrate the whole historical argument.''','0–10: distinguish place from representation. 10–20: explain three senses. 20–30: connect discourse and power. 30–40: examine an example. 40–50: discuss a limitation.','What is the difference between an actual place and an “imagined geography”? Why does authority matter to representation?','https://philopedia.org/works/orientalism/'),
n('fanon-intro','Frantz Fanon · Introduction to Black Skin, White Masks', '''## Question
Fanon introduces a study of how colonial racism shapes the social and psychological experience of Black people in a world structured by white supremacy. His approach joins lived experience, philosophical analysis, clinical thinking and attention to social and economic conditions.

## Method
He argues that the inferiority complex is not merely an individual misunderstanding: it develops in a racial hierarchy and material system. The title’s “mask” suggests pressure to conform to white norms, not a claim that all Black people respond to racism in the same way. His examples are historically situated, particularly in relation to the French Antilles and France.

## Reading responsibly
The syllabus assigns the introduction, not the entire book. Later chapters examine language, desire and recognition; do not attribute every later argument to the introduction. Fanon’s gendered formulations and psychoanalytic assumptions invite critical discussion. His work is social theory, not a diagnostic tool for students.''','0–10: establish historical context. 10–20: map social and psychological dimensions. 20–30: discuss the title metaphor. 30–40: distinguish introduction from later chapters. 40–50: consider strengths and limits.','Why is racism not merely an individual feeling in Fanon’s account? How can a historically situated argument remain useful?','https://philopedia.org/works/black-skin-white-masks/'),
n('spivak-subaltern','Gayatri Chakravorty Spivak · Can the Subaltern Speak?', '''## Representation
Spivak questions whether people excluded from dominant structures can become recognisable as political subjects when elites claim to speak for them. She distinguishes representation as political speaking-for from representation as depiction. Her question is about the institutions and power that make speech audible and authoritative, not an assertion that oppressed people never make sounds or act.

## Colonialism, gender and archives
Her essay examines colonial and nationalist accounts of sati and the case of Bhuvaneswari Bhaduri, whose suicide was misread in ways that obscured its political context. She asks how subaltern women can be doubly displaced by imperial and patriarchal representations. Her analysis should not be mistaken for an endorsement of widow burning.

## Method and limits
Spivak also critiques intellectuals who assume they can transparently recover another’s voice. A responsible reader checks archives, translation and mediation, and asks who can respond. The syllabus names the essay without specifying version: the 1988 essay and later revisions differ, so verify the assigned text.''','0–10: distinguish speaking-for and depiction. 10–20: explain structural exclusion. 20–30: discuss gender and colonial archives. 30–40: consider Bhaduri’s misreading sensitively. 40–50: debate the critic’s responsibility.','Does Spivak mean that subaltern people are literally silent? Why do institutions matter to whether speech is heard?','https://www.researchgate.net/publication/236707448_CAN_THE_SUBALTERN_SPEAK_New_York_February_2004',True)]
with open(P,'w',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Added',sum(len(d[f'course-41:{i}']) for i in range(5)),'selections')
