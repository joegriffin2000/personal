import string

def remove_punctuation(text:str) -> str:
    if isinstance(text,str):
        return text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    elif isinstance(text,ls):
        return [i.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))) for i in text]
    else:
        raise ValueError("must pass text in string or list form")

def hasPunctuation(text:str) -> bool:
    if isinstance(text,str):
        return any(p in text for p in string.punctuation)
    elif isinstance(text,ls):
        return any([True for i in text if any(p in i for p in string.punctuation)])
    else:
        raise ValueError("must pass text in string or list form")