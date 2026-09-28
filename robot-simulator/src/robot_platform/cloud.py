"""Single-process, isolated visitor entry point for a TLS-terminating host."""
import os
from urllib.parse import urlsplit

from .visitor_api import VisitorRegistry, create_personal_app


def _bounded_int(name, default, minimum, maximum):
    value = int(os.environ.get(name, default))
    if not minimum <= value <= maximum:
        raise ValueError(f'{name} must be between {minimum} and {maximum}')
    return value


def public_origins():
    configured = os.environ.get('ROBOT_PUBLIC_ORIGINS', '').strip()
    if not configured:
        domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN', '').strip()
        configured = f'https://{domain}' if domain else ''
    origins = tuple(x.strip() for x in configured.split(',') if x.strip())
    if not origins:
        raise ValueError('Set ROBOT_PUBLIC_ORIGINS to the simulator HTTPS origin before starting.')
    for origin in origins:
        parts = urlsplit(origin)
        if (parts.scheme != 'https' or not parts.hostname or parts.username or parts.password
                or parts.path or parts.query or parts.fragment or '*' in origin):
            raise ValueError('ROBOT_PUBLIC_ORIGINS must contain exact HTTPS origins without paths.')
        try:
            parts.port
        except ValueError as error:
            raise ValueError('Invalid port in ROBOT_PUBLIC_ORIGINS') from error
    return origins


def create_cloud_app():
    origins = public_origins()
    registry = VisitorRegistry(
        ttl=_bounded_int('ROBOT_VISITOR_TTL_SECONDS', 1800, 300, 14400),
        key_ttl=_bounded_int('ROBOT_KEY_TTL_SECONDS', 1800, 60, 1800),
        max_visitors=_bounded_int('ROBOT_MAX_VISITORS', 2, 1, 8),
        initial_template='multifloor-cargo',
    )
    return create_personal_app(registry=registry, origins=origins)


def main():
    import uvicorn
    # The container port must be reachable only through the host's HTTPS proxy.
    # Keep one worker/replica: sessions and credentials live in process memory.
    uvicorn.run('robot_platform.cloud:create_cloud_app', factory=True,
                host='0.0.0.0', port=_bounded_int('PORT', 8000, 1, 65535),
                workers=1, proxy_headers=True,
                forwarded_allow_ips=os.environ.get('FORWARDED_ALLOW_IPS', '127.0.0.1'),
                timeout_graceful_shutdown=15)


if __name__ == '__main__':
    main()
