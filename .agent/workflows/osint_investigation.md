# Workflow: OSINT Investigation and Mentorship Cycle

This workflow governs the execution of all intelligence gathering operations, ensuring OPSEC compliance and structured learning.

## Step 1: Scope Definition & Tool Recommendation
* **Action:** Define the intelligence target (CTI infrastructure or HUMINT profile).
* **Requirement:** Recommend a specific tool stack for the task. Briefly explain the mechanism of the chosen tools and provide installation commands (`zypper`, `pip`, or git clone) if not present.

## Step 2: OPSEC Evaluation
* **Action:** Classify the upcoming operation (Passive vs Active).
* **Requirement:** If the operation is active, output a bolded risk warning detailing the specific footprints that will be left on the target infrastructure. 

## Step 3: Atomic Execution & Intercept
* **Action:** Provide the exact CLI command or script to execute the recon step.
* **Requirement:** Halt all output immediately. Wait for the user to provide the terminal output or parsed data logs.

## Step 4: Intelligence Collation (Documentation-as-Code)
* **Action:** Analyze the raw data provided by the user.
* **Requirement:** Format the extracted intelligence into a structured Markdown table or report. Conclude with a recommendation for the next logical step in the intelligence cycle.
