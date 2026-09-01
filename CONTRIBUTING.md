# Contributing

Thanks for contributing to the Context.dev Haystack integration.

## Setup

This project uses [Hatch](https://hatch.pypa.io/) for environments, formatting, tests, and builds.

```bash
pip install hatch
hatch --version
```

## Checks

Run the same checks used by CI before opening a pull request:

```bash
hatch run fmt-check
hatch run test:types
hatch run test:unit
hatch run test:cov
```

Integration tests call the live Context.dev API and consume credits. They are skipped unless `CONTEXT_API_KEY` is set:

```bash
export CONTEXT_API_KEY="your-api-key"
hatch run test:integration
```

## Pull requests

Keep changes focused, add tests for behavior changes, and use Conventional Commit titles such as `feat: add a component option` or `fix: preserve response metadata`.

## Releases

Maintainers publish releases by pushing a semantic version tag such as `v0.1.0`. The release workflow builds the source distribution and wheel, then publishes both to PyPI.
