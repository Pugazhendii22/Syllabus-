import json
p='prepared-notes.json';d=json.load(open(p))
def note(id,title,body,source,status=None):
 n={'id':id,'title':title,'source':source,'text':f'# {title}\nLiterature and Visual Media · Semester 3\n\n{body}\n\n## Before class\nRead the prescribed essay or view the assigned film in the department’s edition. These notes are teaching aids, not replacements for the work; interpretations should be tested against specific passages or shots.'}
 if status:n['status']=status
 return n
S='https://www.pondiuni.edu.in/wp-content/uploads/2024/03/SyllabusNEP-B.A.HonorsEnglish2023-24.pdf'
d['course-17:0']=[
note('visual-intro','Visual culture, everyday life and postmodernism','''## What is visual culture?
Visual culture studies how images, acts of looking and ways of making things visible produce and contest meaning in particular social settings. Its objects include films, photographs, advertisements, screens, religious images, posters and everyday spaces. Ask not only “What does this image show?” but “Who produced it, who can see it, in what context, and with what consequences?”

Art history often studies works, forms, makers, patronage and institutions historically. Cultural studies examines the relation of cultural practices to power, identity and institutions. Visual culture overlaps both, but extends inquiry to ordinary images and the social conditions of seeing. None of these fields has an exclusive or rigid boundary.

## Visual literacy: a worked example
Imagine a public-health poster showing a doctor in a white coat. First describe composition, words and colours; then consider what the coat may imply about authority. Ask whose language is used, whether the information is accessible and what response the poster seeks. A reader may interpret it differently depending on experience and context. A proposed meaning is not proven merely by naming it: connect claims to visible features and evidence about circulation.

## Pastiche, simulation and postmodernism
Pastiche brings together or imitates recognisable styles; unlike parody it need not mock its sources. Postmodernism is a contested description of cultural and intellectual developments, not a claim that all reality disappears. Baudrillard’s simulation concerns models and signs that can precede and organise what is treated as real. His “hyperreal” names an effect in which distinctions between model and reality become difficult to sustain. Do not reduce this argument to “every picture is fake.”

## 50-minute lesson
0–10: list images encountered on the way to class. 10–20: distinguish description from interpretation using a poster. 20–30: compare art history, cultural studies and visual culture. 30–42: discuss a fictional example of pastiche or simulation. 42–50: write one claim supported by a visual detail.

## Questions
How does the location of an image change its meaning? How could an image be visually persuasive without proving its claim?''','https://www.pomoculture.org/2013/09/10/building-pictures-hiroshi-sugimoto-on-visual-culture/'),
note('visual-williams','Raymond Williams · Culture, Art and Democracy','''## A guide to Keywords
In Keywords, Raymond Williams investigates the historical and contested uses of important social words. A keyword is not simply a term with one correct, timeless meaning: changes in its uses can reveal social and political struggles. The following is an introduction; consult the exact entries and edition for their detailed histories.

## Culture
The word has histories associated with cultivation and development. Williams distinguishes, among other uses, intellectual or artistic development, a particular way of life, and works or practices of intellectual and artistic activity. These senses coexist and can conflict. Calling something culture may praise “high art,” describe a shared practice, or refer to a process of learning; context matters.

## Art
Art has been associated with skill and making as well as more specialised senses of creative and aesthetic practice. Its separation into a distinct category from craft and other skilled activity has a history. Ask who has the authority to designate a film, song or image as art and what kinds of labour may be overlooked.

## Democracy
Democracy concerns rule or power of the people, but “the people,” representation, participation and equality have been understood differently. Formal voting is one important dimension; democratic control and social equality are also contested questions. Williams’s historical approach prevents a single present-day definition from erasing conflict over the term.

## A classroom application
Compare the sentence “Cinema is art” with “Cinema is part of popular culture.” Do the two statements contradict each other? Identify the sense of each word and discuss how both can be true.

## 50-minute lesson
0–10: collect students’ definitions. 10–22: read the culture entry and trace two meanings. 22–35: compare art and skill. 35–45: discuss democracy and cultural access. 45–50: write a sentence explaining how context changes a keyword.''','https://philopedia.org/thinkers/raymond-henry-williams/'),
note('visual-barthes','Roland Barthes · The Photographic Message','''## Central question
How can a photograph appear to show reality directly while also carrying meanings shaped by culture? Barthes examines the press photograph as part of a communicative setting that includes producers, publication, surrounding text and readers.

## Denotation and connotation
At a basic level a photograph seems to show what was in front of the camera: its denoted message. Barthes calls attention to the photograph’s apparent status as a message without a code, but he also analyses connotation: meanings produced through cultural assumptions and editorial choices. This coexistence is the “photographic paradox.” Do not conclude that a photograph has no relationship to what was photographed; ask how that relationship is framed and interpreted.

## How connotation is constructed
Barthes discusses procedures including trick effects, pose, objects, photogenia (such as lighting and technical treatment), aestheticism and syntax, or meaning produced by a sequence of images. A caption can direct interpretation, adding information or emphasis that is not self-evident in the photograph. A familiar gesture or object may signal different things to different audiences.

## Worked example
A picture shows a person holding a folder outside a building: that is a basic description. A low camera angle, official emblem and caption calling the person a “leader” can suggest authority. Another caption could emphasise a protest or controversy. Neither interpretation should be treated as self-evident without examining the broader context.

## 50-minute lesson
0–10: describe an image without evaluating it. 10–22: distinguish denotation and connotation. 22–35: compare two captions for the same image. 35–45: identify one photographic procedure and its potential effect. 45–50: write an evidence-based interpretation.

## Questions
Why does a press photograph seem objective? What work does a caption do? How might different cultural readers interpret the same pose?''','https://photo-graph.org/2014/10/08/barthes-the-photographic-message/'),
note('visual-mirzoeff','Nicholas Mirzoeff · What is Visual Culture?','''## Central idea
Mirzoeff introduces visual culture as a way of examining visual events: situations in which a person encounters visual information, meaning or pleasure through a technology or practice of seeing. His introduction draws attention to everyday visual experience, not only the gallery or cinema.

## Concepts
Visualisation makes an issue, process or place available to sight through an image, map, screen, chart or representation. It is a social and technological practice, not a transparent window onto every aspect of the world. Spectatorship asks how people look and how situations invite, guide or restrict looking. Visual literacy involves learning to question images and their contexts.

Mirzoeff’s attention to screens and visual technologies is influential. A critic might ask whether this emphasis overlooks other everyday visual experiences, including buildings, public space or bodies. The question is an invitation to debate the field’s scope, not proof that Mirzoeff denies the existence of those objects.

## Apply the idea
For a map on a phone, ask what is shown, what is left out, who designed its categories, what data supports it, and whose movement it makes easier. Compare this with looking at a family photograph: both are visual events, but they involve different purposes and relationships.

## 50-minute lesson
0–10: students name three visual events. 10–22: define visualisation and spectatorship. 22–35: analyse a map or poster. 35–45: discuss whether visual culture extends beyond screens. 45–50: exit response describing one image and its social context.

## Questions
Why study looking as well as images? What does a visualisation make easier to know, and what might it hide?''','https://www.pomoculture.org/2013/09/10/building-pictures-hiroshi-sugimoto-on-visual-culture/')]
d['course-17:1']=[
note('visual-race','Gender, race, religion and caste in visual media','''## Representation and power
Gender is not simply a fixed set of roles that images mirror: ideas about femininity, masculinity and other gender identities are learned, negotiated and contested in social life. Media can repeat conventions, challenge them or do both. Ask who speaks, acts, watches, is watched and has authority. Avoid assuming that all viewers respond identically.

Race and ethnicity are historically constructed categories whose effects are real; visual stereotypes can naturalise inequality. Religion may appear through clothing, spaces, rituals or narrative roles, but no single image represents an entire faith. Caste is a specific historically embedded hierarchy in South Asia: do not treat it as interchangeable with race or class. Analyse representation together with material conditions, production, distribution and audience.

Globalisation moves images, media industries, genres and audiences across borders. It can expand access and collaboration, while unequal ownership and distribution can concentrate power. Local audiences also interpret and adapt imported forms; global influence is not simply passive imitation.

## Classroom practice
Select a short clip. Record camera position, dialogue, who has decision-making power and what the narrative expects viewers to know. Then ask whose point of view is absent and whether an apparently familiar image relies on stereotypes. Respect participants’ lived experiences; nobody must speak for an entire community.

## 50-minute lesson
0–10: define representation and stereotype. 10–22: examine gender roles in a short example. 22–35: discuss race, religion and caste without equating them. 35–45: analyse circulation and globalisation. 45–50: cite a precise feature and offer an interpretation.''',S),
note('visual-fanon-dyer','Fanon and Dyer · race, looking and the norm','''## Fanon: The Fact of Blackness
In a chapter of Black Skin, White Masks, translated under different titles including “The Fact of Blackness” and “The Lived Experience of the Black Man,” Frantz Fanon describes how a racist gaze imposes meanings on a Black person’s body. A child’s fearful recognition is not an innocent neutral observation: it draws upon a history of colonial stereotypes. Fanon’s discussion of a racialised bodily schema shows how racism can disrupt ordinary bodily experience and force a person to encounter themselves through another’s judgement.

Fanon’s chapter moves through anger, analysis, attempts at self-assertion and debates about history and Black identity. It is not simply a statement that looking itself is always oppressive, or that Black identity is reducible to what white observers think. Attend to the translation, the chapter’s changing voice and historical context.

## Dyer: White
Richard Dyer asks why whiteness in much Western visual culture can be treated as ordinary or universal while other groups are explicitly marked as racial. Making whiteness visible as a constructed racial position allows representation and power to be examined rather than taking a presumed norm for granted. Lighting, casting and narrative point of view are among possible objects of analysis. The course title may refer to an essay or extract: confirm the assigned selection.

## Compare
Fanon foregrounds the embodied effect of being made an object of a racialising look; Dyer examines how a dominant position can escape notice as a norm. They are related but not interchangeable. For a film still, ask whose perspective is centred and what evidence supports the claim.

## 50-minute lesson
0–10: explain “unmarked norm.” 10–22: discuss Fanon’s account of the gaze. 22–35: examine Dyer’s question about whiteness. 35–45: compare their methods using an image. 45–50: write one similarity and one difference.''','https://www.litcharts.com/lit/black-skin-white-masks/chapter-5-the-lived-experience-of-the-black-man'),
note('visual-bicycle','Vittorio De Sica · Bicycle Thieves','''## Film overview
Bicycle Thieves (1948) is set in postwar Rome. Antonio Ricci, who has been unemployed, obtains work putting up posters, but the job requires a bicycle. His wife Maria pawns the family’s sheets so he can recover his bicycle from the pawnshop.

## Story from beginning to end
On Antonio’s first day at work the bicycle is stolen. The police take a report but offer little immediate hope of recovery. Antonio and his young son Bruno search the city with help from acquaintances, visiting markets where bicycle parts are traded. They follow leads, but an old man associated with the suspect escapes their questioning.

The search strains the father–son relationship. Antonio strikes Bruno in frustration; later he fears his son may have drowned, only to find him safe. They eat together, and a glimpse of another family’s comfort sharpens the contrast between their circumstances and their hopes.

Antonio eventually confronts the suspected thief in his neighbourhood. The young man’s neighbours defend him, and the officer called to the scene cannot establish the accusation from the available evidence. Antonio leaves without the bicycle. Near a football stadium he sees many bicycles and attempts to steal an unattended one. The owner and others catch him. Bruno sees the humiliation; the owner decides not to press charges. Father and son walk away hand in hand in the crowd. Antonio’s bicycle is not recovered, and the film does not show a secure solution to his livelihood.

## Form and interpretation
Italian neorealism is associated with attention to ordinary people, locations and social conditions, though individual films differ. The bicycle is both a practical means of work and a focus for dignity and dependence. The ending complicates a simple distinction between victim and thief without making poverty an excuse that settles every ethical question.

## 50-minute lesson
0–10: establish the employment problem. 10–25: map the search and the father–son relationship. 25–35: compare the first theft with Antonio’s attempted theft. 35–45: analyse the final crowd and handholding. 45–50: exit response with one precise scene.

## Questions
Why does one object matter so much? How does Bruno’s viewpoint affect the ending? What remains unresolved?''','https://www.deepfocusreview.com/definitives/bicycle-thieves/'),
note('visual-motorcycle','Walter Salles · The Motorcycle Diaries','''## Film overview
The Motorcycle Diaries (2004) dramatises a 1952 South American journey by young medical student Ernesto Guevara and his friend Alberto Granado. Based on travel accounts, the film is a retrospective narrative rather than a transparent record of every historical event.

## Journey and ending
Ernesto and Alberto leave Argentina on an ageing motorcycle, La Poderosa. Early mishaps and breakdowns give the journey an adventurous, comic quality. After the motorcycle can no longer carry them, they continue by other means. Encounters with workers, displaced people and Indigenous communities bring poverty and inequality more sharply into view. The film contrasts the travellers’ relative privilege with the experiences they witness.

In Peru they visit Machu Picchu and reflect on Indigenous histories and colonial power. At San Pablo they work with people affected by Hansen’s disease, then commonly called leprosy. The film represents separation between patients and staff and shows Ernesto resisting stigma. On his birthday he speaks of a more united Latin America and swims across the river to the patients’ side, despite his asthma. The crossing is a dramatic image of solidarity; it should not be mistaken for a medical recommendation. Hansen’s disease is treatable, and film depictions should not be used as medical advice.

The travellers leave and later part in Venezuela. The ending places the youthful journey beside the men’s later histories. The film suggests political awakening, but the journey alone does not explain every aspect of Guevara’s subsequent politics or establish a simple historical cause.

## Film form and questions
How does the road-movie structure change from adventure to social observation? Whose experiences are seen through the travellers’ eyes? How does the river acquire symbolic meaning? Compare a film scene with a historical source without assuming either is neutral.

## 50-minute lesson
0–10: introduce a road film and biographical adaptation. 10–25: trace three encounters. 25–35: examine framing of illness and stigma. 35–45: analyse the river crossing. 45–50: distinguish a filmic choice from a historical claim.''','https://www.spiritualityandpractice.com/films/reviews/view/9212/the-motorcycle-diaries')]
d['course-17:2']=[
note('visual-film-theory','Film theory · seven approaches and key terms','''## Before interpreting: film language
A shot is an uninterrupted recorded or edited view; a scene generally gathers action in a place and time. Framing selects what appears within the image. Mise-en-scène includes the arrangement of setting, costume, lighting, bodies and movement. Editing connects shots; sound may come from the represented world (diegetic) or be added for the audience (nondiegetic). These terms are tools for noticing evidence, not automatic interpretations.

## Seven approaches
Auteur approaches study patterns associated with a director, while recognising that cinema is collaborative and shaped by producers, performers, technicians and institutions. Gender film theory asks how films construct gender, looking and spectatorship; different feminist and queer critics do not all make the same argument.

Formalism examines how composition, editing, sound and performance make effects; it does not require ignoring history. Marxist approaches connect cultural form to class, labour, ownership and ideology, but differ in their accounts of economic power. Psychoanalytic approaches use theories of desire, identification and the unconscious to interpret spectatorship or narrative; they are theoretical frameworks, not clinical diagnoses of audiences.

Structuralism asks how meaning emerges from relations, contrasts and conventions rather than isolated elements. Genre studies examines recurring conventions and variation in industrial, historical and audience contexts. A film may cross genres.

## Worked comparison
A sequence of a worker in a factory might be analysed for rapid cuts (formalist), labour relations (Marxist), gendered division of work (gender theory), or its relation to the director’s other films (auteur). Strong analysis explains how the chosen evidence supports a claim rather than attaching labels.

## 50-minute lesson
0–10: identify shot, framing and sound. 10–25: introduce four approaches with examples. 25–35: compare the remaining approaches. 35–45: groups analyse one scene using two lenses. 45–50: exit ticket explaining how interpretations differ.''',S),
note('visual-bazin-harman','Bazin and Harman · realism, editing and signs','''## André Bazin: The Evolution of the Language of Cinema
Bazin discusses different directions in film history, contrasting filmmakers who emphasise the constructed image and montage with those who place greater faith in the revelation of reality. Montage can produce meanings through the relation between shots; it is not merely the fact that a film has cuts. Bazin considers deep focus and staging in depth important because multiple elements can remain visible within a shot, offering the spectator choices about where to look and preserving a degree of ambiguity.

Do not state that Bazin thought any edited film was false or that a long take is automatically neutral. Framing and staging also guide attention. Ask what evidence a particular scene supplies and whether a viewer truly has unrestricted choice.

## Gilbert Harman: Semiotics and the Cinema: Metz and Wollen
Semiotics studies signs and meaning. Christian Metz explores cinema as a signifying practice; Peter Wollen develops another account drawing on approaches to signs. Harman examines and questions assumptions in these theories, including how “code” is used. Do not treat his essay as a simple endorsement of a single film grammar or claim that every shot functions like a word in spoken language.

## Worked comparison
A cut from a face to a closed door may prompt an inference about what a character sees or fears. A longer shot showing the character and door together still selects a position and duration. Compare the kinds of information available in each version, then ask how a viewer learns the conventions needed to understand them.

## 50-minute lesson
0–10: review shot and edit. 10–22: explain Bazin on depth and ambiguity. 22–35: discuss sign and code with a film example. 35–45: debate advantages and limits of each framework. 45–50: exit ticket contrasting montage and deep-focus staging.''','https://www.craftfilmschool.com/userfiles/files/Leo%20Braudy,%20Marshall%20Cohen-Film%20Theory%20and%20Criticism-Oxford%20University%20Press,%20USA%20(2009).pdf'),
note('visual-city','Charlie Chaplin · City Lights','''## Introduction
City Lights (1931), a largely silent romantic comedy with synchronised music and effects, follows Chaplin’s Tramp in a city divided by wealth. The film includes a suicide attempt; introduce the subject sensitively.

## Story overview
The Tramp meets a blind flower seller and buys a flower. A sequence involving a car door leads her to mistake him for a wealthy man. He becomes fond of her. That night he encounters a drunken millionaire attempting suicide and helps him; the millionaire treats him warmly while intoxicated but fails to recognise him when sober. Their recurring encounters produce comedy as the Tramp moves between luxury and exclusion.

The flower seller and her grandmother face money problems. The Tramp takes work and tries to obtain enough money for rent and a proposed operation. His comic attempt to win a boxing prize fails. The intoxicated millionaire later gives him money, but burglars rob the millionaire and knock him unconscious. The police find the Tramp with the money, and the millionaire cannot remember giving it to him. The Tramp gets the money to the flower seller and is arrested.

After a period in prison, he returns to the street and finds that the woman’s sight has been restored and she now works in a flower shop. She does not initially recognise him and offers the poorly dressed man a flower and a coin. Touching his hand, she recognises her benefactor. Their final exchange and expressions invite tenderness and uncertainty; the film does not show their later life together.

## Form and questions
Pantomime, timing, composition and recurring misunderstandings carry much of the story. Compare the millionaire’s drunken and sober treatment of the Tramp. How do class and appearance affect recognition? Discuss disability respectfully: the film’s use of blindness is a narrative convention, not a general truth about blind people.

## 50-minute lesson
0–10: silent-film and sound context. 10–25: map recognition and mistaken identity. 25–35: examine a gesture in the final scene. 35–45: discuss class and the film’s representation of disability. 45–50: exit ticket on how performance conveys meaning.''','https://cinemontage.org/charles-chaplins-city-lights-1931/'),
note('visual-potemkin','Sergei Eisenstein · Battleship Potemkin','''## Context
Eisenstein’s 1925 silent Soviet film reworks the 1905 mutiny on the battleship Potemkin. It is a political film as well as a landmark in editing. Its images of violence require a content warning. The film is a constructed interpretation, not a documentary record of every incident shown.

## Five-part story
1. Sailors are ordered to eat meat they believe is rotten. Their complaints reveal the officers’ contempt and the unequal conditions aboard ship.
2. The confrontation escalates into a mutiny when sailors refuse to submit to punishment. The ship is taken from the officers; the sailor Vakulinchuk is mortally wounded.
3. At Odesa, his body becomes a focus of public mourning. People gather, and solidarity between townspeople and sailors grows.
4. In the famous Odessa Steps sequence, troops move against civilians. Rapidly connected images of running crowds, soldiers and injured people create fear and collective outrage. A baby carriage descending the steps becomes a memorable image within the sequence. The sequence should not be presented as a literal filmed record of a specific massacre on those exact steps.
5. A squadron approaches the Potemkin. Rather than destroy the rebellious ship, the sailors allow it to pass. The film concludes with an image of solidarity.

## Montage and ideology
Montage creates relationships across shots. In the steps sequence, editing combines movement, repeated angles and fragmented bodies to intensify the event and organise an emotional and political response. Compare this with Bazin’s interest in ambiguity and staging in depth, without assuming either filmmaker uses only one technique.

## 50-minute lesson
0–10: distinguish 1905 event and 1925 representation. 10–22: outline five parts. 22–35: examine a short, appropriately chosen montage sequence. 35–45: discuss how editing produces an interpretation. 45–50: exit ticket connecting two shots to an effect.

## Questions
Why does the film use collective crowds? How does editing reshape time? What are the ethical responsibilities of interpreting a violent historical representation?''','https://www.britannica.com/topic/Battleship-Potemkin')]
d['course-17:3']=[
note('visual-genre','Genre, narrative and criticism across media','''## Film and narrative
A story is a sequence of events as understood by a reader or viewer; narration is how a work presents information, including order, viewpoint and omission. Film and fiction can both use a restricted perspective or a flashback, but film also works through moving images, sound, performance and editing. Avoid assuming that a film’s camera is always equivalent to a novel’s narrator.

Theatre and film share performance, space and time, but editing and camera position can create relations not available in the same way in a live performance. Theatre also has distinctive possibilities of shared space and live presence. Films interact with music, painting, photography and other arts.

## Genre and alternative forms
Genres are historically changing groupings of conventions, institutions and expectations; a film can mix them. Film noir is often associated with crime, shadowed imagery and moral uncertainty, but scholars debate whether it is a genre, style or cycle. Documentary makes claims about the world through selected images and sounds; it is constructed even when addressing real events. Queer and subaltern cinema are not single styles: consider whose experiences, authorship and structures of power are involved.

## Prescribed critical readings
Stephen Neale’s “Film Noir” should be read for its specific argument about classification and history rather than reduced to a checklist. S. Theodore Baskaran’s “Patriotic Cinema: An Aspect of the Freedom Struggle” asks for attention to the historical relation of cinema and anticolonial politics; verify the assigned essay’s examples in the original. In “Reading Against the Reel,” Sundar Sarukkai argues that criticism connects a film, a reviewer’s standpoint and audiences, helping a film have an afterlife in writing. Criticism need not be merely a recommendation to watch or avoid.

## 50-minute lesson
0–10: define story and narration. 10–20: compare a written and filmed scene. 20–30: debate noir as a category. 30–40: consider documentary and political context. 40–50: write a short review based on one observed detail.

## Questions
How does a review illuminate rather than simply rate? Why does a historical context matter to an account of patriotic cinema?''','https://www.thehindu.com/entertainment/movies/reading-against-the-reel/article19608515.ece'),
note('visual-rashomon','Akira Kurosawa · Rashomon','''## Context and content note
Rashomon (1950) uses competing accounts of a violent encounter involving a samurai, his wife and a bandit. It includes sexual violence. Discuss the woman’s representation with care and do not treat the bandit’s version of consent as automatically reliable.

## Story and conflicting accounts
A woodcutter and a priest shelter from heavy rain at the ruined Rashomon gate. A commoner joins them. They discuss a case: a samurai has been found dead in a grove and the bandit Tajomaru has been captured. Testimonies are presented through the frame of their conversation.

Tajomaru says he lured and tied up the samurai, encountered the wife and killed her husband in a duel. His self-dramatising account presents him as bold. The wife describes the bandit’s assault and her husband’s contempt; in distress she faints and finds him dead. Through a medium, the dead samurai gives a different version, claiming that he killed himself after the encounter. Their accounts conflict about motives, actions and the death.

The woodcutter, who had originally said he found the body, offers another account after indicating that he witnessed the event. His version portrays a less heroic, awkward fight. The commoner questions his reliability and suggests that he may have taken the missing valuable dagger. The film does not supply a final, independently verified solution that makes one whole account certainly true.

A baby is found abandoned at the gate. The commoner takes its belongings and departs. The woodcutter offers to care for the child, and the priest’s damaged faith in people is tentatively renewed. The ending places an act of care beside unresolved deception.

## Form and questions
The film’s flashbacks do not simply replay an objectively known event: each account frames the past. Ask how gesture, camera, performance and editing shape the competing narratives. Does the ending answer the murder mystery, or offer a different kind of ethical response?

## 50-minute lesson
0–10: content note and framing situation. 10–25: chart four accounts without choosing a winner. 25–35: analyse credibility and motive. 35–45: discuss the child and the ending. 45–50: write one supported interpretation of uncertainty.''','https://www.gradesaver.com/rashomon-film/study-guide/summary-the-woodcutters-tale-and-ending'),
note('visual-pickpocket','Robert Bresson · Pickpocket','''## Story
In Pickpocket (1959), Michel, an isolated young man in Paris, steals from a woman at a racetrack. He is arrested but released for lack of evidence. His mother is ill, and Jeanne, a neighbour who helps care for her, urges him to visit. His friend Jacques also tries to help him. Michel nevertheless grows increasingly absorbed in theft.

He practises and learns techniques from an experienced pickpocket. Sequences in stations and other crowded places concentrate on hands, wallets and coordinated movement. Michel discusses an idea that exceptional people might be entitled to break ordinary laws, but the film does not simply endorse his self-justification. His mother dies, and Michel continues to evade both the police inspector’s attention and close human relationships.

When he realises the police are watching, Michel leaves France. After a period away he returns and learns that Jeanne has a child and is struggling. He tries legitimate work but returns to theft. At the racetrack he steals from a man who is part of a police operation and is arrested. Jeanne visits him in prison. Their encounter across the bars suggests a movement towards connection or grace, but viewers may debate how complete that change is.

## Film form
Bresson’s restrained performances, ellipses, attention to hands and economical use of sound make viewers assemble motivations and actions. The film is related by critics to questions of crime and redemption, including comparisons with Dostoevsky; it is not a direct scene-by-scene adaptation of Crime and Punishment.

## Lesson: 50 minutes
0–10: contrast a crime plot with a character study. 10–25: trace Michel’s choices. 25–35: analyse a sequence of hands and objects. 35–45: discuss the prison ending. 45–50: write a claim supported by a filmic detail.

## Questions
What does Michel’s theory of exceptional people do for him? How does the focus on hands shape our understanding? What different meanings might Jeanne’s visit have?''','https://www.tcm.com/tcmdb/title/962404/pickpocket'),
note('visual-breathless','Jean-Luc Godard · Breathless','''## Story
In Breathless (1960), small-time criminal Michel Poiccard steals a car and kills a police officer during a pursuit. He reaches Paris and reconnects with Patricia, an American student and aspiring journalist selling newspapers. He tries to obtain money and persuade her to leave with him for Italy, while the police search for him.

Their time together includes extended conversations about love, freedom, identity and their uncertain relationship. Patricia is attracted to Michel but also questions what she feels and what his criminal situation means. The police contact her. Eventually she informs them of Michel’s whereabouts and tells him what she has done. Michel does not initially flee. When the police arrive he is shot and collapses in the street. His final words are difficult for Patricia to understand and vary in translation; she repeats a gesture associated with him and addresses a question about the word used. The film does not make her motives or the meaning of the final exchange completely transparent.

## Technique and context
The film is associated with the French New Wave. Jump cuts can interrupt apparent continuity within a scene, making editing noticeable. Location shooting, references to cinema and a loose crime narrative combine familiarity with disruption. Michel’s imitation of American gangster style is an example of intertextuality: another film tradition becomes part of his self-presentation.

## Teaching questions
How does the film use and unsettle crime-film expectations? What do the jump cuts do to time and movement? How do Michel and Patricia imagine freedom differently? How might different subtitles affect interpretation of the final scene?

## 50-minute lesson
0–10: introduce the French New Wave. 10–22: outline the pursuit and relationship. 22–35: examine editing and cinema references. 35–45: discuss Patricia’s decision without assuming a single motive. 45–50: exit ticket on form and effect.''','https://en.wikipedia.org/wiki/Breathless_(1960_film)')]
d['course-17:4']=[
note('visual-film-text','Reading film as text · form, discourse and ideology','''## What does “film as text” mean?
A film can be treated as an organised object of interpretation, not because it is literally a written page, but because images, sounds, performances and narrative relations can be analysed. An interpretation begins with precise description: identify a scene, what is visible and audible, the sequence of shots and relevant context.

## Discourse and ideology
A discourse is a way of organising language, images and assumptions around a subject. Ask how a film makes some statements or identities appear obvious and others difficult to express. Ideology refers to patterns of ideas and practices connected with power; a film can negotiate conflicting positions rather than expressing one simple message. Analysis needs evidence from form and context, not just a label.

## Step-by-step method
1. Describe a specific moment: who is present, what happens and what is heard?
2. Identify a formal choice: framing, duration, camera angle, lighting, editing, sound or performance.
3. Explain a possible effect: what does the choice invite a viewer to notice or feel?
4. Connect it to representation or power while recognising alternative readings.
5. Check the film’s historical and production context. A claim about an audience’s actual response needs audience evidence; it cannot be proven from the shot alone.

## Example
A character framed alone in a crowded station might suggest isolation. That is an interpretation supported by composition, not proof of what every viewer feels. Compare the scene’s sound and neighbouring shots before deciding whether the interpretation holds.

## 50-minute lesson
0–10: distinguish description and interpretation. 10–20: define discourse and ideology. 20–35: analyse a brief film scene in pairs. 35–45: compare two interpretations and their evidence. 45–50: exit ticket on one formal feature and a supported effect.''',S),
note('visual-ray-essays','Ray, Pandian and Prasad · studying Indian cinema','''## Satyajit Ray: What Is Wrong with Indian Films?
In this historically situated critical essay, Ray argues that filmmaking needs imagination, planning and sensitivity to the medium rather than a reliance on imitation or technical gloss. He criticises aspects of contemporary production and calls for films grounded in the contexts they represent. Treat this as Ray’s argument from a particular historical moment, not a timeless verdict on all Indian films. Ask whether his ideas of realism and national style exclude other valuable forms, including popular song-and-dance cinema.

## M. S. S. Pandian: Tamil Cultural Elites and Cinema
Pandian’s essay examines relations between Tamil cultural elites and cinema. A productive starting question is how judgements about taste, respectability, popular entertainment and realism can be connected to caste and class. Do not assume that “elite” describes every person or that one attitude exhausts Tamil film history. Read the article for its historical examples and specific argument before attributing a detailed claim to it.

## M. Madhava Prasad: Ideology of the Hindi Film
Prasad’s study connects cinematic forms to political and economic history. One important concept, “feudal family romance,” helps analyse how certain narratives organise authority through family and social hierarchy, even as they also include modern desires and institutions. It is an analytical category for particular films and historical conditions, not a claim that all Hindi films have one plot. A scholarly review linked below also questions aspects of the historical fit; engage with disagreement rather than treating a framework as a formula.

## Compare and discuss
How does Ray’s judgement of style differ from Pandian’s analysis of cultural authority? How might Prasad connect a family ending to a wider structure of power? Use a scene and the assigned reading to substantiate the comparison.

## 50-minute lesson
0–10: define historical context. 10–22: identify Ray’s claim. 22–32: discuss who gets to define good taste. 32–42: apply a family-authority question to a film scene. 42–50: exit ticket distinguishing an author’s argument from your own.

## Reading limitation
This is an introductory comparison. Read the specific prescribed extracts for full arguments, historical examples and qualifications.''','https://jmionline.org/articles/1999/ideology_of_the_hindi_film_a_historical_construct.pdf','preliminary'),
note('visual-pather','Satyajit Ray · Pather Panchali','''## Introduction
Pather Panchali (1955) is Satyajit Ray’s Bengali film adapted from Bibhutibhushan Bandyopadhyay’s novel. The film follows a family in rural Bengal through everyday pleasures, poverty and bereavement. This note describes the film, not every event of the novel.

## Story from beginning to end
Harihar Ray, a priest and aspiring writer, struggles to support his family. His wife Sarbajaya manages the household and cares for their daughter Durga; an elderly relative, Indir Thakrun, also lives with them at times. Sarbajaya’s frustration with scarce resources contributes to conflict with Indir, while Durga shares affection and small treats with her.

Apu is born and grows up close to his older sister. The children explore their surroundings, watch travelling entertainers and follow a sweet seller they cannot afford. In a celebrated sequence they move through fields and discover a passing train. Their curiosity and delight coexist with the family’s economic difficulties. Indir leaves after conflict and dies away from the house; the children encounter her body.

Harihar travels in search of work, leaving Sarbajaya to manage an increasingly difficult situation. Durga is accused of stealing a neighbour’s necklace. During the monsoon the children enjoy the rain, but Durga falls ill and dies during a violent storm while her father is away. Do not infer a particular medical diagnosis from a short plot summary.

Harihar returns with gifts, not knowing of the death. When he shows the sari he has bought for Durga, Sarbajaya breaks down and he learns what has happened. As the family prepares to leave, Apu discovers the necklace hidden among Durga’s belongings and throws it into a pond. Harihar, Sarbajaya and Apu depart their village by cart for a new life. The film’s ending does not show the events of the later Apu films.

## Form and interpretation
Attention to landscape, sound, faces, everyday action and changes in pace gives small events weight. The train can be read as an image of discovery and a wider changing world; support an interpretation with the scene rather than treating a single symbolism as compulsory. Sarbajaya’s harshness and tenderness should be considered alongside the pressures she faces.

## 50-minute lesson
0–10: introduce family and adaptation. 10–25: map the children’s experiences and the family’s pressures. 25–35: discuss one use of sound or landscape. 35–45: analyse the homecoming and departure. 45–50: exit response on a detail and its effect.

## Questions
How does the film combine play with hardship? What changes when Harihar returns? Why might Apu throw the necklace away?''','https://satyajitray.org/pather-panchali-song-of-the-little-road/'),
note('visual-jaibhim','Anand Patwardhan · Jai Bhim Comrade','''## Introduction and content note
Jai Bhim Comrade (2011) is a documentary by Anand Patwardhan made over many years. It addresses caste discrimination, police violence and the politics of Dalit cultural expression. The film includes accounts of deaths and suicide; offer a content note and allow sensitive discussion.

## Structure and major subjects
The documentary takes the 1997 police firing in Mumbai’s Ramabai Ambedkar Nagar as a starting point. Residents had protested the desecration of a statue of B. R. Ambedkar; police opened fire, killing people. The film connects this event with the death of Dalit poet and singer Vilas Ghogre, who died by suicide after the violence.

Rather than following a single fictional plot, the film moves among testimony, songs, archival materials, political gatherings and arguments about caste, labour and collective action. It attends to Ambedkar’s legacy and to tensions and alliances in Dalit and left politics. Interviews and songs allow speakers to articulate experiences and positions, while selection, editing and the filmmaker’s perspective shape how audiences encounter them. The documentary’s construction does not by itself make the events imaginary or the testimony unimportant.

## Key approaches
Ask who is speaking, what knowledge they claim, how the film positions their testimony, and how a song differs from an interview in its emotional and political work. Avoid presenting Dalit communities as passive objects: the film records organised protest and cultural production. Historical claims about the police firing and legal proceedings should be checked against reliable reporting as well as the film.

## 50-minute lesson
0–10: establish respectful discussion and historical context. 10–22: outline the event and the documentary’s scope. 22–35: analyse an interview or song in a suitable excerpt. 35–45: discuss editing, evidence and filmmaker position. 45–50: exit ticket distinguishing a documented event from an interpretation.

## Questions
What can song communicate that an interview may not? How can a documentary be constructed and still investigate real events? How does the film relate caste to political organising?''','https://www.imdb.com/title/tt2157192/plotsummary/')]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added Literature and Visual Media: 5 units,',sum(len(d[f'course-17:{i}']) for i in range(5)),'note selections')
