import paralleldots
paralleldots.set_api_key('2wvOXhkMg7NRUGq1EGk9dAoQCU4UO804uJoI46ZLwfo')

def ner(text):

    ner = paralleldots.ner(text)
    return ner

