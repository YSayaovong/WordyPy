# This cell has the tests your Letter class should pass in order to
# be evaluated as correct. Some of the tests you can see here and
# try on your own (press the button labeled validate on the toolbar).
# Others are hidden from your view, and will be evaluated only when
# you submit to the autograder.

# Check if the Letter class exists
assert "Letter" in dir(), "The Letter class does not exist, did you define it?"

# Check to see if the Letter class can be created
l: Letter
try:
    l = Letter("s")
except:
    assert (
        False
    ), "Unable to create a Letter object with Letter('s'), did you correctly define the Letter class?"

# Check to see if the Letter class has the in_correct_place attribute
assert hasattr(
    l, "in_correct_place"
), "The letter object created has no in_correct_place attribute, but this should be False by default. Did you create this attribute?"
