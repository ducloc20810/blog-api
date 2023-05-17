from flask import Blueprint, request
from main.engines.post import get_posts_pagination
from main.libs.common import to_response
from main.schemas.post import PostResponseSchema, CreatePostSchema, UpdatePostSchema
from main.common.decorators import require_access_token, parse_args_with
from main.engines.post import (
    get_post_by_id,
    create_new_post,
    check_post_owner,
    update_post_with_id,
    check_user_liked_post,
)
from main.db import db

post = Blueprint("post", __name__)


@post.get("/posts")
def get_posts():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))
    posts = get_posts_pagination(offset=offset, limit=limit)

    response = []

    for post in posts:
        response.append(to_response(schema=PostResponseSchema, clsObject=post))

    return {"total_items": len(response), "items": response}


@post.post("/posts")
@require_access_token
@parse_args_with(CreatePostSchema)
def create_post(args, **kwargs):
    user = kwargs["user"]
    new_post = create_new_post(data=args, author_id=user.id)

    return {"post": to_response(schema=PostResponseSchema, clsObject=new_post)}, 200


@post.put("/posts/<id>")
@require_access_token
@parse_args_with(UpdatePostSchema)
def update_post(id, args, **kwargs):
    user = kwargs["user"]

    if check_post_owner(user_id=user.id, post_id=id) is False:
        return {"message": "You do not have permission to update this post"}, 403

    updated_post = update_post_with_id(post_id=id, data=args)

    return {"post": to_response(schema=PostResponseSchema, clsObject=updated_post)}, 200
