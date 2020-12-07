def what_to_do(instructions):
    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        instructions = instructions.replace("Simon says", "").strip()
        return "I " + instructions
    return "I won't do it!"
