class ProviderError(ValueError):
    """Safe, user-facing provider failure (never raw credential or response bodies)."""
