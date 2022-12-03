def get_score(guide):
    shape_score = {"X": 1, "Y": 2, "Z": 3}
    draw = ["A X", "C Z", "B Y"]
    win = ["C X", "B Z", "A Y"]
    score = 0
    for turn in guide:
        if turn in draw:
            score += 3
        elif turn in win:
            score += 6
        score += shape_score[turn[2]]
    return score


def real_score(guide):
    shape_score = {"A": 0, "B": 1, "C": 2}
    score = 0
    for turn in guide:
        shape_points = shape_score[turn[0]]
        # draw
        if turn[2] == "Y":
            score += 3
            score += shape_points + 1
        # win
        elif turn[2] == "Z":
            score += 6
            score += ((shape_points + 1) % 3) + 1
        # lose
        else:
            score += ((shape_points + 2) % 3) + 1
    return score


def real_score_alternative(guide):
    draw_score = {"A": 1, "B": 2, "C": 3}
    win_score = {"A": 2, "B": 3, "C": 1}
    lose_score = {"A": 3, "B": 1, "C": 2}
    score = 0
    for turn in guide:
        shape = turn[0]
        if turn[2] == "Y":
            score += 3
            score += draw_score[shape]
        elif turn[2] == "Z":
            score += 6
            score += win_score[shape]
        else:
            score += lose_score[shape]
    return score

