import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def train_ml_model(influencers):
    df = pd.DataFrame(influencers)

    df["engagement_rate"] = (
        (df["likes"] + df["comments"] + df["shares"]) / df["followers"]
    ) * 100

    # synthetic target for hackathon demo
    df["campaign_success_score"] = (
        0.25 * df["authenticity"]
        + 0.25 * df["growth_score"]
        + 0.20 * df["brand_match_score"]
        + 0.30 * df["engagement_rate"] * 10
    )

    df["campaign_success_score"] = df["campaign_success_score"].clip(0, 100)

    features = [
        "followers",
        "likes",
        "comments",
        "shares",
        "saves",
        "views",
        "posts_per_week",
        "authenticity",
        "growth_score",
        "brand_match_score",
    ]

    X = df[features]
    y = df["campaign_success_score"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    predictions = model.predict(X)

    return [round(score) for score in predictions]