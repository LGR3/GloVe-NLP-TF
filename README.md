# GloVe-NLP-TF
RecrutAi GloVe NLP Task Force: a One-Liner Text_Normalize()

This code/lib should be used in-code and must be identical for model constructors and for using the models predict().

```python
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
```

The essence of the code is the snippet above.  

---

For downloading GloVe PreTrained files, refer to :  

English GloVe : 
https://nlp.stanford.edu/data/glove.840B.300d.zip  

from: https://nlp.stanford.edu/projects/glove/  



Portuguse GloVe
http://143.107.183.175:22980/download.php?file=embeddings/glove/glove_s300.zip

from: http://nilc.icmc.usp.br/embeddings  
OR  
http://nilc.icmc.usp.br/nilc/index.php/repositorio-de-word-embeddings-do-nilc
