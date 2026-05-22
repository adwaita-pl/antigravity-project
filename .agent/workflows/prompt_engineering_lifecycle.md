# Workflow: Prompt Engineering Lifecycle

This workflow governs the execution of requirements gathering, profile mapping, validation, and deployment of agentic system prompts.

## Step 1: Requirements Gathering & Profile Mapping
* **Action:** Initiate the session by parsing user requirements and generating a structured profile map table containing:
  * **Role**
  * **Technical Domain / Environment**
  * **Critical Knowledge Sources**
  * **Specific Constraints**

## Step 2: Gap Analysis & Parameter Verification
* **Action:** Review the generated profile map against the target environment.
* **Requirement:** If any critical parameter is missing or ambiguous, halt execution immediately. List the missing variables and prompt the user for input. Do not guess default values.

## Step 3: Hard Checkpoint (Profile Authorization)
* **Action:** Suspend all further automated prompt generation.
* **Requirement:** Wait unconditionally for the user to explicitly approve the profile map table before proceeding to compilation.

## Step 4: Prompt Architecture Compilation
* **Action:** Apply the mandatory Core Prompt Blueprint defined in the system rules to generate the final system prompt.
* **Requirement:** Embed the prompt entirely within clear, copiable markdown code blocks.

## Step 5: Post-Deployment Review
* **Action:** Log the finalized asset into the local agent directory structure (`/.agent/rules/` or `/.agent/workflows/`).
* **Requirement:** Provide a brief post-mortem summary of the prompt's structural changes and references to the engineering standards applied.
