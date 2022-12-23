# Jira Service Management

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Jira Service Management                   |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/jira-service-management](https://hub.docker.com/r/weevenetwork/jira-service-management) |
| Authors        | Jakub Grzelak                    |

- [Jira Service Management](#jira-service-management)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Generate and send Service Requests to your Jira Service Management. At the moment, the module enables configuring Request ticket's Summary and Description section. Hence, selected Requests types should not "require" any other fields than Summary and Description. To compose Summary and Description fields, we recommend our [Message Composer module](https://github.com/weeve-modules/message-composer).

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Atlassian Domain    | ATLASSIAN_DOMAIN         | string   | Your Atlassian domain of Jira Service Management.            |
| Atlassian Email    | ATLASSIAN_EMAIL         | string   | Atlassian account email of the Request Reporter.            |
| Atlassian API Token    | ATLASSIAN_API_TOKEN         | string   | Atlassian account API token of the Request Reporter. |
| Service Desk ID    | SERVICE_DESK_ID         | string   | Service desk ID to which the Request is send. |
| Request Type ID    | REQUEST_TYPE_ID         | string   | Request type ID of the Request. |
| Summary Label    | SUMMARY_LABEL         | string   | Label in incoming data that holds the Summary text of the Jira Service Request ticket. |
| Description Label    | DESCRIPTION_LABEL         | string   | Label in incoming data that holds the Description text of the Jira Service Request ticket. |


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
requests
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "summary-label": "Device RaspPi-12a in London is broken.",
    "description-label": "Device got broken by overheating. It recorded a temperature of 100 Celsius. It requires immediate fix by our onside team."
}
```


## Output

Output of this module is:

Service Request ticket of selected Request Type in Jira Service Management with summary "Device RaspPi-12a in London is broken." and description "Device got broken by overheating. It recorded a temperature of 100 Celsius. It requires immediate fix by our onside team.". It is reported by the person whose email and token was provided in module's configuration.
