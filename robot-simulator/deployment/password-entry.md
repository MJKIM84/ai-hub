# Password-protected simulator entry

The launcher uses the label **시뮬레이션 시작하기**. A password form authenticates on the server before a runtime is allocated or its URL is returned. This is a shared entry password, not an administrative permission system inside the simulator.

- `ROBOT_ACCESS_PASSWORD_HASH`: server-only salted scrypt verifier (`scrypt:<16-byte salt hex>:<64-byte derived key hex>`).
- `ROBOT_ACCESS_SECRET`: separate 32-byte random signing key, encoded as hex. Never commit either value.
- Access cookies are HttpOnly, Secure, SameSite=Strict, bound to the browser identity, expire after 30 minutes and are invalidated by a verifier change.
- Vercel firewall rule `Simulator password attempts`: POST `/api/access`, 6 requests per IP per 600 seconds, HTTP 429. Counters are regional; this is not a guarantee against distributed guessing. A longer password remains preferable for an internet-facing service.
- Runtime entry uses a 90-second, single-use signed handoff scoped to a specific runtime. It travels in a URL fragment, is removed before API exchange, and is never a reusable administrator password. The runtime sets its own secure HttpOnly cookie.
- `ROBOT_ENTRY_REQUIRED=1` requires a per-runtime signing key. The launcher supplies it at boot, not in the snapshot. Unauthenticated direct runtime requests cannot allocate visitor state, read APIs, load app assets or control physics. Health checks alone remain public.
- No password, verifier, signing key, ticket or access cookie is logged or placed in public HTML/JS, browser storage, Git or build images.
- Changing the launcher code also requires a runtime snapshot containing `entry_gate.py`. Keep the approved source revision and snapshot paired during rollout.

Validation: Node access/session tests plus Python entry-gate/cloud/visitor tests cover absent configuration, wrong password, forged/expired or cross-browser cookies, cross-origin requests, direct API access, single-use ticket replay, different-runtime tickets and successful visitor initialization. Live verification separately checks the password form and successful protected entry. These checks do not establish hardware safety or rerun the full cargo scenario.

Existing anonymous runtimes created before this change keep their earlier protection until they stop or expire (maximum 30 minutes). Deployment verification must check that none remain active; do not quietly discard an in-progress user's work to migrate it.
