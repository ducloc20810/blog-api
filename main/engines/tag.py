from main.models.tag import Tag
from main.models.post import Post
from main.libs.post import extract_tags
from main.db import db


def get_tag_by_name(tag_name):
    return Tag.query.filter(tag_name == Tag.name).one_or_none()


def update_tag_from_post_content(post_content: str, post: Post):
    extracted_tags = extract_tags(post_content)

    for tag in extracted_tags:
        exists_tag = get_tag_by_name(tag)
        if exists_tag is None:
            new_tag = Tag(name=tag)
            db.session.add(new_tag)
            post.tags.append(new_tag)
        else:
            post.tags.append(exists_tag)
