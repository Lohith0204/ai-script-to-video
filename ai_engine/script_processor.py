def split_script(script:str):
    script=script.split(".")
    cleaned=[]
    for s in script:
        s=s.strip()
        if s:
            cleaned.append(s)
    return cleaned        