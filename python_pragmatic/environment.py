import os


def load_env_from_file(env_file):
    with open(env_file) as fh:
        variables = dict(
            (line.split('=', 1)[0], line.split('=', 1)[1].rstrip("\n"))
            for line in fh.readlines() if not line.startswith('#')
        )

        for key, value in variables.items():
            os.environ[key] = value
