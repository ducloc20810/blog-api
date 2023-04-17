from main.models.post import Post
from main.models.tag import Tag
from main.db import db
from main.schemas.post import CreatePostSchema
from main.libs.post import extract_tags
from .tag import get_tag_by_name


def get_posts_pagination(offset: int, limit: int):
    posts = db.session.query(Post).order_by("id").offset(offset).limit(limit)
    return posts


def create_new_post(data: CreatePostSchema, author_id: int):
    post = Post(
        title=data.title,
        content=data.content,
        category_id=data.category_id,
        author_id=author_id,
    )

    extracted_tags = extract_tags(data.content)

    for tag in extracted_tags:
        exists_tag = get_tag_by_name(tag)
        if exists_tag is None:
            new_tag = Tag(name=tag)
            db.session.add(new_tag)
            post.tags.append(new_tag)
        else:
            post.tags.append(exists_tag)

    db.session.add(post)
    db.session.commit()
    return post
