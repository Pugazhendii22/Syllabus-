import json
p='prepared-notes.json';d=json.load(open(p))
def n(id,title,text,source): return {'id':id,'title':title,'source':source,'status':'preliminary','text':text}
d['course-17:0'].insert(1,n('visual-baudrillard','Jean Baudrillard · Simulation — preliminary outline','''# Jean Baudrillard · Simulation — preliminary outline
Literature and Visual Media · Semester 3, Unit 1

## Reading limitation
The exact boundaries of the prescribed “Postmodern and Popular Culture Simulations” selection have not been independently confirmed. This is a conceptual introduction, not a complete summary of the assigned text. Check the course anthology before relying on specific examples or quotations.

## Representation and simulation
A common model of representation assumes an image refers back to an original reality, which it may represent accurately or distort. Baudrillard asks what happens when models, signs and mediated representations organise what a society experiences as real. Simulation is not simply lying: its force lies in complicating the distinction between a copy and an independently accessible original.

## Hyperreality and Disneyland
Hyperreality describes a condition in which models and signs can become more decisive than any stable original they seem to represent. Baudrillard’s discussion of Disneyland suggests that presenting the park as an imaginary space can make the world outside appear simply real, even though that outside world is also mediated and constructed. This is his provocative argument, not a factual claim that people or material conditions do not exist.

## Apply and question
Consider a carefully designed online profile. It selects images and styles that may influence how someone is perceived. This can illustrate mediation, but a curated profile alone does not prove Baudrillard’s larger claim about simulation. Ask what evidence would support or challenge the argument.

## Lesson and questions
0–10 min: distinguish a map from a landscape. 10–25: compare representation and simulation. 25–38: examine the Disneyland example. 38–45: discuss a digital example and its limits. 45–50: explain why simulation is not merely a synonym for “fake.”''','https://www.iacis.org/iis/2024/2_iis_2024_1-8.pdf'))
d['course-17:3'].insert(1,n('visual-neale-baskaran','Neale and Baskaran · prescribed essays — preliminary outline','''# Neale and Baskaran · prescribed essays — preliminary outline
Literature and Visual Media · Semester 3, Unit 4

## Important limitation
The exact prescribed extracts have not yet been examined in full. These are starting questions, not complete summaries of the essays. Read the assigned versions before making detailed attributions.

## Stephen Neale: Film Noir
Film noir is often associated with crime, hard-edged or uncertain morality and distinctive lighting, but the category is contested. Neale’s genre scholarship encourages attention to how genres are defined historically, including industrial and critical uses, rather than assuming all examples share one timeless essence. Ask whether “noir” describes a genre recognised by producers at the time, a retrospective critical label, a style or a cycle. These positions need not be reduced to a single checklist.

## S. Theodore Baskaran: Patriotic Cinema: An Aspect of the Freedom Struggle
The essay is listed as a chapter of The Message Bearers, a study of nationalist politics and entertainment media in South India. Investigate how film, song, performance and colonial censorship interacted with political movements. Do not attribute particular films or intentions to Baskaran until the assigned chapter confirms them. A work can evoke national sentiment in multiple, historically specific ways; the audience’s response also needs evidence.

## Classroom plan
0–10 min: discuss what makes a genre. 10–22: compare two possible definitions of noir. 22–35: consider film, song and censorship in historical context. 35–45: identify a claim in each assigned essay and its evidence. 45–50: write one question for further reading.

## Questions
Who creates a genre label and when? How can restrictions on expression affect cinematic form?''','http://www-lib.tufs.ac.jp/opac/en/recordID/catalog.bib/BB0571960X?hit=-1&caller=xc-search'))
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added 2 explicitly incomplete outlines')
