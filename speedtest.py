# speed test
import random,time
def get_random_sentence():
    sample_sentences = [
        "CodersCave is a project-based learning organization dedicated to shaping a strong tech future for all developers.",
        "We believe that practical knowledge is key to success in the tech industry, and our aim is to help individuals develop the personal and professional skills they need to excel in their careers.",
        "Our programs are designed for students who are interested in starting a career in a technical field but lack basic knowledge.",
        "At CodersCave, we support students in acquiring new skills by providing opportunities for hands-on learning through live projects and real-world examples."
    ]
    return random.choice(sample_sentences)

def calc_typing_speed(start_time, end_time, text_typed):
    total_time = end_time - start_time
    words = text_typed.split()
    word_count = len(words)
    wpm = (word_count / total_time) * 60
    return wpm

def main():
    print("Test your typing speed!")
    input("Press Enter to start...")

    text_to_type = get_random_sentence()
    print("Type the following text:")
    print(text_to_type)

    input("Press Enter when you're ready to start typing...")

    start_time = time.time()

    text_typed = input("Start typing: ")

    end_time = time.time()

    wpm = calc_typing_speed(start_time, end_time, text_typed)
    print(f"Your typing speed: {wpm:.2f} WPM")
    accuracy = sum(1 for a, b in zip(text_to_type, text_typed) if a == b) / max(len(text_to_type), len(text_typed)) * 100
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
