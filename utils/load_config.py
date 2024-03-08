import yaml


def config(config_file, file_type):
    """
    Read configuration data from a file.

    Parameters:
        config_file (str): The path to the configuration file.
        file_type (str): The type of the configuration file. Supported types are 'json' and 'yaml'.

    Returns:
        dict: A dictionary containing the configuration data read from the file.

    Raises:
        FileNotFoundError: If the specified configuration file does not exist.
        ValueError: If the file_type parameter is not 'json' or 'yaml'.
        json.JSONDecodeError: If there is an error parsing the JSON configuration file.
        yaml.YAMLError: If there is an error parsing the YAML configuration file.
    """

    try:
        # Read configuration from YAML file
        if file_type == "yaml":
            with open(config_file, "r") as yaml_file:
                return yaml.safe_load(yaml_file)
        else:
            raise ValueError(
                "Unsupported file type. Currently supported types are files are 'json' and 'yaml'."
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    except Exception as e:
        raise Exception(
            f"Error in reading configuration file '{config_file}': {e}"
        )
