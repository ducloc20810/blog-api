from main.models.post import Post
from main.models.tag import Tag
from main.db import db
from main.schemas.post import CreatePostSchema, UpdatePostSchema
from main.libs.post import extract_tags
from main.libs.common import update_schema_data
from .tag import get_tag_by_name, update_tag_from_post_content


def get_posts_pagination(offset: int, limit: int):
    posts = db.session.query(Post).order_by("id").offset(offset).limit(limit)
    return posts


def get_post_by_id(post_id: int) -> Post:
    return Post.query.filter(Post.id == post_id).one_or_none()


def create_new_post(data: CreatePostSchema, author_id: int):
    post = Post(
        title=data.title,
        content=data.content,
        category_id=data.category_id,
        author_id=author_id,
    )

    update_tag_from_post_content(post_content=data.content, post=post)

    db.session.add(post)
    db.session.commit()
    return post


def check_post_owner(user_id: int, post_id: int) -> bool:
    post = get_post_by_id(post_id)
    if post is None:
        return False

    return post.author_id == user_id


def update_post_with_id(post_id: int, data: UpdatePostSchema):
    post = get_post_by_id(post_id)

    if post is None:
        return None

    updated_data = update_schema_data(post, data)

    if data.content is not None:
        update_tag_from_post_content(post_content=data.content, post=post)

    db.session.commit()
    return updated_data
