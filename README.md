# Context.dev for Haystack

[![PyPI](https://img.shields.io/pypi/v/context-dev-haystack)](https://pypi.org/project/context-dev-haystack/)
[![Python](https://img.shields.io/pypi/pyversions/context-dev-haystack)](https://pypi.org/project/context-dev-haystack/)
[![Test](https://github.com/context-dot-dev/context-haystack/actions/workflows/test.yml/badge.svg)](https://github.com/context-dot-dev/context-haystack/actions/workflows/test.yml)
[![License](https://img.shields.io/github/license/context-dot-dev/context-haystack)](LICENSE)

Haystack components for live web search, webpage and YouTube transcript retrieval, and bounded website crawling with [Context.dev](https://context.dev).

## Installation

```bash
pip install context-dev-haystack
```

Create an API key in the [Context.dev dashboard](https://context.dev/dashboard/api-keys), then export it:

```bash
export CONTEXT_API_KEY="your-api-key"
```

## Components

| Component | Purpose | Import |
| --- | --- | --- |
| `ContextWebSearch` | Search the live web and return ranked Haystack Documents and source links | `haystack_integrations.components.websearch.context` |
| `ContextFetcher` | Fetch webpages or YouTube videos as clean Markdown Documents | `haystack_integrations.components.fetchers.context` |
| `ContextCrawler` | Crawl websites into Documents with explicit page and depth limits | `haystack_integrations.components.fetchers.context` |

All components support both `run()` and `run_async()`, Haystack serialization, custom timeouts, and retry configuration.

## Search the live web

```python
from haystack_integrations.components.websearch.context import ContextWebSearch

search = ContextWebSearch(top_k=5, include_markdown=True)
result = search.run(query="Recent advances in retrieval-augmented generation")

documents = result["documents"]
links = result["links"]
```

Use `include_domains`, `exclude_domains`, `freshness`, and `country` to constrain results. Extra Context.dev Search API fields can be supplied through `search_params`.

## Fetch webpages or YouTube transcripts

```python
from haystack_integrations.components.fetchers.context import ContextFetcher

fetcher = ContextFetcher()
result = fetcher.run(
    urls=[
        "https://haystack.deepset.ai",
        "https://www.youtube.com/watch?v=UF8uR6Z6KLc",
    ]
)

documents = result["documents"]
```

Each URL becomes a Haystack `Document`. Webpages contain clean Markdown and page metadata; supported YouTube URLs return timestamped transcript Markdown.

## Crawl a website

```python
from haystack_integrations.components.fetchers.context import ContextCrawler

crawler = ContextCrawler(crawl_params={"maxPages": 25, "maxDepth": 2})
result = crawler.run(urls=["https://docs.haystack.deepset.ai"])

documents = result["documents"]
```

`ContextCrawler` defaults to one page to prevent accidental credit consumption. Set `maxPages` explicitly for larger crawls.

## Async usage

```python
result = await search.run_async(query="Haystack agents")
documents = result["documents"]
```

The fetcher and crawler process multiple input URLs concurrently in their async methods.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for the Hatch-based development and release workflow.

## License

Apache-2.0. See [LICENSE](LICENSE).
