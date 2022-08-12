from flask import Flask
from utils import get_all, get_by_pk, get_by_skill, load_candidates

FILEPATH = 'candidates.json'

data = load_candidates(FILEPATH)

candidates_list = get_all(data)

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates_string = '<pre>' + '\n'
    for item in candidates_list:
        candidates_string += f'{item}\n\n'
    candidates_string += '</pre>'
    return candidates_string


@app.route('/candidates/<int:pk>/')
def get_candidate(pk):
    candidate = get_by_pk(pk, candidates_list)
    if candidate:
        candidate_info = f'<img src = "{candidate.picture}">'
        candidate_info += f'<pre> {candidate} </pre>'
    else:
        candidate_info = 'NOT FOUND'
    return candidate_info


@app.route('/skills/<skill>/')
def get_skills(skill):
    users = get_by_skill(skill, candidates_list)
    if users:
        candidates_string = '<pre>'
        for item in users:
            candidates_string += f'{item}\n\n'
        candidates_string += '</pre>'
    else:
        candidates_string = "NOT FOUND"
    return candidates_string


if __name__ == '__main__':
    app.run(port=5000)
