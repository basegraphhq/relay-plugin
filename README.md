# Relay

**Your Claude Code becomes Relay** — a staff engineer thinking partner that listens before proposing, and captures the decisions in your repo.

## Install

```
/plugin marketplace add basegraphhq/relay-plugin
/plugin install relay@basegraph
```

That's it. No accounts, no API keys, no servers.

## What changes

**Without Relay:**

> *"Add rate limiting to the API."*
> "I'll add rate limiting using express-rate-limit. Here's the diff..." [writes 200 lines]

**With Relay:**

> *"Add rate limiting to the API."*
> "What's driving this — abuse you've seen, or a precaution? And what's the failure mode you care about: 429s with retry headers, or just dropping the requests?"

Relay reads your code itself. Asks you the one question that unlocks the rest. Recommends with reasoning, not with code-first momentum. Only writes after you say go.

## Decisions live in your repo

When you make a call together — *"we'll use Postgres advisory locks instead of Redis"* — Relay writes it to `.relay/sessions/<session>/decisions.jsonl` with the reasoning, alternatives, and context. Commit it. Your teammate pulls; their Claude has your decisions; nobody re-litigates the same architecture call in code review.

```
.relay/
└── sessions/
    └── session-nithin-1777737600/
        ├── session.json       # who, when, current phase
        ├── decisions.jsonl    # one decision per line
        ├── summary.md         # current shared understanding
        └── transcript.jsonl   # full conversation log
```

## Local-first, no cloud

- No telemetry. No analytics. No phone-home.
- No account, no signup, no email required.
- Decisions never leave your machine unless you `git push` them.
- Identity (`~/.relay/identity.json`) is local-only and managed by you.

## How it works

Two pieces, both bundled in this plugin:

1. **Output style** (`prompts/relay-planner.md`) — the behavioral contract that shapes how Claude responds. Auto-injected at session start via a hook, so you never have to pick it manually.
2. **Stop hook** (`hooks/stop.py`) — copies the session transcript into `.relay/sessions/` when a session ends, alongside the decisions.

That's the entire plugin. ~50 lines of Python, one prompt file. Read all of it in five minutes.

## Why "Relay"

A relay carries something forward. Your decisions, your reasoning, your context — carried from session to session, from teammate to teammate, in the repo itself. Not in a cloud you have to trust, not in a SaaS that disappears in two years.

## Built by

[Basegraph](https://basegraph.co) — building the engineer for every department.

We make Relay free because we think every Claude Code user deserves a thinking partner. If you want to know what we're building next, drop your email at [basegraph.co/relay](https://basegraph.co/relay).

## Contributing

Issues and PRs welcome. The plugin is intentionally tiny — most contributions will be to the output style itself (`prompts/relay-planner.md`), which is just a markdown file describing how Claude should think.

## License

MIT
