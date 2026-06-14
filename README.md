# Relay

**Your Claude Code becomes Relay** -- a staff engineer thinking partner that listens before proposing.

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

Relay reads your code itself. Asks you the one question that unlocks the rest. Recommends with reasoning, not with code-first momentum. Only writes code after you say go.

## No hidden session state

Relay keeps the live conversation as the source of truth. It does not create sessions, decisions logs, summaries, task logs, phase files, diagrams, or transcripts unless you explicitly ask for that artifact.

Existing `.relay` folders can stay on disk. Relay ignores them by default.

## Local-first, no cloud

- No telemetry. No analytics. No phone-home.
- No account, no signup, no email required.
- No automatic repo-local memory files.

## How it works

One piece, bundled in this plugin:

1. **Output style** (`prompts/relay-planner.md`) -- the behavioral contract that shapes how Claude responds.

After installing, select it once with `/output-style` and pick **Relay Planner**. That's the entire plugin: a single prompt file, no hooks, no scripts.

## Why "Relay"

A relay carries the thread forward. It helps you slow down, clarify the goal, and choose the right next step before code changes.

## Built by

[Basegraph](https://basegraph.co).

**Touchbase** is what we're building next -- the final work app. Slack, Linear, and Notion replaced by one native macOS app where humans and agents work together.

Stealth, invite-only at launch — we're showing it to a handful of people genuinely curious about what comes after Slack and Linear. If that's you, [book a call](https://cal.com/nithinsj) or [drop your email](https://basegraph.co/plugin) and we'll let you know when it ships.

Relay's free because every Claude Code user deserves a thinking partner.

## Contributing

Issues and PRs welcome. The plugin is intentionally tiny. Most contributions will be to the output style itself (`prompts/relay-planner.md`), which is just a markdown file describing how Claude should think.

## License

MIT
