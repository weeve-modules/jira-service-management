# Module Name

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Module Name                           |
| Version        | v0.0.0                                |
| Dockerhub Link | [dockerhub-repo-name](https://hub.docker.com/r/dockerhub-repo-name) |
| authors        | Author 1, Author 2                    |

- [Module Name](#module-name)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This is module description. This explains in detail what module does.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Environment Var 1    | ENVIRONMENT_VAR_1         | string   | Description what this environment represents.            |
| Environment Var 2    | ENVIRONMENT_VAR_2         | integer  | Description what this environment represents.            |
| Environment Var 3    | ENVIRONMENT_VAR_3         | boolean  | Description what this environment represents.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle

dependency-4
dependency-5
dependency-6
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

* array of JSON body objects, example:

```json
[
    {
        "label-1": 12,
        "label-2": "speed"
    },
    {
        "label-1": 15,
        "label-2": "volume"
    }
]
```

## Output

Output of this module is:

Input data saved to a database X table Y / showed to the screen Z / etc...
