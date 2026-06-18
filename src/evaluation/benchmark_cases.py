BENCHMARK_CASES = [
    {
        "case_id": "client_email_001",
        "input_text": "can u send me the report asap client is asking",
        "tone": "Formal",
        "purpose": "Request Message",
        "use_case": "Client Email",
        "expected_terms": ["report", "client"],
        "contains_sensitive_data": False,
        "mask_sensitive_data": True
    },
    {
        "case_id": "incident_001",
        "input_text": "server is down users cant login team is checking",
        "tone": "Formal",
        "purpose": "Email",
        "use_case": "Incident Communication",
        "expected_terms": ["server", "login", "team"],
        "contains_sensitive_data": False,
        "mask_sensitive_data": True
    },
    {
        "case_id": "project_status_001",
        "input_text": "completed frontend api privacy guard next working on analytics dashboard",
        "tone": "Professional",
        "purpose": "General Text",
        "use_case": "Project Status Update",
        "expected_terms": ["frontend", "api", "privacy", "analytics"],
        "contains_sensitive_data": False,
        "mask_sensitive_data": True
    },
    {
        "case_id": "meeting_summary_001",
        "input_text": "we discussed api work frontend work and next feedback analytics deployment docs",
        "tone": "Professional",
        "purpose": "General Text",
        "use_case": "Meeting Summary",
        "expected_terms": ["api", "frontend", "feedback", "analytics"],
        "contains_sensitive_data": False,
        "mask_sensitive_data": True
    },
    {
        "case_id": "executive_update_001",
        "input_text": "project has tone purpose templates privacy guard feedback and analytics ready",
        "tone": "Concise",
        "purpose": "General Text",
        "use_case": "Executive Update",
        "expected_terms": ["privacy", "feedback", "analytics"],
        "contains_sensitive_data": False,
        "mask_sensitive_data": True
    },
    {
        "case_id": "privacy_guard_001",
        "input_text": "hello my email is manas@gmail.com and phone number is 9876543210 please make this professional",
        "tone": "Professional",
        "purpose": "General Text",
        "use_case": "General Refinement",
        "expected_terms": ["email", "phone"],
        "contains_sensitive_data": True,
        "mask_sensitive_data": True
    }
]