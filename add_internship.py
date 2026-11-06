import json
C='courses.json';P='prepared-notes.json';
with open(C,encoding='utf-8') as f:c=json.load(f)
with open(P,encoding='utf-8') as f:d=json.load(f)
course=next(x for x in c if x['id']=='course-30')
course['units']=[
 {'title':'Internship A · Identification','content':'Course content A: Define career goals; identify prospective employers conducive to meeting career goals. The course description describes outreach teaching of basic communication and writing to working adults in neighbouring coastal and rural communities.'},
 {'title':'Internship B · Application','content':'Course content B: Job application and follow-up; interviewing.'},
 {'title':'Internship C · Enrollment','content':'Course content C: Fill out the Internship Registration Form; obtain approvals from the major faculty advisor and internship coordinator; the internship office facilitates course enrollment. The syllabus says the student cannot self-enroll.'},
 {'title':'Internship D · Requirements','content':'Course content D: Complete required work hours; submit written reports and a self-assessment; facilitate employer evaluation; meet due dates. The printed syllabus specifies a minimum of 80 work hours per credit hour and references Blackboard; confirm current institutional instructions.'}]
def n(id,title,body,lesson,questions):
 return {'id':id,'title':title,'source':'https://www.pondiuni.edu.in/wp-content/uploads/2024/03/SyllabusNEP-B.A.HonorsEnglish2023-24.pdf','text':f'# {title}\nInternship · Semester 5\n\n{body}\n\n## Suggested 50-minute preparation session\n{lesson}\n\n## Reflection\n{questions}\n\nThis is practical guidance, not an official form, approval or placement. The syllabus labels A–D as course-content sections, not formal units. Confirm all requirements with the college.'}
