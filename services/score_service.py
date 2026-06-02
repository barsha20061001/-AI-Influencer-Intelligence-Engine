def calculate_ratefluencer_score(influencer):
    authenticity = influencer["authenticity"]
    growth = influencer["growth_score"]

    followers = influencer["followers"]
    likes = influencer["likes"]
    comments = influencer["comments"]
    shares = influencer["shares"]

    engagement_rate = ((likes + comments + shares) / followers) * 100

    engagement_score = min(engagement_rate * 10, 100)

    final_score = (
        0.4 * authenticity +
        0.3 * growth +
        0.3 * engagement_score
    )

    return round(final_score)