# -*- coding: utf-8 -*-


def set_permissions(annotation):
    """Set the given annotation's permissions according to its group."""
    # If this annotation doesn't have a permissions field, we don't know how to
    # handle it and should bail.
    permissions = annotation.get('permissions')
    if permissions is None:
        return

    # For private annotations (visible only to the user who created them) the
    # client sends just the user's ID in the read permissions.
    is_private = (permissions.get('read') == [annotation['user']])

    if is_private:
        # The groups feature doesn't change the permissions for private
        # annotations at all.
        return

    group = annotation.get('group')
    if group == '__world__':
        # The groups feature doesn't change the permissions for annotations
        # that don't belong to a group.
        return

    group_principal = 'group:' + group

    # If the annotation belongs to a group, we make it so that only users who
    # are members of that group can read the annotation.
    annotation['permissions']['read'] = [group_principal]


def group_principals(user):
    """Return any 'group:<pubid>' principals for the given user.

    Return a list of 'group:<pubid>' principals for the groups that the given
    user is a member of.

    :param user: the authorized user, as a User object
    :type user: h.accounts.models.User

    :rtype: list of strings

    """
    principals = ['group:__world__']

    principals.extend(['group:{pubid}'.format(pubid=group.pubid)
                       for group in user.groups])

    return principals
