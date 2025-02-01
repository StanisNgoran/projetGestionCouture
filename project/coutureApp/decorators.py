from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def role_requis(role_autorise):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'profil') and request.user.profil.role == role_autorise:
                return view_func(request, *args, **kwargs)
            else:
                # messages.error(request, "Vous n'avez pas l'autorisation d'accéder à cette page.")
                return redirect('homeUser')  # Redirection si l'accès est refusé
        return _wrapped_view
    return decorator
