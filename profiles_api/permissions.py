from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  # BasePermission provided by DRF for us to create custom permission
  """Allow user to edit their own profile"""


  # get called everytime a request is made to the api we assign the function to
  def has_object_permission(self, request, view, obj):
    """Check user is trying to edit their own profile"""
    # SAFE_METHODS eg. get(), post()
    if request.method in permissions.SAFE_METHODS:
      return True
    
    # if put, etc, all modifying methods
    return obj.id == request.user.id