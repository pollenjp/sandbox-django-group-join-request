# Third Party Library
import rules


@rules.predicate
def is_request_post_owner(user, request_post):
    return user == request_post.created_by


@rules.predicate
def has_view_all_request_post_permission(user):
    return user.has_perm("join_request.view_all_request_post")


@rules.predicate
def has_approve_request_post_permission(user):
    return user.has_perm("join_request.approve_request_post")


rules.add_perm(
    "join_request.rules_view_all_request_post",
    has_view_all_request_post_permission,
)

rules.add_perm(
    "join_request.rules_view_request_post_detail",
    is_request_post_owner | has_view_all_request_post_permission,
)

rules.add_perm(
    "join_request.rules_approve_request_post",
    has_approve_request_post_permission,
)
