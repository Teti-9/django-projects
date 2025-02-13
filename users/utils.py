def usuario(request):
    return getattr(request.user, "id", None) or request.session.get("user_id")