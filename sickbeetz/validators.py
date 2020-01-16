from django.core.exceptions import ValidationError
import magic


def validate_file_type(file):
    if 'WAVE audio' not in magic.from_buffer(file.read(2048)):
        raise ValidationError(u'Unsupported file type.')
