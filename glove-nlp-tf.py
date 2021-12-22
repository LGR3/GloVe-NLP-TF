
# ########################################################### #
# RecrutAi GloVe NLP Task Force: a One-Liner Text_Normalize()
# by Lucas Glasner Regis <lgr3@cin.ufpe.br>


# ################# #
# IMPORTs
import re


# Remove URLs
def remove_url(s):
    url = re.compile(r"https?://\S+|www\.\S+")
    return url.sub(r"", s)


# Remove HTML Tags
def remove_html(s):
    html = re.compile(r"<.*?>")
    return html.sub(r"", s)


# Remove Hashtags
def remove_hashtags(s):
    return re.sub(r"#\S+", '', s)


# Remove Whole Word with Number/s in it
def remove_words_with_numbers(s):
    return re.sub(r'\S+[0-9]+\w*', '', s)


# Remove Emojis ( DOUBLE CHECK This one )
def remove_emoji(s):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", s)


# Remove Emails and @usernames
def remove_emails_usernames(s):
    return re.sub(r"\S*@\S*\s?", ' ', s)


# Remove exact match of *PROPNAME* e *propname*
def remove_propname(s):
    return re.sub(r"\*PROPNAME\*|\*propname\*", '', s)


# Remove string literals and extra blank spaces
def remove_extra_white_spaces(s):
    return re.sub('\s+', ' ', s)


# Set words to lower case aggressively
def force_lowercase(s):
    s = s.casefold()
    return s


# ======================
# Define the Text Normalize Function calling all the above methods
def text_normalize(s, language):
    s = remove_url(s)
    s = remove_html(s)
    s = remove_hashtags(s)
    s = remove_words_with_numbers(s)
    s = remove_emoji(s)
    s = remove_emails_usernames(s)
    s = remove_propname(s)
    s = remove_extra_white_spaces(s)

    if language == 'portuguese':
        s = force_lowercase(s)

    return s
