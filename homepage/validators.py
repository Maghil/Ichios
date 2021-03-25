from django.core.exceptions import ValidationError
import fleep

def validateSoundAssets(value):
    if not "wav" in value:
        raise ValidationError("A valid school email must be entered in")
    else:
        return value

    # with open(value, "rb") as file:
    #     info = fleep.get(file.read(128))

    #     print(info.type)
    #     print(info.extension) 
    #     print(info.mime)
