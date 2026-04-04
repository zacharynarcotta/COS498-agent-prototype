# AI Capabilities Agent — Design Spec

## Purpose

An AI agent that will assist users in forming better mental models of what AI agent systems are actually capable of, what is hype versus reality, how trained person + AI can do more than an AI system, teaching and showing that AI “capabilities” are always socially situated and often involve and require users than one might think or be hyped about.

## Architecture

### Skills (5 total, in `.claude/skills/`)

| Skill | Trigger | Approach | Tone |
|-------|---------|----------|------|
| `session-start` | Every conversation start | Reads persona context, classifies user intent, routes to appropriate skill | Warm, welcoming |
| `mental_model_probe` | Surfaces the user's current model of AI | Socratic questioning: what is AI? what has changed about your understanding of AI? what do you already know? | Socratic guide |
| `reality_check` | User mentions AI's capabilities, "AI does X better/faster/more accurately than humans" | Decomposes AI hype claims into sociotechnical reality | Structured mentor |
| `self_disclosure` | Makes the agent's own limitations visible to the user | Offers genuine, digestible information: ethical limitations, environmental impact | Warm, therapeutic |
| `comparison_engine` | Reframes "human-vs-AI" comparisons into useful analyses | Compares what the user thinks and feels with broader, more realistic social applications. Does not try to persuade or change user opinion | Warm coach |

### Workflow

```
User opens session
       |
       v
  session-start (classifies intent)
       |
       +---> "AI does X better than
       |      humans" ---> mental_model_probe
       |                           |
       |                  upset/charged/emotional? ---> reality_check
       |
       +---> "AI will replace humans at X" ---> comparison_engine 
       |
       +---> general check-in ---> self_disclosure
       |
       v
  Any path can close with self_disclosure
```

**Rules:**
- `session-start` always fires first
- Skills can chain (want-examination -> reframe is common)
- `self_disclosure` is a natural session closer
- Agent can stay in one skill for a full session
- Tone adapts: warm by default, Socratic during want-examination, structured during flourishing-prompt

### Personas (4, in `data/personas/`)

1. **Kai, 28, UX Designer** — Early AI adopter, consults AI agents for feedback, coding, emails, etc.
2. **Bill, 45, Sales Manager** — Stubborn in older technology, "paper > digital", dislikes AI
3. **Sara, 18, College Freshman** — Uses AI for many assignments, particularly writing
4. **Beau, 22, College Senior** — Politically active, upset with AI corporations

### Interaction Examples (in `data/interactions/`)

**Beneficial (3):** Agent successfully helps user reflect, reframe, or find non-purchase alternatives
**Unhelpful (3):** Agent is preachy, dismissive, gives unsolicited lectures, or shames the user

## File Structure

```
.claude/skills/
  session-start.md
  mental_model_probe.md
  reality_check.md
  self_disclosure.md
  coparison_engine.md
data/personas/
  kai.json
  bill.json
  sara.json
  beau.json
data/interactions/
  beneficial-01-kai.md
  beneficial-02-bill.md
  beneficial-03-sara.md
  beneficial-04-beau.md
  unhelpful-01-preachy-lecture.md
  unhelpful-02-dismissive-shame.md
  unhelpful-03-unsolicited-advice.md
  unhelpful-04-frustrated-attacking.md
```
