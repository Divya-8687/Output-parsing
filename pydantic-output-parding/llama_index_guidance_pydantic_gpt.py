from pydantic import BaseModel
from typing import List
from guidance.llms import OpenAI

from llama_index.program import GuidancePydanticProgram

class Response(BaseModel):
  client_emotional_state: str
  therapist_emotional_state: str
  
if __name__=="__main__":
    program = GuidancePydanticProgram(
        output_cls=Response,
        prompt_template_str="A client has following emotions - anger, fear, sadness, shame, loneliness, nervousness, disappointment, helplessness, guilt, boredom, joy, love, optimism, relief, calm. A therapist has the following emotions - supportive, empathetic, compassionate, calm, kind, bored, frustrated, irritated, sad, angry. Assume that only these emotions exist for the following analysis. Assign top three emotions to the patient and the therapist, only from the list provided, along with a fractional confidence. Do a sentiment analysis on following dialogue -\n{{query}}\n",
        guidance_llm=OpenAI("text-davinci-003"),
        verbose=True
    )
    output = program(query="THERAPIST:Yeah,yeah.(chuckle)\nCLIENT:I should do this cause boom,I'll get a job (laughter)\nTHERAPIST:That's not a reason to have.That one got a job,so okay,I'll do that.(continued laughter)\nCLIENT:Yeah,I think like,I see a lot of people,like our post-doc's leave our lab and get like industry jobs or,you know good jobs.So I'm like doubtful,it seems like a long haul.\nTHERAPIST:Yeah,they usually end up going for six years and then post doc for like a couple or three years can really\nCLIENT:Right.There was,Tanya,the one who's right behind me,she's been going for eight years.[00:14:57]\nTHERAPIST:(inaudible) sooner for post doc.Woah.\nCLIENT:She was,yeah.And I know another post doc who's been real long,I don't know how long it's been,but he just had his 42nd birthday.I was like don't you ever want to leave?(chuckle) I think that he had like this really (inaudible) But that's life.\nTHERAPIST:Yes.\nCLIENT:Yeah.I don't know.(pause) I don't know like where to,like what I should think about when deciding.Which ones you know,are my choices.Like right now I think I'm just going to look and see like,what,what is this going to get me?(chuckle) I don't know.\nTHERAPIST:Like what does the future of the job market look like.\nCLIENT:Right.\nTHERAPIST:And that stuf f probably looks better while in school.\nCLIENT:Right.[00:16:23] But I think I have a list,like which (mumbles) in school.\nTHERAPIST:Do you like (inaudible) or do you like high school period.I don't know a lot of this school,and used to but,sorry.\nCLIENT:Period.I don't know,and again,I don't know if I want to put myself through the process.(mumbles) I don't know.\nTHERAPIST:Could your career have a (inaudible) to be up again?\nCLIENT:Right.I don't know,it's a lot,you have to do resident and then yeah,but the application takes such a long time.It will take another year and seems like a waste of a year.\nTHERAPIST:Got it.\nCLIENT:(pause) I don't know.(pause)")
    print(output)