from main.models.tag import Tag


def get_tag_by_name(tag_name):
    return Tag.query.filter(tag_name == Tag.name).one_or_none()
