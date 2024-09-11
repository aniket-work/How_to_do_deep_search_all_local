import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch

# Expanded arrays for story generation
beginnings = [
    "Once upon a time, in a small village nestled among rolling hills,",
    "In the bustling city of New York, where dreams come to life,",
    "Deep in the heart of the Amazon rainforest,",
    "On a distant planet, light-years away from Earth,",
    "In a world where magic and technology coexist,",
    "As the first rays of sunlight peeked over the horizon,",
    "In the depths of an ancient library, filled with forgotten knowledge,",
    "Amidst the ruins of a once-great civilization,",
    "On a stormy night, when the wind howled and the rain poured,",
    "In a hidden valley, untouched by the outside world for centuries,"
]

middles = [
    "a young adventurer stumbled upon an ancient artifact.",
    "two strangers' paths crossed, changing their lives forever.",
    "a brilliant scientist made a groundbreaking discovery.",
    "a group of friends embarked on a perilous journey.",
    "a long-lost secret was finally revealed.",
    "a mysterious figure appeared, bearing an urgent message.",
    "an unlikely hero rose to face an impending threat.",
    "a forgotten prophecy began to unfold in unexpected ways.",
    "a series of inexplicable events set in motion a chain reaction.",
    "an ordinary person discovered they possessed extraordinary abilities.",
    "conflicting factions clashed over control of a powerful resource.",
    "a time traveler arrived with a warning from the future.",
    "an artificial intelligence gained sentience and questioned its purpose.",
    "a long-dormant evil awakened, threatening to engulf the world.",
    "a revolutionary invention promised to solve humanity's greatest challenges."
]

developments = [
    "As tensions rose, alliances were formed and broken.",
    "The characters found themselves racing against time to prevent disaster.",
    "Unexpected obstacles forced them to question their beliefs and motivations.",
    "A twist of fate brought new allies and enemies into the fray.",
    "Ancient wisdom and cutting-edge technology collided in spectacular fashion.",
    "The lines between reality and illusion began to blur.",
    "Personal sacrifices were made for the greater good.",
    "Hidden agendas came to light, complicating matters further.",
    "Nature itself seemed to rebel against the unfolding events.",
    "Moral dilemmas tested the characters' resolve and integrity.",
    "A journey into the unknown revealed startling truths about the past.",
    "The balance of power shifted dramatically, reshaping the political landscape.",
    "Long-buried secrets resurfaced, threatening to unravel everything.",
    "A seemingly insignificant detail proved to be the key to solving the mystery.",
    "The characters were forced to confront their deepest fears and insecurities."
]

endings = [
    "Little did they know, this was just the beginning of an epic tale.",
    "The consequences of their actions would ripple through time.",
    "From that moment on, nothing would ever be the same.",
    "It was a turning point that would shape the future of humanity.",
    "And so, a new chapter in history was written.",
    "The world held its breath, waiting to see what would happen next.",
    "As one adventure ended, another loomed on the horizon.",
    "The true impact of their discovery would not be known for generations.",
    "In the end, they realized that the journey had changed them profoundly.",
    "The stage was set for a conflict that would determine the fate of all.",
    "Questions were answered, but even more mysteries emerged.",
    "They stood at the threshold of a new era, filled with both hope and uncertainty.",
    "The boundaries between myth and reality had been forever blurred.",
    "As they looked to the future, they knew their lives would never be ordinary again.",
    "The echoes of their actions would resonate through the cosmos for eons to come."
]


def generate_story():
    num_paragraphs = random.randint(3, 5)
    story = ""

    for i in range(num_paragraphs):
        if i == 0:
            paragraph = random.choice(beginnings) + " " + random.choice(middles)
        elif i == num_paragraphs - 1:
            paragraph = random.choice(developments) + " " + random.choice(endings)
        else:
            paragraph = random.choice(developments) + " " + random.choice(middles)

        story += paragraph + "\n\n"

    return story.strip()


def create_pdf(filename, story):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    styles = getSampleStyleSheet()
    style = styles['Normal']

    # Create a frame for the text
    frame = Frame(inch, inch, width - 2 * inch, height - 2 * inch, showBoundary=0)

    # Create a paragraph with the story
    story_para = Paragraph(story.replace("\n", "<br/><br/>"), style)

    # Draw the story on the PDF
    frame.addFromList([story_para], c)

    c.save()


# Generate 5 PDF files
for i in range(5):
    story = generate_story()
    filename = f"story_{i + 1}.pdf"
    create_pdf("data_store/"+filename, story)
    print(f"Generated {filename}")

print("All PDFs generated successfully!")