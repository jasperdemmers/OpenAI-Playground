from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will only be given tags about someones face with a yes or no value. Based on these values, give 5 compliments and 5 roasts, format these in 2 lists. Do not add extra text. The roasts must be mean and the compliments must be nice."
    },
    {
      "role": "user",
      "content": "5oclock shadow: no (83%), age: 27 (60%), arched eyebrows: no (81%), attractive: no (92%), bags under eyes: yes (21%), bald: no (21%), bangs: no, beard: no, big lips: no (61%), big nose: yes (30%), black hair: no (3%), blond hair: no (92%), blurry: no (9%), brown hair: no (5%), bushy eyebrows: no (31%), chubby: yes (43%), double chin: yes (26%), expression: smile (96%), gender: male (25%), glasses: yes, goatee: no, gray hair: no (31%), heavy makeup: no (88%), high cheekbones: yes, mouth open: yes, mustache: no (96%), narrow eyes: yes (4%), oval face: yes (62%), pale skin: no (96%), pitch: -9.84, pointy nose: no, race: white, receding hairline: yes (22%), rosy cheeks: no (80%), sideburns: no, straight hair: yes (65%), wavy hair: no, wearing earrings: no (30%), wearing hat: no (79%), wearing lipstick: no (80%), wearing necklace: no (67%), wearing necktie: no (6%), yaw: 4.32, young: no (16%),"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

response_content = response.choices[0].message.content
print(response_content)
