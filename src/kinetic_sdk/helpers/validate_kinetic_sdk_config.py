# pylint: disable=missing-function-docstring,missing-module-docstring
from kinetic_sdk.generated import Commitment


def validate_kinetic_sdk_config(config):
    if "endpoint" not in config:
        raise Exception("validate_kinetic_sdk_config: no endpoint configured.")
    if not config["endpoint"].startswith("http"):
        raise Exception("validate_kinetic_sdk_config: the endpoint should start with http or https.")

    if "environment" not in config:
        raise Exception("validate_kinetic_sdk_config: no environment configured.")
    if "index" not in config:
        raise Exception("validate_kinetic_sdk_config: no index configured.")
    try:
        int(config["index"])
    except ValueError as exc:
        raise Exception("validate_kinetic_sdk_config: index should be an integer.") from exc

    if "commitment" not in config:
        config["commitment"] = Commitment("Confirmed")

    if config["endpoint"].endswith("/"):
        config["endpoint"] = config["endpoint"][:-1]

    return config
