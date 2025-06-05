from django.shortcuts import redirect
from functools import wraps

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or request.user.role != role:
                return redirect('no_access')  # или показывай сообщение
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
