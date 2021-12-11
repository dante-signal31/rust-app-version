""" Test get_version launcher. """
import os.path
from test_common.fs.temp import temp_dir
import test_common.fs.ops as fs_ops
import test_common.system.output as system_output

import rust_app_version.get_version as get_version

CARGO_TOML_PATH = "rust_app_version/tests/resources/Cargo.toml"
APP_VERSION = "0.9.2+post7"


def test_get_version(temp_dir):
    # Setup test.
    destination_folder = os.path.join(temp_dir, "tests/resources/")
    os.makedirs(destination_folder, exist_ok=True)
    fs_ops.copy_file(CARGO_TOML_PATH, destination_folder)
    args = f"-f {destination_folder}".split()
    # Run test.
    with system_output.OutputLogger.get_logger() as logger:
        get_version.main(args)
        assert logger.output[0] == APP_VERSION
