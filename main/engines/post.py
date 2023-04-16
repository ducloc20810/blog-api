from main.models.post import Post
from main.db import db


def get_posts_pagination(offset, limit):
    posts = db.session.query(Post).order_by("id").offset(offset).limit(limit)
    return posts
