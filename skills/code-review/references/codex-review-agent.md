# Codex Review Parameters

Use `.codex/agents/enterprise-review.toml` for the repository’s durable deep-review defaults.

```toml
model = "gpt-5.6"
model_reasoning_effort = "xhigh"
```

`gpt-5.6` is the current Codex choice for demanding, multi-step review work. `xhigh` requests the deepest supported configuration setting; availability depends on the active model and account.

## Tune these settings

| Need | Tune here | Recommended setting |
|---|---|---|
| Deep primary review | `.codex/agents/enterprise-review.toml` | `model = "gpt-5.6"` and `model_reasoning_effort = "xhigh"` |
| Faster supporting scans | Spawn configuration or a separate agent | `gpt-5.6-terra` with `high` or `medium` reasoning |
| All local Codex work | `~/.codex/config.toml` | Set `model` and `model_reasoning_effort` only if you want a personal default |
| One desktop review | Model and reasoning control beneath the composer | Choose the strongest available model and highest desired intelligence level |
| Parallel review | Desktop **Ultra** mode or an explicit multi-agent request | Use separate agents for security, tests, data, and maintainability |

The skill itself cannot force the app to use a particular model. The custom-agent file supplies a durable review default when that agent is selected. Desktop **Ultra** and **Max** are session controls, not fields in the agent file.

## External double-check

The second-model stage is intentionally unconfigured. Connect an approved provider first, then approve the code and context sent to it. The review skill creates the review packet and reconciles the returned findings; it must not claim that Claude or another provider ran unless a real approved connection is available.
