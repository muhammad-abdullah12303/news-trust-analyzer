import streamlit as st
import string

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="News Analyzer", layout="centered")
st.title("News Credibility Analyzer")

# ---------------- WORD LISTS ----------------
fear_words = ["danger", "alert", "threat", "warn", "panic", "fury", "angry"]
sensational_words = ["breaking", "shocking", "exclusive", "wasting"]
named_sources = ["police", "council", "mayor", "hospital", "official", "reporter"]
opinion_words = ["think", "believe", "angry", "furious", "insult"]

# ---------------- USER INPUT ----------------
news_input = st.text_area("Paste a news article below:", height=250)

# ---------------- ANALYSIS ----------------
if news_input.strip():

    # Capital words & punctuation (before cleaning)
    capital_count = sum(1 for w in news_input.split() if w.isupper() and len(w) > 2)
    exclamation_count = news_input.count("!")

    # Clean text
    cleaned = news_input.lower()
    for p in string.punctuation:
        cleaned = cleaned.replace(p, "")
    words = cleaned.split()

    # Counts
    fear_count = sum(1 for w in words if w in fear_words)
    sensational_count = sum(1 for w in words if w in sensational_words)
    source_count = sum(1 for w in words if w in named_sources)
    opinion_count = sum(1 for w in words if w in opinion_words)

    # ---------------- TONE ----------------
    if fear_count >= 2:
        tone = "Fear-based"
    elif sensational_count >= 2:
        tone = "Sensational"
    elif fear_count >= 1 or sensational_count >= 1:
        tone = "Emotional"
    else:
        tone = "Neutral"

    # ---------------- CREDIBILITY SCORE ----------------
    score = 100
    score -= fear_count * 5
    score -= sensational_count * 5
    score -= opinion_count * 10
    score -= capital_count * 5
    score -= exclamation_count * 5
    score += source_count * 10
    score = max(0, min(100, score))

    # ---------------- OUTPUT ----------------
    st.divider()
    st.metric("Credibility Score", f"{score}/100")
    


    



