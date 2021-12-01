from google.cloud import language


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")



# text = "Guido van Rossum is great!"
# analyze_text_sentiment(text)
# print("This is awesome")

def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")


# text = "Guido van Rossum is great!"
# print(analyze_text_entities(text))




def analyze_text_syntax(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    fmts = "{:10}: {}"
    print(fmts.format("sentences", len(response.sentences)))
    print(fmts.format("tokens", len(response.tokens)))
    for token in response.tokens:
        print(fmts.format(token.part_of_speech.tag.name, token.text.content))


# text = "Guido van Rossum is great!"
# analyze_text_syntax(text)


def classify_text(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")


text = (
    "Python is an interpreted, high-level, general-purpose programming language. "
    "Created by Guido van Rossum and first released in 1991, "
    "Python's design philosophy emphasizes code readability "
    "with its notable use of significant whitespace."
)
classify_text(text)

# text = "Guido van Rossum is great!"
analyze_text_entities(text)