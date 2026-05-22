# Workflow: Antigravity Engineering and SDK Lifecycle

This workflow governs all operational phases including initialization, execution, debugging, and asset documentation within the Antigravity 2.0 Python environment.

## Step 1: Baseline Environment Mapping
* **Action:** Begin every new session or diagnostic routine by constructing a structured matrix mapping the current infrastructure state (e.g., active Antigravity CLI/SDK versions, local Python virtual environment parameters, and active VS Code workspace settings).
* **Requirement:** Halt further automation until this state map is outputted and validated.

## Step 2: Atomic Execution Phase
* **Action:** Present exactly one logical phase of the requested operation at a time (e.g., project initialization, virtual environment mapping, CLI deployment, dependency resolution).
* **Requirement:** Isolate the precise commands or file changes needed for this atomic step.

## Step 3: Hard Checkpoint
* **Action:** Freeze all output generation immediately.
* **Requirement:** Wait unconditionally for explicit user confirmation, raw terminal outputs, VS Code logs, or configuration file dumps before initiating the next sequential step.

## Step 4: Documentation Compilation (Post-Mortem)
* **Action:** Upon successful completion of the deployment or troubleshooting phase, compile a post-mortem or technical blueprint in Markdown.
* **Requirement:** Deliver ready-to-archive configurations, installation scripts, and link directly to the authoritative documentation utilized.
