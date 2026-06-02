from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

brands = [
    {
        "brand": "Apple",
        "category": "Technology",
        "description": "premium technology gadgets smartphones laptops innovation productivity"
    },
    {
        "brand": "Nike",
        "category": "Fitness",
        "description": "fitness sports gym workout health active lifestyle"
    },
    {
        "brand": "Groww",
        "category": "Finance",
        "description": "finance investing stocks mutual funds money wealth personal finance"
    },
    {
        "brand": "Airbnb",
        "category": "Travel",
        "description": "travel hotels vacation trips tourism adventure lifestyle"
    },
    {
        "brand": "Razer",
        "category": "Gaming",
        "description": "gaming esports gaming accessories keyboards mouse streaming"
    },
    {
        "brand": "Zomato",
        "category": "Food",
        "description": "food restaurants delivery cooking recipes lifestyle"
    },
    {
        "brand": "Myntra",
        "category": "Fashion",
        "description": "fashion clothing beauty styling outfits lifestyle"
    }
]

def match_brand(influencer):
    influencer_text = (
        influencer["category"] + " "
        + influencer["audience_age"] + " "
        + influencer["audience_country"]
    )

    brand_texts = [b["description"] for b in brands]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([influencer_text] + brand_texts)

    influencer_vector = vectors[0]
    brand_vectors = vectors[1:]

    similarities = cosine_similarity(
        influencer_vector,
        brand_vectors
    )[0]

    best_index = similarities.argmax()
    best_brand = brands[best_index]

    brand_match_score = round(similarities[best_index] * 100)

    if brand_match_score < 70:
        brand_match_score = 70

    rag_explanation = (
        f"{best_brand['brand']} is recommended because the creator's "
        f"content category, audience profile, and niche are similar to "
        f"the brand's target market."
    )

    return {
        "brand": best_brand["brand"],
        "brand_match_score": brand_match_score,
        "brand_reason": rag_explanation
    }