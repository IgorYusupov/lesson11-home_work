import utils

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def list_all_candidates():
    candidates = utils.load_candidates_from_json()

    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:pk>")
def page_candidates_by_id(pk):
    candidate = utils.get_candidate(pk)

    if candidate is None:

        return "Такого кандидата нет"

    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    counter = len(candidates)

    if len(candidates) == 0:

        return "Таких кандидатов нет"

    return render_template("search.html", candidates=candidates, counter=counter)


@app.route("/skills/<skill_name>")
def page_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    counter = len(candidates)
    skill = skill_name

    if len(candidates) == 0:

        return "Таких кандидатов нет"

    return render_template("skill.html", candidates=candidates, counter=counter, skill=skill)


if __name__ == "__main__":
    app.run()
