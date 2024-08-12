import os
from gemba.utils import get_gemba_scores


def compute_mqm_scores(
    source,
    hypothesis,
    source_lang="English",
    target_lang="Spanish",
    method="GEMBA-MQM",
    model="gpt-4o",
    explanations=False,
):
    if not os.path.isfile(source):
        raise Exception(f"Source file {source} does not exist.")

    if not os.path.isfile(hypothesis):
        raise Exception(f"Source file {hypothesis} does not exist.")

    with open(source, "r") as f:
        source = f.readlines()
    source = [x.strip() for x in source]

    with open(hypothesis, "r") as f:
        hypothesis = f.readlines()

    hypothesis = [x.strip() for x in hypothesis]

    assert len(source) == len(
        hypothesis
    ), "Source and hypothesis files must have the same number of lines."

    if not explanations:
        answers = get_gemba_scores(
            source, hypothesis, source_lang, target_lang, method, model
        )
    else:
        answers = get_gemba_scores(
            source,
            hypothesis,
            source_lang,
            target_lang,
            method,
            model,
            list_mqm_errors=True,
        )

    return answers


if __name__ == "__main__":
    import sys

    res = compute_mqm_scores(sys.argv[1], sys.argv[2], explanations=True)
    print(res)
