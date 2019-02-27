# rdb-comp-tap-hubspot

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
- Pulls raw data from HubSpot's [REST API](http://developers.hubspot.com/docs/overview)
- Extracts the following resources from HubSpot
  - [Campaigns](http://developers.hubspot.com/docs/methods/email/get_campaign_data)
  - [Companies](http://developers.hubspot.com/docs/methods/companies/get_company)
  - [Contacts](https://developers.hubspot.com/docs/methods/contacts/get_contacts)
  - [Contact Lists](http://developers.hubspot.com/docs/methods/lists/get_lists)
  - [Deals](http://developers.hubspot.com/docs/methods/deals/get_deals_modified)
  - [Deal Pipelines](https://developers.hubspot.com/docs/methods/deal-pipelines/get-all-deal-pipelines)
  - [Email Events](http://developers.hubspot.com/docs/methods/email/get_events)
  - [Engagements](https://developers.hubspot.com/docs/methods/engagements/get-all-engagements)
  - [Forms](http://developers.hubspot.com/docs/methods/forms/v2/get_forms)
  - [Keywords](http://developers.hubspot.com/docs/methods/keywords/get_keywords)
  - [Owners](http://developers.hubspot.com/docs/methods/owners/get_owners)
  - [Subscription Changes](http://developers.hubspot.com/docs/methods/email/get_subscriptions_timeline)
  - [Workflows](http://developers.hubspot.com/docs/methods/workflows/v3/get_workflows)
- Outputs a schema that is relational database compatible for each resource
- Incrementally pulls data based on the input state

## Configuration

This tap requires a `config.json` which specifies details regarding [OAuth 2.0](https://developers.hubspot.com/docs/methods/oauth2/oauth2-overview) authentication, a cutoff date for syncing historical data, and an optional flag which controls collection of anonymous usage metrics. See [config.sample.json](config.sample.json) for an example. You may specify an API key instead of OAuth parameters for development purposes, as detailed below.
You can specify a maximum number of pages that are retrieved for each stream that is synchronized.

### Config.json

The fields available to be specified in the config file are specified here.

| Field | Type | Default | Details |
| ----- | ---- | ------- | ------- |
| `redirect_uri` |`["string"]` | `N/A` | | 
| `refresh_token` | `["string"]`|  `N/A` | Token that will be used to get a new access token.|
| `client_id` | `["string"]`|  `N/A` | |
| `client_secret` | `["string"]` |  `N/A` | |
| `start_date` | `["string"]`|  `N/A` | |
| `disable_collection` | `["string", "null"]` | `false` | Include `true` in your config to disable [Singer Usage Logging](#usage-logging). |

Example of config.json:
   ```json
  {
    "redirect_uri": "https://api.hubspot.com/",
    "client_id": 123456789000,
    "client_secret": "my_secret",
    "refresh_token": "my_token",
    "start_date": "2017-01-01T00:00:00Z",
    "disable_collection": false
  }
   ```
This format of config.json is reccomanded in a production environment, but for development purposes an API Key Authentication can be use instead of  OAuth 2.0. More information below.

## API Key Authentication (for development)

As an alternative to OAuth 2.0 authentication during development, you may specify an API key (`HAPIKEY`) to authenticate with the HubSpot API. This should be used only for low-volume development work, as the [HubSpot API Usage Guidelines](https://developers.hubspot.com/apps/api_guidelines) specify that integrations should use OAuth for authentication.

To use an API key, include a `hapikey` configuration variable in your `config.json` and set it to the value of your HubSpot API key. Any OAuth authentication parameters in your `config.json` **will be ignored** if this key is present!

To run `rdb-comp-tap-hubspot` with the configuration file, use this command:

```bash
› rdb-com-tap-hubspot -c my-config.json
```

---
This is an adapted version of tap-hubspot (https://github.com/singer-io/tap-hubspot). All copyrights belong to Stitch.
Copyright &copy; 2017 Stitch
