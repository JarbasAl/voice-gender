# Voice Gender

simple voice gender recognition, GMMs trained on [Free ST American English Corpus](https://www.openslr.org/45/)

## install

    pip install voice-gender
    
## Usage

```python
from voice_gender import GenderClassifier

my_file = "test.wav"

gender = GenderClassifier.predict(my_file)

if gender == "female":
    print("female speaker")
elif gender == "male":
    print("male speaker")
```