def log_step(step_name: str, data=None):
    print(f"[Akaion Workflow] {step_name}")
    if data is not None:
        print(data)