def calculate_growth_score(influencer):
    followers = influencer["followers"]
    posts_per_week = influencer["posts_per_week"]
    views = influencer["views"]
    audience_expansion = influencer["audience_expansion"]

    view_rate = (views / followers) * 100

    score = 40

    if view_rate > 40:
        score += 20

    if posts_per_week >= 5:
        score += 20

    if audience_expansion >= 80:
        score += 20
    elif audience_expansion >= 70:
        score += 10

    return min(score, 100)











