import os
import PyPDF2
import openai
import easygui
from Hub import hubmain

# Configure OpenAI API key
openai.api_key = hubmain.OAI


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text


def get_best_candidate_direct(cv_texts, role):
    scores = []
    for index, cv_text in enumerate(cv_texts):
        truncated_cv_text = cv_text[:2000]  # Adjust this as needed

        messages = [
            {"role": "system",
             "content": "You are a hiring manager assessing CVs for roles I will provide. Rate the suitability of this CV on a scale of 1-10. And only provide a number and nothing else"},
            {"role": "assistant", "content": f"Evaluate for an {role} role"},
            {"role": "user", "content": f"Here's the CV content: {truncated_cv_text}"}
        ]

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        try:
            score = float(response.choices[0].message['content'].strip())
            scores.append((index, score))
        except ValueError:
            scores.append((index, 0))

    # Sort by score and get the CV with the highest score
    best_index, best_score = sorted(scores, key=lambda x: x[1], reverse=True)[0]
    return cv_files[best_index], best_score

def get_reasoning_for_best_candidate(cv_text, role):
    messages = [
        {"role": "system",
         "content": f"You have identified this CV as the best fit for an {role} role among the provided options. Please elaborate on the reasons why this candidate is considered the best."},
        {"role": "user", "content": f"Here's the best CV content: {cv_text}"}
    ]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message['content'].strip()


if __name__ == "__main__":
    directory_path = "CVs"
    cv_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.pdf')]
    cv_texts = [extract_text_from_pdf(cv) for cv in cv_files]

    desired_role = easygui.enterbox("Enter the desired role for which you're hiring:")

    best_cv, score = get_best_candidate_direct(cv_texts, desired_role)

    best_cv_text = extract_text_from_pdf(best_cv)
    reasoning = get_reasoning_for_best_candidate(best_cv_text[:2000],
                                                 desired_role)  # Truncating for simplicity, adjust as needed.

    result_message = f"The best CV for the {desired_role} role is: {os.path.basename(best_cv)} with a score of: {score}\n\nReasoning for choosing this CV: {reasoning}"

    easygui.msgbox(result_message, title="Result")





