"""Jeff Bezos full-body battle sprite with crossed arms, 56x56 Game Boy shades."""
import base64
import zlib
PIXELS = "eNqtlkkWwzAIQy10/zvXDHbsVVFevGizyK9AIjRjfH4AvKPwgixCBtf9poGw7A9+IRyzSZg3qAlauaJyZWWIapjh+FbDc8y09LxOPXqsauX8nDHRzUiCrmXyXEeFsl405qYQGhWD5t/sS+btE6TlabcWcjDCeWvWutSm3FtuXvkHulZ6iaHFfn8xJtniEMosJods8R2OG9RiyNtJFtaemIJUbB7H3M/glUfBHlM1jjs7amPN7SdEuZ1DW++JQBYsLgzVOFL1E9eQydxQ26vA14RrnMctFlplDlUwXTkCEcsMQUocea02wc7riRKm7Fo2fVuWRJ/DxeXMQEpBczS3+7OimoUinrqTYyeJ7O7YRWCnQzC3Ju6l8fdvHrkYcFXA+5e0l7WvXvZ/w2IFQA=="
def jeff_bezos_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y*56:(y+1)*56]) for y in range(56)]
