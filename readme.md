# Voice Gender

simple voice gender recognition

## install

    pip install voice-gender
    
## Usage

```python
from voice_gender import GenderIdentifier

my_file = "test.wav"

gender = GenderIdentifier.predict(my_file)

if gender == "female":
    print("female speaker")
elif gender == "male":
    print("male speaker")
```