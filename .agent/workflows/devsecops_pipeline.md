# Workflow: DevSecOps Architecture Pipeline

**Trigger:** When the user asks to "Design and audit", "Combined mode", or uses the tag #DevSecOps.

**Execution Steps (STRICT SEQUENCE):**

Process the user's prompt in two distinct, separate phases. DO NOT MIX ROLES.

### PHASE 1: System Architecture Design
1. Load the context from `system_architect.md` and procedures from `infrastructure_operations.md`.
2. Act EXCLUSIVELY as the System Architect.
3. Prepare the full design, topology, architecture, or deployment scripts as requested by the user.
4. End Phase 1 with a clear separator: `--- [HANDOVER TO CYBERSEC AUDIT] ---`

### PHASE 2: Security Audit & Penetration Testing
1. Drop the Architect role. Load the context from `cybersec_mentor.md` and procedures from `pentest_operations.md`.
2. Act EXCLUSIVELY as the Cybersec Mentor.
3. Analyze the architecture design just generated (in Phase 1) for attack vectors, vulnerabilities, and misconfigurations. Be highly critical and actively look for flaws.
4. Apply a threat modeling framework (e.g., STRIDE).
5. Generate a report containing:
   - Identified architectural vulnerabilities.
   - Recommended remediations (specific configuration parameters, architectural changes).

**Outcome Format:** The final output must always contain these two explicit headers: `# 🏗️ ARCHITECTURE DESIGN (System Architect)` and `# 🛡️ CYBERSEC REPORT (Cybersec Mentor)`.
