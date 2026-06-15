# Security Policy

## Reporting A Vulnerability

Please use GitHub private vulnerability reporting if available, or contact the repository owner through their preferred GitHub profile channel.

Do not open a public issue with exploit details before the maintainer has had time to review the report.

## Scope

This action installs `codex-maintainer-kit`, reads the checked-out repository, writes generated Markdown/JSON files, and optionally uploads them as workflow artifacts.

Security-sensitive changes should pay attention to:

- avoiding secret reads
- avoiding token logging
- keeping generated files as review artifacts rather than auto-merged changes
- pinning or overriding `kit-ref` intentionally
