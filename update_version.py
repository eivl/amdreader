from tomlkit import dumps, parse, table


def update_init(major=False, minor=False, patch=False):
    """Update the version in __init__.py"""
    if all([not major, not minor, not patch]):
        print("Please specify the version to update")
        return
    file_name = r"amd\__init__.py"
    with open(file_name) as f:
        raw_data = f.read()
    data = raw_data.split("__version__ = ")
    file_version = data[1].splitlines()[0].strip().strip('"')
    version = update_version(file_version, major, minor, patch)

    with open(file_name, "w") as f:
        f.write(raw_data.replace(file_version, ".".join(version)))

    return True


def update_poetry_version(major=False, minor=False, patch=False):
    """Update the version in pyproject.toml"""
    if all([not major, not minor, not patch]):
        print("Please specify the version to update")
        return

    with open("pyproject.toml", "r") as f:
        data = f.read()

    toml = parse(data)
    version = toml["tool"]["poetry"]["version"]
    version = update_version(version, major, minor, patch)
    toml["tool"]["poetry"]["version"] = ".".join(version)

    with open("pyproject.toml", "w") as f:
        f.write(dumps(toml))
        return True


def update_version(version, major=False, minor=False, patch=False):
    version = version.split(".")
    if major:
        version[0] = str(int(version[0]) + 1)
        version[1] = "0"
        version[2] = "0"
    elif minor:
        version[1] = str(int(version[1]) + 1)
        version[2] = "0"
    elif patch:
        version[2] = str(int(version[2]) + 1)
    return version


if __name__ == "__main__":
    ...