d['course-30:0']=[n('internship-identification','A · Finding a suitable internship', '''## What the syllabus asks
Define career goals and identify prospective employers or hosts. The course description specifically envisions outreach in which undergraduate students support working adults in neighbouring coastal and rural communities with basic communication and writing. The description also mentions professional settings, so check which placements and host organisations your college approves.

## A practical sequence
1. Write two or three goals: for example, practise listening to adult learners, design an accessible English activity, and learn to document work responsibly.
2. With the faculty coordinator, identify a potential local organisation, community group or approved workplace. Do not promise training or contact participants on behalf of the college without authorisation.
3. Ask about location, safety, supervision, working hours, language preferences and accessible timings. Discuss whether the placement genuinely matches both the course and the community’s needs.
4. Choose tentative goals with the host rather than assuming learners are deficient. Adults bring existing languages, work skills and expertise; English learning should build on those strengths.
5. Record the name and role of the person contacted, response and next step without collecting unnecessary personal data.

## Planning a respectful outreach session
With consent, ask what participants want to use English for—perhaps introductions, a simple workplace message or reading a notice. Use Tamil or another shared language for explanation where helpful, and adapt to different literacy levels. Participation should be voluntary. Arrange a supervised and accessible venue.''','0–10: list goals. 10–20: discuss community strengths and needs. 20–30: brainstorm suitable hosts. 30–40: assess safety and access. 40–50: draft three questions for the coordinator.','Which placements match your goals and the course description? How will you find out what participants actually want to learn?')]
d['course-30:1']=[n('internship-application','B · Application, follow-up and interview', '''## Preparation
Confirm the approved application procedure and whether the placement requires an introduction letter. Read the host’s description and write a short, truthful résumé: education, communication skills, relevant teaching or volunteering and contact details. Do not invent experience or include sensitive documents unless the authorised process requires them.

## Sample professional email
Subject: Inquiry about an approved undergraduate internship

Dear [name or role],
I am an undergraduate English student at [college]. I am exploring an internship that supports adult communication and writing skills. I would be grateful to know whether your organisation hosts students and what the application process involves. My faculty coordinator can provide details of the course requirements.
Thank you for your time.\n[Name and contact]

Personalise and confirm the recipient before sending. After a reasonable interval, one polite follow-up can ask whether the message was received; do not repeatedly pressure the host.

## Interview practice
Prepare a brief introduction, one example of teamwork, and how you would ask adult learners about their goals. Ask about supervision, hours, safety, accessibility and what information you may share. Dress appropriately for the setting as directed; a dress code should be safe, accessible and respectful.''','0–10: examine a host description. 10–20: draft a short introduction. 20–30: practise interview questions in pairs. 30–40: edit the email for clarity. 40–50: prepare two questions for the host.','How does your experience match the placement? What do you need to know before accepting?')]
d['course-30:2']=[n('internship-enrolment','C · Enrollment and approvals', '''## Syllabus sequence
The published course content says to complete an Internship Registration Form, obtain approval signatures from the major faculty advisor and internship coordinator, and enroll through the internship office; it says the student cannot self-enroll. Names of offices and procedures may have changed, so verify current forms and instructions with your college. This app does not submit a form or enroll you.

## Practical checklist
1. Confirm eligibility, approved host, supervisor and whether the role fits the course.
2. Obtain the current form through the college’s official channel. Complete dates, placement details and contact information accurately.
3. Obtain the required faculty-advisor and coordinator approvals in the order your college specifies; ask where the signed form must go.
4. Confirm that the responsible office has completed enrollment. Save an acknowledgement securely.
5. Agree on the schedule, supervision, reporting process and safeguarding or accessibility arrangements before beginning.

Never upload identification, signatures or participants’ personal details into an unsecured form or public repository. These notes cannot verify a placement’s approval.''','0–10: arrange the published steps. 10–20: identify who can answer procedural questions. 20–30: review a blank sample form, if supplied by the college. 30–40: discuss privacy. 40–50: write a personal checklist.','Who confirms your enrollment? Which details must be checked before your first day?')]
d['course-30:3']=[n('internship-requirements','D · Hours, reports and reflection', '''## Check the actual rules first
The syllabus specifies a minimum of 80 work hours per credit hour. For this listed four-credit course, that arithmetic is 320 hours. The document also mentions reports, a self-assessment, an employer evaluation and Blackboard deadlines. **Confirm the currently applicable hour requirement, forms, deadlines, placement conditions and submission system with your college before making commitments**; this app cannot establish whether those details have changed.

## Keeping a log
Record date, start and end times, approved activity, learning and supervisor confirmation in the format the college requires. Separate planning, direct work and reflection if instructed. Record actual hours only; do not backdate, fabricate attendance or assume travel counts. Protect participant privacy: use anonymous descriptions unless informed consent and college policy permit identification.

## Suggested report structure
Title and placement details; approved objectives; description of the host’s work; responsibilities and activities; one anonymised communication or teaching activity; what worked and what changed based on participant feedback; challenges and ethical decisions; skills learned; and a short evaluation of how the placement relates to educational and career goals. Attach only documents requested through an approved channel.

## Sample adult-English activity: 50 minutes
0–5: agree on a practical goal with learners. 5–15: model a short spoken greeting and workplace request. 15–25: practise in pairs, allowing translation. 25–35: jointly draft a short message. 35–45: participants adapt it to their own situation. 45–50: invite optional feedback and one question. This is a suggested activity, not a mandated internship session.

Ask the supervisor about the employer evaluation and submit the self-assessment by the confirmed deadline. Never claim credit until the college confirms completion.''','0–10: locate the current official requirement. 10–20: practise an honest log entry. 20–30: outline an anonymised report. 30–40: adapt the sample activity. 40–50: write one strength and one learning goal.','What does the printed syllabus say about hours, and who confirms the current rule? How can you report learning while protecting privacy?')]
with open(C,'w',encoding='utf-8') as f:json.dump(c,f,ensure_ascii=False,indent=2);f.write('\n')
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
