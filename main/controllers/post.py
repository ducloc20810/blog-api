from flask import Blueprint, request
from main.engines.post import get_posts_pagination
from main.schemas.comment import (
    CommentResponseSchemaWithReplies,
    CommentRequestSchema,
    ReplyResponseSchema,
)
from main.libs.common import to_response
from main.schemas.post import PostResponseSchema, CreatePostSchema, UpdatePostSchema
from main.common.decorators import require_access_token, parse_args_with
from main.engines.post import (
    create_new_post,
    check_post_owner,
    update_post_with_id,
    check_user_liked_post,
    get_post_by_id,
    get_comment_by_id,
    user_commend_to_post,
    user_reply_comment,
)
from main.db import db

post = Blueprint("post", __name__)


@post.get("/posts")
def get_posts():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))
    posts = get_posts_pagination(offset=offset, limit=limit)

    for post in posts:
        post.comments = [
            comment for comment in post.comments if comment.parent_id is None
        ]

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


@post.post("/posts/<id>/like")
@require_access_token
def like_post(id, **kwargs):
    user = kwargs["user"]
    post = get_post_by_id(id)

    if post is None:
        return {"message": "Post not found"}, 404

    if check_user_liked_post(user, post):
        post.liked_users.remove(user)
    else:
        post.liked_users.append(user)

    db.session.commit()

    return {}, 200


@post.post("/posts/<id>/comments")
@require_access_token
@parse_args_with(CommentRequestSchema)
def commend_post(id, args, **kwargs):
    user = kwargs["user"]
    post = get_post_by_id(id)

    if post is None:
        return {"message": "Post not found"}, 404

    comment = user_commend_to_post(user, post, args.content)

    return {
        "comment": to_response(
            schema=CommentResponseSchemaWithReplies, clsObject=comment
        )
    }


@post.post("/posts/<post_id>/comments/<comment_id>/replies")
@require_access_token
@parse_args_with(CommentRequestSchema)
def reply_comment(post_id, comment_id, args, **kwargs):
    user = kwargs["user"]
    post = get_post_by_id(post_id)
    comment = get_comment_by_id(comment_id)

    if post is None:
        return {"message": "Post not found"}, 404

    if comment is None:
        return {"message": "Comment not found"}, 404

    reply = user_reply_comment(user, comment, args.content)

    return {"reply": to_response(schema=ReplyResponseSchema, clsObject=reply)}
