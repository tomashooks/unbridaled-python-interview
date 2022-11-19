from sqlalchemy.exc import IntegrityError


def integrity_error_formatter(e: IntegrityError):
    return str(e.orig).split(':')[-1].replace('\n', '').strip()
