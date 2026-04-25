# Relay

**Your Claude Code becomes Relay** — a staff engineer thinking partner that listens before proposing, and captures the decisions in your repo.

*Built by [Basegraph](https://basegraph.co) — we're also building Touchbase, the final work app. (Stealth)*

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

[Basegraph](https://basegraph.co).

**Touchbase** is what we're building next — the final work app. Slack, Linear, and Notion replaced by one native macOS app where humans and agents work together. You open it and it already knows: yesterday's decisions captured with the reasoning, the hallway conversation routed to the right work item, what's waiting on you sitting on top. Decisions become reminders become actions, automatically.

Stealth, invite-only at launch — we're showing it to a handful of people genuinely curious about what comes after Slack and Linear. If that's you, [book a call](https://cal.com/nithinsj) or [drop your email](https://basegraph.co/plugin) and we'll let you know when it ships.

Relay's free because every Claude Code user deserves a thinking partner.

## Contributing

Issues and PRs welcome. The plugin is intentionally tiny — most contributions will be to the output style itself (`prompts/relay-planner.md`), which is just a markdown file describing how Claude should think.

## License

MIT
