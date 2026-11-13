# SPDX-FileCopyrightText: 2026-present Context.dev
#
# SPDX-License-Identifier: Apache-2.0

from haystack import Pipeline

from haystack_integrations.components.websearch.context import ContextWebSearch

pipeline = Pipeline()
pipeline.add_component("search", ContextWebSearch(top_k=5, include_markdown=True))

result = pipeline.run({"search": {"query": "What is Haystack by deepset?"}})
for document in result["search"]["documents"]:
    print(document.meta["url"])
