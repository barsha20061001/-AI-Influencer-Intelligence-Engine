import pandas as pd
import os

from services.authenticity_service import calculate_authenticity
from services.growth_service import calculate_growth_score
from services.score_service import calculate_ratefluencer_score
from services.brand_service import match_brand
from services.ml_service import train_ml_model

def get_influencers():

    csv_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "influencers.csv"
    )

    df = pd.read_csv(csv_path)

    influencers = df.to_dict(
        orient="records"
    )

    for influencer in influencers:
        influencer["authenticity"] = calculate_authenticity(influencer)

        influencer["growth_score"] = calculate_growth_score(influencer)

        brand_result = match_brand(influencer)
        influencer["best_brand"] = brand_result["brand"]
        influencer["brand_match_score"] = brand_result["brand_match_score"]
        influencer["brand_reason"] = brand_result["brand_reason"]

        
    

    ml_scores = train_ml_model(influencers)

    for influencer, score in zip(influencers, ml_scores):
        influencer["ratefluencer_score"] = score
   
    return influencers