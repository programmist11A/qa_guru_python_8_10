from pathlib import Path
import home_8_10


def path(file_name):
    return str(
        Path(home_8_10.__file__).parent.joinpath(f'picture/{file_name}').absolute()
    )
