"""CR7 full-body battle sprite adapted from the user's latest reference image.
56x56 pixels, four Game Boy grayscale tones, with the complete celebration pose.
"""
import base64
import zlib
PIXELS = "eNq9louywiAMRLub//9nyQMurS0m6FwcnVF7uiHZhB7HzxfYFuqY2CqDlD1Q0BY3OOoG61zLiaLCajbbCyr5P9xh1UM1zOBYr5+G2bKyYRgtQtlpSlkdapLmMqt7yWrdnI3Vdx4LqfhAvoU41PKR+t5kWsxmUk5YRpAudZb77FI111mr7Vb9vTKWzqLWBJcIYU7Fen6ZKXnJiP7Oj5QKDvIYHJ4cYrXWv69yHv49aHqx+5v8W7qeuLg77+rWzHZfRMjATPlab3mc+sCEBctzAlaedoJv84UrDl3NwrpwUZXHznODut4c6MIzMjZmgkz2LN0serX0jaY4P7v0YpWWJIfg6K6xb0geJt2k0VO5c8UnUg9OBVkA+67gPZVMqQ8zN2MMtsLJEDJz2Klooz3gYaNyQMztUXlawmS9tODfcE+7pgeKeYQgH+ic4XykwHwTJIv4lN6dh9EdQflCkJuCO3o6Qn7xsP8CWgwHBg=="
def cr7_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y * 56:(y + 1) * 56]) for y in range(56)]
