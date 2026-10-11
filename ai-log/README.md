# Conversation exports

The work ran as one orchestrating Claude Code session plus several sub-agents and Codex sessions
working in parallel, so a single `/export` of one chat would show only a fraction of it. These
files are exported from the sessions' own log files (the same data `/export` reads), one file per
session, in the order the work happened.

- `01-orchestrator.md` — the main conversation: planning, briefs, reviews, decisions. Mostly in
  Russian (my working language). Tool outputs and automatically injected context are left out,
  private details are replaced by `[redacted: …]` markers; nothing else is edited.
- `0N-agent-*.md` — Claude Code sub-agents: the full brief at the top, then every step and tool
  call, with long tool outputs shortened.
- `0N-codex-*.md` — Codex CLI sessions (a different model family), same format.

The agents' final messages are often in Russian because they report to me; the files they wrote
are in English.
