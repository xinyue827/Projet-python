
import resend
from openai import OpenAI
import pandas as pd

# # Envoi de mails avec pièces jointes à l'aide de l'API Resend

client = OpenAI(api_key="XXX")
resend.api_key = "XXX"

def send_email(recipient, content, cv_path):
    f = open(cv_path, "rb").read()
    params = {
        "from": "cv@rooster.work",
        "to": recipient,
        "subject": "Candidature d'emploi",
        "html": content,
        "bcc": ["jingjing996131@gmail.com"],
        "attachments": [{"filename": "CV_Jingjing_Alternance.pdf", "content": list(f)}],
    }
    resend.Emails.send(params)


# # Utilise le modèle GPT d'OpenAI pour générer un contenu en HTML pour une lettre de candidature professionnelle

def gpt(text):
    role_system = """
You are a job application specialist with a focus on creating professional HTML email formats. Your task is to craft a concise and clear job application email for Jingjing, who is currently a Master's student in Statistics and Econometrics at the University of Strasbourg. Jingjing has solid expertise in economics, finance, and data analysis, with previous internships as an accounting assistant and analysis & reporting officer. The email should highlight her academic background, professional experiences, and her ability to work both independently and in a team. The output must be in HTML format, tailored to a French company's job listing that Jingjing is applying for. The content should be professional, in French, and directly address the hiring manager or recruitment team of the company.
-Objective: To assist Jingjing in creating a strong first impression with her job application email, effectively showcasing her qualifications for a position that aligns with her background in statistics, econometrics, economics, and finance.
-Format Requirements: HTML email format, professional and concise language, French content."""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": role_system},
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message.content


# # Charge les descriptions de travail à partir d'un fichier Excel, génère des e-mails personnalisés basés sur ces descriptions, et les envoie aux destinataires avec un CV en pièce jointe.

import pandas as pd

file_path = "job_descriptions.xlsx"
df = pd.read_excel(file_path)
cv_path = "CV_Jingjing_Alternance.pdf"

for index, row in df.iterrows():
    recipient = row['Email']
    description = row['Description']
    send_email(recipient, gpt(description), cv_path)
    print(f"Send OK {index}")

