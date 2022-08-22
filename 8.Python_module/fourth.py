"""
Let’s break that down a little bit.

The recognize_speech_from_mic() function takes a Recognizer and Microphone instance as arguments and returns a dictionary with three keys. The first key, "success", is a boolean that indicates whether or not the API request was successful. The second key, "error", is either None or an error message indicating that the API is unavailable or the speech was unintelligible. Finally, the "transcription" key contains the transcription of the audio recorded by the microphone.

The function first checks that the recognizer and microphone arguments are of the correct type, and raises a TypeError if either is invalid:

if not isinstance(recognizer, sr.Recognizer):
    raise TypeError('`recognizer` must be `Recognizer` instance')

if not isinstance(microphone, sr.Microphone):
    raise TypeError('`microphone` must be a `Microphone` instance')
The listen() method is then used to record microphone input:

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
The adjust_for_ambient_noise() method is used to calibrate the recognizer for changing noise conditions each time the recognize_speech_from_mic() function is called.

Next, recognize_google() is called to transcribe any speech in the recording. A try...except block is used to catch the RequestError and UnknownValueError exceptions and handle them accordingly. The success of the API request, any error messages, and the transcribed speech are stored in the success, error and transcription keys of the response dictionary, which is returned by the recognize_speech_from_mic() function.

response = {
    "success": True,
    "error": None,
    "transcription": None
}

try:
    response["transcription"] = recognizer.recognize_google(audio)
except sr.RequestError:
    # API was unreachable or unresponsive
    response["success"] = False
    response["error"] = "API unavailable"
except sr.UnknownValueError:
    # speech was unintelligible
    response["error"] = "Unable to recognize speech"

return response
You can test the recognize_speech_from_mic() function by saving the above script to a file called “guessing_game.py” and running the following in an interpreter session:

>>> import speech_recognition as sr
>>> from guessing_game import recognize_speech_from_mic
>>> r = sr.Recognizer()
>>> m = sr.Microphone()
>>> recognize_speech_from_mic(r, m)
{'success': True, 'error': None, 'transcription': 'hello'}
>>> # Your output will vary depending on what you say
The game itself is pretty simple. First, a list of words, a maximum number of allowed guesses and a prompt limit are declared:

WORDS = ['apple', 'banana', 'grape', 'orange', 'mango', 'lemon']
NUM_GUESSES = 3
PROMPT_LIMIT = 5
Next, a Recognizer and Microphone instance is created and a random word is chosen from WORDS:

recognizer = sr.Recognizer()
microphone = sr.Microphone()
word = random.choice(WORDS)
After printing some instructions and waiting for 3 three seconds, a for loop is used to manage each user attempt at guessing the chosen word. The first thing inside the for loop is another for loop that prompts the user at most PROMPT_LIMIT times for a guess, attempting to recognize the input each time with the recognize_speech_from_mic() function and storing the dictionary returned to the local variable guess.

If the "transcription" key of guess is not None, then the user’s speech was transcribed and the inner loop is terminated with break. If the speech was not transcribed and the "success" key is set to False, then an API error occurred and the loop is again terminated with break. Otherwise, the API request was successful but the speech was unrecognizable. The user is warned and the for loop repeats, giving the user another chance at the current attempt.

for j in range(PROMPT_LIMIT):
    print('Guess {}. Speak!'.format(i+1))
    guess = recognize_speech_from_mic(recognizer, microphone)
    if guess["transcription"]:
        break
    if not guess["success"]:
        break
    print("I didn't catch that. What did you say?\n")
Once the inner for loop terminates, the guess dictionary is checked for errors. If any occurred, the error message is displayed and the outer for loop is terminated with break, which will end the program execution.

if guess['error']:
    print("ERROR: {}".format(guess["error"]))
    break
If there weren’t any errors, the transcription is compared to the randomly selected word. The lower() method for string objects is used to ensure better matching of the guess to the chosen word. The API may return speech matched to the word “apple” as “Apple” or “apple,” and either response should count as a correct answer.

If the guess was correct, the user wins and the game is terminated. If the user was incorrect and has any remaining attempts, the outer for loop repeats and a new guess is retrieved. Otherwise, the user loses the game.

guess_is_correct = guess["transcription"].lower() == word.lower()
user_has_more_attempts = i < NUM_GUESSES - 1

if guess_is_correct:
    print('Correct! You win!'.format(word))
    break
elif user_has_more_attempts:
    print('Incorrect. Try again.\n')
else:
    print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
    break
When run, the output will look something like this:

I'm thinking of one of these words:
apple, banana, grape, orange, mango, lemon
You have 3 tries to guess which one.

Guess 1. Speak!
You said: banana
Incorrect. Try again.

Guess 2. Speak!
You said: lemon
Incorrect. Try again.

Guess 3. Speak!
You said: Orange
Correct! You win!
"""

import time

import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    word = random.choice(WORDS)

    # format the instructions string
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        if guess_is_correct:
            print("Correct! You win!".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            break