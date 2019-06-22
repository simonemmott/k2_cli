# k2 Command Line Interface

The K2 command line interface provides command line interaction with a K2 IDE service

## Getting Started

The K2 CLI can be installed using `pip install k2_cli`

With `k2_cli` installed the K2 command line can be executed as `k2 ...`

For help with the K2 CLI execute `k2 --help`

For information about the installed K2 CLI execute `k2 about`

## Installing a K2 Application

K2 applications are installed from an instance of the K2 IDE service.

The default K2 IDE service is expected to be at `http://localhost:8000`

The default installation location is `./app` i.e. the K2 application will be installed in a directory `app` as a child of the current directory

To install a K2 application execute `k2 install <app_id>` where `<app_id>` is the application `id` or `name`

The URL of the K2 IDE service can be specified on the command line with the `--k2_ide_url` option.

`k2 install <app_id> --k2_ide_url <IDE URL>`

The installation destination can be specified on the command line with the `--dest` option.

`k2 install <app_id> --dest <install dest>`

For example the command `k2 install myApp --k2_ide_url http://myserver.com --dest ~/apps` will install the application named `myApp` from the K2 IDE service running at `http://myserver.com` into the directory `apps` under the current users home directory

## Configuring the K2 CLI

The K2 CLI reads it's configuration details from a configuration file. By default this file is named `k2_cli.ini`

This default can be overridden by setting the environment variable `K2_CLI_CFG`
This environment variable can be a relative or absolute path.

The K2 CLI reads it's logging information from a logging configuration file. By default this file is named `logging.yaml`

This default can be overridden by setting the environment variable `LOG_CFG`
This environment variable can be a relative or absolute path.

### Configuration File Search Order

The K2 CLI searches for an instance of it's configuration files from the following locations.

The table below lists in order the search path for K2 CLI configuration files

| Search Order |
|--------------|
| The directory in which the `k2` command is executed |
| The locations identified by the environment variable `K2_SEARCH_PATH`. This environment variable is a list of `:` separated directories to search for configuration files |
| The directory in which python executable is installed |
| The parent directory in which the python executable is installed. This means that if a virtual environment is being used the root of the virtual environment will be searched for configuration files |
| The users home directory or the directory identfied by the `HOME` environment variable |

If the K2 CLI cannot find the configuration files then default configuration parameters are used.

### Logging Configuration

The K2 CLI logger can be configured by editing the logging configuration file `logging.yaml`.

The logging configuration file is a `YAML` or `JSON` formatted file containing logging configuration which is read and passed to the `logging.config.dictConfig(...)` method. Please see the [python logging documentation](https://docs.python.org/3/howto/logging-cookbook.html) for more details on the structure of the logging configuyration data.

### Configuration Parameters

The `k2_cli.ini` file provides values for the following configuration details

| Key       | Default | Description |
|-----------|---------|-------------|
| [DEFAULT] |
| logging_config        | logging.yaml          | The name of the logging configuration file |
| logging_config_format | YAML                  | The format of the logging configuration file. valid values are `YAML` or `JSON` |
| k2_ide_url            | http://localhost:8000 | The base URL of the source K2 IDE service |
| install_dir           | ./apps                | The directory into which the downloaded application will be installed |

