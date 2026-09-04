def TupleForm(text):
    length = len(text)
    words = text.split()
    upper = text.upper()
    word_count = len(words)
    return length, words, upper, word_count

subject = "Returning multiple value in one return function"
sol = TupleForm(subject)
print(sol)
print(f"There are total {sol[3]} in the sentance")
length_here, all_words, uppercase, word_count = TupleForm(subject)
print(f"And, the length is {length_here}")


from dataclasses import dataclass
# mutable
@dataclass
class summarized:
    length: int
    words: int
    upper_case: str
    present_words: str

def summarize(text_here):
    return summarized(
        length=len(text_here),
        upper_case=text_here.upper(),
        present_words=text_here.split(),
        words=len(text_here.split())
    )

summary = summarize("Now returning multiple values.")
print(summary)
print(summary.length)
summary.length = 10 # Mutable
print(summary.length)

def analyze_text(text):
    return{
        "length": len(text),
        "upper": text.upper(),
        "all_words": text.split(),
        "number_words": len(all_words)
    }
final = analyze_text("Now returning multiple values.")
print(final)