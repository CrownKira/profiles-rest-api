from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    # BasePermission provided by DRF for us to create custom permission
    """Allow user to edit their own profile"""

    # life cycle method
    # gets called everytime a request is made to the api we assign the function to
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # SAFE_METHODS eg. get(), post()
        if request.method in permissions.SAFE_METHODS:
            return True

        # if put, etc, all modifying methods
        # the header must have the authentication
        # retrieve the user id from the authentication token
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
