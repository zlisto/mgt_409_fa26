# Peabody visitor-ops mock (Fall 2026)

Internal briefing for the course assignment. This pack imitates how a museum
might expose **hours/ticketing**, **exhibits**, and **visitor policy** as
separate MCP tools. Gallery names and public hours are inspired by
[peabody.yale.edu](https://peabody.yale.edu). Membership events, bag rules,
and photography rules in the JSON files are **course fiction**.

## Why three tools

Front-desk staff, exhibit teams, and visitor services do not share one
document. An agent that reads only one tool will sound confident and still
be wrong. Your job is to wrap the feeds as an MCP server, then put an
**orchestrator** in front that calls the tools it needs for a complex
question — and refuses to invent a compromise when two tools disagree.

## What to watch for

The exhibits feed and the visitor-policy handbook are maintained by
different desks. They are not guaranteed to agree. If two tools disagree,
the orchestrator should refuse rather than invent a blended policy.
