def calculate_authenticity(influencer):

    followers = influencer["followers"]
    following = influencer["following"]
    likes = influencer["likes"]
    comments = influencer["comments"]
    shares = influencer["shares"]
    saves = influencer["saves"]
    engagement_spike = influencer["engagement_spike"]

    engagement_rate = (
        (likes + comments + shares) / followers
    ) * 100

    score = 100

    if engagement_rate < 8:
        score -= 15

    if engagement_rate < 6:
        score -= 20

    if following > followers * 0.01:
        score -= 10

    if comments < likes * 0.06:
        score -= 10

    if comments > likes * 0.15:
        score -= 10

    if shares > likes * 0.12:
        score -= 10

    if engagement_spike > 1.3:
        score -= 10    

    return max(score, 0)