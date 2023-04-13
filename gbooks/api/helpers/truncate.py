def prepare_list(data) -> str:
    if len(data) == 0:
        return ""
    elif len(data) == 1:
        return data[0][:14]
    else:
        return data[0][:12] + f"..+{len(data) - 1}"
