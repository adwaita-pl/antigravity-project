# Workflow: Infrastructure and Deployment Operations

This workflow must be strictly adhered to during any diagnostic, deployment, or configuration session within jureknet and Antigravity environments.

## Step 1: State Mapping (Initialization)
* **Action:** Begin every new session or troubleshooting sequence by generating a structural map or table detailing the current state of the infrastructure in the relevant scope (e.g., running Podman containers, network interfaces, Antigravity SDK versions).
* **Requirement:** Do not proceed to execution until the baseline is established.

## Step 2: Atomic Execution (One Step at a Time)
* **Action:** Present only one logical operational phase at a time (e.g., Quadlet syntax editing, SELinux policy adjustment, Antigravity service deployment).
* **Requirement:** Provide the exact command or configuration block required for this specific phase.

## Step 3: Hard Checkpoint
* **Action:** Halt all output.
* **Requirement:** Wait unconditionally for user confirmation, output logs, or supplementary questions before initiating the next logical step.

## Step 4: Documentation Update (Post-Mortem)
* **Action:** Upon successful resolution or deployment, formulate a brief technical summary.
* **Requirement:** Update internal event maps by logging errors, failure points, and the applied solutions. Conclude with a direct URL reference to the relevant official documentation used during the process.